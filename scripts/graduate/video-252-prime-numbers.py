r"""
Video 252: Prime Numbers — Number Theory

Definition, infinitude (Euclid's proof), sieve of Eratosthenes,
distribution of primes (PNT statement), Euclid's lemma.

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


class Video252_PrimeNumbers(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_infinitude()
        self.scene4_sieve()
        self.scene5_distribution()
        self.scene6_properties()
        self.scene7_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Every integer has a story about how it breaks apart. "
            "Some numbers refuse to break down at all. "
            "These are the prime numbers, the atoms of arithmetic.",
            duration=12,
        )
        play_intro(self, "Prime Numbers", "Number Theory")

        title = self.ly.title("The Atoms of Arithmetic")
        items = [
            Text("2, 3, 5, 7, 11, 13, 17, 19, 23, 29...",
                 font_size=HEADING_SIZE, color=ACCENT, font=SANS),
            Text("These numbers refuse to be broken down further",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Every other integer is built from them",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene2_definition(self):
        self.add_subcaption(
            "A prime number is an integer greater than one whose only "
            "positive divisors are one and itself. A composite number has "
            "at least one other divisor. Note that one is neither prime nor "
            "composite, which is crucial for unique factorization.",
            duration=15,
        )
        self.ly.section_divider(1, "Definition")
        title = self.ly.title("What is a Prime?")

        defn = MathTex(
            r"p > 1, \; d | p \Rightarrow d=1 \text{ or } d=p",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(defn, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(FAST)

        items = [
            Text("Divisors of p are exactly {1, p}",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Composite: n > 1 with a non-trivial divisor",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("1 is neither prime nor composite (by convention)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    def scene3_infinitude(self):
        self.add_subcaption(
            "Euclid proved that there are infinitely many primes around "
            "300 BC. The proof is by contradiction. Assume there are only "
            "finitely many primes, multiply them all together and add one. "
            "This new number cannot be divided by any prime on the list.",
            duration=15,
        )
        self.ly.section_divider(2, "Infinitely Many Primes")
        title = self.ly.title("Euclid's Theorem")

        items = [
            Text("Theorem: there are infinitely many prime numbers",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Proof (by contradiction):",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        # The title + 2 items from above are already on screen (5 items used? No - progressive_reveal auto-removes oldest)
        # Actually, progressive_reveal removes oldest at 5 items. We had 3 (title is not counted as part of items).
        # Let's just clear and show proof steps fresh.
        self.ly.clear()

        title2 = self.ly.title("Proof Steps")
        steps = [
            Text("Assume only finitely many: p_1, ..., p_n",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Let N = p_1 * p_2 * ... * p_n + 1",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("N mod p_i = 1 for each i (not divisible)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("N is prime or has a new prime factor",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Contradiction! Infinitely many primes exist",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(steps, start_from=title2)
        self.ly.clear()

    def scene4_sieve(self):
        self.add_subcaption(
            "The Sieve of Eratosthenes is an ancient algorithm for finding "
            "all primes up to a given limit. Start with two, cross out all "
            "its multiples, then move to the next uncrossed number and repeat.",
            duration=13,
        )
        self.ly.section_divider(3, "Finding Primes")
        title = self.ly.title("The Sieve of Eratosthenes")

        items = [
            Text("Algorithm: list integers from 2 to N",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Cross out all multiples of 2 (evens)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Next uncrossed number is prime: 3, 5, 7, ...",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Complexity: O(N log log N)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene5_distribution(self):
        self.add_subcaption(
            "How common are primes? The prime counting function pi of N "
            "counts primes up to N. Pi of 10 is 4, pi of 100 is 25, and "
            "pi of 1000 is 168. The prime number theorem tells us pi of N "
            "is approximately N over the natural log of N.",
            duration=15,
        )
        self.ly.section_divider(4, "Distribution of Primes")
        title = self.ly.title("How Common Are Primes?")

        pi_fn = MathTex(
            r"\pi(N) = \text{number of primes } \leq N",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(pi_fn, DOWN, anchor=title, buff=0.4)
        self.play(Write(pi_fn), run_time=NORMAL)
        self.wait(FAST)

        items = [
            MathTex(r"\pi(10)=4, \quad \pi(100)=25, \quad \pi(1000)=168",
                    font_size=BODY_SIZE, color=WHITE),
            MathTex(r"\pi(N) \sim \frac{N}{\ln N} \; \text{(Prime Number Thm)}",
                    font_size=BODY_SIZE, color=ACCENT),
            Text("Primes thin out, but never run out",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=pi_fn)
        self.ly.clear()

    def scene6_properties(self):
        self.add_subcaption(
            "Euclid's lemma: if a prime divides a product, it must divide "
            "at least one factor. This uses Bezout's identity from the "
            "previous video and is the key step toward unique factorization.",
            duration=13,
        )
        self.ly.section_divider(5, "Key Properties")
        title = self.ly.title("Euclid's Lemma")

        lemma = MathTex(
            r"p \mid ab \; \Rightarrow \; p \mid a \; \text{ or } \; p \mid b",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(lemma, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(lemma), run_time=NORMAL)
        self.wait(FAST)

        items = [
            Text("Only true for primes (not composites!)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Proof uses Bezout's identity (Video 251)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("This is the key to unique factorization",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    def scene7_summary(self):
        self.add_subcaption(
            "Today we covered four key ideas. Primes have exactly two "
            "divisors. There are infinitely many, as Euclid proved. The "
            "sieve of Eratosthenes finds primes efficiently. And the prime "
            "number theorem describes how primes thin out. Next, we prove "
            "that every integer factors uniquely into primes.",
            duration=18,
        )
        self.ly.section_divider(6, "Summary")
        title = self.ly.title("Key Takeaways")

        items = [
            Text("1. Primes: p > 1 with divisors {1, p}",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Infinitely many (Euclid, 300 BC)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Sieve of Eratosthenes: O(N log log N)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. pi(N) ~ N / ln(N) (primes thin out)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        play_outro(self, "Fundamental Theorem of Arithmetic", "Number Theory")
