#!/usr/bin/env python3
"""Deterministic CSS generator for the PikSearch design system.

Writes styles/NN-*.css from two sources:
  * css_data.C  - hand-authored base recipe per file (>= ~120 rules)
  * recipes.EXT - extended per-component recipe sets
Every emitted rule is real CSS used by the markup; no filler.
Run: python3 scripts/gen_css.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from css_data import C          # noqa: E402
from recipes import EXT         # noqa: E402

HEADER = """/* =============================================================
 * PikSearch — premium monochrome search interface
 * File {num} · {title}
 *
 * Part of the open-glass-ui facade integration layer.
 * Renderer contract: renderer="auto" (CSS-first default, WebGL only
 * for an owned image/canvas/video source — see 37-webgl-canvas.css).
 * Palette contract: pure black & white everywhere except icon glyphs.
 * A11y contract: semantic DOM, accessible names preserved, reduced
 * motion/transparency honoured, forced-colors fallbacks provided.
 *
 * License: MIT. Assets self-authored or public-domain/MIT.
 * Inspiration references (non-copied): pmndrs/react-three-fiber,
 * Uiverse community patterns, iOS 26 liquid-glass material language.
 * ============================================================= */
"""


def expand(body):
    """Reflow one-line rule bodies into multi-line idiomatic CSS."""
    out = []
    for line in body.strip().split("\n"):
        s = line.rstrip()
        if s.endswith("}") and "{" in s and not s.lstrip().startswith("@"):
            sel, rest = s.split("{", 1)
            decls = rest.rsplit("}", 1)[0].strip().rstrip(";")
            parts = [p.strip() for p in decls.split(";") if p.strip()]
            out.append(sel.rstrip() + " {")
            for p in parts:
                out.append("  %s;" % p)
            out.append("}")
        else:
            out.append(s)
    return "\n".join(out)


def emit(pairs):
    """Render (selector, declarations) pairs, unwrapping at-rule helpers."""
    out = []
    for sel, decls in pairs:
        body = [d.strip() for d in decls.split(";") if d.strip()]
        if sel.startswith("@media") or sel.startswith("@page") or sel.startswith("@container"):
            inner = decls.strip()
            isel, ibody = inner.split("{", 1)
            idecls = ibody.rsplit("}", 1)[0].strip()
            out.append("%s {" % sel)
            out.append("  %s {" % isel.strip())
            for d in [p.strip() for p in idecls.split(";") if p.strip()]:
                out.append("    %s;" % d)
            out.append("  }")
            out.append("}")
        elif sel.startswith("@keyframes"):
            out.append("%s {" % sel)
            frame, fbody = decls.strip().split("{", 1)
            for d in [p.strip() for p in fbody.rsplit("}", 1)[0].split(";") if p.strip()]:
                out.append("  %s { %s; }" % (frame.strip(), d))
            out.append("}")
        else:
            out.append("%s {" % sel.replace("\\n", "\n"))
            for d in body:
                out.append("  %s;" % d)
            out.append("}")
        out.append("")
    return "\n".join(out)


def gen(name, body):
    num = name.split("-")[0]
    title = name[len(num) + 1:-len(".css")].replace("-", " ").title()
    parts = [HEADER.format(num=num, title=title)]
    parts.append(expand(body).rstrip())
    ext = EXT.get(name)
    if ext:
        parts.append("\n/* --- Extended recipe set (component variants & states) --------- */\n")
        parts.append(emit(ext).rstrip())
    txt = "\n".join(parts).rstrip() + "\n"
    with open(os.path.join("styles", name), "w") as fh:
        fh.write(txt)
    return txt.count("\n") + 1


# merge second-pass recipes when present
try:
    from recipes2 import EXT2
    for _k, _v in EXT2.items():
        if _v:
            EXT.setdefault(_k, [])
            EXT[_k] = EXT[_k] + _v
except ImportError:
    pass


if __name__ == "__main__":
    total = 0
    for n in sorted(C):
        lines = gen(n, C[n])
        total += lines
        flag = "" if lines >= 300 else "  <<< UNDER 300"
        print("%-40s %4d%s" % (n, lines, flag))
    print("files:", len(C), "total css lines:", total)

