"""
Video 194: Curves in R^n -- Differential Geometry Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video194_CurvesRn

Topics: Parametrized curves in R^n, tangent vectors and velocity,
        speed, regular curves, reparametrization.

Prerequisites: Calculus III (Videos 41-54), Linear Algebra (Videos 25-40).

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


class Video194_CurvesRn(Scene):
    """Curves in R^n -- Differential Geometry Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_parametrized_curves()
        self.scene3_tangent_vectors()
        self.scene4_regular_curves()
        self.scene5_reparametrization()
        self.scene6_examples_summary()
        self.scene7_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Welcome to our new playlist on Differential Geometry. "
            "We begin with the most fundamental object: a curve. "
            "From roller coasters to planetary orbits, from DNA "
            "helixes to particle physics, curves are everywhere. "
            "But what exactly is a curve, mathematically?",
            duration=9,
        )
        play_intro(self, "Curves in R^n", "Differential Geometry")

        title = self.ly.title("Why Study Curves?")

        items = [
            Text("Physics: particle trajectories, orbits", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Engineering: roller coasters, robotics paths", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Biology: DNA double helix, protein folding", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Parametrized Curves
    # ------------------------------------------------------------------ #
    def scene2_parametrized_curves(self):
        self.ly.section_divider("1", "Parametrized Curves")
        self.add_subcaption(
            "A curve is not just a set of points in space. It is "
            "a smooth mapping from an interval to R^n. The map "
            "itself carries information about direction and "
            "speed, which the image alone cannot capture.",
            duration=8,
        )
        title = self.ly.title("Definition: Parametrized Curve")

        defn = MathTex(
            r"\gamma", r": [a, b] \to \mathbb{R}^n",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.formula_box(defn, PRIMARY)
        self.ly.safe_place(defn, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)

        components = MathTex(
            r"\gamma(t) = (x_1(t),\, x_2(t),\, \ldots,\, x_n(t))",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(components, direction=DOWN, anchor=defn, buff=0.4)
        self.play(Write(components), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

        # Circle example (simple, no TracedPath)
        self.add_subcaption(
            "For example, the unit circle is the image of this "
            "parametrization. As t goes from zero to two pi, "
            "the point traces the entire circle.",
            duration=6,
        )
        title2 = self.ly.title("Example: Unit Circle")

        circle_formula = MathTex(
            r"\gamma(t) = (\cos t,\, \sin t), \quad t \in [0, 2\pi]",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(circle_formula, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(circle_formula), run_time=FAST)

        axes = Axes(
            x_range=[-1.8, 1.8, 1], y_range=[-1.8, 1.8, 1],
            x_length=4, y_length=4,
            axis_config={"color": DIM, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        self.play(Create(axes), run_time=FAST)

        circle = Circle(radius=1.5, color=PRIMARY, stroke_width=2)
        circle.move_to(axes.get_center())
        dot = Dot(color=ACCENT, radius=0.06).move_to(
            axes.get_center() + RIGHT * 1.5,
        )

        self.add(dot)
        self.play(
            Create(circle), run_time=2.5, rate_func=linear,
        )

        self.wait(1.0)
        self.ly.clear()

        # Helix example (2D projection)
        self.add_subcaption(
            "In three dimensions, a helix spirals upward. "
            "The x and y coordinates trace a circle while "
            "z increases linearly. This is a fundamental "
            "example in differential geometry and physics.",
            duration=8,
        )
        title3 = self.ly.title("Example: Helix in 3D")

        helix_formula = MathTex(
            r"\gamma(t) = (\cos t,\, \sin t,\, t), \quad t \in [0, 4\pi]",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(helix_formula, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(helix_formula), run_time=FAST)

        # Draw helix as 2D parametric curve (x=cos, y=sin+0.25*t for oblique view)
        helix_2d = ParametricFunction(
            lambda t: np.array([
                np.cos(t),
                np.sin(t) + t * 0.18,
                0,
            ]),
            t_range=[0, 4 * PI],
            color=PRIMARY,
            stroke_width=2.5,
        )
        helix_2d.scale(0.8)
        self.ly.center_in_content(helix_2d)
        self.play(Create(helix_2d), run_time=3.0, rate_func=linear)

        # Label z-axis direction
        z_label = Text("z direction", font_size=LABEL_SIZE, color=DIM, font=SANS)
        self.ly.safe_place(z_label, direction=DOWN, anchor=helix_2d, buff=0.3)
        self.play(FadeIn(z_label), run_time=FAST)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Tangent Vectors
    # ------------------------------------------------------------------ #
    def scene3_tangent_vectors(self):
        self.ly.section_divider("2", "Tangent Vectors")
        self.add_subcaption(
            "The derivative of a curve gives us the tangent "
            "vector, also called the velocity. Its magnitude is "
            "the speed. The tangent vector always points in the "
            "direction the curve is moving.",
            duration=8,
        )
        title = self.ly.title("Velocity and Speed")

        vel_formula = MathTex(
            r"\gamma'(t) = \left(\frac{dx_1}{dt},\, \frac{dx_2}{dt},\, \ldots,\, \frac{dx_n}{dt}\right)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.formula_box(vel_formula, ACCENT)
        self.ly.safe_place(vel_formula, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(vel_formula), run_time=NORMAL)

        speed_formula = MathTex(
            r"v(t) = |\gamma'(t)| = \text{speed at parameter } t",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(speed_formula, direction=DOWN, anchor=vel_formula, buff=0.4)
        self.play(Write(speed_formula), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Visual: tangent on helix (2D projection)
        self.add_subcaption(
            "Here we show the tangent vector at several points "
            "along the helix. Notice how it always touches "
            "the curve and points in the direction of motion. "
            "This is the geometric meaning of the derivative.",
            duration=8,
        )
        title2 = self.ly.title("Tangent Vectors on the Helix")

        helix_2d = ParametricFunction(
            lambda t: np.array([
                np.cos(t),
                np.sin(t) + t * 0.18,
                0,
            ]),
            t_range=[0, 4 * PI],
            color=PRIMARY,
            stroke_width=2,
        )
        helix_2d.scale(0.8)
        self.ly.center_in_content(helix_2d)
        self.play(Create(helix_2d), run_time=2.5, rate_func=linear)

        # Draw tangent arrows at several points
        for t_val in [PI / 2, PI, 3 * PI / 2, 2 * PI]:
            scale_f = 0.8
            pt = np.array([scale_f * np.cos(t_val),
                           scale_f * (np.sin(t_val) + t_val * 0.18), 0])
            # Tangent direction: (-sin(t), cos(t) + 0.18*t, 0) but simpler
            tangent_end = pt + np.array([
                scale_f * 0.6 * (-np.sin(t_val)),
                scale_f * 0.6 * (np.cos(t_val) + 0.18),
                0,
            ])
            arrow = Arrow(
                pt, tangent_end, color=ACCENT, buff=0, stroke_width=2,
                max_tip_length_to_length_ratio=0.2,
            )
            self.play(Create(arrow), run_time=0.5)

        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Regular Curves
    # ------------------------------------------------------------------ #
    def scene4_regular_curves(self):
        self.ly.section_divider("3", "Regular Curves")
        self.add_subcaption(
            "A curve is called regular if its derivative is never "
            "zero. Regular curves have a well-defined tangent "
            "direction at every point. When the derivative "
            "vanishes, strange things can happen, like cusps.",
            duration=8,
        )
        title = self.ly.title("Regular Curves")

        defn = MathTex(
            r"\gamma \text{ is regular } \iff \gamma'(t) \neq 0 \text{ for all } t",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.formula_box(defn, PRIMARY)
        self.ly.safe_place(defn, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)

        note = Text(
            "Regular = well-defined tangent line everywhere",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=defn, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

        # Cusp example
        self.add_subcaption(
            "Here is a curve that fails to be regular at t "
            "equals zero. The parametrization gamma of t "
            "equals t cubed comma t squared has a cusp at "
            "the origin, where the tangent direction changes "
            "abruptly.",
            duration=8,
        )
        title2 = self.ly.title("Non-Regular Example: Cusp")

        cusp_label = MathTex(
            r"\gamma(t) = (t^3,\, t^2)",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.formula_box(cusp_label, RED)
        self.ly.safe_place(cusp_label, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(cusp_label), run_time=FAST)

        axes2 = Axes(
            x_range=[-1.5, 1.5, 0.5], y_range=[-0.3, 1.5, 0.5],
            x_length=5, y_length=3.5,
            axis_config={"color": DIM, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes2)
        self.play(Create(axes2), run_time=FAST)

        cusp = ParametricFunction(
            lambda t: axes2.c2p(t ** 3, t ** 2),
            t_range=[-1.2, 1.2],
            color=RED,
            stroke_width=2.5,
        )
        self.play(Create(cusp), run_time=2.5, rate_func=linear)

        self.wait(1.0)
        self.ly.clear()

        # Cusp detail
        self.add_subcaption(
            "At t equals zero the derivative vanishes, creating "
            "a cusp. The curve is not regular here because the "
            "tangent direction changes abruptly.",
            duration=6,
        )
        title3 = self.ly.title("Cusp at t=0")

        axes3 = Axes(
            x_range=[-1.5, 1.5, 0.5], y_range=[-0.3, 1.5, 0.5],
            x_length=5, y_length=3.5,
            axis_config={"color": DIM, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes3)
        self.play(Create(axes3), run_time=FAST)

        cusp2 = ParametricFunction(
            lambda t: axes3.c2p(t ** 3, t ** 2),
            t_range=[-1.2, 1.2],
            color=RED,
            stroke_width=2.5,
        )
        self.play(Create(cusp2), run_time=2.0, rate_func=linear)

        cusp_dot = Dot(axes3.c2p(0, 0), color=ACCENT, radius=0.06)
        self.play(FadeIn(cusp_dot), run_time=FAST)

        cusp_note = Text(
            "gamma prime of zero equals zero!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(cusp_note, direction=DOWN, anchor=cusp_dot, buff=0.3)
        self.play(FadeIn(cusp_note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Reparametrization
    # ------------------------------------------------------------------ #
    def scene5_reparametrization(self):
        self.ly.section_divider("4", "Reparametrization")
        self.add_subcaption(
            "We can reparametrize a curve by composing it with "
            "a smooth, increasing function. This changes the speed "
            "of traversal but not the geometry. The arc-length "
            "parametrization is the natural choice where speed "
            "equals one everywhere.",
            duration=9,
        )
        title = self.ly.title("Reparametrization")

        formula = MathTex(
            r"\alpha(s) = \gamma(\phi(s)), \quad \phi'(s) > 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.formula_box(formula, SECONDARY)
        self.ly.safe_place(formula, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(formula), run_time=NORMAL)

        items = [
            Text("Same geometric curve (same image)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Different speed of traversal", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Arc-length param: |alpha prime| = 1", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=formula)

        self.wait(1.0)
        self.ly.clear()

        # Visual: static comparison
        self.add_subcaption(
            "Both dots trace the same circle, but the green one "
            "moves at constant speed while the orange one moves "
            "at variable speed. The curve is identical, but the "
            "parametrization tells us how fast we move along it.",
            duration=8,
        )
        title2 = self.ly.title("Same Curve, Different Speeds")

        items = [
            Text("Green: constant speed (arc-length param)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Orange: variable speed (arbitrary param)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Image is the same circle either way", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)

        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Examples Summary
    # ------------------------------------------------------------------ #
    def scene6_examples_summary(self):
        self.ly.section_divider("5", "Examples Summary")
        self.add_subcaption(
            "Let us summarize with key examples. On the left, "
            "regular curves with well-defined tangents everywhere. "
            "On the right, special cases that need extra care.",
            duration=7,
        )
        title = self.ly.title("Examples at a Glance")

        left_items = [
            Text("Line: gamma(t) = a + tv", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Circle: gamma(t) = (cos t, sin t)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Helix: gamma(t) = (cos t, sin t, t)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        right_items = [
            Text("Cusp: gamma(t) = (t^3, t^2)", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Self-intersection: figure eight", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Singular: gamma'(t) = 0", font_size=BODY_SIZE, color=RED, font=SANS),
        ]

        left_col_header = Text(
            "Regular Curves", font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        right_col_header = Text(
            "Special Cases", font_size=HEADING_SIZE, color=RED, font=SANS,
        )

        left_col, right_col = self.ly.two_columns(
            [left_col_header] + left_items,
            [right_col_header] + right_items,
            start_from=title,
        )
        self.play(
            FadeIn(left_col, shift=LEFT * 0.15),
            FadeIn(right_col, shift=RIGHT * 0.15),
            run_time=NORMAL,
        )

        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Outro
    # ------------------------------------------------------------------ #
    def scene7_outro(self):
        self.add_subcaption(
            "In this video, we defined parametrized curves "
            "in R^n, tangent vectors, regularity, and "
            "reparametrization. Next time, we measure how "
            "long a curve is and introduce curvature, the "
            "measure of how much a curve bends. See you there!",
            duration=8,
        )
        play_outro(self, "Arc Length & Curvature", "Differential Geometry")
