"""
Video 40: Singular Value Decomposition
Linear Algebra Playlist -- Video 16 of 16 (FINALE)

Covers: motivation for SVD, geometric intuition, the U-Sigma-V-T decomposition,
computing SVD via eigenvalues of A^T A, and low-rank approximation.

Render draft:  manim -ql scripts/undergraduate/video-40-svd.py Video40_SVD
Render final:  manim -qh scripts/undergraduate/video-40-svd.py Video40_SVD
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


class Video40_SVD(Scene):
    """Full video: Singular Value Decomposition."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_motivation()
        self.scene3_geometric_picture()
        self.scene4_formula()
        self.scene5_computing()
        self.scene6_connections()
        self.scene7_low_rank()
        self.scene8_summary()

    # ── Scene 1: Hook + Channel Intro ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Diagonalization only works for nice matrices. "
            "The Singular Value Decomposition works for every matrix, "
            "square or rectangular, symmetric or not. "
            "It is the crown jewel of linear algebra.",
            duration=8,
        )
        play_intro(self, "Singular Value Decomposition", "Linear Algebra")

        recap = Text(
            "The decomposition that works for EVERY matrix",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(recap)
        self.play(FadeIn(recap, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ── Scene 2: Why Do We Need SVD? ───────────────────────────────
    def scene2_motivation(self):
        self.ly.section_divider(1, "Why SVD?")
        self.wait(0.3)

        self.add_subcaption(
            "Diagonalization needs n independent eigenvectors. "
            "Not all matrices have them. "
            "And non-square matrices cannot be diagonalized at all.",
            duration=7,
        )

        title = self.ly.title("The Problem with Diagonalization")

        prob1 = Text(
            "Not all matrices are diagonalizable",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        prob2 = Text(
            "Non-square matrices have no eigenvalues",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )

        self.add_subcaption(
            "The Singular Value Decomposition solves all of these problems. "
            "It works for any matrix of any size.",
            duration=6,
        )

        solution = Text(
            "SVD works for ANY m by n matrix",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        items = [prob1, prob2, solution]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 3: The Geometric Picture ─────────────────────────────
    def scene3_geometric_picture(self):
        self.ly.section_divider(2, "The Geometric Picture")
        self.wait(0.3)

        self.add_subcaption(
            "Any linear transformation can be broken into three steps: "
            "rotate in the domain, scale along axes, then rotate in the output space.",
            duration=7,
        )

        title = self.ly.title("Rotation, Scaling, Rotation")

        step1 = Text(
            "1. V-transpose: rotate the input space",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        step2 = Text(
            "2. Sigma: scale along orthogonal axes",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        step3 = Text(
            "3. U: rotate the output space",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        self.add_subcaption(
            "Under any matrix, a unit circle becomes an ellipse. "
            "The ellipse axes are the singular vectors, "
            "and their lengths are the singular values.",
            duration=7,
        )

        insight = Text(
            "Unit circle becomes an ellipse under any matrix",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )

        items = [step1, step2, step3, insight]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 4: The SVD Formula ───────────────────────────────────
    def scene4_formula(self):
        self.ly.section_divider(3, "The SVD Formula")
        self.wait(0.3)

        self.add_subcaption(
            "The Singular Value Decomposition writes any matrix A "
            "as U times Sigma times V transpose.",
            duration=5,
        )

        title = self.ly.title("A = U Sigma V Transpose")

        svd_eq = MathTex(
            r"A = U \Sigma V^T",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        self.add_subcaption(
            "U is an m by m orthogonal matrix of left singular vectors. "
            "Sigma is an m by n diagonal matrix of singular values. "
            "V transpose is an n by n orthogonal matrix of right singular vectors.",
            duration=8,
        )

        u_desc = MathTex(
            r"U \in \mathbb{R}^{m \times m}",
            r"\text{ (left singular vectors)}",
            font_size=BODY_SIZE,
        )
        u_desc[0].set_color(PRIMARY)
        u_desc[1].set_color(DIM)

        sigma_desc = MathTex(
            r"\Sigma \in \mathbb{R}^{m \times n}",
            r"\text{ (singular values)}",
            font_size=BODY_SIZE,
        )
        sigma_desc[0].set_color(ACCENT)
        sigma_desc[1].set_color(DIM)

        vt_desc = MathTex(
            r"V^T \in \mathbb{R}^{n \times n}",
            r"\text{ (right singular vectors)}",
            font_size=BODY_SIZE,
        )
        vt_desc[0].set_color(SECONDARY)
        vt_desc[1].set_color(DIM)

        items = [svd_eq, u_desc, sigma_desc, vt_desc]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 5: Computing the SVD ─────────────────────────────────
    def scene5_computing(self):
        self.ly.section_divider(4, "Computing the SVD")
        self.wait(0.3)

        self.add_subcaption(
            "To find the SVD, we use a clever trick. "
            "Compute A transpose A, which is always symmetric "
            "and positive semi-definite.",
            duration=7,
        )

        title = self.ly.title("Step-by-Step Algorithm")

        step1 = MathTex(
            r"\text{1. Form } A^T A",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        self.add_subcaption(
            "Find the eigenvalues and eigenvectors of A transpose A. "
            "The square roots of the eigenvalues are the singular values.",
            duration=7,
        )

        step2 = MathTex(
            r"\text{2. Eigenvectors } \mathbf{v}_i \text{ of } A^TA",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        step3 = MathTex(
            r"\text{3. } \sigma_i = \sqrt{\lambda_i(A^TA)}",
            font_size=BODY_SIZE, color=ACCENT,
        )

        self.add_subcaption(
            "Finally, compute the left singular vectors "
            "by applying A to each right singular vector "
            "and normalizing by the singular value.",
            duration=7,
        )

        step4 = MathTex(
            r"\text{4. } \mathbf{u}_i = \frac{A\mathbf{v}_i}{\sigma_i}",
            font_size=BODY_SIZE, color=SECONDARY,
        )

        items = [step1, step2, step3, step4]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 6: Connections to Other Concepts ─────────────────────
    def scene6_connections(self):
        self.ly.section_divider(5, "Deep Connections")
        self.wait(0.3)

        self.add_subcaption(
            "The SVD ties together everything we have learned. "
            "Singular values are square roots of eigenvalues of A transpose A.",
            duration=6,
        )

        title = self.ly.title("SVD and Eigenvalues")

        conn1 = Text(
            "Singular values = sqrt of eigenvalues of A^T A",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )

        self.add_subcaption(
            "For symmetric matrices, the SVD reduces to "
            "the eigenvalue decomposition. The rank of A "
            "equals the number of nonzero singular values.",
            duration=7,
        )

        conn2 = Text(
            "Symmetric A: SVD = eigenvalue decomposition",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        conn3 = Text(
            "Rank(A) = number of nonzero singular values",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        items = [conn1, conn2, conn3]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Low-Rank Approximation ────────────────────────────
    def scene7_low_rank(self):
        self.ly.section_divider(6, "Low-Rank Approximation")
        self.wait(0.3)

        self.add_subcaption(
            "One of the most powerful applications of SVD "
            "is data compression. By keeping only the top k "
            "singular values, we get the best rank-k approximation.",
            duration=7,
        )

        title = self.ly.title("The Best Rank-k Approximation")

        approx = MathTex(
            r"A \approx \sum_{i=1}^{k} \sigma_i \, \mathbf{u}_i \mathbf{v}_i^T",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        self.add_subcaption(
            "This is guaranteed to be the best possible approximation "
            "by the Eckart-Young theorem. "
            "Applications include image compression, "
            "noise reduction, and recommendation systems.",
            duration=7,
        )

        eckart = Text(
            "Eckart-Young: best rank-k approximation",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        apps = Text(
            "Apps: image compression, noise filtering, recommenders",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )

        items = [approx, eckart, apps]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 8: Summary + Outro ───────────────────────────────────
    def scene8_summary(self):
        self.add_subcaption(
            "The Singular Value Decomposition is the ultimate "
            "matrix factorization. It works for any matrix, "
            "reveals hidden structure, and powers countless applications.",
            duration=7,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text("SVD works for ANY matrix: A = U Sigma V^T", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Geometrically: rotate, scale, rotate", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Singular values = sqrt(eigenvalues of A^T A)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Low-rank approximation via top-k singular values", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("This completes our Linear Algebra playlist!", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]

        self.ly.progressive_reveal(takeaways, start_from=title)
        self.wait(2.0)
        self.ly.clear()

        self.add_subcaption(
            "Congratulations on completing the Linear Algebra playlist! "
            "From vectors to SVD, you now have the tools "
            "to understand the mathematics behind data science, "
            "machine learning, physics, and engineering. "
            "Thank you for watching!",
            duration=10,
        )

        play_outro(self, "Calculus III: Multivariable", "Math Channel")


# ── Compile check ──────────────────────────────────────────────────
if __name__ == "__main__":
    import py_compile
    py_compile.compile(__file__, doraise=True)
    print(f"Compile OK: {__file__}")
