---
doc_id: LSK-CAL-001
title: LaneSkiff sizing calculations
project: LaneSkiff
doc_type: Calculation
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First sizing of the constructable design (LSK-DDR-002); results against LSK-REQ-001
---

# LaneSkiff sizing calculations

On paper the constructable LaneSkiff does what the concept asks of it in the water, but it is twice as heavy as the carry target. Boarding over the stern step heels the boat 4.3 degrees against 15.6 degrees over the side; swamped with six people aboard it stays afloat and nearly level; the halves join in about six minutes with one spanner; and the beam fits a 1.2 m lane. The hull weighs 100 kg as built in plywood and epoxy (halves of 56 and 45 kg), so the carry mass, the payload ratio and the draft at a six-person rated load are not met, and the swamped transom freeboard is only 36 mm. Each of these is set out for Amish with options in `docs/REVIEW.md`; section 9 gives the numbers behind the options.

Every figure comes from `docs/04-calcs/sizing.py`, which imports the parametric model (`cad/src/model.py`), so the sizes here are those of the STEP files, the drawings and the build plan. Tags in square brackets match the script output and `docs/04-calcs/results.csv`. These are screening estimates for a paper proof of concept; they do not replace the load, boarding and swamp trials, which are TRL 4 work.

> **Safety:** These numbers are for a design review, not a rating. No LaneSkiff carries people before its step, straps, handles and bow eye are proof-loaded and it has passed a load test and a swamp test in calm, shallow water with a safety boat and every person in a life jacket. Never in moving water.

## 1. Method and assumptions

**Masses.** Every made part's volume from the model times its material density, plus catalogue masses for bought fittings, plus glass, epoxy, coating and tape worked out from the panel areas and seam lengths.

**Afloat.** The hull envelope (the outside of the planking and the skids) is cut at a trial waterline and the draft found where the displaced water equals the total weight. Trim and heel come from the waterplane, which is a rectangle while the waterline is on the flat part of the bottom: transverse stability GM = KB + I_T / V - KG, and trim = (LCB - LCG) / GM_L.

**Swamped.** Every body floats on its own: the water inside the hull is part of the flood and carries nothing. Foam gives lift for its submerged volume. Plywood, timber and HDPE count as exactly as dense as water, so they give no lift when submerged and their full weight above water (conservative). Glass, epoxy, fittings and foam count at full weight. People count at two thirds of their weight.

*Table 1. Assumptions.*

| # | Assumption | Value | Basis |
| --- | --- | --- | --- |
| A1 | Water density | 1,000 kg/m3 | Fresh floodwater |
| A2 | Marine plywood | 600 kg/m3 | BS 1088 plywood runs from about 450 (okoume) to 700 (gurjan); middle of the range as found in India |
| A3 | Durable hardwood | 700 kg/m3 | Teak, jackwood or similar local timber |
| A4 | Foam | Closed-cell polyethylene, 30 kg/m3, under 1 % water uptake by volume | Supplier data to confirm |
| A5 | Glass and epoxy | 0.80 kg/m2 outside the bottom and sides, 0.40 kg/m2 inside the floor, 0.20 kg/m2 per coated face, 0.25 kg per metre of taped seam, 1.5 kg of small fixings | Typical stitch-and-glue practice |
| A6 | Persons | 75 kg each; rated load six (a crew of two and four adults, 450 kg); boarder 80 kg | LSK-REQ-001 |
| A7 | Person positions, rated load | Crew standing aft at 0.4 m (poling) and kneeling forward at 2.9 m; two adults on the aft benches at 1.0 m, two on the forward benches at 2.2 m | Placement for the paper case; trials place people as crews do |
| A8 | Persons when swamped | Two thirds of their weight carried by the boat | Conservative design assumption, to be replaced by the ABYC H-8 procedure test |
| A9 | Material strengths | Plywood bending 40 MPa (glass ignored); M10 A4-70 bolt 29 kN; nut plate bearing 16 kN; 25 mm webbing 8 kN; strap hinge 4 kN | To confirm with real parts |

## 2. Masses

*Table 2. Hull mass, plywood and epoxy path.*

| Tag | Item | Mass |
| --- | --- | --- |
| [M4ply] | Plywood: bottoms, sides, transoms, bulkheads, bow box, step decks | 34.9 kg |
| [M4hw] | Hardwood: ring frames, inwales, stringers, bench rails, knuckle floor, hinge rail, float rim, rung | 21.8 kg |
| [M4foam] | Foam: bench modules, bow box, step float | 15.3 kg |
| [M5] | Glass, epoxy, coating, tapes, small fixings | 13.6 kg |
| [M4hdpe] | HDPE rub strakes and skids | 4.7 kg |
| [M4fabric] | Bench module covers and straps | 4.2 kg |
| [M4bought] | Bought fittings: hinges, pad eyes, straps, handles | 4.3 kg |
| [M4steel] | Joint bolts, nut plates, pins, rail bolts, bow eye | 1.3 kg |
| [M1] | **Hull, as carried** | **100.2 kg** |
| [M2], [M3] | Aft half with the stern step; forward half | 55.7 kg; 44.5 kg |
| [M6] | Loose gear (pole, paddles, bow line), not in the hull mass | 6.2 kg |

Plywood areas [M8]: bottom 3.58 m2, sides 2.73 m2, other panels 2.95 m2. Hull centre of mass [M7]: 1,588 mm forward of the transom, 174 mm above the outside of the bottom.

## 3. Afloat

*Table 3. Hydrostatics, fresh water.*

| Tag | Case | Result |
| --- | --- | --- |
| [L1], [L2] | Rated load; over hull mass | 450 kg; 4.49 |
| [H1] | Draft at rated load, even keel | 175 mm |
| [H2] | Trim at rated load; draft at the transom; at the forward end of the waterline | 0.41 deg bow down; 162 mm; 187 mm |
| [H3] | Lowest freeboard at rated load | 238 mm |
| [H4] | Waterline length and beam at rated load | 3.49 m; 1.05 m |
| [H5] | Transverse GM at rated load, with the aft crew standing | 0.15 m |
| [H6] | Load to sink 10 mm at rated draft | 36.6 kg |
| [H7], [H8] | Load carried at 150 mm draft, even keel; over hull mass | 361 kg; 3.61 |
| [H9] | Draft with the crew of two only | 87 mm |

With a crew of two the boat draws under 90 mm, so it can be poled through knee-deep water to reach people. At the six-person rated load it draws 175 mm on an even keel and, with the people placed as in A7, 187 mm at the forward end of the waterline. The load the hull can carry within 150 mm of draft is 361 kg, about five persons.

## 4. Swamped

*Table 4. Swamped with the rated persons aboard (people at two thirds of their weight).*

| Tag | Quantity | Result |
| --- | --- | --- |
| [F1] | Buoyancy foam in the hull (benches 0.34 m3, bow box 0.16 m3) | 0.494 m3 |
| [F2] | Water level, inside and out, above the outside of the bottom | 290 mm |
| [F3] | Weight carried by the foam | 357 kg |
| [F4] | Trim | 2.05 deg stern down |
| [F5] | Freeboard at the transom; at the bow | 36 mm; 164 mm |
| [F6] | Transverse GM, swamped | 0.32 m |
| [F7], [F8] | Two seated persons move 400 mm to one side: heel; low-side freeboard | 19.3 deg; minus 85 mm (the gunwale dips) |
| [F9] | Lift needed for zero freeboard as a share of the fitted foam | 0.69 |

The swamped boat floats nearly level, which is what the LevelHull layout is for: the foam is outboard, so the waterplane of the foam is wide and the swamped boat resists heel (GM 0.32 m). The margin at the transom is small, because the standing crew member, the transom and the step are all aft while the bow box puts foam forward. If people move about in a swamped boat it can dip a gunwale; that is a training point for crews and a reason the R5 options in section 9 add margin aft.

## 5. Boarding over the stern step

*Table 5. An 80 kg person boarding, crew of two seated amidships (1.6 m on the benches).*

| Tag | Case | Result |
| --- | --- | --- |
| [B1] | Heel with the boarder's weight on the step, 150 mm off the centreline | 4.3 deg |
| [B2] | Trim and transom freeboard while boarding over the stern | 0.7 deg stern down; 270 mm |
| [B3] | For comparison, the same person climbing over the side at the gunwale | 15.6 deg heel |
| [B4] | Low-side freeboard in the side case | 133 mm |

The stern step works as the concept intends: a person climbing over the end of the boat moves its weight a short distance sideways, so the boat barely heels. The same person over the side heels it nearly four times as much and brings the gunwale within 133 mm of the water. The float's own buoyancy (about 17 L) is ignored here, so the real heel and trim while boarding are a little lower.

## 6. Structure

*Table 6. Screening checks of the parts that carry the most load.*

| Tag | Check | Result |
| --- | --- | --- |
| [S1], [S2], [S3] | Floor: largest clear span between stringers and bench rails; bending stress under a 1.2 kN foot load on a 300 mm strip; factor on plywood strength | 160 mm; 26.7 MPa; 1.5 (glass ignored) |
| [S4], [S5] | Joint: boat with rated load hogging over a kerb at the joint, ends free; tension in each top bolt; factor on the bolt and on the nut plate bearing | 3.2 kN; 9.0 and 5.0 |
| [S6], [S7] | Step: 80 kg kneeling on the aft edge of the float at its stop, dynamic factor 2; pull in each stop strap; factor on the webbing | 1.88 kN; 4.2 |
| [S8] | Step hinges: load on each (upper bound) and factor | 2.67 kN; 1.5 |

The floor needs its centre stringer and the bench rails: with only two stringers the span would be 255 mm and the factor under 1. The step hinges have the smallest factor; heavy hinges with 6 mm pins are specified and the hinge is proof-loaded before any boarding trial (LSK-BLD-001, safety stops).

## 7. Joining the halves

[T1] Placing and aligning the halves on the two pins takes about 2 minutes, eight bolts at about 25 seconds each with one 17 mm spanner about 3.2 minutes, and a final check about 1 minute: about 6.2 minutes for two people (estimate). The nuts are welded to plates on the aft frame, so nobody needs to hold a second spanner inside the boat.

## 8. Material substitution table

*Table 7. Build paths, same hull form (R8).*

| Tag | Build path | Hull mass | Load at 150 mm draft | Load over hull mass |
| --- | --- | --- | --- | --- |
| [P1] | Plywood and epoxy, stitch and glue (prototype) | 100 kg | 361 kg | 3.6 |
| [P2] | Aluminium 5052 sheet: 2.5 mm bottom, 2.0 mm sides and ends, welded or riveted; aluminium angle frames | 98 kg | 364 kg | 3.7 |
| [P3] | HDPE or polypropylene sheet: 8 mm bottom, 6 mm sides, 5 mm ends, plastic welded | 110 kg | 352 kg | 3.2 |

The paths come out close, because the foam, step, fittings and framing weigh the same in each. Aluminium needs welding or riveting skills and corrosion care; plastic sheet needs a plastic welder and is the heaviest but the most abrasion-tolerant. Plywood and epoxy is the path most yards in Kerala and Bihar can build and repair.

## 9. Numbers behind the options for Amish

*Table 8. Option estimates (screening; see `docs/REVIEW.md`, Decisions for Amish).*

| Tag | Option | Result |
| --- | --- | --- |
| [O1], [O2] | Light timber specification: okoume plywood (about 450 kg/m3), 4 mm sides, softwood framing (about 500 kg/m3), no glass inside the floor | Hull 82.5 kg; halves 45.9 and 36.6 kg |
| [O3] | Light specification, six persons: load over hull mass | 5.45 |
| [O4] | Rated load of five persons (375 kg), present specification: deepest draft; over hull mass | 160 mm; 3.74 |
| [O9] | Rated load of four persons (300 kg): deepest draft; over hull mass | 155 mm; 2.99 |
| [O10] | Light specification with five persons: deepest draft; over hull mass | 154 mm; 4.54 |
| [O5] | Light specification with six persons: deepest draft | 184 mm |
| [O6] | Bottom 60 mm wider (beam about 1.20 m): deepest draft at six persons | about 176 mm |
| [O7] | 30 L of foam in the two stern quarters: swamped trim; transom freeboard | 0.37 deg; about 113 mm (estimate) |
| [O8] | Operating rule: the aft crew member moves amidships when swamped: trim; transom freeboard | 0.02 deg; 109 mm |

Combining the light specification, a five-person rating and a 60 mm wider bottom gives a deepest draft of about 145 mm (scaled from [O10] and [O6]).

## 10. Cost

[C1] Estimated cost of the constructable design, from `bom/bom.csv`: USD 1,922. Value-engineering target: USD 1,500. Over the value-engineering target by USD 422. The largest lines are the foam (USD 330), epoxy (USD 200), the 6 mm plywood (USD 280) and the fittings (handles USD 100, step USD 75).

## 11. Results against the requirements

*Table 9. Results against LSK-REQ-001.*

| ID | Result | Status |
| --- | --- | --- |
| R1 | Hull 100 kg; halves 56 and 45 kg | Not met |
| R2 | 450 kg rated load is 4.5 times hull mass | Not met |
| R3 | 187 mm at the forward end of the waterline, 162 mm at the transom (six persons) | Not met |
| R4 | 1,137 mm over the rub strakes | Met |
| R5 | Afloat, 2.1 deg trim, 36 mm freeboard at the transom | Met on paper, small margin (at risk) |
| R6 | 4.3 deg over the stern step | Met on paper |
| R7 | About 6 min, one spanner | Met on paper (estimate) |
| R8 | Three build paths with mass and payload | Met on paper |
| R9 | USD 1,922 | Over the value-engineering target by USD 422 |
| R10 | No fin drive in the first prototype design | Not shown on paper |
