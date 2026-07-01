"""
Video 92: Proof by Contrapositive
Introduction to Proofs — Video 3 of 9 (Proof-Based Mathematics, L4)

Covers: The contrapositive of an implication (P → Q ≡ ¬Q → ¬P), why they are
equivalent (truth table), when to use contrapositive instead of direct proof,
two worked examples (n² even → n even; irrational product), and the distinction
between contrapositive and contradiction.

Plan: planning/video-92-proof-by-contrapositive.md

Render draft:  manim -ql scripts/undergraduate/video-92-proof-by-contrapositive.py Video92_ProofByContrapositive
Render final:  manim -qh scripts/undergraduate/video-92-proof-by-contrapositive.py Video92_ProofByContrapositive
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


class Video92_ProofByContrapositive(Scene):
    """Proof by contrapositive: flip and negate the implication, prove the rest."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_when_to_use()
        self.scene4_example_even_square()
        self.scene5_example_rational_product()
        self.scene6_vs_contradiction()
        self.scene7_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook — The Back Door (~20s)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Sometimes the direct path is blocked, but the back door is wide open.",
            duration=8,
        )
        play_intro(self, "Proof by Contrapositive", "Introduction to Proofs")

        self.add_subcaption(
            "The contrapositive gives you an equivalent statement that may be easier to prove.",
            duration=9,
        )

        title = self.ly.title("The Back Door Strategy")

        # Original implication: P → Q  (shown as "locked")
        p_label = Text("P", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        arrow_orig = MathTex(r"\Longrightarrow", color=DIM, font_size=HEADING_SIZE)
        q_label = Text("Q", font_size=HEADING_SIZE, color=ACCENT, font=SANS)
        orig_chain = VGroup(p_label, arrow_orig, q_label).arrange(RIGHT, buff=0.6)

        locked = Text("locked", font_size=SMALL_SIZE, color=RED, font=SANS)
        orig_group = VGroup(orig_chain, locked).arrange(DOWN, buff=0.2)

        self.ly.safe_place(orig_group, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(p_label), run_time=FAST)
        self.play(Write(arrow_orig), run_time=FAST)
        self.play(Write(q_label), run_time=FAST)
        self.play(FadeIn(locked, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        # Transition to contrapositive
        self.add_subcaption(
            "The contrapositive flips and negates: not Q implies not P.",
            duration=8,
        )
        self.play(FadeOut(orig_group), run_time=FAST)

        neg_q = Text(r"\neg Q", font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        arrow_new = MathTex(r"\Longrightarrow", color=SECONDARY, font_size=HEADING_SIZE)
        neg_p = Text(r"\neg P", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        new_chain = VGroup(neg_q, arrow_new, neg_p).arrange(RIGHT, buff=0.6)

        unlocked = Text("unlocked!", font_size=SMALL_SIZE, color=SECONDARY, font=SANS)
        new_group = VGroup(new_chain, unlocked).arrange(DOWN, buff=0.2)

        self.ly.safe_place(new_group, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(neg_q), run_time=FAST)
        self.play(Write(arrow_new), run_time=FAST)
        self.play(Write(neg_p), run_time=FAST)
        self.play(FadeIn(unlocked, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Definition — What IS the Contrapositive? (~40s)
    # ------------------------------------------------------------------
    def scene2_definition(self):
        self.add_subcaption(
            "The contrapositive of an implication is formed by flipping and negating both sides.",
            duration=9,
        )

        title = self.ly.title("The Contrapositive")

        # Statement of equivalence
        equiv = MathTex(
            r"P \to Q", r"\;\equiv\;", r"\neg Q \to \neg P",
            color=WHITE, font_size=HEADING_SIZE,
        )
        equiv[0].set_color(PRIMARY)
        equiv[2].set_color(ACCENT)
        self.ly.safe_place(equiv, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(equiv), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Truth table proof
        self.add_subcaption(
            "Let us verify this with a truth table. Both columns match exactly.",
            duration=9,
        )
        title2 = self.ly.title("Truth Table Proof")

        # Build truth table as a VGroup of rows
        headers = MathTex(
            r"P", r"Q", r"P \to Q", r"\neg Q", r"\neg P", r"\neg Q \to \neg P",
            color=WHITE, font_size=LABEL_SIZE,
        )
        for h in [headers[0], headers[3], headers[4]]:
            h.set_color(PRIMARY)
        for h in [headers[1]]:
            h.set_color(ACCENT)

        rows = []
        row_data = [
            ("T", "T", "T", "F", "F", "T"),
            ("T", "F", "F", "T", "F", "F"),
            ("F", "T", "T", "F", "T", "T"),
            ("F", "F", "T", "T", "T", "T"),
        ]
        for vals in row_data:
            row = MathTex(
                *vals,
                color=WHITE, font_size=LABEL_SIZE,
            )
            # Color the P→Q and ¬Q→¬P columns
            row[2].set_color(PRIMARY)
            row[5].set_color(ACCENT)
            rows.append(row)

        table = VGroup(headers, *rows).arrange(DOWN, buff=0.15)
        ensure_fits(table, max_width=7.0)
        self.ly.safe_place(table, direction=DOWN, anchor=title2, buff=0.4)

        self.play(Write(title2), run_time=FAST)
        # Reveal rows one at a time
        self.play(Write(headers), run_time=NORMAL)
        for row in rows:
            self.play(Write(row), run_time=FAST)
            self.wait(1)
        self.wait(2)

        # Highlight matching columns
        self.add_subcaption(
            "Columns three and six match in every row. The statements are equivalent.",
            duration=8,
        )
        highlight_box = SurroundingRectangle(
            VGroup(headers, *rows),
            color=SECONDARY, buff=0.15, corner_radius=0.1,
        )
        self.play(FadeIn(highlight_box), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: When to Use Contrapositive (~30s)
    # ------------------------------------------------------------------
    def scene3_when_to_use(self):
        self.add_subcaption(
            "When should you choose contrapositive over a direct proof?",
            duration=6,
        )

        title = self.ly.title("Strategy Selection")

        criteria = [
            Text("1. The conclusion's NEGATION is simpler",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. The hypothesis's NEGATION gives you more to work with",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Direct proof hits a dead end",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(criteria, start_from=title)
        self.wait(4)

        self.ly.clear()

        # Example teaser
        self.add_subcaption(
            "For example: if n squared is even then n is even. Direct proof is awkward. Contrapositive is natural.",
            duration=10,
        )
        title2 = self.ly.title("Example Setup")

        stmt = MathTex(
            r"\text{If } n^2 \text{ is even, then } n \text{ is even.}",
            color=WHITE, font_size=BODY_SIZE,
        )
        self.ly.safe_place(stmt, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(title2), run_time=FAST)
        self.play(Write(stmt), run_time=NORMAL)
        self.wait(2)

        contrap = MathTex(
            r"\text{Contrapositive: If } n \text{ is odd, then } n^2 \text{ is odd.}",
            color=ACCENT, font_size=BODY_SIZE,
        )
        self.ly.safe_place(contrap, direction=DOWN, anchor=stmt, buff=0.5)
        self.play(Write(contrap), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Example 1 — If n² is Even, Then n is Even (~50s)
    # ------------------------------------------------------------------
    def scene4_example_even_square(self):
        self.add_subcaption(
            "Example one: prove that if n squared is even, then n is even.",
            duration=8,
        )

        title = self.ly.title("Example 1: n² Even Implies n Even")

        stmt = MathTex(
            r"\text{Theorem: If } n^2 \text{ is even, then } n \text{ is even.}",
            color=WHITE, font_size=BODY_SIZE,
        )
        self.ly.safe_place(stmt, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(title), run_time=FAST)
        self.play(Write(stmt), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Show contrapositive
        self.add_subcaption(
            "We use the contrapositive: if n is odd, then n squared is odd.",
            duration=8,
        )
        title2 = self.ly.title("Proof (Contrapositive)")

        contra = MathTex(
            r"\text{Prove: If } n \text{ is odd, then } n^2 \text{ is odd.}",
            color=ACCENT, font_size=BODY_SIZE,
        )
        self.ly.safe_place(contra, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(title2), run_time=FAST)
        self.play(Write(contra), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        # Step 1: Let n = 2k+1
        self.add_subcaption(
            "Let n equal 2k plus 1 for some integer k.",
            duration=6,
        )
        title3 = self.ly.title("Proof Steps")
        step1 = MathTex(
            r"\text{Let } n = 2k + 1 \text{ for integer } k",
            color=PRIMARY, font_size=BODY_SIZE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(title3), run_time=FAST)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(3)

        # Step 2: Square both sides
        self.add_subcaption(
            "Squaring: n squared equals 4k squared plus 4k plus 1.",
            duration=8,
        )
        step2 = MathTex(
            r"n^2 = (2k+1)^2 = 4k^2 + 4k + 1",
            color=SECONDARY, font_size=BODY_SIZE,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.5)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(4)

        # Step 3: Factor and conclude
        self.add_subcaption(
            "Factor out the 2: this is 2 times an integer plus 1, which is odd. Q.E.D.",
            duration=9,
        )
        step3 = MathTex(
            r"= 2(2k^2 + 2k) + 1 \text{, which is odd. } \blacksquare",
            color=ACCENT, font_size=BODY_SIZE,
        )
        self.ly.safe_place(step3, direction=DOWN, anchor=step2, buff=0.5)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Example 2 — Product of Rationals (~50s)
    # ------------------------------------------------------------------
    def scene5_example_rational_product(self):
        self.add_subcaption(
            "Example two: if x y is irrational, then at least one of x or y is irrational.",
            duration=9,
        )

        title = self.ly.title("Example 2: Irrational Product")

        stmt = MathTex(
            r"\text{Theorem: If } xy \text{ is irrational,}",
            r"\text{ then } x \text{ or } y \text{ is irrational.}",
            color=WHITE, font_size=BODY_SIZE,
        )
        self.ly.safe_place(stmt, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(title), run_time=FAST)
        self.play(Write(stmt), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Show contrapositive
        self.add_subcaption(
            "Contrapositive: if both x and y are rational, then x y is rational.",
            duration=8,
        )
        title2 = self.ly.title("Proof (Contrapositive)")

        contra = MathTex(
            r"\text{Prove: If } x, y \in \mathbb{Q}, \text{ then } xy \in \mathbb{Q}.",
            color=ACCENT, font_size=BODY_SIZE,
        )
        self.ly.safe_place(contra, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(title2), run_time=FAST)
        self.play(Write(contra), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        # Step 1: Write rational numbers as fractions
        self.add_subcaption(
            "Since x and y are rational, write x as a over b and y as c over d.",
            duration=8,
        )
        title3 = self.ly.title("Proof Steps")
        step1 = MathTex(
            r"x = \frac{a}{b}, \ y = \frac{c}{d}",
            r"\text{ for } a,b,c,d \in \mathbb{Z}, \ b,d \neq 0",
            color=PRIMARY, font_size=BODY_SIZE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(title3), run_time=FAST)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(4)

        # Step 2: Multiply
        self.add_subcaption(
            "Multiplying: x y equals a c over b d.",
            duration=6,
        )
        step2 = MathTex(
            r"xy = \frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}",
            color=SECONDARY, font_size=BODY_SIZE,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.5)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(3)

        # Step 3: Conclude
        self.add_subcaption(
            "This is a ratio of two integers with nonzero denominator, so it is rational. Q.E.D.",
            duration=10,
        )
        step3 = MathTex(
            r"ac, bd \in \mathbb{Z}, \ bd \neq 0",
            color=SECONDARY, font_size=BODY_SIZE,
        )
        self.ly.safe_place(step3, direction=DOWN, anchor=step2, buff=0.5)
        self.play(Write(step3), run_time=FAST)
        self.wait(2)

        step4 = MathTex(
            r"\therefore xy \in \mathbb{Q}. \ \blacksquare",
            color=ACCENT, font_size=HEADING_SIZE,
        )
        self.ly.safe_place(step4, direction=DOWN, anchor=step3, buff=0.4)
        self.play(Write(step4), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Contrapositive vs Contradiction (~35s)
    # ------------------------------------------------------------------
    def scene6_vs_contradiction(self):
        self.add_subcaption(
            "Students often confuse contrapositive with contradiction. They are different.",
            duration=8,
        )

        title = self.ly.title("Contrapositive vs. Contradiction")

        # Contrapositive description
        self.add_subcaption(
            "Contrapositive: you prove the equivalent statement, not Q implies not P.",
            duration=8,
        )
        cp_label = Text("Contrapositive", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        cp_desc = Text("Prove the equivalent: \negQ → \negP",
                       font_size=BODY_SIZE, color=WHITE, font=SANS)
        cp_note = Text("(linear proof — one assumption, one conclusion)",
                       font_size=SMALL_SIZE, color=DIM, font=SANS)

        self.ly.safe_place(cp_label, direction=DOWN, anchor=title, buff=0.5)
        self.ly.safe_place(cp_desc, direction=DOWN, anchor=cp_label, buff=0.3)
        self.ly.safe_place(cp_note, direction=DOWN, anchor=cp_desc, buff=0.2)
        self.play(Write(cp_label), run_time=FAST)
        self.play(FadeIn(cp_desc, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(cp_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Contradiction description
        self.add_subcaption(
            "Contradiction: you assume the opposite and derive a logical explosion.",
            duration=8,
        )
        title2 = self.ly.title("Contrapositive vs. Contradiction")
        cx_label = Text("Contradiction", font_size=BODY_SIZE, color=RED, font=SANS)
        cx_desc = Text("Assume P and not Q, derive False",
                       font_size=BODY_SIZE, color=WHITE, font=SANS)
        cx_note = Text("(two assumptions collide → anything false)",
                       font_size=SMALL_SIZE, color=DIM, font=SANS)

        self.ly.safe_place(cx_label, direction=DOWN, anchor=title2, buff=0.5)
        self.ly.safe_place(cx_desc, direction=DOWN, anchor=cx_label, buff=0.3)
        self.ly.safe_place(cx_note, direction=DOWN, anchor=cx_desc, buff=0.2)
        self.play(Write(title2), run_time=FAST)
        self.play(Write(cx_label), run_time=FAST)
        self.play(FadeIn(cx_desc, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(cx_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Key point
        self.add_subcaption(
            "Both are indirect methods, but contrapositive is more structured and often cleaner.",
            duration=8,
        )
        title3 = self.ly.title("Key Point")
        key_point = Text(
            "Contrapositive: an equivalent statement to prove directly.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        key_point2 = Text(
            "Contradiction: assume the worst and show it cannot happen.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(key_point, direction=DOWN, anchor=title3, buff=0.5)
        self.ly.safe_place(key_point2, direction=DOWN, anchor=key_point, buff=0.4)
        self.play(Write(title3), run_time=FAST)
        self.play(FadeIn(key_point, shift=LEFT * 0.15), run_time=NORMAL)
        self.play(FadeIn(key_point2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Recap + Outro (~25s)
    # ------------------------------------------------------------------
    def scene7_outro(self):
        self.add_subcaption(
            "The contrapositive is a powerful proof technique when the direct approach fails.",
            duration=8,
        )

        title = self.ly.title("Key Takeaways")

        items = [
            Text(r"Contrapositive: P→Q ≡ ¬Q→¬P",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Always logically equivalent to the original",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Use when negations simplify the work",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Different from contradiction!",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(6)

        play_outro(self, "Proof by Contradiction", "Introduction to Proofs")
