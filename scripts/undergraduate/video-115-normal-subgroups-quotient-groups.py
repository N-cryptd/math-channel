"""Video 115: Normal Subgroups and Quotient Groups
TEMPLATE v2 -- Professional quality Manim script

Playlist: Abstract Algebra I (Video 5 of 12)
Class: Video115_NormalSubgroupsQuotientGroups
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


class Video115_NormalSubgroupsQuotientGroups(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_prototype()
        self.scene3_when_things_break()
        self.scene4_definition()
        self.scene5_equivalent_conditions()
        self.scene6_quotient_group()
        self.scene7_example_s3()
        self.scene8_summary()

    # --- Scene 1: Hook — When Do Cosets Form a Group? ---

    def scene1_hook(self):
        self.add_subcaption(
            "In the last video, we saw that cosets partition a group "
            "into equal-sized blocks. "
            "A natural question arises. "
            "Can we make these blocks into a group themselves? "
            "If we could multiply blocks together, we'd get a brand new group "
            "built from pieces of the original. "
            "But this doesn't always work. "
            "It requires something special about the subgroup.",
            duration=28,
        )
        play_intro(self, "Normal Subgroups and Quotient Groups", "Abstract Algebra I")

        title = self.ly.title("When Do Cosets Form a Group?")

        items = [
            Text("Cosets partition G into equal-size blocks", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Can these blocks form a GROUP?", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD),
            Text("We need: (aH)(bH) = (ab)H", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("This requires H to be 'normal'", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.3)
        self.ly.clear()

    # --- Scene 2: The Prototype — Z/nZ ---

    def scene2_prototype(self):
        self.add_subcaption(
            "Let's start with a familiar example. "
            "Consider the integers under addition, Z, "
            "and the subgroup n Z, all multiples of n. "
            "The cosets are the congruence classes modulo n. "
            "And they form a group called Z over n Z. "
            "The key property here is that adding cosets is well-defined. "
            "It doesn't matter which representative you pick. "
            "Zero plus one equals one, whether you use zero or seven "
            "as the representative of zero's class.",
            duration=30,
        )
        self.ly.section_divider(1, "The Prototype")

        title = self.ly.title("Modular Arithmetic as a Quotient Group")

        # Show Z and nZ
        g_label = MathTex(r"\mathbb{Z}", color=PRIMARY, font_size=38)
        h_label = MathTex(r"n\mathbb{Z} = \{..., -2n, -n, 0, n, 2n, ...\}", color=SECONDARY, font_size=28)
        self.ly.safe_place(g_label, anchor=title, direction=DOWN, buff=0.5)
        self.ly.safe_place(h_label, anchor=g_label, direction=DOWN, buff=0.4)
        self.play(Write(g_label), run_time=FAST)
        self.play(Write(h_label), run_time=NORMAL)
        self.wait(0.3)

        # Show cosets
        coset_text = MathTex(
            r"[0] = n\mathbb{Z}, \quad [1] = 1 + n\mathbb{Z}, \quad ..., \quad [n{-}1]",
            color=WHITE, font_size=26,
        )
        self.ly.safe_place(coset_text, anchor=h_label, direction=DOWN, buff=0.5)
        self.play(Write(coset_text), run_time=NORMAL)
        self.wait(0.3)

        # The quotient group
        boxed_q = self.ly.formula_box(
            MathTex(r"\mathbb{Z}/n\mathbb{Z}", color=ACCENT, font_size=36),
            color=ACCENT,
        )
        self.ly.safe_place(boxed_q, anchor=coset_text, direction=DOWN, buff=0.5)
        self.play(Write(boxed_q[0]), Create(boxed_q[1]), run_time=NORMAL)
        self.wait(0.3)

        # Well-definedness
        well_def = MathTex(
            r"[a] + [b] = [a + b]",
            color=WHITE, font_size=30,
        )
        note = Text(
            "(doesn't depend on representatives)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(well_def, anchor=boxed_q, direction=DOWN, buff=0.5)
        self.ly.safe_place(note, anchor=well_def, direction=DOWN, buff=0.2)
        self.play(Write(well_def), FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 3: What Can Go Wrong? ---

    def scene3_when_things_break(self):
        self.add_subcaption(
            "Now let's see what happens when things go wrong. "
            "Consider S 3, the symmetric group on three elements. "
            "Take H to be the subgroup containing just the identity "
            "and the transposition one two. "
            "Let's compute the left cosets and the right cosets. "
            "One three times H gives one three and one three two. "
            "But H times one three gives one three and one two three. "
            "These are different sets. "
            "The left and right cosets don't agree. "
            "If we tried to multiply cosets, the result would depend "
            "on which representative we choose.",
            duration=35,
        )
        self.ly.section_divider(2, "When Things Break")

        title = self.ly.title("S_3: Left and Right Cosets Disagree")

        # H
        h_text = MathTex(
            r"H = \{e, (12)\} \subset S_3",
            color=SECONDARY, font_size=30,
        )
        self.ly.safe_place(h_text, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(h_text), run_time=NORMAL)
        self.wait(0.3)

        # Left coset
        left_coset = MathTex(
            r"(13)H = \{(13),\, (132)\}",
            color=PRIMARY, font_size=28,
        )
        self.ly.safe_place(left_coset, anchor=h_text, direction=DOWN, buff=0.5)
        self.play(Write(left_coset), run_time=NORMAL)
        self.wait(0.3)

        # Right coset (different!)
        right_coset = MathTex(
            r"H(13) = \{(13),\, (123)\}",
            color=RED, font_size=28,
        )
        self.ly.safe_place(right_coset, anchor=left_coset, direction=DOWN, buff=0.4)
        self.play(Write(right_coset), run_time=NORMAL)
        self.wait(0.3)

        # Not equal
        not_eq = MathTex(
            r"(13)H \neq H(13)",
            color=RED, font_size=32,
        )
        self.ly.safe_place(not_eq, anchor=right_coset, direction=DOWN, buff=0.4)
        self.play(Write(not_eq), run_time=FAST)
        self.wait(0.3)

        # Conclusion
        bad_news = Text(
            "Coset multiplication would be ILL-DEFINED",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(bad_news, anchor=not_eq, direction=DOWN, buff=0.4)
        self.play(FadeIn(bad_news, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 4: Definition of Normal Subgroup ---

    def scene4_definition(self):
        self.add_subcaption(
            "A subgroup H is called normal in G "
            "if the left and right cosets always agree. "
            "That is, g H equals H g for every element g in G. "
            "We write this as H triangle G. "
            "An equivalent condition is that conjugation by any element "
            "of G sends H back into itself. "
            "That is, g h g inverse is in H for every g in G and h in H. "
            "This is the conjugation perspective, "
            "and it's often the most useful way to check normality.",
            duration=28,
        )
        self.ly.section_divider(3, "Normal Subgroups")

        title = self.ly.title("Definition: Normal Subgroup")

        # Main definition
        def1 = MathTex(
            r"H \triangleleft G",
            color=ACCENT, font_size=36,
        )
        iff = MathTex(
            r"\iff",
            color=WHITE, font_size=30,
        )
        def1b = MathTex(
            r"gH = Hg \quad \forall\, g \in G",
            color=WHITE, font_size=28,
        )
        self.ly.safe_place(def1, anchor=title, direction=DOWN, buff=0.5)
        self.ly.safe_place(iff, anchor=def1, direction=DOWN, buff=0.3)
        self.ly.safe_place(def1b, anchor=iff, direction=DOWN, buff=0.3)
        self.play(Write(def1), run_time=FAST)
        self.play(Write(iff), Write(def1b), run_time=NORMAL)
        self.wait(0.3)

        # Conjugation condition
        conj_label = Text(
            "Conjugation perspective:",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        conj_def = MathTex(
            r"gHg^{-1} \subseteq H \quad \forall\, g \in G",
            color=PRIMARY, font_size=28,
        )
        boxed_conj = self.ly.formula_box(conj_def, color=PRIMARY)
        self.ly.safe_place(conj_label, anchor=def1b, direction=DOWN, buff=0.5)
        self.ly.safe_place(boxed_conj, anchor=conj_label, direction=DOWN, buff=0.3)
        self.play(FadeIn(conj_label, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(conj_def), Create(boxed_conj[1]), run_time=NORMAL)
        self.wait(0.3)

        # Note about meaning
        meaning = Text(
            "Normal = left cosets = right cosets = conjugation closed",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(meaning, anchor=boxed_conj, direction=DOWN, buff=0.4)
        self.play(FadeIn(meaning, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 5: Equivalent Conditions ---

    def scene5_equivalent_conditions(self):
        self.add_subcaption(
            "There are several equivalent ways to characterize normal subgroups. "
            "First: g H equals H g for all g. "
            "Second: the conjugate g h g inverse stays in H. "
            "Third: conjugation by g actually preserves H exactly, "
            "not just a subset. These are equivalent because "
            "conjugation by g is a bijection on G. "
            "A key consequence: in abelian groups, "
            "every subgroup is normal, "
            "because commuting means g H equals H g trivially.",
            duration=28,
        )
        self.ly.section_divider(4, "Equivalent Conditions")

        title = self.ly.title("H is Normal iff...")

        conditions = [
            MathTex(r"1.\; gH = Hg \;\;\forall\, g", color=PRIMARY, font_size=26),
            MathTex(r"2.\; gHg^{-1} \subseteq H \;\;\forall\, g", color=PRIMARY, font_size=26),
            MathTex(r"3.\; gHg^{-1} = H \;\;\forall\, g", color=PRIMARY, font_size=26),
            Text("4. Every left coset is a right coset", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(conditions, start_from=title, run_time=0.7)
        self.wait(0.3)

        # Why 2 ↔ 3
        why = Text(
            "2 ↔ 3: conjugation by g is a bijection, so same size",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(why, anchor=conditions[-1], direction=DOWN, buff=0.3)
        self.play(FadeIn(why, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        self.ly.clear()

        # Abelian fact
        title2 = self.ly.title("Abelian Groups: Always Normal")

        abel_stmt = MathTex(
            r"G \text{ abelian } \implies H \triangleleft G",
            color=SECONDARY, font_size=30,
        )
        boxed_abel = self.ly.formula_box(abel_stmt, color=SECONDARY)

        reason = Text(
            "Proof: gh = hg for all g, h, so gH = Hg trivially",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(boxed_abel, anchor=title2, direction=DOWN, buff=0.5)
        self.ly.safe_place(reason, anchor=boxed_abel, direction=DOWN, buff=0.4)
        self.play(Write(abel_stmt), Create(boxed_abel[1]), run_time=NORMAL)
        self.play(FadeIn(reason, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 6: The Quotient Group G/H ---

    def scene6_quotient_group(self):
        self.add_subcaption(
            "Now for the main event. "
            "If H is normal in G, then the set of all cosets "
            "forms a group called the quotient group G over H. "
            "The elements are the cosets themselves. "
            "The operation is multiplication of cosets: "
            "a H times b H equals a b H. "
            "The identity is the coset e H, which is just H itself. "
            "The inverse of a H is a inverse H. "
            "And the order of G over H is the index of H in G, "
            "which by Lagrange's theorem equals the order of G "
            "divided by the order of H.",
            duration=32,
        )
        self.ly.section_divider(5, "The Quotient Group")

        title = self.ly.title("Definition: G/H")

        # Main definition
        elements = MathTex(
            r"G/H = \{gH : g \in G\}",
            color=PRIMARY, font_size=30,
        )
        operation = MathTex(
            r"(aH)(bH) = (ab)H",
            color=ACCENT, font_size=32,
        )
        boxed_op = self.ly.formula_box(operation, color=ACCENT)
        self.ly.safe_place(elements, anchor=title, direction=DOWN, buff=0.5)
        self.ly.safe_place(boxed_op, anchor=elements, direction=DOWN, buff=0.4)
        self.play(Write(elements), run_time=NORMAL)
        self.play(Write(operation), Create(boxed_op[1]), run_time=NORMAL)
        self.wait(0.3)

        # Group axioms
        axioms = [
            Text("Identity: eH = H", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Inverse: (aH)^{-1} = a^{-1}H", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Associativity: inherited from G", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(axioms, start_from=boxed_op, run_time=0.6)
        self.wait(0.3)

        self.ly.clear()

        # Order of G/H
        title2 = self.ly.title("Order of the Quotient Group")

        order_formula = MathTex(
            r"|G/H| = [G:H] = \frac{|G|}{|H|}",
            color=SECONDARY, font_size=32,
        )
        boxed_order = self.ly.formula_box(order_formula, color=SECONDARY)
        note = Text(
            "Follows from Lagrange's Theorem",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(boxed_order, anchor=title2, direction=DOWN, buff=0.5)
        self.ly.safe_place(note, anchor=boxed_order, direction=DOWN, buff=0.3)
        self.play(Write(order_formula), Create(boxed_order[1]), run_time=NORMAL)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 7: Example — S_3 / A_3 ---

    def scene7_example_s3(self):
        self.add_subcaption(
            "Let's work through our canonical example. "
            "G equals S 3 and H equals A 3, "
            "the alternating group of even permutations. "
            "A 3 contains the identity, the cycle one two three, "
            "and the cycle one three two. "
            "Since A 3 has index two in S 3, "
            "it's automatically normal. "
            "There are only two cosets: A 3 itself, "
            "and one two times A 3, the odd permutations. "
            "The quotient group S 3 over A 3 "
            "is isomorphic to Z over 2 Z, "
            "a two-element group that captures "
            "the parity structure of permutations.",
            duration=35,
        )
        self.ly.section_divider(6, "Example: S_3 / A_3")

        title = self.ly.title("S_3 / A_3")

        # Define A_3
        a3 = MathTex(
            r"A_3 = \{e, (123), (132)\}",
            color=SECONDARY, font_size=28,
        )
        self.ly.safe_place(a3, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(a3), run_time=NORMAL)
        self.wait(0.2)

        # Two cosets
        cosets = MathTex(
            r"S_3 / A_3 = \{\, A_3, \;\; (12)A_3 \,\}",
            color=WHITE, font_size=28,
        )
        self.ly.safe_place(cosets, anchor=a3, direction=DOWN, buff=0.4)
        self.play(Write(cosets), run_time=NORMAL)
        self.wait(0.2)

        # Index 2 note
        idx2 = Text(
            "Index 2 ⟹ A_3 is normal in S_3",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(idx2, anchor=cosets, direction=DOWN, buff=0.4)
        self.play(FadeIn(idx2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        self.ly.clear()

        # Multiplication table
        title2 = self.ly.title("Multiplication Table")

        header_left = MathTex(r"\cdot", color=DIM, font_size=26)
        header_a3 = MathTex(r"A_3", color=SECONDARY, font_size=26)
        header_odd = MathTex(r"(12)A_3", color=PRIMARY, font_size=26)

        row1_label = MathTex(r"A_3", color=SECONDARY, font_size=26)
        row1_vals = MathTex(r"A_3", color=SECONDARY, font_size=26)
        row1_plus = MathTex(r"(12)A_3", color=PRIMARY, font_size=26)

        row2_label = MathTex(r"(12)A_3", color=PRIMARY, font_size=26)
        row2_vals = MathTex(r"(12)A_3", color=PRIMARY, font_size=26)
        row2_plus = MathTex(r"A_3", color=SECONDARY, font_size=26)

        # Layout as a 3x3 grid manually using VGroup
        col_gap = 1.4
        row_gap = 0.5

        # Row 0: headers
        h0 = VGroup(header_left, header_a3, header_odd).arrange(RIGHT, buff=col_gap)

        # Row 1
        r1l = row1_label.copy()
        r1a = row1_vals.copy()
        r1b = row1_plus.copy()
        h1 = VGroup(r1l, r1a, r1b).arrange(RIGHT, buff=col_gap)

        # Row 2
        r2l = row2_label.copy()
        r2a = row2_vals.copy()
        r2b = row2_plus.copy()
        h2 = VGroup(r2l, r2a, r2b).arrange(RIGHT, buff=col_gap)

        table = VGroup(h0, h1, h2).arrange(DOWN, buff=row_gap)
        table.move_to(ORIGIN + UP * 0.3)

        # Fade in table row by row
        self.play(FadeIn(table[0]), run_time=FAST)
        self.play(FadeIn(table[1]), run_time=FAST)
        self.play(FadeIn(table[2]), run_time=FAST)
        self.wait(0.3)

        # Isomorphism
        iso = MathTex(
            r"S_3 / A_3 \cong \mathbb{Z}/2\mathbb{Z}",
            color=ACCENT, font_size=30,
        )
        self.ly.safe_place(iso, anchor=table, direction=DOWN, buff=0.5)
        self.play(Write(iso), run_time=NORMAL)
        self.wait(0.3)

        # Interpretation
        interp = Text(
            "Even + Even = Even | Even + Odd = Odd | Odd + Odd = Even",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(interp, anchor=iso, direction=DOWN, buff=0.3)
        self.play(FadeIn(interp, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 8: Summary + Outro ---

    def scene8_summary(self):
        self.add_subcaption(
            "Let's recap what we've learned. "
            "A normal subgroup has g H equals H g for all g in G. "
            "Normality is exactly what we need for coset multiplication "
            "to be well-defined. "
            "The quotient group G over H has cosets as its elements. "
            "Z over n Z is our motivating prototype. "
            "And in abelian groups, every subgroup is normal. "
            "Next time, we'll explore group homomorphisms, "
            "the structure-preserving maps between groups.",
            duration=25,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text("1. Normal: gH = Hg for all g in G", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Normality makes coset multiplication well-defined", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3. G/H has cosets as elements", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("4. Z/nZ is the motivating prototype", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("5. Every subgroup of an abelian group is normal", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title, run_time=0.6)
        self.wait(0.3)

        closing = Text(
            "Next: Group Homomorphisms",
            font_size=HEADING_SIZE, color=WHITE, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(closing, anchor=takeaways[-1], direction=DOWN, buff=0.5)
        clamp_position(closing)
        self.play(FadeIn(closing, scale=1.05), run_time=NORMAL)
        self.wait(0.5)

        play_outro(self, "Normal Subgroups and Quotient Groups", "Abstract Algebra I")
