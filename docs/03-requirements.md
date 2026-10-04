---
doc_id: LSK-REQ-001
title: LaneSkiff requirements
project: LaneSkiff
doc_type: Requirements
version: "0.3"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Rated load and test conditions stated; TRL 3 status from LSK-CAL-001; targets unchanged
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: Round 2 requirement decisions by Amish (LSK-DDR-003); rated load five persons (375 kg); light timber specification; status from LSK-CAL-001 v0.2; targets unchanged
---

# LaneSkiff requirements

Requirements for the first prototype, built on the plywood and epoxy path to the light timber specification. Targets are those set at TRL 1 and are unchanged. Status is the paper result at TRL 3 from LSK-CAL-001 v0.2, with Amish's round 2 decisions of 2026-10-03 (LSK-DDR-003); every requirement is verified by test at TRL 4. Open decisions are set out in `docs/REVIEW.md` and listed in LSK-DEC-001.

*Table 1. Requirements.*

| ID | Requirement | Target | Verification (TRL 4) | TRL 3 status |
| --- | --- | --- | --- | --- |
| R1 | Carry mass | Complete hull 50 kg or less; each half 25 kg or less (plywood and epoxy path, target) | Weigh the prototype halves | Not met on paper: hull 88 kg, halves 50 and 38 kg; carried by two per half with the shoulder slings, 25 and 19 kg each (LSK-DDR-003) |
| R2 | Payload | At least 6 times hull mass, about 300 kg or four adults plus crew (target) | Static load test with water ballast in calm water | Not met on paper: 375 kg five-person rated load is 4.26 times hull mass (4.5 before the five-person rating); no rating meets R2 and R3 together (new decision for Amish) |
| R3 | Draft at rated load | 15 cm or less | Measured at the transom and bow during the load test | Met on paper: 148 mm at the transom, 138 mm at the forward end of the waterline, five persons (LSK-DDR-003); 2 mm margin |
| R4 | Width for lanes | Beam 1.2 m or less overall | Tape measure; trial passage through a 1.3 m gate | Met: 1,197 mm over the rub strakes (bottom 60 mm wider, LSK-DDR-003) |
| R5 | Level flotation when swamped | Floats approximately level with rated persons aboard when fully swamped, using the ABYC H-8 test method (not certified) | Swamp test in a pool following ABYC H-8 procedure | Met on paper: 0.45 deg trim, 160 mm freeboard at the transom with nobody moving; 215 mm with the operating rule (stern quarter foam and the rule, LSK-DDR-003) |
| R6 | Boarding from waist-deep water | An 80 kg adult boards over the stern step unaided; heel stays under 10 degrees (target) | Boarding trials with several volunteers of different builds, inclinometer on the hull | Met on paper: 3.3 deg heel over the stern step (12.8 deg over the side for comparison) |
| R7 | Assembly | Two halves joined in 10 min or less by two people with one spanner | Timed assembly trial | Met on paper (estimate): about 6 min, one 17 mm spanner |
| R8 | Local build | At least two build paths (plywood and epoxy, aluminium or plastic sheet) documented with mass and payload | Build by a partner boatyard from the published drawings | Met on paper: three paths in the material substitution table (LSK-CAL-001, section 8) |
| R9 | Prototype cost | USD 1,500 or less including step, poles and paddles | Bill of materials and receipts | USD 2,098: over the value-engineering target by USD 598 |
| R10 | Optional fin drive | Removable in 5 min or less; the boat meets R2 to R6 without it | Trials with and without the drive fitted | Not shown on paper: no drive in the first prototype, decided by Amish (LSK-DDR-003); an open forward-only fin drive is kept as a later portfolio idea |

## Definitions used for the TRL 3 status

- **Hull mass:** the complete boat with its stern step, handles, strakes, skids and buoyancy, as carried; the push pole, paddles and bow line are loose gear (6.2 kg) and not counted.
- **Rated load:** five persons at 75 kg (a crew of two and three adults, 375 kg), placed as in LSK-CAL-001, section 3; decided by Amish with R3 (LSK-DDR-003) and stated on the capacity plate.
- **Swamped:** both halves full to the outside water level, persons aboard counted at two thirds of their weight (a conservative design assumption, not the ABYC H-8 rule itself).
- **Draft:** from the water surface to the outside of the bottom, at the transom and at the forward end of the waterline.

## Assumptions

- Fresh floodwater, 1,000 kg/m3; calm, slow water.
- Okoume marine plywood of about 450 kg/m3, softwood framing of about 500 kg/m3 and durable hardwood of about 700 kg/m3 for the step and bow eye pad can be bought near the first partner (light timber specification, LSK-DDR-003).
- Closed-cell polyethylene foam of about 30 kg/m3 with under 1 % water uptake by volume is available near the first partner.
- Two people can carry about 40 to 50 kg between them over a short distance; four can carry the assembled boat.
- A stern-centre step heels the boat less than a side step; LSK-CAL-001 confirms this on paper, the boarding trials confirm it in water.

> **Safety:** LaneSkiff is an open engineering reference for a rescue boat, not certified equipment. Every trial behind R2, R3, R5 and R6 is run in calm, shallow water with a safety boat or bank team, every person in a life jacket, and the volunteers briefed; no trial uses moving water. The step hinge and stop straps are proof-loaded to twice their working load before any boarding trial. The five-person rating and the swamped operating rule (stay in the boat, sit low and centred, the aft crew member moves amidships) are printed on the capacity plate.
