r"""
Video 246: Rate-Distortion Theory
Information Theory playlist, video 6/10.

Covers: lossy compression, distortion measures, rate-distortion function,
the tradeoff between rate and quality.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-246-rate-distortion.py Video246_RateDistortion
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


class Video246_RateDistortion(Scene):
    """Rate-Distortion Theory."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_lossy_compression()
        self.scene3_distortion_measures()
        self.scene4_rate_distortion_function()
        self.scene5_tradeoff()
        self.scene6_applications()
        self.scene7_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Not all compression can be lossless. Images, audio, and video "
            "tolerate some quality loss. Rate-distortion theory asks: "
            "for a given quality level, what is the minimum data rate?",
            duration=14,
        )
        play_intro(self, "Rate-Distortion Theory", "Information Theory")

        title = self.ly.title("Beyond Lossless")
        items = [
            Text("Images and audio tolerate quality loss", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("For a given quality, what is the minimum rate?", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("This is the rate-distortion problem", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene2_lossy_compression(self):
        self.add_subcaption(
            "JPEG, MP3, and H.264 are all lossy compressors. "
            "They throw away information you cannot perceive. "
            "The question is: how much can we throw away "
            "while keeping quality acceptable?",
            duration=14,
        )
        title = self.ly.title("Lossy Compression")
        items = [
            Text("JPEG, MP3, H.264 are lossy", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Throw away imperceptible information", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("How much can we discard?", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene3_distortion_measures(self):
        self.add_subcaption(
            "We need a way to measure quality loss. "
            "For scalars, mean squared error is common. "
            "For binary data, the Hamming distortion counts bit errors. "
            "The choice of distortion measure shapes the entire problem.",
            duration=16,
        )
        title = self.ly.title("Distortion Measures")
        items = [
            Text("Mean squared error for real values", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Hamming distortion for binary data", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Choice shapes the entire problem", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene4_rate_distortion_function(self):
        self.add_subcaption(
            "The rate-distortion function R of D gives the minimum rate "
            "needed to achieve average distortion at most D. "
            "It is the lossy analog of Shannon's source coding theorem. "
            "Below R of D, achieving distortion D is impossible.",
            duration=16,
        )
        title = self.ly.title("The Rate-Distortion Function")
        items = [
            MathTex(r"R(D) = \\min_{q(\hat{x}|x)} I(X; \\hat{X})", font_size=HEADING_SIZE, color=PRIMARY),
            Text("Minimum rate for distortion D", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Below R(D): distortion D is impossible", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene5_tradeoff(self):
        self.add_subcaption(
            "The rate-distortion curve is always decreasing. "
            "Higher rate means lower distortion, and vice versa. "
            "At zero distortion, R of zero equals the entropy H of X, "
            "recovering the lossless case.",
            duration=16,
        )
        title = self.ly.title("The Tradeoff")
        items = [
            Text("Higher rate, lower distortion", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("D = 0: R(0) = H(X) (lossless limit)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("D = max: R(D_max) = 0 (send nothing)", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene6_applications(self):
        self.add_subcaption(
            "Rate-distortion theory guides every lossy compressor. "
            "JPEG uses the discrete cosine transform and quantization "
            "guided by rate-distortion optimization. "
            "Modern video codecs like HEVC use Lagrangian RD optimization.",
            duration=16,
        )
        title = self.ly.title("Applications")
        items = [
            Text("JPEG: DCT + quantization", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Video codecs: Lagrangian RD optimization", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Guides all modern lossy compressors", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene7_summary(self):
        self.add_subcaption(
            "Rate-distortion theory extends Shannon's framework to lossy compression. "
            "R of D is the fundamental limit. "
            "Every practical codec is guided by this theory. "
            "Next, we explore relative entropy and KL divergence.",
            duration=14,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("R(D) = minimum rate for distortion D", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Recover lossless limit at D = 0", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Guides all practical codecs", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        play_outro(self, next_video="Relative Entropy and KL Divergence", next_playlist="Information Theory")
