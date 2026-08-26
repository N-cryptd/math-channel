r"""
Video 248: Maximum Entropy Principle
Information Theory playlist, video 8/10.

Covers: maximum entropy principle, constraints, examples
(Gaussian, exponential), Jaynes' philosophy.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-248-maximum-entropy.py Video248_MaximumEntropy
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


class Video248_MaximumEntropy(Scene):
    """Maximum Entropy Principle."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_principle()
        self.scene3_mean_constraint()
        self.scene4_gaussian()
        self.scene5_exponential()
        self.scene6_philosophy()
        self.scene7_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Suppose you know only the mean and variance of a distribution. "
            "What distribution should you choose? The maximum entropy principle says: "
            "pick the distribution with the most uncertainty, subject to your constraints.",
            duration=16,
        )
        play_intro(self, "Maximum Entropy Principle", "Information Theory")

        title = self.ly.title("Least Assumption, Most Uncertainty")
        items = [
            Text("You have partial knowledge", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Which distribution to choose?", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Maximize entropy subject to constraints", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene2_principle(self):
        self.ly.section_divider(1, "Jaynes' Principle")

        self.add_subcaption(
            "The maximum entropy principle, due to E.T. Jaynes, states that "
            "among all distributions consistent with our constraints, "
            "we should choose the one with maximum entropy. "
            "This is the least informative distribution: it assumes nothing extra.",
            duration=16,
        )
        title = self.ly.title("Jaynes' Principle")
        items = [
            Text("Maximize H(p) subject to constraints", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Consistent with what you know", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Assumes nothing extra", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene3_mean_constraint(self):
        self.ly.section_divider(2, "No Constraints: Uniform")

        self.add_subcaption(
            "With no constraints, the maximum entropy distribution "
            "is uniform: equal probability for all outcomes. "
            "This makes intuitive sense: if you know nothing, "
            "assume maximum uncertainty.",
            duration=14,
        )
        title = self.ly.title("No Constraints: Uniform")
        items = [
            Text("No constraints: uniform distribution", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Maximum uncertainty when we know nothing", font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"p_i = 1/n", font_size=HEADING_SIZE, color=PRIMARY),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene4_gaussian(self):
        self.ly.section_divider(3, "Mean + Variance: Gaussian")

        self.add_subcaption(
            "If you fix the mean and variance, the maximum entropy distribution "
            "is the Gaussian. This is why the Gaussian appears everywhere: "
            "it is the most unbiased distribution with given first two moments. "
            "The central limit theorem gives another reason, but max entropy is deeper.",
            duration=16,
        )
        title = self.ly.title("Mean + Variance: Gaussian")
        items = [
            Text("Fix mean and variance", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Maximum entropy = Gaussian", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Why Gaussians appear everywhere", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene5_exponential(self):
        self.ly.section_divider(4, "Positive Mean: Exponential")

        self.add_subcaption(
            "If you fix only the mean and require non-negativity, "
            "the maximum entropy distribution is the exponential. "
            "This models waiting times, radioactive decay, and many natural processes. "
            "Different constraints lead to different maximum entropy distributions.",
            duration=16,
        )
        title = self.ly.title("Positive Mean: Exponential")
        items = [
            Text("Fix mean, require non-negativity", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Maximum entropy = Exponential", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Models waiting times and decay", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene6_philosophy(self):
        self.add_subcaption(
            "Jaynes' insight was that probability is not about frequency "
            "but about information. The maximum entropy principle is a "
            "philosophy of inference: use all available information, "
            "but assume nothing else.",
            duration=16,
        )
        title = self.ly.title("Philosophy of Inference")
        items = [
            Text("Probability = information, not frequency", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Use all available information", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Assume nothing else", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene7_summary(self):
        self.add_subcaption(
            "The maximum entropy principle gives a principled way to choose "
            "distributions. Uniform for no constraints, Gaussian for mean and variance, "
            "exponential for positive mean. Next, we connect information theory to physics.",
            duration=14,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Max H(p) subject to constraints", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Uniform -> Gaussian -> Exponential", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Jaynes: probability as information", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        play_outro(self, next_video="Information Theory and Physics", next_playlist="Information Theory")
