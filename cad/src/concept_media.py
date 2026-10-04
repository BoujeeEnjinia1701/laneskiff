"""LaneSkiff concept media (TRL 3, constructable design of LSK-DDR-002 and LSK-DDR-003), generated from the model.

Run from the repo root:  python cad/src/concept_media.py
Takes every part of cad/src/model.py and renders the media set with .kit/concept.py:
media/hero.png (with a 1.75 m person), media/cutaway.png (a cut across the boat through the aft
benches), media/exploded.png (halves, step and fittings pulled apart; numbers match bom/bom.csv),
media/concept-blueprint.png, .pdf and .svg (LSK-DWG-010), media/model.glb and media/viewer.html.
No flow diagram: the boat moves no energy or material (it carries people, which the sheet states).
Figures on the sheet come from docs/04-calcs/results.csv (LSK-CAL-001).
CONCEPT, NOT FOR FABRICATION.
"""
import csv
import functools
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import concept as K  # noqa: E402
from concept import Part, render_all  # noqa: E402
from build123d import Compound  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
PROJECT = "LaneSkiff"
TITLE = "Two-piece flood rescue skiff with a stern boarding step"

# media groups: (label, BOM line, colour, name prefixes, explode offset)
GROUPS = [
    ("Bottom panels", 1, "#C9A46C", ("bottom",), (0, 0, -260)),
    ("Side panels", 2, "#E2C28F", ("side",), (0, 0, 0)),
    ("Stern transom", 3, "#B07D46", ("stern transom",), (-150, 0, 0)),
    ("Bow transom", 4, "#B07D46", ("bow transom",), (150, 0, 0)),
    ("Joint bulkheads", 5, "#A0703F", ("joint bulkhead",), (0, 0, 0)),
    ("Ring frames", 6, "#7C4A1E", ("ring frame",), (0, 0, 180)),
    ("Inwales", 7, "#8B5A2B", ("inwale",), (0, 0, 380)),
    ("Stringers and knuckle floor", 8, "#6F4521", ("stringer", "knuckle floor"), (0, 0, 120)),
    ("Bench modules: rails, covers, straps", 9, "#EA580C", ("bench rail", "bench cover", "bench straps"), (0, 0, 560)),
    ("Bow box wall and deck", 9, "#D9B98C", ("bow box wall", "bow deck"), (0, 0, 560)),
    ("Buoyancy foam", 10, "#FACC15", ("bench foam", "bow foam", "step float foam"), (0, 0, 760)),
    ("Stern quarter foam modules", 29, "#F97316", ("quarter cover", "quarter foam", "quarter strap"), (0, 0, 820)),
    ("Joint bolts and nut plates", 11, "#374151", ("joint bolt", "alignment pin"), (0, 0, 0)),
    ("Rub strakes", 12, "#1F2937", ("rub strake",), (0, 0, 260)),
    ("Bottom skids", 13, "#111827", ("skid",), (0, 0, -480)),
    ("Stern step", 14, "#0F766E", ("hinge rail", "transom backing block", "rail bolts", "step float rim",
                                    "step float top deck", "step float bottom deck", "strap hinges"), (-650, 0, 0)),
    ("Stop straps and pad eyes", 15, "#1D4ED8", ("stop straps", "float pad eyes", "transom pad eyes"), (-650, 0, 0)),
    ("Kick rung", 16, "#14B8A6", ("kick rung",), (-650, 0, 0)),
    ("Transom grab handles", 17, "#9CA3AF", ("transom grab handles",), (-150, 0, 300)),
    ("Carry handles", 18, "#6B7280", ("carry handles",), (0, 0, 520)),
    ("Push pole (two sections)", 19, "#94A3B8", ("push pole",), (0, 0, 1000)),
    ("Paddles", 20, "#2563EB", ("paddles",), (0, 0, 1000)),
    ("Bow eye and bow line", 21, "#DC2626", ("bow eye", "bow line"), (300, 0, 300)),
]


def R():
    rows = {r["tag"]: r for r in csv.DictReader((ROOT / "docs" / "04-calcs" / "results.csv").open())}
    return lambda t: rows[t]["value"]


def media_parts(rows=None, explode_halves=0.0):
    rows = rows or M.build_all(P)
    out = []
    for label, bom, col, pre, ex in GROUPS:
        sh = [s for n, h, b, s in rows if n.startswith(pre)]
        if not sh:
            continue
        if explode_halves:
            # forward half pieces travel forward with the half
            fwd = [s for n, h, b, s in rows if n.startswith(pre) and h == M.FWD]
            aft = [s for n, h, b, s in rows if n.startswith(pre) and h != M.FWD]
            if fwd and aft:
                out.append(Part(label, M.flat(aft), col, bom, ex))
                out.append(Part(label + " (forward half)", M.flat(fwd), col, None,
                                (ex[0] + explode_halves, ex[1], ex[2])))
                continue
            if fwd:
                ex = (ex[0] + explode_halves, ex[1], ex[2])
        out.append(Part(label, M.flat(sh), col, bom, ex))
    return out


def cross_section(parts, xc=1000.0):
    """Cut across the boat at xc (through the aft benches), keeping the part forward of the cut."""
    cutter = M.box(xc, 6000, -2000, 2000, -1000, 2000)
    out = []
    for q in parts:
        s = q.shape & cutter
        if s is not None and s.volume > 1:
            out.append(Part(q.name, s, q.color, q.bom))
    return out


def web(parts):
    """Coarse glTF tessellation (1 mm chord, 0.35 rad) keeps media/model.glb a few MB."""
    import build123d as bd
    orig = bd.export_gltf
    bd.export_gltf = functools.partial(orig, linear_deflection=1.0, angular_deflection=0.35)
    K.export_gltf = bd.export_gltf
    try:
        return K.export_web_model(parts, "media", title=f"{PROJECT}: {TITLE}")
    finally:
        bd.export_gltf = orig


def main():
    r = R()
    rows = M.build_all(P)
    parts = media_parts(rows)
    render_all(
        parts, project=PROJECT, title=f"{TITLE} concept", dwg_no="LSK-DWG-010",
        key_figures=[
            "Hull 3.6 m long, 1.20 m beam over the rub strakes, 0.40 m deep; two halves of 1.8 m",
            f"Hull {float(r('M1')):.0f} kg (halves {float(r('M2')):.0f} and {float(r('M3')):.0f} kg); okoume and epoxy",
            f"Rated load five persons, 375 kg; deepest draft {max(float(v) for v in r('H2').split('; ')[1:]):.0f} mm",
            f"Stern-step boarding heel {float(r('B1')):.1f} deg; over the side {float(r('B3')):.1f} deg",
            f"Swamped with rated persons: afloat, {r('F5').split('; ')[0]} mm freeboard at the transom (30 L stern foam)",
            f"Halves join with eight M10 bolts and one spanner in about {float(r('T1')):.0f} min (estimate)",
        ],
        scale_figure=True, web_model=False, cut=False,
    )
    K._render(media_parts(rows, explode_halves=900.0), ROOT / "media" / "exploded.png", offsets=True, labels=True,
              elev=24, azim=-58, size=(11, 7.5), title=f"{PROJECT}: exploded view",
              note="Seen from the front right and above, 24 deg elevation; halves pulled apart along the boat, stern "
                   "step pulled aft, fittings lifted; numbers match bom/bom.csv")
    K._render(cross_section(media_parts(M.build_all(P))), ROOT / "media" / "cutaway.png", elev=14, azim=-160,
              size=(10, 7.5), title=f"{PROJECT}: cutaway across the aft half",
              note="Cut across the boat 1.0 m forward of the transom, seen from aft and slightly to starboard, 14 deg "
                   "elevation. The foam bench modules sit outboard against the sides, under the inwales, so a swamped "
                   "boat floats level; the floor between them is clear for people. The two stern quarter modules "
                   "stand either side of the step opening, aft of the cut")
    web(media_parts(M.build_all(P)))
    for d in ("_views", "_views_fig"):
        shutil.rmtree(ROOT / "media" / d, ignore_errors=True)


if __name__ == "__main__":
    main()
