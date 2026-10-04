"""LaneSkiff general arrangement sheet LSK-DWG-001, Rev P3 (TRL 3; LSK-DDR-002 and LSK-DDR-003 applied).

Run from the repo root:  python cad/src/sheets.py
Writes cad/drawings/LSK-DWG-001.svg, .pdf and .png from the parametric model in cad/src/model.py
with .kit/drawing.py: the assembled skiff (front, top and right views), section A-A across the
aft half at 1:10, and the main sizes. Dimensions come from PARAMS, so they follow any parameter
change. The concept blueprint in media/ is LSK-DWG-010; the making sketches are LSK-DWG-101 onward
(cad/src/build_plan_media.py).
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from build123d import Compound  # noqa: E402
from drawing import Sheet, _t, project_views, INK, MUTED  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
DATE = "2026-10-03"
SEC_X = 1000.0          # section A-A: across the aft half, through the benches
SEC_K = 0.1             # 1:10


def leader(x1, y1, x2, y2, text, anchor="start"):
    return [f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{MUTED}" stroke-width="0.15"/>',
            f'<circle cx="{x1:.2f}" cy="{y1:.2f}" r="0.5" fill="{INK}"/>',
            _t(x2 + (1 if anchor == "start" else -1), y2 + 0.8, text, 2.1, 400, INK, anchor)]


def main():
    work = ROOT / "cad" / "drawings" / "_ga_views"
    rows = M.build_all(P)
    asm = M.flat([s for *_, s in rows])
    views = project_views(asm, work)
    slab = M.box(SEC_X - 60, SEC_X, -900, 900, -50, 600)
    def cut(s):
        r = s & slab
        return r if r is not None and r.volume > 1 else None
    sec = M.flat([c for c in (cut(s) for n, h, b, s in rows if h in (M.AFT, "outfit")) if c is not None])
    sv = project_views(sec, work / "sec")
    sb = sec.bounding_box()
    s = Sheet(project="LaneSkiff", title="Two-piece flood rescue skiff: general arrangement",
              dwg_no="LSK-DWG-001", rev="P3", author="Amish Chadha", date=DATE,
              material="Okoume plywood, softwood framing and epoxy; parts per bom/bom.csv. PRELIMINARY, NOT FOR FABRICATION",
              revisions=[("P1", "Preliminary GA for TRL 3 (from cad/src/model.py)", DATE, "AC"),
                         ("P2", "LSK-DDR-002: design for construction", DATE, "AC"),
                         ("P3", "LSK-DDR-003: light timber, bottom 60 wider, 4 mm sides, stern quarter foam", DATE, "AC")])
    s.add_ortho(views)
    vw = (sb.max.Y - sb.min.Y) * SEC_K
    vh = (sb.max.Z - sb.min.Z) * SEC_K
    x0, y0 = 279.0, 36.0
    s.add_svg(sv["right"], x0, y0, vw, vh, scale=SEC_K)
    L = [_t(x0 + vw / 2, y0 + vh + 6, "SECTION A-A", 2.8, 600, INK, "middle"),
         _t(x0 + vw / 2, y0 + vh + 10, f"Scale 1:10; looking aft (along -X), {SEC_X / 1000:.1f} m forward of the transom",
            2.2, 400, MUTED, "middle")]
    cy, cz = (sb.min.Y + sb.max.Y) / 2, (sb.min.Z + sb.max.Z) / 2
    X = lambda y: x0 + vw / 2 + (y - cy) * SEC_K   # noqa: E731
    Z = lambda z: y0 + vh / 2 - (z - cz) * SEC_K   # noqa: E731
    tx = x0 + vw + 3
    yb = (P["bench_y"] + M.half(180, P["t_side"], P)) / 2
    L += leader(X(-yb), Z(180), x0 - 1, y0 + vh + 16, "FOAM MODULE IN COVER (9, 10)", "end")
    L += leader(X(M.half(380, 16, P)), Z(380), tx, y0 + 2, "INWALE (7)")
    L += leader(X(M.half(385, -6, P)), Z(385), tx, y0 + 8, "RUB STRAKE (12)")
    L += leader(X(M.half(200, 3, P)), Z(200), tx, y0 + 14, "SIDE 4 PLY (2)")
    L += leader(X(P["bench_y"] - 20), Z(16), tx, y0 + 20, "BENCH RAIL (9)")
    L += leader(X(P["stringer_y"]), Z(16), tx, y0 + 26, "STRINGER (8)")
    L += leader(X(P["stringer_y"]), Z(-4), tx, y0 + 32, "SKID (13)")
    L += leader(X(0), Z(3), tx, y0 + 38, "BOTTOM 6 PLY (1)")
    s._layers += L
    bb = asm.bounding_box()
    s.add_notes("Main sizes and figures (mm unless stated)", [
        f"Length 3,600 in two halves of 1,800; beam overall {bb.max.Y - bb.min.Y:,.0f}",
        f"Depth 400; bottom {2 * P['half_bot']:,.0f} wide at the chine; sides flared 8 deg",
        "Bottom flat to 2,700 from the transom, raked to 200 at the bow",
        "Each half closed by its own bulkhead; joint: 8 M10 x 80 bolts",
        "Bench modules 330 from the centreline to the side, top 360",
        "Stern step float 450 x 600 x 90, hinged 40 behind the rail",
        "Kick rung 270 below the float; stop straps at 20 deg down",
        "Stern quarter foam 2 x 15 L, 250 clear way between (29)",
        "Rated load 5 persons (375 kg); see LSK-CAL-001 for drafts",
        "Third-angle; X from transom, Y to port; (n) = BOM line",
    ], x=276, y=118, width=146)
    out = s.save(ROOT / "cad" / "drawings" / "LSK-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
