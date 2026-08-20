"""
Video 221: Splitting Fields — Advanced Abstract Algebra
Splitting field definition, existence, uniqueness up to isomorphism,
degree of splitting field, examples (x^2-2, x^3-2 over Q).

QUALITY RULES:
1. Max 5 visible elements per scene
2. LayoutEngine for ALL positioning
3. Progressive disclosure
4. Raw strings with single backslashes for LaTeX
5. ly.clear() between scenes
6. One subcaption per scene, self.wait(5-8) after content

Competitive analysis: Borcherds (33K, tablet lecture, rigorous),
Nicholson (14K, whiteboard), Glesser (23K, whiteboard example-focused).
Mathemaniac/Aleph 0 use splitting fields but never define them.
Our approach: animated definition, existence construction as field tree,
uniqueness teaser, color-coded root factorization, tower diagrams.
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


class Video221_SplittingFields(Scene):
    """Splitting Fields: where polynomials break apart completely."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_existence()
        self.scene4_uniqueness()
        self.scene5_example_x2_2()
        self.scene6_example_x3_2()
        self.scene7_degree_bounds()
        self.scene8_summary()

    def scene1_hook(self):
        """Hook — where do the missing roots live?"""
        self.add_subcaption(
            "Consider x squared minus 2. Over the rational numbers, "
            "this polynomial has no root at all. Over the reals, it has "
            "square root of 2 and negative square root of 2. For x cubed "
            "minus 2, the situation is even more dramatic: we need the "
            "real cube root of 2 plus two complex cube roots. The splitting "
            "field is the answer to a natural question: what is the smallest "
            "field that contains all the roots of a polynomial?",
            duration=30,
        )
        play_intro(self, "Splitting Fields", "Advanced Abstract Algebra")

        title = self.ly.title("Where Do the Missing Roots Live?")
        items = [
            MathTex(r"x^2 - 2 = 0", font_size=BODY_SIZE, color=PRIMARY),
            Text("Over Q: no roots. Over R: sqrt(2) and -sqrt(2)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("The splitting field contains ALL roots",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(7)
        self.ly.clear()

    def scene2_definition(self):
        """Formal definition of splitting field."""
        self.add_subcaption(
            "Let f of x be a polynomial with coefficients in a field K. "
            "We say f splits completely over an extension E if f of x "
            "equals a constant times the product of x minus r sub i for "
            "all roots r sub i, where every r sub i lies in E. The "
            "splitting field of f over K is the smallest extension E of K "
            "where f splits completely. Equivalently, it is the field K "
            "adjoined with all the roots: K of r 1 through r sub n.",
            duration=34,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("Splitting Field")

        # f splits over E
        splits = MathTex(
            r"f(x) = c\,(x - r_1)(x - r_2) \cdots (x - r_n)",
            r"\text{ with each } r_i \in E",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        boxed_splits = self.ly.formula_box(splits, color=PRIMARY)
        self.ly.safe_place(boxed_splits, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_splits), run_time=NORMAL)
        self.wait(3)

        # Splitting field definition
        defn = MathTex(
            r"\text{Split}(f, K) = K(r_1, r_2, \ldots, r_n)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed_def = self.ly.formula_box(defn, color=SECONDARY)
        self.ly.safe_place(boxed_def, DOWN, anchor=boxed_splits, buff=0.5)
        self.play(FadeIn(boxed_def), run_time=NORMAL)
        self.wait(3)

        # Key remark
        remark = Text(
            "Smallest extension of K where f factors into linears",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(remark, DOWN, anchor=boxed_def, buff=0.4)
        self.play(FadeIn(remark, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene3_existence(self):
        """Every polynomial has a splitting field."""
        self.add_subcaption(
            "Does every polynomial have a splitting field? Yes. Here is "
            "the construction idea. Start with K and f of x. Pick an "
            "irreducible factor g of f, and adjoin a root alpha using "
            "the quotient ring K of x modulo g of x. Now f has one more "
            "linear factor over K of alpha. Repeat this process. Since "
            "f has finite degree, the process terminates. The result is "
            "a field where f splits completely.",
            duration=32,
        )
        self.ly.section_divider(2, "Existence")

        title = self.ly.title("Every Polynomial Has One")

        # Theorem
        thm = Text(
            "For any f in K[x], a splitting field exists.",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(thm, DOWN, anchor=title, buff=0.5)
        self.play(Write(thm), run_time=NORMAL)
        self.wait(3)

        # Construction steps
        self.play(FadeOut(thm), run_time=FAST)
        steps = [
            Text("1. Pick irreducible factor g(x) of f(x)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("2. Adjoin root: K -> K[x]/(g(x))",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Repeat until f splits completely",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(steps, start_from=title)
        self.wait(3)

        # Termination
        term = Text(
            "Terminates because deg(f) is finite!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(term, DOWN, anchor=steps[-1], buff=0.4)
        self.play(FadeIn(term, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene4_uniqueness(self):
        """Splitting fields are unique up to isomorphism."""
        self.add_subcaption(
            "A crucial fact: any two splitting fields of the same "
            "polynomial over K are isomorphic. The proof extends "
            "isomorphisms one root at a time using the isomorphism "
            "extension theorem. This matters because the Galois group, "
            "defined as the automorphisms of the splitting field that "
            "fix K, is well-defined regardless of which splitting field "
            "we choose.",
            duration=26,
        )
        self.ly.section_divider(3, "Uniqueness")

        title = self.ly.title("Unique Up to Isomorphism")

        # Statement
        thm = MathTex(
            r"E_1, E_2 \text{ splitting fields of } f \text{ over } K",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(thm, DOWN, anchor=title, buff=0.5)
        self.play(Write(thm), run_time=NORMAL)
        self.wait(2)

        arrow = MathTex(
            r"\Rightarrow E_1 \cong_K E_2",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(arrow, DOWN, anchor=thm, buff=0.5)
        self.play(Write(arrow), run_time=NORMAL)
        self.wait(3)

        # Why it matters
        self.play(FadeOut(thm), FadeOut(arrow), run_time=FAST)
        why = Text(
            "Why it matters: Gal(f/K) = Aut_K(Split(f)) is well-defined",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(why, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(why, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        proof_idea = Text(
            "Proof: extend isomorphisms one root at a time",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(proof_idea, DOWN, anchor=why, buff=0.4)
        self.play(FadeIn(proof_idea, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene5_example_x2_2(self):
        """Example 1: x^2 - 2 over Q."""
        self.add_subcaption(
            "Let us compute the splitting field of x squared minus 2 over "
            "the rationals. By Eisenstein with p equals 2, this polynomial "
            "is irreducible over Q. Adjoining square root of 2 gives us "
            "Q of square root of 2. Since the other root is just negative "
            "square root of 2, which also lives in this field, the "
            "splitting field is simply Q of square root of 2, with degree "
            "2 over Q.",
            duration=30,
        )
        self.ly.section_divider(4, "Example: x^2 - 2")

        title = self.ly.title("x^2 - 2 over Q")

        # Polynomial
        poly = MathTex(
            r"f(x) = x^2 - 2, \quad \text{irreducible (Eisenstein, } p = 2\text{)}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(poly, DOWN, anchor=title, buff=0.5)
        self.play(Write(poly), run_time=NORMAL)
        self.wait(3)

        # Roots
        self.play(FadeOut(poly), run_time=FAST)
        roots = MathTex(
            r"r_1 = \sqrt{2}, \quad r_2 = -\sqrt{2}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(roots, DOWN, anchor=title, buff=0.5)
        self.play(Write(roots), run_time=NORMAL)
        self.wait(3)

        # Splitting field and degree
        self.play(FadeOut(roots), run_time=FAST)
        result = MathTex(
            r"\text{Split}(f, \mathbb{Q}) = \mathbb{Q}(\sqrt{2})"
            r", \quad [\mathbb{Q}(\sqrt{2}) : \mathbb{Q}] = 2",
            font_size=BODY_SIZE, color=ACCENT,
        )
        boxed_result = self.ly.formula_box(result, color=ACCENT)
        self.ly.safe_place(boxed_result, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_result), run_time=NORMAL)
        self.wait(3)

        # Tower
        tower = MathTex(
            r"\mathbb{Q} \subset \mathbb{Q}(\sqrt{2})",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(tower, DOWN, anchor=boxed_result, buff=0.4)
        self.play(Write(tower), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene6_example_x3_2(self):
        """Example 2: x^3 - 2 over Q — degree 6 splitting field."""
        self.add_subcaption(
            "Now the more interesting case: x cubed minus 2 over Q. The "
            "three roots are the real cube root of 2, omega times cube root "
            "of 2, and omega squared times cube root of 2, where omega is "
            "a primitive cube root of unity. First adjoin the real cube root "
            "of 2. By Eisenstein, the minimal polynomial is x cubed minus "
            "2, so the degree is 3. But omega, which equals e to the 2 pi "
            "i over 3, does not live in Q of cube root of 2. We must "
            "adjoin it, adding another degree 2. The splitting field has "
            "total degree 3 times 2 equals 6.",
            duration=44,
        )
        self.ly.section_divider(5, "Example: x^3 - 2")

        title = self.ly.title("x^3 - 2 over Q")

        # Roots
        roots = MathTex(
            r"r_1 = \sqrt[3]{2}"
            r", \quad r_2 = \omega\sqrt[3]{2}"
            r", \quad r_3 = \omega^2\sqrt[3]{2}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(roots, DOWN, anchor=title, buff=0.5)
        self.play(Write(roots), run_time=NORMAL)
        self.wait(3)

        # omega definition
        omega_def = MathTex(
            r"\omega = e^{2\pi i / 3} = -\frac{1}{2} + \frac{\sqrt{3}}{2}\,i",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(omega_def, DOWN, anchor=roots, buff=0.4)
        self.play(Write(omega_def), run_time=NORMAL)
        self.wait(3)

        # Step 1: adjoin cube root
        self.play(FadeOut(roots), FadeOut(omega_def), run_time=FAST)
        step1 = MathTex(
            r"\mathbb{Q}(\sqrt[3]{2}) / \mathbb{Q}"
            r": [\mathbb{Q}(\sqrt[3]{2}) : \mathbb{Q}] = 3",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step1, DOWN, anchor=title, buff=0.5)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(3)

        # Step 2: adjoin omega
        step2 = MathTex(
            r"\omega \notin \mathbb{Q}(\sqrt[3]{2}) \Rightarrow"
            r"\text{ adjoin } \omega: \text{ degree } 2",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(step2, DOWN, anchor=step1, buff=0.4)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(3)

        # Final result
        self.play(FadeOut(step1), FadeOut(step2), run_time=FAST)
        result = MathTex(
            r"\text{Split}(x^3 - 2, \mathbb{Q}) = "
            r"\mathbb{Q}(\sqrt[3]{2},\, \omega)"
            r", \quad [\text{Split} : \mathbb{Q}] = 3 \times 2 = 6",
            font_size=BODY_SIZE, color=ACCENT,
        )
        boxed_result = self.ly.formula_box(result, color=ACCENT)
        self.ly.safe_place(boxed_result, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_result), run_time=NORMAL)
        self.wait(3)

        # Tower
        tower = MathTex(
            r"\mathbb{Q} \subset \mathbb{Q}(\sqrt[3]{2}) "
            r"\subset \mathbb{Q}(\sqrt[3]{2}, \omega)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(tower, DOWN, anchor=boxed_result, buff=0.4)
        self.play(Write(tower), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene7_degree_bounds(self):
        """Degree of splitting field divides n!"""
        self.add_subcaption(
            "How large can a splitting field be? If f has degree n, then "
            "the splitting field over K has degree dividing n factorial. "
            "The reason is that at each step we adjoin one root, and the "
            "degree of the new root over the current field is at most the "
            "number of remaining factors, which decreases each time. For "
            "x cubed minus 2, the degree is 6, which divides 3 factorial "
            "equals 6. This bound means the Galois group of f over K "
            "is a subgroup of the symmetric group S sub n.",
            duration=34,
        )
        self.ly.section_divider(6, "Degree Bounds")

        title = self.ly.title("How Large Can It Be?")

        # Theorem
        thm = MathTex(
            r"[\text{Split}(f, K) : K] \mid n!, \text{ where } n = \deg(f)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_thm = self.ly.formula_box(thm, color=PRIMARY)
        self.ly.safe_place(boxed_thm, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_thm), run_time=NORMAL)
        self.wait(3)

        # Check with example
        check = MathTex(
            r"x^3 - 2: \quad [\text{Split} : \mathbb{Q}] = 6 \mid 3! = 6 \; \checkmark",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(check, DOWN, anchor=boxed_thm, buff=0.5)
        self.play(Write(check), run_time=NORMAL)
        self.wait(3)

        # Connection to Galois group
        self.play(FadeOut(check), run_time=FAST)
        galois = MathTex(
            r"\text{Gal}(f/K) = \text{Aut}_K(\text{Split}(f))"
            r"\leq S_n",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(galois, DOWN, anchor=boxed_thm, buff=0.5)
        self.play(Write(galois), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene8_summary(self):
        """Summary and outro."""
        self.add_subcaption(
            "Let us summarize. A splitting field is the smallest "
            "extension of K where a polynomial splits into linear factors. "
            "Every polynomial has one, and any two are isomorphic. The "
            "degree divides n factorial and can be computed using the "
            "tower law. In the next video we will define the Galois group "
            "as the automorphisms of the splitting field that fix the "
            "base field. This is where the real power of field theory "
            "emerges. Thank you for watching!",
            duration=34,
        )
        self.ly.section_divider(7, "Summary")

        title = self.ly.title("Key Takeaways")
        items = [
            Text("Splitting field: smallest E/K where f splits completely",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Exists for every polynomial; unique up to isomorphism",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Degree divides n!; computed via tower law",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3)

        extra = Text(
            "Gal(f/K) = Aut_K(Split(f)) <= S_n (next video!)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.progressive_reveal([extra], start_from=items[-1])
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "Thank you for watching! Next time we study Galois groups.",
            duration=8,
        )
        play_outro(self, "Galois Groups", "Advanced Abstract Algebra")
