r"""
Video 253: The Fundamental Theorem of Arithmetic — Number Theory

Statement, existence proof, uniqueness proof via Euclid's lemma,
applications to GCD and LCM.

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


class Video253_FundamentalTheoremArithmetic(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_statement()
        self.scene3_existence()
        self.scene4_uniqueness()
        self.scene5_applications()
        self.scene6_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Every integer greater than one has a unique fingerprint. "
            "No matter how you try to break it apart, the prime factors "
            "are always the same. This fact is so natural that we take it "
            "for granted, but it actually requires a careful proof.",
            duration=16,
        )
        play_intro(self, "Fundamental Theorem of Arithmetic", "Number Theory")

        title = self.ly.title("The Unique Fingerprint of Every Integer")
        items = [
            Text("12 = 2 * 2 * 3, and there is no other way",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("This is NOT obvious -- it requires proof",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("We need: Existence AND Uniqueness",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene2_statement(self):
        self.add_subcaption(
            "The Fundamental Theorem of Arithmetic states that every integer "
            "greater than one can be written uniquely as a product of primes "
            "in non-decreasing order, up to the order of the factors.",
            duration=13,
        )
        self.ly.section_divider(1, "The Theorem")
        title = self.ly.title("Statement")

        thm = MathTex(
            r"n > 1 \;\text{ factors uniquely as }",
            r"n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(thm, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(thm), run_time=NORMAL)
        self.wait(FAST)

        items = [
            Text("p_1 < p_2 < ... < p_k are distinct primes",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Each exponent a_i >= 1",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    def scene3_existence(self):
        self.add_subcaption(
            "Existence means every integer greater than one can be factored "
            "into primes. We prove this by strong induction on n. "
            "If n is prime, we are done. Otherwise n equals a times b where "
            "both a and b are smaller, so by induction they factor into primes.",
            duration=16,
        )
        self.ly.section_divider(2, "Existence")
        title = self.ly.title("Every n > 1 Has a Prime Factorization")

        items = [
            Text("Base case: n=2 is prime, done",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Inductive step: assume true for all < n",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("If n is prime: done",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("If composite: n = a*b where 1 < a, b < n",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("By induction: a and b factor into primes",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene4_uniqueness(self):
        self.add_subcaption(
            "Uniqueness is the harder part. We use Euclid's lemma from "
            "the previous video. If we had two different factorizations, "
            "a prime from the first must divide a prime from the second, "
            "so they must be equal. Cancel and repeat.",
            duration=16,
        )
        self.ly.section_divider(3, "Uniqueness")
        title = self.ly.title("Why the Factorization is Unique")

        items = [
            Text("Assume two factorizations of n",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("p_1 * p_2 * ... * p_k = q_1 * q_2 * ... * q_m",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("By Euclid's lemma: p_1 divides some q_j",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Since q_j is prime: p_1 = q_j",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Cancel p_1 = q_j, apply induction on k",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene5_applications(self):
        self.add_subcaption(
            "The fundamental theorem gives us powerful tools. The GCD is "
            "the product of the minimum prime powers. The LCM is the product "
            "of the maximum. And they satisfy a beautiful relationship: "
            "GCD times LCM equals the product.",
            duration=15,
        )
        self.ly.section_divider(4, "Applications")
        title = self.ly.title("GCD, LCM, and Prime Factorization")

        gcd_lcm = MathTex(
            r"\mathrm{gcd}(a,b) \times \mathrm{lcm}(a,b) = a \times b",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(gcd_lcm, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(gcd_lcm), run_time=NORMAL)
        self.wait(FAST)

        items = [
            Text("GCD: take minimum exponent of each prime",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("LCM: take maximum exponent of each prime",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Example: gcd(12,18)=6, lcm(12,18)=36",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    def scene6_summary(self):
        self.add_subcaption(
            "Today we proved the fundamental theorem of arithmetic. "
            "Every integer greater than one has a unique prime "
            "factorization. Existence follows by induction, and "
            "uniqueness follows from Euclid's lemma. We also saw "
            "how prime factorization simplifies GCD and LCM computation. "
            "Next, we enter the world of modular arithmetic.",
            duration=19,
        )
        self.ly.section_divider(5, "Summary")
        title = self.ly.title("Key Takeaways")

        items = [
            Text("1. Every n > 1 factors uniquely into primes",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Existence: strong induction on n",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Uniqueness: Euclid's lemma + cancellation",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. gcd * lcm = a * b",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        play_outro(self, "Modular Arithmetic", "Number Theory")
