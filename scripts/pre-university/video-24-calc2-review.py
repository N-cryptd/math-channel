"""
Video 24: Calculus II Review
Covers: comprehensive review of all Calculus II topics, connections between concepts,
strategy guide for exams, preview of Calculus III.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, formula_box, proper narration timing.

Render draft:  manim -ql scripts/pre-university/video-24-calc2-review.py Video24_Calc2Review
Render final:  manim -qh scripts/pre-university/video-24-calc2-review.py Video24_Calc2Review

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


class Video24_Calc2Review(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_sequences_series()
        self.scene3_convergence_toolkit()
        self.scene4_power_taylor()
        self.scene5_parametric_polar()
        self.scene6_exam_strategy()
        self.scene7_common_mistakes()
        self.scene8_closing()

    # ── Scene 1: Hook — Big Picture ───────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Let us review everything we have learned in Calculus II. "
            "This video connects all the dots and prepares you for what comes next.",
            duration=12,
        )
        play_intro(self, "Calculus II Review", "Calculus II")

        overview = self.ly.title("The Big Picture of Calculus II")

        # Three pillars using two_columns
        left_items = [
            VGroup(
                MathTex(r"\sum", font_size=TITLE_SIZE, color=PRIMARY),
                Text("Sequences & Series", font_size=BODY_SIZE, color=WHITE, font=SANS),
            ).arrange(DOWN, buff=0.2),
            VGroup(
                MathTex(r"P_n(x)", font_size=TITLE_SIZE, color=SECONDARY),
                Text("Power & Taylor", font_size=BODY_SIZE, color=WHITE, font=SANS),
            ).arrange(DOWN, buff=0.2),
        ]
        right_items = [
            VGroup(
                MathTex(r"(r, \theta)", font_size=TITLE_SIZE, color=ACCENT),
                Text("Parametric & Polar", font_size=BODY_SIZE, color=WHITE, font=SANS),
            ).arrange(DOWN, buff=0.2),
        ]
        self.ly.two_columns(left_items, right_items, start_from=overview)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 2: Sequences & Series Review ─────────────────────────
    def scene2_sequences_series(self):
        self.ly.section_divider(1, "Sequences & Series")

        self.add_subcaption(
            "We started with sequences as functions of natural numbers, "
            "then built series as sums of sequence terms.",
            duration=10,
        )

        title = self.ly.title("Key Ideas")

        items = [
            Text(
                "Sequence: a_n as n -> infinity",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Series: sum of sequence terms",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            MathTex(
                r"S_n = \sum_{k=1}^{n} a_k",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            Text(
                "Geometric: a/(1-r) when |r| < 1",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Harmonic diverges — key counterexample!",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 3: Convergence Toolkit ───────────────────────────────
    def scene3_convergence_toolkit(self):
        self.ly.section_divider(2, "Convergence Decision Tree")

        self.add_subcaption(
            "The convergence tests form a decision tree. "
            "Always start with the easiest test and work your way up.",
            duration=10,
        )

        title = self.ly.title("Test Order")

        items = [
            Text(
                "1. Divergence test (n-th term test)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
            ),
            Text(
                "2. Is it a p-series or geometric?",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "3. Ratio test (factorials, exponentials)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "4. Comparison or Integral test",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "5. Alternating series test if signs alternate",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)

        remember = Text(
            "Absolute convergence => convergence (always!)",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        last_item = None
        for m in reversed(self.mobjects):
            if m not in [self._bg_dots, self._bg_gradient] and hasattr(m, 'get_bottom'):
                last_item = m
                break
        if last_item is not None:
            self.ly.safe_place(remember, direction=DOWN, anchor=last_item)
        self.play(FadeIn(remember, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 4: Power & Taylor ───────────────────────────────────
    def scene4_power_taylor(self):
        self.ly.section_divider(3, "Power & Taylor Series")

        self.add_subcaption(
            "Power series turn sums into functions. "
            "Taylor series approximate any smooth function with polynomials.",
            duration=10,
        )

        title = self.ly.title("Key Formulas")

        items = [
            VGroup(
                Text("Power:", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD),
                MathTex(r"\sum c_n (x-a)^n, \; R = 1/\rho", font_size=BODY_SIZE, color=WHITE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("Taylor:", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD),
                MathTex(
                    r"f(x) = \sum \frac{f^{(n)}(a)}{n!}(x-a)^n",
                    font_size=BODY_SIZE, color=PRIMARY,
                ),
            ).arrange(RIGHT, buff=0.3),
            Text(
                "Maclaurin = Taylor at a = 0",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "5 essential series: e^x, sin, cos, ln, 1/(1-x)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 5: Parametric & Polar ───────────────────────────────
    def scene5_parametric_polar(self):
        self.ly.section_divider(4, "Parametric & Polar")

        self.add_subcaption(
            "Parametric equations model motion along curves. "
            "Polar coordinates describe circular and spiral shapes.",
            duration=10,
        )

        title = self.ly.title("Side by Side")

        left_items = [
            Text("Parametric", font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD),
            MathTex(r"dy/dx = (dy/dt)/(dx/dt)", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"L = \int \sqrt{(dx/dt)^2+(dy/dt)^2}\, dt", font_size=BODY_SIZE, color=WHITE),
        ]
        right_items = [
            Text("Polar", font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD),
            MathTex(r"x = r\cos\theta, \; y = r\sin\theta", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"A = \tfrac{1}{2}\int r^2\, d\theta", font_size=BODY_SIZE, color=PRIMARY),
        ]
        self.ly.two_columns(left_items, right_items, start_from=title)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 6: Exam Strategy ─────────────────────────────────────
    def scene6_exam_strategy(self):
        self.ly.section_divider(5, "Exam Strategy")

        self.add_subcaption(
            "On exams, read the problem first, identify which tool applies, "
            "and show your work clearly.",
            duration=10,
        )

        title = self.ly.title("The RISEV Method")

        items = [
            Text(
                "R — READ: What type of problem?",
                font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
            ),
            Text(
                "I — IDENTIFY: Series? Convergence? Taylor?",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "S — SELECT: Pick the right test or formula",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "E — EXECUTE: Show all steps clearly",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "V — VERIFY: Does the answer make sense?",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 7: Common Mistakes ───────────────────────────────────
    def scene7_common_mistakes(self):
        self.ly.section_divider(6, "Common Mistakes")

        self.add_subcaption(
            "Avoid these frequent errors on exams.",
            duration=6,
        )

        title = self.ly.title("Watch Out!")

        items = [
            Text(
                "Forgetting to test endpoints of power series",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Wrong second derivative for parametric curves",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Confusing conditional vs absolute convergence",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 8: Closing ──────────────────────────────────────────
    def scene8_closing(self):
        self.add_subcaption(
            "Congratulations on completing Calculus II. "
            "Next up: Calculus III takes us into 3D space.",
            duration=10,
        )

        congrats = self.ly.title("Congratulations!")

        items = [
            Text("Sequences & Series", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Convergence Tests", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Power & Taylor Series", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Parametric Equations", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Polar Coordinates", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]

        self.ly.progressive_reveal(items, start_from=congrats)
        self.wait(1.0)
        self.ly.clear()

        # Preview of Calc III
        self.add_subcaption(
            "Coming up in Calculus III: vectors in 3D, "
            "partial derivatives, and multiple integrals.",
            duration=8,
        )
        preview_title = self.ly.title("Next: Calculus III")

        preview_items = [
            Text("Vectors in 3D Space", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Partial Derivatives", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Multiple Integrals", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]

        self.ly.progressive_reveal(preview_items, start_from=preview_title)
        self.wait(1.0)

        play_outro(self, "Vectors (Calculus III)", "Calculus III")
