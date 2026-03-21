#!/usr/bin/env python3
"""
Fill the ACBL Convention Card PDF form with Betsy & Steve's system.

Downloads the official fillable PDF from ACBL's site, fills all text fields
and checkboxes, and saves to pdfs/ACBL-Convention-Card.pdf.

Field naming: SECTION.c.NUMBER = checkbox, SECTION.t.NUMBER = text field.
Lines marked GUESSED indicate checkboxes confirmed by positional research but
not visually verified — adjust if the output shows a wrong box checked.
"""

import sys
import urllib.request
import tempfile
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print("ERROR: pypdf not installed. Run: pip install pypdf", file=sys.stderr)
    sys.exit(1)

ACBL_PDF_URL = "https://web2.acbl.org/documentLibrary/play/ConventionCard.pdf"
REPO_ROOT = Path(__file__).parent.parent
OUTPUT_PATH = REPO_ROOT / "pdfs" / "ACBL-Convention-Card.pdf"

# ---------------------------------------------------------------------------
# Text fields
# ---------------------------------------------------------------------------
TEXT_FIELDS = {
    # Partnership name
    "Name.t.1":    "Betsy & Steve",

    # 1NT opening — range
    "1NT.t.1":     "15",
    "1NT.t.2":     "17",

    # Major openings — free-text descriptions of non-standard raises
    "1H1S.t.11":   "Bergen (See below)",
    "1H1S.t.15":   "2way Rev", # Drury
    "1H1S.t.16":   "",  # Other.  not needed
    "1H1S.t.23":   "Bergen - 4 card support and 2M=4-6  3C=10-12  3D=7-9",  



    # 2C strong opening
    "2C.t.1":      "22+",
    "2C.t.2":      "Any shape",
    "2C.t.6":      "",   # Steps text, not applicable

    # 2NT opening — range
    "2NT.t.1":     "20",
    "2NT.t.2":     "21",

    # Weak 2s — HCP range and 2NT response meaning
    "2D.t.1":      "5",   "2D.t.2":  "11",  "2D.t.9":  "2NT = forcing inquiry",
    "2H.t.1":      "5",   "2H.t.2":  "11",  "2H.t.9":  "2NT = forcing inquiry",
    "2S.t.1":      "5",   "2S.t.3":  "11",  "2S.t.9":  "2NT = forcing inquiry",

    # Doubles — "through" levels
    "D.t.2":       "3S",   # negative doubles through
    "D.t.8":       "2S",   # support doubles through

    # Overcalls (OC section)
    "OC.t.1":      "8",    # 1-level HCP low
    "OC.t.2":      "15",   # 1-level HCP high
    "OC.t.4":      "10",   # 2-level HCP low
    "OC.t.5":      "15",   # 2-level HCP high
    "OC.t.10":     "", # Conventional text box

    # NT overcalls (NTO)
    "NTO.t.1":     "15",   # direct 1NT low
    "NTO.t.2":     "18",   # direct 1NT high
    "NTO.t.4":     "12",   # balancing 1NT low
    "NTO.t.5":     "14",   # balancing 1NT high
    "NTO.t.10":    "",     # Other box - no need to fill

    # Slam
    "SL.t.8":      "",
    "SL.t.9":      "",

    # Signals / carding
    "SI.t.8":      "",  # Exceptions - none
    "SI.t.14":     "Suit preference secondary",
    "SI.t.15":     "",  # Second line of description, not needed

    # Direct cuebids — Michaels description
    "DC.t.13":     "", # No need for explanation in "Describe" field

    # Defense vs 1NT — Landy
    "V1NT.t.5":    "Landy",
    "V1NT.t.6":    "5/4+ majors",

    # Vs preempts
    "VP.t.1":      "", # 2NT overcall box, left empty
    "VP.t.2":      "4S", # Takeout thru 

    # Other conventions (O section = NMF / 4th-suit area at bottom of card)
    "O.t.1":       "",  # Jump shift response
    "O.t.2":       "",  # Vs very strong open
}

# ---------------------------------------------------------------------------
# Checkboxes
# Field-to-label mapping researched from ACBL PDF structure and reference
# manual. Lines marked GUESSED are positionally inferred — verify the output.
# ---------------------------------------------------------------------------
CHECKBOXES = {
    # 1H/1S — Major openings
    "1H1S.c.2":   True,   # 5-card majors, 1st/2nd seat
    "1H1S.c.4":   True,   # 5-card majors, 3rd/4th seat
    "1H1S.c.5":   False,   # 1NT response: Forcing
    "1H1S.c.8":   True,   # Artificial raise: 2NT (Jacoby 2NT)
    "1H1S.c.10":  True,   # Artificial raise: Splinter
    "1H1S.c.12":  True,   # Drury: 2C
    "1H1S.c.13":  True,   # Drury: 2D
    "1H1S.c.17":  True,   # Jump raise uncontested: Weak (Bergen 3M = 0-3 pts)
    "1H1S.c.20":  True,   # Jump raise after overcall: Weak

    # 1NT — responses
    "1NT.c.6":    True,   # 2C = Stayman
    "1NT.c.10":   True,   # 2D = Transfer to hearts (Jacoby)
    "1NT.c.13":   True,   # 2H = Transfer to spades (Jacoby)
    "1NT.c.22":   True,   # 4-level transfer: Texas (4D → hearts)
    "1NT.c.23":   True,   # 4-level transfer: Texas (4H → spades)

    # 1C — minor opening
    "1C.c.3":     True,   # Min opening length: 3 cards
    "1C.c.19":    True,   # Single raise: Inv+ (Inverted minor, 11+)
    "1C.c.21":    True,   # Jump raise: Weak (preemptive)

    # 1D — minor opening
    "1D.c.3":     True,   # Min opening length: 3 cards
    "1D.c.17":    True,   # Single raise: Inv+ (Inverted minor, 11+)
    "1D.c.19":    True,   # Jump raise: Weak (preemptive)

    # 2C — strong artificial
    "2C.c.3b":    False,  # Negative
    "2C.c.3c":    True,   # 2D = waiting response

    # 2D / 2H / 2S — weak twos
    "2D.c.4":     True,   # Weak two
    "2H.c.4":     True,   # Weak two
    "2S.c.4":     True,   # Weak two

    # Doubles
    "D.c.1":      True,   # Negative doubles active
    "D.c.7":      True,   # Support doubles active
    "D.c.9":      True,   # Support redouble active

    # Overcalls — response style
    "OC.c.6":     True,   # Jump raise after overcall: Weak
    "OC.c.11":    True,   # New suit response: Non-Forcing Constructive

    # Jump overcalls
    "OV.c.5":     True,   # Jump overcall style: Intermediate

    # NT overcalls
    "NTO.c.3":    True,   # Direct 1NT: Systems On
    "NTO.c.6":    True,   # Balancing 1NT: Systems On
    "NTO.c.9":    True,   # Unusual 2NT

    # Slam
    "SL.c.7":     True,   # 4NT = RKC 1430

    # Signals — Standard Attitude primary
    "SI.c.2":     True,   # Standard Attitude on Declarer's lead
    "SI.c.3":     True,   # Standard Attitude on Partner's lead

    # Direct cuebids — Michaels
    "DC.c.1":     False,  # Michaels over artificial 1c/1d, not on
    "DC.c.2":     False,  # Michaels over quasi-natural, not on
    "DC.c.3":     True,   # Michaels over minor opening - natural
    "DC.c.4":     True,   # Michaels over major opening - natural

    # Vs preempts
    "VP.c.3":     False,   # Penalty

    # Other conventions — NMF
    "O.c.3":      True,   # 2-Way New Minor Forcing
}


def get_on_value(reader: PdfReader, field_name: str) -> str:
    """Return the PDF 'on' export value for a checkbox (usually '/Yes')."""
    fields = reader.get_fields()
    if field_name not in fields:
        return "/Yes"
    field = fields[field_name]
    ap = field.get("/AP")
    if ap and "/N" in ap:
        on_states = [k for k in ap["/N"].keys() if k != "/Off"]
        if on_states:
            return on_states[0]
    return "/Yes"


def main() -> None:
    print("Downloading ACBL Convention Card template...")
    tmp = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
    try:
        urllib.request.urlretrieve(ACBL_PDF_URL, tmp.name)
        template_path = Path(tmp.name)
    finally:
        tmp.close()

    print("Filling form fields...")
    try:
        reader = PdfReader(template_path)
        writer = PdfWriter()
        writer.append(reader)

        # Merge text fields and resolved checkbox values
        fields: dict[str, str] = dict(TEXT_FIELDS)
        for name, checked in CHECKBOXES.items():
            fields[name] = get_on_value(reader, name) if checked else "/Off"

        writer.update_page_form_field_values(
            writer.pages[0],
            fields,
            auto_regenerate=False,
        )

        OUTPUT_PATH.parent.mkdir(exist_ok=True)
        with open(OUTPUT_PATH, "wb") as f:
            writer.write(f)

        print(f"  → pdfs/ACBL-Convention-Card.pdf")
    finally:
        template_path.unlink(missing_ok=True)

    print("Done.")


if __name__ == "__main__":
    main()
