r"""
Video 255: Linear Congruences -- Number Theory

Solving ax = b (mod n), modular inverses via extended Euclidean algorithm,
existence criterion (gcd | b), number of solutions, systems of congruences.

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


class Video255_LinearCongruences(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_inverses()
        self.scene4_systems()
        self.scene5_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "What is x if three x equals seven mod eleven? "
            "To answer this, we need the modular inverse of three. "
            "The Euclidean algorithm from video two fifty one gives us a way.",
            duration=14,
        )
        play_intro(self, "Linear Congruences", "Number Theory")

        title = self.ly.title("Solving Equations Mod n")
        items = [
            Text("What is x if 3x = 7 (mod 11)?",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("We need the modular inverse of 3 mod 11",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The Euclidean algorithm finds it for us",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene2_definition(self):
        self.add_subcaption(
            "A linear congruence is an equation of the form a x "
            "equals b mod n. It has a solution if and only if the "
            "greatest common divisor of a and n divides b. "
            "If gcd of a and n is one, there is exactly one solution.",
            duration=16,
        )
        self.ly.section_divider(1, "Linear Congruences")
        title = self.ly.title("When Does a Solution Exist?")

        eq = MathTex(
            r"ax \\equiv b \\pmod{n}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(eq, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(FAST)

        items = [
            MathTex(r"\mathrm{Solvable} \iff \gcd(a,n) \mid b",
                    font_size=BODY_SIZE, color=PRIMARY),
            Text("If gcd(a,n) = 1: unique solution",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("If gcd(a,n) = d > 1 and d | b: d solutions",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    def scene3_inverses(self):
        self.add_subcaption(
            "The modular inverse of a modulo n is a number a inverse "
            "such that a times a inverse equals one mod n. We find it using "
            "the extended Euclidean algorithm. For example, the inverse of "
            "three mod eleven is four, since three times four is twelve, "
            "which is one mod eleven.",
            duration=18,
        )
        self.ly.section_divider(2, "Modular Inverse")
        title = self.ly.title("Finding the Inverse")

        inv_def = MathTex(
            r"a \\cdot a^{-1} \\equiv 1 \\pmod{n}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(inv_def, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(inv_def), run_time=NORMAL)
        self.wait(FAST)

        items = [
            Text("Exists iff gcd(a, n) = 1",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Find via extended Euclidean algorithm",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"3^{-1} = 4 \\pmod{11} \\(3 \\cdot 4 = 12 \\equiv 1)",
                    font_size=BODY_SIZE, color=SECONDARY),
            Text("Then 3x = 7 (mod 11) gives x = 4*7 = 28 = 6 (mod 11)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    def scene4_systems(self):
        self.add_subcaption(
            "What if we have multiple congruences simultaneously? "
            "For example, x equals two mod three and x equals three mod five. "
            "Checking by hand: two, five, eight, eleven, fourteen. "
            "Eight mod five is three. So x equals eight is the answer. "
            "But there is a systematic method called the Chinese Remainder Theorem.",
            duration=20,
        )
        self.ly.section_divider(3, "Systems of Congruences")
        title = self.ly.title("Multiple Constraints")

        items = [
            MathTex(r"x \\equiv 2 \\pmod{3}, \\quad x \\equiv 3 \\pmod{5}",
                    font_size=BODY_SIZE, color=PRIMARY),
            Text("Check: 2, 5, 8, 11, 14, 17, 20, 23...",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("8 mod 3 = 2 and 8 mod 5 = 3. Solution: x = 8",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("This is tedious -- we need the Chinese Remainder Theorem",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene5_summary(self):
        self.add_subcaption(
            "Today we learned how to solve linear congruences. "
            "The equation a x equals b mod n is solvable when the "
            "GCD of a and n divides b. We find the modular inverse "
            "using the extended Euclidean algorithm. And systems of "
            "congruences lead us to the Chinese Remainder Theorem, "
            "which we will cover in the next video.",
            duration=20,
        )
        self.ly.section_divider(4, "Summary")
        title = self.ly.title("Key Takeaways")

        items = [
            Text("1. ax = b (mod n) solvable iff gcd(a,n) | b",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Modular inverse via extended Euclidean algorithm",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Unique solution when gcd(a,n) = 1",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Systems of congruences -> Chinese Remainder Theorem",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        play_outro(self, "Chinese Remainder Theorem", "Number Theory")
