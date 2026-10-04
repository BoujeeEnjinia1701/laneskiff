---
doc_id: LSK-DEC-001
title: LaneSkiff design decisions register
project: LaneSkiff
doc_type: Design decisions register
version: "0.3"
status: Draft
date: '2026-10-04'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened; design choices decided under Amish's 2026-10-03 pre-approvals; requirements not met or at risk proposed for Amish's decision
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Open items 1 to 5 decided by Amish (30A, 31C, 32A; LSK-DDR-003) and moved to Decisions made; new open item on R2 after the five-person rating; items to confirm for okoume and softwood; cost updated
- version: "0.3"
  date: '2026-10-04'
  author: Amish Chadha
  change: "Open item 1 (R2) decided by Amish (round-3 decision 6A, LSK-DDR-004) and moved to Decisions made; no open decisions"
---

# LaneSkiff design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or, for the open items, in `docs/REVIEW.md` (TRL 3 section, Decisions for Amish); this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several entries set safety limits: the step gap and stop, proof loads before trials, the swamped margin at the transom, and the rating of the boat. Each decided item takes the conservative option and names the evidence that would relax it. Amish set the rating at five persons and chose stern quarter foam with the aft-crew rule for the swamped margin (LSK-DDR-003).

## Open decisions

None. Items 1 to 5 of version 0.1 were decided on 2026-10-03 and the R2 question (open item 1 of version 0.2) on 2026-10-04; all are under Decisions made.

## To confirm when parts are bought

These are facts that can only be settled with real parts or the first partner. None changes a decision; each may change a size or a limit.

*Table 2. Items to confirm.*

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Density of the okoume plywood and softwood actually available (450 and 500 kg/m3 assumed) | Hull mass (R1, R2) and draft (R3, 2 mm margin) | LSK-DDR-003 |
| 2 | Foam density about 30 kg/m3 and water uptake under 1 % by volume on the supplier's data sheet; then 30 days immersion of samples | Swamped freeboard (R5) | LSK-DDR-002, A2 |
| 3 | Strap hinge pin strength (4 kN each assumed); webbing breaking strength (8 kN assumed) | Step factors 1.5 and 4.2 | LSK-CAL-001, table 1 |
| 4 | Nut plate weld quality and the M10 bolt grade (A4-70) | Joint factor in the kerb case | LSK-DDR-002, C3 |
| 5 | Mass of the epoxy, glass and coating as applied (weigh the first half after glassing) | 13.6 kg assumed | LSK-DDR-002, A6 |
| 6 | Price of polyethylene foam and marine plywood near the first partner | Foam and plywood are about a third of the cost | `bom/bom.csv`, lines 1 to 5 and 10 |
| 7 | Body mass of the partner's crews and of the people they rescue (75 kg assumed) | Rated load and draft (R3 met by 2 mm at five persons) | LSK-CAL-001, A6 |
| 8 | Bending strength of the okoume plywood bought (40 MPa assumed), and floor wear with no glass inside | Floor factor 1.5 under a foot load | LSK-CAL-001, A9 and section 6 |
| 9 | Screw holding of the skid and strake screws in softwood stringers and inwales; nut plate bearing on the softwood joint frame (10 MPa assumed) | Skid and strake security; joint factor 5.9 | LSK-DDR-003 |
| 10 | Beam over the rub strakes as built (1,197 mm drawn, 1,200 mm limit) | R4, 3 mm margin | LSK-CAL-001, section 11 |

## Value engineering

Value-engineering target: USD 1,500 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 1,961 (USD 461 over the target). Main cost drivers and savings worth trying:

- The largest lines are the foam (USD 385), the 6 mm okoume (USD 270 for three sheets), the epoxy (USD 175), the carry and grab handles (USD 100) and the stern step hardware (USD 75).
- Line 9 still prices two sheets of 4 mm plywood for bench boxes (USD 110), which LSK-DDR-002 replaced with tarpaulin covers and straps; repricing it as covers and straps (perhaps USD 60) is worth doing at the next BOM review.
- Savings worth trying: foam by the block from a fishing-float maker, cut locally (perhaps USD 100); rope or webbing carry loops in place of bought handles (about USD 80); local hardwood offcuts for the frames, rails and step rim (about USD 40); polyurethane-varnish coating on the inside faces in place of a second epoxy coat (about USD 50).
- A boatyard building a batch shares the stitching, fillet and glassing set-up across boats, which is where most of the labour goes.

## Decisions made

*Table 3. Decisions made.*

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | TRL 2 review items D1 to D10: punt form 3.6 x 1.0 m bottom with bow rake and 8 deg flared sides; two closed halves; plywood and epoxy first, aluminium and HDPE paths at concept level; LevelHull buoyancy layout with no lift from timber and persons at two thirds when swamped; floating stern step with kick rung and transom handholds; calculations at six persons (450 kg); shoulder slings in place of yoke fittings; two-section pole; first co-design candidates (a Malappuram fishers' rescue group with a local boatyard, north Bihar boat makers, a state disaster response unit; none approached yet); targets unchanged; pitch, problem, design-arounds and budget unchanged | Amish, pre-approvals of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds" | LSK-DDR-001 |
| 2026-10-03 | Design for construction, changes C1 to C13: stitch-and-glue panels with a bow knuckle; two bulkheads with ring frames; eight M10 bolts into welded nut plates and two pins; covered foam bench modules held by inwale, straps and bench rails; bow box; three stringers per half and a knuckle floor; inwales; hinge rail, float, strap hinges, 40 mm gap, stop straps and kick rung; 9 mm transom, 6 mm bulkheads; HDPE strakes and skids screwed into hardwood; handles and slings; two-section pole; bow U-bolt with pad | Amish, same pre-approvals | LSK-DDR-002 |
| 2026-10-03 | Assumptions A1 to A6: timber densities, foam data, persons at two thirds when swamped, fitting strengths, hinge gap, epoxy and glass rates | Amish, same pre-approvals | LSK-DDR-002 |
| 2026-10-03 | Step hinge gap 40 mm and stop at 20 deg below level (conservative; narrowed only after a pinch check with test fingers and a boot) | Amish, same pre-approvals | LSK-DDR-001, D5 |
| 2026-10-03 | No person carried before the step, stop straps, handles, bow eye and joint are proof-loaded to twice their working load, and no boarding or swamp trial except in calm, shallow water with a safety boat and every person in a life jacket (a gate, not relaxed) | Amish, same pre-approvals | LSK-BLD-001, sections 5 and 6 |
| 2026-10-03 | R1, R2 and R3 (decision 30A): light timber specification (okoume plywood, 4 mm sides, softwood framing, no glass inside the floor), a five-person rating (375 kg) and a bottom 60 mm wider; halves carried with the shoulder slings | Amish, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." | LSK-DDR-003 |
| 2026-10-03 | R5 (decision 31C): 30 L of foam in the stern quarters (two 15 L modules either side of the step opening) and the aft-crew rule | Amish, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." | LSK-DDR-003 |
| 2026-10-03 | R10 (decision 32A): no fin drive in the first prototype; an open fixed forward-only drive kept as a later portfolio idea | Amish, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." | LSK-DDR-003 |
| 2026-10-03 | Appearance model departures: orange painted topsides and light grey inside, a wet concrete lane slab and a 1.75 m mannequin on the far side of the boat, kick rung left out of the hero (rolled up on land), and a cut-back stern for the detail view, drawn for the renders only | Amish, same pre-approvals | `docs/REVIEW.md`, TRL 3 section |
| 2026-10-04 | R2 (6A): restated as "payload 375 kg (five persons) within the R3 draft limit; the payload-to-hull ratio is reported"; met at 375 kg and 148 mm draft, ratio 4.3 reported | Amish: "For round 3, I agree with all your proposed recommendations" | LSK-DDR-004 |
