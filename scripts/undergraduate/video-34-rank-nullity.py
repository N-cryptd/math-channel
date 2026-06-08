"""
Video 34: Rank and Nullity
Linear Algebra Playlist — Video 10 of 16

Covers: rank definition (pivot count and dimension of column space),
nullity, row rank equals column rank proof idea,
rank-nullity theorem, rank of special matrices.

Render draft:  manim -ql scripts/undergraduate/video-34-rank-nullity.py Video34_RankNullity
Render final:  manim -qh scripts/undergraduate/video-34-rank-nullity.py Video34_RankNullity
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


class Video34_RankNullity(Scene):
    """Full video: rank and nullity of matrices."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_what_is_rank()
        self.scene3_rank_by_example()
        self.scene4_nullity()
        self.scene5_row_equals_column_rank()
        self.scene6_rank_nullity_deep_dive()
        self.scene7_special_matrices()
        self.scene8_summary()

    # ── Scene 1: Hook + Channel Intro ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "We just met the null space and column space. "
            "Today we go deeper into their dimensions.",
            duration=5,
        )
        play_intro(self, "Rank & Nullity", "Linear Algebra")

        self.add_subcaption(
            "And we uncover a surprising fact: "
            "the row rank always equals the column rank.",
            duration=5,
        )

        recap = Text(
            "The dimensions of these subspaces reveal deep structure",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(recap)
        self.play(FadeIn(recap, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ── Scene 2: What is Rank? ─────────────────────────────────────
    def scene2_what_is_rank(self):
        self.ly.section_divider(1, "What is Rank?")
        self.wait(0.3)

        self.add_subcaption(
            "The rank of a matrix is the number of pivot columns "
            "in its row echelon form.",
            duration=6,
        )

        title = self.ly.title("Rank of a Matrix")

        defn = MathTex(
            r"\text{rank}(A) = \text{number of pivots in REF}(A)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )

        self.add_subcaption(
            "It counts how many columns are truly independent. "
            "Equivalently, it is the dimension of the column space.",
            duration=6,
        )

        equiv = Text(
            "Also equals dim(Col A) = dim(Row A)",
            font_size=BODY_SIZE, color=WHITE, font=MONO,
        )

        items = [defn, equiv]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.6)
        self.ly.center_in_content(fitted)
        self.play(Write(defn), run_time=NORMAL)
        self.play(FadeIn(equiv, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 3: Rank by Example ───────────────────────────────────
    def scene3_rank_by_example(self):
        self.add_subcaption(
            "Consider this 3 by 4 matrix.",
            duration=3,
        )

        title = self.ly.title("Rank by Example")

        mat_A = MathTex(
            r"A = \begin{bmatrix} 1 & 0 & 2 & -1 \\ "
            r"0 & 1 & -1 & 3 \\ "
            r"0 & 0 & 0 & 0 \end{bmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(mat_A, DOWN, anchor=title, buff=0.6)
        self.play(Write(mat_A), run_time=NORMAL)
        self.wait(1.0)

        self.add_subcaption(
            "This matrix is already in row echelon form. "
            "We see two pivot positions, in columns 1 and 2.",
            duration=6,
        )

        pivots = Text(
            "Pivots in columns 1 and 2",
            font_size=BODY_SIZE, color=ACCENT, font=MONO,
        )
        rank_val = MathTex(
            r"\text{rank}(A) = 2",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        nullity_val = MathTex(
            r"\text{nullity}(A) = n - \text{rank} = 4 - 2 = 2",
            font_size=HEADING_SIZE, color=SECONDARY,
        )

        pivot_group = VGroup(pivots, rank_val, nullity_val).arrange(
            DOWN, buff=0.4, aligned_edge=LEFT,
        )
        self.ly.safe_place(pivot_group, DOWN, anchor=mat_A, buff=0.5)
        self.play(FadeIn(pivots, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(rank_val), run_time=FAST)
        self.play(Write(nullity_val), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 4: Nullity ───────────────────────────────────────────
    def scene4_nullity(self):
        self.ly.section_divider(2, "Nullity")
        self.wait(0.3)

        self.add_subcaption(
            "Nullity is the dimension of the null space. "
            "It tells us how many dimensions get collapsed to zero.",
            duration=7,
        )

        title = self.ly.title("Nullity")

        defn = MathTex(
            r"\text{nullity}(A) = \dim(\text{Nul}\, A)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        formula = MathTex(
            r"\text{nullity}(A) = n - \text{rank}(A)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        note = Text(
            "Equals the number of free variables in RREF",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )

        items = [defn, formula, note]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.5)
        self.ly.center_in_content(fitted)
        self.play(Write(defn), run_time=NORMAL)
        self.play(Write(formula), run_time=FAST)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 5: Row Rank = Column Rank ────────────────────────────
    def scene5_row_equals_column_rank(self):
        self.ly.section_divider(3, "Row Rank = Column Rank")
        self.wait(0.3)

        self.add_subcaption(
            "Here is a remarkable fact: the number of independent rows "
            "always equals the number of independent columns.",
            duration=7,
        )

        title = self.ly.title("Row Rank Equals Column Rank")

        claim = Text(
            "rank = number of independent rows",
            font_size=BODY_SIZE, color=PRIMARY, font=MONO,
        )
        claim2 = Text(
            "rank = number of independent columns",
            font_size=BODY_SIZE, color=SECONDARY, font=MONO,
        )

        items = [claim, claim2]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)

        self.add_subcaption(
            "Why? Row operations preserve the row space. "
            "In RREF, the number of nonzero rows "
            "equals the number of pivot columns.",
            duration=7,
        )

        reason = Text(
            "RREF: nonzero rows = pivot columns",
            font_size=BODY_SIZE, color=ACCENT, font=MONO,
        )
        self.ly.safe_place(reason, DOWN, anchor=claim2, buff=0.4)
        self.play(FadeIn(reason, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 6: Rank-Nullity Deep Dive ────────────────────────────
    def scene6_rank_nullity_deep_dive(self):
        self.ly.section_divider(4, "The Rank-Nullity Theorem")
        self.wait(0.3)

        self.add_subcaption(
            "The rank-nullity theorem says: "
            "rank plus nullity equals the number of columns.",
            duration=5,
        )

        title = self.ly.title("Rank-Nullity Theorem")

        formula = MathTex(
            r"\text{rank}(A) + \text{nullity}(A) = n",
            font_size=HEADING_SIZE, color=WHITE,
        )

        self.add_subcaption(
            "Think of it as an accounting equation. "
            "Every column is either a pivot column, "
            "contributing to the rank, "
            "or a free column, contributing to the nullity.",
            duration=8,
        )

        metaphor = Text(
            "Pivot columns (rank) + Free columns (nullity) = All columns (n)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )

        items = [formula, metaphor]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.6)
        self.ly.center_in_content(fitted)
        self.play(Write(formula), run_time=NORMAL)
        self.play(FadeIn(metaphor, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        # Example
        self.add_subcaption(
            "For our 3 by 4 example: rank 2 plus nullity 2 "
            "equals 4 columns. The books balance.",
            duration=6,
        )

        example = MathTex(
            r"\underbrace{2}_{\text{rank}} + \underbrace{2}_{\text{nullity}}"
            r" = \underbrace{4}_{n} \quad \checkmark",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(example, DOWN, anchor=formula, buff=0.5)
        self.play(Write(example), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Rank of Special Matrices ──────────────────────────
    def scene7_special_matrices(self):
        self.add_subcaption(
            "Let us look at some important special cases.",
            duration=3,
        )

        title = self.ly.title("Rank of Special Matrices")

        # Identity matrix
        self.add_subcaption(
            "The identity matrix has full rank. "
            "Its nullity is zero because nothing gets collapsed.",
            duration=6,
        )

        ident_label = Text(
            "Identity Matrix I_n:",
            font_size=BODY_SIZE, color=PRIMARY, font=MONO,
        )
        ident_info = MathTex(
            r"\text{rank} = n, \quad \text{nullity} = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        item1 = VGroup(ident_label, ident_info).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.ly.safe_place(item1, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(item1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.0)
        self.play(FadeOut(item1), run_time=FAST)

        # Zero matrix
        self.add_subcaption(
            "The zero matrix has rank zero. "
            "Everything gets mapped to zero, "
            "so the nullity equals n.",
            duration=6,
        )

        zero_label = Text(
            "Zero Matrix (all entries 0):",
            font_size=BODY_SIZE, color=RED, font=MONO,
        )
        zero_info = MathTex(
            r"\text{rank} = 0, \quad \text{nullity} = n",
            font_size=HEADING_SIZE, color=WHITE,
        )
        item2 = VGroup(zero_label, zero_info).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.ly.safe_place(item2, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(item2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.0)
        self.play(FadeOut(item2), run_time=FAST)

        # Invertible matrix
        self.add_subcaption(
            "Any invertible matrix has full rank and zero nullity. "
            "It preserves the dimension of the space.",
            duration=6,
        )

        inv_label = Text(
            "Invertible Matrix (n x n):",
            font_size=BODY_SIZE, color=SECONDARY, font=MONO,
        )
        inv_info = MathTex(
            r"\text{rank} = n, \quad \text{nullity} = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        item3 = VGroup(inv_label, inv_info).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.ly.safe_place(item3, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(item3, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 8: Summary + Outro ───────────────────────────────────
    def scene8_summary(self):
        self.add_subcaption(
            "To summarize: rank counts independent columns, "
            "nullity counts what gets collapsed, "
            "and together they account for every column.",
            duration=7,
        )

        title = self.ly.title("Summary")

        bullet1 = Text(
            "rank(A) = number of pivots = dim(Col A)",
            font_size=BODY_SIZE, color=PRIMARY, font=MONO,
        )
        bullet2 = Text(
            "nullity(A) = n - rank(A) = dim(Nul A)",
            font_size=BODY_SIZE, color=SECONDARY, font=MONO,
        )
        bullet3 = Text(
            "Row rank always equals column rank",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )

        items = [bullet1, bullet2, bullet3]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "Next time we meet eigenvalues and eigenvectors. "
            "Thanks for watching!",
            duration=4,
        )
        play_outro(self, "Eigenvalues & Eigenvectors", "Linear Algebra")
        self.ly.clear()
