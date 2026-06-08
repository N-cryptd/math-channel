"""
Video 20: Power Series & Radius of Convergence
Covers: definition of power series, interval of convergence, radius of convergence,
center of convergence, computing R via ratio/root test.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, formula_box, proper narration timing.

Render draft:  manim -ql scripts/pre-university/video-20-power-series.py Video20_PowerSeries
Render final:  manim -qh scripts/pre-university/video-20-power-series.py Video20_PowerSeries

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


class Video20_PowerSeries(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_radius_of_convergence()
        self.scene4_radius_examples()
        self.scene5_interval_of_convergence()
        self.scene6_operations()
        self.scene7_recap()

    # ── Scene 1: Hook — "Can we represent functions as polynomials?" ─
    def scene1_hook(self):
        self.add_subcaption(
            "What if a series has x as a variable? "
            "We get a power series — a function defined by infinite sums.",
            duration=10,
        )
        play_intro(self, "Power Series", "Calculus II")

        # Motivating question
        question = Text(
            "Can we represent functions as infinite polynomials?",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(question)
        self.play(Write(question), run_time=NORMAL)
        self.wait(0.5)

        # General form
        power = MathTex(
            r"f(x) = \sum_{n=0}^{\infty} c_n (x - a)^n",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(power, direction=DOWN, anchor=question)
        self.play(Write(power), run_time=NORMAL)
        self.wait(0.5)

        # Expansion
        expansion = MathTex(
            r"= c_0 + c_1(x-a) + c_2(x-a)^2 + c_3(x-a)^3 + \cdots",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(expansion, direction=DOWN, anchor=power)
        self.play(Write(expansion), run_time=NORMAL)
        self.wait(0.5)

        # Famous example
        sin_series = MathTex(
            r"\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(sin_series, direction=DOWN, anchor=expansion)
        self.play(Write(sin_series), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 2: Definition ────────────────────────────────────────
    def scene2_definition(self):
        self.ly.section_divider(1, "Definition")

        self.add_subcaption(
            "A power series centered at a is an infinite polynomial "
            "in powers of x minus a. "
            "It may converge for some x values and diverge for others.",
            duration=14,
        )

        title = self.ly.title("Power Series Definition")

        # Formula box
        defn_tex = MathTex(
            r"\sum_{n=0}^{\infty} c_n (x - a)^n "
            r"= c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots",
            font_size=HEADING_SIZE, color=WHITE,
        )
        defn_boxed = self.ly.formula_box(defn_tex)
        self.ly.safe_place(defn_boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(defn_boxed), run_time=SLOW)
        self.wait(1.0)

        # Labels — progressive
        label_a = Text(
            "a = center of the series",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(label_a, direction=DOWN, anchor=defn_boxed)
        self.play(FadeIn(label_a, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        label_c = Text(
            "c_n = coefficients",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(label_c, direction=DOWN, anchor=label_a)
        self.play(FadeIn(label_c, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Key fact
        key = Text(
            "The series ALWAYS converges at x = a.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=label_c)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 3: Radius of Convergence (visual) ────────────────────
    def scene3_radius_of_convergence(self):
        self.ly.section_divider(2, "Radius of Convergence")

        self.add_subcaption(
            "Every power series has a radius of convergence R. "
            "Inside the radius it converges, outside it diverges.",
            duration=10,
        )

        title = self.ly.title("Radius of Convergence")

        # Number line
        ax = NumberLine(
            x_range=[-3, 3, 1], length=9,
            color=DIM, include_numbers=True,
        )
        self.ly.center_in_content(ax)
        self.play(Create(ax), run_time=NORMAL)

        # Center dot
        center_dot = Dot(ax.n2p(0), color=PRIMARY, radius=0.1)
        center_label = Text("a", font_size=HEADING_SIZE, color=PRIMARY, font=MONO)
        center_label.next_to(center_dot, DOWN, buff=0.2)
        self.play(FadeIn(center_dot), Write(center_label), run_time=FAST)

        # Convergence region
        conv_region = Rectangle(
            width=4, height=0.5, fill_color=SECONDARY,
            fill_opacity=0.25, stroke_color=SECONDARY, stroke_width=2,
        )
        conv_region.move_to(ax.n2p(0))
        conv_label = Text("Converges", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)
        conv_label.next_to(conv_region, UP, buff=0.1)
        self.play(FadeIn(conv_region), FadeIn(conv_label), run_time=FAST)

        # Divergence regions
        div_l = Text("Diverges", font_size=LABEL_SIZE, color=RED, font=SANS)
        div_l.move_to(ax.n2p(-2.2) + UP * 0.6)
        div_r = Text("Diverges", font_size=LABEL_SIZE, color=RED, font=SANS)
        div_r.move_to(ax.n2p(2.2) + UP * 0.6)
        self.play(FadeIn(div_l), FadeIn(div_r), run_time=FAST)

        # Boundary labels
        r_label = Text("test!", font_size=LABEL_SIZE, color=ACCENT, font=MONO, weight=BOLD)
        r_label.next_to(ax.n2p(2), DOWN, buff=0.3)
        r_label_l = Text("test!", font_size=LABEL_SIZE, color=ACCENT, font=MONO, weight=BOLD)
        r_label_l.next_to(ax.n2p(-2), DOWN, buff=0.3)
        self.play(FadeIn(r_label), FadeIn(r_label_l), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

        # R formula and cases
        self.add_subcaption(
            "We compute R using the ratio test. "
            "R equals one over rho, where rho is the limit of the ratio of consecutive coefficients.",
            duration=12,
        )
        title2 = self.ly.title("Computing R")

        formula_tex = MathTex(
            r"R = \frac{1}{\rho}, \quad "
            r"\rho = \lim_{n \to \infty} \left|\frac{c_{n+1}}{c_n}\right|",
            font_size=BODY_SIZE, color=WHITE,
        )
        formula_boxed = self.ly.formula_box(formula_tex)
        self.ly.safe_place(formula_boxed, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(formula_boxed), run_time=SLOW)
        self.wait(1.0)

        c1 = Text(
            "R = 0: converges only at x = a",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(c1, direction=DOWN, anchor=formula_boxed)
        self.play(FadeIn(c1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        c2 = Text(
            "R = infinity: converges for all x",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(c2, direction=DOWN, anchor=c1)
        self.play(FadeIn(c2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        c3 = Text(
            "0 < R < infinity: determine the interval",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(c3, direction=DOWN, anchor=c2)
        self.play(FadeIn(c3, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 4: Radius Examples ────────────────────────────────────
    def scene4_radius_examples(self):
        self.ly.section_divider(3, "Examples")

        self.add_subcaption(
            "Example 1: the exponential series converges for all x "
            "because the ratio limit is zero, giving infinite radius.",
            duration=10,
        )

        title = self.ly.title("Example 1: e^x Series")

        ex1_series = MathTex(
            r"\sum_{n=0}^{\infty} \frac{x^n}{n!}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex1_series, direction=DOWN, anchor=title)
        self.play(Write(ex1_series), run_time=NORMAL)
        self.wait(0.5)

        ex1_ratio = MathTex(
            r"\rho = \lim \left|\frac{x^{n+1}/(n+1)!}{x^n/n!}\right| "
            r"= \lim \frac{|x|}{n+1} = 0",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex1_ratio, direction=DOWN, anchor=ex1_series)
        self.play(Write(ex1_ratio), run_time=NORMAL)
        self.wait(0.5)

        ex1_result = Text(
            "R = infinity: converges for ALL x!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(ex1_result, direction=DOWN, anchor=ex1_ratio)
        self.play(FadeIn(ex1_result, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Example 2
        self.add_subcaption(
            "Example 2: this series centered at 2 has radius 1. "
            "We must test the endpoints x equals 1 and x equals 3.",
            duration=12,
        )
        title2 = self.ly.title("Example 2: Centered at 2")

        ex2_series = MathTex(
            r"\sum_{n=1}^{\infty} \frac{(x-2)^n}{n}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex2_series, direction=DOWN, anchor=title2)
        self.play(Write(ex2_series), run_time=NORMAL)
        self.wait(0.5)

        ex2_ratio = MathTex(
            r"\rho = \lim \frac{n}{n+1}|x-2| = |x-2|",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex2_ratio, direction=DOWN, anchor=ex2_series)
        self.play(Write(ex2_ratio), run_time=NORMAL)
        self.wait(0.5)

        ex2_result = Text(
            "R = 1, centered at a = 2. Test endpoints x = 1 and x = 3!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(ex2_result, direction=DOWN, anchor=ex2_ratio)
        self.play(FadeIn(ex2_result, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 5: Interval of Convergence ────────────────────────────
    def scene5_interval_of_convergence(self):
        self.ly.section_divider(4, "Interval of Convergence")

        self.add_subcaption(
            "The interval of convergence is the set of x values where "
            "the series converges, including endpoints that pass individual tests.",
            duration=12,
        )

        title = self.ly.title("Three Cases")

        # R = 0
        c1 = Text(
            "R = 0: interval = {a} (single point)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(c1, direction=DOWN, anchor=title)
        self.play(FadeIn(c1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        # R = infinity
        c2 = Text(
            "R = infinity: interval = (-infinity, infinity)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(c2, direction=DOWN, anchor=c1)
        self.play(FadeIn(c2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        # Finite R
        c3 = Text(
            "0 < R < infinity: interval = (a-R, a+R)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(c3, direction=DOWN, anchor=c2)
        self.play(FadeIn(c3, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Important note
        note = Text(
            "Endpoints MUST be tested individually!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=c3)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 6: Operations on Power Series ────────────────────────
    def scene6_operations(self):
        self.ly.section_divider(5, "Operations on Power Series")

        self.add_subcaption(
            "Power series can be added, differentiated, and integrated "
            "term by term within their radius of convergence.",
            duration=10,
        )

        title = self.ly.title("Term-by-Term Operations")

        # Addition
        add_title = Text(
            "Addition/Subtraction:",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(add_title, direction=DOWN, anchor=title)
        self.play(Write(add_title), run_time=FAST)

        add_tex = MathTex(
            r"\sum a_n x^n + \sum b_n x^n = \sum (a_n + b_n) x^n",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(add_tex, direction=DOWN, anchor=add_title)
        self.play(Write(add_tex), run_time=FAST)
        self.wait(0.5)
        self.ly.clear()

        # Differentiation
        diff_title = Text(
            "Differentiation (within R):",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(diff_title, direction=DOWN, anchor=title)
        self.play(Write(diff_title), run_time=FAST)

        diff_tex = MathTex(
            r"\frac{d}{dx}\sum c_n (x-a)^n "
            r"= \sum n\, c_n (x-a)^{n-1}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(diff_tex, direction=DOWN, anchor=diff_title)
        self.play(Write(diff_tex), run_time=FAST)
        self.wait(0.5)
        self.ly.clear()

        # Integration
        int_title = Text(
            "Integration (within R):",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(int_title, direction=DOWN, anchor=title)
        self.play(Write(int_title), run_time=FAST)

        int_tex = MathTex(
            r"\int \sum c_n (x-a)^n\,dx "
            r"= C + \sum \frac{c_n}{n+1}(x-a)^{n+1}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(int_tex, direction=DOWN, anchor=int_title)
        self.play(Write(int_tex), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 7: Recap ────────────────────────────────────────────
    def scene7_recap(self):
        self.ly.section_divider(6, "Summary")

        self.add_subcaption(
            "Power series turn infinite sums into functions. "
            "Next: Taylor and Maclaurin series — how to find the coefficients.",
            duration=10,
        )

        title = self.ly.title("What We Learned")

        items = [
            Text(
                "Power series: infinite polynomial centered at a",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Radius R: converges inside, diverges outside",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Use ratio test to find R",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Test endpoints individually!",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Can differentiate and integrate term by term",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)

        play_outro(self, "Taylor & Maclaurin Series", "Calculus II")
