"""
Video 21: Taylor & Maclaurin Series
Covers: Taylor polynomial, Taylor series formula, Maclaurin series,
common Maclaurin series (e^x, sin x, cos x, ln(1+x), 1/(1-x)),
Taylor's theorem with remainder, Taylor's inequality.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, formula_box, proper narration timing.

Render draft:  manim -ql scripts/pre-university/video-21-taylor-maclaurin.py Video21_TaylorMaclaurin
Render final:  manim -qh scripts/pre-university/video-21-taylor-maclaurin.py Video21_TaylorMaclaurin

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


class Video21_TaylorMaclaurin(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_taylor_formula()
        self.scene3_terms_intuition()
        self.scene4_maclaurin_series()
        self.scene5_common_series()
        self.scene6_visual()
        self.scene7_remainder()
        self.scene8_inequality()
        self.scene9_recap()

    # ── Scene 1: Hook — "Polynomials approximating e^x" ─────────────
    def scene1_hook(self):
        self.add_subcaption(
            "How can we approximate any smooth function using polynomials? "
            "Taylor series give us the answer.",
            duration=10,
        )
        play_intro(self, "Taylor & Maclaurin Series", "Calculus II")

        question = Text(
            "What polynomial best approximates e^x near x = 0?",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(question)
        self.play(Write(question), run_time=NORMAL)
        self.wait(0.5)

        # Progressive buildup
        p0 = MathTex(r"P_0(x) = 1", font_size=BODY_SIZE, color=DIM)
        self.ly.safe_place(p0, direction=DOWN, anchor=question)
        self.play(Write(p0), run_time=FAST)
        self.wait(0.2)

        p1 = MathTex(r"P_1(x) = 1 + x", font_size=BODY_SIZE, color=SECONDARY)
        self.ly.safe_place(p1, direction=DOWN, anchor=p0)
        self.play(Write(p1), run_time=FAST)
        self.wait(0.2)

        p2 = MathTex(r"P_2(x) = 1 + x + \frac{x^2}{2}", font_size=BODY_SIZE, color=PRIMARY)
        self.ly.safe_place(p2, direction=DOWN, anchor=p1)
        self.play(Write(p2), run_time=FAST)
        self.wait(0.5)

        result = MathTex(r"\cdots = e^x", font_size=HEADING_SIZE, color=ACCENT)
        self.ly.safe_place(result, direction=DOWN, anchor=p2)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 2: Taylor Series Formula ──────────────────────────────
    def scene2_taylor_formula(self):
        self.ly.section_divider(1, "The Taylor Series")

        self.add_subcaption(
            "The Taylor series of a function centered at a "
            "uses derivatives to match the function's behavior.",
            duration=10,
        )

        title = self.ly.title("Taylor Series Formula")

        # THE formula — formula box
        formula_tex = MathTex(
            r"f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        formula_boxed = self.ly.formula_box(formula_tex)
        self.ly.safe_place(formula_boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(formula_boxed), run_time=SLOW)
        self.wait(1.0)

        # Expansion
        expansion = MathTex(
            r"= f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(expansion, direction=DOWN, anchor=formula_boxed)
        self.play(Write(expansion), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 3: Terms Intuition ───────────────────────────────────
    def scene3_terms_intuition(self):
        self.ly.section_divider(2, "What Each Term Does")

        self.add_subcaption(
            "Each term adds one more derivative's worth of information. "
            "The zeroth term matches the value, the first matches the slope, and so on.",
            duration=14,
        )

        title = self.ly.title("Term-by-Term Intuition")

        items = [
            Text(
                "0th term: matches f(a) — the value",
                font_size=BODY_SIZE, color=DIM, font=SANS,
            ),
            Text(
                "1st term: matches f'(a) — the slope",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "2nd term: matches f''(a) — the concavity",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "nth term: matches the nth derivative",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)

        key = Text(
            "More terms = better approximation!",
            font_size=BODY_SIZE, color=WHITE, font=SANS, weight=BOLD,
        )
        # Place below the last visible item
        visible = self.mobjects
        last_item = None
        for m in reversed(visible):
            if m not in [self._bg_dots, self._bg_gradient] and hasattr(m, 'get_bottom'):
                last_item = m
                break
        if last_item is not None:
            self.ly.safe_place(key, direction=DOWN, anchor=last_item)
        else:
            self.ly.safe_place(key, direction=DOWN, anchor=title)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 4: Maclaurin Series ────────────────────────────────────
    def scene4_maclaurin_series(self):
        self.ly.section_divider(3, "Maclaurin Series")

        self.add_subcaption(
            "A Maclaurin series is simply a Taylor series centered at zero. "
            "It is the most common special case.",
            duration=10,
        )

        title = self.ly.title("Maclaurin Series (a = 0)")

        # Formula box
        formula_tex = MathTex(
            r"f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_boxed = self.ly.formula_box(formula_tex)
        self.ly.safe_place(formula_boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(formula_boxed), run_time=SLOW)
        self.wait(1.0)

        note = Text(
            "Same formula, just plug in a = 0.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=formula_boxed)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.0)
        self.ly.clear()

        # Steps to compute
        self.add_subcaption(
            "To find a Maclaurin series, compute derivatives at zero, "
            "divide by n factorial, and write the sum.",
            duration=10,
        )
        title2 = self.ly.title("How to Compute")

        items = [
            Text(
                "1. Compute f(0), f'(0), f''(0), ...",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. Divide each by n!",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "3. Write the infinite sum",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 5: Common Maclaurin Series ───────────────────────────
    def scene5_common_series(self):
        self.ly.section_divider(4, "Essential Series")

        self.add_subcaption(
            "These five Maclaurin series are so important that you should memorize them.",
            duration=8,
        )

        title = self.ly.title("Memorize These!")

        items = [
            MathTex(
                r"e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"\sin x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"\cos x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"\ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1} x^n}{n}",
                font_size=BODY_SIZE, color=SECONDARY,
            ),
            MathTex(
                r"\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n",
                font_size=BODY_SIZE, color=SECONDARY,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 6: Visual — Taylor Polynomials ───────────────────────
    def scene6_visual(self):
        self.ly.section_divider(5, "Taylor Polynomials Visualized")

        self.add_subcaption(
            "Higher-degree Taylor polynomials approximate the function better "
            "over a wider range. This is the beauty of Taylor series.",
            duration=12,
        )

        title = self.ly.title("Approximating e^x")

        # Graph
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-2, 5, 1],
            x_length=7, y_length=4,
            color=DIM, axis_config={"include_numbers": True},
        )
        self.ly.safe_place(axes, direction=DOWN, anchor=title)
        self.play(Create(axes), run_time=FAST)

        # e^x
        exp_graph = axes.plot(lambda x: np.exp(x), color=WHITE, x_range=[-3, 1.6])
        exp_label = MathTex(r"e^x", font_size=BODY_SIZE, color=WHITE)
        exp_label.next_to(exp_graph, RIGHT, buff=0.2)
        self.play(Create(exp_graph), Write(exp_label), run_time=NORMAL)

        # P_1
        p1 = axes.plot(lambda x: 1 + x, color=SECONDARY, x_range=[-3, 3])
        p1_label = MathTex(r"P_1", font_size=LABEL_SIZE, color=SECONDARY)
        p1_label.next_to(p1, RIGHT, buff=0.1)
        self.play(Create(p1), Write(p1_label), run_time=FAST)
        self.wait(0.3)

        # P_2
        p2 = axes.plot(lambda x: 1 + x + x**2 / 2, color=PRIMARY, x_range=[-3, 3])
        p2_label = MathTex(r"P_2", font_size=LABEL_SIZE, color=PRIMARY)
        p2_label.next_to(p2, RIGHT, buff=0.1)
        self.play(Create(p2), Write(p2_label), run_time=FAST)
        self.wait(0.3)

        # P_4
        p4 = axes.plot(
            lambda x: 1 + x + x**2/2 + x**3/6 + x**4/24,
            color=ACCENT, x_range=[-3, 3],
        )
        p4_label = MathTex(r"P_4", font_size=LABEL_SIZE, color=ACCENT)
        p4_label.next_to(p4, RIGHT, buff=0.1)
        self.play(Create(p4), Write(p4_label), run_time=FAST)
        self.wait(1.0)

        insight = Text(
            "More terms = better approximation over a wider range.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=axes)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 7: Taylor's Remainder ──────────────────────────────────
    def scene7_remainder(self):
        self.ly.section_divider(6, "Taylor's Theorem")

        self.add_subcaption(
            "Taylor's theorem tells us the error when using a Taylor polynomial. "
            "This error term is called the remainder.",
            duration=12,
        )

        title = self.ly.title("Taylor's Remainder")

        # Formula box
        formula_tex = MathTex(
            r"R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_boxed = self.ly.formula_box(formula_tex)
        self.ly.safe_place(formula_boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(formula_boxed), run_time=SLOW)
        self.wait(1.0)

        # Key notes
        note1 = Text(
            "c is some number between a and x",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note1, direction=DOWN, anchor=formula_boxed)
        self.play(FadeIn(note1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        note2 = Text(
            "R_n(x) = f(x) - P_n(x) — the exact error",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(note2, direction=DOWN, anchor=note1)
        self.play(FadeIn(note2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        note3 = Text(
            "If lim R_n(x) = 0, the series equals f(x)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note3, direction=DOWN, anchor=note2)
        self.play(FadeIn(note3, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 8: Taylor's Inequality ──────────────────────────────
    def scene8_inequality(self):
        self.ly.section_divider(7, "Taylor's Inequality")

        self.add_subcaption(
            "Taylor's inequality gives a practical bound on the error "
            "using the maximum of the next derivative.",
            duration=10,
        )

        title = self.ly.title("Bounding the Error")

        # Inequality
        ineq_tex = MathTex(
            r"|R_n(x)| \leq \frac{M}{(n+1)!}|x-a|^{n+1}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ineq_boxed = self.ly.formula_box(ineq_tex)
        self.ly.safe_place(ineq_boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(ineq_boxed), run_time=SLOW)
        self.wait(1.0)

        note = Text(
            "M = max of |f^(n+1)(z)| on the interval between a and x",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=ineq_boxed)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 9: Recap ──────────────────────────────────────────────
    def scene9_recap(self):
        self.ly.section_divider(8, "Summary")

        self.add_subcaption(
            "Taylor and Maclaurin series let us represent smooth functions "
            "as infinite polynomials. Next: parametric equations.",
            duration=10,
        )

        title = self.ly.title("What We Learned")

        items = [
            Text(
                "Taylor series: function as infinite polynomial",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Maclaurin = Taylor centered at 0",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            MathTex(
                r"f(x) = \sum \frac{f^{(n)}(a)}{n!}(x-a)^n",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            Text(
                "5 essential series to memorize",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Remainder term bounds the approximation error",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)

        play_outro(self, "Parametric Equations", "Calculus II")
