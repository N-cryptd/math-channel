r"""
Video 258: Euler's Totient Function -- Number Theory

Definition via coprime counting, prime power formula, multiplicative
property (via CRT), product formula, and Euler's theorem as the
generalization of Fermat's Little Theorem.

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


class Video258_EulersTotient(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_table()
        self.scene4_prime_powers()
        self.scene5_multiplicative()
        self.scene6_product_formula()
        self.scene7_euler_theorem()
        self.scene8_summary()

    # ── Scene 1: Hook ───────────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Last time we saw Fermat's little theorem. For a prime p, "
            "a to the p minus one equals one mod p. But what if the "
            "modulus is composite? Euler found the answer, and the key "
            "is a remarkable counting function.",
            duration=18,
        )
        play_intro(self, "Euler's Totient Function", "Number Theory")

        title = self.ly.title("A Generalization of Fermat")
        items = [
            Text("Fermat: a^(p-1) = 1 (mod p)  -- primes only",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Question: what about mod 12? mod 15?",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Answer: Euler's totient function phi(n)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    # ── Scene 2: Definition and First Examples ──────────────────────
    def scene2_definition(self):
        self.add_subcaption(
            "Euler's totient function phi of n counts the integers from "
            "one to n that are coprime to n. Two numbers are coprime if "
            "their greatest common divisor is one. For example, phi of "
            "ten equals four, because one, three, seven, and nine are "
            "coprime to ten.",
            duration=24,
        )
        self.ly.section_divider(1, "Definition")
        title = self.ly.title("Euler's Totient Function")

        defn = MathTex(
            r"\varphi(n) = \#\left\{k \in \{1, \dots, n\} : \gcd(k, n) = 1\right\}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(defn, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(FAST)

        items = [
            Text("phi(10) = 4  (coprimes: 1, 3, 7, 9)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("phi(12) = 4  (coprimes: 1, 5, 7, 11)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    # ── Scene 3: Table of Values and Patterns ───────────────────────
    def scene3_table(self):
        self.add_subcaption(
            "Let's compute phi for the first twelve integers. For "
            "primes, phi of p equals p minus one, since every number "
            "from one to p minus one is coprime to p. There are other "
            "interesting patterns hiding in this table.",
            duration=20,
        )
        self.ly.section_divider(2, "Building Intuition")
        title = self.ly.title("phi(n) for n = 1 to 12")

        phi_vals = {
            1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 2,
            7: 6, 8: 4, 9: 6, 10: 4, 11: 10, 12: 4,
        }
        primes = {2, 3, 5, 7, 11}

        # Build rows in pairs to respect 5-item max visible
        pairs = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)]
        rows = []
        for grp in pairs:
            cells = []
            for n in grp:
                color = RED if n in primes else WHITE
                label = MathTex(
                    rf"\varphi({n})={phi_vals[n]}",
                    font_size=LABEL_SIZE, color=color,
                )
                cells.append(label)
            row = VGroup(*cells).arrange(RIGHT, buff=0.6)
            rows.append(row)

        # Reveal each row progressively
        for i, row in enumerate(rows):
            if i == 0:
                self.ly.safe_place(row, DOWN, anchor=title, buff=0.5)
            else:
                self.ly.safe_place(row, DOWN, anchor=rows[i - 1], buff=0.3)
            self.play(FadeIn(row, shift=LEFT * 0.1), run_time=FAST)
        self.wait(FAST)

        # Pattern callout
        items = [
            Text("Primes (red): phi(p) = p - 1",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=rows[-1])
        self.ly.clear()

    # ── Scene 4: Prime Powers ───────────────────────────────────────
    def scene4_prime_powers(self):
        self.add_subcaption(
            "For a prime p, every number from one to p minus one is "
            "coprime to p. So phi of p equals p minus one. For a prime "
            "power p to the k, we count all p to the k numbers and "
            "subtract the multiples of p. This gives phi of p to the k "
            "equals p to the k minus p to the k minus one.",
            duration=26,
        )
        self.ly.section_divider(3, "Prime Powers")
        title = self.ly.title("Totient of Prime Powers")

        items = [
            Text("For prime p: phi(p) = p - 1",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            MathTex(
                r"\varphi(p^k) = p^k - p^{k-1} = p^{k-1}(p - 1)",
                font_size=BODY_SIZE, color=ACCENT,
            ),
            Text("Example: phi(27) = 27 - 9 = 18",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Example: phi(16) = 16 - 8 = 8",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    # ── Scene 5: Multiplicative Property ────────────────────────────
    def scene5_multiplicative(self):
        self.add_subcaption(
            "The totient function is multiplicative. If m and n are "
            "coprime, then phi of m n equals phi of m times phi of n. "
            "This follows from the Chinese Remainder Theorem, which we "
            "saw earlier. Each coprime residue mod m pairs with each "
            "coprime residue mod n.",
            duration=22,
        )
        self.ly.section_divider(4, "Multiplicative Property")
        title = self.ly.title("When gcd(m, n) = 1")

        prop = MathTex(
            r"\varphi(mn) = \varphi(m) \cdot \varphi(n)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(prop, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(prop), run_time=NORMAL)
        self.wait(FAST)

        items = [
            Text("Proof idea: Chinese Remainder Theorem",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Each coprime residue mod m pairs with mod n",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("phi(15) = phi(3)*phi(5) = 2*4 = 8",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    # ── Scene 6: The Product Formula ────────────────────────────────
    def scene6_product_formula(self):
        self.add_subcaption(
            "Combining prime powers and multiplicativity gives the "
            "product formula. If n factors as p one to the a one times "
            "p two to the a two and so on, then phi of n equals n times "
            "one minus one over p one, times one minus one over p two, "
            "and so on. Let's work through an example.",
            duration=26,
        )
        self.ly.section_divider(5, "The Product Formula")
        title = self.ly.title("phi(n) via Prime Factorization")

        formula = MathTex(
            r"n = \textstyle\prod p_i^{a_i} "
            r"\Rightarrow "
            r"\varphi(n) = n \prod\!\left(1 - \tfrac{1}{p_i}\right)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(formula, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(FAST)

        items = [
            Text("phi(60) = 60 * (1-1/2)(1-1/3)(1-1/5) = 16",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("phi(72) = 72 * (1-1/2)(1-1/3) = 24",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    # ── Scene 7: Euler's Theorem ────────────────────────────────────
    def scene7_euler_theorem(self):
        self.add_subcaption(
            "Euler's theorem is the payoff. If a is coprime to n, then "
            "a to the phi of n equals one mod n. When n is prime, phi "
            "of n equals n minus one, and we recover Fermat's little "
            "theorem. For example, three to the eighth equals six "
            "thousand five hundred sixty one, which is one mod fifteen.",
            duration=26,
        )
        self.ly.section_divider(6, "Euler's Theorem")
        title = self.ly.title("The Generalization")

        thm = MathTex(
            r"\gcd(a, n) = 1 \; \Rightarrow \; a^{\varphi(n)} \equiv 1 \pmod{n}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(thm, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(thm), run_time=NORMAL)
        self.wait(FAST)

        items = [
            Text("When n = p: phi(p) = p - 1, so a^(p-1) = 1 (mod p)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("3^8 = 6561 = 1 (mod 15). phi(15) = 8. Confirmed!",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    # ── Scene 8: Summary and Outro ──────────────────────────────────
    def scene8_summary(self):
        self.add_subcaption(
            "Today we defined Euler's totient function phi of n, which "
            "counts the coprime integers up to n. We derived the prime "
            "power formula, the multiplicative property, and the product "
            "formula via prime factorization. Finally, Euler's theorem "
            "generalized Fermat's little theorem. The totient function "
            "is the key to RSA encryption, which we will explore next.",
            duration=28,
        )
        self.ly.section_divider(7, "Summary")
        title = self.ly.title("Key Takeaways")

        items = [
            Text("1. phi(n) counts integers coprime to n",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. phi(p^k) = p^(k-1)(p - 1)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Multiplicative: phi(mn) = phi(m)*phi(n)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Euler's theorem: a^phi(n) = 1 (mod n)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        play_outro(self, "Euler's Totient Function", "Number Theory")
