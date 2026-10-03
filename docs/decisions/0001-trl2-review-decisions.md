---
doc_id: LSK-DDR-001
title: LaneSkiff TRL 2 review decisions
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
  change: TRL 2 review items decided under Amish's 2026-10-03 pre-approvals
---

# 0001: TRL 2 review decisions

- **Date:** 2026-10-03
- **Status:** decided. Decided by Amish under his pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and, for this batch, "Proceed with the remaining 15 scaffolds".
- **Not decided here:** requirements that are not met or at risk on paper (R1, R2, R3, R5, R10). Those are set out with options for Amish in `docs/REVIEW.md` and listed as open decisions in LSK-DEC-001.

## Context

The scaffold (LSK-PRB-001, LSK-PRC-001 and LSK-REQ-001, all v0.1) described a flat-bottomed skiff of about 3.5 by 1.2 m in two rigid halves bolted at a mid bulkhead, with buoyancy under side benches and at the ends, a hinged buoyant step at the stern centre, carry handles and yoke points, rub strakes and skids, an optional fin drive and a material substitution table. It left five open questions: the build material, the step depth and folding, level flotation inside the weight budget, the fin drive, and the trial partner. Populating the concept to TRL 2 meant settling the concept choices below. Items that touch safety take the conservative option and say what evidence would relax it. Partners and regions are the first candidates to approach, not agreements.

## Options considered

*Table 1. Options.*

| # | Item | Options |
| --- | --- | --- |
| D1 | Hull form | (a) jon boat with a narrow bow transom; (b) punt form, constant width, flat bottom raked at the bow, flat flared sides; (c) round-bilge skiff |
| D2 | The split | (a) one mid bulkhead shared by both halves; (b) each half closed by its own bulkhead, bolted face to face |
| D3 | First build path | (a) plywood and epoxy, stitch and glue; (b) aluminium sheet; (c) HDPE sheet |
| D4 | Buoyancy layout and accounting | (a) foam low under the floor; (b) LevelHull layout: outboard along the sides and in a bow box, no lift credited to the timber, persons at two thirds when swamped |
| D5 | Boarding step | (a) rigid ladder; (b) floating step on a hinge, kick rung below, transom handholds |
| D6 | Load case for the calculations | (a) 300 kg; (b) six persons, a crew of two and four adults, 450 kg |
| D7 | Shoulder yoke points | (a) separate yoke fittings; (b) padded slings clipped to the carry handles |
| D8 | Propulsion stowage | (a) one-piece 3 m pole; (b) two 1.5 m sections that stow inside a half |
| D9 | Co-design candidates | First candidates to approach |
| D10 | Requirement targets | (a) revise; (b) keep the TRL 1 targets unchanged and report against them |

## Decisions

- **D1: (b) punt form.** Constant width gives the widest waterline for a lane-width beam and the lowest draft, and every panel is flat. Bottom 1.0 m wide at the chine, flat for 2.7 m, raked to 200 mm at the bow; sides 400 mm, flared 8 degrees; 3.6 m long.
- **D2: (b) two closed halves.** Each half floats on its own and the joint carries load but needs no seal; it keeps the bolt-together design-around clear of folding or flexible hulls.
- **D3: (a) plywood and epoxy** for the first prototype; aluminium and HDPE paths documented at concept level in the material substitution table (meets the intent of R8 on paper).
- **D4: (b) LevelHull layout,** with conservative accounting: plywood and timber give no lift when submerged; people count at two thirds of their weight when swamped. Relaxed only by an ABYC H-8 procedure swamp test.
- **D5: (b) floating step** after the expired US6932020B2 form: a buoyant float hinged to a rail on the transom, a kick rung 270 mm below it on webbing, two transom grab handles. Conservative safety choices: a 40 mm gap between float and rail so nothing can be trapped through the swing, stop straps at 20 degrees below level, and a proof load to twice the working load before any boarding trial. A smaller gap would need a pinch test with a test finger to justify it.
- **D6: (b) six persons, 450 kg,** for the calculations, reading "four adults plus crew" literally. The rating of the first prototype is part of the R3 decision for Amish.
- **D7: (b) padded slings** clipped to the two carry handles at one end of a half; no separate yoke fittings.
- **D8: (b) two 1.5 m sections** joined by an internal sleeve.
- **D9: first candidates to approach,** none approached yet: a fishers' volunteer rescue group in Malappuram district, Kerala, with a nearby plywood-and-epoxy boatyard; country boat makers in a flood-prone district of north Bihar; a state disaster response force or civil defence training unit for trials.
- **D10: (b) targets unchanged.** Requirements not met are reported and put to Amish with options; the cost requirement is reported against the value-engineering target (STANDARDS section 18).
- Pitch, problem, design-arounds and `budget_usd` unchanged.

## Consequences

- The constructable design (LSK-DDR-002) follows from D1 to D8.
- With D3 and D4 the hull comes out at 100 kg, which leaves R1 and R2 unmet; with D6 the draft misses R3. These are for Amish.

## Safety

> **Safety:** D4 and D5 are safety choices and take the conservative option. Flotation and a stable step do not make flood rescue safe: life jackets, training, a safety boat for trials, and no moving water remain the rules in every document.
