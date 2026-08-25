r"""
Video 243: Joint Entropy and Mutual Information
Information Theory playlist, video 3/10.

Covers: joint entropy, conditional entropy, mutual information,
chain rule, Venn diagram interpretation.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-243-joint-entropy-mutual-information.py Video243_JointEntropyMI
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


class Video243_JointEntropyMI(Scene):
    """Joint Entropy and Mutual Information."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_joint_entropy()
        self.scene3_conditional_entropy()
        self.scene4_mutual_information()
        self.scene5_venn_interpretation()
        self.scene6_chain_rule()
        self.scene7_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "So far we have measured the information in a single random variable. "
            "But real systems have multiple variables that interact. "
            "How much information do they share? How much is unique to each?",
            duration=14,
        )
        play_intro(self, "Joint Entropy and Mutual Information", "Information Theory")

        title = self.ly.title("Beyond One Variable")
        items = [
            Text("Real systems have multiple variables", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("How much do they share?", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("How much is unique?", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene2_joint_entropy(self):
        self.add_subcaption(
            "Joint entropy extends Shannon entropy to pairs of random variables. "
            "It measures the total uncertainty in the pair X, Y taken together. "
            "If X and Y are independent, the joint entropy equals the sum of their individual entropies.",
            duration=16,
        )
        title = self.ly.title("Joint Entropy")
        items = [
            MathTex(r"H(X,Y) = -\sum_{x,y} p(x,y) \log p(x,y)", font_size=HEADING_SIZE, color=PRIMARY),
            Text("Total uncertainty in the pair", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Independent: H(X,Y) = H(X) + H(Y)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene3_conditional_entropy(self):
        self.add_subcaption(
            "Conditional entropy measures the remaining uncertainty in X "
            "after we know Y. It is the average of H of X given Y equals y, "
            "weighted by the probability of each y. "
            "Knowing Y can only reduce uncertainty, never increase it.",
            duration=16,
        )
        title = self.ly.title("Conditional Entropy")
        items = [
            MathTex(r"H(X|Y) = \sum_y p(y)\, H(X|Y{=}y)", font_size=HEADING_SIZE, color=PRIMARY),
            Text("Remaining uncertainty after knowing Y", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("H(X|Y) <= H(X) always", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene4_mutual_information(self):
        self.add_subcaption(
            "Mutual information measures how much knowing one variable "
            "reduces uncertainty about the other. "
            "It is the difference between the entropy of X "
            "and the conditional entropy of X given Y.",
            duration=14,
        )
        title = self.ly.title("Mutual Information")
        items = [
            MathTex(r"I(X;Y) = H(X) - H(X|Y)", font_size=HEADING_SIZE, color=PRIMARY),
            Text("Information shared between X and Y", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("I(X;Y) >= 0, equals 0 iff independent", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene5_venn_interpretation(self):
        self.add_subcaption(
            "Think of a Venn diagram. H of X is the left circle. "
            "H of Y is the right circle. Their overlap is mutual information. "
            "Joint entropy is the total area. "
            "Conditional entropy is the non-overlapping part of one circle.",
            duration=16,
        )
        title = self.ly.title("The Venn Diagram View")
        items = [
            Text("H(X) = left circle", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("H(Y) = right circle", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("I(X;Y) = overlap", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene6_chain_rule(self):
        self.add_subcaption(
            "The chain rule for entropy says that joint entropy equals "
            "the entropy of X plus the conditional entropy of Y given X. "
            "This extends to more variables. "
            "The chain rule is the foundation of data processing analysis.",
            duration=16,
        )
        title = self.ly.title("Chain Rule")
        items = [
            MathTex(r"H(X,Y) = H(X) + H(Y|X)", font_size=HEADING_SIZE, color=PRIMARY),
            Text("Extends to any number of variables", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Foundation of data processing analysis", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene7_summary(self):
        self.add_subcaption(
            "Joint entropy measures total uncertainty. "
            "Conditional entropy measures remaining uncertainty. "
            "Mutual information measures shared information. "
            "Next time, we apply these tools to communication channels.",
            duration=14,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("H(X,Y): total uncertainty", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("H(X|Y): remaining after knowing Y", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("I(X;Y): shared information", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        play_outro(self, next_video="Channel Capacity", next_playlist="Information Theory")
