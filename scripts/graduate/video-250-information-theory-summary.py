r"""
Video 250: Information Theory Summary
Information Theory playlist, video 10/10.

Covers: recap of entire playlist, connections between concepts,
the big picture of information theory.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-250-information-theory-summary.py Video250_InfoTheorySummary
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


class Video250_InfoTheorySummary(Scene):
    """Information Theory Summary."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_foundations()
        self.scene3_compression()
        self.scene4_channels()
        self.scene5_statistics()
        self.scene6_physics()
        self.scene7_big_picture()
        self.scene8_outro()

    def scene1_hook(self):
        self.add_subcaption(
            "We started with a simple question: what is information? "
            "From that question, we built an entire theory. "
            "This video recaps the Information Theory playlist "
            "and shows how every piece connects.",
            duration=14,
        )
        play_intro(self, "Information Theory Summary", "Information Theory")

        title = self.ly.title("The Journey")
        items = [
            Text("From bits to black holes", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("One question, one theory", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("10 videos, unified framework", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene2_foundations(self):
        self.ly.section_divider(1, "Part I: Foundations")

        self.add_subcaption(
            "The foundation: information as surprise, measured by negative log. "
            "Entropy averages this to measure uncertainty. "
            "Joint entropy and conditional entropy extend it to multiple variables. "
            "Mutual information measures what they share.",
            duration=17,
        )
        title = self.ly.title("Part I: Foundations")
        items = [
            Text("I(x) = -log p(x): information", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("H(X) = E[I(X)]: entropy", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("I(X;Y): mutual information", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(9)
        self.ly.clear()

    def scene3_compression(self):
        self.ly.section_divider(2, "Part II: Compression")

        self.add_subcaption(
            "Source coding: entropy is the limit of lossless compression. "
            "Huffman codes approach this limit. "
            "Rate-distortion theory extends it to lossy compression. "
            "Every codec, from JPEG to HEVC, is guided by these ideas.",
            duration=16,
        )
        title = self.ly.title("Part II: Compression")
        items = [
            Text("H(X): lossless limit", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Huffman: near-optimal codes", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("R(D): lossy compression limit", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(8)
        self.ly.clear()

    def scene4_channels(self):
        self.ly.section_divider(3, "Part III: Channels")

        self.add_subcaption(
            "Channel capacity C equals maximum mutual information. "
            "Below C, reliable communication is possible. "
            "Above C, it is impossible. "
            "Error-correcting codes make this practical.",
            duration=14,
        )
        title = self.ly.title("Part III: Channels")
        items = [
            MathTex(r"C = \max_{p(x)} I(X;Y)", font_size=HEADING_SIZE, color=PRIMARY),
            Text("Noisy-channel coding theorem", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Error-correcting codes in practice", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(6)
        self.ly.clear()

    def scene5_statistics(self):
        self.ly.section_divider(4, "Part IV: Statistics and ML")

        self.add_subcaption(
            "KL divergence measures distribution differences. "
            "It is the foundation of cross-entropy loss in machine learning. "
            "The maximum entropy principle gives a principled way "
            "to choose distributions based on constraints.",
            duration=15,
        )
        title = self.ly.title("Part IV: Statistics and ML")
        items = [
            Text("D(P|Q): KL divergence", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Basis of cross-entropy loss", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Max entropy: principled distributions", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(7)
        self.ly.clear()

    def scene6_physics(self):
        self.ly.section_divider(5, "Part V: Physics")

        self.add_subcaption(
            "Boltzmann entropy and Shannon entropy share the same formula. "
            "Landauer's principle links information to energy. "
            "Black hole entropy shows that physics is fundamentally about information. "
            "It from bit, as John Wheeler said.",
            duration=16,
        )
        title = self.ly.title("Part V: Physics")
        items = [
            Text("Boltzmann = Shannon (same idea)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Landauer: erasure costs energy", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Black holes and holography", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(11)
        self.ly.clear()

    def scene7_big_picture(self):
        self.add_subcaption(
            "Information theory is a unifying framework. "
            "It connects communication, computation, statistics, and physics. "
            "Every concept builds on entropy. "
            "Shannon's 1948 paper may be the most important work of the 20th century.",
            duration=17,
        )
        title = self.ly.title("The Big Picture")
        items = [
            Text("Everything builds on entropy", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Unifies communication, stats, physics", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Shannon's 1948: a century-defining work", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(12)
        self.ly.clear()

    def scene8_outro(self):
        self.add_subcaption(
            "Thank you for watching the Information Theory playlist. "
            "From a simple question about surprise, we traveled through "
            "compression, channels, physics, and beyond. "
            "Stay curious, and keep asking: what is information?",
            duration=15,
        )
        title = self.ly.title("Thank You")
        items = [
            Text("10 videos, one unified theory", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("From surprise to black holes", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Stay curious", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)

        play_outro(self, next_video="", next_playlist="Information Theory")
