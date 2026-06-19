"""Video 76: Estimation and Confidence Intervals
Probability & Statistics -- Video 10 of 12

Covers: Point estimation, CLT-to-CI derivation, confidence level interpretation,
repeated sampling visual, choosing confidence levels, worked example,
t-distribution introduction, t-based confidence intervals.

Plan: planning/video-76-estimation-confidence-intervals.md

Render draft:  manim -ql scripts/undergraduate/video-76-estimation-confidence-intervals.py Video76_EstimationConfidenceIntervals
Render final:  manim -qh scripts/undergraduate/video-76-estimation-confidence-intervals.py Video76_EstimationConfidenceIntervals
"""

from manim import *
import sys, os, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video76_EstimationConfidenceIntervals(Scene):
    """Estimation and Confidence Intervals -- point estimates, CI derivation,
    coverage interpretation, worked example, t-distribution."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook_and_clt_recap()
        self.scene2_point_estimation()
        self.scene3_deriving_ci()
        self.scene4_interpretation()
        self.scene5_confidence_levels()
        self.scene6_worked_example()
        self.scene7_t_distribution()
        self.scene8_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook + CLT Recap (1:30)
    # ------------------------------------------------------------------
    def scene1_hook_and_clt_recap(self):
        self.add_subcaption(
            "Last time we learned the Central Limit Theorem. The sample mean "
            "is approximately normally distributed, centered at the true mean. "
            "Now we put that powerful result to work.",
            duration=12,
        )
        play_intro(self, "Confidence Intervals", "Probability & Statistics")

        title = self.ly.title("From CLT to Confidence Intervals")

        items = [
            Text(
                "CLT: X-bar is approximately N(mu, sigma squared over n)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "We know the shape and spread of the sampling distribution",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Can we use this to estimate mu from a single sample?",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(4)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Point Estimation (1:30)
    # ------------------------------------------------------------------
    def scene2_point_estimation(self):
        self.add_subcaption(
            "The most natural estimate for the population mean is the "
            "sample mean x-bar. It is unbiased: its expected value equals "
            "the true mean. But a single number tells us nothing about "
            "uncertainty. We need a range.",
            duration=13,
        )

        title = self.ly.title("Point Estimation")

        items = [
            Text(
                "Estimate mu with x-bar (the sample mean)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Unbiased: E[x-bar] = mu",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Consistent: variance goes to zero as n grows",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "But a single point gives no sense of uncertainty!",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(5)
        self.ly.clear()

        # Motivate intervals
        self.add_subcaption(
            "Instead of giving a single number, we give an interval: "
            "a range of plausible values for the true mean. This interval "
            "comes with a confidence level.",
            duration=10,
        )

        title2 = self.ly.title("From Points to Intervals")

        items2 = [
            Text(
                "Give a range of plausible values for mu",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "The range is centered on x-bar",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Width depends on variability and sample size",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "The confidence level quantifies our certainty",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)

        self.wait(4)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Deriving the CI (3:00)
    # ------------------------------------------------------------------
    def scene3_deriving_ci(self):
        self.add_subcaption(
            "We derive the confidence interval directly from the CLT. "
            "The CLT tells us the standardized sample mean is approximately "
            "standard normal. From this, we construct an interval.",
            duration=12,
        )

        self.ly.section_divider(3, "Deriving the Confidence Interval")

        # Step 1: CLT in standardized form
        self.add_subcaption(
            "Starting from the CLT: the probability that Z falls between "
            "negative z star and z star is our confidence level, say 0.95.",
            duration=10,
        )

        step1 = MathTex(
            r"P\!\left(",
            r"-z^*",
            r"<",
            r"\frac{\bar{X} - \mu}{\sigma / \sqrt{n}}",
            r"<",
            r"z^*",
            r"\right)",
            r"=",
            r"0.95",
            font_size=HEADING_SIZE,
        )
        step1.set_color_by_tex(r"-z^*", PRIMARY)
        step1.set_color_by_tex(r"z^*", PRIMARY)
        step1.set_color_by_tex(r"0.95", ACCENT)
        box1 = self.ly.formula_box(step1)

        self.play(FadeIn(box1, shift=UP * 0.15), run_time=NORMAL)
        self.wait(8)

        # Step 2: Multiply through
        self.add_subcaption(
            "Now we multiply all parts by sigma over root n, and add "
            "mu to each side to isolate mu in the middle.",
            duration=10,
        )

        step2 = MathTex(
            r"P\!\left(",
            r"\bar{X} - z^* \frac{\sigma}{\sqrt{n}}",
            r"<",
            r"\mu",
            r"<",
            r"\bar{X} + z^* \frac{\sigma}{\sqrt{n}}",
            r"\right)",
            r"=",
            r"0.95",
            font_size=HEADING_SIZE,
        )
        step2.set_color_by_tex(r"\mu", ACCENT)
        step2.set_color_by_tex(r"0.95", ACCENT)
        step2.set_color_by_tex(r"z^*", PRIMARY)
        box2 = self.ly.formula_box(step2)

        self.play(
            Transform(box1, box2),
            run_time=SLOW,
        )
        self.wait(8)

        # Step 3: Identify CI
        self.add_subcaption(
            "And there is our 95% confidence interval. The margin of "
            "error is z star times sigma over root n.",
            duration=9,
        )

        # Margin of error label
        me_label = Text(
            "Margin of Error",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        me_formula = MathTex(
            r"\text{ME}",
            r"=",
            r"z^* \cdot \frac{\sigma}{\sqrt{n}}",
            font_size=HEADING_SIZE,
        )
        me_formula.set_color_by_tex(r"z^*", PRIMARY)
        me_formula.set_color_by_tex(r"\sigma", ACCENT)

        self.play(
            FadeOut(box1),
            FadeIn(me_label, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        me_label.move_to(UP * self.ly.content_top)
        self.play(Write(me_formula), run_time=SLOW)
        self.wait(6)

        # Final CI formula
        self.add_subcaption(
            "The confidence interval is x-bar plus or minus the margin "
            "of error. This is the most important formula in statistics.",
            duration=10,
        )

        ci_label = Text(
            "95% Confidence Interval",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        ci_formula = MathTex(
            r"\left(",
            r"\bar{X}",
            r"\pm",
            r"z^*",
            r"\frac{\sigma}{\sqrt{n}}",
            r"\right)",
            font_size=HEADING_SIZE,
        )
        ci_formula.set_color_by_tex(r"\bar{X}", PRIMARY)
        ci_formula.set_color_by_tex(r"z^*", PRIMARY)
        ci_formula.set_color_by_tex(r"\sigma", ACCENT)
        ci_box = self.ly.formula_box(ci_formula)

        self.play(
            FadeOut(me_label), FadeOut(me_formula),
            FadeIn(ci_label, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        ci_label.move_to(UP * self.ly.content_top)
        self.play(
            FadeIn(ci_box, shift=UP * 0.15),
            run_time=NORMAL,
        )
        self.play(Write(ci_formula), run_time=SLOW)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: What Does "95% Confident" Mean? (2:30)
    # ------------------------------------------------------------------
    def scene4_interpretation(self):
        self.add_subcaption(
            "This is the most common misunderstanding in all of statistics. "
            "A 95% confidence interval does NOT mean there is a 95 percent "
            "probability that mu lies in our particular interval.",
            duration=14,
        )

        title = self.ly.title('What Does "95% Confident" Mean?')

        # Misconception
        wrong = Text(
            "WRONG: \"There is a 95% probability that mu is in this interval\"",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(wrong, DOWN, title)
        self.wait(5)

        # Why it's wrong
        self.add_subcaption(
            "Mu is a fixed constant. It either is or is not in our interval. "
            "There is no probability involved. The randomness comes from "
            "the sample, not from mu.",
            duration=11,
        )

        why_wrong = Text(
            "Mu is fixed (not random). The interval is random.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(why_wrong, DOWN, wrong)
        self.wait(5)

        self.ly.clear()

        # Correct interpretation
        self.add_subcaption(
            "The correct interpretation: if we repeated the experiment many "
            "times, about 95 percent of the intervals we construct would "
            "contain the true mean mu.",
            duration=12,
        )

        title2 = self.ly.title("Correct Interpretation")

        correct = Text(
            "If we repeat the sampling process many times,",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        correct2 = Text(
            "about 95% of the intervals we construct",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        correct3 = Text(
            "will contain the true mean mu",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        self.ly.progressive_reveal(
            [correct, correct2, correct3],
            start_from=title2,
        )
        self.wait(6)

        self.ly.clear()

        # Visual: simulated CIs
        self.add_subcaption(
            "Here is what that looks like. We draw 20 samples and "
            "construct a confidence interval from each. About 19 out "
            "of 20 contain the true mean. The ones that miss are shown "
            "in red.",
            duration=15,
        )

        sim_title = self.ly.title("Repeated Sampling Simulation")

        rng = np.random.RandomState(123)
        mu_true = 10.0
        sigma = 3.0
        n = 30
        n_intervals = 20
        z_star = 1.96

        ci_group = VGroup()
        for i in range(n_intervals):
            sample = rng.normal(mu_true, sigma, n)
            x_bar = sample.mean()
            me = z_star * sigma / math.sqrt(n)
            lo = x_bar - me
            hi = x_bar + me
            contains_mu = lo <= mu_true <= hi

            # Draw horizontal CI bar
            bar_y = -3.0 + i * 0.3
            bar_start = lo * 0.2  # scale to fit
            bar_end = hi * 0.2
            color = SECONDARY if contains_mu else RED

            ci_bar = Line(
                start=[bar_start, bar_y, 0],
                end=[bar_end, bar_y, 0],
                stroke_width=3,
                color=color,
            )
            # Endpoint dots
            dot_left = Dot(
                point=[bar_start, bar_y, 0],
                radius=0.04,
                color=color,
            )
            dot_right = Dot(
                point=[bar_end, bar_y, 0],
                radius=0.04,
                color=color,
            )
            # Center dot
            center = Dot(
                point=[x_bar * 0.2, bar_y, 0],
                radius=0.03,
                color=PRIMARY,
            )

            ci_group.add(ci_bar, dot_left, dot_right, center)

        # Scale and position
        ci_group.scale(0.45)
        self.ly.center_in_content(ci_group)

        # True mean line
        mu_x = mu_true * 0.2 * 0.45
        mu_line = DashedLine(
            start=[mu_x, ci_group.get_bottom()[1] - 0.3, 0],
            end=[mu_x, ci_group.get_top()[1] + 0.3, 0],
            color=ACCENT,
            stroke_width=2,
        )
        mu_label_mob = Text(
            "mu", font_size=SMALL_SIZE, color=ACCENT, font=MONO,
        )
        mu_label_mob.next_to(mu_line, UP, buff=0.1)

        # Legend
        legend_green = VGroup(
            Line(ORIGIN, RIGHT * 0.5, color=SECONDARY, stroke_width=3),
            Text("contains mu", font_size=SMALL_SIZE, color=SECONDARY, font=SANS),
        ).arrange(RIGHT, buff=0.1)
        legend_red = VGroup(
            Line(ORIGIN, RIGHT * 0.5, color=RED, stroke_width=3),
            Text("misses mu", font_size=SMALL_SIZE, color=RED, font=SANS),
        ).arrange(RIGHT, buff=0.1)
        legend = VGroup(legend_green, legend_red).arrange(RIGHT, buff=0.4)
        legend.to_edge(DOWN, buff=0.3)

        self.play(Create(ci_group, lag_ratio=0.05), run_time=SLOW)
        self.play(
            Create(mu_line),
            FadeIn(mu_label_mob),
            FadeIn(legend),
            run_time=NORMAL,
        )
        self.wait(5)

        # Count how many miss
        n_miss = sum(
            1 for i in range(n_intervals)
            if rng.normal(0, 1) < -1.96 or rng.normal(0, 1) > 1.96
        )
        count_text = Text(
            f"19 out of 20 intervals contain mu (95%)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(count_text, DOWN, sim_title)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Choosing the Confidence Level (1:30)
    # ------------------------------------------------------------------
    def scene5_confidence_levels(self):
        self.add_subcaption(
            "The confidence level is a trade-off. Higher confidence means "
            "a wider interval. 90 percent, 95 percent, and 99 percent are "
            "the most common choices. Each uses a different critical value z star.",
            duration=14,
        )

        title = self.ly.title("Choosing the Confidence Level")

        levels = [
            ("90%", "z* = 1.645", "Narrower interval, less confidence"),
            ("95%", "z* = 1.960", "Standard choice"),
            ("99%", "z* = 2.576", "Wider interval, more confidence"),
        ]

        items = []
        for level_name, z_val, desc in levels:
            level_text = Text(
                f"{level_name}:  {z_val}  --  {desc}",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            )
            items.append(level_text)

        self.ly.progressive_reveal(items, start_from=title)
        self.wait(6)

        # Visual comparison: three intervals
        self.ly.clear()

        self.add_subcaption(
            "Visually, higher confidence means wider intervals. "
            "A 99 percent interval is much wider than a 90 percent one.",
            duration=10,
        )

        vis_title = self.ly.title("Interval Width Comparison")

        mu_vis = 3.0  # center
        intervals = [
            (1.645, SECONDARY, "90%"),
            (1.96, PRIMARY, "95%"),
            (2.576, ACCENT, "99%"),
        ]

        int_group = VGroup()
        y_positions = [1.0, 0.3, -0.4]

        for (z, color, label_text), y in zip(intervals, y_positions):
            half_width = z * 0.6
            bar = Line(
                start=[mu_vis - half_width, y, 0],
                end=[mu_vis + half_width, y, 0],
                stroke_width=4,
                color=color,
            )
            left_dot = Dot(
                point=[mu_vis - half_width, y, 0],
                radius=0.05, color=color,
            )
            right_dot = Dot(
                point=[mu_vis + half_width, y, 0],
                radius=0.05, color=color,
            )
            lbl = Text(
                label_text, font_size=SMALL_SIZE, color=color, font=SANS,
            )
            lbl.next_to(bar, LEFT, buff=0.2)

            int_group.add(bar, left_dot, right_dot, lbl)

        self.ly.center_in_content(int_group)

        self.play(Create(int_group, lag_ratio=0.1), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Worked Example (2:00)
    # ------------------------------------------------------------------
    def scene6_worked_example(self):
        self.add_subcaption(
            "Let us work through a concrete example. We take a sample of "
            "size 50, observe a sample mean of 24.8, and know the population "
            "standard deviation is 6.2. We want a 95 percent confidence "
            "interval.",
            duration=14,
        )

        title = self.ly.title("Worked Example")

        # Given
        given = Text(
            "Given: n = 50,  x-bar = 24.8,  sigma = 6.2,  95% CI",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(given, DOWN, title)
        self.wait(6)

        # Step 1: z*
        self.add_subcaption(
            "Step one: the critical value for 95 percent confidence "
            "is z star equals 1.96.",
            duration=8,
        )

        step1 = MathTex(
            r"z^*",
            r"=",
            r"1.96",
            font_size=HEADING_SIZE,
        )
        step1.set_color_by_tex(r"1.96", PRIMARY)
        box1 = self.ly.formula_box(step1)

        self.play(
            FadeOut(given),
            FadeIn(box1, shift=UP * 0.15),
            run_time=NORMAL,
        )
        self.wait(5)

        # Step 2: ME
        self.add_subcaption(
            "Step two: compute the margin of error. It is 1.96 times "
            "6.2 divided by the square root of 50, which equals 1.72.",
            duration=10,
        )

        step2 = MathTex(
            r"\text{ME}",
            r"=",
            r"1.96",
            r"\cdot",
            r"\frac{6.2}{\sqrt{50}}",
            r"=",
            r"1.72",
            font_size=HEADING_SIZE,
        )
        step2.set_color_by_tex(r"1.96", PRIMARY)
        step2.set_color_by_tex(r"6.2", ACCENT)
        step2.set_color_by_tex(r"1.72", SECONDARY)
        box2 = self.ly.formula_box(step2)

        self.play(Transform(box1, box2), run_time=SLOW)
        self.wait(7)

        # Step 3: Final CI
        self.add_subcaption(
            "Step three: the confidence interval is 24.8 plus or minus "
            "1.72, giving us the interval from 23.08 to 26.52.",
            duration=10,
        )

        step3 = MathTex(
            r"(",
            r"24.8",
            r"-",
            r"1.72",
            r",\;",
            r"24.8",
            r"+",
            r"1.72",
            r")",
            r"=",
            r"(23.08,\; 26.52)",
            font_size=HEADING_SIZE,
        )
        step3.set_color_by_tex(r"24.8", PRIMARY)
        step3.set_color_by_tex(r"1.72", PRIMARY)
        step3.set_color_by_tex(r"(23.08,\; 26.52)", SECONDARY)
        box3 = self.ly.formula_box(step3)

        self.play(Transform(box1, box3), run_time=SLOW)
        self.wait(6)

        # Interpretation
        self.ly.clear()

        self.add_subcaption(
            "Interpretation: we are 95 percent confident that the true "
            "mean lies between 23.08 and 26.52. This means that if we "
            "repeated this process many times, 95 percent of intervals "
            "would contain the true mean.",
            duration=16,
        )

        interp_title = self.ly.title("Interpretation")

        interp = Text(
            "We are 95% confident that\n"
            "the true mean mu is between 23.08 and 26.52",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(interp, DOWN, interp_title)
        self.wait(8)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: The t-Distribution (2:00)
    # ------------------------------------------------------------------
    def scene7_t_distribution(self):
        self.add_subcaption(
            "In practice, we almost never know the true population "
            "standard deviation sigma. Instead we estimate it with the "
            "sample standard deviation s. This changes the formula slightly.",
            duration=13,
        )

        title = self.ly.title("When Sigma is Unknown")

        items = [
            Text(
                "Replace sigma with sample standard deviation s",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "This introduces extra uncertainty: s varies from sample to sample",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "The standardized statistic follows a t-distribution instead",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)

        self.ly.clear()

        # t-distribution properties
        self.add_subcaption(
            "The t-distribution is like the normal distribution but "
            "with heavier tails. It depends on the degrees of freedom, "
            "which is n minus 1. As n grows, the t-distribution "
            "approaches the standard normal.",
            duration=15,
        )

        t_title = self.ly.title("The t-Distribution")

        t_props = [
            Text(
                "Heavier tails than the normal distribution",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Shape depends on degrees of freedom (n - 1)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "More degrees of freedom = closer to normal",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "For large n: t and normal are nearly identical",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(t_props, start_from=t_title)
        self.wait(5)

        self.ly.clear()

        # Visual: normal vs t
        self.add_subcaption(
            "Here we compare the standard normal with t-distributions "
            "at 3, 10, and 30 degrees of freedom. Notice how the tails "
            "shrink as degrees of freedom increase.",
            duration=12,
        )

        vis_title = self.ly.title("Normal vs t-Distribution")

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.45, 0.1],
            x_length=7,
            y_length=3,
            axis_config={
                "color": DIM,
                "stroke_width": 1.5,
                "include_numbers": True,
                "font_size": SMALL_SIZE,
            },
        )
        axes.set_opacity(0.7)

        def normal_pdf(x):
            return np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi)

        def t_pdf(x, df):
            from scipy.stats import t as t_dist
            return t_dist.pdf(x, df)

        # Normal curve
        normal_curve = axes.plot(
            normal_pdf, color=ACCENT, stroke_width=3,
        )

        self.ly.center_in_content(axes)
        self.play(Create(axes), run_time=FAST)
        self.play(Create(normal_curve), run_time=NORMAL)

        # t-distributions
        dfs = [3, 10, 30]
        t_colors = [RED, SECONDARY, PRIMARY]
        t_curves = []
        for df, color in zip(dfs, t_colors):
            try:
                t_curve = axes.plot(
                    lambda x, d=df: t_pdf(x, d),
                    color=color, stroke_width=2,
                )
                t_curves.append(t_curve)
                self.play(Create(t_curve), run_time=NORMAL)
                self.wait(1)
            except ImportError:
                # scipy not available, skip
                pass

        # Legend
        normal_legend = VGroup(
            Line(ORIGIN, RIGHT * 0.4, color=ACCENT, stroke_width=3),
            Text("Normal", font_size=SMALL_SIZE, color=ACCENT, font=SANS),
        ).arrange(RIGHT, buff=0.1)

        legend_items = [normal_legend]
        for df, color in zip(dfs, t_colors):
            item = VGroup(
                Line(ORIGIN, RIGHT * 0.4, color=color, stroke_width=2),
                Text(f"t (df={df})", font_size=SMALL_SIZE, color=color, font=SANS),
            ).arrange(RIGHT, buff=0.1)
            legend_items.append(item)

        legend = VGroup(*legend_items).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        legend.to_corner(UR, buff=0.3)

        self.play(FadeIn(legend), run_time=FAST)
        self.wait(5)

        self.ly.clear()

        # t-based CI formula
        self.add_subcaption(
            "The confidence interval formula using the t-distribution "
            "replaces z star with t star, and sigma with s. The critical "
            "value t star depends on both the confidence level and the "
            "degrees of freedom.",
            duration=14,
        )

        ci_t_title = self.ly.title("CI with the t-Distribution")

        ci_t_formula = MathTex(
            r"\bar{X}",
            r"\pm",
            r"t^*_{n-1}",
            r"\frac{s}{\sqrt{n}}",
            font_size=HEADING_SIZE,
        )
        ci_t_formula.set_color_by_tex(r"\bar{X}", PRIMARY)
        ci_t_formula.set_color_by_tex(r"t^*_{n-1}", SECONDARY)
        ci_t_formula.set_color_by_tex(r"s", PRIMARY)
        box_t = self.ly.formula_box(ci_t_formula)

        self.play(
            FadeIn(ci_t_title, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.play(
            FadeIn(box_t, shift=UP * 0.15),
            run_time=NORMAL,
        )
        self.play(Write(ci_t_formula), run_time=SLOW)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Summary + Preview (1:30)
    # ------------------------------------------------------------------
    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap. A confidence interval gives a range of "
            "plausible values for a population parameter. The confidence "
            "level tells us how often this method succeeds. When sigma "
            "is unknown, we use the t-distribution.",
            duration=14,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text(
                "CI formula: x-bar plus or minus z star times sigma over root n",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "95% confident means 95% of intervals contain the true mu",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Higher confidence requires wider intervals",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "When sigma is unknown, use t-distribution with n-1 degrees of freedom",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title)

        self.wait(6)
        self.ly.clear()

        # Preview of Video 77
        self.add_subcaption(
            "Next time, we will learn hypothesis testing. If someone "
            "claims the mean is a specific value, how do we evaluate "
            "that claim using our sample data?",
            duration=10,
        )

        next_title = self.ly.title("Coming Up Next")

        next_text = Text(
            "Hypothesis Testing: testing claims about\n"
            "population parameters using sample data",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(next_text, DOWN, next_title)
        self.wait(4)

        self.ly.clear()

        play_outro(self, "Hypothesis Testing", "Probability & Statistics")
