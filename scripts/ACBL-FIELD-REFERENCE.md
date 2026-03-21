# ACBL Convention Card — PDF Form Field Reference

Source PDF: https://web2.acbl.org/documentLibrary/play/ConventionCard.pdf
Form has 433 fields. Field naming: `SECTION.c.NUMBER` = checkbox, `SECTION.t.NUMBER` = text field.

---

## Name

| Field | Meaning |
|-------|---------|
| `Name.t.1` | Partnership names |

---

## 1H1S — Major Openings (1♥ / 1♠)

### Checkboxes

| Field | Meaning |
|-------|---------|
| `c.1` | Min opening length: **4 cards**, 1st/2nd seat |
| `c.2` | Min opening length: **5 cards**, 1st/2nd seat |
| `c.3` | Min opening length: **4 cards**, 3rd/4th seat |
| `c.4` | Min opening length: **5 cards**, 3rd/4th seat |
| `c.5` | 1NT response: **Forcing** |
| `c.6` | 1NT response: **Semi-Forcing** |
| `c.7` | **Bypass ♠** — may bypass spades over 1♥ |
| `c.8` | Artificial raise: **2NT** (Jacoby 2NT) |
| `c.9` | Artificial raise: **3NT** |
| `c.10` | Artificial raise: **Splinter** |
| `c.12` | **Drury 2♣** |
| `c.13` | **Drury 2♦** |
| `c.14` | Drury: **In Competition** |
| `c.17` | Jump raise uncontested: **Weak** (preemptive) |
| `c.18` | Jump raise uncontested: **Mixed** |
| `c.19` | Jump raise uncontested: **Invitational** |
| `c.20` | Jump raise after overcall: **Weak** |
| `c.21` | Jump raise after overcall: **Mixed** |
| `c.22` | Jump raise after overcall: **Invitational** |

### Text Fields

| Field | Meaning |
|-------|---------|
| `t.11` | Free text: "Other" artificial raise description (e.g., Bergen details) |
| `t.15` | Drury variation description |
| `t.16` | Other jump raise agreements (uncontested) |
| `t.16b` | Other jump raise agreements (after overcall) |

---

## 1NT — Opening

### Text Fields

| Field | Meaning |
|-------|---------|
| `t.1` | HCP range low end |
| `t.2` | HCP range high end |
| `t.3` | Seat/vul modifier (low) |
| `t.5` | Seat/vul modifier |
| `t.11` | 2♦ "Other" text |
| `t.14` | 2♥ "Other" text |
| `t.17` | 2♠ "Other" text |
| `t.20` | 2NT "Other" text |
| `t.26` | Smolen/4♣ transfer detail |
| `t.28` | Second range low |
| `t.29` | Second range high |
| `t.32`–`t.37` | Interference response text fields |
| `t.38` | Double "Other" text |
| `t.40` | Lebensohl description |

### Checkboxes

| Field | Meaning |
|-------|---------|
| `c.4` | 5-card major systems on |
| `c.6` | 2♣ = **Stayman** |
| `c.7` | 2♣ = **Puppet Stayman** |
| `c.8` | 2♣ = **Other** |
| `c.9` | 2♦ = **Natural** |
| `c.10` | 2♦ = **Transfer** (to hearts — Jacoby) |
| `c.12` | 2♥ = **Natural** |
| `c.13` | 2♥ = **Transfer** (to spades — Jacoby) |
| `c.15` | 2♠ = **Natural** |
| `c.16` | 2♠ = **Transfer** (to clubs/NT) |
| `c.18` | 2NT = **Natural** |
| `c.19` | 2NT = **Transfer** |
| `c.21` | **Smolen** |
| `c.22` | 4♣ transfer (Texas to hearts) |
| `c.23` | 4♦ transfer (Texas to spades) |
| `c.24` | 4♥ quantitative/natural |
| `c.25` | After interference: double = **Negative** |
| `c.27` | **Lebensohl** |
| `c.30` | Second range: Same responses (Y) |
| `c.31` | Second range: Same responses (N) |
| `c.39` | **Lebensohl** (end of interference section) |

---

## 1C — One Club Opening

### Checkboxes (min opening length)

| Field | Meaning |
|-------|---------|
| `c.1` | Min 5 cards |
| `c.2` | Min 4 cards |
| `c.3` | Min 3 cards |
| `c.4` | NF 2-card |
| `c.5` | NF 1-card |
| `c.6` | NF 0-card (artificial) |
| `c.7` | Artificial Forcing |

### Checkboxes (raise structure, c.18–c.26)

| Field | Meaning |
|-------|---------|
| `c.18` | Single raise uncontested: **NF** (non-forcing) |
| `c.19` | Single raise uncontested: **Inv+** (invitational or better = inverted) |
| `c.20` | Single raise uncontested: **GF** |
| `c.21` | Jump raise uncontested: **Weak** |
| `c.22` | Jump raise uncontested: **Inv** |
| `c.23` | Jump raise uncontested: **GF** |
| `c.24` | Raise after overcall: **Weak** |
| `c.25` | Raise after overcall: **Inv** |
| `c.26` | Raise after overcall: **GF** |

---

## 1D — One Diamond Opening

### Checkboxes (min opening length)

| Field | Meaning |
|-------|---------|
| `c.1` | Min 5 cards |
| `c.2` | Min 4 cards |
| `c.3` | Min 3 cards |
| `c.4` | Unbalanced |

### Checkboxes (raise structure, c.17–c.24)

| Field | Meaning |
|-------|---------|
| `c.17` | Single raise uncontested: **NF** |
| `c.18` | Single raise uncontested: **Inv+** (inverted) |
| `c.19` | Single raise uncontested: **GF** |
| `c.20` | Jump raise uncontested: **Weak** |
| `c.21` | Jump raise uncontested: **Inv** |
| `c.22` | Jump raise uncontested: **GF** |
| `c.23` | Raise after overcall: **Weak** |
| `c.24` | Raise after overcall: **Inv** |

---

## 2C — Two Club Opening

| Field | Meaning |
|-------|---------|
| `t.1` | Strength description |
| `t.2` | Shape description |
| `t.3a` | Response text (paired with c.3b) |
| `t.6` | Additional response description |
| `t.12`, `t.13` | Other text fields |
| `c.3b` | 2♦ = waiting response (**GUESSED** — paired with t.3a) |
| `c.4`–`c.11` | Other response options (meanings not fully confirmed) |

---

## 2D / 2H / 2S — Two-Level Openings

### Text Fields (same structure for all three)

| Field | Meaning |
|-------|---------|
| `t.1` | HCP range low |
| `t.2` | HCP range high |
| `t.3` | Suit length or description (`2S` uses `t.3` for high range) |
| `t.9` | Response description (e.g., "2NT = forcing inquiry") |
| `t.10` | Other |

### Checkboxes

| Field | Meaning |
|-------|---------|
| `c.4` | **Weak** |
| `c.5` | **Intermediate** |
| `c.6` | **Strong** |
| `c.7` | Feature ask (2NT?) |
| `c.8` | Ogust or other response method |

---

## 2NT — Opening

| Field | Meaning |
|-------|---------|
| `t.1` | HCP range low |
| `t.2` | HCP range high |
| `c.3`–`c.10` | Response options (not fully mapped) |

---

## D — Doubles

### Checkboxes

| Field | Meaning |
|-------|---------|
| `c.1` | **Negative** doubles active |
| `c.3` | Negative: secondary = **Penalty** |
| `c.4` | **Responsive** doubles active |
| `c.6` | Responsive: **Maximal** |
| `c.7` | **Support** doubles active |
| `c.9` | Support: **Redouble** also applies |

### Text Fields

| Field | Meaning |
|-------|---------|
| `t.2` | Negative doubles "thru ___" |
| `t.5` | Responsive doubles "thru ___" |
| `t.8` | Support doubles "thru ___" |
| `t.10` | T/O style description |
| `t.11` | Additional double agreements |

---

## OC — Overcalls (responses/advances)

### Text Fields

| Field | Meaning |
|-------|---------|
| `t.1` | 1-level overcall HCP range low |
| `t.2` | 1-level overcall HCP range high |
| `t.4` | 2-level overcall HCP range low |
| `t.5` | 2-level overcall HCP range high |
| `t.10` | Jump overcall style description |
| `t.18` | Conventional overcall agreements |
| `t.20` | Other overcall agreements |

### Checkboxes

| Field | Meaning |
|-------|---------|
| `c.3` | Cuebid = support for partner |
| `c.6` | Jump raise after overcall: **Weak** |
| `c.7` | Jump raise after overcall: **Mixed** |
| `c.8` | Jump raise after overcall: **Inv** |
| `c.9` | New suit response: **Forcing** |
| `c.11` | New suit response: **NFConst** (non-forcing constructive) |
| `c.12` | New suit response: **NF** |
| `c.13` | New suit response: **Transfer** |
| `c.14` | Jump shift: **Weak** |
| `c.15` | Jump shift: **Inv** |
| `c.16` | Jump shift: **Forcing** |
| `c.17` | Jump shift: **Fit** |
| `c.19` | Rdbl after double of overcall = 10+ |

---

## OV — Overcall Style

### Text Fields

| Field | Meaning |
|-------|---------|
| `t.1` | Names (top of back of card) |
| `t.2` | 1-level overcall strength description |
| `t.3` | 2-level overcall strength description |
| `t.6` | Conventional overcall text |
| `t.10` | Free text — responses |
| `t.11` | Additional free text |

### Checkboxes

| Field | Meaning |
|-------|---------|
| `c.4` | Jump overcall: **Weak** |
| `c.5` | Jump overcall: **Intermediate** |
| `c.7` | 1-level often only 4 cards |
| `c.8` | Jump overcall: **Strong** |

---

## NTO — Notrump Overcalls

### Text Fields

| Field | Meaning |
|-------|---------|
| `t.1` | Direct 1NT range low |
| `t.2` | Direct 1NT range high |
| `t.4` | Balancing 1NT range low |
| `t.5` | Balancing 1NT range high |
| `t.8` | Conv text (unusual 2NT description) |
| `t.10` | Other NT overcall agreements |

### Checkboxes

| Field | Meaning |
|-------|---------|
| `c.3` | Direct 1NT: Systems On |
| `c.6` | Balancing 1NT: Systems On |
| `c.7` | Conv (conventional NT overcall) |
| `c.9` | Systems On (other context) |

---

## SL — Slam Conventions

### Checkboxes

| Field | Meaning |
|-------|---------|
| `c.1` | ♣ Gerber: over NT sequence |
| `c.2` | ♣ Gerber: non-NT sequence |
| `c.5` | 4NT = **Blackwood** |
| `c.6` | 4NT = **RKC 0314** |
| `c.7` | 4NT = **RKC 1430** |

### Text Fields

| Field | Meaning |
|-------|---------|
| `t.4` | Gerber "directly over NT" detail |
| `t.8` | Control bids description |
| `t.9` | Vs. interference (e.g., DOPI) |
| `t.10` | Other slam conventions |
| `t.11` | Additional free text |

---

## SI — Signals / Carding

### Checkboxes

| Field | Meaning |
|-------|---------|
| `c.2` | Standard **Attitude**, Declarer's lead |
| `c.3` | Standard **Attitude**, Partner's lead |
| `c.4` | Standard **Count**, Declarer's lead |
| `c.5` | Standard **Count**, Partner's lead |
| `c.6` | Upside-down **Attitude**, Declarer's lead |
| `c.7` | Upside-down **Attitude**, Partner's lead |
| `c.9` | Upside-down **Count**, Declarer's lead |
| `c.10` | Upside-down **Count**, Partner's lead |
| `c.11` | First discard: **Lavinthal** |
| `c.12` | First discard: **Odd/Even** |
| `c.13` | First discard: **Other** |

### Text Fields

| Field | Meaning |
|-------|---------|
| `t.1` | Smith Echo agreements |
| `t.8` | Trump signals |
| `t.14` | Other carding / first discard "Other" text |
| `t.15` | Additional carding free text |

---

## DC — Direct Cuebids

### Checkboxes (3 rows × 4 columns: Michaels / Natural / Other, over ♣♦ / ♥♠)

| Field | Meaning |
|-------|---------|
| `c.1` | **Michaels** over minor (natural) |
| `c.2` | **Michaels** over major (natural) |
| `c.3` | **Michaels** over minor (2nd column variant) |
| `c.4` | **Michaels** over major (2nd column variant) |
| `c.5` | **Natural** cuebid over minor |
| `c.6` | **Natural** cuebid over major |
| `c.7`–`c.8` | Natural, additional columns |
| `c.9`–`c.12` | **Other** cuebid meanings |

### Text Field

| Field | Meaning |
|-------|---------|
| `t.13` | Description of cuebid meanings |

---

## V1NT — Defense vs. Opponent's 1NT

15 text fields (`t.1`–`t.15`), no checkboxes. Used to describe the convention and each bid's meaning.

| Field | Likely meaning |
|-------|---------------|
| `t.1` | Convention name (e.g., "Landy") |
| `t.2` | 2♣ meaning |
| `t.3`–`t.15` | Other bids / descriptions |

---

## VP — Vs. Preempts

| Field | Meaning |
|-------|---------|
| `t.1`–`t.7` | Free text describing agreements |
| `c.3` | Takeout double (**GUESSED**) |
| `c.4` | Other option (**GUESSED**) |

---

## VTD — Vs. Takeout Double

| Field | Meaning |
|-------|---------|
| `c.1`, `c.2` | Redouble options |
| `c.4`–`c.9` | Response style checkboxes |
| `c.11`, `c.12` | Additional options |
| `c.15`, `c.16` | Jump response options |
| `t.3`, `t.10`, `t.13`, `t.14`, `t.17`–`t.19` | Free text fields |

---

## O — Other Conventions (NMF / 4th Suit area, bottom of front)

### Checkboxes

| Field | Meaning |
|-------|---------|
| `c.3` | **2-Way New Minor Forcing** |
| `c.4` | **XYZ** |
| `c.5` | 4th Suit Forcing: **1 Round** |
| `c.6` | 4th Suit Forcing: **GF** |

### Text Fields

| Field | Meaning |
|-------|---------|
| `t.1` | Convention name / description |
| `t.2` | NMF/XYZ descriptor |
| `t.8` | Other agreements (line 1) |
| `t.9` | Other agreements (line 2) |

---

## Notes

- Numbering gaps within sections are intentional (Adobe InDesign form design order).
- `O` prefix = **Other conventions** (NMF area), NOT Overcalls. Overcalls = `OC` and `OV`.
- `SL.c.6` = RKC 0314; `SL.c.7` = RKC 1430.
- `1C.c.19` = Inverted single raise (Inv+); `1D.c.18` = same for diamonds.
- DC section: `c.1`/`c.2` are Michaels over natural minor/major openings. `c.3`/`c.4` are the same for the second set of columns (quasi-natural / different opening types). The user corrected: `c.1`/`c.2` = off (artificial openings), `c.3`/`c.4` = on (natural openings).
