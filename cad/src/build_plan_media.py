"""LaneSkiff prototype build plan pictures (LSK-BLD-001, STANDARDS section 18).

Run from the repo root:  python cad/src/build_plan_media.py [overview|sheets|joints|steps ...]
With no argument it draws everything. Every picture is drawn from cad/src/model.py, so the
pictures and the model never disagree:
    docs/05-build-plan/overview.png    every component pulled apart, numbered in build order
    cad/drawings/LSK-DWG-101 to 115    making sketches for the made components
    docs/05-build-plan/joint-NN.png    close-ups of the joints that need explaining
    docs/05-build-plan/step-NN.png     one picture per assembly step
Uses .kit/build_views.py. BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
from build123d import Pos, Rot  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
OUT = ROOT / "docs" / "05-build-plan"
DWG = ROOT / "cad" / "drawings"
DATE = "2026-10-03"
ROWS = M.build_all(P)
N = {n: s for n, *_, s in ROWS}
H = {n: h for n, h, *_ in ROWS}
PRJ = "LaneSkiff"

COL = {"bottom": "#C9A46C", "side": "#E2C28F", "transom": "#B07D46", "bulkhead": "#A0703F", "frame": "#7C4A1E",
       "inwale": "#8B5A2B", "stringer": "#6F4521", "rail": "#92400E", "cover": "#EA580C", "foam": "#FACC15",
       "strap": "#1D4ED8", "box": "#D9B98C", "bolt": "#374151", "strake": "#1F2937", "skid": "#111827",
       "step": "#0F766E", "hinge": "#6B7280", "rung": "#14B8A6", "handle": "#9CA3AF", "pole": "#94A3B8",
       "paddle": "#2563EB", "eye": "#DC2626", "quarter": "#F97316", "ghost": "#D1D5DB"}


def sel(*prefixes, half=None):
    return M.flat([s for n, s in N.items() if n.startswith(prefixes) and (half is None or H[n] == half)])


def win(shape, x0, x1, y0=-900, y1=900, z0=-400, z1=900):
    return shape & M.box(x0, x1, y0, y1, z0, z1)


AFT_SHELL = ("bottom aft", "side aft", "stern transom", "joint bulkhead aft")
FWD_SHELL = ("bottom forward", "bottom bow", "side forward", "bow transom", "joint bulkhead forward")


# ---------------------------------------------------------------- overview
def components():
    """Made and bought components in build order, one of each where they repeat (the names give counts)."""
    return [
        Part("Bottom panels (3)", sel("bottom"), COL["bottom"], 1, (0, 0, -500)),
        Part("Side panels (4)", sel("side"), COL["side"], 2, (0, 0, 0)),
        Part("Stern transom", N["stern transom"], COL["transom"], 3, (-700, 0, 250)),
        Part("Bow transom", N["bow transom"], COL["transom"], 4, (500, 0, 0)),
        Part("Joint bulkheads (2)", sel("joint bulkhead"), COL["bulkhead"], 5, (0, 0, 250)),
        Part("Ring frames (3)", sel("ring frame"), COL["frame"], 6, (0, 0, 520)),
        Part("Inwales (4)", sel("inwale"), COL["inwale"], 7, (0, 0, 700)),
        Part("Stringers (6) and knuckle floor", sel("stringer", "knuckle floor"), COL["stringer"], 8, (0, 0, 300)),
        Part("Bow box wall, deck and foam", sel("bow box wall", "bow deck", "bow foam", "bow eye pad"), COL["box"], 9,
             (600, 0, 650)),
        Part("Bench modules (4): rail, cover, foam, straps", sel("bench"), COL["cover"], 9, (0, 0, 1050)),
        Part("Stern quarter foam modules (2)", sel("quarter"), COL["quarter"], 29, (-350, 0, 1250)),
        Part("Rub strakes (4) and skids (4)", sel("rub strake", "skid"), COL["strake"], 12, (0, 0, -900)),
        Part("Hinge rail, backing block, bolts", sel("hinge rail", "transom backing block", "rail bolts"), COL["rail"],
             14, (-1250, 0, -150)),
        Part("Step float with strap hinges", sel("step float", "strap hinges"), COL["step"], 14, (-1900, 0, 300)),
        Part("Stop straps, pad eyes, kick rung", sel("stop straps", "float pad eyes", "transom pad eyes", "kick rung"),
             COL["rung"], 15, (-1900, 0, -450)),
        Part("Grab and carry handles", sel("transom grab handles", "carry handles"), COL["handle"], 17, (0, 0, 1500)),
        Part("Joint bolts and nut plates (8)", sel("joint bolt", "alignment pin"), COL["bolt"], 11, (0, -1100, 200)),
        Part("Push pole, paddles, bow eye and line", sel("push pole", "paddles", "bow eye", "bow line"), COL["paddle"],
             19, (0, 0, 1900)),
    ]


def overview():
    ps = components()
    bv.overview(ps, OUT / "overview.png", "LaneSkiff: every component, in build order",
                subtitle="Both halves shown in place along the boat; parts pulled apart up, down, fore and aft. "
                         "Plan, not yet built", elev=22, azim=-62, size=(12, 7.5), key=True)


# ---------------------------------------------------------------- making sketches
def flat_side(shape):
    """Turn a side panel (flared 8 deg) upright so its views show its true shape."""
    c = shape.bounding_box().center()
    return shape.rotate(M.Axis((c.X, c.Y, c.Z), (1, 0, 0)), P["flare_deg"] if c.Y > 0 else -P["flare_deg"])


def sheets():
    def shell(prefixes, skip=()):
        return Part("Hull", M.flat([N[n] for n in N if n.startswith(prefixes) and not n.startswith(skip)]), COL["ghost"])

    hull_aft = [shell(AFT_SHELL)]
    hull_fwd = [shell(FWD_SHELL)]
    both = hull_aft + hull_fwd
    def sheet(no, title, mat, notes, part, nb, vs=None, iv=(22, -60)):
        bv.component_sheet(Part(title, part, "#0F766E"), nb, PRJ, f"LSK-DWG-{no}", title, mat, notes, DATE,
                           view_shape=vs, inset_view=iv, out_dir=str(DWG))
    w = lambda z, d=P["t_side"]: 2 * M.half(z, d, P)   # noqa: E731  width inside the sides at height z
    sheet(101, "Bottom panels (aft, forward flat, bow rake)", "6 mm okoume marine plywood, glass outside only",
          [f"Aft bottom 1,800 x {w(0):,.0f}; forward flat 900 x {w(0):,.0f}; bow rake",
           f"  panel 921 long, {w(0):,.0f} wide aft to {w(P['rise']):,.0f} at the bow.",
           "Mark the centreline and the stringer lines 150 each side.",
           "Long edges are straight; they butt the inside of the side panels.",
           "Drill 2 mm stitch holes 12 in from the edges every 150.",
           "Bow rake: aft edge square, forward edge bevelled 12.5 deg",
           "  to sit under the bow transom.",
           "Seal both faces with epoxy; no glass inside the floor."],
          sel("bottom"), [shell(AFT_SHELL + FWD_SHELL, ("bottom",))])
    sheet(102, "Side panels (four)", "4 mm okoume marine plywood",
          ["Aft sides 1,800 x 400 rectangles (two).",
           "Forward sides 1,800 long, 400 high aft; bottom edge straight",
           "  for 900, then rising to 200 at the bow end (two, handed).",
           "Mark the inwale line 40 below the top edge, inside face.",
           "Stitch holes 12 in from the bottom and end edges every 150.",
           "Sides lean out 8 deg; the panels are flat, no bending.",
           "Fits: bottom edge on the outside of the bottom panel edge,",
           "  ends flush with the transom and bulkhead outer faces."],
          sel("side aft port", "side forward port"), [shell(AFT_SHELL + FWD_SHELL, ("side aft port", "side forward port"))],
          vs=flat_side(sel("side aft port", "side forward port")), iv=(22, 120))
    sheet(103, "Stern transom", "9 mm okoume marine plywood",
          [f"Trapezoid: {w(P['t_bot']):,.0f} wide at the bottom, "
           f"{w(P['D']):,.0f} at the top, 394 high.",
           "Sides bevelled 8 deg to lie flat on the side panels.",
           "Sits on the bottom panel, between the sides, flush aft.",
           "Drill after the ring frame and backing block are glued in:",
           "  four 9 holes for the hinge rail bolts, 130 above the bottom,",
           "  at 110 and 280 each side of the centreline;",
           "  two 9 holes for each pad eye, 380 up, 270 each side."],
          N["stern transom"], [shell(AFT_SHELL, ("stern transom",))], iv=(22, -130))
    sheet(104, "Bow transom", "9 mm okoume marine plywood",
          [f"Trapezoid about {w(P['rise'] + P['t_bot']):,.0f} wide at the bottom edge, {w(P['D']):,.0f} at the",
           "  top, about 196 high; bottom edge bevelled 12.5 deg to the rake.",
           "Sides bevelled 8 deg to the side panels.",
           "Sits on the bow rake panel, between the sides, flush forward.",
           "Bow eye: two 9 holes 330 above the hull bottom line,",
           "  25 each side of the centreline, through the hardwood pad."],
          N["bow transom"], [shell(FWD_SHELL, ("bow transom",))])
    sheet(105, "Joint bulkheads (two)", "6 mm okoume marine plywood",
          [f"Same trapezoid as the transom: 394 high, {w(P['t_bot']):,.0f} to {w(P['D']):,.0f} wide.",
           "One closes each half; the halves are separate boxes.",
           "Sits on the bottom panel, between the sides, flush with the",
           "  panel ends; glued and taped inside and out.",
           "Drill the eight 11 bolt holes and two 12.5 pin holes through",
           "  bulkhead and ring frame together, both halves clamped",
           "  face to face, so the holes line up."],
          N["joint bulkhead aft"], [shell(AFT_SHELL, ("joint bulkhead",))])
    sheet(106, "Ring frames (three)", "Softwood 20 x 45 (pine, fir or similar, about 500 kg/m3)",
          ["Four members: bottom, two sides at 8 deg, top; half-lapped.",
           "Outer edge follows the inside of the hull; 45 wide all round.",
           "One on the transom (inside face), one on each joint bulkhead.",
           "Glue (thickened epoxy) and screw through the plywood from",
           "  outside every 150; 5 x 30 stainless screws.",
           "Joint frames: bolt holes at 75 and 250 each side, 28 up and",
           "  377 up; pins at 400 each side, 377 up.",
           "Nut plates on the aft joint frame's aft face (see joint 4)."],
          N["ring frame joint aft"], hull_aft)
    sheet(107, "Inwales (four)", "Softwood 20 x 40",
          ["Aft inwales 1,745 long; forward inwales 1,765 long.",
           "Top edge bevelled 8 deg to sit flush with the side's top edge.",
           "Glue and screw to the inside of the side panel from outside",
           "  every 150, ends butted to the ring frames (bow transom).",
           "Carry handle bolts (M6) pass down through the inwale.",
           "The rub strake screws go through the side into it.",
           "The bench module top bears up against its underside."],
          N["inwale aft port"], hull_aft, vs=flat_side(N["inwale aft port"]), iv=(30, -120))
    sheet(108, "Stringers and knuckle floor", "Softwood 40 x 20 and 40 x 45",
          ["Six stringers 40 x 20: three per half at the centreline and",
           "  150 each side; aft 1,745 long, forward 854 long.",
           "Glue flat to the floor, butted to the ring frames.",
           "Knuckle floor 40 long x 45 high across the boat at the",
           "  knuckle; underside cut to the two bottom slopes (12.5 deg).",
           "The skids are screwed from outside into the side stringers."],
          sel("stringer aft", "knuckle floor"), both)
    sheet(109, "Bench module (four)", "PE foam 50 mm layers, PVC tarpaulin 650 g/m2, softwood rail, webbing",
          ["Foam core: 50 layers stacked to 350, outboard edge bevelled",
           "  8 deg; 1,741 long aft, 850 long forward; 193 to 242 wide.",
           "Cover: sewn sleeve, laced ends; same as LevelHull modules.",
           "Rail 40 x 20 softwood glued and screwed to the floor along",
           "  the module's inboard foot, 330 from the centreline.",
           "Straps 50 webbing (three aft, two forward): screwed to the",
           "  inwale's inner face, over the module, down to the rail.",
           "Module top touches the underside of the inwale."],
          sel("bench rail aft port", "bench cover aft port", "bench straps aft port"), hull_aft)
    sheet(110, "Bow box: wall, deck, foam, eye pad", "6 mm okoume plywood, PE foam, hardwood pad",
          ["Wall 6 thick at 3,000 from the transom, cut to the rake and",
           f"  notched round the inwales; deck 591 x about {w(P['D'], P['t_side'] + P['inwale'][0]):,.0f}.",
           "Foam fills the box in 50 layers cut to the rake; cut round",
           "  the hardwood bow eye pad (20 x 120 x 80, glued to the",
           "  bow transom before the foam goes in).",
           "Deck glued to the inwales, bow transom and wall; taped."],
          sel("bow box wall", "bow deck", "bow foam", "bow eye pad"), hull_fwd)
    sheet(111, "Hinge rail and transom backing block", "Durable hardwood 40 x 60 and 20 x 60, 640 long",
          ["Rail 40 x 60 x 640 on the transom's outer face, bottom edge",
           "  100 above the hull bottom, centred.",
           "Backing block 20 x 60 x 640 on the inner face, same height,",
           "  between the ring frame's side members.",
           "Four M8 x 90 stainless bolts through rail, transom and block",
           "  at 110 and 280 each side, 130 up; bed in sealant.",
           "Hinge leaves screw to the rail top (60 wide)."],
          sel("hinge rail", "transom backing block"), hull_aft)
    sheet(112, "Step float", "Hardwood rim 20, 9 and 6 mm plywood decks, PE foam core",
          ["450 long x 600 wide x 90 deep; rim 20 x 75 hardwood, glued",
           "  and screwed at the corners.",
           "Foam core 410 x 560 x 75 in the rim; 6 deck below, 9 deck",
           "  on top; all glued with epoxy; non-slip coating on top.",
           "Front edge sits 40 behind the hinge rail (the gap keeps",
           "  fingers and feet clear as the step swings).",
           "Two strap hinges on top across the gap; pad eyes on top",
           "  near the aft corners; rung strap eyes on the aft face."],
          sel("step float"), hull_aft, iv=(22, -130))
    sheet(113, "Kick rung on straps", "Hardwood dowel 32 x 560, 25 mm webbing",
          ["Rung 32 diameter, 560 long, ends rounded.",
           "Two webbing straps sewn round the rung 230 each side of",
           "  the centre, other ends to eyes on the float's aft face.",
           "Rung hangs 270 below the underside of the float.",
           "Rolls up and clips on top of the float for carrying."],
          sel("kick rung"), hull_aft + [Part("Step float", sel("step float"), COL["ghost"])], iv=(18, -130))
    sheet(114, "Push pole (two sections)", "Aluminium tube 38 x 1.6, 1.5 m each",
          ["Two 1,500 sections joined by a 300 internal sleeve",
           "  (35 tube), riveted in one section, pinned in the other.",
           "Hardwood fork foot riveted into the lower end; rubber cap",
           "  on the top end.",
           "Each section stows on the aft floor between the stringers."],
          sel("push pole"), hull_aft)
    ql, qw, qh = P["quarter"]
    sheet(115, "Stern quarter foam module (two)", "PE foam 50 mm layers, PVC tarpaulin 650 g/m2, 50 mm webbing",
          [f"Foam core {ql:.0f} long x {qw:.0f} wide x {qh:.0f} high (15 L): six 50 layers",
           "  plus one 16 layer; no glue. Same sewn sleeve as the benches.",
           f"Stands {P['quarter_x']:.0f} forward of the transom, on the side stringer and the",
           f"  bench rail, inboard face {P['quarter_y']:.0f} off the centreline: 250 clear",
           "  between the two modules for the boarder's legs.",
           "Strap 50 webbing: screwed to the transom ring frame's top",
           "  member, over the module top, down its forward face and",
           "  screwed to the side stringer. Port and starboard alike."],
          sel("quarter cover port", "quarter foam port", "quarter strap port"), hull_aft, iv=(26, -130))


# ---------------------------------------------------------------- joints
def joints():
    # 1 chine: side on bottom, cut across at 900
    c = M.box(860, 900, 100, 700, -60, 160)
    bv.joint([Part("Bottom panel (cut)", N["bottom aft"] & c, COL["bottom"]),
              Part("Side panel (cut)", N["side aft port"] & c, COL["side"]),
              Part("Stringer (cut)", N["stringer aft port"] & c, COL["stringer"]),
              Part("Bench rail (cut)", N["bench rail aft port"] & c, COL["rail"]),
              Part("Module cover and foam (cut)", (N["bench cover aft port"].fuse(N["bench foam aft port"])) & c,
                   COL["cover"]),
              Part("Skid (cut)", N["skid aft port"] & c, COL["skid"])],
             OUT / "joint-01.png", "Joint 1: chine, stitched and glued",
             "Side edge outside the bottom edge; epoxy fillet inside, 100 mm glass tape inside and out", elev=10, azim=-10)
    # 2 transom corner with the ring frame
    c = M.box(-60, 250, 250, 700, -20, 450)
    bv.joint([Part("Bottom panel", N["bottom aft"] & c, COL["bottom"]),
              Part("Side panel", N["side aft port"] & c, COL["side"]),
              Part("Stern transom", N["stern transom"] & c, COL["transom"]),
              Part("Ring frame", N["ring frame transom"] & c, COL["frame"]),
              Part("Inwale", N["inwale aft port"] & c, COL["inwale"]),
              Part("Rub strake", N["rub strake aft port"] & c, COL["strake"])],
             OUT / "joint-02.png", "Joint 2: transom corner, from inside",
             "Transom between the sides, on the bottom; ring frame glued and screwed inside", elev=30, azim=-130)
    # 3 knuckle: cut along the boat at y = 300
    c = M.box(2550, 2860, 280, 320, -40, 120)
    bv.joint([Part("Forward flat bottom (cut)", N["bottom forward flat"] & c, COL["bottom"]),
              Part("Bow rake panel (cut)", N["bottom bow rake"] & c, COL["bottom"]),
              Part("Knuckle floor (cut)", N["knuckle floor"] & c, COL["stringer"]),
              Part("Side panel beyond", N["side forward port"] & M.box(2550, 2860, 300, 700, -40, 120), COL["side"])],
             OUT / "joint-03.png", "Joint 3: bottom knuckle, cut along the boat",
             "Butted panels on the knuckle floor; tape outside, fillet inside", elev=4, azim=-90)
    # 4 halves joint, cut through bolt at y = 250 (bottom row)
    y = 250.0
    c = M.box(1700, 1900, y, y + 60, -20, 120)
    b = M.joint_hardware(P)[0][3]
    bv.joint([Part("Aft ring frame (cut)", N["ring frame joint aft"] & c, COL["frame"]),
              Part("Aft bulkhead (cut)", N["joint bulkhead aft"] & c, COL["bulkhead"]),
              Part("Forward bulkhead (cut)", N["joint bulkhead forward"] & c, COL["bulkhead"]),
              Part("Forward ring frame (cut)", N["ring frame joint forward"] & c, COL["frame"]),
              Part("Bottom panels (cut)", (N["bottom aft"].fuse(N["bottom forward flat"])) & c, COL["bottom"]),
              Part("M10 bolt, washer, nut plate (cut)", b & c, COL["bolt"])],
             OUT / "joint-04.png", "Joint 4: the halves bolted together, cut through a bolt",
             "Bolt from the forward side into the welded nut plate; one 17 mm spanner", elev=8, azim=-90)
    # 5 bench module section: strap from inwale over the module to the rail
    xs = M.stations(P)["aft_in"]
    xstrap = xs[0] + (xs[1] - xs[0]) / 4
    c = M.box(xstrap - 25, xstrap + 25, 250, 700, -20, 450)
    bv.joint([Part("Side panel (cut)", N["side aft port"] & c, COL["side"]),
              Part("Bottom (cut)", N["bottom aft"] & c, COL["bottom"]),
              Part("Inwale (cut)", N["inwale aft port"] & c, COL["inwale"]),
              Part("Rub strake (cut)", N["rub strake aft port"] & c, COL["strake"]),
              Part("Cover (cut)", N["bench cover aft port"] & c, COL["cover"]),
              Part("Foam core (cut)", N["bench foam aft port"] & c, COL["foam"]),
              Part("Strap (cut)", N["bench straps aft port"] & c, COL["strap"]),
              Part("Bench rail (cut)", N["bench rail aft port"] & c, COL["rail"])],
             OUT / "joint-05.png", "Joint 5: bench module, cut across at a strap",
             "Module tight under the inwale; strap screwed to the inwale and the rail", elev=6, azim=-12)
    # 6 hinge rail bolts and the step hinge, cut along the boat at y = 200 (hinge) and 280 (bolt)
    c = M.box(-560, 60, 150, 290, 40, 220)
    bv.joint([Part("Stern transom (cut)", N["stern transom"] & c, COL["transom"]),
              Part("Backing block (cut)", N["transom backing block"] & c, COL["rail"]),
              Part("Hinge rail (cut)", N["hinge rail"] & c, COL["rail"]),
              Part("M8 bolt (cut)", N["rail bolts M8"] & c, COL["bolt"]),
              Part("Strap hinge", (N["strap hinges (rail leaves)"].fuse(N["strap hinges (float leaves)"])) & c,
                   COL["hinge"]),
              Part("Step float (cut)", sel("step float") & c, COL["step"])],
             OUT / "joint-06.png", "Joint 6: hinge rail and step hinge, cut along the boat",
             "40 mm gap between rail and float; hinge pin over the gap; M8 bolts through rail, transom, block",
             elev=6, azim=-90)
    # 7 step swung down to its stop (stop straps tight) and folded up for carrying
    dn = M.step_parts(P, swing=P["stop_deg"])
    bv.joint([Part("Transom and rail", M.flat([N["stern transom"], N["hinge rail"]]) & M.box(-700, 40, -400, 400, -400, 450),
                   COL["transom"]),
              Part("Step float at its 20 deg stop", M.flat([dn[k][1] for k in dn if k.startswith("step float")]), COL["step"]),
              Part("Kick rung", M.flat([dn["kick rung"][1], dn["kick rung straps"][1]]), COL["rung"]),
              Part("Stop strap, taut at the stop", dn["stop straps"][1], COL["strap"])],
             OUT / "joint-07.png", "Joint 7: the step at its stop, from the side",
             "Stop straps from the transom pad eyes hold the float 20 deg below level", elev=4, azim=-90)
    # 8 bow eye through the bow transom and pad, cut at y = 25
    c = M.box(3480, 3700, 25, 120, 240, 420)
    bv.joint([Part("Bow transom (cut)", N["bow transom"] & c, COL["transom"]),
              Part("Hardwood pad (cut)", N["bow eye pad"] & c, COL["rail"]),
              Part("Bow foam (cut)", N["bow foam"] & c, COL["foam"]),
              Part("Bow deck (cut)", N["bow deck"] & c, COL["box"]),
              Part("U-bolt and nuts (cut)", N["bow eye"] & c, COL["eye"])],
             OUT / "joint-08.png", "Joint 8: bow eye, cut through one leg",
             "U-bolt through the bow transom and pad; nuts inside, fitted before the foam", elev=8, azim=-90)
    # 9 stern quarter module, cut along the boat through its strap
    yq = P["quarter_y"] + P["strap"][0] / 2
    c = M.box(-20, 420, yq - 10, yq + 10, -20, 450)
    bv.joint([Part("Stern transom (cut)", N["stern transom"] & c, COL["transom"]),
              Part("Ring frame (cut)", N["ring frame transom"] & c, COL["frame"]),
              Part("Bottom (cut)", N["bottom aft"] & c, COL["bottom"]),
              Part("Side stringer (cut)", N["stringer aft port"] & c, COL["stringer"]),
              Part("Cover (cut)", N["quarter cover port"] & c, COL["cover"]),
              Part("Foam core (cut)", N["quarter foam port"] & c, COL["foam"]),
              Part("Strap (cut)", N["quarter strap port"] & c, COL["strap"])],
             OUT / "joint-09.png", "Joint 9: stern quarter module, cut along the boat at its strap",
             "Strap screwed to the transom ring frame, over the module, down to the side stringer", elev=6, azim=-90)


# ---------------------------------------------------------------- steps
def steps():
    def p(name, shape, col, ex):
        return Part(name, shape, col, None, ex)

    a = "aft"
    bot = p("Aft bottom panel", N["bottom aft"], COL["bottom"], (0, 0, -300))
    sides = p("Aft side panels", sel("side aft"), COL["side"], (0, 0, 300))
    tr = p("Stern transom", N["stern transom"], COL["transom"], (-400, 0, 0))
    bh = p("Aft joint bulkhead", N["joint bulkhead aft"], COL["bulkhead"], (400, 0, 0))
    rf = p("Ring frames", sel("ring frame transom", "ring frame joint aft"), COL["frame"], (0, 0, 450))
    iw = p("Inwales", sel("inwale aft"), COL["inwale"], (0, 0, 400))
    st = p("Stringers and bench rails", sel("stringer aft", "bench rail aft"), COL["stringer"], (0, 0, 400))
    sk = p("Skids and rub strakes", sel("skid aft", "rub strake aft"), COL["skid"], (0, 0, -350))
    bm = p("Bench modules with straps", sel("bench cover aft", "bench foam aft", "bench straps aft"), COL["cover"],
           (0, 0, 450))
    qm = p("Stern quarter modules with straps", sel("quarter"), COL["quarter"], (-300, 0, 450))
    rl = p("Hinge rail, backing block, M8 bolts", sel("hinge rail", "transom backing block", "rail bolts"), COL["rail"],
           (-350, 0, 0))
    fl = p("Step float and hinges", sel("step float", "strap hinges"), COL["step"], (-450, 0, 250))
    sp = p("Stop straps, pad eyes, kick rung", sel("stop straps", "float pad eyes", "transom pad eyes", "kick rung"),
           COL["rung"], (-350, 0, -200))
    hd = p("Grab and carry handles", sel("transom grab handles", "carry handles aft"), COL["handle"], (0, 0, 350))
    seq = [
        ([], [bot, sides], "Step 1: stitch the aft bottom and sides",
         "Sides outside the bottom edges, stitched every 150 mm; check the diagonals are equal"),
        ([bot, sides], [tr, bh], "Step 2: fit the stern transom and the aft joint bulkhead",
         "Both sit on the bottom between the sides; tack with fillets, then tape inside"),
        ([bot, sides, tr, bh], [rf], "Step 3: glue in the ring frames",
         "Transom frame and joint frame, glued and screwed through the plywood"),
        ([bot, sides, tr, bh, rf], [iw], "Step 4: fit the inwales",
         "Inside the top of each side, frame to frame; top edges flush"),
        ([bot, sides, tr, bh, rf, iw], [st], "Step 5: glue down the stringers and bench rails",
         "Three stringers and two bench rails on the floor, butted to the frames"),
        ([bot, sides, tr, bh, rf, iw, st], [sk], "Step 6: glass the outside, then fit skids and strakes",
         "Turn the half over: glass the bottom and sides, then screw the skids into the stringers"),
    ]
    k = 0
    for done, new, title, sub in seq:
        k += 1
        bv.step(done, new, OUT / f"step-{k:02d}.png", title, sub, elev=26, azim=-58, label_done=False)
    # forward half
    fwd_shell = p("Forward bottom panels and sides", M.flat([sel("bottom forward", "bottom bow"), sel("side forward")]),
                  COL["side"], (0, 0, 300))
    fwd_ends = p("Bow transom, joint bulkhead, knuckle floor",
                 sel("bow transom", "joint bulkhead forward", "knuckle floor"), COL["transom"], (0, 0, 400))
    fwd_in = p("Ring frame, inwales, stringers, bench rails",
               sel("ring frame joint forward", "inwale forward", "stringer forward", "bench rail forward"), COL["frame"],
               (0, 0, 400))
    bow = p("Bow eye pad, bow eye, bow foam, wall and deck", sel("bow eye pad", "bow eye", "bow foam", "bow box wall",
                                                                "bow deck"), COL["box"], (0, 0, 450))
    fwd_out = p("Skids, rub strakes, bench modules, carry handles",
                sel("skid forward", "rub strake forward", "bench cover forward", "bench foam forward",
                    "bench straps forward", "carry handles forward"), COL["cover"], (0, 0, 450))
    k += 1
    bv.step([], [fwd_shell, fwd_ends], OUT / f"step-{k:02d}.png", "Step 7: build the forward half the same way",
            "Bottom panels butted at the knuckle on the knuckle floor; bow transom on the rake", elev=26, azim=-58)
    k += 1
    bv.step([fwd_shell, fwd_ends], [fwd_in, bow], OUT / f"step-{k:02d}.png",
            "Step 8: frame the forward half and close the bow box",
            "Bow eye and pad before the foam; foam layers, then the deck glued on", elev=26, azim=-58, label_done=False)
    k += 1
    bv.step([fwd_shell, fwd_ends, fwd_in, bow], [fwd_out], OUT / f"step-{k:02d}.png",
            "Step 9: glass, skids, strakes, bench modules and handles",
            "As steps 6 and 10 to 11 on the aft half", elev=26, azim=-58, label_done=False)
    aft_done = [bot, sides, tr, bh, rf, iw, st, sk]
    for title, sub, new, az in (
            ("Step 10: strap in the aft bench and stern quarter modules",
             "Benches tight under the inwale; quarter modules strapped to the transom frame and stringers",
             [bm, qm], -58),
            ("Step 11: fit the grab and carry handles", "M6 bolts down through the inwales; transom handles through the frame",
             [hd], -58),
            ("Step 12: bolt on the hinge rail", "Four M8 bolts through rail, transom and backing block, bedded in sealant",
             [rl], -130),
            ("Step 13: hang the step float", "Hinge leaves on the rail top and the float top; 40 mm gap", [fl], -130),
            ("Step 14: fit the stop straps and the kick rung", "Float stops 20 deg below level; rung 270 mm below it",
             [sp], -130)):
        k += 1
        bv.step(aft_done, new, OUT / f"step-{k:02d}.png", title, sub, elev=24, azim=az, label_done=False)
        aft_done = aft_done + new
    # join the halves
    aft_all = Part("Aft half, complete", M.flat([s for n, s in N.items() if H[n] in (a, "step") or
                                                 (H[n] == "outfit" and n in ("transom grab handles", "carry handles aft"))]),
                   COL["ghost"])
    fwd_all = p("Forward half", M.flat([s for n, s in N.items() if H[n] == M.FWD or n in ("carry handles forward",
                                                                                          "bow eye", "bow line, coiled")]),
                COL["side"], (600, 0, 0))
    bolts = p("Eight M10 bolts and two pins", sel("joint bolt", "alignment pin"), COL["bolt"], (0, 0, 600))
    k += 1
    bv.step([aft_all], [fwd_all], OUT / f"step-{k:02d}.png", "Step 15: bring the halves together",
            "Pins into their holes, bulkhead faces touching", elev=26, azim=-58, label_done=False)
    k += 1
    bv.step([aft_all, Part("Forward half", fwd_all.shape, COL["ghost"])], [bolts], OUT / f"step-{k:02d}.png",
            "Step 16: bolt the halves together", "Bottom row first, then top; snug with one 17 mm spanner",
            elev=30, azim=-58, label_done=False)
    k += 1
    gear = p("Pole sections, paddles, bow line", sel("push pole", "paddles", "bow line"), COL["paddle"], (0, 0, 600))
    bv.step([aft_all, Part("Forward half", fwd_all.shape, COL["ghost"]), Part("Bolts", bolts.shape, COL["ghost"])],
            [gear], OUT / f"step-{k:02d}.png", "Step 17: stow the pole, paddles and bow line",
            "Pole sections on the aft floor, paddles on the aft benches, line on the bow deck",
            elev=30, azim=-58, label_done=False)


if __name__ == "__main__":
    what = sys.argv[1:] or ["overview", "sheets", "joints", "steps"]
    for w in what:
        globals()[w]()
        print("done", w)
