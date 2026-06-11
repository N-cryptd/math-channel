"""
Video 60: Non-Homogeneous Second-Order Equations
Ordinary Differential Equations -- Video 6 of N

Covers: complementary + particular solution structure, method of undetermined
coefficients, guess rules, polynomial and exponential forcing examples,
coefficient matching.

Render draft:  manim -ql scripts/undergraduate/video-60-non-homogeneous.py Video60_NonHomogeneous
Render final:  manim -qh scripts/undergraduate/video-60-non-homogeneous.py Video60_NonHomogeneous
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


class Video60_NonHomogeneous(Scene):
    """Full video: Non-Homogeneous Second-Order Equations."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_structure()
        self.scene3_method()
        self.scene4_example_poly()
        self.scene5_example_exp()
        self.scene6_summary()

    # ── Scene 1: Hook — When the Right Side Is Not Zero ─────────
    def scene1_hook(self):
        self.add_subcaption(
            "So far, every equation has had zero on the right side. "
            "But in the real world, external forces act on systems. "
            "A spring with a motor, a circuit with a voltage source. "
            "These give non-zero right sides.",
            duration=24,
        )
        play_intro(self, "Non-Homogeneous Equations",
                   "Ordinary Differential Equations")

        title = self.ly.title("Beyond Zero")

        nh_form = MathTex(
            r"a\,y''", r"+", r"b\,y'", r"+", r"c\,y", r"=", r"f(x)",
            font_size=TITLE_SIZE, color=WHITE,
        )
        nh_form[0].set_color(PRIMARY)
        nh_form[2].set_color(SECONDARY)
        nh_form[4].set_color(ACCENT)
        nh_form[6].set_color(RED)
        self.ly.safe_place(nh_form, DOWN, anchor=title, buff=0.5)
        self.play(Write(nh_form), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(nh_form), run_time=FAST)

        self.add_subcaption(
            "The key insight is that the general solution splits into "
            "two parts: the complementary solution from the homogeneous "
            "case, plus a particular solution that accounts for the forcing.",
            duration=24,
        )

        title2 = self.ly.title("The Big Idea")

        structure = MathTex(
            r"y", r"=", r"y_c", r"+", r"y_p",
            font_size=TITLE_SIZE, color=WHITE,
        )
        structure[2].set_color(PRIMARY)
        structure[4].set_color(ACCENT)
        self.ly.safe_place(structure, DOWN, anchor=title2, buff=0.5)
        self.play(Write(structure), run_time=NORMAL)
        self.wait(1)

        self.ly.clear()

    # ── Scene 2: Structure of the Solution ──────────────────────
    def scene2_structure(self):
        self.add_subcaption(
            "Let us define both parts. The complementary function y_c "
            "is the general solution to the homogeneous equation, "
            "with both arbitrary constants. The particular solution "
            "y_p is any single solution to the non-homogeneous equation.",
            duration=24,
        )

        self.ly.section_divider(1, "Complementary + Particular")
        self.wait(0.5)

        title = self.ly.title("Definitions")

        items = [
            Text("y_c: homogeneous solution (has C1, C2)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("y_p: any solution to the full equation", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("y = y_c + y_p: the full general solution", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()

    # ── Scene 3: Method of Undetermined Coefficients ────────────
    def scene3_method(self):
        self.add_subcaption(
            "How do we find a particular solution? The method of "
            "undetermined coefficients says: guess the form of y_p "
            "based on the form of f of x, then plug in and solve "
            "for the coefficients.",
            duration=24,
        )

        self.ly.section_divider(2, "Method of Undetermined Coefficients")
        self.wait(0.5)

        title = self.ly.title("Guess Rules")

        items = [
            Text("f(x) = polynomial → guess polynomial (same degree)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("f(x) = e^{kx} → guess A·e^{kx}", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("f(x) = sin(kx) or cos(kx) → guess A·sin + B·cos", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.play(FadeOut(items[-1]), run_time=FAST)

        # Caution
        self.add_subcaption(
            "Important caveat: if your guess overlaps with part of the "
            "complementary solution, multiply your guess by x. "
            "If it still overlaps, multiply by x squared.",
            duration=24,
        )

        caution = Text(
            "Caution: if guess overlaps y_c, multiply by x!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(caution, DOWN, anchor=items[-2], buff=0.5)
        self.play(FadeIn(caution, shift=LEFT*0.15), run_time=NORMAL)
        self.wait(1)

        self.ly.clear()

    # ── Scene 4: Example 1 — Polynomial Forcing ───────────────
    def scene4_example_poly(self):
        self.add_subcaption(
            "Let us solve y double prime minus 3 y prime plus 2 y "
            "equals 4 x squared.",
            duration=12,
        )

        self.ly.section_divider(3, "Example: Polynomial Forcing")
        self.wait(0.5)

        title = self.ly.title("The Equation")

        ode = MathTex(
            r"y''", r"-", r"3\,y'", r"+", r"2\,y", r"=", r"4x^2",
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

        # Complementary solution
        self.add_subcaption(
            "First, find the complementary solution. The characteristic "
            "equation is r squared minus 3 r plus 2 equals zero, giving "
            "r equals 1 and r equals 2. So y sub c equals C1 e to the x "
            "plus C2 e to the 2 x.",
            duration=24,
        )

        title2 = self.ly.title("Complementary Solution")

        yc = MathTex(
            r"y_c", r"=", r"C_1\,e^{x}", r"+", r"C_2\,e^{2x}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        yc[0].set_color(PRIMARY)
        yc[2].set_color(PRIMARY)
        yc[4].set_color(PRIMARY)
        self.ly.safe_place(yc, DOWN, anchor=title2, buff=0.5)
        self.play(Write(yc), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(yc), run_time=FAST)

        # Guess y_p
        self.add_subcaption(
            "Since the right side is 4 x squared, a degree 2 polynomial, "
            "we guess y sub p equals A x squared plus B x plus C. "
            "Plug this in and match coefficients.",
            duration=24,
        )

        title3 = self.ly.title("Guess: y_p")

        yp_guess = MathTex(
            r"y_p", r"=", r"A\,x^2", r"+", r"B\,x", r"+", r"C",
            font_size=HEADING_SIZE, color=WHITE,
        )
        yp_guess[0].set_color(ACCENT)
        yp_guess[2].set_color(ACCENT)
        self.ly.safe_place(yp_guess, DOWN, anchor=title3, buff=0.5)
        self.play(Write(yp_guess), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(yp_guess), run_time=FAST)

        # Match coefficients
        self.add_subcaption(
            "Taking derivatives: y p prime is 2 A x plus B, and y p "
            "double prime is 2 A. Substituting and collecting like terms, "
            "we match coefficients. From the x squared term: 2 A equals "
            "4, so A equals 2. From the x term: negative 6 A plus 2 B "
            "equals 0, so B equals 6. From the constant: 2 A minus 3 B "
            "plus 2 C equals 0, so C equals 8.",
            duration=24,
        )

        title4 = self.ly.title("Match Coefficients")

        result = MathTex(
            r"y_p", r"=", r"2\,x^2", r"+", r"6\,x", r"+", r"8",
            font_size=HEADING_SIZE, color=WHITE,
        )
        result[0].set_color(ACCENT)
        result[2].set_color(ACCENT)
        self.ly.safe_place(result, DOWN, anchor=title4, buff=0.5)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(result), run_time=FAST)

        # Full solution
        self.add_subcaption(
            "The full general solution is y equals C1 e to the x plus "
            "C2 e to the 2 x plus 2 x squared plus 6 x plus 8.",
            duration=16,
        )

        title5 = self.ly.title("Full Solution")

        full = MathTex(
            r"y", r"=", r"C_1\,e^{x}", r"+", r"C_2\,e^{2x}",
            r"+", r"2x^2", r"+", r"6x", r"+", r"8",
            font_size=HEADING_SIZE, color=WHITE,
        )
        full[2].set_color(PRIMARY)
        full[4].set_color(PRIMARY)
        full[6].set_color(ACCENT)
        full[8].set_color(ACCENT)
        full[10].set_color(ACCENT)
        self.ly.center_in_content(full)
        self.play(Write(full), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ── Scene 5: Example 2 — Exponential Forcing ────────────────
    def scene5_example_exp(self):
        self.add_subcaption(
            "Next: y double prime plus y prime minus 2 y equals "
            "3 e to the 3 x.",
            duration=12,
        )

        self.ly.section_divider(4, "Example: Exponential Forcing")
        self.wait(0.5)

        title = self.ly.title("The Equation")

        ode = MathTex(
            r"y''", r"+", r"y'", r"-", r"2\,y", r"=", r"3\,e^{3x}",
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

        # Complementary solution
        self.add_subcaption(
            "The characteristic equation is r squared plus r minus 2 "
            "equals 0, which factors as r plus 2 times r minus 1 equals 0. "
            "Roots are r equals 1 and r equals negative 2.",
            duration=24,
        )

        title2 = self.ly.title("Complementary Solution")

        yc = MathTex(
            r"y_c", r"=", r"C_1\,e^{x}", r"+", r"C_2\,e^{-2x}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        yc[0].set_color(PRIMARY)
        yc[2].set_color(PRIMARY)
        yc[4].set_color(PRIMARY)
        self.ly.safe_place(yc, DOWN, anchor=title2, buff=0.5)
        self.play(Write(yc), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(yc), run_time=FAST)

        # Guess y_p
        self.add_subcaption(
            "The forcing is 3 e to the 3 x. Since 3 is not a root of the "
            "characteristic equation, our guess is simply y sub p equals "
            "A times e to the 3 x.",
            duration=24,
        )

        title3 = self.ly.title("Guess: y_p")

        yp_guess = MathTex(
            r"y_p", r"=", r"A\,e^{3x}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        yp_guess[0].set_color(ACCENT)
        yp_guess[2].set_color(ACCENT)
        self.ly.safe_place(yp_guess, DOWN, anchor=title3, buff=0.5)
        self.play(Write(yp_guess), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(yp_guess), run_time=FAST)

        # Solve for A
        self.add_subcaption(
            "The derivatives are y p prime equals 3 A e to the 3 x and "
            "y p double prime equals 9 A e to the 3 x. Substituting: "
            "9 A plus 3 A minus 2 A equals 3. So 10 A equals 3, giving "
            "A equals 3 tenths.",
            duration=24,
        )

        title4 = self.ly.title("Solve for A")

        solve = MathTex(
            r"9A", r"+", r"3A", r"-", r"2A", r"=", r"3",
            r"\;\Rightarrow\;", r"10A=3",
            r"\;\Rightarrow\;", r"A=\tfrac{3}{10}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        solve[0].set_color(ACCENT)
        solve[2].set_color(ACCENT)
        solve[4].set_color(ACCENT)
        solve[6].set_color(RED)
        solve[10].set_color(ACCENT)
        self.ly.safe_place(solve, DOWN, anchor=title4, buff=0.5)
        self.play(Write(solve), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(solve), run_time=FAST)

        # Full solution
        self.add_subcaption(
            "The full solution is y equals C1 e to the x plus C2 e "
            "to the negative 2 x plus three tenths e to the 3 x.",
            duration=16,
        )

        title5 = self.ly.title("Full Solution")

        full = MathTex(
            r"y", r"=", r"C_1\,e^{x}",
            r"+", r"C_2\,e^{-2x}",
            r"+", r"\tfrac{3}{10}\,e^{3x}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        full[2].set_color(PRIMARY)
        full[4].set_color(PRIMARY)
        full[6].set_color(ACCENT)
        self.ly.center_in_content(full)
        self.play(Write(full), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ── Scene 6: Summary + Preview ─────────────────────────────
    def scene6_summary(self):
        self.add_subcaption(
            "To summarize: for a non-homogeneous second-order ODE, "
            "the solution is y complementary plus y particular. "
            "Find y c from the characteristic equation. Find y p by "
            "guessing based on the forcing function and matching coefficients.",
            duration=24,
        )

        title = self.ly.title("Summary")

        items = [
            Text("Solution: y = y_c + y_p", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("y_c from characteristic equation", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("y_p by guessing (match coefficients)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()

        self.add_subcaption(
            "The method of undetermined coefficients works when the "
            "forcing function is a polynomial, exponential, or "
            "trigonometric. For more complex forcing, we use "
            "variation of parameters. That is next time.",
            duration=20,
        )

        play_outro(
            self,
            next_video="Variation of Parameters",
            next_playlist="Ordinary Differential Equations",
        )
