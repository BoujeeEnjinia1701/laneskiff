"""LaneSkiff sizing calculations (LSK-CAL-001).

Run from the repo root:  python docs/04-calcs/sizing.py
Prints every result with a tag ([M1], [H3] ...) used in docs/04-calcs/01-sizing.md and writes
docs/04-calcs/results.csv. Geometry comes from the parametric model (cad/src/model.py), so the
panel sizes, foam volumes and positions here are those of the STEP files, drawings and build plan.

Method in brief:
  masses     model volume x material density for every made part, plus bought items and the
             epoxy, glass and coating worked out from the panel areas;
  afloat     the hull envelope (outside of the planking and skids) is cut at a trial waterline and
             the draft found where its displaced water equals the total weight (fresh water); trim
             and heel from the waterplane (a rectangle while the bottom is flat at the waterline);
  swamped    every body floats on its own: the water inside the hull is part of the flood and
             carries nothing. Foam gives lift for its submerged volume; plywood and timber count
             as exactly as dense as water (no lift when submerged, full weight above water);
             people count at two thirds of their weight (conservative design assumption);
  structure  one-way plate bending of the floor, joint bolt tension in a kerb-hogging case, and
             the stop strap pull with a person on the step.
Screening estimates for a paper proof of concept; not a substitute for the TRL 4 tests.
Software license MIT, see LICENSE-SOFTWARE.
"""
import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "cad" / "src")]
import model as M  # noqa: E402
from build123d import Compound  # noqa: E402

P = M.PARAMS
OUT = []

A = {
    "rho_w": 1000.0,          # fresh floodwater, kg/m3
    "rho_ply": 450.0,         # okoume marine plywood (BS 1088), light timber specification (LSK-DDR-003)
    "rho_sw": 500.0,          # softwood framing: ring frames, inwales, stringers, bench rails, knuckle floor
    "rho_hw": 700.0,          # durable hardwood for the step, bow eye pad and rung (teak, jackwood or similar)
    "rho_foam": 30.0,         # closed-cell polyethylene foam
    "rho_hdpe": 950.0,
    "rho_steel": 7900.0,
    "rho_fabric": 325.0,      # model density giving 0.65 kg/m2 tarpaulin at 2 mm and 40 g/m webbing at 50 x 2.5 mm
    "glass_out": 0.80,        # kg/m2: 400 g/m2 glass cloth plus resin on the outside of the bottom and sides
    "glass_in": 0.0,          # kg/m2: no glass inside the floor (light specification; was 0.40)
    "coat": 0.20,             # kg/m2 per face, two coats of epoxy on every other plywood face
    "tape": 0.25,             # kg/m of seam: 100 mm glass tape inside and out, with the fillet
    "fixings": 1.5,           # kg: screws, washers and sealant not modelled
    "person": 75.0,           # kg, design person
    "boarder": 80.0,          # kg, R6 boarder
    "persons": 5,             # rated: a crew of two and three adults (LSK-DDR-003)
    "swamp_person": 2.0 / 3.0,  # share of a person's weight carried by the swamped boat
    "ply_allow": 40.0,        # MPa, bending strength of marine plywood along the face grain (sheath ignored)
    "foot_kN": 1.2,           # kN, 80 kg with a 1.5 dynamic factor on one foot
    "foot_w": 300.0,          # mm, width of floor strip that carries the foot load
    "bolt_proof_kN": 29.0,    # M10 stainless A4-70 at 70 % of 0.2 % proof (58 mm2 x 450 MPa x 1.1)
    "plate_bear_kN": 16.0,    # 40 x 40 mm nut plate on hardwood at 10 MPa
    "webbing_kN": 8.0,        # 25 mm polyester webbing, breaking strength (to confirm)
    "hinge_kN": 4.0,          # heavy stainless strap hinge pin shear, each (to confirm)
}

# ------------------------------------------------------------------ helpers


def out(tag, text, value=None, unit="", req=None, status=None):
    OUT.append({"tag": tag, "item": text, "value": "" if value is None else value, "unit": unit,
                "requirement": req or "", "status": status or ""})
    v = "" if value is None else value
    print(f"[{tag}] {text}: {v} {unit}" + (f"  ({req}: {status})" if req else ""))


def cut_below(shape, z):
    return shape & M.box(-800, 4400, -900, 900, -500, z)


def cut_above(shape, z):
    return shape & M.box(-800, 4400, -900, 900, z, 1200)


def vol(s):
    try:
        return s.volume if s is not None else 0.0
    except Exception:
        return 0.0


ROWS = M.build_all(P)
NAMED = {n: s for n, _, _, s in ROWS}
HALF = {n: h for n, h, _, _ in ROWS}

MAT = {}
for n, h, b, s in ROWS:
    if n.startswith(("bench cover", "bench straps", "quarter cover", "quarter strap")):
        MAT[n] = "fabric"
    elif b in (1, 2, 3, 4, 5) or n in ("bow box wall", "bow deck", "step float top deck", "step float bottom deck"):
        MAT[n] = "ply"
    elif b in (6, 7, 8) or n.startswith("bench rail"):
        MAT[n] = "sw"
    elif n in ("bow eye pad", "hinge rail", "transom backing block", "step float rim", "kick rung"):
        MAT[n] = "hw"
    elif b == 10 or n.startswith("quarter foam"):
        MAT[n] = "foam"
    elif b in (12, 13):
        MAT[n] = "hdpe"
    elif b in (11,) or n in ("rail bolts M8", "bow eye"):
        MAT[n] = "steel"
    else:
        MAT[n] = "bought"
RHO = {"ply": A["rho_ply"], "sw": A["rho_sw"], "hw": A["rho_hw"], "foam": A["rho_foam"], "hdpe": A["rho_hdpe"], "steel": A["rho_steel"],
       "fabric": A["rho_fabric"]}

# bought items at catalogue-type masses (kg), not from model volume
BOUGHT = {
    "strap hinges (rail leaves)": 0.3, "strap hinges (float leaves)": 0.3, "float pad eyes": 0.1,
    "kick rung straps": 0.2, "transom pad eyes": 0.1, "stop straps": 0.15,
    "transom grab handles": 1.2, "carry handles aft": 1.0, "carry handles forward": 1.0,
    "push pole sections": 3.1, "paddles": 2.4, "bow line, coiled": 0.75,
}
LOOSE = ("push pole sections", "paddles", "bow line, coiled")    # gear, not counted in the hull


def part_mass(n):
    m = MAT[n]
    if m == "bought":
        return BOUGHT[n]
    return vol(NAMED[n]) * 1e-9 * RHO[m]


def ply_area(n):
    t = {1: P["t_bot"], 2: P["t_side"], 3: P["t_transom"], 4: P["t_bow"], 5: P["t_bh"]}
    b = [bb for nn, _, bb, _ in ROWS if nn == n][0]
    if n.startswith("bow box") or n == "bow deck":
        th = P["t_box"]
    elif n.startswith("step float top"):
        th = P["float_top"]
    elif n.startswith("step float bottom"):
        th = P["float_bot"]
    else:
        th = t[b]
    return vol(NAMED[n]) / th / 1e6   # m2


# ------------------------------------------------------------------ 1 masses
def masses():
    by_mat, by_half, cg = {}, {"aft": 0.0, "fwd": 0.0}, []
    hull_parts = [n for n in NAMED if n not in LOOSE]
    total = 0.0
    for n in hull_parts:
        m = part_mass(n)
        total += m
        by_mat[MAT[n]] = by_mat.get(MAT[n], 0.0) + m
        h = HALF[n]
        if h in ("step", "aft"):
            by_half["aft"] += m
        elif h == "fwd":
            by_half["fwd"] += m
        else:                       # joint hardware and outfit: split by position
            x = NAMED[n].bounding_box().center().X
            by_half["aft" if x < P["x_joint"] else "fwd"] += m
        c = NAMED[n].center() if MAT[n] != "bought" else NAMED[n].bounding_box().center()
        cg.append((m, c.X, c.Y, c.Z))
    # glass, epoxy and coating from the panel areas
    a_bot = sum(ply_area(n) for n in NAMED if n.startswith("bottom"))
    a_side = sum(ply_area(n) for n in NAMED if n.startswith("side"))
    a_other = sum(ply_area(n) for n in NAMED if MAT.get(n) == "ply" and not n.startswith(("bottom", "side")))
    glass = A["glass_out"] * (a_bot + a_side) + A["glass_in"] * a_bot
    coat = A["coat"] * (a_side + 2 * a_other)
    seams = 2 * P["L"] / 1000 + 4 * (2 * P["D"] + 2 * P["half_bot"]) / 1000 + 2 * P["half_bot"] / 1000   # chines, end panels, knuckle
    tape = A["tape"] * seams
    comp = glass + coat + tape + A["fixings"]
    total += comp
    for k in by_half:
        by_half[k] += comp / 2
    xs = sum(m * x for m, x, _, _ in cg) + comp * 1800
    zs = sum(m * z for m, _, _, z in cg) + comp * 150
    mt = sum(m for m, *_ in cg) + comp
    return {"total": total, "by_mat": by_mat, "by_half": by_half, "glass_epoxy": comp, "lcg": xs / mt, "kg": zs / mt,
            "a_bot": a_bot, "a_side": a_side, "a_other": a_other, "seams": seams,
            "loose": sum(BOUGHT[n] for n in LOOSE)}


# ------------------------------------------------------------------ 2 afloat
def envelope():
    D, L, K = P["D"], P["L"], P["knuckle"]
    hull = M.yz_x(M.trap(0, -1, D, P), 0, L) & M.xz_y([(0, 0), (K, 0), (L, P["rise"]), (L, D), (0, D)])
    skids = [NAMED[n] for n in NAMED if n.startswith("skid")]
    return Compound([hull] + skids)


ENV = envelope()


def displaced(T):
    s = cut_below(ENV, T)
    v = vol(s)
    c = s.center() if v > 0 else None
    return v * 1e-9, c


def waterplane(T):
    """Waterplane at height T above the outside of the bottom: rectangle from the transom to where the raked bottom
    meets the water. Returns area m2, LCF mm, I_T and I_L (about LCF) m4."""
    K, L, r = P["knuckle"], P["L"], P["rise"]
    xT = K + (L - K) * min(max(T, 0.0), r) / r if T > 0 else K
    B = 2 * M.half(T, 0, P) / 1000.0
    Lw = xT / 1000.0
    return B * Lw, xT / 2, Lw * B ** 3 / 12, B * Lw ** 3 / 12, B, Lw


def float_at(W, lcg, kg):
    """Even-keel draft for total mass W (kg), then trim from LCG. Returns dict (mm, deg)."""
    lo, hi = -10.0, P["D"]
    for _ in range(40):
        T = (lo + hi) / 2
        v, _ = displaced(T)
        if v * A["rho_w"] > W:
            hi = T
        else:
            lo = T
    T = (lo + hi) / 2
    v, c = displaced(T)
    Awp, lcf, IT, IL, B, Lw = waterplane(T)
    KB = c.Z / 1000
    BMT, BML = IT / v, IL / v
    GMT = KB + BMT - kg / 1000
    GML = KB + BML - kg / 1000
    theta = (c.X - lcg) / 1000 / GML            # radians, + = stern down
    T_aft = T + theta * (lcf - 0)
    T_fwd = T - theta * (Lw * 1000 - lcf)
    return {"T": T, "V": v, "LCB": c.X, "KB": KB * 1000, "GMT": GMT, "GML": GML, "trim": math.degrees(theta),
            "T_aft": T_aft, "T_fwd": T_fwd, "B": B, "Lw": Lw, "lcf": lcf, "tpc": Awp * A["rho_w"] / 100}


def combine(items):
    W = sum(m for m, *_ in items)
    return W, sum(m * x for m, x, *_ in items) / W, sum(m * y for m, _, y, _ in items) / W, \
        sum(m * z for m, *_, z in items) / W


# ------------------------------------------------------------------ 3 swamped
WOODY = [n for n in NAMED if MAT[n] in ("ply", "sw", "hw", "hdpe")]
FOAM = [n for n in NAMED if MAT[n] == "foam" and not n.startswith("step")]
LEVELS = [10.0 * i for i in range(0, 41)]


def tabulate():
    """Foam submerged volume and centroid, and timber and HDPE mass above water, at 10 mm levels."""
    tab = []
    foam = Compound([NAMED[n] for n in FOAM])
    for z in LEVELS:
        f = cut_below(foam, z)
        fv = vol(f)
        fc = f.center() if fv > 0 else None
        wm, wx, wz = 0.0, 0.0, 0.0
        for n in WOODY:
            s = cut_above(NAMED[n], z)
            v = vol(s)
            if v > 0:
                m = v * 1e-9 * RHO[MAT[n]]
                c = s.center()
                wm += m; wx += m * c.X; wz += m * c.Z
        tab.append({"z": z, "fv": fv * 1e-9, "fx": fc.X if fc else 0, "fz": fc.Z if fc else 0,
                    "wm": wm, "wx": wx / wm if wm else 0, "wz": wz / wm if wm else 0})
    return tab


def interp(tab, z, key):
    for a, b in zip(tab[:-1], tab[1:]):
        if a["z"] <= z <= b["z"]:
            t = (z - a["z"]) / (b["z"] - a["z"])
            return a[key] + t * (b[key] - a[key])
    return tab[-1][key]


def foam_waterplane(z):
    """Area, centroid x and second moments of the foam cut by the water surface at z."""
    pieces = []
    for n in FOAM:
        s = NAMED[n] & M.box(-800, 4400, -900, 900, z - 0.5, z + 0.5)
        if vol(s) > 0:
            bb = s.bounding_box()
            pieces.append((vol(s) / 1e6, (bb.min.X + bb.max.X) / 2000, (bb.min.Y + bb.max.Y) / 2000,
                           (bb.max.X - bb.min.X) / 1000, (bb.max.Y - bb.min.Y) / 1000))
    Aw = sum(a for a, *_ in pieces)
    xc = sum(a * x for a, x, *_ in pieces) / Aw
    IT = sum(a * (y * y + w * w / 12) for a, _, y, _, w in pieces)
    IL = sum(a * ((x - xc) ** 2 + l * l / 12) for a, x, _, l, _ in pieces)
    return Aw, xc, IT, IL


# ------------------------------------------------------------------ main
def main():
    m = masses()
    hull = m["total"]
    out("M1", "Hull mass, complete, plywood and epoxy path, light specification (step, handles and strakes included; "
        "pole, paddles, line not)",
        round(hull, 1), "kg", "R1", "Not met")
    out("M2", "Aft half mass, with the stern step", round(m["by_half"]["aft"], 1), "kg", "R1", "Not met")
    out("M3", "Forward half mass", round(m["by_half"]["fwd"], 1), "kg", "R1", "Not met")
    for k, label in (("ply", "okoume plywood"), ("sw", "softwood framing"), ("hw", "hardwood (step, pad, rung)"),
                     ("foam", "foam"), ("hdpe", "HDPE strakes and skids"),
                     ("steel", "bolts and bow eye"), ("fabric", "bench covers and straps"), ("bought", "bought fittings")):
        out(f"M4{k}", f"Mass of {label}", round(m["by_mat"].get(k, 0.0), 1), "kg")
    out("M5", "Glass, epoxy, coating, tapes and small fixings", round(m["glass_epoxy"], 1), "kg")
    out("M6", "Loose gear: pole, two paddles, bow line", round(m["loose"], 1), "kg")
    out("M7", "Hull LCG from the transom; KG above the outside of the bottom",
        f"{m['lcg']:.0f}; {m['kg']:.0f}", "mm")
    out("M8", "Plywood areas: bottom; sides; other panels", f"{m['a_bot']:.2f}; {m['a_side']:.2f}; {m['a_other']:.2f}", "m2")

    hb = (hull, m["lcg"], 0.0, m["kg"])
    gear = (m["loose"], 700.0, 0.0, 60.0)
    p_ = A["person"]
    six = [
        (p_, 400.0, 0.0, 1006.0),          # crew 1 standing aft, poling
        (p_, 2900.0, 0.0, 500.0),          # crew 2 kneeling forward
        (p_, 1000.0, 440.0, 580.0), (p_, 1000.0, -440.0, 580.0),   # seated on the aft benches
        (p_, 2200.0, 440.0, 580.0), (p_, 2200.0, -440.0, 580.0),   # seated on the forward benches
    ]
    rated = six[:A["persons"]]             # five persons: one forward bench place left empty
    rated_kg = sum(q[0] for q in rated)
    out("L1", "Rated load: a crew of two and three adults at 75 kg (five persons)", round(rated_kg), "kg")
    out("L2", "Rated load over hull mass", round(rated_kg / hull, 2), "", "R2",
        "Met" if rated_kg / hull >= 6 else "Not met")
    W, lcg, _, kg = combine([hb, gear] + rated)
    r = float_at(W, lcg, kg)
    out("H1", "Draft at rated load, even keel (outside of the bottom)", round(r["T"]), "mm")
    out("H2", "Trim at rated load (+ = stern down); draft at the transom; draft at the forward end of the waterline",
        f"{r['trim']:.2f}; {r['T_aft']:.0f}; {r['T_fwd']:.0f}", "deg; mm; mm", "R3",
        "Met" if max(r["T_aft"], r["T_fwd"]) <= 150 else "Not met")
    out("H3", "Freeboard at rated load, lowest (transom)", round(P["D"] - r["T_aft"]), "mm")
    out("H4", "Waterline length and beam at rated load", f"{r['Lw']:.2f}; {r['B']:.2f}", "m")
    out("H5", "Transverse metacentric height GM at rated load", round(r["GMT"], 2), "m")
    out("H6", "Load to sink 10 mm at rated draft", round(r["tpc"], 1), "kg")
    # capacity at the R3 draft
    v150, _ = displaced(150.0)
    cap = v150 * A["rho_w"] - hull - m["loose"]
    out("H7", "Load carried at 150 mm draft, even keel", round(cap), "kg")
    out("H8", "That load over hull mass", round(cap / hull, 2))
    # light ship: hull and two crew
    crew2 = [(p_, 400.0, 0.0, 1006.0), (p_, 2900.0, 0.0, 500.0)]
    W2, l2, _, k2 = combine([hb, gear] + crew2)
    r2 = float_at(W2, l2, k2)
    out("H9", "Draft with the crew of two only", round(r2["T"]), "mm")
    # boarding over the stern step (R6) with the two crew sitting forward to balance
    crew_fwd = [(p_, 2100.0, 440.0, 580.0), (p_, 2100.0, -440.0, 580.0)]
    for case, (x, y, z, label) in {"B": (-150.0, 150.0, 600.0, "stern step, 150 mm off the centreline"),
                                   "S": (1200.0, M.half(P["D"], 0, P), 600.0, "over the side, at the gunwale")}.items():
        items = [hb, gear] + crew_fwd + [(A["boarder"], x, y, z)]
        Wb, lb, yb, kb = combine(items)
        rb = float_at(Wb, lb, kb)
        heel = math.degrees(math.atan(A["boarder"] * y / 1000 / (Wb * rb["GMT"])))
        if case == "B":
            out("B1", f"Heel, 80 kg boarder on the {label}", round(heel, 1), "deg", "R6", "Met" if heel < 10 else "Not met")
            out("B2", "Trim and transom freeboard while boarding over the stern",
                f"{rb['trim']:.1f}; {P['D'] - rb['T_aft']:.0f}", "deg; mm")
        else:
            low = P["D"] - rb["T"] - y / 1000 * math.tan(math.radians(heel)) * 1000
            out("B3", f"For comparison, heel with the same boarder {label}", round(heel, 1), "deg")
            out("B4", "Low-side freeboard with the side boarder", round(low), "mm")

    # swamped (R5)
    tab = tabulate()
    foam_tot = sum(vol(NAMED[n]) for n in FOAM) * 1e-9
    out("F1", "Buoyancy foam in the hull (benches, bow box and stern quarter modules)", round(foam_tot, 3), "m3")
    sw_persons = [(q[0] * A["swamp_person"], q[1], q[2], q[3]) for q in rated]
    steel = sum(part_mass(n) for n in NAMED if MAT[n] == "steel") * (1 - A["rho_w"] / A["rho_steel"])
    bought = sum(BOUGHT[n] for n in BOUGHT if n not in LOOSE) * 0.6
    foam_mass = sum(part_mass(n) for n in FOAM) + part_mass("step float foam")
    fabric = sum(part_mass(n) for n in NAMED if MAT[n] == "fabric")
    fixed = m["glass_epoxy"] + steel + bought + foam_mass + fabric + m["loose"] * 0.5
    stepw = sum(part_mass(n) for n in NAMED if HALF[n] == "step" and MAT[n] in ("ply", "hw")) * 0.0

    def weight(z):
        return fixed + interp(tab, z, "wm") + sum(q[0] for q in sw_persons) + stepw

    def lift(z):
        return interp(tab, z, "fv") * A["rho_w"]

    lo, hi = 0.0, 400.0
    for _ in range(50):
        z = (lo + hi) / 2
        if lift(z) > weight(z):
            hi = z
        else:
            lo = z
    zw = (lo + hi) / 2
    Wsw = weight(zw)
    out("F2", "Swamped, rated persons aboard: water level inside and out, above the outside of the bottom", round(zw), "mm")
    out("F3", "Swamped: weight carried by the foam (persons at two thirds)", round(Wsw), "kg")
    Aw, xc, IT, IL = foam_waterplane(zw)
    fx = interp(tab, zw, "fx")
    fz = interp(tab, zw, "fz")
    wm = interp(tab, zw, "wm")
    items = [(fixed, 1700.0, 0, 150.0), (wm, interp(tab, zw, "wx"), 0, interp(tab, zw, "wz"))] + sw_persons
    Wt, lx, _, kz = combine(items)
    V = Wt / A["rho_w"]
    GML = fz / 1000 + IL / V - kz / 1000
    GMT = fz / 1000 + IT / V - kz / 1000
    trim = math.degrees((fx - lx) / 1000 / GML)
    xa, xf = 0.0, P["L"]
    fb_aft = P["D"] - (zw + math.radians(trim) * (xc * 1000 - xa))
    fb_fwd = P["D"] - (zw - math.radians(trim) * (xf - xc * 1000))
    out("F4", "Swamped trim (+ = stern down)", round(trim, 2), "deg")
    out("F5", "Swamped freeboard at the transom and at the bow", f"{fb_aft:.0f}; {fb_fwd:.0f}", "mm", "R5",
        "Met on paper" if min(fb_aft, fb_fwd) > 0 and abs(trim) < 5 else "Not met")
    out("F6", "Swamped transverse GM", round(GMT, 2), "m")
    hl = math.degrees(math.atan(2 * p_ * A["swamp_person"] * 0.4 / (Wt * GMT)))
    out("F7", "Swamped heel with two seated persons moving 400 mm to one side", round(hl, 1), "deg")
    out("F8", "Swamped low-side freeboard in that case", round(P["D"] - zw - M.half(P["D"], 0, P) * math.tan(math.radians(hl))), "mm")
    out("F9", "Foam needed for zero freeboard, rated persons, as a share of the fitted foam",
        round((weight(400.0)) / (foam_tot * A["rho_w"]), 2))

    # structure
    span = max(P["stringer_y"] - P["stringer"][0] / 2 - P["stringer"][0] / 2,
               P["bench_y"] - P["stringer_y"] - P["stringer"][0] / 2)
    Mf = A["foot_kN"] * 1000 * span / 4 / 1000           # N m
    sig = 6 * Mf / (A["foot_w"] / 1000 * (P["t_bot"] / 1000) ** 2) / 1e6
    out("S1", "Floor: largest clear span between stringers and bench faces", round(span), "mm")
    out("S2", "Floor bending stress under a 1.2 kN foot load (plywood only, glass ignored)", round(sig, 1), "MPa")
    out("S3", "Floor factor against plywood bending strength", round(A["ply_allow"] / sig, 2))
    Wk = (hull + rated_kg) * 9.81
    Mk = Wk * P["L"] / 1000 / 4                               # N m, kerb under the joint, ends free
    arm = (P["D"] - P["frame"][1] / 2) / 1000
    Tb = Mk / arm / 4 / 1000
    out("S4", "Joint: hogging over a kerb at the joint, rated load, top bolt tension each", round(Tb, 1), "kN")
    out("S5", "Joint bolt factor (bolt proof; nut plate bearing)",
        f"{A['bolt_proof_kN'] / Tb:.1f}; {A['plate_bear_kN'] / Tb:.1f}")
    hx, hz = M.hinge_axis(P)
    fl = P["float"][0]
    xf0 = -P["rail"][0] - P["gap"] - fl
    a = (-14.0, 380.0)
    b = (xf0 + 35.0, P["float"][3] + P["float"][2] + 12)
    dx, dz = b[0] - a[0], b[1] - a[1]
    Ls = math.hypot(dx, dz)
    perp = abs(dx * (a[1] - hz) - dz * (a[0] - hx)) / Ls / 1000
    Mh = A["boarder"] * 9.81 * 2.0 * (fl - 20) / 1000      # kneeling on the aft edge, dynamic factor 2
    Ts = Mh / perp / 2 / 1000
    out("S6", "Step: pull in each stop strap, 80 kg kneeling on the aft edge, dynamic factor 2", round(Ts, 2), "kN")
    out("S7", "Stop strap factor against webbing strength", round(A["webbing_kN"] / Ts, 1))
    Rh = (A["boarder"] * 9.81 * 2.0 / 1000 + 2 * Ts) / 2
    out("S8", "Hinge load each (upper bound), and factor", f"{Rh:.2f}; {A['hinge_kN'] / Rh:.1f}", "kN")

    # assembly time (R7), estimate
    t = 2.0 + 8 * 0.4 + 1.0
    out("T1", "Joining the halves: place and align 2 min, eight bolts at 25 s, check 1 min (estimate)", round(t, 1), "min",
        "R7", "Met on paper (estimate)")

    # build paths (R8)
    paths = {
        "Plywood and epoxy": None,
        "Aluminium 5052 sheet, welded or riveted": {"bot": 2.5 * 2.68, "side": 2.0 * 2.68, "other": 2.0 * 2.68,
                                                     "frames": 0.55, "glass": 0.0, "hdpe": 1.0},
        "HDPE or polypropylene sheet, plastic welded": {"bot": 8 * 0.95, "side": 6 * 0.95, "other": 5 * 0.95,
                                                        "frames": 1.0, "glass": 0.0, "hdpe": 1.0},
    }
    ply_kg = m["by_mat"]["ply"]
    hw_kg = m["by_mat"]["hw"] + m["by_mat"]["sw"]        # all framing timber
    rest = hull - ply_kg - hw_kg - m["glass_epoxy"]
    rows = []
    for name, f in paths.items():
        if f is None:
            hm = hull
        else:
            panels = f["bot"] * m["a_bot"] + f["side"] * m["a_side"] + f["other"] * m["a_other"]
            hm = panels + hw_kg * f["frames"] + rest + A["fixings"]
        rows.append((name, hm, cap + hull - hm))
    for i, (name, hm, pay) in enumerate(rows, 1):
        out(f"P{i}", f"Build path: {name}; hull mass; load at 150 mm draft; ratio",
            f"{hm:.0f}; {pay:.0f}; {pay / hm:.1f}", "kg; kg; -", "R8" if i == 1 else None,
            "Met on paper (three paths documented)" if i == 1 else None)

    # decision results (LSK-DDR-003) and the figures behind the new R2 question (docs/REVIEW.md)
    W6, l6, _, k6 = combine([hb, gear] + six)
    r6 = float_at(W6, l6, k6)
    out("D1", "Six persons (450 kg) in the decided design, for comparison: deepest draft; over hull mass",
        f"{max(r6['T_aft'], r6['T_fwd']):.0f}; {450 / hull:.2f}", "mm; -")
    out("D2", "Hull mass at which the five-person rated load is 6 times hull mass", round(rated_kg / 6, 1), "kg")
    out("D3", "Load carried at 150 mm draft over hull mass (as H8)", round(cap / hull, 2), "")
    # the aft-crew rule on its own (stern quarter foam fitted): already in F4 and F5; rule result below
    rule = [(q[0], 1800.0 if q[1] == 400.0 else q[1], q[2], q[3]) for q in sw_persons]
    Wr, lr, _, kr = combine([(fixed, 1700.0, 0, 150.0), (wm, interp(tab, zw, "wx"), 0, interp(tab, zw, "wz"))] + rule)
    trim_r = math.degrees((fx - lr) / 1000 / GML)
    out("F10", "Swamped, with the aft-crew rule (aft crew moves amidships): trim; freeboard at the transom; at the bow",
        f"{trim_r:.2f}; {P['D'] - (zw + math.radians(trim_r) * xc * 1000):.0f}; "
        f"{P['D'] - (zw - math.radians(trim_r) * (P['L'] - xc * 1000)):.0f}", "deg; mm; mm", "R5", "Met on paper")
    qf = sum(vol(NAMED[n]) for n in NAMED if n.startswith("quarter foam")) * 1e-9
    out("F11", "Of the foam in F1, the two stern quarter modules", round(qf * 1000, 1), "L")

    # cost (R9)
    with (ROOT / "bom" / "bom.csv").open() as fh:
        cost = sum(float(rw["qty"]) * float(rw["unit_cost_usd"]) for rw in csv.DictReader(fh))
    out("C1", "Estimated cost of the constructable design (bom/bom.csv)", round(cost), "USD", "R9",
        f"Over the value-engineering target by USD {cost - 1500:.0f}" if cost > 1500 else
        f"Under the value-engineering target by USD {1500 - cost:.0f}")
    out("R10", "Fin drive", "not designed in the first prototype", "", "R10", "Not shown on paper")

    with (ROOT / "docs" / "04-calcs" / "results.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["tag", "item", "value", "unit", "requirement", "status"])
        w.writeheader()
        w.writerows(OUT)


if __name__ == "__main__":
    main()
