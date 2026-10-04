---
doc_id: LSK-BLD-001
title: LaneSkiff prototype build plan
project: LaneSkiff
doc_type: Build plan
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First build plan; design made constructable (LSK-DDR-002)
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Round 2 requirement decisions (LSK-DDR-003); okoume plywood with 4 mm sides, softwood framing, no glass inside the floor, bottom 60 mm wider, stern quarter foam modules, capacity plate with the five-person rating and the swamped operating rule
---

# LaneSkiff prototype build plan

**Plan, not yet built.** How to build the first proof-of-concept LaneSkiff, component by component, on the plywood and epoxy path. Building and testing to it is TRL 4 work. Decisions still to be made are kept in the design decisions register (`docs/06-design-decisions.md`), not here.

> **Safety:** This plan builds a boat that will carry people in floodwater. Epoxy and glass work needs gloves, eye protection and a dust mask for sanding, in a ventilated space. Nobody is carried, and no boarding or swamp trial is run, until the safety stops in section 6 are passed. LaneSkiff is an open engineering reference, not certified rescue equipment, and is never used in moving water.

## 1. What you are building

![Every component, pulled apart and numbered in build order](05-build-plan/overview.png)

*Figure 1. Every component in build order, pulled apart. Both halves are shown in place along the boat.*

A flat-bottomed skiff 3.6 m long and 1.197 m wide over its rub strakes, in two closed halves of 1.8 m that bolt together, rated for five persons. Each half is stitched and glued from flat okoume plywood panels (6 mm bottom, 4 mm sides), framed with softwood, glassed outside only, and fitted with covered foam modules along both sides; the aft half has two more covered foam modules in its stern quarters. The aft half carries a floating boarding step behind its transom; the forward half has a foam-filled bow box under a short deck. Fourteen components are made (the plywood panels, hardwood frames, inwales and stringers, the bench modules, the bow box, the step rail, float and kick rung, and the push pole); the rest are bought (foam sheet, HDPE strip, bolts and nut plates, hinges, webbing, handles, paddles, rope). A capacity plate on the inside of the transom states the rating and what to do if the boat is swamped. The parts cost about USD 2,100 from the bill of materials.

## 2. What changed to make it buildable

*Table 1. Changes from the concept.*

| Component | The concept had | The buildable design has | Why |
| --- | --- | --- | --- |
| Hull | A hull shape | Three flat bottom panels and four flat side panels, stitched and glued with epoxy fillets and glass tape | Every panel is cut flat from a standard sheet |
| The split | One mid bulkhead | Two bulkheads, one closing each half, each with a softwood ring frame | Each half floats alone; the joint needs no seal |
| The joint | Bolts | Eight stainless M10 bolts from the forward side into nut plates on the aft frame, and two alignment pins | One spanner joins the halves |
| Side buoyancy | Blocks under benches | Foam modules in sewn tarpaulin covers, held under the inwale and strapped to a timber rail on the floor | Lighter than plywood boxes; the straps hold the module down when swamped |
| Bow buoyancy | Buoyancy in the bow | A bow box with a plywood wall and deck, filled with foam | Foam forward and high; a dry deck for the bow line |
| Floor | A floor | Three softwood stringers per half and a knuckle floor | Short floor spans; the skids screw into the stringers |
| Stern step | A hinged buoyant step | A float on strap hinges behind a hardwood rail, a 40 mm gap, stop straps and a kick rung | Nothing can be trapped as it swings; the straps take a kneeling person |
| Strakes, skids, handles | Named only | HDPE strip screwed into the framing; bought handles bolted through the inwales and transom frame; shoulder slings | Every fixing lands in solid timber |
| Push pole | A pole | Two 1.5 m sections with a joining sleeve | Stows inside one half |

![The two halves bolted together](05-build-plan/joint-04.png)

*Figure 2. The biggest change: two closed halves, bolted through their ring frames.*

## 3. Making the components

Make every plywood panel first, seal it with epoxy on both faces, and dry-fit before any glue. The aft half and the forward half are built the same way; differences are noted.

### 3.1 Bottom panels

![Making sketch: bottom panels](../cad/drawings/LSK-DWG-101.png)

**What it is and what it is made from.** Three panels of 6 mm okoume marine plywood: the aft bottom (1,800 x 1,052 mm), the forward flat bottom (900 x 1,052 mm), and the bow rake panel (921 mm long, 1,052 mm wide at its aft edge widening to 1,110 mm at the bow, because the sides flare). The floor is glassed outside only; there is no glass on the inside of the floor, so keep grit off it and recoat worn patches.

**How to make it.**

1. Mark the centreline and the lines of the three stringers (on the centreline and 150 mm each side) on the inside face.
2. Cut the straight long edges; they butt against the inside of the side panels.
3. Bevel the forward edge of the bow rake panel 12.5 degrees so it sits flat under the bow transom.
4. Drill 2 mm stitching holes 12 mm in from the long edges every 150 mm.
5. Seal both faces with epoxy.

**How it fits the parts next to it.** The side panels stand on the outside of the bottom panel's long edges and their bottom edges are flush with its underside. Inside, an epoxy fillet fills the corner; outside, 100 mm glass tape runs along the chine.

![Chine joint, cut across](05-build-plan/joint-01.png)

*Figure 3. The chine: side panel outside the bottom edge, stringer and bench rail on the floor, skid below.*

**Check before moving on.** Each panel within 2 mm of size; diagonals of the aft bottom equal within 3 mm.

### 3.2 Side panels

![Making sketch: side panels](../cad/drawings/LSK-DWG-102.png)

**What it is and what it is made from.** Four panels of 4 mm okoume marine plywood, 1,800 mm long. The two aft sides are 400 mm high rectangles. The two forward sides are 400 mm high at their aft end, with the bottom edge straight for 900 mm and then rising to 200 mm at the bow end; make them as a mirrored pair.

**How to make it.**

1. Cut both aft sides from one sheet and both forward sides from another, two to a sheet.
2. Mark the inwale line 40 mm below the top edge on the inside face.
3. Drill stitching holes 12 mm in from the bottom and end edges every 150 mm; in 4 mm plywood pull the stitches only snug, so the wire does not cut the edge.
4. Seal both faces.

**How it fits the parts next to it.** The panels lean out 8 degrees from vertical. Their ends are flush with the outer faces of the transom, bulkhead and bow transom. They stay flat; there is no bending.

**Check before moving on.** Forward sides are a true mirrored pair: lay one on the other, edges within 2 mm.

### 3.3 Stern transom

![Making sketch: stern transom](../cad/drawings/LSK-DWG-103.png)

**What it is and what it is made from.** 9 mm okoume marine plywood, a trapezoid 394 mm high, about 1,054 mm wide at the bottom and 1,164 mm at the top, with both side edges bevelled 8 degrees.

**How to make it.**

1. Cut the trapezoid and bevel the side edges.
2. Seal both faces.
3. After the ring frame and backing block are glued in (section 3.6 and 3.11), drill the four 9 mm holes for the hinge rail bolts, 130 mm above the bottom, at 110 mm and 280 mm each side of the centreline, and the holes for the two stop strap pad eyes, 380 mm up and 270 mm each side.

**How it fits the parts next to it.** It sits on the aft bottom panel, between the side panels, flush with their aft ends. Fillets and tape inside; tape outside.

![Transom corner from inside](05-build-plan/joint-02.png)

*Figure 4. Transom corner: transom between the sides, ring frame inside, inwale and rub strake at the top.*

**Check before moving on.** Square to the bottom within 1 degree.

### 3.4 Bow transom

![Making sketch: bow transom](../cad/drawings/LSK-DWG-104.png)

**What it is and what it is made from.** 9 mm okoume marine plywood, about 1,109 mm wide at the bottom and 1,164 mm at the top, about 196 mm high, with its bottom edge bevelled 12.5 degrees to the rake and its sides bevelled 8 degrees.

**How to make it.** Cut and bevel; drill two 9 mm holes for the bow eye, 330 mm above the line of the hull bottom and 25 mm each side of the centreline; seal.

**How it fits the parts next to it.** It sits on the bow rake panel between the forward side panels, flush with their bow ends. The bow eye pad is glued to its inside (section 3.10).

**Check before moving on.** Top edge level with the side panels' top edges.

### 3.5 Joint bulkheads

![Making sketch: joint bulkheads](../cad/drawings/LSK-DWG-105.png)

**What it is and what it is made from.** Two panels of 6 mm okoume marine plywood, the same trapezoid as the stern transom.

**How to make it.** Cut both from one pattern; seal. Drill the bolt and pin holes later, through bulkhead and ring frame together, with both halves clamped face to face (section 3.6).

**How it fits the parts next to it.** Each closes its half at the joint: it sits on the bottom panel between the side panels, flush with their ends, filleted and taped inside and out. The two bulkheads touch face to face when the boat is assembled.

![Halves joint, cut through a bolt](05-build-plan/joint-04.png)

*Figure 5. Aft ring frame, aft bulkhead, forward bulkhead, forward ring frame, clamped by an M10 bolt into a nut plate.*

**Check before moving on.** With the two halves standing together, the bulkhead faces touch all round (no gap over 1 mm).

### 3.6 Ring frames

![Making sketch: ring frames](../cad/drawings/LSK-DWG-106.png)

**What it is and what it is made from.** Three rings of treated softwood 20 x 45 mm: one inside the stern transom and one on each joint bulkhead. Each ring is four members (bottom, two sides at 8 degrees, top), half-lapped at the corners, following the inside of the hull with a 45 mm wide face.

**How to make it.**

1. Cut the members, lay the ring on its bulkhead, mark and cut the half-laps.
2. Glue the ring to the plywood with thickened epoxy and screw through the plywood from outside every 150 mm with 5 x 30 stainless screws.
3. Joint frames only: with both halves clamped together, drill eight 11 mm bolt holes (at 75 mm and 250 mm each side of the centreline, 28 mm above the floor line and 377 mm up) and two 12.5 mm pin holes (400 mm each side, 377 mm up) through frame and bulkhead of both halves at once.
4. Screw a nut plate (a 40 x 40 x 3 mm steel plate with an M10 nut welded on) over each bolt hole on the aft face of the aft joint frame. Epoxy the two pins into the aft frame.

**How it fits the parts next to it.** The frames butt against the side panels, bottom and transom or bulkhead; the inwales and stringers end against their faces.

**Check before moving on.** A bolt runs freely through all four layers into every nut plate by hand.

### 3.7 Inwales

![Making sketch: inwales](../cad/drawings/LSK-DWG-107.png)

**What it is and what it is made from.** Four lengths of treated softwood 20 x 40 mm: aft inwales 1,739 mm, forward inwales 1,762 mm.

**How to make it.** Bevel the top edge 8 degrees; glue to the inside of the side panel along the inwale line, screwing from outside every 150 mm; ends butt the ring frames (and the bow transom forward).

**How it fits the parts next to it.** Its top is flush with the side's top edge. The carry handle bolts pass down through it, the rub strake screws go into it, and the top of each bench module bears up against its underside.

**Check before moving on.** Top edge flush with the side within 1 mm along its length.

### 3.8 Stringers and knuckle floor

![Making sketch: stringers and knuckle floor](../cad/drawings/LSK-DWG-108.png)

**What it is and what it is made from.** Six treated softwood stringers 40 x 20 mm (three per half: on the centreline and 150 mm each side; 1,739 mm long aft, 851 mm forward) and a knuckle floor 40 mm long and 45 mm high across the forward half at the knuckle, its underside cut to the two bottom slopes.

**How to make it.** Glue the stringers flat to the floor on their marked lines, ends butted to the ring frames and the knuckle floor. Glue and screw the knuckle floor across both bottom panels at the knuckle.

**How it fits the parts next to it.** The bow rake panel and the forward flat bottom butt at the knuckle on top of the knuckle floor; tape outside and fillets inside close the seam.

![Bottom knuckle, cut along the boat](05-build-plan/joint-03.png)

*Figure 6. The knuckle: the two bottom panels butt on the knuckle floor.*

**Check before moving on.** No stringer rocks; fillets continuous.

### 3.9 Bench modules

![Making sketch: bench module](../cad/drawings/LSK-DWG-109.png)

**What it is and what it is made from.** Four modules, one each side of each half: a core of closed-cell polyethylene foam in 50 mm layers, stacked 350 mm high, with its outboard edge bevelled 8 degrees to lie on the side (193 to 242 mm wide, 1,735 mm long aft, 847 mm forward); a sewn sleeve of PVC-coated polyester tarpaulin with laced ends, as for the LevelHull modules; a softwood bench rail 40 x 20 mm on the floor along the module's inboard foot, 330 mm from the centreline; and webbing straps (three per aft module, two per forward module).

**How to make it.**

1. Cut the foam layers, bevel the outboard edges, stack them; no glue.
2. Sew the sleeve to the stack size with two rows of UV-stabilised stitching; slide the stack in and lace the ends.
3. Glue and screw the bench rails to the floor.
4. Cut the straps 50 mm webbing, heat-seal the ends.

**How it fits the parts next to it.** The module sits on the floor against the side panel, between the ring frames, with its top touching the underside of the inwale. Each strap is screwed to the inwale's inner face with two stainless screws and a penny washer, runs over the module top and down its inboard face, and is screwed to the top of the bench rail.

![Bench module, cut across at a strap](05-build-plan/joint-05.png)

*Figure 7. Bench module tight under the inwale, strapped to the inwale and the bench rail.*

**Stern quarter modules (make 2).** One each side of the aft half, inboard of the aft bench module at the transom end: a foam core of 50 mm layers 205 x 222 x 330 mm (15 L), in a sewn tarpaulin cover, outside 209 mm along the boat, 226 mm across and 334 mm high. It stands on the side stringer and the bench rail, 40 mm forward of the transom so it clears the hinge rail bolt nuts, against the bench module's inboard face, and its top is level with the bench top. Two 50 mm webbing straps hold each one: screwed to the floor with a stainless washer at its inboard foot, up its inboard face, over its top and the bench top, and screwed to the inwale's inner face like the bench straps. The standing crew member's place at the pole, 400 mm forward of the transom, stays clear.

**Check before moving on.** No module can be lifted by hand at any strap.

### 3.10 Bow box

![Making sketch: bow box](../cad/drawings/LSK-DWG-110.png)

**What it is and what it is made from.** A 6 mm plywood wall standing 3.0 m forward of the transom, cut to the rake and notched round the inwales; a 6 mm deck 591 mm long and about 1,124 mm wide; foam layers filling the box; and a hardwood pad 20 x 120 x 80 mm for the bow eye.

**How to make it.**

1. Glue the pad to the inside of the bow transom; fit the bow eye (a stainless U-bolt) through transom and pad with its backing plate and nuts inside.
2. Glue in the wall; fillet and tape it to the bottom and sides.
3. Cut the foam layers to the rake and round the pad and nuts; pack the box.
4. Glue the deck to the inwales, bow transom and wall; tape the seams.

**How it fits the parts next to it.** The deck lies between the inwales, flush with their tops; the foam fills the box with no voids.

![Bow eye, cut through one leg](05-build-plan/joint-08.png)

*Figure 8. Bow eye through the bow transom and pad, nuts inside, foam round it.*

**Check before moving on.** Bow eye nuts tight before the foam goes in; the eye does not move under a hard pull by hand.

### 3.11 Hinge rail and transom backing block

![Making sketch: hinge rail and backing block](../cad/drawings/LSK-DWG-111.png)

**What it is and what it is made from.** A hardwood rail 40 x 60 x 640 mm on the transom's outer face, its bottom edge 100 mm above the bottom of the hull, centred; and a hardwood backing block 20 x 60 x 640 mm on the inner face at the same height, between the ring frame's side members.

**How to make it.** Cut, seal, glue the backing block inside; drill through block, transom and rail together for four M8 x 90 stainless bolts at 110 mm and 280 mm each side, 130 mm up; bed the bolts in sealant.

**How it fits the parts next to it.** The strap hinges screw to the rail's top face (60 mm wide).

![Hinge rail and step hinge, cut along the boat](05-build-plan/joint-06.png)

*Figure 9. Hinge rail bolted through transom and backing block; the step hinge crosses the 40 mm gap to the float.*

**Check before moving on.** The rail does not move when levered with a 1 m bar.

### 3.12 Step float

![Making sketch: step float](../cad/drawings/LSK-DWG-112.png)

**What it is and what it is made from.** A float 450 mm long, 600 mm wide and 90 mm deep: a hardwood rim 20 x 75 mm, a foam core 410 x 560 x 75 mm, a 6 mm plywood bottom deck and a 9 mm plywood top deck, all glued with epoxy; non-slip coating on top.

**How to make it.** Glue and screw the rim at the corners; glue the bottom deck on; set the foam in; glue the top deck on; coat. Fit two pad eyes on top near the aft corners and two strap eyes on the aft face.

**How it fits the parts next to it.** Its front edge sits 40 mm behind the hinge rail. Two heavy stainless strap hinges, one leaf on the rail top and one on the float top, cross the gap with their pins over it. Two webbing stop straps run from pad eyes high on the transom to the pad eyes on the float and hold it at 20 degrees below level at most.

![The step at its stop](05-build-plan/joint-07.png)

*Figure 10. The step swung down to its stop, with the kick rung below.*

**Check before moving on.** The float swings from folded up to its stop without touching the rail or transom; nothing closes to less than 25 mm.

### 3.13 Kick rung

![Making sketch: kick rung](../cad/drawings/LSK-DWG-113.png)

**What it is and what it is made from.** A hardwood rung 32 mm in diameter and 560 mm long on two 25 mm webbing straps.

**How to make it.** Round the ends; sew each strap round the rung 230 mm each side of the centre; sew the other ends to the strap eyes on the float's aft face so the rung hangs 270 mm below the float's underside.

**How it fits the parts next to it.** It rolls up and clips on top of the float for carrying.

**Check before moving on.** Each strap holds a person standing on the rung (see section 6).

### 3.14 Push pole

![Making sketch: push pole](../cad/drawings/LSK-DWG-114.png)

**What it is and what it is made from.** Two 1,500 mm sections of aluminium tube 38 x 1.6 mm, joined by a 300 mm internal sleeve riveted into one section and pinned into the other; a hardwood fork foot riveted into the lower end; a rubber cap on the top end.

**How to make it.** Cut, deburr, rivet the sleeve, drill the cross pin, rivet the foot.

**How it fits the parts next to it.** Each section stows on the aft floor between the stringers.

**Check before moving on.** The joined pole does not wobble at the joint.

### 3.15 Bought components

- **Foam sheet:** closed-cell polyethylene, 2,000 x 1,000 x 50 mm, about 30 kg/m3; not polystyrene (fuel dissolves it) and not open-cell foam.
- **HDPE strip:** rub strakes 12 x 30 mm screwed through the side into the inwale every 200 mm; skids 40 x 8 mm screwed into the side stringers every 150 mm with 5 x 30 stainless screws, each hole bedded in sealant; the forward skids bend over the knuckle.
- **Joint bolts and nut plates:** M10 x 80 stainless A4-70 hex bolts with 30 mm washers; nut plates welded by a local welder and galvanised.
- **Hinges and pad eyes:** two heavy stainless strap hinges about 100 mm wide with 6 mm pins; four stainless pad eyes.
- **Webbing:** 25 mm polyester for the stop and rung straps, 50 mm for the bench straps and slings.
- **Handles:** two stainless tube grab handles about 250 mm long for the transom; eight grab handles about 200 mm long for the inwales, each with two M6 bolts.
- **Paddles, bow line and slings:** two 1.4 m paddles, 10 m of 10 mm polyester rope, two padded slings with snap hooks; two carriers take each half with the slings.
- **Capacity plate:** an engraved or etched aluminium plate 150 x 100 mm, screwed to the inside face of the stern transom above the backing block, between the stern quarter modules, where the crew sees it. Its text:

  > LANESKIFF. Maximum 5 persons or 375 kg. Life jackets on at all times. Calm, slow water only; never in moving water. IF SWAMPED: stay in the boat, sit low and centred, and the aft crew member moves amidships at once. Open engineering reference, not certified.

## 4. Putting it together

Each picture shows the parts already fitted in grey and the parts being fitted in colour, with an arrow showing the way they go in.

### Step 1: stitch the aft bottom and sides

![Step 1](05-build-plan/step-01.png)

Stitch the side panels to the bottom with copper wire or cable ties every 150 mm. Check the diagonals are equal before any glue.

### Step 2: fit the stern transom and the aft joint bulkhead

![Step 2](05-build-plan/step-02.png)

Both sit on the bottom between the sides. Tack with small fillets, check square, then fillet and tape every inside seam.

### Step 3: glue in the ring frames

![Step 3](05-build-plan/step-03.png)

Glue and screw the transom frame and the aft joint frame. Hold point: let the epoxy cure before drilling.

### Step 4: fit the inwales

![Step 4](05-build-plan/step-04.png)

Glue and screw inside the top of each side, frame to frame.

### Step 5: glue down the stringers and bench rails

![Step 5](05-build-plan/step-05.png)

Three stringers and two bench rails on their marked lines.

### Step 6: glass the outside, then fit the skids and strakes

![Step 6](05-build-plan/step-06.png)

Turn the half over, remove the stitches, fill and round the chines, and glass the bottom and sides with 400 g/m2 cloth. When cured, screw the skids into the side stringers and the rub strakes into the inwales, each hole bedded in sealant. Paint.

### Step 7: build the forward half the same way

![Step 7](05-build-plan/step-07.png)

As steps 1 and 2, with the two bottom panels butted at the knuckle and the bow transom on the rake.

### Step 8: frame the forward half and close the bow box

![Step 8](05-build-plan/step-08.png)

Ring frame, inwales, stringers and bench rails as on the aft half; then the bow eye and pad, the bow box wall, the foam and the deck.

### Step 9: glass, skids, strakes, bench modules and handles

![Step 9](05-build-plan/step-09.png)

Finish the forward half as in steps 6, 10 and 11.

### Step 10: strap in the aft bench and quarter modules

![Step 10](05-build-plan/step-10.png)

Slide each module under the inwale, against the side; screw each strap to the inwale and the bench rail, pulled snug. Then set each stern quarter module on the side stringer and bench rail against its bench module, and screw its two straps to the floor and the inwale. Screw the capacity plate to the inside of the transom.

### Step 11: fit the grab and carry handles

![Step 11](05-build-plan/step-11.png)

Carry handles with M6 bolts down through the inwales, two at each end of each half; transom grab handles through the transom and its ring frame.

### Step 12: bolt on the hinge rail

![Step 12](05-build-plan/step-12.png)

Four M8 bolts through rail, transom and backing block, bedded in sealant.

### Step 13: hang the step float

![Step 13](05-build-plan/step-13.png)

Screw the hinge leaves to the rail top and the float top with the 40 mm gap set by two spacer blocks; remove the blocks.

### Step 14: fit the stop straps and the kick rung

![Step 14](05-build-plan/step-14.png)

Pad eyes on the transom; adjust the straps so the float stops 20 degrees below level; hang the rung 270 mm below the float.

### Step 15: bring the halves together

![Step 15](05-build-plan/step-15.png)

At the water's edge, stand the halves end to end, slide the pins into their holes and close the bulkhead faces together.

### Step 16: bolt the halves together

![Step 16](05-build-plan/step-16.png)

Bottom row first, then the top row, snugged with one 17 mm spanner from the forward side. Hold point: all eight bolts in before anyone steps in.

### Step 17: stow the pole, paddles and bow line

![Step 17](05-build-plan/step-17.png)

Pole sections on the aft floor between the stringers, paddles on the aft benches, the bow line coiled on the bow deck and tied to the bow eye.

## 5. First checks

These are listed here and recorded in a TRL 4 test report.

*Table 2. First checks.*

| Check | Requirement | How | Pass when |
| --- | --- | --- | --- |
| Beam | R4 | Tape over the rub strakes; carry through a 1.3 m gate | Fits the gate without scraping |
| Carry mass | R1 | Weigh each half on a hanging scale | Recorded against LSK-CAL-001 (50 and 38 kg expected) |
| Joining the halves | R7 | Two people, one spanner, timed from halves on the ground to eight bolts tight | Joined, and within the R7 time |
| Each half alone | Safety | Float each half on its own in calm, shallow water | Floats upright, no leak at the bulkhead |
| Load and draft | R2, R3 | Water ballast in containers placed as the five rated persons (375 kg), in calm water | Draft 150 mm or less at the transom and bow; no water over the gunwale |
| Swamp | R5 | Fill with water, ballast for the five rated persons at two thirds, following the ABYC H-8 procedure in a pool; first with the aft crew's ballast in place, then moved amidships | Floats approximately level; trim and freeboard recorded at the transom and bow in both cases |
| Boarding | R6 | Several volunteers of different builds board over the stern step from waist-deep water, inclinometer on the hull | Heel recorded; every volunteer boards unaided |
| Step proof load | R6, safety | Twice the working load on the float aft edge at its stop (CalRig) | No damage, no hinge or strap movement |

## 6. Safety stops

Work stops at each point below until what is listed is true.

- **Before anyone stands in the boat:** all eight joint bolts in and tight; every hull seam inspected, no dry fillets.
- **Before the first time on the water:** each half floated alone without a leak; the bow eye pulled to twice the towing load.
- **Before any boarding trial:** the step hinges, stop straps and kick rung proof-loaded to twice the working load (an 80 kg person kneeling on the float's aft edge with a factor of two); the hinge gap checked at 40 mm with nothing closing below 25 mm through the swing.
- **Before any load or swamp trial:** calm, shallow water no deeper than chest height, no current; a safety boat or bank team with a throw line; every person in a life jacket and briefed; ballast in place of people for the first swamp test.
- **Before any person is carried:** the capacity plate is on the transom with the five-person rating and the swamped operating rule, and every crew member has read it.
- **Before any rescue use:** the TRL 4 trials passed and the five-person rating on the capacity plate confirmed by the load and swamp tests, and the crew trained under its own agency's rules, including the swamped rule. Never in moving water.

## 7. Tools, skills and workspace

- A covered, ventilated space about 5 x 3 m where epoxy can cure above 15 degrees Celsius, with two trestles.
- Jigsaw or circular saw, block plane, drill and drivers, a sanding block or orbital sander, clamps (twelve or more), mixing pots and fillet spatulas, a tape and long straightedge, a bevel gauge, a 17 mm spanner and a 13 mm spanner.
- Skills: stitch-and-glue boatbuilding (any small boatyard), basic sewing with a heavy machine or a sail maker for the covers and straps, and a welder for the nut plates.
- Gloves, eye protection and a dust mask for epoxy, glass and sanding.

## 8. Where the numbers come from

- Model: `cad/src/model.py` (dimensions, constructability checks), `cad/step/` and `cad/stl/`.
- Drawings: `cad/drawings/LSK-DWG-001` (general arrangement, Rev P2) and `LSK-DWG-101` to `114` (making sketches).
- Calculations: `docs/04-calcs/01-sizing.md` (LSK-CAL-001), `docs/04-calcs/sizing.py`, `docs/04-calcs/results.csv`.
- Bill of materials: `bom/bom.csv`.
- Pictures: `cad/src/build_plan_media.py`.
- Design changes: `docs/decisions/0002-design-for-construction.md` (LSK-DDR-002) and `docs/decisions/0003-requirement-decisions-round2.md` (LSK-DDR-003).
