"""
Video 49: Double Integrals
Calculus III -- Multivariable Playlist -- Video 9 of 14

Covers: double integral as volume under a surface, 2D Riemann sums,
iterated integrals, Fubini's theorem, Type I and Type II regions,
changing order of integration, applications (area, average value).

Render draft:  manim -ql scripts/undergraduate/video-49-double-integrals.py Video49_DoubleIntegrals
Render final:  manim -qh scripts/undergraduate/video-49-double-integrals.py Video49_DoubleIntegrals
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


class Video49_DoubleIntegrals(Scene):
    """Full video: Double Integrals."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_riemann_sum()
        self.scene3_iterated_integrals()
        self.scene4_worked_example()
        self.scene5_general_regions()
        self.scene6_changing_order()
        self.scene7_applications()
        self.scene8_summary()

    # ── Scene 1: Hook — Volume Under a Surface ────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "In single-variable calculus, we found the area under a curve. "
            "Now we extend that idea into three dimensions. What's the "
            "volume under a surface?",
            duration=18,
        )
        play_intro(self, "Double Integrals",
                   "Calculus III -- Multivariable")

        title = self.ly.title("From Area to Volume")

        # 1D reminder
        reminder = Text(
            "Single integral: area under a curve y = f(x)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        formula_1d = MathTex(
            r"\int_a^b f(x)\,dx = \text{area}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(reminder, DOWN, anchor=title, buff=0.4)
        self.ly.safe_place(formula_1d, DOWN, anchor=reminder, buff=0.3)
        self.play(
            FadeIn(reminder, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.play(Write(formula_1d), run_time=NORMAL)
        self.wait(1)

        # 2D extension question
        question = Text(
            "Double integral: volume under a surface z = f(x, y)?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(question, DOWN, anchor=formula_1d, buff=0.5)
        ensure_fits(question)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 2: From 1D to 2D — Riemann Sum ─────────────────────
    def scene2_riemann_sum(self):
        self.add_subcaption(
            "Recall that a single integral divides the x-axis into strips "
            "and sums rectangle areas. For two variables, we divide the "
            "xy-plane into small rectangles and sum column volumes.",
            duration=18,
        )
        self.ly.section_divider(1, "Extending Riemann Sums to 2D")

        title = self.ly.title("The Double Riemann Sum")

        # Step 1: partition
        step1 = Text(
            "1. Partition R into sub-rectangles of area \u0394A = \u0394x \u00b7 \u0394y",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(step1, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(step1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Step 2: sample point + column
        step2 = Text(
            "2. At each sample point, build a column of height f(x*, y*)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(step2, DOWN, anchor=step1, buff=0.3)
        self.play(FadeIn(step2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Step 3: sum and limit
        step3 = Text(
            "3. Sum all columns, then take the limit",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(step3, DOWN, anchor=step2, buff=0.3)
        self.play(FadeIn(step3, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # The formal definition formula
        self.play(
            FadeOut(step1), FadeOut(step2), FadeOut(step3),
            run_time=FAST,
        )

        formula = MathTex(
            r"\iint_R f(x,y)\,dA",
            r"=",
            r"\lim_{m,n \to \infty}",
            r"\sum_{i=1}^m \sum_{j=1}^n",
            r"f(x_i^*, y_j^*)",
            r"\Delta A",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula[4].set_color(ACCENT)
        formula[5].set_color(SECONDARY)
        self.ly.safe_place(formula, DOWN, anchor=title, buff=0.5)
        ensure_fits(formula)
        self.play(Write(formula), run_time=SLOW)
        self.wait(2.5)
        self.ly.clear()

    # ── Scene 3: Iterated Integrals — Fubini's Theorem ────────────
    def scene3_iterated_integrals(self):
        self.add_subcaption(
            "Fubini's theorem tells us we can evaluate a double integral "
            "as two nested single integrals. For continuous functions on "
            "rectangular regions, the order doesn't matter.",
            duration=18,
        )
        self.ly.section_divider(2, "Iterated Integrals and Fubini")

        title = self.ly.title("Fubini's Theorem (Rectangular R)")

        # Statement
        statement = Text(
            "If f is continuous on R = [a, b] \u00d7 [c, d], then:",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(statement, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(statement, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # dy dx order
        order1 = MathTex(
            r"\iint_R f(x,y)\,dA",
            r"=",
            r"\int_a^b \!\!\left[\int_c^d f(x,y)\,dy\right]dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        order1[2].set_color(PRIMARY)
        self.ly.safe_place(order1, DOWN, anchor=statement, buff=0.4)
        self.play(Write(order1), run_time=SLOW)
        self.wait(1.5)

        # dy dx label
        label1 = Text(
            "Integrate inner (dy) first, then outer (dx)",
            font_size=LABEL_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(label1, DOWN, anchor=order1, buff=0.3)
        self.play(FadeIn(label1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        # Swap to dx dy
        self.play(FadeOut(order1), FadeOut(label1), run_time=FAST)

        order2 = MathTex(
            r"\iint_R f(x,y)\,dA",
            r"=",
            r"\int_c^d \!\!\left[\int_a^b f(x,y)\,dx\right]dy",
            font_size=HEADING_SIZE, color=WHITE,
        )
        order2[2].set_color(SECONDARY)
        self.ly.safe_place(order2, DOWN, anchor=statement, buff=0.4)
        self.play(Write(order2), run_time=SLOW)

        label2 = Text(
            "Order of integration can be swapped!",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(label2, DOWN, anchor=order2, buff=0.3)
        self.play(FadeIn(label2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.5)
        self.ly.clear()

    # ── Scene 4: Worked Example — Volume Under a Plane ──────────
    def scene4_worked_example(self):
        self.add_subcaption(
            "Let's find the volume under the plane f equals six minus "
            "two x minus three y over the rectangle zero to one and zero "
            "to two. We'll set up the iterated integral and evaluate step by step.",
            duration=18,
        )
        self.ly.section_divider(3, "Worked Example")

        title = self.ly.title("Volume Under f(x,y) = 6 - 2x - 3y")

        # Problem setup
        problem = Text(
            "R = [0, 1] \u00d7 [0, 2],  find V = \u222b\u222b_R f dA",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(problem, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(problem, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Iterated integral setup
        setup = MathTex(
            r"V",
            r"=",
            r"\int_0^1 \!\!\left[\int_0^2 (6 - 2x - 3y)\,dy\right]dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        setup[2].set_color(PRIMARY)
        self.ly.safe_place(setup, DOWN, anchor=problem, buff=0.4)
        self.play(Write(setup), run_time=SLOW)
        self.wait(1)

        # Evaluate inner integral
        self.play(FadeOut(setup), run_time=FAST)

        inner_result = MathTex(
            r"\int_0^2 (6 - 2x - 3y)\,dy",
            r"=",
            r"\left[6y - 2xy - \tfrac{3}{2}y^2\right]_0^2",
            r"=",
            r"12 - 4x - 6",
            r"=",
            r"6 - 4x",
            font_size=BODY_SIZE, color=WHITE,
        )
        inner_result[4].set_color(ACCENT)
        inner_result[6].set_color(SECONDARY)
        self.ly.safe_place(inner_result, DOWN, anchor=problem, buff=0.4)
        ensure_fits(inner_result)
        self.play(Write(inner_result), run_time=SLOW)
        self.wait(2)

        # Evaluate outer integral
        self.play(FadeOut(inner_result), run_time=FAST)

        outer_result = MathTex(
            r"\int_0^1 (6 - 4x)\,dx",
            r"=",
            r"\left[6x - 2x^2\right]_0^1",
            r"=",
            r"6 - 2",
            r"=",
            r"\mathbf{4}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        outer_result[6].set_color(ACCENT)
        self.ly.safe_place(outer_result, DOWN, anchor=problem, buff=0.4)
        self.play(Write(outer_result), run_time=SLOW)
        self.wait(1)

        # Answer text
        answer = Text(
            "Volume = 4 cubic units",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(answer, DOWN, anchor=outer_result, buff=0.4)
        self.play(FadeIn(answer, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2.5)
        self.ly.clear()

    # ── Scene 5: General Regions — Type I and Type II ────────────
    def scene5_general_regions(self):
        self.add_subcaption(
            "Not all integration regions are rectangles. For general "
            "regions, the bounds of the inner integral become curves "
            "instead of constants. Type I regions have x-constant outer "
            "bounds with y varying between curves.",
            duration=20,
        )
        self.ly.section_divider(4, "General Regions")

        title = self.ly.title("Type I and Type II Regions")

        # Type I
        type1_label = Text(
            "Type I: x ranges [a, b], y between curves",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(type1_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(type1_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        type1_formula = MathTex(
            r"\iint_R f(x,y)\,dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y)\,dy\,dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        type1_formula.set_color(PRIMARY)
        self.ly.safe_place(type1_formula, DOWN, anchor=type1_label, buff=0.3)
        self.play(Write(type1_formula), run_time=SLOW)
        self.wait(1.5)

        # Swap to Type II
        self.play(FadeOut(type1_label), FadeOut(type1_formula), run_time=FAST)

        type2_label = Text(
            "Type II: y ranges [c, d], x between curves",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(type2_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(type2_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        type2_formula = MathTex(
            r"\iint_R f(x,y)\,dA = \int_c^d \int_{h_1(y)}^{h_2(y)} f(x,y)\,dx\,dy",
            font_size=HEADING_SIZE, color=WHITE,
        )
        type2_formula.set_color(SECONDARY)
        self.ly.safe_place(type2_formula, DOWN, anchor=type2_label, buff=0.3)
        self.play(Write(type2_formula), run_time=SLOW)
        self.wait(1.5)

        # Key insight
        self.play(FadeOut(type2_label), FadeOut(type2_formula), run_time=FAST)

        insight = Text(
            "Choose the type that gives simpler bounds!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(insight)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 6: Changing Order of Integration ────────────────────
    def scene6_changing_order(self):
        self.add_subcaption(
            "Sometimes the given order of integration is impossible to "
            "evaluate directly. The trick is to sketch the region and "
            "rewrite the integral with the bounds swapped. Let's see "
            "a classic example.",
            duration=20,
        )
        self.ly.section_divider(5, "Changing the Order")

        title = self.ly.title("When Order Matters")

        # Motivating example
        problem = Text(
            "Evaluate: integral from 0 to 1, integral from x to 1, "
            "of e to the y squared dy dx",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(problem, DOWN, anchor=title, buff=0.4)
        ensure_fits(problem)
        self.play(FadeIn(problem, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Original integral
        original = MathTex(
            r"\int_0^1 \int_x^1 e^{y^2}\,dy\,dx",
            r"\leftarrow \text{impossible!}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        original[1].set_color(RED)
        self.ly.safe_place(original, DOWN, anchor=problem, buff=0.4)
        self.play(Write(original), run_time=NORMAL)
        self.wait(1.5)

        # Explanation
        explanation = Text(
            "e^{y^2} has no elementary antiderivative",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(explanation, DOWN, anchor=original, buff=0.3)
        self.play(FadeIn(explanation, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Swap
        self.play(FadeOut(original), FadeOut(explanation), run_time=FAST)

        swapped = MathTex(
            r"\int_0^1 \int_0^y e^{y^2}\,dx\,dy",
            r"=",
            r"\int_0^1 y\, e^{y^2}\,dy",
            font_size=HEADING_SIZE, color=WHITE,
        )
        swapped[0].set_color(SECONDARY)
        swapped[2].set_color(ACCENT)
        self.ly.safe_place(swapped, DOWN, anchor=problem, buff=0.4)
        self.play(Write(swapped), run_time=SLOW)
        self.wait(1)

        # Final result
        self.play(FadeOut(swapped), run_time=FAST)

        result = MathTex(
            r"=",
            r"\frac{1}{2}\int_0^1 2y\, e^{y^2}\,dy",
            r"=",
            r"\frac{1}{2}\left[e^{y^2}\right]_0^1",
            r"=",
            r"\frac{e - 1}{2}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        result[5].set_color(ACCENT)
        self.ly.safe_place(result, DOWN, anchor=problem, buff=0.4)
        self.play(Write(result), run_time=SLOW)
        self.wait(2.5)
        self.ly.clear()

    # ── Scene 7: Applications — Area and Average Value ───────────
    def scene7_applications(self):
        self.add_subcaption(
            "Double integrals have direct applications. Setting f to "
            "one gives us the area of the region. Dividing by that area "
            "gives the average value of the function over the region.",
            duration=18,
        )
        self.ly.section_divider(6, "Applications")

        title = self.ly.title("Area and Average Value")

        # Area
        area_label = Text(
            "Area of a region R:",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(area_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(area_label, shift=LEFT * 0.15), run_time=NORMAL)

        area_formula = MathTex(
            r"\text{Area}(R) = \iint_R 1\,dA",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(area_formula, DOWN, anchor=area_label, buff=0.3)
        self.play(Write(area_formula), run_time=NORMAL)
        self.wait(1)

        # Average value
        self.play(FadeOut(area_label), FadeOut(area_formula), run_time=FAST)

        avg_label = Text(
            "Average value of f over R:",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(avg_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(avg_label, shift=LEFT * 0.15), run_time=NORMAL)

        avg_formula = MathTex(
            r"f_{\text{avg}}",
            r"=",
            r"\frac{1}{\text{Area}(R)}",
            r"\iint_R f(x,y)\,dA",
            font_size=HEADING_SIZE, color=WHITE,
        )
        avg_formula[0].set_color(ACCENT)
        avg_formula[2].set_color(SECONDARY)
        self.ly.safe_place(avg_formula, DOWN, anchor=avg_label, buff=0.3)
        self.play(Write(avg_formula), run_time=SLOW)
        self.wait(2)

        # Quick note
        self.play(FadeOut(avg_label), FadeOut(avg_formula), run_time=FAST)

        note = Text(
            "These extend the 1D area and average value formulas "
            "to two dimensions.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(note)
        ensure_fits(note)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 8: Summary and Recap ────────────────────────────────
    def scene8_summary(self):
        self.add_subcaption(
            "To recap: a double integral extends the single integral to "
            "two variables, giving us volumes under surfaces. Fubini's "
            "theorem lets us evaluate them as iterated integrals. For "
            "general regions, the bounds of the inner integral are "
            "curves, and sometimes swapping the order is essential.",
            duration=24,
        )
        self.ly.section_divider(7, "Summary")

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "Double integral = volume (or signed volume) under a surface",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Fubini: evaluate as two nested single integrals",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Type I/II: inner bounds are curves, not constants",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Swapping order can make impossible integrals tractable",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

        play_outro(
            self,
            "Triple Integrals",
            "Calculus III -- Multivariable",
        )
