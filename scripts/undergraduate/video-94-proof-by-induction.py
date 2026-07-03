"""
Video 94: Proof by Mathematical Induction
Introduction to Proofs -- Video 5 of 9 (Proof-Based Mathematics, L5)

Covers: The domino analogy for induction, the formal Principle of Mathematical
Induction (base case + inductive step), the anatomy of an induction proof,
two worked examples (sum formula 1+2+...+n=n(n+1)/2 and 2^n > n),
when to use induction, and the strong induction variant.

Plan: planning/video-94-proof-by-induction.md

Render draft:  manim -ql scripts/undergraduate/video-94-proof-by-induction.py Video94_ProofByInduction
Render final:  manim -qh scripts/undergraduate/video-94-proof-by-induction.py Video94_ProofByInduction
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


class Video94_ProofByInduction(Scene):
    """Proof by induction: base case + inductive step = infinite certainty."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_domino_hook()
        self.scene2_why_induction()
        self.scene3_principle()
        self.scene4_anatomy()
        self.scene5_sum_formula()
        self.scene6_inequality()
        self.scene7_when_to_use()
        self.scene8_strong_induction()
        self.scene9_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook -- The Domino Effect (~30s)
    # ------------------------------------------------------------------
    def scene1_domino_hook(self):
        self.add_subcaption(
            "Imagine a line of dominoes. You push the first one, "
            "and each domino knocks over the next.",
            duration=10,
        )
        play_intro(self, "Proof by Induction", "Introduction to Proofs")

        # Create domino rectangles
        num_dominos = 7
        dominos = []
        for i in range(num_dominos):
            d = RoundedRectangle(
                corner_radius=0.05,
                width=0.5, height=1.2,
                fill_color=WHITE, fill_opacity=0.85,
                stroke_color=DIM, stroke_width=1,
            )
            d.shift(RIGHT * i * 0.65)
            dominos.append(d)

        domino_group = VGroup(*dominos)
        domino_group.move_to(DOWN * 0.3)
        self.ly.center_in_content(domino_group)

        self.add_subcaption(
            "If every domino is guaranteed to knock over the next one, "
            "then pushing just the first one makes them ALL fall.",
            duration=10,
        )
        self.play(FadeIn(domino_group, shift=UP * 0.2), run_time=NORMAL)

        # Animate dominoes falling one by one
        falling_anims = []
        for i, d in enumerate(dominos):
            falling_anims.append(
                d.animate.rotate(PI / 6).set_fill(opacity=0.4)
            )

        # Sequential fall
        for i, anim in enumerate(falling_anims):
            if i == 0:
                self.play(anim, run_time=FAST)
            else:
                # Make each domino fall as the previous one reaches it
                self.play(anim, run_time=FAST)

        self.wait(1)

        # Label: "This is induction."
        self.add_subcaption(
            "This simple idea is one of the most powerful proof "
            "techniques in all of mathematics.",
            duration=8,
        )
        label = Text(
            "This is mathematical induction.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(label, direction=UP, anchor=domino_group, buff=0.5)
        self.play(Write(label), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Why We Need Induction (~40s)
    # ------------------------------------------------------------------
    def scene2_why_induction(self):
        self.add_subcaption(
            "Suppose we want to prove that some statement is true "
            "for every positive integer n.",
            duration=8,
        )
        title = self.ly.title("Why We Need Induction")

        # Build left column: infinite checklist
        self.add_subcaption(
            "We could check n equals 1, then n equals 2, then 3, "
            "then 4... but we can never check all infinitely many cases.",
            duration=10,
        )

        check_label = Text("Direct check:", font_size=LABEL_SIZE, color=DIM, font=SANS)
        checks = VGroup(
            MathTex(r"n=1\;\checkmark", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"n=2\;\checkmark", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"n=3\;\checkmark", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"n=4\;\checkmark", font_size=BODY_SIZE, color=SECONDARY),
            Text("...", font_size=HEADING_SIZE, color=RED, font=SANS),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        check_group = VGroup(check_label, checks).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        # Build right column: induction shortcut
        shortcut_box = RoundedRectangle(
            corner_radius=0.15,
            fill_color=PRIMARY,
            fill_opacity=0.12,
            stroke_color=PRIMARY,
            stroke_width=1.5,
            width=4.5, height=2.5,
        )
        ind_label = Text("Induction:", font_size=LABEL_SIZE, color=PRIMARY, font=SANS)
        ind_step1 = Text("1. Check n = 1", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        ind_step2 = Text("2. Show: if n=k works,", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        ind_step3 = Text("   then n=k+1 works", font_size=BODY_SIZE, color=ACCENT, font=SANS)
        ind_items = VGroup(ind_step1, ind_step2, ind_step3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        ind_group = VGroup(ind_label, ind_items).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        ind_group.move_to(shortcut_box)

        shortcut_col = VGroup(shortcut_box, ind_group)

        # Use two_columns for proper v2 positioning
        left_col, right_col = self.ly.two_columns(
            [check_group], [shortcut_col], start_from=title,
        )

        # Animate left column first (sequential reveal)
        self.play(
            FadeIn(check_label, shift=LEFT * 0.1),
            run_time=FAST,
        )
        for c in checks:
            self.play(FadeIn(c, shift=LEFT * 0.1), run_time=FAST)
            self.wait(0.3)
        self.wait(1)

        # Animate right column
        self.add_subcaption(
            "Mathematical induction gives us a way to prove all "
            "infinitely many cases using just two finite steps.",
            duration=10,
        )
        self.play(
            FadeIn(shortcut_box),
            FadeIn(ind_label, shift=LEFT * 0.1),
            run_time=NORMAL,
        )
        self.play(FadeIn(ind_step1, shift=LEFT * 0.1), run_time=FAST)
        self.wait(0.5)
        self.play(FadeIn(ind_step2, shift=LEFT * 0.1), run_time=FAST)
        self.play(FadeIn(ind_step3, shift=LEFT * 0.1), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: The Principle of Mathematical Induction (~50s)
    # ------------------------------------------------------------------
    def scene3_principle(self):
        self.add_subcaption(
            "Here is the formal statement of the Principle of "
            "Mathematical Induction.",
            duration=8,
        )
        title = self.ly.title("The Principle of Induction")

        # Statement box
        stmt_box = RoundedRectangle(
            corner_radius=0.15,
            fill_color=PRIMARY,
            fill_opacity=0.08,
            stroke_color=PRIMARY,
            stroke_width=1.5,
            width=10.0, height=3.5,
        )
        self.ly.safe_place(stmt_box, direction=DOWN, anchor=title, buff=0.5)

        # P(n) label
        pn_label = MathTex(
            r"\text{Let } P(n) \text{ be a statement about integers } n \ge 1.",
            font_size=BODY_SIZE, color=WHITE,
        )
        pn_label.move_to(stmt_box.get_top() + DOWN * 0.5)

        self.play(FadeIn(stmt_box), Write(pn_label), run_time=NORMAL)
        self.wait(2)

        # Step 1: Base case
        self.add_subcaption(
            "Step 1: The base case. Prove that P of 1 is true.",
            duration=8,
        )
        step1 = MathTex(
            r"\textbf{(1) Base case: } P(1) \text{ is true.}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        step1.move_to(pn_label.get_bottom() + DOWN * 0.5)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(2)

        # Step 2: Inductive step
        self.add_subcaption(
            "Step 2: The inductive step. Show that for every k "
            "greater than or equal to 1, if P of k is true, "
            "then P of k plus 1 must also be true.",
            duration=12,
        )
        step2 = MathTex(
            r"\textbf{(2) Inductive step: } P(k) \Longrightarrow P(k+1)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        step2.move_to(step1.get_bottom() + DOWN * 0.5)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(2)

        # Conclusion
        self.add_subcaption(
            "If both steps hold, then P of n is true for "
            "every positive integer n.",
            duration=8,
        )
        conclusion = MathTex(
            r"\text{Then } P(n) \text{ is true for all } n \ge 1. \quad \blacksquare",
            font_size=BODY_SIZE, color=ACCENT,
        )
        conclusion.move_to(step2.get_bottom() + DOWN * 0.6)
        self.play(Write(conclusion), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Anatomy of an Induction Proof (~35s)
    # ------------------------------------------------------------------
    def scene4_anatomy(self):
        self.add_subcaption(
            "Every proof by induction follows the same recipe. "
            "Let's break it down.",
            duration=8,
        )
        title = self.ly.title("Anatomy of an Induction Proof")

        # Recipe card
        recipe_box = RoundedRectangle(
            corner_radius=0.2,
            fill_color=BG,
            fill_opacity=0.9,
            stroke_color=PRIMARY,
            stroke_width=2,
            width=8.0, height=4.5,
        )
        self.ly.center_in_content(recipe_box)

        items = [
            (r"\textbf{1. Base Case}", r"\text{Prove } P(1)", SECONDARY),
            (r"\textbf{2. Hypothesis}", r"\text{Assume } P(k) \text{ for some } k \ge 1", PRIMARY),
            (r"\textbf{3. Inductive Step}", r"\text{Prove } P(k+1) \text{ using the hypothesis}", ACCENT),
            (r"\textbf{4. Conclusion}", r"P(n) \text{ is true for all } n \ge 1", WHITE),
        ]

        recipe_items = VGroup()
        for i, (label_tex, desc_tex, color) in enumerate(items):
            label = MathTex(label_tex, font_size=LABEL_SIZE, color=color)
            desc = MathTex(desc_tex, font_size=BODY_SIZE, color=color)
            row = VGroup(label, desc).arrange(RIGHT, buff=0.5)
            recipe_items.add(row)

        recipe_items.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        recipe_items.move_to(recipe_box)

        self.play(FadeIn(recipe_box), run_time=FAST)
        for item in recipe_items:
            self.play(FadeIn(item, shift=LEFT * 0.15), run_time=NORMAL)
            self.wait(1)
        self.wait(4)

        # Key note
        self.add_subcaption(
            "The inductive hypothesis is the key ingredient. "
            "You assume P of k is true, and use that fact to "
            "show that P of k plus 1 follows.",
            duration=10,
        )
        note = Text(
            "The hypothesis P(k) is your tool — use it to reach P(k+1).",
            font_size=LABEL_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=recipe_box, buff=0.5)
        self.ly.clear()
        self.play(FadeIn(note, shift=UP * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Example 1 -- Sum Formula with Grid Visual (~150s)
    # ------------------------------------------------------------------
    def scene5_sum_formula(self):
        # Part A: Statement + Grid visual
        self.add_subcaption(
            "Let's prove one of the most famous formulas in mathematics: "
            "the sum of the first n positive integers equals "
            "n times n plus 1, all divided by 2.",
            duration=12,
        )
        title = self.ly.title("Example: Sum Formula")

        # Statement P(n)
        statement = MathTex(
            r"P(n):\; 1 + 2 + \cdots + n = \frac{n(n+1)}{2}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(statement, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(statement), run_time=NORMAL)
        self.wait(3)

        # Grid visualization for n=4
        self.add_subcaption(
            "Here is a visual way to see this. For n equals 4, "
            "the sum 1 plus 2 plus 3 plus 4 forms a right triangle "
            "of dots: one row of one, one row of two, and so on.",
            duration=12,
        )
        self.ly.clear()

        title2 = self.ly.title("Visual Proof: The Triangle Trick")

        # Build a triangle of dots for n=4
        dot_groups = VGroup()
        colors_dot = [PRIMARY, SECONDARY, ACCENT, RED]
        for row in range(1, 5):
            row_dots = VGroup(*[
                Dot(radius=0.08, color=colors_dot[row - 1])
                for _ in range(row)
            ]).arrange(RIGHT, buff=0.25)
            dot_groups.add(row_dots)
        dot_groups.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.ly.center_in_content(dot_groups)

        self.play(LaggedStart(*[FadeIn(d) for d in dot_groups], lag_ratio=0.3), run_time=NORMAL)
        self.wait(2)

        # Label: "10 dots = 4(5)/2"
        label_sum = MathTex(
            r"1+2+3+4 = 10 = \frac{4 \cdot 5}{2}",
            font_size=LABEL_SIZE, color=ACCENT,
        )
        self.ly.safe_place(label_sum, direction=DOWN, anchor=dot_groups, buff=0.5)
        self.play(Write(label_sum), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Part B: Base case
        self.add_subcaption(
            "Now the proof. Step 1, the base case: n equals 1.",
            duration=6,
        )
        title3 = self.ly.title("Example: Sum Formula")

        base_label = Text("Base case (n = 1):", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)
        base_eq = MathTex(
            r"1 = \frac{1 \cdot 2}{2} = 1 \quad \checkmark",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        base_group = VGroup(base_label, base_eq).arrange(DOWN, buff=0.3)
        self.ly.safe_place(base_group, direction=DOWN, anchor=title3, buff=0.5)

        self.play(
            FadeIn(base_label, shift=LEFT * 0.1),
            Write(base_eq),
            run_time=NORMAL,
        )
        self.wait(3)

        self.ly.clear()

        # Part C: Inductive hypothesis + step
        self.add_subcaption(
            "Step 2: The inductive hypothesis. Assume that for some "
            "k greater than or equal to 1, the formula holds.",
            duration=10,
        )
        title4 = self.ly.title("Example: Sum Formula")

        hyp_label = Text("Inductive hypothesis:", font_size=LABEL_SIZE, color=PRIMARY, font=SANS)
        hyp_eq = MathTex(
            r"1 + 2 + \cdots + k = \frac{k(k+1)}{2}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        hyp_group = VGroup(hyp_label, hyp_eq).arrange(DOWN, buff=0.3)
        self.ly.safe_place(hyp_group, direction=DOWN, anchor=title4, buff=0.5)

        self.play(
            FadeIn(hyp_label, shift=LEFT * 0.1),
            Write(hyp_eq),
            run_time=NORMAL,
        )
        self.wait(3)

        # Inductive step
        self.add_subcaption(
            "Step 3: The inductive step. We want to prove the formula "
            "for k plus 1. Start with the left side and add k plus 1.",
            duration=12,
        )
        step_label = Text("Inductive step (prove P(k+1)):", font_size=LABEL_SIZE, color=ACCENT, font=SANS)

        # Algebra line by line
        line1 = MathTex(
            r"1 + 2 + \cdots + k + (k+1) = \frac{k(k+1)}{2} + (k+1)",
            font_size=BODY_SIZE, color=WHITE,
        )
        # Show substitution of hypothesis
        line2 = MathTex(
            r"= (k+1)\left(\frac{k}{2} + 1\right)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        line3 = MathTex(
            r"= (k+1)\cdot\frac{k+2}{2}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        line4 = MathTex(
            r"= \frac{(k+1)(k+2)}{2} \quad \blacksquare",
            font_size=BODY_SIZE, color=ACCENT,
        )

        self.ly.safe_place(step_label, direction=DOWN, anchor=hyp_group, buff=0.5)
        self.play(FadeIn(step_label, shift=LEFT * 0.1), run_time=FAST)

        self.ly.safe_place(line1, direction=DOWN, anchor=step_label, buff=0.4)
        self.play(Write(line1), run_time=NORMAL)
        self.wait(2)

        self.ly.safe_place(line2, direction=DOWN, anchor=line1, buff=0.3)
        self.play(Write(line2), run_time=NORMAL)
        self.wait(2)

        self.ly.safe_place(line3, direction=DOWN, anchor=line2, buff=0.3)
        self.play(Write(line3), run_time=NORMAL)
        self.wait(2)

        self.ly.safe_place(line4, direction=DOWN, anchor=line3, buff=0.3)
        self.play(Write(line4), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Part D: Conclusion
        self.add_subcaption(
            "The formula holds for k plus 1. By the Principle of "
            "Mathematical Induction, it holds for all positive integers n.",
            duration=10,
        )
        title5 = self.ly.title("Conclusion")

        conclusion = MathTex(
            r"1 + 2 + \cdots + n = \frac{n(n+1)}{2} "
            r"\text{ for all } n \ge 1. \quad \blacksquare",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(conclusion)
        self.play(Write(conclusion), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Example 2 -- 2^n > n (~90s)
    # ------------------------------------------------------------------
    def scene6_inequality(self):
        self.add_subcaption(
            "Let's try another example. Prove that 2 to the power of n "
            "is greater than n, for all positive integers n.",
            duration=10,
        )
        title = self.ly.title("Example: " + r"$2^n > n$")

        # Statement
        statement = MathTex(
            r"P(n):\; 2^n > n \quad \text{for all } n \ge 1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(statement, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(statement), run_time=NORMAL)
        self.wait(2)

        # Base case
        self.add_subcaption(
            "Base case: n equals 1. We have 2 to the power of 1 "
            "equals 2, which is greater than 1. Done.",
            duration=8,
        )
        base = MathTex(
            r"2^1 = 2 > 1 \quad \checkmark",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(base, direction=DOWN, anchor=statement, buff=0.5)
        self.play(Write(base), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        # Inductive hypothesis
        self.add_subcaption(
            "Inductive hypothesis: assume 2 to the k is greater than k "
            "for some k greater than or equal to 1.",
            duration=8,
        )
        title2 = self.ly.title("Example: " + r"$2^n > n$")

        hyp = MathTex(
            r"\text{Assume: } 2^k > k \text{ for some } k \ge 1",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(hyp, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(hyp), run_time=NORMAL)
        self.wait(2)

        # Inductive step
        self.add_subcaption(
            "Inductive step: multiply both sides by 2. "
            "This gives 2 to the k plus 1 is greater than 2k. "
            "Since k is at least 1, 2k is at least k plus 1. "
            "Therefore 2 to the k plus 1 is greater than k plus 1.",
            duration=14,
        )

        step_line1 = MathTex(
            r"2^{k+1} = 2 \cdot 2^k > 2k",
            font_size=BODY_SIZE, color=WHITE,
        )
        step_line2 = MathTex(
            r"2k = k + k \ge k + 1 \quad (\text{since } k \ge 1)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        step_line3 = MathTex(
            r"\therefore 2^{k+1} > k + 1 \quad \blacksquare",
            font_size=BODY_SIZE, color=ACCENT,
        )

        self.ly.safe_place(step_line1, direction=DOWN, anchor=hyp, buff=0.5)
        self.play(Write(step_line1), run_time=NORMAL)
        self.wait(2)

        self.ly.safe_place(step_line2, direction=DOWN, anchor=step_line1, buff=0.4)
        self.play(Write(step_line2), run_time=NORMAL)
        self.wait(2)

        self.ly.safe_place(step_line3, direction=DOWN, anchor=step_line2, buff=0.4)
        self.play(Write(step_line3), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Conclusion
        self.add_subcaption(
            "By induction, 2 to the n is greater than n "
            "for every positive integer n.",
            duration=8,
        )
        title3 = self.ly.title("Conclusion")
        conclusion = MathTex(
            r"2^n > n \text{ for all } n \ge 1. \quad \blacksquare",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(conclusion)
        self.play(Write(conclusion), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: When to Use Induction (~40s)
    # ------------------------------------------------------------------
    def scene7_when_to_use(self):
        self.add_subcaption(
            "How do you know when to use induction? "
            "Here are the common signals.",
            duration=6,
        )
        title = self.ly.title("When to Use Induction")

        signals = [
            Text('"For all n \u2265 ..."', font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Sum and product formulas", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Recursive definitions (n!, Fibonacci)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Inequalities about sequences", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Divisibility claims", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(signals, start_from=title)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Strong Induction (~60s)
    # ------------------------------------------------------------------
    def scene8_strong_induction(self):
        self.add_subcaption(
            "There is a more powerful variant called strong induction. "
            "Instead of assuming only P of k, you assume "
            "P of 1, P of 2, all the way up to P of k.",
            duration=12,
        )
        title = self.ly.title("Strong Induction")

        # Weak induction
        weak_label = Text("Weak Induction", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        weak_desc = MathTex(
            r"\text{Assume } P(k) \Longrightarrow \text{prove } P(k+1)",
            font_size=LABEL_SIZE, color=WHITE,
        )
        weak_note = Text(
            "Single rung of a ladder",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        weak_group = VGroup(weak_label, weak_desc, weak_note).arrange(DOWN, buff=0.2)
        self.ly.safe_place(weak_group, direction=DOWN, anchor=title, buff=0.5)

        self.play(
            FadeIn(weak_label, shift=LEFT * 0.1),
            Write(weak_desc),
            FadeIn(weak_note, shift=LEFT * 0.05),
            run_time=NORMAL,
        )
        self.wait(2)

        self.ly.clear()

        # Strong induction
        self.add_subcaption(
            "Strong induction: assume ALL previous cases hold, "
            "not just the immediate predecessor. "
            "This gives you more to work with in the inductive step.",
            duration=12,
        )
        title2 = self.ly.title("Strong Induction")

        strong_label = Text("Strong Induction", font_size=BODY_SIZE, color=RED, font=SANS)
        strong_desc = MathTex(
            r"\text{Assume } P(1), P(2), \ldots, P(k) \Longrightarrow \text{prove } P(k+1)",
            font_size=LABEL_SIZE, color=WHITE,
        )
        strong_note = Text(
            "Full staircase foundation",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        strong_group = VGroup(strong_label, strong_desc, strong_note).arrange(DOWN, buff=0.2)
        self.ly.safe_place(strong_group, direction=DOWN, anchor=title2, buff=0.5)

        self.play(
            FadeIn(strong_label, shift=LEFT * 0.1),
            Write(strong_desc),
            FadeIn(strong_note, shift=LEFT * 0.05),
            run_time=NORMAL,
        )
        self.wait(3)

        self.ly.clear()

        # Key relationship
        self.add_subcaption(
            "Every weak induction proof is also a strong induction proof, "
            "because assuming P of k is a special case of assuming "
            "P of 1 through P of k. But not vice versa.",
            duration=12,
        )
        title3 = self.ly.title("Key Relationship")

        key = Text(
            "Weak \u2282 Strong  (strong is more general)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.center_in_content(key)
        self.play(FadeIn(key, shift=UP * 0.15), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Summary & Outro (~30s)
    # ------------------------------------------------------------------
    def scene9_outro(self):
        self.add_subcaption(
            "To recap: mathematical induction proves that a "
            "statement is true for all positive integers "
            "by establishing a base case and an inductive step.",
            duration=12,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("1. Base case: verify P(1) is true", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("2. Assume P(k) and prove P(k+1)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("3. The domino metaphor: first falls + chain reaction", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Strong induction: assume all previous cases", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(6)

        play_outro(self, "Proof by Cases", "Introduction to Proofs")
