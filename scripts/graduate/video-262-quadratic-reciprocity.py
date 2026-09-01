r"""
Video 262: Quadratic Reciprocity -- Number Theory

Statement of quadratic reciprocity, Gauss's lemma, proof sketch,
and computing Legendre symbols using the law.

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


class Video262_QuadraticReciprocity(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_statement()
        self.scene3_intuition()
        self.scene4_computing()
        self.scene5_worked_example()
        self.scene6_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Gauss called quadratic reciprocity the golden theorem. "
            "It lets us flip the Legendre symbol, turning hard "
            "computations into easy ones. For example, is seven a "
            "square mod eleven? Reciprocity turns this into: is eleven "
            "a square mod seven? Much easier to check.",
            duration=32,
        )
        play_intro(self, "Quadratic Reciprocity", "Number Theory")
        title = self.ly.title("The Golden Theorem")
        items = [
            Text("(7/11) = ?  Hard to compute directly",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Reciprocity: (7/11) = -(11/7) = -(4/7) = -1",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene2_statement(self):
        self.add_subcaption(
            "For odd primes p and q, the Legendre symbols satisfy: "
            "p over q times q over p equals minus one to the power "
            "p minus one times q minus one over four. This means they "
            "agree unless both are three mod four, in which case "
            "they disagree.",
            duration=32,
        )
        self.ly.section_divider(1, "The Law")
        title = self.ly.title("Quadratic Reciprocity")
        law = MathTex(
            r"\left(\frac{p}{q}\right)\!\left(\frac{q}{p}\right)"
            r" = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(law, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(law), run_time=NORMAL)
        self.wait(FAST)
        items = [
            Text("Both p,q = 1 (mod 4): symbols AGREE",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Both p,q = 3 (mod 4): symbols DISAGREE",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    def scene3_intuition(self):
        self.add_subcaption(
            "Why does this work? Gauss's lemma counts how many of the "
            "numbers q, two q, three q, up to p minus one over two times q, "
            "when reduced mod p, end up greater than p over two. This "
            "count determines the sign. The full proof is beautiful but "
            "technical, so we focus on using the law.",
            duration=36,
        )
        self.ly.section_divider(2, "Why It Works")
        title = self.ly.title("Gauss's Lemma (Idea)")
        items = [
            Text("Count: how many of q, 2q, ..., ((p-1)/2)q",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("when reduced mod p, exceed p/2?",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("If count is even: (q/p) = 1",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("If count is odd: (q/p) = -1",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene4_computing(self):
        self.add_subcaption(
            "To compute Legendre symbols, combine reciprocity with "
            "Euler's criterion and the special cases we learned. "
            "Step one: if the top number is even, factor out twos. "
            "Step two: use the law of quadratic reciprocity to flip. "
            "Step three: reduce the top modulo the bottom. Repeat.",
            duration=34,
        )
        self.ly.section_divider(3, "Algorithm")
        title = self.ly.title("Computing Legendre Symbols")
        items = [
            Text("1. Factor out (2/p) using: (2/p)=(-1)^((p^2-1)/8)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Use reciprocity to flip (a/p) to (p/a)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Reduce top mod bottom, repeat",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene5_worked_example(self):
        self.add_subcaption(
            "Let's compute the Legendre symbol of thirteen over "
            "thirty seven. Both are one mod four, so reciprocity gives "
            "thirteen over thirty seven equals thirty seven mod "
            "thirteen over thirteen. Thirty seven mod thirteen is "
            "eleven. So we need eleven over thirteen. Both are three mod "
            "four, so there is a sign flip. Thirteen mod eleven is two. "
            "Two over eleven equals minus one, since eleven is three mod "
            "eight. Putting it together: minus one times minus one "
            "times minus one equals minus one.",
            duration=56,
        )
        self.ly.section_divider(4, "Worked Example")
        title = self.ly.title("Compute (13/37)")
        items = [
            Text("(13/37) = (37/13)  [both 1 mod 4]",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("= (11/13)  [37 mod 13 = 11]",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("= -(13/11)  [both 3 mod 4, flip sign]",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("= -(2/11)  [13 mod 11 = 2]",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()
        title2 = self.ly.title("Finishing Up")
        items2 = [
            Text("(2/11) = (-1)^((121-1)/8) = (-1)^15 = -1",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("So (13/37) = -(-1) = -1  -> QNR",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.ly.clear()

    def scene6_summary(self):
        self.add_subcaption(
            "Quadratic reciprocity is one of the deepest results in "
            "elementary number theory. It gives an efficient algorithm "
            "for computing Legendre symbols, analogous to the Euclidean "
            "algorithm for greatest common divisors. Next time we will "
            "explore which numbers can be written as sums of two squares.",
            duration=30,
        )
        self.ly.section_divider(5, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("1. (p/q)(q/p) = (-1)^((p-1)(q-1)/4)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Flip + reduce, like the Euclidean algorithm",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. (2/p) = (-1)^((p^2-1)/8)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()
        play_outro(self, "Quadratic Reciprocity", "Number Theory")
