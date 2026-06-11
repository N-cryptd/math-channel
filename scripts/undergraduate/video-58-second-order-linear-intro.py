"""
Video 58: Second-Order Linear Differential Equations — Introduction
Ordinary Differential Equations -- Video 4 of N

Covers: standard form ay'' + by' + cy = f(x), linearity definition,
the characteristic equation (trial solution y = e^{rx}), three cases
(distinct real, repeated, complex roots), worked examples for each case,
superposition principle.

Render draft:  manim -ql scripts/undergraduate/video-58-second-order-linear-intro.py Video58_SecondOrderLinearIntro
Render final:  manim -qh scripts/undergraduate/video-58-second-order-linear-intro.py Video58_SecondOrderLinearIntro
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


class Video58_SecondOrderLinearIntro(Scene):
    """Full video: Second-Order Linear Differential Equations."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_anatomy()
        self.scene3_characteristic()
        self.scene4_example_real()
        self.scene5_example_repeated()
        self.scene6_example_complex()
        self.scene7_summary()

    # ── Scene 1: Hook — Beyond First Order ──────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "We have solved first-order equations with one derivative and "
            "one initial condition. But the real world often involves "
            "second derivatives. Think of a mass on a spring.",
            duration=24,
        )
        play_intro(self, "Second-Order Linear Equations",
                   "Ordinary Differential Equations")

        title = self.ly.title("From Last Time...")

        # Recall first-order
        fo_eq = MathTex(
            r"\frac{dy}{dx}", r"+", r"P(x)\,y", r"=", r"Q(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        fo_eq[0].set_color(PRIMARY)
        fo_eq[2].set_color(ACCENT)
        fo_eq[4].set_color(SECONDARY)
        self.ly.safe_place(fo_eq, DOWN, anchor=title, buff=0.5)
        self.play(Write(fo_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(fo_eq), run_time=FAST)

        self.add_subcaption(
            "Newton's second law says force equals mass times acceleration. "
            "Acceleration is the second derivative of position. This means "
            "we need equations with d squared y over d x squared.",
            duration=24,
        )

        title2 = self.ly.title("Why Second Order?")

        items = [
            Text("Springs and oscillations", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Electric circuits (RLC)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Pendulums and waves", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(1)

        self.ly.clear()

    # ── Scene 2: Anatomy of a Second-Order ODE ─────────────────
    def scene2_anatomy(self):
        self.add_subcaption(
            "A second-order linear ODE has the form: a y double prime "
            "plus b y prime plus c y equals f of x. The coefficients "
            "a, b, c are constants. The function f is the forcing term.",
            duration=24,
        )

        title = self.ly.title("Standard Form")

        std_form = MathTex(
            r"a\,y''", r"+", r"b\,y'", r"+", r"c\,y", r"=", r"f(x)",
            font_size=TITLE_SIZE, color=WHITE,
        )
        std_form[0].set_color(PRIMARY)
        std_form[2].set_color(SECONDARY)
        std_form[4].set_color(ACCENT)
        std_form[6].set_color(RED)
        self.ly.safe_place(std_form, DOWN, anchor=title, buff=0.5)
        self.play(Write(std_form), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(std_form), run_time=FAST)

        # Homogeneous vs non-homogeneous
        self.add_subcaption(
            "When the forcing function is zero, we call it homogeneous. "
            "When it is nonzero, it is non-homogeneous. We start with "
            "the homogeneous case because it is the foundation.",
            duration=24,
        )

        title2 = self.ly.title("Homogeneous vs Non-Homogeneous")

        items = [
            Text("Homogeneous: f(x) = 0", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Non-homogeneous: f(x) ≠ 0", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("We start with homogeneous", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(1)

        self.play(FadeOut(items[-1]), run_time=FAST)

        # Superposition
        self.add_subcaption(
            "Here is a beautiful property: if y1 and y2 are both solutions "
            "to a linear homogeneous ODE, then any linear combination "
            "c1 y1 plus c2 y2 is also a solution. This is called "
            "the superposition principle.",
            duration=24,
        )

        title3 = self.ly.title("Superposition Principle")

        sup_eq = MathTex(
            r"y", r"=", r"C_1", r"\cdot", r"y_1",
            r"+", r"C_2", r"\cdot", r"y_2",
            font_size=TITLE_SIZE, color=WHITE,
        )
        sup_eq[0].set_color(WHITE)
        sup_eq[2].set_color(PRIMARY)
        sup_eq[4].set_color(PRIMARY)
        sup_eq[6].set_color(SECONDARY)
        sup_eq[8].set_color(SECONDARY)
        self.ly.safe_place(sup_eq, DOWN, anchor=title3, buff=0.5)
        self.play(Write(sup_eq), run_time=NORMAL)
        self.wait(1)

        self.ly.clear()

    # ── Scene 3: The Characteristic Equation ────────────────────
    def scene3_characteristic(self):
        self.add_subcaption(
            "The key idea is to try y equals e to the r x as a trial "
            "solution. If we substitute this into the homogeneous equation, "
            "we get a simple algebraic equation.",
            duration=24,
        )

        self.ly.section_divider(2, "The Characteristic Equation")
        self.wait(0.5)

        title = self.ly.title("Trial Solution")

        trial = MathTex(
            r"y", r"=", r"e^{rx}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        trial[0].set_color(WHITE)
        trial[2].set_color(ACCENT)
        self.ly.safe_place(trial, DOWN, anchor=title, buff=0.5)
        self.play(Write(trial), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(trial), run_time=FAST)

        # Show derivatives
        self.add_subcaption(
            "Taking derivatives: y prime is r times e to the r x, "
            "and y double prime is r squared times e to the r x. "
            "Notice the pattern: each derivative brings down a factor of r.",
            duration=24,
        )

        title2 = self.ly.title("Derivatives of e^{rx}")

        derivs = [
            MathTex(
                r"y'", r"=", r"r\,e^{rx}",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            MathTex(
                r"y''", r"=", r"r^2\,e^{rx}",
                font_size=HEADING_SIZE, color=WHITE,
            ),
        ]
        derivs[0][1].set_color(PRIMARY)
        derivs[0][2].set_color(ACCENT)
        derivs[1][1].set_color(PRIMARY)
        derivs[1][2].set_color(ACCENT)

        fitted, overflow = self.ly.stack_down(derivs, start_from=title2, spacing=0.4)
        for d in derivs:
            self.play(Write(d), run_time=NORMAL)
            self.wait(0.5)

        self.play(FadeOut(*derivs), run_time=FAST)

        # Substitution
        self.add_subcaption(
            "Now substitute into a y double prime plus b y prime plus c y "
            "equals zero. Factor out e to the r x, which is never zero. "
            "This gives us the characteristic equation: a r squared "
            "plus b r plus c equals zero.",
            duration=24,
        )

        title3 = self.ly.title("The Characteristic Equation")

        char_eq = MathTex(
            r"a\,r^2", r"+", r"b\,r", r"+", r"c", r"= 0",
            font_size=TITLE_SIZE, color=WHITE,
        )
        char_eq[0].set_color(PRIMARY)
        char_eq[2].set_color(SECONDARY)
        char_eq[4].set_color(ACCENT)
        self.ly.safe_place(char_eq, DOWN, anchor=title3, buff=0.5)
        self.play(Write(char_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(char_eq), run_time=FAST)

        # Three cases
        self.add_subcaption(
            "The discriminant D equals b squared minus 4 a c determines "
            "the nature of the roots. If D is positive, two distinct "
            "real roots. If D is zero, one repeated root. "
            "If D is negative, complex roots.",
            duration=24,
        )

        title4 = self.ly.title("Three Cases")

        disc = MathTex(
            r"D", r"=", r"b^2", r"-", r"4ac",
            font_size=HEADING_SIZE, color=WHITE,
        )
        disc[0].set_color(WHITE)
        disc[2].set_color(PRIMARY)
        disc[4].set_color(RED)
        self.ly.safe_place(disc, DOWN, anchor=title4, buff=0.5)
        self.play(Write(disc), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(disc), run_time=FAST)

        cases = [
            Text("D > 0: Two distinct real roots", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("D = 0: One repeated root", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("D < 0: Complex roots", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(cases, start_from=title4)
        self.wait(1)

        self.ly.clear()

    # ── Scene 4: Example 1 — Distinct Real Roots ────────────────
    def scene4_example_real(self):
        self.add_subcaption(
            "Let us work through our first example. Solve y double prime "
            "minus 5 y prime plus 6 y equals zero.",
            duration=12,
        )

        self.ly.section_divider(3, "Example: Distinct Real Roots")
        self.wait(0.5)

        title = self.ly.title("The Equation")

        eq = MathTex(
            r"y''", r"-", r"5\,y'", r"+", r"6\,y", r"= 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        eq[0].set_color(PRIMARY)
        eq[2].set_color(SECONDARY)
        eq[4].set_color(ACCENT)
        self.ly.safe_place(eq, DOWN, anchor=title, buff=0.5)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(eq), run_time=FAST)

        # Characteristic equation
        self.add_subcaption(
            "The characteristic equation is r squared minus 5 r plus "
            "6 equals zero. This factors as r minus 2 times r minus 3 "
            "equals zero, giving roots r equals 2 and r equals 3.",
            duration=24,
        )

        title2 = self.ly.title("Characteristic Equation")

        char_eq = MathTex(
            r"r^2", r"-", r"5\,r", r"+", r"6", r"= 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        char_eq[0].set_color(PRIMARY)
        char_eq[2].set_color(SECONDARY)
        char_eq[4].set_color(ACCENT)
        self.ly.safe_place(char_eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(char_eq), run_time=NORMAL)
        self.wait(1)

        self.play(Transform(char_eq, MathTex(
            r"(r-2)", r"(r-3)", r"= 0",
            font_size=HEADING_SIZE, color=WHITE,
        )), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(char_eq), run_time=FAST)

        # Roots
        title3 = self.ly.title("Roots")

        roots = MathTex(
            r"r_1", r"=", r"2",
            r"\qquad",
            r"r_2", r"=", r"3",
            font_size=HEADING_SIZE, color=WHITE,
        )
        roots[0].set_color(PRIMARY)
        roots[2].set_color(PRIMARY)
        roots[4].set_color(SECONDARY)
        roots[6].set_color(SECONDARY)
        self.ly.safe_place(roots, DOWN, anchor=title3, buff=0.5)
        self.play(Write(roots), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(roots), run_time=FAST)

        # General solution
        self.add_subcaption(
            "Since both roots are real and distinct, the general "
            "solution is y equals C1 times e to the 2 x plus "
            "C2 times e to the 3 x. Two arbitrary constants, "
            "because it is a second-order equation.",
            duration=24,
        )

        title4 = self.ly.title("General Solution")

        sol = MathTex(
            r"y", r"=", r"C_1\,e^{2x}",
            r"+", r"C_2\,e^{3x}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        sol[0].set_color(WHITE)
        sol[2].set_color(PRIMARY)
        sol[4].set_color(SECONDARY)
        self.ly.center_in_content(sol)
        self.play(Write(sol), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ── Scene 5: Example 2 — Repeated Roots ─────────────────────
    def scene5_example_repeated(self):
        self.add_subcaption(
            "Next example: y double prime minus 4 y prime plus 4 y "
            "equals zero. The characteristic equation has a double root.",
            duration=24,
        )

        self.ly.section_divider(4, "Example: Repeated Root")
        self.wait(0.5)

        title = self.ly.title("The Equation")

        eq = MathTex(
            r"y''", r"-", r"4\,y'", r"+", r"4\,y", r"= 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        eq[0].set_color(PRIMARY)
        eq[2].set_color(SECONDARY)
        eq[4].set_color(ACCENT)
        self.ly.safe_place(eq, DOWN, anchor=title, buff=0.5)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(eq), run_time=FAST)

        # Characteristic equation
        self.add_subcaption(
            "The characteristic equation is r squared minus 4 r plus "
            "4 equals zero, which factors as r minus 2 all squared "
            "equals zero. We get r equals 2 with multiplicity 2.",
            duration=24,
        )

        title2 = self.ly.title("Characteristic Equation")

        char_eq = MathTex(
            r"r^2", r"-", r"4\,r", r"+", r"4", r"= 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        char_eq[0].set_color(PRIMARY)
        char_eq[2].set_color(SECONDARY)
        char_eq[4].set_color(ACCENT)
        self.ly.safe_place(char_eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(char_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(char_eq), run_time=FAST)

        # Repeated root
        title3 = self.ly.title("Repeated Root")

        root = MathTex(
            r"r", r"=", r"2",
            r"\quad \text{(multiplicity 2)}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        root[0].set_color(PRIMARY)
        root[2].set_color(PRIMARY)
        self.ly.safe_place(root, DOWN, anchor=title3, buff=0.5)
        self.play(Write(root), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(root), run_time=FAST)

        # General solution
        self.add_subcaption(
            "When the root repeats, we need a second independent solution. "
            "The trick is to multiply by x. The general solution becomes "
            "y equals C1 times e to the 2 x plus C2 times x times e to "
            "the 2 x.",
            duration=24,
        )

        title4 = self.ly.title("General Solution")

        sol = MathTex(
            r"y", r"=", r"C_1\,e^{2x}",
            r"+", r"C_2\,x\,e^{2x}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        sol[0].set_color(WHITE)
        sol[2].set_color(PRIMARY)
        sol[4].set_color(SECONDARY)
        self.ly.center_in_content(sol)
        self.play(Write(sol), run_time=NORMAL)
        self.wait(1)

        # Highlight the x factor
        self.add_subcaption(
            "The x factor in the second term is what makes the two "
            "solutions independent. Without it, we would not have "
            "enough degrees of freedom.",
            duration=20,
        )

        highlight = MathTex(
            r"x", r"\,e^{2x}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(highlight, DOWN, anchor=sol, buff=0.5)
        self.play(Write(highlight), run_time=NORMAL)
        self.wait(1)

        self.ly.clear()

    # ── Scene 6: Example 3 — Complex Roots ─────────────────────
    def scene6_example_complex(self):
        self.add_subcaption(
            "Our final example: y double prime plus 2 y prime plus 5 y "
            "equals zero. This time the characteristic equation has "
            "complex roots, leading to oscillating solutions.",
            duration=24,
        )

        self.ly.section_divider(5, "Example: Complex Roots")
        self.wait(0.5)

        title = self.ly.title("The Equation")

        eq = MathTex(
            r"y''", r"+", r"2\,y'", r"+", r"5\,y", r"= 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        eq[0].set_color(PRIMARY)
        eq[2].set_color(SECONDARY)
        eq[4].set_color(ACCENT)
        self.ly.safe_place(eq, DOWN, anchor=title, buff=0.5)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(eq), run_time=FAST)

        # Characteristic equation
        self.add_subcaption(
            "The characteristic equation is r squared plus 2 r plus 5 "
            "equals zero. Using the quadratic formula, the discriminant "
            "is 4 minus 20, which is negative 16. So we get complex roots.",
            duration=24,
        )

        title2 = self.ly.title("Characteristic Equation")

        char_eq = MathTex(
            r"r^2", r"+", r"2\,r", r"+", r"5", r"= 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        char_eq[0].set_color(PRIMARY)
        char_eq[2].set_color(SECONDARY)
        char_eq[4].set_color(ACCENT)
        self.ly.safe_place(char_eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(char_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(char_eq), run_time=FAST)

        # Complex roots
        self.add_subcaption(
            "The roots are r equals negative 1 plus or minus 2 i. "
            "We write alpha equals negative 1 and beta equals 2, "
            "where alpha is the real part and beta is the imaginary part.",
            duration=24,
        )

        title3 = self.ly.title("Complex Roots")

        roots = MathTex(
            r"r", r"=", r"-1", r"\pm", r"2i",
            font_size=HEADING_SIZE, color=WHITE,
        )
        roots[0].set_color(PRIMARY)
        roots[2].set_color(ACCENT)
        roots[4].set_color(RED)
        self.ly.safe_place(roots, DOWN, anchor=title3, buff=0.5)
        self.play(Write(roots), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(roots), run_time=FAST)

        # alpha and beta
        ab_items = [
            MathTex(r"\alpha", r"=", r"-1", font_size=HEADING_SIZE, color=WHITE),
            MathTex(r"\beta", r"=", r"2", font_size=HEADING_SIZE, color=WHITE),
        ]
        ab_items[0][0].set_color(ACCENT)
        ab_items[0][2].set_color(ACCENT)
        ab_items[1][0].set_color(RED)
        ab_items[1][2].set_color(RED)

        fitted, overflow = self.ly.stack_down(ab_items, start_from=title3, spacing=0.4)
        for item in ab_items:
            self.play(Write(item), run_time=NORMAL)
            self.wait(0.5)

        self.play(FadeOut(*ab_items), run_time=FAST)

        # General solution
        self.add_subcaption(
            "For complex roots, the general solution involves sines and "
            "cosines. We get y equals e to the alpha x times C1 cosine "
            "beta x plus C2 sine beta x. Here that is e to the negative "
            "x times C1 cosine 2 x plus C2 sine 2 x.",
            duration=24,
        )

        title4 = self.ly.title("General Solution")

        sol = MathTex(
            r"y", r"=", r"e^{-x}\!\left(",
            r"C_1", r"\cos(2x)",
            r"+", r"C_2", r"\sin(2x)",
            r"\right)",
            font_size=TITLE_SIZE, color=WHITE,
        )
        sol[0].set_color(WHITE)
        sol[2].set_color(ACCENT)
        sol[3].set_color(PRIMARY)
        sol[4].set_color(PRIMARY)
        sol[6].set_color(SECONDARY)
        sol[7].set_color(SECONDARY)
        self.ly.center_in_content(sol)
        self.play(Write(sol), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ── Scene 7: Summary + Preview ─────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "Let us recap what we have learned. A second-order linear "
            "ODE has the form a y double prime plus b y prime plus c y "
            "equals zero. The characteristic equation gives us the roots, "
            "and the nature of the roots determines the form of the solution.",
            duration=24,
        )

        title = self.ly.title("Summary")

        items = [
            Text("Standard form: ay'' + by' + cy = 0", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Characteristic eq: ar² + br + c = 0", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("D > 0: C1·e^{r₁x} + C2·e^{r₂x}", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("D = 0: C1·e^{rx} + C2·x·e^{rx}", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("D < 0: e^{αx}(C1·cos βx + C2·sin βx)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()

        self.add_subcaption(
            "Next time we will learn how to use initial conditions "
            "to find the specific values of C1 and C2. This is called "
            "solving an initial value problem. See you then!",
            duration=20,
        )

        play_outro(
            self,
            next_video="Initial Value Problems",
            next_playlist="Ordinary Differential Equations",
        )
