---
doc_id: LSK-DDR-003
title: LaneSkiff requirement decisions, round 2
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
  change: Five requirement decisions (R1, R2, R3, R5, R10) decided by Amish on 2026-10-03 as recommended, and carried into the design
---

# 0003: Requirement decisions, round 2

- **Date:** 2026-10-03
- **Status:** Decided
- **Decided by:** Amish Chadha, 2026-10-03

## Context

The TRL 3 review (`docs/REVIEW.md`, Session 2026-10-03: TRL 3, Decisions for Amish) posed five requirements that were not met, at risk or not shown on paper as decisions for Amish, each with its state, options and a recommendation: R1 carry mass, R2 payload ratio, R3 draft at rated load, R5 swamped margin at the transom and R10 the optional fin drive. On 2026-10-03 Amish wrote: "i approve all of the 47 recommendations provided by you. Execute them." Each of the five is therefore decided as its recommendation, exactly as worded, and carried into the design at TRL 3 scope only: model, calculations, bill of materials, drawings, build plan and documents. Nothing here is built or tested; the conditions below are checked at TRL 4.

The decisions are linked. R1 A (the light timber specification, with the slings) also settles R2 A, and R3 B takes the same light specification with a five-person rating and a bottom 60 mm wider. The five-person rating changes every result that depends on the rated load or the swamped buoyancy, so all of them were recomputed in LSK-CAL-001 v0.2 on the decided design together, not added option by option.

> **Safety:** Decision 4 (R5) is a safety item. The operating rule that the aft crew member moves amidships when the boat is swamped is printed on a capacity plate on the inside of the transom (BOM line 30) with the five-person rating, and is in the README operating notes and the build plan safety stops. The stern quarter foam gives margin even if the rule is not followed.

## Options considered

The options for each decision are set out in full in `docs/REVIEW.md` (Session 2026-10-03: TRL 3, Decisions for Amish). Table 1 lists the option chosen.

## Decision

*Table 1. Decisions of 2026-10-03, with their effect on the decided design (LSK-CAL-001 v0.2, paper estimates).*

| # | Requirement | Option chosen | Effect | Condition |
| --- | --- | --- | --- | --- |
| 1 | R1, carry mass | A, with the slings: light timber specification (okoume plywood about 450 kg/m3, 4 mm sides, softwood framing about 500 kg/m3, no glass inside the floor), each half carried by two people with the shoulder slings | Hull 88.0 kg (100.2 kg before), halves 49.9 and 38.1 kg; 25.0 and 19.0 kg for each of two carriers per half. The light specification saves about 18 kg as estimated; the wider bottom of decision 3 and the extra foam of decision 4 put back about 6 kg. R1 (50 kg) still not met | Okoume and softwood at the assumed densities near the first partner; less abrasion margin on the floor; floor bending factor 1.5 assumes 40 MPa plywood; joint nut plates now bear on softwood (factor 3.5, estimate) |
| 2 | R2, payload ratio | A, taken together with R1 A | With the five-person rating of decision 3 the ratio is 375 / 88.0 = 4.26 (4.49 before). The option's 5.45 assumed six persons on an 83 kg hull; at six persons this hull would give 5.11 but a 177 mm draft. R2 not met, and further from the target than before | A new question is posed: no rating meets R2 and R3 together on this hull |
| 3 | R3, draft at rated load | B: light specification and a five-person rating (375 kg), with the bottom 60 mm wider (1,060 mm at the chine) | Deepest draft 148 mm at the transom, 138 mm at the forward end of the waterline (187 mm before); beam 1,197 mm over the rub strakes, R4 still met; transverse GM at rated load 0.31 m (0.15 m before). R3 met on paper with a 2 mm margin | The five-person rating goes on the capacity plate; crew and passenger masses near 75 kg (to confirm with the partner) |
| 4 | R5, swamped margin at the transom (safety) | C: two 15 L covered stern quarter foam modules, and the operating rule that the aft crew member moves amidships when swamped | With five persons, quarter foam and nobody moving: trim 0.45 deg stern down, transom freeboard 160 mm. With the rule as well: 215 mm. For comparison, without either (five persons, lighter hull) 115 mm; before the decisions 36 mm. Two people moving to one side swamped leave 38 mm at the low gunwale (it dipped before). R5 met on paper | The rule is printed on the capacity plate and taught to crews; the modules are strapped so they cannot lift off when swamped |
| 5 | R10, optional fin drive | A, with C kept as a later idea for the portfolio | No fin drive in the first prototype; no cost or mass. R10 stays not shown on paper. An open fixed forward-only fin drive after the expired US6022249 is recorded as a separate, later portfolio idea, not started | None for this prototype |

Placement of the stern quarter modules. The TRL 3 review described the modules as "high in the stern quarters, either side of the step opening". The outboard stern quarters are already filled by the aft bench modules, so each module stands inboard of its bench module at the transom end, from the side stringer and bench rail up to the bench top (209 x 226 x 334 mm outside, 15 L of foam), 40 mm forward of the transom to clear the hinge rail bolt nuts, held by two webbing straps from the floor over the module and the bench top to the inwale. Standing on the stringer it is submerged over most of its height when swamped, so it gives more lift than a module placed high would; the standing crew member's place 400 mm forward of the transom stays clear.

## Consequences

- `cad/src/model.py`: bottom half width 500 to 530 mm, side panels 6 to 4 mm, two stern quarter modules (cover, foam, straps). All 80 constructability checks pass (73 before; seven new contact checks for the modules). STEP and STL re-exported.
- `docs/04-calcs/sizing.py`, `01-sizing.md` (LSK-CAL-001 v0.2) and `results.csv`: okoume, softwood and no inside glass; five persons; swamped cases with and without the rule and the quarter foam; nut plate bearing on softwood.
- `bom/bom.csv`: plywood lines 1 to 5 as okoume (priced at about 1.4 times the plywood before, an estimate), framing lines 6 to 8 as softwood, line 10 seven foam sheets, line 23 glass outside only, new line 29 (stern quarter module covers and straps) and line 30 (capacity plate). Estimated cost USD 2,098 (USD 1,922 before), USD 598 over the value-engineering target; `budget_usd` stays at 1,500.
- `LSK-DWG-001` Rev P3; `LSK-DWG-101` to `110` Rev P2; build plan pictures, concept media and `media/model.glb` regenerated.
- `docs/03-requirements.md` v0.3 (rated load five persons; targets unchanged), `docs/02-concept.md` v0.3, `docs/05-build-plan.md` v0.2, `README.md` (with operating notes).
- New questions raised by these decisions are posed in `docs/REVIEW.md` and the design decisions register.
