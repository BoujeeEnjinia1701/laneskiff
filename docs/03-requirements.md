---
doc_id: LSK-REQ-001
title: LaneSkiff requirements
project: LaneSkiff
doc_type: Requirements
version: "0.4"
status: Draft
date: '2026-10-04'
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
  change: Amish's decisions 30A, 31C and 32A (LSK-DDR-003) carried out; rated load restated as five persons (375 kg); R5 states the stern quarter foam and the aft-crew rule; R10 left out of the first prototype; TRL 3 status from LSK-CAL-001 v0.2; numeric targets unchanged
- version: "0.4"
  date: '2026-10-04'
  author: Amish Chadha
  change: "R2 restated by Amish's round-3 decision 6A (LSK-DDR-004): payload 375 kg (five persons) within the R3 draft limit, ratio reported; met"
---

# LaneSkiff requirements

Requirements for the first prototype, built on the plywood and epoxy path in the light timber specification (okoume plywood, 4 mm sides, softwood framing). Numeric targets are those set at TRL 1 and are unchanged. On 2026-10-03 Amish decided the open requirement items (LSK-DDR-003): "i agree with all the 46 recommendations you provided. please proceed." Decision 30A sets the rated load at five persons, 31C adds stern quarter foam and the aft-crew rule to R5, and 32A leaves the fin drive out of the first prototype. Status is the paper result at TRL 3 from LSK-CAL-001; every requirement is verified by test at TRL 4. On 2026-10-04 Amish decided option 6A on R2: "For round 3, I agree with all your proposed recommendations". R2 is restated as "payload 375 kg (five persons) within the R3 draft limit; the payload-to-hull ratio is reported" (LSK-DDR-004). Where a requirement is not met or is at risk on paper, the state and the options are set out for Amish in `docs/REVIEW.md` and listed as open decisions in LSK-DEC-001.

*Table 1. Requirements.*

| ID | Requirement | Target | Verification (TRL 4) | TRL 3 status |
| --- | --- | --- | --- | --- |
| R1 | Carry mass | Complete hull 50 kg or less; each half 25 kg or less (plywood and epoxy path, target) | Weigh the prototype halves | Not met on paper: hull 87.9 kg, halves 49.9 and 38.1 kg; accepted by Amish with the light timber specification and shoulder slings (decision 30A) |
| R2 | Payload | Payload 375 kg (five persons) within the R3 draft limit; the payload-to-hull ratio is reported, not a pass mark (restated 2026-10-04, decision 6A) | Static load test with water ballast in calm water | Met on paper as restated: 375 kg at 148 mm draft, inside the 150 mm limit. Reported ratio: 4.3 times hull mass at the rated load; 401 kg fits within the R3 draft (4.6) |
| R3 | Draft at rated load | 15 cm or less at the rated load of five persons (375 kg), Amish, 2026-10-03, decision 30A: "i agree with all the 46 recommendations you provided. please proceed." | Measured at the transom and bow during the load test | Met on paper: 148 mm at the transom, 138 mm at the forward end of the waterline |
| R4 | Width for lanes | Beam 1.2 m or less overall | Tape measure; trial passage through a 1.3 m gate | Met: 1,197 mm over the rub strakes (3 mm margin after the 60 mm wider bottom) |
| R5 | Level flotation when swamped | Floats approximately level with rated persons aboard when fully swamped, using the ABYC H-8 test method (not certified); 30 L of foam in the stern quarters, and the aft crew moves amidships when swamped (operating rule), Amish, 2026-10-03, decision 31C: "i agree with all the 46 recommendations you provided. please proceed." | Swamp test in a pool following ABYC H-8 procedure, with and without the aft-crew rule | Met on paper: 0.4 deg trim and 161 mm freeboard at the transom with the foam alone; 216 mm at the transom and 141 mm at the bow with the rule as well |
| R6 | Boarding from waist-deep water | An 80 kg adult boards over the stern step unaided; heel stays under 10 degrees (target) | Boarding trials with several volunteers of different builds, inclinometer on the hull | Met on paper: 3.3 deg heel over the stern step (12.8 deg over the side for comparison) |
| R7 | Assembly | Two halves joined in 10 min or less by two people with one spanner | Timed assembly trial | Met on paper (estimate): about 6 min, one 17 mm spanner |
| R8 | Local build | At least two build paths (plywood and epoxy, aluminium or plastic sheet) documented with mass and payload | Build by a partner boatyard from the published drawings | Met on paper: three paths in the material substitution table (LSK-CAL-001, section 8) |
| R9 | Prototype cost | USD 1,500 or less including step, poles and paddles | Bill of materials and receipts | USD 1,961: over the value-engineering target by USD 461 |
| R10 | Optional fin drive | Removable in 5 min or less; the boat meets R2 to R6 without it. Not part of the first prototype, Amish, 2026-10-03, decision 32A: "i agree with all the 46 recommendations you provided. please proceed." | Trials with and without the drive fitted, once a drive exists | Not shown on paper: left out of the first prototype by decision; R2 to R6 are assessed without a drive |

## Definitions used for the TRL 3 status

- **Hull mass:** the complete boat with its stern step, handles, strakes, skids and buoyancy, as carried; the push pole, paddles and bow line are loose gear (6.2 kg) and not counted.
- **Rated load:** five persons at 75 kg (a crew of two and three adults, 375 kg), placed as in LSK-CAL-001, section 3; decided by Amish on 2026-10-03 (decision 30A) and marked on the transom.
- **Swamped:** both halves full to the outside water level, persons aboard counted at two thirds of their weight (a conservative design assumption, not the ABYC H-8 rule itself).
- **Draft:** from the water surface to the outside of the bottom, at the transom and at the forward end of the waterline.

## Assumptions

- Fresh floodwater, 1,000 kg/m3; calm, slow water.
- Okoume marine plywood of about 450 kg/m3 and softwood framing of about 500 kg/m3 (light timber specification, decision 30A); hardwood of about 700 kg/m3 only for the step, the bow eye pad and the rung.
- Closed-cell polyethylene foam of about 30 kg/m3 with under 1 % water uptake by volume is available near the first partner.
- Two people can carry about 40 to 50 kg between them over a short distance; four can carry the assembled boat.
- A stern-centre step heels the boat less than a side step; LSK-CAL-001 confirms this on paper, the boarding trials confirm it in water.

> **Safety:** LaneSkiff is an open engineering reference for a rescue boat, not certified equipment. Every trial behind R2, R3, R5 and R6 is run in calm, shallow water with a safety boat or bank team, every person in a life jacket, and the volunteers briefed; no trial uses moving water. The step hinge and stop straps are proof-loaded to twice their working load before any boarding trial. The boat carries no more than five persons; when swamped, the aft crew moves amidships and everyone stays seated, low and centred.
