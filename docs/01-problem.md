---
doc_id: LSK-PRB-001
title: LaneSkiff problem statement
project: LaneSkiff
doc_type: Problem statement
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Budget stated as a value-engineering target; open questions answered at TRL 3; first co-design candidates; safety section
---

# LaneSkiff problem statement

Floods strand people in narrow lanes and low houses where big boats cannot go. The small boats that can go there are hard to carry, easy to tip, and hard to climb into from waist-deep water.

## The problem

Most flood deaths are drownings ([WHO](https://www.who.int/health-topics/floods/drowning---key-facts)), and most flood-exposed people live in low and middle income countries ([Rentschler et al., 2022](https://www.nature.com/articles/s41467-022-30727-4)). In the first hours, rescue is done by local fishers, volunteers and whatever boats are nearby, as in Kerala in 2018 ([The Week, 2018](https://www.theweek.in/news/india/2018/08/20/kerala-fisherman-turns-stepping-stone-to-safety-literally.html)) and Houston in 2017 ([NBC News, 2017](https://www.nbcnews.com/storyline/hurricane-harvey/triumph-struggle-ragtag-cajun-navy-responds-houston-flood-n796991)). Boarding is the weak point: a person in waist-deep water has to lift their own weight over a side that tips toward them.

Existing craft solve parts of the problem. Inflatable rescue craft are light and buoyant but cost USD 4,900 ([Oceanid](https://oceanid.com/RDC-Pricing-Specifications.html)). Jon boats are cheap and flat but rated for two ([Lund](https://www.lundboats.com/families/jon-boat/1240.html)). Folding boats such as the Porta-Bote Alpha 12 carry three people and weigh 127 lb (58 kg) assembled ([Porta-Bote](https://portabote.com/product/alpha-series-12/)). The patented emergency watercraft of US7832348B2 carries about 30 people on inflatable pontoons behind a personal watercraft ([Google Patents](https://patents.google.com/patent/US7832348B2/en)), which needs an engine and a PWC. Small boats under 20 ft are expected to float level when swamped ([New Boat Builders](https://newboatbuilders.com/pages/flot.html); [ABYC H-8](https://webstore.ansi.org/standards/abyc/abyc2022-2483768)). No open design combines a carry-in hull, a stable stern boarding step, level swamped flotation and local build paths.

## Users and context

| User | Need | Context |
| --- | --- | --- |
| Community rescuers (fishers, volunteers) | A boat two people can carry into a lane and pole along, that people can board from the water | First hours of a flood, before or alongside official teams |
| Civil defence and disaster response teams | A light, cheap craft to add to heavier boats for lane work | Urban and village floods; transport by pickup or small truck |
| People being rescued, including older adults, children and people with limited mobility | A stable step and handholds to climb in without help from below | Standing in waist-deep water or at a doorway or window |
| Local boatbuilders | Drawings and a material table they can build from with local sheet and timber | Small yards building before the monsoon season |

## Operating environment

- Floodwater in lanes and streets, typically knee to chest deep, with debris, submerged walls, kerbs and drains.
- Lanes and doorways about 1.2 m wide or more (estimate of the target envelope).
- Mostly slow-moving water; not designed for swiftwater or open water.
- Heat, rain and night work; boats stored for months between floods.

## Constraints

- Value-engineering target for the prototype: USD 1,500 (a hypothetical control target, not a spending limit; STANDARDS section 18).
- Carried by two people: about 40 to 50 kg total carry mass (estimate from the preliminary screen), in two halves.
- Payload 5 to 8 times hull mass (a rigid hull; 10 times is not realistic).
- Single flat hull, poled or paddled; no twin pontoons, jet ski transom or hinged bow ramp.
- Two rigid halves that bolt together; no flexible panel hull or folding transom.
- Optional fin drive fixed and forward-only, with no reverse mechanism.
- Hardware under CERN-OHL-S-2.0; any software or calculation scripts under MIT.

## Out of scope

- Swiftwater, surf or open-water rescue.
- Outboard engines and powered propulsion other than the optional fin drive.
- Inflatable sponsons in the first version.
- Certification as a rescue boat or to CE or USCG standards at this TRL.
- Rescue training; users must follow their own agency's water rescue training.

## Prior work

| Prior work | What it does | Gap for these users | Source |
| --- | --- | --- | --- |
| Oceanid RDC rapid deployment craft | Inflatable rescue craft, 15 ft 4 in, 50 lb, more than 2,000 lb buoyancy, USD 4,900 | Costly and imported; no stable boarding step for people in the water | [link](https://oceanid.com/RDC-Pricing-Specifications.html) |
| Lund 1240 jon boat | 12 ft flat-bottom aluminium boat, 107 lb, 535 lb load, from USD 1,694 | Rated for two people; side boarding tips the boat | [link](https://www.lundboats.com/families/jon-boat/1240.html) |
| MetalBoatKits 19 ft Flood Rescue Skiff | Aluminium kit boat for eight people, hull about 245 kg, 8 in draft at full load | Far too heavy to carry into a lane; needs an outboard | [link](https://metalboatkits.com/product/19-foot-6m-flood-rescue-skiff-new/) |
| Porta-Bote Alpha Series 12 | Folding boat, 12.2 ft, 127 lb assembled, 3 people, 555 lb load | Low capacity for rescue; folding hull covered by live Porta-Bote patents | [link](https://portabote.com/product/alpha-series-12/) |
| US7832348B2, emergency watercraft (Newcomb) | Twin inflatable pontoons with a floor, hinged ramp and a transom for a personal watercraft; about 30 people; anticipated expiry 2028 | Needs a PWC and a large crew to assemble; live patent LaneSkiff avoids | [link](https://patents.google.com/patent/US7832348B2/en) |
| US6932020B2, boat boarding device (expired 2013) | Hinged floating platform with flotation and a step for swimmers to board | Recreational add-on; free prior art LaneSkiff builds on for its stern step | [link](https://patents.google.com/patent/US6932020B2/en) |

## Co-design

A coastal fishing community or volunteer rescue group with flood rescue experience, working with a local boatyard, in a flood-prone state such as Kerala or Bihar, so the step, carry handles and material choices are shaped by people who have done lane rescues.

First candidates to approach (none approached yet, nothing agreed; LSK-DDR-001, D9):

- [ ] A fishers' volunteer rescue group in Malappuram district, Kerala, with a boatyard on the same coast that builds plywood and epoxy boats.
- [ ] Country boat makers in a flood-prone district of north Bihar, for the timber and local-material build path.
- [ ] A state disaster response force or civil defence training unit, for the boarding and swamp trials.

## Open questions

The TRL 1 questions are answered on paper at TRL 3 (LSK-CAL-001, LSK-DDR-001); the answers are confirmed by trials at TRL 4.

- **Best build material for Kerala and Bihar?** Plywood and epoxy, stitch and glue, for the first prototype: the most widely available skills and materials, and repairable. Aluminium and HDPE paths come out at similar mass (LSK-CAL-001, section 8).
- **Step depth and folding for children and older adults?** A float that lies on the water behind the transom, with a kick rung 270 mm below it, and two transom handles; a person steps on the rung, kneels on the float and rolls over the transom. The float folds up against the transom for carrying.
- **Level swamped flotation inside the weight budget?** Level flotation works with 0.49 m3 of foam (15 kg) placed outboard and forward, but the hull comes out at 100 kg against the 50 kg target. The options are with Amish (`docs/REVIEW.md`).
- **Is the fin drive worth it?** Not in the first prototype design; the options are with Amish.
- **Which partner hosts the first trials?** The first candidates above, to approach.

> **Safety:** Flood water is dangerous even when it looks calm: submerged walls, open drains and manholes, live electrical wires, debris and contaminated water. LaneSkiff is not for swiftwater, surf, open water or water flowing faster than a person can wade against. Crew and passengers wear life jackets at all times, crews follow their own agency's water rescue training, and the boat is an open engineering reference, not certified rescue equipment.
