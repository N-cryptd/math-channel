"""Video 75: Central Limit Theorem
Probability & Statistics -- Video 9 of 12

Covers: CLT statement (sum and mean forms), Galton board visual,
sampling distribution of the mean, normal approximation,
examples with different population distributions (uniform, exponential, bimodal),
connection to LLN from Video 74, real-world applications,
assumptions and caveats, preview of Video 76.

Plan: planning/video-75-central-limit-theorem.md

Render draft:  manim -ql scripts/undergraduate/video-75-central-limit-theorem.py Video75_CentralLimitTheorem
Render final:  manim -qh scripts/undergraduate/video-75-central-limit-theorem.py Video75_CentralLimitTheorem
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


class Video75_CentralLimitTheorem(Scene):
    """Central Limit Theorem -- CLT statement, sampling distributions,
    Galton board, universality, applications."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook_and_lln_recap()
        self.scene2_galton_board()
        self.scene3_clt_statement()
        self.scene4_dice_example()
        self.scene5_universality()
        self.scene6_intuition()
        self.scene7_applications()
        self.scene8_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook + LLN Recap (1:30)
    # ------------------------------------------------------------------
    def scene1_hook_and_lln_recap(self):
        self.add_subcaption(
            "Last time, we saw the Law of Large Numbers: the sample mean "
            "converges to the true expected value. But it does not tell us "
            "about the shape of those fluctuations.",
            duration=12,
        )
        play_intro(self, "Central Limit Theorem", "Probability & Statistics")

        title = self.ly.title("Where LLN Leaves Off")

        items = [
            Text(
                "LLN tells us WHERE the sample mean converges: to mu",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "But LLN says nothing about the SHAPE of the fluctuations",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Do sample means scatter uniformly? Skew left? Bell-shaped?",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "There is a beautiful theorem that answers this exactly",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(4)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: The Galton Board (2:30)
    # ------------------------------------------------------------------
    def scene2_galton_board(self):
        self.add_subcaption(
            "Imagine dropping thousands of tiny balls through a peg board. "
            "At each peg, each ball bounces left or right with equal "
            "probability. Where do they land?",
            duration=11,
        )
        title = self.ly.title("The Galton Board")

        # Visual: Show concept with a simplified illustration
        desc = Text(
            "Balls drop through rows of pegs, bouncing left or right at each level",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(desc, DOWN, title)
        self.wait(4)

        # Show that the final position = sum of many small binary choices
        insight = MathTex(
            r"\text{Final position}", r"=", r"\sum_{i=1}^{n}", r"X_i",
            r"\quad", r"(X_i \in \{-1, +1\})",
            font_size=BODY_SIZE,
        )
        insight.set_color_by_tex(r"\sum_{i=1}^{n}", PRIMARY)
        insight.set_color_by_tex(r"X_i", ACCENT)
        formula_box = self.ly.formula_box(insight)
        self.play(
            FadeOut(desc),
            FadeIn(formula_box, shift=UP * 0.15),
            run_time=NORMAL,
        )
        self.wait(4)

        # Key insight: binomial -> bell curve
        self.add_subcaption(
            "The binomial distribution from thousands of small random "
            "choices forms a smooth bell curve. This is the Central Limit "
            "Theorem in action, before we even state it.",
            duration=10,
        )

        self.ly.clear()

        result_title = self.ly.title("The Result")

        result_items = [
            Text(
                "The distribution of landing positions is binomial",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "For thousands of pegs, this binomial is nearly indistinguishable",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "from a perfect Gaussian bell curve",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(result_items, start_from=result_title)

        self.wait(3)

        # Show the Gaussian shape
        self.ly.clear()

        gauss_title = self.ly.title("The Bell Curve Emerges")

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

        def gaussian(x):
            return np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi)

        gauss_curve = axes.plot(gaussian, color=PRIMARY, stroke_width=3)
        gauss_label = Text(
            "Gaussian / Normal", font_size=SMALL_SIZE,
            color=PRIMARY, font=SANS,
        )
        gauss_label.next_to(axes, DOWN, buff=0.15)

        self.ly.center_in_content(axes)
        gauss_label.move_to(axes.get_bottom() + DOWN * 0.3)

        self.play(Create(axes), run_time=NORMAL)
        self.play(Create(gauss_curve), run_time=SLOW)
        self.play(FadeIn(gauss_label), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: CLT Statement (2:00)
    # ------------------------------------------------------------------
    def scene3_clt_statement(self):
        self.add_subcaption(
            "The Central Limit Theorem says: let X one through X n be "
            "independent, identically distributed random variables, with "
            "expected value mu and finite variance sigma squared. Then the "
            "sample mean is approximately normal for large n.",
            duration=14,
        )

        self.ly.section_divider(3, "CLT Statement")

        # Setup
        setup = Text(
            r"Let $X_1, X_2, \dots, X_n$ be i.i.d. with "
            r"$E[X_i] = \mu$, $\text{Var}(X_i) = \sigma^2$",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.play(FadeIn(setup, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(10)

        # Sum formulation
        self.add_subcaption(
            "The sum of the observations is approximately normal with "
            "mean n times mu and variance n times sigma squared.",
            duration=9,
        )

        sum_title = Text(
            "Sum Formulation", font_size=HEADING_SIZE,
            color=PRIMARY, font=SANS,
        )
        sum_formula = MathTex(
            r"S_n", r"=", r"\sum_{i=1}^{n}", r"X_i",
            r"\;\approx\;", r"\mathcal{N}(",
            r"n\mu", r",\;", r"n\sigma^2", r")",
            font_size=HEADING_SIZE,
        )
        sum_formula.set_color_by_tex(r"S_n", PRIMARY)
        sum_formula.set_color_by_tex(r"\mathcal{N}", ACCENT)
        sum_formula.set_color_by_tex(r"n\mu", SECONDARY)
        sum_formula.set_color_by_tex(r"n\sigma^2", SECONDARY)
        sum_box = self.ly.formula_box(sum_formula)

        self.play(
            FadeOut(setup),
            FadeIn(sum_title, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        sum_title.move_to(UP * self.ly.content_top)
        sum_box.move_to(ORIGIN)

        self.play(Write(sum_formula), run_time=SLOW)
        self.wait(7)

        # Mean formulation
        self.add_subcaption(
            "Equivalently, the sample mean is approximately normal with "
            "mean mu and variance sigma squared over n. As n grows, "
            "the sampling distribution narrows around the true mean.",
            duration=12,
        )

        mean_title = Text(
            "Mean Formulation", font_size=HEADING_SIZE,
            color=PRIMARY, font=SANS,
        )
        mean_formula = MathTex(
            r"\bar{X}_n", r"=", r"\frac{1}{n}",
            r"\sum_{i=1}^{n}", r"X_i",
            r"\;\approx\;", r"\mathcal{N}(",
            r"\mu", r",\;", r"\frac{\sigma^2}{n}", r")",
            font_size=HEADING_SIZE,
        )
        mean_formula.set_color_by_tex(r"\bar{X}_n", PRIMARY)
        mean_formula.set_color_by_tex(r"\mathcal{N}", ACCENT)
        mean_formula.set_color_by_tex(r"\mu", SECONDARY)
        mean_formula.set_color_by_tex(r"\frac{\sigma^2}{n}", SECONDARY)
        mean_box = self.ly.formula_box(mean_formula)

        self.play(
            FadeOut(sum_title), FadeOut(sum_box),
            FadeIn(mean_title, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        mean_title.move_to(UP * self.ly.content_top)
        mean_box.move_to(ORIGIN)

        self.play(Write(mean_formula), run_time=SLOW)
        self.wait(10)

        # Standardized form
        self.add_subcaption(
            "The standardized version converges to the standard normal "
            "distribution. This is the most useful form for computations.",
            duration=9,
        )

        std_formula = MathTex(
            r"Z_n", r"=", r"\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}}",
            r"\;\xrightarrow{d}\;", r"\mathcal{N}(0, 1)",
            font_size=HEADING_SIZE,
        )
        std_formula.set_color_by_tex(r"Z_n", PRIMARY)
        std_formula.set_color_by_tex(r"\mathcal{N}(0, 1)", ACCENT)
        std_box = self.ly.formula_box(std_formula)

        self.play(
            FadeOut(mean_title), FadeOut(mean_box),
            FadeIn(std_box, shift=UP * 0.15),
            run_time=NORMAL,
        )
        self.play(Write(std_formula), run_time=SLOW)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Dice Example -- From Uniform to Normal (2:00)
    # ------------------------------------------------------------------
    def scene4_dice_example(self):
        self.add_subcaption(
            "Consider rolling a fair die. The population is uniform: each "
            "face has probability one sixth. What happens when we take the "
            "mean of multiple rolls?",
            duration=11,
        )

        title = self.ly.title("Dice: From Uniform to Bell Curve")

        # Show uniform population
        self.wait(9)
        self.add_subcaption(
            "A single die roll is uniform. But watch what happens to the "
            "sampling distribution as we increase the sample size from two "
            "to one hundred rolls.",
            duration=9,
        )

        # Simulate sampling distribution of the mean
        rng = np.random.RandomState(42)
        sample_sizes = [2, 5, 30, 100]
        n_samples = 10000

        for idx, n in enumerate(sample_sizes):
            # Generate sample means
            rolls = rng.randint(1, 7, size=(n_samples, n))
            means = rolls.mean(axis=1)

            # Histogram
            axes = Axes(
                x_range=[1, 6, 1],
                y_range=[0, 0.7, 0.1],
                x_length=6,
                y_length=3,
                axis_config={
                    "color": DIM,
                    "stroke_width": 1.5,
                    "include_numbers": True,
                    "font_size": SMALL_SIZE,
                },
            )
            axes.set_opacity(0.7)

            # Create histogram bars manually
            bins = np.linspace(1, 6, 26)
            counts, _ = np.histogram(means, bins=bins, density=True)
            bar_width = (bins[1] - bins[0])
            bar_group = VGroup()

            for i, count in enumerate(counts):
                if count > 0.005:
                    bar = Rectangle(
                        width=bar_width * 0.9,
                        height=count * 3,
                        fill_color=PRIMARY,
                        fill_opacity=0.7,
                        stroke_color=PRIMARY,
                        stroke_width=1,
                    )
                    bar.move_to(axes.c2p(
                        (bins[i] + bins[i + 1]) / 2,
                        count / 2,
                    ))
                    bar_group.add(bar)

            n_label = Text(
                f"n = {n}",
                font_size=HEADING_SIZE, color=ACCENT, font=MONO,
            )

            if idx == 0:
                self.ly.center_in_content(axes)
                n_label.to_edge(UP, buff=0.4)
                self.play(Create(axes), run_time=FAST)
                self.play(FadeIn(n_label), run_time=FAST)
            else:
                new_axes = axes.copy()
                new_bar_group = bar_group.copy()
                new_n_label = Text(
                    f"n = {n}",
                    font_size=HEADING_SIZE, color=ACCENT, font=MONO,
                )
                new_n_label.to_edge(UP, buff=0.4)
                self.play(
                    FadeOut(bar_group), FadeOut(axes), FadeOut(n_label),
                    run_time=FAST,
                )
                self.ly.center_in_content(new_axes)
                self.add(new_axes, new_bar_group, new_n_label)
                axes = new_axes
                bar_group = new_bar_group
                n_label = new_n_label

            self.play(FadeIn(bar_group, lag_ratio=0.02), run_time=FAST)
            self.wait(1.5)

        self.wait(3)
        self.ly.clear()

        # Summary of dice demo
        self.add_subcaption(
            "Even though the population is perfectly flat, the sampling "
            "distribution of the mean converges to a bell curve as the "
            "sample size increases. This is not a coincidence.",
            duration=10,
        )

        result = Text(
            "Flat population + large samples = bell-shaped sampling distribution",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.center_in_content(result)
        self.play(FadeIn(result, shift=UP * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: CLT Universality -- Multiple Populations (2:00)
    # ------------------------------------------------------------------
    def scene5_universality(self):
        self.add_subcaption(
            "The Central Limit Theorem works for any population distribution, "
            "as long as the variance is finite. Uniform, exponential, bimodal, "
            "it does not matter. They all produce bell-shaped sampling "
            "distributions for large enough samples.",
            duration=14,
        )

        title = self.ly.title("Universality of the CLT")

        # Show 3 population shapes
        populations = [
            ("Uniform", SECONDARY, "Flat: every value equally likely"),
            ("Exponential", SECONDARY, "Right-skewed: small values most common"),
            ("Bimodal", SECONDARY, "Two peaks: mixture of two groups"),
        ]

        for pop_name, color, description in populations:
            pop_label = Text(
                f"Population: {pop_name}",
                font_size=BODY_SIZE, color=color, font=SANS,
            )
            pop_desc = Text(
                description,
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            )
            sampling_label = Text(
                f"Sampling dist. (n=30):",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            )
            result = Text(
                "Approximately Normal!",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            )

            pair = VGroup(
                VGroup(pop_label, pop_desc).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
                Text("->", font_size=HEADING_SIZE, color=DIM, font=SANS),
                VGroup(sampling_label, result).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.5)

            # Use progressive reveal for each population
            self.ly.progressive_reveal(
                [pop_label, pop_desc, sampling_label, result],
                start_from=title,
            )
            self.wait(6)
            self.ly.clear()

        # Key message
        self.add_subcaption(
            "This is why the normal distribution appears everywhere in nature "
            "and science. Any quantity that is the sum or average of many "
            "small independent effects will be approximately normal.",
            duration=11,
        )

        key_msg = Text(
            "Any population shape + many samples = Normal distribution",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.center_in_content(key_msg)
        self.play(Write(key_msg), run_time=SLOW)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Why Does It Work? (Intuition) (1:30)
    # ------------------------------------------------------------------
    def scene6_intuition(self):
        self.add_subcaption(
            "Why does the Central Limit Theorem hold? Each observation "
            "contributes a small random amount to the sum. Positive and "
            "negative deviations tend to cancel out. The most likely "
            "configuration is centered on the expected value.",
            duration=12,
        )

        title = self.ly.title("Intuition: Why the Bell Curve?")

        items = [
            Text(
                "Each X_i adds a small random amount to the sum",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Positive and negative deviations cancel out",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "By LLN, they cancel in a predictable, symmetric way",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "The most probable configuration is centered on mu",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(8)
        self.ly.clear()

        # Connection to characteristic functions
        self.add_subcaption(
            "A formal proof uses characteristic functions and Levy's "
            "continuity theorem. The key idea: the logarithm of the "
            "characteristic function of a sum is the sum of the logarithms, "
            "and its Taylor expansion is a quadratic, which corresponds "
            "to a Gaussian.",
            duration=16,
        )

        proof_title = self.ly.title("Proof Sketch (Characteristic Functions)")

        proof_items = [
            Text(
                "Characteristic function of sum = product of individual CFs",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Take the logarithm: becomes a sum of log-CFs",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Taylor expansion: dominated by the quadratic term",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Quadratic in the exponent = Gaussian!",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(proof_items, start_from=proof_title)

        self.wait(5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Real-World Applications (1:30)
    # ------------------------------------------------------------------
    def scene7_applications(self):
        self.add_subcaption(
            "The Central Limit Theorem is the workhorse of statistics. "
            "It explains why polling works, how quality control operates, "
            "and why medical trials can draw conclusions from small samples.",
            duration=10,
        )

        title = self.ly.title("Applications")

        apps = [
            Text(
                "Polling: 1000 people predict an election because "
                "the CLT gives us the margin of error",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Quality Control: average defect rate across sampled "
                "products follows a predictable normal distribution",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Medical Trials: treatment effects measured by sample "
                "means, analyzed with normal-based tests",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Finance: portfolio returns (weighted average of many "
                "assets) are approximately normally distributed",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(apps, start_from=title)

        self.wait(4)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: CLT + LLN Together + Summary (2:00)
    # ------------------------------------------------------------------
    def scene8_summary(self):
        self.add_subcaption(
            "Let us bring it all together. The Law of Large Numbers tells "
            "us where the sample mean converges. The Central Limit Theorem "
            "describes the shape of that convergence. Together, they are "
            "the foundation of all statistical inference.",
            duration=13,
        )

        title = self.ly.title("LLN and CLT: Two Pillars")

        # LLN column
        lln_label = Text(
            "Law of Large Numbers", font_size=HEADING_SIZE,
            color=PRIMARY, font=SANS,
        )
        lln_where = Text(
            "WHERE:", font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        lln_desc = Text(
            "Sample mean converges to mu",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        lln_formula = MathTex(
            r"\bar{X}_n \to \mu",
            font_size=BODY_SIZE,
        ).set_color(PRIMARY)

        lln_col = VGroup(lln_label, lln_where, lln_desc, lln_formula).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT,
        )

        # CLT column
        clt_label = Text(
            "Central Limit Theorem", font_size=HEADING_SIZE,
            color=SECONDARY, font=SANS,
        )
        clt_shape = Text(
            "SHAPE:", font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        clt_desc = Text(
            "Fluctuations are bell-shaped",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        clt_formula = MathTex(
            r"\bar{X}_n \approx \mathcal{N}(\mu, \sigma^2/n)",
            font_size=BODY_SIZE,
        ).set_color(SECONDARY)

        clt_col = VGroup(clt_label, clt_shape, clt_desc, clt_formula).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT,
        )

        self.ly.two_columns([lln_col], [clt_col], start_from=title)

        self.play(
            *[FadeIn(m, shift=LEFT * 0.15) for m in [lln_col, clt_col]],
            run_time=NORMAL,
        )
        self.wait(4)
        self.ly.clear()

        # Assumptions
        self.add_subcaption(
            "The CLT requires three assumptions: the samples are "
            "independent and identically distributed, the population "
            "has finite variance, and the sample size is large enough. "
            "A common rule of thumb is n at least thirty for non-normal "
            "populations.",
            duration=14,
        )

        assume_title = self.ly.title("Assumptions")

        assumptions = [
            Text(
                "1. Observations are i.i.d. (independent, identically distributed)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. Finite variance (sigma squared is not infinite)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "3. Sample size is large enough",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Rule of thumb: n >= 30 for non-normal populations",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(assumptions, start_from=assume_title)

        self.wait(4)
        self.ly.clear()

        # Preview of Video 76
        self.add_subcaption(
            "Now that we know the sampling distribution is approximately "
            "normal, we can use it to build confidence intervals. That is "
            "exactly what we will do in the next video.",
            duration=10,
        )

        next_title = self.ly.title("Coming Up Next")

        next_text = Text(
            "Confidence Intervals: quantifying our uncertainty\n"
            "about the true mean using the CLT",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(next_text, DOWN, next_title)
        self.wait(4)

        self.ly.clear()

        # Key takeaways
        takeaways_title = self.ly.title("Key Takeaways")

        takeaways = [
            Text(
                "Sample means are approximately normally distributed",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Works for ANY population with finite variance",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "LLN + CLT form the foundation of statistics",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(takeaways, start_from=takeaways_title)

        self.wait(4)
        self.ly.clear()

        play_outro(self, "Confidence Intervals", "Probability & Statistics")
