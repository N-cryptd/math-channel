"""
Video 36: Diagonalization
Linear Algebra Playlist -- Video 12 of 16

Covers: motivation for diagonalization, A = PDP^{-1} decomposition,
worked 2x2 example, computing matrix powers, when diagonalization fails.

Render draft:  manim -ql scripts/undergraduate/video-36-diagonalization.py Video36_Diagonalization
Render final:  manim -qh scripts/undergraduate/video-36-diagonalization.py Video36_Diagonalization
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


class Video36_Diagonalization(Scene):
    """Full video: diagonalization of matrices."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_why_diagonalize()
        self.scene3_decomposition()
        self.scene4_worked_example()
        self.scene5_computing_powers()
        self.scene6_when_it_fails()
        self.scene7_summary()

    # ── Scene 1: Hook + Channel Intro ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Computing the 100th power of a matrix seems impossible. "
            "But diagonalization makes it almost trivial.",
            duration=6,
        )
        play_intro(self, "Diagonalization", "Linear Algebra")

        self.add_subcaption(
            "We use eigenvectors to change coordinates "
            "and simplify the matrix.",
            duration=5,
        )

        recap = Text(
            "A = PDP^{-1}: the most useful matrix factorization",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(recap)
        self.play(FadeIn(recap, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ── Scene 2: Why Diagonalize? ──────────────────────────────────
    def scene2_why_diagonalize(self):
        self.ly.section_divider(1, "Why Diagonalize?")
        self.wait(0.3)

        self.add_subcaption(
            "A diagonal matrix is incredibly easy to work with. "
            "Powers, exponentials, and determinants "
            "are all trivial to compute.",
            duration=7,
        )

        title = self.ly.title("The Power of Diagonal Matrices")

        diag = MathTex(
            r"D = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}"
            r"\Rightarrow "
            r"D^n = \begin{bmatrix} 3^n & 0 \\ 0 & 1 \end{bmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(diag, DOWN, anchor=title, buff=0.6)
        self.play(Write(diag), run_time=NORMAL)
        self.wait(1.5)

        self.add_subcaption(
            "If we can write A as PDP inverse, "
            "then computing A to the n "
            "is just P times D to the n times P inverse.",
            duration=7,
        )

        power = MathTex(
            r"A^n = PD^nP^{-1}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(power, DOWN, anchor=diag, buff=0.5)
        self.play(Write(power), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 3: The Decomposition ─────────────────────────────────
    def scene3_decomposition(self):
        self.ly.section_divider(2, "The Decomposition")
        self.wait(0.3)

        self.add_subcaption(
            "If A has n linearly independent eigenvectors, "
            "we can write A equals PDP inverse.",
            duration=6,
        )

        title = self.ly.title("A = PDP inverse")

        formula = MathTex(
            r"A = PDP^{-1}",
            font_size=TITLE_SIZE, color=WHITE,
        )

        self.add_subcaption(
            "P is the matrix of eigenvectors. "
            "D is the diagonal matrix of eigenvalues.",
            duration=6,
        )

        desc1 = Text(
            "P = [v1 | v2 | ... | vn]  (eigenvectors as columns)",
            font_size=BODY_SIZE, color=PRIMARY, font=MONO,
        )
        desc2 = Text(
            "D = diag(lambda1, lambda2, ..., lambdan)",
            font_size=BODY_SIZE, color=SECONDARY, font=MONO,
        )

        items = [formula, desc1, desc2]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.5)
        self.ly.center_in_content(fitted)
        self.play(Write(formula), run_time=NORMAL)
        self.play(FadeIn(desc1, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(desc2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 4: Worked Example ────────────────────────────────────
    def scene4_worked_example(self):
        self.add_subcaption(
            "Recall our matrix from last time. "
            "It has eigenvalues 3 and 1, "
            "with eigenvectors (1, -1) and (1, 1).",
            duration=7,
        )

        title = self.ly.title("Worked Example")

        mat_A = MathTex(
            r"A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(mat_A, DOWN, anchor=title, buff=0.5)
        self.play(Write(mat_A), run_time=FAST)
        self.wait(1.0)
        self.play(FadeOut(mat_A), run_time=FAST)

        self.add_subcaption(
            "We build P from eigenvectors and D from eigenvalues. "
            "Then we verify that A equals PDP inverse.",
            duration=7,
        )

        step_P = MathTex(
            r"P = \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        step_D = MathTex(
            r"D = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )

        steps = VGroup(step_P, step_D).arrange(DOWN, buff=0.4)
        self.ly.center_in_content(steps)
        self.play(Write(step_P), run_time=NORMAL)
        self.play(Write(step_D), run_time=NORMAL)
        self.wait(1.5)

        verify = MathTex(
            r"PDP^{-1} = "
            r"\begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}"
            r"\begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}"
            r"\frac{1}{2}\begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}"
            r"= \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(verify, DOWN, anchor=step_D, buff=0.5)
        ensure_fits(verify, max_width=6.5)
        self.play(Write(verify), run_time=2.0)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 5: Computing Powers ──────────────────────────────────
    def scene5_computing_powers(self):
        self.add_subcaption(
            "Now computing A to the 10th power is easy. "
            "We just need D to the 10th.",
            duration=5,
        )

        title = self.ly.title("Computing A^n")

        D10 = MathTex(
            r"D^{10} = \begin{bmatrix} 3^{10} & 0 \\ 0 & 1 \end{bmatrix}"
            r"= \begin{bmatrix} 59049 & 0 \\ 0 & 1 \end{bmatrix}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(D10, DOWN, anchor=title, buff=0.5)
        self.play(Write(D10), run_time=NORMAL)
        self.wait(1.0)

        self.add_subcaption(
            "Then A to the 10 equals P times D to the 10 "
            "times P inverse.",
            duration=5,
        )

        result = MathTex(
            r"A^{10} = PD^{10}P^{-1} "
            r"= \frac{1}{2}\begin{bmatrix} 59050 & 59048 \\ 59048 & 59050 \end{bmatrix}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(result, DOWN, anchor=D10, buff=0.5)
        ensure_fits(result, max_width=6.5)
        self.play(Write(result), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 6: When Does It Fail? ────────────────────────────────
    def scene6_when_it_fails(self):
        self.ly.section_divider(3, "When Diagonalization Fails")
        self.wait(0.3)

        self.add_subcaption(
            "A matrix is diagonalizable "
            "if and only if it has n linearly independent eigenvectors.",
            duration=6,
        )

        title = self.ly.title("Not Every Matrix Diagonalizes")

        rule = Text(
            "Need n independent eigenvectors",
            font_size=BODY_SIZE, color=WHITE, font=MONO,
        )
        self.ly.safe_place(rule, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(rule, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.0)
        self.play(FadeOut(rule), run_time=FAST)

        self.add_subcaption(
            "Consider this matrix. "
            "It has eigenvalue 1 with multiplicity 2, "
            "but only one independent eigenvector.",
            duration=7,
        )

        bad_mat = MathTex(
            r"\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}"
            r"\quad \lambda = 1 \text{ (double)}, \quad"
            r"\text{only } \begin{pmatrix} 1 \\ 0 \end{pmatrix}",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(bad_mat, DOWN, anchor=title, buff=0.5)
        ensure_fits(bad_mat, max_width=6.5)
        self.play(Write(bad_mat), run_time=NORMAL)

        label = Text(
            "Not enough eigenvectors = not diagonalizable",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(label, DOWN, anchor=bad_mat, buff=0.4)
        self.play(FadeIn(label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Summary + Outro ───────────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "To summarize: A equals PDP inverse if A has "
            "enough independent eigenvectors. "
            "This makes powers and exponentials trivial.",
            duration=7,
        )

        title = self.ly.title("Summary")

        bullet1 = Text(
            "A = PDP^{-1} decomposes A using eigenvectors",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        bullet2 = Text(
            "A^n = PD^nP^{-1}: powers become easy",
            font_size=BODY_SIZE, color=SECONDARY, font=MONO,
        )
        bullet3 = Text(
            "Fails when eigenvectors are insufficient",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )

        items = [bullet1, bullet2, bullet3]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "Next time we explore inner product spaces. "
            "Thanks for watching!",
            duration=4,
        )
        play_outro(self, "Inner Product Spaces", "Linear Algebra")
        self.ly.clear()
