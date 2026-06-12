"""
Video 61: Variation of Parameters
Ordinary Differential Equations -- Video 7 of N

Covers: motivation when undetermined coefficients fails, key idea of
varying constants to functions, derivation of the variation of parameters
formula, the Wronskian, worked example y'' + y = sec(x), comparison with
undetermined coefficients.

Render draft:  manim -ql scripts/undergraduate/video-61-variation-of-parameters.py Video61_VariationOfParameters
Render final:  manim -qh scripts/undergraduate/video-61-variation-of-parameters.py Video61_VariationOfParameters
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


class Video61_VariationOfParameters(Scene):
    """Full video: Variation of Parameters for second-order linear ODEs."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_idea()
        self.scene3_derivation()
        self.scene4_wronskian()
        self.scene5_example()
        self.scene6_comparison()
        self.scene7_summary()

    # ── Scene 1: Hook — When Undetermined Coefficients Fails ─────
    def scene1_hook(self):
        self.add_subcaption(
            "Last time we used undetermined coefficients: guess the form "
            "of the particular solution based on the forcing function. "
            "But what if the forcing function is the natural log of x? "
            "Or the tangent of x? There is no standard guess for those.",
            duration=24,
        )
        play_intro(self, "Variation of Parameters",
                   "Ordinary Differential Equations")

        title = self.ly.title("The Limit of Guessing")

        ode = MathTex(
            r"a\,y''", r"+", r"b\,y'", r"+", r"c\,y", r"=", r"f(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ode[0].set_color(PRIMARY)
        ode[2].set_color(SECONDARY)
        ode[4].set_color(ACCENT)
        ode[6].set_color(RED)
        self.ly.safe_place(ode, DOWN, anchor=title, buff=0.5)
        self.play(Write(ode), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ode), run_time=FAST)

        self.add_subcaption(
            "We need a method that works for any continuous forcing "
            "function, not just polynomials, exponentials, and "
            "trigonometric functions. That method is variation of "
            "parameters.",
            duration=20,
        )

        title2 = self.ly.title("We Need a General Method")

        items = [
            Text("Undetermined coefficients: limited to specific f(x)", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Variation of parameters: works for ANY f(x)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(1)

        self.ly.clear()

    # ── Scene 2: The Key Idea ───────────────────────────────────
    def scene2_idea(self):
        self.add_subcaption(
            "Recall the complementary solution has the form C1 times "
            "y1 plus C2 times y2, where C1 and C2 are constants. "
            "The brilliant idea is to replace those constants with "
            "functions of x. Let u1 of x replace C1, and u2 of x "
            "replace C2.",
            duration=24,
        )

        self.ly.section_divider(1, "The Key Insight")
        self.wait(0.5)

        title = self.ly.title("Vary the Constants")

        yc = MathTex(
            r"y_c", r"=", r"C_1", r"\cdot", r"y_1",
            r"+", r"C_2", r"\cdot", r"y_2",
            font_size=HEADING_SIZE, color=WHITE,
        )
        yc[0].set_color(PRIMARY)
        yc[2].set_color(PRIMARY)
        yc[6].set_color(PRIMARY)
        self.ly.safe_place(yc, DOWN, anchor=title, buff=0.5)
        self.play(Write(yc), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(yc), run_time=FAST)

        self.add_subcaption(
            "Now the particular solution becomes u1 of x times y1 "
            "plus u2 of x times y2. We just need to find u1 and u2.",
            duration=16,
        )

        yp = MathTex(
            r"y_p", r"=", r"u_1(x)", r"\cdot", r"y_1",
            r"+", r"u_2(x)", r"\cdot", r"y_2",
            font_size=HEADING_SIZE, color=WHITE,
        )
        yp[0].set_color(ACCENT)
        yp[2].set_color(ACCENT)
        yp[6].set_color(ACCENT)
        self.ly.safe_place(yp, DOWN, anchor=title, buff=0.5)
        self.play(Write(yp), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(yp), run_time=FAST)

        self.add_subcaption(
            "We have two unknown functions but only one equation, "
            "so we get to choose a second condition. We impose "
            "u1 prime y1 plus u2 prime y2 equals zero. This "
            "simplifies the derivatives enormously.",
            duration=20,
        )

        constraint = MathTex(
            r"u_1'\,y_1", r"+", r"u_2'\,y_2", r"=", r"0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        constraint[0].set_color(SECONDARY)
        constraint[2].set_color(SECONDARY)
        self.ly.formula_box(constraint, SECONDARY)
        self.wait(2)

        self.ly.clear()

    # ── Scene 3: Derivation ─────────────────────────────────────
    def scene3_derivation(self):
        self.add_subcaption(
            "Let us derive the formulas. Differentiate y p using the "
            "product rule. Because of our constraint, the terms with "
            "u1 prime and u2 prime cancel, leaving only u1 y1 prime "
            "plus u2 y2 prime.",
            duration=20,
        )

        self.ly.section_divider(2, "Deriving the Formulas")
        self.wait(0.5)

        title = self.ly.title("First Derivative")

        yp_prime = MathTex(
            r"y_p'", r"=", r"u_1\,y_1'", r"+", r"u_2\,y_2'",
            font_size=HEADING_SIZE, color=WHITE,
        )
        yp_prime[0].set_color(ACCENT)
        yp_prime[2].set_color(ACCENT)
        yp_prime[4].set_color(ACCENT)
        self.ly.safe_place(yp_prime, DOWN, anchor=title, buff=0.5)
        self.play(Write(yp_prime), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(yp_prime), run_time=FAST)

        self.add_subcaption(
            "Differentiate again to get y p double prime, substitute "
            "into the original ODE, and use the constraint equation. "
            "After simplification, we get a system of two linear "
            "equations for u1 prime and u2 prime.",
            duration=24,
        )

        title2 = self.ly.title("The System")

        sys_eq = MathTex(
            r"u_1'\,y_1", r"+", r"u_2'\,y_2", r"=", r"0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sys_eq[0].set_color(SECONDARY)
        sys_eq[2].set_color(SECONDARY)
        self.ly.safe_place(sys_eq, DOWN, anchor=title2, buff=0.4)
        self.play(Write(sys_eq), run_time=NORMAL)
        self.wait(0.5)

        sys_eq2 = MathTex(
            r"u_1'\,y_1'", r"+", r"u_2'\,y_2'", r"=", r"\dfrac{f(x)}{a}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sys_eq2[0].set_color(PRIMARY)
        sys_eq2[2].set_color(PRIMARY)
        sys_eq2[4].set_color(RED)
        self.ly.safe_place(sys_eq2, DOWN, anchor=sys_eq, buff=0.3)
        self.play(Write(sys_eq2), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(sys_eq), FadeOut(sys_eq2), run_time=FAST)

        self.add_subcaption(
            "Solving this system by Cramer's rule gives the formulas "
            "for u1 prime and u2 prime. The denominator is the "
            "Wronskian of y1 and y2. We will define it in the next "
            "section.",
            duration=20,
        )

        title3 = self.ly.title("Solutions by Cramer's Rule")

        u1p = MathTex(
            r"u_1'", r"=", r"\frac{-y_2\,f(x)}{a\,W}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        u1p[0].set_color(SECONDARY)
        u1p[2].set_color(ACCENT)
        self.ly.safe_place(u1p, DOWN, anchor=title3, buff=0.4)
        self.play(Write(u1p), run_time=NORMAL)
        self.wait(0.5)

        u2p = MathTex(
            r"u_2'", r"=", r"\frac{y_1\,f(x)}{a\,W}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        u2p[0].set_color(PRIMARY)
        u2p[2].set_color(ACCENT)
        self.ly.safe_place(u2p, DOWN, anchor=u1p, buff=0.3)
        self.play(Write(u2p), run_time=NORMAL)
        self.wait(1)

        self.ly.clear()

    # ── Scene 4: The Wronskian ─────────────────────────────────
    def scene4_wronskian(self):
        self.add_subcaption(
            "The Wronskian of two functions y1 and y2 is the "
            "determinant of a 2 by 2 matrix with y1, y2 in the "
            "first row and y1 prime, y2 prime in the second row. "
            "It measures whether y1 and y2 are truly independent.",
            duration=24,
        )

        self.ly.section_divider(3, "The Wronskian")
        self.wait(0.5)

        title = self.ly.title("Definition")

        W = MathTex(
            r"W(y_1, y_2)", r"=", r"\det",
            r"\begin{pmatrix} y_1 & y_2",
            r"y_1' & y_2' \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        W[0].set_color(ACCENT)
        W[3].set_color(PRIMARY)
        W[4].set_color(PRIMARY)
        self.ly.safe_place(W, DOWN, anchor=title, buff=0.5)
        self.play(Write(W), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(W), run_time=FAST)

        self.add_subcaption(
            "Expanding the determinant: W equals y1 y2 prime minus "
            "y2 y1 prime. The Wronskian is nonzero exactly when y1 "
            "and y2 are linearly independent solutions. This is "
            "guaranteed by Abel's theorem.",
            duration=20,
        )

        title2 = self.ly.title("Expanded Form")

        W_exp = MathTex(
            r"W", r"=", r"y_1\,y_2'", r"-", r"y_2\,y_1'",
            font_size=HEADING_SIZE, color=WHITE,
        )
        W_exp[0].set_color(ACCENT)
        W_exp[2].set_color(PRIMARY)
        W_exp[4].set_color(SECONDARY)
        self.ly.formula_box(W_exp, ACCENT)
        self.wait(2)

        self.ly.clear()

    # ── Scene 5: Example — y'' + y = sec(x) ───────────────────
    def scene5_example(self):
        self.add_subcaption(
            "Let us solve y double prime plus y equals secant of x. "
            "This is perfect for variation of parameters because "
            "secant of x cannot be handled by undetermined coefficients.",
            duration=20,
        )

        self.ly.section_divider(4, "Example: y'' + y = sec(x)")
        self.wait(0.5)

        title = self.ly.title("The Equation")

        ode = MathTex(
            r"y''", r"+", r"y", r"=", r"\sec(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ode[0].set_color(PRIMARY)
        ode[2].set_color(SECONDARY)
        ode[4].set_color(RED)
        self.ly.safe_place(ode, DOWN, anchor=title, buff=0.5)
        self.play(Write(ode), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ode), run_time=FAST)

        # Complementary solution
        self.add_subcaption(
            "The characteristic equation is r squared plus 1 equals 0, "
            "so r equals plus or minus i. The complementary solution "
            "is y c equals C1 cosine of x plus C2 sine of x.",
            duration=20,
        )

        title2 = self.ly.title("Complementary Solution")

        yc = MathTex(
            r"y_c", r"=", r"C_1\cos(x)", r"+", r"C_2\sin(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        yc[0].set_color(PRIMARY)
        yc[2].set_color(PRIMARY)
        yc[4].set_color(PRIMARY)
        self.ly.safe_place(yc, DOWN, anchor=title2, buff=0.5)
        self.play(Write(yc), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(yc), run_time=FAST)

        # Wronskian
        self.add_subcaption(
            "Here y1 is cosine of x and y2 is sine of x. "
            "The Wronskian is cosine times cosine minus sine times "
            "negative sine, which simplifies to cosine squared "
            "plus sine squared, which is exactly 1.",
            duration=24,
        )

        title3 = self.ly.title("The Wronskian")

        W_calc = MathTex(
            r"W", r"=", r"\cos^2(x)", r"+", r"\sin^2(x)", r"=", r"1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        W_calc[0].set_color(ACCENT)
        W_calc[2].set_color(PRIMARY)
        W_calc[4].set_color(SECONDARY)
        W_calc[6].set_color(SECONDARY)
        self.ly.safe_place(W_calc, DOWN, anchor=title3, buff=0.5)
        self.play(Write(W_calc), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(W_calc), run_time=FAST)

        # Find u1
        self.add_subcaption(
            "Now u1 prime equals negative y2 times f of x over W, "
            "which is negative sine of x times secant of x. "
            "Since secant is 1 over cosine, this becomes negative "
            "tangent of x. Integrating gives u1 equals the natural "
            "log of the absolute value of cosine of x.",
            duration=28,
        )

        title4 = self.ly.title("Find u1")

        u1 = MathTex(
            r"u_1", r"=", r"\ln|\cos(x)|",
            font_size=HEADING_SIZE, color=WHITE,
        )
        u1[0].set_color(ACCENT)
        u1[2].set_color(ACCENT)
        self.ly.safe_place(u1, DOWN, anchor=title4, buff=0.5)
        self.play(Write(u1), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(u1), run_time=FAST)

        # Find u2
        self.add_subcaption(
            "Similarly, u2 prime equals y1 times f of x over W, "
            "which is cosine of x times secant of x, giving exactly 1. "
            "Integrating gives u2 equals x.",
            duration=16,
        )

        title5 = self.ly.title("Find u2")

        u2 = MathTex(
            r"u_2", r"=", r"x",
            font_size=HEADING_SIZE, color=WHITE,
        )
        u2[0].set_color(PRIMARY)
        u2[2].set_color(PRIMARY)
        self.ly.safe_place(u2, DOWN, anchor=title5, buff=0.5)
        self.play(Write(u2), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(u2), run_time=FAST)

        # Full particular solution
        self.add_subcaption(
            "The particular solution is y p equals cosine of x "
            "times the natural log of cosine of x plus x times sine "
            "of x. Adding the complementary solution gives the full "
            "general solution.",
            duration=24,
        )

        title6 = self.ly.title("Particular Solution")

        yp = MathTex(
            r"y_p", r"=", r"\cos(x)\ln|\cos(x)|",
            r"+", r"x\sin(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        yp[0].set_color(ACCENT)
        yp[2].set_color(ACCENT)
        yp[4].set_color(ACCENT)
        self.ly.formula_box(yp, ACCENT)
        self.wait(2)

        self.ly.clear()

    # ── Scene 6: Comparison with Undetermined Coefficients ─────
    def scene6_comparison(self):
        self.add_subcaption(
            "Let us compare both methods on a problem undetermined "
            "coefficients can handle: y double prime minus 3 y prime "
            "plus 2 y equals 3 e to the 3 x. We solved this in the "
            "last video by guessing.",
            duration=24,
        )

        self.ly.section_divider(5, "Method Comparison")
        self.wait(0.5)

        title = self.ly.title("Same Problem, Different Tools")

        ode = MathTex(
            r"y''", r"-", r"3y'", r"+", r"2y", r"=", r"3e^{3x}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ode[0].set_color(PRIMARY)
        ode[2].set_color(SECONDARY)
        ode[4].set_color(ACCENT)
        ode[6].set_color(RED)
        self.ly.safe_place(ode, DOWN, anchor=title, buff=0.5)
        self.play(Write(ode), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ode), run_time=FAST)

        self.add_subcaption(
            "Using variation of parameters with y1 equals e to the x "
            "and y2 equals e to the 2 x, the Wronskian is e to the "
            "3 x. Working through the integrals gives the same "
            "particular solution: three tenths e to the 3 x.",
            duration=24,
        )

        title2 = self.ly.title("By Variation of Parameters")

        result = MathTex(
            r"y_p", r"=", r"\frac{3}{10}\,e^{3x}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        result[0].set_color(ACCENT)
        result[2].set_color(ACCENT)
        self.ly.safe_place(result, DOWN, anchor=title2, buff=0.5)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(result), run_time=FAST)

        self.add_subcaption(
            "Both methods give the same answer, but undetermined "
            "coefficients was faster. So use that when the forcing "
            "function allows it. Variation of parameters is your "
            "fallback for everything else.",
            duration=20,
        )

        title3 = self.ly.title("When to Use Which")

        items = [
            Text("Undetermined coefficients: fast for standard f(x)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Variation of parameters: general, works for any f(x)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Both give the same particular solution", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title3)
        self.wait(1)

        self.ly.clear()

    # ── Scene 7: Summary + Outro ───────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "To summarize: variation of parameters replaces the "
            "constants C1 and C2 with functions u1 and u2. "
            "The formulas come from the Wronskian and the forcing "
            "function. It always works for continuous f of x, "
            "but requires integration.",
            duration=24,
        )

        title = self.ly.title("Summary")

        items = [
            Text("Replace C1, C2 with u1(x), u2(x)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Constraint: u1'·y1 + u2'·y2 = 0", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Use Wronskian to solve for u1' and u2'", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Integrate to get u1, u2, then form y_p", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()

        self.add_subcaption(
            "The trade-off is clear: undetermined coefficients is "
            "faster but limited. Variation of parameters is slower "
            "but universal. In the next video we explore yet another "
            "approach: power series solutions.",
            duration=20,
        )

        play_outro(
            self,
            next_video="Power Series Solutions",
            next_playlist="Ordinary Differential Equations",
        )
