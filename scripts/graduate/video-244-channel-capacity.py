r"""
Video 244: Channel Capacity
Information Theory playlist, video 4/10.

Covers: communication channels, noise, channel capacity,
Shannon's noisy-channel coding theorem.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-244-channel-capacity.py Video244_ChannelCapacity
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


class Video244_ChannelCapacity(Scene):
    """Channel Capacity."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_channel_model()
        self.scene3_mutual_info_role()
        self.scene4_capacity_formula()
        self.scene5_binary_symmetric()
        self.scene6_noisy_coding_theorem()
        self.scene7_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Real communication is never perfect. Wi-Fi drops packets. "
            "Radio has static. Even fiber optic cables have tiny error rates. "
            "Shannon asked: given noise, how fast can we reliably communicate?",
            duration=14,
        )
        play_intro(self, "Channel Capacity", "Information Theory")

        title = self.ly.title("The Noisy Channel Problem")
        items = [
            Text("Real communication has noise", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("How fast can we transmit reliably?", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Shannon found the answer", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene2_channel_model(self):
        self.ly.section_divider(1, "The Channel Model")

        self.add_subcaption(
            "A communication channel takes input X and produces output Y. "
            "Noise corrupts the signal. The channel is described by "
            "the conditional distribution P of Y given X.",
            duration=14,
        )
        title = self.ly.title("The Channel Model")
        items = [
            Text("Input: X (transmitted symbol)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Output: Y (received symbol)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Channel: P(Y | X)", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene3_mutual_info_role(self):
        self.add_subcaption(
            "The mutual information I of X semicolon Y tells us how much "
            "information passes through the channel. We want to maximize this "
            "over all possible input distributions on X.",
            duration=14,
        )
        title = self.ly.title("Maximizing Information Flow")
        items = [
            MathTex(r"I(X;Y) = H(X) - H(X|Y)", font_size=HEADING_SIZE, color=PRIMARY),
            Text("How much info passes through?", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Maximize over input distribution", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene4_capacity_formula(self):
        self.ly.section_divider(2, "Channel Capacity")

        self.add_subcaption(
            "The channel capacity C is the maximum mutual information, "
            "maximized over all input distributions. "
            "It has units of bits per channel use. "
            "This is the fundamental limit of reliable communication.",
            duration=16,
        )
        title = self.ly.title("Channel Capacity")
        cap_formula = MathTex(r"C = \max_{p(x)} I(X;Y)", font_size=HEADING_SIZE, color=PRIMARY)
        boxed = self.ly.formula_box(cap_formula, color=PRIMARY)
        self.ly.safe_place(boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(boxed), run_time=NORMAL)
        items = [
            Text("Units: bits per channel use", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Fundamental limit of communication", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.wait(2)
        self.ly.clear()

    def scene5_binary_symmetric(self):
        self.add_subcaption(
            "For a binary symmetric channel with bit flip probability p, "
            "the capacity is 1 minus H of p. At p equals zero, capacity is 1 bit. "
            "At p equals one half, capacity is zero, because the output is useless.",
            duration=16,
        )
        title = self.ly.title("Binary Symmetric Channel")
        items = [
            MathTex(r"C = 1 - H(p)", font_size=HEADING_SIZE, color=PRIMARY),
            Text("p = 0: perfect channel, C = 1 bit", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("p = 0.5: useless, C = 0 bits", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene6_noisy_coding_theorem(self):
        self.ly.section_divider(3, "Noisy-Channel Coding Theorem")

        self.add_subcaption(
            "Shannon's noisy-channel coding theorem is one of the most "
            "remarkable results in mathematics. It says that if your rate "
            "is below capacity, you can communicate with arbitrarily low error. "
            "Above capacity, reliable communication is impossible.",
            duration=16,
        )
        title = self.ly.title("Noisy-Channel Coding Theorem")
        items = [
            Text("Rate < C: reliable communication possible", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Rate > C: reliable communication impossible", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("One of the greatest results in mathematics", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene7_summary(self):
        self.add_subcaption(
            "Channel capacity is the maximum rate of reliable communication. "
            "The noisy-channel coding theorem separates the possible from the impossible. "
            "Next, we look at how to actually achieve this capacity with error-correcting codes.",
            duration=14,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("C = max I(X;Y) over input distribution", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Below C: reliable, above C: impossible", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Binary symmetric channel: C = 1 - H(p)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        play_outro(self, next_video="Error-Correcting Codes", next_playlist="Information Theory")
