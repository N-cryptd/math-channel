"""
Video 90: Why Proofs?
Introduction to Proofs — Video 1 of 9 (Proof-Based Mathematics, L4)

Covers: What is a mathematical proof, why examples aren't enough,
the anatomy of a proof (axioms → deductions → theorem), preview of proof techniques
(direct, contrapositive, contradiction, induction), and a first direct proof example.

Plan: planning/video-90-intro-to-proofs.md

Render draft:  manim -ql scripts/undergraduate/video-90-intro-to-proofs.py Video90_WhyProofs
Render final:  manim -qh scripts/undergraduate/video-90-intro-to-proofs.py Video90_WhyProofs
"""

from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits

import math


class Video90_WhyProofs(Scene):
    """Why do we need proofs? Examples fail. Proof techniques preview. First direct proof."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_what_is_proof()
        self.scene3_anatomy()
        self.scene4_types_preview()
        self.scene5_first_direct_proof()
        self.scene6_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook — The Danger of Examples (50s)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Why do mathematicians insist on proofs? "
            "Can't we just check a bunch of examples and call it true? "
            "Here's why that strategy can fail catastrophically.",
            duration=18,
        )
        play_intro(self, "Why Proofs?", "Introduction to Proofs")

        title = self.ly.title("The Danger of Examples")

        # Show the conjecture: n^2 + n + 41 is prime for all n >= 0
        conj = MathTex(r"n^2 + n + 41", color=WHITE, font_size=BODY_SIZE)
        conj_label = Text("Conjecture:", font_size=LABEL_SIZE, color=PRIMARY, font=SANS)
        self.ly.safe_place(conj, direction=DOWN, anchor=title)
        self.ly.safe_place(conj_label, direction=LEFT, anchor=conj, buff=0.3)

        self.play(Write(conj_label), run_time=NORMAL)
        self.play(Write(conj), run_time=NORMAL)
        self.wait(1)

        # Show n = 0 to 39 works (small checkmarks)
        check_group = VGroup()
        for i in range(5):
            val = i
            res = val * val + val + 41
            is_prime = all(res % p for p in range(2, int(math.sqrt(res)) + 1)) and res > 1
            label = Text(f"n={val}: {res}", font_size=SMALL_SIZE, color=SECONDARY if is_prime else RED, font=SANS)
            check_group.add(label)

        self.ly.stack_down(list(check_group), start_from=conj, spacing=0.25)
        self.play(LaggedStartMap(FadeIn, check_group, lag_ratio=0.1), run_time=FAST)
        self.wait(1)

        # Transition to the big reveal
        and_more = Text("... and it works for n = 0 to 39!", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(and_more, direction=DOWN, anchor=check_group, buff=0.4)
        self.play(FadeIn(and_more, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # The counterexample: n = 40
        n40 = 40
        res40 = n40 * n40 + n40 + 41
        counter = Text(f"n = 40: {res40} = 41²", font_size=HEADING_SIZE, color=RED, font=SANS)
        self.ly.safe_place(counter, direction=DOWN, anchor=and_more, buff=0.5)

        # Dramatic reveal
        self.play(FadeIn(counter, shift=LEFT * 0.15), run_time=SLOW)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: What Is a Proof? (60s)
    # ------------------------------------------------------------------
    def scene2_what_is_proof(self):
        self.add_subcaption(
            "A proof is not just a collection of examples. "
            "It is a logical chain that guarantees a statement is true for all cases, "
            "with no exceptions.",
            duration=15,
        )

        title = self.ly.title("What Is a Proof?")

        # Definition text, progressive reveal
        items = [
            Text("A proof is a logical argument that", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("guarantees a mathematical statement", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("is TRUE for all cases, with no", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("exceptions.", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Anatomy of a Proof (70s)
    # ------------------------------------------------------------------
    def scene3_anatomy(self):
        self.add_subcaption(
            "Every proof has the same basic anatomy. We start with axioms — "
            "statements we accept as true. We apply logical deductions step by step, "
            "and arrive at a theorem — a mathematical truth we have now rigorously established.",
            duration=18,
        )

        title = self.ly.title("Anatomy of a Proof")

        # Build chain: AXIOMS → → THEOREM
        axioms = Text("AXIOMS", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        arrow1 = Text("→", font_size=HEADING_SIZE, color=WHITE, font=SANS)
        deductions = Text("DEDUCTIONS", font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        arrow2 = Text("→", font_size=HEADING_SIZE, color=WHITE, font=SANS)
        theorem = Text("THEOREM", font_size=HEADING_SIZE, color=ACCENT, font=SANS)

        chain = VGroup(axioms, arrow1, deductions, arrow2, theorem).arrange(RIGHT, buff=0.4)
        self.ly.center_in_content(chain)

        # Progressive reveal of the chain
        self.play(Write(axioms), run_time=NORMAL)
        self.play(Write(arrow1), run_time=FAST)
        self.play(Write(deductions), run_time=NORMAL)
        self.play(Write(arrow2), run_time=FAST)
        self.play(Write(theorem), run_time=NORMAL)
        self.wait(2)

        # Add explanation below
        explain = Text(
            "Each step must follow from the previous by pure logic.",
            font_size=LABEL_SIZE, color=DIM, font=SANS
        )
        self.ly.safe_place(explain, direction=DOWN, anchor=chain, buff=0.5)
        self.play(FadeIn(explain, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Types of Proofs — Preview (80s)
    # ------------------------------------------------------------------
    def scene4_types_preview(self):
        self.add_subcaption(
            "Over the next several videos, we will master four fundamental proof techniques. "
            "Direct proof, proof by contrapositive, proof by contradiction, "
            "and mathematical induction.",
            duration=16,
        )

        title = self.ly.title("Proof Techniques We'll Learn")

        cards = [
            Text("1. Direct Proof", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Contrapositive", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Contradiction", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Induction", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(cards, start_from=title)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: A First Direct Proof (90s)
    # ------------------------------------------------------------------
    def scene5_first_direct_proof(self):
        self.add_subcaption(
            "Let us see a direct proof in action. We will prove that the sum of two even integers is always even.",
            duration=10,
        )

        title = self.ly.title("A First Direct Proof")

        # Statement
        stmt = MathTex(r"\text{Prove: If } a \text{ and } b \text{ are even, then } a + b \text{ is even.}",
                       color=WHITE, font_size=BODY_SIZE)
        self.ly.safe_place(stmt, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(stmt), run_time=NORMAL)
        self.wait(1)

        # Let step
        let_step = MathTex(r"\text{Let } a = 2k,\ b = 2m \text{ for integers } k, m", color=WHITE, font_size=LABEL_SIZE)
        self.ly.safe_place(let_step, direction=DOWN, anchor=stmt, buff=0.4)
        self.play(Write(let_step), run_time=NORMAL)
        self.wait(1)

        # Algebra step
        algebra = MathTex(r"a + b = 2k + 2m = 2(k + m)", color=SECONDARY, font_size=LABEL_SIZE)
        self.ly.safe_place(algebra, direction=DOWN, anchor=let_step, buff=0.4)
        self.play(Write(algebra), run_time=NORMAL)
        self.wait(1)

        # Conclusion
        conc = MathTex(r"\therefore a + b \text{ is even}", color=ACCENT, font_size=LABEL_SIZE)
        self.ly.safe_place(conc, direction=DOWN, anchor=algebra, buff=0.4)
        self.play(Write(conc), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Outro (30s)
    # ------------------------------------------------------------------
    def scene6_outro(self):
        self.add_subcaption(
            "You now understand what a proof is and why it matters. "
            "In the next video, we dive into direct proofs — the simplest and most common technique.",
            duration=12,
        )

        play_outro(self, "Direct Proof", "Introduction to Proofs")
