r"""
Video 245: Error-Correcting Codes
Information Theory playlist, video 5/10.

Covers: repetition codes, Hamming distance, Hamming codes,
error detection vs correction.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-245-error-correcting-codes.py Video245_ErrorCorrectingCodes
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


class Video245_ErrorCorrectingCodes(Scene):
    """Error-Correcting Codes."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_motivation()
        self.scene3_repetition_codes()
        self.scene4_hamming_distance()
        self.scene5_hamming_codes()
        self.scene6_detection_vs_correction()
        self.scene7_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Shannon proved reliable communication is possible below capacity. "
            "But he did not say how. Error-correcting codes are the how. "
            "They add carefully chosen redundancy to detect and fix errors.",
            duration=14,
        )
        play_intro(self, "Error-Correcting Codes", "Information Theory")

        title = self.ly.title("The How of Reliable Communication")
        items = [
            Text("Shannon said it is possible", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Error-correcting codes show how", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Add redundancy to fix errors", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene2_motivation(self):
        self.add_subcaption(
            "Every digital system needs error correction. "
            "QR codes, satellite links, deep space probes, "
            "and your phone all use error-correcting codes. "
            "Without them, a single bit flip could corrupt an entire file.",
            duration=16,
        )
        title = self.ly.title("Why Error Correction?")
        items = [
            Text("QR codes and satellite links", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Deep space communication", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("One bit flip could corrupt everything", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene3_repetition_codes(self):
        self.add_subcaption(
            "The simplest error-correcting code: repeat each bit three times. "
            "Send 000 for 0 and 111 for 1. "
            "If one bit flips, majority vote recovers the original. "
            "But this triples the data rate, which is very expensive.",
            duration=16,
        )
        title = self.ly.title("Repetition Code")
        items = [
            Text("Send each bit 3 times: 000 or 111", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Majority vote corrects 1 error", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Rate = 1/3: very expensive", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene4_hamming_distance(self):
        self.add_subcaption(
            "The Hamming distance between two codewords is the number of "
            "positions where they differ. A code with minimum distance d "
            "can detect up to d minus 1 errors and correct up to "
            "floor of d minus 1 over 2 errors.",
            duration=16,
        )
        title = self.ly.title("Hamming Distance")
        items = [
            Text("Count differing bit positions", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Min distance d: detect d-1 errors", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Correct: floor((d-1)/2) errors", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene5_hamming_codes(self):
        self.add_subcaption(
            "Hamming codes are the first practical error-correcting codes. "
            "They use parity check bits placed at powers of two. "
            "A Hamming 7,4 code encodes 4 data bits into 7 bits "
            "and can correct any single-bit error.",
            duration=16,
        )
        title = self.ly.title("Hamming Codes")
        items = [
            Text("Parity bits at positions 1, 2, 4", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Hamming(7,4): 4 data + 3 check bits", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Corrects any single-bit error", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene6_detection_vs_correction(self):
        self.add_subcaption(
            "Error detection is easier than error correction. "
            "A checksum can detect errors but cannot fix them. "
            "Modern codes like LDPC and Turbo codes approach "
            "Shannon capacity and are used in 5G and Wi-Fi.",
            duration=16,
        )
        title = self.ly.title("Detection vs Correction")
        items = [
            Text("Detection: cheaper, but need retransmit", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Correction: more redundancy needed", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("LDPC and Turbo codes approach capacity", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    def scene7_summary(self):
        self.add_subcaption(
            "Error-correcting codes make Shannon's theorem practical. "
            "Hamming distance determines how many errors a code can fix. "
            "Modern codes approach channel capacity. "
            "Next, we measure the inefficiency of codes with rate-distortion theory.",
            duration=16,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Codes add controlled redundancy", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Hamming distance determines power", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Modern codes approach Shannon capacity", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        play_outro(self, next_video="Rate-Distortion Theory", next_playlist="Information Theory")
