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
  change: Re-run for Amish's decisions 30A, 31C and 32A (LSK-DDR-003); light timber specification, five-person rating, bottom 60 mm wider, 30 L of stern quarter foam and the aft-crew rule; option table replaced by the decided results
---

# LaneSkiff sizing calculations

This revision sizes the design Amish chose on 2026-10-03 (LSK-DDR-003; his words: "i agree with all the 46 recommendations you provided. please proceed."): okoume plywood with 4 mm sides and softwood framing, a five-person rating, a bottom 60 mm wider, 30 L of foam in the stern quarters with the aft-crew rule, and no fin drive in the first prototype. On paper the boat now draws 148 mm at its rated load of five persons (R3 met), floats swamped with 161 mm of freeboard at the transom (R5 met with margin), heels 3.3 degrees when someone boards over the stern step, joins in about six minutes, and fits a 1.2 m lane with 3 mm to spare. The hull weighs 87.9 kg (halves of 49.9 and 38.1 kg), so the carry mass is still not met, as Amish accepted with the decision; and the five-person rated load is 4.3 times the hull mass against a target of 6, which is put to Amish as a new question in `docs/REVIEW.md`.

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
| A2 | Marine plywood | Okoume, 450 kg/m3 | Light timber specification (LSK-DDR-003); BS 1088 okoume |
| A3 | Framing and other timber | Softwood framing 500 kg/m3 (ring frames, inwales, stringers, bench rails, knuckle floor); durable hardwood 700 kg/m3 for the step, bow eye pad and rung | Light timber specification; the step and pad keep hardwood for wear and bolt bearing |
| A4 | Foam | Closed-cell polyethylene, 30 kg/m3, under 1 % water uptake by volume | Supplier data to confirm |
| A5 | Glass and epoxy | 0.80 kg/m2 outside the bottom and sides, none inside the floor, 0.20 kg/m2 per coated face, 0.25 kg per metre of taped seam, 1.5 kg of small fixings | Typical stitch-and-glue practice |
| A6 | Persons | 75 kg each; rated load five (a crew of two and three adults, 375 kg); boarder 80 kg | LSK-REQ-001; five-person rating decided by Amish (LSK-DDR-003) |
| A7 | Person positions, rated load | Crew standing aft at 0.4 m (poling) and kneeling forward at 2.9 m; two adults on the aft benches at 1.0 m, one on a forward bench at 2.2 m | Placement for the paper case; trials place people as crews do |
| A8 | Persons when swamped | Two thirds of their weight carried by the boat | Conservative design assumption, to be replaced by the ABYC H-8 procedure test |
| A9 | Material strengths | Plywood bending 40 MPa (glass ignored; okoume to confirm, see LSK-DEC-001); M10 A4-70 bolt 29 kN; nut plate bearing 16 kN; 25 mm webbing 8 kN; strap hinge 4 kN | To confirm with real parts |

## 2. Masses

*Table 2. Hull mass, light timber specification.*

| Tag | Item | Mass |
| --- | --- | --- |
| [M4ply] | Okoume plywood: bottoms, 4 mm sides, transoms, bulkheads, bow box, step decks | 24.8 kg |
| [M4sw] | Softwood framing: ring frames, inwales, stringers, bench rails, knuckle floor | 12.8 kg |
| [M4hw] | Hardwood: hinge rail, backing block, float rim, bow eye pad, rung | 4.2 kg |
| [M4foam] | Foam: bench modules, bow box, stern quarter modules, step float | 18.3 kg |
| [M5] | Glass (outside only), epoxy, coating, tapes, small fixings | 12.4 kg |
| [M4hdpe] | HDPE rub strakes and skids | 4.7 kg |
| [M4fabric] | Bench and quarter module covers and straps | 5.1 kg |
| [M4bought] | Bought fittings: hinges, pad eyes, straps, handles | 4.3 kg |
| [M4steel] | Joint bolts, nut plates, pins, rail bolts, bow eye | 1.3 kg |
| [M1] | **Hull, as carried** | **87.9 kg** |
| [M2], [M3] | Aft half with the stern step; forward half | 49.9 kg; 38.1 kg |
| [M6] | Loose gear (pole, paddles, bow line), not in the hull mass | 6.2 kg |

Plywood areas [M8]: bottom 3.82 m2, sides 2.73 m2, other panels 3.09 m2. Hull centre of mass [M7]: 1,556 mm forward of the transom, 177 mm above the outside of the bottom.

The light specification saves 14.9 kg of timber and 1.2 kg of glass and epoxy against version 0.1 (100.2 kg), but the wider bottom widens the bench modules and the stern quarter modules add 30 L, so foam and covers add 3.9 kg; the net saving is 12.3 kg, less than the 18 kg screening estimate, which left the foam unchanged. Each half carried by two people with the shoulder slings is about 25 and 19 kg a person.

## 3. Afloat

*Table 3. Hydrostatics, fresh water.*

| Tag | Case | Result |
| --- | --- | --- |
| [L1], [L2] | Rated load (five persons); over hull mass | 375 kg; 4.26 |
| [H1] | Draft at rated load, even keel | 143 mm |
| [H2] | Trim at rated load; draft at the transom; at the forward end of the waterline | 0.16 deg stern down; 148 mm; 138 mm |
| [H3] | Lowest freeboard at rated load | 252 mm |
| [H4] | Waterline length and beam at rated load | 3.34 m; 1.10 m |
| [H5] | Transverse GM at rated load, with the aft crew standing | 0.31 m |
| [H6] | Load to sink 10 mm at rated draft | 36.8 kg |
| [H7], [H8] | Load carried at 150 mm draft, even keel; over hull mass | 401 kg; 4.56 |
| [H9] | Draft with the crew of two only | 79 mm |
| [D1] | For comparison, six persons (450 kg) in this design: deepest draft; over hull mass | 177 mm; 5.12 |

With a crew of two the boat draws under 80 mm. At its five-person rated load it draws 148 mm at the transom, inside the 150 mm limit by 2 mm; the wider bottom also doubles the transverse GM at rated load (0.31 m against 0.15 m). Six persons would bring the draft back to 177 mm, so the rating plate says five. The load the hull carries within 150 mm of draft is 401 kg.

## 4. Swamped

*Table 4. Swamped with the rated persons aboard (people at two thirds of their weight).*

| Tag | Quantity | Result |
| --- | --- | --- |
| [F1] | Buoyancy foam in the hull (benches 0.39 m3, bow box 0.17 m3, stern quarter modules 0.03 m3) | 0.592 m3 |
| [F11] | Of which, the two stern quarter modules | 30.0 L |
| [F2] | Water level, inside and out, above the outside of the bottom | 224 mm |
| [F3] | Weight carried by the foam | 307 kg |
| [F4] | Trim, quarter foam fitted, aft crew where they stand | 0.42 deg stern down |
| [F5] | Freeboard at the transom; at the bow | 161 mm; 188 mm |
| [F10] | With the aft-crew rule as well (the aft crew moves amidships): trim; freeboard at the transom; at the bow | 1.19 deg bow down; 216 mm; 141 mm |
| [F6] | Transverse GM, swamped | 0.56 m |
| [F7], [F8] | Two seated persons move 400 mm to one side: heel; low-side freeboard | 13.1 deg; 39 mm (the gunwale stays out) |
| [F9] | Lift needed for zero freeboard as a share of the fitted foam | 0.49 |

The swamped boat floats nearly level with the stern quarter foam alone: 0.4 degrees stern down and 161 mm at the transom, against 36 mm before. The foam gives this margin even when nobody follows the rule. The aft-crew rule adds margin aft but trims the boat 1.2 degrees bow down, so both ends keep at least 141 mm. Fewer persons and wider bench modules also help: two people moving to one side no longer dip the gunwale. Crews still keep people seated, low and centred in a swamped boat.

## 5. Boarding over the stern step

*Table 5. An 80 kg person boarding, crew of two seated amidships (1.6 m on the benches).*

| Tag | Case | Result |
| --- | --- | --- |
| [B1] | Heel with the boarder's weight on the step, 150 mm off the centreline | 3.3 deg |
| [B2] | Trim and transom freeboard while boarding over the stern | 0.7 deg stern down; 279 mm |
| [B3] | For comparison, the same person climbing over the side at the gunwale | 12.8 deg heel |
| [B4] | Low-side freeboard in the side case | 164 mm |

The stern step works as the concept intends: a person climbing over the end of the boat moves its weight a short distance sideways, so the boat barely heels. The same person over the side heels it nearly four times as much and brings the gunwale within 164 mm of the water. The two stern quarter modules leave 250 mm clear between them at the step opening, so the boarder's legs come over the transom between them; their tops (346 mm above the bottom) are a knee rest. The float's own buoyancy (about 17 L) is ignored here, so the real heel and trim while boarding are a little lower.

## 6. Structure

*Table 6. Screening checks of the parts that carry the most load.*

| Tag | Check | Result |
| --- | --- | --- |
| [S1], [S2], [S3] | Floor: largest clear span between stringers and bench rails; bending stress under a 1.2 kN foot load on a 300 mm strip; factor on plywood strength | 160 mm; 26.7 MPa; 1.5 (no glass inside) |
| [S4], [S5] | Joint: boat with rated load hogging over a kerb at the joint, ends free; tension in each top bolt; factor on the bolt and on the nut plate bearing | 2.7 kN; 10.7 and 5.9 |
| [S6], [S7] | Step: 80 kg kneeling on the aft edge of the float at its stop, dynamic factor 2; pull in each stop strap; factor on the webbing | 1.88 kN; 4.2 |
| [S8] | Step hinges: load on each (upper bound) and factor | 2.67 kN; 1.5 |

The floor needs its centre stringer and the bench rails: with only two stringers the span would be 255 mm and the factor under 1. The floor check never counted the inside glass, so leaving it out does not change the factor; it does leave the floor with less abrasion margin, and the 40 MPa bending strength is to be confirmed for the okoume actually bought. The nut plates bear on softwood now; the factor of 5.9 uses the 10 MPa bearing figure, which softwood across the grain may not reach, so the plates are checked in the joint proof load. The step hinges have the smallest factor; heavy hinges with 6 mm pins are specified and the hinge is proof-loaded before any boarding trial (LSK-BLD-001, safety stops).

## 7. Joining the halves

[T1] Placing and aligning the halves on the two pins takes about 2 minutes, eight bolts at about 25 seconds each with one 17 mm spanner about 3.2 minutes, and a final check about 1 minute: about 6.2 minutes for two people (estimate). The nuts are welded to plates on the aft frame, so nobody needs to hold a second spanner inside the boat.

## 8. Material substitution table

*Table 7. Build paths, same hull form (R8).*

| Tag | Build path | Hull mass | Load at 150 mm draft | Load over hull mass |
| --- | --- | --- | --- | --- |
| [P1] | Okoume plywood and epoxy, stitch and glue, softwood framing (prototype) | 88 kg | 401 kg | 4.6 |
| [P2] | Aluminium 5052 sheet: 2.5 mm bottom, 2.0 mm sides and ends, welded or riveted; aluminium angle frames | 101 kg | 388 kg | 3.8 |
| [P3] | HDPE or polypropylene sheet: 8 mm bottom, 6 mm sides, 5 mm ends, plastic welded | 111 kg | 377 kg | 3.4 |

The plywood path is now the lightest; the other two come out close to each other, because the foam, step, fittings and framing weigh the same in each. Aluminium needs welding or riveting skills and corrosion care; plastic sheet needs a plastic welder and is the heaviest but the most abrasion-tolerant. Plywood and epoxy is the path most yards in Kerala and Bihar can build and repair.

## 9. Results of Amish's decisions of 2026-10-03

*Table 8. What decisions 30A, 31C and 32A changed (LSK-DDR-003).*

| Decision | Change | Result |
| --- | --- | --- |
| 30A | Okoume plywood, 4 mm sides, softwood framing, no glass inside the floor; five-person rating; bottom 60 mm wider (1,060 mm at the chine) | Hull 87.9 kg (was 100.2), halves 49.9 and 38.1 kg; deepest draft 148 mm at five persons (was 187 mm at six); beam 1,197 mm |
| 31C | Two 15 L foam modules in the stern quarters, and the aft-crew rule | Swamped transom freeboard 161 mm with the foam alone, 216 mm with the rule as well (was 36 mm) |
| 32A | No fin drive in the first prototype | Nothing to compute; R10 stays not shown |

*Table 9. Figures behind the R2 restatement (decision 6A of 2026-10-04, LSK-DDR-004; ratio reported, not a pass mark).*

| Tag | Quantity | Result |
| --- | --- | --- |
| [L2] | Five-person rated load over hull mass | 4.26 |
| [D3] | Load carried at 150 mm draft over hull mass | 4.56 |
| [D2] | Hull mass at which the five-person load would be 6 times hull mass | 62.5 kg |
| [D1] | Six persons over hull mass (but 177 mm draft) | 5.12 |

## 10. Cost

[C1] Value-engineering target: USD 1,500. Estimated cost of the constructable design: USD 1,961 (USD 461 over the target), from `bom/bom.csv`. The decisions added USD 39: okoume plywood (USD 40 more across the five sheet lines), one more foam sheet for the wider benches (USD 55) and the two stern quarter modules (USD 30), less softwood framing (USD 41), glass (USD 21) and epoxy (USD 25). The largest lines are the foam (USD 385), the 6 mm okoume (USD 270 for three sheets), the epoxy (USD 175) and the fittings (handles USD 100, step USD 75).

## 11. Results against the requirements

*Table 10. Results against LSK-REQ-001 (version 0.3).*

| ID | Result | Status |
| --- | --- | --- |
| R1 | Hull 87.9 kg; halves 49.9 and 38.1 kg | Not met (accepted with decision 30A) |
| R2 | 375 kg five-person rated load is 4.3 times hull mass; 401 kg within 150 mm draft (4.6) | Met as restated (ratio reported) |
| R3 | 148 mm at the transom, 138 mm at the forward end of the waterline (five persons) | Met on paper |
| R4 | 1,197 mm over the rub strakes | Met (3 mm margin) |
| R5 | Afloat, 0.4 deg trim, 161 mm freeboard at the transom; 216 mm with the aft-crew rule | Met on paper |
| R6 | 3.3 deg over the stern step | Met on paper |
| R7 | About 6 min, one spanner | Met on paper (estimate) |
| R8 | Three build paths with mass and payload | Met on paper |
| R9 | USD 1,961 | Over the value-engineering target by USD 461 |
| R10 | No fin drive in the first prototype (decision 32A) | Not shown on paper |
