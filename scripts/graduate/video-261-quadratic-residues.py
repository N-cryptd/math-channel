r"""
Video 261: Quadratic Residues -- Number Theory

Definition of quadratic residues, Legendre symbol,
Euler's criterion, and key properties.

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


class Video261_QuadraticResidues(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_definition()
        self.scene3_legendre()
        self.scene4_euler_criterion()
        self.scene5_properties()
        self.scene6_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Which numbers are squares modulo a prime? For modulus "
            "seven, the squares of one through six are one, four, two, "
            "two, four, and one. Only three out of six nonzero residues "
            "are squares. These are called quadratic residues.",
            duration=26,
        )
        play_intro(self, "Quadratic Residues", "Number Theory")
        title = self.ly.title("Which Numbers Are Squares?")
        items = [
            Text("Squares mod 7: {1,4,2} out of {1,2,3,4,5,6}",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Exactly half the nonzero residues are squares",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene2_definition(self):
        self.add_subcaption(
            "A quadratic residue modulo p is a number a for which "
            "there exists some x with x squared equals a mod p. If no "
            "such x exists, a is a quadratic nonresidue. For p equal "
            "to seven, the quadratic residues are one, two, and four. "
            "Three, five, and six are nonresidues.",
            duration=32,
        )
        self.ly.section_divider(1, "Definition")
        title = self.ly.title("Quadratic Residues")
        items = [
            Text("QR: a = x^2 (mod p) for some x",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("QNR: no such x exists",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Mod 7: QRs = {1, 2, 4}, QNRs = {3, 5, 6}",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene3_legendre(self):
        self.add_subcaption(
            "The Legendre symbol captures QR versus QNR concisely. "
            "It equals one if a is a residue, minus one if it is a "
            "nonresidue, and zero if p divides a. It is multiplicative: "
            "the Legendre symbol of a b equals the product of the "
            "individual symbols.",
            duration=30,
        )
        self.ly.section_divider(2, "The Legendre Symbol")
        title = self.ly.title("The Legendre Symbol (a/p)")
        items = [
            Text("(a/p) = 1  if a is a QR mod p",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("(a/p) = -1 if a is a QNR mod p",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("(a/p) = 0  if p divides a",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Multiplicative: (ab/p) = (a/p)(b/p)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene4_euler_criterion(self):
        self.add_subcaption(
            "Euler's criterion gives a way to compute the Legendre "
            "symbol using modular exponentiation. The Legendre symbol "
            "of a over p equals a to the power p minus one over two, "
            "taken mod p. The result is one for residues and p minus one "
            "for nonresidues. For example, two over seven equals two "
            "cubed equals eight, which is one mod seven. Confirmed, two "
            "is a quadratic residue.",
            duration=44,
        )
        self.ly.section_divider(3, "Euler's Criterion")
        title = self.ly.title("Computing (a/p) via Exponentiation")
        criterion = MathTex(
            r"\left(\frac{a}{p}\right) \equiv a^{(p-1)/2} \pmod{p}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(criterion, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(criterion), run_time=NORMAL)
        self.wait(FAST)
        items = [
            Text("Result: 1 for QR, p-1 (= -1) for QNR",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("(2/7) = 2^3 = 8 = 1 (mod 7) -> QR",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("(3/7) = 3^3 = 27 = 6 = -1 (mod 7) -> QNR",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    def scene5_properties(self):
        self.add_subcaption(
            "Some useful special cases. The Legendre symbol of one "
            "is always one. The Legendre symbol of minus one depends "
            "on p mod four. It is one if p is one mod four, and minus "
            "one if p is three mod four. Also, a squared is always a "
            "quadratic residue.",
            duration=32,
        )
        self.ly.section_divider(4, "Special Cases")
        title = self.ly.title("Useful Properties")
        items = [
            Text("(1/p) = 1  (1 is always a square)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("(-1/p) = 1 if p = 1 (mod 4), -1 if p = 3 (mod 4)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("(a^2/p) = 1  (squares are always QRs)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene6_summary(self):
        self.add_subcaption(
            "Today we defined quadratic residues and the Legendre "
            "symbol, and learned Euler's criterion for computing it. "
            "This is already powerful, but the real breakthrough comes "
            "next: quadratic reciprocity, which lets us flip the "
            "Legendre symbol and compute (p/q) in terms of (q/p).",
            duration=28,
        )
        self.ly.section_divider(5, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("1. QR: a is a square mod p",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Legendre symbol (a/p): 1, -1, or 0",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Euler's criterion: (a/p) = a^((p-1)/2)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Next: Quadratic Reciprocity!",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()
        play_outro(self, "Quadratic Residues", "Number Theory")
