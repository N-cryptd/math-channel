"""
Video 95: Strong Induction
TEMPLATE v2 — Professional quality Manim script

Playlist: Introduction to Proofs (Video 6 of 9)
Class: Video95_StrongInduction

QUALITY RULES (enforced):
  1. Max 5 visible elements per scene at any time
  2. Use LayoutEngine for ALL positioning — no manual .shift() or .to_edge()
  3. Progressive disclosure: add items one at a time
  4. Use consistent animation vocabulary (Write, FadeIn, Create, etc.)
  5. Each add_subcaption() duration ≈ words / 2.5 seconds
  6. Call ly.clear() between scenes
  7. Raw strings for MathTex with single backslashes
  8. No font= parameter on MathTex (only on Text)
"""

from manim import *
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video95_StrongInduction(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_recap_weak()
        self.scene3_limit_fibonacci()
        self.scene4_principle_strong()
        self.scene5_weak_vs_strong()
        self.scene6_example_fibonacci()
        self.scene7_example_primes()
        self.scene8_summary()

    # ─── Scene 1: Hook — Staircase vs. Bridge ───
    def scene1_hook(self):
        self.add_subcaption(
            "Regular induction is like climbing stairs. "
            "Each step only needs the one below it. "
            "But what if your problem is like building a bridge, "
            "where each piece depends on everything before it?",
            duration=12,
        )
        play_intro(self, "Strong Induction", "Introduction to Proofs")

        # Build a simple staircase (left side)
        stair_title = Text("Weak Induction", font_size=LABEL_SIZE, color=PRIMARY, font=SANS)
        stairs = VGroup(
            Rectangle(width=1.2, height=0.3, fill_color=SECONDARY, fill_opacity=0.7, stroke_width=0),
            Rectangle(width=1.0, height=0.3, fill_color=SECONDARY, fill_opacity=0.5, stroke_width=0),
            Rectangle(width=0.8, height=0.3, fill_color=SECONDARY, fill_opacity=0.35, stroke_width=0),
            Rectangle(width=0.6, height=0.3, fill_color=SECONDARY, fill_opacity=0.25, stroke_width=0),
        ).arrange(DOWN, buff=0.05, aligned_edge=RIGHT)

        # Build a bridge (right side)
        bridge_title = Text("Strong Induction", font_size=LABEL_SIZE, color=RED, font=SANS)
        bridge_segments = VGroup(*[
            Rectangle(width=0.5, height=0.15, fill_color=ACCENT, fill_opacity=0.6, stroke_width=0)
            for _ in range(6)
        ]).arrange(RIGHT, buff=0.02)
        bridge_anchors = VGroup(*[
            Dot(radius=0.04, color=PRIMARY)
            for _ in range(7)
        ]).arrange(RIGHT, buff=0.45)
        bridge_anchors.move_to(bridge_segments)
        bridge = VGroup(bridge_anchors, bridge_segments)

        left_col, right_col = self.ly.two_columns(
            [VGroup(stair_title, stairs)],
            [VGroup(bridge_title, bridge)],
        )

        self.play(
            FadeIn(left_col, shift=LEFT * 0.15),
            FadeIn(right_col, shift=RIGHT * 0.15),
            run_time=NORMAL,
        )
        self.wait(2)

        # Arrow from each stair step to the one below
        weak_arrow = Arrow(
            stairs[2].get_bottom(), stairs[1].get_top(),
            buff=0.05, color=PRIMARY, stroke_width=2,
        )
        weak_label = Text("P(k) only", font_size=SMALL_SIZE, color=PRIMARY, font=SANS)
        weak_label.next_to(weak_arrow, LEFT, buff=0.1)

        self.play(Create(weak_arrow), Write(weak_label), run_time=FAST)
        self.wait(1)

        # Arrow from bridge segment to ALL anchors
        strong_arrow = Arrow(
            bridge_segments[3].get_bottom(), bridge_anchors[0].get_top(),
            buff=0.05, color=RED, stroke_width=2,
        )
        strong_label = Text("P(1)...P(k)", font_size=SMALL_SIZE, color=RED, font=SANS)
        strong_label.next_to(strong_arrow, RIGHT, buff=0.1)

        self.play(Create(strong_arrow), Write(strong_label), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 2: Recap — Weak Induction ───
    def scene2_recap_weak(self):
        self.add_subcaption(
            "Let's recap regular induction. "
            "The key assumption is that we only assume P of k "
            "to prove P of k plus one. Just one previous case.",
            duration=10,
        )

        title = self.ly.title("Recap: Weak (Regular) Induction")

        items = [
            MathTex(r"\text{(1) Base case: } P(1) \text{ is true}", font_size=LABEL_SIZE, color=SECONDARY),
            MathTex(r"\text{(2) Inductive step: } P(k) \Longrightarrow P(k+1)", font_size=LABEL_SIZE, color=PRIMARY),
            MathTex(r"\text{(3) Conclusion: } P(n) \text{ true for all } n \ge 1", font_size=LABEL_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1)

        # Highlight the single P(k)
        highlight = MathTex(r"P(k)", font_size=HEADING_SIZE, color=RED)
        self.ly.safe_place(highlight, direction=DOWN, anchor=items[1], buff=0.5)
        self.play(Write(highlight), run_time=FAST)
        self.wait(1)

        note = Text(
            "We only assume ONE previous case.",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=highlight, buff=0.3)
        self.play(FadeIn(note, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 3: The Limit of Weak Induction — Fibonacci ───
    def scene3_limit_fibonacci(self):
        self.add_subcaption(
            "Consider the Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, and so on. "
            "Each term is the sum of the two previous terms. "
            "If we try to prove F of n is at least n using weak induction, "
            "we get stuck because we need F of k minus 1 too.",
            duration=15,
        )

        title = self.ly.title("The Problem: Fibonacci Depends on TWO Steps")

        fib_label = Text("Fibonacci:", font_size=LABEL_SIZE, color=WHITE, font=SANS)
        fib_seq = MathTex(
            r"f_1=1,\; f_2=1,\; f_3=2,\; f_4=3,\; f_5=5,\; f_6=8,\; \ldots",
            font_size=LABEL_SIZE, color=WHITE,
        )
        fib_rule = MathTex(
            r"f_{n} = f_{n-1} + f_{n-2}",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        self.play(Write(fib_label), run_time=FAST)
        self.ly.safe_place(fib_seq, direction=DOWN, anchor=fib_label, buff=0.3)
        self.play(Write(fib_seq), run_time=FAST)
        self.ly.safe_place(fib_rule, direction=DOWN, anchor=fib_seq, buff=0.3)
        self.play(Write(fib_rule), run_time=NORMAL)
        self.wait(1)

        # Show arrows for TWO dependencies
        dep_text = Text("f_{k+1} needs BOTH f_k AND f_{k-1}!", font_size=BODY_SIZE, color=RED, font=SANS)
        self.ly.safe_place(dep_text, direction=DOWN, anchor=fib_rule, buff=0.5)
        self.play(FadeIn(dep_text, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1)

        fail_text = Text("Weak induction only gives us f_k!", font_size=BODY_SIZE, color=RED, font=SANS)
        self.ly.safe_place(fail_text, direction=DOWN, anchor=dep_text, buff=0.3)
        self.play(FadeIn(fail_text, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 4: The Principle of Strong Induction ───
    def scene4_principle_strong(self):
        self.add_subcaption(
            "The Principle of Strong Induction. "
            "If P of 1 is true, and for every k, "
            "if ALL of P of 1, P of 2, through P of k are true, "
            "then P of k plus 1 is true. "
            "Then P of n is true for all n.",
            duration=14,
        )

        self.ly.section_divider(1, "The Principle of Strong Induction")

        # Formal statement
        items = [
            MathTex(
                r"\textbf{Strong Induction Principle}",
                font_size=BODY_SIZE, color=WHITE,
            ),
            MathTex(
                r"\text{(1) Base: } P(1) \text{ is true}",
                font_size=LABEL_SIZE, color=SECONDARY,
            ),
            MathTex(
                r"\text{(2) Strong step: } P(1) \wedge P(2) \wedge \cdots \wedge P(k) \Longrightarrow P(k+1)",
                font_size=LABEL_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"\text{(3) Conclusion: } P(n) \text{ is true for all } n \ge 1",
                font_size=LABEL_SIZE, color=ACCENT,
            ),
        ]
        title = self.ly.title("Strong Induction")
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1)

        # Visual: highlight the "ALL" part
        all_label = Text(
            "Assume ALL previous cases, not just P(k)!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(all_label, direction=DOWN, anchor=items[2], buff=0.5)
        self.play(FadeIn(all_label, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 5: Weak vs. Strong — Side by Side ───
    def scene5_weak_vs_strong(self):
        self.add_subcaption(
            "The only difference is what you assume. "
            "Weak induction: assume P of k. "
            "Strong induction: assume everything from P of 1 through P of k. "
            "Since you can always ignore extra assumptions, "
            "strong induction is strictly more powerful.",
            duration=14,
        )

        title = self.ly.title("Weak vs. Strong: The Key Difference")

        weak_label = Text("Weak Induction", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        weak_hyp = MathTex(
            r"\text{Assume: } P(k) \Longrightarrow P(k+1)",
            font_size=LABEL_SIZE, color=PRIMARY,
        )
        weak_note = Text("Single previous case", font_size=SMALL_SIZE, color=DIM, font=SANS)

        strong_label = Text("Strong Induction", font_size=BODY_SIZE, color=RED, font=SANS)
        strong_hyp = MathTex(
            r"\text{Assume: } P(1) \wedge \cdots \wedge P(k) \Longrightarrow P(k+1)",
            font_size=LABEL_SIZE, color=RED,
        )
        strong_note = Text("ALL previous cases", font_size=SMALL_SIZE, color=DIM, font=SANS)

        left_items = VGroup(weak_label, weak_hyp, weak_note).arrange(DOWN, buff=0.2)
        right_items = VGroup(strong_label, strong_hyp, strong_note).arrange(DOWN, buff=0.2)

        left_col, right_col = self.ly.two_columns(
            [left_items], [right_items], start_from=title,
        )

        self.play(
            FadeIn(left_col, shift=LEFT * 0.15),
            FadeIn(right_col, shift=RIGHT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1)

        key_text = Text(
            "Strong induction is always valid — sometimes necessary!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(key_text, direction=DOWN, anchor=left_col, buff=0.4)
        self.play(FadeIn(key_text, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 6: Example 1 — Fibonacci Strong Induction Proof ───
    def scene6_example_fibonacci(self):
        self.add_subcaption(
            "Let's prove that the n-th Fibonacci number "
            "is at least n for all n greater than or equal to 5. "
            "We'll use strong induction. "
            "First, check the base cases. "
            "F of 5 equals 5, and F of 6 equals 8. Both satisfy the claim.",
            duration=16,
        )

        self.ly.section_divider(2, "Example 1: Fibonacci Bound")

        title = self.ly.title("Prove: f_n \\ge n \\text{ for all } n \\ge 5")

        # Base cases
        base_label = Text("Base cases:", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)
        base1 = MathTex(r"f_5 = 5 \ge 5 \;\checkmark", font_size=BODY_SIZE, color=SECONDARY)
        base2 = MathTex(r"f_6 = 8 \ge 6 \;\checkmark", font_size=BODY_SIZE, color=SECONDARY)
        bases = VGroup(base1, base2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(Write(base_label), run_time=FAST)
        self.ly.safe_place(bases, direction=DOWN, anchor=base_label, buff=0.2)
        self.play(Write(bases), run_time=NORMAL)
        self.wait(1)

        self.add_subcaption(
            "Strong hypothesis: assume f_i is at least i "
            "for all i from 5 to k. "
            "Now for the inductive step. "
            "We know f of k plus 1 equals f of k plus f of k minus 1. "
            "By the strong hypothesis, f of k is at least k, "
            "and f of k minus 1 is at least k minus 1. "
            "So f of k plus 1 is at least k plus k minus 1 equals 2k minus 1, "
            "which is at least k plus 1 for k at least 5. Done!",
            duration=20,
        )

        # Strong hypothesis
        hyp_label = Text("Strong hypothesis:", font_size=LABEL_SIZE, color=PRIMARY, font=SANS)
        hyp_eq = MathTex(
            r"f_i \ge i \text{ for all } 5 \le i \le k",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(hyp_label, direction=DOWN, anchor=bases, buff=0.4)
        self.play(Write(hyp_label), run_time=FAST)
        self.ly.safe_place(hyp_eq, direction=DOWN, anchor=hyp_label, buff=0.2)
        self.play(Write(hyp_eq), run_time=FAST)
        self.wait(0.5)

        # Inductive step — show the derivation
        step_label = Text("Inductive step:", font_size=LABEL_SIZE, color=ACCENT, font=SANS)
        line1 = MathTex(
            r"f_{k+1} = f_k + f_{k-1}",
            font_size=BODY_SIZE, color=WHITE,
        )
        line2 = MathTex(
            r"\ge k + (k-1) = 2k - 1",
            font_size=BODY_SIZE, color=WHITE,
        )
        line3 = MathTex(
            r"\ge k+1 \quad \text{ for } k \ge 5 \;\blacksquare",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        lines = VGroup(line1, line2, line3).arrange(DOWN, buff=0.15, aligned_edge=LEFT)

        self.ly.safe_place(step_label, direction=DOWN, anchor=hyp_eq, buff=0.4)
        self.play(Write(step_label), run_time=FAST)
        self.ly.safe_place(lines, direction=DOWN, anchor=step_label, buff=0.2)
        for line in lines:
            self.play(Write(line), run_time=NORMAL)
            self.wait(0.3)

        self.wait(1.5)
        self.ly.clear()

    # ─── Scene 7: Example 2 — Every Integer ≥ 2 is a Product of Primes ───
    def scene7_example_primes(self):
        self.add_subcaption(
            "Example 2. Every integer n greater than or equal to 2 "
            "is either prime or a product of primes. "
            "Base case: 2 is prime. "
            "Strong hypothesis: every integer from 2 to k satisfies this. "
            "If k plus 1 is prime, we are done. "
            "If k plus 1 is composite, it equals a times b, "
            "where a and b are between 2 and k. "
            "By the strong hypothesis, both a and b are products of primes. "
            "So k plus 1 is also a product of primes.",
            duration=22,
        )

        self.ly.section_divider(3, "Example 2: Products of Primes")

        title = self.ly.title("Every n >= 2 is prime or a product of primes")

        # Base case
        base_label = Text("Base case:", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)
        base_eq = MathTex(r"2 \text{ is prime } \checkmark", font_size=BODY_SIZE, color=SECONDARY)

        self.play(Write(base_label), run_time=FAST)
        self.ly.safe_place(base_eq, direction=DOWN, anchor=base_label, buff=0.2)
        self.play(Write(base_eq), run_time=FAST)
        self.wait(0.5)

        # Strong hypothesis
        hyp_label = Text("Strong hypothesis:", font_size=LABEL_SIZE, color=PRIMARY, font=SANS)
        hyp_eq = MathTex(
            r"\text{All integers } 2 \le i \le k \text{ are prime or products of primes}",
            font_size=LABEL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(hyp_label, direction=DOWN, anchor=base_eq, buff=0.4)
        self.play(Write(hyp_label), run_time=FAST)
        self.ly.safe_place(hyp_eq, direction=DOWN, anchor=hyp_label, buff=0.2)
        self.play(Write(hyp_eq), run_time=NORMAL)
        self.wait(0.5)

        # Case 1: k+1 is prime
        case1 = MathTex(
            r"\text{If } k+1 \text{ is prime: done } \checkmark",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(case1, direction=DOWN, anchor=hyp_eq, buff=0.4)
        self.play(Write(case1), run_time=NORMAL)
        self.wait(0.5)

        # Case 2: composite
        case2 = MathTex(
            r"\text{If } k+1 = a \cdot b, \; 2 \le a, b \le k",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(case2, direction=DOWN, anchor=case1, buff=0.3)
        self.play(Write(case2), run_time=NORMAL)
        self.wait(0.5)

        # Conclusion of case 2
        case2_conc = MathTex(
            r"\text{By hypothesis: } a, b \text{ are products of primes} \Longrightarrow k+1 \text{ too } \blacksquare",
            font_size=LABEL_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(case2_conc, direction=DOWN, anchor=case2, buff=0.3)
        self.play(Write(case2_conc), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 8: Summary ───
    def scene8_summary(self):
        self.add_subcaption(
            "To summarize, use strong induction when your proof step "
            "needs more than just the immediately previous case. "
            "Common signals include recurrence relations, "
            "claims about all integers above a threshold, "
            "and divisibility chains. "
            "Strong induction is always valid. "
            "Next up, we will learn proof by cases.",
            duration=15,
        )

        title = self.ly.title("When to Use Strong Induction")

        items = [
            Text("Recurrence relations (Fibonacci)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Claims about ALL integers >= threshold", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Divisibility or factorization chains", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Any problem needing MULTIPLE previous cases", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1)

        key = Text(
            "Strong induction is always valid — sometimes unnecessary.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=items[-1], buff=0.5)
        self.play(FadeIn(key, shift=LEFT * 0.1), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

        play_outro(self, "Proof by Cases", "Introduction to Proofs")
