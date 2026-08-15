"""
Video 203: Manifolds Introduction -- Differential Geometry Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video203_ManifoldsIntro

Topics: Manifolds, topological manifolds, coordinate charts, atlases,
        transition maps, smooth manifolds, examples (circle, sphere,
        torus, projective spaces), motivation from physics.

Prerequisites: Video 200 (Gaussian Curvature), Video 202 (Gauss-Bonnet),
               Multivariable Calculus, Linear Algebra.

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


class Video203_ManifoldsIntro(Scene):
    """Manifolds Introduction -- Differential Geometry Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_charts_atlases()
        self.scene4_examples()
        self.scene5_smooth_manifolds()
        self.scene6_motivation()
        self.scene7_dimensions()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook — Beyond Surfaces
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Everything we've studied so far has been "
            "on surfaces in R three. Curvature, "
            "geodesics, Gauss-Bonnet. But what about "
            "spaces that don't fit in R three? "
            "Spacetime, configuration spaces, abstract "
            "surfaces? The answer is manifolds. "
            "Spaces that are locally flat but "
            "globally curved.",
            duration=11,
        )
        play_intro(self, "Manifolds", "Differential Geometry")

        title = self.ly.title("Beyond Surfaces")

        items = [
            Text(
                "Surfaces in R\u00B3 \u2192 abstract spaces",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Locally flat, globally curved",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "The foundation of modern geometry and physics",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Definition — What is a Manifold?
    # ------------------------------------------------------------------ #
    def scene2_definition(self):
        self.ly.section_divider("1", "Definition")
        self.add_subcaption(
            "A topological manifold of dimension n "
            "is a topological space that is Hausdorff, "
            "second countable, and locally Euclidean "
            "of dimension n. Locally Euclidean means "
            "every point has a neighborhood that "
            "looks like a piece of R n.",
            duration=9,
        )

        title = self.ly.title("Topological Manifold")

        items = [
            Text(
                "A topological space M of dimension n",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "1. Hausdorff: distinct points have disjoint neighborhoods",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "2. Second-countable: countable base of open sets",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3. Locally Euclidean: each point \u2208 open set \u2248 R\u207F",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Coordinate Charts and Atlases
    # ------------------------------------------------------------------ #
    def scene3_charts_atlases(self):
        self.add_subcaption(
            "A coordinate chart is a pair U phi "
            "where U is an open set in the manifold "
            "and phi maps U homeomorphically to "
            "R n. An atlas is a collection of "
            "charts that covers the entire "
            "manifold. Where charts overlap, "
            "we get transition maps between "
            "copies of R n.",
            duration=10,
        )
        title = self.ly.title("Charts and Atlases")

        chart_def = MathTex(
            r"\text{Chart: } (U, \varphi), \quad"
            r"\varphi : U \to \mathbb{R}^n",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(chart_def, DOWN, title)
        self.play(Write(chart_def), run_time=NORMAL)
        self.wait(0.5)

        items = [
            Text(
                "Atlas: collection of charts covering M",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            MathTex(
                r"\text{Transition: } \varphi_j \circ \varphi_i^{-1} : \mathbb{R}^n \to \mathbb{R}^n",
                font_size=BODY_SIZE, color=SECONDARY,
            ),
            Text(
                "Overlaps give us coordinate changes",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=chart_def)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Examples
    # ------------------------------------------------------------------ #
    def scene4_examples(self):
        self.add_subcaption(
            "Let's see some examples. The circle S "
            "one is a one-dimensional manifold. "
            "It needs at least two charts to cover "
            "it, since a single chart would miss "
            "at least one point. The sphere S two "
            "needs at least two charts via "
            "stereographic projection.",
            duration=10,
        )
        title = self.ly.title("Classic Examples")

        items = [
            Text(
                "S\u00B9 (circle): 1D, min 2 charts",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "S\u00B2 (sphere): 2D, stereographic projection (2 charts)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "T\u00B2 (torus): 2D, flat square representation (4 charts)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "RP\u00B2 (projective plane): 2D, needs \u22653 charts",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Smooth Manifolds
    # ------------------------------------------------------------------ #
    def scene5_smooth_manifolds(self):
        self.ly.section_divider("2", "Smooth Structure")
        self.add_subcaption(
            "A smooth manifold is a topological "
            "manifold whose transition maps are "
            "infinitely differentiable. This means "
            "coordinate changes are smooth, so "
            "calculus makes sense on the manifold. "
            "Not every topological manifold admits "
            "a smooth structure, but most of the "
            "spaces we care about do.",
            duration=10,
        )

        title = self.ly.title("Smooth Manifolds")

        items = [
            Text(
                "Topological manifold + smooth transition maps",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            MathTex(
                r"\varphi_j \circ \varphi_i^{-1} \in C^{\infty}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            Text(
                "Calculus becomes well-defined on M",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Required for: geodesics, curvature, integration",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Why Manifolds?
    # ------------------------------------------------------------------ #
    def scene6_motivation(self):
        self.add_subcaption(
            "Why do we need manifolds? First, "
            "general relativity models spacetime "
            "as a four-dimensional Lorentzian "
            "manifold. Second, configuration "
            "spaces in mechanics are manifolds. "
            "Third, the Gauss-Bonnet theorem "
            "generalizes to manifolds via the "
            "Chern-Gauss-Bonnet theorem.",
            duration=10,
        )
        title = self.ly.title("Why Manifolds Matter")

        items = [
            Text(
                "Physics: spacetime is a 4D manifold (GR)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Mechanics: configuration spaces are manifolds",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Math: abstract surfaces, Grassmannians",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Gauss-Bonnet \u2192 Chern-Gauss-Bonnet on manifolds",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Dimensions and Non-Examples
    # ------------------------------------------------------------------ #
    def scene7_dimensions(self):
        self.add_subcaption(
            "Manifolds exist in every dimension. "
            "One-dimensional: lines and circles. "
            "Two-dimensional: surfaces like spheres "
            "and tori. The figure eight is NOT a "
            "manifold because the crossing point "
            "has no neighborhood homeomorphic to R "
            "one. Four-dimensional: spacetime.",
            duration=10,
        )
        title = self.ly.title("Dimensions")

        items = [
            Text(
                "1D: line, circle (S\u00B9)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "2D: sphere (S\u00B2), torus (T\u00B2), Klein bottle",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "4D: spacetime (Lorentzian manifold)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "NOT a manifold: figure-eight (crossing point)",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary_outro(self):
        self.add_subcaption(
            "To summarize, a manifold is a space "
            "that is locally Euclidean but may "
            "be globally curved. Charts provide "
            "local coordinates, atlases cover "
            "the whole space, and smooth "
            "transition maps let us do calculus. "
            "Next, we'll study tangent spaces "
            "and vector fields on manifolds.",
            duration=10,
        )
        title = self.ly.title("Summary")

        items = [
            Text(
                "Locally Euclidean, globally curved",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Charts: local coordinates \u2192 R\u207F",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Smooth: C^\u221E transition maps",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

        self.add_subcaption(
            "That's manifolds. Spaces that look "
            "flat locally but can be curved "
            "globally. Next time, we'll study "
            "tangent spaces and vector fields. "
            "Thanks for watching!",
            duration=7,
        )
        play_outro(self, "Tangent Spaces & Vector Fields", "Differential Geometry")
