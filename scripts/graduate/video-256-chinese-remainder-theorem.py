r"""
Video 256: Chinese Remainder Theorem -- Number Theory

Statement, constructive algorithm, Sun Tzu's problem,
applications to RSA and secret sharing.

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


class Video256_ChineseRemainderTheorem(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_statement()
        self.scene3_algorithm()
        self.scene4_applications()
        self.scene5_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "In the third century, the Chinese mathematician Sun Tzu posed "
            "a puzzle. A number leaves remainder two when divided by three, "
            "remainder three when divided by five, and remainder two when "
            "divided by seven. What is the number? "
            "This is the oldest known problem solved by the Chinese Remainder Theorem.",
            duration=20,
        )
        play_intro(self, "Chinese Remainder Theorem", "Number Theory")

        title = self.ly.title("An Ancient Puzzle")
        items = [
            Text("Counted in 3s: remainder 2",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Counted in 5s: remainder 3",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Counted in 7s: remainder 2",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene2_statement(self):
        self.add_subcaption(
            "The Chinese Remainder Theorem says that if the moduli "
            "are pairwise coprime, then the system of congruences "
            "has a unique solution modulo the product of all moduli. "
            "This is both an existence and uniqueness result.",
            duration=15,
        )
        self.ly.section_divider(1, "The Theorem")
        title = self.ly.title("Statement")

        items = [
            MathTex(r"x \equiv a_i \pmod{n_i}, \quad i = 1, \ldots, k",
                    font_size=BODY_SIZE, color=PRIMARY),
            Text("If gcd(n_i, n_j) = 1 for all i != j",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"\Rightarrow \exists ! \; x \pmod{N}, \; N = n_1 \cdots n_k",
                    font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene3_algorithm(self):
        self.add_subcaption(
            "Here is the constructive algorithm. Let N be the product "
            "of all moduli. For each i, compute N_i equals N over n_i, "
            "then find the modular inverse m_i of N_i modulo n_i. "
            "The solution is the sum of a_i times m_i times N_i, modulo N.",
            duration=18,
        )
        self.ly.section_divider(2, "Constructing the Solution")
        title = self.ly.title("The Algorithm")

        items = [
            MathTex(r"N = n_1 \cdot n_2 \cdots n_k",
                    font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"N_i = N / n_i, \quad m_i = N_i^{-1} \pmod{n_i}",
                    font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"x = \sum_{i=1}^{k} a_i \, m_i \, N_i \pmod{N}",
                    font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        title2 = self.ly.title("Sun Tzu Example")
        ex_items = [
            Text("n_1=3, n_2=5, n_3=7,  so N = 105",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("N_1=35,  N_2=21,  N_3=15",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("m_1=2 (35*2=70=1 mod 3),  m_2=1,  m_3=1",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            MathTex(r"x = 2(2)(35) + 3(1)(21) + 2(1)(15) = 233 \equiv 23 \pmod{105}",
                    font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(ex_items, start_from=title2)
        self.ly.clear()

    def scene4_applications(self):
        self.add_subcaption(
            "The Chinese Remainder Theorem has deep applications in "
            "cryptography. RSA decryption uses it to reconstruct the "
            "message from smaller moduli. It is also used in secret "
            "sharing schemes and in speeding up modular arithmetic.",
            duration=15,
        )
        self.ly.section_divider(3, "Applications")
        title = self.ly.title("Why This Matters")

        items = [
            Text("RSA: reconstruct plaintext from smaller moduli",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Secret sharing: split a secret into shares",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Speed up: work mod small primes, then combine",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene5_summary(self):
        self.add_subcaption(
            "Today we learned the Chinese Remainder Theorem. "
            "Given pairwise coprime moduli, a system of congruences "
            "has a unique solution. The constructive algorithm uses "
            "modular inverses. And this theorem is fundamental to "
            "modern cryptography. Next, Fermat's little theorem in depth.",
            duration=20,
        )
        self.ly.section_divider(4, "Summary")
        title = self.ly.title("Key Takeaways")

        items = [
            Text("1. CRT: unique solution for coprime moduli",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Constructive: modular inverses + weighted sum",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Foundation for RSA and secret sharing",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        play_outro(self, "Fermat's Little Theorem", "Number Theory")
