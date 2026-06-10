"""
Video 56: First-Order Separable Equations
Ordinary Differential Equations -- Video 2 of N

Covers: separable form dy/dx = g(x)h(y), separation technique,
exponential growth/decay example, Newton's Law of Cooling example,
implicit vs explicit solutions, recognition of separable equations.

Render draft:  manim -ql scripts/undergraduate/video-56-separable-equations.py Video56_SeparableEquations
Render final:  manim -qh scripts/undergraduate/video-56-separable-equations.py Video56_SeparableEquations
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


class Video56_SeparableEquations(Scene):
    """Full video: First-Order Separable Equations."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_technique()
        self.scene4_example1()
        self.scene5_example2()
        self.scene6_summary()

    # ── Scene 1: Hook — We Can Actually Solve This ──────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Remember the last video? We had dN over dt equals r times N, "
            "the population growth equation. We called it a differential "
            "equation, but we never actually solved it. Today we learn how.",
            duration=24,
        )
        play_intro(self, "Separable Equations",
                   "Ordinary Differential Equations")

        title = self.ly.title("From Last Time...")

        # Recall the DE
        recall_eq = MathTex(
            r"\frac{dN}{dt}", r"=", r"rN",
            font_size=HEADING_SIZE, color=WHITE,
        )
        recall_eq[0].set_color(PRIMARY)
        recall_eq[2].set_color(ACCENT)
        self.ly.safe_place(recall_eq, DOWN, anchor=title, buff=0.5)
        self.play(Write(recall_eq), run_time=NORMAL)
        self.wait(1)

        self.ly.clear()

        self.add_subcaption(
            "Here is the trick. If the right side is a product of something "
            "involving only t and something involving only N, we can split "
            "the variables apart. Move all the N terms to the left with dN, "
            "and all the t terms to the right with dt.",
            duration=24,
        )

        title2 = self.ly.title("The Trick: Split the Variables")

        # Separated form
        sep_eq = MathTex(
            r"\frac{dN}{N}", r"=", r"r \, dt",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sep_eq[0].set_color(PRIMARY)
        sep_eq[2].set_color(SECONDARY)
        self.ly.safe_place(sep_eq, DOWN, anchor=title2, buff=0.5)
        self.play(TransformFromCopy(recall_eq, sep_eq), run_time=SLOW)
        self.wait(1)

        # Integrate
        self.play(FadeOut(sep_eq), run_time=FAST)

        int_eq = MathTex(
            r"\int", r"\frac{dN}{N}", r"=",
            r"\int", r"r \, dt",
            font_size=HEADING_SIZE, color=WHITE,
        )
        int_eq[0].set_color(ACCENT)
        int_eq[1].set_color(PRIMARY)
        int_eq[4].set_color(SECONDARY)
        self.ly.safe_place(int_eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(int_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(int_eq), run_time=FAST)

        # Solution
        sol_eq = MathTex(
            r"\ln|N|", r"=", r"rt + C",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sol_eq[0].set_color(PRIMARY)
        sol_eq[2].set_color(ACCENT)
        self.ly.safe_place(sol_eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(sol_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(sol_eq), run_time=FAST)

        # Final form
        final_eq = MathTex(
            r"N(t)", r"=", r"Ce^{rt}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        final_eq[0].set_color(PRIMARY)
        final_eq[2].set_color(ACCENT)
        self.ly.center_in_content(final_eq)
        self.play(Write(final_eq), run_time=SLOW)
        self.wait(0.5)

        label = Text(
            "Exponential growth — our first solution!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(label, DOWN, anchor=final_eq, buff=0.4)
        self.play(FadeIn(label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 2: Definition — What Makes an Equation Separable? ───
    def scene2_definition(self):
        self.add_subcaption(
            "A first-order differential equation is called separable if it "
            "can be written so that the x terms and y terms are on different "
            "sides of the equation. Formally, dy/dx equals g of x times "
            "h of y, where g only uses x and h only uses y.",
            duration=24,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("The Separable Form")

        # Formal definition
        form = MathTex(
            r"\frac{dy}{dx}", r"=", r"g(x)", r"\cdot", r"h(y)",
            font_size=TITLE_SIZE, color=WHITE,
        )
        form[0].set_color(PRIMARY)
        form[2].set_color(SECONDARY)
        form[4].set_color(ACCENT)
        self.ly.safe_place(form, DOWN, anchor=title, buff=0.5)
        self.play(Write(form), run_time=SLOW)
        self.wait(1)

        # Explanation
        self.play(FadeOut(form), run_time=FAST)

        self.add_subcaption(
            "The key test: can you algebraically move all the y terms to "
            "the left side with dy, and all the x terms to the right side "
            "with dx? If yes, it's separable. Let's check some examples.",
            duration=24,
        )

        title2 = self.ly.title("The Separability Test")

        test = Text(
            "Can you split x and y to opposite sides?",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(test)
        self.play(FadeIn(test, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(test), run_time=FAST)

        # Separable examples
        sep_label = Text(
            "Separable:",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(sep_label, DOWN, anchor=title2, buff=0.4)
        self.play(FadeIn(sep_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        sep_ex = MathTex(
            r"\frac{dy}{dx}", r"=", r"x \cdot y",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sep_ex[0].set_color(PRIMARY)
        sep_ex[2].set_color(ACCENT)
        self.ly.safe_place(sep_ex, DOWN, anchor=sep_label, buff=0.3)
        self.play(Write(sep_ex), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(sep_label), FadeOut(sep_ex), run_time=FAST)

        # Non-separable examples
        nsep_label = Text(
            "NOT separable:",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(nsep_label, DOWN, anchor=title2, buff=0.4)
        self.play(FadeIn(nsep_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        nsep_ex = MathTex(
            r"\frac{dy}{dx}", r"=", r"x + y",
            font_size=HEADING_SIZE, color=WHITE,
        )
        nsep_ex[0].set_color(PRIMARY)
        nsep_ex[2].set_color(RED)
        self.ly.safe_place(nsep_ex, DOWN, anchor=nsep_label, buff=0.3)
        self.play(Write(nsep_ex), run_time=NORMAL)
        self.wait(0.5)

        why = Text(
            "Can't split x and y apart!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(why, DOWN, anchor=nsep_ex, buff=0.3)
        self.play(FadeIn(why, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 3: The Separation Technique ────────────────────────
    def scene3_technique(self):
        self.add_subcaption(
            "Now for the method. Once you confirm an equation is separable, "
            "follow these four steps. Step one: identify g of x and h of y. "
            "Step two: separate the variables. Step three: integrate both "
            "sides. Step four: solve for y if possible.",
            duration=24,
        )
        self.ly.section_divider(2, "The Technique")

        title = self.ly.title("Four Steps to Solve")

        steps = [
            Text(
                "1. Write as dy/dx = g(x) \u00b7 h(y)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. Separate: dy/h(y) = g(x) dx",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3. Integrate both sides",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "4. Solve for y (if possible)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(steps, start_from=title)
        self.wait(2)

        self.ly.clear()

        # Visual: animated separation
        self.add_subcaption(
            "Let's see step two in action. We take the h of y term and "
            "move it to the left side with dy. We take the g of x term "
            "and move it to the right side with dx. Think of it like "
            "sorting: y things go left, x things go right.",
            duration=24,
        )

        title2 = self.ly.title("The Key Step: Separation")

        # Starting equation
        start_eq = MathTex(
            r"\frac{dy}{dx}", r"=", r"g(x)", r"\cdot", r"h(y)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        start_eq[0].set_color(PRIMARY)
        start_eq[2].set_color(SECONDARY)
        start_eq[4].set_color(ACCENT)
        self.ly.safe_place(start_eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(start_eq), run_time=SLOW)
        self.wait(1)

        self.play(FadeOut(start_eq), run_time=FAST)

        # After separation
        end_eq = MathTex(
            r"\frac{1}{h(y)}", r"dy", r"=",
            r"g(x)", r"dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        end_eq[0].set_color(ACCENT)
        end_eq[1].set_color(PRIMARY)
        end_eq[3].set_color(SECONDARY)
        end_eq[4].set_color(PRIMARY)
        self.ly.safe_place(end_eq, DOWN, anchor=title2, buff=0.5)
        self.play(TransformFromCopy(start_eq, end_eq), run_time=SLOW)
        self.wait(0.5)

        # Then integrate
        self.play(FadeOut(end_eq), run_time=FAST)

        int_eq = MathTex(
            r"\int", r"\frac{1}{h(y)}", r"dy", r"=",
            r"\int", r"g(x)", r"dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        int_eq[0].set_color(ACCENT)
        int_eq[1].set_color(ACCENT)
        int_eq[3].set_color(PRIMARY)
        int_eq[5].set_color(ACCENT)
        int_eq[6].set_color(PRIMARY)
        self.ly.safe_place(int_eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(int_eq), run_time=SLOW)
        self.wait(0.5)

        # Add + C
        self.play(FadeOut(int_eq), run_time=FAST)

        c_note = Text(
            "Don't forget the + C!",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(c_note)
        self.play(FadeIn(c_note, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 4: Example 1 — Exponential Growth/Decay ─────────────
    def scene4_example1(self):
        self.add_subcaption(
            "Let's work through a complete example. Solve dy/dx equals "
            "negative 0.1 times y. This models radioactive decay, "
            "population decline, or any process that decreases "
            "proportionally to its current value.",
            duration=24,
        )
        self.ly.section_divider(3, "Example: Exponential Decay")

        title = self.ly.title("dy/dx = -0.1y")

        # Step 1: Already separable
        step1 = Text(
            "Step 1: Already separable!  g(x) = -0.1,  h(y) = y",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(step1, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(step1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(step1), run_time=FAST)

        # Step 2: Separate
        self.add_subcaption(
            "Step two, separate. Move the y to the left with dy, and "
            "the negative 0.1 and dx stay on the right.",
            duration=20,
        )

        step2_label = Text(
            "Step 2: Separate the variables",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(step2_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(step2_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        step2_eq = MathTex(
            r"\frac{dy}{y}", r"=", r"-0.1 \, dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        step2_eq[0].set_color(PRIMARY)
        step2_eq[2].set_color(SECONDARY)
        self.ly.safe_place(step2_eq, DOWN, anchor=step2_label, buff=0.3)
        self.play(Write(step2_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(step2_label), FadeOut(step2_eq), run_time=FAST)

        # Step 3: Integrate
        self.add_subcaption(
            "Step three, integrate. The left side integrates to the "
            "natural log of absolute y. The right side integrates to "
            "negative 0.1 x plus a constant.",
            duration=20,
        )

        step3_label = Text(
            "Step 3: Integrate both sides",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(step3_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(step3_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        step3_eq = MathTex(
            r"\ln|y|", r"=", r"-0.1x", r"+ C",
            font_size=HEADING_SIZE, color=WHITE,
        )
        step3_eq[0].set_color(PRIMARY)
        step3_eq[2].set_color(SECONDARY)
        step3_eq[3].set_color(ACCENT)
        self.ly.safe_place(step3_eq, DOWN, anchor=step3_label, buff=0.3)
        self.play(Write(step3_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(step3_label), FadeOut(step3_eq), run_time=FAST)

        # Step 4: Solve for y
        self.add_subcaption(
            "Step four, solve for y. Exponentiate both sides to remove "
            "the natural log. We get y equals e to the C times e to the "
            "negative 0.1 x. Since e to the C is just another constant, "
            "we write it as a capital C.",
            duration=24,
        )

        step4_label = Text(
            "Step 4: Solve for y",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(step4_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(step4_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        step4_eq = MathTex(
            r"y", r"=", r"Ce^{-0.1x}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        step4_eq[0].set_color(PRIMARY)
        step4_eq[2].set_color(ACCENT)
        self.ly.safe_place(step4_eq, DOWN, anchor=step4_label, buff=0.3)
        self.play(Write(step4_eq), run_time=SLOW)
        self.wait(0.5)

        # Highlight
        sol_label = Text(
            "Exponential decay!",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(sol_label, DOWN, anchor=step4_eq, buff=0.4)
        self.play(FadeIn(sol_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 5: Example 2 — Newton's Law of Cooling ──────────────
    def scene5_example2(self):
        self.add_subcaption(
            "Now a real-world example. A cup of coffee at 90 degrees Celsius "
            "sits in a room at 20 degrees. Newton's Law of Cooling says the "
            "rate of cooling is proportional to the temperature difference "
            "between the object and its surroundings.",
            duration=24,
        )
        self.ly.section_divider(4, "Example: Newton's Cooling")

        title = self.ly.title("Coffee Cooling Problem")

        # Setup
        setup_text = Text(
            "Coffee at 90\u00b0C, room at 20\u00b0C",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(setup_text, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(setup_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(setup_text), run_time=FAST)

        # The DE
        self.add_subcaption(
            "The differential equation is dT/dt equals negative k times "
            "the quantity T minus 20, where k is a positive constant "
            "called the cooling constant. When T is much larger than 20, "
            "the cooling is fast. As T approaches 20, it slows down.",
            duration=24,
        )

        de_eq = MathTex(
            r"\frac{dT}{dt}", r"=", r"-k(T - 20)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        de_eq[0].set_color(PRIMARY)
        de_eq[2].set_color(ACCENT)
        self.ly.safe_place(de_eq, DOWN, anchor=title, buff=0.5)
        self.play(Write(de_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(de_eq), run_time=FAST)

        # Substitution
        self.add_subcaption(
            "Here's a clever substitution. Let u equal T minus 20. Then "
            "du/dt also equals dT/dt, since the 20 is a constant. The "
            "equation becomes du/dt equals negative k times u, which we "
            "already know how to solve!",
            duration=24,
        )

        title2 = self.ly.title("Substitution: u = T - 20")

        sub_eq = MathTex(
            r"\frac{du}{dt}", r"=", r"-ku",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sub_eq[0].set_color(PRIMARY)
        sub_eq[2].set_color(ACCENT)
        self.ly.safe_place(sub_eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(sub_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(sub_eq), run_time=FAST)

        # Quick solve
        self.add_subcaption(
            "Using the same separation technique, du/u equals negative k "
            "dt. Integrating gives ln|u| equals negative kt plus C, so "
            "u equals C times e to the negative kt. Substituting back, "
            "T equals 20 plus C times e to the negative kt.",
            duration=24,
        )

        title3 = self.ly.title("Solving")

        quick_eq = MathTex(
            r"u", r"=", r"Ce^{-kt}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        quick_eq[0].set_color(ACCENT)
        quick_eq[2].set_color(SECONDARY)
        self.ly.safe_place(quick_eq, DOWN, anchor=title3, buff=0.5)
        self.play(Write(quick_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(quick_eq), run_time=FAST)

        # Final form
        title4 = self.ly.title("Back to T")

        final_eq = MathTex(
            r"T(t)", r"=", r"20 + Ce^{-kt}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        final_eq[0].set_color(PRIMARY)
        final_eq[2].set_color(ACCENT)
        self.ly.safe_place(final_eq, DOWN, anchor=title4, buff=0.5)
        self.play(Write(final_eq), run_time=SLOW)
        self.wait(0.5)

        # Initial condition
        self.play(FadeOut(final_eq), run_time=FAST)

        self.add_subcaption(
            "Now apply the initial condition. At t equals zero, T is 90. "
            "So 90 equals 20 plus C, which gives C equals 70. Our complete "
            "solution is T of t equals 20 plus 70 times e to the negative kt.",
            duration=24,
        )

        ic_label = Text(
            "T(0) = 90:  so  C = 70",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(ic_label, DOWN, anchor=title4, buff=0.4)
        self.play(FadeIn(ic_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ic_label), run_time=FAST)

        answer = MathTex(
            r"T(t)", r"=", r"20 + 70e^{-kt}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        answer[0].set_color(PRIMARY)
        answer[2].set_color(ACCENT)
        self.ly.safe_place(answer, DOWN, anchor=title4, buff=0.5)
        self.play(Write(answer), run_time=SLOW)
        self.wait(0.5)

        interp = Text(
            "The coffee approaches room temperature exponentially.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(interp, DOWN, anchor=answer, buff=0.3)
        self.play(FadeIn(interp, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 6: Summary + Preview ───────────────────────────────
    def scene6_summary(self):
        self.add_subcaption(
            "Let's recap. A separable differential equation has the form "
            "dy/dx equals g of x times h of y. The method is: separate "
            "the variables, integrate both sides, and solve for y. Not "
            "every equation is separable, but when it is, this method "
            "always works.",
            duration=24,
        )

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "Separable form:  dy/dx = g(x) \u00b7 h(y)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Separate:  dy/h(y) = g(x) dx",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Integrate both sides, then solve for y",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Always include the constant C",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        self.ly.clear()

        self.add_subcaption(
            "Next time, we'll tackle first-order linear equations, which "
            "use a different technique called the integrating factor. "
            "It handles equations that are not separable, like dy/dx "
            "plus p of x times y equals q of x.",
            duration=24,
        )

        title2 = self.ly.title("Coming Up Next")

        next_text = Text(
            "First-Order Linear Equations",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(next_text)
        self.play(FadeIn(next_text, shift=UP * 0.15), run_time=NORMAL)
        self.wait(0.5)

        next_eq = MathTex(
            r"\frac{dy}{dx}", r"+", r"P(x)y", r"=", r"Q(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        next_eq[0].set_color(PRIMARY)
        next_eq[2].set_color(ACCENT)
        next_eq[4].set_color(SECONDARY)
        self.ly.safe_place(next_eq, DOWN, anchor=next_text, buff=0.5)
        self.play(Write(next_eq), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        play_outro(
            self,
            next_video="First-Order Linear Equations",
            next_playlist="ODE",
        )
