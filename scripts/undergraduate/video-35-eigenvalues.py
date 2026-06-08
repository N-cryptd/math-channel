"""
Video 35: Eigenvalues and Eigenvectors
Linear Algebra Playlist — Video 11 of 16

Covers: geometric intuition, formal definition, characteristic polynomial,
worked 2x2 example, finding eigenvectors, geometric interpretation,
and key properties (trace, determinant).

Render draft:  manim -ql scripts/undergraduate/video-35-eigenvalues.py Video35_Eigenvalues
Render final:  manim -qh scripts/undergraduate/video-35-eigenvalues.py Video35_Eigenvalues
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


class Video35_Eigenvalues(Scene):
    """Full video: eigenvalues and eigenvectors."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_geometric_idea()
        self.scene3_formal_definition()
        self.scene4_characteristic_polynomial()
        self.scene5_worked_example()
        self.scene6_finding_eigenvectors()
        self.scene7_geometric_interpretation()
        self.scene8_key_properties()
        self.scene9_summary()

    # ── Scene 1: Hook + Channel Intro ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Some transformations stretch space along certain directions "
            "while leaving those directions unchanged.",
            duration=6,
        )
        play_intro(self, "Eigenvalues & Eigenvectors", "Linear Algebra")

        self.add_subcaption(
            "Today we find those special directions "
            "and measure how much they stretch.",
            duration=5,
        )

        recap = Text(
            "Every matrix has hidden natural axes",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(recap)
        self.play(FadeIn(recap, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ── Scene 2: The Geometric Idea ────────────────────────────────
    def scene2_geometric_idea(self):
        self.ly.section_divider(1, "The Core Idea")
        self.wait(0.3)

        self.add_subcaption(
            "Imagine applying a transformation to a vector. "
            "Most vectors change direction.",
            duration=5,
        )

        title = self.ly.title("Which Vectors Stay on Course?")

        normal = Text(
            "Most vectors: direction changes after A",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(normal, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(normal, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.0)
        self.play(FadeOut(normal), run_time=FAST)

        self.add_subcaption(
            "But some special vectors only get scaled. "
            "They stay on the same line. "
            "These are eigenvectors.",
            duration=6,
        )

        formula = MathTex(
            r"A\mathbf{v} = \lambda \mathbf{v}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        desc = Text(
            "Same direction, just scaled by lambda",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        items = [formula, desc]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.6)
        self.ly.center_in_content(fitted)
        self.play(Write(formula), run_time=NORMAL)
        self.play(FadeIn(desc, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 3: Formal Definition ─────────────────────────────────
    def scene3_formal_definition(self):
        self.ly.section_divider(2, "Formal Definition")
        self.wait(0.3)

        self.add_subcaption(
            "Formally: a nonzero vector v is an eigenvector of A "
            "if A v equals lambda v for some scalar lambda.",
            duration=6,
        )

        title = self.ly.title("Definition")

        defn = MathTex(
            r"A\mathbf{v} = \lambda \mathbf{v}, \quad \mathbf{v} \neq \mathbf{0}",
            font_size=HEADING_SIZE, color=WHITE,
        )

        self.add_subcaption(
            "Lambda is the eigenvalue, the scaling factor. "
            "V is the eigenvector, the invariant direction.",
            duration=6,
        )

        note1 = Text(
            "lambda = eigenvalue (scaling factor)",
            font_size=BODY_SIZE, color=ACCENT, font=MONO,
        )
        note2 = Text(
            "v = eigenvector (invariant direction)",
            font_size=BODY_SIZE, color=PRIMARY, font=MONO,
        )

        items = [defn, note1, note2]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.5)
        self.ly.center_in_content(fitted)
        self.play(Write(defn), run_time=NORMAL)
        self.play(FadeIn(note1, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(note2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 4: Characteristic Polynomial ─────────────────────────
    def scene4_characteristic_polynomial(self):
        self.ly.section_divider(3, "Finding Eigenvalues")
        self.wait(0.3)

        self.add_subcaption(
            "How do we find eigenvalues? "
            "We rearrange the equation.",
            duration=4,
        )

        title = self.ly.title("The Characteristic Equation")

        step1 = MathTex(
            r"A\mathbf{v} = \lambda \mathbf{v}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1, DOWN, anchor=title, buff=0.5)
        self.play(Write(step1), run_time=FAST)
        self.wait(0.5)

        self.add_subcaption(
            "Factor out v: A minus lambda I times v equals zero. "
            "For a nonzero solution, the matrix must be singular.",
            duration=7,
        )

        step2 = MathTex(
            r"(A - \lambda I)\mathbf{v} = \mathbf{0}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(step2, DOWN, anchor=step1, buff=0.4)
        self.play(Transform(step1.copy(), step2), run_time=NORMAL)
        self.wait(0.5)

        step3 = MathTex(
            r"\det(A - \lambda I) = 0",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(step3, DOWN, anchor=step2, buff=0.4)
        self.play(Write(step3), run_time=NORMAL)

        label = Text(
            "This is the characteristic equation",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(label, DOWN, anchor=step3, buff=0.4)
        self.play(FadeIn(label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 5: Worked Example ────────────────────────────────────
    def scene5_worked_example(self):
        self.add_subcaption(
            "Let us find the eigenvalues of a 2 by 2 matrix.",
            duration=4,
        )

        title = self.ly.title("Worked Example")

        mat_A = MathTex(
            r"A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(mat_A, DOWN, anchor=title, buff=0.5)
        self.play(Write(mat_A), run_time=NORMAL)
        self.wait(1.0)

        self.add_subcaption(
            "Compute A minus lambda I and set its determinant to zero. "
            "This gives a quadratic in lambda.",
            duration=6,
        )

        step1 = MathTex(
            r"A - \lambda I = \begin{bmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{bmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        step2 = MathTex(
            r"\det = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3",
            font_size=HEADING_SIZE, color=WHITE,
        )
        step3 = MathTex(
            r"= (\lambda - 3)(\lambda - 1) = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )

        result = MathTex(
            r"\lambda_1 = 3, \quad \lambda_2 = 1",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        self.play(FadeOut(mat_A), run_time=FAST)

        steps = VGroup(step1, step2, step3, result).arrange(
            DOWN, buff=0.35, aligned_edge=LEFT,
        )
        ensure_fits(steps, max_height=5.0)
        self.ly.center_in_content(steps)

        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.5)
        self.play(Write(step3), run_time=FAST)
        self.wait(0.5)

        self.add_subcaption(
            "So our eigenvalues are lambda 1 equals 3 "
            "and lambda 2 equals 1.",
            duration=5,
        )

        self.play(Write(result), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 6: Finding Eigenvectors ──────────────────────────────
    def scene6_finding_eigenvectors(self):
        self.add_subcaption(
            "For each eigenvalue, we find eigenvectors "
            "by solving (A minus lambda I) v equals zero.",
            duration=6,
        )

        title = self.ly.title("Finding Eigenvectors")

        # Eigenvalue 1
        ev1_label = Text(
            "For lambda_1 = 3:",
            font_size=BODY_SIZE, color=PRIMARY, font=MONO,
        )
        ev1_calc = MathTex(
            r"(A - 3I)\mathbf{v} = \mathbf{0}"
            r" \Rightarrow "
            r"\begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}"
            r"\mathbf{v} = \mathbf{0}",
            font_size=BODY_SIZE, color=WHITE,
        )
        ev1_result = MathTex(
            r"\mathbf{v}_1 = t\begin{pmatrix} 1 \\ -1 \end{pmatrix}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )

        item1 = VGroup(ev1_label, ev1_calc, ev1_result).arrange(
            DOWN, buff=0.3, aligned_edge=LEFT,
        )
        self.ly.safe_place(item1, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(ev1_label, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(ev1_calc), run_time=NORMAL)
        self.play(Write(ev1_result), run_time=FAST)
        self.wait(1.5)

        # Clear and show eigenvalue 2
        self.play(FadeOut(item1), run_time=FAST)

        self.add_subcaption(
            "For lambda 1, eigenvectors are multiples of (1, -1). "
            "For lambda 2, eigenvectors are multiples of (1, 1).",
            duration=7,
        )

        ev2_label = Text(
            "For lambda_2 = 1:",
            font_size=BODY_SIZE, color=SECONDARY, font=MONO,
        )
        ev2_calc = MathTex(
            r"(A - I)\mathbf{v} = \mathbf{0}"
            r" \Rightarrow "
            r"\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}"
            r"\mathbf{v} = \mathbf{0}",
            font_size=BODY_SIZE, color=WHITE,
        )
        ev2_result = MathTex(
            r"\mathbf{v}_2 = t\begin{pmatrix} 1 \\ 1 \end{pmatrix}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )

        item2 = VGroup(ev2_label, ev2_calc, ev2_result).arrange(
            DOWN, buff=0.3, aligned_edge=LEFT,
        )
        self.ly.safe_place(item2, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(ev2_label, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(ev2_calc), run_time=NORMAL)
        self.play(Write(ev2_result), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Geometric Interpretation ──────────────────────────
    def scene7_geometric_interpretation(self):
        self.add_subcaption(
            "Geometrically, our transformation stretches by 3 "
            "along direction (1, -1) and leaves "
            "direction (1, 1) unchanged.",
            duration=7,
        )

        title = self.ly.title("Geometric Meaning")

        dir1 = Text(
            "Direction (1, -1): stretches by factor 3",
            font_size=BODY_SIZE, color=PRIMARY, font=MONO,
        )
        dir2 = Text(
            "Direction (1, 1): stays the same (factor 1)",
            font_size=BODY_SIZE, color=SECONDARY, font=MONO,
        )
        insight = Text(
            "Eigenvectors = natural axes of the transformation",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        items = [dir1, dir2, insight]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 8: Key Properties ────────────────────────────────────
    def scene8_key_properties(self):
        self.ly.section_divider(4, "Key Properties")
        self.wait(0.3)

        self.add_subcaption(
            "Some important facts about eigenvalues. "
            "Their sum equals the trace. "
            "Their product equals the determinant.",
            duration=7,
        )

        title = self.ly.title("Eigenvalue Properties")

        prop1 = MathTex(
            r"\lambda_1 + \lambda_2 + \cdots + \lambda_n = \text{tr}(A)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop2 = MathTex(
            r"\lambda_1 \cdot \lambda_2 \cdots \lambda_n = \det(A)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop3 = Text(
            "An n x n matrix has at most n eigenvalues",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )

        items = [prop1, prop2, prop3]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)

        # Verify with our example
        self.add_subcaption(
            "For our example: 3 plus 1 equals 4, "
            "which is the trace. And 3 times 1 equals 3, "
            "which is the determinant.",
            duration=7,
        )

        check = MathTex(
            r"3 + 1 = 4 = \text{tr}(A), \quad 3 \times 1 = 3 = \det(A) \quad \checkmark",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(check, DOWN, anchor=prop3, buff=0.4)
        self.play(Write(check), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 9: Summary + Outro ───────────────────────────────────
    def scene9_summary(self):
        self.add_subcaption(
            "To summarize: eigenvectors are invariant directions, "
            "eigenvalues measure scaling, "
            "and we find them via the characteristic polynomial.",
            duration=7,
        )

        title = self.ly.title("Summary")

        bullet1 = Text(
            "Av = lambda v: eigenvectors stay on their line",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        bullet2 = Text(
            "det(A - lambda I) = 0 gives eigenvalues",
            font_size=BODY_SIZE, color=ACCENT, font=MONO,
        )
        bullet3 = Text(
            "Sum = trace, Product = determinant",
            font_size=BODY_SIZE, color=WHITE, font=MONO,
        )

        items = [bullet1, bullet2, bullet3]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "Next time we use eigenvectors to diagonalize matrices. "
            "Thanks for watching!",
            duration=4,
        )
        play_outro(self, "Diagonalization", "Linear Algebra")
        self.ly.clear()
