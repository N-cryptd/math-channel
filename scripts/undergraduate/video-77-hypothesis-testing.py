"""Video 77: Hypothesis Testing
Probability & Statistics -- Video 11 of 12

Covers: Null/alternative hypothesis framework, test statistic derivation from CLT,
rejection regions, significance level, p-value calculation, worked example,
Type I/II errors, CI-test duality.

Plan: planning/video-77-hypothesis-testing.md

Render draft:  manim -ql scripts/undergraduate/video-77-hypothesis-testing.py Video77_HypothesisTesting
Render final:  manim -qh scripts/undergraduate/video-77-hypothesis-testing.py Video77_HypothesisTesting
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


class Video77_HypothesisTesting(Scene):
    """Hypothesis Testing -- H0/H1 framework, test statistic, rejection regions,
    p-value, worked example, Type I/II errors, CI-test duality."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook_and_ci_recap()
        self.scene2_null_and_alternative()
        self.scene3_test_statistic()
        self.scene4_rejection_regions()
        self.scene5_p_value()
        self.scene6_worked_example()
        self.scene7_type_I_II_errors()
        self.scene8_ci_duality()
        self.scene9_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook + CI Recap (1:30)
    # ------------------------------------------------------------------
    def scene1_hook_and_ci_recap(self):
        self.add_subcaption(
            "Last time we learned confidence intervals. They give us a range "
            "of plausible values for the population mean. But what if someone "
            "makes a specific claim about that mean? How do we test it?",
            duration=14,
        )
        play_intro(self, "Hypothesis Testing", "Probability & Statistics")

        title = self.ly.title("From Confidence Intervals to Hypothesis Tests")

        items = [
            Text(
                "CI: x-bar +/- z* times sigma over root n",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Gives a range of plausible values for mu",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "But what if someone claims mu = 20? Is that plausible?",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(4)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: The Framework: H0 and H1 (1:30)
    # ------------------------------------------------------------------
    def scene2_null_and_alternative(self):
        self.add_subcaption(
            "Hypothesis testing starts with two competing claims. "
            "The null hypothesis H naught is the default assumption, "
            "like innocent until proven guilty. The alternative "
            "hypothesis H-one is the claim we want to test.",
            duration=16,
        )

        self.ly.section_divider(2, "The Framework: Null and Alternative")

        title = self.ly.title("Two Competing Claims")

        items = [
            Text(
                "H0 (null): the default assumption (status quo)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "H1 (alternative): the claim we seek evidence for",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "We assume H0 is true, then look for evidence against it",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "\"The burden of proof is on the challenger\"",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(4)
        self.ly.clear()

        # Notation
        self.add_subcaption(
            "In notation, we write H naught: mu equals mu-zero for the null, "
            "and H-one: mu not equal to mu-zero for a two-sided alternative. "
            "We can also use one-sided alternatives like mu greater than mu-zero.",
            duration=16,
        )

        title2 = self.ly.title("Notation")

        h0 = MathTex(
            r"H_0", r":", r"\mu", r"=", r"\mu_0",
            font_size=HEADING_SIZE,
        )
        h0.set_color_by_tex(r"H_0", PRIMARY)
        h0.set_color_by_tex(r"\mu_0", ACCENT)

        h1 = MathTex(
            r"H_1", r":", r"\mu", r"\neq", r"\mu_0",
            font_size=HEADING_SIZE,
        )
        h1.set_color_by_tex(r"H_1", SECONDARY)
        h1.set_color_by_tex(r"\mu_0", ACCENT)

        group = VGroup(h0, h1).arrange(DOWN, buff=0.5)
        self.ly.safe_place(group, DOWN, title2)

        self.wait(5)

        # One-sided note
        onesided = Text(
            "One-sided: H1: mu > mu0 or H1: mu < mu0",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(onesided, DOWN, group)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: The Test Statistic (2:00)
    # ------------------------------------------------------------------
    def scene3_test_statistic(self):
        self.add_subcaption(
            "If H naught is true, then mu equals mu-zero. By the Central "
            "Limit Theorem, the sample mean is approximately normal, centered "
            "at mu-zero with standard deviation sigma over root n. "
            "We standardize this to get our test statistic.",
            duration=16,
        )

        self.ly.section_divider(3, "The Test Statistic")

        title = self.ly.title("Building the Test Statistic")

        items = [
            Text(
                "Under H0: X-bar ~ N(mu-zero, sigma squared over n)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Standardize: z = (x-bar - mu-zero) / (sigma / root n)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Under H0, z ~ N(0, 1)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(4)
        self.ly.clear()

        # Formula box
        self.add_subcaption(
            "The test statistic z measures how many standard errors our "
            "sample mean is from the null value. If H-zero is true, z "
            "should be close to zero. A large value of z is evidence "
            "against H-zero.",
            duration=14,
        )

        z_label = Text(
            "Test Statistic",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        z_formula = MathTex(
            r"z",
            r"=",
            r"\frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}",
            font_size=HEADING_SIZE,
        )
        z_formula.set_color_by_tex(r"z", ACCENT)
        z_formula.set_color_by_tex(r"\bar{X}", PRIMARY)
        z_formula.set_color_by_tex(r"\mu_0", ACCENT)
        z_box = self.ly.formula_box(z_formula)

        z_label.move_to(UP * self.ly.content_top)
        self.play(Write(z_label), run_time=NORMAL)
        self.play(FadeIn(z_box, shift=UP * 0.15), run_time=NORMAL)
        self.play(Write(z_formula), run_time=SLOW)
        self.wait(5)

        # Visual: sampling distribution under H0
        self.ly.clear()

        self.add_subcaption(
            "Visually, under H-zero the sampling distribution of x-bar is "
            "centered at mu-zero. Our observed x-bar appears as a point on "
            "this distribution. The test statistic z is how many standard "
            "errors away it is from the center.",
            duration=16,
        )

        vis_title = self.ly.title("Sampling Distribution Under H0")

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.45, 0.1],
            x_length=6,
            y_length=2.5,
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

        curve = axes.plot(normal_pdf, color=PRIMARY, stroke_width=3)
        curve_label = Text(
            "Distribution of z under H0", font_size=SMALL_SIZE,
            color=PRIMARY, font=SANS,
        )
        curve_label.next_to(curve, UP, buff=0.2)

        # Observed test statistic at z = -1.5 (example)
        z_obs = -1.5
        dot = Dot(
            point=axes.c2p(z_obs, normal_pdf(z_obs)),
            radius=0.06, color=ACCENT,
        )
        dot_label = MathTex(
            r"z_{\text{obs}}", r"=", r"-1.5",
            font_size=SMALL_SIZE, color=ACCENT,
        )
        dot_label.next_to(dot, DOWN, buff=0.2)

        group = VGroup(axes, curve, curve_label, dot, dot_label)
        self.ly.center_in_content(group)

        self.play(Create(axes), run_time=FAST)
        self.play(Create(curve), run_time=NORMAL)
        self.play(
            FadeIn(curve_label),
            FadeIn(dot),
            FadeIn(dot_label),
            run_time=NORMAL,
        )
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Rejection Regions and Significance Level (2:00)
    # ------------------------------------------------------------------
    def scene4_rejection_regions(self):
        self.add_subcaption(
            "If H naught is true, z should be near zero. If z is very "
            "far from zero, that is evidence against H naught. But how far "
            "is far enough? We set a threshold called the significance level.",
            duration=14,
        )

        self.ly.section_divider(4, "Rejection Regions")

        title = self.ly.title("How Far Is Far Enough?")

        items = [
            Text(
                "Significance level alpha = P(reject H0 | H0 is true)",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Common choice: alpha = 0.05 (5%)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Rejection region: |z| > z* = 1.96",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(4)
        self.ly.clear()

        # Visual: rejection regions
        self.add_subcaption(
            "Here is the sampling distribution under H-naught. The red "
            "shaded tails are the rejection regions. If our test statistic "
            "falls in the red, we reject H-naught. The total area of the "
            "red tails is exactly alpha, our significance level.",
            duration=18,
        )

        vis_title = self.ly.title("Rejection Regions (alpha = 0.05)")

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

        curve = axes.plot(normal_pdf, color=PRIMARY, stroke_width=3)

        # Rejection regions (left and right tails)
        left_rejection = axes.get_area(
            curve, x_range=[-4, -1.96], color=RED, opacity=0.3,
        )
        right_rejection = axes.get_area(
            curve, x_range=[1.96, 4], color=RED, opacity=0.3,
        )

        # Critical value labels
        z_left_label = MathTex(
            r"-z^*", font_size=LABEL_SIZE, color=RED,
        ).next_to(axes.c2p(-1.96, 0), DOWN, buff=0.15)
        z_right_label = MathTex(
            r"+z^*", font_size=LABEL_SIZE, color=RED,
        ).next_to(axes.c2p(1.96, 0), DOWN, buff=0.15)

        # Dashed lines at critical values
        crit_left = DashedLine(
            axes.c2p(-1.96, 0), axes.c2p(-1.96, normal_pdf(-1.96)),
            color=RED, stroke_width=1.5,
        )
        crit_right = DashedLine(
            axes.c2p(1.96, 0), axes.c2p(1.96, normal_pdf(1.96)),
            color=RED, stroke_width=1.5,
        )

        # Alpha labels in tails
        alpha_left = Text(
            "alpha/2", font_size=SMALL_SIZE, color=RED, font=SANS,
        ).move_to(axes.c2p(-3, 0.06))
        alpha_right = Text(
            "alpha/2", font_size=SMALL_SIZE, color=RED, font=SANS,
        ).move_to(axes.c2p(3, 0.06))

        group = VGroup(axes, curve, left_rejection, right_rejection,
                        z_left_label, z_right_label, crit_left, crit_right,
                        alpha_left, alpha_right)
        self.ly.center_in_content(group)

        self.play(Create(axes), run_time=FAST)
        self.play(Create(curve), run_time=NORMAL)
        self.play(
            FadeIn(left_rejection), FadeIn(right_rejection),
            run_time=NORMAL,
        )
        self.play(
            Create(crit_left), Create(crit_right),
            FadeIn(z_left_label), FadeIn(z_right_label),
            FadeIn(alpha_left), FadeIn(alpha_right),
            run_time=NORMAL,
        )
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: The p-Value (2:00)
    # ------------------------------------------------------------------
    def scene5_p_value(self):
        self.add_subcaption(
            "The p-value is the probability of observing a test statistic "
            "as extreme as ours, assuming H-naught is true. A small "
            "p-value means our data is unlikely under H-naught, so we "
            "reject it. The decision rule: reject H-naught if p < alpha.",
            duration=16,
        )

        self.ly.section_divider(5, "The p-Value")

        title = self.ly.title("The p-Value")

        items = [
            Text(
                "p = P(|Z| >= |z_obs|) assuming H0 is true",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Small p-value = strong evidence against H0",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Decision rule: reject H0 if p < alpha",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(5)
        self.ly.clear()

        # Visual: p-value calculation
        self.add_subcaption(
            "Here is the p-value visually. Our observed test statistic "
            "is at negative 1.90. The p-value is the total area in the "
            "tails beyond 1.90 and negative 1.90. This area is 0.057, "
            "which is greater than alpha equals 0.05.",
            duration=18,
        )

        vis_title = self.ly.title("p-Value Visualization")

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

        curve = axes.plot(normal_pdf, color=PRIMARY, stroke_width=3)

        z_obs_val = -1.90
        p_left = axes.get_area(
            curve, x_range=[-4, z_obs_val], color=RED, opacity=0.35,
        )
        p_right = axes.get_area(
            curve, x_range=[-z_obs_val, 4], color=RED, opacity=0.35,
        )

        # Observed point
        dot = Dot(
            point=axes.c2p(z_obs_val, normal_pdf(z_obs_val)),
            radius=0.06, color=ACCENT,
        )
        dot_label = MathTex(
            r"z_{\text{obs}}", r"=", r"-1.90",
            font_size=LABEL_SIZE, color=ACCENT,
        )
        dot_label.next_to(dot, DOWN, buff=0.2)

        # Dashed lines at observed value
        obs_line_left = DashedLine(
            axes.c2p(z_obs_val, 0),
            axes.c2p(z_obs_val, normal_pdf(z_obs_val)),
            color=ACCENT, stroke_width=1.5,
        )
        obs_line_right = DashedLine(
            axes.c2p(-z_obs_val, 0),
            axes.c2p(-z_obs_val, normal_pdf(-z_obs_val)),
            color=ACCENT, stroke_width=1.5,
        )

        # p-value label
        p_label = MathTex(
            r"p", r"=", r"0.057",
            font_size=HEADING_SIZE, color=RED,
        )
        p_label.move_to(axes.c2p(3, 0.15))

        # alpha label
        alpha_label = MathTex(
            r"\alpha", r"=", r"0.05",
            font_size=LABEL_SIZE, color=DIM,
        )
        alpha_label.move_to(axes.c2p(-3, 0.2))

        group = VGroup(axes, curve, p_left, p_right, dot, dot_label,
                        obs_line_left, obs_line_right, p_label, alpha_label)
        self.ly.center_in_content(group)

        self.play(Create(axes), run_time=FAST)
        self.play(Create(curve), run_time=NORMAL)
        self.play(
            FadeIn(p_left), FadeIn(p_right),
            run_time=NORMAL,
        )
        self.play(
            FadeIn(dot), FadeIn(dot_label),
            Create(obs_line_left), Create(obs_line_right),
            run_time=NORMAL,
        )
        self.play(
            FadeIn(p_label), FadeIn(alpha_label),
            run_time=FAST,
        )
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Worked Example (2:00)
    # ------------------------------------------------------------------
    def scene6_worked_example(self):
        self.add_subcaption(
            "Let us work through a concrete example. A factory claims "
            "its light bulbs last 1000 hours on average. A consumer "
            "group tests 40 bulbs and finds a sample mean of 985 hours. "
            "The population standard deviation is 50 hours. At the "
            "5 percent significance level, is the claim supported?",
            duration=20,
        )

        self.ly.section_divider(6, "Worked Example")

        title = self.ly.title("Light Bulb Lifetime Test")

        # Setup
        setup_text = Text(
            "Factory claims mu = 1000 hrs. Test: n=40, x-bar=985, sigma=50.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(setup_text, DOWN, title)
        self.wait(5)

        # Step 1: H0 and H1
        self.ly.clear()

        self.add_subcaption(
            "Step one: set up the hypotheses. H-naught is mu equals 1000, "
            "and H-one is mu does not equal 1000, a two-sided test.",
            duration=10,
        )

        step_title = self.ly.title("Step 1: Hypotheses")

        h0_text = MathTex(
            r"H_0", r":", r"\mu", r"=", r"1000",
            font_size=HEADING_SIZE,
        )
        h0_text.set_color_by_tex(r"H_0", PRIMARY)
        h1_text = MathTex(
            r"H_1", r":", r"\mu", r"\neq", r"1000",
            font_size=HEADING_SIZE,
        )
        h1_text.set_color_by_tex(r"H_1", SECONDARY)

        hyp_group = VGroup(h0_text, h1_text).arrange(DOWN, buff=0.5)
        self.ly.safe_place(hyp_group, DOWN, step_title)
        self.wait(4)

        # Step 2: Test statistic
        self.ly.clear()

        self.add_subcaption(
            "Step two: compute the test statistic. z equals 985 minus "
            "1000, divided by 50 over the square root of 40, which "
            "equals negative 1.90.",
            duration=12,
        )

        step2_title = self.ly.title("Step 2: Test Statistic")

        z_formula = MathTex(
            r"z",
            r"=",
            r"\frac{985 - 1000}{50 / \sqrt{40}}",
            r"=",
            r"\frac{-15}{7.91}",
            r"=",
            r"-1.90",
            font_size=HEADING_SIZE,
        )
        z_formula.set_color_by_tex(r"985", PRIMARY)
        z_formula.set_color_by_tex(r"1000", ACCENT)
        z_formula.set_color_by_tex(r"-1.90", RED)

        box = self.ly.formula_box(z_formula)
        self.ly.safe_place(box, DOWN, step2_title)
        self.wait(6)

        # Step 3: Decision
        self.ly.clear()

        self.add_subcaption(
            "Step three: compare with the critical value. The absolute "
            "value of z is 1.90, which is less than 1.96. So the test "
            "statistic does NOT fall in the rejection region. We do not "
            "reject H-naught.",
            duration=16,
        )

        step3_title = self.ly.title("Step 3: Decision")

        decision = MathTex(
            r"|z|", r"=", r"1.90", r"<", r"1.96", r"= z^*",
            font_size=HEADING_SIZE,
        )
        decision.set_color_by_tex(r"1.90", PRIMARY)
        decision.set_color_by_tex(r"1.96", RED)

        box3 = self.ly.formula_box(decision)
        self.ly.safe_place(box3, DOWN, step3_title)
        self.wait(5)

        # p-value
        self.ly.clear()

        self.add_subcaption(
            "The p-value is 0.057, which is greater than 0.05. So we "
            "fail to reject H-naught. There is not enough evidence to "
            "say the factory's claim is wrong. This does not prove the "
            "claim is true, just that we cannot refute it.",
            duration=18,
        )

        p_title = self.ly.title("Conclusion")

        p_result = MathTex(
            r"p", r"=", r"0.057", r">", r"0.05", r"=",
            r"\alpha",
            font_size=HEADING_SIZE,
        )
        p_result.set_color_by_tex(r"0.057", RED)
        p_result.set_color_by_tex(r"0.05", DIM)

        box_p = self.ly.formula_box(p_result)
        self.ly.safe_place(box_p, DOWN, p_title)
        self.wait(4)

        conclusion = Text(
            "Fail to reject H0. Not enough evidence to dispute the claim.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(conclusion, DOWN, box_p)
        self.wait(6)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Type I and Type II Errors (1:30)
    # ------------------------------------------------------------------
    def scene7_type_I_II_errors(self):
        self.add_subcaption(
            "Whenever we make a decision in hypothesis testing, we might "
            "make an error. A Type 1 error is rejecting H-naught when it "
            "is actually true, a false positive. Its probability is "
            "exactly alpha. A Type 2 error is failing to reject H-naught "
            "when it is false, a false negative. Its probability is beta.",
            duration=22,
        )

        self.ly.section_divider(7, "Type I and Type II Errors")

        title = self.ly.title("Two Ways to Be Wrong")

        items = [
            Text(
                "Type I: Reject H0 when it is TRUE (false positive)",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Probability of Type I = alpha (the significance level)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Type II: Fail to reject H0 when it is FALSE (false negative)",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Probability of Type II = beta. Power = 1 - beta.",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(4)
        self.ly.clear()

        # 2x2 truth table
        self.add_subcaption(
            "This truth table summarizes all four possible outcomes. "
            "We hope to make a correct decision, either rejecting a "
            "false H-naught or failing to reject a true one. The errors "
            "sit in the off-diagonal cells.",
            duration=16,
        )

        table_title = self.ly.title("Decision Truth Table")

        # Headers
        header_row = VGroup(
            Text("Reality:", font_size=LABEL_SIZE, color=DIM, font=SANS),
            Text("H0 True", font_size=LABEL_SIZE, color=PRIMARY, font=SANS),
            Text("H0 False", font_size=LABEL_SIZE, color=SECONDARY, font=SANS),
        ).arrange(RIGHT, buff=1.0)

        # Row 1: Don't reject
        row1 = VGroup(
            Text("Don't Reject", font_size=LABEL_SIZE, color=WHITE, font=SANS),
            Text("Correct!", font_size=LABEL_SIZE, color=SECONDARY, font=SANS),
            Text("Type II", font_size=LABEL_SIZE, color=RED, font=SANS),
        ).arrange(RIGHT, buff=1.0)

        # Row 2: Reject
        row2 = VGroup(
            Text("Reject H0", font_size=LABEL_SIZE, color=WHITE, font=SANS),
            Text("Type I", font_size=LABEL_SIZE, color=RED, font=SANS),
            Text("Correct!", font_size=LABEL_SIZE, color=SECONDARY, font=SANS),
        ).arrange(RIGHT, buff=1.0)

        table = VGroup(header_row, row1, row2).arrange(DOWN, buff=0.3)
        self.ly.safe_place(table, DOWN, table_title)

        self.wait(5)

        # Power note
        power = Text(
            "Power = P(correctly reject H0) = 1 - beta",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(power, DOWN, table)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: CI and Hypothesis Tests: The Duality (1:00)
    # ------------------------------------------------------------------
    def scene8_ci_duality(self):
        self.add_subcaption(
            "There is a beautiful connection between confidence intervals "
            "and hypothesis tests. A 95 percent confidence interval and a "
            "two-sided test at alpha equals 0.05 always give the same "
            "conclusion. If mu-zero is inside the interval, we do not "
            "reject. If it is outside, we do reject.",
            duration=20,
        )

        self.ly.section_divider(8, "CI-Test Duality")

        title = self.ly.title("Confidence Intervals and Hypothesis Tests")

        items = [
            Text(
                "95% CI and two-sided test at alpha=0.05 give the same answer",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "mu0 INSIDE CI -> do NOT reject H0",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "mu0 OUTSIDE CI -> DO reject H0",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(4)
        self.ly.clear()

        # Visual: CI bar with mu0
        self.add_subcaption(
            "Here is what that looks like. The confidence interval is the "
            "green bar. The null value mu-zero is the yellow marker. If "
            "the marker falls inside the bar, we keep H-naught. If it "
            "falls outside, we reject.",
            duration=16,
        )

        vis_title = self.ly.title("Visual: CI vs Hypothesis Test")

        # CI bar
        ci_left = 23.08
        ci_right = 26.52
        ci_bar = Line(
            start=[ci_left * 0.2, 0, 0],
            end=[ci_right * 0.2, 0, 0],
            stroke_width=6, color=SECONDARY,
        )
        # Endpoint dots
        ci_left_dot = Dot(
            point=[ci_left * 0.2, 0, 0], radius=0.06, color=SECONDARY,
        )
        ci_right_dot = Dot(
            point=[ci_right * 0.2, 0, 0], radius=0.06, color=SECONDARY,
        )

        # Center mark
        ci_center_dot = Dot(
            point=[24.8 * 0.2, 0, 0], radius=0.04, color=PRIMARY,
        )
        ci_label = Text(
            "95% CI: (23.08, 26.52)", font_size=LABEL_SIZE,
            color=SECONDARY, font=SANS,
        ).next_to(ci_bar, UP, buff=0.3)

        ci_group = VGroup(ci_bar, ci_left_dot, ci_right_dot,
                          ci_center_dot, ci_label)

        # mu0 marker (INSIDE the CI)
        mu0_val = 24.0
        mu0_line = DashedLine(
            [mu0_val * 0.2, -0.4, 0],
            [mu0_val * 0.2, 0.4, 0],
            color=ACCENT, stroke_width=2,
        )
        mu0_text = Text(
            r"mu_0 = 24", font_size=LABEL_SIZE,
            color=ACCENT, font=SANS,
        ).next_to(mu0_line, DOWN, buff=0.1)

        mu0_marker = VGroup(mu0_line, mu0_text)

        full_group = VGroup(ci_group, mu0_marker)
        self.ly.center_in_content(full_group)

        self.play(
            FadeIn(ci_group, shift=UP * 0.15),
            run_time=NORMAL,
        )
        self.play(FadeIn(mu0_marker), run_time=NORMAL)
        self.wait(3)

        result_text = Text(
            "mu0 is INSIDE the CI -> Do NOT reject H0",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(result_text, DOWN, full_group)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Summary + Preview (1:30)
    # ------------------------------------------------------------------
    def scene9_summary(self):
        self.add_subcaption(
            "Let us recap what we learned. Hypothesis testing gives us "
            "a principled framework for evaluating claims about population "
            "parameters using sample data. The test statistic comes from "
            "the CLT. The p-value quantifies the evidence. And hypothesis "
            "tests are deeply connected to confidence intervals.",
            duration=22,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text(
                "H0 is the default; reject only if evidence is strong (p < alpha)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Test statistic z = (x-bar - mu-zero) / (sigma / root n)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Type I error probability = alpha; Type II error probability = beta",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "A 95% CI and a two-sided test at alpha=0.05 always agree",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title)

        self.wait(6)
        self.ly.clear()

        # Preview of Video 78
        self.add_subcaption(
            "Next time, we wrap up the Probability and Statistics "
            "playlist with Regression. We will learn how to model "
            "relationships between variables using the tools we have "
            "built throughout this entire series.",
            duration=14,
        )

        next_title = self.ly.title("Coming Up Next")

        next_text = Text(
            "Regression: modeling relationships\n"
            "between variables with data",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(next_text, DOWN, next_title)
        self.wait(4)

        self.ly.clear()

        play_outro(self, "Regression", "Probability & Statistics")
