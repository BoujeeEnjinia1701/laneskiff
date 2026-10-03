"""LaneSkiff parametric model (build123d), TRL 3, constructable design (LSK-DDR-002).

Run from the repo root:  python cad/src/model.py [--check] [--export]
  --check   run the constructability checks (overlaps, contacts, bolt paths, step swing, beam)
  --export  write cad/step/*.step and cad/stl/*.stl

A flat-bottomed punt-form skiff in two rigid halves, plywood and epoxy build path (stitch and glue).
Each half is a closed box: its own end panel (transom or bow transom) and its own joint bulkhead,
so each half floats on its own and the joint between them needs no seal. The halves bolt together
through hardwood ring frames on the two joint bulkheads (eight M10 bolts into tee nuts).

Coordinates in mm. X along the boat from the outer face of the stern transom (x = 0) to the bow
(x = 3,600); Y across, port side positive; Z up from the outside of the bottom (z = 0). Hull sides
are flat panels flared outward by 8 deg. The bottom is flat to the knuckle at x = 2,700 and rakes
up to 200 mm at the bow.

Components (BOM line numbers in brackets, see bom/bom.csv):
  [1]  bottom panels, 6 mm plywood (aft, forward flat, bow rake)
  [2]  side panels, 6 mm plywood (4)
  [3]  stern transom, 9 mm plywood        [4]  bow transom, 9 mm plywood
  [5]  joint bulkheads, 6 mm plywood (2)  [6]  ring frames, hardwood 20 x 45 (transom, two joint frames)
  [7]  inwales, hardwood 20 x 40 (4)      [8]  bottom stringers, hardwood 40 x 20 (6), knuckle floor
  [9]  bench modules: hardwood bench rails, tarpaulin covers, webbing straps; bow box wall and deck, 6 mm plywood
  [10] buoyancy foam, closed-cell polyethylene (LevelHull layout: outboard benches and bow box)
  [11] joint bolts M10 x 80 into welded nut plates (8), alignment pins (2)
  [12] rub strakes, HDPE 12 x 30 (4)      [13] bottom skids, HDPE 40 x 8 (4)
  [14] stern step: hinge rail, transom backing block, M8 bolts, float (rim, decks, foam), strap hinges
  [15] step stop straps and pad eyes      [16] kick rung on straps
  [17] transom grab handles (2)           [18] carry handles (8)
  [19] push pole, two 1.5 m sections      [20] paddles (2)
  [21] bow eye, backing pad and bow line
CONCEPT, NOT FOR FABRICATION.
"""
import math
import sys
from pathlib import Path

from build123d import (Axis, Box, Compound, Cylinder, Face, Pos, Rot, Torus, Vector, Wire,
                       extrude, export_step, export_stl)

ROOT = Path(__file__).resolve().parents[2]

PARAMS = {
    "L": 3600.0,            # overall length of the hull (bow transom outer face)
    "x_joint": 1800.0,      # joint plane between the halves (faces of the two bulkheads)
    "knuckle": 2700.0,      # bottom knuckle, start of the bow rake
    "rise": 200.0,          # bottom height at the bow
    "D": 400.0,             # side height (sheer), constant
    "half_bot": 500.0,      # outer half width of the bottom at the chine
    "flare_deg": 8.0,       # side flare from vertical
    "t_bot": 6.0, "t_side": 6.0, "t_transom": 9.0, "t_bow": 9.0, "t_bh": 6.0,
    "cover_t": 2.0, "t_box": 6.0,
    "bench_rail": (40.0, 20.0),   # hardwood rail on the floor along the inboard foot of each bench module
    "strap": (50.0, 2.5), "straps_aft": 3, "straps_fwd": 2,
    "frame": (20.0, 45.0),      # ring frames: thickness along the boat, member width
    "inwale": (20.0, 40.0),     # thickness square to the side, height
    "stringer": (40.0, 20.0),   # width, height
    "stringer_y": 150.0,
    "floor": (40.0, 45.0),      # knuckle floor: length along the boat, height
    "bench_y": 330.0,           # inboard face of the bench modules from the centreline
    "bench_top": 360.0,         # bench top, level with the underside of the inwale
    "bench_fwd_end": 2680.0,    # forward bench boxes stop at the knuckle floor
    "bow_box_x": 3000.0,        # aft face of the bow box wall
    "strake": (12.0, 30.0),     # HDPE rub strake: thickness, height
    "skid": (40.0, 8.0),        # HDPE skid: width, thickness
    "joint_bolts": [(-250.0, "b"), (-75.0, "b"), (75.0, "b"), (250.0, "b"),
                    (-250.0, "t"), (-100.0, "t"), (100.0, "t"), (250.0, "t")],
    "pins_y": (-400.0, 400.0),
    # stern step (hinged float with a hanging kick rung)
    "rail": (40.0, 60.0, 640.0, 100.0),    # thickness aft of the transom, height, length, bottom edge z
    "gap": 40.0,                           # rail to float gap
    "float": (450.0, 600.0, 90.0, 70.0),   # length (aft), width, depth, bottom z when deployed
    "float_rim": 20.0, "float_top": 9.0, "float_bot": 6.0,
    "hinge_y": (-200.0, 200.0),
    "stop_deg": 20.0,                      # step swings at most this far below level (stop straps)
    "rung_drop": 270.0,                    # rung centre below the float bottom
    "rung": (16.0, 560.0),                 # radius, length
    "rail_bolts_y": (-280.0, -110.0, 110.0, 280.0),
    "grab_y": (-250.0, 250.0), "grab": (250.0, 120.0),
    "carry_x": [300.0, 1550.0, 2050.0, 3300.0], "carry": (200.0, 50.0),
    "pole": (19.0, 1500.0), "paddle": (1400.0, 160.0, 12.0, 450.0),
}

AFT, FWD = "aft", "fwd"


# ---------------------------------------------------------------- geometry helpers
def tf(p=PARAMS):
    a = math.radians(p["flare_deg"])
    return math.tan(a), math.cos(a)


def half(z, d=0.0, p=PARAMS):
    """Half width at height z of the plane offset d (square to the side) inward from the outside."""
    t, c = tf(p)
    return p["half_bot"] + z * t - d / c


def zb(x, p=PARAMS):
    """Height of the outside of the bottom at x."""
    k, L = p["knuckle"], p["L"]
    return 0.0 if x <= k else p["rise"] * (x - k) / (L - k)


def ztop_bottom(x, p=PARAMS):
    return zb(x, p) + p["t_bot"]


def trap(d, z0, z1, p=PARAMS):
    return [(-half(z0, d, p), z0), (half(z0, d, p), z0), (half(z1, d, p), z1), (-half(z1, d, p), z1)]


def yz_x(poly, x0, x1):
    """Prism of a (y, z) polygon from x0 to x1."""
    w = Wire.make_polygon([Vector(x0, y, z) for y, z in poly], close=True)
    return extrude(Face(w), amount=x1 - x0, dir=(1, 0, 0))


def xz_y(poly, y0=-900.0, y1=900.0):
    """Prism of an (x, z) polygon from y0 to y1."""
    w = Wire.make_polygon([Vector(x, y0, z) for x, z in poly], close=True)
    return extrude(Face(w), amount=y1 - y0, dir=(0, 1, 0))


def rect_xz(x0, x1, z0, z1):
    return [(x0, z0), (x1, z0), (x1, z1), (x0, z1)]


def inner(x0, x1, p=PARAMS, z0=-20.0, z1=None):
    """Space between the inner faces of the side panels."""
    return yz_x(trap(p["t_side"], z0, (z1 or p["D"] + 20), p), x0, x1)


def box(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)


def flat(shapes):
    """One compound of every solid in shapes (nested compounds report no volume)."""
    sol = []
    for s in shapes:
        sol += list(s.solids()) if hasattr(s, "solids") else [s]
    return Compound(sol)


def rod(a, b, r):
    a, b = Vector(*a), Vector(*b)
    v = b - a
    L = v.length
    c = Cylinder(r, L)
    z = Vector(0, 0, 1)
    ax = z.cross(v)
    if ax.length < 1e-9:
        rot = c if v.Z > 0 else Rot(180, 0, 0) * c
    else:
        ang = math.degrees(math.acos(max(-1, min(1, z.dot(v) / L))))
        rot = c.rotate(Axis((0, 0, 0), (ax.X, ax.Y, ax.Z)), ang)
    return Pos(*(a + v * 0.5)) * rot


def port_stbd_split(shape):
    big = 2000.0
    return shape & box(-500, 4200, 0, big, -500, 900), shape & box(-500, 4200, -big, 0, -500, 900)


def mirror_y(shape):
    from build123d import Plane, mirror
    return mirror(shape, about=Plane.XZ)


# ---------------------------------------------------------------- derived x stations
def stations(p=PARAMS):
    fx, fw = p["frame"]
    xj = p["x_joint"]
    tt, tbh, tbw = p["t_transom"], p["t_bh"], p["t_bow"]
    return {
        "transom": (0.0, tt), "tframe": (tt, tt + fx),
        "bh_aft": (xj - tbh, xj), "fr_aft": (xj - tbh - fx, xj - tbh),
        "bh_fwd": (xj, xj + tbh), "fr_fwd": (xj + tbh, xj + tbh + fx),
        "bow": (p["L"] - tbw, p["L"]),
        "floor": (p["knuckle"] - p["floor"][0] / 2, p["knuckle"] + p["floor"][0] / 2),
        "aft_in": (tt + fx, xj - tbh - fx), "fwd_in": (xj + tbh + fx, p["L"] - tbw),
    }


# ---------------------------------------------------------------- hull halves
def hull_parts(p=PARAMS):
    """Every made hull piece of both halves: dict name -> (half, BOM line, shape)."""
    S = stations(p)
    D, tb, ts = p["D"], p["t_bot"], p["t_side"]
    L, K, xj = p["L"], p["knuckle"], p["x_joint"]
    fx, fw = p["frame"]
    out = {}

    def add(name, half_, bom, shape):
        out[name] = (half_, bom, shape)

    # [1] bottom panels, between the side panels
    add("bottom aft", AFT, 1, xz_y(rect_xz(0, xj, 0, tb)) & inner(0, xj, p))
    add("bottom forward flat", FWD, 1, xz_y(rect_xz(xj, K, 0, tb)) & inner(xj, K, p))
    add("bottom bow rake", FWD, 1, xz_y([(K, 0), (L, p["rise"]), (L, p["rise"] + tb), (K, tb)]) & inner(K, L, p))
    # [2] side panels, full length of each half, bottom edge to the sheer
    wall = yz_x(trap(0, 0, D, p), -10, L + 10) - yz_x(trap(ts, -10, D + 10, p), -20, L + 20)
    prof_a = xz_y(rect_xz(0, xj, 0, D))
    prof_f = xz_y([(xj, 0), (K, 0), (L, p["rise"]), (L, D), (xj, D)])
    for half_, prof, tag in ((AFT, prof_a, "aft"), (FWD, prof_f, "forward")):
        sp, ss = port_stbd_split(wall & prof)
        add(f"side {tag} port", half_, 2, sp)
        add(f"side {tag} starboard", half_, 2, ss)
    # [3] stern transom and [4] bow transom, on the bottom between the sides
    x0, x1 = S["transom"]
    add("stern transom", AFT, 3, xz_y(rect_xz(x0, x1, tb, D)) & inner(x0, x1, p))
    x0, x1 = S["bow"]
    add("bow transom", FWD, 4, xz_y([(x0, ztop_bottom(x0, p)), (x1, ztop_bottom(x1, p)), (x1, D), (x0, D)])
        & inner(x0, x1, p))
    # [5] joint bulkheads
    for key, half_, tag in (("bh_aft", AFT, "aft"), ("bh_fwd", FWD, "forward")):
        x0, x1 = S[key]
        add(f"joint bulkhead {tag}", half_, 5, xz_y(rect_xz(x0, x1, tb, D)) & inner(x0, x1, p))
    # [6] ring frames (hardwood 20 x 45 members round the inside of the transom and both bulkheads)
    for key, half_, tag in (("tframe", AFT, "transom"), ("fr_aft", AFT, "joint aft"), ("fr_fwd", FWD, "joint forward")):
        x0, x1 = S[key]
        ring = (xz_y(rect_xz(x0, x1, tb, D)) & inner(x0, x1, p)) - yz_x(trap(ts + fw, tb + fw, D - fw, p), x0 - 1, x1 + 1)
        add(f"ring frame {tag}", half_, 6, ring)
    # [7] inwales, inside the top of each side panel, frame to frame (to the bow transom forward)
    iw, ih = p["inwale"]
    for half_, (x0, x1), tag in ((AFT, S["aft_in"], "aft"), (FWD, S["fwd_in"], "forward")):
        band = yz_x(trap(ts, D - ih, D, p), x0, x1) - yz_x(trap(ts + iw, D - ih - 1, D + 1, p), x0 - 1, x1 + 1)
        ip, is_ = port_stbd_split(band)
        add(f"inwale {tag} port", half_, 7, ip)
        add(f"inwale {tag} starboard", half_, 7, is_)
    # [8] bottom stringers (two per half) and the knuckle floor
    sw, sh = p["stringer"]
    for half_, (x0, x1), tag in ((AFT, S["aft_in"], "aft"), (FWD, (S["fwd_in"][0], S["floor"][0]), "forward")):
        for sy, side in ((p["stringer_y"], "port"), (0.0, "centre"), (-p["stringer_y"], "starboard")):
            add(f"stringer {tag} {side}", half_, 8, box(x0, x1, sy - sw / 2, sy + sw / 2, tb, tb + sh))
    f0, f1 = S["floor"]
    fh = p["floor"][1]
    add("knuckle floor", FWD, 8, xz_y([(f0, tb), (K, tb), (f1, ztop_bottom(f1, p)), (f1, tb + fh), (f0, tb + fh)])
        & inner(f0, f1, p))
    # [9] bench modules (LevelHull layout): foam cores in sewn tarpaulin covers, outboard on both sides of both
    # halves, held under the inwale by the inwale itself and by webbing straps to a hardwood bench rail on the floor
    by, bt, ct = p["bench_y"], p["bench_top"], p["cover_t"]
    rw, rh = p["bench_rail"]
    sw_, st_ = p["strap"]
    iw = p["inwale"][0]
    for half_, (x0, x1), tag, ns in ((AFT, S["aft_in"], "aft", p["straps_aft"]),
                                     (FWD, (S["fwd_in"][0], p["bench_fwd_end"]), "forward", p["straps_fwd"])):
        env = yz_x([(by, tb), (half(tb, ts, p), tb), (half(bt, ts, p), bt), (by, bt)], x0, x1)
        core = yz_x([(by + ct, tb + ct), (half(tb + ct, ts + ct, p), tb + ct), (half(bt - ct, ts + ct, p), bt - ct),
                     (by + ct, bt - ct)], x0 + ct, x1 - ct)
        rail = box(x0, x1, by - rw, by, tb, tb + rh)
        straps = []
        for k in range(ns):
            xs = x0 + (x1 - x0) * (k + 1) / (ns + 1)
            a, b = xs - sw_ / 2, xs + sw_ / 2
            yi = half(bt + st_, ts + iw, p)
            top_band = yz_x([(by - st_, bt), (half(bt, ts + iw, p), bt), (yi, bt + st_), (by - st_, bt + st_)], a, b)
            straps += [top_band, box(a, b, by - st_, by, tb + rh, bt), box(a, b, by - rw, by - st_, tb + rh, tb + rh + st_)]
        strap = straps[0]
        for q in straps[1:]:
            strap = strap.fuse(q)
        for side, f in (("port", lambda s_: s_), ("starboard", mirror_y)):
            add(f"bench rail {tag} {side}", half_, 9, f(rail))
            add(f"bench cover {tag} {side}", half_, 9, f(env - core))
            add(f"bench foam {tag} {side}", half_, 10, f(core))
            add(f"bench straps {tag} {side}", half_, 9, f(strap))
    # bow box: aft wall and deck (6 mm plywood) closing the foam block under the bow deck
    tbx = p["t_box"]
    bx = p["bow_box_x"]
    xb1 = S["bow"][0]
    inw = Compound([v[2] for k, v in out.items() if k.startswith("inwale forward")])
    wall_b = (xz_y([(bx, ztop_bottom(bx, p)), (bx + tbx, ztop_bottom(bx + tbx, p)), (bx + tbx, D - tbx), (bx, D - tbx)])
              & inner(bx, bx + tbx, p)) - inw
    deck = (xz_y(rect_xz(bx, xb1, D - tbx, D)) & inner(bx, xb1, p)) - inw
    add("bow box wall", FWD, 9, wall_b)
    add("bow deck", FWD, 9, deck)
    # bow eye backing pad (hardwood) inside the bow transom, cut out of the bow foam
    pad = box(xb1 - 20, xb1, -60, 60, 290, 370)
    add("bow eye pad", FWD, 21, pad)
    bow_foam = (xz_y([(bx + tbx, ztop_bottom(bx + tbx, p)), (xb1, ztop_bottom(xb1, p)), (xb1, D - tbx), (bx + tbx, D - tbx)])
                & inner(bx + tbx, xb1, p)) - inw - pad
    add("bow foam", FWD, 10, bow_foam)
    # [12] rub strakes outside the sheer, [13] skids under the bottom
    so, sh2 = p["strake"]
    st = yz_x(trap(-so, D - sh2, D, p), -1, L + 1) - yz_x(trap(0, D - sh2 - 1, D + 1, p), -2, L + 2)
    for half_, (x0, x1), tag in ((AFT, (0, xj), "aft"), (FWD, (xj, L), "forward")):
        sp, ss = port_stbd_split(st & box(x0, x1, -900, 900, 0, 600))
        add(f"rub strake {tag} port", half_, 12, sp)
        add(f"rub strake {tag} starboard", half_, 12, ss)
    kw, kt = p["skid"]
    for sy, side in ((p["stringer_y"], "port"), (-p["stringer_y"], "starboard")):
        y0, y1 = sy - kw / 2, sy + kw / 2
        add(f"skid aft {side}", AFT, 13, xz_y(rect_xz(0, xj, -kt, 0), y0, y1))
        add(f"skid forward {side}", FWD, 13,
            xz_y([(xj, -kt), (K, -kt), (L, p["rise"] - kt), (L, p["rise"]), (K, 0), (xj, 0)], y0, y1))
    return out


# ---------------------------------------------------------------- joint hardware
def joint_hardware(p=PARAMS):
    """Eight M10 x 80 hex bolts (heads forward) into captive nut plates on the aft ring frame, two alignment pins.
    A nut plate is a 40 x 40 x 3 mm steel plate with an M10 nut welded on, screwed to the frame's aft face, so the
    halves are joined with one spanner from the forward side."""
    S = stations(p)
    fw = p["frame"][1]
    a0 = S["fr_aft"][0]
    f1 = S["fr_fwd"][1]
    zbot = p["t_bot"] + fw / 2
    ztop = p["D"] - fw / 2
    bolts = []
    for y, row in p["joint_bolts"]:
        z = zbot if row == "b" else ztop
        shank = rod((a0 - 11, y, z), (f1 + 7, y, z), 5.0)
        head = Pos(f1 + 2 + 6.4 / 2 + 1, y, z) * Rot(0, 90, 0) * Cylinder(8.5, 6.4)
        washer = Pos(f1 + 1, y, z) * Rot(0, 90, 0) * Cylinder(10.5, 2.0)
        plate = box(a0 - 3, a0, y - 20, y + 20, z - 20, z + 20)
        nut = Pos(a0 - 3 - 4, y, z) * Rot(0, 90, 0) * Cylinder(8.5, 8.0)
        bolts.append(Compound([shank, head, washer, plate, nut]))
    pins = [rod((a0 + 2, y, ztop), (f1 - 2, y, ztop), 6.0) for y in p["pins_y"]]
    return bolts, pins


# ---------------------------------------------------------------- stern step
def step_parts(p=PARAMS, swing=0.0):
    """Stern boarding step. swing: degrees the float is turned down (+) or up (-) about the hinge.
    Returns dict name -> (BOM line, shape). The rail, backing block and rail bolts never move."""
    rt, rh, rl, rz = p["rail"]
    tt, fx = p["t_transom"], p["frame"][0]
    fl, fwid, fd, fz = p["float"]
    rim, ttop, tbot = p["float_rim"], p["float_top"], p["float_bot"]
    xf1 = -rt - p["gap"]           # float front face
    xf0 = xf1 - fl                 # float aft face
    ztop = fz + fd
    hx, hz = -rt - p["gap"] / 2, ztop + 5.0     # hinge pin axis, over the gap
    out = {}
    out["hinge rail"] = (14, box(-rt, 0, -rl / 2, rl / 2, rz, rz + rh))
    out["transom backing block"] = (14, box(tt, tt + fx, -rl / 2, rl / 2, rz, rz + rh))
    bolts = []
    for y in p["rail_bolts_y"]:
        zc = rz + rh / 2
        shank = rod((-rt - 4, y, zc), (tt + fx + 9, y, zc), 4.0)
        head = Pos(-rt - 3, y, zc) * Rot(0, 90, 0) * Cylinder(6.5, 5.3)
        nut = Pos(tt + fx + 4, y, zc) * Rot(0, 90, 0) * Cylinder(7.0, 7.0)
        bolts.append(Compound([shank, head, nut]))
    out["rail bolts M8"] = (14, flat(bolts))
    # float: hardwood rim, 9 mm top deck, 6 mm bottom deck, foam core
    yh = fwid / 2
    outer = box(xf0, xf1, -yh, yh, fz + tbot, ztop - ttop)
    hole = box(xf0 + rim, xf1 - rim, -yh + rim, yh - rim, fz, ztop)
    mov = {
        "step float rim": (14, outer - hole),
        "step float top deck": (14, box(xf0, xf1, -yh, yh, ztop - ttop, ztop)),
        "step float bottom deck": (14, box(xf0, xf1, -yh, yh, fz, fz + tbot)),
        "step float foam": (10, box(xf0 + rim, xf1 - rim, -yh + rim, yh - rim, fz + tbot, ztop - ttop)),
    }
    # strap hinges: leaf on the rail top, knuckle over the gap, leaf on the float top deck
    hinges_fixed, hinges_mov = [], []
    for y in p["hinge_y"]:
        hinges_fixed.append(box(hx, -5, y - 50, y + 50, rz + rh, rz + rh + 2))
        hinges_fixed.append(Pos(hx, y, hz) * Rot(90, 0, 0) * Cylinder(5.0, 100))
        hinges_mov.append(box(xf1 - 140, hx - 6, y - 50, y + 50, ztop, ztop + 2))
    out["strap hinges (rail leaves)"] = (14, Compound(hinges_fixed))
    mov["strap hinges (float leaves)"] = (14, Compound(hinges_mov))
    # pad eyes on the float for the stop straps (top) and the rung straps (aft face)
    pe = []
    for y in (-270.0, 270.0):
        pe.append(box(xf0 + 15, xf0 + 55, y - 12, y + 12, ztop, ztop + 8))
    mov["float pad eyes"] = (15, Compound(pe))
    # kick rung on two straps from the float's aft face
    rr, rlen = p["rung"]
    zr = fz - p["rung_drop"]
    xr = xf0 - 12
    rung_straps = [box(xr - 3, xr + 3, y - 12, y + 12, zr + rr, fz + 40) for y in (-230.0, 230.0)]
    mov["kick rung straps"] = (16, Compound(rung_straps))
    mov["kick rung"] = (16, Pos(xr, 0, zr) * Rot(90, 0, 0) * Cylinder(rr, rlen))
    # turn the moving parts about the hinge axis
    if swing:
        ax = Axis((hx, 0, hz), (0, 1, 0))
        mov = {k: (b, s.rotate(ax, -swing)) for k, (b, s) in mov.items()}   # +swing turns the aft edge down
    out.update(mov)
    # stop straps: transom pad eyes (fixed) to the float pad eyes (deployed position)
    tp = []
    for y in (-270.0, 270.0):
        tp.append(box(-10, 0, y - 12, y + 12, 360, 400))
    out["transom pad eyes"] = (15, Compound(tp))
    # stop straps run to the float pad eyes wherever the float is (taut at the stop, slack when level)
    a = math.radians(-swing)
    dx, dz = xf0 + 35 - hx, ztop + 12 - hz
    ex, ez = hx + dx * math.cos(a) + dz * math.sin(a), hz - dx * math.sin(a) + dz * math.cos(a)
    sts = [rod((-14, y, 380), (ex, y, ez), 3.5) for y in (-270.0, 270.0)]
    out["stop straps"] = (15, Compound(sts))
    return out


def hinge_axis(p=PARAMS):
    rt = p["rail"][0]
    fl, fwid, fd, fz = p["float"]
    return -rt - p["gap"] / 2, fz + fd + 5.0


# ---------------------------------------------------------------- handles, outfit
def outfit_parts(p=PARAMS):
    D, ts = p["D"], p["t_side"]
    out = {}
    # [17] transom grab handles: stainless U on the transom top (transom and frame, 32 mm wide)
    gl, gh = p["grab"]
    xc = (p["t_transom"] + p["frame"][0]) / 2
    gs = []
    for yc in p["grab_y"]:
        a, b = yc - gl / 2 + 15, yc + gl / 2 - 15
        gs += [rod((xc, a, D), (xc, a, D + gh), 11), rod((xc, b, D), (xc, b, D + gh), 11),
               rod((xc, a, D + gh), (xc, b, D + gh), 11),
               box(xc - 15, xc + 15, a - 20, a + 20, D, D + 4), box(xc - 15, xc + 15, b - 20, b + 20, D, D + 4)]
    out["transom grab handles"] = (17, Compound(gs))
    # [18] carry handles on the inwales: grip 200 long, 50 high
    cl, chh = p["carry"]
    yc = half(D, ts + p["inwale"][0] / 2, p)
    for tag, xs in (("aft", [x for x in p["carry_x"] if x < p["x_joint"]]),
                    ("forward", [x for x in p["carry_x"] if x > p["x_joint"]])):
        cs = []
        for x in xs:
            for y in (yc, -yc):
                a, b = x - cl / 2, x + cl / 2
                cs += [rod((a, y, D), (a, y, D + chh), 8), rod((b, y, D), (b, y, D + chh), 8),
                       rod((a - 8, y, D + chh), (b + 8, y, D + chh), 12)]
        out[f"carry handles {tag}"] = (18, Compound(cs))
    # [19] push pole: two 1.5 m sections on the aft floor between the stringers
    pr, pl = p["pole"]
    S = stations(p)
    x0 = S["aft_in"][0] + 80
    zf = p["t_bot"] + pr
    out["push pole sections"] = (19, Compound([rod((x0, y, zf), (x0 + pl, y, zf), pr) for y in (-80.0, 80.0)]))
    # [20] paddles on the aft bench tops
    plen, pw, pt, pbl = p["paddle"]
    pads = []
    for y0 in (p["bench_y"] + 110, -(p["bench_y"] + 110)):
        zt = p["bench_top"] + p["strap"][1]   # lies on the bench straps
        blade = box(x0, x0 + pbl, y0 - pw / 2, y0 + pw / 2, zt, zt + pt)
        shaft = rod((x0 + pbl - 20, y0, zt + 15), (x0 + plen, y0, zt + 15), 15)
        grip = rod((x0 + plen - 10, y0 - 50, zt + 15), (x0 + plen - 10, y0 + 50, zt + 15), 14)
        pads.append(Compound([blade, shaft, grip]))
    out["paddles"] = (20, flat(pads))
    # [21] bow eye (U-bolt through the bow transom and pad) and the bow line coiled on the deck
    L = p["L"]
    xb1 = L - p["t_bow"]
    zc = 330.0
    legs = [rod((xb1 - 20 - 12, y, zc), (L + 30, y, zc), 5) for y in (-25.0, 25.0)]
    loop = Pos(L + 30, 0, zc) * Rot(90, 0, 0) * Torus(25, 5) & box(L + 30, L + 70, -40, 40, zc - 40, zc + 40)
    nuts = [Pos(xb1 - 20 - 5, y, zc) * Rot(0, 90, 0) * Cylinder(9, 9) for y in (-25.0, 25.0)]
    out["bow eye"] = (21, Compound(legs + [loop] + nuts))
    out["bow line, coiled"] = (21, Pos(3300, 0, D + 6) * Torus(130, 6))
    return out


BOM_NAMES = {  # noqa: E501
    1: "Bottom panels, 6 mm plywood", 2: "Side panels, 6 mm plywood", 3: "Stern transom, 12 mm plywood",
    4: "Bow transom, 9 mm plywood", 5: "Joint bulkheads, 9 mm plywood", 6: "Ring frames, hardwood 20 x 45",
    7: "Inwales, hardwood 20 x 40", 8: "Stringers and knuckle floor, hardwood", 9: "Bench modules and bow box",
    10: "Buoyancy foam, closed-cell PE", 11: "Joint bolts M10 and alignment pins", 12: "Rub strakes, HDPE",
    13: "Bottom skids, HDPE", 14: "Stern step: rail, float and hinges", 15: "Step stop straps and pad eyes",
    16: "Kick rung on straps", 17: "Transom grab handles", 18: "Carry handles", 19: "Push pole, two sections",
    20: "Paddles", 21: "Bow eye and bow line",
}


def build_all(p=PARAMS, swing=0.0):
    """Every part: list of (name, half or 'step'/'outfit', BOM line, shape)."""
    rows = [(n, h, b, s) for n, (h, b, s) in hull_parts(p).items()]
    bolts, pins = joint_hardware(p)
    rows += [(f"joint bolt {i + 1}", "joint", 11, s) for i, s in enumerate(bolts)]
    rows += [(f"alignment pin {i + 1}", "joint", 11, s) for i, s in enumerate(pins)]
    rows += [(n, "step", b, s) for n, (b, s) in step_parts(p, swing).items()]
    rows += [(n, "outfit", b, s) for n, (b, s) in outfit_parts(p).items()]
    return rows


def by_bom(rows):
    out = {}
    for n, h, b, s in rows:
        out.setdefault(b, []).append(s)
    return {b: flat(v) for b, v in sorted(out.items())}


def assembly(p=PARAMS):
    return Compound([s for _, _, _, s in build_all(p)])


def half_assembly(which, p=PARAMS):
    return Compound([s for n, h, b, s in build_all(p) if h == which])


# ---------------------------------------------------------------- constructability checks
def _vol(a, b):
    try:
        r = a & b
        return r.volume if r is not None else 0.0
    except Exception:
        return float("nan")


def _bb_touch(a, b, m=1.0):
    A, B = a.bounding_box(), b.bounding_box()
    return not (A.max.X < B.min.X - m or B.max.X < A.min.X - m or A.max.Y < B.min.Y - m or B.max.Y < A.min.Y - m
                or A.max.Z < B.min.Z - m or B.max.Z < A.min.Z - m)


# parts that are meant to pass through others (bolts through what they clamp, pins in their holes)
THROUGH = ("joint bolt", "alignment pin", "rail bolts", "bow eye")


def checks(p=PARAMS):
    """List of (name, passed, detail). Overlap tolerance 1 mm3, contact tolerance 0.5 mm."""
    rows = build_all(p)
    named = {n: s for n, _, _, s in rows}
    res = []

    def add(name, ok, detail=""):
        res.append((name, bool(ok), detail))

    # 1 no two solid parts overlap (fasteners excluded: they pass through drilled holes)
    solid = [(n, s) for n, _, _, s in rows if not n.startswith(THROUGH)]
    worst = []
    for i in range(len(solid)):
        for j in range(i + 1, len(solid)):
            (na, a), (nb, b) = solid[i], solid[j]
            if not _bb_touch(a, b):
                continue
            v = _vol(a, b)
            if v > 1.0:
                worst.append(f"{na} / {nb}: {v:.0f} mm3")
    add("no overlapping parts (all pairs of made and bought parts)", not worst, "; ".join(worst[:6]))
    # 2 every part touches the part it is fixed to
    contacts = [
        ("side aft port", "bottom aft"), ("side aft starboard", "bottom aft"),
        ("side forward port", "bottom forward flat"), ("side forward port", "bottom bow rake"),
        ("bottom forward flat", "bottom bow rake"),
        ("stern transom", "bottom aft"), ("stern transom", "side aft port"),
        ("bow transom", "bottom bow rake"), ("bow transom", "side forward starboard"),
        ("joint bulkhead aft", "bottom aft"), ("joint bulkhead forward", "bottom forward flat"),
        ("joint bulkhead aft", "joint bulkhead forward"),
        ("ring frame transom", "stern transom"), ("ring frame joint aft", "joint bulkhead aft"),
        ("ring frame joint forward", "joint bulkhead forward"),
        ("inwale aft port", "side aft port"), ("inwale forward starboard", "side forward starboard"),
        ("inwale aft port", "ring frame joint aft"), ("inwale forward port", "bow transom"),
        ("stringer aft port", "bottom aft"), ("stringer forward starboard", "knuckle floor"),
        ("knuckle floor", "bottom bow rake"), ("knuckle floor", "bottom forward flat"),
        ("bench cover aft port", "side aft port"), ("bench cover aft port", "bottom aft"),
        ("bench cover aft port", "inwale aft port"), ("bench rail aft port", "bottom aft"),
        ("bench rail aft port", "bench cover aft port"), ("bench straps aft port", "bench rail aft port"),
        ("bench straps aft port", "inwale aft port"), ("bench straps forward starboard", "bench cover forward starboard"),
        ("bench foam aft port", "bench cover aft port"), ("bench cover forward starboard", "side forward starboard"),
        ("bow box wall", "bottom bow rake"), ("bow deck", "inwale forward port"), ("bow deck", "bow transom"),
        ("bow foam", "bow deck"), ("bow eye pad", "bow transom"),
        ("rub strake aft port", "side aft port"), ("rub strake forward starboard", "side forward starboard"),
        ("skid aft port", "bottom aft"), ("skid forward port", "bottom bow rake"),
        ("hinge rail", "stern transom"), ("transom backing block", "stern transom"),
        ("step float top deck", "step float rim"), ("step float foam", "step float bottom deck"),
        ("strap hinges (rail leaves)", "hinge rail"), ("strap hinges (float leaves)", "step float top deck"),
        ("transom pad eyes", "stern transom"), ("kick rung", "kick rung straps"),
        ("transom grab handles", "ring frame transom"), ("carry handles aft", "inwale aft port"),
        ("carry handles forward", "inwale forward starboard"),
        ("push pole sections", "bottom aft"), ("paddles", "bench straps aft port"),
        ("bow line, coiled", "bow deck"),
    ]
    for a, b in contacts:
        d = named[a].distance_to(named[b])
        add(f"{a} sits on {b}", d < 0.5, f"gap {d:.2f} mm")
    # 3 bolts: through what they clamp, clear of benches, stringers and inwales
    bolts, pins = joint_hardware(p)
    clamp = [named["ring frame joint aft"], named["joint bulkhead aft"], named["joint bulkhead forward"],
             named["ring frame joint forward"]]
    keep_clear = Compound([s for n, s in named.items() if n.startswith(("bench", "stringer", "inwale", "side"))])
    for i, b in enumerate(bolts):
        ok = all(_vol(b, c) > 50 for c in clamp)
        v = _vol(b, keep_clear)
        add(f"joint bolt {i + 1}: through both ring frames and both bulkheads, clear of benches and stringers",
            ok and v < 1.0, f"{v:.1f} mm3 into benches or stringers")
    for i, pn in enumerate(pins):
        add(f"alignment pin {i + 1}: within the two ring frames", _vol(pn, Compound(clamp)) > 0.95 * pn.volume, "")
    rb = named["rail bolts M8"]
    add("rail bolts: through rail, transom and backing block, clear of the ring frame",
        all(_vol(rb, named[k]) > 100 for k in ("hinge rail", "stern transom", "transom backing block"))
        and _vol(rb, named["ring frame transom"]) < 1.0, "")
    be = named["bow eye"]
    add("bow eye: through the bow transom and pad, clear of the bow deck",
        _vol(be, named["bow transom"]) > 100 and _vol(be, named["bow eye pad"]) > 100 and _vol(be, named["bow deck"]) < 1, "")
    # 4 halves separate at the joint plane: nothing but the bolts and pins crosses it
    xj = p["x_joint"]
    cross = [n for n, h, _, s in rows if h in (AFT, FWD, "outfit")
             and s.bounding_box().min.X < xj - 0.01 and s.bounding_box().max.X > xj + 0.01]
    add("only the joint bolts and pins cross the joint plane", not cross, ", ".join(cross))
    # 5 stern step swings to the stop and folds up without touching the transom or rail
    fixed = Compound([named[k] for k in ("hinge rail", "stern transom", "rub strake aft port", "rub strake aft starboard",
                                         "skid aft port", "skid aft starboard", "transom pad eyes")])
    for sw in (p["stop_deg"], -60.0):
        mv = step_parts(p, swing=sw)
        movers = Compound([s for k, (b, s) in mv.items() if k.startswith(("step float", "kick rung", "float pad"))])
        v = _vol(movers, fixed)
        dmin = movers.distance_to(Compound([named["hinge rail"], named["stern transom"]]))
        add(f"step float turned {sw:+.0f} deg about the hinge: clear of rail and transom", v < 1.0,
            f"{v:.1f} mm3, closest {dmin:.1f} mm")
    # 6 lane width
    bb = assembly(p).bounding_box()
    add("overall beam within 1,200 mm", bb.max.Y - bb.min.Y <= 1200.0, f"{bb.max.Y - bb.min.Y:.0f} mm")
    return res


# ---------------------------------------------------------------- export
def export(p=PARAMS):
    step = ROOT / "cad" / "step"
    stl = ROOT / "cad" / "stl"
    step.mkdir(parents=True, exist_ok=True)
    stl.mkdir(parents=True, exist_ok=True)
    rows = build_all(p)
    export_step(Compound([s for *_, s in rows]), str(step / "laneskiff-assembly.step"))
    export_step(half_assembly(AFT, p), str(step / "laneskiff-aft-half.step"))
    export_step(half_assembly(FWD, p), str(step / "laneskiff-forward-half.step"))
    export_step(Compound([s for n, h, b, s in rows if h == "step"]), str(step / "laneskiff-stern-step.step"))
    named = {n: s for n, *_, s in rows}
    for n in ("bottom aft", "side aft port", "side forward port", "stern transom", "joint bulkhead aft", "bow transom"):
        export_step(named[n], str(step / f"panel-{n.replace(' ', '-')}.step"))
    for n in ("ring frame joint aft", "knuckle floor", "hinge rail"):
        export_stl(named[n], str(stl / f"{n.replace(' ', '-')}.stl"), tolerance=0.5, angular_tolerance=0.3)


if __name__ == "__main__":
    if "--check" in sys.argv:
        r = checks()
        for name, ok, det in r:
            if not ok:
                print("FAIL", name, det)
        print(f"{sum(ok for _, ok, _ in r)} of {len(r)} constructability checks pass")
    if "--export" in sys.argv:
        export()
        print("exported STEP and STL")
    if len(sys.argv) == 1:
        for n, h, b, s in build_all():
            print(f"{n:40s} {h:6s} {b:3d} {s.volume / 1e6:8.3f} L")
