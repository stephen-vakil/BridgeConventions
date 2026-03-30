#!/usr/bin/env python3
"""Generate PDFs from Bridge Convention markdown files.

Steps for each file:
  1. Replace mermaid code blocks with rendered PNG images (via mmdc)
  2. Convert processed markdown to PDF via pandoc + weasyprint

Run from the repo root or via GitHub Actions.
"""

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PDF_DIR = REPO_ROOT / "pdfs"
IMG_DIR = REPO_ROOT / "tmp_images"
CSS_FILE = REPO_ROOT / "print.css"

# Order of files in the combined PDF
COMBINED_ORDER = [
    "BetsyAndSteve.md",
    "NTResponses.md",
    "MajorRaises.md",
    "InvertedMinors.md",
    "AfterOpponentsInterfereWithNT.md",
    "SupportDoubles.md",
    "RKC1430.md",
    "NewMinorForcing.md",
    "WONT.md",
    "MichaelsCuebid.md",
    "Unusual2NT.md",
]

# Files to skip (not convention docs)
SKIP_FILES = {"Readme.md"}

PAGE_BREAK = '\n\n<div style="page-break-after: always"></div>\n\n'


def render_mermaid(content: str, base_name: str) -> str:
    """Replace ```mermaid blocks with rendered PNG image references."""
    count = [0]

    def replace(match):
        count[0] += 1
        src = match.group(1).strip()
        img_path = IMG_DIR / f"{base_name}_{count[0]}.png"

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".mmd", delete=False, encoding="utf-8"
        ) as f:
            f.write(src)
            tmp = f.name

        try:
            result = subprocess.run(
                [
                    "mmdc",
                    "-i", tmp,
                    "-o", str(img_path),
                    "-b", "white",
                    "--width", "2400",
                    "--scale", "3",
                    "--puppeteerConfigFile", str(REPO_ROOT / "puppeteer-config.json"),
                ],
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                print(
                    f"  Warning: mmdc failed on {base_name} diagram {count[0]}:\n"
                    f"  {result.stderr.strip()}",
                    file=sys.stderr,
                )
                return f"\n*[Diagram {count[0]}: rendering failed]*\n"
        finally:
            os.unlink(tmp)

        return f"\n![Diagram {count[0]}]({img_path})\n"

    return re.sub(
        r"```mermaid\s*\n(.*?)\n```", replace, content, flags=re.DOTALL
    )


def to_pdf(content: str, output: Path, title: str) -> None:
    """Convert markdown content to PDF via pandoc + weasyprint."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, dir=REPO_ROOT, encoding="utf-8"
    ) as f:
        f.write(content)
        tmp = Path(f.name)

    try:
        result = subprocess.run(
            [
                "pandoc", str(tmp),
                "-o", str(output),
                "--pdf-engine=weasyprint",
                "--css", str(CSS_FILE),
                "--standalone",
                "--metadata", f"title={title}",
                "--from", "markdown-yaml_metadata_block+raw_html",
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"  Error generating {output.name}:\n  {result.stderr.strip()}", file=sys.stderr)
            sys.exit(1)
    finally:
        tmp.unlink(missing_ok=True)


def main():
    PDF_DIR.mkdir(exist_ok=True)
    IMG_DIR.mkdir(exist_ok=True)

    # --- Individual PDFs ---
    all_md = sorted(f for f in REPO_ROOT.glob("*.md") if f.name not in SKIP_FILES)
    for md_file in all_md:
        print(f"Processing {md_file.name}...")
        raw = md_file.read_text(encoding="utf-8")
        processed = render_mermaid(raw, md_file.stem)
        title = md_file.stem.replace("-", " ").replace("_", " ")
        out = PDF_DIR / f"{md_file.stem}.pdf"
        to_pdf(processed, out, title)
        print(f"  → pdfs/{md_file.stem}.pdf")

    # --- Combined PDF ---
    print("Generating combined PDF...")
    parts = []
    for name in COMBINED_ORDER:
        path = REPO_ROOT / name
        if path.exists():
            raw = path.read_text(encoding="utf-8")
            parts.append(render_mermaid(raw, f"combined_{path.stem}"))
        else:
            print(f"  Skipping {name} (file not found)")

    combined = PAGE_BREAK.join(parts)
    to_pdf(combined, PDF_DIR / "Complete-Conventions.pdf", "Betsy & Steve — Complete Bridge Conventions")
    print("  → pdfs/Complete-Conventions.pdf")

    # Clean up temp images
    for f in IMG_DIR.glob("*.png"):
        f.unlink()
    IMG_DIR.rmdir()

    print("Done.")


if __name__ == "__main__":
    main()
