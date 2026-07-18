"""
Video 125: Quotient Rings — Animated Abstract Algebra
TEMPLATE v2 -- Professional quality Manim script

Playlist: Abstract Algebra I (Video 15 of 15)
Class: Video125_QuotientRings

Topics: motivation from modular arithmetic, construction of R/I from ideals,
         coset operations, well-definedness, examples Z/6Z and F_4,
         first isomorphism theorem for rings, correspondence theorem,
         comparison with quotient groups.

Based on competitive analysis: first animated explanation of quotient rings on YouTube.
Color coding: PRIMARY=ring R elements, SECONDARY=ideal I elements,
              ACCENT=coset representatives/highlights, RED=zero divisors.

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


class Video125_QuotientRings(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_recap()
        self.scene3_construction()
        self.scene4_example_z6()
        self.scene5_example_f4()
        self.scene6_isomorphism()
        self.scene7_correspondence()
        self.scene8_summary()

    # --- Scene 1: Hook --- "You Already Know a Quotient Ring"
    # Narration ~35s.

    def scene1_hook(self):
        self.add_subcaption(
            "You already know a quotient ring. "
            "When you compute mod seven on a clock, "
            "you're working in the ring Z slash seven Z. "
            "This is the integers modulo the ideal seven Z. "
            "The question is: can we build these quotient rings "
            "for ANY ring, not just the integers? "
            "The answer is yes, using ideals. "
            "This is Abstract Algebra, Video 125.",
            duration=35,
        )
        play_intro(self, "Quotient Rings", "Abstract Algebra I")

        title = self.ly.title("You Already Know a Quotient Ring")
        self.wait(1)

        # Modular arithmetic as the familiar example
        items = [
            Text("Clock arithmetic = modular arithmetic", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Hours wrap around after 12 (or 7, or n)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("This is the ring  \\mathbb{Z}/n\\mathbb{Z}", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(6)

        # Reveal formula
        reveal = MathTex(
            r"\mathbb{Z}/n\mathbb{Z} = R/I \;\text{ where } R = \mathbb{Z},\; I = n\mathbb{Z}",
            color=WHITE, font_size=28,
        )
        boxed = self.ly.formula_box(reveal, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=items[-1], direction=DOWN, buff=0.35)
        self.play(Write(reveal), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

        # Motivating question
        title2 = self.ly.title("The Big Question")
        self.wait(1)

        question = Text(
            "Can we build R/I for ANY ring R?",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.center_in_content(question)
        self.play(Write(question), run_time=NORMAL)
        self.wait(4)

        answer = Text(
            "YES \u2014 if I is an ideal (Video 124)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(answer, anchor=question, direction=DOWN, buff=0.4)
        self.play(FadeIn(answer, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: Recap --- Ideals as Ring "Normal Subgroups"
    # Narration ~30s.

    def scene2_recap(self):
        self.add_subcaption(
            "Last time we defined ideals. "
            "An ideal I of a ring R absorbs multiplication: "
            "for every r in R and a in I, "
            "both r a and a r belong to I. "
            "This absorption property is exactly what we need "
            "to make coset multiplication well-defined in R over I. "
            "Ideals are the ring-theoretic analog of normal subgroups. "
            "Just as normal subgroups let us quotient groups, "
            "ideals let us quotient rings.",
            duration=30,
        )

        self.ly.section_divider("1", "Recap: Why Ideals Matter")

        title = self.ly.title("The Absorption Property")
        self.wait(1)

        absorption = MathTex(
            r"I \trianglelefteq R: \quad r a \in I \;\text{ and }\; a r \in I \quad \forall\, r \in R,\; a \in I",
            color=WHITE, font_size=28,
        )
        boxed = self.ly.formula_box(absorption, color=SECONDARY)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.4)
        self.play(Write(absorption), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        items = [
            Text("Additive subgroup: (I, +) \\u2264 (R, +)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Absorption: products of ring elements stay in I", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("This makes coset multiplication well-defined", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed, run_time=0.8)
        self.wait(8)

        self.ly.clear()

        # Parallel with groups
        title2 = self.ly.title("Normal Subgroups \\u2194 Ideals")
        self.wait(1)

        left_items = [
            Text("Groups", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
            Text("N \\u25c1 G (normal)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("gNg\\u207b\\u00b9 = N", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("\\u2192 G/N exists", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        right_items = [
            Text("Rings", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
            Text("I \\u25c1 R (ideal)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("rI, Ir \\u2286 I", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("\\u2192 R/I exists", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        left_group, right_group = self.ly.two_columns(left_items, right_items, start_from=title2)
        self.play(
            *[FadeIn(item, shift=LEFT * 0.15) for item in left_items],
            *[FadeIn(item, shift=RIGHT * 0.15) for item in right_items],
            run_time=1.5,
        )
        self.wait(10)

        self.ly.clear()

    # --- Scene 3: Quotient Ring Construction R/I
    # Narration ~60s.

    def scene3_construction(self):
        self.add_subcaption(
            "Here's how we build the quotient ring R over I. "
            "Start with a ring R and an ideal I. "
            "The elements of R over I are the additive cosets "
            "a plus I, which are sets of the form "
            "a plus I equals a plus i for i in I. "
            "These cosets partition R into disjoint blocks. "
            "We define addition of cosets as "
            "a plus I plus b plus I equals a plus b plus I. "
            "And multiplication as "
            "a plus I times b plus I equals a b plus I. "
            "The crucial question: is this well-defined? "
            "If we pick different representatives, "
            "do we get the same coset? "
            "For addition, yes, because cosets of any additive subgroup work. "
            "For multiplication, we need I to be an ideal "
            "to guarantee that a plus I times b plus I "
            "always lands in a b plus I.",
            duration=60,
        )

        self.ly.section_divider("2", "Constructing R/I")

        title = self.ly.title("The Elements: Additive Cosets")
        self.wait(1)

        coset_def = MathTex(
            r"a + I = \{a + i \mid i \in I\}",
            color=WHITE, font_size=34,
        )
        boxed = self.ly.formula_box(coset_def, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.4)
        self.play(Write(coset_def), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        note = Text(
            "Cosets partition R into disjoint blocks",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, anchor=boxed, direction=DOWN, buff=0.35)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Operations
        title2 = self.ly.title("Coset Operations")
        self.wait(1)

        add_op = MathTex(
            r"(a+I) + (b+I) = (a+b) + I",
            color=PRIMARY, font_size=32,
        )
        boxed_add = self.ly.formula_box(add_op, color=PRIMARY)
        self.ly.safe_place(boxed_add, anchor=title2, direction=DOWN, buff=0.4)
        self.play(Write(add_op), Create(boxed_add[1]), run_time=NORMAL)
        self.wait(4)

        mul_op = MathTex(
            r"(a+I) \cdot (b+I) = (ab) + I",
            color=ACCENT, font_size=32,
        )
        boxed_mul = self.ly.formula_box(mul_op, color=ACCENT)
        self.ly.safe_place(boxed_mul, anchor=boxed_add, direction=DOWN, buff=0.4)
        self.play(Write(mul_op), Create(boxed_mul[1]), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

        # Well-definedness
        title3 = self.ly.title("Why Ideals Are Essential")
        self.wait(1)

        items = [
            Text("Addition: always well-defined (abelian cosets)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Multiplication: needs absorption law!", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Without ideals, coset product could escape", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("I absorbs: r \\u00b7 I \\u2286 I and I \\u00b7 r \\u2286 I", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Result: R/I is a bona fide ring", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title3, run_time=0.8)
        self.wait(10)

        self.ly.clear()

    # --- Scene 4: Example — Z/6Z
    # Narration ~45s.

    def scene4_example_z6(self):
        self.add_subcaption(
            "Let's work through a concrete example. "
            "Take R equals Z and I equals 6Z. "
            "The quotient ring Z over 6Z has six elements: "
            "the cosets 0, 1, 2, 3, 4, and 5 mod 6. "
            "We can write this as Z subscript 6. "
            "Let's check multiplication. "
            "In Z subscript 6, the product 2 times 3 equals 6, "
            "which is 0 mod 6. "
            "So 2 times 3 equals 0 with neither factor being zero. "
            "These are zero divisors! "
            "This tells us the ideal 6Z is neither prime nor maximal, "
            "since Z over 6Z is not an integral domain.",
            duration=45,
        )

        self.ly.section_divider("3", "Example: Z/6Z")

        title = self.ly.title("The Ring Z/6Z")
        self.wait(1)

        # Elements
        elements_label = Text(
            "Elements:", font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        elements = MathTex(
            r"\mathbb{Z}/6\mathbb{Z} = \{[0],\; [1],\; [2],\; [3],\; [4],\; [5]\}",
            color=WHITE, font_size=30,
        )
        self.ly.safe_place(elements_label, anchor=title, direction=DOWN, buff=0.4)
        self.ly.safe_place(elements, anchor=elements_label, direction=DOWN, buff=0.3)
        self.play(FadeIn(elements_label, shift=LEFT * 0.15), Write(elements), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

        # Zero divisors
        title2 = self.ly.title("Zero Divisors in Z/6Z")
        self.wait(1)

        product = MathTex(
            r"[2] \cdot [3] = [6] = [0] \;\text{ in } \mathbb{Z}/6\mathbb{Z}",
            color=WHITE, font_size=30,
        )
        boxed = self.ly.formula_box(product, color=RED)
        self.ly.safe_place(boxed, anchor=title2, direction=DOWN, buff=0.4)
        self.play(Write(product), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        items = [
            Text("Neither [2] nor [3] is zero", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("But their product is [0] = zero divisor!", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("6Z is NOT prime (R/I has zero divisors)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed, run_time=0.8)
        self.wait(8)

        self.ly.clear()

        # Connection to prime/composite
        title3 = self.ly.title("When Is Z/nZ \"Nice\"?")
        self.wait(1)

        items = [
            Text("n prime \\u2192 Z/nZ is a field (no zero divisors)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("n composite \\u2192 Z/nZ has zero divisors", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("nZ prime \\u21d4 n prime \\u21d4 Z/nZ integral domain", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title3, run_time=0.8)
        self.wait(8)

        self.ly.clear()

    # --- Scene 5: Example — Constructing F_4
    # Narration ~50s.

    def scene5_example_f4(self):
        self.add_subcaption(
            "Here's a more surprising example. "
            "We'll construct a finite field with 4 elements "
            "that is NOT Z subscript 4. "
            "Start with R equals Z subscript 2 bracket x, "
            "polynomials over the field with 2 elements. "
            "Take I to be the ideal generated by "
            "x squared plus x plus 1. "
            "In the quotient R over I, "
            "the relation x squared plus x plus 1 equals 0 holds, "
            "so x squared equals x plus 1. "
            "Every polynomial reduces to degree 0 or 1, "
            "so the elements of R over I are "
            "0, 1, x, and x plus 1. Only four elements! "
            "And this is a field. "
            "Every nonzero element has a multiplicative inverse. "
            "We've just constructed F subscript 4, "
            "the finite field of order 4.",
            duration=50,
        )

        self.ly.section_divider("4", "Example: Constructing F_4")

        title = self.ly.title("Building a New Finite Field")
        self.wait(1)

        setup = MathTex(
            r"R = \mathbb{Z}_2[x], \quad I = \langle x^2 + x + 1 \rangle",
            color=WHITE, font_size=30,
        )
        boxed = self.ly.formula_box(setup, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.4)
        self.play(Write(setup), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Key relation
        title2 = self.ly.title("Key Relation in R/I")
        self.wait(1)

        relation = MathTex(
            r"x^2 + x + 1 = 0 \;\Rightarrow\; x^2 = x + 1",
            color=WHITE, font_size=30,
        )
        boxed2 = self.ly.formula_box(relation, color=ACCENT)
        self.ly.safe_place(boxed2, anchor=title2, direction=DOWN, buff=0.4)
        self.play(Write(relation), Create(boxed2[1]), run_time=NORMAL)
        self.wait(4)

        items = [
            Text("Every polynomial reduces to degree 0 or 1", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Only 4 elements remain!", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed2, run_time=0.8)
        self.wait(5)

        self.ly.clear()

        # The four elements
        title3 = self.ly.title("Elements of F_4")
        self.wait(1)

        elems = MathTex(
            r"\mathbb{F}_4 = \{0,\; 1,\; x,\; x+1\}",
            color=WHITE, font_size=34,
        )
        boxed3 = self.ly.formula_box(elems, color=SECONDARY)
        self.ly.safe_place(boxed3, anchor=title3, direction=DOWN, buff=0.4)
        self.play(Write(elems), Create(boxed3[1]), run_time=NORMAL)
        self.wait(4)

        items = [
            Text("x squared = x plus 1 (the key relation)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Every nonzero element has an inverse", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("This is a FIELD (unlike Z subscript 4)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed3, run_time=0.8)
        self.wait(8)

        self.ly.clear()

    # --- Scene 6: First Isomorphism Theorem for Rings
    # Narration ~55s.

    def scene6_isomorphism(self):
        self.add_subcaption(
            "One of the most powerful results in ring theory "
            "is the first isomorphism theorem. "
            "If phi is a ring homomorphism from R to S, "
            "then R over the kernel of phi "
            "is isomorphic to the image of phi. "
            "There's a natural projection map pi "
            "from R to R over I, sending each element to its coset. "
            "And there's an induced map phi bar "
            "from R over I to S, "
            "defined by phi bar of a plus I equals phi of a. "
            "The theorem says phi equals phi bar composed with pi. "
            "Example: the evaluation map from Z to Z subscript 7 "
            "sending n to n mod 7 has kernel 7Z. "
            "So Z over 7Z is isomorphic to Z subscript 7.",
            duration=55,
        )

        self.ly.section_divider("5", "First Isomorphism Theorem")

        title = self.ly.title("First Isomorphism Theorem for Rings")
        self.wait(1)

        # Statement
        thm_label = Text(
            "Theorem:", font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        thm = MathTex(
            r"\varphi: R \to S \;\text{ ring homomorphism} \Rightarrow R/\ker(\varphi) \cong \text{im}(\varphi)",
            color=WHITE, font_size=26,
        )
        thm_group = VGroup(thm_label, thm).arrange(RIGHT, buff=0.3)
        boxed = self.ly.formula_box(thm, color=PRIMARY)
        self.ly.safe_place(thm_label, anchor=title, direction=DOWN, buff=0.4)
        self.ly.safe_place(boxed, anchor=thm_label, direction=DOWN, buff=0.3)
        self.play(FadeIn(thm_label, shift=LEFT * 0.15), Write(thm), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

        # Commutative diagram
        title2 = self.ly.title("The Commutative Diagram")
        self.wait(1)

        # Build diagram with MathTex labels and arrows
        r_label = Text("R", font_size=HEADING_SIZE, color=PRIMARY, font=MONO)
        ri_label = Text("R/I", font_size=HEADING_SIZE, color=SECONDARY, font=MONO)
        s_label = Text("S", font_size=HEADING_SIZE, color=ACCENT, font=MONO)

        # Position: R top-left, R/I bottom-left, S right-middle
        r_label.move_to(LEFT * 2.2 + UP * 1.0)
        ri_label.move_to(LEFT * 2.2 + DOWN * 1.0)
        s_label.move_to(RIGHT * 2.2)

        # Arrows
        arrow_pi = Arrow(
            r_label.get_bottom(), ri_label.get_top(),
            buff=0.15, color=SECONDARY, stroke_width=2,
        )
        arrow_phi = Arrow(
            r_label.get_right(), s_label.get_left(),
            buff=0.15, color=PRIMARY, stroke_width=2,
        )
        arrow_phibar = Arrow(
            ri_label.get_right(), s_label.get_bottom(),
            buff=0.15, color=ACCENT, stroke_width=2,
        )

        pi_tex = MathTex(r"\pi", color=SECONDARY, font_size=24).next_to(arrow_pi, LEFT, buff=0.1)
        phi_tex = MathTex(r"\varphi", color=PRIMARY, font_size=24).next_to(arrow_phi, UP, buff=0.1)
        phibar_tex = MathTex(r"\bar{\varphi}", color=ACCENT, font_size=24).next_to(arrow_phibar, DOWN, buff=0.1)

        self.play(
            FadeIn(r_label), FadeIn(ri_label), FadeIn(s_label),
            run_time=FAST,
        )
        self.play(
            Create(arrow_pi), Create(arrow_phi), Create(arrow_phibar),
            FadeIn(pi_tex), FadeIn(phi_tex), FadeIn(phibar_tex),
            run_time=NORMAL,
        )
        self.wait(8)

        eq_text = MathTex(
            r"\varphi = \bar{\varphi} \circ \pi",
            color=WHITE, font_size=28,
        )
        self.ly.safe_place(eq_text, anchor=s_label, direction=DOWN, buff=0.6)
        self.play(Write(eq_text), run_time=FAST)
        self.wait(5)

        self.ly.clear()

        # Worked example
        title3 = self.ly.title("Example: Z \\u2192 Z_7")
        self.wait(1)

        example = MathTex(
            r"\varphi: \mathbb{Z} \to \mathbb{Z}_7, \;\varphi(n) = n \bmod 7",
            color=WHITE, font_size=28,
        )
        boxed_ex = self.ly.formula_box(example, color=PRIMARY)
        self.ly.safe_place(boxed_ex, anchor=title3, direction=DOWN, buff=0.4)
        self.play(Write(example), Create(boxed_ex[1]), run_time=NORMAL)
        self.wait(4)

        result = MathTex(
            r"\ker(\varphi) = 7\mathbb{Z} \;\Rightarrow\; \mathbb{Z}/7\mathbb{Z} \cong \mathbb{Z}_7",
            color=SECONDARY, font_size=28,
        )
        boxed_res = self.ly.formula_box(result, color=SECONDARY)
        self.ly.safe_place(boxed_res, anchor=boxed_ex, direction=DOWN, buff=0.4)
        self.play(Write(result), Create(boxed_res[1]), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 7: Correspondence Theorem
    # Narration ~40s.

    def scene7_correspondence(self):
        self.add_subcaption(
            "The correspondence theorem gives us a powerful way "
            "to understand the ideals of a quotient ring. "
            "It says: the ideals of R over I "
            "are in one-to-one correspondence "
            "with the ideals of R that contain I. "
            "If J is an ideal between I and R, "
            "then J over I is an ideal of R over I. "
            "Moreover, prime ideals stay prime "
            "and maximal ideals stay maximal under this correspondence. "
            "This means we can study the ideal structure "
            "of R over I entirely through the ideals of R. "
            "It's like collapsing the lattice of ideals "
            "by quotienting out I.",
            duration=40,
        )

        self.ly.section_divider("6", "Correspondence Theorem")

        title = self.ly.title("Ideal Correspondence")
        self.wait(1)

        # Statement
        items = [
            Text("Ideals of R/I \\u21d4 Ideals of R containing I", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("If I \\u2286 J \\u2286 R, then J/I is ideal of R/I", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Prime ideals \\u2192 stay prime", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Maximal ideals \\u2192 stay maximal", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(10)

        self.ly.clear()

        # Lattice visual
        title2 = self.ly.title("Collapsing the Lattice")
        self.wait(1)

        # Lattice: R at top, I at bottom, intermediate J
        r_node = MathTex(r"R", color=PRIMARY, font_size=34)
        j_node = MathTex(r"J", color=ACCENT, font_size=34)
        i_node = MathTex(r"I", color=SECONDARY, font_size=34)

        r_node.move_to(UP * 1.5)
        j_node.move_to(UP * 0)
        i_node.move_to(DOWN * 1.5)

        line_rj = Line(r_node.get_bottom(), j_node.get_top(), color=DIM, stroke_width=2)
        line_ji = Line(j_node.get_bottom(), i_node.get_top(), color=DIM, stroke_width=2)

        self.play(
            FadeIn(r_node), FadeIn(i_node), FadeIn(j_node),
            Create(line_rj), Create(line_ji),
            run_time=NORMAL,
        )
        self.wait(3)

        # Arrow showing collapse
        collapse_label = Text(
            "\\u27a1 Quotient by I:", font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(collapse_label, anchor=r_node, direction=RIGHT, buff=0.8)

        ri_node = MathTex(r"R/I", color=PRIMARY, font_size=30)
        ji_node = MathTex(r"J/I", color=ACCENT, font_size=30)
        zero_node = MathTex(r"\{0\}", color=SECONDARY, font_size=30)

        ri_node.move_to(RIGHT * 2.5 + UP * 1.0)
        ji_node.move_to(RIGHT * 2.5 + DOWN * 0.0)
        zero_node.move_to(RIGHT * 2.5 + DOWN * 1.0)

        line_riji = Line(ri_node.get_bottom(), ji_node.get_top(), color=DIM, stroke_width=2)
        line_jizero = Line(ji_node.get_bottom(), zero_node.get_top(), color=DIM, stroke_width=2)

        arrow_collapse = Arrow(
            r_node.get_right(), ri_node.get_left(),
            buff=0.15, color=PRIMARY, stroke_width=2,
        )

        self.play(
            FadeIn(collapse_label, shift=LEFT * 0.15),
            FadeIn(ri_node), FadeIn(ji_node), FadeIn(zero_node),
            Create(line_riji), Create(line_jizero),
            Create(arrow_collapse),
            run_time=NORMAL,
        )
        self.wait(6)

        self.ly.clear()

    # --- Scene 8: Summary --- Groups vs Rings Parallel
    # Narration ~35s.

    def scene8_summary(self):
        self.add_subcaption(
            "Let's recap what we've learned about quotient rings. "
            "Given a ring R and an ideal I, "
            "the quotient ring R over I has cosets a plus I as elements, "
            "with operations inherited from R. "
            "The absorption law of ideals is what makes "
            "coset multiplication well-defined. "
            "The first isomorphism theorem "
            "lets us identify quotient rings as images of homomorphisms. "
            "And the correspondence theorem connects "
            "the ideal structures of R and R over I. "
            "Notice the beautiful parallel with group theory: "
            "normal subgroups give quotient groups, "
            "ideals give quotient rings, "
            "and the first isomorphism theorem "
            "has the same form in both worlds. "
            "This completes our Abstract Algebra I playlist. "
            "Thank you for watching!",
            duration=35,
        )

        title = self.ly.title("Summary: Quotient Rings")
        self.wait(1)

        items = [
            Text("R/I: cosets a+I with inherited operations", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Absorption law makes multiplication well-defined", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("1st Isomorphism Thm: R/ker(\\varphi) \\u2245 im(\\varphi)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Correspondence Thm: ideals of R/I \\u21d4 ideals J \\u2287 I", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(10)

        self.ly.clear()

        # Parallel comparison
        title2 = self.ly.title("The Beautiful Parallel")
        self.wait(1)

        left_items = [
            Text("Group Theory", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
            Text("Normal subgroup N", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("G/N quotient group", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("G/ker(\\varphi) \\u2245 im(\\varphi)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        right_items = [
            Text("Ring Theory", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
            Text("Ideal I", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("R/I quotient ring", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("R/ker(\\varphi) \\u2245 im(\\varphi)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        left_group, right_group = self.ly.two_columns(left_items, right_items, start_from=title2)
        self.play(
            *[FadeIn(item, shift=LEFT * 0.15) for item in left_items],
            *[FadeIn(item, shift=RIGHT * 0.15) for item in right_items],
            run_time=1.5,
        )
        self.wait(8)

        self.ly.clear()

        play_outro(self)
