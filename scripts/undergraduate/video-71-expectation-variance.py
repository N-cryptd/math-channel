"""Video 71: Expectation and Variance
Probability & Statistics -- Video 5 of 12

Covers: expected value E[X], variance Var(X), standard deviation,
properties (linearity of expectation, scaling), examples with dice.

Competitive analysis: jbstatistics, StatQuest, Steve Brunton, Khan Academy
Plan: planning/video-71-expectation-variance.md

Render draft:  manim -ql scripts/undergraduate/video-71-expectation-variance.py Video71_ExpectationVariance
Render final:  manim -qh scripts/undergraduate/video-71-expectation-variance.py Video71_ExpectationVariance
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


class Video71_ExpectationVariance(Scene):
    """Full video: Expectation and Variance -- measuring center and spread."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_casino_hook()
        self.scene2_expected_value_definition()
        self.scene3_die_roll_example()
        self.scene4_misleading_insight()
        self.scene5_variance_definition()
        self.scene6_variance_die_example()
        self.scene7_shortcut_and_properties()
        self.scene8_summary()

    # -- Scene 1: Hook -- The Casino Question --
    def scene1_casino_hook(self):
        self.add_subcaption(
            "Imagine a simple casino game. You pay two dollars to play, "
            "and a wheel spins. You win ten dollars with probability "
            "one tenth, five dollars with probability three tenths, or "
            "nothing otherwise. Should you play?",
            duration=24,
        )
        play_intro(self, "Expectation and Variance", "Probability & Statistics")

        title = self.ly.title("The Casino Question")

        # Three outcome boxes
        outcomes_data = [
            ("$10", "p = 1/10"),
            ("$5", "p = 3/10"),
            ("$0", "p = 6/10"),
        ]
        boxes = VGroup()
        for val, prob in outcomes_data:
            box = VGroup(
                Text(val, font_size=HEADING_SIZE, color=ACCENT, font=SANS),
                Text(prob, font_size=SMALL_SIZE, color=DIM, font=MONO),
            ).arrange(DOWN, buff=0.15)
            box_surr = RoundedRectangle(
                corner_radius=0.1, width=1.6, height=0.9,
                fill_color=BG, fill_opacity=0.8,
                stroke_color=PRIMARY, stroke_width=1.5,
            )
            box_surr.move_to(box)
            grp = VGroup(box_surr, box)
            boxes.add(grp)

        boxes.arrange(RIGHT, buff=0.6)
        self.ly.safe_place(boxes, DOWN, anchor=title, buff=0.8)
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.3), run_time=NORMAL)
        self.wait(0.5)

        # Cost label
        self.add_subcaption(
            "The answer depends on the expected value. In the long run, "
            "how much does the casino pay you per game on average? This "
            "is why casinos always profit.",
            duration=20,
        )
        cost_text = Text(
            "You pay: $2 per game",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(cost_text, DOWN, anchor=boxes, buff=0.5)
        self.play(FadeIn(cost_text, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1)

        # Teaser formula
        ev_teaser = MathTex(
            r"E[\text{winnings}]",
            r"=",
            r"10 \cdot \tfrac{1}{10}",
            r"+",
            r"5 \cdot \tfrac{3}{10}",
            r"+",
            r"0 \cdot \tfrac{6}{10}",
            r"=",
            r"2.5",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ev_teaser[0].set_color(ACCENT)
        ev_teaser[8].set_color(ACCENT)
        self.ly.safe_place(ev_teaser, DOWN, anchor=cost_text, buff=0.4)
        ensure_fits(ev_teaser)
        self.play(Write(ev_teaser), run_time=SLOW)
        self.wait(0.5)

        box = self.ly.formula_box(ev_teaser, color=ACCENT)
        self.play(Create(box), run_time=FAST)
        self.wait(1)

        # Key insight
        self.add_subcaption(
            "On average the casino pays you two dollars fifty cents, but "
            "you only pay two dollars to play. The casino loses fifty "
            "cents per game. In reality, casinos design games where the "
            "expected value is always in their favor.",
            duration=24,
        )
        insight = Text(
            "E[winnings] > cost  =>  you profit on average!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=ev_teaser, buff=0.3)
        ensure_fits(insight)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # -- Scene 2: Expected Value -- Definition --
    def scene2_expected_value_definition(self):
        self.add_subcaption(
            "The expected value of a discrete random variable X is "
            "the weighted average of all its possible values, weighted "
            "by their probabilities. Think of it as the center of "
            "gravity of the probability mass function.",
            duration=24,
        )
        self.ly.section_divider(1, "Expected Value")

        title = self.ly.title("Expected Value")

        # Definition formula
        ev_def = MathTex(
            r"E[X]",
            r"=",
            r"\sum_{x}",
            r"x \cdot p(x)",
            font_size=TITLE_SIZE, color=WHITE,
        )
        ev_def[0].set_color(ACCENT)
        ev_def[3].set_color(ACCENT)
        self.ly.center_in_content(ev_def)
        self.play(Write(ev_def), run_time=SLOW)
        self.wait(0.5)

        box = self.ly.formula_box(ev_def, color=ACCENT)
        self.play(Create(box), run_time=FAST)
        self.wait(1)

        self.play(FadeOut(box), FadeOut(ev_def), run_time=FAST)

        # Notation breakdown
        self.add_subcaption(
            "E brackets X means the expected value of X. The sum "
            "symbol means add up over all possible values. Each term "
            "is the value times its probability.",
            duration=20,
        )

        title2 = self.ly.title("Notation")

        notation_items = [
            MathTex(
                r"E[X]", font_size=HEADING_SIZE, color=ACCENT,
            ),
            MathTex(
                r"\sum_{x}", font_size=HEADING_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"x \cdot p(x)", font_size=HEADING_SIZE, color=SECONDARY,
            ),
        ]
        labels = [
            Text('"expected value of X"', font_size=BODY_SIZE, color=DIM, font=SANS),
            Text('"sum over all values"', font_size=BODY_SIZE, color=DIM, font=SANS),
            Text('"value times its probability"', font_size=BODY_SIZE, color=DIM, font=SANS),
        ]

        title_l = self.ly.title("Breaking Down the Formula")
        for i in range(3):
            row = VGroup(notation_items[i], labels[i]).arrange(RIGHT, buff=0.5)
            if i == 0:
                self.ly.safe_place(row, DOWN, anchor=title_l, buff=0.5)
            else:
                row.next_to(prev_row, DOWN, buff=0.4)
            ensure_fits(row)
            self.play(Write(notation_items[i]), FadeIn(labels[i], shift=LEFT * 0.1), run_time=NORMAL)
            self.wait(0.3)
            prev_row = row

        self.wait(1)
        self.ly.clear()

        # Balance point visual
        self.add_subcaption(
            "Think of the PMF as physical bars on a plank. The expected "
            "value is where the fulcrum balances the whole thing. It is "
            "the center of gravity of the distribution.",
            duration=20,
        )

        title3 = self.ly.title("The Balance Point")

        # Simple uniform PMF (die) bars
        bar_width = 0.5
        bar_height = 1.2
        bars = VGroup()
        bar_labels = VGroup()
        for i in range(1, 7):
            bar = Rectangle(
                width=bar_width, height=bar_height,
                fill_color=PRIMARY, fill_opacity=0.6,
                stroke_color=WHITE, stroke_width=1,
            )
            bars.add(bar)
            lbl = Text(str(i), font_size=SMALL_SIZE, color=WHITE, font=MONO)
            lbl.next_to(bar, DOWN, buff=0.1)
            bar_labels.add(lbl)

        bars.arrange(RIGHT, buff=0.15)
        bar_labels.arrange(RIGHT, buff=0.15)
        for lbl, bar in zip(bar_labels, bars):
            lbl.align_to(bar, DOWN)

        bar_group = VGroup(bars, bar_labels)
        self.ly.safe_place(bar_group, DOWN, anchor=title3, buff=0.6)

        self.play(LaggedStart(*[Create(b) for b in bars], lag_ratio=0.1), run_time=NORMAL)
        self.play(FadeIn(bar_labels), run_time=FAST)
        self.wait(0.5)

        # Fulcrum line at 3.5
        fulcrum_x_pos = bars[2].get_center()[0] + (bars[3].get_center()[0] - bars[2].get_center()[0]) / 2
        fulcrum = DashedLine(
            UP * 3, DOWN * 3,
            color=ACCENT, stroke_width=3,
        )
        fulcrum.move_to(RIGHT * fulcrum_x_pos)
        self.play(Create(fulcrum), run_time=NORMAL)

        # E[X] label
        ev_label = MathTex(
            r"E[X]", r"= 3.5",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        ev_label.next_to(fulcrum, UP, buff=0.2)
        ensure_fits(ev_label)
        self.play(Write(ev_label), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # -- Scene 3: Expected Value -- Die Roll Example --
    def scene3_die_roll_example(self):
        self.add_subcaption(
            "Let us compute E of X for a fair six-sided die. X takes "
            "values one through six, each with probability one sixth.",
            duration=16,
        )
        self.ly.section_divider(2, "Example: Fair Die")

        title = self.ly.title("E[X] for a Fair Die")

        # Computation: E[X] = 1(1/6) + 2(1/6) + ... + 6(1/6) = 21/6 = 3.5
        terms = [
            MathTex(r"1 \cdot \tfrac{1}{6}", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"+\; 2 \cdot \tfrac{1}{6}", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"+\; 3 \cdot \tfrac{1}{6}", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"+\; 4 \cdot \tfrac{1}{6}", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"+\; 5 \cdot \tfrac{1}{6}", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"+\; 6 \cdot \tfrac{1}{6}", font_size=HEADING_SIZE, color=PRIMARY),
        ]

        # Summation notation
        sum_eq = MathTex(
            r"E[X]", r"=",
            r"\sum_{x=1}^{6}", r"x \cdot \tfrac{1}{6}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sum_eq[0].set_color(ACCENT)
        sum_eq[2].set_color(PRIMARY)
        sum_eq[3].set_color(PRIMARY)
        self.ly.safe_place(sum_eq, DOWN, anchor=title, buff=0.5)
        self.play(Write(sum_eq), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(sum_eq), run_time=FAST)

        # Expand terms progressively
        title2 = self.ly.title("Expanding the Sum")

        # Show first 3 terms, then swap for last 3
        for i, term in enumerate(terms[:3]):
            if i == 0:
                self.ly.safe_place(term, DOWN, anchor=title2, buff=0.5)
            else:
                term.next_to(prev_term, RIGHT, buff=0.3)
            ensure_fits(term)
            self.play(Write(term), run_time=FAST)
            self.wait(0.2)
            prev_term = term

        # Show "..." and remaining
        dots = MathTex(r"\cdots", font_size=HEADING_SIZE, color=DIM)
        dots.next_to(prev_term, RIGHT, buff=0.3)
        self.play(Write(dots), run_time=FAST)

        last_term = terms[5].copy()
        last_term.next_to(dots, RIGHT, buff=0.3)
        ensure_fits(last_term)
        self.play(Write(last_term), run_time=FAST)
        self.wait(0.5)

        all_terms = VGroup(*terms[:3], dots, last_term)
        self.play(FadeOut(all_terms), run_time=FAST)

        # Simplification
        self.add_subcaption(
            "Factor out the one sixth. The sum of one through six is "
            "twenty one. So E of X equals twenty one over six, which "
            "is three point five.",
            duration=20,
        )

        title3 = self.ly.title("Simplifying")

        step1 = MathTex(
            r"= \tfrac{1}{6}", r"(1 + 2 + 3 + 4 + 5 + 6)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        step1[0].set_color(DIM)
        step1[1].set_color(PRIMARY)
        self.ly.safe_place(step1, DOWN, anchor=title3, buff=0.5)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(step1), run_time=FAST)

        step2 = MathTex(
            r"= \tfrac{1}{6}", r"\cdot 21", r"= \tfrac{21}{6}", r"= 3.5",
            font_size=HEADING_SIZE, color=WHITE,
        )
        step2[0].set_color(DIM)
        step2[1].set_color(PRIMARY)
        step2[2].set_color(PRIMARY)
        step2[3].set_color(ACCENT)
        self.ly.safe_place(step2, DOWN, anchor=title3, buff=0.5)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.5)

        box = self.ly.formula_box(step2, color=ACCENT)
        self.play(Create(box), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # -- Scene 4: The "Misleading" Insight --
    def scene4_misleading_insight(self):
        self.add_subcaption(
            "But wait. The expected value is three point five. Can you "
            "roll a three point five on a die? No. Every single roll "
            "gives a whole number from one to six. E of X is not a "
            "value that X will actually take.",
            duration=24,
        )
        self.ly.section_divider(3, "The Key Misconception")

        title = self.ly.title("E[X] Is NOT a Single Outcome")

        # Warning in red
        warning = MathTex(
            r"E[X] = 3.5", r"\quad \text{but you can NEVER roll } 3.5",
            font_size=HEADING_SIZE, color=WHITE,
        )
        warning[0].set_color(ACCENT)
        warning[1].set_color(RED)
        self.ly.safe_place(warning, DOWN, anchor=title, buff=0.6)
        self.play(Write(warning), run_time=SLOW)
        self.wait(0.5)

        box = self.ly.formula_box(warning, color=RED)
        self.play(Create(box), run_time=FAST)
        self.wait(1)

        self.play(FadeOut(box), FadeOut(warning), run_time=FAST)

        # Explanation
        self.add_subcaption(
            "E of X is the long run average. If you roll the die "
            "thousands of times and average the results, that average "
            "converges to three point five. It does not predict any "
            "single outcome.",
            duration=20,
        )

        title2 = self.ly.title("E[X] = Long-Run Average")

        insight_text = Text(
            "Roll once: X = 1, 2, 3, 4, 5, or 6",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(insight_text, DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(insight_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(insight_text), run_time=FAST)

        insight_text2 = Text(
            "Roll 10,000 times and average: approaches 3.5",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(insight_text2, DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(insight_text2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(insight_text2), run_time=FAST)

        key_point = Text(
            "E[X] does NOT predict a single outcome!",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(key_point, DOWN, anchor=title2, buff=0.5)
        self.play(Write(key_point), run_time=SLOW)
        self.wait(1.5)

        self.ly.clear()

    # -- Scene 5: Variance -- Definition --
    def scene5_variance_definition(self):
        self.add_subcaption(
            "Expected value tells us the center. But two random "
            "variables can have the same mean yet behave very "
            "differently. Variance measures how spread out the "
            "values are around the mean.",
            duration=20,
        )
        self.ly.section_divider(4, "Variance")

        title = self.ly.title("Variance: Measuring Spread")

        # Two PMFs comparison (conceptual)
        # Left: narrow (concentrated around mean)
        # Right: wide (spread out)
        left_label = Text("Narrow spread", font_size=SMALL_SIZE, color=PRIMARY, font=SANS)
        right_label = Text("Wide spread", font_size=SMALL_SIZE, color=RED, font=SANS)

        # Narrow bars (concentrated around center)
        narrow_bars = VGroup()
        for h, x_off in [(0.5, -1.5), (1.2, -0.7), (1.8, 0), (1.2, 0.7), (0.5, 1.5)]:
            bar = Rectangle(
                width=0.4, height=h,
                fill_color=PRIMARY, fill_opacity=0.6,
                stroke_color=WHITE, stroke_width=1,
            )
            bar.move_to(LEFT * 2.5 + RIGHT * x_off)
            narrow_bars.add(bar)

        # Wide bars (spread out)
        wide_bars = VGroup()
        for h, x_off in [(1.5, -1.5), (0.8, -0.7), (0.5, 0), (0.8, 0.7), (1.5, 1.5)]:
            bar = Rectangle(
                width=0.4, height=h,
                fill_color=RED, fill_opacity=0.6,
                stroke_color=WHITE, stroke_width=1,
            )
            bar.move_to(RIGHT * 2.5 + RIGHT * x_off)
            wide_bars.add(bar)

        left_group = VGroup(left_label, narrow_bars).arrange(DOWN, buff=0.2)
        right_group = VGroup(right_label, wide_bars).arrange(DOWN, buff=0.2)
        comparison = VGroup(left_group, right_group).arrange(RIGHT, buff=1.5)
        self.ly.safe_place(comparison, DOWN, anchor=title, buff=0.5)
        ensure_fits(comparison)
        self.play(
            FadeIn(left_label), FadeIn(right_label),
            LaggedStart(*[Create(b) for b in narrow_bars], lag_ratio=0.1),
            LaggedStart(*[Create(b) for b in wide_bars], lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.play(FadeOut(comparison), run_time=FAST)

        # Variance formula
        self.add_subcaption(
            "Variance is the average squared distance from the mean. "
            "We square the distance so positive and negative deviations "
            "do not cancel each other out.",
            duration=18,
        )

        title2 = self.ly.title("Variance Definition")

        var_def = MathTex(
            r"\text{Var}(X)",
            r"=",
            r"E\left[(X - \mu)^2\right]",
            r"=",
            r"\sum_{x}",
            r"(x - \mu)^2 \cdot p(x)",
            font_size=TITLE_SIZE, color=WHITE,
        )
        var_def[0].set_color(SECONDARY)
        var_def[2].set_color(SECONDARY)
        var_def[5].set_color(SECONDARY)
        self.ly.center_in_content(var_def)
        self.play(Write(var_def), run_time=SLOW)
        self.wait(0.5)

        box = self.ly.formula_box(var_def, color=SECONDARY)
        self.play(Create(box), run_time=FAST)
        self.wait(1)

        self.play(FadeOut(box), FadeOut(var_def), run_time=FAST)

        # Standard deviation
        self.add_subcaption(
            "The square root of the variance gives us the standard "
            "deviation, sigma, which has the same units as X and is "
            "easier to interpret.",
            duration=16,
        )

        title3 = self.ly.title("Standard Deviation")

        sd_eq = MathTex(
            r"\sigma",
            r"=",
            r"\sqrt{\text{Var}(X)}",
            r"=",
            r"\sqrt{E\left[(X - \mu)^2\right]}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sd_eq[0].set_color(ACCENT)
        sd_eq[2].set_color(ACCENT)
        self.ly.safe_place(sd_eq, DOWN, anchor=title3, buff=0.5)
        self.play(Write(sd_eq), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # -- Scene 6: Variance -- Die Roll Example --
    def scene6_variance_die_example(self):
        self.add_subcaption(
            "For our fair die with E of X equal to three point five, "
            "let us compute the variance. We need the squared "
            "distance from the mean for each value.",
            duration=20,
        )
        self.ly.section_divider(5, "Example: Variance of a Die")

        title = self.ly.title("Var(X) for a Fair Die")

        # Show computation for x=1 and x=6 (by symmetry all have same variance)
        step1 = MathTex(
            r"(1 - 3.5)^2 \cdot \tfrac{1}{6}",
            r"=",
            r"(-2.5)^2 \cdot \tfrac{1}{6}",
            r"=",
            r"\tfrac{6.25}{6}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        step1[0].set_color(PRIMARY)
        step1[4].set_color(ACCENT)
        self.ly.safe_place(step1, DOWN, anchor=title, buff=0.5)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(step1), run_time=FAST)

        step2 = MathTex(
            r"(6 - 3.5)^2 \cdot \tfrac{1}{6}",
            r"=",
            r"(2.5)^2 \cdot \tfrac{1}{6}",
            r"=",
            r"\tfrac{6.25}{6}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        step2[0].set_color(PRIMARY)
        step2[4].set_color(ACCENT)
        self.ly.safe_place(step2, DOWN, anchor=title, buff=0.5)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(step2), run_time=FAST)

        self.add_subcaption(
            "By symmetry, every face contributes the same amount to "
            "the variance. Each gives six point two five over six. "
            "Multiply by six faces.",
            duration=16,
        )

        title2 = self.ly.title("Summing Up")

        step3 = MathTex(
            r"\text{Var}(X)",
            r"=",
            r"6 \cdot \tfrac{6.25}{6}",
            r"=",
            r"\tfrac{35}{12}",
            r"\approx 2.917",
            font_size=HEADING_SIZE, color=WHITE,
        )
        step3[0].set_color(SECONDARY)
        step3[4].set_color(ACCENT)
        step3[5].set_color(ACCENT)
        self.ly.safe_place(step3, DOWN, anchor=title2, buff=0.5)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(0.5)

        box = self.ly.formula_box(step3, color=SECONDARY)
        self.play(Create(box), run_time=FAST)
        self.wait(1)

        self.play(FadeOut(box), FadeOut(step3), run_time=FAST)

        # Standard deviation
        title3 = self.ly.title("Standard Deviation")

        sd_result = MathTex(
            r"\sigma",
            r"=",
            r"\sqrt{\tfrac{35}{12}}",
            r"\approx 1.708",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sd_result[0].set_color(ACCENT)
        sd_result[3].set_color(ACCENT)
        self.ly.safe_place(sd_result, DOWN, anchor=title3, buff=0.5)
        self.play(Write(sd_result), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # -- Scene 7: Computational Shortcut and Properties --
    def scene7_shortcut_and_properties(self):
        self.add_subcaption(
            "Computing squared distances for every value can be "
            "tedious. There is a useful shortcut for variance.",
            duration=14,
        )
        self.ly.section_divider(6, "Shortcut and Properties")

        title = self.ly.title("Computational Shortcut")

        shortcut = MathTex(
            r"\text{Var}(X)",
            r"=",
            r"E[X^2]",
            r"-",
            r"(E[X])^2",
            font_size=TITLE_SIZE, color=WHITE,
        )
        shortcut[0].set_color(SECONDARY)
        shortcut[2].set_color(PRIMARY)
        shortcut[4].set_color(ACCENT)
        self.ly.safe_place(shortcut, DOWN, anchor=title, buff=0.5)
        self.play(Write(shortcut), run_time=SLOW)
        self.wait(0.5)

        box = self.ly.formula_box(shortcut, color=SECONDARY)
        self.play(Create(box), run_time=FAST)
        self.wait(1)

        self.play(FadeOut(box), FadeOut(shortcut), run_time=FAST)

        # Properties
        self.add_subcaption(
            "Important properties. First, scaling a random variable "
            "by a stretches the variance by a squared. Shifting by b "
            "does not change variance at all. Second, expectation is "
            "linear: E of aX plus b equals a times E of X plus b.",
            duration=28,
        )

        title2 = self.ly.title("Properties")

        props = [
            MathTex(
                r"\text{Var}(aX + b)", r"=", r"a^2", r"\cdot", r"\text{Var}(X)",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            Text(
                "Scaling stretches variance by a^2, shifting does nothing",
                font_size=SMALL_SIZE, color=DIM, font=SANS,
            ),
            MathTex(
                r"E[aX + b]", r"=", r"aE[X]", r"+", r"b",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            Text(
                "Linearity of expectation",
                font_size=SMALL_SIZE, color=DIM, font=SANS,
            ),
        ]
        # Color key parts
        props[0][0].set_color(SECONDARY)
        props[0][2].set_color(ACCENT)
        props[0][4].set_color(SECONDARY)
        props[2][0].set_color(ACCENT)
        props[2][2].set_color(PRIMARY)

        self.ly.progressive_reveal(props, start_from=title2)
        self.wait(1.5)

        self.ly.clear()

        # Additional properties
        self.add_subcaption(
            "Also remember: variance is always non-negative, and "
            "variance is zero only when X is constant, meaning there "
            "is no randomness.",
            duration=16,
        )

        title3 = self.ly.title("More Properties")

        more_props = [
            Text(
                "Var(X) >= 0  always",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Var(X) = 0  if and only if  X is constant",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(more_props, start_from=title3)
        self.wait(1.5)

        self.ly.clear()

    # -- Scene 8: Summary and Outro --
    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap. Expected value is the center of a random "
            "variable. Variance measures the spread. The standard "
            "deviation is the square root of variance, and there is a "
            "handy shortcut for computing it.",
            duration=24,
        )

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "E[X] = sum of x*p(x) -- center / long-run average",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "E[X] is NOT a single predicted outcome",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Var(X) = E[(X-mu)^2] -- spread around the mean",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "sigma = sqrt(Var(X)) -- same units as X",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Shortcut: Var(X) = E[X^2] - (E[X])^2",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        self.ly.clear()

        self.add_subcaption(
            "Next time, we will explore common probability "
            "distributions, the families of random variables that "
            "appear everywhere in science and engineering.",
            duration=20,
        )

        play_outro(
            self,
            next_video="Common Distributions",
            next_playlist="Probability & Statistics",
        )
