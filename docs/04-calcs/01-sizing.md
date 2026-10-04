---
doc_id: LSK-CAL-001
title: LaneSkiff sizing calculations
project: LaneSkiff
doc_type: Calculation
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First sizing of the constructable design (LSK-DDR-002); results against LSK-REQ-001
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Round 2 requirement decisions (LSK-DDR-003); light timber specification, bottom 60 mm wider, five-person rating, stern quarter foam and the swamped operating rule; every result recomputed
---

# LaneSkiff sizing calculations

With Amish's round 2 decisions of 2026-10-03 (LSK-DDR-003) the hull is built to the light timber specification with a bottom 60 mm wider and is rated for five persons (375 kg). On paper it now meets the draft target (148 mm at the transom), floats swamped with 160 mm of freeboard at the transom even if nobody moves, boards over the stern step with 3.3 degrees of heel, and still fits a 1.2 m lane at 1,197 mm. It is still too heavy for the carry target (88 kg; halves of 50 and 38 kg) and, because the rating fell from six to five persons, the payload ratio is lower than before: 4.26 against the target of 6. Section 9 compares the decided design with the design before the decisions.

Every figure comes from `docs/04-calcs/sizing.py`, which imports the parametric model (`cad/src/model.py`), so the sizes here are those of the STEP files, the drawings and the build plan. Tags in square brackets match the script output and `docs/04-calcs/results.csv`. These are screening estimates for a paper proof of concept; they do not replace the load, boarding and swamp trials, which are TRL 4 work.

> **Safety:** These numbers are for a design review, not a rating. No LaneSkiff carries people before its step, straps, handles and bow eye are proof-loaded and it has passed a load test and a swamp test in calm, shallow water with a safety boat and every person in a life jacket. Never in moving water. The five-person rating and the swamped operating rule go on the capacity plate (BOM line 30).

## 1. Method and assumptions

**Masses.** Every made part's volume from the model times its material density, plus catalogue masses for bought fittings, plus glass, epoxy, coating and tape worked out from the panel areas and seam lengths.

**Afloat.** The hull envelope (the outside of the planking and the skids) is cut at a trial waterline and the draft found where the displaced water equals the total weight. Trim and heel come from the waterplane, which is a rectangle while the waterline is on the flat part of the bottom: transverse stability GM = KB + I_T / V - KG, and trim = (LCB - LCG) / GM_L.

**Swamped.** Every body floats on its own: the water inside the hull is part of the flood and carries nothing. Foam gives lift for its submerged volume. Plywood, timber and HDPE count as exactly as dense as water, so they give no lift when submerged and their full weight above water (conservative). Glass, epoxy, fittings and foam count at full weight. People count at two thirds of their weight. The R5 result is taken with the people where they sit (the operating rule not followed); the case with the rule is given beside it.

*Table 1. Assumptions.*

| # | Assumption | Value | Basis |
| --- | --- | --- | --- |
| A1 | Water density | 1,000 kg/m3 | Fresh floodwater |
| A2 | Marine plywood | Okoume, 450 kg/m3 (600 before) | Light timber specification, LSK-DDR-003; BS 1088 okoume |
| A3 | Timber | Softwood framing 500 kg/m3 (ring frames, inwales, stringers, bench rails, knuckle floor); durable hardwood 700 kg/m3 for the hinge rail, backing block, float rim, kick rung and bow eye pad | LSK-DDR-003 |
| A4 | Foam | Closed-cell polyethylene, 30 kg/m3, under 1 % water uptake by volume | Supplier data to confirm |
| A5 | Glass and epoxy | 0.80 kg/m2 outside the bottom and sides, no glass inside the floor (0.40 kg/m2 before), 0.20 kg/m2 per coated face, 0.25 kg per metre of taped seam, 1.5 kg of small fixings | LSK-DDR-003; typical stitch-and-glue practice |
| A6 | Persons | 75 kg each; rated load five (a crew of two and three adults, 375 kg; six and 450 kg before); boarder 80 kg | LSK-DDR-003 |
| A7 | Person positions, rated load | Crew standing aft at 0.4 m (poling) and kneeling forward at 2.9 m; two adults on the aft benches at 1.0 m, one on the forward benches at 2.2 m | Placement for the paper case; trials place people as crews do |
| A8 | Persons when swamped | Two thirds of their weight carried by the boat | Conservative design assumption, to be replaced by the ABYC H-8 procedure test |
| A9 | Material strengths | Plywood bending 40 MPa (glass ignored); M10 A4-70 bolt 29 kN; nut plate bearing 9.6 kN on softwood at 6 MPa (estimate; 16 kN on hardwood before); 25 mm webbing 8 kN; strap hinge 4 kN | To confirm with real parts; okoume may be weaker in bending than the plywood the 40 MPa was taken for |

## 2. Masses

*Table 2. Hull mass, light timber specification.*

| Tag | Item | Mass |
| --- | --- | --- |
| [M4ply] | Okoume plywood: bottoms, sides, transoms, bulkheads, bow box, step decks | 24.8 kg |
| [M4sw] | Softwood framing: ring frames, inwales, stringers, bench rails, knuckle floor | 12.8 kg |
| [M4hw] | Hardwood: hinge rail, backing block, float rim, rung, bow eye pad | 4.2 kg |
| [M4foam] | Foam: bench modules, stern quarter modules, bow box, step float | 18.3 kg |
| [M5] | Glass, epoxy, coating, tapes, small fixings | 12.4 kg |
| [M4hdpe] | HDPE rub strakes and skids | 4.7 kg |
| [M4fabric] | Module covers and straps | 5.1 kg |
| [M4bought] | Bought fittings: hinges, pad eyes, straps, handles | 4.3 kg |
| [M4steel] | Joint bolts, nut plates, pins, rail bolts, bow eye | 1.3 kg |
| [M1] | **Hull, as carried** | **88.0 kg** (100.2 kg before) |
| [M2], [M3] | Aft half with the stern step; forward half | 49.9 kg; 38.1 kg (55.7 and 44.5 kg before) |
| [M9] | Each of two carriers per half with the shoulder slings: aft half; forward half | 25.0 kg; 19.0 kg |
| [M6] | Loose gear (pole, paddles, bow line), not in the hull mass | 6.2 kg |

Plywood areas [M8]: bottom 3.82 m2, sides 2.73 m2, other panels 3.09 m2. Hull centre of mass [M7]: 1,554 mm forward of the transom, 177 mm above the outside of the bottom. The light specification saves about 18 kg as the option estimated; the wider bottom and the extra foam put back about 6 kg (wider panels, wider bench foam, the two quarter modules).

## 3. Afloat

*Table 3. Hydrostatics, fresh water, five-person rated load.*

| Tag | Case | Result |
| --- | --- | --- |
| [L1], [L2] | Rated load; over hull mass | 375 kg; 4.26 |
| [H1] | Draft at rated load, even keel | 143 mm |
| [H2] | Trim at rated load; draft at the transom; at the forward end of the waterline | 0.16 deg stern down; 148 mm; 138 mm |
| [H3] | Lowest freeboard at rated load | 252 mm |
| [H4] | Waterline length and beam at rated load | 3.34 m; 1.10 m |
| [H5] | Transverse GM at rated load, with the aft crew standing | 0.31 m |
| [H6] | Load to sink 10 mm at rated draft | 36.8 kg |
| [H7], [H8] | Load carried at 150 mm draft, even keel; over hull mass | 401 kg; 4.55 |
| [H9] | Draft with the crew of two only | 79 mm |

With a crew of two the boat draws 79 mm. At the five-person rated load the deepest draft is 148 mm, at the transom, inside the 150 mm of R3 by 2 mm; the option estimated about 145 mm. The load the hull can carry within 150 mm of draft is 401 kg, so the margin is about 26 kg, a third of a person. The wider bottom doubles the transverse GM at rated load (0.31 m against 0.15 m before).

## 4. Swamped

*Table 4. Swamped with the five rated persons aboard (people at two thirds of their weight).*

| Tag | Quantity | Result |
| --- | --- | --- |
| [F1] | Buoyancy foam in the hull (benches 0.40 m3, stern quarter modules 0.03 m3, bow box 0.17 m3) | 0.592 m3 |
| [F2] | Water level, inside and out, above the outside of the bottom | 225 mm |
| [F3] | Weight carried by the foam | 307 kg |
| [F4] | Trim, quarter foam fitted, aft crew where they stood | 0.45 deg stern down |
| [F5] | Freeboard at the transom; at the bow, same case | 160 mm; 188 mm |
| [F5r] | Quarter foam fitted and the operating rule followed (aft crew amidships): trim; transom freeboard; bow freeboard | 1.17 deg bow down; 215 mm; 142 mm |
| [F5o] | For comparison, the rule without the quarter foam: trim; transom freeboard | 0.44 deg bow down; 181 mm |
| [F5n] | For comparison, neither: trim; transom freeboard | 1.41 deg stern down; 115 mm |
| [F6] | Transverse GM, swamped | 0.56 m |
| [F7], [F8] | Two seated persons move 400 mm to one side: heel; low-side freeboard | 13.2 deg; 38 mm |
| [F9] | Lift needed for zero freeboard as a share of the fitted foam | 0.49 |

R5 is met on paper with margin. The swamped boat floats within half a degree of level with 160 mm at the transom even if the aft crew member stays aft, and the operating rule raises the transom freeboard to 215 mm. Most of the gain over the 36 mm before comes from the five-person rating, the lighter hull and the wider bench foam; the quarter foam and the rule each add margin at the stern. If two people move to one side the low-side gunwale stays 38 mm above the water, where before it dipped; moving about in a swamped boat is still a training point.

## 5. Boarding over the stern step

*Table 5. An 80 kg person boarding, crew of two seated amidships (2.1 m on the benches).*

| Tag | Case | Result |
| --- | --- | --- |
| [B1] | Heel with the boarder's weight on the step, 150 mm off the centreline | 3.3 deg |
| [B2] | Trim and transom freeboard while boarding over the stern | 0.7 deg stern down; 279 mm |
| [B3] | For comparison, the same person climbing over the side at the gunwale | 12.8 deg heel |
| [B4] | Low-side freeboard in the side case | 164 mm |

The stern step works as the concept intends, and the wider bottom lowers the heel further (4.3 degrees before). The float's own buoyancy (about 17 L) is ignored, so the real heel and trim while boarding are a little lower.

## 6. Structure

*Table 6. Screening checks of the parts that carry the most load.*

| Tag | Check | Result |
| --- | --- | --- |
| [S1], [S2], [S3] | Floor: largest clear span between stringers and bench rails; bending stress under a 1.2 kN foot load on a 300 mm strip; factor on plywood strength | 160 mm; 26.7 MPa; 1.5 (glass ignored) |
| [S4], [S5] | Joint: boat with rated load hogging over a kerb at the joint, ends free; tension in each top bolt; factor on the bolt and on the nut plate bearing | 2.7 kN; 10.7 and 3.5 |
| [S6], [S7] | Step: 80 kg kneeling on the aft edge of the float at its stop, dynamic factor 2; pull in each stop strap; factor on the webbing | 1.88 kN; 4.2 |
| [S8] | Step hinges: load on each (upper bound) and factor | 2.67 kN; 1.5 |

The floor factor of 1.5 assumes 40 MPa bending strength and ignores glass; with okoume and no glass inside the floor this is the check to confirm first (an open item in LSK-DEC-001). The nut plates now bear on softwood frames, so their factor falls to 3.5 (an estimate; 5.0 before on hardwood); it stays above the bolt's need, but the bearing strength of the softwood bought is to be confirmed. The 4 mm sides carry no calculated load case here; their resistance to knocks against walls and kerbs in a lane is not checked on paper. The step hinges have the smallest factor; they are proof-loaded before any boarding trial (LSK-BLD-001, safety stops).

## 7. Joining the halves

[T1] Placing and aligning the halves on the two pins takes about 2 minutes, eight bolts at about 25 seconds each with one 17 mm spanner about 3.2 minutes, and a final check about 1 minute: about 6.2 minutes for two people (estimate).

## 8. Material substitution table

*Table 7. Build paths, same hull form (R8).*

| Tag | Build path | Hull mass | Load at 150 mm draft | Load over hull mass |
| --- | --- | --- | --- | --- |
| [P1] | Okoume plywood and epoxy, stitch and glue (prototype) | 88 kg | 401 kg | 4.6 |
| [P2] | Aluminium 5052 sheet: 2.5 mm bottom, 2.0 mm sides and ends, welded or riveted; aluminium angle frames | 101 kg | 387 kg | 3.8 |
| [P3] | HDPE or polypropylene sheet: 8 mm bottom, 6 mm sides, 5 mm ends, plastic welded | 111 kg | 377 kg | 3.4 |

The light plywood path is now the lightest. The aluminium and plastic paths carry the same foam, step and fittings and are screening estimates only.

## 9. The decided design against the design before

*Table 8. Comparisons (LSK-DDR-003).*

| Tag | Case | Result |
| --- | --- | --- |
| [D1] | Six persons (450 kg) on the decided hull: deepest draft; load over hull mass | 177 mm; 5.11 |
| [D2] | Rated load that R2 (six times hull mass) would need on the decided hull; in 75 kg persons | 528 kg; 7.0 |

The R2 option in the TRL 3 review gave a ratio of about 5.45 for the light specification at six persons. The R3 decision rates the boat for five persons, so the ratio is 375 / 88 = 4.26, lower than the 4.49 of the design before the decisions. At six persons the ratio would be 5.11 on this hull but the draft 177 mm (R3 not met). No rating meets R2 and R3 together on this hull: R2 needs 528 kg aboard, R3 allows about 401 kg. This is posed as a new decision in `docs/REVIEW.md`.

## 10. Cost

[C1] Estimated cost of the constructable design, from `bom/bom.csv`: USD 2,098 (USD 1,922 before). Value-engineering target: USD 1,500. Over the value-engineering target by USD 598. The increase is okoume plywood (about USD 144, priced at about 1.4 times the local marine plywood, an estimate), one more foam sheet (USD 55), the stern quarter module covers and straps (USD 14, estimate) and the capacity plate (USD 10, estimate), less softwood framing (USD 27) and the glass no longer inside the floor (USD 21). The largest lines are the foam (USD 385), the hull plywood (USD 624, lines 1 to 5), the epoxy (USD 200) and the fittings (handles USD 100, step USD 75).

## 11. Results against the requirements

*Table 9. Results against LSK-REQ-001 (before LSK-DDR-003 in brackets).*

| ID | Result | Status |
| --- | --- | --- |
| R1 | Hull 88 kg; halves 50 and 38 kg; 25 and 19 kg each for two carriers per half with the slings (100 kg; 56 and 45 kg) | Not met |
| R2 | 375 kg rated load is 4.26 times hull mass (4.49) | Not met |
| R3 | 148 mm at the transom, 138 mm at the forward end of the waterline, five persons (187 mm, six persons) | Met on paper, 2 mm margin |
| R4 | 1,197 mm over the rub strakes (1,137 mm) | Met |
| R5 | 0.45 deg trim, 160 mm freeboard at the transom with nobody moving; 215 mm with the operating rule (2.1 deg, 36 mm) | Met on paper |
| R6 | 3.3 deg over the stern step (4.3 deg) | Met on paper |
| R7 | About 6 min, one spanner | Met on paper (estimate) |
| R8 | Three build paths with mass and payload | Met on paper |
| R9 | USD 2,098 (USD 1,922) | Over the value-engineering target by USD 598 |
| R10 | No fin drive in the first prototype, decided (LSK-DDR-003) | Not shown on paper |
