r"""
Video 247: Relative Entropy and KL Divergence
Information Theory playlist, video 7/10.

Covers: KL divergence, properties, relation to mutual information,
applications in statistics and machine learning.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-247-kl-divergence.py Video247_KLDivergence
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


class Video247_KLDivergence(Scene):
    """KL Divergence."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_properties()
        self.scene4_relation_to_mi()
        self.scene5_applications()
        self.scene6_example()
        self.scene7_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "How do we measure the difference between two probability distributions? "
            "The Kullback-Leibler divergence is the answer. "
            "It measures how much information is lost when we use one distribution to approximate another.",
            duration=16,
        )
        play_intro(self, "KL Divergence", "Information Theory")

        title = self.ly.title("Measuring Distribution Differences")
        items = [
            Text("How different are two distributions?", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("KL divergence quantifies this", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Core tool in ML and statistics", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene2_definition(self):
        self.add_subcaption(
            "The KL divergence from distribution Q to P is the expected value "
            "of log P over Q, using P's probabilities. "
            "It measures the inefficiency of assuming Q when the truth is P.",
            duration=14,
        )
        title = self.ly.title("Definition")
        items = [
            MathTex(r"D(P \|Q) = \sum_x P(x) \log\frac{P(x)}{Q(x)}", font_size=HEADING_SIZE, color=PRIMARY),
            Text("Expected log-ratio of P to Q", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Not symmetric: D(P|Q) != D(Q|P)", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene3_properties(self):
        self.add_subcaption(
            "KL divergence is always non-negative, by Jensen's inequality. "
            "It equals zero if and only if P equals Q. "
            "But it is not a true distance because it is not symmetric "
            "and does not satisfy the triangle inequality.",
            duration=16,
        )
        title = self.ly.title("Properties")
        items = [
            Text("D(P|Q) >= 0 (Gibbs inequality)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Equals 0 iff P = Q", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("NOT a true distance (not symmetric)", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene4_relation_to_mi(self):
        self.add_subcaption(
            "Mutual information is a special case of KL divergence. "
            "It equals the KL divergence between the joint distribution "
            "and the product of the marginals. "
            "This connects everything we have learned.",
            duration=16,
        )
        title = self.ly.title("Connection to Mutual Information")
        items = [
            MathTex(r"I(X;Y) = D(P_{XY} \| P_X \times P_Y)", font_size=HEADING_SIZE, color=PRIMARY),
            Text("Joint vs product of marginals", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Unifies the framework", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene5_applications(self):
        self.add_subcaption(
            "KL divergence appears everywhere. In machine learning, "
            "it is the basis of variational inference and the cross-entropy loss. "
            "In statistics, it justifies maximum likelihood estimation. "
            "In physics, it connects to free energy.",
            duration=16,
        )
        title = self.ly.title("Applications")
        items = [
            Text("ML: cross-entropy loss, variational inference", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Statistics: maximum likelihood", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Physics: free energy connection", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene6_example(self):
        self.add_subcaption(
            "Consider a fair coin P and a biased coin Q with p = 0.9. "
            "The KL divergence is small, about 0.13 bits, because the "
            "distributions are similar. But P = (0.5, 0.5) vs Q = (0.99, 0.01) "
            "gives KL about 1.77 bits, a much bigger difference.",
            duration=16,
        )
        title = self.ly.title("Example: Fair vs Biased Coin")
        items = [
            Text("P=(0.5,0.5) vs Q=(0.9,0.1): D = 0.13 bits", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("P=(0.5,0.5) vs Q=(0.99,0.01): D = 1.77 bits", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("More different distributions = higher KL", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene7_summary(self):
        self.add_subcaption(
            "KL divergence measures how one distribution differs from another. "
            "It is non-negative, zero only for identical distributions. "
            "Mutual information is a special case. "
            "Next, we explore the principle of maximum entropy.",
            duration=14,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("D(P|Q): measures distribution difference", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Non-negative, asymmetric", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Foundation of ML loss functions", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        play_outro(self, next_video="Maximum Entropy Principle", next_playlist="Information Theory")
