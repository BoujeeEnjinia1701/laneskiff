---
doc_id: LSK-DEC-001
title: LaneSkiff design decisions register
project: LaneSkiff
doc_type: Design decisions register
version: "0.2"
status: Draft
date: '2026-10-03'
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
  change: The five requirement decisions decided by Amish as recommended (LSK-DDR-003) and moved to decisions made; two new questions proposed, awaiting Amish; items to confirm and value engineering updated
---

# LaneSkiff design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or, for the open items, in `docs/REVIEW.md` (TRL 3 section, Decisions for Amish); this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several entries set safety limits: the step gap and stop, proof loads before trials, the swamped margin at the transom, and the rating of the boat. Each decided item takes the conservative option and names the evidence that would relax it. The five-person rating and the swamped operating rule are on the capacity plate (LSK-DDR-003); both are paper values until the TRL 4 load and swamp tests.

## Open decisions

The five requirement decisions of the TRL 3 review were decided by Amish on 2026-10-03 (LSK-DDR-003) and are listed under Decisions made. Carrying them into the design raised the two questions below; the state, options and estimates are in `docs/REVIEW.md`, Session 2026-10-03: round 2 requirement decisions applied.

*Table 1. Open decisions, each Proposed, awaiting Amish.*

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| 6 | R2 payload against R3 draft: at five persons the ratio is 4.26; R2 would need 528 kg aboard, R3 allows about 401 kg, so no rating meets both | A: restate R2 as an absolute payload, five persons (375 kg) within the R3 draft, with the ratio reported; B: restate R2 as a ratio of at least 4; C: keep six times hull mass and record R2 as not met | **A** | Requirements only; no change to the boat | LSK-CAL-001 v0.2, sections 3 and 9; `docs/REVIEW.md` |
| 7 | Floor and side strength with the light specification: okoume floor with no inside glass, 4 mm sides, not checked against knocks | A: keep the decided specification and test sample panels at TRL 4 (foot load on the floor, a knock on a 4 mm side panel) before the hull is built; B: put 200 g/m2 glass back inside the floor (about 1.5 kg and USD 30 with its resin, estimate); C: 6 mm sides on the aft half only | **A** | Floor glass and side thickness only if a test fails | LSK-CAL-001 v0.2, section 6; `docs/REVIEW.md` |

## To confirm when parts are bought

These are facts that can only be settled with real parts or the first partner. None changes a decision; each may change a size or a limit.

*Table 2. Items to confirm.*

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Density of the okoume plywood and softwood actually available (450 and 500 kg/m3 assumed), and of the hardwood for the step and pad (700 kg/m3) | Hull mass (R1, R2) and draft (R3, 2 mm margin) | LSK-DDR-003 |
| 2 | Foam density about 30 kg/m3 and water uptake under 1 % by volume on the supplier's data sheet; then 30 days immersion of samples | Swamped freeboard (R5) | LSK-DDR-002, A2 |
| 3 | Strap hinge pin strength (4 kN each assumed); webbing breaking strength (8 kN assumed) | Step factors 1.5 and 4.2 | LSK-CAL-001, table 1 |
| 4 | Nut plate weld quality, the M10 bolt grade (A4-70) and the bearing strength of the softwood ring frames (6 MPa assumed) | Joint factor in the kerb case (3.5 on the nut plate bearing) | LSK-DDR-002, C3; LSK-DDR-003 |
| 5 | Mass of the epoxy, glass and coating as applied (weigh the first half after glassing) | 13.6 kg assumed | LSK-DDR-002, A6 |
| 6 | Price of polyethylene foam and of okoume plywood near the first partner (okoume priced at about 1.4 times local marine plywood) | Foam and plywood are about half of the cost | `bom/bom.csv`, lines 1 to 5 and 10 |
| 7 | Body mass of the partner's crews and of the people they rescue (75 kg assumed) | Rated load and draft (148 mm at five persons, 2 mm inside R3) | LSK-CAL-001, A6 |
| 8 | Bending strength of the okoume bought (40 MPa assumed for the floor) | Floor factor 1.5 with no glass inside | LSK-CAL-001 v0.2, section 6 |
| 9 | Wording of the capacity plate with the first partner's crews, in their language | The swamped rule only works if the crew reads and follows it | LSK-DDR-003, item 4 |

## Value engineering

Value-engineering target: USD 1,500 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 2,098 (USD 598 over the target; USD 1,922 before LSK-DDR-003). Main cost drivers and savings worth trying:

- The largest lines are the okoume plywood (USD 624 for lines 1 to 5), the foam (USD 385), the epoxy (USD 200), the carry and grab handles (USD 100) and the stern step hardware (USD 75). The light specification adds about USD 96 net (okoume dearer, softwood and less glass cheaper), the extra foam USD 55, and the quarter module covers and capacity plate USD 24 (estimates).
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
| 2026-10-03 | R1: light timber specification (okoume plywood, 4 mm sides, softwood framing, no glass inside the floor), with the shoulder slings (option A) | Amish: "i approve all of the 47 recommendations provided by you. Execute them." | LSK-DDR-003, item 1 |
| 2026-10-03 | R2: light specification, taken together with R1 A (option A); with the five-person rating the ratio is 4.26 | Amish, same approval | LSK-DDR-003, item 2 |
| 2026-10-03 | R3: light specification, five-person rating (375 kg) and the bottom 60 mm wider, beam about 1,197 mm (option B) | Amish, same approval | LSK-DDR-003, item 3 |
| 2026-10-03 | R5 (safety): two 15 L covered stern quarter foam modules and the operating rule that the aft crew member moves amidships when swamped, on the capacity plate (option C) | Amish, same approval | LSK-DDR-003, item 4 |
| 2026-10-03 | R10: no fin drive in the first prototype; an open fixed forward-only fin drive kept as a later portfolio idea (option A, with C) | Amish, same approval | LSK-DDR-003, item 5 |
| 2026-10-03 | Appearance model departures: orange painted topsides and light grey inside, a wet concrete lane slab and a 1.75 m mannequin on the far side of the boat, kick rung left out of the hero (rolled up on land), and a cut-back stern for the detail view, drawn for the renders only | Amish, same pre-approvals | `docs/REVIEW.md`, TRL 3 section |

## Change log

- 2026-10-03 (v0.2): open decisions 1 to 5 decided by Amish as recommended (LSK-DDR-003) and moved to Decisions made; new open decisions 6 and 7 added; items to confirm 1, 4, 6 and 7 updated and 8 and 9 added; value engineering updated.
