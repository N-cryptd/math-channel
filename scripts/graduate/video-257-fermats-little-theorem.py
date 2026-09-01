"""
Video 257: Fermat's Little Theorem -- Number Theory

Statement, proof via group theory (Lagrange), direct combinatorial proof,
Wilson's theorem, applications to modular exponentiation, inverses, and primality.

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


class Video257_FermatsLittleTheorem(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_statement()
        self.scene3_group_proof()
        self.scene4_direct_proof()
        self.scene5_wilson()
        self.scene6_applications()
        self.scene7_summary()

    # ──────────────────────────────────────────────────────────────
    # Scene 1: Hook — Powers Modulo p
    # ──────────────────────────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "What is two to the power of one hundred, modulo seven? "
            "Computing this directly would be astronomical. But a beautiful "
            "result from the seventeenth century makes it trivial. "
            "This is Fermat's little theorem.",
            duration=20,
        )
        play_intro(self, "Fermat's Little Theorem", "Number Theory")

        title = self.ly.title("An Impossible Computation?")
        q = MathTex(r"2^{100} \bmod 7 = \;?",
                     font_size=TITLE_SIZE, color=RED)
        self.ly.safe_place(q, DOWN, anchor=title, buff=0.5)
        self.play(Write(q), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        title2 = self.ly.title("Look for a Pattern")
        items = [
            MathTex(r"2^1 = 2 \pmod{7}",
                    font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"2^2 = 4 \pmod{7}",
                    font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"2^3 = 1 \pmod{7}",
                    font_size=BODY_SIZE, color=ACCENT),
            MathTex(r"2^4 = 2, \; 2^5 = 4, \; 2^6 = 1 \pmod{7}",
                    font_size=BODY_SIZE, color=SECONDARY),
            Text("The period is 6 = 7 - 1.",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.ly.clear()

    # ──────────────────────────────────────────────────────────────
    # Scene 2: Statement
    # ──────────────────────────────────────────────────────────────
    def scene2_statement(self):
        self.add_subcaption(
            "Fermat's little theorem states that if p is prime and "
            "a is any integer not divisible by p, then a to the power "
            "p minus one is congruent to one modulo p. An equivalent "
            "form is a to the p equals a modulo p, for all integers a.",
            duration=18,
        )
        self.ly.section_divider(1, "The Theorem")
        title = self.ly.title("Statement")

        flt = MathTex(
            r"a^{p-1} \equiv 1 \pmod{p} \quad (\gcd(a,p)=1)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(flt, PRIMARY)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(flt), run_time=NORMAL)
        self.wait(2)
        self.play(FadeOut(boxed), run_time=FAST)

        items = [
            Text("Equivalent form (for all integers a):",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
            MathTex(r"a^{p} \equiv a \pmod{p}",
                    font_size=HEADING_SIZE, color=SECONDARY),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        title2 = self.ly.title("Examples")
        ex = [
            Text("p = 7,  a = 3:  3^6 = 729 = 1 (mod 7)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("p = 11, a = 5:  5^10 = 9765625 = 1 (mod 11)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("p = 5,  a = 2:  2^4 = 16 = 1 (mod 5)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(ex, start_from=title2)
        self.ly.clear()

    # ──────────────────────────────────────────────────────────────
    # Scene 3: Proof via Group Theory (Lagrange)
    # ──────────────────────────────────────────────────────────────
    def scene3_group_proof(self):
        self.add_subcaption(
            "The most elegant proof uses group theory. "
            "The multiplicative group of integers modulo p has "
            "order p minus one. By Lagrange's theorem, the order "
            "of any element divides the group order. "
            "Therefore a to the p minus one equals the identity.",
            duration=20,
        )
        self.ly.section_divider(2, "Proof via Lagrange")
        title = self.ly.title("The Group-Theoretic Proof")

        items = [
            Text("The multiplicative group (Z/pZ)* has order p - 1",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("It consists of {1, 2, ..., p-1} under multiplication",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
            MathTex(r"|\,(\mathbb{Z}/p\mathbb{Z})^{\times}\,| = p - 1",
                    font_size=BODY_SIZE, color=PRIMARY),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        title2 = self.ly.title("Lagrange's Theorem")
        items2 = [
            Text("The order of any element divides |G|",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("So ord(a) | (p - 1)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Therefore a^(p-1) = 1 (mod p)",
                 font_size=HEADING_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.ly.clear()

    # ──────────────────────────────────────────────────────────────
    # Scene 4: Direct Combinatorial Proof
    # ──────────────────────────────────────────────────────────────
    def scene4_direct_proof(self):
        self.add_subcaption(
            "Here is an elementary proof that does not need group theory. "
            "Multiply every element of one through p minus one by a. "
            "Since a is coprime to p, the map x to a x is a permutation "
            "of the set. So the products are equal, giving us the theorem.",
            duration=22,
        )
        self.ly.section_divider(3, "Direct Proof")
        title = self.ly.title("Permutation Argument")

        items = [
            Text("Consider the set S = {1, 2, ..., p-1}",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The map f(x) = ax (mod p) is a permutation of S",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("(since gcd(a,p) = 1, no collisions)",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        title2 = self.ly.title("Key Identity")
        items2 = [
            MathTex(r"\prod_{x=1}^{p-1} x \;=\; \prod_{x=1}^{p-1} ax \pmod{p}",
                    font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"(p-1)! \;=\; a^{p-1} \cdot (p-1)! \pmod{p}",
                    font_size=BODY_SIZE, color=SECONDARY),
            Text("Cancel (p-1)! (since gcd((p-1)!, p) = 1):",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"\Rightarrow \; a^{p-1} \equiv 1 \pmod{p} \quad \blacksquare",
                    font_size=HEADING_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.ly.clear()

    # ──────────────────────────────────────────────────────────────
    # Scene 5: Wilson's Theorem
    # ──────────────────────────────────────────────────────────────
    def scene5_wilson(self):
        self.add_subcaption(
            "A close cousin of Fermat's little theorem is Wilson's theorem. "
            "It says that p is prime if and only if p minus one factorial "
            "is congruent to negative one modulo p. We can prove it using "
            "the fact that in a group, every element has a unique inverse.",
            duration=22,
        )
        self.ly.section_divider(4, "Wilson's Theorem")
        title = self.ly.title("Wilson's Theorem")

        wilson = MathTex(
            r"p \text{ is prime } \iff (p-1)! \equiv -1 \pmod{p}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(wilson, PRIMARY)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(wilson), run_time=NORMAL)
        self.wait(2)
        self.play(FadeOut(boxed), run_time=FAST)

        items = [
            Text("In (Z/pZ)*, elements pair with their inverses",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Only 1 and -1 are self-inverse (for p > 2)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("So (p-1)! = 1 * (-1) * (pairs) = -1 (mod p)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        title2 = self.ly.title("Example")
        ex = [
            Text("p = 7:  6! = 720 = 102 * 7 + 6",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            MathTex(r"720 \equiv 6 \equiv -1 \pmod{7} \; \checkmark",
                    font_size=BODY_SIZE, color=ACCENT),
            Text("p = 5:  4! = 24 = 5*5 - 1",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            MathTex(r"24 \equiv -1 \pmod{5} \; \checkmark",
                    font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(ex, start_from=title2)
        self.ly.clear()

    # ──────────────────────────────────────────────────────────────
    # Scene 6: Applications
    # ──────────────────────────────────────────────────────────────
    def scene6_applications(self):
        self.add_subcaption(
            "Fermat's little theorem has powerful applications. "
            "We can compute enormous powers modulo p by reducing the "
            "exponent. It also gives us a formula for modular inverses "
            "and forms the basis of probabilistic primality tests.",
            duration=20,
        )
        self.ly.section_divider(5, "Applications")
        title = self.ly.title("Fast Modular Exponentiation")

        items = [
            Text("Compute 2^100 mod 7:",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"2^{100} = 2^{96} \cdot 2^4 = (2^6)^{16} \cdot 16",
                    font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"\equiv 1^{16} \cdot 16 \equiv 16 \equiv 2 \pmod{7}",
                    font_size=BODY_SIZE, color=ACCENT),
            Text("Answer: 2 (not so impossible after all!)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        title2 = self.ly.title("More Applications")
        items2 = [
            Text("Modular inverse:  a^{-1} = a^{p-2} (mod p)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Fermat primality test:",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("  if a^{p-1} != 1 (mod p), then p is composite",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Foundation of RSA encryption",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.ly.clear()

    # ──────────────────────────────────────────────────────────────
    # Scene 7: Summary
    # ──────────────────────────────────────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "Today we covered Fermat's little theorem: a to the p minus "
            "one equals one modulo p when p is prime. We proved it using "
            "Lagrange's theorem and a direct permutation argument. "
            "We saw Wilson's theorem and applications in cryptography.",
            duration=20,
        )
        self.ly.section_divider(6, "Key Takeaways")
        title = self.ly.title("Summary")

        items = [
            Text("1. a^{p-1} = 1 (mod p)  when gcd(a,p) = 1",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Proof: Lagrange's theorem or permutation argument",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Wilson's theorem: (p-1)! = -1 (mod p)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Applications: fast powers, inverses, primality",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        play_outro(self, "Euler's Totient Function", "Number Theory")
