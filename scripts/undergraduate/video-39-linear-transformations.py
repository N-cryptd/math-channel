"""
Video 39: Linear Transformations (Abstract)
Linear Algebra Playlist -- Video 15 of 16

Covers: linear transformations as structure-preserving functions, formal axioms,
matrix connection, kernel, image, and the dimension theorem.

Render draft:  manim -ql scripts/undergraduate/video-39-linear-transformations.py Video39_LinearTransformations
Render final:  manim -qh scripts/undergraduate/video-39-linear-transformations.py Video39_LinearTransformations
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


class Video39_LinearTransformations(Scene):
    """Full video: abstract linear transformations, kernel, image."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_functions()
        self.scene3_visual_intuition()
        self.scene4_formal_definition()
        self.scene5_matrix_connection()
        self.scene6_kernel_and_image()
        self.scene7_examples()
        self.scene8_summary()

    # ── Scene 1: Hook + Channel Intro ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "We have used matrices to transform vectors. "
            "But what exactly IS a linear transformation? "
            "Let us find out.",
            duration=7,
        )
        play_intro(self, "Linear Transformations", "Linear Algebra")

        recap = Text(
            "From matrices to the abstract idea of transformations",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(recap)
        self.play(FadeIn(recap, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ── Scene 2: What is a Function? ───────────────────────────────
    def scene2_functions(self):
        self.ly.section_divider(1, "Functions Between Spaces")
        self.wait(0.3)

        self.add_subcaption(
            "A function takes inputs from one set and produces outputs in another. "
            "We write T maps V to W.",
            duration=5,
        )

        title = self.ly.title("Functions Between Vector Spaces")

        func_text = MathTex(
            r"T \colon V \to W",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        self.add_subcaption(
            "But not all functions are special. "
            "Linear transformations preserve the vector space structure.",
            duration=5,
        )

        note = Text(
            "Some functions preserve the structure of vector spaces",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )

        items = [func_text, note]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.6)
        self.ly.center_in_content(fitted)
        self.play(Write(func_text), run_time=NORMAL)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 3: The Visual Intuition ──────────────────────────────
    def scene3_visual_intuition(self):
        self.ly.section_divider(2, "Visual Intuition")
        self.wait(0.3)

        self.add_subcaption(
            "A linear transformation keeps grid lines as straight lines, "
            "and the origin stays fixed.",
            duration=5,
        )

        title = self.ly.title("What Does Linear Mean Visually?")

        rule1 = Text(
            "1. Lines map to lines",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        rule2 = Text(
            "2. The origin stays at the origin",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        self.add_subcaption(
            "Translations shift the origin, so they are NOT linear. "
            "Curves get bent, so they are NOT linear either.",
            duration=6,
        )

        not1 = Text(
            "Translations are NOT linear (origin moves)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        not2 = Text(
            "Non-linear curves are NOT linear (lines bend)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )

        items = [rule1, rule2, not1, not2]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 4: Formal Definition ─────────────────────────────────
    def scene4_formal_definition(self):
        self.ly.section_divider(3, "Formal Definition")
        self.wait(0.3)

        self.add_subcaption(
            "A transformation T from V to W is linear if it satisfies "
            "two rules: additivity and homogeneity.",
            duration=6,
        )

        title = self.ly.title("The Axioms of Linearity")

        axiom1 = MathTex(
            r"T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        label1 = Text(
            "Additivity (preserves addition)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )

        self.add_subcaption(
            "Additivity: the transformation of a sum equals "
            "the sum of the transformed vectors.",
            duration=5,
        )

        group1 = VGroup(axiom1, label1).arrange(DOWN, buff=0.15)

        self.add_subcaption(
            "Homogeneity: scaling a vector first then transforming "
            "gives the same result as transforming first then scaling.",
            duration=6,
        )

        axiom2 = MathTex(
            r"T(c\mathbf{u}) = c \, T(\mathbf{u})",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        label2 = Text(
            "Homogeneity (preserves scalar multiplication)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )

        group2 = VGroup(axiom2, label2).arrange(DOWN, buff=0.15)

        self.add_subcaption(
            "Combining both rules, a linear transformation "
            "preserves all linear combinations.",
            duration=5,
        )

        combined = MathTex(
            r"T(c\mathbf{u} + d\mathbf{v}) = c\,T(\mathbf{u}) + d\,T(\mathbf{v})",
            font_size=BODY_SIZE, color=ACCENT,
        )

        items = [group1, group2, combined]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 5: Matrix Connection ─────────────────────────────────
    def scene5_matrix_connection(self):
        self.ly.section_divider(4, "Matrix Connection")
        self.wait(0.3)

        self.add_subcaption(
            "Every matrix defines a linear transformation via "
            "matrix-vector multiplication.",
            duration=5,
        )

        title = self.ly.title("Every Matrix is a Linear Transformation")

        mat_eq = MathTex(
            r"T(\mathbf{x}) = A\mathbf{x}",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        self.add_subcaption(
            "The columns of A tell you where the standard basis "
            "vectors land under the transformation.",
            duration=6,
        )

        col_eq = MathTex(
            r"A = \begin{bmatrix} T(\mathbf{e}_1) & T(\mathbf{e}_2) & \cdots & T(\mathbf{e}_n) \end{bmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )

        note = Text(
            "Columns of A = images of the basis vectors",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        items = [mat_eq, col_eq, note]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 6: Kernel and Image ──────────────────────────────────
    def scene6_kernel_and_image(self):
        self.ly.section_divider(5, "Kernel and Image")
        self.wait(0.3)

        self.add_subcaption(
            "The kernel is everything that gets sent to zero. "
            "It is the same as the null space we studied earlier.",
            duration=6,
        )

        title = self.ly.title("Kernel (Null Space)")

        kernel_def = MathTex(
            r"\ker(T) = \{\mathbf{v} \in V : T(\mathbf{v}) = \mathbf{0}\}",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        kernel_note = Text(
            "Same as Null(A)! All vectors mapped to zero.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        items1 = [kernel_def, kernel_note]
        self.ly.progressive_reveal(items1, start_from=title)
        self.wait(1.5)

        self.ly.clear()

        self.add_subcaption(
            "The image is the set of all possible outputs. "
            "It is the same as the column space.",
            duration=6,
        )

        title2 = self.ly.title("Image (Column Space)")

        image_def = MathTex(
            r"\text{im}(T) = \{T(\mathbf{v}) : \mathbf{v} \in V\}",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        image_note = Text(
            "Same as Col(A)! All possible outputs.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        items2 = [image_def, image_note]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(1.5)
        self.ly.clear()

        self.add_subcaption(
            "The dimension theorem connects the kernel and image. "
            "Their dimensions always add up to the dimension of the domain.",
            duration=7,
        )

        title3 = self.ly.title("Dimension Theorem")

        dim_formula = MathTex(
            r"\dim(\ker T) + \dim(\text{im}\, T) = \dim V",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        rank_note = Text(
            "This is the Rank-Nullity Theorem!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        fitted, _ = self.ly.stack_down([dim_formula, rank_note], start_from=title3, spacing=0.6)
        self.ly.center_in_content(fitted)
        self.play(Write(dim_formula), run_time=NORMAL)
        self.play(FadeIn(rank_note, shift=LEFT * 0.15), run_time=FAST)
        self.play(Indicate(dim_formula), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Examples ──────────────────────────────────────────
    def scene7_examples(self):
        self.ly.section_divider(6, "Examples")
        self.wait(0.3)

        # Example 1: Projection
        self.add_subcaption(
            "Example one: projection onto the x-axis. "
            "The kernel is the y-axis, the image is the x-axis.",
            duration=7,
        )

        title = self.ly.title("Example: Projection onto x-axis")

        proj_mat = MathTex(
            r"P = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )

        ker1 = Text(
            "ker(P) = y-axis (vectors of the form (0, y))",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        im1 = Text(
            "im(P) = x-axis (vectors of the form (x, 0))",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        items1 = [proj_mat, ker1, im1]
        self.ly.progressive_reveal(items1, start_from=title)
        self.wait(2.0)
        self.ly.clear()

        # Example 2: Rotation
        self.add_subcaption(
            "Example two: rotation by ninety degrees. "
            "The kernel is just the zero vector, "
            "and the image is all of R squared.",
            duration=7,
        )

        title2 = self.ly.title("Example: Rotation by 90 degrees")

        rot_mat = MathTex(
            r"R = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )

        ker2 = Text(
            "ker(R) = {(0, 0)} only",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        im2 = Text(
            "im(R) = all of R squared (rotation is onto)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        items2 = [rot_mat, ker2, im2]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(2.0)
        self.ly.clear()

        # Example 3: Zero transformation
        self.add_subcaption(
            "Example three: the zero transformation sends everything to zero. "
            "The kernel is the entire space, and the image is just the origin.",
            duration=7,
        )

        title3 = self.ly.title("Example: Zero Transformation")

        zero_mat = MathTex(
            r"T(\mathbf{x}) = \mathbf{0}",
            font_size=HEADING_SIZE, color=WHITE,
        )

        ker3 = Text(
            "ker(T) = all of R squared",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        im3 = Text(
            "im(T) = {(0, 0)} only",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        items3 = [zero_mat, ker3, im3]
        self.ly.progressive_reveal(items3, start_from=title3)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 8: Summary + Outro ───────────────────────────────────
    def scene8_summary(self):
        self.add_subcaption(
            "To summarize: a linear transformation preserves addition "
            "and scalar multiplication. Every matrix gives one, "
            "and the kernel and image reveal its structure.",
            duration=7,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text("T preserves addition and scalar multiplication", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Every matrix defines a linear transformation", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Columns of A = where basis vectors land", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Kernel = Null(A), Image = Col(A)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("dim(ker T) + dim(im T) = dim V", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]

        self.ly.progressive_reveal(takeaways, start_from=title)
        self.wait(2.0)
        self.ly.clear()

        self.add_subcaption(
            "Next time, we explore the Singular Value Decomposition, "
            "which reveals the hidden geometry of any transformation. "
            "Thanks for watching!",
            duration=6,
        )

        play_outro(self, "Singular Value Decomposition", "Linear Algebra")


# ── Compile check ──────────────────────────────────────────────────
if __name__ == "__main__":
    import py_compile
    py_compile.compile(__file__, doraise=True)
    print(f"Compile OK: {__file__}")
