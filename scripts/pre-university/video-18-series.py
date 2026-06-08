"""
Video 18: Infinite Series
Covers: partial sums, sigma notation, geometric series, divergence test,
harmonic series, telescoping series, n-th term test.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, formula_box, proper narration timing.

Render draft:  manim -ql scripts/pre-university/video-18-series.py Video18_Series
Render final:  manim -qh scripts/pre-university/video-18-series.py Video18_Series

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


class Video18_Series(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_partial_sums()
        self.scene3_sigma_notation()
        self.scene4_geometric_series()
        self.scene5_harmonic_and_divergence()
        self.scene6_telescoping()
        self.scene7_recap()

    # ── Scene 1: The Hook — "Can you add infinitely many numbers?" ─────
    def scene1_hook(self):
        self.add_subcaption(
            "Can you add infinitely many numbers and get a finite result? "
            "The answer is yes, and it is beautiful.",
            duration=10,
        )
        play_intro(self, "Infinite Series", "Calculus II")

        # Central question
        question = Text(
            "What is 1 + 1/2 + 1/4 + 1/8 + ... ?",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(question)
        self.play(Write(question), run_time=NORMAL)
        self.wait(0.5)

        # Visual: shrinking bars representing partial sums
        # Bar 1: 1.0, Bar 2: 0.5, Bar 3: 0.25...
        bars = VGroup()
        bar_data = [
            (1.0, "1", PRIMARY),
            (0.5, "1/2", SECONDARY),
            (0.25, "1/4", ACCENT),
            (0.125, "1/8", RED),
        ]
        bar_width = 0.8
        x_cursor = -2.0
        for height, label_str, col in bar_data:
            bar = Rectangle(
                width=bar_width, height=height,
                fill_color=col, fill_opacity=0.5,
                stroke_color=WHITE, stroke_width=1,
            )
            bar.move_to(DOWN * 0.8).shift(RIGHT * x_cursor)
            bar.align_to(DOWN * 2.5, DOWN)
            lbl = MathTex(label_str, font_size=LABEL_SIZE, color=WHITE)
            lbl.next_to(bar, UP, buff=0.1)
            bars.add(bar, lbl)
            x_cursor += bar_width + 0.15

        ensure_fits(bars)
        for i in range(0, len(bars), 2):
            self.play(
                FadeIn(bars[i]), FadeIn(bars[i + 1]),
                run_time=FAST,
            )
            self.wait(0.2)

        # Show the answer
        answer = MathTex(
            r"1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots = 2",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(answer, direction=DOWN, anchor=bars, buff=0.4)
        self.play(Write(answer), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 2: Partial Sums ───────────────────────────────────────
    def scene2_partial_sums(self):
        self.ly.section_divider(1, "Partial Sums")

        self.add_subcaption(
            "We define the sum of an infinite series as the limit of its partial sums. "
            "If that limit exists, the series converges.",
            duration=12,
        )

        title = self.ly.title("Partial Sums")

        # Partial sum definition
        defn = MathTex(
            r"S_n = \sum_{k=1}^{n} a_k = a_1 + a_2 + \cdots + a_n",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(defn, direction=DOWN, anchor=title)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(0.5)

        # Convergence definition
        conv = MathTex(
            r"\sum_{k=1}^{\infty} a_k = \lim_{n \to \infty} S_n",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(conv, direction=DOWN, anchor=defn)
        self.play(Write(conv), run_time=NORMAL)
        self.wait(0.5)

        # Converges note
        note = Text(
            "If the limit exists (finite), the series CONVERGES.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=conv)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Diverges note (replaces converges after delay)
        note2 = Text(
            "Otherwise, the series DIVERGES.",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(note2, direction=DOWN, anchor=conv)
        self.play(
            FadeOut(note), FadeIn(note2, shift=LEFT * 0.15),
            run_time=FAST,
        )
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 3: Sigma Notation ────────────────────────────────────
    def scene3_sigma_notation(self):
        self.ly.section_divider(2, "Sigma Notation")

        self.add_subcaption(
            "Sigma notation lets us write sums compactly. "
            "The index variable, start and end values define the range of summation.",
            duration=10,
        )

        title = self.ly.title("Sigma Notation")

        # Annotated sigma
        sigma = MathTex(
            r"\overbrace{\sum_{k=1}^{\infty}}^{\text{sum}} "
            r"\overbrace{a_k}^{\text{terms}}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(sigma, direction=DOWN, anchor=title)
        self.play(Write(sigma), run_time=NORMAL)
        self.wait(0.5)

        # Example 1: finite
        ex1 = MathTex(
            r"\sum_{k=1}^{5} k = 1 + 2 + 3 + 4 + 5 = 15",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex1, direction=DOWN, anchor=sigma)
        self.play(Write(ex1), run_time=NORMAL)
        self.wait(0.5)

        # Example 2: geometric
        ex2 = MathTex(
            r"\sum_{k=1}^{\infty} \frac{1}{2^k} = \frac{1}{2} + \frac{1}{4} + \cdots",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex2, direction=DOWN, anchor=ex1)
        self.play(Write(ex2), run_time=NORMAL)
        self.wait(0.5)

        # Example 3: oscillating
        ex3 = MathTex(
            r"\sum_{k=0}^{\infty} (-1)^k = 1 - 1 + 1 - 1 + \cdots",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(ex3, direction=DOWN, anchor=ex2)
        self.play(Write(ex3), run_time=NORMAL)
        self.wait(0.5)

        # Note on oscillating
        osc = Text(
            "This last one oscillates — it diverges!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(osc, direction=DOWN, anchor=ex3)
        self.play(FadeIn(osc, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 4: Geometric Series (KEY FORMULA) ────────────────────
    def scene4_geometric_series(self):
        self.ly.section_divider(3, "Geometric Series")

        self.add_subcaption(
            "The geometric series is the most important series in calculus. "
            "It converges when the common ratio r has absolute value less than one.",
            duration=14,
        )

        title = self.ly.title("Geometric Series")

        # General form
        geo = MathTex(
            r"\sum_{k=0}^{\infty} ar^k = a + ar + ar^2 + ar^3 + \cdots",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(geo, direction=DOWN, anchor=title)
        self.play(Write(geo), run_time=NORMAL)
        self.wait(0.5)

        # THE formula — with formula box
        formula_tex = MathTex(
            r"= \frac{a}{1 - r}, \quad |r| < 1",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        formula_boxed = self.ly.formula_box(formula_tex)
        self.ly.safe_place(formula_boxed, direction=DOWN, anchor=geo, buff=0.5)
        self.play(Write(formula_boxed), run_time=SLOW)
        self.wait(1.5)
        self.ly.clear()  # clear before the number line

        # Number line showing convergence/divergence regions
        self.add_subcaption(
            "The series converges only when r is between negative one and one.",
            duration=8,
        )
        title2 = self.ly.title("Convergence Region")

        ax = NumberLine(
            x_range=[-2, 2, 0.5], length=8,
            color=DIM, include_numbers=True,
        )
        self.ly.center_in_content(ax)
        self.play(Create(ax), run_time=NORMAL)

        # Converges box
        converge_box = Rectangle(
            width=4, height=0.5, fill_color=SECONDARY,
            fill_opacity=0.2, stroke_color=SECONDARY, stroke_width=2,
        )
        converge_box.move_to(ax.n2p(0))
        converge_label = Text(
            "Converges", font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        converge_label.next_to(converge_box, UP, buff=0.1)
        self.play(FadeIn(converge_box), FadeIn(converge_label), run_time=FAST)

        # Diverges labels
        div_left = Text(
            "Diverges", font_size=LABEL_SIZE, color=RED, font=SANS,
        )
        div_left.move_to(ax.n2p(-1.5) + UP * 0.6)
        div_right = Text(
            "Diverges", font_size=LABEL_SIZE, color=RED, font=SANS,
        )
        div_right.move_to(ax.n2p(1.5) + UP * 0.6)
        self.play(FadeIn(div_left), FadeIn(div_right), run_time=FAST)
        self.wait(1.0)
        self.ly.clear()

        # Examples scene
        self.add_subcaption(
            "Example: the sum of one over two to the k equals two. "
            "And three tenths plus three hundredths converges to ten thirds.",
            duration=12,
        )
        title3 = self.ly.title("Examples")

        ex1 = MathTex(
            r"\sum_{k=0}^{\infty} \frac{1}{2^k} = \frac{1}{1 - 1/2} = 2",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex1, direction=DOWN, anchor=title3)
        self.play(Write(ex1), run_time=NORMAL)
        self.wait(0.5)

        ex2 = MathTex(
            r"\sum_{k=0}^{\infty} \frac{3}{10^k} = \frac{3}{1 - 1/10} = \frac{10}{3}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex2, direction=DOWN, anchor=ex1)
        self.play(Write(ex2), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 5: Harmonic Series & Divergence Test ─────────────────
    def scene5_harmonic_and_divergence(self):
        self.ly.section_divider(4, "Harmonic Series")

        self.add_subcaption(
            "The harmonic series is a classic counterexample. "
            "Its terms go to zero, but the series still diverges to infinity.",
            duration=10,
        )

        title = self.ly.title("The Harmonic Series")

        # Harmonic series formula
        harmonic = MathTex(
            r"\sum_{k=1}^{\infty} \frac{1}{k} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots = \infty",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(harmonic, direction=DOWN, anchor=title)
        self.play(Write(harmonic), run_time=NORMAL)
        self.wait(0.5)

        # The paradox
        paradox = Text(
            "Even though 1/k → 0, the sum diverges!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(paradox, direction=DOWN, anchor=harmonic)
        self.play(FadeIn(paradox, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Divergence Test scene
        self.ly.section_divider(5, "Divergence Test")

        self.add_subcaption(
            "The divergence test says: if the terms do not go to zero, "
            "then the series diverges. But the converse is false.",
            duration=12,
        )

        title2 = self.ly.title("The n-th Term Test")

        # Statement in formula box
        dt_tex = MathTex(
            r"\text{If } \lim_{n \to \infty} a_n \neq 0,"
            r"\; \text{then } \sum a_n \text{ diverges.}",
            font_size=BODY_SIZE, color=WHITE,
        )
        dt_boxed = self.ly.formula_box(dt_tex)
        self.ly.safe_place(dt_boxed, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(dt_boxed), run_time=SLOW)
        self.wait(1.0)

        # Warning
        warning = Text(
            "BUT: a_n → 0 does NOT guarantee convergence!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(warning, direction=DOWN, anchor=dt_boxed, buff=0.6)
        self.play(FadeIn(warning, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Counterexample
        counter = Text(
            "The harmonic series is the counterexample!",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(counter, direction=DOWN, anchor=warning)
        self.play(FadeIn(counter, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 6: Telescoping Series ────────────────────────────────
    def scene6_telescoping(self):
        self.ly.section_divider(6, "Telescoping Series")

        self.add_subcaption(
            "Telescoping series cancel their middle terms, "
            "leaving only the first and last. The key is partial fractions.",
            duration=10,
        )

        title = self.ly.title("Telescoping Series")

        # The classic example
        series = MathTex(
            r"\sum_{k=1}^{\infty} \left(\frac{1}{k} - \frac{1}{k+1}\right)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(series, direction=DOWN, anchor=title)
        self.play(Write(series), run_time=NORMAL)
        self.wait(0.5)

        # Expansion showing cancellation
        expansion = MathTex(
            r"= \left(1 - \frac{1}{2}\right) "
            r"+ \left(\frac{1}{2} - \frac{1}{3}\right) "
            r"+ \left(\frac{1}{3} - \frac{1}{4}\right) + \cdots",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(expansion, direction=DOWN, anchor=series)
        self.play(Write(expansion), run_time=NORMAL)
        self.wait(0.5)

        # Final result with formula box
        final_tex = MathTex(
            r"= 1 - \frac{1}{n+1} \;\xrightarrow{n \to \infty}\; 1",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        final_boxed = self.ly.formula_box(final_tex)
        self.ly.safe_place(final_boxed, direction=DOWN, anchor=expansion, buff=0.5)
        self.play(Write(final_boxed), run_time=NORMAL)
        self.wait(1.0)

        # Tip
        tip = Text(
            "Tip: Write out the partial sum S_n first, then take the limit.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(tip, direction=DOWN, anchor=final_boxed)
        self.play(FadeIn(tip, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 7: Recap ─────────────────────────────────────────────
    def scene7_recap(self):
        self.ly.section_divider(7, "Summary")

        self.add_subcaption(
            "Today we learned what infinite series are, the geometric series formula, "
            "the divergence test, and telescoping series. "
            "Next time we will cover convergence tests in depth.",
            duration=14,
        )

        title = self.ly.title("What We Learned")

        items = [
            Text(
                "An infinite series = limit of partial sums",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            MathTex(
                r"\sum_{k=0}^{\infty} ar^k = \frac{a}{1-r}, \; |r|<1",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            Text(
                "Harmonic series diverges even though terms → 0",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Divergence test: if a_n does not → 0, series diverges",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Telescoping series cancel intermediate terms",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)

        play_outro(self, "Tests for Convergence", "Calculus II")
