"""
Video 195: Arc Length and Curvature -- Differential Geometry Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video195_ArcLengthCurvature

Topics: Arc length formula, arc-length parametrization,
        curvature definition, curvature of circle and helix.

Prerequisites: Video 194 (Curves in R^n), Calculus III, Linear Algebra.

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


class Video195_ArcLengthCurvature(Scene):
    """Arc Length and Curvature -- Differential Geometry Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_arc_length_formula()
        self.scene4_arclength_parametrization()
        self.scene5_curvature_definition()
        self.scene6_curvature_circle()
        self.scene7_curvature_helix()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Imagine two roads connecting the same two towns. "
            "One goes straight across the valley. The other "
            "winds through the hills. Both connect A to B, "
            "but the winding road is longer. How do we "
            "measure the length of a curve?",
            duration=9,
        )
        play_intro(self, "Arc Length & Curvature", "Differential Geometry")

        title = self.ly.title("The Road Question")

        # Straight road
        road_a_label = Text(
            "Road A: straight",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        road_b_label = Text(
            "Road B: winding",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        question = Text(
            "Which is longer? How much longer?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.progressive_reveal(
            [road_a_label, road_b_label, question],
            start_from=title,
        )

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Intro + Section Divider
    # ------------------------------------------------------------------ #
    def scene2_intro(self):
        self.ly.section_divider("1", "Arc Length")
        self.add_subcaption(
            "Today we answer this question rigorously using "
            "integration. Then we go further and develop "
            "curvature: the precise measure of how much "
            "a curve bends at any point.",
            duration=6,
        )
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Arc Length Formula
    # ------------------------------------------------------------------ #
    def scene3_arc_length_formula(self):
        self.add_subcaption(
            "To find the length of a curve, we use the "
            "same idea from calculus. Chop the curve into "
            "tiny segments. Each segment is approximately "
            "straight, with length equal to the speed "
            "times the time interval.",
            duration=8,
        )
        title = self.ly.title("Arc Length Formula")

        integral = MathTex(
            r"s = \int_a^b |\gamma'(t)| \, dt",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(integral, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(integral), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Interpretation
        self.add_subcaption(
            "The integrand is the speed, the magnitude of "
            "the tangent vector. Integrating speed over "
            "time gives total distance traveled. This "
            "depends only on the image of the curve, not "
            "the parametrization.",
            duration=8,
        )
        title2 = self.ly.title("Interpretation")

        items = [
            Text(
                "|gamma'(t)| = speed at parameter t",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Integral of speed = total distance",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Invariant under reparametrization",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title2)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Arc-Length Parametrization
    # ------------------------------------------------------------------ #
    def scene4_arclength_parametrization(self):
        self.add_subcaption(
            "Given a regular curve, we define the arc "
            "length function s of t as the integral from "
            "a to t of speed dt. This measures how far "
            "we have traveled along the curve.",
            duration=8,
        )
        title = self.ly.title("Arc-Length Function")

        s_func = MathTex(
            r"s(t) = \int_a^t |\gamma'(u)| \, du",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(s_func, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(s_func), run_time=NORMAL)

        note = Text(
            "s(t) = distance traveled from starting point",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=s_func, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

        # Arc-length parametrization definition
        self.add_subcaption(
            "Since gamma is regular, s of t is strictly "
            "increasing and has an inverse. The arc-length "
            "parametrization is alpha of s equals gamma "
            "composed with t of s. The magic: speed is "
            "always exactly one.",
            duration=9,
        )
        title2 = self.ly.title("Arc-Length Parametrization")

        alpha_def = MathTex(
            r"\alpha(s) = \gamma(t(s)), \quad t(s) = s^{-1}(t)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(alpha_def, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(alpha_def), run_time=NORMAL)

        speed_one = MathTex(
            r"|\alpha'(s)| = 1 \text{ for all } s",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(speed_one, direction=DOWN, anchor=alpha_def, buff=0.4)
        self.play(Write(speed_one), run_time=NORMAL)

        key = Text(
            "s = distance traveled along the curve",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=speed_one, buff=0.4)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Curvature Definition
    # ------------------------------------------------------------------ #
    def scene5_curvature_definition(self):
        self.ly.section_divider("2", "Curvature")
        self.ly.clear()

        self.add_subcaption(
            "Now we measure how much a curve bends. "
            "A straight line has zero curvature. A "
            "circle has constant curvature, and a "
            "tighter circle bends more. Formally, "
            "curvature is defined using the arc-length "
            "parametrization.",
            duration=9,
        )
        title = self.ly.title("Curvature")

        kappa_def = MathTex(
            r"\kappa(s) = |\alpha''(s)|",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(kappa_def, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(kappa_def), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Geometric intuition
        self.add_subcaption(
            "The second derivative of the arc-length "
            "parametrization measures how fast the unit "
            "tangent vector rotates. Since the tangent "
            "has unit length, the second derivative is "
            "perpendicular to the curve, pointing toward "
            "the center of bending.",
            duration=9,
        )
        title2 = self.ly.title("Geometric Meaning")

        items = [
            Text(
                "Straight line: kappa = 0 everywhere",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Circle: constant kappa, same at all points",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "alpha'' is perpendicular to the curve",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title2)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Curvature of a Circle
    # ------------------------------------------------------------------ #
    def scene6_curvature_circle(self):
        self.add_subcaption(
            "Let us compute the curvature of a circle. "
            "The unit circle gamma of t equals cosine t, "
            "sine t is already arc-length parametrized "
            "since the speed is exactly one.",
            duration=8,
        )
        title = self.ly.title("Curvature of a Circle")

        circle_eq = MathTex(
            r"\gamma(t) = (\cos t,\, \sin t)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(circle_eq, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(circle_eq), run_time=NORMAL)

        speed_note = Text(
            "Speed: |gamma'(t)| = 1  (arc-length param!)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(speed_note, direction=DOWN, anchor=circle_eq, buff=0.4)
        self.play(FadeIn(speed_note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Computation
        self.add_subcaption(
            "The second derivative is negative gamma, "
            "so its magnitude is one. The curvature "
            "of the unit circle is exactly one.",
            duration=6,
        )
        title2 = self.ly.title("Unit Circle: kappa = 1")

        deriv1 = MathTex(
            r"\gamma''(t) = (-\cos t,\, -\sin t) = -\gamma(t)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(deriv1, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(deriv1), run_time=NORMAL)

        kappa1 = MathTex(
            r"\kappa = |\gamma''(t)| = 1",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(kappa1, direction=DOWN, anchor=deriv1, buff=0.4)
        self.play(Write(kappa1), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # General radius
        self.add_subcaption(
            "For a circle of radius R, after arc-length "
            "reparametrization, the curvature is one over "
            "R. A larger circle bends less. This matches "
            "our geometric intuition perfectly.",
            duration=8,
        )
        title3 = self.ly.title("General Circle")

        general = MathTex(
            r"\kappa = \frac{1}{R}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(general, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(general), run_time=NORMAL)

        interp = Text(
            "Larger radius = smaller curvature = less bending",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(interp, direction=DOWN, anchor=general, buff=0.4)
        self.play(FadeIn(interp, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Curvature of a Helix
    # ------------------------------------------------------------------ #
    def scene7_curvature_helix(self):
        self.add_subcaption(
            "Now the helix, gamma of t equals cosine t, "
            "sine t, t. Its speed is root 2 everywhere. "
            "We rescale to get the arc-length "
            "parametrization.",
            duration=8,
        )
        title = self.ly.title("Curvature of a Helix")

        helix_eq = MathTex(
            r"\gamma(t) = (\cos t,\, \sin t,\, t)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(helix_eq, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(helix_eq), run_time=NORMAL)

        speed_h = MathTex(
            r"|\gamma'(t)| = \sqrt{2}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(speed_h, direction=DOWN, anchor=helix_eq, buff=0.4)
        self.play(Write(speed_h), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Computation result
        self.add_subcaption(
            "After arc-length reparametrization with s "
            "divided by root 2, the second derivative "
            "gives curvature of exactly one half. The "
            "helix has constant curvature, less than "
            "the unit circle.",
            duration=9,
        )
        title2 = self.ly.title("Helix: kappa = 1/2")

        alpha_helix = MathTex(
            r"\alpha(s) = \left(\cos\!\frac{s}{\sqrt{2}},\;"
            r"\sin\!\frac{s}{\sqrt{2}},\;"
            r"\frac{s}{\sqrt{2}}\right)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(alpha_helix, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(alpha_helix), run_time=NORMAL)

        kappa_helix = MathTex(
            r"\kappa = |\alpha''(s)| = \frac{1}{2}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(kappa_helix, direction=DOWN, anchor=alpha_helix, buff=0.4)
        self.play(Write(kappa_helix), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Interpretation
        self.add_subcaption(
            "The helix curvature is less than the unit "
            "circle because the helix also advances "
            "upward. Not all the turning goes into "
            "bending in the plane. Some goes into the "
            "third dimension.",
            duration=8,
        )
        title3 = self.ly.title("Interpretation")

        items = [
            Text(
                "Helix: kappa = 1/2 < 1 (unit circle)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Constant curvature, same at every point",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Some turning goes upward, not just bending",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title3)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary_outro(self):
        self.add_subcaption(
            "Today we learned two fundamental quantities "
            "associated with curves. The arc length "
            "measures how long a curve is. The curvature "
            "measures how much it bends. Next time we "
            "build the Frenet-Serret frame, the natural "
            "moving coordinate system for curves.",
            duration=9,
        )
        title = self.ly.title("Summary")

        items = [
            Text(
                "1. Arc length: integral of |gamma'| dt",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "2. Arc-length param: |alpha'| = 1",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3. Curvature: kappa = |alpha''|",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "4. Circle: kappa = 1/R",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "5. Helix: kappa = 1/2 (constant)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.5)
        self.ly.clear()

        play_outro(self, "Frenet-Serret Frame", "Differential Geometry")
