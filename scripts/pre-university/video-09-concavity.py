"""
Video 09: Concavity & the Second Derivative Test
Calculus I — concavity, inflection points, second derivative test.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, proper narration timing, SANS font for body.

Render draft:  manim -ql scripts/pre-university/video-09-concavity.py Video09_ConcavitySecondDeriv
Render final:  manim -qh scripts/pre-university/video-09-concavity.py Video09_ConcavitySecondDeriv

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


class Video09_ConcavitySecondDeriv(Scene):
    """Full video: 7 scenes — concavity visual, inflection points, 2nd deriv test, example."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_concavity()
        self.scene3_inflection()
        self.scene4_second_deriv_test()
        self.scene5_example()
        self.scene6_comparison()
        self.scene7_recap()

    # ── Scene 1: Hook ───────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "You found critical points using the first derivative. "
            "Now the second derivative tells you the shape "
            "and gives a faster way to classify extrema.",
            duration=8,
        )
        play_intro(self, "Concavity & 2nd Derivative Test", "Calculus I")

        self.add_subcaption(
            "Critical point found. Is it a peak or a valley?",
            duration=4,
        )

        problem = Text(
            "Critical point found. Peak or valley?",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        solution = Text(
            "The second derivative gives the answer instantly.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(solution, direction=DOWN, anchor=problem, buff=0.5)
        self.play(Write(solution), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 2: Concavity ───────────────────────────────────────
    def scene2_concavity(self):
        self.add_subcaption(
            "A function is concave up where its second derivative is positive. "
            "It looks like a bowl that holds water. "
            "Concave down means the second derivative is negative.",
            duration=8,
        )

        self.ly.section_divider(1, "Concavity")

        rules = [
            MathTex(r"f''(x) > 0", font_size=HEADING_SIZE, color=SECONDARY),
            Text("Concave up — holds water", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            MathTex(r"f''(x) < 0", font_size=HEADING_SIZE, color=RED),
            Text("Concave down — spills water", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(rules, start_from=None, run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 3: Inflection Points ───────────────────────────────
    def scene3_inflection(self):
        self.add_subcaption(
            "An inflection point is where the concavity changes. "
            "The second derivative is zero there, "
            "but not every zero is an inflection point.",
            duration=8,
        )

        self.ly.section_divider(2, "Inflection Points")

        definition = Text(
            "Inflection point: concavity changes sign at c",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(definition, anchor=None)
        self.play(FadeIn(definition, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        condition = MathTex(
            r"f''(c) = 0 \text{ and } f'' \text{ changes sign}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(condition, direction=DOWN, anchor=definition, buff=0.5)
        self.play(Write(condition), run_time=NORMAL)
        self.wait(0.5)

        # Counterexample
        self.add_subcaption(
            "For x to the fourth, the second derivative is zero at x equals 0, "
            "but concavity is always up. So x equals 0 is not an inflection point.",
            duration=8,
        )
        counter = Text(
            "f''(c) = 0 is necessary, not sufficient!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(counter, direction=DOWN, anchor=condition, buff=0.5)
        self.play(Write(counter), run_time=NORMAL)
        self.wait(0.5)

        ex = MathTex(
            r"f(x) = x^4: \; f''(0) = 0 \text{ but always concave up}",
            font_size=LABEL_SIZE, color=DIM,
        )
        self.ly.safe_place(ex, direction=DOWN, anchor=counter, buff=0.3)
        self.play(Write(ex), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 4: Second Derivative Test ──────────────────────────
    def scene4_second_deriv_test(self):
        self.add_subcaption(
            "At a critical point where f prime is zero, "
            "check the second derivative. "
            "Positive means local minimum. Negative means local maximum. "
            "Zero means the test is inconclusive.",
            duration=10,
        )

        self.ly.section_divider(3, "Second Derivative Test")

        precond = Text(
            "If f'(c) = 0 (critical point):",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(precond, anchor=None)
        self.play(Write(precond), run_time=FAST)
        self.wait(0.3)

        cases = [
            MathTex(r"f''(c) > 0 \implies \text{local minimum}", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"f''(c) < 0 \implies \text{local maximum}", font_size=BODY_SIZE, color=RED),
            MathTex(r"f''(c) = 0 \implies \text{inconclusive}", font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(cases, start_from=precond, run_time=FAST)
        self.wait(0.5)

        note = Text(
            "If inconclusive: fall back to 1st Derivative Test",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=cases[-1], buff=0.4)
        self.play(Write(note), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 5: Worked Example ──────────────────────────────────
    def scene5_example(self):
        self.add_subcaption(
            "Example: f of x equals x cubed minus 3x plus 2. "
            "Critical points at x equals plus or minus 1. "
            "Use the second derivative test to classify.",
            duration=8,
        )

        self.ly.section_divider(4, r"Example: $f(x) = x^3 - 3x + 2$")

        # Step 1
        step1 = MathTex(
            r"f'(x) = 3x^2 - 3 = 0 \implies x = \pm 1",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1, anchor=None)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)

        # Step 2
        step2 = MathTex(
            r"f''(x) = 6x",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.4)
        self.play(Write(step2), run_time=FAST)
        self.wait(0.5)

        # Classification
        self.add_subcaption(
            "At x equals negative 1, f double prime is negative 6, so local max. "
            "At x equals 1, f double prime is 6, so local min.",
            duration=8,
        )
        result1 = MathTex(
            r"f''(-1) = -6 < 0 \implies \text{local max}",
            font_size=BODY_SIZE, color=RED,
        )
        result2 = MathTex(
            r"f''(1) = 6 > 0 \implies \text{local min}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(result1, direction=DOWN, anchor=step2, buff=0.4)
        self.ly.safe_place(result2, direction=DOWN, anchor=result1, buff=0.3)
        self.play(Write(result1), run_time=FAST)
        self.play(Write(result2), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 6: Comparison of Tests ─────────────────────────────
    def scene6_comparison(self):
        self.add_subcaption(
            "The second derivative test is faster but sometimes inconclusive. "
            "The first derivative test always works.",
            duration=6,
        )

        self.ly.section_divider(5, "1st vs 2nd Derivative Test")

        # Two columns
        col1_header = Text("1st Derivative Test", font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD)
        col1_items = [
            Text("Always works", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Needs sign chart", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]

        col2_header = Text("2nd Derivative Test", font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD)
        col2_items = [
            Text("Faster (one value)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Inconclusive if f''=0", font_size=BODY_SIZE, color=RED, font=SANS),
        ]

        self.ly.two_columns(
            [col1_header] + col1_items,
            [col2_header] + col2_items,
        )
        self.play(Write(col1_header), Write(col2_header), run_time=FAST)
        self.play(
            FadeIn(col1_items[0], shift=LEFT * 0.15),
            FadeIn(col2_items[0], shift=RIGHT * 0.15),
            run_time=FAST,
        )
        self.play(
            FadeIn(col1_items[1], shift=LEFT * 0.15),
            FadeIn(col2_items[1], shift=RIGHT * 0.15),
            run_time=FAST,
        )
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 7: Recap + Outro ──────────────────────────────────
    def scene7_recap(self):
        self.add_subcaption(
            "Today: concavity, inflection points, second derivative test. "
            "Next: curve sketching.",
            duration=4,
        )

        title = self.ly.title("Summary")

        recap = [
            Text("f'' > 0 → concave up, f'' < 0 → concave down", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Inflection: concavity changes at c", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("2nd Deriv Test: f'' < 0 max, f'' > 0 min", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("If f'' = 0: fall back to 1st Deriv Test", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(recap, start_from=title, run_time=FAST)
        self.wait(1.0)

        play_outro(self, "Curve Sketching", "Calculus I")
