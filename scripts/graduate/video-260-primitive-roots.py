r"""
Video 260: Primitive Roots -- Number Theory

Order of an element, primitive root definition, existence theorems,
how to test for primitive roots, and applications.

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


class Video260_PrimitiveRoots(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_order()
        self.scene3_definition()
        self.scene4_existence()
        self.scene5_when_exist()
        self.scene6_finding()
        self.scene7_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Consider the powers of three modulo seven. Three to the "
            "first is three, three squared is two, three cubed is six, "
            "and so on. We get every nonzero residue. But the powers "
            "of two only give us one, two, and four. What makes three "
            "special? It is a primitive root.",
            duration=26,
        )
        play_intro(self, "Primitive Roots", "Number Theory")
        title = self.ly.title("Powers That Generate Everything")
        items = [
            Text("Powers of 3 mod 7: 3, 2, 6, 4, 5, 1 (all 6!)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Powers of 2 mod 7: 2, 4, 1 (only 3)",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("3 is a primitive root mod 7; 2 is not",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene2_order(self):
        self.add_subcaption(
            "The order of a modulo n is the smallest positive integer "
            "k such that a to the k equals one mod n. The order always "
            "divides phi of n, by Lagrange's theorem from group theory. "
            "For example, the order of three mod seven is six, which "
            "equals phi of seven. The order of two mod seven is three.",
            duration=30,
        )
        self.ly.section_divider(1, "Order of an Element")
        title = self.ly.title("The Order Function")
        defn = MathTex(
            r"\text{ord}_n(a) = 	ext{min}\{k > 0 : a^k \equiv 1 \pmod{n}\}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(defn, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(FAST)
        items = [
            Text("ord_n(a) always divides phi(n)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("ord_7(3) = 6 = phi(7)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("ord_7(2) = 3",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    def scene3_definition(self):
        self.add_subcaption(
            "A primitive root modulo n is an integer a whose order "
            "equals phi of n. In group theory terms, a primitive root "
            "generates the entire multiplicative group. The powers of a "
            "cycle through every element coprime to n. Three generates "
            "all of the nonzero residues mod seven, so it is a primitive root.",
            duration=30,
        )
        self.ly.section_divider(2, "Primitive Root Definition")
        title = self.ly.title("When Order Equals phi(n)")
        defn = MathTex(
            r"a \text{ is a primitive root mod } n \\ \iff \\ \text{ord}_n(a) = \varphi(n)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(defn, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(FAST)
        items = [
            Text("3 is a primitive root mod 7 (order = 6 = phi(7))",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2 is NOT: order is 3, but phi(7) = 6",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Powers of a primitive root give ALL coprime residues",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    def scene4_existence(self):
        self.add_subcaption(
            "A fundamental theorem states that primitive roots exist "
            "for every prime p. The multiplicative group of integers "
            "mod p is always cyclic. How many primitive roots are there "
            "mod p? Exactly phi of p minus one. For p equals seven, "
            "phi of six equals two, and the primitive roots are three and five.",
            duration=34,
        )
        self.ly.section_divider(3, "Existence for Primes")
        title = self.ly.title("Every Prime Has Primitive Roots")
        items = [
            Text("(Z/pZ)* is always cyclic (for prime p)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            MathTex(r"	ext{\# primitive roots mod } p = \varphi(p-1)",
                    font_size=BODY_SIZE, color=ACCENT),
            Text("p=7: phi(6)=2, primitive roots are 3 and 5",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene5_when_exist(self):
        self.add_subcaption(
            "More generally, primitive roots exist modulo n exactly "
            "when n is two, four, p to the k, or two p to the k, for "
            "an odd prime p. In particular, they never exist modulo "
            "two to the k for k at least three. For example, mod eight "
            "the orders are all at most two, but phi of eight is four.",
            duration=32,
        )
        self.ly.section_divider(4, "When Do They Exist?")
        title = self.ly.title("The Existence Theorem")
        items = [
            Text("Primes p: ALWAYS have primitive roots",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("p^k and 2p^k (p odd): always",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("n = 4: yes (primitive root = 3)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2^k for k >= 3: NEVER",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene6_finding(self):
        self.add_subcaption(
            "To test whether g is a primitive root mod p, factor "
            "p minus one into primes. Then for each prime factor q, "
            "check that g to the power of p minus one over q is not "
            "one mod p. If all checks pass, g is a primitive root. "
            "For example, to test five mod eleven: p minus one is ten, "
            "whose prime factors are two and five.",
            duration=36,
        )
        self.ly.section_divider(5, "Finding Primitive Roots")
        title = self.ly.title("Testing Algorithm")
        items = [
            Text("1. Factor p-1 = q1 * q2 * ...",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. For each prime factor q of p-1:",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("   check g^((p-1)/q) != 1 (mod p)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. If all pass: g is a primitive root",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene7_summary(self):
        self.add_subcaption(
            "Today we defined the order of an element and primitive "
            "roots. Every prime has primitive roots, and we learned "
            "exactly when they exist for composite moduli. The "
            "discrete logarithm problem, given a primitive root g and "
            "a residue b, finding the exponent, is the basis of "
            "Diffie-Hellman key exchange. Next time: quadratic residues.",
            duration=30,
        )
        self.ly.section_divider(6, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("1. ord_n(a) = smallest k with a^k = 1 (mod n)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Primitive root: order = phi(n)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Exist for primes, p^k, 2p^k, and n=4",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Applications: discrete log, Diffie-Hellman",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()
        play_outro(self, "Primitive Roots", "Number Theory")
