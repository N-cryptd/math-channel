"""
Video 264: Diophantine Equations -- Number Theory (FINALE)

Linear Diophantine equations (existence + extended Euclidean algorithm),
Pythagorean triples (Euclid's formula with proof idea),
and general strategies for solving Diophantine equations.

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


class Video264_DiophantineEquations(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_definition()
        self.scene3_existence()
        self.scene4_extended_euclid()
        self.scene5_general_solution()
        self.scene6_pythagorean()
        self.scene7_general_strategy()
        self.scene8_summary()

    def scene1_hook(self):
        """Fermat's Last Theorem as motivation."""
        self.add_subcaption(
            "In 1637, Pierre de Fermat wrote in the margin of a book "
            "that x to the n plus y to the n equals z to the n has no "
            "positive integer solutions when n is greater than two. He "
            "claimed he had a proof, but the margin was too small to "
            "contain it. It took three hundred and fifty eight years before "
            "Andrew Wiles finally proved this. The equation Fermat was "
            "studying is a Diophantine equation. We seek integer solutions "
            "to polynomial equations, and today we learn which ones we "
            "can actually solve.",
            duration=52,
        )
        play_intro(self, "Diophantine Equations", "Number Theory")
        title = self.ly.title("Fermat's Famous Margin")
        flt = MathTex(
            r"x^n + y^n = z^n", r"\quad (n > 2)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(flt, DOWN, anchor=title, buff=0.5)
        self.play(Write(flt), run_time=NORMAL)
        self.wait(FAST)
        items = [
            Text("No positive integer solutions (Wiles, 1995)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Today: the Diophantine equations we CAN solve",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=flt)
        self.ly.clear()

    def scene2_definition(self):
        """Define Diophantine equations and contrast with continuous."""
        self.add_subcaption(
            "A Diophantine equation is a polynomial equation where we "
            "restrict ourselves to integer solutions only. Named after "
            "Diophantus of Alexandria, who studied them in the third "
            "century. The key distinction: the equation x plus y equals "
            "five has infinitely many real solutions, a whole line, but "
            "only finitely many integer solutions. We want exactly those "
            "lattice points.",
            duration=42,
        )
        self.ly.section_divider(1, "What Are Diophantine Equations?")
        title = self.ly.title("Integer Solutions Only")
        items = [
            Text("Polynomial equation P(x, y, ...) = 0",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Solutions must be INTEGERS (not real or complex)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Named after Diophantus of Alexandria (3rd century)",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        title2 = self.ly.title("Example: x + y = 5")
        eq = MathTex(
            r"x + y = 5", r"\;\Rightarrow\;",
            r"(0,5),\; (1,4),\; (2,3),\; (3,2),\; (4,1),\; (5,0)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(eq), run_time=SLOW)
        self.wait(FAST)
        item = Text(
            "6 integer solutions out of infinitely many real ones",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(item, DOWN, anchor=eq, buff=0.4)
        self.play(FadeIn(item, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(FAST)
        self.ly.clear()

    def scene3_existence(self):
        """Existence criterion for linear Diophantine equations."""
        self.add_subcaption(
            "The simplest Diophantine equations are linear: a x plus b y "
            "equals c. When do integer solutions exist? The answer is "
            "clean: solutions exist if and only if the greatest common divisor "
            "of a and b divides c. The reasoning is straightforward. If d "
            "equals gcd of a and b, then d divides a x plus b y for all "
            "integers x and y. So if d does not divide c, no solutions. "
            "Conversely, the extended Euclidean algorithm guarantees a "
            "solution when d does divide c.",
            duration=50,
        )
        self.ly.section_divider(2, "Linear Diophantine Equations")
        title = self.ly.title("When Do Solutions Exist?")
        eq = MathTex(
            r"ax + by = c",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(eq, DOWN, anchor=title, buff=0.5)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(FAST)
        items = [
            Text("Let d = gcd(a, b)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Solutions exist  if and only if  d | c",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=eq)
        self.ly.clear()

        title2 = self.ly.title("Yes: 6x + 15y = 9")
        items2 = [
            Text("gcd(6, 15) = 3",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3 | 9, so solutions EXIST",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.ly.clear()

        title3 = self.ly.title("No: 6x + 15y = 10")
        items3 = [
            Text("gcd(6, 15) = 3",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3 does NOT divide 10, so NO solutions",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items3, start_from=title3)
        self.ly.clear()

    def scene4_extended_euclid(self):
        """Worked example using the extended Euclidean algorithm."""
        self.add_subcaption(
            "Let us solve two x plus five y equals three. Since gcd of two "
            "and five is one, and one divides three, solutions exist. We use "
            "the extended Euclidean algorithm. Divide five by two: five "
            "equals two times two plus one. This gives us one equals five minus "
            "two times two. Multiply by three: three equals fifteen minus "
            "six, or equivalently, two times negative one plus five times one "
            "equals three. So one solution is x zero equals negative one, y "
            "zero equals one.",
            duration=56,
        )
        self.ly.section_divider(3, "Extended Euclidean Algorithm")
        title = self.ly.title("Example: 2x + 5y = 3")
        eq = MathTex(
            r"2x + 5y = 3", r"\quad d = \gcd(2,5) = 1 \mid 3 \;\checkmark",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(eq, DOWN, anchor=title, buff=0.5)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(FAST)
        items = [
            Text("Step 1: Euclidean algorithm",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            MathTex(r"5 = 2 \cdot 2 + 1", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"2 = 1 \cdot 2 + 0 \;\Rightarrow\; \gcd = 1",
                    font_size=BODY_SIZE, color=WHITE),
        ]
        self.ly.progressive_reveal(items, start_from=eq)
        self.ly.clear()

        title2 = self.ly.title("Back-Substitution")
        items2 = [
            MathTex(r"1 = 5 - 2 \cdot 2",
                    font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"3 = 3(5 - 2 \cdot 2) = 15 - 6",
                    font_size=BODY_SIZE, color=SECONDARY),
            Text("One solution: x\u2080 = -1,  y\u2080 = 1",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.ly.clear()

    def scene5_general_solution(self):
        """Parameterize all solutions."""
        self.add_subcaption(
            "Once we have one particular solution x zero, y zero, we get "
            "all solutions by adding multiples of the homogeneous part. "
            "The general solution is x equals x zero plus b over d times t, "
            "y equals y zero minus a over d times t, where t is any integer "
            "and d is the greatest common divisor of a and b. For our "
            "example, x equals negative one plus five t, y equals one minus "
            "two t. Setting t to zero gives our original solution. "
            "Setting t to one gives x equals four, y equals negative one. "
            "Every integer t gives another valid solution.",
            duration=50,
        )
        self.ly.section_divider(4, "All Solutions")
        title = self.ly.title("General Solution")
        gen = MathTex(
            r"x = x_0 + \frac{b}{d}", r"\,t", r"\qquad",
            r"y = y_0 - \frac{a}{d}", r"\,t", r"\qquad t \in \mathbb{Z}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(gen, DOWN, anchor=title, buff=0.5)
        self.play(Write(gen), run_time=SLOW)
        self.wait(FAST)
        self.ly.clear()

        title2 = self.ly.title("Example Continued: 2x + 5y = 3")
        items = [
            MathTex(r"x = -1 + 5t", r"\qquad y = 1 - 2t",
                    font_size=HEADING_SIZE, color=SECONDARY),
            MathTex(r"t=0: (-1, 1) \quad t=1: (4, -1) \quad t=2: (9, -3)",
                    font_size=BODY_SIZE, color=PRIMARY),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.ly.clear()

    def scene6_pythagorean(self):
        """Pythagorean triples and Euclid's formula."""
        self.add_subcaption(
            "Perhaps the most famous Diophantine equation is x squared plus "
            "y squared equals z squared, the Pythagorean equation. We want "
            "all integer solutions. A Pythagorean triple is called primitive "
            "if x, y, and z share no common factor. Every primitive triple "
            "has the form x equals m squared minus n squared, y equals two m n, "
            "z equals m squared plus n squared, where m and n are coprime "
            "positive integers with different parity and m greater than n. "
            "For example, m equals two, n equals one gives three, four, "
            "five. Every triple is a multiple of a primitive one.",
            duration=58,
        )
        self.ly.section_divider(5, "Pythagorean Triples")
        title = self.ly.title("x^2 + y^2 = z^2")
        items = [
            Text("Pythagorean triple: integer (x,y,z) satisfying the equation",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Primitive: gcd(x,y,z) = 1",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        title2 = self.ly.title("Euclid's Formula (Primitive Triples)")
        formula = MathTex(
            r"x = m^2 - n^2", r",\quad",
            r"y = 2mn", r",\quad",
            r"z = m^2 + n^2",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(formula, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title2, buff=0.4)
        self.play(Write(formula), run_time=SLOW)
        self.wait(FAST)
        items2 = [
            Text("m, n coprime, opposite parity, m > n > 0",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=boxed)
        self.ly.clear()

        title3 = self.ly.title("Examples")
        items3 = [
            MathTex(r"m{=}2,\, n{=}1: \; (3, 4, 5)",
                    font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"m{=}3,\, n{=}2: \; (5, 12, 13)",
                    font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"m{=}4,\, n{=}1: \; (15, 8, 17)",
                    font_size=BODY_SIZE, color=SECONDARY),
        ]
        self.ly.progressive_reveal(items3, start_from=title3)
        self.ly.clear()

    def scene7_general_strategy(self):
        """Three general tools for Diophantine equations."""
        self.add_subcaption(
            "For more difficult Diophantine equations, we have three main "
            "tools. First, modular arithmetic can rule out solutions. For "
            "example, x squared plus y squared equals three has no integer "
            "solutions, because squares are zero or one mod four, so the "
            "sum can only be zero, one, or two mod four. Second, we try to "
            "find a parametric description of all solutions, like Euclid's "
            "formula for Pythagorean triples. Third, descent arguments: show "
            "that any solution leads to a smaller one, implying no "
            "nontrivial solution exists. These ideas connect to modern "
            "algebraic geometry, where the geometry of curves determines "
            "whether solutions exist.",
            duration=56,
        )
        self.ly.section_divider(6, "General Strategy")
        title = self.ly.title("Three Tools")
        items = [
            Text("1. Modular arithmetic: rule out impossible cases",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Parametric formulas: describe ALL solutions",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Descent: any solution implies a smaller one",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        title2 = self.ly.title("Modular Arithmetic Example")
        eq = MathTex(
            r"x^2 + y^2 = 3", r"\quad\text{?}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(FAST)
        items2 = [
            MathTex(r"n^2 \bmod 4 \in \{0, 1\}",
                    font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"x^2 + y^2 \bmod 4 \in \{0, 1, 2\} \neq 3",
                    font_size=BODY_SIZE, color=RED),
            Text("No integer solutions!",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=eq)
        self.ly.clear()

    def scene8_summary(self):
        """Summary and outro."""
        self.add_subcaption(
            "Let us recap what we have learned. Linear Diophantine equations "
            "a x plus b y equals c have integer solutions if and only if "
            "the greatest common divisor of a and b divides c. The extended "
            "Euclidean algorithm finds one solution, and we can parametrize "
            "all of them with a single free parameter. Pythagorean triples "
            "are completely classified by Euclid's formula. For harder "
            "equations, modular arithmetic, parametric methods, and descent "
            "arguments are our main tools. This concludes our number theory "
            "playlist. From divisibility and primes through modular "
            "arithmetic, quadratic reciprocity, and finally Diophantine "
            "equations, you now have the core toolkit of elementary "
            "number theory. Thank you for watching.",
            duration=52,
        )
        self.ly.section_divider(7, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("1. ax+by=c: solutions iff gcd(a,b)|c",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Extended Euclidean algorithm finds one solution",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Pythagorean triples: m^2-n^2, 2mn, m^2+n^2",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()
        play_outro(self, "Diophantine Equations", "Number Theory")
