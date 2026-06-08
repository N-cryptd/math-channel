"""
Video 16: Applications of Integrals
Calculus I — area between curves, volumes of revolution (disk method), arc length.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, proper narration timing, SANS font for body.

Render draft:  manim -ql scripts/pre-university/video-16-applications.py Video16_Applications
Render final:  manim -qh scripts/pre-university/video-16-applications.py Video16_Applications

QUALITY RULES (enforced):
  1. Max 5 visible elements per scene at any time
  2. Use LayoutEngine for ALL text/formula positioning — no raw .shift() or .to_edge()
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


class Video16_Applications(Scene):
    """Full video: 7 scenes — hook, area between, area example, disk method, arc length, recap."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_area_between()
        self.scene3_area_example()
        self.scene4_disk_method()
        self.scene5_arc_length()
        self.scene6_recap()

    # ── Scene 1: Hook ───────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Integrals compute areas between curves, volumes of 3D solids, "
            "arc lengths, and more. This is where calculus gets powerful.",
            duration=6,
        )
        play_intro(self, "Applications of Integrals", "Calculus I")

        apps = [
            Text("Area between curves", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
            Text("Volumes of revolution", font_size=HEADING_SIZE, color=SECONDARY, font=SANS),
            Text("Arc length", font_size=HEADING_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(apps, start_from=None, run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 2: Area Between Curves ────────────────────────────
    def scene2_area_between(self):
        self.add_subcaption(
            "The area between two curves f and g from a to b "
            "is the integral of absolute f minus g dx. "
            "Always integrate top minus bottom.",
            duration=6,
        )

        self.ly.section_divider(1, "Area Between Curves")

        formula = MathTex(
            r"A = \int_a^b |f(x) - g(x)| \, dx",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(formula, color=ACCENT)
        self.ly.safe_place(formula, anchor=None)
        self.play(Write(formula), run_time=SLOW)
        self.wait(0.5)

        tip = Text(
            "Always integrate top minus bottom!",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(tip, direction=DOWN, anchor=formula, buff=0.5)
        self.play(Write(tip), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 3: Area Example ───────────────────────────────────
    def scene3_area_example(self):
        self.add_subcaption(
            "Find area between y equals x squared and y equals 2x. "
            "Intersections at x equals 0 and x equals 2. "
            "Integrate 2x minus x squared from 0 to 2.",
            duration=8,
        )

        self.ly.section_divider(2, r"Example: $y = x^2$ vs $y = 2x$")

        intersect = MathTex(
            r"x^2 = 2x \Rightarrow x = 0, \; 2",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(intersect, anchor=None)
        self.play(Write(intersect), run_time=FAST)
        self.wait(0.5)

        integral = MathTex(
            r"A = \int_0^2 (2x - x^2)\,dx = \left[x^2 - \frac{x^3}{3}\right]_0^2 = \frac{4}{3}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(integral, direction=DOWN, anchor=intersect, buff=0.5)
        self.play(Write(integral), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 4: Disk Method ─────────────────────────────────────
    def scene4_disk_method(self):
        self.add_subcaption(
            "Rotate a region around an axis to create a solid. "
            "The disk method: volume equals pi times integral of f of x squared dx. "
            "Each disk has radius f of x and thickness dx.",
            duration=8,
        )

        self.ly.section_divider(3, "Disk Method for Volumes")

        formula = MathTex(
            r"V = \pi \int_a^b [f(x)]^2 \, dx",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(formula, color=ACCENT)
        self.ly.safe_place(formula, anchor=None)
        self.play(Write(formula), run_time=SLOW)
        self.wait(0.5)

        self.ly.clear()

        # Example
        self.add_subcaption(
            "Rotate y equals root x about the x-axis from 0 to 4. "
            "Volume is pi times the integral of x from 0 to 4, which is 8 pi.",
            duration=6,
        )

        title4 = self.ly.title("Example")

        problem = MathTex(
            r"y = \sqrt{x}, \text{ about } x\text{-axis}, \; x \in [0, 4]",
            font_size=LABEL_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, direction=DOWN, anchor=title4, buff=0.4)
        self.play(Write(problem), run_time=FAST)
        self.wait(0.5)

        result = MathTex(
            r"V = \pi \int_0^4 x\,dx = \pi \left[\frac{x^2}{2}\right]_0^4 = 8\pi",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=problem, buff=0.4)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 5: Arc Length ─────────────────────────────────────
    def scene5_arc_length(self):
        self.add_subcaption(
            "Arc length from a to b is the integral of "
            "square root of one plus f prime squared dx. "
            "From the Pythagorean theorem on infinitesimal segments.",
            duration=6,
        )

        self.ly.section_divider(4, "Arc Length")

        formula = MathTex(
            r"L = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(formula, color=ACCENT)
        self.ly.safe_place(formula, anchor=None)
        self.play(Write(formula), run_time=SLOW)
        self.wait(0.5)

        self.ly.clear()

        # Example
        self.add_subcaption(
            "Length of y equals two-thirds x to the three-halves "
            "from 0 to 3. F prime is root x. "
            "Result is 14 thirds.",
            duration=6,
        )

        title5 = self.ly.title("Example")

        result = MathTex(
            r"L = \int_0^3 \sqrt{1+x}\,dx = \frac{14}{3}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=title5, buff=0.5)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 6: Recap + Outro ─────────────────────────────────
    def scene6_recap(self):
        self.add_subcaption(
            "Applications: area between curves, volumes by disk method, arc length. "
            "This completes Calculus I! Next: Calculus II techniques.",
            duration=6,
        )

        title = self.ly.title("Summary")

        recap = [
            Text("Area between curves: integral of |f - g|", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Volume (disk): pi * integral of [f(x)]^2", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Arc length: integral of sqrt(1 + [f']^2)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(recap, start_from=title, run_time=FAST)
        self.wait(1.0)

        celebration = Text(
            "This completes Calculus I!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(celebration, direction=DOWN, anchor=None, buff=0.5)
        self.play(Write(celebration), run_time=SLOW)
        self.wait(1.0)

        play_outro(self, "Sequences (Calc II)", "Calculus I")
