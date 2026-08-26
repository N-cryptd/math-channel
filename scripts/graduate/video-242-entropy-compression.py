r"""
Video 242: Entropy and Data Compression
Information Theory playlist, video 2/10.

Covers: source coding, fixed vs variable length codes, Huffman coding,
the source coding theorem, entropy of English.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-242-entropy-compression.py Video242_EntropyCompression
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


class Video242_EntropyCompression(Scene):
    """Entropy and Data Compression."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_motivation()
        self.scene2_source_coding()
        self.scene3_fixed_vs_variable()
        self.scene4_huffman()
        self.scene5_source_coding_theorem()
        self.scene6_english()
        self.scene7_summary()

    def scene1_motivation(self):
        self.add_subcaption(
            "Every time you send a photo, stream a video, or store a file, "
            "compression is happening. The question is: how far can we compress? "
            "Shannon's source coding theorem says the limit is entropy.",
            duration=14,
        )
        play_intro(self, "Entropy and Data Compression", "Information Theory")

        title = self.ly.title("The Compression Problem")
        items = [
            Text("Files are compressed every day", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("How far can we go?", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Entropy is the answer", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene2_source_coding(self):
        self.ly.section_divider(1, "Source Coding")

        self.add_subcaption(
            "Source coding means assigning binary codewords to source symbols. "
            "The goal is to minimize the average codeword length. "
            "If some symbols are more likely, we can give them shorter codewords.",
            duration=14,
        )
        title = self.ly.title("Source Coding")
        items = [
            Text("Assign binary codes to symbols", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Minimize average codeword length", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Frequent symbols get short codes", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene3_fixed_vs_variable(self):
        self.add_subcaption(
            "Consider four symbols with probabilities one half, one quarter, "
            "one eighth, one eighth. A fixed-length code uses 2 bits per symbol. "
            "But variable-length codes give the likely symbol just 1 bit. "
            "The average drops from 2 to 1.75 bits.",
            duration=16,
        )
        title = self.ly.title("Fixed vs Variable Length")
        items = [
            Text("p = (1/2, 1/4, 1/8, 1/8)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Fixed: 2, 2, 2, 2 bits (avg = 2)", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Variable: 1, 2, 3, 3 bits (avg = 1.75)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene4_huffman(self):
        self.ly.section_divider(2, "Huffman Coding")

        self.add_subcaption(
            "Huffman coding is an optimal prefix-free code. "
            "Repeatedly merge the two least probable symbols into a new node. "
            "The resulting tree minimizes expected length. "
            "Huffman is used in JPEG, ZIP, and MP3.",
            duration=14,
        )
        title = self.ly.title("Huffman Coding")
        items = [
            Text("Optimal prefix-free code", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Merge two least probable symbols", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Used in JPEG, ZIP, MP3", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene5_source_coding_theorem(self):
        self.ly.section_divider(3, "Source Coding Theorem")

        self.add_subcaption(
            "Shannon's source coding theorem: the average codeword length "
            "L can never be less than the entropy H. "
            "But we can get arbitrarily close to H from above. "
            "This is why entropy is the limit of compression.",
            duration=14,
        )
        title = self.ly.title("Source Coding Theorem")
        sc_formula = MathTex(r"H(X) \leq L < H(X) + 1", font_size=HEADING_SIZE, color=PRIMARY)
        boxed = self.ly.formula_box(sc_formula, color=PRIMARY)
        self.ly.safe_place(boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(boxed), run_time=NORMAL)
        items = [
            Text("Entropy is the lower bound", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Can approach H arbitrarily closely", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.wait(2)
        self.ly.clear()

    def scene6_english(self):
        self.add_subcaption(
            "The entropy of English text is about 1 to 1.5 bits per letter, "
            "far less than the 5 bits for fixed-length encoding. "
            "This shows English has massive redundancy. "
            "Shannon estimated this through guessing experiments.",
            duration=14,
        )
        title = self.ly.title("Entropy of English")
        items = [
            Text("Fixed-length: 5 bits per letter", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Entropy: about 1.0 - 1.5 bits per letter", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Shannon's guessing experiments", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene7_summary(self):
        self.add_subcaption(
            "Entropy is the fundamental limit of lossless compression. "
            "Huffman coding achieves near-optimal performance. "
            "English text has far less entropy than its alphabet suggests. "
            "Next, we look at two random variables at once.",
            duration=14,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("H(X) is the compression limit", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Huffman coding is near-optimal", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Redundancy = room for compression", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        play_outro(self, next_video="Joint Entropy and Mutual Information", next_playlist="Information Theory")
