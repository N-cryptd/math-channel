"""
Video 23: Polar Coordinates
Covers: polar coordinate system, converting between Cartesian and polar,
graphing polar curves, area in polar coordinates, arc length in polar.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, formula_box, proper narration timing.

Render draft:  manim -ql scripts/pre-university/video-23-polar.py Video23_Polar
Render final:  manim -qh scripts/pre-university/video-23-polar.py Video23_Polar

QUALITY RULES (enforced):
  1. Max 5 visible elements per scene at any time
  2. Use LayoutEngine for ALL text/formula positioning — no raw .shift() or .to_edge() for content
  3. Progressive disclosure: add items one at a time
  4. Consistent animation vocabulary (Write for titles, FadeIn for body)
  5. Narration: ~12 words per 5 seconds
  6. ly.clear() between scenes
  7. setup_background() for dot grid in construct()
  8. SANS for body/titles, MONO only for code/labels
"""

from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video23_Polar(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_polar_system()
        self.scene3_conversion()
        self.scene4_polar_to_cartesian()
        self.scene5_common_curves()
        self.scene6_area()
        self.scene7_arc_length()
        self.scene8_area_example()
        self.scene9_recap()

    # ── Scene 1: Hook — Polar visual ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Instead of x and y, what if we describe a point by its distance "
            "from the origin and its angle? Welcome to polar coordinates.",
            duration=12,
        )
        play_intro(self, "Polar Coordinates", "Calculus II")

        title = self.ly.title("A Different Way to Locate Points")

        # Visual: r line and angle
        origin = Dot(ORIGIN, color=WHITE, radius=0.06)
        self.ly.safe_place(origin, direction=DOWN, anchor=title, buff=1.0)
        self.play(FadeIn(origin), run_time=FAST)

        r_line = Line(ORIGIN, RIGHT * 2.5 + UP * 1.5, color=PRIMARY, stroke_width=3)
        self.play(Create(r_line), run_time=NORMAL)

        angle_arc = Arc(
            radius=1.0, start_angle=0,
            angle=np.arctan(1.5 / 2.5),
            color=ACCENT, stroke_width=2,
        )
        self.play(Create(angle_arc), run_time=FAST)

        point = Dot(RIGHT * 2.5 + UP * 1.5, color=ACCENT, radius=0.08)
        r_label = MathTex(r"r", font_size=HEADING_SIZE, color=PRIMARY)
        r_label.move_to((RIGHT * 2.5 + UP * 1.5) / 2 + UP * 0.3)
        theta_label = MathTex(r"\theta", font_size=HEADING_SIZE, color=ACCENT)
        theta_label.move_to(RIGHT * 0.6 + UP * 0.3)
        self.play(
            FadeIn(point), Write(r_label), Write(theta_label),
            run_time=FAST,
        )

        eq = MathTex(r"(r, \theta)", font_size=HEADING_SIZE, color=WHITE)
        self.ly.safe_place(eq, direction=DOWN, anchor=origin, buff=0.3)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 2: Polar Coordinate System ───────────────────────────
    def scene2_polar_system(self):
        self.ly.section_divider(1, "The Polar System")

        self.add_subcaption(
            "In polar coordinates, r is the distance from the origin "
            "and theta is the angle from the positive x-axis.",
            duration=10,
        )

        title = self.ly.title("Key Concepts")

        items = [
            VGroup(
                MathTex(r"r", font_size=HEADING_SIZE, color=PRIMARY),
                Text(
                    "= distance from origin",
                    font_size=BODY_SIZE, color=WHITE, font=SANS,
                ),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                MathTex(r"\theta", font_size=HEADING_SIZE, color=ACCENT),
                Text(
                    "= angle from positive x-axis (radians)",
                    font_size=BODY_SIZE, color=WHITE, font=SANS,
                ),
            ).arrange(RIGHT, buff=0.3),
            Text(
                "r can be NEGATIVE (go opposite direction!)",
                font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
            ),
            Text(
                "(r, theta) and (r, theta + 2 pi k) are the same point",
                font_size=BODY_SIZE, color=DIM, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 3: Conversion — Polar to Cartesian ────────────────────
    def scene3_conversion(self):
        self.ly.section_divider(2, "Polar to Cartesian")

        self.add_subcaption(
            "Converting between Cartesian and polar uses basic trigonometry.",
            duration=8,
        )

        title = self.ly.title("Polar to Cartesian")

        # Formula box
        p2c_tex = MathTex(
            r"x = r \cos \theta, \quad y = r \sin \theta",
            font_size=HEADING_SIZE, color=WHITE,
        )
        p2c_boxed = self.ly.formula_box(p2c_tex)
        self.ly.safe_place(p2c_boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(p2c_boxed), run_time=SLOW)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 4: Conversion — Cartesian to Polar ──────────────────
    def scene4_polar_to_cartesian(self):
        self.ly.section_divider(3, "Cartesian to Polar")

        self.add_subcaption(
            "To go from Cartesian to polar, use the Pythagorean theorem and arctangent.",
            duration=8,
        )

        title = self.ly.title("Cartesian to Polar")

        r_tex = MathTex(
            r"r = \sqrt{x^2 + y^2}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(r_tex, direction=DOWN, anchor=title)
        self.play(Write(r_tex), run_time=NORMAL)
        self.wait(0.5)

        theta_tex = MathTex(
            r"\theta = \tan^{-1}\!\left(\frac{y}{x}\right)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(theta_tex, direction=DOWN, anchor=r_tex)
        self.play(Write(theta_tex), run_time=NORMAL)
        self.wait(0.5)

        shortcut = MathTex(
            r"x^2 + y^2 = r^2",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(shortcut, direction=DOWN, anchor=theta_tex)
        self.play(Write(shortcut), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 5: Common Polar Curves ──────────────────────────────
    def scene5_common_curves(self):
        self.ly.section_divider(4, "Common Polar Curves")

        self.add_subcaption(
            "Polar equations produce beautiful symmetric curves "
            "like circles, cardioids, roses, and limacons.",
            duration=10,
        )

        title = self.ly.title("Shapes to Know")

        items = [
            VGroup(
                Text("Circle:", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD),
                MathTex(r"r = a", font_size=BODY_SIZE, color=WHITE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("Cardioid:", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD),
                MathTex(r"r = a(1 + \cos\theta)", font_size=BODY_SIZE, color=WHITE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("Rose:", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD),
                MathTex(r"r = a\cos(n\theta)", font_size=BODY_SIZE, color=WHITE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("Limacon:", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD),
                MathTex(r"r = a + b\cos\theta", font_size=BODY_SIZE, color=WHITE),
            ).arrange(RIGHT, buff=0.3),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)

        tip = Text(
            "Tip: Test theta = 0, pi/2, pi to find symmetry quickly.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        # Place below last visible item
        last_item = None
        for m in reversed(self.mobjects):
            if m not in [self._bg_dots, self._bg_gradient] and hasattr(m, 'get_bottom'):
                last_item = m
                break
        if last_item is not None:
            self.ly.safe_place(tip, direction=DOWN, anchor=last_item)
        self.play(FadeIn(tip, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 6: Area in Polar ────────────────────────────────────
    def scene6_area(self):
        self.ly.section_divider(5, "Area in Polar Coordinates")

        self.add_subcaption(
            "The area formula in polar coordinates is remarkably simple. "
            "It is one half r squared, integrated over the angle.",
            duration=10,
        )

        title = self.ly.title("Area Formula")

        # Formula box
        area_tex = MathTex(
            r"A = \frac{1}{2}\int_{\alpha}^{\beta} r^2\, d\theta",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        area_boxed = self.ly.formula_box(area_tex)
        self.ly.safe_place(area_boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(area_boxed), run_time=SLOW)
        self.wait(1.0)

        wedge = MathTex(
            r"dA = \frac{1}{2}r^2\, d\theta",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(wedge, direction=DOWN, anchor=area_boxed)
        self.play(Write(wedge), run_time=FAST)
        self.wait(0.3)

        note = Text(
            "Think of a thin wedge — like a pizza slice!",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=wedge)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 7: Arc Length in Polar ──────────────────────────────
    def scene7_arc_length(self):
        self.ly.section_divider(6, "Arc Length")

        self.add_subcaption(
            "Arc length in polar coordinates uses r and its derivative with respect to theta.",
            duration=8,
        )

        title = self.ly.title("Arc Length Formula")

        arc_tex = MathTex(
            r"L = \int_{\alpha}^{\beta} "
            r"\sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}"
            r"\, d\theta",
            font_size=HEADING_SIZE, color=WHITE,
        )
        arc_boxed = self.ly.formula_box(arc_tex)
        self.ly.safe_place(arc_boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(arc_boxed), run_time=SLOW)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 8: Area Example ──────────────────────────────────────
    def scene8_area_example(self):
        self.ly.section_divider(7, "Area Example")

        self.add_subcaption(
            "Let us find the area enclosed by a cardioid "
            "using the polar area formula.",
            duration=10,
        )

        title = self.ly.title("Area of a Cardioid")

        given = MathTex(
            r"r = 1 + \cos\theta",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(given, direction=DOWN, anchor=title)
        self.play(Write(given), run_time=NORMAL)
        self.wait(0.5)

        integral = MathTex(
            r"A = \frac{1}{2}\int_0^{2\pi} (1+\cos\theta)^2\, d\theta",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(integral, direction=DOWN, anchor=given)
        self.play(Write(integral), run_time=NORMAL)
        self.wait(0.5)

        expand = MathTex(
            r"= \frac{1}{2}\int_0^{2\pi} "
            r"\!\left(1 + 2\cos\theta + \frac{1+\cos 2\theta}{2}\right)"
            r" d\theta",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(expand, direction=DOWN, anchor=integral)
        self.play(Write(expand), run_time=NORMAL)
        self.wait(0.5)

        result_tex = MathTex(
            r"= \frac{3\pi}{2}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        result_boxed = self.ly.formula_box(result_tex)
        self.ly.safe_place(result_boxed, direction=DOWN, anchor=expand, buff=0.4)
        self.play(Write(result_boxed), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 9: Recap ────────────────────────────────────────────
    def scene9_recap(self):
        self.ly.section_divider(8, "Summary")

        self.add_subcaption(
            "Polar coordinates use r and theta instead of x and y. "
            "They excel at describing circular and spiral shapes.",
            duration=10,
        )

        title = self.ly.title("What We Learned")

        items = [
            Text(
                "Polar: (r, theta) = distance and angle",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            MathTex(
                r"x = r\cos\theta, \quad y = r\sin\theta",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            Text(
                "Common curves: cardioid, rose, limacon, spiral",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            MathTex(
                r"A = \tfrac{1}{2}\int r^2\, d\theta",
                font_size=BODY_SIZE, color=ACCENT,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)

        play_outro(self, "Calculus II Review", "Calculus II")
