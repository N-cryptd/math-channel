"""
Video 19: Tests for Convergence
Covers: comparison test, limit comparison test, ratio test, root test,
integral test, alternating series test, absolute vs conditional convergence.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, formula_box, proper narration timing.

Render draft:  manim -ql scripts/pre-university/video-19-convergence-tests.py Video19_ConvergenceTests
Render final:  manim -qh scripts/pre-university/video-19-convergence-tests.py Video19_ConvergenceTests

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


class Video19_ConvergenceTests(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_direct_comparison()
        self.scene3_limit_comparison()
        self.scene4_ratio_test()
        self.scene5_ratio_example()
        self.scene6_integral_test()
        self.scene7_p_series()
        self.scene8_alternating()
        self.scene9_absolute_conditional()
        self.scene10_recap()

    # ── Scene 1: Hook — "How do we decide?" ───────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "How do we decide if a series converges? "
            "We need a systematic toolbox of tests.",
            duration=10,
        )
        play_intro(self, "Tests for Convergence", "Calculus II")

        # Motivating question
        problem = Text(
            "Does this converge?",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(problem)
        self.play(Write(problem), run_time=NORMAL)

        series = MathTex(
            r"\sum_{n=1}^{\infty} \frac{n^2}{n^4 + 1}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(series, direction=DOWN, anchor=problem)
        self.play(Write(series), run_time=NORMAL)
        self.wait(1.0)

        toolbox = Text(
            "We need a toolbox of convergence tests.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(toolbox, direction=DOWN, anchor=series)
        self.play(FadeIn(toolbox, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 2: Direct Comparison Test ───────────────────────────
    def scene2_direct_comparison(self):
        self.ly.section_divider(1, "Direct Comparison Test")

        self.add_subcaption(
            "The direct comparison test lets us relate an unknown series "
            "to a known one. If your series is smaller than a convergent "
            "series, it also converges.",
            duration=14,
        )

        title = self.ly.title("Direct Comparison Test")

        # The condition
        cond = MathTex(
            r"0 \leq a_n \leq b_n \quad \text{for all } n",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(cond, direction=DOWN, anchor=title)
        self.play(Write(cond), run_time=NORMAL)
        self.wait(0.5)

        # Converges implication
        conv = Text(
            "If sum b_n converges, then sum a_n converges.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(conv, direction=DOWN, anchor=cond)
        self.play(FadeIn(conv, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Diverges implication
        div = Text(
            "If sum a_n diverges, then sum b_n diverges.",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(div, direction=DOWN, anchor=conv)
        self.play(FadeIn(div, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 3: Limit Comparison Test ──────────────────────────────
    def scene3_limit_comparison(self):
        self.ly.section_divider(2, "Limit Comparison Test")

        self.add_subcaption(
            "The limit comparison test is more flexible. "
            "If the ratio of terms approaches a finite positive limit, "
            "both series share the same convergence behavior.",
            duration=14,
        )

        title = self.ly.title("Limit Comparison Test")

        # The limit
        limit = MathTex(
            r"L = \lim_{n \to \infty} \frac{a_n}{b_n}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(limit, direction=DOWN, anchor=title)
        self.play(Write(limit), run_time=NORMAL)
        self.wait(0.5)

        # The result
        result = Text(
            "If 0 < L < infinity, both converge or both diverge.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=limit)
        self.play(FadeIn(result, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.0)

        # Note
        note = Text(
            "Choose b_n to be a known benchmark (p-series, geometric).",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=result)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 4: Ratio Test (statement) ─────────────────────────────
    def scene4_ratio_test(self):
        self.ly.section_divider(3, "The Ratio Test")

        self.add_subcaption(
            "The ratio test is extremely powerful. "
            "It works especially well for series involving factorials and exponentials.",
            duration=10,
        )

        title = self.ly.title("The Ratio Test")

        # The test formula
        formula_tex = MathTex(
            r"\rho = \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right|",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_boxed = self.ly.formula_box(formula_tex)
        self.ly.safe_place(formula_boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(formula_boxed), run_time=SLOW)
        self.wait(1.0)

        # Three cases
        c1 = Text(
            "rho < 1: series CONVERGES absolutely",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(c1, direction=DOWN, anchor=formula_boxed)
        self.play(FadeIn(c1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        c2 = Text(
            "rho > 1: series DIVERGES",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(c2, direction=DOWN, anchor=c1)
        self.play(FadeIn(c2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        c3 = Text(
            "rho = 1: INCONCLUSIVE (use another test)",
            font_size=BODY_SIZE, color=DIM, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(c3, direction=DOWN, anchor=c2)
        self.play(FadeIn(c3, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 5: Ratio Test Example ───────────────────────────────
    def scene5_ratio_example(self):
        self.ly.section_divider(4, "Ratio Test Example")

        self.add_subcaption(
            "Let us apply the ratio test to a series with factorials. "
            "Factor n over ten to the n diverges because the ratio grows without bound.",
            duration=14,
        )

        title = self.ly.title("Example")

        ex_series = MathTex(
            r"\sum_{n=0}^{\infty} \frac{n!}{10^n}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex_series, direction=DOWN, anchor=title)
        self.play(Write(ex_series), run_time=NORMAL)
        self.wait(0.5)

        # Ratio computation
        ratio = MathTex(
            r"\rho = \lim \frac{(n+1)!\, /\, 10^{n+1}}{n!\, /\, 10^n}"
            r" = \lim \frac{n+1}{10} = \infty > 1",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ratio, direction=DOWN, anchor=ex_series)
        self.play(Write(ratio), run_time=NORMAL)
        self.wait(0.5)

        result = Text(
            "The series DIVERGES by the ratio test.",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=ratio)
        self.play(FadeIn(result, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 6: Integral Test ─────────────────────────────────────
    def scene6_integral_test(self):
        self.ly.section_divider(5, "The Integral Test")

        self.add_subcaption(
            "When the terms come from a positive, decreasing function, "
            "we can compare the series to an improper integral.",
            duration=10,
        )

        title = self.ly.title("Integral Test")

        # Conditions
        conditions = Text(
            "If f is positive, continuous, and decreasing:",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(conditions, direction=DOWN, anchor=title)
        self.play(FadeIn(conditions, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Formula box
        formula_tex = MathTex(
            r"\sum_{n=1}^{\infty} f(n) \;\text{ and }\; "
            r"\int_1^{\infty} f(x)\,dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_boxed = self.ly.formula_box(formula_tex)
        self.ly.safe_place(formula_boxed, direction=DOWN, anchor=conditions, buff=0.4)
        self.play(Write(formula_boxed), run_time=SLOW)
        self.wait(1.0)

        result = Text(
            "Either BOTH converge or BOTH diverge.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=formula_boxed)
        self.play(FadeIn(result, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 7: p-Series (corollary) ──────────────────────────────
    def scene7_p_series(self):
        self.ly.section_divider(6, "p-Series")

        self.add_subcaption(
            "A p-series converges when p is greater than one, "
            "and diverges when p is one or less. "
            "The case p equals one is the harmonic series.",
            duration=12,
        )

        title = self.ly.title("p-Series (Corollary)")

        # Formula box for p-series
        p_tex = MathTex(
            r"\sum_{n=1}^{\infty} \frac{1}{n^p}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(p_tex, direction=DOWN, anchor=title)
        self.play(Write(p_tex), run_time=NORMAL)
        self.wait(0.5)

        # Converges case
        conv = Text(
            "Converges if p > 1",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(conv, direction=DOWN, anchor=p_tex)
        self.play(FadeIn(conv, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        # Diverges case
        div = Text(
            "Diverges if p <= 1",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(div, direction=DOWN, anchor=conv)
        self.play(FadeIn(div, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Note about harmonic
        note = Text(
            "(p = 1 is the harmonic series!)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=div)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 8: Alternating Series Test ────────────────────────────
    def scene8_alternating(self):
        self.ly.section_divider(7, "Alternating Series Test")

        self.add_subcaption(
            "Alternating series have terms that switch sign. "
            "The test checks two conditions: decreasing magnitude "
            "and terms going to zero.",
            duration=12,
        )

        title = self.ly.title("Alternating Series Test")

        # General form
        form = MathTex(
            r"\sum_{n=1}^{\infty} (-1)^{n-1} b_n = b_1 - b_2 + b_3 - \cdots",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(form, direction=DOWN, anchor=title)
        self.play(Write(form), run_time=NORMAL)
        self.wait(0.5)

        # Condition 1
        c1 = Text(
            "1. b_n is decreasing: b_1 >= b_2 >= ...",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(c1, direction=DOWN, anchor=form)
        self.play(FadeIn(c1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        # Condition 2
        c2 = Text(
            "2. lim b_n = 0",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(c2, direction=DOWN, anchor=c1)
        self.play(FadeIn(c2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Conclusion
        conclusion = Text(
            "If BOTH hold, the series converges.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(conclusion, direction=DOWN, anchor=c2)
        self.play(FadeIn(conclusion, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        # Example
        self.add_subcaption(
            "The alternating harmonic series converges to the natural logarithm of 2.",
            duration=8,
        )
        title2 = self.ly.title("Example")

        example = MathTex(
            r"\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n} = \ln 2",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(example, direction=DOWN, anchor=title2)
        self.play(Write(example), run_time=NORMAL)
        self.wait(0.5)

        name = Text(
            "This is the alternating harmonic series!",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(name, direction=DOWN, anchor=example)
        self.play(FadeIn(name, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 9: Absolute vs Conditional Convergence ───────────────
    def scene9_absolute_conditional(self):
        self.ly.section_divider(8, "Absolute vs Conditional")

        self.add_subcaption(
            "Absolute convergence is stronger than conditional convergence. "
            "A series that converges absolutely also converges, "
            "but not the other way around.",
            duration=14,
        )

        title = self.ly.title("Two Types of Convergence")

        # Absolute convergence
        abs_title = Text(
            "Absolute Convergence:",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(abs_title, direction=DOWN, anchor=title)
        self.play(Write(abs_title), run_time=FAST)

        abs_def = MathTex(
            r"\sum |a_n| \text{ converges}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(abs_def, direction=DOWN, anchor=abs_title)
        self.play(Write(abs_def), run_time=FAST)

        abs_note = Text(
            "Strongest form — rearranging terms is safe.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(abs_note, direction=DOWN, anchor=abs_def)
        self.play(FadeIn(abs_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.0)
        self.ly.clear()

        # Conditional convergence
        cond_title = Text(
            "Conditional Convergence:",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(cond_title, direction=DOWN, anchor=title)
        self.play(Write(cond_title), run_time=FAST)

        cond_def = MathTex(
            r"\sum a_n \text{ converges but } \sum |a_n| \text{ diverges}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(cond_def, direction=DOWN, anchor=cond_title)
        self.play(Write(cond_def), run_time=FAST)

        cond_note = Text(
            "Rearranging terms can change the sum!",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(cond_note, direction=DOWN, anchor=cond_def)
        self.play(FadeIn(cond_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.0)
        self.ly.clear()

        # Key implication
        self.add_subcaption(
            "Key fact: absolute convergence always implies regular convergence.",
            duration=6,
        )
        title2 = self.ly.title("Key Implication")

        key = Text(
            "Absolute convergence always implies convergence!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(key)
        self.play(Write(key), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 10: Recap ───────────────────────────────────────────
    def scene10_recap(self):
        self.ly.section_divider(9, "Summary")

        self.add_subcaption(
            "We now have a full toolkit for testing convergence. "
            "Next we will explore power series and Taylor series.",
            duration=10,
        )

        title = self.ly.title("Your Convergence Toolkit")

        items = [
            Text(
                "Divergence test: first check, easy to apply",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Comparison tests: compare to known series",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Ratio test: great for factorials, exponentials",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Integral test: for positive, decreasing terms",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Alternating series test: for sign-changing terms",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Absolute convergence implies convergence",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)

        play_outro(self, "Power Series & Taylor Series", "Calculus II")
