r"""
Video 254: Modular Arithmetic -- Number Theory

Definition of congruence, equivalence classes, arithmetic rules,
exponentiation, Fermat's little theorem, applications.

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


class Video254_ModularArithmetic(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_rules()
        self.scene4_exponentiation()
        self.scene5_applications()
        self.scene6_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "What time is it ten hours after seven o'clock? "
            "The answer is five o'clock. You just did modular "
            "arithmetic mod twelve without realizing it."
            " This simple idea powers modern cryptography.",
            duration=14,
        )
        play_intro(self, "Modular Arithmetic", "Number Theory")

        title = self.ly.title("Clock Arithmetic")
        items = [
            Text("7 + 10 = 17, but on a clock: 17 mod 12 = 5",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("We only care about the remainder",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Powers all of modern cryptography (RSA)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene2_definition(self):
        self.add_subcaption(
            "We say a is congruent to b modulo n if n divides "
            "a minus b. This defines an equivalence relation on "
            "the integers, partitioning them into n residue classes.",
            duration=13,
        )
        self.ly.section_divider(1, "Congruence")
        title = self.ly.title("Definition of Congruence")

        defn = MathTex(
            r"a \equiv b \pmod{n} \iff n \mid (a - b)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(defn, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(FAST)

        items = [
            Text("Reflexive: a = a (mod n)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Symmetric: a = b => b = a (mod n)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Transitive: a = b and b = c => a = c (mod n)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    def scene3_rules(self):
        self.add_subcaption(
            "Modular arithmetic preserves addition and multiplication. "
            "You can reduce modulo n at any point in the computation. "
            "This makes computing with large numbers much easier.",
            duration=13,
        )
        self.ly.section_divider(2, "Arithmetic Rules")
        title = self.ly.title("Computing Mod n")

        items = [
            MathTex(r"(a + b) \bmod n = ((a \bmod n) + (b \bmod n)) \bmod n",
                    font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"(a \cdot b) \bmod n = ((a \bmod n) \cdot (b \bmod n)) \bmod n",
                    font_size=BODY_SIZE, color=SECONDARY),
            Text("Reduce at any step -- order does not matter",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Example: 17 * 23 mod 5 = 2 * 3 mod 5 = 1",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene4_exponentiation(self):
        self.add_subcaption(
            "Fermat's little theorem says that for any prime p "
            "and integer a not divisible by p, a to the power of "
            "p minus one is congruent to one modulo p. This is "
            "incredibly powerful for computing large powers mod p.",
            duration=16,
        )
        self.ly.section_divider(3, "Fermat's Little Theorem")
        title = self.ly.title("A Powerful Shortcut")

        flt = MathTex(
            r"a^{p-1} \equiv 1 \pmod{p} \quad (p \text{ prime, } p \nmid a)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(flt, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.4)
        self.play(Write(flt), run_time=NORMAL)
        self.wait(FAST)

        items = [
            Text("Compute 2^100 mod 7 using FLT",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            MathTex(r"2^6 \equiv 1 \pmod{7}, \; 100 = 16 \cdot 6 + 4",
                    font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"2^{100} = (2^6)^{16} \cdot 2^4 \equiv 1 \cdot 16 \equiv 2 \pmod{7}",
                    font_size=BODY_SIZE, color=WHITE),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.ly.clear()

    def scene5_applications(self):
        self.add_subcaption(
            "Modular arithmetic appears everywhere. ISBN check "
            "digits detect typos in book numbers. Hash functions "
            "in computer science use modular arithmetic. And "
            "RSA encryption relies entirely on modular exponentiation.",
            duration=16,
        )
        self.ly.section_divider(4, "Applications")
        title = self.ly.title("Why This Matters")

        items = [
            Text("ISBN check digits: detect errors in book numbers",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Hash functions: map data to fixed-size values",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("RSA encryption: relies on modular exponentiation",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Next video: solving equations in modular arithmetic",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene6_summary(self):
        self.add_subcaption(
            "Today we learned modular arithmetic. Congruence means "
            "two numbers have the same remainder. Modular arithmetic "
            "preserves addition and multiplication. Fermat's little "
            "theorem gives a powerful shortcut for prime moduli. "
            "Next, we solve linear equations in modular arithmetic.",
            duration=18,
        )
        self.ly.section_divider(5, "Summary")
        title = self.ly.title("Key Takeaways")

        items = [
            Text("1. a = b (mod n) iff n divides (a-b)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Addition and multiplication work mod n",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Fermat: a^(p-1) = 1 (mod p) for prime p",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Foundation for cryptography and CS",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        play_outro(self, "Linear Congruences", "Number Theory")
