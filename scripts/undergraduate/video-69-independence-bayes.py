"""
Video 69: Independence and Bayes' Theorem
Probability & Statistics -- Video 3 of 12

Covers: independence definition, equivalent forms, examples and
counterexamples, pairwise vs mutual independence, Bayes' theorem
derivation, prior/likelihood/posterior, medical test worked example,
connection between independence and Bayes.

Render draft:  manim -ql scripts/undergraduate/video-69-independence-bayes.py Video69_IndependenceBayes
Render final:  manim -qh scripts/undergraduate/video-69-independence-bayes.py Video69_IndependenceBayes
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


class Video69_IndependenceBayes(Scene):
    """Full video: Independence and Bayes' Theorem."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_examples()
        self.scene4_mutual_independence()
        self.scene5_bayes_derivation()
        self.scene6_medical_example()
        self.scene7_independence_and_bayes()
        self.scene8_summary()

    # ── Scene 1: Hook -- The Coin Paradox ─────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Flip a fair coin twice. You already know the first flip "
            "is heads. What is the probability the second flip is "
            "also heads? Most people overthink it. But the answer is "
            "simple: one half.",
            duration=24,
        )
        play_intro(self, "Independence and Bayes' Theorem",
                   "Probability & Statistics")

        title = self.ly.title("The Coin Paradox")

        # Question 1
        q1 = Text(
            "Flip two coins.  First coin is H.  P(second is H)?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(q1, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(q1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        a1 = Text(
            "Answer: 1/2  --  the flips don't affect each other",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(a1, DOWN, anchor=q1, buff=0.4)
        self.play(FadeIn(a1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.play(FadeOut(q1), FadeOut(a1), run_time=FAST)

        # Question 2
        self.add_subcaption(
            "Now a trickier version. Flip two coins and I tell you "
            "that at least one of them is heads. What is the "
            "probability that BOTH are heads?",
            duration=24,
        )

        q2 = Text(
            "Flip two coins.  At least one is H.  P(both H)?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(q2, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(q2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        a2 = Text(
            "Answer: 1/3  --  not 1/2!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(a2, DOWN, anchor=q2, buff=0.4)
        self.play(FadeIn(a2, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.play(FadeOut(q2), FadeOut(a2), run_time=FAST)

        # Teaser
        tease = Text(
            "Why? Because the first question uses independence, "
            "the second uses conditional probability.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(tease)
        ensure_fits(tease)
        self.play(FadeIn(tease, shift=UP * 0.1), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 2: Formal Definition of Independence ────────────────
    def scene2_definition(self):
        self.add_subcaption(
            "Two events A and B are independent if knowing whether "
            "B occurred tells us nothing about A. Formally, the "
            "probability of A intersect B equals the product P of A "
            "times P of B.",
            duration=24,
        )
        self.ly.section_divider(1, "Independence")

        title = self.ly.title("Definition")

        # Formal definition with formula box
        def_eq = MathTex(
            r"A", r",", r"B", r"\text{ independent }",
            r"\iff",
            r"P(A \cap B)", r"=", r"P(A)", r"\cdot", r"P(B)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        def_eq[0].set_color(PRIMARY)
        def_eq[2].set_color(PRIMARY)
        def_eq[5].set_color(PRIMARY)
        def_eq[7].set_color(PRIMARY)
        def_eq[9].set_color(PRIMARY)
        self.ly.center_in_content(def_eq)
        self.play(Write(def_eq), run_time=SLOW)
        self.wait(0.5)

        box = self.ly.formula_box(def_eq, color=ACCENT)
        self.play(Create(box), run_time=FAST)
        self.wait(1)

        self.play(FadeOut(box), FadeOut(def_eq), run_time=FAST)

        # Equivalent form
        self.add_subcaption(
            "Equivalently, P of A given B equals P of A. Conditioning "
            "on B does not change the probability of A at all.",
            duration=24,
        )

        title2 = self.ly.title("Equivalent Form")

        eq_form = MathTex(
            r"P(A|B)", r"=", r"P(A)",
            font_size=TITLE_SIZE, color=WHITE,
        )
        eq_form[0].set_color(PRIMARY)
        eq_form[2].set_color(PRIMARY)
        self.ly.center_in_content(eq_form)
        self.play(Write(eq_form), run_time=SLOW)
        self.wait(0.5)

        intuition = Text(
            '"Knowing B tells you nothing about A"',
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(intuition, DOWN, anchor=eq_form, buff=0.4)
        self.play(FadeIn(intuition, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.play(FadeOut(eq_form), FadeOut(intuition), run_time=FAST)

        # Venn diagram visualization
        self.add_subcaption(
            "Visually, the overlap area equals the product of the "
            "individual areas. This is what independence looks like "
            "in the Venn diagram.",
            duration=20,
        )

        title3 = self.ly.title("Visual Intuition")

        omega = RoundedRectangle(
            corner_radius=0.15, width=5, height=3,
            fill_color=DIM, fill_opacity=0.15,
            stroke_color=DIM, stroke_width=1.5,
        )
        self.ly.center_in_content(omega)

        omega_label = MathTex(
            r"\Omega", font_size=LABEL_SIZE, color=DIM,
        )
        omega_label.next_to(omega, LEFT, buff=0.2)

        circ_a = Circle(radius=1.0, fill_color=PRIMARY,
                         fill_opacity=0.35, stroke_color=PRIMARY,
                         stroke_width=2)
        circ_a.move_to(omega.get_center() + LEFT * 0.6)

        circ_b = Circle(radius=1.0, fill_color=SECONDARY,
                         fill_opacity=0.35, stroke_color=SECONDARY,
                         stroke_width=2)
        circ_b.move_to(omega.get_center() + RIGHT * 0.6)

        label_a = MathTex(r"A", font_size=LABEL_SIZE, color=PRIMARY)
        label_a.move_to(circ_a.get_center() + UP * 0.7)

        label_b = MathTex(r"B", font_size=LABEL_SIZE, color=SECONDARY)
        label_b.move_to(circ_b.get_center() + UP * 0.7)

        self.play(Create(omega), run_time=FAST)
        self.play(FadeIn(omega_label), run_time=FAST)
        self.play(Create(circ_a), run_time=NORMAL)
        self.play(FadeIn(label_a), run_time=FAST)
        self.play(Create(circ_b), run_time=NORMAL)
        self.play(FadeIn(label_b), run_time=FAST)
        self.wait(1)

        overlap_text = MathTex(
            r"P(A \cap B)", r"=", r"P(A)", r"\cdot", r"P(B)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        overlap_text[0].set_color(ACCENT)
        overlap_text[2].set_color(PRIMARY)
        overlap_text[4].set_color(SECONDARY)
        overlap_text.next_to(omega, DOWN, buff=0.5)
        ensure_fits(overlap_text)
        self.play(Write(overlap_text), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 3: Examples and Counterexamples ────────────────────
    def scene3_examples(self):
        self.add_subcaption(
            "Let's test this with two examples. First, two fair coin "
            "flips. Let A be heads on the first flip, B be heads on "
            "the second. P of A is one half, P of B is one half, and "
            "the probability of both is one quarter. Since one "
            "quarter equals one half times one half, they are independent.",
            duration=30,
        )
        self.ly.section_divider(2, "Examples")

        title = self.ly.title("Example 1: Coin Flips")

        # Coin flip example
        setup1 = MathTex(
            r"A", r"=", r"\text{1st flip = H},",
            r"\quad",
            r"B", r"=", r"\text{2nd flip = H}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        setup1[0].set_color(PRIMARY)
        setup1[4].set_color(SECONDARY)
        self.ly.safe_place(setup1, DOWN, anchor=title, buff=0.4)
        self.play(Write(setup1), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(setup1), run_time=FAST)

        check1 = MathTex(
            r"P(A)", r"=", r"\tfrac{1}{2},",
            r"\quad",
            r"P(B)", r"=", r"\tfrac{1}{2},",
            r"\quad",
            r"P(A \cap B)", r"=", r"\tfrac{1}{4}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        check1[0].set_color(PRIMARY)
        check1[4].set_color(SECONDARY)
        check1[8].set_color(ACCENT)
        check1[10].set_color(ACCENT)
        self.ly.safe_place(check1, DOWN, anchor=title, buff=0.4)
        self.play(Write(check1), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(check1), run_time=FAST)

        result1 = Text(
            "1/4 = (1/2)(1/2)  -- Independent!",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(result1, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(result1, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.play(FadeOut(result1), run_time=FAST)

        # Die example
        self.add_subcaption(
            "Now consider rolling a die. Let A be rolling an even "
            "number and B be rolling at least 4. P of A is one half, "
            "P of B is one half, but P of A intersect B equals P of "
            "the set 4 comma 6, which is one third. One third does "
            "not equal one quarter, so A and B are NOT independent.",
            duration=30,
        )

        title2 = self.ly.title("Example 2: Die Roll")

        setup2 = MathTex(
            r"A", r"=", r"\{2, 4, 6\},",
            r"\quad",
            r"B", r"=", r"\{4, 5, 6\}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        setup2[0].set_color(PRIMARY)
        setup2[4].set_color(SECONDARY)
        self.ly.safe_place(setup2, DOWN, anchor=title2, buff=0.4)
        self.play(Write(setup2), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(setup2), run_time=FAST)

        check2 = MathTex(
            r"P(A \cap B)", r"=", r"P(\{4, 6\})",
            r"=", r"\tfrac{2}{6}", r"=",
            r"\tfrac{1}{3}", r"\neq", r"\tfrac{1}{4}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        check2[0].set_color(ACCENT)
        check2[4].set_color(WHITE)
        check2[6].set_color(WHITE)
        check2[8].set_color(RED)
        self.ly.safe_place(check2, DOWN, anchor=title2, buff=0.4)
        self.play(Write(check2), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(check2), run_time=FAST)

        result2 = Text(
            "NOT independent!",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(result2, DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(result2, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.play(FadeOut(result2), run_time=FAST)

        # Common misconception
        self.add_subcaption(
            "A crucial warning: independence is not the same as being "
            "mutually exclusive. In fact, mutually exclusive events "
            "with positive probability are never independent, because "
            "their intersection is empty, which has probability zero.",
            duration=24,
        )

        warning = Text(
            "Independence ≠ Mutually Exclusive",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(warning, DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(warning, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1)

        detail = Text(
            "Mutually exclusive: P(A∩B)=0, but independence requires P(A)*P(B)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(detail, DOWN, anchor=warning, buff=0.3)
        self.play(FadeIn(detail, shift=LEFT * 0.1), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 4: Pairwise vs. Mutual Independence ───────────────
    def scene4_mutual_independence(self):
        self.add_subcaption(
            "What about three events? We might think that if every "
            "pair is independent, then all three are independent. "
            "But that's not true. There's a stronger condition called "
            "mutual independence.",
            duration=24,
        )
        self.ly.section_divider(3, "Mutual Independence")

        title = self.ly.title("Definition")

        # Formal definition
        def1 = MathTex(
            r"A, B, C", r"\text{ mutually independent }",
            r"\iff",
            font_size=HEADING_SIZE, color=WHITE,
        )
        def1[0].set_color(PRIMARY)
        self.ly.safe_place(def1, DOWN, anchor=title, buff=0.3)
        self.play(Write(def1), run_time=NORMAL)
        self.wait(0.5)

        # The four conditions
        conds = VGroup(
            MathTex(r"P(A \cap B)", r"=", r"P(A) P(B)",
                    font_size=BODY_SIZE, color=WHITE),
            MathTex(r"P(A \cap C)", r"=", r"P(A) P(C)",
                    font_size=BODY_SIZE, color=WHITE),
            MathTex(r"P(B \cap C)", r"=", r"P(B) P(C)",
                    font_size=BODY_SIZE, color=WHITE),
            MathTex(r"P(A \cap B \cap C)", r"=", r"P(A) P(B) P(C)",
                    font_size=BODY_SIZE, color=WHITE),
        )
        for i, c in enumerate(conds):
            c[0].set_color(ACCENT)
            c[2].set_color(ACCENT)

        conds.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        conds.next_to(def1, DOWN, buff=0.3)
        ensure_fits(conds)

        self.play(
            *[FadeIn(c, shift=LEFT * 0.15) for c in conds],
            run_time=NORMAL, lag_ratio=0.2,
        )
        self.wait(1.5)

        self.play(FadeOut(def1), FadeOut(*conds), run_time=FAST)

        # Warning
        warn_title = self.ly.title("The Pitfall")

        warn = Text(
            "Pairwise independence ≠ Mutual independence",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(warn, DOWN, anchor=warn_title, buff=0.4)
        self.play(FadeIn(warn, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(warn), run_time=FAST)

        # Counterexample
        self.add_subcaption(
            "Here is a classic counterexample. Flip two fair coins. "
            "Define A as first flip heads, B as second flip heads, "
            "and C as both flips being the same. Every pair is "
            "independent, but all three together are not.",
            duration=24,
        )

        ce_title = self.ly.title("Counterexample: Two Coin Flips")

        # Show outcome grid
        grid_labels = ["HH", "HT", "TH", "TT"]
        grid_cells = VGroup()
        for i, label in enumerate(grid_labels):
            row, col = divmod(i, 2)
            cell = RoundedRectangle(
                corner_radius=0.08,
                width=1.3, height=0.6,
                fill_color=DIM, fill_opacity=0.2,
                stroke_color=DIM, stroke_width=1,
            )
            cell.move_to(
                UP * (0.5 - row * 0.8) + LEFT * (0.7 - col * 1.5)
            )
            txt = Text(label, font_size=LABEL_SIZE, color=WHITE, font=MONO)
            txt.move_to(cell)
            grid_cells.add(VGroup(cell, txt))

        grid_cells.move_to(ORIGIN + LEFT * 1.5)

        self.play(
            *[FadeIn(g) for g in grid_cells],
            run_time=NORMAL, lag_ratio=0.15,
        )
        self.wait(0.5)

        # Define events
        ev_a = Text("A: 1st = H → {HH, HT}", font_size=LABEL_SIZE,
                     color=PRIMARY, font=SANS)
        ev_b = Text("B: 2nd = H → {HH, TH}", font_size=LABEL_SIZE,
                     color=SECONDARY, font=SANS)
        ev_c = Text("C: same → {HH, TT}", font_size=LABEL_SIZE,
                     color=ACCENT, font=SANS)
        events_list = VGroup(ev_a, ev_b, ev_c).arrange(DOWN, buff=0.25,
                                                        aligned_edge=LEFT)
        events_list.move_to(ORIGIN + RIGHT * 2.5)

        self.play(
            *[FadeIn(e, shift=LEFT * 0.15) for e in events_list],
            run_time=NORMAL, lag_ratio=0.2,
        )
        self.wait(1)

        # Show the triple intersection problem
        self.play(FadeOut(*grid_cells), FadeOut(*events_list), run_time=FAST)

        triple = MathTex(
            r"P(A \cap B \cap C)",
            r"=",
            r"P(\{HH\})",
            r"=",
            r"\tfrac{1}{4}",
            r"\neq",
            r"\left(\tfrac{1}{2}\right)^3",
            r"=",
            r"\tfrac{1}{8}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        triple[0].set_color(ACCENT)
        triple[2].set_color(WHITE)
        triple[4].set_color(WHITE)
        triple[6].set_color(RED)
        triple[8].set_color(RED)
        self.ly.center_in_content(triple)
        self.play(Write(triple), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 5: Bayes' Theorem Derivation ───────────────────────
    def scene5_bayes_derivation(self):
        self.add_subcaption(
            "Now for the main event. Bayes' theorem is one of the most "
            "important results in all of probability and statistics. "
            "It tells us how to update our beliefs when we get new "
            "evidence. And the derivation is beautifully simple.",
            duration=24,
        )
        self.ly.section_divider(4, "Bayes' Theorem")

        title = self.ly.title("Derivation")

        # Start from conditional probability
        step1 = MathTex(
            r"P(A|B)", r"=", r"\frac{P(A \cap B)}{P(B)}",
            r"\quad \cdots",
            r"(1)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        step1[0].set_color(PRIMARY)
        self.ly.safe_place(step1, DOWN, anchor=title, buff=0.5)
        self.play(Write(step1), run_time=SLOW)
        self.wait(1)

        self.play(FadeOut(step1), run_time=FAST)

        # Flip the conditional
        self.add_subcaption(
            "We can also write P of B given A. Since A intersect B "
            "equals B intersect A, we get a second expression for the "
            "same intersection.",
            duration=20,
        )

        step2 = MathTex(
            r"P(B|A)", r"=", r"\frac{P(A \cap B)}{P(A)}",
            r"\quad \Longrightarrow \quad",
            r"P(A \cap B)", r"=", r"P(B|A)", r"\cdot", r"P(A)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        step2[0].set_color(PRIMARY)
        step2[4].set_color(ACCENT)
        step2[6].set_color(ACCENT)
        step2[7].set_color(PRIMARY)
        self.ly.safe_place(step2, DOWN, anchor=title, buff=0.5)
        self.play(Write(step2), run_time=SLOW)
        self.wait(1.5)

        self.play(FadeOut(step2), run_time=FAST)

        # Substitute
        self.add_subcaption(
            "Now substitute this expression for P of A intersect B "
            "back into equation one. This gives us Bayes' theorem.",
            duration=16,
        )

        step3 = MathTex(
            r"P(A|B)", r"=", r"\frac{P(B|A)", r"\cdot", r"P(A)}{P(B)}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        step3[0].set_color(PRIMARY)
        step3[2].set_color(PRIMARY)
        step3[4].set_color(PRIMARY)
        self.ly.center_in_content(step3)
        self.play(Write(step3), run_time=SLOW)
        self.wait(0.5)

        # Highlight as the key result
        box = self.ly.formula_box(step3, color=ACCENT)
        self.play(Create(box), run_time=FAST)
        self.wait(2)

        self.play(FadeOut(box), FadeOut(step3), run_time=FAST)

        # Expand denominator with law of total probability
        self.add_subcaption(
            "We can expand the denominator using the law of total "
            "probability. The probability of B equals P of B "
            "given A times P of A, plus P of B given not A times "
            "P of not A.",
            duration=24,
        )

        title2 = self.ly.title("Full Form")

        full = MathTex(
            r"P(A|B)", r"=",
            r"\frac{P(B|A) \cdot P(A)}{P(B|A) \cdot P(A) + P(B|A^c) \cdot P(A^c)}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        full[0].set_color(PRIMARY)
        full[2].set_color(PRIMARY)
        self.ly.center_in_content(full)
        self.play(Write(full), run_time=SLOW)
        self.wait(0.5)

        box2 = self.ly.formula_box(full, color=ACCENT)
        self.play(Create(box2), run_time=FAST)
        self.wait(1)
        self.play(FadeOut(box2), run_time=FAST)

        # Prior, likelihood, posterior labels
        prior_label = Text(
            "Prior", font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        prior_label.next_to(full[2], DOWN, buff=0.6)
        self.play(FadeIn(prior_label, shift=UP * 0.1), run_time=FAST)
        self.wait(0.3)

        like_label = Text(
            "Likelihood", font_size=LABEL_SIZE, color=PRIMARY, font=SANS,
        )
        like_label.next_to(full[2], UP, buff=0.6)
        self.play(FadeIn(like_label, shift=DOWN * 0.1), run_time=FAST)
        self.wait(0.3)

        post_label = Text(
            "Posterior", font_size=LABEL_SIZE, color=ACCENT, font=SANS,
            weight=BOLD,
        )
        post_label.next_to(full[0], UP, buff=0.6)
        self.play(FadeIn(post_label, shift=DOWN * 0.1), run_time=FAST)
        self.wait(2)

        self.ly.clear()

    # ── Scene 6: Worked Example -- Medical Test ─────────────────
    def scene6_medical_example(self):
        self.add_subcaption(
            "Let's apply Bayes' theorem to the medical test problem. "
            "A disease affects 1 in 1000 people. The test is 99 "
            "percent accurate. If you test positive, what is the "
            "probability you actually have the disease?",
            duration=24,
        )
        self.ly.section_divider(5, "Worked Example")

        title = self.ly.title("The Medical Test")

        # Setup parameters
        prev = MathTex(
            r"P(D)", r"=", r"0.001",
            r"\qquad",
            r"P(+|D)", r"=", r"0.99",
            r"\qquad",
            r"P(+|D^c)", r"=", r"0.01",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prev[0].set_color(PRIMARY)
        prev[2].set_color(PRIMARY)
        prev[4].set_color(SECONDARY)
        prev[6].set_color(SECONDARY)
        prev[8].set_color(DIM)
        prev[10].set_color(DIM)
        self.ly.safe_place(prev, DOWN, anchor=title, buff=0.4)
        self.play(Write(prev), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(prev), run_time=FAST)

        # Apply Bayes step by step
        self.add_subcaption(
            "Apply Bayes: P of D given plus equals P of plus given D "
            "times P of D, divided by P of plus given D times P of D "
            "plus P of plus given not D times P of not D.",
            duration=24,
        )

        title2 = self.ly.title("Apply Bayes' Theorem")

        bayes_num = MathTex(
            r"P(D|+)", r"=",
            r"\frac{0.99 \times 0.001}{0.99 \times 0.001 + 0.01 \times 0.999}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        bayes_num[0].set_color(PRIMARY)
        self.ly.safe_place(bayes_num, DOWN, anchor=title2, buff=0.5)
        self.play(Write(bayes_num), run_time=SLOW)
        self.wait(1)

        self.play(FadeOut(bayes_num), run_time=FAST)

        # Compute
        comp = MathTex(
            r"=", r"\frac{0.00099}{0.00099 + 0.00999}",
            r"=", r"\frac{0.00099}{0.01098}",
            r"\approx", r"0.09",
            font_size=HEADING_SIZE, color=WHITE,
        )
        comp[2].set_color(WHITE)
        comp[4].set_color(WHITE)
        comp[5].set_color(ACCENT)
        self.ly.safe_place(comp, DOWN, anchor=title2, buff=0.5)
        self.play(Write(comp), run_time=SLOW)
        self.wait(1)

        self.play(FadeOut(comp), run_time=FAST)

        # Area model
        self.add_subcaption(
            "Here is why this is so surprising. Let's visualize it "
            "with an area model. The sample space is split into "
            "disease and no disease. Most positive tests come from "
            "healthy people, not sick ones.",
            duration=24,
        )

        title3 = self.ly.title("Area Model")

        # No disease rectangle (wide)
        no_d_rect = RoundedRectangle(
            corner_radius=0.1, width=5.5, height=2.2,
            fill_color=SECONDARY, fill_opacity=0.15,
            stroke_color=SECONDARY, stroke_width=1.5,
        )
        self.ly.center_in_content(no_d_rect)

        # Disease rectangle (thin)
        d_rect = RoundedRectangle(
            corner_radius=0.1, width=0.55, height=2.2,
            fill_color=PRIMARY, fill_opacity=0.4,
            stroke_color=PRIMARY, stroke_width=1.5,
        )
        d_rect.next_to(no_d_rect, LEFT, buff=0)

        # False positive region (part of no_d)
        fp_rect = RoundedRectangle(
            corner_radius=0.05, width=5.5 * 0.01, height=2.2,
            fill_color=RED, fill_opacity=0.6,
            stroke_width=0,
        )
        fp_rect.move_to(no_d_rect.get_center() + LEFT * (2.5 - 0.0275))
        # Make false positives visible by scaling up for visual effect
        fp_display = RoundedRectangle(
            corner_radius=0.05, width=0.8, height=2.2,
            fill_color=RED, fill_opacity=0.5,
            stroke_color=RED, stroke_width=1,
        )
        fp_display.move_to(no_d_rect.get_center() + LEFT * 2.0)

        # True positive region (part of d)
        tp_display = RoundedRectangle(
            corner_radius=0.05, width=0.45, height=2.2,
            fill_color=ACCENT, fill_opacity=0.6,
            stroke_color=ACCENT, stroke_width=1,
        )
        tp_display.move_to(d_rect.get_center())

        self.play(Create(no_d_rect), run_time=NORMAL)
        self.play(Create(d_rect), run_time=NORMAL)
        self.wait(0.5)

        # Labels
        no_d_label = Text("No Disease (99.9%)", font_size=SMALL_SIZE,
                           color=SECONDARY, font=SANS)
        no_d_label.next_to(no_d_rect, UP, buff=0.2)
        d_label = Text("Disease", font_size=SMALL_SIZE,
                         color=PRIMARY, font=SANS)
        d_label.next_to(d_rect, UP, buff=0.2)

        self.play(FadeIn(no_d_label), FadeIn(d_label), run_time=FAST)
        self.wait(0.5)

        # Show positive test regions
        self.play(FadeIn(fp_display), FadeIn(tp_display), run_time=NORMAL)
        self.wait(0.5)

        fp_label = Text("False +", font_size=SMALL_SIZE,
                          color=RED, font=SANS)
        fp_label.next_to(fp_display, DOWN, buff=0.15)
        tp_label = Text("True +", font_size=SMALL_SIZE,
                          color=ACCENT, font=SANS)
        tp_label.next_to(tp_display, DOWN, buff=0.15)

        self.play(FadeIn(fp_label), FadeIn(tp_label), run_time=FAST)
        self.wait(1)

        # Answer reveal
        answer = Text(
            "~9%  --  Most positives are false alarms!",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(answer, DOWN, anchor=no_d_rect, buff=0.4)
        self.play(FadeIn(answer, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 7: Independence and Bayes Connection ────────────────
    def scene7_independence_and_bayes(self):
        self.add_subcaption(
            "Let's connect the two topics. What happens if A and B "
            "are independent? Then Bayes' theorem simplifies "
            "dramatically.",
            duration=16,
        )
        self.ly.section_divider(6, "Putting It Together")

        title = self.ly.title("If A and B Are Independent")

        # Start with Bayes
        bayes = MathTex(
            r"P(A|B)", r"=",
            r"\frac{P(B|A) \cdot P(A)}{P(B)}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        bayes[0].set_color(PRIMARY)
        self.ly.safe_place(bayes, DOWN, anchor=title, buff=0.5)
        self.play(Write(bayes), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(bayes), run_time=FAST)

        # Simplify using independence
        self.add_subcaption(
            "If A and B are independent, then P of B given A "
            "equals P of B. Substituting into Bayes, the P of B "
            "terms cancel, and we get P of A given B equals P of A. "
            "No new information at all.",
            duration=20,
        )

        simp1 = MathTex(
            r"P(A|B)", r"=",
            r"\frac{P(B) \cdot P(A)}{P(B)}",
            r"=", r"P(A)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        simp1[0].set_color(PRIMARY)
        simp1[4].set_color(PRIMARY)
        self.ly.safe_place(simp1, DOWN, anchor=title, buff=0.5)
        self.play(TransformFromCopy(bayes, simp1), run_time=SLOW)
        self.wait(1.5)

        self.play(FadeOut(simp1), run_time=FAST)

        # Key insight
        insight = Text(
            "Independence = evidence tells you nothing",
            font_size=HEADING_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(insight)
        self.play(FadeIn(insight, shift=UP * 0.1), run_time=NORMAL)
        self.wait(1.5)

        self.play(FadeOut(insight), run_time=FAST)

        # The exciting version
        insight2 = Text(
            "Bayes' theorem is powerful precisely",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(insight2)
        self.play(FadeIn(insight2, shift=UP * 0.1), run_time=NORMAL)
        self.wait(0.5)

        insight3 = Text(
            "when events are NOT independent",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(insight3, DOWN, anchor=insight2, buff=0.2)
        self.play(FadeIn(insight3, shift=UP * 0.1), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 8: Summary and Outro ──────────────────────────────
    def scene8_summary(self):
        self.add_subcaption(
            "Let's recap what we learned today. Independence means "
            "knowing one event tells you nothing about another, and "
            "it has a precise definition. Mutual independence is a "
            "stronger condition. Bayes' theorem lets us update our "
            "beliefs with evidence.",
            duration=24,
        )

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "Independence:  P(A ∩ B) = P(A) · P(B)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Equivalent:  P(A|B) = P(A)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Pairwise ≠ Mutual  (need P(A∩B∩C) = P(A)P(B)P(C))",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Bayes:  P(A|B) = P(B|A)·P(A) / P(B)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Prior → Likelihood → Posterior",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

        self.add_subcaption(
            "Next time, we will introduce random variables, which "
            "turn events into numbers and give us powerful tools "
            "for modeling real-world phenomena.",
            duration=24,
        )

        play_outro(
            self,
            next_video="Random Variables",
            next_playlist="Probability & Statistics",
        )
