r"""
Video 241: What is Information?
Information Theory playlist, video 1/10.

Covers: information as surprise, Shannon's information function, properties,
entropy as expected information.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-241-what-is-information.py Video241_WhatIsInformation
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


class Video241_WhatIsInformation(Scene):
    """What is Information? -- Introduction to Information Theory."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_surprise()
        self.scene3_properties()
        self.scene4_example()
        self.scene5_entropy()
        self.scene6_entropy_intuition()
        self.scene7_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "What is information? A single bit of data? A 500-page book? "
            "In 1948, Claude Shannon gave information a precise mathematical definition "
            "that revolutionized communication and computing.",
            duration=14,
        )
        play_intro(self, "What is Information?", "Information Theory")

        title = self.ly.title("The Question")
        items = [
            Text("A coin flip tells you 1 bit", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("A page of text has redundancy", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Shannon made it mathematical", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene2_surprise(self):
        self.add_subcaption(
            "Think about surprise. If someone tells you the sun rose this morning, "
            "you learn nothing. If they tell you they won the lottery, "
            "you learn a lot. Rare events carry more information.",
            duration=14,
        )
        title = self.ly.title("Information as Surprise")
        items = [
            MathTex(r"I(x) = -\log(p(x))", font_size=HEADING_SIZE, color=PRIMARY),
            Text("Sunrise: high probability, low information", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Lottery win: low probability, high information", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3)
        self.ly.clear()

    def scene3_properties(self):
        self.add_subcaption(
            "Shannon's information function has three natural properties. "
            "First, it is always non-negative. Second, rarer events carry more information. "
            "Third, information from independent events adds up. "
            "These three properties force the logarithm.",
            duration=16,
        )
        title = self.ly.title("Three Key Properties")
        items = [
            Text("1. Non-negative: p <= 1, so I(x) >= 0", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. Decreasing: rarer events, more information", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3. Additive for independent events", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3)
        self.ly.clear()

    def scene4_example(self):
        self.add_subcaption(
            "A fair coin has probability one half, so each outcome carries 1 bit. "
            "A fair die gives about 2.58 bits. "
            "A biased coin with probability 0.9 for heads "
            "gives only 0.15 bits for heads but 3.32 bits for tails.",
            duration=14,
        )
        title = self.ly.title("Computing Information")
        items = [
            Text("Fair coin: p = 1/2, I = 1 bit", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Fair die: p = 1/6, I = 2.58 bits", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Biased coin (p=0.9): I(H)=0.15, I(T)=3.32", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3)
        self.ly.clear()

    def scene5_entropy(self):
        self.add_subcaption(
            "What about a random variable with many possible outcomes? "
            "We take the expected value of the information function. "
            "This is called Shannon entropy, H of X. "
            "It measures the average uncertainty per observation.",
            duration=14,
        )
        title = self.ly.title("Shannon Entropy")
        items = [
            MathTex(r"H(X) = \mathbb{E}[I(X)]", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"= -\sum_{i} p_i \log p_i", font_size=HEADING_SIZE, color=PRIMARY),
            Text("Average uncertainty per observation", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3)
        self.ly.clear()

    def scene6_entropy_intuition(self):
        self.add_subcaption(
            "Entropy is highest when all outcomes are equally likely, "
            "and zero when one outcome is certain. "
            "A fair coin has entropy 1 bit. A fair die has 2.58 bits. "
            "A coin that always lands heads has entropy 0.",
            duration=14,
        )
        title = self.ly.title("What Does Entropy Measure?")
        items = [
            Text("Fair coin: H = 1 bit", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Fair die: H = 2.58 bits", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Certain event (p=1): H = 0 bits", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3)
        self.ly.clear()

    def scene7_summary(self):
        self.add_subcaption(
            "Today we defined information as surprise, quantified it with "
            "the negative log, and averaged it to get Shannon entropy. "
            "In the next video, we will see how entropy leads to "
            "data compression, and why it sets a fundamental limit.",
            duration=14,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Information = -log(p(x))", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Entropy = expected information", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Entropy bounds compression", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        play_outro(self, next_video="Entropy and Data Compression", next_playlist="Information Theory")
