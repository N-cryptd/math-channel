"""Video 114: Cosets and Lagrange's Theorem
TEMPLATE v2 -- Professional quality Manim script

Playlist: Abstract Algebra I (Video 5 of 12)
Class: Video114_CosetsAndLagrangesTheorem
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


class Video114_CosetsAndLagrangesTheorem(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_example_z6()
        self.scene4_properties()
        self.scene5_example_s3()
        self.scene6_lagrange_statement()
        self.scene7_proof()
        self.scene8_applications()
        self.scene9_summary()

    # --- Scene 1: Hook --- Partitioning a Group ---

    def scene1_hook(self):
        self.add_subcaption(
            "Imagine you have a group G, and inside it a subgroup H. "
            "What happens if you take every element of H and shift it by some fixed element g? "
            "You get another block the same size as H. "
            "Shift by a different element, you get another block, same size again. "
            "These blocks partition the entire group perfectly, "
            "like slicing a pie into equal pieces. "
            "This simple observation leads to one of the most powerful theorems in all of group theory. "
            "Today we explore cosets and Lagrange's Theorem.",
            duration=31.3,
        )
        play_intro(self, "Cosets and Lagrange's Theorem", "Abstract Algebra I")

        title = self.ly.title("Partitioning a Group")

        # Show Z_6 elements on a circle
        z6_elements = [str(i) for i in range(6)]
        circle_radius = 1.8
        dots = VGroup()
        labels = VGroup()
        for i, elem in enumerate(z6_elements):
            angle = -PI / 2 + i * TAU / 6
            pos = circle_radius * np.array([np.cos(angle), np.sin(angle), 0])
            d = Dot(pos, color=PRIMARY, radius=0.15)
            t = Text(elem, font_size=LABEL_SIZE, color=WHITE, font=MONO).move_to(pos + UP * 0.35)
            dots.add(d)
            labels.add(t)

        self.ly.center_in_content(dots)
        self.play(*[Create(d) for d in dots], run_time=NORMAL)
        self.play(*[Write(t) for t in labels], run_time=FAST)
        self.wait(0.3)

        # Highlight subgroup {0, 3}
        highlight_h = VGroup(dots[0], dots[3], labels[0], labels[3])
        h_label = MathTex(r"H = \{0,\, 3\}", color=SECONDARY, font_size=28)
        self.ly.safe_place(h_label, anchor=dots, direction=DOWN, buff=0.5)
        self.play(
            highlight_h.animate.set_color(SECONDARY),
            Write(h_label),
            run_time=NORMAL,
        )
        self.wait(0.3)

        # Show coset 1+H = {1, 4}
        coset1 = VGroup(dots[1], dots[4], labels[1], labels[4])
        c1_label = MathTex(r"1+H = \{1,\, 4\}", color=ACCENT, font_size=28)
        self.ly.safe_place(c1_label, anchor=h_label, direction=DOWN, buff=0.3)
        self.play(
            coset1.animate.set_color(ACCENT),
            Write(c1_label),
            run_time=NORMAL,
        )
        self.wait(0.3)

        # Show coset 2+H = {2, 5}
        coset2 = VGroup(dots[2], dots[5], labels[2], labels[5])
        c2_label = MathTex(r"2+H = \{2,\, 5\}", color=RED, font_size=28)
        self.ly.safe_place(c2_label, anchor=c1_label, direction=DOWN, buff=0.3)
        self.play(
            coset2.animate.set_color(RED),
            Write(c2_label),
            run_time=NORMAL,
        )
        self.wait(0.3)

        # Bridge
        bridge = Text(
            "Three equal blocks, perfectly partition Z_6!",
            font_size=HEADING_SIZE, color=WHITE, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(bridge, anchor=c2_label, direction=DOWN, buff=0.4)
        self.play(FadeIn(bridge, scale=1.05), run_time=NORMAL)
        self.wait(15.7)  # pacing: extends seg0 caption slot (+15.2s)

        self.ly.clear()

    # --- Scene 2: Definition of Cosets ---

    def scene2_definition(self):
        self.ly.section_divider(2, "Definition of Cosets")
        self.add_subcaption(
            "Given a group G and a subgroup H, "
            "the left coset of H by g is the set gH, "
            "defined as everything you get by taking each element h of H and multiplying by g on the left. "
            "Formally, gH equals the set of g times h for all h in H. "
            "Similarly, the right coset Hg is the set of h times g for all h in H. "
            "In abelian groups, left and right cosets are always the same. "
            "The element g is called the representative of the coset gH.",
            duration=33.5,
        )

        title = self.ly.title("Left Cosets")

        defn_box = Text(
            "For H a subgroup of G and g in G:",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(defn_box, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(defn_box), run_time=NORMAL)
        self.wait(0.2)

        left_coset = MathTex(
            r"gH = \{gh : h \in H\}",
            color=PRIMARY, font_size=36,
        )
        self.ly.safe_place(left_coset, anchor=defn_box, direction=DOWN, buff=0.4)
        self.play(Write(left_coset), run_time=NORMAL)
        self.wait(0.2)

        right_coset = MathTex(
            r"Hg = \{hg : h \in H\}",
            color=SECONDARY, font_size=36,
        )
        self.ly.safe_place(right_coset, anchor=left_coset, direction=DOWN, buff=0.4)
        self.play(Write(right_coset), run_time=NORMAL)
        self.wait(0.3)

        # Explanation
        expl = Text(
            "gH: multiply every h in H by g on the LEFT",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(expl, anchor=right_coset, direction=DOWN, buff=0.4)
        self.play(FadeIn(expl, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.2)

        repr_note = Text(
            "g is called the REPRESENTATIVE of the coset gH",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(repr_note, anchor=expl, direction=DOWN, buff=0.35)
        self.play(FadeIn(repr_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        # Quick example
        self.ly.clear()

        title2 = self.ly.title("Quick Example in Z_6")

        h_set = MathTex(
            r"H = \{0,\, 3\}, \quad 1+H = \{1+0,\, 1+3\} = \{1,\, 4\}",
            color=WHITE, font_size=28,
        )
        self.ly.safe_place(h_set, anchor=title2, direction=DOWN, buff=0.5)
        self.play(Write(h_set), run_time=NORMAL)
        self.wait(0.3)

        h_set2 = MathTex(
            r"2+H = \{2+0,\, 2+3\} = \{2,\, 5\}",
            color=WHITE, font_size=28,
        )
        self.ly.safe_place(h_set2, anchor=h_set, direction=DOWN, buff=0.4)
        self.play(Write(h_set2), run_time=NORMAL)
        self.wait(0.3)

        note = Text(
            "Each coset has size |H| = 2",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, anchor=h_set2, direction=DOWN, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(21.2)  # pacing: extends seg1 caption slot (+20.7s, incl. +0.3 quantization margin)

        self.ly.clear()

    # --- Scene 3: Example -- Cosets in Z_6 ---

    def scene3_example_z6(self):
        self.ly.section_divider(3, "Example in Z_6")
        self.add_subcaption(
            "Let's work through a complete example. "
            "Take G equals Z six, the integers mod six under addition. "
            "Our subgroup is H equals the set containing zero and three, "
            "which is the cyclic group generated by three. "
            "Let's compute all six left cosets. "
            "Zero plus H gives H itself: zero and three. "
            "One plus H gives one and four. "
            "Two plus H gives two and five. "
            "Now here's the key observation. "
            "Three plus H gives three and zero, which is just H again. "
            "Four plus H gives four and one, which equals one plus H. "
            "And five plus H gives five and two, which equals two plus H. "
            "So even though we started with six elements, "
            "we only get three DISTINCT cosets, each of size two. "
            "This is no accident. It is Lagrange's Theorem in action.",
            duration=52.5,
        )

        title = self.ly.title("Example: Cosets in Z_6")

        group_def = MathTex(
            r"G = \mathbb{Z}_6 = \{0,1,2,3,4,5\}, \quad H = \{0,\,3\} = \langle 3 \rangle",
            color=WHITE, font_size=28,
        )
        self.ly.safe_place(group_def, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(group_def), run_time=NORMAL)
        self.wait(0.3)

        # Compute cosets one by one
        cosets_data = [
            (r"0 + H = \{0,\, 3\} = H", SECONDARY),
            (r"1 + H = \{1,\, 4\}", ACCENT),
            (r"2 + H = \{2,\, 5\}", RED),
        ]

        cosets_vg = VGroup()
        for tex_str, col in cosets_data:
            c = MathTex(tex_str, color=col, font_size=28)
            cosets_vg.add(c)

        cosets_vg.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.ly.safe_place(cosets_vg, anchor=group_def, direction=DOWN, buff=0.4)

        for c in cosets_vg:
            self.play(Write(c), run_time=FAST)
            self.wait(0.2)
        self.wait(0.3)

        # Show duplicates
        self.ly.clear()

        title2 = self.ly.title("Duplicates Collapse")

        dup1 = MathTex(
            r"3 + H = \{3,\, 0\} = 0 + H \quad \checkmark",
            color=SECONDARY, font_size=28,
        )
        self.ly.safe_place(dup1, anchor=title2, direction=DOWN, buff=0.5)
        self.play(Write(dup1), run_time=FAST)
        self.wait(0.15)

        dup2 = MathTex(
            r"4 + H = \{4,\, 1\} = 1 + H \quad \checkmark",
            color=ACCENT, font_size=28,
        )
        self.ly.safe_place(dup2, anchor=dup1, direction=DOWN, buff=0.3)
        self.play(Write(dup2), run_time=FAST)
        self.wait(0.15)

        dup3 = MathTex(
            r"5 + H = \{5,\, 2\} = 2 + H \quad \checkmark",
            color=RED, font_size=28,
        )
        self.ly.safe_place(dup3, anchor=dup2, direction=DOWN, buff=0.3)
        self.play(Write(dup3), run_time=FAST)
        self.wait(0.3)

        # Summary box
        summary = Text(
            "Only 3 distinct cosets, each of size 2",
            font_size=HEADING_SIZE, color=WHITE, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(summary, anchor=dup3, direction=DOWN, buff=0.4)
        self.play(FadeIn(summary, scale=1.05), run_time=NORMAL)
        self.wait(0.3)

        equation = MathTex(
            r"3 \times 2 = 6 = |\mathbb{Z}_6|",
            color=ACCENT, font_size=34,
        )
        self.ly.safe_place(equation, anchor=summary, direction=DOWN, buff=0.35)
        self.play(Write(equation), run_time=NORMAL)
        self.wait(41.8)  # pacing: extends seg2 caption slot (+41.3s)

        self.ly.clear()

    # --- Scene 4: Properties of Cosets ---

    def scene4_properties(self):
        self.ly.section_divider(4, "Properties of Cosets")
        self.add_subcaption(
            "Cosets have four key properties that make Lagrange's Theorem work. "
            "Property one: the element g is always in the coset gH, "
            "because g equals g times the identity, and the identity is in H. "
            "Property two: if two cosets gH and kH are equal, "
            "then g inverse times k is in H. "
            "Property three: two cosets are either identical or they are completely disjoint. "
            "They never partially overlap. "
            "Property four: every coset has the same size as H. "
            "The map sending h to g times h is a bijection, "
            "so it pairs up elements of H with elements of gH one to one.",
            duration=41.5,
        )

        title = self.ly.title("Key Properties of Cosets")

        # Properties 1 & 2
        props_12 = [
            MathTex(r"1.\; g \in gH", color=PRIMARY, font_size=28),
            MathTex(r"2.\; gH = kH \iff g^{-1}k \in H", color=PRIMARY, font_size=28),
        ]
        notes_12 = [
            Text("g = g \cdot e, and e \in H", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("cosets coincide iff reps differ by H", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        cards_12 = VGroup()
        for math_part, text_part in zip(props_12, notes_12):
            card_bg = Rectangle(
                width=10, height=0.9,
                color=PRIMARY, fill_opacity=0.08,
                stroke_width=1,
            )
            card_content = VGroup(math_part, text_part).arrange(RIGHT, buff=0.6)
            card = VGroup(card_bg, card_content).arrange(DOWN, buff=0.15)
            cards_12.add(card)
        cards_12.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.ly.safe_place(cards_12, anchor=title, direction=DOWN, buff=0.5)
        for card in cards_12:
            self.play(FadeIn(card), run_time=NORMAL)
            self.wait(0.25)
        self.wait(0.3)

        self.ly.clear()

        # Properties 3 & 4
        title2 = self.ly.title("Properties (continued)")
        props_34 = [
            MathTex(r"3.\; gH = kH \;\text{or}\;gH \cap kH = \emptyset",
                   color=PRIMARY, font_size=28),
            MathTex(r"4.\; |gH| = |H|", color=PRIMARY, font_size=28),
        ]
        notes_34 = [
            Text("cosets are equal OR disjoint (never overlap)", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("map h -> gh is a bijection", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        cards_34 = VGroup()
        for math_part, text_part in zip(props_34, notes_34):
            card_bg = Rectangle(
                width=10, height=0.9,
                color=PRIMARY, fill_opacity=0.08,
                stroke_width=1,
            )
            card_content = VGroup(math_part, text_part).arrange(RIGHT, buff=0.6)
            card = VGroup(card_bg, card_content).arrange(DOWN, buff=0.15)
            cards_34.add(card)
        cards_34.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.ly.safe_place(cards_34, anchor=title2, direction=DOWN, buff=0.5)
        for card in cards_34:
            self.play(FadeIn(card), run_time=NORMAL)
            self.wait(0.25)
        self.wait(33.2)  # pacing: extends seg3 caption slot (+32.7s)

        self.ly.clear()

    # --- Scene 5: Example -- Cosets in S_3 ---

    def scene5_example_s3(self):
        self.ly.section_divider(5, "Example in S_3")
        self.add_subcaption(
            "Now let's look at a non-abelian example. "
            "Take G equals S three, the symmetric group on three elements. "
            "It has six elements. "
            "Our subgroup H is A three, the alternating group, "
            "which consists of the even permutations: "
            "the identity e, the three-cycle one two three, and its inverse one three two. "
            "So H has order three. "
            "Let's compute the left cosets. "
            "The coset e times H is just H itself: e, one two three, and one three two. "
            "Now take the transposition one two times H. "
            "Multiplying one two by each element of H gives us "
            "one two, one three, and two three. "
            "That's our second coset. "
            "We can verify that the other transpositions give duplicates. "
            "So we have exactly two distinct cosets, "
            "each of size three, and two times three equals six, which is the order of S three.",
            duration=56.3,
        )

        title = self.ly.title("Example: Cosets in S_3")

        group_def = MathTex(
            r"G = S_3, \quad |G| = 6",
            color=WHITE, font_size=30,
        )
        self.ly.safe_place(group_def, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(group_def), run_time=NORMAL)
        self.wait(0.2)

        h_def = MathTex(
            r"H = A_3 = \{e,\; (123),\; (132)\}, \quad |H| = 3",
            color=SECONDARY, font_size=28,
        )
        self.ly.safe_place(h_def, anchor=group_def, direction=DOWN, buff=0.35)
        self.play(Write(h_def), run_time=NORMAL)
        self.wait(0.3)

        self.ly.clear()

        title2 = self.ly.title("Computing the Cosets")

        coset1_title = MathTex(
            r"eH = H = \{e,\; (123),\; (132)\}",
            color=SECONDARY, font_size=28,
        )
        self.ly.safe_place(coset1_title, anchor=title2, direction=DOWN, buff=0.5)
        self.play(Write(coset1_title), run_time=NORMAL)
        self.wait(0.2)

        coset2_title = MathTex(
            r"(12)H = \{(12),\; (12)(123),\; (12)(132)\}",
            color=ACCENT, font_size=26,
        )
        self.ly.safe_place(coset2_title, anchor=coset1_title, direction=DOWN, buff=0.35)
        self.play(Write(coset2_title), run_time=NORMAL)
        self.wait(0.2)

        # Simplify
        coset2_simplified = MathTex(
            r"\;\;= \{(12),\; (13),\; (23)\}",
            color=ACCENT, font_size=28,
        )
        self.ly.safe_place(coset2_simplified, anchor=coset2_title, direction=DOWN, buff=0.25)
        self.play(Write(coset2_simplified), run_time=FAST)
        self.wait(0.3)

        # Check others
        check_note = Text(
            "Verifying: (13)H and (23)H give duplicates",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(check_note, anchor=coset2_simplified, direction=DOWN, buff=0.35)
        self.play(FadeIn(check_note, shift=LEFT * 0.1), run_time=FAST)
        self.wait(0.3)

        # Summary
        summary = Text(
            "2 distinct cosets, each of size 3",
            font_size=HEADING_SIZE, color=WHITE, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(summary, anchor=check_note, direction=DOWN, buff=0.35)
        self.play(FadeIn(summary, scale=1.05), run_time=NORMAL)
        self.wait(0.2)

        equation = MathTex(
            r"2 \times 3 = 6 = |S_3|",
            color=ACCENT, font_size=34,
        )
        self.ly.safe_place(equation, anchor=summary, direction=DOWN, buff=0.35)
        self.play(Write(equation), run_time=NORMAL)
        self.wait(45.0)  # pacing: extends seg4 caption slot (+44.5s)

        self.ly.clear()

    # --- Scene 6: Lagrange's Theorem Statement ---

    def scene6_lagrange_statement(self):
        self.ly.section_divider(6, "Lagrange's Theorem")
        self.add_subcaption(
            "We are now ready for one of the most important theorems in finite group theory. "
            "Lagrange's Theorem states: if H is a subgroup of a finite group G, "
            "then the order of H divides the order of G. "
            "We define the index of H in G, "
            "written with square brackets G colon H, "
            "as the number of distinct left cosets of H in G. "
            "Then the theorem says the order of G "
            "equals the index times the order of H. "
            "In our Z six example, the index was three, "
            "the order of H was two, and three times two equals six. "
            "In S three, the index was two, the order of H was three, "
            "and two times three equals six. "
            "This theorem is named after Joseph Louis Lagrange, "
            "who worked in the seventeen hundreds.",
            duration=47.3,
        )

        title = self.ly.title("Lagrange's Theorem")

        # The theorem box
        theorem_bg = Rectangle(
            width=11, height=1.8,
            color=ACCENT, fill_opacity=0.1,
            stroke_width=2,
        )
        self.ly.center_in_content(theorem_bg)

        theorem_text = MathTex(
            r"\textbf{Theorem. } \; H \leq G \implies |H| \;\Big|\; |G|",
            color=WHITE, font_size=30,
        ).move_to(theorem_bg)

        self.play(
            FadeIn(theorem_bg),
            Write(theorem_text),
            run_time=NORMAL,
        )
        self.wait(0.3)

        # Index definition
        self.ly.clear()

        title2 = self.ly.title("The Index")

        index_def = MathTex(
            r"[G : H] = \text{number of distinct cosets of } H \text{ in } G",
            color=WHITE, font_size=26,
        )
        self.ly.safe_place(index_def, anchor=title2, direction=DOWN, buff=0.5)
        self.play(Write(index_def), run_time=NORMAL)
        self.wait(0.2)

        formula = MathTex(
            r"|G| = [G : H] \cdot |H|",
            color=ACCENT, font_size=38,
        )
        boxed_formula = self.ly.formula_box(formula)
        self.ly.safe_place(boxed_formula, anchor=index_def, direction=DOWN, buff=0.5)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(0.3)

        # Examples
        ex1 = MathTex(
            r"\mathbb{Z}_6:\; [G:H] = 3,\; |H|=2 \implies 3 \times 2 = 6\; \checkmark",
            color=SECONDARY, font_size=24,
        )
        self.ly.safe_place(ex1, anchor=formula, direction=DOWN, buff=0.4)
        self.play(Write(ex1), run_time=FAST)
        self.wait(0.15)

        ex2 = MathTex(
            r"S_3:\; [G:H] = 2,\; |H|=3 \implies 2 \times 3 = 6\; \checkmark",
            color=SECONDARY, font_size=24,
        )
        self.ly.safe_place(ex2, anchor=ex1, direction=DOWN, buff=0.3)
        self.play(Write(ex2), run_time=FAST)
        self.wait(0.3)

        # Historical note
        hist = Text(
            "Joseph-Louis Lagrange (1736 - 1813)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(hist, anchor=ex2, direction=DOWN, buff=0.4)
        self.play(FadeIn(hist, shift=LEFT * 0.1), run_time=FAST)
        self.wait(39.1)  # pacing: extends seg5 caption slot (+38.6s, incl. +0.3 quantization margin)

        self.ly.clear()

    # --- Scene 7: Proof Sketch ---

    def scene7_proof(self):
        self.ly.section_divider(7, "Proof")
        self.add_subcaption(
            "The proof of Lagrange's Theorem is remarkably short. "
            "It uses three observations. "
            "Step one: the cosets of H partition G. "
            "By property three, any two cosets are either equal or disjoint. "
            "And every element g of G belongs to the coset gH by property one. "
            "So the cosets cover all of G without overlap. "
            "Step two: every coset has the same size as H. "
            "Property four tells us that the map sending h to g times h "
            "is a bijection, so the coset gH has exactly as many elements as H. "
            "Step three: count. "
            "If there are index of G colon H distinct cosets, "
            "and each has size H, "
            "then the total number of elements is index times H, "
            "which equals the order of G. Done!",
            duration=49.4,
        )

        title = self.ly.title("Proof of Lagrange's Theorem")

        # Step 1
        step1_label = MathTex(
            r"\text{Step 1: Cosets partition } G",
            color=PRIMARY, font_size=28,
        )
        self.ly.safe_place(step1_label, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(step1_label), run_time=FAST)
        self.wait(0.1)

        step1_detail = Text(
            "Every g in G lies in gH (Property 1).\n"
            "Two cosets are equal or disjoint (Property 3).\n"
            "=> Cosets cover G without overlap.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(step1_detail, anchor=step1_label, direction=DOWN, buff=0.35)
        self.play(FadeIn(step1_detail, shift=LEFT * 0.1), run_time=NORMAL)
        self.wait(0.3)

        self.ly.clear()

        # Step 2
        title2 = self.ly.title("Proof (continued)")

        step2_label = MathTex(
            r"\text{Step 2: Every coset has size } |H|",
            color=SECONDARY, font_size=28,
        )
        self.ly.safe_place(step2_label, anchor=title2, direction=DOWN, buff=0.5)
        self.play(Write(step2_label), run_time=FAST)
        self.wait(0.1)

        step2_detail = Text(
            "The map h -> gh is a bijection (Property 4).\n"
            "=> |gH| = |H| for every coset.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(step2_detail, anchor=step2_label, direction=DOWN, buff=0.35)
        self.play(FadeIn(step2_detail, shift=LEFT * 0.1), run_time=NORMAL)
        self.wait(0.3)

        self.ly.clear()

        # Step 3
        title3 = self.ly.title("Proof (conclusion)")

        step3_label = MathTex(
            r"\text{Step 3: Count}",
            color=ACCENT, font_size=28,
        )
        self.ly.safe_place(step3_label, anchor=title3, direction=DOWN, buff=0.5)
        self.play(Write(step3_label), run_time=FAST)
        self.wait(0.1)

        counting = MathTex(
            r"[G:H] \text{ cosets, each of size } |H| "
            r"\implies |G| = [G:H] \cdot |H|",
            color=WHITE, font_size=28,
        )
        self.ly.safe_place(counting, anchor=step3_label, direction=DOWN, buff=0.4)
        self.play(Write(counting), run_time=NORMAL)
        self.wait(0.2)

        done_label = MathTex(
            r"\blacksquare",
            color=SECONDARY, font_size=40,
        )
        self.ly.safe_place(done_label, anchor=counting, direction=DOWN, buff=0.4)
        self.play(FadeIn(done_label, scale=1.2), run_time=FAST)
        self.wait(0.2)

        remark = Text(
            "The proof is remarkably short — three observations, and we're done.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(remark, anchor=done_label, direction=DOWN, buff=0.4)
        self.play(FadeIn(remark, shift=LEFT * 0.1), run_time=FAST)
        self.wait(38.6)  # pacing: extends seg6 caption slot (+38.1s, incl. +0.3 quantization margin)

        self.ly.clear()

    # --- Scene 8: Applications ---

    def scene8_applications(self):
        self.ly.section_divider(8, "Applications")
        self.add_subcaption(
            "Lagrange's Theorem has beautiful applications. "
            "Application one: the order of any element divides the order of the group. "
            "The cyclic subgroup generated by g has order equal to the order of g. "
            "Since this is a subgroup, Lagrange says its order divides the order of G. "
            "Application two: every group of prime order is cyclic. "
            "If the order of G is a prime p, "
            "then for any non-identity element g, "
            "the order of g must divide p and be greater than one. "
            "So the order of g equals p, "
            "meaning the cyclic subgroup generated by g is all of G. "
            "There is essentially only one group of prime order up to isomorphism: "
            "the cyclic group. "
            "Application three: as a teaser, "
            "Lagrange's Theorem gives us a clean proof of Fermat's Little Theorem, "
            "that a to the power p minus one is congruent to one mod p. "
            "We will see this connection when we study group homomorphisms.",
            duration=59.4,
        )

        title = self.ly.title("Applications")

        # App 1
        app1_label = MathTex(
            r"1.\; \text{Order of an element divides } |G|",
            color=PRIMARY, font_size=26,
        )
        self.ly.safe_place(app1_label, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(app1_label), run_time=FAST)
        self.wait(0.1)

        app1_detail = MathTex(
            r"\langle g \rangle \leq G \implies |\langle g \rangle| \;\Big|\; |G| \implies \text{ord}(g) \;\Big|\; |G|",
            color=WHITE, font_size=24,
        )
        self.ly.safe_place(app1_detail, anchor=app1_label, direction=DOWN, buff=0.35)
        self.play(Write(app1_detail), run_time=NORMAL)
        self.wait(0.3)

        self.ly.clear()

        # App 2
        title2 = self.ly.title("Applications (continued)")

        app2_label = MathTex(
            r"2.\; \text{Groups of prime order are cyclic}",
            color=SECONDARY, font_size=26,
        )
        self.ly.safe_place(app2_label, anchor=title2, direction=DOWN, buff=0.5)
        self.play(Write(app2_label), run_time=FAST)
        self.wait(0.1)

        app2_detail = Text(
            "If |G| = p (prime), for any g != e:\n"
            "  ord(g) divides p and ord(g) > 1\n"
            "  => ord(g) = p => <g> = G",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(app2_detail, anchor=app2_label, direction=DOWN, buff=0.35)
        self.play(FadeIn(app2_detail, shift=LEFT * 0.1), run_time=NORMAL)
        self.wait(0.2)

        app2_conclusion = Text(
            "There is essentially only one group of prime order: Z_p",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(app2_conclusion, anchor=app2_detail, direction=DOWN, buff=0.35)
        self.play(FadeIn(app2_conclusion, shift=LEFT * 0.1), run_time=FAST)
        self.wait(0.3)

        self.ly.clear()

        # App 3
        title3 = self.ly.title("Application: Fermat's Little Theorem")

        app3_text = MathTex(
            r"a^{p-1} \equiv 1 \pmod{p}",
            color=PRIMARY, font_size=34,
        )
        self.ly.safe_place(app3_text, anchor=title3, direction=DOWN, buff=0.5)
        self.play(Write(app3_text), run_time=NORMAL)
        self.wait(0.2)

        teaser = Text(
            "Lagrange's Theorem gives a clean proof!\n"
            "(Connection via group homomorphisms -- coming soon)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(teaser, anchor=app3_text, direction=DOWN, buff=0.4)
        self.play(FadeIn(teaser, shift=LEFT * 0.1), run_time=FAST)
        self.wait(52.8)  # pacing: extends seg7 caption slot (+52.3s)

        self.ly.clear()

    # --- Scene 9: Summary + Outro ---

    def scene9_summary(self):
        self.add_subcaption(
            "Let's summarize what we learned today. "
            "A left coset gH shifts the subgroup H by the element g. "
            "The cosets of H partition G into equal size blocks. "
            "Lagrange's Theorem states that the order of H divides the order of G. "
            "The index of H in G equals the order of G divided by the order of H, "
            "and it counts the number of cosets. "
            "The order of any element divides the order of the group. "
            "And every group of prime order is cyclic. "
            "Next time, we study group homomorphisms, "
            "the structure preserving maps between groups.",
            duration=35.2,
        )
        play_outro(self, "Cosets and Lagrange's Theorem", "Abstract Algebra I")

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text("1. A left coset gH shifts subgroup H by g", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. Cosets partition G into equal-size blocks", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3. Lagrange's Theorem: |H| divides |G|", font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD),
            Text("4. The index [G:H] = |G|/|H| counts the cosets", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5. Order of any element divides |G|", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]

        self.ly.progressive_reveal(takeaways, start_from=title)

        self.wait(0.5)

        # Preview
        self.ly.clear()
        title2 = self.ly.title("Coming Next")

        preview = Text(
            "Group Homomorphisms:\n"
            "Structure-Preserving Maps Between Groups",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(preview, anchor=title2, direction=DOWN, buff=0.5)
        self.play(FadeIn(preview, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(19.7)  # pacing: extends seg8 caption slot (+19.2s)

        self.ly.clear()
