# Review note: LaneSkiff

## Session 2026-10-03: round 2 requirement decisions applied

Amish, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." The five LaneSkiff decisions posed in the TRL 3 session below (R1, R2, R3, R5, R10) are therefore decided exactly as recommended and recorded in `docs/decisions/0003-requirement-decisions-round2.md` (LSK-DDR-003). They were carried into the design at TRL 3 scope only; nothing was built, tested or bought. The decisions are linked, and the five-person rating of R3 changes every result that depends on the rated load or the swamped buoyancy, so LSK-CAL-001 was recomputed on the decided design as a whole.

### What changed

| Decision | What changed in the repo |
| --- | --- |
| R1 A, with the slings: light timber specification | `cad/src/model.py` side panels 6 to 4 mm; `sizing.py` okoume plywood 450 kg/m3, softwood framing 500 kg/m3 (ring frames, inwales, stringers, bench rails, knuckle floor), no glass inside the floor, nut plate bearing on softwood; BOM lines 1 to 8 and 23; making sketches `LSK-DWG-101` to `108` Rev P2; build plan sections 1, 3.1 to 3.8 |
| R2 A, with R1 A | No further change; ratio recomputed at the five-person rating (see below) |
| R3 B: light specification, five persons (375 kg), bottom 60 mm wider | `model.py` bottom half width 500 to 530 mm (beam 1,197 mm); `sizing.py` five persons; BOM line 10 (7 foam sheets) and panel sizes; `LSK-DWG-001` Rev P3, `LSK-DWG-109`, `110` Rev P2; requirements definition of rated load; concept and README |
| R5 C (safety): stern quarter foam and the operating rule | `model.py` two covered 15 L modules with straps (seven new contact checks, 80 of 80 checks pass); `sizing.py` swamped cases with and without the rule and the foam; BOM line 29 (covers and straps) and line 30 (capacity plate); capacity plate text in the build plan (section 3.15, step 10 and the safety stops) and in the README Safety and new Operating notes sections |
| R10 A, with C as a later idea | Requirements, concept, README and register: no fin drive in the first prototype; an open fixed forward-only fin drive kept as a later, separate portfolio idea |

Also updated: `docs/04-calcs/01-sizing.md` (LSK-CAL-001 v0.2) and `results.csv`, `docs/03-requirements.md` (v0.3; targets unchanged, only the rated load definition restated as the R3 option says), `docs/02-concept.md` (v0.3), `docs/05-build-plan.md` (v0.2), `docs/06-design-decisions.md` (v0.2), `cad/src/concept_media.py`, `cad/src/product_model.py` (colours for the new parts), `cad/src/build_plan_media.py`, `cad/src/sheets.py`, and `project.yaml` (trl_evidence; estimate in the budget comment). STEP and STL, the GA, all fourteen making sketches, the build plan overview, joints and steps, the concept media (`hero.png`, `exploded.png`, `cutaway.png`, `concept-blueprint`) and `media/model.glb` (linear deflection 1.0, angular 0.35) were regenerated from the model.

### Requirement status

| ID | Before | After |
| --- | --- | --- |
| R1 | Not met: 100.2 kg; halves 55.7 and 44.5 kg | Not met: 88.0 kg; halves 49.9 and 38.1 kg; 25.0 and 19.0 kg each for two carriers per half with the slings |
| R2 | Not met: 4.49 at six persons | Not met: 4.26 at five persons (lower than before; the option's 5.45 assumed six persons) |
| R3 | Not met: 187 mm at six persons | Met on paper: 148 mm at the transom, 138 mm forward, five persons (2 mm margin) |
| R4 | Met: 1,137 mm | Met: 1,197 mm |
| R5 | At risk: 2.1 deg, 36 mm at the transom | Met on paper: 0.45 deg, 160 mm with nobody moving; 215 mm with the rule |
| R6 | Met on paper: 4.3 deg | Met on paper: 3.3 deg |
| R9 | USD 1,922, USD 422 over the target | USD 2,098, USD 598 over the target |
| R10 | Not shown (open) | Not shown on paper, decided: no drive in the first prototype |

R7 and R8 are unchanged and met on paper.

### Cost

Value-engineering target: USD 1,500 (unchanged). Estimated cost of the constructable design: USD 2,098 (USD 1,922 before), USD 598 over the target. The light specification adds about USD 96 net: okoume plywood about USD 144 more (priced at about 1.4 times the local marine plywood of the BOM, an estimate), less USD 27 for softwood framing and USD 21 for the glass no longer inside the floor. One more foam sheet for the wider benches and the quarter modules adds USD 55, the quarter module covers and straps USD 14 (estimate), and the capacity plate USD 10 (estimate). The option estimates were about USD 150 together (USD 100, 20 and 30); the BOM gives USD 175 including the plate. `budget_usd` stays at 1,500 as Amish's value-engineering target; the estimate is updated in its comment.

### New questions, proposed, awaiting Amish

**6. R2 payload against R3 draft.**
State: with the five-person rating the payload ratio is 4.26, lower than the 4.49 before the decisions, because the rating fell from six persons to five while the hull fell only from 100 to 88 kg. R2 (six times hull mass) would need 528 kg aboard; R3 (150 mm) allows about 401 kg. No rating meets both on this hull. The R2 target text also gives "about 300 kg or four adults plus crew", which 375 kg exceeds.

| Option | Effect | Cost or mass |
| --- | --- | --- |
| A: restate R2 as an absolute payload: five persons (375 kg) within the R3 draft, with the ratio reported | R2 met on paper (375 kg at 148 mm) | None |
| B: restate R2 as a ratio of at least 4 | Met on paper (4.26) | None |
| C: keep six times hull mass | R2 not met; would need a hull of about 63 kg at five persons | None now |

**Recommendation: A**: the payload that matters in a lane is how many people the boat carries within its draft, and that is what the capacity plate states.

**7. Floor and side strength with the light specification.**
State: the floor factor of 1.5 assumes 40 MPa plywood bending strength with no glass counted; okoume may be weaker, and the decided specification takes the glass off the inside of the floor. The 4 mm sides have no calculated load case for knocks against walls and kerbs in a lane.

| Option | Effect | Cost or mass |
| --- | --- | --- |
| A: keep the decided specification; test sample panels at TRL 4 (a foot load on a floor panel between stringers, a knock on a 4 mm side panel) before the hull is built | Confirms or rejects the specification early | Test panels only |
| B: put 200 g/m2 glass back inside the floor | Floor stiffer and abrasion margin restored | About 1.5 kg and USD 30 with its resin (estimate) |
| C: 6 mm sides on the aft half only | Stronger sides where people board and carry | About 1.5 kg and USD 10 (estimate) |

**Recommendation: A**: it keeps the decided mass saving and settles the question with a cheap test before any hull is built.

### Safety notes

- The swamped operating rule (stay in the boat, sit low and centred, the aft crew member moves amidships at once) is printed on the capacity plate with the five-person rating, and is in the README operating notes and the build plan safety stops. A new stop: no person is carried until the plate is on the transom and every crew member has read it.
- The quarter foam alone keeps 160 mm at the transom, so the boat stays nearly level swamped even if the rule is not followed; with two people moving to one side the low gunwale stays 38 mm clear (it dipped before).
- The draft at the rated load is only 2 mm inside R3; an extra person or heavier people push it over 150 mm. The plate states the limit in persons and kilograms.
- The quarter modules are strapped down at the floor and the inwale like the bench modules so they cannot float out when swamped; they stand forward of the hinge rail bolts and clear of the poler's place.
- The light specification lowers some margins: the joint nut plates now bear on softwood (factor 3.5, estimate, 5.0 before), the floor has no glass inside, and the 4 mm sides are thinner. Question 7 and the items to confirm cover them.
- Unchanged: life jackets always, never in moving water, proof loads before boarding trials, the first swamp test with ballast in a pool.

### Re-render

The hero geometry changed visibly: the beam grew by 60 mm (1,137 to 1,197 mm), the side panels are thinner and two stern quarter modules now stand inside the stern, visible from above. The photoreal renders made on Amish's Mac (`media/render-hero.png` and the exploded and detail views) need a re-render from `cad/src/product_model.py`; the card and social preview should be remade after.

### Pre-existing inconsistencies noticed (not changed)

- BOM line 3 calls for a 12 mm transom sheet and line 5 calls the bulkhead sheet 9 mm, while the model has a 9 mm transom and 6 mm bulkheads; `BOM_NAMES` in `model.py` repeats this.
- BOM line 9 still lists 4 mm plywood bench boxes, which LSK-DDR-002 replaced with tarpaulin-covered modules.

### Recommended next step

Amish's choices on questions 6 and 7 and a corrected BOM for the two pre-existing inconsistencies; then, when the phase allows TRL 4, the sample panel tests of question 7, the aft half built first, weighed, floated alone, and the step proof-loaded with CalRig before any boarding trial.

## Session 2026-09-30: scaffolded

### What was done

- Repository created from kit 1.6.0 at TRL 1, target TRL 2.
- `docs/01-problem.md` (LSK-PRB-001 v0.1): problem with cited evidence, users, environment, constraints, prior work, open questions.
- `docs/02-concept.md` (LSK-PRC-001 v0.1): how it works, components, patent design-arounds, shared blocks, safety.
- `docs/03-requirements.md` (LSK-REQ-001 v0.1): 10 proposed requirements.
- `README.md` with concept rationale, burning platform, where it could be used, and what sparked the idea.

### Next

- Run `/populate` to bring the repo to a strong TRL 2 with concept media.

## Session 2026-10-03: TRL 2 (populate)

Run as the first half of `/to-trl3` under Amish's pre-approvals of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and "Proceed with the remaining 15 scaffolds". Kit 1.7.0 installed.

### What was done

- `docs/01-problem.md` (LSK-PRB-001 v0.2): constraints restated with the value-engineering target, open questions answered, first co-design candidates, safety section.
- `docs/02-concept.md` (LSK-PRC-001 v0.2): how it works, components with BOM numbers, key design choices, first-order numbers, material substitution table, design-arounds kept, safety.
- `docs/03-requirements.md` (LSK-REQ-001 v0.2): ten requirements, targets unchanged, with TRL 3 status and definitions.
- Concept media from `cad/src/concept_media.py`: `media/hero.png` (1.75 m person for scale), `media/cutaway.png`, `media/exploded.png` (BOM callouts), `media/concept-blueprint.png`, `.pdf` and `.svg` (LSK-DWG-010), `media/model.glb` (1.1 MB, coarse tessellation) and `media/viewer.html`. No flow diagram: the boat carries people but moves no energy or material.
- `bom/bom.csv`: 28 priced lines.

### Results

- Level flotation works with the LevelHull layout (foam outboard and forward); stern-centre boarding heels the boat a quarter as much as boarding over the side.

### Requirements not met

- R1, R2 and R3 are not met and R5 is at risk; R10 is not shown. See the TRL 3 section.

### Decisions made under the pre-approval

LSK-DDR-001, items D1 to D10: punt form; two closed halves; plywood and epoxy first; LevelHull layout with conservative accounting; floating stern step with a 40 mm hinge gap and 20 degree stop; calculations at six persons; slings in place of yoke fittings; two-section pole; first co-design candidates (not approached); targets unchanged.

### Safety concerns

- Flood rescue is hazardous whatever the boat: life jackets, training, no moving water, and a safety boat for every trial.

## Session 2026-10-03: TRL 3 (advance and build plan)

Run as the second half of `/to-trl3` under the same pre-approvals, which count as the TRL 2 approval. Not committed or pushed (batch run).

### What was done

- `cad/src/model.py`: parametric build123d model of both halves, the joint hardware, the stern step and the outfit; 73 of 73 constructability checks pass (no overlaps between any two parts; every part touching the part it is fixed to; joint bolts through both frames and both bulkheads and clear of benches and stringers; rail bolts and bow eye through what they clamp; only bolts and pins cross the joint plane; the step float clear of rail and transom at its 20 degree stop and folded up; beam within 1.2 m). Exports `cad/step/laneskiff-assembly.step`, `laneskiff-aft-half.step`, `laneskiff-forward-half.step`, `laneskiff-stern-step.step`, six panel STEP files, and STL of a ring frame, the knuckle floor and the hinge rail.
- `docs/04-calcs/01-sizing.md` (LSK-CAL-001 v0.1) with `docs/04-calcs/sizing.py` and `results.csv`: masses, hydrostatics, swamped flotation, boarding heel, structure, joining time, build paths, option estimates and cost.
- `cad/src/sheets.py`: general arrangement `cad/drawings/LSK-DWG-001` (SVG, PDF, PNG) at Rev P2 with section A-A at 1:10.
- `cad/src/build_plan_media.py`: `docs/05-build-plan/overview.png`, 14 making sketches `cad/drawings/LSK-DWG-101` to `114`, 8 joint close-ups and 17 step pictures.
- `docs/05-build-plan.md` (LSK-BLD-001 v0.1), `docs/06-design-decisions.md` (LSK-DEC-001 v0.1), `docs/decisions/0001-trl2-review-decisions.md` (LSK-DDR-001) and `docs/decisions/0002-design-for-construction.md` (LSK-DDR-002).
- `cad/src/product_model.py` (appearance model) and render scenes exported with `.kit/export_views.py` to `/home/claude/renders/laneskiff` for hero, exploded and detail views; photoreal renders and cards are made on Amish's Mac.
- `project.yaml`: trl 3, trl_target 3, `design_state: constructable`, evidence listed; `budget_usd` unchanged. README leads with `media/render-hero.png` and has a "Building the prototype" section.

### Results

- Hull 3.60 m long, 1,137 mm over the rub strakes, 400 mm deep; 100 kg as carried (aft half with the step 56 kg, forward half 45 kg); plywood 35 kg, hardwood 22 kg, foam 15 kg, glass and epoxy 14 kg.
- Rated load assessed at six persons (450 kg, 4.5 times hull mass): 175 mm draft on an even keel, 162 mm at the transom and 187 mm at the forward end of the waterline; 87 mm with a crew of two; 361 kg carried within 150 mm of draft.
- Boarding over the stern step: 4.3 deg heel, 270 mm transom freeboard; over the side: 15.6 deg.
- Swamped with the rated persons (at two thirds of their weight): afloat, 2.1 deg stern down, freeboard 36 mm at the transom and 164 mm at the bow; two people moving 400 mm to one side dip the gunwale.
- Joining the halves: about 6 minutes, one spanner (estimate). Factors: floor 1.5, joint bolt 9.0 and nut plate 5.0 in a kerb case, stop strap 4.2, hinge 1.5.
- Build paths: plywood 100 kg, aluminium 98 kg, HDPE 110 kg (screening).
- Value-engineering target: USD 1,500. Estimated cost of the constructable design: USD 1,922 (USD 422 over the target).

### Requirements not met

- R1 not met (100 kg; halves 56 and 45 kg), R2 not met (4.5), R3 not met (187 mm), R5 at risk (36 mm at the transom), R10 not shown. Each is set out below for Amish's decision.
- R9: over the value-engineering target by USD 422; reported against the target (STANDARDS section 18), accepted under the pre-approval, and not put as a budget decision.
- The test half of R2 to R8 is TRL 4 work.

### Decisions for Amish

Each item is Proposed, awaiting Amish, and listed in LSK-DEC-001 as an open decision. Estimates are from LSK-CAL-001, section 9.

**R1, carry mass.**
- *State:* hull 100 kg as carried; aft half 56 kg, forward half 45 kg. Cause: closed-box halves with level-flotation foam (15 kg) and glass and epoxy (14 kg) in 600 kg/m3 plywood and 700 kg/m3 hardwood.
- *Option A, light timber specification:* okoume plywood (about 450 kg/m3), 4 mm sides, softwood framing (about 500 kg/m3), no glass inside the floor. Hull about 83 kg (halves 46 and 37 kg); still not met but 18 kg closer; cost about USD 100 more (okoume dearer); less abrasion margin on the floor.
- *Option B, keep the specification:* hull 100 kg; each half carried by two people with the shoulder slings (about 28 and 23 kg each) or the whole boat by four; no cost or mass change.
- *Option C, shorter hull:* 3.0 m in two 1.5 m halves; about 85 kg (rough estimate), about USD 100 less, rated load falls to about five persons.
- **Recommendation: A**, with the slings: the largest mass saving that keeps the hull form, the rating and the step unchanged.

**R2, payload ratio.**
- *State:* 450 kg rated load is 4.5 times hull mass. Cause: the 100 kg hull (R1).
- *Option A, light timber specification (as R1 A):* ratio about 5.45; cost about USD 100 more; mass 18 kg less.
- *Option B, accept the ratio:* 4.5 at six persons; no cost or mass change.
- **Recommendation: A**, taken together with R1 A.

**R3, draft at rated load.**
- *State:* 187 mm at the forward end of the waterline and 162 mm at the transom with six persons. Cause: a 450 kg load plus a 100 kg hull on a 3.5 x 1.05 m waterline.
- *Option A, light specification and a five-person rating (375 kg):* about 154 mm; cost about USD 100 more; mass 18 kg less.
- *Option B, as A with the bottom 60 mm wider:* about 145 mm; beam about 1,197 mm (R4 still met); a further USD 20 and 3 kg.
- *Option C, keep six persons:* 187 mm; no cost or mass change; the boat needs deeper water to carry a full load.
- **Recommendation: B**: meets R3 on paper with the smallest change to the concept.

**R5, swamped margin at the transom.**
- *State:* afloat with the rated persons, 2.1 deg stern down, 36 mm freeboard at the transom (164 mm at the bow). Cause: the standing crew member, transom and step are aft while the bow box puts foam forward.
- *Option A, stern quarter foam:* two 15 L covered foam modules high in the stern quarters, either side of the step opening; transom freeboard about 113 mm, trim about 0.4 deg; about 1 kg and USD 30.
- *Option B, operating rule:* the aft crew member moves amidships when the boat is swamped; transom freeboard 109 mm, trim 0.0 deg; no cost or mass.
- *Option C, both A and B.*
- **Recommendation: C**: the foam gives margin even when the rule is not followed, and the rule costs nothing.

**R10, optional fin drive.**
- *State:* no fin drive in the first prototype design, so its removal time and the boat's performance with it cannot be shown. Cause: the drive is an add-on and was not designed at TRL 3.
- *Option A, leave it out of the first prototype:* no cost or mass; R10 stays unshown until a drive exists.
- *Option B, clamp-on bracket for a bought pedal fin drive:* perhaps USD 800 to 1,500 and 7 to 10 kg; needs a patent and mark check of the chosen product (no MirageDrive or Hobie marks, no reverse or 360 degree mechanism).
- *Option C, an open fixed forward-only fin drive after the expired US6022249, as its own project:* no cost to this prototype; a separate design effort.
- **Recommendation: A**, with C kept as a later idea for the portfolio.

### Decisions made under the pre-approval

- LSK-DDR-002: design for construction, changes C1 to C13 and assumptions A1 to A6.
- Step hinge gap 40 mm and stop 20 deg below level (conservative).
- No person carried before the proof loads, and no trial except in calm, shallow water with a safety boat and life jackets.
- Appearance model departures (renders only): orange painted topsides and light grey inside; a wet concrete lane slab under the boat; a 1.75 m mannequin standing on the far side of the boat; the kick rung left out of the hero view (rolled up on land); a cut-back stern for the detail view.

### Build plan findings

- Design changes for construction (2026-10-03), all in LSK-DDR-002: stitch-and-glue panels with a bow knuckle; two bulkheads with hardwood ring frames; eight M10 bolts into welded nut plates and two pins; covered foam bench modules held by the inwale, straps and bench rails (plywood bench boxes dropped, about 9 kg saved); a foam bow box; three stringers per half and a knuckle floor; inwales; a hinge rail with backing block, float, strap hinges, 40 mm gap, stop straps and kick rung; 9 mm transom and 6 mm bulkheads; HDPE strakes and skids screwed into hardwood; handles and slings; a two-section pole; a bow U-bolt with pad.
- The floor needs the centre stringer: without it the span is 255 mm and the factor under a foot load falls below 1.
- Items to confirm with real parts (timber and foam densities, hinge and webbing strengths, nut plate welds, epoxy mass, foam and plywood prices, crew masses) are in LSK-DEC-001.

### Safety concerns

- Rescue in floodwater: life jackets always, crew training, never in moving water, and every trial in calm, shallow water with a safety boat. Safety stops in LSK-BLD-001 section 6 gate standing in the boat, the first launch, boarding trials, load and swamp trials, and rescue use.
- The step hinge has the lowest factor (1.5); it is proof-loaded to twice the working load before any boarding trial.
- Swamped, the transom freeboard is small (36 mm) and two people moving to one side dip the gunwale; until R5 is decided, crews keep people seated, low and centred and move the aft crew amidships.
- The halves weigh 56 and 45 kg; carrying them over rubble or through water is a lifting hazard, so four carriers or the slings are used.

### Recommended next step

Amish decides the five items above. The design looks ready for TRL 4 once he chooses to start it: build the aft half first with the first co-design candidate's boatyard, weigh it, float it alone, and proof-load the step with CalRig before any boarding trial.

## 2026-10-03: photoreal renders

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.
