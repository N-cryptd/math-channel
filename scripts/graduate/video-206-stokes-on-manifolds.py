"""
Video 206: Stokes' Theorem on Manifolds -- Differential Geometry Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video206_StokesOnManifolds

Topics: General Stokes' theorem, orientation, special cases (FTC, Green's,
        classical Stokes, divergence theorem), connection to Gauss-Bonnet,
        playlist recap.

Prerequisites: Video 205 (Differential Forms), Video 202 (Gauss-Bonnet),
               Multivariable Calculus (integral theorems).

Quality Rules (mandatory):
1. Max 5 visible elements per scene
2. Use LayoutEngine for ALL positioning
3. Progressive disclosure
4. Narration timing ~12 words / 5s
5. Call ly.clear() between scenes
6. MathTex: raw strings with single backslashes
"""

from manim import *
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video206_StokesOnManifolds(Scene):
    """Stokes' Theorem on Manifolds -- Differential Geometry Playlist (FINALE)."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_statement()
        self.scene3_orientation()
        self.scene4_ftc()
        self.scene5_greens_stokes()
        self.scene6_divergence()
        self.scene7_gauss_bonnet()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook — One Theorem to Rule Them All
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "The fundamental theorem of calculus, "
            "Green's theorem, the classical Stokes' "
            "theorem, the divergence theorem, and "
            "even Gauss-Bonnet. They're ALL special "
            "cases of one single, beautiful result: "
            "the general Stokes' theorem on "
            "manifolds.",
            duration=10,
        )
        play_intro(self, "Stokes on Manifolds", "Differential Geometry")

        title = self.ly.title("One Theorem to Rule Them All")

        items = [
            Text(
                "FTC, Green's, Stokes, Divergence, Gauss-Bonnet",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "All are special cases of ONE theorem",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "The grand finale of differential geometry",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Statement of the General Stokes' Theorem
    # ------------------------------------------------------------------ #
    def scene2_statement(self):
        self.ly.section_divider("1", "The General Stokes' Theorem")
        self.add_subcaption(
            "Let Omega be an oriented k-dimensional "
            "manifold with boundary. Let omega be "
            "a k minus one form on Omega. Then the "
            "integral of omega over the boundary "
            "of Omega equals the integral of d "
            "omega over Omega itself. The boundary "
            "integral equals the interior integral "
            "of the exterior derivative.",
            duration=11,
        )

        title = self.ly.title("Statement")

        stokes = MathTex(
            r"\int_{\partial \Omega} \omega"
            r"= \int_{\Omega} d\omega",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(stokes, color=ACCENT)

        self.wait(0.5)

        items = [
            Text(
                "\u03A9: k-dimensional oriented manifold with boundary",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "\u03C9: (k\u22121)-form on \u03A9",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "\u2202\u03A9: boundary of \u03A9 (k\u22121 dimensional)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=formula_box)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Orientation of the Boundary
    # ------------------------------------------------------------------ #
    def scene3_orientation(self):
        self.add_subcaption(
            "The boundary of Omega inherits an "
            "orientation from Omega. In two "
            "dimensions, this means the boundary "
            "is traversed counterclockwise. In "
            "three dimensions, the outward normal "
            "determines the boundary orientation. "
            "Getting the orientation wrong flips "
            "the sign of the integral.",
            duration=10,
        )
        title = self.ly.title("Orientation of \u2202\u03A9")

        items = [
            Text(
                "2D: boundary traversed counterclockwise",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3D: outward normal determines orientation",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Wrong orientation \u2192 sign change!",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Special Case — Fundamental Theorem of Calculus
    # ------------------------------------------------------------------ #
    def scene4_ftc(self):
        self.ly.section_divider("2", "Special Cases")
        self.add_subcaption(
            "The simplest case is k equals one. "
            "Omega is the interval a to b. The "
            "boundary is b minus a. The form "
            "omega is f, so d omega is f prime "
            "dx. Stokes gives f of b minus f "
            "of a equals the integral from a to "
            "b of f prime dx. The fundamental "
            "theorem of calculus!",
            duration=11,
        )
        title = self.ly.title("Case 1: Fundamental Theorem of Calculus")

        ftc = MathTex(
            r"f(b) - f(a) = \int_a^b f'(x) \, dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(ftc, color=PRIMARY)

        self.wait(0.5)

        detail = Text(
            "k=1: \u03A9=[a,b], \u03C9=f (0-form), d\u03C9=f' dx",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(detail, DOWN, formula_box)
        self.play(FadeIn(detail, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Special Case — Green's and Classical Stokes
    # ------------------------------------------------------------------ #
    def scene5_greens_stokes(self):
        self.add_subcaption(
            "For k equals two, we get Green's "
            "theorem. The form omega is P dx "
            "plus Q dy. Its exterior derivative "
            "is partial Q over partial x minus "
            "partial P over partial y times dx "
            "wedge dy. The integral over the "
            "boundary curve equals the double "
            "integral of the curl over the region.",
            duration=11,
        )
        title = self.ly.title("Case 2: Green's Theorem")

        green = MathTex(
            r"\oint_{\partial \Omega} (P\,dx + Q\,dy)"
            r"= \iint_\Omega "
            r"\left(\frac{\partial Q}{\partial x}"
            r"- \frac{\partial P}{\partial y}\right)"
            r"dA",
            font_size=BODY_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(green, color=PRIMARY)

        self.wait(0.5)

        classic = MathTex(
            r"\oint_{\partial S} \mathbf{F} \cdot d\mathbf{r}"
            r"= \iint_S (\nabla \times \mathbf{F})"
            r"\cdot d\mathbf{S}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(classic, DOWN, formula_box)
        self.play(Write(classic), run_time=NORMAL)

        self.wait(0.5)

        label = Text(
            "Classical Stokes' theorem (3D surface in R\u00B3)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(label, DOWN, classic)
        self.play(FadeIn(label, shift=LEFT * 0.15), run_time=FAST)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Special Case — Divergence Theorem
    # ------------------------------------------------------------------ #
    def scene6_divergence(self):
        self.add_subcaption(
            "For k equals three, Stokes' theorem "
            "becomes the divergence theorem. "
            "The boundary of a volume is its "
            "surface. The flux through the "
            "surface equals the integral of "
            "divergence over the volume. This "
            "is also called Gauss's theorem.",
            duration=10,
        )
        title = self.ly.title("Case 3: Divergence Theorem")

        div_thm = MathTex(
            r"\oiint_{\partial V} \mathbf{F} \cdot d\mathbf{S}"
            r"= \iiint_V (\nabla \cdot \mathbf{F}) \, dV",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(div_thm, color=PRIMARY)

        self.wait(0.5)

        note = Text(
            "k=3: flux through surface = integral of divergence",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, DOWN, formula_box)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Connection to Gauss-Bonnet
    # ------------------------------------------------------------------ #
    def scene7_gauss_bonnet(self):
        self.ly.section_divider("3", "Gauss-Bonnet as a Special Case")
        self.add_subcaption(
            "Remarkably, the Gauss-Bonnet theorem "
            "is also a special case of Stokes. "
            "The total curvature integral equals "
            "two pi times the Euler characteristic. "
            "This arises from integrating the "
            "Euler class, a topological differential "
            "form. The circle is complete: from "
            "geodesics to topology and back.",
            duration=11,
        )
        title = self.ly.title("Case 4: Gauss-Bonnet Theorem")

        gb = MathTex(
            r"\iint_S K \, dA = 2\pi \, \chi(S)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(gb, color=ACCENT)

        self.wait(0.5)

        items = [
            Text(
                "Gauss-Bonnet: Stokes' applied to the Euler class",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Curvature (geometry) = Euler characteristic (topology)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "The full circle: geodesics \u2192 forms \u2192 Stokes \u2192 Gauss-Bonnet",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=formula_box)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Playlist Recap
    # ------------------------------------------------------------------ #
    def scene8_summary_outro(self):
        self.add_subcaption(
            "Stokes' theorem on manifolds is the "
            "ultimate generalization of the "
            "fundamental theorem of calculus. "
            "It unifies FTC, Green's, classical "
            "Stokes, divergence theorem, and "
            "Gauss-Bonnet into one elegant "
            "equation. This completes our "
            "differential geometry journey, "
            "from curves in R n all the way "
            "to the most profound theorem "
            "in geometry.",
            duration=13,
        )
        title = self.ly.title("Differential Geometry: Complete")

        items = [
            Text(
                "Stokes: one theorem, five faces",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "\u222BK dA = 2\u03C0\u03C7: geometry meets topology",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "From curves (194) to Stokes (206): the full journey",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

        self.add_subcaption(
            "This concludes our Differential Geometry "
            "playlist. From curves in R n to the "
            "Gauss-Bonnet theorem and Stokes on "
            "manifolds. Thank you for watching "
            "this entire journey. See you in "
            "the next playlist!",
            duration=9,
        )
        play_outro(self, None, None)
