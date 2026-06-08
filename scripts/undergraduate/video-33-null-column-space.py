"""
Video 33: Null Space and Column Space
Linear Algebra Playlist — Video 9 of 16

Covers: null space definition, finding null space via row reduction,
column space definition, pivot columns and basis, geometric visualization,
and the rank-nullity theorem.

Render draft:  manim -ql scripts/undergraduate/video-33-null-column-space.py Video33_NullColumnSpace
Render final:  manim -qh scripts/undergraduate/video-33-null-column-space.py Video33_NullColumnSpace
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


class Video33_NullColumnSpace(Scene):
    """Full video: null space and column space of a matrix."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_big_picture()
        self.scene3_null_space_definition()
        self.scene4_finding_null_space()
        self.scene5_column_space_definition()
        self.scene6_finding_column_space()
        self.scene7_geometric_visual()
        self.scene8_rank_nullity()
        self.scene9_summary()

    # ── Scene 1: Hook + Channel Intro ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Last time we reduced matrices to row echelon form. "
            "But what does that tell us about the matrix itself?",
            duration=7,
        )
        play_intro(self, "Null Space & Column Space", "Linear Algebra")

        self.add_subcaption(
            "Today we explore two fundamental subspaces "
            "hidden inside every matrix.",
            duration=5,
        )

        recap = Text(
            "Row reduction reveals the hidden structure of A",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(recap)
        self.play(FadeIn(recap, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ── Scene 2: The Big Picture ───────────────────────────────────
    def scene2_big_picture(self):
        self.add_subcaption(
            "Every matrix A defines a transformation from R n to R m. "
            "Two natural questions arise.",
            duration=6,
        )

        self.ly.title("Two Fundamental Questions")

        self.add_subcaption(
            "Question 1: Which vectors get mapped to zero? "
            "Question 2: Which vectors can we actually reach?",
            duration=7,
        )

        mapping = MathTex(
            r"A : \mathbb{R}^n \to \mathbb{R}^m",
            font_size=HEADING_SIZE, color=WHITE,
        )
        q1 = Text(
            "1. What gets sent to zero?",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        q2 = Text(
            "2. What can we reach?",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        group = VGroup(mapping, q1, q2).arrange(DOWN, buff=0.5)
        ensure_fits(group, max_height=4.0)
        self.ly.center_in_content(group)
        self.play(Write(mapping), run_time=NORMAL)
        self.play(FadeIn(q1, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(q2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 3: Null Space — Definition ───────────────────────────
    def scene3_null_space_definition(self):
        self.ly.section_divider(1, "Null Space")
        self.wait(0.3)

        self.add_subcaption(
            "The null space of A, written Nul A, "
            "is the set of all vectors x such that A x equals zero.",
            duration=8,
        )

        title = self.ly.title("Null Space (Kernel)")

        formula = MathTex(
            r"\text{Nul}\, A = \{ \mathbf{x} \in \mathbb{R}^n : A\mathbf{x} = \mathbf{0} \}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(formula, DOWN, anchor=title, buff=0.6)

        self.add_subcaption(
            "These are the vectors that get completely annihilated "
            "by the transformation. The null space is a subspace of R n.",
            duration=8,
        )

        desc1 = Text(
            "All vectors mapped to the zero vector",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        desc2 = Text(
            "Subspace of R^n (the domain)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )

        items = [formula, desc1, desc2]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.5)
        self.ly.center_in_content(fitted)
        self.play(Write(formula), run_time=NORMAL)
        self.play(FadeIn(desc1, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(desc2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 4: Finding the Null Space ────────────────────────────
    def scene4_finding_null_space(self):
        self.add_subcaption(
            "To find the null space, we solve A x equals zero "
            "using row reduction.",
            duration=5,
        )

        title = self.ly.title("Finding the Null Space")

        # Original matrix
        mat_A = MathTex(
            r"A = \begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 3 \end{bmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(mat_A, DOWN, anchor=title, buff=0.6)
        self.play(Write(mat_A), run_time=NORMAL)
        self.wait(1.0)

        # Arrow and RREF
        self.add_subcaption(
            "After Gaussian elimination, we get this reduced form. "
            "Columns 1 and 3 have pivots. Column 2 is free.",
            duration=7,
        )

        arrow = MathTex(
            r"\xrightarrow{\text{RREF}}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        rref = MathTex(
            r"\begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )

        arrow.next_to(mat_A, RIGHT, buff=0.8)
        rref.next_to(arrow, RIGHT, buff=0.8)
        clamp = VGroup(arrow, rref)
        ensure_fits(clamp, max_width=5.5)
        self.play(Write(arrow), run_time=FAST)
        self.play(Write(rref), run_time=NORMAL)
        self.wait(1.0)

        # Clear and show solution
        self.play(
            FadeOut(mat_A), FadeOut(arrow), FadeOut(rref),
            run_time=FAST,
        )
        self.remove(mat_A, arrow, rref)

        self.add_subcaption(
            "From row one: x plus 2 y equals 0, so x equals negative 2 y. "
            "From row two: z equals 0. "
            "Setting y equal to t, the null space is t times negative 2, 1, 0.",
            duration=10,
        )

        sol_title = Text(
            "Solution:",
            font_size=BODY_SIZE, color=PRIMARY, font=MONO,
        )
        sol_lines = VGroup(
            MathTex(r"x + 2y = 0 \Rightarrow x = -2y", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"z = 0", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"\text{Free: } y = t", font_size=BODY_SIZE, color=ACCENT),
            MathTex(
                r"\text{Nul}\, A = \text{span}\{(-2,\, 1,\, 0)\}",
                font_size=HEADING_SIZE, color=PRIMARY,
            ),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

        items2 = [sol_title, sol_lines]
        fitted2, _ = self.ly.stack_down(items2, start_from=title, spacing=0.4)
        self.ly.center_in_content(fitted2)
        self.play(FadeIn(sol_title, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(sol_lines), run_time=2.5)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 5: Column Space — Definition ─────────────────────────
    def scene5_column_space_definition(self):
        self.ly.section_divider(2, "Column Space")
        self.wait(0.3)

        self.add_subcaption(
            "The column space of A, written Col A, "
            "is the span of all column vectors of A.",
            duration=6,
        )

        title = self.ly.title("Column Space")

        formula = MathTex(
            r"\text{Col}\, A = \text{span}\{\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n\}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )

        self.add_subcaption(
            "It is every vector b for which "
            "the system A x equals b has a solution.",
            duration=6,
        )

        desc1 = Text(
            "All linear combinations of columns",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        desc2 = Text(
            "All vectors b reachable via Ax = b",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        desc3 = Text(
            "Subspace of R^m (the codomain)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )

        items = [formula, desc1, desc2, desc3]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.4)
        self.ly.center_in_content(fitted)
        self.play(Write(formula), run_time=NORMAL)
        self.play(FadeIn(desc1, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(desc2, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(desc3, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 6: Finding the Column Space ──────────────────────────
    def scene6_finding_column_space(self):
        self.add_subcaption(
            "The pivot columns of the RREF tell us "
            "which original columns of A form a basis.",
            duration=6,
        )

        title = self.ly.title("Finding the Column Space")

        # Show RREF with pivot indicators
        rref_label = Text(
            "RREF of A:",
            font_size=BODY_SIZE, color=WHITE, font=MONO,
        )
        rref_mat = MathTex(
            r"\begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        pivots = Text(
            "Pivots in columns 1 and 3",
            font_size=BODY_SIZE, color=ACCENT, font=MONO,
        )

        rref_group = VGroup(rref_label, rref_mat, pivots).arrange(DOWN, buff=0.3)
        self.ly.safe_place(rref_group, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(rref_label, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(rref_mat), run_time=NORMAL)
        self.play(FadeIn(pivots, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        # Clear and show basis
        self.play(FadeOut(rref_group), run_time=FAST)

        self.add_subcaption(
            "So the basis for the column space uses "
            "columns 1 and 3 of the original matrix A.",
            duration=6,
        )

        basis_label = Text(
            "Basis for Col A:",
            font_size=BODY_SIZE, color=SECONDARY, font=MONO,
        )
        basis = MathTex(
            r"\left\{ \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix},\;"
            r"\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \right\}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        dim_text = Text(
            "dim(Col A) = 2",
            font_size=BODY_SIZE, color=WHITE, font=MONO,
        )

        items = [basis_label, basis, dim_text]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.5)
        self.ly.center_in_content(fitted)
        self.play(FadeIn(basis_label, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(basis), run_time=NORMAL)
        self.play(FadeIn(dim_text, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Geometric Visualization ───────────────────────────
    def scene7_geometric_visual(self):
        self.add_subcaption(
            "Let us visualize both subspaces in three dimensions. "
            "The null space is a line through the origin.",
            duration=7,
        )

        title = self.ly.title("Geometric Picture")

        # Create a simple visual with axes representation
        axes_label = Text(
            "In R^3 for our 3x3 matrix A:",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(axes_label, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(axes_label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)
        self.play(FadeOut(axes_label), run_time=FAST)

        # Null space line description
        ns_title = Text(
            "Null Space",
            font_size=HEADING_SIZE, color=PRIMARY, font=MONO,
        )
        ns_vec = MathTex(
            r"\text{Nul}\, A = \text{span}\{(-2,\, 1,\, 0)\}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        ns_desc = Text(
            "A line through the origin",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        ns_dim = Text(
            "Dimension: 1",
            font_size=LABEL_SIZE, color=DIM, font=MONO,
        )

        ns_group = VGroup(ns_title, ns_vec, ns_desc, ns_dim).arrange(
            DOWN, buff=0.25, aligned_edge=LEFT,
        )
        self.ly.center_in_content(ns_group)
        self.play(Write(ns_title), run_time=FAST)
        self.play(Write(ns_vec), run_time=FAST)
        self.play(FadeIn(ns_desc, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(ns_dim, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.play(FadeOut(ns_group), run_time=FAST)

        # Column space plane description
        self.add_subcaption(
            "The column space is a plane in R^3. "
            "Every vector in this plane can be written as A x.",
            duration=7,
        )

        cs_title = Text(
            "Column Space",
            font_size=HEADING_SIZE, color=SECONDARY, font=MONO,
        )
        cs_vec = MathTex(
            r"\text{Col}\, A = \text{span}\{(1,2,1),\,(1,2,3)\}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        cs_desc = Text(
            "A plane through the origin",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        cs_dim = Text(
            "Dimension: 2",
            font_size=LABEL_SIZE, color=DIM, font=MONO,
        )

        cs_group = VGroup(cs_title, cs_vec, cs_desc, cs_dim).arrange(
            DOWN, buff=0.25, aligned_edge=LEFT,
        )
        self.ly.center_in_content(cs_group)
        self.play(Write(cs_title), run_time=FAST)
        self.play(Write(cs_vec), run_time=FAST)
        self.play(FadeIn(cs_desc, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(cs_dim, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 8: Rank-Nullity Theorem ──────────────────────────────
    def scene8_rank_nullity(self):
        self.ly.section_divider(3, "The Rank-Nullity Theorem")
        self.wait(0.3)

        self.add_subcaption(
            "The null space and column space are connected "
            "by a beautiful relationship called the rank-nullity theorem.",
            duration=7,
        )

        title = self.ly.title("Rank-Nullity Theorem")

        formula = MathTex(
            r"\dim(\text{Nul}\, A) + \dim(\text{Col}\, A) = n",
            font_size=HEADING_SIZE, color=WHITE,
        )

        self.add_subcaption(
            "The dimension of the null space plus "
            "the dimension of the column space "
            "equals the number of columns n.",
            duration=7,
        )

        note = Text(
            "n = number of columns of A",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )

        items = [formula, note]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.6)
        self.ly.center_in_content(fitted)
        self.play(Write(formula), run_time=NORMAL)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        # Show the example verification
        self.add_subcaption(
            "For our example: dimension of null space is 1, "
            "dimension of column space is 2, "
            "and 1 plus 2 equals 3, which is the number of columns.",
            duration=8,
        )

        example = VGroup(
            Text("Our example:", font_size=BODY_SIZE, color=WHITE, font=MONO),
            MathTex(
                r"\underbrace{1}_{\text{Nul}} + \underbrace{2}_{\text{Col}}"
                r" = \underbrace{3}_{n}",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            Text("Check!", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ).arrange(DOWN, buff=0.4)

        self.ly.safe_place(example, DOWN, anchor=formula, buff=0.5)
        self.play(FadeIn(example, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 9: Summary + Outro ───────────────────────────────────
    def scene9_summary(self):
        self.add_subcaption(
            "To summarize: the null space captures what gets annihilated. "
            "The column space captures what we can reach.",
            duration=7,
        )

        title = self.ly.title("Summary")

        bullet1 = Text(
            "Null space = {x : Ax = 0}, subspace of domain",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        bullet2 = Text(
            "Column space = span of columns, subspace of codomain",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        bullet3 = Text(
            "dim(Nul A) + dim(Col A) = n",
            font_size=BODY_SIZE, color=WHITE, font=MONO,
        )

        items = [bullet1, bullet2, bullet3]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "Next time we explore rank in depth. "
            "Thanks for watching!",
            duration=4,
        )
        play_outro(self, "Rank and Nullity", "Linear Algebra")
        self.ly.clear()
