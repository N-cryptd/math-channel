"""
Video 62: Power Series Solutions
Ordinary Differential Equations -- Video 9 of N

Covers: motivation when other methods fail, power series review,
index shifting technique, simplest example (y' = y recovers e^x),
Airy's equation (y'' - xy = 0), initial conditions, convergence,
applications.

Render draft:  manim -ql scripts/undergraduate/video-62-power-series-solutions.py Video62_PowerSeriesSolutions
Render final:  manim -qh scripts/undergraduate/video-62-power-series-solutions.py Video62_PowerSeriesSolutions
"""

from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video62_PowerSeriesSolutions(Scene):
    """Full video: Power Series Solutions for ODEs."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_review()
        self.scene3_simple_example()
        self.scene4_index_shifting()
        self.scene5_airy_equation()
        self.scene6_initial_conditions()
        self.scene7_summary()

    # -- Scene 1: Hook -- When Other Methods Fail --
    def scene1_hook(self):
        self.add_subcaption(
            "We have learned many techniques for solving differential "
            "equations: separation of variables, integrating factors, "
            "undetermined coefficients, variation of parameters. But "
            "consider this equation: y double prime minus x times y "
            "equals zero. None of our methods work here.",
            duration=28,
        )
        play_intro(self, "Power Series Solutions",
                   "Ordinary Differential Equations")

        title = self.ly.title("The Universal Method")

        methods = [
            Text("Separation, Linear, Undetermined Coefficients...",
                  font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Variation of Parameters", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(methods, start_from=title)
        self.wait(0.5)

        self.ly.clear()

        self.add_subcaption(
            "This is Airy's equation. The coefficient of y is not "
            "constant, it depends on x. The characteristic equation "
            "method fails. We need a completely different approach: "
            "express the solution as an infinite power series.",
            duration=24,
        )

        title2 = self.ly.title("The Problem")

        airy = MathTex(
            r"y''", r"-", r"x\,y", r"=", r"0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        airy[0].set_color(PRIMARY)
        airy[2].set_color(RED)
        airy[4].set_color(RED)
        self.ly.safe_place(airy, DOWN, anchor=title2, buff=0.5)
        self.play(Write(airy), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(airy), run_time=FAST)

        title3 = self.ly.title("The Idea")

        idea = MathTex(
            r"y", r"=", r"\sum_{n=0}^{\infty}",
            r"a_n\, x^n",
            font_size=HEADING_SIZE, color=WHITE,
        )
        idea[0].set_color(PRIMARY)
        idea[2].set_color(ACCENT)
        idea[3].set_color(ACCENT)
        self.ly.formula_box(idea, ACCENT)
        self.wait(2)

        self.ly.clear()

    # -- Scene 2: Power Series Review --
    def scene2_review(self):
        self.add_subcaption(
            "Let us quickly review power series. From our earlier "
            "videos, you already know that many functions can be "
            "expressed as infinite sums. The exponential, sine, "
            "cosine, and geometric series are all power series.",
            duration=24,
        )

        self.ly.section_divider(1, "Power Series Recap")
        self.wait(0.5)

        title = self.ly.title("General Form")

        series = MathTex(
            r"y", r"=", r"\sum_{n=0}^{\infty}",
            r"a_n\, x^n",
            r"= a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \cdots",
            font_size=HEADING_SIZE, color=WHITE,
        )
        series[0].set_color(PRIMARY)
        series[2].set_color(ACCENT)
        series[3].set_color(ACCENT)
        self.ly.safe_place(series, DOWN, anchor=title, buff=0.5)
        self.play(Write(series), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(series), run_time=FAST)

        self.add_subcaption(
            "To substitute into a differential equation, we need "
            "the derivatives. Differentiating term by term shifts "
            "the index. Watch carefully: y prime has the sum start "
            "at n equals 1, which we rewrite starting at n equals 0 "
            "by replacing n with n plus 1.",
            duration=28,
        )

        title2 = self.ly.title("Differentiating Shifts the Index")

        yp = MathTex(
            r"y'", r"=", r"\sum_{n=1}^{\infty}",
            r"n\,a_n\, x^{n-1}",
            r"=", r"\sum_{n=0}^{\infty}",
            r"(n{+}1)\,a_{n+1}\, x^n",
            font_size=HEADING_SIZE, color=WHITE,
        )
        yp[0].set_color(SECONDARY)
        yp[2].set_color(ACCENT)
        yp[3].set_color(ACCENT)
        yp[5].set_color(ACCENT)
        yp[6].set_color(SECONDARY)
        self.ly.safe_place(yp, DOWN, anchor=title2, buff=0.5)
        self.play(Write(yp), run_time=NORMAL)
        self.wait(1.5)

        self.play(FadeOut(yp), run_time=FAST)

        title3 = self.ly.title("Second Derivative")

        ypp = MathTex(
            r"y''", r"=", r"\sum_{n=0}^{\infty}",
            r"(n{+}2)(n{+}1)\,a_{n+2}\, x^n",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ypp[0].set_color(PRIMARY)
        ypp[2].set_color(ACCENT)
        ypp[3].set_color(PRIMARY)
        self.ly.safe_place(ypp, DOWN, anchor=title3, buff=0.5)
        self.play(Write(ypp), run_time=NORMAL)
        self.wait(1)

        self.ly.clear()

    # -- Scene 3: Simplest Example y' = y --
    def scene3_simple_example(self):
        self.add_subcaption(
            "Let us start with the simplest possible example: "
            "y prime equals y. We already know the answer is "
            "C times e to the x. But let us solve it using "
            "power series to see the method in action.",
            duration=20,
        )

        self.ly.section_divider(2, "Simplest Example: y' = y")
        self.wait(0.5)

        title = self.ly.title("The Equation")

        ode = MathTex(
            r"y'", r"=", r"y",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ode[0].set_color(RED)
        ode[2].set_color(PRIMARY)
        self.ly.safe_place(ode, DOWN, anchor=title, buff=0.5)
        self.play(Write(ode), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ode), run_time=FAST)

        self.add_subcaption(
            "Substitute y equals the sum and y prime equals the "
            "derivative sum. Set them equal. Since the series "
            "are equal, each coefficient must match. This gives "
            "us a recurrence relation: a sub n plus 1 equals "
            "a sub n divided by n plus 1.",
            duration=24,
        )

        title2 = self.ly.title("Matching Coefficients")

        sub = MathTex(
            r"\sum_{n=0}^{\infty}",
            r"(n{+}1)\,a_{n+1}\, x^n",
            r"=",
            r"\sum_{n=0}^{\infty}",
            r"a_n\, x^n",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sub[0].set_color(ACCENT)
        sub[1].set_color(SECONDARY)
        sub[3].set_color(ACCENT)
        sub[4].set_color(PRIMARY)
        self.ly.safe_place(sub, DOWN, anchor=title2, buff=0.5)
        self.play(Write(sub), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(sub), run_time=FAST)

        title3 = self.ly.title("Recurrence Relation")

        recur = MathTex(
            r"a_{n+1}", r"=", r"\frac{a_n}{n+1}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        recur[0].set_color(ACCENT)
        recur[2].set_color(ACCENT)
        self.ly.formula_box(recur, ACCENT)
        self.wait(2)

        self.ly.clear()

        self.add_subcaption(
            "Starting with a sub 0, we get a sub 1 equals a sub 0, "
            "a sub 2 equals a sub 0 over 2, a sub 3 equals a sub 0 "
            "over 6, and in general a sub n equals a sub 0 over "
            "n factorial. So the solution is y equals a sub 0 "
            "times the sum of x to the n over n factorial.",
            duration=28,
        )

        title4 = self.ly.title("Solving the Recurrence")

        sol = MathTex(
            r"a_n", r"=", r"\frac{a_0}{n!}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sol[0].set_color(ACCENT)
        sol[2].set_color(ACCENT)
        self.ly.safe_place(sol, DOWN, anchor=title4, buff=0.5)
        self.play(Write(sol), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(sol), run_time=FAST)

        title5 = self.ly.title("The Solution")

        result = MathTex(
            r"y", r"=", r"a_0", r"\sum_{n=0}^{\infty}",
            r"\frac{x^n}{n!}",
            r"=", r"a_0\, e^x",
            font_size=HEADING_SIZE, color=WHITE,
        )
        result[0].set_color(PRIMARY)
        result[2].set_color(ACCENT)
        result[3].set_color(ACCENT)
        result[4].set_color(ACCENT)
        result[6].set_color(SECONDARY)
        self.ly.formula_box(result, SECONDARY)
        self.wait(2)

        self.ly.clear()

    # -- Scene 4: Index Shifting Technique --
    def scene4_index_shifting(self):
        self.add_subcaption(
            "Index shifting is the core computational skill. When we "
            "substitute series into a differential equation, different "
            "terms may have different powers of x. We need all sums "
            "to have the same power before we can match coefficients. "
            "We do this by shifting the summation index.",
            duration=28,
        )

        self.ly.section_divider(3, "The Art of Index Shifting")
        self.wait(0.5)

        title = self.ly.title("The General Pattern")

        before = MathTex(
            r"\sum_{n=k}^{\infty}", r"c_n\, x^{n}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        before[0].set_color(ACCENT)
        before[1].set_color(PRIMARY)
        self.ly.safe_place(before, DOWN, anchor=title, buff=0.5)
        self.play(Write(before), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(before), run_time=FAST)

        self.add_subcaption(
            "To shift: let m equal n minus k. Then n equals m "
            "plus k. Replace every n in the sum. The new sum "
            "starts at m equals zero and the power becomes x "
            "to the m plus k. This aligns all our sums so "
            "we can equate coefficients term by term.",
            duration=24,
        )

        title2 = self.ly.title("After Shifting")

        arrow = MathTex(
            r"\Downarrow", font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(arrow, DOWN, anchor=title2, buff=0.3)
        self.play(Write(arrow), run_time=FAST)
        self.wait(0.3)

        after = MathTex(
            r"=", r"\sum_{m=0}^{\infty}",
            r"c_{m+k}\, x^{m+k}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        after[0].set_color(ACCENT)
        after[1].set_color(ACCENT)
        after[2].set_color(PRIMARY)
        self.ly.safe_place(after, DOWN, anchor=arrow, buff=0.3)
        self.play(Write(after), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

        title3 = self.ly.title("Key Rule")

        rule = Text(
            "All sums must have the SAME power of x before matching.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(rule, DOWN, anchor=title3, buff=0.5)
        self.play(FadeIn(rule, shift=LEFT * 0.2), run_time=NORMAL)
        self.wait(1)

        self.ly.clear()

    # -- Scene 5: Airy's Equation --
    def scene5_airy_equation(self):
        self.add_subcaption(
            "Now let us solve Airy's equation: y double prime minus "
            "x y equals zero. This appears in optics and quantum "
            "mechanics. The variable coefficient x makes our "
            "standard methods impossible, but power series "
            "handle it naturally.",
            duration=24,
        )

        self.ly.section_divider(4, "Airy's Equation: y'' - xy = 0")
        self.wait(0.5)

        title = self.ly.title("The Equation")

        airy = MathTex(
            r"y''", r"-", r"x\,y", r"=", r"0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        airy[0].set_color(PRIMARY)
        airy[2].set_color(RED)
        airy[4].set_color(RED)
        self.ly.safe_place(airy, DOWN, anchor=title, buff=0.5)
        self.play(Write(airy), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(airy), run_time=FAST)

        self.add_subcaption(
            "Substituting y double prime and x y as series and "
            "shifting indices to align the powers of x, we get "
            "the recurrence relation: a sub n plus 2 equals "
            "a sub n minus 1, divided by the quantity n plus 2 "
            "times n plus 1.",
            duration=24,
        )

        title2 = self.ly.title("The Recurrence Relation")

        recur = MathTex(
            r"a_{n+2}", r"=", r"\frac{a_{n-1}}{(n+2)(n+1)}",
            r"\quad \text{for } n \ge 1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        recur[0].set_color(ACCENT)
        recur[2].set_color(ACCENT)
        recur[3].set_color(DIM)
        self.ly.formula_box(recur, ACCENT)
        self.wait(2)

        self.ly.clear()

        self.add_subcaption(
            "Notice: the recurrence skips every two indices. This "
            "splits the solution into an even series depending "
            "on a sub 0, and an odd series depending on a sub 1. "
            "These are two linearly independent solutions.",
            duration=20,
        )

        title3 = self.ly.title("Two Independent Solutions")

        even_label = Text(
            "Even series (depends on a_0):",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(even_label, DOWN, anchor=title3, buff=0.4)
        self.play(FadeIn(even_label, shift=LEFT * 0.2), run_time=NORMAL)
        self.wait(0.5)

        even = MathTex(
            r"y_1", r"= a_0\!\left(1",
            r"+ \frac{x^3}{6}",
            r"+ \frac{x^6}{180}",
            r"+ \cdots\right)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        even[0].set_color(PRIMARY)
        even[2].set_color(SECONDARY)
        even[3].set_color(SECONDARY)
        self.ly.safe_place(even, DOWN, anchor=even_label, buff=0.3)
        self.play(Write(even), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(even), FadeOut(even_label), run_time=FAST)

        odd_label = Text(
            "Odd series (depends on a_1):",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(odd_label, DOWN, anchor=title3, buff=0.4)
        self.play(FadeIn(odd_label, shift=LEFT * 0.2), run_time=NORMAL)
        self.wait(0.5)

        odd = MathTex(
            r"y_2", r"= a_1\!\left(x",
            r"+ \frac{x^4}{12}",
            r"+ \frac{x^7}{504}",
            r"+ \cdots\right)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        odd[0].set_color(SECONDARY)
        odd[2].set_color(PRIMARY)
        odd[3].set_color(PRIMARY)
        self.ly.safe_place(odd, DOWN, anchor=odd_label, buff=0.3)
        self.play(Write(odd), run_time=NORMAL)
        self.wait(1)

        self.ly.clear()

        self.add_subcaption(
            "The general solution is y equals a sub 0 times the "
            "even series plus a sub 1 times the odd series. "
            "These series cannot be expressed in terms of "
            "elementary functions. They define entirely new "
            "functions called Airy functions.",
            duration=24,
        )

        title4 = self.ly.title("General Solution")

        general = MathTex(
            r"y", r"=", r"a_0\, y_1(x)", r"+", r"a_1\, y_2(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        general[0].set_color(PRIMARY)
        general[2].set_color(PRIMARY)
        general[4].set_color(SECONDARY)
        self.ly.formula_box(general, PRIMARY)
        self.wait(2)

        self.ly.clear()

    # -- Scene 6: Initial Conditions and Convergence --
    def scene6_initial_conditions(self):
        self.add_subcaption(
            "How do initial conditions work with power series? "
            "Since y of zero equals a sub 0 plus all the terms "
            "with x, evaluating at x equals zero gives y of zero "
            "equals a sub 0. Similarly, y prime of zero equals "
            "a sub 1.",
            duration=24,
        )

        self.ly.section_divider(5, "Initial Conditions")
        self.wait(0.5)

        title = self.ly.title("Evaluating at x = 0")

        ic1 = MathTex(
            r"y(0)", r"=", r"a_0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ic1[0].set_color(PRIMARY)
        ic1[2].set_color(ACCENT)
        self.ly.safe_place(ic1, DOWN, anchor=title, buff=0.5)
        self.play(Write(ic1), run_time=NORMAL)
        self.wait(0.5)

        ic2 = MathTex(
            r"y'(0)", r"=", r"a_1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ic2[0].set_color(SECONDARY)
        ic2[2].set_color(ACCENT)
        self.ly.safe_place(ic2, DOWN, anchor=ic1, buff=0.3)
        self.play(Write(ic2), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ic1), FadeOut(ic2), run_time=FAST)

        self.add_subcaption(
            "This is really just Taylor's theorem applied to "
            "differential equations. The coefficients a sub n "
            "are proportional to the n-th derivative of y "
            "evaluated at zero, divided by n factorial. "
            "The series converges within its radius of "
            "convergence, which depends on the coefficients "
            "of the differential equation.",
            duration=28,
        )

        title2 = self.ly.title("Connection to Taylor Series")

        items = [
            Text("a_n = y^{(n)}(0) / n!  (Taylor coefficients)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Convergence within radius of convergence",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Power series solutions ARE Taylor expansions",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(1)

        self.ly.clear()

    # -- Scene 7: Summary + Outro --
    def scene7_summary(self):
        self.add_subcaption(
            "To summarize: power series solutions expand the "
            "universe of solvable differential equations. When "
            "standard methods fail, assume a series solution, "
            "substitute into the equation, shift indices to "
            "align powers, match coefficients, and solve the "
            "recurrence relation.",
            duration=28,
        )

        title = self.ly.title("Summary")

        items = [
            Text("Works when other methods fail (variable coefficients)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Assume y = sum a_n x^n, substitute and match",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Index shifting aligns all sums to same power of x",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Recurrence relation determines all coefficients",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("a_0 = y(0) and a_1 = y'(0) from initial conditions",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()

        self.add_subcaption(
            "Power series solutions appear everywhere: Airy's "
            "equation in optics, Bessel's equation in cylindrical "
            "wave propagation, and Hermite polynomials in quantum "
            "mechanics. In the next video we explore Laplace "
            "transforms, yet another powerful tool for solving "
            "differential equations.",
            duration=28,
        )

        play_outro(
            self,
            next_video="Laplace Transforms",
            next_playlist="Ordinary Differential Equations",
        )
