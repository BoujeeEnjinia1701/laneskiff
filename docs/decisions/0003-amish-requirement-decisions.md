---
doc_id: LSK-DDR-003
title: LaneSkiff requirement decisions of 2026-10-03
project: LaneSkiff
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Amish's decisions 30A, 31C and 32A recorded and carried out in the model, calculations, drawings and build plan
---

# 0003: Requirement decisions of 2026-10-03

- **Date:** 2026-10-03
- **Status:** accepted. Decided by Amish on 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed."

## Context

The TRL 3 sizing (LSK-CAL-001 v0.1) left five open items in LSK-DEC-001: R1 carry mass (hull 100 kg), R2 payload ratio (4.5 at six persons), R3 draft (187 mm at six persons), R5 swamped margin (36 mm at the transom) and R10 fin drive (not designed). The state, options and recommendations were put to Amish in `docs/REVIEW.md`. He accepted every recommendation; in the portfolio's numbering they are 30A (items 1 to 3), 31C (item 4) and 32A (item 5).

## Options considered

The options for each item are in `docs/REVIEW.md` (TRL 3 section, "Decisions for Amish") and in LSK-CAL-001 v0.1, section 9. In short: for mass, a light timber specification, carrying with four people, or a shorter hull; for draft, a five-person rating with or without a wider bottom, or keeping six persons; for the swamped margin, stern quarter foam, an operating rule, or both; for the fin drive, leaving it out, a bracket for a bought drive, or an open drive as a separate project.

## Decision

*Table 1. Decisions and what was changed.*

| # | Decision | Changed in the design | Result (LSK-CAL-001 v0.2) |
| --- | --- | --- | --- |
| 30A | Light timber specification: okoume plywood (about 450 kg/m3), 4 mm sides, softwood framing (about 500 kg/m3), no glass inside the floor; a five-person rating (375 kg); the bottom 60 mm wider; each half carried with the shoulder slings | `half_bot` 500 to 530 mm and `t_side` 6 to 4 mm in `cad/src/model.py`; densities and inside glass in `docs/04-calcs/sizing.py`; plywood, framing, glass, epoxy and foam lines in `bom/bom.csv`; rating in LSK-REQ-001 | Hull 87.9 kg (was 100.2), halves 49.9 and 38.1 kg; deepest draft 148 mm at five persons (R3 met); beam 1,197 mm (R4 met, 3 mm margin); rated load 4.3 times hull mass (R2 not met) |
| 31C | 30 L of foam in the stern quarters, and the aft-crew rule (the aft crew member moves amidships when swamped) | Two 15 L foam modules (250 x 190 x 316 mm cores) in tarpaulin covers, either side of the step opening, on the side stringer and bench rail, strapped to the transom ring frame and the stringer (BOM line 29); the rule in the build plan and the requirements | Swamped transom freeboard 161 mm with the foam alone, 216 mm with the rule as well (was 36 mm); R5 met on paper |
| 32A | Leave the fin drive out of the first prototype; an open fixed forward-only fin drive stays a later portfolio idea | Nothing in the prototype; R10 restated | R10 not shown; R2 to R6 assessed without a drive |

## Consequences

- Nine constructability checks were added (82 of 82 pass): the quarter modules sit on the stringer and bench rail, their straps reach the ring frame and stringer, they leave 250 mm clear between them at the step opening, they clear the stowed pole, and the beam stays within 1,200 mm.
- The aft crew still stands at 0.4 m from the transom, forward of the quarter modules (which end 0.30 m from the transom).
- The R1 carry mass is still not met; Amish accepted this with the decision. The R2 payload ratio falls to 4.3 because the rating is now five persons; this is put to Amish as a new question in `docs/REVIEW.md` and LSK-DEC-001.
- Estimated cost rises by USD 39 to USD 1,961 (value-engineering target USD 1,500; USD 461 over).
- Okoume and softwood are weaker and softer than the gurjan and hardwood assumed before: the plywood bending strength, the screw holding of the skid and strake screws in softwood, and the nut plate bearing on the softwood joint frame are added to the items to confirm.
- The general arrangement goes to Rev P3; a making sketch for the quarter module (LSK-DWG-115) and a joint close-up (joint 9) are added; every making sketch, joint, step picture and the concept media are regenerated from the changed model.

## Safety

> **Safety:** The rating is five persons and is marked on the transom; six persons put the draft back to 177 mm. When the boat is swamped, the aft crew member moves amidships and everyone stays seated, low and centred. The stern quarter foam gives margin even when the rule is not followed. The proof loads and trial gates of LSK-BLD-001 are unchanged.
