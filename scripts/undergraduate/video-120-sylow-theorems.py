"""Video 120: Sylow Theorems
TEMPLATE v2 -- Professional quality Manim script

Playlist: Abstract Algebra I (Video 10 of 12)
Class: Video120_SylowTheorems

Topics: Sylow p-subgroups, existence (1st theorem), conjugacy (2nd theorem),
         counting (3rd theorem), applications to groups of order pq and 30.

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


class Video120_SylowTheorems(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_first_theorem()
        self.scene4_second_theorem()
        self.scene5_third_theorem()
        self.scene6_application_pq()
        self.scene7_application_order30()
        self.scene8_summary()

    # --- Scene 1: Hook --- "The Mystery of the p-Part"
    # Narration ~40s.

    def scene1_hook(self):
        self.add_subcaption(
            "What subgroups must every finite group of order 60 have? "
            "This is the question that motivated Sylow. "
            "A group of order 60 has 60 equals 2 squared times 3 times 5. "
            "Cauchy's theorem tells us there exist elements of order 2, 3, and 5. "
            "But can we guarantee an entire subgroup of order 4, of order 3, or of order 5? "
            "The Sylow theorems answer this with a resounding yes. "
            "They are among the most powerful tools in finite group theory. "
            "Today we will prove three theorems: "
            "existence, conjugacy, and counting of subgroups of prime power order. "
            "This is Abstract Algebra, Video 10.",
            duration=40,
        )
        play_intro(self, "Sylow Theorems", "Abstract Algebra I")

        title = self.ly.title("The Mystery of the p-Part")
        self.wait(2)

        items = [
            Text("|G| = 60 = 2\u00b2 \u00b7 3 \u00b7 5", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Cauchy: elements of order 2, 3, 5 exist", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("But what about subgroups of order 4, 3, 5?", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(6)

        # Key notation
        notation = MathTex(
            r"|G| = p^k \cdot m, \quad p \nmid m",
            color=WHITE, font_size=36,
        )
        boxed = self.ly.formula_box(notation, color=ACCENT)
        self.ly.safe_place(boxed, anchor=items[-1], direction=DOWN, buff=0.4)
        self.play(Write(notation), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        # Tease
        tease = Text(
            "Three theorems: Existence, Conjugacy, Counting",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(tease, anchor=boxed, direction=DOWN, buff=0.3)
        self.play(FadeIn(tease, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: Sylow p-Subgroups -- Definition ---
    # Narration ~50s.

    def scene2_definition(self):
        self.add_subcaption(
            "Before stating the theorems, we need the key definition. "
            "A p-group is a group whose order is a power of a prime p. "
            "If p to the k divides the order of G, "
            "but p to the k plus 1 does not divide the order of G, "
            "we write p to the k exactly divides the order of G. "
            "A Sylow p-subgroup of G is a subgroup of order p to the k, "
            "the largest power of p dividing the order of G. "
            "For example, if the order of G is 60, "
            "then a Sylow 2-subgroup has order 4, "
            "a Sylow 3-subgroup has order 3, "
            "and a Sylow 5-subgroup has order 5. "
            "Lagrange's theorem tells us that the order of any subgroup "
            "divides the order of G, so p to the k is the maximum possible. "
            "Cauchy's theorem says that if p divides the order of G, "
            "there is an element of order p. "
            "The Sylow theorems vastly generalize this "
            "from one element to an entire subgroup.",
            duration=50,
        )

        title = self.ly.title("Sylow p-Subgroups: Definition")
        self.wait(2)

        # p-group definition
        pgroup = MathTex(
            r"\text{p-group: } |H| = p^n \text{ for some } n",
            color=WHITE, font_size=30,
        )
        self.ly.safe_place(pgroup, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(pgroup), run_time=NORMAL)
        self.wait(4)

        # Exact power
        exact = MathTex(
            r"p^k \parallel |G| \;\Longleftrightarrow\; p^k \mid |G|, \; p^{k+1} \nmid |G|",
            color=PRIMARY, font_size=28,
        )
        self.ly.safe_place(exact, anchor=pgroup, direction=DOWN, buff=0.4)
        self.play(Write(exact), run_time=NORMAL)
        self.wait(5)

        # Sylow definition
        sylow_def = MathTex(
            r"\text{Sylow p-subgroup: subgroup of order } p^k",
            color=ACCENT, font_size=32,
        )
        self.play(FadeOut(pgroup), FadeOut(exact), run_time=FAST)
        self.ly.safe_place(sylow_def, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(sylow_def), run_time=NORMAL)
        self.wait(5)

        # Example
        example = Text(
            "|G| = 60: Syl_2 has order 4, Syl_3 has order 3, Syl_5 has order 5",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(example, anchor=sylow_def, direction=DOWN, buff=0.4)
        self.play(FadeIn(example, shift=LEFT * 0.15), run_time=FAST)
        self.wait(6)

        # Motivation chain
        lagrange = Text(
            "Lagrange: |H| divides |G|  =>  p^k is the max possible",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.play(FadeOut(sylow_def), FadeOut(example), run_time=FAST)
        self.ly.safe_place(lagrange, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(lagrange), run_time=NORMAL)
        self.wait(4)

        cauchy = Text(
            "Cauchy: one element of order p  =>  Sylow: whole subgroup of order p^k",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(cauchy, anchor=lagrange, direction=DOWN, buff=0.4)
        self.play(FadeIn(cauchy, shift=LEFT * 0.15), run_time=FAST)
        self.wait(6)

        self.ly.clear()

    # --- Scene 3: First Sylow Theorem -- Existence ---
    # Narration ~55s.

    def scene3_first_theorem(self):
        self.add_subcaption(
            "The first Sylow theorem guarantees that these subgroups actually exist. "
            "Theorem one: for every prime p dividing the order of G, "
            "G has a subgroup of order p to the k, "
            "where p to the k is the highest power of p dividing the order of G. "
            "In other words, Sylow p-subgroups always exist. "
            "The proof uses the action of G on subsets. "
            "Let Omega be the set of all subsets of G of size p to the k. "
            "G acts on Omega by left multiplication: "
            "g sends S to gS. "
            "By the orbit-stabilizer theorem, "
            "the size of every orbit divides the order of G. "
            "Since the order of G is p to the k times m, "
            "where p does not divide m, "
            "the orbits have sizes dividing p to the k times m. "
            "A key counting argument shows "
            "that Omega has a multiple of p to the k elements. "
            "Therefore some orbit must have size not divisible by p, "
            "so the stabilizer of a point in that orbit "
            "has order divisible by p to the k. "
            "This stabilizer is our Sylow p-subgroup.",
            duration=55,
        )

        self.ly.section_divider(1, "First Sylow Theorem: Existence")
        self.wait(2)

        title = self.ly.title("First Sylow Theorem")
        self.wait(2)

        # Statement
        stmt = MathTex(
            r"\forall \; p \mid |G|, \; \exists \; P \leq G \text{ with } |P| = p^k",
            color=WHITE, font_size=32,
        )
        boxed = self.ly.formula_box(stmt, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(stmt), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        subtitle = Text(
            "Sylow p-subgroups always exist",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(subtitle, anchor=boxed, direction=DOWN, buff=0.4)
        self.play(FadeIn(subtitle, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        # Proof sketch (part 1)
        proof_title = Text(
            "Proof sketch: action on subsets",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.play(FadeOut(boxed), FadeOut(subtitle), run_time=FAST)
        self.ly.safe_place(proof_title, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(proof_title), run_time=NORMAL)
        self.wait(3)

        steps1 = [
            MathTex(r"\Omega = \{S \subseteq G : |S| = p^k\}", color=WHITE, font_size=28),
            Text("G acts on Omega by left multiplication", font_size=SMALL_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.stack_down(steps1, start_from=proof_title, spacing=0.3)
        for s in steps1:
            if isinstance(s, MathTex):
                self.play(Write(s), run_time=FAST)
            else:
                self.play(FadeIn(s, shift=LEFT * 0.1), run_time=FAST)
            self.wait(2)
        self.wait(4)

        # Proof sketch (part 2) — FadeOut first 2 steps to stay within budget
        self.play(FadeOut(steps1[0]), FadeOut(steps1[1]), run_time=FAST)
        steps2 = [
            Text("Orbit sizes divide |G| = p^k . m", font_size=SMALL_SIZE, color=WHITE, font=SANS),
            Text("Some orbit coprime to p => stabilizer has order p^k", font_size=SMALL_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.stack_down(steps2, start_from=proof_title, spacing=0.3)
        for s in steps2:
            self.play(FadeIn(s, shift=LEFT * 0.1), run_time=FAST)
            self.wait(2)
        self.wait(6)

        # Key insight
        insight = Text(
            "Existence guarantees we can always find the p-part",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.play(
            FadeOut(proof_title),
            *[FadeOut(s) for s in steps2],
            run_time=FAST,
        )
        self.ly.safe_place(insight, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 4: Second Sylow Theorem -- Conjugacy ---
    # Narration ~50s.

    def scene4_second_theorem(self):
        self.add_subcaption(
            "The second Sylow theorem tells us that all Sylow p-subgroups "
            "are essentially the same, up to conjugation. "
            "Theorem two: if P and Q are Sylow p-subgroups of G, "
            "then there exists an element g in G "
            "such that P equals g Q g inverse. "
            "In other words, all Sylow p-subgroups are conjugate to each other. "
            "This is a powerful structural result. "
            "It means that any Sylow p-subgroup "
            "is just another viewed from a different angle. "
            "The proof uses the conjugation action. "
            "G acts on its Sylow p-subgroups by conjugation: "
            "g sends P to gPg inverse. "
            "Since P is a Sylow p-subgroup, "
            "the normalizer of P contains P itself. "
            "A double coset counting argument shows "
            "that the index of the normalizer of P "
            "equals the number of Sylow p-subgroups, "
            "which must equal 1 mod p. "
            "This forces all Sylow p-subgroups into one conjugacy class.",
            duration=50,
        )

        title = self.ly.title("Second Sylow Theorem: Conjugacy")
        self.wait(2)

        # Statement
        stmt = MathTex(
            r"P, Q \in \mathrm{Syl}_p(G) \implies \exists g \in G: P = gQg^{-1}",
            color=WHITE, font_size=30,
        )
        boxed = self.ly.formula_box(stmt, color=SECONDARY)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(stmt), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        interp = Text(
            "All Sylow p-subgroups are conjugate (same structure, different view)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(interp, anchor=boxed, direction=DOWN, buff=0.4)
        self.play(FadeIn(interp, shift=LEFT * 0.15), run_time=FAST)
        self.wait(6)

        # Conjugation action
        conj = Text(
            "G acts on Syl_p(G) by conjugation",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.play(FadeOut(boxed), FadeOut(interp), run_time=FAST)
        self.ly.safe_place(conj, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(conj), run_time=NORMAL)
        self.wait(3)

        conj_formula = MathTex(
            r"g \cdot P = gPg^{-1}",
            color=WHITE, font_size=32,
        )
        self.ly.safe_place(conj_formula, anchor=conj, direction=DOWN, buff=0.4)
        self.play(Write(conj_formula), run_time=NORMAL)
        self.wait(5)

        # Consequence
        consequence = Text(
            "Normalizer: N_G(P) contains P, index equals number of Sylow subgroups",
            font_size=SMALL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(consequence, anchor=conj_formula, direction=DOWN, buff=0.3)
        self.play(FadeIn(consequence, shift=LEFT * 0.1), run_time=FAST)
        self.wait(5)

        result = Text(
            "One conjugacy class: n_p = [G : N_G(P)]",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(result, anchor=consequence, direction=DOWN, buff=0.3)
        self.play(FadeIn(result, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 5: Third Sylow Theorem -- Counting ---
    # Narration ~60s.

    def scene5_third_theorem(self):
        self.add_subcaption(
            "The third Sylow theorem gives us precise numerical constraints "
            "on how many Sylow p-subgroups a group can have. "
            "Theorem three: let n sub p denote the number of Sylow p-subgroups of G. "
            "Then n sub p is congruent to 1 modulo p, "
            "and n sub p divides the order of G divided by p to the k. "
            "That is, the number of Sylow p-subgroups "
            "is tightly constrained in two ways simultaneously. "
            "The first condition says n sub p minus 1 is divisible by p, "
            "so n sub p could be 1, p plus 1, 2p plus 1, and so on. "
            "The second condition narrows it further: "
            "it must also divide m, where the order of G equals p to the k times m. "
            "Together, these often force a unique value for n sub p. "
            "The proof uses the conjugation action of G "
            "on the set of all Sylow p-subgroups. "
            "The orbit of any Sylow p-subgroup P under this action "
            "gives n sub p. "
            "Restricting the action to P acting on its conjugates "
            "shows that n sub p is congruent to 1 mod p.",
            duration=60,
        )

        self.ly.section_divider(2, "Third Sylow Theorem: Counting")
        self.wait(2)

        title = self.ly.title("Third Sylow Theorem")
        self.wait(2)

        # Statement
        stmt1 = MathTex(
            r"n_p \equiv 1 \pmod{p}",
            color=WHITE, font_size=34,
        )
        stmt2 = MathTex(
            r"n_p \mid \frac{|G|}{p^k}",
            color=WHITE, font_size=34,
        )
        boxed1 = self.ly.formula_box(stmt1, color=ACCENT)
        boxed2 = self.ly.formula_box(stmt2, color=PRIMARY)

        self.ly.safe_place(boxed1, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(stmt1), Create(boxed1[1]), run_time=NORMAL)
        self.wait(4)
        self.ly.safe_place(boxed2, anchor=boxed1, direction=DOWN, buff=0.4)
        self.play(Write(stmt2), Create(boxed2[1]), run_time=NORMAL)
        self.wait(5)

        # Explanation
        where = Text(
            "n_p = number of Sylow p-subgroups of G",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(where, anchor=boxed2, direction=DOWN, buff=0.4)
        self.play(FadeIn(where, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        # Constraint narrowing example
        self.play(
            FadeOut(boxed1), FadeOut(boxed2), FadeOut(where),
            run_time=FAST,
        )
        narrow = Text(
            "Example: |G| = 12 = 2\u00b2 \u00b7 3",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(narrow, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(narrow), run_time=NORMAL)
        self.wait(3)

        syl3 = Text(
            "n_3 = 1 mod 3 and n_3 | 4  =>  n_3 = 1",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(syl3, anchor=narrow, direction=DOWN, buff=0.3)
        self.play(FadeIn(syl3, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        syl2 = Text(
            "n_2 = 1 mod 2 and n_2 | 3  =>  n_2 = 1 or 3",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(syl2, anchor=syl3, direction=DOWN, buff=0.3)
        self.play(FadeIn(syl2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        payoff = Text(
            "Two constraints often force a unique value!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(payoff, anchor=syl2, direction=DOWN, buff=0.3)
        self.play(FadeIn(payoff, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 6: Application -- Groups of Order pq ---
    # Narration ~55s.

    def scene6_application_pq(self):
        self.add_subcaption(
            "Let us apply the Sylow theorems to classify groups of order p q, "
            "where p and q are distinct primes. "
            "Consider the case of order 6, which is 2 times 3. "
            "By the first Sylow theorem, "
            "there exist Sylow 2-subgroups of order 2 "
            "and Sylow 3-subgroups of order 3. "
            "For the Sylow 3-subgroups: "
            "n_3 is congruent to 1 mod 3 and n_3 divides 2. "
            "So n_3 equals 1. "
            "This means there is exactly one Sylow 3-subgroup, "
            "so it is normal in G. "
            "For the Sylow 2-subgroups: "
            "n_2 is congruent to 1 mod 2 and n_2 divides 3. "
            "So n_2 is 1 or 3. "
            "When n_2 equals 1, both Sylow subgroups are normal "
            "and G is cyclic of order 6. "
            "When n_2 equals 3, we get the symmetric group S_3. "
            "More generally, for distinct primes p and q "
            "with p not dividing q minus 1, "
            "every group of order p q is cyclic.",
            duration=55,
        )

        title = self.ly.title("Application: Groups of Order pq")
        self.wait(2)

        # Setup
        setup = MathTex(
            r"|G| = 6 = 2 \times 3",
            color=WHITE, font_size=32,
        )
        self.ly.safe_place(setup, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(setup), run_time=NORMAL)
        self.wait(3)

        # Sylow 3
        syl3_title = Text("Sylow 3-subgroups:", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        syl3_work = MathTex(
            r"n_3 \equiv 1 \pmod{3}, \quad n_3 \mid 2 \;\Longrightarrow\; n_3 = 1",
            color=WHITE, font_size=28,
        )
        self.ly.safe_place(syl3_title, anchor=setup, direction=DOWN, buff=0.4)
        self.play(Write(syl3_title), run_time=FAST)
        self.wait(1)
        self.ly.safe_place(syl3_work, anchor=syl3_title, direction=DOWN, buff=0.3)
        self.play(Write(syl3_work), run_time=NORMAL)
        self.wait(5)

        # Unique => normal
        normal = Text(
            "Unique Syl_3 => normal in G",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(normal, anchor=syl3_work, direction=DOWN, buff=0.3)
        self.play(FadeIn(normal, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        # Sylow 2
        self.play(FadeOut(setup), FadeOut(syl3_title), FadeOut(syl3_work), FadeOut(normal), run_time=FAST)
        syl2_title = Text("Sylow 2-subgroups:", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        syl2_work = MathTex(
            r"n_2 \equiv 1 \pmod{2}, \quad n_2 \mid 3 \;\Longrightarrow\; n_2 = 1 \text{ or } 3",
            color=WHITE, font_size=28,
        )
        self.ly.safe_place(syl2_title, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(syl2_title), run_time=FAST)
        self.wait(1)
        self.ly.safe_place(syl2_work, anchor=syl2_title, direction=DOWN, buff=0.3)
        self.play(Write(syl2_work), run_time=NORMAL)
        self.wait(5)

        # Result
        result1 = Text(
            "n_2 = 1: G is cyclic (Z_6)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        result2 = Text(
            "n_2 = 3: G is S_3",
            font_size=BODY_SIZE, color=RED, font=SANS)
        self.ly.safe_place(result1, anchor=syl2_work, direction=DOWN, buff=0.3)
        self.play(FadeIn(result1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)
        self.ly.safe_place(result2, anchor=result1, direction=DOWN, buff=0.3)
        self.play(FadeIn(result2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(6)

        # General theorem
        self.play(
            FadeOut(syl2_title), FadeOut(syl2_work),
            FadeOut(result1), FadeOut(result2), run_time=FAST,
        )
        general = MathTex(
            r"p \nmid (q - 1) \implies G \cong \mathbb{Z}_{pq}",
            color=ACCENT, font_size=34,
        )
        boxed = self.ly.formula_box(general, color=ACCENT)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(general), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        gen_label = Text(
            "When p does not divide q - 1, every group of order pq is cyclic",
            font_size=LABEL_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(gen_label, anchor=boxed, direction=DOWN, buff=0.3)
        self.play(FadeIn(gen_label, shift=LEFT * 0.1), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 7: Application -- Groups of Order 30 ---
    # Narration ~50s.

    def scene7_application_order30(self):
        self.add_subcaption(
            "Let us classify groups of order 30. "
            "We have 30 equals 2 times 3 times 5. "
            "For the Sylow 5-subgroups: "
            "n_5 is congruent to 1 mod 5 and n_5 divides 6. "
            "So n_5 is 1 or 6. "
            "For the Sylow 3-subgroups: "
            "n_3 is congruent to 1 mod 3 and n_3 divides 10. "
            "So n_3 is 1 or 10. "
            "A counting argument eliminates some possibilities. "
            "If n_5 equals 6 and n_3 equals 10, "
            "we would need 6 times 4 plus 10 times 2 plus 1 equals 45 non-identity elements, "
            "but the group only has 29 non-identity elements. Contradiction. "
            "So at least one of the Sylow subgroups is unique, hence normal. "
            "When both are unique, G is cyclic. "
            "When only the Sylow 5-subgroup is unique, "
            "we get the dihedral group D_15 or a semidirect product. "
            "This shows the power of Sylow's counting constraints.",
            duration=50,
        )

        title = self.ly.title("Application: Groups of Order 30")
        self.wait(2)

        # Setup
        setup = MathTex(
            r"|G| = 30 = 2 \cdot 3 \cdot 5",
            color=WHITE, font_size=32,
        )
        self.ly.safe_place(setup, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(setup), run_time=NORMAL)
        self.wait(3)

        # Sylow 5
        syl5 = MathTex(
            r"n_5 \equiv 1 \pmod{5}, \quad n_5 \mid 6 \;\Longrightarrow\; n_5 = 1 \text{ or } 6",
            color=PRIMARY, font_size=28,
        )
        self.ly.safe_place(syl5, anchor=setup, direction=DOWN, buff=0.4)
        self.play(Write(syl5), run_time=NORMAL)
        self.wait(5)

        # Sylow 3
        syl3 = MathTex(
            r"n_3 \equiv 1 \pmod{3}, \quad n_3 \mid 10 \;\Longrightarrow\; n_3 = 1 \text{ or } 10",
            color=SECONDARY, font_size=28,
        )
        self.ly.safe_place(syl3, anchor=syl5, direction=DOWN, buff=0.3)
        self.play(Write(syl3), run_time=NORMAL)
        self.wait(5)

        # Counting argument
        count = Text(
            "If n_5=6, n_3=10: need 6(4)+10(2)+1=45 > 29 non-identity elements",
            font_size=LABEL_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(count, anchor=syl3, direction=DOWN, buff=0.3)
        self.play(FadeIn(count, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        # Conclusion
        self.play(FadeOut(setup), FadeOut(syl5), FadeOut(syl3), FadeOut(count), run_time=FAST)
        conclusion = Text(
            "At least one Sylow subgroup is unique => normal",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(conclusion, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(conclusion), run_time=NORMAL)
        self.wait(4)

        results = [
            Text("Both unique: G is cyclic (Z_30)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Only Syl_5 unique: semidirect product", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(results, start_from=conclusion, run_time=0.8)
        self.wait(6)

        power = Text(
            "Sylow counting constraints drive the classification",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(power, anchor=results[-1], direction=DOWN, buff=0.3)
        self.play(FadeIn(power, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 8: Summary ---
    # Narration ~30s.

    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap the three Sylow theorems. "
            "The first theorem guarantees existence: "
            "for every prime p dividing the order of G, "
            "there is a Sylow p-subgroup of the largest possible order p to the k. "
            "The second theorem tells us about conjugacy: "
            "all Sylow p-subgroups are conjugate to each other. "
            "The third theorem gives counting constraints: "
            "n sub p is congruent to 1 mod p "
            "and n sub p divides the order of G divided by p to the k. "
            "Together, these theorems are the cornerstone "
            "of the classification of finite groups. "
            "They let us determine group structure "
            "just by counting and divisibility. "
            "Next time, we will explore finite simple groups "
            "and why the Sylow theorems are essential for their study. "
            "This is Abstract Algebra, Video 10.",
            duration=30,
        )

        title = self.ly.title("Summary: The Three Sylow Theorems")
        self.wait(2)

        items = [
            Text("1st: Existence \u2014 Syl_p(G) is nonempty", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2nd: Conjugacy \u2014 all Sylow p-subgroups are conjugate", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3rd: Counting \u2014 n_p \u2261 1 (mod p) and n_p | |G|/p^k", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(6)

        # Connection
        connection = Text(
            "Cornerstone of the classification of finite groups",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(connection, anchor=items[-1], direction=DOWN, buff=0.4)
        self.play(FadeIn(connection, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Tease next
        self.add_subcaption(
            "Next time: Finite Simple Groups.",
            duration=3,
        )
        tease = self.ly.title("Next: Finite Simple Groups")
        self.wait(3)
        self.ly.clear()

        play_outro(self)
