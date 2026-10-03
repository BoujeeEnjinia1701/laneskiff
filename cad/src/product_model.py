"""LaneSkiff product appearance model (build123d), TRL 3, constructable design (LSK-DDR-002).

Finished-product look for photoreal renders, built from the constructable model: every part of
cad/src/model.py build_all() is used as it is (panels, frames, inwales, stringers, bench modules,
bow box, strakes, skids, joint bolts, stern step, handles, pole, paddles, bow eye and line).
Only the look is added, as recorded in docs/REVIEW.md: painted topsides (high-visibility orange
outside, light grey inside), a wet concrete lane slab under the boat, and a 1.75 m mannequin
standing on the far side of the boat for scale (never between the camera and the boat). The detail
view repeats the stern of the aft half, cut back, with the step deployed.
APPEARANCE MODEL ONLY: no tolerances, no fabrication detail. CONCEPT, NOT FOR FABRICATION.

Axes as model.py: X from the transom forward, Y to port, Z up from the outside of the bottom.
Groups: "shell" (everything seen from outside), "internal" (foam cores), "context" (lane slab,
mannequin), "rung" (kick rung, exploded view only), "stern" (the detail view only).

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]

from build123d import Box, Pos  # noqa: E402
import model as M  # noqa: E402

TITLE = "LaneSkiff: two-piece flood rescue skiff with a stern boarding step"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "internal", "context"], "explode": False, "el": 24, "az": -32,
     "note": "Product render from the bow and starboard side, above (about 24 deg elevation): the assembled 3.6 m skiff "
             "on a wet lane, orange topsides, foam bench modules along both sides, stern step float lowered (kick rung "
             "rolled up); a 1.75 m person stands on the far side of the boat for scale"},
    {"name": "exploded", "groups": ["shell", "internal", "rung"], "explode": True, "el": 26, "az": -40,
     "note": "Exploded view from the bow and starboard side, above (about 26 deg elevation): forward half pulled "
             "forward, stern step pulled aft, bench modules, foam, inwales, handles and gear lifted; lane and person "
             "not shown"},
    {"name": "detail", "groups": ["stern"], "explode": False, "el": 18, "az": -150,
     "note": "Detail of the stern from aft and to starboard (about 18 deg elevation): the step float on its strap "
             "hinges behind the hinge rail, the stop straps from the transom, the kick rung below, and the two "
             "transom grab handles"},
]

C_PAINT = "#F26B1D"      # high-visibility orange topsides and bottom
C_INSIDE = "#D9D4CC"     # light grey painted inside
C_WOOD = "#9A6A3A"       # varnished hardwood
C_FOAM = "#F2D04B"
C_COVER = "#E2621B"
C_STRAP = "#1E40AF"
C_HDPE = "#1F2933"
C_STEEL = "#A9B0B8"
C_STEP = "#0F766E"
C_ROPE = "#F5F5F4"
C_CLAY = "#B9B4AC"
C_LANE = "#8D8A85"


def look(name):
    """(colour, material, group, explode) for a model part name."""
    n = name
    fwd = 0.0
    if n.startswith(("bottom", "side")):
        return C_PAINT, "painted", "shell", (0, 0, -250 if n.startswith("bottom") else 0)
    if n.startswith(("stern transom", "bow transom", "joint bulkhead", "bow box wall", "bow deck")):
        return C_INSIDE, "painted", "shell", (fwd, 0, 0)
    if n.startswith(("ring frame", "inwale", "stringer", "knuckle floor", "bench rail", "bow eye pad")):
        return C_WOOD, "wood", "shell", (0, 0, 380 if n.startswith("inwale") else 150)
    if n.startswith(("bench foam", "bow foam", "step float foam")):
        return C_FOAM, "rubber", "internal", (0, 0, 760)
    if n.startswith("bench cover"):
        return C_COVER, "fabric", "shell", (0, 0, 560)
    if n.startswith(("bench straps", "stop straps", "kick rung straps")):
        return C_STRAP, "fabric", "shell", (0, 0, 620)
    if n.startswith(("rub strake", "skid")):
        return C_HDPE, "plastic", "shell", (0, 0, -480 if n.startswith("skid") else 260)
    if n.startswith(("joint bolt", "alignment pin", "rail bolts", "bow eye", "transom grab", "carry handles",
                     "strap hinges", "pad eyes", "float pad eyes", "transom pad eyes")):
        return C_STEEL, "metal", "shell", (0, 0, 520 if "handles" in n else 0)
    if n.startswith(("hinge rail", "transom backing block", "step float rim", "kick rung")):
        return C_WOOD, "wood", "shell", (0, 0, 0)
    if n.startswith("step float"):
        return C_STEP, "painted", "shell", (0, 0, 0)
    if n.startswith("push pole"):
        return C_STEEL, "metal", "shell", (0, 0, 1000)
    if n.startswith("paddles"):
        return "#2563EB", "plastic", "shell", (0, 0, 1000)
    if n.startswith("bow line"):
        return C_ROPE, "fabric", "shell", (300, 0, 300)
    return "#9CA3AF", "plastic", "shell", (0, 0, 0)


def product_parts(p=M.PARAMS):
    rows = M.build_all(p)
    out = []

    def add(name, shape, color, material, bom, group, explode=(0, 0, 0)):
        out.append({"name": name, "shape": shape, "color": color, "material": material, "bom": bom,
                    "group": group, "explode": tuple(explode)})

    for n, h, b, s in rows:
        col, mat, grp, ex = look(n)
        ex = list(ex)
        if h == M.FWD or n in ("carry handles forward", "bow eye", "bow line, coiled"):
            ex[0] += 900.0
        if h == "step":
            ex[0] -= 650.0
        if n.startswith("kick rung"):
            grp = "rung"            # rolled up on the float when the boat is on land: exploded view only
        add(n[0].upper() + n[1:], s, col, mat, b, grp, ex)
    # context: a wet concrete lane under the boat, and a person standing on the far (port) side
    add("Lane, wet concrete (context)", Pos(1600, 350, -48) * Box(4800, 2500, 80), C_LANE, "clay", None, "context")
    from context_parts import mannequin
    person = Pos(1700, 1250, -8) * mannequin(1750, "stand")      # faces -Y, toward the boat, beyond it from the camera
    add("Person, 1.75 m (scale), standing beside the boat", person, C_CLAY, "clay", None, "context")
    # detail: the stern of the aft half cut back, with the step deployed
    win = M.box(-700, 650, -900, 900, -500, 900)
    for n, h, b, s in rows:
        if h in (M.AFT, "step") or n in ("transom grab handles", "carry handles aft"):
            cut = s & win
            if cut is not None and cut.volume > 1:
                col, mat, _, _ = look(n)
                add(f"Stern: {n}", cut, col, mat, b, "stern")
    return out


if __name__ == "__main__":
    for q in product_parts():
        s = q["shape"]
        print(f"{q['name']:55s} {q['group']:9s} {q['material']:8s} vol={s.volume / 1000:10.1f} cm3")
