"""
Video 204: Tangent Spaces and Vector Fields -- Differential Geometry Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video204_TangentSpacesVectorFields

Topics: Tangent spaces, tangent vectors as derivations, coordinate
        vector fields, vector fields, pushforward, tangent bundle.

Prerequisites: Video 203 (Manifolds Introduction), Linear Algebra,
               Multivariable Calculus.

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


class Video204_TangentSpacesVectorFields(Scene):
    """Tangent Spaces and Vector Fields -- Differential Geometry Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_tangent_as_curves()
        self.scene3_tangent_as_derivations()
        self.scene4_tangent_space()
        self.scene5_vector_fields()
        self.scene6_pushforward()
        self.scene7_tangent_bundle()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook — Vectors Without an Ambient Space
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "In R three, a tangent vector to a "
            "surface lives in the surrounding "
            "space. But on an abstract manifold, "
            "there's no ambient space. How do we "
            "define tangent vectors? This is "
            "one of the deepest constructions "
            "in differential geometry.",
            duration=9,
        )
        play_intro(self, "Tangent Spaces & Vector Fields", "Differential Geometry")

        title = self.ly.title("Vectors Without an Ambient Space")

        items = [
            Text(
                "Surface in R\u00B3: tangent vector = arrow in R\u00B3",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Abstract manifold: no surrounding space!",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Solution: tangent vectors as directional derivatives",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Tangent Vectors as Equivalence Classes of Curves
    # ------------------------------------------------------------------ #
    def scene2_tangent_as_curves(self):
        self.ly.section_divider("1", "Approach One: Curves")
        self.add_subcaption(
            "A curve gamma passing through a point p "
            "defines a velocity vector. Two curves "
            "give the same tangent vector if their "
            "coordinate representations have the "
            "same derivative at t equals zero. "
            "This is independent of the chart "
            "chosen.",
            duration=9,
        )

        title = self.ly.title("Tangent Vectors as Curves")

        items = [
            Text(
                "Curve \u03B3(t) with \u03B3(0) = p",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Velocity: d(\u03C6 \u2218 \u03B3)/dt at t=0",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Same velocity \u2192 same tangent vector",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Chart-independent (invariant notion)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Tangent Vectors as Derivations
    # ------------------------------------------------------------------ #
    def scene3_tangent_as_derivations(self):
        self.ly.section_divider("2", "Approach Two: Derivations")
        self.add_subcaption(
            "A tangent vector v at p is a linear "
            "map from smooth functions to real "
            "numbers satisfying the Leibniz rule. "
            "It acts like a directional derivative. "
            "This abstract definition is elegant "
            "and completely intrinsic. It doesn't "
            "refer to any embedding.",
            duration=9,
        )

        title = self.ly.title("Tangent Vectors as Derivations")

        leibniz = MathTex(
            r"v(fg) = v(f) \cdot g(p) + f(p) \cdot v(g)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(leibniz, color=PRIMARY)

        self.wait(0.5)

        items = [
            Text(
                "v: C^\u221E(M) \u2192 R is a derivation at p",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Acts like a directional derivative",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Completely intrinsic (no embedding needed)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=formula_box)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: The Tangent Space
    # ------------------------------------------------------------------ #
    def scene4_tangent_space(self):
        self.add_subcaption(
            "The tangent space T sub p M is the set "
            "of all tangent vectors at the point p. "
            "It forms an n-dimensional real vector "
            "space. Given coordinates x one through "
            "x n, the partial derivatives form a "
            "natural basis for T sub p M.",
            duration=9,
        )
        title = self.ly.title("The Tangent Space T_p M")

        basis = MathTex(
            r"T_p M = \mathrm{span}\left\{"
            r"\frac{\partial}{\partial x^1}, \ldots, "
            r"\frac{\partial}{\partial x^n}"
            r"\right\}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(basis, color=PRIMARY)

        self.wait(0.5)

        items = [
            Text(
                "n-dimensional real vector space at each point",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Coordinate basis: \u2202/\u2202x\u1D62",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Changes under coordinate transformation",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=formula_box)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Vector Fields
    # ------------------------------------------------------------------ #
    def scene5_vector_fields(self):
        self.ly.section_divider("3", "Vector Fields")
        self.add_subcaption(
            "A vector field assigns a tangent vector "
            "to every point on the manifold. In "
            "coordinates, it's written as a sum "
            "of component functions times the "
            "coordinate basis vectors. A vector "
            "field is smooth if all its "
            "components are smooth functions.",
            duration=9,
        )

        title = self.ly.title("Vector Fields")

        vf = MathTex(
            r"X = X^i(x) \frac{\partial}{\partial x^i}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(vf, color=PRIMARY)

        self.wait(0.5)

        items = [
            Text(
                "X: M \u2192 TM (smooth section of tangent bundle)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Component functions X\u2071(x) must be C^\u221E",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Einstein summation convention: sum over i",
                font_size=BODY_SIZE, color=DIM, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=formula_box)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Pushforward
    # ------------------------------------------------------------------ #
    def scene6_pushforward(self):
        self.add_subcaption(
            "A smooth map between manifolds induces "
            "a map between their tangent spaces "
            "called the pushforward. The pushforward "
            "F star sends tangent vectors at p "
            "to tangent vectors at F of p. Its "
            "matrix representation is the "
            "Jacobian matrix.",
            duration=9,
        )
        title = self.ly.title("The Pushforward Map")

        pf_def = MathTex(
            r"F_* : T_p M \to T_{F(p)} N",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(pf_def, color=PRIMARY)

        self.wait(0.5)

        items = [
            MathTex(
                r"(F_* v)(f) = v(f \circ F)",
                font_size=BODY_SIZE, color=SECONDARY,
            ),
            Text(
                "Matrix: Jacobian of F in coordinates",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Generalizes directional derivative",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=formula_box)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: The Tangent Bundle
    # ------------------------------------------------------------------ #
    def scene7_tangent_bundle(self):
        self.ly.section_divider("4", "The Tangent Bundle")
        self.add_subcaption(
            "The tangent bundle TM is the union of "
            "all tangent spaces. It's a manifold "
            "of dimension two n. A smooth "
            "assignment of a tangent vector at "
            "each point is called a section of "
            "the tangent bundle, which is "
            "precisely a vector field.",
            duration=9,
        )

        title = self.ly.title("The Tangent Bundle")

        bundle = MathTex(
            r"TM = \bigcup_{p \in M} T_p M",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(bundle, color=PRIMARY)

        self.wait(0.5)

        items = [
            Text(
                "dim(TM) = 2 \u00D7 dim(M)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Sections of TM = vector fields",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Fundamental object in differential geometry",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=formula_box)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary_outro(self):
        self.add_subcaption(
            "To summarize. Tangent vectors can "
            "be defined as curves through a "
            "point, or as derivations acting on "
            "functions. The tangent space is an "
            "n-dimensional vector space at each "
            "point. Vector fields are smooth "
            "sections of the tangent bundle. "
            "The pushforward maps tangent "
            "spaces between manifolds.",
            duration=10,
        )
        title = self.ly.title("Summary")

        items = [
            Text(
                "Tangent vectors: curves or derivations",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "T_p M: n-dim vector space, basis \u2202/\u2202x\u1D62",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Vector fields: X = X\u2071\u2202/\u2202x\u1D62",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

        self.add_subcaption(
            "That's tangent spaces and vector fields. "
            "Next time, we'll meet their duals: "
            "differential forms. Thanks for watching!",
            duration=6,
        )
        play_outro(self, "Differential Forms", "Differential Geometry")
