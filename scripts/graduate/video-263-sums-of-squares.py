r"""
Video 263: Sums of Two Squares -- Number Theory

Which primes are sums of two squares, Fermat's theorem on sums of
two squares, Brahmagupta-Fibonacci identity, full integer classification,
and worked examples.

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


class Video263_SumsOfSquares(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_which_primes()
        self.scene3_brahmagupta()
        self.scene4_descent_idea()
        self.scene5_negative_case()
        self.scene6_full_classification()
        self.scene7_worked_examples()
        self.scene8_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Which numbers can be written as a sum of two squares? "
            "Five equals one squared plus two squared. Thirteen equals "
            "two squared plus three squared. But can seven be written "
            "this way? The answer reveals a deep connection between "
            "addition and prime numbers.",
            duration=34,
        )
        play_intro(self, "Sums of Two Squares", "Number Theory")
        title = self.ly.title("A Simple Question")
        items = [
            Text("5 = 1\u00b2 + 2\u00b2     13 = 2\u00b2 + 3\u00b2",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Can 7 be written as a\u00b2 + b\u00b2 ?",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene2_which_primes(self):
        self.add_subcaption(
            "Let us check small primes. Two equals one plus one, a sum "
            "of squares. Five equals one plus four. Thirteen equals four "
            "plus nine. Seventeen equals one plus sixteen. But three, "
            "seven, eleven, nineteen cannot be expressed this way. "
            "The pattern is: a prime p is a sum of two squares if and "
            "only if p equals two or p is one modulo four.",
            duration=46,
        )
        self.ly.section_divider(1, "Which Primes?")
        title = self.ly.title("Checking Small Primes")
        items = [
            Text("2=1\u00b2+1\u00b2  5=1\u00b2+2\u00b2  13=2\u00b2+3\u00b2",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("17=1\u00b2+4\u00b2  29=2\u00b2+5\u00b2  37=1\u00b2+6\u00b2",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3=NO  7=NO  11=NO  19=NO  23=NO",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        title2 = self.ly.title("Fermat's Theorem")
        theorem = MathTex(
            r"p = a^2 + b^2",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(theorem, DOWN, anchor=title2, buff=0.4)
        self.play(Write(theorem), run_time=NORMAL)
        self.wait(FAST)
        items2 = [
            Text("if and only if  p = 2  or  p = 1 (mod 4)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Connection: -1 is a QR mod p  iff  p = 1 (mod 4)",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=theorem)
        self.ly.clear()

    def scene3_brahmagupta(self):
        self.add_subcaption(
            "The key tool is the Brahmagupta-Fibonacci identity. It says "
            "that the product of two sums of squares is itself a sum of "
            "squares. Specifically, a squared plus b squared times c "
            "squared plus d squared equals the quantity ac minus bd "
            "squared plus the quantity ad plus bc squared. This "
            "identity is why prime factorization matters.",
            duration=46,
        )
        self.ly.section_divider(2, "The Key Identity")
        title = self.ly.title("Brahmagupta-Fibonacci Identity")
        identity = MathTex(
            r"(a^2 + b^2)(c^2 + d^2)",
            r"= (ac - bd)^2 + (ad + bc)^2",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(identity, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(identity), run_time=SLOW)
        self.wait(FAST)
        items = [
            Text("Product of two sums-of-squares IS a sum-of-squares",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

        title2 = self.ly.title("Example: 5 x 13 = 65")
        items2 = [
            Text("5 = 1\u00b2+2\u00b2,   13 = 2\u00b2+3\u00b2",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("a=1, b=2, c=2, d=3",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("ac-bd = 1(2)-2(3) = -4,  ad+bc = 1(3)+2(2) = 7",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("65 = (-4)\u00b2 + 7\u00b2 = 16 + 49 = 65",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.ly.clear()

    def scene4_descent_idea(self):
        self.add_subcaption(
            "Why is Fermat's theorem true? The key insight is a descent "
            "argument. If a prime p divides some sum of two squares, and "
            "p equals one mod four, then p itself must be a sum of two "
            "squares. The proof uses Thue's lemma, which guarantees the "
            "existence of integers x and y such that x squared plus y "
            "squared equals k times p for a small integer k. Then we "
            "use the Brahmagupta identity to reduce k step by step "
            "until k equals one.",
            duration=52,
        )
        self.ly.section_divider(3, "Why It's True")
        title = self.ly.title("Infinite Descent")
        items = [
            Text("1. p | (a\u00b2 + b\u00b2) for some a, b",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Thue's lemma: x\u00b2 + y\u00b2 = kp,  0 < k < p",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Brahmagupta identity reduces k to smaller k'",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Repeat until k = 1:  p = x\u00b2 + y\u00b2",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        title2 = self.ly.title("Crucial Ingredient")
        items2 = [
            Text("-1 is a QR mod p  iff  p = 1 (mod 4)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("(from quadratic reciprocity, Video 262)",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("So p | (a\u00b2 + 1) has a solution when p = 1 (mod 4)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.ly.clear()

    def scene5_negative_case(self):
        self.add_subcaption(
            "Why can a prime that is three mod four never be a sum of "
            "two squares? The reason is simple: modulo four, every "
            "integer square is either zero or one. So the sum of two "
            "squares can only be zero, one, or two modulo four. It can "
            "never equal three. Therefore no prime congruent to three "
            "mod four can be written as a sum of two squares.",
            duration=42,
        )
        self.ly.section_divider(4, "Why 3 mod 4 Fails")
        title = self.ly.title("The Modulo 4 Argument")
        items = [
            Text("n mod 4:     0   1   2   3",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("n\u00b2 mod 4:   0   1   0   1",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("So x\u00b2 + y\u00b2 mod 4 is 0, 1, or 2 only",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("x\u00b2 + y\u00b2 = 3 (mod 4) is IMPOSSIBLE",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene6_full_classification(self):
        self.add_subcaption(
            "Fermat's theorem tells us about primes, but what about all "
            "integers? The full classification says: a positive integer n "
            "is a sum of two squares if and only if every prime factor "
            "congruent to three mod four appears with an even exponent "
            "in the prime factorization of n.",
            duration=38,
        )
        self.ly.section_divider(5, "All Integers")
        title = self.ly.title("Full Classification")
        items = [
            Text("n = x\u00b2 + y\u00b2  iff every prime q = 3 (mod 4)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("appears with EVEN exponent in n's factorization",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        title2 = self.ly.title("Examples")
        items2 = [
            Text("45 = 3\u00b2 x 5  ->  3 squared (even)  ->  45 = 6\u00b2+3\u00b2",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("50 = 2 x 5\u00b2  ->  no 3-mod-4 primes  ->  50 = 5\u00b2+5\u00b2",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("21 = 3 x 7  ->  3,7 are 3 mod 4, exp 1  ->  NO",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.ly.clear()

    def scene7_worked_examples(self):
        self.add_subcaption(
            "Let us use the Brahmagupta identity to find a representation. "
            "Write sixty five as a sum of two squares. We know five "
            "equals one squared plus two squared, and thirteen equals two "
            "squared plus three squared. Setting a equals one, b equals two, "
            "c equals two, d equals three, we get ac minus bd equals minus four, "
            "and ad plus bc equals seven. So sixty five equals sixteen plus "
            "forty nine, which is four squared plus seven squared.",
            duration=56,
        )
        self.ly.section_divider(6, "Worked Examples")
        title = self.ly.title("Constructing 65 = 5 x 13")
        items = [
            Text("5 = 1\u00b2+2\u00b2  (a=1, b=2)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("13 = 2\u00b2+3\u00b2  (c=2, d=3)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("ac-bd = 1(2)-2(3) = -4",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("ad+bc = 1(3)+2(2) = 7",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("65 = (-4)\u00b2 + 7\u00b2 = 16 + 49",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene8_summary(self):
        self.add_subcaption(
            "To summarize. A prime is a sum of two squares exactly when "
            "it equals two or it is one modulo four. The Brahmagupta "
            "identity extends this to all integers: a number is a sum "
            "of two squares precisely when every prime factor congruent "
            "to three mod four appears with an even exponent. This "
            "beautiful result connects additive structure to the "
            "multiplicative structure of integers.",
            duration=46,
        )
        self.ly.section_divider(7, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("1. p = a\u00b2+b\u00b2  iff  p = 2 or p = 1 (mod 4)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Brahmagupta identity: products preserve the property",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. For all n: 3-mod-4 primes need even exponents",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()
        play_outro(self, "Sums of Two Squares", "Number Theory")
