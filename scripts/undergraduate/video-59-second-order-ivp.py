"""
Video 59: Initial Value Problems for Second-Order ODEs
Ordinary Differential Equations -- Video 5 of N

Covers: IVP setup for second-order equations, two initial conditions,
solving for C1 and C2, examples with distinct real, repeated, and
complex roots, the general system method.

Render draft:  manim -ql scripts/undergraduate/video-59-second-order-ivp.py Video59_SecondOrderIVP
Render final:  manim -qh scripts/undergraduate/video-59-second-order-ivp.py Video59_SecondOrderIVP
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


class Video59_SecondOrderIVP(Scene):
    """Full video: Initial Value Problems for Second-Order ODEs."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_setup()
        self.scene3_example_real()
        self.scene4_example_repeated()
        self.scene5_example_complex()
        self.scene6_method()
        self.scene7_summary()

    # ── Scene 1: Hook — Finding C1 and C2 ──────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Last time we found general solutions with arbitrary constants "
            "C1 and C2. But which specific solution describes our system? "
            "We need initial conditions to find C1 and C2.",
            duration=24,
        )
        play_intro(self, "Initial Value Problems",
                   "Ordinary Differential Equations")

        title = self.ly.title("The Problem with Constants")

        gen_sol = MathTex(
            r"y", r"=", r"C_1", r"\cdot", r"f_1(x)",
            r"+", r"C_2", r"\cdot", r"f_2(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        gen_sol[2].set_color(PRIMARY)
        gen_sol[6].set_color(SECONDARY)
        self.ly.safe_place(gen_sol, DOWN, anchor=title, buff=0.5)
        self.play(Write(gen_sol), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(gen_sol), run_time=FAST)

        self.add_subcaption(
            "For a second-order ODE, we need TWO initial conditions. "
            "Think of a spring: you need both the initial position "
            "and the initial velocity to predict the future.",
            duration=24,
        )

        title2 = self.ly.title("Two Initial Conditions")

        items = [
            Text("y(0) = starting value", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("y'(0) = starting rate of change", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Together, they determine C1 and C2", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(1)

        self.ly.clear()

    # ── Scene 2: Setting Up an IVP ─────────────────────────────
    def scene2_setup(self):
        self.add_subcaption(
            "An initial value problem specifies the ODE together with "
            "initial conditions. For a second-order equation, the standard "
            "form is: a y double prime plus b y prime plus c y equals zero, "
            "with y of zero equals y naught and y prime of zero equals v naught.",
            duration=24,
        )

        self.ly.section_divider(1, "What Is an IVP?")
        self.wait(0.5)

        title = self.ly.title("General Form")

        ivp_form = MathTex(
            r"a\,y''", r"+", r"b\,y'", r"+", r"c\,y", r"= 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ivp_form[0].set_color(PRIMARY)
        ivp_form[2].set_color(SECONDARY)
        ivp_form[4].set_color(ACCENT)
        self.ly.safe_place(ivp_form, DOWN, anchor=title, buff=0.5)
        self.play(Write(ivp_form), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ivp_form), run_time=FAST)

        # ICs
        ics = [
            MathTex(
                r"y(0)", r"=", r"y_0",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            MathTex(
                r"y'(0)", r"=", r"v_0",
                font_size=HEADING_SIZE, color=WHITE,
            ),
        ]
        ics[0][0].set_color(PRIMARY)
        ics[0][2].set_color(RED)
        ics[1][0].set_color(SECONDARY)
        ics[1][2].set_color(RED)

        title2 = self.ly.title("Initial Conditions")
        fitted, overflow = self.ly.stack_down(ics, start_from=title2, spacing=0.4)
        for ic in ics:
            self.play(Write(ic), run_time=NORMAL)
            self.wait(0.5)

        self.ly.clear()

    # ── Scene 3: Example 1 — Distinct Real Roots ───────────────
    def scene3_example_real(self):
        self.add_subcaption(
            "Let us solve our first IVP. Y double prime minus 3 y prime "
            "plus 2 y equals zero, with y of zero equals 1 and y prime "
            "of zero equals 0.",
            duration=24,
        )

        self.ly.section_divider(2, "Example: Distinct Real Roots")
        self.wait(0.5)

        title = self.ly.title("The IVP")

        # The ODE
        ode = MathTex(
            r"y''", r"-", r"3\,y'", r"+", r"2\,y", r"= 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ode[0].set_color(PRIMARY)
        ode[2].set_color(SECONDARY)
        ode[4].set_color(ACCENT)
        self.ly.safe_place(ode, DOWN, anchor=title, buff=0.5)
        self.play(Write(ode), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ode), run_time=FAST)

        # Characteristic equation
        self.add_subcaption(
            "The characteristic equation is r squared minus 3 r plus 2 "
            "equals 0, which factors as r minus 1 times r minus 2 equals 0. "
            "Roots are r equals 1 and r equals 2.",
            duration=24,
        )

        title2 = self.ly.title("Characteristic Equation")

        char_eq = MathTex(
            r"r^2", r"-", r"3r", r"+", r"2", r"= 0",
            r"\;\Rightarrow\; (r-1)(r-2)=0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        char_eq[0].set_color(PRIMARY)
        char_eq[2].set_color(SECONDARY)
        char_eq[4].set_color(ACCENT)
        self.ly.safe_place(char_eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(char_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(char_eq), run_time=FAST)

        # General solution
        title3 = self.ly.title("General Solution")

        gen_sol = MathTex(
            r"y", r"=", r"C_1\,e^{x}",
            r"+", r"C_2\,e^{2x}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        gen_sol[2].set_color(PRIMARY)
        gen_sol[4].set_color(SECONDARY)
        self.ly.safe_place(gen_sol, DOWN, anchor=title3, buff=0.5)
        self.play(Write(gen_sol), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(gen_sol), run_time=FAST)

        # Apply ICs
        self.add_subcaption(
            "Now apply the initial conditions. First: y of zero equals "
            "C1 plus C2 equals 1. Second: y prime of zero equals C1 "
            "plus 2 C2 equals 0.",
            duration=24,
        )

        title4 = self.ly.title("Apply Initial Conditions")

        ic_items = [
            MathTex(
                r"y(0)", r"=", r"C_1", r"+", r"C_2", r"=", r"1",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            MathTex(
                r"y'(0)", r"=", r"C_1", r"+", r"2C_2", r"=", r"0",
                font_size=HEADING_SIZE, color=WHITE,
            ),
        ]
        ic_items[0][0].set_color(PRIMARY)
        ic_items[0][6].set_color(RED)
        ic_items[1][0].set_color(SECONDARY)
        ic_items[1][6].set_color(RED)

        fitted, overflow = self.ly.stack_down(ic_items, start_from=title4, spacing=0.4)
        for item in ic_items:
            self.play(Write(item), run_time=NORMAL)
            self.wait(0.5)

        self.play(FadeOut(*ic_items), run_time=FAST)

        # Solve
        self.add_subcaption(
            "From the second equation, C1 equals negative 2 C2. "
            "Substituting into the first: negative 2 C2 plus C2 equals 1, "
            "so C2 equals negative 1 and C1 equals 2.",
            duration=24,
        )

        title5 = self.ly.title("Solve for Constants")

        result = MathTex(
            r"C_1", r"=", r"2",
            r"\qquad",
            r"C_2", r"=", r"-1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        result[0].set_color(PRIMARY)
        result[2].set_color(ACCENT)
        result[4].set_color(SECONDARY)
        result[6].set_color(ACCENT)
        self.ly.safe_place(result, DOWN, anchor=title5, buff=0.5)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(result), run_time=FAST)

        # Particular solution
        self.add_subcaption(
            "The particular solution is y equals 2 e to the x minus "
            "e to the 2 x. This is the unique solution satisfying "
            "both initial conditions.",
            duration=20,
        )

        title6 = self.ly.title("Particular Solution")

        part_sol = MathTex(
            r"y", r"=", r"2\,e^{x}", r"-", r"e^{2x}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        part_sol[2].set_color(PRIMARY)
        part_sol[4].set_color(SECONDARY)
        self.ly.center_in_content(part_sol)
        self.play(Write(part_sol), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ── Scene 4: Example 2 — Repeated Root ─────────────────────
    def scene4_example_repeated(self):
        self.add_subcaption(
            "Next example: y double prime minus 4 y prime plus 4 y "
            "equals zero, with y of zero equals 3 and y prime of zero "
            "equals 5.",
            duration=24,
        )

        self.ly.section_divider(3, "Example: Repeated Root")
        self.wait(0.5)

        title = self.ly.title("The IVP")

        ode = MathTex(
            r"y''", r"-", r"4\,y'", r"+", r"4\,y", r"= 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ode[0].set_color(PRIMARY)
        ode[2].set_color(SECONDARY)
        ode[4].set_color(ACCENT)
        self.ly.safe_place(ode, DOWN, anchor=title, buff=0.5)
        self.play(Write(ode), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ode), run_time=FAST)

        # General solution
        self.add_subcaption(
            "From before, the characteristic equation gives a repeated "
            "root r equals 2. The general solution is y equals C1 "
            "e to the 2 x plus C2 x e to the 2 x.",
            duration=24,
        )

        title2 = self.ly.title("General Solution")

        gen_sol = MathTex(
            r"y", r"=", r"C_1\,e^{2x}",
            r"+", r"C_2\,x\,e^{2x}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        gen_sol[2].set_color(PRIMARY)
        gen_sol[4].set_color(SECONDARY)
        self.ly.safe_place(gen_sol, DOWN, anchor=title2, buff=0.5)
        self.play(Write(gen_sol), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(gen_sol), run_time=FAST)

        # Apply ICs
        self.add_subcaption(
            "First condition: y of zero equals C1 equals 3. "
            "For the derivative, use the product rule: y prime equals "
            "2 C1 e to the 2 x plus C2 e to the 2 x plus 2 C2 x e to "
            "the 2 x. At x equals zero, this gives 2 C1 plus C2 equals 5.",
            duration=24,
        )

        title3 = self.ly.title("Apply ICs")

        ic_items = [
            MathTex(
                r"y(0)", r"=", r"C_1", r"=", r"3",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            MathTex(
                r"y'(0)", r"=", r"2C_1", r"+", r"C_2", r"=", r"5",
                font_size=HEADING_SIZE, color=WHITE,
            ),
        ]
        ic_items[0][0].set_color(PRIMARY)
        ic_items[0][4].set_color(RED)
        ic_items[1][0].set_color(SECONDARY)
        ic_items[1][6].set_color(RED)

        fitted, overflow = self.ly.stack_down(ic_items, start_from=title3, spacing=0.4)
        for item in ic_items:
            self.play(Write(item), run_time=NORMAL)
            self.wait(0.5)

        self.play(FadeOut(*ic_items), run_time=FAST)

        # Solve
        self.add_subcaption(
            "Since C1 is 3, the second equation gives 6 plus C2 "
            "equals 5, so C2 equals negative 1. The particular solution "
            "is y equals 3 e to the 2 x minus x e to the 2 x.",
            duration=24,
        )

        title4 = self.ly.title("Solve")

        part_sol = MathTex(
            r"y", r"=", r"3\,e^{2x}", r"-", r"x\,e^{2x}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        part_sol[2].set_color(PRIMARY)
        part_sol[4].set_color(SECONDARY)
        self.ly.center_in_content(part_sol)
        self.play(Write(part_sol), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ── Scene 5: Example 3 — Complex Roots ────────────────────
    def scene5_example_complex(self):
        self.add_subcaption(
            "Final example with complex roots: y double prime plus 2 y "
            "prime plus 5 y equals zero, with y of zero equals 0 and "
            "y prime of zero equals 1.",
            duration=24,
        )

        self.ly.section_divider(4, "Example: Complex Roots")
        self.wait(0.5)

        title = self.ly.title("The IVP")

        ode = MathTex(
            r"y''", r"+", r"2\,y'", r"+", r"5\,y", r"= 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ode[0].set_color(PRIMARY)
        ode[2].set_color(SECONDARY)
        ode[4].set_color(ACCENT)
        self.ly.safe_place(ode, DOWN, anchor=title, buff=0.5)
        self.play(Write(ode), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ode), run_time=FAST)

        # General solution
        self.add_subcaption(
            "From Video 58, the roots are negative 1 plus or minus 2 i, "
            "so alpha equals negative 1 and beta equals 2. The general "
            "solution is y equals e to the negative x times C1 cosine "
            "2 x plus C2 sine 2 x.",
            duration=24,
        )

        title2 = self.ly.title("General Solution")

        gen_sol = MathTex(
            r"y", r"=", r"e^{-x}",
            r"\!\left(", r"C_1\cos 2x",
            r"+", r"C_2\sin 2x", r"\right)",
            font_size=TITLE_SIZE, color=WHITE,
        )
        gen_sol[2].set_color(ACCENT)
        gen_sol[3].set_color(PRIMARY)
        gen_sol[5].set_color(SECONDARY)
        self.ly.safe_place(gen_sol, DOWN, anchor=title2, buff=0.5)
        self.play(Write(gen_sol), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(gen_sol), run_time=FAST)

        # IC 1
        self.add_subcaption(
            "First condition: y of zero equals e to the 0 times C1 "
            "cosine 0 plus C2 sine 0. Cosine 0 is 1 and sine 0 is 0, "
            "so y of zero equals C1 equals 0.",
            duration=24,
        )

        title3 = self.ly.title("IC 1")

        ic1 = MathTex(
            r"y(0)", r"=", r"C_1", r"=", r"0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ic1[0].set_color(PRIMARY)
        ic1[4].set_color(RED)
        self.ly.safe_place(ic1, DOWN, anchor=title3, buff=0.5)
        self.play(Write(ic1), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ic1), run_time=FAST)

        # IC 2 — the derivative
        self.add_subcaption(
            "For the derivative, we need the chain rule. The derivative "
            "of e to the negative x is negative e to the negative x. "
            "At x equals zero, y prime of zero equals negative C1 plus "
            "2 C2. Since C1 is 0, we get 2 C2 equals 1, so C2 equals one half.",
            duration=24,
        )

        title4 = self.ly.title("IC 2")

        ic2 = MathTex(
            r"y'(0)", r"=", r"-C_1", r"+", r"2\,C_2",
            r"=", r"1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ic2[0].set_color(SECONDARY)
        ic2[6].set_color(RED)
        self.ly.safe_place(ic2, DOWN, anchor=title4, buff=0.5)
        self.play(Write(ic2), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ic2), run_time=FAST)

        # Particular solution
        self.add_subcaption(
            "The particular solution is y equals one half e to the "
            "negative x sine 2 x. A pure oscillation decaying over time. "
            "It starts at zero with velocity 1 and gradually dies down.",
            duration=24,
        )

        title5 = self.ly.title("Particular Solution")

        part_sol = MathTex(
            r"y", r"=", r"\frac{1}{2}",
            r"\,e^{-x}", r"\sin(2x)",
            font_size=TITLE_SIZE, color=WHITE,
        )
        part_sol[2].set_color(ACCENT)
        part_sol[3].set_color(ACCENT)
        part_sol[4].set_color(SECONDARY)
        self.ly.center_in_content(part_sol)
        self.play(Write(part_sol), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ── Scene 6: The General Method ─────────────────────────────
    def scene6_method(self):
        self.add_subcaption(
            "Let us formalize the approach. Every second-order IVP "
            "follows the same four steps.",
            duration=12,
        )

        self.ly.section_divider(5, "The General Method")
        self.wait(0.5)

        title = self.ly.title("Four Steps")

        steps = [
            Text("1. Write the characteristic equation", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Find the general solution from the roots", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Compute y'(x) using the chain rule", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Plug x=0 into both → solve 2×2 system", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(steps, start_from=title)
        self.wait(1)

        self.ly.clear()

    # ── Scene 7: Summary + Preview ─────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "To summarize: a second-order IVP gives us a specific "
            "solution by fixing the two arbitrary constants. We always "
            "get a 2 by 2 linear system from the initial conditions.",
            duration=24,
        )

        title = self.ly.title("Summary")

        items = [
            Text("Second-order IVP needs TWO initial conditions", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("y(0) and y'(0) determine C1 and C2 uniquely", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Same method for all three root types", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()

        self.add_subcaption(
            "Next time: what happens when the right side is not zero? "
            "Non-homogeneous equations and the method of undetermined "
            "coefficients. See you then!",
            duration=20,
        )

        play_outro(
            self,
            next_video="Non-Homogeneous Equations",
            next_playlist="Ordinary Differential Equations",
        )
