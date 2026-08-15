"""
Video 205: Differential Forms -- Differential Geometry Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video205_DifferentialForms

Topics: Differential forms, 1-forms, k-forms, wedge product, exterior
        derivative, closed and exact forms, integration preview.

Prerequisites: Video 204 (Tangent Spaces), Linear Algebra (dual spaces,
               alternating multilinear maps).

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


class Video205_DifferentialForms(Scene):
    """Differential Forms -- Differential Geometry Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_one_forms()
        self.scene3_k_forms()
        self.scene4_wedge_product()
        self.scene5_exterior_derivative()
        self.scene6_closed_exact()
        self.scene7_integration()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook — The Language of Integration
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Every integral you've ever computed, "
            "line integrals, surface integrals, "
            "flux integrals, is really the integral "
            "of a differential form. Differential "
            "forms are the natural language for "
            "integration on manifolds. They unify "
            "all the multivariable calculus "
            "integral theorems into one.",
            duration=11,
        )
        play_intro(self, "Differential Forms", "Differential Geometry")

        title = self.ly.title("The Language of Integration")

        items = [
            Text(
                "Line integrals, surface integrals, flux",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "All are integrals of differential forms",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "The unifying framework for multivariable calculus",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Differential 1-Forms
    # ------------------------------------------------------------------ #
    def scene2_one_forms(self):
        self.ly.section_divider("1", "Differential 1-Forms")
        self.add_subcaption(
            "A differential one-form at a point p "
            "is a linear map from the tangent space "
            "to the real numbers. It's an element "
            "of the cotangent space, the dual of "
            "the tangent space. In coordinates, "
            "a one-form is written as a sum of "
            "component functions times dx to the i.",
            duration=10,
        )

        title = self.ly.title("1-Forms: Dual to Vector Fields")

        one_form = MathTex(
            r"\omega = a_i(x) \, dx^i",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(one_form, color=PRIMARY)

        self.wait(0.5)

        items = [
            MathTex(
                r"\omega_p : T_p M \to \mathbb{R}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            Text(
                "dx^i is dual to \u2202/\u2202x^i",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Cotangent space T*_p M = dual of T_p M",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=formula_box)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Differential k-Forms
    # ------------------------------------------------------------------ #
    def scene3_k_forms(self):
        self.add_subcaption(
            "A k-form at a point p is an alternating "
            "k-linear map from the tangent space "
            "to the reals. Zero-forms are smooth "
            "functions. One-forms are dual to "
            "vectors. Two-forms measure areas. "
            "Three-forms measure volumes. The "
            "exterior derivative generalizes "
            "gradient, curl, and divergence.",
            duration=11,
        )
        title = self.ly.title("k-Forms")

        items = [
            Text(
                "0-forms: smooth functions f",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "1-forms: a_i dx^i (dual to vectors)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "2-forms: dx^i \u2227 dx^j (area elements)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "k-forms: alternating k-linear maps on T_p M",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Wedge Product
    # ------------------------------------------------------------------ #
    def scene4_wedge_product(self):
        self.ly.section_divider("2", "The Wedge Product")
        self.add_subcaption(
            "The wedge product combines a k-form "
            "and an l-form into a k plus l form. "
            "It is anticommutative: the wedge of "
            "alpha and beta equals minus the wedge "
            "of beta and alpha. This means that "
            "dx wedge dx equals zero, since it "
            "equals minus itself.",
            duration=10,
        )

        title = self.ly.title("Wedge Product \u2227")

        wedge_prop = MathTex(
            r"\alpha \wedge \beta = -\beta \wedge \alpha",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(wedge_prop, color=PRIMARY)

        self.wait(0.5)

        items = [
            MathTex(
                r"\omega \in \Omega^k, \;\eta \in \Omega^l"
                r"\;\Rightarrow\; \omega \wedge \eta \in \Omega^{k+l}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            Text(
                "dx \u2227 dy = area element in 2D",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "dx \u2227 dx = 0 (anticommutativity)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=formula_box)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Exterior Derivative
    # ------------------------------------------------------------------ #
    def scene5_exterior_derivative(self):
        self.ly.section_divider("3", "Exterior Derivative")
        self.add_subcaption(
            "The exterior derivative d maps k-forms "
            "to k plus one forms. It generalizes "
            "the gradient, curl, and divergence "
            "from vector calculus. The key "
            "property is that d composed with d "
            "equals zero. This means the boundary "
            "of a boundary is always empty.",
            duration=10,
        )

        title = self.ly.title("Exterior Derivative d")

        grad = MathTex(
            r"f \xrightarrow{d} df = \frac{\partial f}{\partial x^i} dx^i",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        curl = MathTex(
            r"a_i dx^i \xrightarrow{d}"
            r"\left(\frac{\partial a_j}{\partial x^i}"
            r"- \frac{\partial a_i}{\partial x^j}\right)"
            r"dx^i \wedge dx^j",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        dd_zero = MathTex(
            r"d \circ d = 0",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        self.ly.safe_place(grad, DOWN, title)
        self.play(Write(grad), run_time=NORMAL)
        self.wait(0.3)

        self.ly.safe_place(curl, DOWN, grad)
        self.play(FadeIn(curl, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        self.ly.safe_place(dd_zero, DOWN, curl)
        self.play(Write(dd_zero), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Closed and Exact Forms
    # ------------------------------------------------------------------ #
    def scene6_closed_exact(self):
        self.add_subcaption(
            "A form is closed if its exterior "
            "derivative is zero. A form is exact "
            "if it is the exterior derivative of "
            "another form. Since d composed with "
            "d is zero, every exact form is "
            "closed. But not every closed form "
            "is exact. The difference measures "
            "the topology of the space.",
            duration=11,
        )
        title = self.ly.title("Closed and Exact Forms")

        items = [
            Text(
                "Closed: d\u03C9 = 0",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Exact: \u03C9 = d\u03B7 for some \u03B7",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Every exact form is closed (dd = 0)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Closed but not exact \u2192 topology matters!",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Integration of Forms
    # ------------------------------------------------------------------ #
    def scene7_integration(self):
        self.ly.section_divider("4", "Integration")
        self.add_subcaption(
            "Differential forms are the objects "
            "that can be integrated over "
            "submanifolds. A k-form integrates "
            "over a k-dimensional manifold. "
            "Change of variables works naturally "
            "because forms transform correctly "
            "under coordinate changes. This leads "
            "to the grand unification: Stokes' "
            "theorem.",
            duration=10,
        )

        title = self.ly.title("Integration of Differential Forms")

        stokes = MathTex(
            r"\int_{\partial \Omega} \omega = \int_{\Omega} d\omega",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(stokes, color=ACCENT)

        self.wait(0.5)

        items = [
            Text(
                "Generalizes: Fundamental theorem, Green's, Stokes', Divergence",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "k-form \u2192 integrate over k-dimensional manifold",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Next video: Stokes on manifolds",
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
            "Differential forms are the dual "
            "objects to vector fields. They "
            "generalize gradients, curls, and "
            "divergences into a single operator: "
            "the exterior derivative d. The "
            "wedge product combines forms. And "
            "Stokes' theorem unifies all integral "
            "theorems. Next: the full Stokes "
            "theorem on manifolds.",
            duration=10,
        )
        title = self.ly.title("Summary")

        items = [
            Text(
                "k-forms: alternating multilinear maps on T_p M",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "d: exterior derivative, dd = 0",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "\u2227: wedge product, anticommutative",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

        self.add_subcaption(
            "That's differential forms. Next time, "
            "we'll prove Stokes' theorem on "
            "manifolds and complete our "
            "differential geometry journey. "
            "Thanks for watching!",
            duration=7,
        )
        play_outro(self, "Stokes on Manifolds", "Differential Geometry")
