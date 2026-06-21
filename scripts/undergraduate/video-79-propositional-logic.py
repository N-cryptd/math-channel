"""Video 79: Propositional Logic
Discrete Mathematics -- Video 1 of 12

Covers: Liar's paradox hook, propositions, logical connectives (NOT, AND, OR,
IMPLIES, IFF), truth tables, De Morgan's laws, tautologies/contradictions,
logical equivalence.

Plan: planning/video-79-propositional-logic.md

Render draft:  manim -ql scripts/undergraduate/video-79-propositional-logic.py Video79_PropositionalLogic
Render final:  manim -qh scripts/undergraduate/video-79-propositional-logic.py Video79_PropositionalLogic
"""

from manim import *
import sys, os, math
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video79_PropositionalLogic(Scene):
    """Propositional Logic -- paradox hook, propositions, connectives,
    truth tables, De Morgan's laws, tautologies/contradictions, equivalence."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_propositions()
        self.scene3_connectives()
        self.scene4_implies_iff()
        self.scene5_truth_table_construction()
        self.scene6_de_morgan()
        self.scene7_tautologies()
        self.scene8_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook — The Liar's Paradox (1:00)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Consider this sentence: This statement is false. "
            "If it's true, then it must be false. "
            "But if it's false, then it must be true. "
            "This is the liar's paradox. "
            "To reason clearly, we need a framework that avoids "
            "such self-referential traps.",
            duration=14,
        )
        play_intro(self, "Propositional Logic", "Discrete Mathematics")

        title = self.ly.title("A Paradox")

        # The liar's paradox statement
        paradox = Text(
            '"This statement is false."',
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(paradox, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(paradox), run_time=SLOW)
        self.wait(0.5)

        # Show the circular reasoning
        branch_true = Text(
            "If TRUE  ->  must be FALSE",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        branch_false = Text(
            "If FALSE  ->  must be TRUE",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(branch_true, direction=DOWN, anchor=paradox, buff=0.5)
        self.play(FadeIn(branch_true, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.ly.safe_place(branch_false, direction=DOWN, anchor=branch_true, buff=0.4)
        self.play(FadeIn(branch_false, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Resolution teaser
        resolution = Text(
            "We need logic without paradox.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(resolution, direction=DOWN, anchor=branch_false, buff=0.5)
        self.play(FadeIn(resolution, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: What is a Proposition? (1:00)
    # ------------------------------------------------------------------
    def scene2_propositions(self):
        self.add_subcaption(
            "A proposition is a declarative sentence that is "
            "either true or false, but not both. "
            "Two plus three equals five is a proposition. "
            "X is greater than seven is not a proposition, "
            "because its truth depends on X. "
            "Close the door is a command, not a proposition.",
            duration=15,
        )
        self.ly.section_divider(2, "What is a Proposition?")

        title = self.ly.title("Declarative Sentences")

        # Definition
        defn = MathTex(
            r"\text{A \textbf{proposition} has a definite truth value: T or F}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(defn, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(defn), run_time=SLOW)
        self.wait(0.5)

        # Three examples
        ex1 = Text(
            '"2 + 3 = 5"  ->  Proposition (TRUE)',
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        ex2 = Text(
            '"x > 7"  ->  NOT a proposition (depends on x)',
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        ex3 = Text(
            '"Close the door!"  ->  NOT a proposition (command)',
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        items = [ex1, ex2, ex3]
        self.ly.progressive_reveal(items, start_from=defn)
        self.wait(1)

        # Introduce p and q
        self.ly.clear()
        title2 = self.ly.title("Propositional Variables")

        vars_text = MathTex(
            r"p, q, r, s, \ldots",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(vars_text, direction=DOWN, anchor=title2, buff=0.6)
        self.play(Write(vars_text), run_time=SLOW)
        self.wait(0.5)

        desc = Text(
            "Letters represent propositions (like variables in algebra)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(desc, direction=DOWN, anchor=vars_text, buff=0.5)
        self.play(FadeIn(desc, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Logical Connectives (1:30)
    # ------------------------------------------------------------------
    def scene3_connectives(self):
        self.add_subcaption(
            "Logical connectives combine propositions to build "
            "complex statements. NOT negates a proposition, "
            "flipping its truth value. AND is true only when both "
            "propositions are true. OR is false only when both "
            "are false. Each connective has its own truth table.",
            duration=17,
        )
        self.ly.section_divider(3, "Logical Connectives")

        # --- NOT ---
        title_not = self.ly.title("NOT  (Negation)")

        not_symbol = MathTex(
            r"\neg p",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(not_symbol, direction=DOWN, anchor=title_not, buff=0.5)
        self.play(Write(not_symbol), run_time=NORMAL)
        self.wait(0.3)

        not_table = self._make_mini_table(
            ["p", r"\neg p"],
            [["T", "F"], ["F", "T"]],
            col_colors=[PRIMARY, ACCENT],
        )
        self.ly.safe_place(not_table, direction=DOWN, anchor=not_symbol, buff=0.5)
        self.play(Create(not_table), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # --- AND ---
        title_and = self.ly.title("AND  (Conjunction)")

        and_symbol = MathTex(
            r"p \land q",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(and_symbol, direction=DOWN, anchor=title_and, buff=0.5)
        self.play(Write(and_symbol), run_time=NORMAL)
        self.wait(0.3)

        and_table = self._make_mini_table(
            ["p", "q", r"p \land q"],
            [["T", "T", "T"], ["T", "F", "F"], ["F", "T", "F"], ["F", "F", "F"]],
            col_colors=[PRIMARY, SECONDARY, ACCENT],
        )
        self.ly.safe_place(and_table, direction=DOWN, anchor=and_symbol, buff=0.5)
        self.play(Create(and_table), run_time=NORMAL)
        self.wait(1)

        and_note = Text(
            "True only when BOTH are true",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(and_note, direction=DOWN, anchor=and_table, buff=0.4)
        self.play(FadeIn(and_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # --- OR ---
        title_or = self.ly.title("OR  (Disjunction)")

        or_symbol = MathTex(
            r"p \lor q",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(or_symbol, direction=DOWN, anchor=title_or, buff=0.5)
        self.play(Write(or_symbol), run_time=NORMAL)
        self.wait(0.3)

        or_table = self._make_mini_table(
            ["p", "q", r"p \lor q"],
            [["T", "T", "T"], ["T", "F", "T"], ["F", "T", "T"], ["F", "F", "F"]],
            col_colors=[PRIMARY, SECONDARY, ACCENT],
        )
        self.ly.safe_place(or_table, direction=DOWN, anchor=or_symbol, buff=0.5)
        self.play(Create(or_table), run_time=NORMAL)
        self.wait(1)

        or_note = Text(
            "False only when BOTH are false",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(or_note, direction=DOWN, anchor=or_table, buff=0.4)
        self.play(FadeIn(or_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Implication and Biconditional (2:00)
    # ------------------------------------------------------------------
    def scene4_implies_iff(self):
        self.add_subcaption(
            "Implication is the trickiest connective. "
            "P implies Q is only false when P is true but Q is false. "
            "Think of it as a promise: if it rains I'll bring an umbrella. "
            "The only way to break the promise is if it rains and I don't "
            "bring the umbrella. "
            "Biconditional means if and only if, true when both "
            "propositions agree.",
            duration=20,
        )
        self.ly.section_divider(4, "Implication and Biconditional")

        # --- IMPLIES ---
        title_imp = self.ly.title("IMPLIES  (Conditional)")

        imp_symbol = MathTex(
            r"p \rightarrow q",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(imp_symbol, direction=DOWN, anchor=title_imp, buff=0.5)
        self.play(Write(imp_symbol), run_time=NORMAL)
        self.wait(0.3)

        imp_table = self._make_mini_table(
            ["p", "q", r"p \rightarrow q"],
            [["T", "T", "T"], ["T", "F", "F"], ["F", "T", "T"], ["F", "F", "T"]],
            col_colors=[PRIMARY, SECONDARY, RED],
            highlight_row=1,  # highlight the F row
        )
        self.ly.safe_place(imp_table, direction=DOWN, anchor=imp_symbol, buff=0.5)
        self.play(Create(imp_table), run_time=NORMAL)
        self.wait(0.5)

        imp_note = Text(
            "FALSE only when promise is broken: true premise, false conclusion",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(imp_note, direction=DOWN, anchor=imp_table, buff=0.4)
        self.play(FadeIn(imp_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Real-world example
        self.ly.clear()
        title_ex = self.ly.title("Promise Example")

        promise = Text(
            'If it rains (p), I\'ll bring an umbrella (q)',
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(promise, direction=DOWN, anchor=title_ex, buff=0.5)
        self.play(FadeIn(promise, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        items = [
            Text(
                "Rains + umbrella: promise kept (T)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Rains + no umbrella: BROKEN (F)",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "No rain: promise not tested (T)",
                font_size=BODY_SIZE, color=DIM, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=promise)
        self.wait(1)
        self.ly.clear()

        # --- IFF ---
        title_iff = self.ly.title("IFF  (Biconditional)")

        iff_symbol = MathTex(
            r"p \leftrightarrow q",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(iff_symbol, direction=DOWN, anchor=title_iff, buff=0.5)
        self.play(Write(iff_symbol), run_time=NORMAL)
        self.wait(0.3)

        iff_table = self._make_mini_table(
            ["p", "q", r"p \leftrightarrow q"],
            [["T", "T", "T"], ["T", "F", "F"], ["F", "T", "F"], ["F", "F", "T"]],
            col_colors=[PRIMARY, SECONDARY, RED],
        )
        self.ly.safe_place(iff_table, direction=DOWN, anchor=iff_symbol, buff=0.5)
        self.play(Create(iff_table), run_time=NORMAL)
        self.wait(0.5)

        iff_note = Text(
            "True when p and q have the SAME truth value",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(iff_note, direction=DOWN, anchor=iff_table, buff=0.4)
        self.play(FadeIn(iff_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Building Truth Tables (1:30)
    # ------------------------------------------------------------------
    def scene5_truth_table_construction(self):
        self.add_subcaption(
            "Let's build a truth table for a compound statement. "
            "We evaluate (p AND q) implies NOT p step by step. "
            "First list all combinations of p and q. "
            "Then compute p AND q, then NOT p, and finally the "
            "implication. Each column is computed from previous ones.",
            duration=18,
        )
        self.ly.section_divider(5, "Building Truth Tables")

        title = self.ly.title("Worked Example")

        expr = MathTex(
            r"(p \land q) \rightarrow \neg p",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(expr, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(expr), run_time=SLOW)
        self.wait(0.5)

        # Full truth table — build column by column
        headers = ["p", "q", r"p \land q", r"\neg p", r"(p \land q) \rightarrow \neg p"]
        rows = [
            ["T", "T", "T", "F", "F"],
            ["T", "F", "F", "F", "T"],
            ["F", "T", "F", "T", "T"],
            ["F", "F", "F", "T", "T"],
        ]
        col_colors = [PRIMARY, SECONDARY, ACCENT, ACCENT, RED]

        # Build header
        col_tex = [MathTex(h, font_size=LABEL_SIZE, color=WHITE) for h in headers]
        header_row = VGroup(*col_tex).arrange(RIGHT, buff=0.4)
        ensure_fits(header_row, max_width=12)
        self.ly.safe_place(header_row, direction=DOWN, anchor=expr, buff=0.6)
        self.play(FadeIn(header_row), run_time=NORMAL)
        self.wait(0.3)

        # Add separator line
        sep = Line(
            header_row.get_corner(DL) + DOWN * 0.1,
            header_row.get_corner(DR) + DOWN * 0.1,
            color=DIM, stroke_width=1.5,
        )
        self.play(Create(sep), run_time=FAST)
        self.wait(0.2)

        # Add rows one by one
        for i, row in enumerate(rows):
            row_mobs = []
            for j, val in enumerate(row):
                color = col_colors[j] if val == "T" else RED if val == "F" else WHITE
                row_mobs.append(
                    Text(val, font_size=LABEL_SIZE, color=color, font=MONO)
                )
            row_group = VGroup(*row_mobs).arrange(RIGHT, buff=0.4)
            ensure_fits(row_group, max_width=12)
            row_group.next_to(header_row, DOWN, buff=0.15 * (i + 1) + 0.2)
            # Align to header
            for mob, hdr in zip(row_mobs, col_tex):
                mob.align_to(hdr, LEFT)
            self.play(FadeIn(row_group), run_time=0.4)
            self.wait(0.2)

        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: De Morgan's Laws (1:30)
    # ------------------------------------------------------------------
    def scene6_de_morgan(self):
        self.add_subcaption(
            "De Morgan's laws let us distribute NOT over AND and OR. "
            "NOT of A AND B equals NOT A OR NOT B. "
            "Think: it's not the case that both happened means "
            "at least one didn't happen. "
            "Similarly, NOT of A OR B equals NOT A AND NOT B. "
            "Both sides have identical truth tables.",
            duration=17,
        )
        self.ly.section_divider(6, "De Morgan's Laws")

        # --- Law 1 ---
        title1 = self.ly.title("Law 1: Negating AND")

        law1 = MathTex(
            r"\neg(p \land q) \equiv \neg p \lor \neg q",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(law1, direction=DOWN, anchor=title1, buff=0.6)
        self.play(Write(law1), run_time=SLOW)
        self.wait(0.5)

        meaning1 = Text(
            '"NOT (both)" = "at least one is NOT"',
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(meaning1, direction=DOWN, anchor=law1, buff=0.4)
        self.play(FadeIn(meaning1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        example1 = Text(
            '"NOT (raining AND cold)" = "NOT raining OR NOT cold"',
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(example1, direction=DOWN, anchor=meaning1, buff=0.4)
        self.play(FadeIn(example1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # --- Law 2 ---
        title2 = self.ly.title("Law 2: Negating OR")

        law2 = MathTex(
            r"\neg(p \lor q) \equiv \neg p \land \neg q",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(law2, direction=DOWN, anchor=title2, buff=0.6)
        self.play(Write(law2), run_time=SLOW)
        self.wait(0.5)

        meaning2 = Text(
            '"NOT (either)" = "both are NOT"',
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(meaning2, direction=DOWN, anchor=law2, buff=0.4)
        self.play(FadeIn(meaning2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        example2 = Text(
            '"NOT (raining OR cold)" = "NOT raining AND NOT cold"',
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(example2, direction=DOWN, anchor=meaning2, buff=0.4)
        self.play(FadeIn(example2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Visual: show equivalence with same truth tables side by side
        self.ly.clear()
        title3 = self.ly.title("Verify: Same Truth Tables")

        # Left: ¬(p ∧ q), Right: ¬p ∨ ¬q
        left_header = Text(
            r"¬(p ∧ q)", font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        right_header = Text(
            r"¬p ∨ ¬q", font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        left_vals = Text(
            "F  T  T  T", font_size=BODY_SIZE, color=WHITE, font=MONO,
        )
        right_vals = Text(
            "F  T  T  T", font_size=BODY_SIZE, color=WHITE, font=MONO,
        )

        left_items = [left_header, left_vals]
        right_items = [right_header, right_vals]

        left_col, right_col = self.ly.two_columns(left_items, right_items)

        eq_symbol = MathTex(
            r"\equiv", font_size=HEADING_SIZE, color=ACCENT,
        ).move_to(ORIGIN)
        self.play(FadeIn(left_col), FadeIn(right_col), run_time=NORMAL)
        self.play(Write(eq_symbol), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Tautologies, Contradictions, and Equivalence (1:00)
    # ------------------------------------------------------------------
    def scene7_tautologies(self):
        self.add_subcaption(
            "A tautology is a statement that is always true, "
            "no matter the truth values of its variables. "
            "P OR NOT P is a classic example. "
            "A contradiction is always false, like P AND NOT P. "
            "Two statements are logically equivalent if they have "
            "identical truth tables. For instance, P implies Q is "
            "equivalent to NOT P or Q.",
            duration=18,
        )
        self.ly.section_divider(7, "Tautologies & Equivalence")

        title = self.ly.title("Special Statements")

        # Tautology
        taut = MathTex(
            r"p \lor \neg p = \text{True}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(taut, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(taut), run_time=NORMAL)
        self.wait(0.3)

        taut_label = Text(
            "TAUTOLOGY: always true (Law of Excluded Middle)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(taut_label, direction=DOWN, anchor=taut, buff=0.4)
        self.play(FadeIn(taut_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Contradiction
        contra = MathTex(
            r"p \land \neg p = \text{False}",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(contra, direction=DOWN, anchor=taut_label, buff=0.4)
        self.play(Write(contra), run_time=NORMAL)
        self.wait(0.3)

        contra_label = Text(
            "CONTRADICTION: always false",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(contra_label, direction=DOWN, anchor=contra, buff=0.4)
        self.play(FadeIn(contra_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # Logical equivalence
        title2 = self.ly.title("Logical Equivalence")

        eq_intro = Text(
            "Two statements are equivalent if they have",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(eq_intro, direction=DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(eq_intro, shift=LEFT * 0.15), run_time=NORMAL)

        eq_intro2 = Text(
            "the same truth table column:",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(eq_intro2, direction=DOWN, anchor=eq_intro, buff=0.3)
        self.play(FadeIn(eq_intro2, shift=LEFT * 0.15), run_time=FAST)

        eq_pair = MathTex(
            r"p \rightarrow q \equiv \neg p \lor q",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(eq_pair, direction=DOWN, anchor=eq_intro2, buff=0.5)
        self.play(Write(eq_pair), run_time=SLOW)
        self.wait(1)

        # Quick verification
        verify = Text(
            "Both truth tables: T, F, T, T",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(verify, direction=DOWN, anchor=eq_pair, buff=0.4)
        self.play(FadeIn(verify, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Summary + Outro (0:30)
    # ------------------------------------------------------------------
    def scene8_summary(self):
        self.add_subcaption(
            "Today we built the foundation of propositional logic. "
            "We defined propositions, the five logical connectives, "
            "truth tables, De Morgan's laws, and logical equivalence. "
            "This is the bedrock of discrete mathematics. "
            "Next time, we'll extend this to predicate logic.",
            duration=14,
        )

        title = self.ly.title("Propositional Logic Recap")

        items = [
            Text(
                "Propositions: declarative sentences with truth values",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Five connectives: NOT, AND, OR, IMPLIES, IFF",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Truth tables: systematic evaluation of compound statements",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "De Morgan's laws: distributing NOT over AND and OR",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Tautologies and logical equivalence",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()

        # Outro
        play_outro(
            self,
            next_video="Predicate Logic",
            next_playlist="Discrete Mathematics",
        )

        self.ly.clear()

    # ------------------------------------------------------------------
    # Helper: mini truth table for connectives
    # ------------------------------------------------------------------
    def _make_mini_table(self, headers, rows, col_colors=None,
                         highlight_row=None):
        """Create a compact truth table as a VGroup of Text/MathTex objects."""
        # Header row
        header_mobs = []
        for i, h in enumerate(headers):
            color = col_colors[i] if col_colors and i < len(col_colors) else WHITE
            header_mobs.append(MathTex(h, font_size=LABEL_SIZE, color=color))

        header_group = VGroup(*header_mobs).arrange(RIGHT, buff=0.35)

        # Data rows
        data_groups = []
        for ri, row in enumerate(rows):
            row_mobs = []
            for ci, val in enumerate(row):
                if val == "T":
                    color = col_colors[ci] if col_colors and ci < len(col_colors) else SECONDARY
                elif val == "F":
                    color = RED
                else:
                    color = WHITE
                row_mobs.append(
                    Text(val, font_size=LABEL_SIZE, color=color, font=MONO)
                )
            rg = VGroup(*row_mobs).arrange(RIGHT, buff=0.35)
            # Highlight row background
            if highlight_row is not None and ri == highlight_row:
                bg_rect = SurroundingRectangle(
                    rg, color=RED, fill_color=RED,
                    fill_opacity=0.15, buff=0.08, corner_radius=0.05,
                )
                rg_with_bg = VGroup(bg_rect, rg)
            else:
                rg_with_bg = rg
            data_groups.append(rg_with_bg)

        # Stack
        all_groups = [header_group] + data_groups
        table = VGroup(*all_groups).arrange(DOWN, buff=0.15, aligned_edge=LEFT)

        ensure_fits(table, max_width=10)
        return table
