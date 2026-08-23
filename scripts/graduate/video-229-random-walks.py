"""
Video 229: Random Walks
Stochastic Processes playlist, video 1/12.

Covers: 1D simple random walk definition, visual simulation,
expected displacement and variance, Polya's recurrence theorem,
2D random walk intuition, and gambler's ruin.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background,
section dividers, content budgets, proper narration timing.

Render:  manim -ql scripts/graduate/video-229-random-walks.py Video229_RandomWalks
"""

from manim import *
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video229_RandomWalks(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_visual_1d()
        self.scene4_expected_value()
        self.scene5_variance()
        self.scene6_recurrence()
        self.scene7_2d_walk()
        self.scene8_gamblers_ruin()
        self.scene9_summary()

    # -- Scene 1: Hook ------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Imagine flipping a coin and taking a step right for heads, "
            "left for tails. Where do you end up after a hundred flips?",
            duration=8,
        )
        play_intro(self, "Random Walks", "Stochastic Processes")

        title = self.ly.title("The Simplest Stochastic Process")
        items = [
            Text("A random walk is a path built from random steps",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Each step is determined by chance, not by design",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Models stock prices, diffusion, search algorithms",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 2: Formal definition -----------------------------------
    def scene2_definition(self):
        self.add_subcaption(
            "Formally, a simple random walk is a sequence of positions "
            "where each step adds plus one or minus one with equal probability.",
            duration=7,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("Simple Random Walk on Z")
        items = [
            Text("Start at the origin, S sub zero equals zero",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"S_0 = 0", font_size=BODY_SIZE, color=SECONDARY),
            Text("Each step: plus one or minus one, probability one half each",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(NORMAL)

        self.add_subcaption(
            "After n steps, the position is the sum of n independent "
            "random variables, each equally likely to be plus or minus one.",
            duration=7,
        )

        step_formula = MathTex(r"S_n = X_1 + X_2 + \cdots + X_n")
        step_box = self.ly.formula_box(step_formula, color=ACCENT)
        self.ly.safe_place(step_box, DOWN, anchor=items[-1])
        self.wait(NORMAL)

        self.add_subcaption(
            "The step variables X sub i are independent and identically distributed. "
            "This i.i.d. property makes random walks easy to analyze.",
            duration=7,
        )

        iid = Text(
            "Steps are independent and identically distributed (i.i.d.)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(iid, DOWN, anchor=step_box)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 3: Visual 1D walk --------------------------------------
    def scene3_visual_1d(self):
        self.add_subcaption(
            "Let us visualize a one-dimensional random walk. "
            "We start at zero and flip a coin at each step.",
            duration=7,
        )
        title = self.ly.title("Visualizing a 1D Walk")
        self.wait(FAST)

        # Draw number line
        axes = Axes(
            x_range=[-5, 6, 1], y_range=[-0.5, 0.5, 1],
            x_length=10, y_length=0.5,
            axis_config={"color": DIM, "font_size": LABEL_SIZE},
        ).shift(DOWN * 1.5)
        self.play(Create(axes), run_time=FAST)

        self.add_subcaption(
            "Heads means step right, tails means step left. "
            "Watch how the walk wanders without any clear direction.",
            duration=8,
        )

        # Animate a sample walk with seed for reproducibility
        import random
        random.seed(42)
        positions = [0]
        for _ in range(10):
            positions.append(positions[-1] + random.choice([-1, 1]))

        # Starting dot
        dot = Dot(axes.c2p(positions[0], 0), color=PRIMARY, radius=0.08)
        self.play(FadeIn(dot), run_time=FAST)

        for i in range(1, len(positions)):
            new_dot = Dot(axes.c2p(positions[i], 0), color=PRIMARY, radius=0.08)
            step_color = ACCENT if positions[i] > positions[i - 1] else RED
            line = Line(
                axes.c2p(positions[i - 1], 0),
                axes.c2p(positions[i], 0),
                color=step_color, stroke_width=3,
            )
            self.play(Create(line), FadeIn(new_dot), run_time=FAST)

        self.wait(NORMAL)

        self.add_subcaption(
            "Even though the walk has no drift, it can stray "
            "surprisingly far from the origin. Let us quantify this.",
            duration=7,
        )

        self.ly.clear()

    # -- Scene 4: Expected displacement --------------------------------
    def scene4_expected_value(self):
        self.add_subcaption(
            "What is the expected position after n steps? "
            "Since each step has zero mean, the expected position stays at zero.",
            duration=8,
        )
        self.ly.section_divider(2, "Expected Displacement")

        title = self.ly.title("Expected Value of S sub n")
        items = [
            MathTex(
                r"E[X_i] = (+1) \cdot \tfrac{1}{2} + (-1) \cdot \tfrac{1}{2} = 0",
                font_size=BODY_SIZE, color=WHITE,
            ),
            Text("Each step has zero mean",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(NORMAL)

        self.add_subcaption(
            "By linearity of expectation, the expected position after "
            "any number of steps is simply the sum of the individual expectations.",
            duration=8,
        )

        result = MathTex(r"E[S_n] = \sum_{i=1}^{n} E[X_i] = 0",
                         font_size=BODY_SIZE, color=SECONDARY)
        result_box = self.ly.formula_box(result, color=ACCENT)
        self.ly.safe_place(result_box, DOWN, anchor=items[-1])
        self.wait(NORMAL)

        insight = Text(
            "On average, the walk never leaves the origin",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=result_box)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 5: Variance --------------------------------------------
    def scene5_variance(self):
        self.add_subcaption(
            "While the expected position is zero, the walk spreads out. "
            "The variance grows linearly with the number of steps.",
            duration=8,
        )
        title = self.ly.title("Variance Grows Linearly")
        items = [
            MathTex(
                r"\mathrm{Var}(X_i) = E[X_i^2] - (E[X_i])^2 = 1 - 0 = 1",
                font_size=BODY_SIZE, color=WHITE,
            ),
            Text("Steps are independent, so variances add",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(NORMAL)

        self.add_subcaption(
            "Since the steps are independent, the variances add. "
            "The variance of S sub n is exactly n.",
            duration=7,
        )

        result = MathTex(r"\mathrm{Var}(S_n) = n",
                         font_size=BODY_SIZE, color=SECONDARY)
        result_box = self.ly.formula_box(result, color=ACCENT)
        self.ly.safe_place(result_box, DOWN, anchor=items[-1])
        self.wait(NORMAL)

        self.add_subcaption(
            "The standard deviation is the square root of n. "
            "This tells us how far the walk typically strays from the origin.",
            duration=7,
        )

        sd = MathTex(r"\mathrm{SD}(S_n) = \sqrt{n}",
                      font_size=BODY_SIZE, color=PRIMARY)
        self.ly.safe_place(sd, DOWN, anchor=result_box)
        self.wait(NORMAL)
        self.ly.clear()

    # -- Scene 6: Polya's recurrence -----------------------------------
    def scene6_recurrence(self):
        self.add_subcaption(
            "One of the most surprising results about random walks is Polya's "
            "recurrence theorem, proved in 1921.",
            duration=7,
        )
        self.ly.section_divider(3, "Polya's Recurrence Theorem")

        title = self.ly.title("Will the Walk Return Home?")
        items = [
            Text("A walk is recurrent if it returns to the origin",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("with probability one, and infinitely often",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("In 1D and 2D: the walk is recurrent",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("In 3D and higher: the walk is transient",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(NORMAL)

        self.add_subcaption(
            "In three dimensions and above, there is a positive probability "
            "that the walk wanders off forever, never returning to where it started.",
            duration=8,
        )

        prob_line1 = MathTex(r"P(\mathrm{return}) = 1", r"\quad" ,r"d = 1, 2",
                             font_size=BODY_SIZE, color=SECONDARY)
        prob_line2 = MathTex(r"P(\mathrm{return}) < 1", r"\quad" ,r"d \geq 3",
                             font_size=BODY_SIZE, color=RED)
        prob_group = VGroup(prob_line1, prob_line2).arrange(DOWN, buff=0.3)
        prob_box = SurroundingRectangle(prob_group, color=ACCENT, buff=0.25,
                                        stroke_width=2, corner_radius=0.1)
        prob_box_group = VGroup(prob_group, prob_box)
        self.ly.safe_place(prob_box_group, DOWN, anchor=items[-1])
        self.play(FadeIn(prob_box_group), run_time=NORMAL)
        self.wait(SLOW)
        self.ly.clear()

    # -- Scene 7: 2D walk intuition -----------------------------------
    def scene7_2d_walk(self):
        self.add_subcaption(
            "In two dimensions, the walker moves to one of four neighbors "
            "with equal probability. Surprisingly, it still returns home.",
            duration=8,
        )
        self.ly.section_divider(4, "The 2D Random Walk")

        title = self.ly.title("Why Does Dimension Matter?")
        items = [
            Text("2D walk: four directions, each with probability one quarter",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Return probability is still one, but returns are rare",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Expected time to return is infinite in 2D",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(NORMAL)

        self.add_subcaption(
            "In three dimensions, there are too many directions to escape into. "
            "The walk gets lost in space with positive probability.",
            duration=8,
        )

        insight = Text(
            "Higher dimensions give the walk more room to escape",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=items[-1])
        self.wait(SLOW)
        self.ly.clear()

    # -- Scene 8: Gambler's ruin --------------------------------------
    def scene8_gamblers_ruin(self):
        self.add_subcaption(
            "A classic application is the gambler's ruin problem. "
            "A gambler with k dollars plays against a casino with N minus k.",
            duration=8,
        )
        self.ly.section_divider(5, "Gambler's Ruin")

        title = self.ly.title("Gambler's Ruin Problem")
        items = [
            Text("Gambler has k dollars, opponent has N minus k",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Each round: win or lose one dollar, equal chance",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Game ends when one player is bankrupt",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(NORMAL)

        self.add_subcaption(
            "The probability of ruin is one minus k over N. "
            "A poorer gambler facing a richer opponent is almost certain to go broke.",
            duration=8,
        )

        ruin = MathTex(r"P(\mathrm{ruin}) = 1 - \frac{k}{N}",
                       font_size=BODY_SIZE, color=RED)
        ruin_box = self.ly.formula_box(ruin, color=RED)
        self.ly.safe_place(ruin_box, DOWN, anchor=items[-1])
        self.wait(NORMAL)

        self.add_subcaption(
            "As N grows large with fixed k, the ruin probability approaches one. "
            "This is why casinos always win in the long run.",
            duration=8,
        )

        corollary = Text(
            "As N goes to infinity, ruin is certain: "
            "a fair game against an infinitely wealthy opponent is fatal",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(corollary, DOWN, anchor=ruin_box)
        self.wait(SLOW)
        self.ly.clear()

    # -- Scene 9: Summary ---------------------------------------------
    def scene9_summary(self):
        self.add_subcaption(
            "To summarize: random walks are sums of independent steps. "
            "The expected position stays at zero, but the variance grows linearly. "
            "Walks are recurrent in one and two dimensions, transient in higher ones. "
            "Next time, we will generalize to Markov chains.",
            duration=15,
        )
        title = self.ly.title("Summary")
        items = [
            Text("Random walk: sum of i.i.d. steps",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"E[S_n] = 0, \quad \mathrm{Var}(S_n) = n",
                    font_size=BODY_SIZE, color=SECONDARY),
            Text("1D and 2D walks are recurrent (return probability one)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("3D and higher walks are transient",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(NORMAL)
        play_outro(self, "Markov Chains", "Stochastic Processes")
        self.ly.clear()
