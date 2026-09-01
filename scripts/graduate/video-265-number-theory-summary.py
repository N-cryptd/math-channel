r"""
Video 265: Number Theory Summary -- Number Theory

Recap of the entire Number Theory playlist (Videos 251-265).

Follows v2 template quality rules.
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


class Video265_NumberTheorySummary(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_foundations()
        self.scene3_modular()
        self.scene4_structure()
        self.scene5_advanced()
        self.scene6_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Over fifteen videos we have journeyed through the "
            "foundations of number theory. From the Euclidean algorithm "
            "to RSA encryption, from quadratic residues to sums of "
            "squares. Let us recap the key ideas and see how they connect.",
            duration=32,
        )
        play_intro(self, "Number Theory Summary", "Number Theory")
        title = self.ly.title("Fifteen Videos of Number Theory")
        items = [
            Text("Videos 251-265: a complete introduction",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Building from basics to modern cryptography",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene2_foundations(self):
        self.add_subcaption(
            "We started with divisibility and the Euclidean algorithm, "
            "the backbone of computational number theory. The "
            "fundamental theorem of arithmetic tells us every integer "
            "factors uniquely into primes. This uniqueness is the "
            "foundation everything else rests on.",
            duration=32,
        )
        self.ly.section_divider(1, "Foundations")
        title = self.ly.title("Divisibility and Primes")
        items = [
            Text("Euclidean algorithm: efficient gcd computation",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Fundamental theorem: unique prime factorization",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Prime distribution: infinite but irregular",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene3_modular(self):
        self.add_subcaption(
            "Modular arithmetic gave us a new way to work with integers. "
            "The Chinese Remainder Theorem lets us reconstruct numbers "
            "from their residues. Fermat's little theorem and Euler's "
            "theorem provide exponentiation shortcuts. And these theorems "
            "directly power the RSA cryptosystem.",
            duration=38,
        )
        self.ly.section_divider(2, "Modular Arithmetic")
        title = self.ly.title("Working Modulo n")
        items = [
            Text("Chinese Remainder Theorem: reconstruct from pieces",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Fermat and Euler: exponentiation shortcuts",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("RSA: encryption from number theory",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene4_structure(self):
        self.add_subcaption(
            "We studied the multiplicative structure of integers "
            "mod n through Euler's totient function and primitive roots. "
            "Quadratic residues and the Legendre symbol revealed which "
            "numbers are squares modulo a prime. And quadratic reciprocity "
            "gave us an efficient algorithm for computing these symbols.",
            duration=40,
        )
        self.ly.section_divider(3, "Structure")
        title = self.ly.title("Multiplicative Structure")
        items = [
            Text("Euler's totient: counts coprime integers",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Primitive roots: generators of cyclic groups",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Quadratic residues: which numbers are squares",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene5_advanced(self):
        self.add_subcaption(
            "Finally we applied these tools to classical problems. "
            "Sums of two squares connect quadratic residues to geometry. "
            "Diophantine equations seek integer solutions to polynomial "
            "equations. Together these topics form a complete introduction "
            "to elementary number theory.",
            duration=36,
        )
        self.ly.section_divider(4, "Applications")
        title = self.ly.title("Classical Problems")
        items = [
            Text("Sums of squares: Fermat's theorem, Brahmagupta",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Diophantine equations: integer solutions only",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("From Euclid to RSA: a beautiful journey",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene6_summary(self):
        self.add_subcaption(
            "This completes our Number Theory playlist. You now have "
            "the tools to understand divisibility, modular arithmetic, "
            "quadratic residues, and even how your web browser keeps "
            "secrets safe. Thank you for watching.",
            duration=28,
        )
        self.ly.section_divider(5, "Thank You")
        title = self.ly.title("The End of the Journey")
        items = [
            Text("15 videos covering the core of number theory",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("From Euclidean algorithm to RSA encryption",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("You now understand how number theory powers cryptography",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()
        play_outro(self, "Number Theory Summary", "Number Theory")
