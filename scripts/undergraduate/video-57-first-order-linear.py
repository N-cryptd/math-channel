"""
Video 57: First-Order Linear Differential Equations
Ordinary Differential Equations -- Video 3 of N

Covers: standard form dy/dx + P(x)y = Q(x), linearity definition,
integrating factor derivation, constant-coefficient example,
mixing problem example.

Render draft:  manim -ql scripts/undergraduate/video-57-first-order-linear.py Video57_FirstOrderLinear
Render final:  manim -qh scripts/undergraduate/video-57-first-order-linear.py Video57_FirstOrderLinear
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


class Video57_FirstOrderLinear(Scene):
    """Full video: First-Order Linear Differential Equations."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_linearity()
        self.scene3_derivation()
        self.scene4_example1()
        self.scene5_example2()
        self.scene6_summary()

    # ── Scene 1: Hook — When Separation Fails ──────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Last time we solved separable equations, where dy/dx equals "
            "g of x times h of y. The key trick was splitting the variables "
            "apart. But not every equation lets you do that.",
            duration=24,
        )
        play_intro(self, "First-Order Linear Equations",
                   "Ordinary Differential Equations")

        title = self.ly.title("From Last Time...")

        # Recall separable form
        sep_eq = MathTex(
            r"\frac{dy}{dx}", r"=", r"g(x)", r"\cdot", r"h(y)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sep_eq[0].set_color(PRIMARY)
        sep_eq[2].set_color(SECONDARY)
        sep_eq[4].set_color(ACCENT)
        self.ly.safe_place(sep_eq, DOWN, anchor=title, buff=0.5)
        self.play(Write(sep_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(sep_eq), run_time=FAST)

        # The problem
        self.add_subcaption(
            "Consider dy/dx plus 2y equals 6. You cannot separate the "
            "variables here, because the y terms are on different sides "
            "and they don't factor into a product. We need a new technique.",
            duration=24,
        )

        title2 = self.ly.title("The Problem: Can't Separate")

        prob_eq = MathTex(
            r"\frac{dy}{dx}", r"+", r"2y", r"=", r"6",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prob_eq[0].set_color(PRIMARY)
        prob_eq[2].set_color(ACCENT)
        prob_eq[4].set_color(RED)
        self.ly.safe_place(prob_eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(prob_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(prob_eq), run_time=FAST)

        # Not separable label
        nsep = Text(
            "Can't split into g(x) * h(y)!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(nsep)
        self.play(FadeIn(nsep, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.play(FadeOut(nsep), run_time=FAST)

        # Standard form reveal
        self.add_subcaption(
            "Equations like this belong to a special family called "
            "first-order linear differential equations. They all have "
            "this standard form: dy/dx plus P of x times y equals Q of x.",
            duration=24,
        )

        title3 = self.ly.title("The Standard Form")

        std_eq = MathTex(
            r"\frac{dy}{dx}", r"+", r"P(x)\,y", r"=",
            r"Q(x)",
            font_size=TITLE_SIZE, color=WHITE,
        )
        std_eq[0].set_color(PRIMARY)
        std_eq[2].set_color(ACCENT)
        std_eq[4].set_color(SECONDARY)
        self.ly.center_in_content(std_eq)
        self.play(Write(std_eq), run_time=SLOW)
        self.wait(0.5)

        label = Text(
            "First-order linear ODE",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(label, DOWN, anchor=std_eq, buff=0.4)
        self.play(FadeIn(label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 2: What Does "Linear" Mean? ──────────────────────────
    def scene2_linearity(self):
        self.add_subcaption(
            "Linear means that y and dy/dx only appear to the first power. "
            "No y squared, no sine of y, no y times dy/dx. Just y and its "
            "derivative, possibly multiplied by functions of x.",
            duration=24,
        )
        self.ly.section_divider(1, "What Makes It Linear?")

        title = self.ly.title("The Linearity Test")

        # Linear examples
        lin_label = Text(
            "Linear:",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(lin_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(lin_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        lin_ex1 = MathTex(
            r"\frac{dy}{dx}", r"+", r"3y", r"=",
            r"x",
            font_size=HEADING_SIZE, color=WHITE,
        )
        lin_ex1[0].set_color(PRIMARY)
        lin_ex1[2].set_color(ACCENT)
        lin_ex1[4].set_color(SECONDARY)
        self.ly.safe_place(lin_ex1, DOWN, anchor=lin_label, buff=0.3)
        self.play(Write(lin_ex1), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(lin_label), FadeOut(lin_ex1), run_time=FAST)

        # Non-linear examples
        nlin_label = Text(
            "NOT linear:",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(nlin_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(nlin_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        self.add_subcaption(
            "For example, dy/dx plus y squared equals 1 is not linear "
            "because of the y squared. And dy/dx plus sine of y equals 0 "
            "is not linear because sine of y is not a degree-one function of y.",
            duration=24,
        )

        nlin_ex1 = MathTex(
            r"\frac{dy}{dx}", r"+", r"y^2", r"=",
            r"1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        nlin_ex1[0].set_color(PRIMARY)
        nlin_ex1[2].set_color(RED)
        nlin_ex1[4].set_color(RED)
        self.ly.safe_place(nlin_ex1, DOWN, anchor=nlin_label, buff=0.3)
        self.play(Write(nlin_ex1), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(nlin_ex1), run_time=FAST)

        nlin_ex2 = MathTex(
            r"\frac{dy}{dx}", r"+", r"\sin(y)", r"=",
            r"0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        nlin_ex2[0].set_color(PRIMARY)
        nlin_ex2[2].set_color(RED)
        self.ly.safe_place(nlin_ex2, DOWN, anchor=nlin_label, buff=0.3)
        self.play(Write(nlin_ex2), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(nlin_label), FadeOut(nlin_ex2), run_time=FAST)

        # Key takeaway
        key = Text(
            "y and dy/dx must appear to degree 1 only",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(key)
        self.play(FadeIn(key, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 3: Deriving the Integrating Factor ──────────────────
    def scene3_derivation(self):
        self.add_subcaption(
            "Here is the key idea. We want to turn the left side into a "
            "single derivative using the product rule. If we multiply the "
            "entire equation by some clever function, the left side becomes "
            "the derivative of a product.",
            duration=24,
        )
        self.ly.section_divider(2, "The Integrating Factor")

        title = self.ly.title("The Product Rule Trick")

        # Start with standard form
        std = MathTex(
            r"\frac{dy}{dx}", r"+", r"P(x)\,y", r"=",
            r"Q(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        std[0].set_color(PRIMARY)
        std[2].set_color(ACCENT)
        std[4].set_color(SECONDARY)
        self.ly.safe_place(std, DOWN, anchor=title, buff=0.5)
        self.play(Write(std), run_time=SLOW)
        self.wait(1)

        self.play(FadeOut(std), run_time=FAST)

        # Product rule
        self.add_subcaption(
            "The product rule says: d/dx of mu times y equals mu times "
            "dy/dx plus d mu/dx times y. We want this to match the left "
            "side of our equation, but multiplied by mu.",
            duration=24,
        )

        title2 = self.ly.title("Product Rule")

        pr_eq = MathTex(
            r"\frac{d}{dx}", r"[", r"\mu", r"\cdot", r"y", r"]",
            r"=", r"\mu", r"\frac{dy}{dx}",
            r"+", r"\mu'", r"y",
            font_size=HEADING_SIZE, color=WHITE,
        )
        pr_eq[0].set_color(DIM)
        pr_eq[2].set_color(ACCENT)
        pr_eq[4].set_color(PRIMARY)
        pr_eq[7].set_color(ACCENT)
        pr_eq[10].set_color(ACCENT)
        self.ly.safe_place(pr_eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(pr_eq), run_time=SLOW)
        self.wait(1.5)

        self.play(FadeOut(pr_eq), run_time=FAST)

        # Match condition
        self.add_subcaption(
            "For the product rule to match, we need mu prime to equal "
            "mu times P of x. This is itself a separable equation! "
            "Dividing both sides by mu gives d mu over mu equals "
            "P of x dx.",
            duration=24,
        )

        title3 = self.ly.title("Finding mu")

        cond_eq = MathTex(
            r"\mu'", r"=", r"\mu", r"\cdot", r"P(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        cond_eq[0].set_color(ACCENT)
        cond_eq[2].set_color(ACCENT)
        cond_eq[4].set_color(ACCENT)
        self.ly.safe_place(cond_eq, DOWN, anchor=title3, buff=0.5)
        self.play(Write(cond_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(cond_eq), run_time=FAST)

        # Separated form
        sep_mu = MathTex(
            r"\frac{d\mu}{\mu}", r"=", r"P(x)", r"\, dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sep_mu[0].set_color(ACCENT)
        sep_mu[2].set_color(ACCENT)
        self.ly.safe_place(sep_mu, DOWN, anchor=title3, buff=0.5)
        self.play(TransformFromCopy(cond_eq, sep_mu), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(sep_mu), run_time=FAST)

        # Integrate
        self.add_subcaption(
            "Integrating both sides gives the natural log of absolute "
            "mu equals the integral of P of x dx. Exponentiating, "
            "we get the integrating factor: mu equals e to the power "
            "of the integral of P of x dx.",
            duration=24,
        )

        title4 = self.ly.title("The Integrating Factor")

        mu_eq = MathTex(
            r"\mu(x)", r"=", r"e^{\int P(x)\, dx}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        mu_eq[0].set_color(ACCENT)
        mu_eq[2].set_color(ACCENT)
        self.ly.center_in_content(mu_eq)
        self.play(Write(mu_eq), run_time=SLOW)
        self.wait(1)

        # Highlight it
        box = self.ly.formula_box(mu_eq, color=ACCENT)
        self.play(Create(box), run_time=FAST)
        self.wait(1)

        self.play(FadeOut(box), FadeOut(mu_eq), run_time=FAST)

        # Apply: multiply through
        self.add_subcaption(
            "Now multiply the entire original equation by this mu. "
            "The left side becomes d/dx of mu times y, and the right "
            "side is mu times Q of x. This is perfect because we "
            "can now just integrate both sides.",
            duration=24,
        )

        title5 = self.ly.title("Multiply Through")

        mult_eq = MathTex(
            r"\frac{d}{dx}", r"[", r"\mu", r"\cdot", r"y", r"]",
            r"=", r"\mu", r"\cdot", r"Q(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        mult_eq[0].set_color(DIM)
        mult_eq[2].set_color(ACCENT)
        mult_eq[4].set_color(PRIMARY)
        mult_eq[7].set_color(ACCENT)
        mult_eq[9].set_color(SECONDARY)
        self.ly.safe_place(mult_eq, DOWN, anchor=title5, buff=0.5)
        self.play(Write(mult_eq), run_time=SLOW)
        self.wait(1)

        self.play(FadeOut(mult_eq), run_time=FAST)

        # Integrate both sides
        title6 = self.ly.title("Integrate Both Sides")

        int_eq = MathTex(
            r"\mu", r"\cdot", r"y", r"=",
            r"\int", r"\mu", r"\cdot", r"Q(x)", r"\, dx",
            r"+ C",
            font_size=HEADING_SIZE, color=WHITE,
        )
        int_eq[0].set_color(ACCENT)
        int_eq[2].set_color(PRIMARY)
        int_eq[7].set_color(SECONDARY)
        int_eq[9].set_color(ACCENT)
        self.ly.safe_place(int_eq, DOWN, anchor=title6, buff=0.5)
        self.play(Write(int_eq), run_time=SLOW)
        self.wait(1)

        self.play(FadeOut(int_eq), run_time=FAST)

        # Final formula
        title7 = self.ly.title("The General Solution")

        sol = MathTex(
            r"y", r"=", r"\frac{1}{\mu}",
            r"\left(", r"\int", r"\mu", r"\cdot",
            r"Q(x)", r"\, dx", r"+ C",
            r"\right)",
            font_size=TITLE_SIZE, color=WHITE,
        )
        sol[0].set_color(PRIMARY)
        sol[2].set_color(ACCENT)
        sol[7].set_color(SECONDARY)
        sol[9].set_color(ACCENT)
        self.ly.center_in_content(sol)
        self.play(Write(sol), run_time=SLOW)
        self.wait(2)
        self.ly.clear()

    # ── Scene 4: Example 1 — Constant Coefficient ──────────────────
    def scene4_example1(self):
        self.add_subcaption(
            "Let's put this into practice. Solve dy/dx plus 2y equals 6. "
            "This is a constant-coefficient example where P is just "
            "the number 2 and Q is just the number 6.",
            duration=24,
        )
        self.ly.section_divider(3, "Example: Constant Coefficient")

        title = self.ly.title("dy/dx + 2y = 6")

        # Identify P and Q
        id_text = Text(
            "P(x) = 2,   Q(x) = 6",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(id_text, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(id_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(id_text), run_time=FAST)

        # Compute mu
        self.add_subcaption(
            "First, compute the integrating factor. Mu equals e to the "
            "integral of 2 dx, which is e to the 2x. Simple!",
            duration=20,
        )

        title2 = self.ly.title("Step 1: Find mu")

        mu_eq = MathTex(
            r"\mu", r"=", r"e^{\int 2\, dx}", r"=",
            r"e^{2x}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        mu_eq[0].set_color(ACCENT)
        mu_eq[2].set_color(ACCENT)
        mu_eq[4].set_color(ACCENT)
        self.ly.safe_place(mu_eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(mu_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(mu_eq), run_time=FAST)

        # Multiply through
        self.add_subcaption(
            "Multiply the entire equation by e to the 2x. The left side "
            "becomes d/dx of e to the 2x times y, and the right side "
            "is 6 times e to the 2x.",
            duration=20,
        )

        title3 = self.ly.title("Step 2: Multiply Through")

        mult_eq = MathTex(
            r"\frac{d}{dx}", r"[", r"e^{2x}", r"y", r"]",
            r"=", r"6", r"e^{2x}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        mult_eq[0].set_color(DIM)
        mult_eq[2].set_color(ACCENT)
        mult_eq[3].set_color(PRIMARY)
        mult_eq[6].set_color(SECONDARY)
        mult_eq[7].set_color(ACCENT)
        self.ly.safe_place(mult_eq, DOWN, anchor=title3, buff=0.5)
        self.play(Write(mult_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(mult_eq), run_time=FAST)

        # Integrate
        self.add_subcaption(
            "Now integrate both sides. The left side gives e to the 2x "
            "times y. The right side gives 3 times e to the 2x plus C.",
            duration=20,
        )

        title4 = self.ly.title("Step 3: Integrate")

        int_eq = MathTex(
            r"e^{2x}", r"y", r"=", r"3", r"e^{2x}",
            r"+ C",
            font_size=HEADING_SIZE, color=WHITE,
        )
        int_eq[0].set_color(ACCENT)
        int_eq[1].set_color(PRIMARY)
        int_eq[3].set_color(SECONDARY)
        int_eq[4].set_color(ACCENT)
        int_eq[5].set_color(ACCENT)
        self.ly.safe_place(int_eq, DOWN, anchor=title4, buff=0.5)
        self.play(Write(int_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(int_eq), run_time=FAST)

        # Solve for y
        self.add_subcaption(
            "Divide both sides by e to the 2x. The e terms cancel, "
            "and we get y equals 3 plus C times e to the negative 2x.",
            duration=20,
        )

        title5 = self.ly.title("Step 4: Solve for y")

        sol_eq = MathTex(
            r"y", r"=", r"3", r"+",
            r"Ce^{-2x}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        sol_eq[0].set_color(PRIMARY)
        sol_eq[2].set_color(SECONDARY)
        sol_eq[4].set_color(ACCENT)
        self.ly.center_in_content(sol_eq)
        self.play(Write(sol_eq), run_time=SLOW)
        self.wait(0.5)

        # Interpretation
        interp = Text(
            "As x grows, y approaches 3 (steady state)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(interp, DOWN, anchor=sol_eq, buff=0.4)
        self.play(FadeIn(interp, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 5: Example 2 — Mixing Problem ────────────────────────
    def scene5_example2(self):
        self.add_subcaption(
            "Here's a classic application. A tank holds 100 liters of "
            "water with 5 kilograms of salt dissolved. Fresh water "
            "flows in at 2 liters per minute, and the mixture drains "
            "out at 2 liters per minute. How much salt remains over time?",
            duration=24,
        )
        self.ly.section_divider(4, "Example: Mixing Problem")

        title = self.ly.title("Tank Problem")

        # Setup info
        setup = Text(
            "Tank: 100 L water, 5 kg salt",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(setup, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(setup, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(setup), run_time=FAST)

        # Set up DE
        self.add_subcaption(
            "Let y of t be the amount of salt in kilograms. The rate of "
            "change of salt equals the rate in minus the rate out. "
            "Fresh water enters, so rate in is zero. Rate out is the "
            "concentration times the flow rate: y over 100 times 2.",
            duration=24,
        )

        title2 = self.ly.title("Setting Up the DE")

        de_eq = MathTex(
            r"\frac{dy}{dt}", r"=", r"0", r"-",
            r"\frac{y}{100}", r"\cdot", r"2",
            r"=", r"-\frac{y}{50}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        de_eq[0].set_color(PRIMARY)
        de_eq[2].set_color(SECONDARY)
        de_eq[8].set_color(RED)
        self.ly.safe_place(de_eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(de_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(de_eq), run_time=FAST)

        # Standard form
        self.add_subcaption(
            "In standard form: dy/dt plus one over 50 times y equals 0. "
            "This is actually both separable and linear! The integrating "
            "factor is e to the t over 50.",
            duration=20,
        )

        title3 = self.ly.title("Standard Form")

        std_eq = MathTex(
            r"\frac{dy}{dt}", r"+", r"\frac{1}{50}\,y", r"=",
            r"0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        std_eq[0].set_color(PRIMARY)
        std_eq[2].set_color(ACCENT)
        std_eq[4].set_color(RED)
        self.ly.safe_place(std_eq, DOWN, anchor=title3, buff=0.5)
        self.play(Write(std_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(std_eq), run_time=FAST)

        # Solve quickly
        self.add_subcaption(
            "Using the integrating factor method: mu equals e to the "
            "t over 50. Multiplying through and integrating gives "
            "y times e to the t over 50 equals C. So y equals C "
            "times e to the negative t over 50.",
            duration=24,
        )

        title4 = self.ly.title("Solving")

        mu_eq = MathTex(
            r"\mu", r"=", r"e^{t/50}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        mu_eq[0].set_color(ACCENT)
        mu_eq[2].set_color(ACCENT)
        self.ly.safe_place(mu_eq, DOWN, anchor=title4, buff=0.5)
        self.play(Write(mu_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(mu_eq), run_time=FAST)

        # Apply IC
        self.add_subcaption(
            "Using the initial condition y of zero equals 5: 5 equals "
            "C times e to the zero, so C equals 5. The complete "
            "solution is y of t equals 5 times e to the negative t "
            "over 50.",
            duration=24,
        )

        title5 = self.ly.title("Apply Initial Condition")

        ic_text = Text(
            "y(0) = 5:  so  C = 5",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(ic_text, DOWN, anchor=title5, buff=0.4)
        self.play(FadeIn(ic_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ic_text), run_time=FAST)

        # Final answer
        answer = MathTex(
            r"y(t)", r"=", r"5", r"e^{-t/50}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        answer[0].set_color(PRIMARY)
        answer[2].set_color(ACCENT)
        answer[3].set_color(ACCENT)
        self.ly.center_in_content(answer)
        self.play(Write(answer), run_time=SLOW)
        self.wait(0.5)

        interp = Text(
            "Salt drains exponentially — half-life ~35 min",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(interp, DOWN, anchor=answer, buff=0.4)
        self.play(FadeIn(interp, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 6: Summary + Preview ────────────────────────────────
    def scene6_summary(self):
        self.add_subcaption(
            "Let's recap. A first-order linear ODE has the standard form "
            "dy/dx plus P of x times y equals Q of x. The integrating "
            "factor mu equals e to the integral of P of x dx transforms "
            "the equation into an exact derivative, which we can integrate.",
            duration=24,
        )

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "Standard form:  dy/dx + P(x)y = Q(x)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Integrating factor:  \u03bc = e^{\u222bP(x) dx}",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Multiply, then d/dx[\u03bc\u00b7y] = \u03bc\u00b7Q(x)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Integrate and solve for y",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        self.ly.clear()

        self.add_subcaption(
            "Next time, we'll move up to second-order linear equations, "
            "which model oscillations like springs and circuits. The "
            "techniques generalize beautifully from what we learned today.",
            duration=24,
        )

        title2 = self.ly.title("Coming Up Next")

        next_text = Text(
            "Second-Order Linear Equations",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(next_text)
        self.play(FadeIn(next_text, shift=UP * 0.15), run_time=NORMAL)
        self.wait(0.5)

        next_eq = MathTex(
            r"a", r"\frac{d^2y}{dx^2}", r"+",
            r"b\frac{dy}{dx}", r"+",
            r"cy", r"=", r"f(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        next_eq[1].set_color(PRIMARY)
        next_eq[3].set_color(PRIMARY)
        next_eq[5].set_color(ACCENT)
        next_eq[7].set_color(SECONDARY)
        self.ly.safe_place(next_eq, DOWN, anchor=next_text, buff=0.5)
        self.play(Write(next_eq), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        play_outro(
            self,
            next_video="Second-Order Linear Equations",
            next_playlist="ODE",
        )
