"""Video 118: Direct Products and Finite Abelian Groups
TEMPLATE v2 -- Professional quality Manim script

Playlist: Abstract Algebra I (Video 8 of 12)
Class: Video118_DirectProductsFiniteAbelian

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


class Video118_DirectProductsFiniteAbelian(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_cyclic_product()
        self.scene4_properties()
        self.scene5_internal_product()
        self.scene6_classification_statement()
        self.scene7_classification_examples()
        self.scene8_summary()

    # --- Scene 1: Hook ---
    # Narration ~32s. Animations must fill this time.
    # play_intro ~8s, then items + waits to fill remaining ~24s.

    def scene1_hook(self):
        self.add_subcaption(
            "How do we build complex groups from simpler ones? "
            "In chemistry, atoms combine to form molecules. "
            "In group theory, simple groups combine through the direct product. "
            "Today we will learn how to take two groups and create a new one, "
            "and then we will see the most powerful classification result "
            "in all of finite group theory. "
            "Every finite abelian group can be decomposed "
            "into a direct product of cyclic groups. "
            "This is Abstract Algebra, Video 8.",
            duration=32,
        )
        play_intro(self, "Direct Products and Finite Abelian Groups", "Abstract Algebra I")

        title = self.ly.title("Building Complex Groups from Simple Ones")
        self.wait(3)

        items = [
            Text("Atoms combine to form molecules", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Groups combine via the direct product", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Every finite abelian group is a product of cyclic groups", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(3)

        # Teaser formula
        teaser = MathTex(
            r"\mathbb{Z}_2 \times \mathbb{Z}_3 \cong \mathbb{Z}_6",
            color=WHITE, font_size=36,
        )
        boxed = self.ly.formula_box(teaser, color=ACCENT)
        self.play(FadeOut(items[0]), run_time=FAST)
        self.ly.safe_place(boxed, anchor=items[-1], direction=DOWN, buff=0.5)
        self.play(Write(teaser), Create(boxed[1]), run_time=NORMAL)
        self.wait(6)

        self.ly.clear()

    # --- Scene 2: External Direct Product Definition ---
    # Narration ~50s.

    def scene2_definition(self):
        self.add_subcaption(
            "The external direct product of groups G and H "
            "is the set of ordered pairs g comma h where g is in G and h is in H, "
            "with the operation performed component by component. "
            "The group operation is: g1 h1 times g2 h2 equals g1 g2 comma h1 h2. "
            "The identity is e_G comma e_H, "
            "and the inverse of g h is g inverse comma h inverse. "
            "As an example, consider Z_2 times Z_3. "
            "This has 6 elements: 0 0, 1 0, 0 1, 1 1, 0 2, and 1 2. "
            "We add component-wise, mod 2 in the first coordinate and mod 3 in the second. "
            "Then we meet the Klein four-group Z_2 times Z_2, "
            "where every element has order 1 or 2, so it is not cyclic.",
            duration=50,
        )

        title = self.ly.title("External Direct Product")
        self.wait(2)

        # Definition
        defn = MathTex(
            r"G \times H = \{(g, h) : g \in G,\; h \in H\}",
            color=WHITE, font_size=32,
        )
        self.ly.safe_place(defn, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(4)

        # Operation
        op = MathTex(
            r"(g_1, h_1) \cdot (g_2, h_2) = (g_1 g_2,\; h_1 h_2)",
            color=PRIMARY, font_size=30,
        )
        op_label = Text("component-wise operation", font_size=SMALL_SIZE, color=PRIMARY, font=SANS)
        op_group = VGroup(op, op_label).arrange(DOWN, buff=0.15)
        self.ly.safe_place(op_group, anchor=defn, direction=DOWN, buff=0.4)
        self.play(Write(op), run_time=NORMAL)
        self.ly.safe_place(op_label, anchor=op, direction=DOWN, buff=0.15)
        self.play(FadeIn(op_label, shift=LEFT * 0.1), run_time=FAST)
        self.wait(6)

        # Example: Z_2 x Z_3
        ex_label = Text(
            "Example: Z_2 x Z_3 (order 6)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.play(FadeOut(defn), FadeOut(op), FadeOut(op_label), run_time=FAST)
        self.ly.safe_place(ex_label, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(ex_label), run_time=NORMAL)
        self.wait(3)

        elements = MathTex(
            r"\{(0,0),\; (1,0),\; (0,1),\; (1,1),\; (0,2),\; (1,2)\}",
            color=WHITE, font_size=28,
        )
        self.ly.safe_place(elements, anchor=ex_label, direction=DOWN, buff=0.3)
        self.play(Write(elements), run_time=NORMAL)
        self.wait(8)

        # Klein four-group
        klein = Text(
            "Z_2 x Z_2 = Klein four-group V_4",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.play(FadeOut(ex_label), FadeOut(elements), run_time=FAST)
        self.ly.safe_place(klein, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(klein), run_time=NORMAL)
        self.wait(3)

        klein_note = Text(
            "Every element has order 1 or 2 -- not cyclic!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(klein_note, anchor=klein, direction=DOWN, buff=0.3)
        self.play(FadeIn(klein_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(6)

        self.ly.clear()

    # --- Scene 3: When is the Product Cyclic? ---
    # Narration ~60s.

    def scene3_cyclic_product(self):
        self.add_subcaption(
            "A natural question: when is the direct product of cyclic groups itself cyclic? "
            "The answer is beautiful and connects to number theory. "
            "Z_m times Z_n is isomorphic to Z_{m n} "
            "if and only if the greatest common divisor of m and n equals 1. "
            "For example, gcd of 2 and 3 is 1, "
            "so Z_2 times Z_3 is isomorphic to Z_6. "
            "The element 1 1 generates the entire group: "
            "1 1, then 0 2, then 1 0, then 0 1, then 1 2, then 0 0. "
            "A full 6-cycle. "
            "But Z_2 times Z_2 is not cyclic because gcd of 2 and 2 is 2, not 1. "
            "The Klein four-group has no element of order 4. "
            "This result is the Chinese Remainder Theorem in disguise.",
            duration=60,
        )

        self.ly.section_divider(1, "When is the Product Cyclic?")
        self.wait(3)

        title = self.ly.title("Cyclic Direct Products")
        self.wait(1)

        # The theorem
        theorem = MathTex(
            r"\mathbb{Z}_m \times \mathbb{Z}_n \cong \mathbb{Z}_{mn}"
            r"\;\iff\; \gcd(m, n) = 1",
            color=ACCENT, font_size=32,
        )
        boxed = self.ly.formula_box(theorem, color=ACCENT)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(theorem), Create(boxed[1]), run_time=NORMAL)
        self.wait(6)

        # Visual: Z_2 x Z_3 lattice
        z2z3_label = Text("Z_2 x Z_3 (gcd=1, cyclic!)", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(z2z3_label, anchor=boxed, direction=DOWN, buff=0.5)
        self.play(Write(z2z3_label), run_time=FAST)
        self.wait(3)

        # Build a 2x3 grid of dots showing the lattice structure
        grid_dots = VGroup()
        grid_labels = VGroup()
        for i in range(2):
            for j in range(3):
                dot = Dot(radius=0.08, color=PRIMARY if (i + j) % 3 == 0 else WHITE)
                dot.move_to(LEFT * 2.0 + i * 1.2 + DOWN * 0.5 + j * 0.8)
                grid_dots.add(dot)
                label = Text(
                    f"({i},{j})", font_size=18, color=DIM, font=MONO,
                ).next_to(dot, RIGHT, buff=0.1)
                grid_labels.add(label)
        # Connect dots to show cyclic order: (0,0)->(1,1)->(0,2)->(1,0)->(0,1)->(1,2)->(0,0)
        cycle_order = [(0, 0), (1, 1), (0, 2), (1, 0), (0, 1), (1, 2), (0, 0)]
        cycle_arrows = VGroup()
        for k in range(len(cycle_order) - 1):
            i1, j1 = cycle_order[k]
            i2, j2 = cycle_order[k + 1]
            d1 = grid_dots[i1 * 3 + j1]
            d2 = grid_dots[i2 * 3 + j2]
            cycle_arrows.add(
                Arrow(d1.get_center(), d2.get_center(),
                      color=ACCENT, stroke_width=1.5, buff=0.08)
            )

        self.play(*[FadeIn(d) for d in grid_dots], run_time=FAST)
        self.play(*[FadeIn(l, shift=LEFT * 0.05) for l in grid_labels], run_time=FAST)
        self.play(*[Create(a) for a in cycle_arrows], run_time=NORMAL)
        self.wait(8)

        # Counterexample
        self.play(
            FadeOut(grid_dots), FadeOut(grid_labels), FadeOut(cycle_arrows),
            FadeOut(z2z3_label), run_time=FAST,
        )
        counter_label = Text("Z_2 x Z_2 (gcd=2, NOT cyclic)", font_size=BODY_SIZE, color=RED, font=SANS)
        self.ly.safe_place(counter_label, anchor=boxed, direction=DOWN, buff=0.5)
        self.play(Write(counter_label), run_time=FAST)
        self.wait(3)

        counter_reason = Text(
            "All elements have order 1 or 2",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(counter_reason, anchor=counter_label, direction=DOWN, buff=0.3)
        self.play(FadeIn(counter_reason, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        note = Text(
            "This is the Chinese Remainder Theorem for groups",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, anchor=counter_reason, direction=DOWN, buff=0.3)
        self.play(FadeIn(note, shift=LEFT * 0.1), run_time=FAST)
        self.wait(6)

        self.ly.clear()

    # --- Scene 4: Properties of Direct Products ---
    # Narration ~50s.

    def scene4_properties(self):
        self.add_subcaption(
            "Let us list the key properties of direct products. "
            "First, the order: the order of G times H equals the order of G times the order of H. "
            "Second, subgroups: if A is a subgroup of G and B is a subgroup of H, "
            "then A times B is a subgroup of G times H. "
            "Third, abelian-ness: G times H is abelian if and only if both G and H are abelian. "
            "Fourth, the projection maps. "
            "The map pi_1 of g h equals g projects onto the first factor, "
            "and pi_2 of g h equals h projects onto the second factor. "
            "These are homomorphisms. "
            "The operations happen independently in each coordinate.",
            duration=50,
        )

        title = self.ly.title("Properties of Direct Products")
        self.wait(2)

        properties = [
            Text(
                "1. |G x H| = |G| times |H|",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "2. A <= G and B <= H => A x B <= G x H",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "3. G x H is abelian iff both G and H are abelian",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "4. Projection maps pi_1, pi_2 are homomorphisms",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(properties, start_from=title, run_time=1.0)
        self.wait(8)

        # Formula for projections
        proj = MathTex(
            r"\pi_1(g,h) = g, \quad \pi_2(g,h) = h",
            color=PRIMARY, font_size=30,
        )
        self.play(FadeOut(properties[0]), run_time=FAST)
        self.ly.safe_place(proj, anchor=properties[-1], direction=DOWN, buff=0.5)
        self.play(Write(proj), run_time=NORMAL)
        self.wait(6)

        # Key insight
        insight = Text(
            "Operations happen independently in each coordinate",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(insight, anchor=proj, direction=DOWN, buff=0.4)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=FAST)
        self.wait(8)

        self.ly.clear()

    # --- Scene 5: Internal Direct Products ---
    # Narration ~55s.

    def scene5_internal_product(self):
        self.add_subcaption(
            "So far we have discussed external direct products, "
            "building a new group from two separate groups. "
            "But sometimes a group already contains subgroups "
            "that behave like a direct product. "
            "We say G is the internal direct product of H and K "
            "when four conditions hold. "
            "First, H is a normal subgroup of G. "
            "Second, K is a normal subgroup of G. "
            "Third, H intersect K equals the identity. "
            "Fourth, H K equals G, meaning every element of G "
            "can be written as h k for some h in H and k in K. "
            "When all four conditions hold, "
            "G is isomorphic to H times K. "
            "Example: Z_6 is the internal direct product of Z_2 and Z_3 "
            "via the subgroups generated by 3 and by 2.",
            duration=55,
        )

        self.ly.section_divider(2, "Internal Direct Products")
        self.wait(3)

        title = self.ly.title("Internal Direct Products")
        self.wait(1)

        # Key question
        question = Text(
            "When does G already contain H x K as subgroups?",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(question, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(question), run_time=NORMAL)
        self.wait(5)

        # Four conditions
        conditions = [
            (r"H \trianglelefteq G", "H is normal", RED),
            (r"K \trianglelefteq G", "K is normal", SECONDARY),
            (r"H \cap K = \{e\}", "Trivial intersection", ACCENT),
            (r"HK = G", "Product is the whole group", PRIMARY),
        ]

        prev = question
        for i, (cond_tex, cond_label, cond_color) in enumerate(conditions):
            if i == 2:
                self.play(FadeOut(question), run_time=FAST)
            cond_formula = MathTex(cond_tex, color=cond_color, font_size=30)
            cond_text = Text(cond_label, font_size=SMALL_SIZE, color=cond_color, font=SANS)
            cond_group = VGroup(cond_formula, cond_text).arrange(RIGHT, buff=0.3)
            self.ly.safe_place(cond_group, anchor=prev, direction=DOWN, buff=0.35)
            self.play(
                FadeIn(cond_group, shift=LEFT * 0.1),
                run_time=NORMAL,
            )
            prev = cond_group
            self.wait(4)

        self.wait(3)

        # Result
        result = MathTex(
            r"\text{If all four hold: } G \cong H \times K",
            color=WHITE, font_size=28,
        )
        self.ly.safe_place(result, anchor=prev, direction=DOWN, buff=0.4)
        self.play(Write(result), run_time=NORMAL)
        self.wait(5)

        # Example (remove last condition group to make room)
        self.play(
            FadeOut(prev), run_time=FAST,
        )
        ex = MathTex(
            r"\mathbb{Z}_6 \cong \langle 3 \rangle \times \langle 2 \rangle"
            r"\cong \mathbb{Z}_2 \times \mathbb{Z}_3",
            color=ACCENT, font_size=26,
        )
        self.ly.safe_place(ex, anchor=result, direction=DOWN, buff=0.4)
        self.play(Write(ex), run_time=NORMAL)
        self.wait(6)

        self.ly.clear()

    # --- Scene 6: Classification Theorem ---
    # Narration ~60s.

    def scene6_classification_statement(self):
        self.add_subcaption(
            "Now we arrive at one of the most important results in group theory. "
            "The Fundamental Theorem of Finite Abelian Groups. "
            "Every finite abelian group is isomorphic to a direct product "
            "of cyclic groups of prime-power order. "
            "Moreover, this decomposition is essentially unique. "
            "There are two standard ways to write the decomposition. "
            "The invariant factor form: "
            "Z_{d_1} times Z_{d_2} times dot dot dot times Z_{d_k} "
            "where d_1 divides d_2 divides dot dot dot divides d_k. "
            "The elementary divisor form: "
            "each factor is Z_{p^e} for a prime p and exponent e. "
            "Think of it like prime factorization of integers. "
            "Every integer factors uniquely into primes. "
            "Every finite abelian group factors uniquely into cyclic p-groups.",
            duration=60,
        )

        self.ly.section_divider(3, "Classification of Finite Abelian Groups")
        self.wait(4)

        title = self.ly.title("Fundamental Theorem")
        self.wait(1)

        # Theorem statement
        theorem = MathTex(
            r"\text{Every finite abelian group } G \cong "
            r"\prod_{i} \mathbb{Z}_{p_i^{e_i}}",
            color=ACCENT, font_size=30,
        )
        boxed = self.ly.formula_box(theorem, color=ACCENT)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(theorem), Create(boxed[1]), run_time=NORMAL)
        self.wait(6)

        # Uniqueness
        unique = Text(
            "This decomposition is essentially unique",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(unique, anchor=boxed, direction=DOWN, buff=0.4)
        self.play(FadeIn(unique, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        # Two forms
        form1_label = Text("Invariant factor form:", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        form1 = MathTex(
            r"\mathbb{Z}_{d_1} \times \mathbb{Z}_{d_2} \times \cdots \times \mathbb{Z}_{d_k}"
            r"\;\text{ where } d_1 \mid d_2 \mid \cdots \mid d_k",
            color=PRIMARY, font_size=24,
        )
        self.play(FadeOut(unique), run_time=FAST)
        self.ly.safe_place(form1_label, anchor=boxed, direction=DOWN, buff=0.4)
        self.play(Write(form1_label), run_time=NORMAL)
        self.ly.safe_place(form1, anchor=form1_label, direction=DOWN, buff=0.2)
        self.play(Write(form1), run_time=NORMAL)
        self.wait(8)

        form2_label = Text("Elementary divisor form:", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        form2 = MathTex(
            r"\mathbb{Z}_{p^{e_1}} \times \mathbb{Z}_{p^{e_2}} \times \cdots"
            r"\;\text{ (prime powers)}",
            color=SECONDARY, font_size=24,
        )
        self.play(
            FadeOut(form1_label), FadeOut(form1),
            run_time=FAST,
        )
        self.ly.safe_place(form2_label, anchor=boxed, direction=DOWN, buff=0.4)
        self.play(Write(form2_label), run_time=NORMAL)
        self.ly.safe_place(form2, anchor=form2_label, direction=DOWN, buff=0.2)
        self.play(Write(form2), run_time=NORMAL)
        self.wait(8)

        # Analogy
        self.play(
            FadeOut(form2_label), FadeOut(form2),
            run_time=FAST,
        )
        analogy = Text(
            "Like prime factorization of integers, but for groups!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(analogy, anchor=boxed, direction=DOWN, buff=0.5)
        self.play(FadeIn(analogy, shift=LEFT * 0.15), run_time=FAST)
        self.wait(6)

        self.ly.clear()

    # --- Scene 7: Classification Examples ---
    # Narration ~65s.

    def scene7_classification_examples(self):
        self.add_subcaption(
            "Let us work through concrete examples. "
            "First, all abelian groups of order 8. "
            "We factor 8 as 2 cubed. "
            "The partitions of the exponent 3 are: 3, then 2 plus 1, then 1 plus 1 plus 1. "
            "This gives us three groups: "
            "Z_8, Z_4 times Z_2, and Z_2 times Z_2 times Z_2. "
            "These are all the abelian groups of order 8, up to isomorphism. "
            "Second, all abelian groups of order 36. "
            "We factor 36 as 4 times 9, that is 2 squared times 3 squared. "
            "For the 2-part, partitions of 2 give us Z_4 or Z_2 times Z_2. "
            "For the 3-part, partitions of 2 give us Z_9 or Z_3 times Z_3. "
            "Combining, we get four groups. "
            "The algorithm: factor the order, "
            "then partition the exponents of each prime power.",
            duration=65,
        )

        self.ly.section_divider(4, "Classification Examples")
        self.wait(3)

        title = self.ly.title("Examples")
        self.wait(1)

        # Example 1: order 8
        ex1_title = Text(
            "All abelian groups of order 8",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(ex1_title, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(ex1_title), run_time=NORMAL)
        self.wait(3)

        ex1_factor = Text(
            "8 = 2^3, partitions of 3: {3}, {2,1}, {1,1,1}",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(ex1_factor, anchor=ex1_title, direction=DOWN, buff=0.3)
        self.play(FadeIn(ex1_factor, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        groups_8 = [
            MathTex(r"\mathbb{Z}_8", color=ACCENT, font_size=30),
            MathTex(r"\mathbb{Z}_4 \times \mathbb{Z}_2", color=SECONDARY, font_size=30),
            MathTex(r"\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2", color=RED, font_size=26),
        ]
        g1_label = Text("1.", font_size=SMALL_SIZE, color=ACCENT, font=SANS)
        g1 = VGroup(g1_label, groups_8[0]).arrange(RIGHT, buff=0.2)
        self.play(FadeOut(ex1_factor), run_time=FAST)
        self.ly.safe_place(g1, anchor=ex1_title, direction=DOWN, buff=0.3)
        self.play(Write(g1), run_time=NORMAL)
        self.wait(3)

        g2_label = Text("2.", font_size=SMALL_SIZE, color=SECONDARY, font=SANS)
        g2 = VGroup(g2_label, groups_8[1]).arrange(RIGHT, buff=0.2)
        self.ly.safe_place(g2, anchor=g1, direction=DOWN, buff=0.25)
        self.play(Write(g2), run_time=NORMAL)
        self.wait(3)

        g3_label = Text("3.", font_size=SMALL_SIZE, color=RED, font=SANS)
        g3 = VGroup(g3_label, groups_8[2]).arrange(RIGHT, buff=0.2)
        self.ly.safe_place(g3, anchor=g2, direction=DOWN, buff=0.25)
        self.play(Write(g3), run_time=NORMAL)
        self.wait(5)

        # Example 2: order 36
        ex2_title = Text(
            "All abelian groups of order 36",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.play(
            FadeOut(ex1_title), FadeOut(g1), FadeOut(g2), FadeOut(g3),
            run_time=FAST,
        )
        self.ly.safe_place(ex2_title, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(ex2_title), run_time=NORMAL)
        self.wait(3)

        ex2_factor = Text(
            "36 = 2^2 x 3^2: (Z_4 or Z_2xZ_2) x (Z_9 or Z_3xZ_3)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(ex2_factor, anchor=ex2_title, direction=DOWN, buff=0.3)
        self.play(FadeIn(ex2_factor, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        groups_36 = [
            MathTex(r"\mathbb{Z}_4 \times \mathbb{Z}_9 \cong \mathbb{Z}_{36}", color=ACCENT, font_size=26),
            MathTex(r"\mathbb{Z}_4 \times \mathbb{Z}_3 \times \mathbb{Z}_3", color=SECONDARY, font_size=26),
            MathTex(r"\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_9", color=PRIMARY, font_size=26),
            MathTex(r"\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_3 \times \mathbb{Z}_3", color=RED, font_size=22),
        ]

        self.play(FadeOut(ex2_factor), run_time=FAST)

        grps_to_remove = []
        prev_grp = ex2_title
        for i, grp in enumerate(groups_36):
            num_label = Text(f"{i+1}.", font_size=SMALL_SIZE, color=grp.color, font=SANS)
            grp_line = VGroup(num_label, grp).arrange(RIGHT, buff=0.2)
            self.ly.safe_place(grp_line, anchor=prev_grp, direction=DOWN, buff=0.3)
            self.play(Write(grp_line), run_time=NORMAL)
            self.wait(3)
            prev_grp = grp_line
            grps_to_remove.append(grp_line)
            # Remove earlier ones to stay in budget
            if i >= 2:
                self.play(FadeOut(grps_to_remove[0]), run_time=FAST)
                grps_to_remove.pop(0)

        self.wait(3)

        # Algorithm summary
        self.play(FadeOut(ex2_title), FadeOut(prev_grp), run_time=FAST)
        algo = Text(
            "Algorithm: factor |G|, partition exponents, enumerate products",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(algo, anchor=title, direction=DOWN, buff=0.5)
        self.play(FadeIn(algo, shift=LEFT * 0.15), run_time=FAST)
        self.wait(6)

        self.ly.clear()

    # --- Scene 8: Summary + Outro ---
    # Narration ~60s.

    def scene8_summary(self):
        self.add_subcaption(
            "Let us summarize what we learned today. "
            "The direct product G times H pairs elements from G and H, "
            "with component-wise operations. "
            "Z_m times Z_n is cyclic if and only if gcd of m and n equals 1. "
            "The internal direct product describes when a group "
            "naturally splits into a product of subgroups. "
            "The Fundamental Theorem of Finite Abelian Groups says "
            "every finite abelian group is a direct product "
            "of cyclic groups of prime-power order, uniquely. "
            "This is like the periodic table for finite abelian groups. "
            "Direct products are the building blocks of abelian group theory. "
            "Next time, we explore group actions "
            "and see how groups can act on sets. "
            "Thanks for watching.",
            duration=60,
        )

        title = self.ly.title("Summary")
        self.wait(2)

        takeaways = [
            Text("1. G x H: ordered pairs, component-wise operation", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Z_m x Z_n cyclic iff gcd(m,n) = 1", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Internal product: H,K normal, trivial intersection, HK=G", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Every finite abelian group = product of cyclic p-groups", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5. Classification: the periodic table of finite abelian groups", font_size=BODY_SIZE, color=RED, font=SANS),
        ]

        self.ly.progressive_reveal(takeaways, start_from=title, run_time=0.8)
        self.wait(10)

        self.ly.clear()

        play_outro(self, "Group Actions", "Abstract Algebra I")
