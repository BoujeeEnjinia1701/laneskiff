---
doc_id: LSK-DEC-001
title: LaneSkiff design decisions register
project: LaneSkiff
doc_type: Design decisions register
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened; design choices decided under Amish's 2026-10-03 pre-approvals; requirements not met or at risk proposed for Amish's decision
---

# LaneSkiff design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or, for the open items, in `docs/REVIEW.md` (TRL 3 section, Decisions for Amish); this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several entries set safety limits: the step gap and stop, proof loads before trials, the swamped margin at the transom, and the rating of the boat. Each decided item takes the conservative option and names the evidence that would relax it. The rating and the swamped margin are open and stay at the conservative reading (no people carried beyond what trials show safe) until Amish decides.

## Open decisions

Requirements not met or at risk on paper are not decided under the pre-approval (Amish, 2026-10-03: "A simple statement doesn't add value - ensure you are identifying a state and posing it as a clear recommendation for me to decide on."). The state, options and estimates are in `docs/REVIEW.md`.

*Table 1. Open decisions, each Proposed, awaiting Amish.*

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | R1 carry mass: hull 100 kg, halves 56 and 45 kg | A: light timber specification (about 83 kg); B: keep the specification, carry halves with four people or slings; C: shorter 3.0 m hull | **A**, with the slings | Plywood and timber species, side thickness, floor glass | LSK-CAL-001, sections 2 and 9; `docs/REVIEW.md` |
| 2 | R2 payload ratio: 4.5 at six persons | A: light specification (5.45); B: accept 4.5 at six persons; C: rate for fewer persons (ratio falls further) | **A** | As item 1 | LSK-CAL-001, sections 3 and 9 |
| 3 | R3 draft: 187 mm at six persons | A: light specification and a five-person rating (154 mm); B: as A with a 60 mm wider bottom (about 145 mm); C: keep six persons at 187 mm | **B** | Bottom panel width, transom and bulkhead widths, rating plate | LSK-CAL-001, sections 3 and 9 |
| 4 | R5 swamped margin: 36 mm at the transom, 2.1 deg trim | A: 30 L of foam in the stern quarters (about 113 mm); B: operating rule, aft crew moves amidships when swamped (109 mm); C: both | **C** | Two quarter foam modules either side of the step opening | LSK-CAL-001, sections 4 and 9 |
| 5 | R10 fin drive: not designed | A: leave it out of the first prototype; B: clamp-on bracket for a bought pedal fin drive; C: an open fixed forward-only fin drive as a separate project | **A** | Nothing in the first prototype | LSK-PRC-001; `docs/REVIEW.md` |

## To confirm when parts are bought

These are facts that can only be settled with real parts or the first partner. None changes a decision; each may change a size or a limit.

*Table 2. Items to confirm.*

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Density of the plywood and hardwood actually available (600 and 700 kg/m3 assumed) | Hull mass (R1, R2) and draft (R3) | LSK-DDR-002, A1 |
| 2 | Foam density about 30 kg/m3 and water uptake under 1 % by volume on the supplier's data sheet; then 30 days immersion of samples | Swamped freeboard (R5) | LSK-DDR-002, A2 |
| 3 | Strap hinge pin strength (4 kN each assumed); webbing breaking strength (8 kN assumed) | Step factors 1.5 and 4.2 | LSK-CAL-001, table 1 |
| 4 | Nut plate weld quality and the M10 bolt grade (A4-70) | Joint factor in the kerb case | LSK-DDR-002, C3 |
| 5 | Mass of the epoxy, glass and coating as applied (weigh the first half after glassing) | 13.6 kg assumed | LSK-DDR-002, A6 |
| 6 | Price of polyethylene foam and marine plywood near the first partner | Foam and plywood are about a third of the cost | `bom/bom.csv`, lines 1 to 5 and 10 |
| 7 | Body mass of the partner's crews and of the people they rescue (75 kg assumed) | Rated load and draft | LSK-CAL-001, A6 |

## Value engineering

Value-engineering target: USD 1,500 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 1,922 (USD 422 over the target). Main cost drivers and savings worth trying:

- The largest lines are the foam (USD 330), the epoxy (USD 200), the 6 mm plywood (USD 280 for four sheets), the carry and grab handles (USD 100) and the stern step hardware (USD 75).
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
| 2026-10-03 | Appearance model departures: orange painted topsides and light grey inside, a wet concrete lane slab and a 1.75 m mannequin on the far side of the boat, kick rung left out of the hero (rolled up on land), and a cut-back stern for the detail view, drawn for the renders only | Amish, same pre-approvals | `docs/REVIEW.md`, TRL 3 section |
