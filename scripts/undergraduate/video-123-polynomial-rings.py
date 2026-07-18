"""
Video 123: Polynomial Rings
TEMPLATE v2 -- Professional quality Manim script

Playlist: Abstract Algebra I (Video 10 of 15)
Class: Video123_PolynomialRings

Topics: definition of R[x], polynomial operations (addition and multiplication),
         degree function, R[x] is a ring, properties inherited from R,
         R integral domain implies R[x] integral domain, units in F[x],
         irreducible polynomials, the evaluation homomorphism.

Quality Rules (mandatory):
1. Max 5 visible elements per scene at any time
2. Use LayoutEngine for ALL positioning -- no manual .shift() or .to_edge()
3. Progressive disclosure: add items one at a time
4. Each add_subcaption() duration = words / 2.5 seconds (12 words = 5s)
5. Call ly.clear() between scenes
6. Use consistent animation vocabulary from channel_branding.py
7. MathTex: raw strings with single backslashes
"""

from manim import *
import numpy as np
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits, clamp_position


class Video123_PolynomialRings(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_operations()
        self.scene4_ring_axioms()
        self.scene5_properties()
        self.scene6_units()
        self.scene7_irreducible()
        self.scene8_evaluation()
        self.scene9_summary()

    # --- Scene 1: Hook --- "The Ring Factory"
    # Narration ~30s.

    def scene1_hook(self):
        self.add_subcaption(
            "In the last video, we defined rings and saw several examples. "
            "The integers, modular arithmetic, matrices, and polynomials. "
            "Today we zoom in on one of the most important constructions "
            "in all of algebra: the polynomial ring. "
            "Given any ring R, we can build a brand new ring R of x, "
            "whose elements are polynomials with coefficients in R. "
            "This is Abstract Algebra, Video 10.",
            duration=30,
        )
        play_intro(self, "Polynomial Rings", "Abstract Algebra I")

        title = self.ly.title("The Ring Factory")
        self.wait(2)

        items = [
            Text("Take any ring R (Z, Q, R, Z_n, ...)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Adjoin an indeterminate x", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Get a new ring R[x] of polynomials", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(8)

        # Bridge from Video 122
        bridge = MathTex(
            r"R \;\xrightarrow{\text{adjoin } x}\; R[x]",
            color=WHITE, font_size=36,
        )
        boxed = self.ly.formula_box(bridge, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=items[-1], direction=DOWN, buff=0.4)
        self.play(Write(bridge), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: Definition of R[x] ---
    # Narration ~55s.

    def scene2_definition(self):
        self.add_subcaption(
            "Let R be a commutative ring with unity. "
            "The polynomial ring R of x is the set of all formal expressions "
            "a sub n x to the n plus a sub n minus one x to the n minus one "
            "plus dot dot dot plus a one x plus a zero, "
            "where each coefficient a sub i belongs to R, "
            "and a sub n is nonzero. "
            "The integer n is called the degree of the polynomial. "
            "The highest power of x with a nonzero coefficient "
            "determines the degree. "
            "The coefficient a sub n is the leading coefficient, "
            "and a sub zero is the constant term. "
            "We write deg of f to denote the degree of f. "
            "The zero polynomial is assigned degree minus infinity.",
            duration=55,
        )
        self.ly.section_divider("1", "Definition of R[x]")

        title = self.ly.title("Polynomial Ring R[x]")
        self.wait(1)

        # Formal definition
        defn = MathTex(
            r"R[x] = \{a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0\}",
            color=WHITE, font_size=32,
        )
        boxed = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.center_in_content(boxed)
        self.play(Write(defn), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        # Components
        self.ly.clear()

        title2 = self.ly.title("Key Components")
        self.wait(1)

        items = [
            Text("deg(f) = n (highest power with nonzero coeff.)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("a_n = leading coefficient", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("a_0 = constant term", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("deg(0) = -\\u221e (convention)", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2, run_time=0.8)
        self.wait(10)

        # Example
        self.ly.clear()

        title3 = self.ly.title("Example in Q[x]")
        self.wait(1)

        example = MathTex(
            r"f(x) = 3x^4 - 2x + 7, \quad g(x) = 5x^2 + x - 1",
            color=WHITE, font_size=30,
        )
        self.ly.safe_place(example, anchor=title3, direction=DOWN, buff=0.4)
        self.play(Write(example), run_time=NORMAL)
        self.wait(3)

        items2 = [
            Text("deg(f) = 4,  leading coeff = 3", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("deg(g) = 2,  leading coeff = 5", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=example, run_time=0.8)
        self.wait(6)

        self.ly.clear()

    # --- Scene 3: Polynomial Operations ---
    # Narration ~55s.

    def scene3_operations(self):
        self.add_subcaption(
            "Polynomials can be added and multiplied "
            "using the familiar rules from high school algebra. "
            "Addition is term by term. "
            "The degree of a sum satisfies "
            "deg of f plus g is at most the max of deg f and deg g. "
            "Equality holds unless the leading terms cancel. "
            "Multiplication uses the distributive law. "
            "Each term of f pairs with each term of g. "
            "When R is an integral domain, "
            "the degree of a product is exactly "
            "the sum of the degrees. "
            "This is because there are no zero divisors to cause cancellation.",
            duration=55,
        )
        self.ly.section_divider("2", "Polynomial Operations")

        title = self.ly.title("Addition")
        self.wait(1)

        add_ex = MathTex(
            r"(2x^3 + x + 1) + (3x^2 - x + 4) = 2x^3 + 3x^2 + 5",
            color=WHITE, font_size=28,
        )
        boxed = self.ly.formula_box(add_ex, color=SECONDARY)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.35)
        self.play(Write(add_ex), Create(boxed[1]), run_time=NORMAL)
        self.wait(3)

        deg_rule = MathTex(
            r"\deg(f + g) \leq \max(\deg f,\, \deg g)",
            color=ACCENT, font_size=30,
        )
        self.ly.safe_place(deg_rule, anchor=boxed, direction=DOWN, buff=0.4)
        self.play(Write(deg_rule), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

        # Multiplication
        title2 = self.ly.title("Multiplication")
        self.wait(1)

        mul_ex = MathTex(
            r"(x + 1)(x^2 - x + 1) = x^3 + 1",
            color=WHITE, font_size=30,
        )
        boxed2 = self.ly.formula_box(mul_ex, color=PRIMARY)
        self.ly.safe_place(boxed2, anchor=title2, direction=DOWN, buff=0.35)
        self.play(Write(mul_ex), Create(boxed2[1]), run_time=NORMAL)
        self.wait(3)

        # Steps of multiplication
        self.ly.clear()

        title3 = self.ly.title("Term-by-Term Distribution")
        self.wait(1)

        steps = [
            MathTex(r"x \cdot x^2 = x^3", color=PRIMARY, font_size=28),
            MathTex(r"x \cdot (-x) = -x^2", color=SECONDARY, font_size=28),
            MathTex(r"x \cdot 1 = x", color=ACCENT, font_size=28),
            MathTex(r"1 \cdot x^2 = x^2", color=SECONDARY, font_size=28),
            MathTex(r"1 \cdot (-x) = -x", color=ACCENT, font_size=28),
        ]
        self.ly.progressive_reveal(steps, start_from=title3, run_time=0.7)
        self.wait(6)

        # Degree formula
        self.ly.clear()

        title4 = self.ly.title("Degree of a Product")
        self.wait(1)

        deg_prod = MathTex(
            r"\text{If } R \text{ is an integral domain: } \deg(fg) = \deg f + \deg g",
            color=WHITE, font_size=28,
        )
        boxed4 = self.ly.formula_box(deg_prod, color=ACCENT)
        self.ly.center_in_content(boxed4)
        self.play(Write(deg_prod), Create(boxed4[1]), run_time=NORMAL)
        self.wait(3)

        reason = Text(
            "No zero divisors \\u21d2 leading terms cannot cancel",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(reason, anchor=boxed4, direction=DOWN, buff=0.4)
        self.play(FadeIn(reason, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # --- Scene 4: R[x] is a Ring ---
    # Narration ~40s.

    def scene4_ring_axioms(self):
        self.add_subcaption(
            "We now verify that R of x satisfies the ring axioms. "
            "Under addition, polynomials form an abelian group. "
            "The zero polynomial is the additive identity, "
            "and negating all coefficients gives the additive inverse. "
            "Multiplication is associative because "
            "it is associative in the coefficient ring R. "
            "The distributive laws hold because "
            "they hold for each coefficient individually. "
            "So R of x is indeed a ring, "
            "whenever R is. "
            "The ring factory works automatically.",
            duration=40,
        )

        title = self.ly.title("R[x] is a Ring")
        self.wait(1)

        items = [
            Text("(R[x], +) is an abelian group", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("  Zero polynomial = additive identity", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Multiplication is associative", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Distributive laws hold", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(10)

        # Key insight
        self.play(*[FadeOut(v) for v in items[:2]], run_time=FAST)

        insight = MathTex(
            r"R \text{ is a ring } \implies R[x] \text{ is a ring}",
            color=WHITE, font_size=32,
        )
        boxed = self.ly.formula_box(insight, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=items[-1], direction=DOWN, buff=0.4)
        self.play(Write(insight), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 5: Properties from R to R[x] ---
    # Narration ~50s.

    def scene5_properties(self):
        self.add_subcaption(
            "Important properties of the coefficient ring R "
            "carry over to the polynomial ring R of x. "
            "If R is commutative, then R of x is commutative. "
            "If R has a multiplicative identity one, "
            "then the constant polynomial one "
            "is the multiplicative identity in R of x. "
            "And the key theorem: "
            "if R is an integral domain, then R of x is an integral domain. "
            "The proof uses the degree formula. "
            "If f times g equals zero, "
            "then the degree of f times g is the sum of the degrees, "
            "which is finite. But the zero polynomial has degree minus infinity. "
            "This is a contradiction, so f times g cannot be zero "
            "unless f or g is zero. "
            "For example, the integers Z are an integral domain, "
            "so Z of x is also an integral domain.",
            duration=50,
        )
        self.ly.section_divider("3", "Inherited Properties")

        title = self.ly.title("Properties Transfer")
        self.wait(1)

        items = [
            Text("R commutative \\u21d2 R[x] commutative", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("R has unity 1 \\u21d2 R[x] has unity (constant 1)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("R integral domain \\u21d2 R[x] integral domain", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(8)

        # Theorem proof sketch
        self.ly.clear()

        title2 = self.ly.title("Theorem: ID \\u21d2 ID")
        self.wait(1)

        proof = MathTex(
            r"R \text{ integral domain } \implies R[x] \text{ integral domain}",
            color=WHITE, font_size=28,
        )
        boxed = self.ly.formula_box(proof, color=ACCENT)
        self.ly.safe_place(boxed, anchor=title2, direction=DOWN, buff=0.35)
        self.play(Write(proof), Create(boxed[1]), run_time=NORMAL)
        self.wait(3)

        steps = [
            Text("Proof: fg = 0 \\u21d2 deg(fg) = -\\u221e", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("But deg(fg) = deg(f) + deg(g) \\u2265 0 (finite)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Contradiction \\u21d2 f = 0 or g = 0", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(steps, start_from=boxed, run_time=0.8)
        self.wait(10)

        self.ly.clear()

    # --- Scene 6: Units in R[x] ---
    # Narration ~40s.

    def scene6_units(self):
        self.add_subcaption(
            "Which polynomials are units, "
            "that is, which have a multiplicative inverse? "
            "If F is a field, then the units of F of x "
            "are exactly the nonzero constant polynomials. "
            "This is because if deg f is greater than zero, "
            "then deg of f times g equals deg f plus deg g, "
            "which is greater than zero, "
            "so f times g cannot equal one. "
            "Over the integers, the situation is even more restrictive. "
            "The only units in Z of x are one and minus one. "
            "This is because the coefficients must stay in Z, "
            "and only one and minus one have integer inverses.",
            duration=40,
        )

        title = self.ly.title("Units in F[x]")
        self.wait(1)

        items = [
            Text("F a field \\u21d2 units of F[x] = nonzero constants", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("deg(fg) = deg(f) + deg(g) > 0 if deg f, deg g > 0", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("\\u21d2 fg \\u2260 1 (constant polynomial)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(10)

        self.ly.clear()

        # Z[x] case
        title2 = self.ly.title("Units in Z[x]")
        self.wait(1)

        items2 = [
            Text("Only units: +1 and -1", font_size=BODY_SIZE, color=RED, font=SANS),
            MathTex(r"R[x]^\times = R^\times \cap \text{constants}", color=WHITE, font_size=30),
        ]
        self.ly.progressive_reveal(items2, start_from=title2, run_time=0.8)
        self.wait(8)

        self.ly.clear()

    # --- Scene 7: Irreducible Polynomials ---
    # Narration ~55s.

    def scene7_irreducible(self):
        self.add_subcaption(
            "Just as prime numbers are the building blocks of the integers, "
            "irreducible polynomials are the building blocks of polynomial rings. "
            "A nonzero polynomial f that is not a unit "
            "is called irreducible if whenever f equals g times h, "
            "either g or h must be a unit. "
            "This is the exact polynomial analogue of primality. "
            "Over the field of rationals Q, "
            "the polynomial x squared minus 2 is irreducible. "
            "It has no rational roots. "
            "Over the reals, it factors as x minus root 2 times x plus root 2. "
            "Over the complex numbers, every nonconstant polynomial factors completely. "
            "A useful test: if f has degree 2 or 3 and is reducible, "
            "then f has a root. So for low degree, "
            "checking for roots tells you about irreducibility.",
            duration=55,
        )
        self.ly.section_divider("4", "Irreducibility")

        title = self.ly.title("Irreducible Polynomials")
        self.wait(1)

        defn = MathTex(
            r"f \text{ irreducible } \iff f = gh \implies g \text{ or } h \text{ is a unit}",
            color=WHITE, font_size=28,
        )
        boxed = self.ly.formula_box(defn, color=RED)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.35)
        self.play(Write(defn), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        analogy = Text(
            "Irreducible polynomials : polynomial rings = primes : integers",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(analogy, anchor=boxed, direction=DOWN, buff=0.4)
        self.play(FadeIn(analogy, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

        # Examples
        title2 = self.ly.title("Examples")
        self.wait(1)

        items = [
            MathTex(r"x^2 - 2 \text{ irreducible over } \mathbb{Q}", color=WHITE, font_size=28),
            MathTex(r"x^2 - 2 = (x - \sqrt{2})(x + \sqrt{2}) \text{ over } \mathbb{R}", color=SECONDARY, font_size=28),
            Text("Fundamental Theorem of Algebra:", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            MathTex(r"\text{Every nonconstant } f \in \mathbb{C}[x] \text{ factors completely}", color=WHITE, font_size=28),
        ]
        self.ly.progressive_reveal(items, start_from=title2, run_time=0.8)
        self.wait(10)

        self.ly.clear()

        # Degree 2-3 test
        title3 = self.ly.title("Irreducibility Test (deg 2, 3)")
        self.wait(1)

        test = MathTex(
            r"\deg f \in \{2, 3\}: \quad f \text{ reducible } \iff f \text{ has a root in } F",
            color=WHITE, font_size=28,
        )
        boxed3 = self.ly.formula_box(test, color=ACCENT)
        self.ly.center_in_content(boxed3)
        self.play(Write(test), Create(boxed3[1]), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 8: The Evaluation Homomorphism ---
    # Narration ~45s.

    def scene8_evaluation(self):
        self.add_subcaption(
            "There is a deep connection between polynomial algebra "
            "and substitution. Given an element a in the ring R, "
            "we define the evaluation map ev sub a "
            "from R of x to R by ev sub a of f equals f of a. "
            "This means plug a into the polynomial for x. "
            "The evaluation map is a ring homomorphism. "
            "It preserves addition and multiplication. "
            "An important consequence is the remainder theorem. "
            "When we divide f by x minus a, "
            "the remainder is exactly f of a. "
            "In particular, a is a root of f "
            "if and only if x minus a divides f. "
            "This links the algebraic notion of divisibility "
            "to the analytic notion of evaluating at a point.",
            duration=45,
        )
        self.ly.section_divider("5", "Evaluation Homomorphism")

        title = self.ly.title("The Evaluation Map")
        self.wait(1)

        ev_def = MathTex(
            r"\text{ev}_a : R[x] \to R, \quad \text{ev}_a(f) = f(a)",
            color=WHITE, font_size=32,
        )
        boxed = self.ly.formula_box(ev_def, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.35)
        self.play(Write(ev_def), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        items = [
            Text("ev_a is a ring homomorphism", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("ev_a(f + g) = f(a) + g(a)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("ev_a(fg) = f(a) \\u00b7 g(a)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed, run_time=0.8)
        self.wait(8)

        self.ly.clear()

        # Remainder theorem
        title2 = self.ly.title("Remainder Theorem")
        self.wait(1)

        theorem = MathTex(
            r"f(x) = q(x)(x - a) + r, \quad r = f(a)",
            color=WHITE, font_size=30,
        )
        boxed2 = self.ly.formula_box(theorem, color=ACCENT)
        self.ly.center_in_content(boxed2)
        self.play(Write(theorem), Create(boxed2[1]), run_time=NORMAL)
        self.wait(4)

        corollary = MathTex(
            r"f(a) = 0 \iff (x - a) \mid f(x)",
            color=WHITE, font_size=30,
        )
        boxed3 = self.ly.formula_box(corollary, color=RED)
        self.ly.safe_place(boxed3, anchor=boxed2, direction=DOWN, buff=0.4)
        self.play(Write(corollary), Create(boxed3[1]), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 9: Summary ---
    # Narration ~30s.

    def scene9_summary(self):
        self.add_subcaption(
            "Let us summarize what we learned about polynomial rings. "
            "Given any ring R, the polynomial ring R of x "
            "is the ring of formal polynomials with coefficients in R. "
            "Key properties of R carry over to R of x. "
            "If R is an integral domain, so is R of x. "
            "The units of F of x are the nonzero constants when F is a field. "
            "Irreducible polynomials are the building blocks, "
            "analogous to prime numbers. "
            "And the evaluation homomorphism links algebra to substitution. "
            "In the next video, we will study ideals. "
            "Thank you for watching.",
            duration=30,
        )

        title = self.ly.title("Summary")
        self.wait(1)

        items = [
            Text("R[x] = polynomials with coefficients in R", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("R ID \\u21d2 R[x] ID; deg(fg) = deg(f) + deg(g)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Units of F[x] = nonzero constants", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Irreducible = polynomial analogue of prime", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("ev_a: R[x] \\u2192 R is a ring homomorphism", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(10)

        self.ly.clear()

        # Teaser
        teaser = Text(
            "Next: Ideals and Quotient Rings",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.center_in_content(teaser)
        self.play(FadeIn(teaser, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()
        play_outro(self)
