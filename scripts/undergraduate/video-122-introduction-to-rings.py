"""
Video 122: Introduction to Rings and Fields
TEMPLATE v2 -- Professional quality Manim script

Playlist: Abstract Algebra I (Video 12 of 12)
Class: Video122_IntroductionToRings

Topics: definition of a ring, ring axioms, examples (Z, Z_n, matrices,
         polynomials), commutative rings, rings with unity, integral
         domains, zero divisors, fields, field examples (Q, R, C, Z_p),
         ring taxonomy hierarchy.

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


class Video122_IntroductionToRings(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_ring_axioms()
        self.scene3_examples_z()
        self.scene4_examples_matrices_polynomials()
        self.scene5_special_types()
        self.scene6_integral_domains()
        self.scene7_fields()
        self.scene8_summary()

    # --- Scene 1: Hook --- "Beyond Groups"
    # Narration ~35s.

    def scene1_hook(self):
        self.add_subcaption(
            "In our study of group theory, we focused on a single operation. "
            "Addition in the integers, composition of permutations, "
            "multiplication of invertible matrices. "
            "But many important algebraic structures have two operations. "
            "The integers have addition and multiplication. "
            "Polynomials can be added and multiplied. "
            "Matrices can be added and multiplied. "
            "A ring is the algebraic structure that captures "
            "the interplay between two operations. "
            "Today we define rings, explore examples, "
            "and build up to the concept of a field. "
            "This is Abstract Algebra, Video 12.",
            duration=35,
        )
        play_intro(self, "Introduction to Rings and Fields", "Abstract Algebra I")

        title = self.ly.title("Beyond Groups")
        self.wait(2)

        items = [
            Text("Groups: ONE operation (+ or \u00b7)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Rings: TWO operations (+ and \u00b7)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Where do we see both? Z, polynomials, matrices", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(8)

        # Bridge from groups
        bridge = MathTex(
            r"(R, +) \text{ is a group} \quad + \quad \text{multiplication } \cdot",
            color=WHITE, font_size=30,
        )
        boxed = self.ly.formula_box(bridge, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=items[-1], direction=DOWN, buff=0.35)
        self.play(Write(bridge), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: The Ring Axioms ---
    # Narration ~50s.

    def scene2_ring_axioms(self):
        self.add_subcaption(
            "A ring is a set R together with two binary operations, "
            "called addition and multiplication, satisfying three conditions. "
            "First, R is an abelian group under addition. "
            "This means addition is associative, commutative, "
            "there is an additive identity zero, "
            "and every element has an additive inverse. "
            "Second, multiplication is associative. "
            "Third, multiplication distributes over addition "
            "from both the left and the right. "
            "That is, a times the sum of b and c "
            "equals a b plus a c, "
            "and the sum of a and b times c "
            "equals a c plus b c. "
            "Notice that we do NOT require multiplication to be commutative, "
            "and we do NOT require a multiplicative identity. "
            "These are optional extra properties.",
            duration=50,
        )
        self.ly.section_divider("1", "Definition of a Ring")

        title = self.ly.title("Ring Axioms")
        self.wait(1)

        # Definition box
        defn = MathTex(
            r"\text{A ring } (R, +, \cdot) \text{ satisfies:}",
            color=WHITE, font_size=30,
        )
        self.ly.center_in_content(defn)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(4)

        # Three conditions (progressive reveal)
        self.ly.clear()

        title2 = self.ly.title("Three Conditions")
        self.wait(1)

        items = [
            Text("1. (R, +) is an abelian group", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("2. Multiplication is associative", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("3. Distributive: a(b+c) = ab + ac", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("   and (a+b)c = ac + bc", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2, run_time=0.8)
        self.wait(8)

        # Important note — fade items first
        self.play(*[FadeOut(v) for v in [items[0], items[1]]], run_time=FAST)

        note = Text(
            "NOT required: commutativity of \u00b7, multiplicative identity",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(note, anchor=items[-1], direction=DOWN, buff=0.35)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 3: The First Examples ---
    # Narration ~45s.

    def scene3_examples_z(self):
        self.add_subcaption(
            "Let us verify that the integers form a ring. "
            "Under addition, the integers are an abelian group. "
            "Addition is associative and commutative, "
            "zero is the identity, and every integer n "
            "has additive inverse minus n. "
            "Multiplication is associative. "
            "And the distributive law holds because "
            "a times the sum of b and c "
            "equals a b plus a c for all integers. "
            "So the integers Z are a ring. "
            "Similarly, Z subscript n, the integers modulo n, "
            "form a ring under modular addition and multiplication. "
            "For example, Z subscript 6 is a ring. "
            "The key point is that every ring contains "
            "an abelian group hiding inside it, under addition.",
            duration=45,
        )

        title = self.ly.title("Example: The Integers")
        self.wait(1)

        # Z is a ring
        items = [
            Text(r"$(\mathbb{Z}, +)$ is an abelian group \u2713", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text(r"Multiplication is associative \u2713", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text(r"Distributive law holds \u2713", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text(r"$\therefore (\mathbb{Z}, +, \times)$ is a ring!", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(8)

        self.ly.clear()

        # Z_n
        title2 = self.ly.title("Example: Modular Arithmetic")
        self.wait(1)

        zn = MathTex(
            r"\mathbb{Z}_n = \{0, 1, 2, \ldots, n-1\}",
            color=WHITE, font_size=34,
        )
        boxed = self.ly.formula_box(zn, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=title2, direction=DOWN, buff=0.4)
        self.play(Write(zn), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        items2 = [
            Text(r"$\mathbb{Z}_6$: addition mod 6, multiplication mod 6", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Every ring has an abelian group under +", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=boxed, run_time=0.8)
        self.wait(6)

        self.ly.clear()

    # --- Scene 4: Matrices and Polynomials ---
    # Narration ~45s.

    def scene4_examples_matrices_polynomials(self):
        self.add_subcaption(
            "Not all rings are commutative. "
            "The set of n by n matrices with real entries "
            "forms a ring under matrix addition and multiplication. "
            "Addition makes them an abelian group. "
            "Matrix multiplication is associative. "
            "And multiplication distributes over addition. "
            "But for n greater than or equal to 2, "
            "matrix multiplication is not commutative. "
            "For example, with specific two by two matrices A and B, "
            "we can have A B not equal to B A. "
            "On the other hand, the ring of polynomials "
            "with real coefficients is commutative. "
            "Polynomials can be added term by term "
            "and multiplied by distributing. "
            "Both are important examples of rings "
            "that go beyond the integers.",
            duration=45,
        )

        title = self.ly.title("Example: Matrices")
        self.wait(1)

        mat_def = MathTex(
            r"M_n(\mathbb{R}) = \{n \times n \text{ matrices with real entries}\}",
            color=WHITE, font_size=30,
        )
        self.ly.safe_place(mat_def, anchor=title, direction=DOWN, buff=0.35)
        self.play(Write(mat_def), run_time=NORMAL)
        self.wait(3)

        items = [
            Text("Ring under + and matrix multiplication", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("NOT commutative (for n \u2265 2)", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        visible = self.ly.progressive_reveal(items, start_from=mat_def, run_time=0.8)
        self.wait(5)

        # Counterexample formula
        self.play(*[FadeOut(v) for v in visible if v is not None], run_time=FAST)
        counter = MathTex(
            r"\text{E.g. } AB \neq BA \text{ for specific } A, B \in M_2(\mathbb{R})",
            color=RED, font_size=28,
        )
        self.ly.safe_place(counter, anchor=mat_def, direction=DOWN, buff=0.5)
        self.play(Write(counter), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Polynomials
        title2 = self.ly.title("Example: Polynomials")
        self.wait(1)

        poly_def = MathTex(
            r"\mathbb{R}[x] = \{a_n x^n + \cdots + a_1 x + a_0\}",
            color=WHITE, font_size=34,
        )
        boxed = self.ly.formula_box(poly_def, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=title2, direction=DOWN, buff=0.4)
        self.play(Write(poly_def), Create(boxed[1]), run_time=NORMAL)
        self.wait(3)

        poly_note = Text(
            "Commutative ring under + and polynomial multiplication",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(poly_note, anchor=boxed, direction=DOWN, buff=0.35)
        self.play(FadeIn(poly_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # --- Scene 5: Special Types of Rings ---
    # Narration ~50s.

    def scene5_special_types(self):
        self.add_subcaption(
            "Not all rings are created equal. "
            "We can classify rings by adding extra properties. "
            "A commutative ring is a ring where "
            "multiplication commutes, that is, a b equals b a for all elements. "
            "A ring with unity has a multiplicative identity element one, "
            "such that one times a equals a for every element a. "
            "An integral domain is a commutative ring with unity "
            "that has no zero divisors. "
            "A zero divisor is a nonzero element a "
            "such that a times b equals zero for some nonzero b. "
            "And a field is a commutative ring with unity "
            "where every nonzero element has a multiplicative inverse. "
            "These form a hierarchy: "
            "every field is an integral domain, "
            "every integral domain is a commutative ring with unity, "
            "and every commutative ring with unity is a ring.",
            duration=50,
        )
        self.ly.section_divider("2", "Ring Taxonomy")

        title = self.ly.title("Types of Rings")
        self.wait(1)

        # Hierarchy as progressive reveal
        items = [
            Text("Ring (basic axioms)", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Commutative ring (ab = ba)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Ring with unity (1 \u00b7 a = a)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Integral domain (no zero divisors)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Field (every nonzero has inverse)", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(8)

        self.ly.clear()

        # Arrow summary
        title2 = self.ly.title("The Hierarchy")
        self.wait(1)

        hierarchy = MathTex(
            r"\text{Ring} \supset \text{Comm. Ring} \supset \text{Int. Domain} \supset \text{Field}",
            color=WHITE, font_size=30,
        )
        boxed = self.ly.formula_box(hierarchy, color=PRIMARY)
        self.ly.center_in_content(boxed)
        self.play(Write(hierarchy), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        note = Text(
            "Each step adds one more property",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, anchor=boxed, direction=DOWN, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # --- Scene 6: Integral Domains ---
    # Narration ~50s.

    def scene6_integral_domains(self):
        self.add_subcaption(
            "Let us focus on zero divisors and integral domains. "
            "In the ring Z subscript 6, "
            "the elements 2 and 3 are both nonzero, "
            "but their product is 0 modulo 6. "
            "These are called zero divisors. "
            "An integral domain is a commutative ring with unity "
            "that has no zero divisors. "
            "The integers Z form an integral domain "
            "because if a times b equals zero in Z, "
            "then either a or b must be zero. "
            "A key consequence of having no zero divisors "
            "is the cancellation law. "
            "If a b equals a c and a is nonzero, "
            "then b must equal c. "
            "This fails in Z subscript 6: "
            "2 times 3 equals 2 times 0, "
            "but 3 does not equal 0.",
            duration=50,
        )

        title = self.ly.title("Zero Divisors")
        self.wait(1)

        # Z_6 example
        items = [
            MathTex(r"\mathbb{Z}_6:\; 2 \neq 0,\; 3 \neq 0", color=WHITE, font_size=30),
            MathTex(r"\text{but } 2 \times 3 = 6 \equiv 0 \pmod{6}", color=RED, font_size=30),
            Text(r"$\therefore$ Z_6 has zero divisors", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(8)

        self.ly.clear()

        # Integral domain definition
        title2 = self.ly.title("Integral Domain")
        self.wait(1)

        defn = MathTex(
            r"\text{Integral Domain} = \text{Comm. Ring w/ Unity} + \text{No Zero Divisors}",
            color=WHITE, font_size=28,
        )
        boxed = self.ly.formula_box(defn, color=ACCENT)
        self.ly.safe_place(boxed, anchor=title2, direction=DOWN, buff=0.35)
        self.play(Write(defn), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        items2 = [
            Text(r"$\mathbb{Z}$ is an integral domain", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Cancellation law: ab = ac, a \u2260 0 \u21d2 b = c", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=boxed, run_time=0.8)
        self.wait(6)

        self.ly.clear()

    # --- Scene 7: Fields ---
    # Narration ~50s.

    def scene7_fields(self):
        self.add_subcaption(
            "A field is the richest kind of ring. "
            "Formally, a field is a commutative ring with unity "
            "where every nonzero element has a multiplicative inverse. "
            "That is, for every nonzero a, "
            "there exists a to the minus one such that "
            "a times a to the minus one equals one. "
            "The rational numbers Q form a field. "
            "The real numbers R form a field. "
            "The complex numbers C form a field. "
            "And for any prime p, "
            "Z subscript p is a field under modular arithmetic. "
            "This is because finite integral domains are always fields. "
            "The integers Z are NOT a field, "
            "because 2 has no multiplicative inverse in Z. "
            "Fields are the algebraic structure "
            "that best captures the arithmetic we are used to.",
            duration=50,
        )
        self.ly.section_divider("3", "Fields")

        title = self.ly.title("Field Definition")
        self.wait(1)

        defn = MathTex(
            r"\text{Field: comm. ring w/ unity, } \forall\, a \neq 0,\; \exists\, a^{-1}: a \cdot a^{-1} = 1",
            color=WHITE, font_size=28,
        )
        boxed = self.ly.formula_box(defn, color=RED)
        self.ly.center_in_content(boxed)
        self.play(Write(defn), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

        # Examples
        title2 = self.ly.title("Field Examples")
        self.wait(1)

        left_items = [
            Text(r"$\mathbb{Q}$ (rationals)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text(r"$\mathbb{R}$ (reals)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        right_items = [
            Text(r"$\mathbb{C}$ (complex)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text(r"$\mathbb{Z}_p$ (p prime)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        left_col, right_col = self.ly.two_columns(left_items, right_items, start_from=title2)
        self.play(FadeIn(left_col[0], shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(left_col[1], shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(right_col[0], shift=RIGHT * 0.15), run_time=FAST)
        self.play(FadeIn(right_col[1], shift=RIGHT * 0.15), run_time=FAST)
        self.wait(4)

        # Non-examples — fade columns first
        self.play(
            *[FadeOut(left_col[i]) for i in range(len(left_col))],
            *[FadeOut(right_col[i]) for i in range(len(right_col))],
            run_time=FAST,
        )
        non_ex = Text(
            r"NOT fields: $\mathbb{Z}$ (no inverses), $\mathbb{Z}_6$ (zero divisors)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(non_ex, anchor=title2, direction=DOWN, buff=0.5)
        self.play(FadeIn(non_ex, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # --- Scene 8: Summary ---
    # Narration ~35s.

    def scene8_summary(self):
        self.add_subcaption(
            "Let us summarize what we learned today. "
            "A ring is a set with two operations, "
            "addition and multiplication, "
            "where addition forms an abelian group, "
            "multiplication is associative, "
            "and multiplication distributes over addition. "
            "Important examples include the integers, "
            "modular arithmetic, matrices, and polynomials. "
            "We classified rings into a hierarchy: "
            "commutative rings, rings with unity, "
            "integral domains, and fields. "
            "Fields are the most structured rings, "
            "capturing the familiar arithmetic of Q, R, and C. "
            "In future videos, we will explore polynomial rings, "
            "ideals, and quotient rings in depth. "
            "This completes our introduction to abstract algebra. "
            "Thank you for watching.",
            duration=35,
        )

        title = self.ly.title("Summary")
        self.wait(1)

        items = [
            Text("Ring: (R,+) abelian group + assoc. mult. + distributivity", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Examples: Z, Z_n, M_n(R), R[x]", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Hierarchy: Ring \u2192 Comm. \u2192 Int. Domain \u2192 Field", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Fields: Q, R, C, Z_p (p prime)", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(8)

        # Closing note
        self.ly.clear()

        closing = Text(
            "This completes Abstract Algebra I. Thank you for watching!",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.center_in_content(closing)
        self.play(FadeIn(closing, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()
        play_outro(self)
