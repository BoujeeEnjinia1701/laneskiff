---
doc_id: LSK-DDR-002
title: LaneSkiff design for construction
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
  change: Design made constructable; changes C1 to C13 and assumptions A1 to A6 decided under Amish's 2026-10-03 pre-approvals
---

# 0002: Design for construction

- **Date:** 2026-10-03
- **Status:** decided. Decided by Amish under his pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and, for this batch, "Proceed with the remaining 15 scaffolds".

## Context

STANDARDS section 18 asks that every part can be made by a stated process and fits and fastens to its neighbours. The concept named a hull "in two rigid halves that bolt together at a mid bulkhead", "closed buoyancy blocks under the side benches", "a hinged buoyant step" and handles, strakes and skids, but did not say how the panels join, what the bolts clamp, what holds the foam down when it lifts, or what stops the step. The constructability review of the model (`cad/src/model.py --check`, 73 checks: no overlap between any two parts; every part touching the part it is fixed to; every joint bolt through both ring frames and both bulkheads and clear of benches and stringers; rail bolts and bow eye through what they clamp; nothing but bolts and pins crossing the joint plane; the step float clear of the rail and transom at its 20 degree stop and when folded up; beam within 1.2 m) led to the changes below. All 73 checks pass. None changes what the product does, its pitch or its safety case.

## Changes

*Table 1. Changes made for construction.*

| # | The concept had | The constructable design has | Why |
| --- | --- | --- | --- |
| C1 | A hull massing shape | Stitch-and-glue panels: three bottom panels (aft, forward flat, bow rake) butting the inside of four flat side panels; transoms and bulkheads sitting on the bottom between the sides; epoxy fillets and glass tape on every seam | Every panel is flat and cut from a standard sheet; the bow rake is a separate panel joined at a knuckle |
| C2 | One mid bulkhead | Two 6 mm bulkheads, one closing each half, each with a hardwood ring frame 20 x 45 | Each half floats alone; the joint needs no seal; the frames give the bolts something to clamp |
| C3 | Bolts at the joint | Eight M10 x 80 stainless bolts from the forward side into nut plates (40 x 40 x 3 steel with a welded nut) screwed to the aft frame; two 12 mm alignment pins | One spanner joins the halves (R7); the plate spreads the load into the hardwood (factor 5 in the kerb case) |
| C4 | Buoyancy blocks under side benches | Foam modules in sewn tarpaulin covers (the LevelHull module), outboard from 330 mm off the centreline to the side, top touching the inwale; held by the inwale and by webbing straps screwed to the inwale and to a hardwood bench rail on the floor | Plywood bench boxes would have added about 9 kg; the inwale and straps carry the swamped lift; the cover protects the foam |
| C5 | Buoyancy in the bow | A bow box: 6 mm wall at 3.0 m, 6 mm deck, foam layers cut to the rake | Puts foam forward and high; the deck is a dry place for the bow line |
| C6 | A flat floor | Three hardwood stringers 40 x 20 per half (centreline and 150 mm each side), bench rails, and a knuckle floor across the boat | Largest floor span 160 mm (factor 1.5 on a foot load); the skids screw into the side stringers; the knuckle floor joins the two bottom slopes |
| C7 | Sheer edge | Hardwood inwales 20 x 40 inside the top of each side, frame to frame | Stiffen the sheer; carry the handle bolts, the strake screws and the bench module tops |
| C8 | A hinged buoyant step | Hardwood hinge rail 40 x 60 on the transom, bolted through a backing block with four M8 bolts; a float 450 x 600 x 90 (hardwood rim, plywood decks, foam core); two strap hinges across a 40 mm gap; stop straps to transom pad eyes at 20 deg below level; kick rung 270 mm below on webbing | The float swings without trapping fingers or feet (checked at the stop and folded up); the straps take the kneeling load (factor 4.2) |
| C9 | Stern transom and bulkheads (thickness not set) | Transom 9 mm with a ring frame; bulkheads 6 mm with ring frames; bow transom 9 mm | The frames carry the loads; thinner plywood saves mass |
| C10 | Rub strakes and skids | HDPE strakes 12 x 30 screwed through the side into the inwale; HDPE skids 40 x 8 screwed into the side stringers, the forward pair bent over the knuckle | Every screw lands in hardwood, never in 6 mm plywood alone |
| C11 | Carry handles and yoke points | Eight bought grab handles bolted through the inwales, two at each end of each half; padded shoulder slings clip to them; transom grab handles bolted through the transom ring frame | Each half has its own four handles; no separate yoke fittings |
| C12 | Push pole | Two 1.5 m aluminium sections with a sleeve, stowed on the aft floor between the stringers; paddles on the aft bench tops | Nothing stowed crosses the joint |
| C13 | Bow line point | Stainless U-bolt through the bow transom and a hardwood pad, nuts inside, fitted before the bow foam | Tow and doorway line; the pad spreads the load |

## Assumptions

*Table 2. Assumptions decided with the changes.*

| # | Assumption | What would change it |
| --- | --- | --- |
| A1 | Marine plywood about 600 kg/m3, hardwood about 700 kg/m3 | Weighing the sheets and timber bought; lighter stock lowers the hull mass (see the R1 options) |
| A2 | Closed-cell polyethylene foam 30 kg/m3, under 1 % water uptake by volume | Supplier data sheet, then 30 days immersion of samples |
| A3 | Persons count at two thirds of their weight when swamped (conservative) | The ABYC H-8 procedure swamp test |
| A4 | Hinges, webbing and nut plates at the strengths in LSK-CAL-001, table 1 | Proof load of the step and joint before trials (CalRig) |
| A5 | The 40 mm hinge gap is wide enough to keep fingers and feet clear | A pinch check with test fingers and a boot at TRL 4; never narrowed without it |
| A6 | Epoxy and glass at the rates in LSK-CAL-001, A5 | Weighing the first half after glassing |

## Consequences

- The hull is 100 kg as built (LSK-CAL-001). The changes added hardwood and fixings that the massing model did not have, and removed about 9 kg by using covered foam modules in place of plywood bench boxes.
- Requirements not met or at risk (R1, R2, R3, R5, R10) are set out for Amish in `docs/REVIEW.md`; nothing in this record decides them.
- STEP and STL files, the general arrangement (LSK-DWG-001, Rev P2), the making sketches (LSK-DWG-101 to 114), the concept media and the build plan (LSK-BLD-001) are generated from the changed model.

## Safety

> **Safety:** C3, C8 and C13 carry people's weight or a tow; each is proof-loaded to twice its working load before trials (LSK-BLD-001, safety stops). C8's 40 mm gap and 20 degree stop are conservative; they are kept until a pinch check and boarding trials show a closer gap is safe.
