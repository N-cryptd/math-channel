"""Video 117: Isomorphism Theorems
TEMPLATE v2 -- Professional quality Manim script

Playlist: Abstract Algebra I (Video 7 of 12)
Class: Video117_IsomorphismTheorems

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


class Video117_IsomorphismTheorems(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_recap()
        self.scene3_first_intuition()
        self.scene4_first_statement_proof()
        self.scene5_first_examples()
        self.scene6_second_motivation_statement()
        self.scene7_second_proof()
        self.scene8_third_theorem()
        self.scene9_unifying_theme()
        self.scene10_summary()

    # --- Scene 1: Hook ---

    def scene1_hook(self):
        self.add_subcaption(
            "In the last video, we studied homomorphisms: "
            "functions between groups that preserve the group operation. "
            "Today we see the deepest connection in basic group theory. "
            "If you quotient a group by the kernel of a homomorphism, "
            "you get a group isomorphic to the image. "
            "This is the First Isomorphism Theorem, "
            "and it has two powerful consequences. "
            "This is Abstract Algebra, Video 7.",
            duration=27.0,  # pacing: 1.08x natural 24.74 + 0.3
        )
        play_intro(self, "Isomorphism Theorems", "Abstract Algebra I")

        title = self.ly.title("The Deepest Connection in Group Theory")

        items = [
            Text("Homomorphism  phi : G -> H", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Kernel  ker(phi)  collapses to identity", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Image  im(phi)  captures what gets hit", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.6)
        self.wait(0.3)

        # Big payoff statement
        payoff = MathTex(
            r"G / \ker(\varphi) \cong \operatorname{im}(\varphi)",
            color=ACCENT, font_size=36,
        )
        boxed = self.ly.formula_box(payoff, color=ACCENT)
        self.play(FadeOut(items[0]), run_time=FAST)
        self.ly.safe_place(boxed, anchor=items[-1], direction=DOWN, buff=0.5)
        self.play(Write(payoff), Create(boxed[1]), run_time=NORMAL)
        self.wait(18.0)  # pacing: extends previous caption slot (Δ=17.5)

        self.ly.clear()

    # --- Scene 2: Recap ---

    def scene2_recap(self):
        self.add_subcaption(
            "Before we prove this theorem, let us recall three key facts "
            "from the last video about homomorphisms. "
            "First, a homomorphism phi from G to H preserves operations: "
            "phi of a b equals phi of a times phi of b. "
            "Second, the kernel consists of all elements "
            "that map to the identity in H. "
            "The kernel is always a normal subgroup of G. "
            "Third, the image is the set of all elements in H "
            "that actually get hit by phi. "
            "The image is always a subgroup of H.",
            duration=34.8,  # pacing: 1.08x natural 31.90 + 0.3
        )

        title = self.ly.title("Recap: Homomorphisms")

        recap_items = [
            MathTex(
                r"\varphi(ab) = \varphi(a)\,\varphi(b)",
                color=PRIMARY, font_size=32,
            ),
            MathTex(
                r"\ker(\varphi) = \{g \in G : \varphi(g) = e_H\}",
                color=RED, font_size=30,
            ),
            MathTex(
                r"\operatorname{im}(\varphi) = \{\varphi(g) : g \in G\}",
                color=SECONDARY, font_size=30,
            ),
        ]

        labels = [
            Text("Preserves the operation", font_size=SMALL_SIZE, color=PRIMARY, font=SANS),
            Text("Always a normal subgroup", font_size=SMALL_SIZE, color=RED, font=SANS),
            Text("Always a subgroup", font_size=SMALL_SIZE, color=SECONDARY, font=SANS),
        ]

        # Show first fact with label
        self.ly.safe_place(recap_items[0], anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(recap_items[0]), run_time=FAST)
        self.ly.safe_place(labels[0], anchor=recap_items[0], direction=DOWN, buff=0.25)
        self.play(FadeIn(labels[0], shift=LEFT * 0.1), run_time=FAST)
        self.wait(0.2)

        # Second fact
        self.ly.safe_place(recap_items[1], anchor=labels[0], direction=DOWN, buff=0.4)
        self.play(Write(recap_items[1]), run_time=FAST)
        self.ly.safe_place(labels[1], anchor=recap_items[1], direction=DOWN, buff=0.25)
        self.play(FadeIn(labels[1], shift=LEFT * 0.1), run_time=FAST)
        self.wait(0.2)

        # Third fact (remove first to stay in budget)
        self.play(FadeOut(recap_items[0]), FadeOut(labels[0]), run_time=FAST)
        self.ly.safe_place(recap_items[2], anchor=labels[1], direction=DOWN, buff=0.4)
        self.play(Write(recap_items[2]), run_time=FAST)
        self.ly.safe_place(labels[2], anchor=recap_items[2], direction=DOWN, buff=0.25)
        self.play(FadeIn(labels[2], shift=LEFT * 0.1), run_time=FAST)
        self.wait(33.8)  # pacing: extends previous caption slot (Δ=33.3)

        self.ly.clear()

    # --- Scene 3: First Isomorphism Theorem -- Intuition ---

    def scene3_first_intuition(self):
        self.add_subcaption(
            "Let us build the intuition. "
            "Suppose phi maps G to H. "
            "If two elements map to the same place, "
            "say phi of g1 equals phi of g2, "
            "then phi of g1 times g2 inverse equals the identity. "
            "This means g1 times g2 inverse is in the kernel. "
            "So g1 and g2 belong to the same coset of the kernel. "
            "In other words, a homomorphism naturally partitions G "
            "into cosets of its kernel. "
            "Each coset maps to exactly one element of the image. "
            "The quotient group G over ker phi "
            "captures exactly this collapsed structure.",
            duration=41.9,  # pacing: 1.08x natural 38.54 + 0.3
        )

        self.ly.section_divider(1, "First Isomorphism Theorem — Intuition")

        title = self.ly.title("First Isomorphism Theorem: Intuition")

        # Function diagram labels
        g_label = Text("G (domain)", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        h_label = Text("H (codomain)", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(g_label, anchor=title, direction=DOWN, buff=0.6)
        arrow = Arrow(
            start=g_label.get_right() + RIGHT * 0.3,
            end=g_label.get_right() + RIGHT * 2.0,
            color=WHITE, stroke_width=2.5,
        )
        phi_label = MathTex(r"\varphi", color=WHITE, font_size=30).next_to(arrow, UP, buff=0.15)
        self.ly.safe_place(h_label, anchor=g_label, direction=RIGHT, buff=3.5)

        self.play(Write(g_label), Create(arrow), Write(phi_label), Write(h_label), run_time=FAST)
        self.wait(0.3)

        # Key insight items
        insight1 = Text(
            "Same coset of ker(phi) -> same image element",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.play(FadeOut(g_label), run_time=FAST)
        self.ly.safe_place(insight1, anchor=h_label, direction=DOWN, buff=0.6)
        self.play(FadeIn(insight1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.2)

        insight2 = Text(
            "Different cosets -> different image elements",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight2, anchor=insight1, direction=DOWN, buff=0.4)
        self.play(FadeIn(insight2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.2)

        # The conclusion
        conclusion = MathTex(
            r"G/\ker(\varphi) \;\leftrightarrow\; \operatorname{im}(\varphi)",
            color=ACCENT, font_size=34,
        )
        boxed = self.ly.formula_box(conclusion, color=ACCENT)
        self.play(FadeOut(arrow), FadeOut(phi_label), FadeOut(h_label), run_time=FAST)
        self.ly.safe_place(boxed, anchor=insight2, direction=DOWN, buff=0.5)
        self.play(Write(conclusion), Create(boxed[1]), run_time=NORMAL)
        self.wait(38.8)  # pacing: extends previous caption slot (Δ=38.3)

        self.ly.clear()

    # --- Scene 4: First Isomorphism Theorem -- Statement and Proof ---

    def scene4_first_statement_proof(self):
        self.add_subcaption(
            "First Isomorphism Theorem. "
            "If phi from G to H is a homomorphism, "
            "then G over ker phi is isomorphic to im phi. "
            "The map phi-hat of g ker phi equals phi of g "
            "is an isomorphism. "
            "The proof has four steps. "
            "Step one, well-defined. "
            "If g1 ker equals g2 ker, "
            "then g1 g2 inverse is in ker, so phi of g1 g2 inverse is e. "
            "This gives phi of g1 equals phi of g2. "
            "Step two, homomorphism. "
            "Phi-hat of g1 ker times g2 ker equals phi-hat of g1 g2 ker "
            "equals phi of g1 g2 equals phi of g1 times phi of g2. "
            "Step three, injective. "
            "If phi-hat of g ker is the identity, "
            "then phi of g is e, so g is in ker, "
            "so g ker is the identity coset. "
            "Step four, surjective. "
            "For any y in im phi, choose g with phi of g equals y. "
            "Then phi-hat of g ker equals y.",
            duration=68.9,  # pacing: 1.08x natural 63.55 + 0.3
        )

        self.ly.section_divider(2, "First Isomorphism Theorem — Statement & Proof")

        title = self.ly.title("Statement and Proof")

        # Boxed theorem statement
        theorem_text = MathTex(
            r"G / \ker(\varphi) \cong \operatorname{im}(\varphi)",
            color=ACCENT, font_size=34,
        )
        boxed_theorem = self.ly.formula_box(theorem_text, color=ACCENT)
        self.ly.safe_place(boxed_theorem, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(theorem_text), Create(boxed_theorem[1]), run_time=NORMAL)
        self.wait(0.3)

        # Magic map definition
        magic = MathTex(
            r"\hat\varphi(g \cdot \ker\varphi) = \varphi(g)",
            color=WHITE, font_size=30,
        )
        self.ly.safe_place(magic, anchor=boxed_theorem, direction=DOWN, buff=0.5)
        self.play(Write(magic), run_time=FAST)
        self.wait(0.2)

        # Four proof steps
        steps = [
            ("1. Well-defined", r"g_1\ker = g_2\ker \Rightarrow \varphi(g_1) = \varphi(g_2)", SECONDARY),
            ("2. Homomorphism", r"\hat\varphi(ab\ker) = \hat\varphi(a\ker)\,\hat\varphi(b\ker)", PRIMARY),
            ("3. Injective", r"\hat\varphi(g\ker) = e \Rightarrow g \in \ker", ACCENT),
            ("4. Surjective", r"\forall\, y \in \operatorname{im}\varphi,\;\exists\, g:\;\hat\varphi(g\ker) = y", SECONDARY),
        ]

        prev = magic
        for i, (step_name, step_tex, step_color) in enumerate(steps):
            # Remove old elements to stay in budget
            if i == 2:
                self.play(FadeOut(magic), run_time=FAST)

            step_label = Text(step_name, font_size=SMALL_SIZE, color=step_color, font=SANS)
            step_formula = MathTex(step_tex, color=step_color, font_size=26)

            step_group = VGroup(step_label, step_formula).arrange(DOWN, buff=0.15)
            self.ly.safe_place(step_group, anchor=prev, direction=DOWN, buff=0.35)
            self.play(
                FadeIn(step_group, shift=LEFT * 0.1),
                run_time=FAST,
            )
            prev = step_group
            self.wait(0.2)

        self.wait(68.9)  # pacing: extends previous caption slot (Δ=68.4)
        self.ly.clear()

    # --- Scene 5: First Isomorphism Theorem -- Examples ---

    def scene5_first_examples(self):
        self.add_subcaption(
            "Let us see three concrete examples. "
            "Example 1: the determinant map from GL n R to R star. "
            "The kernel is SL n R, matrices with determinant 1. "
            "The image is all non-zero reals. "
            "So GL n R over SL n R is isomorphic to R star. "
            "Example 2: the sign homomorphism from S n "
            "to the group plus minus 1. "
            "The kernel is the alternating group A n. "
            "The image is Z over 2 Z. "
            "So S n over A n is isomorphic to Z over 2 Z. "
            "Example 3: the canonical projection "
            "from Z to Z over n Z. "
            "The kernel is n Z and the image is Z over n Z. "
            "So Z over n Z is isomorphic to Z over n Z, "
            "which confirms the structure.",
            duration=55.1,  # pacing: 1.08x natural 50.76 + 0.3
        )

        self.ly.section_divider(3, "First Isomorphism Theorem — Examples")

        title = self.ly.title("Examples of the First Theorem")

        # Example 1
        ex1_title = Text(
            "1. det: GL(n,R) -> R*",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(ex1_title, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(ex1_title), run_time=FAST)

        ex1_result = MathTex(
            r"GL(n,\mathbb{R}) \,/\, SL(n,\mathbb{R}) \cong \mathbb{R}^*",
            color=WHITE, font_size=30,
        )
        self.ly.safe_place(ex1_result, anchor=ex1_title, direction=DOWN, buff=0.3)
        self.play(Write(ex1_result), run_time=FAST)
        self.wait(0.3)

        # Example 2 (replace ex1)
        ex2_title = Text(
            "2. sign: S_n -> {+1, -1}",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.play(
            FadeOut(ex1_title), FadeOut(ex1_result),
            run_time=FAST,
        )
        self.ly.safe_place(ex2_title, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(ex2_title), run_time=FAST)

        ex2_result = MathTex(
            r"S_n \,/\, A_n \cong \mathbb{Z}/2\mathbb{Z}",
            color=WHITE, font_size=30,
        )
        self.ly.safe_place(ex2_result, anchor=ex2_title, direction=DOWN, buff=0.3)
        self.play(Write(ex2_result), run_time=FAST)
        self.wait(0.3)

        # Example 3 (replace ex2)
        ex3_title = Text(
            "3. phi: Z -> Z/nZ (canonical projection)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.play(
            FadeOut(ex2_title), FadeOut(ex2_result),
            run_time=FAST,
        )
        self.ly.safe_place(ex3_title, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(ex3_title), run_time=FAST)

        ex3_result = MathTex(
            r"\mathbb{Z} \,/\, n\mathbb{Z} \cong \mathbb{Z}/n\mathbb{Z}",
            color=WHITE, font_size=30,
        )
        self.ly.safe_place(ex3_result, anchor=ex3_title, direction=DOWN, buff=0.3)
        self.play(Write(ex3_result), run_time=FAST)
        self.wait(53.7)  # pacing: extends previous caption slot (Δ=53.2)

        self.ly.clear()

    # --- Scene 6: Second Isomorphism Theorem ---

    def scene6_second_motivation_statement(self):
        self.add_subcaption(
            "Now the Second Isomorphism Theorem. "
            "If N is a normal subgroup of G, "
            "and H is any subgroup of G, "
            "what connects quotients and intersections? "
            "The answer is: H over H intersect N "
            "is isomorphic to HN over N. "
            "Here HN is the product of H and N, "
            "which is a subgroup because N is normal. "
            "And H intersect N is normal in H. "
            "This is sometimes called the Diamond Isomorphism Theorem "
            "because the subgroups form a diamond shape in the lattice.",
            duration=34.7,  # pacing: 1.08x natural 31.85 + 0.3
        )

        self.ly.section_divider(4, "Second Isomorphism Theorem")

        title = self.ly.title("Second Isomorphism Theorem")

        # Diamond lattice diagram
        g_node = MathTex("G", color=WHITE, font_size=28)
        hn_node = MathTex("HN", color=ACCENT, font_size=28)
        h_node = MathTex("H", color=PRIMARY, font_size=28)
        n_node = MathTex("N", color=RED, font_size=28)
        hkn_node = MathTex(r"H \cap N", color=SECONDARY, font_size=28)

        # Position diamond manually (within safe zone)
        g_node.move_to(UP * 1.2)
        hn_node.move_to(UP * 1.2 + RIGHT * 2.0)
        h_node.move_to(ORIGIN + LEFT * 1.0)
        n_node.move_to(ORIGIN + RIGHT * 1.0)
        hkn_node.move_to(DOWN * 1.2)
        for node in [g_node, hn_node, h_node, n_node, hkn_node]:
            clamp_position(node, margin=0.6)

        # Draw edges
        edges = VGroup(
            Line(g_node.get_bottom(), h_node.get_top(), color=DIM, stroke_width=1.5),
            Line(g_node.get_bottom(), n_node.get_top(), color=DIM, stroke_width=1.5),
            Line(g_node.get_right(), hn_node.get_left(), color=DIM, stroke_width=1.5),
            Line(h_node.get_bottom(), hkn_node.get_top(), color=DIM, stroke_width=1.5),
            Line(n_node.get_bottom(), hkn_node.get_top(), color=DIM, stroke_width=1.5),
            Line(h_node.get_right(), hn_node.get_left() + DOWN * 0.3, color=DIM, stroke_width=1.5),
            Line(n_node.get_left(), hn_node.get_right() + DOWN * 0.3, color=DIM, stroke_width=1.5),
        )

        diamond = VGroup(g_node, hn_node, h_node, n_node, hkn_node, edges)
        self.ly.safe_place(diamond, anchor=title, direction=DOWN, buff=0.4)
        self.play(
            *[Create(e) for e in edges],
            *[Write(n) for n in [g_node, hn_node, h_node, n_node, hkn_node]],
            run_time=NORMAL,
        )
        self.wait(0.3)

        # Theorem statement
        theorem = MathTex(
            r"H \,/\, (H \cap N) \cong HN \,/\, N",
            color=ACCENT, font_size=34,
        )
        boxed = self.ly.formula_box(theorem, color=ACCENT)
        self.ly.safe_place(boxed, anchor=diamond, direction=DOWN, buff=0.4)
        self.play(Write(theorem), Create(boxed[1]), run_time=NORMAL)
        self.wait(32.7)  # pacing: extends previous caption slot (Δ=32.2)

        self.ly.clear()

    # --- Scene 7: Second Isomorphism Theorem -- Proof ---

    def scene7_second_proof(self):
        self.add_subcaption(
            "The proof strategy is the same as always: "
            "find a homomorphism and apply the First Isomorphism Theorem. "
            "Define f from H to HN over N by f of h equals h N. "
            "This is well-defined because HN over N is the quotient group. "
            "The kernel of f is the set of h in H such that h N equals N, "
            "which means h is in N. "
            "So ker of f equals H intersect N. "
            "The image is all of HN over N, "
            "because any element h n N equals h N for some h in H. "
            "Applying the First Isomorphism Theorem, "
            "H over H intersect N is isomorphic to HN over N.",
            duration=45.6,  # pacing: 1.08x natural 41.93 + 0.3
        )

        self.ly.section_divider(5, "Second Isomorphism Theorem — Proof")

        title = self.ly.title("Proof of the Second Theorem")

        # Key map
        key_map = MathTex(
            r"f: H \to HN/N, \quad f(h) = hN",
            color=PRIMARY, font_size=30,
        )
        self.ly.safe_place(key_map, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(key_map), run_time=NORMAL)
        self.wait(0.3)

        # Kernel
        ker_text = Text("Kernel:", font_size=BODY_SIZE, color=RED, font=SANS)
        ker_formula = MathTex(
            r"\ker(f) = H \cap N",
            color=RED, font_size=30,
        )
        ker_group = VGroup(ker_text, ker_formula).arrange(RIGHT, buff=0.3)
        self.ly.safe_place(ker_group, anchor=key_map, direction=DOWN, buff=0.5)
        self.play(Write(ker_text), Write(ker_formula), run_time=FAST)
        self.wait(0.2)

        # Image
        im_text = Text("Image:", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        im_formula = MathTex(
            r"\operatorname{im}(f) = HN/N",
            color=SECONDARY, font_size=30,
        )
        im_group = VGroup(im_text, im_formula).arrange(RIGHT, buff=0.3)
        self.ly.safe_place(im_group, anchor=ker_group, direction=DOWN, buff=0.4)
        self.play(Write(im_text), Write(im_formula), run_time=FAST)
        self.wait(0.2)

        # Apply FIT
        self.play(FadeOut(key_map), run_time=FAST)
        apply_fit = Text(
            "Apply the First Isomorphism Theorem:",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(apply_fit, anchor=im_group, direction=DOWN, buff=0.4)
        self.play(FadeIn(apply_fit, shift=LEFT * 0.1), run_time=FAST)
        self.wait(0.2)

        result = MathTex(
            r"H \,/\, (H \cap N) \cong HN \,/\, N",
            color=ACCENT, font_size=32,
        )
        boxed = self.ly.formula_box(result, color=ACCENT)
        self.ly.safe_place(boxed, anchor=apply_fit, direction=DOWN, buff=0.4)
        self.play(Write(result), Create(boxed[1]), run_time=NORMAL)
        self.wait(42.3)  # pacing: extends previous caption slot (Δ=41.8)

        self.ly.clear()

    # --- Scene 8: Third Isomorphism Theorem ---

    def scene8_third_theorem(self):
        self.add_subcaption(
            "The Third Isomorphism Theorem answers the question: "
            "what happens when we quotient twice? "
            "If K is contained in N, both normal in G, "
            "then G over N quotiented by K over N "
            "is isomorphic to G over K. "
            "The proof is once again by the First Isomorphism Theorem. "
            "Define f from G over N to G over K "
            "by f of g N equals g K. "
            "The kernel is the set of g N such that g K equals K, "
            "meaning g is in K, so ker of f is K over N. "
            "The image is G over K. "
            "Applying the First Isomorphism Theorem gives the result. "
            "Quotienting by N then by K over N "
            "is the same as quotienting by K directly.",
            duration=49.2,  # pacing: 1.08x natural 45.29 + 0.3
        )

        self.ly.section_divider(6, "Third Isomorphism Theorem")

        title = self.ly.title("Third Isomorphism Theorem")

        # Tower visualization
        level1 = MathTex(r"G", color=WHITE, font_size=30)
        level2 = MathTex(r"G/N", color=PRIMARY, font_size=30)
        level3 = MathTex(r"(G/N)\,/\,(K/N)", color=SECONDARY, font_size=28)
        level3_direct = MathTex(r"G/K", color=ACCENT, font_size=30)

        level1.move_to(LEFT * 1.5 + UP * 1.5)
        level2.move_to(LEFT * 1.5 + UP * 0.0)
        level3.move_to(LEFT * 1.5 + DOWN * 1.5)
        level3_direct.move_to(RIGHT * 2.0 + DOWN * 0.75)
        for node in [level1, level2, level3, level3_direct]:
            clamp_position(node, margin=0.6)

        arrow1 = Arrow(level1.get_bottom(), level2.get_top(), color=PRIMARY, stroke_width=2)
        arrow1_label = Text("quotient by N", font_size=SMALL_SIZE, color=PRIMARY, font=SANS).next_to(arrow1, LEFT, buff=0.15)
        arrow2 = Arrow(level2.get_bottom(), level3.get_top(), color=SECONDARY, stroke_width=2)
        arrow2_label = Text("quotient by K/N", font_size=SMALL_SIZE, color=SECONDARY, font=SANS).next_to(arrow2, LEFT, buff=0.15)
        arrow3 = Arrow(level1.get_right(), level3_direct.get_left(), color=ACCENT, stroke_width=2)
        arrow3_label = Text("quotient by K", font_size=SMALL_SIZE, color=ACCENT, font=SANS).next_to(arrow3, UP, buff=0.15)

        tower = VGroup(level1, level2, level3, level3_direct, arrow1, arrow2, arrow3, arrow1_label, arrow2_label, arrow3_label)

        self.ly.safe_place(tower, anchor=title, direction=DOWN, buff=0.4)
        self.play(
            *[Write(n) for n in [level1, level2, level3, level3_direct]],
            *[Create(a) for a in [arrow1, arrow2, arrow3]],
            *[FadeIn(l, shift=LEFT * 0.1) for l in [arrow1_label, arrow2_label, arrow3_label]],
            run_time=NORMAL,
        )
        self.wait(0.3)

        # Theorem statement
        theorem = MathTex(
            r"(G/N) \,/\, (K/N) \cong G/K",
            color=ACCENT, font_size=34,
        )
        boxed = self.ly.formula_box(theorem, color=ACCENT)
        self.ly.safe_place(boxed, anchor=tower, direction=DOWN, buff=0.4)
        self.play(Write(theorem), Create(boxed[1]), run_time=NORMAL)
        self.wait(49.5)  # pacing: extends previous caption slot (Δ=49.0)

        self.ly.clear()

    # --- Scene 9: Unifying Theme ---

    def scene9_unifying_theme(self):
        self.add_subcaption(
            "Now let us step back and see the big picture. "
            "All three isomorphism theorems share a common structure. "
            "The First Isomorphism Theorem is the foundation. "
            "It says G over ker phi is isomorphic to im phi. "
            "The Second Theorem: H over H intersect N is isomorphic to HN over N. "
            "This is proved by applying the First Theorem "
            "to the map f of h equals h N. "
            "The Third Theorem: G over N quotiented by K over N "
            "is isomorphic to G over K. "
            "This is proved by applying the First Theorem "
            "to the map f of g N equals g K. "
            "The First Isomorphism Theorem is the master theorem. "
            "The other two are just clever applications. "
            "In practice, to prove two quotient groups are isomorphic, "
            "find a homomorphism, compute its kernel and image, "
            "and apply the First Isomorphism Theorem.",
            duration=58.7,  # pacing: 1.08x natural 54.07 + 0.3 (was 44.1 — copy of seg 9)
        )

        title = self.ly.title("The Big Picture")

        items = [
            Text(
                "1st (Foundation): G/ker(phi) is isomorphic to im(phi)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "2nd (Diamond): H/(H intersect N) is isomorphic to HN/N",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3rd (Nested): (G/N)/(K/N) is isomorphic to G/K",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.6)
        self.wait(0.3)

        # Unifying message
        message = Text(
            "Strategy: find a homomorphism, use the First Theorem",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.play(FadeOut(items[0]), run_time=FAST)
        self.ly.safe_place(message, anchor=items[-1], direction=DOWN, buff=0.5)
        self.play(FadeIn(message, shift=LEFT * 0.1), run_time=FAST)
        self.wait(61.4)  # pacing: extends previous caption slot (Δ=60.9)

        self.ly.clear()

    # --- Scene 10: Summary + Outro ---

    def scene10_summary(self):
        self.add_subcaption(
            "Let us summarize. "
            "The First Isomorphism Theorem: "
            "G over ker phi is isomorphic to im phi. "
            "The magic map phi-hat of g ker equals phi of g "
            "is the natural isomorphism. "
            "The Second Isomorphism Theorem: "
            "H over H intersect N is isomorphic to HN over N. "
            "The Third Isomorphism Theorem: "
            "G over N quotiented by K over N is isomorphic to G over K. "
            "All three derive from the First Isomorphism Theorem. "
            "The First Isomorphism Theorem is the master tool "
            "for proving quotient groups are isomorphic. "
            "Next time, we apply these theorems to classify groups "
            "and explore simple groups and composition series. "
            "Thanks for watching.",
            duration=48.0,  # pacing: 1.08x natural 44.14 + 0.3
        )

        title = self.ly.title("Summary")

        takeaways = [
            Text("1. G/ker(phi) is isomorphic to im(phi)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("2. The map phi-hat(g ker) = phi(g) is the isomorphism", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("3. H/(H intersect N) is isomorphic to HN/N", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("4. (G/N)/(K/N) is isomorphic to G/K", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5. All three derive from the First Theorem", font_size=BODY_SIZE, color=RED, font=SANS),
        ]

        self.ly.progressive_reveal(takeaways, start_from=title, run_time=0.5)
        self.wait(40.9)  # pacing: extends previous caption slot (Δ=40.4)

        self.ly.clear()

        play_outro(self, "Isomorphism Theorems", "Abstract Algebra I")
