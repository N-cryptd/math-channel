"""Video 74: Law of Large Numbers
Probability & Statistics -- Video 8 of 12

Covers: Weak LLN, Strong LLN, Bernoulli coin flip simulation,
convergence visualization, Chebyshev proof sketch, real-world applications.

Plan: planning/video-74-law-of-large-numbers.md

Render draft:  manim -ql scripts/undergraduate/video-74-law-of-large-numbers.py Video74_LawOfLargeNumbers
Render final:  manim -qh scripts/undergraduate/video-74-law-of-large-numbers.py Video74_LawOfLargeNumbers
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


class Video74_LawOfLargeNumbers(Scene):
    """Law of Large Numbers — Weak form, Strong form, simulation, applications."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_sample_mean()
        self.scene3_coin_simulation()
        self.scene4_weak_law()
        self.scene5_strong_law()
        self.scene6_applications()
        self.scene7_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook — The Casino Paradox
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Why does the casino always win in the long run? "
            "The Law of Large Numbers holds the answer.",
            duration=5,
        )
        play_intro(self, "Law of Large Numbers", "Probability & Statistics")

        title = self.ly.title("The Casino Paradox")

        items = [
            Text("One spin of the wheel — anything can happen",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Ten thousand spins — the house edge appears",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("A fundamental theorem guarantees this convergence",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: What is the Sample Mean?
    # ------------------------------------------------------------------
    def scene2_sample_mean(self):
        self.add_subcaption(
            "Let X one through X n be independent, identically distributed "
            "random variables. Their sample mean converges to the expected value.",
            duration=8,
        )

        self.ly.section_divider(2, "The Sample Mean")

        # i.i.d. definition
        iid = Text(
            r"Let $X_1, X_2, \dots, X_n$ be i.i.d. with $E[X_i] = \mu$",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.play(FadeIn(iid, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Sample mean formula
        sample_mean = MathTex(
            r"\bar{X}_n", r"=", r"\frac{1}{n}", r"\sum_{i=1}^{n}", r"X_i",
            font_size=HEADING_SIZE,
        )
        sample_mean.set_color_by_tex(r"\bar{X}_n", PRIMARY)
        sample_mean.set_color_by_tex(r"\frac{1}{n}", ACCENT)
        formula_box = self.ly.formula_box(sample_mean)
        self.play(Write(sample_mean), run_time=SLOW)
        self.wait(1)

        self.play(FadeOut(iid), FadeOut(formula_box), run_time=FAST)

        # Key properties
        props_title = self.ly.title("Key Properties")

        props = [
            MathTex(
                r"E[\bar{X}_n] = \mu",
                font_size=BODY_SIZE,
            ).set_color(PRIMARY),
            MathTex(
                r"\text{Var}(\bar{X}_n) = \frac{\sigma^2}{n}",
                font_size=BODY_SIZE,
            ).set_color(SECONDARY),
            Text(
                r"As $n \to \infty$, the variance shrinks to zero",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(props, start_from=props_title)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Coin Flip Simulation
    # ------------------------------------------------------------------
    def scene3_coin_simulation(self):
        self.add_subcaption(
            "Consider flipping a fair coin. The proportion of heads "
            "should approach one half. Let us watch this happen.",
            duration=7,
        )

        title = self.ly.title("Coin Flip Simulation")

        # Fixed random seed for reproducibility
        rng = np.random.RandomState(42)
        n_flips = 500
        flips = rng.randint(0, 2, size=n_flips)  # 0=tails, 1=heads

        # Running proportion of heads
        running_prop = np.cumsum(flips) / np.arange(1, n_flips + 1)

        # Create axes
        axes = Axes(
            x_range=[0, n_flips, 100],
            y_range=[0, 1, 0.1],
            x_length=8,
            y_length=3.5,
            axis_config={
                "color": DIM,
                "stroke_width": 1.5,
                "include_numbers": False,
                "font_size": SMALL_SIZE,
            },
        )
        axes.set_opacity(0.7)

        # True probability line at 0.5
        true_line = axes.get_horizontal_line(
            axes.c2p(0, 0.5),
            color=SECONDARY,
            stroke_width=2,
        )
        true_label = Text(
            "p = 0.5", font_size=SMALL_SIZE, color=SECONDARY, font=MONO,
        )
        true_label.next_to(true_line, RIGHT, buff=0.15)

        # The sample mean curve
        x_vals = np.arange(1, n_flips + 1)
        points = [
            axes.c2p(x_vals[i], running_prop[i])
            for i in range(n_flips)
        ]
        sample_curve = VMobject()
        sample_curve.set_points_smoothly(points)
        sample_curve.set_color(PRIMARY)
        sample_curve.set_stroke_width(2.5)

        # Axis labels
        x_label = Text(
            "Number of flips (n)", font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        x_label.next_to(axes, DOWN, buff=0.2)
        y_label = Text(
            "Proportion of heads", font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        y_label.rotate(PI / 2)
        y_label.next_to(axes, LEFT, buff=0.2)

        # Animate
        self.add(axes, true_line, true_label, x_label, y_label)

        # Draw curve progressively (in segments for visual effect)
        self.add_subcaption(
            "Notice how the proportion wobbles wildly at first, "
            "then steadily settles toward one half.",
            duration=10,
        )
        self.play(Create(sample_curve), run_time=8, rate_func=linear)

        # Highlight key checkpoints
        for n_check in [10, 50, 200]:
            dot = Dot(axes.c2p(n_check, running_prop[n_check - 1]),
                      color=ACCENT, radius=0.08)
            lbl = Text(
                f"n={n_check}: {running_prop[n_check - 1]:.2f}",
                font_size=SMALL_SIZE, color=ACCENT, font=MONO,
            )
            lbl.next_to(dot, UP, buff=0.15)
            self.play(FadeIn(dot, scale=0.5), FadeIn(lbl), run_time=FAST)
            self.wait(0.3)
            if n_check == 200:
                self.wait(1.5)
            else:
                self.play(FadeOut(dot), FadeOut(lbl), run_time=FAST)

        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Weak Law of Large Numbers
    # ------------------------------------------------------------------
    def scene4_weak_law(self):
        self.add_subcaption(
            "The Weak Law of Large Numbers says that for any positive epsilon, "
            "the probability that the sample mean deviates from mu by more than "
            "epsilon goes to zero as n grows.",
            duration=12,
        )

        self.ly.section_divider(4, "Weak Law of Large Numbers")

        # Theorem statement
        theorem_title = Text(
            "Theorem (Weak LLN)", font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.play(Write(theorem_title), run_time=NORMAL)
        self.wait(0.5)

        theorem = MathTex(
            r"\text{For any } \varepsilon > 0:",
            font_size=BODY_SIZE,
        )
        self.play(Write(theorem), run_time=NORMAL)
        self.wait(0.5)

        main_formula = MathTex(
            r"\lim_{n \to \infty}", r"P\!\left(\left|", r"\bar{X}_n",
            r"- \mu\right|", r"> \varepsilon\right)", r"= 0",
            font_size=HEADING_SIZE,
        )
        main_formula.set_color_by_tex(r"\bar{X}_n", PRIMARY)
        main_formula.set_color_by_tex(r"\mu", ACCENT)
        formula_box = self.ly.formula_box(main_formula)
        self.play(Write(main_formula), run_time=SLOW)
        self.wait(1.5)

        self.play(
            FadeOut(theorem_title), FadeOut(theorem), FadeOut(formula_box),
            run_time=FAST,
        )

        # Proof sketch via Chebyshev
        proof_title = self.ly.title("Proof Sketch: Chebyshev's Inequality")

        cheby_items = [
            MathTex(
                r"P(|\bar{X}_n - \mu| \geq \varepsilon)",
                r"\leq",
                r"\frac{\text{Var}(\bar{X}_n)}{\varepsilon^2}",
                font_size=BODY_SIZE,
            ).set_color_by_tex(r"\leq", ACCENT),
            MathTex(
                r"=", r"\frac{\sigma^2}{n \varepsilon^2}",
                font_size=BODY_SIZE,
            ).set_color_by_tex(r"\sigma^2", PRIMARY),
            Text(
                r"As $n \to \infty$, this bound $\to 0$",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(cheby_items, start_from=proof_title)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Strong Law of Large Numbers
    # ------------------------------------------------------------------
    def scene5_strong_law(self):
        self.add_subcaption(
            "The Strong Law goes further: the sample mean doesn't just get "
            "probably close — it converges to mu with probability one.",
            duration=9,
        )

        self.ly.section_divider(5, "Strong Law of Large Numbers")

        # Strong LLN statement
        strong_title = Text(
            "Theorem (Strong LLN)", font_size=HEADING_SIZE,
            color=SECONDARY, font=SANS,
        )
        self.play(Write(strong_title), run_time=NORMAL)
        self.wait(0.5)

        strong_formula = MathTex(
            r"P\!\left(\lim_{n \to \infty}", r"\bar{X}_n",
            r"= \mu\right)", r"= 1",
            font_size=HEADING_SIZE,
        )
        strong_formula.set_color_by_tex(r"\bar{X}_n", PRIMARY)
        strong_formula.set_color_by_tex(r"= 1", SECONDARY)
        self.play(Write(strong_formula), run_time=SLOW)
        self.wait(1.5)

        self.play(FadeOut(strong_title), FadeOut(strong_formula), run_time=FAST)

        # Comparison
        comp_title = self.ly.title("Weak vs Strong")

        weak_label = Text(
            "Weak LLN", font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        weak_desc = Text(
            '"Probably close" to \u03bc',
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        weak_formula = MathTex(
            r"P(|\bar{X}_n - \mu| > \varepsilon) \to 0",
            font_size=BODY_SIZE,
        ).set_color(PRIMARY)

        strong_label = Text(
            "Strong LLN", font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        strong_desc = Text(
            '"Almost surely" converges to \u03bc',
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        strong_formula = MathTex(
            r"P(\lim \bar{X}_n = \mu) = 1",
            font_size=BODY_SIZE,
        ).set_color(SECONDARY)

        # Build two columns manually with layout engine
        weak_col = VGroup(weak_label, weak_desc, weak_formula).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT,
        )
        strong_col = VGroup(strong_label, strong_desc, strong_formula).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT,
        )

        self.ly.two_columns(
            [weak_col], [strong_col], start_from=comp_title,
        )

        # Arrow showing implication
        arrow_note = Text(
            "Strong implies Weak (not vice versa)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(arrow_note, DOWN, comp_title)

        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Real-World Applications
    # ------------------------------------------------------------------
    def scene6_applications(self):
        self.add_subcaption(
            "The Law of Large Numbers explains why insurance works, "
            "why polls need large samples, and why Monte Carlo simulations converge.",
            duration=10,
        )

        title = self.ly.title("Applications")

        apps = [
            Text(
                "Insurance: with millions of policyholders, "
                "claims average out to expected losses",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Polling: larger samples yield smaller margins of error",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Monte Carlo: computer simulations approximate "
                "hard integrals via random sampling",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Quality Control: defect rates stabilize over "
                "large production runs",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(apps, start_from=title)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Summary and Connection to CLT
    # ------------------------------------------------------------------
    def scene7_summary(self):
        self.add_subcaption(
            "The Law of Large Numbers tells you where the sample mean converges. "
            "The Central Limit Theorem, coming up next, tells you how it fluctuates "
            "along the way.",
            duration=12,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text(
                "Sample mean of i.i.d. variables converges to the "
                "true expected value",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Weak LLN: convergence in probability",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Strong LLN: almost sure convergence",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Sample size is everything in statistics",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title)

        self.wait(1)
        self.ly.clear()

        # Connection to next video
        self.add_subcaption(
            "In the next video, we explore the Central Limit Theorem, "
            "which reveals the beautiful bell curve shape of sample means.",
            duration=9,
        )

        next_title = self.ly.title("Coming Up Next")
        connection = Text(
            "Central Limit Theorem: the beautiful bell curve\n"
            "shape of the sampling distribution",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(connection, DOWN, next_title)
        self.wait(1.5)
        self.ly.clear()

        play_outro(self, "Central Limit Theorem", "Probability & Statistics")
