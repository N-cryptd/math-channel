r"""
Video 251: Divisibility and the Euclidean Algorithm — Number Theory

Divisibility definition, division algorithm, GCD, Euclidean algorithm,
Bezout's identity. First video in the Number Theory playlist (Videos 251-265).

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


class Video251_DivisibilityEuclidean(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_divisibility()
        self.scene3_division_algorithm()
        self.scene4_gcd()
        self.scene5_euclidean_algorithm()
        self.scene6_why_it_works()
        self.scene7_bezout()
        self.scene8_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Number theory begins with a simple question: when does one integer "
            "divide another? This idea of divisibility is the foundation for "
            "everything that follows, from prime numbers to cryptography.",
            duration=14,
        )
        play_intro(self, "Divisibility and the Euclidean Algorithm", "Number Theory")

        title = self.ly.title("The Foundation of Number Theory")
        items = [
            Text("Every integer secretly encodes its divisors",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Cryptography depends on divisibility properties",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Prime factorization, Diophantine equations, modular arithmetic",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene2_divisibility(self):
        self.add_subcaption(
            "We say a divides b, written with a vertical bar, if there exists "
            "an integer k such that b equals a times k. For example, 3 divides 12 "
            "because 12 equals 3 times 4. But 5 does not divide 12. "
            "Divisibility is reflexive and transitive.",
            duration=18,
        )
        self.ly.section_divider(1, "Divisibility")
        title = self.ly.title("Divisibility")

        # Definition in a formula box
        defn = MathTex(
            r"a \mid b \; \iff \; \exists\, k \in \mathbb{Z}: \; b = ak",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(defn, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(3)
        self.play(FadeOut(boxed), run_time=FAST)

        items = [
            MathTex(r"3 \mid 12", r"\quad \text{since } 12 = 3 \cdot 4",
                    font_size=BODY_SIZE, color=WHITE),
            MathTex(r"5 \nmid 12", r"\quad \text{(no integer } k \text{ works)}",
                    font_size=BODY_SIZE, color=RED),
            Text("Reflexive: a|a, Transitive: a|b and b|c implies a|c",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene3_division_algorithm(self):
        self.add_subcaption(
            "The division algorithm says that for any positive integer a and "
            "any integer b, there exist unique integers q and r such that "
            "b equals a times q plus r, where the remainder r satisfies "
            "0 is less than or equal to r, which is less than a. "
            "Think of it as placing b on the number line between consecutive multiples of a.",
            duration=22,
        )
        self.ly.section_divider(2, "Division Algorithm")
        title = self.ly.title("The Division Algorithm")

        # Theorem box
        thm = MathTex(
            r"a > 0, \; b \in \mathbb{Z} \; \Longrightarrow \; \exists!\, q, r: \; b = aq + r, \; 0 \leq r < a",
            font_size=BODY_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(thm, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(thm), run_time=NORMAL)
        self.wait(3)
        self.play(FadeOut(boxed), run_time=FAST)

        # Number line visualization for b=17, a=5
        axis = NumberLine(
            x_range=[0, 22, 1], length=10,
            color=DIM, include_numbers=False, font_size=LABEL_SIZE,
        )
        self.ly.safe_place(axis, DOWN, anchor=title, buff=0.6)

        # Multiples of 5
        mults = [0, 5, 10, 15, 20]
        dots_and_labels = VGroup()
        for m in mults:
            d = Dot(axis.n2p(m), radius=0.07, color=PRIMARY)
            lbl = MathTex(r"{}a".format(m // 5) if m > 0 else r"0",
                          font_size=LABEL_SIZE, color=PRIMARY)
            lbl.next_to(d, UP, buff=0.15)
            dots_and_labels.add(d, lbl)

        # b = 17
        b_dot = Dot(axis.n2p(17), radius=0.07, color=ACCENT)
        b_label = MathTex(r"b", font_size=LABEL_SIZE, color=ACCENT)
        b_label.next_to(b_dot, DOWN, buff=0.15)

        self.play(Create(axis), run_time=FAST)
        self.play(
            *[FadeIn(d) for d in dots_and_labels],
            run_time=1.0, lag_ratio=0.15,
        )
        self.play(FadeIn(b_dot), FadeIn(b_label), run_time=FAST)
        self.wait(1.5)

        # Show q=3, r=2
        qr_text = MathTex(
            r"q = 3, \quad r = 2, \quad b = 5 \cdot 3 + 2",
            font_size=BODY_SIZE, color=WHITE,
        )
        qr_text.next_to(axis, DOWN, buff=0.4)
        self.play(Write(qr_text), run_time=NORMAL)
        self.wait(3)
        self.ly.clear()

    def scene4_gcd(self):
        self.add_subcaption(
            "The greatest common divisor of a and b is the largest positive "
            "integer that divides both. We write it as G C D of a comma b. "
            "When the G C D equals 1, we say a and b are coprime or relatively prime. "
            "For example, 8 and 15 are coprime since they share no common factor.",
            duration=18,
        )
        self.ly.section_divider(3, "Greatest Common Divisor")
        title = self.ly.title("Greatest Common Divisor")

        defn = MathTex(
            r"\gcd(a, b) = \max\{d > 0 : d \mid a \text{ and } d \mid b\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(defn, PRIMARY)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(3)
        self.play(FadeOut(boxed), run_time=FAST)

        items = [
            MathTex(r"\gcd(12, 18) = 6",
                    font_size=HEADING_SIZE, color=WHITE),
            MathTex(r"\gcd(35, 14) = 7",
                    font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"\gcd(8, 15) = 1 \quad \text{(coprime)}",
                    font_size=HEADING_SIZE, color=SECONDARY),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene5_euclidean_algorithm(self):
        self.add_subcaption(
            "The Euclidean algorithm computes the G C D efficiently using "
            "repeated division. The key idea: G C D of a and b equals G C D "
            "of b and the remainder. We apply this repeatedly until the remainder "
            "is zero. Let us find G C D of 252 and 105.",
            duration=18,
        )
        self.ly.section_divider(4, "The Euclidean Algorithm")
        title = self.ly.title("The Euclidean Algorithm")

        # Key property
        key_prop = MathTex(
            r"\gcd(a, b) = \gcd(b, \; a \bmod b)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(key_prop, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(key_prop), run_time=NORMAL)
        self.wait(3)
        self.play(FadeOut(boxed), run_time=FAST)

        # Worked example step by step
        steps = [
            MathTex(r"252 = 2 \cdot 105 + 42",
                    font_size=HEADING_SIZE, color=WHITE),
            MathTex(r"105 = 2 \cdot 42 + 21",
                    font_size=HEADING_SIZE, color=WHITE),
            MathTex(r"42 = 2 \cdot 21 + 0",
                    font_size=HEADING_SIZE, color=WHITE),
        ]
        result = MathTex(
            r"\therefore \; \gcd(252, 105) = 21",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.progressive_reveal(steps, start_from=title)
        self.ly.safe_place(result, DOWN, anchor=steps[-1], buff=0.3)
        self.play(Write(result), run_time=NORMAL)
        self.wait(3)
        self.ly.clear()

    def scene6_why_it_works(self):
        self.add_subcaption(
            "Why does the Euclidean algorithm work? If d divides both a and b, "
            "then d divides any linear combination, in particular d divides a minus b q. "
            "So the set of common divisors is unchanged when we replace a with the "
            "remainder. The remainders strictly decrease, so the algorithm must terminate.",
            duration=18,
        )
        title = self.ly.title("Correctness of the Algorithm")

        items = [
            Text("If d|a and d|b, then d|(a - bq) for any integer q",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("So: common divisors of (a, b) = common divisors of (b, r)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Remainders form a strictly decreasing sequence",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Terminates when r = 0, and the last nonzero r is the GCD",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene7_bezout(self):
        self.add_subcaption(
            "Bezout's identity states that for any integers a and b, not both zero, "
            "there exist integers x and y such that a x plus b y equals G C D of a and b. "
            "We find x and y by back-substituting through the Euclidean algorithm steps. "
            "For our example, 21 equals 5 times 105 minus 2 times 252. "
            "A corollary: a and b are coprime if and only if a x plus b y equals 1 has a solution.",
            duration=24,
        )
        self.ly.section_divider(5, "Bezout's Identity")
        title = self.ly.title("Bezout's Identity")

        # Theorem
        thm = MathTex(
            r"\exists\, x, y \in \mathbb{Z}: \; ax + by = \gcd(a, b)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(thm, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(thm), run_time=NORMAL)
        self.wait(3)
        self.play(FadeOut(boxed), run_time=FAST)

        # Back-substitution
        sub1 = MathTex(
            r"21 = 105 - 2 \cdot 42",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(sub1, DOWN, anchor=title, buff=0.5)
        self.play(Write(sub1), run_time=NORMAL)
        self.wait(2)
        self.play(FadeOut(sub1), run_time=FAST)

        sub2 = MathTex(
            r"42 = 252 - 2 \cdot 105 \; \Rightarrow \; 21 = 5 \cdot 105 - 2 \cdot 252",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(sub2, DOWN, anchor=title, buff=0.5)
        self.play(Write(sub2), run_time=NORMAL)
        self.wait(3)
        self.play(FadeOut(sub2), run_time=FAST)

        # Corollary
        cor = MathTex(
            r"a, b \text{ coprime } \iff \exists\, x, y: \; ax + by = 1",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(cor, DOWN, anchor=title, buff=0.5)
        self.play(Write(cor), run_time=NORMAL)
        self.wait(3)
        self.ly.clear()

    def scene8_summary(self):
        self.add_subcaption(
            "To summarize: divisibility captures when one integer is a multiple of another. "
            "The division algorithm guarantees unique quotients and remainders. "
            "The G C D finds the largest shared divisor. The Euclidean algorithm "
            "computes it efficiently. And Bezout's identity shows the G C D is a "
            "linear combination. These tools power everything in number theory.",
            duration=20,
        )
        self.ly.section_divider(6, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("a|b iff b = ak for some integer k",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Division algorithm: b = aq + r with 0 <= r < a",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("gcd(a, b) = largest positive common divisor",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Euclidean algorithm: gcd(a, b) = gcd(b, a mod b)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Bezout: ax + by = gcd(a, b) always has a solution",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        play_outro(self, "Prime Numbers", "Number Theory")
