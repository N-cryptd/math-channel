"""
Video 22: Parametric Equations
Covers: parametric curves, eliminating the parameter, calculus of parametric curves,
arc length, area under a parametric curve.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, formula_box, proper narration timing.

Render draft:  manim -ql scripts/pre-university/video-22-parametric.py Video22_Parametric
Render final:  manim -qh scripts/pre-university/video-22-parametric.py Video22_Parametric

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


class Video22_Parametric(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_advantages()
        self.scene4_eliminating_parameter()
        self.scene5_derivatives()
        self.scene6_arc_length()
        self.scene7_examples()
        self.scene8_recap()

    # ── Scene 1: Hook — Circle animation ──────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "What if both x and y depend on a third variable t? "
            "This gives us parametric equations — a powerful way to describe curves.",
            duration=12,
        )
        play_intro(self, "Parametric Equations", "Calculus II")

        title = self.ly.title("Describing a Circle")

        # Parametric equations for a circle
        eq_x = MathTex(
            r"x(t) = \cos t",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(eq_x, direction=DOWN, anchor=title)
        self.play(Write(eq_x), run_time=NORMAL)
        self.wait(0.3)

        eq_y = MathTex(
            r"y(t) = \sin t",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(eq_y, direction=DOWN, anchor=eq_x)
        self.play(Write(eq_y), run_time=NORMAL)
        self.wait(0.3)

        domain = Text(
            "0 <= t <= 2 pi",
            font_size=BODY_SIZE, color=DIM, font=MONO,
        )
        self.ly.safe_place(domain, direction=DOWN, anchor=eq_y)
        self.play(FadeIn(domain, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Draw the circle
        circle = Circle(radius=1.5, color=PRIMARY)
        self.ly.safe_place(circle, direction=RIGHT, anchor=eq_x, buff=2.5)
        self.play(Create(circle), run_time=NORMAL)

        # Animate the dot
        dot = Dot(circle.point_from_proportion(0), color=ACCENT, radius=0.08)
        self.add(dot)
        self.play(
            MoveAlongPath(dot, circle), run_time=3,
            rate_func=linear,
        )
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 2: Definition ────────────────────────────────────────
    def scene2_definition(self):
        self.ly.section_divider(1, "Parametric Curves")

        self.add_subcaption(
            "A parametric curve describes both x and y as functions of "
            "a parameter t, usually representing time or angle.",
            duration=10,
        )

        title = self.ly.title("Definition")

        # Formula box
        defn_tex = VGroup(
            MathTex(
                r"x = f(t), \quad y = g(t)",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            Text(
                "for t in [a, b]",
                font_size=BODY_SIZE, color=DIM, font=SANS,
            ),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        defn_boxed = self.ly.formula_box(defn_tex[0])
        self.ly.safe_place(defn_boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(defn_boxed), run_time=SLOW)
        self.wait(1.0)

        domain = Text(
            "t is called the parameter (often time or angle)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(domain, direction=DOWN, anchor=defn_boxed)
        self.play(FadeIn(domain, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 3: Advantages ───────────────────────────────────────
    def scene3_advantages(self):
        self.ly.section_divider(2, "Why Parametric?")

        self.add_subcaption(
            "Parametric equations can describe curves that fail the "
            "vertical line test, model motion, and create beautiful shapes.",
            duration=10,
        )

        title = self.ly.title("Why Parametric?")

        items = [
            Text(
                "Curves that fail the vertical line test",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Motion along paths (physics!)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Lissajous figures, cycloids, spirals...",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 4: Eliminating the Parameter ─────────────────────────
    def scene4_eliminating_parameter(self):
        self.ly.section_divider(3, "Eliminating the Parameter")

        self.add_subcaption(
            "Sometimes we can eliminate the parameter t to get a Cartesian equation. "
            "This helps identify what kind of curve we have.",
            duration=12,
        )

        title = self.ly.title("Example: Ellipse")

        # Given
        given = MathTex(
            r"x = 2\cos t, \quad y = 3\sin t",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(given, direction=DOWN, anchor=title)
        self.play(Write(given), run_time=NORMAL)
        self.wait(0.5)

        # Step 1
        step1 = MathTex(
            r"\frac{x}{2} = \cos t, \quad \frac{y}{3} = \sin t",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=given)
        self.play(Write(step1), run_time=FAST)
        self.wait(0.3)

        # Step 2
        step2 = MathTex(
            r"\left(\frac{x}{2}\right)^2 + \left(\frac{y}{3}\right)^2 "
            r"= \cos^2 t + \sin^2 t = 1",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1)
        self.play(Write(step2), run_time=FAST)
        self.wait(0.5)

        # Result
        result_tex = MathTex(
            r"\frac{x^2}{4} + \frac{y^2}{9} = 1",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        result_boxed = self.ly.formula_box(result_tex)
        self.ly.safe_place(result_boxed, direction=DOWN, anchor=step2, buff=0.4)
        self.play(Write(result_boxed), run_time=NORMAL)
        self.wait(1.0)

        label = Text(
            "An ellipse!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(label, direction=DOWN, anchor=result_boxed)
        self.play(FadeIn(label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 5: Derivatives ──────────────────────────────────────
    def scene5_derivatives(self):
        self.ly.section_divider(4, "Derivatives")

        self.add_subcaption(
            "To find dy/dx for a parametric curve, we use the chain rule. "
            "The second derivative requires dividing by dx/dt again.",
            duration=12,
        )

        title = self.ly.title("First Derivative")

        # Formula box
        dydx_tex = MathTex(
            r"\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{g'(t)}{f'(t)}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        dydx_boxed = self.ly.formula_box(dydx_tex)
        self.ly.safe_place(dydx_boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(dydx_boxed), run_time=SLOW)
        self.wait(1.5)
        self.ly.clear()

        # Second derivative
        self.add_subcaption(
            "For the second derivative, differentiate dy/dx with respect to t, "
            "then divide by dx/dt again.",
            duration=8,
        )
        title2 = self.ly.title("Second Derivative")

        d2_tex = MathTex(
            r"\frac{d^2y}{dx^2} = "
            r"\frac{d}{dt}\!\left(\frac{dy}{dx}\right) "
            r"\Big/ \frac{dx}{dt}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        d2_boxed = self.ly.formula_box(d2_tex)
        self.ly.safe_place(d2_boxed, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(d2_boxed), run_time=SLOW)
        self.wait(1.0)

        warning = Text(
            "Don't just differentiate twice — divide by dx/dt!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(warning, direction=DOWN, anchor=d2_boxed)
        self.play(FadeIn(warning, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 6: Arc Length ────────────────────────────────────────
    def scene6_arc_length(self):
        self.ly.section_divider(5, "Arc Length")

        self.add_subcaption(
            "Arc length for parametric curves uses the Pythagorean "
            "theorem in integral form with both dx/dt and dy/dt.",
            duration=10,
        )

        title = self.ly.title("Arc Length Formula")

        # Formula box
        arc_tex = MathTex(
            r"L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 "
            r"+ \left(\frac{dy}{dt}\right)^2}\, dt",
            font_size=HEADING_SIZE, color=WHITE,
        )
        arc_boxed = self.ly.formula_box(arc_tex)
        self.ly.safe_place(arc_boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(arc_boxed), run_time=SLOW)
        self.wait(1.0)

        note = Text(
            "The integrand is the speed ds/dt!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=arc_boxed)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 7: Famous Examples ──────────────────────────────────
    def scene7_examples(self):
        self.ly.section_divider(6, "Famous Parametric Curves")

        self.add_subcaption(
            "Parametric equations describe many beautiful curves "
            "that are hard to express with Cartesian equations.",
            duration=8,
        )

        title = self.ly.title("Cycloid (Rolling Wheel)")

        cycloid_eq = MathTex(
            r"x = r(t - \sin t), \quad y = r(1 - \cos t)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(cycloid_eq, direction=DOWN, anchor=title)
        self.play(Write(cycloid_eq), run_time=NORMAL)
        self.wait(0.5)

        # Draw cycloid
        cycloid_points = [
            np.array([
                0.8 * (t - np.sin(t)) - 2,
                0.8 * (1 - np.cos(t)) - 1, 0,
            ])
            for t in [i * 0.05 for i in range(int(2 * np.pi / 0.05))]
        ]
        cycloid_curve = VMobject()
        cycloid_curve.set_points_smoothly(cycloid_points)
        cycloid_curve.set_color(PRIMARY)
        ensure_fits(cycloid_curve)
        self.ly.center_in_content(cycloid_curve)
        cycloid_curve.shift(DOWN * 0.5)
        self.play(Create(cycloid_curve), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        # Other curves
        self.add_subcaption(
            "Other famous curves include Lissajous figures, "
            "spirals, and asteroids.",
            duration=6,
        )
        title2 = self.ly.title("More Curves")

        items = [
            Text(
                "Lissajous: x = sin(at), y = sin(bt)",
                font_size=BODY_SIZE, color=SECONDARY, font=MONO,
            ),
            Text(
                "Spiral: x = t cos(t), y = t sin(t)",
                font_size=BODY_SIZE, color=SECONDARY, font=MONO,
            ),
            Text(
                "Asteroid: x = a cos^3(t), y = a sin^3(t)",
                font_size=BODY_SIZE, color=SECONDARY, font=MONO,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 8: Recap ────────────────────────────────────────────
    def scene8_recap(self):
        self.ly.section_divider(7, "Summary")

        self.add_subcaption(
            "Parametric equations give us x and y as functions of a parameter. "
            "Next: polar coordinates, another way to describe curves in the plane.",
            duration=10,
        )

        title = self.ly.title("What We Learned")

        items = [
            Text(
                "x = f(t), y = g(t) defines a parametric curve",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            MathTex(
                r"\frac{dy}{dx} = (dy/dt) \big/ (dx/dt)",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            Text(
                "Arc length uses the Pythagorean integrand",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Famous curves: cycloid, spiral, Lissajous",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)

        play_outro(self, "Polar Coordinates", "Calculus II")
