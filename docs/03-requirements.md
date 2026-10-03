---
doc_id: LSK-REQ-001
title: LaneSkiff requirements
project: LaneSkiff
doc_type: Requirements
version: "0.2"
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
---

# LaneSkiff requirements

Requirements for the first prototype, built on the plywood and epoxy path. Targets are those set at TRL 1 and are unchanged. Status is the paper result at TRL 3 from LSK-CAL-001; every requirement is verified by test at TRL 4. Where a requirement is not met or is at risk on paper, the state and the options are set out for Amish in `docs/REVIEW.md` (TRL 3 section) and listed as open decisions in LSK-DEC-001.

*Table 1. Requirements.*

| ID | Requirement | Target | Verification (TRL 4) | TRL 3 status |
| --- | --- | --- | --- | --- |
| R1 | Carry mass | Complete hull 50 kg or less; each half 25 kg or less (plywood and epoxy path, target) | Weigh the prototype halves | Not met on paper: hull 100 kg, halves 56 and 45 kg (decision for Amish) |
| R2 | Payload | At least 6 times hull mass, about 300 kg or four adults plus crew (target) | Static load test with water ballast in calm water | Not met on paper: 450 kg rated load is 4.5 times hull mass (decision for Amish) |
| R3 | Draft at rated load | 15 cm or less | Measured at the transom and bow during the load test | Not met on paper: 187 mm at the forward end of the waterline, 162 mm at the transom, six persons (decision for Amish) |
| R4 | Width for lanes | Beam 1.2 m or less overall | Tape measure; trial passage through a 1.3 m gate | Met: 1,137 mm over the rub strakes |
| R5 | Level flotation when swamped | Floats approximately level with rated persons aboard when fully swamped, using the ABYC H-8 test method (not certified) | Swamp test in a pool following ABYC H-8 procedure | Met on paper with a small margin: 2.1 deg trim, 36 mm freeboard at the transom (at risk; decision for Amish) |
| R6 | Boarding from waist-deep water | An 80 kg adult boards over the stern step unaided; heel stays under 10 degrees (target) | Boarding trials with several volunteers of different builds, inclinometer on the hull | Met on paper: 4.3 deg heel over the stern step (15.6 deg over the side for comparison) |
| R7 | Assembly | Two halves joined in 10 min or less by two people with one spanner | Timed assembly trial | Met on paper (estimate): about 6 min, one 17 mm spanner |
| R8 | Local build | At least two build paths (plywood and epoxy, aluminium or plastic sheet) documented with mass and payload | Build by a partner boatyard from the published drawings | Met on paper: three paths in the material substitution table (LSK-CAL-001, section 8) |
| R9 | Prototype cost | USD 1,500 or less including step, poles and paddles | Bill of materials and receipts | USD 1,922: over the value-engineering target by USD 422 |
| R10 | Optional fin drive | Removable in 5 min or less; the boat meets R2 to R6 without it | Trials with and without the drive fitted | Not shown on paper: no drive in the first prototype design (decision for Amish) |

## Definitions used for the TRL 3 status

- **Hull mass:** the complete boat with its stern step, handles, strakes, skids and buoyancy, as carried; the push pole, paddles and bow line are loose gear (6.2 kg) and not counted.
- **Rated load:** six persons at 75 kg (a crew of two and four adults, 450 kg), placed as in LSK-CAL-001, section 3. The final rating of the first prototype is part of the R3 decision.
- **Swamped:** both halves full to the outside water level, persons aboard counted at two thirds of their weight (a conservative design assumption, not the ABYC H-8 rule itself).
- **Draft:** from the water surface to the outside of the bottom, at the transom and at the forward end of the waterline.

## Assumptions

- Fresh floodwater, 1,000 kg/m3; calm, slow water.
- Marine plywood of about 600 kg/m3 and durable hardwood of about 700 kg/m3, as found in India and Bangladesh; lighter okoume plywood is an option (LSK-CAL-001, section 9).
- Closed-cell polyethylene foam of about 30 kg/m3 with under 1 % water uptake by volume is available near the first partner.
- Two people can carry about 40 to 50 kg between them over a short distance; four can carry the assembled boat.
- A stern-centre step heels the boat less than a side step; LSK-CAL-001 confirms this on paper, the boarding trials confirm it in water.

> **Safety:** LaneSkiff is an open engineering reference for a rescue boat, not certified equipment. Every trial behind R2, R3, R5 and R6 is run in calm, shallow water with a safety boat or bank team, every person in a life jacket, and the volunteers briefed; no trial uses moving water. The step hinge and stop straps are proof-loaded to twice their working load before any boarding trial.
