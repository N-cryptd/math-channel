"""
Video 91: Direct Proof
Introduction to Proofs — Video 2 of 9 (Proof-Based Mathematics, L4)

Covers: The structure of a direct proof (assume P, derive Q), the standard
template (Let/Suppose/Then/Therefore), three examples of increasing difficulty
(sum of evens, product of odds, divisibility proof), and common mistakes to avoid.

Plan: planning/video-91-direct-proof.md

Render draft:  manim -ql scripts/undergraduate/video-91-direct-proof.py Video91_DirectProof
Render final:  manim -qh scripts/undergraduate/video-91-direct-proof.py Video91_DirectProof
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


class Video91_DirectProof(Scene):
    """Direct proof technique: assume hypothesis, chain deductions, reach conclusion."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_template()
        self.scene3_example_sum_of_evens()
        self.scene4_example_product_of_odds()
        self.scene5_example_divisibility()
        self.scene6_common_mistakes()
        self.scene7_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook — What Does "Direct" Mean? (~20s)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Direct proof is the most natural proof technique.",
            duration=8,
        )
        play_intro(self, "Direct Proof", "Introduction to Proofs")

        self.add_subcaption(
            "You know where you are going, and you walk straight there.",
            duration=8,
        )

        title = self.ly.title("What Does \"Direct\" Mean?")

        # Build the diagram: P → (straight path) → Q
        p_label = Text("P", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        q_label = Text("Q", font_size=HEADING_SIZE, color=ACCENT, font=SANS)
        arrow_direct = MathTex(r"\Longrightarrow", color=SECONDARY, font_size=HEADING_SIZE)
        arrow_label = Text("direct proof", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)

        chain = VGroup(p_label, arrow_direct, q_label).arrange(RIGHT, buff=0.6)
        self.ly.center_in_content(chain)

        self.play(Write(p_label), run_time=NORMAL)
        self.play(Write(arrow_direct), run_time=FAST)
        self.ly.safe_place(arrow_label, direction=DOWN, anchor=arrow_direct, buff=0.1)
        self.play(FadeIn(arrow_label, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(q_label), run_time=NORMAL)
        self.wait(2)

        # Add explanatory text below
        explain = Text(
            "Assume P is true. Use logic to reach Q.",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(explain, direction=DOWN, anchor=chain, buff=0.6)
        self.play(FadeIn(explain, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: The Direct Proof Template (~20s)
    # ------------------------------------------------------------------
    def scene2_template(self):
        self.add_subcaption(
            "Every direct proof follows the same four-step template.",
            duration=8,
        )

        title = self.ly.title("The Direct Proof Template")

        steps = [
            Text("1. STATE the theorem: \"If P, then Q\"",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. ASSUME P is true",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. DEDUCE: chain of logical steps",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("4. CONCLUDE: therefore Q",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(steps, start_from=title)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Example 1 — Sum of Even Numbers (~40s)
    # ------------------------------------------------------------------
    def scene3_example_sum_of_evens(self):
        self.add_subcaption(
            "Let us prove: the sum of two even integers is even.",
            duration=8,
        )

        title = self.ly.title("Example 1: Sum of Evens")

        stmt = MathTex(
            r"\text{Theorem: If } m \text{ and } n \text{ are even,}",
            r"\text{ then } m + n \text{ is even.}",
            color=WHITE, font_size=BODY_SIZE,
        )
        self.ly.safe_place(stmt, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(stmt), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Proof step by step — each caption is short (~5s)
        self.add_subcaption(
            "By definition, m equals 2k, and n equals 2j.",
            duration=7,
        )
        title2 = self.ly.title("Proof")
        step1 = MathTex(r"\text{Let } m = 2k, \ n = 2j \text{ for integers } k, j",
                         color=PRIMARY, font_size=BODY_SIZE)
        self.ly.safe_place(step1, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(title2), run_time=FAST)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(3)

        self.add_subcaption(
            "Adding: m plus n equals 2k plus 2j, which factors to 2 times k plus j.",
            duration=9,
        )
        step2 = MathTex(r"m + n = 2k + 2j = 2(k + j)",
                         color=SECONDARY, font_size=BODY_SIZE)
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.5)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "This is 2 times an integer, so the sum is even. Q.E.D.",
            duration=8,
        )
        step3 = MathTex(r"\therefore m + n = 2(k+j) \text{ is even.} \ \blacksquare",
                         color=ACCENT, font_size=BODY_SIZE)
        self.ly.safe_place(step3, direction=DOWN, anchor=step2, buff=0.5)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Example 2 — Product of Odd Numbers (~40s)
    # ------------------------------------------------------------------
    def scene4_example_product_of_odds(self):
        self.add_subcaption(
            "Next: the product of two odd integers is always odd.",
            duration=8,
        )

        title = self.ly.title("Example 2: Product of Odds")

        stmt = MathTex(
            r"\text{Theorem: If } a \text{ and } b \text{ are odd,}",
            r"\text{ then } a \cdot b \text{ is odd.}",
            color=WHITE, font_size=BODY_SIZE,
        )
        self.ly.safe_place(stmt, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(stmt), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        self.add_subcaption(
            "Let a equal 2k plus 1, and b equal 2m plus 1.",
            duration=8,
        )
        title2 = self.ly.title("Proof")
        step1 = MathTex(
            r"\text{Let } a = 2k+1, \ b = 2m+1",
            r"\text{ for integers } k, m",
            color=PRIMARY, font_size=BODY_SIZE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(title2), run_time=FAST)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "Expanding the product and grouping terms, we get:",
            duration=8,
        )
        step2 = MathTex(
            r"a \cdot b = (2k+1)(2m+1) = 4km + 2k + 2m + 1",
            color=SECONDARY, font_size=LABEL_SIZE,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.5)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "Factor out the 2 to get 2 times some integer, plus 1. That is odd. Q.E.D.",
            duration=10,
        )
        step3 = MathTex(
            r"= 2(2km + k + m) + 1 \text{, which is odd.} \ \blacksquare",
            color=ACCENT, font_size=LABEL_SIZE,
        )
        self.ly.safe_place(step3, direction=DOWN, anchor=step2, buff=0.5)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(6)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Example 3 — Divisibility (~50s)
    # ------------------------------------------------------------------
    def scene5_example_divisibility(self):
        self.add_subcaption(
            "A harder example: prove that 3 n squared plus n plus 2 is always even.",
            duration=9,
        )

        title = self.ly.title("Example 3: A Parity Proof")

        stmt = MathTex(
            r"\text{Theorem: For any integer } n,",
            r"\ 3n^2 + n + 2 \text{ is even.}",
            color=WHITE, font_size=BODY_SIZE,
        )
        self.ly.safe_place(stmt, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(stmt), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Case 1
        self.add_subcaption(
            "Case 1: n is even. Write n as 2k and substitute.",
            duration=8,
        )
        title2 = self.ly.title("Case 1: n is even")
        step1 = MathTex(
            r"n = 2k \implies 3(2k)^2 + 2k + 2",
            r"= 12k^2 + 2k + 2 = 2(6k^2 + k + 1)",
            color=PRIMARY, font_size=LABEL_SIZE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(title2), run_time=FAST)
        self.play(Write(step1), run_time=SLOW)
        self.wait(4)

        self.add_subcaption(
            "Every term has a factor of 2, so the result is even.",
            duration=7,
        )
        c1_note = Text(
            "All terms are multiples of 2. Even!",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(c1_note, direction=DOWN, anchor=step1, buff=0.3)
        self.play(FadeIn(c1_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Case 2
        self.add_subcaption(
            "Case 2: n is odd. Write n as 2k plus 1 and substitute.",
            duration=9,
        )
        title3 = self.ly.title("Case 2: n is odd")
        step2 = MathTex(
            r"n = 2k{+}1: 3n^2{+}n{+}2 = 2(6k^2{+}7k{+}3)",
            color=SECONDARY, font_size=LABEL_SIZE,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(title3), run_time=FAST)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "In both cases, the result is even. Q.E.D.",
            duration=6,
        )
        conc = MathTex(
            r"\therefore 3n^2 + n + 2 \text{ is even for all integers } n. \ \blacksquare",
            color=ACCENT, font_size=LABEL_SIZE,
        )
        self.ly.safe_place(conc, direction=DOWN, anchor=step2, buff=0.4)
        self.play(Write(conc), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Common Mistakes (~25s)
    # ------------------------------------------------------------------
    def scene6_common_mistakes(self):
        self.add_subcaption(
            "Two common mistakes to avoid when writing direct proofs.",
            duration=8,
        )

        title = self.ly.title("Common Mistakes")

        # Mistake 1
        self.add_subcaption(
            "Circular reasoning: do not use the conclusion as a step.",
            duration=8,
        )
        m1_label = Text("Mistake 1: Circular Reasoning",
                        font_size=BODY_SIZE, color=RED, font=SANS)
        self.ly.safe_place(m1_label, direction=DOWN, anchor=title, buff=0.5)
        m1_ex = MathTex(
            r"2k + 2m = 2(k+m)",
            color=RED, font_size=LABEL_SIZE,
        )
        m1_warn = Text("uses the conclusion!", font_size=SMALL_SIZE, color=RED, font=SANS)
        self.ly.safe_place(m1_ex, direction=DOWN, anchor=m1_label, buff=0.3)
        self.ly.safe_place(m1_warn, direction=RIGHT, anchor=m1_ex, buff=0.3)
        self.play(Write(m1_label), run_time=FAST)
        self.play(Write(m1_ex), run_time=FAST)
        self.play(FadeIn(m1_warn, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Mistake 2
        self.add_subcaption(
            "Assuming the conclusion. Always start from definitions.",
            duration=8,
        )
        title2 = self.ly.title("Common Mistakes (cont.)")
        m2_label = Text("Mistake 2: Assuming the Conclusion",
                         font_size=BODY_SIZE, color=RED, font=SANS)
        self.ly.safe_place(m2_label, direction=DOWN, anchor=title2, buff=0.5)
        m2_ex = MathTex(
            r"\text{Want: } a+b \text{ is even}",
            color=RED, font_size=LABEL_SIZE,
        )
        self.ly.safe_place(m2_ex, direction=DOWN, anchor=m2_label, buff=0.3)
        m2_fix = Text(
            "Fix: Start from definitions, not from the goal.",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(m2_fix, direction=DOWN, anchor=m2_ex, buff=0.3)
        self.play(Write(title2), run_time=FAST)
        self.play(Write(m2_label), run_time=FAST)
        self.play(Write(m2_ex), run_time=FAST)
        self.play(FadeIn(m2_fix, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Recap + Outro (~25s)
    # ------------------------------------------------------------------
    def scene7_outro(self):
        self.add_subcaption(
            "Direct proof: assume the hypothesis, chain deductions, reach the conclusion.",
            duration=10,
        )

        title = self.ly.title("Key Takeaways")

        items = [
            Text("Direct proof = Assume P, derive Q",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Template: Let, Expand, Deduce, Conclude",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Always start from definitions",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Avoid circular reasoning",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(6)

        play_outro(self, "Proof by Contrapositive", "Introduction to Proofs")
