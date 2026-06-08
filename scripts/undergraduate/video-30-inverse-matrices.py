"""
Video 30: Inverse Matrices
Linear Algebra Playlist — Video 6 of 16

Covers: inverse as undoing a transformation, invertibility conditions,
the 2x2 formula derivation, worked example, augmented matrix method,
key properties, and connection to systems of equations.

Render draft:  manim -ql scripts/undergraduate/video-30-inverse-matrices.py Video30_InverseMatrices
Render final:  manim -qh scripts/undergraduate/video-30-inverse-matrices.py Video30_InverseMatrices
Preview still: manim -ql --format=png -s scripts/undergraduate/video-30-inverse-matrices.py Video30_InverseMatrices
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
import numpy as np


# ── Helper: create a NumberPlane with standard styling ───────────────
PLANE_BG = "#3A3870"
PLANE_FADED = "#2A2850"


def make_plane(
    x_range=(-4, 4, 1), y_range=(-4, 4, 1),
    length=6.5, shift=ORIGIN,
):
    plane = NumberPlane(
        x_range=list(x_range), y_range=list(y_range),
        x_length=length, y_length=length,
        background_line_style={"stroke_color": PLANE_BG, "stroke_width": 1},
        axis_config={"color": DIM, "stroke_width": 2},
        faded_line_style={"stroke_color": PLANE_FADED, "stroke_width": 0.5},
    ).shift(shift)
    return plane


def make_unit_square(plane):
    """Create a filled unit square on the given plane."""
    sq = Polygon(
        plane.c2p(0, 0), plane.c2p(1, 0),
        plane.c2p(1, 1), plane.c2p(0, 1),
        fill_color=ACCENT, fill_opacity=0.25,
        stroke_color=ACCENT, stroke_width=2,
    )
    return sq


def apply_to_plane(plane, mat2x2):
    """Apply a 2x2 matrix to a plane copy, returning the transformed plane."""
    mat3x3 = np.array([
        [mat2x2[0][0], mat2x2[0][1], 0],
        [mat2x2[1][0], mat2x2[1][1], 0],
        [0, 0, 1],
    ])
    return plane.copy().apply_matrix(mat3x3)


# ═══════════════════════════════════════════════════════════════════════
class Video30_InverseMatrices(Scene):
    """Full video: inverse matrices as the transformation that undoes A."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_undoing_transformation()
        self.scene3_invertibility_conditions()
        self.scene4_two_by_two_formula()
        self.scene5_worked_example()
        self.scene6_augmented_matrix_method()
        self.scene7_properties()
        self.scene8_summary()

    # ── Scene 1: Hook + ChannelIntro ─────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "If every matrix is a transformation, "
            "can every transformation be undone? "
            "The answer is no. And understanding when you CAN undo "
            "a transformation is one of the most powerful ideas "
            "in linear algebra.",
            duration=16,
        )
        play_intro(self, "Inverse Matrices", "Linear Algebra")

        # Show the central question
        mat_tex = MathTex(
            r"A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        question = Text(
            "Can we reverse this transformation?",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )

        group = VGroup(mat_tex, question).arrange(DOWN, buff=0.6)
        self.ly.center_in_content(group)
        self.play(Write(mat_tex), run_time=NORMAL)
        self.wait(0.5)
        self.play(Write(question), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 2: The Inverse as "Undoing" ───────────────────────────
    def scene2_undoing_transformation(self):
        self.add_subcaption(
            "The inverse of a matrix A, written A inverse, "
            "is the transformation that exactly reverses A. "
            "Apply A, then apply A inverse, and you get back "
            "to where you started.",
            duration=16,
        )

        self.ly.title("The Inverse: Undoing a Transformation")

        plane = make_plane(length=5.5, shift=ORIGIN)
        sq = make_unit_square(plane)

        self.play(Create(plane), run_time=FAST)
        self.play(FadeIn(sq), run_time=FAST)
        self.wait(0.5)

        # Apply transformation A = [[2, 1], [1, 1]]  (det = 1)
        mat_a = [[2, 1], [1, 1]]
        t_plane = apply_to_plane(plane, mat_a)
        t_sq = Polygon(
            plane.c2p(0, 0), plane.c2p(2, 1),
            plane.c2p(3, 2), plane.c2p(1, 1),
            fill_color=PRIMARY, fill_opacity=0.2,
            stroke_color=PRIMARY, stroke_width=2,
        )

        self.add_subcaption(
            "Here, matrix A transforms the unit square "
            "into a parallelogram. The grid morphs. "
            "Now watch what happens when we apply A inverse.",
            duration=14,
        )

        # Show "A" label
        a_label = Text(
            "Apply A", font_size=BODY_SIZE,
            color=PRIMARY, font=SANS, weight=BOLD,
        ).to_edge(LEFT, buff=0.4).shift(UP * 2)

        self.play(
            Transform(plane, t_plane),
            Transform(sq, t_sq),
            FadeIn(a_label),
            run_time=1.5,
        )
        self.wait(1.0)

        # Apply inverse A⁻¹ = [[1, -1], [-1, 2]]  (det = 1, so 1/det = 1)
        mat_inv = [[1, -1], [-1, 2]]
        orig_plane = apply_to_plane(plane, mat_inv)
        orig_sq = make_unit_square(plane)

        self.add_subcaption(
            "A inverse reverses the transformation. "
            "The parallelogram becomes a square again. "
            "The grid returns to its original form. "
            "A inverse times A equals the identity matrix.",
            duration=16,
        )

        inv_label = Text(
            "Apply A\u207B\u00B9", font_size=BODY_SIZE,
            color=ACCENT, font=SANS, weight=BOLD,
        ).next_to(a_label, RIGHT, buff=0.3)

        self.play(
            Transform(plane, orig_plane),
            Transform(sq, orig_sq),
            FadeIn(inv_label),
            run_time=1.5,
        )
        self.wait(1.0)

        self.ly.clear()

        # Key formula
        self.add_subcaption(
            "Formally, A inverse times A equals the identity. "
            "And A times A inverse also equals the identity. "
            "This means applying A and then undoing it "
            "gets you exactly back to the start.",
            duration=16,
        )

        formula = MathTex(
            r"A^{-1} A = A A^{-1} = I",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        box = SurroundingRectangle(
            formula, color=ACCENT, buff=0.25,
            stroke_width=3, corner_radius=0.1,
        )
        group = VGroup(formula, box)
        self.ly.center_in_content(group)
        self.play(Write(formula), Create(box), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 3: When Does the Inverse Exist? ───────────────────────
    def scene3_invertibility_conditions(self):
        self.add_subcaption(
            "So when does A inverse actually exist? "
            "The answer connects directly to the determinant. "
            "If the determinant is zero, the transformation "
            "squishes space, and you cannot undo that.",
            duration=16,
        )

        self.ly.title("When Does A\u207B\u00B9 Exist?")

        # Two grids side by side
        plane_left = make_plane(length=4, shift=LEFT * 3.5)
        plane_right = make_plane(length=4, shift=RIGHT * 3.5)

        self.play(Create(plane_left), Create(plane_right), run_time=FAST)

        # Left: invertible (det != 0)
        sq_left = make_unit_square(plane_left)
        label_left = Text(
            "det \u2260 0 : Invertible",
            font_size=LABEL_SIZE,
            color=SECONDARY, font=SANS, weight=BOLD,
        ).move_to(LEFT * 3.5 + DOWN * 2.8)

        # Right: non-invertible (det = 0)
        sq_right = make_unit_square(plane_right)
        label_right = Text(
            "det = 0 : Not invertible",
            font_size=LABEL_SIZE,
            color=RED, font=SANS, weight=BOLD,
        ).move_to(RIGHT * 3.5 + DOWN * 2.8)

        self.play(
            FadeIn(sq_left), FadeIn(sq_right),
            Write(label_left), Write(label_right),
            run_time=FAST,
        )
        self.wait(0.5)

        # Left: apply invertible transformation [[2, 0], [0, 1]] (det = 2)
        self.add_subcaption(
            "On the left, the determinant is 2. "
            "The transformation stretches horizontally "
            "but keeps 2D space intact. "
            "We can reverse this by shrinking back.",
            duration=14,
        )

        t_left = apply_to_plane(plane_left, [[2, 0], [0, 1]])
        para_left = Polygon(
            plane_left.c2p(0, 0), plane_left.c2p(2, 0),
            plane_left.c2p(2, 1), plane_left.c2p(0, 1),
            fill_color=PRIMARY, fill_opacity=0.2,
            stroke_color=PRIMARY, stroke_width=2,
        )
        self.play(
            Transform(plane_left, t_left),
            Transform(sq_left, para_left),
            run_time=1.5,
        )
        self.wait(1.0)

        # Right: apply non-invertible transformation [[1, 2], [2, 4]] (det = 0)
        self.add_subcaption(
            "On the right, the determinant is zero. "
            "The entire 2D plane collapses onto a single line. "
            "Information is lost. Multiple original points "
            "all land on the same output point. "
            "There is no way to reverse this.",
            duration=16,
        )

        t_right = apply_to_plane(plane_right, [[1, 2], [2, 4]])
        collapsed = Polygon(
            plane_right.c2p(-2, -4), plane_right.c2p(2, 4),
            plane_right.c2p(2.05, 4.1), plane_right.c2p(-1.95, -3.9),
            fill_color=RED, fill_opacity=0.3,
            stroke_color=RED, stroke_width=2,
        )
        self.play(
            Transform(plane_right, t_right),
            Transform(sq_right, collapsed),
            run_time=1.5,
        )
        self.wait(1.0)

        # Key condition
        self.add_subcaption(
            "The condition is simple: "
            "A inverse exists if and only if the determinant "
            "of A is not zero. "
            "This is the most important test for invertibility.",
            duration=14,
        )

        condition = MathTex(
            r"\det(A) \neq 0 \iff A^{-1} \text{ exists}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        box = SurroundingRectangle(
            condition, color=ACCENT, buff=0.2, stroke_width=2,
        )
        VGroup(condition, box).move_to(UP * 2.5)
        self.play(Write(condition), Create(box), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 4: The 2x2 Formula Derivation ─────────────────────────
    def scene4_two_by_two_formula(self):
        self.add_subcaption(
            "For a 2 by 2 matrix, we can derive A inverse explicitly. "
            "We want A times A inverse to equal the identity matrix. "
            "Let A inverse have unknown entries.",
            duration=14,
        )

        self.ly.title("The 2\u00D72 Inverse Formula")

        # Show A and unknown A⁻¹
        mat_a = MathTex(
            r"A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        mat_inv_unk = MathTex(
            r"A^{-1} = \begin{pmatrix} w & x \\ y & z \end{pmatrix}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        eq = MathTex(r"=", font_size=HEADING_SIZE, color=DIM)

        group = VGroup(mat_a, eq, mat_inv_unk).arrange(RIGHT, buff=0.4)
        self.ly.center_in_content(group)
        self.play(Write(mat_a), run_time=NORMAL)
        self.play(Write(eq), FadeIn(mat_inv_unk), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

        # Show A · A⁻¹ = I
        self.add_subcaption(
            "Setting A times A inverse equal to the identity "
            "gives us four equations. "
            "Solving, we find that w equals d divided by the determinant, "
            "x equals negative b over the determinant, "
            "and so on.",
            duration=18,
        )

        system = MathTex(
            r"A \, A^{-1} = I",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(system)
        self.play(Write(system), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        # Show the multiplication result
        mult = MathTex(
            r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}"
            r"\begin{pmatrix} w & x \\ y & z \end{pmatrix}"
            r"= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ensure_fits(mult, max_height=2.5)
        self.ly.center_in_content(mult)
        self.play(Write(mult), run_time=SLOW)
        self.wait(1.5)

        self.ly.clear()

        # Show the solution
        self.add_subcaption(
            "The solution reveals a beautiful pattern. "
            "The diagonal entries swap places, "
            "and the off-diagonal entries change sign. "
            "Everything is divided by the determinant.",
            duration=14,
        )

        formula = MathTex(
            r"A^{-1} = \frac{1}{ad - bc}"
            r"\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        box = SurroundingRectangle(
            formula, color=ACCENT, buff=0.25,
            stroke_width=3, corner_radius=0.1,
        )
        group = VGroup(formula, box)
        self.ly.center_in_content(group)
        self.play(Write(formula), Create(box), run_time=NORMAL)
        self.wait(1.0)

        # Note about det in denominator
        note = Text(
            "det in denominator \u2192 confirms det \u2260 0 is required!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        note.next_to(box, DOWN, buff=0.4)
        self.play(Write(note), run_time=FAST)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 5: Worked Example ──────────────────────────────────────
    def scene5_worked_example(self):
        self.add_subcaption(
            "Let us find the inverse of a concrete matrix. "
            "Take A with entries 2, 1, 5, 3. "
            "First, compute the determinant: "
            "2 times 3 minus 1 times 5 equals 1. "
            "Since the determinant is nonzero, the inverse exists.",
            duration=18,
        )

        self.ly.title("Worked Example")

        # Show the matrix
        mat = MathTex(
            r"A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        self.ly.center_in_content(mat)
        self.play(Write(mat), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        # Step 1: Compute determinant
        self.add_subcaption(
            "The determinant is 2 times 3 minus 1 times 5, "
            "which equals 6 minus 5, which equals 1. "
            "A determinant of 1 means the transformation "
            "preserves area perfectly.",
            duration=16,
        )

        det = MathTex(
            r"\det(A) = (2)(3) - (1)(5) = 6 - 5 = 1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(det)
        self.play(Write(det), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

        # Step 2: Apply formula
        self.add_subcaption(
            "Now apply the formula. Swap the diagonal entries: "
            "3 and 2. Negate the off-diagonal entries: "
            "minus 1 and minus 5. "
            "Divide by the determinant, which is 1.",
            duration=16,
        )

        inv = MathTex(
            r"A^{-1} = \frac{1}{1}"
            r"\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}"
            r"= \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        ensure_fits(inv, max_height=2.5)
        self.ly.center_in_content(inv)
        self.play(Write(inv), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

        # Step 3: Verify
        self.add_subcaption(
            "Always verify your answer. "
            "Multiply A by A inverse. "
            "If we did everything correctly, "
            "we should get the identity matrix.",
            duration=14,
        )

        verify = MathTex(
            r"A A^{-1} = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}"
            r"\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}"
            r"= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        ensure_fits(verify, max_height=2.5)
        self.ly.center_in_content(verify)
        self.play(Write(verify), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 6: The Augmented Matrix Method ─────────────────────────
    def scene6_augmented_matrix_method(self):
        self.add_subcaption(
            "For larger matrices, there is a systematic method "
            "that always works, called the augmented matrix method. "
            "Write A next to the identity matrix. "
            "Apply row operations to turn A into I. "
            "The right side becomes A inverse.",
            duration=18,
        )

        self.ly.title("Augmented Matrix Method")

        # Show [A | I]
        aug = MathTex(
            r"\left[\begin{array}{cc|cc}"
            r"2 & 1 & 1 & 0 \\"
            r"5 & 3 & 0 & 1"
            r"\end{array}\right]",
            font_size=TITLE_SIZE, color=WHITE,
        )
        self.ly.center_in_content(aug)
        self.play(Write(aug), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        # Show row operations
        self.add_subcaption(
            "Row 2 minus 2 times Row 1. "
            "Then Row 1 minus Row 2. "
            "These row operations systematically "
            "transform the left side into the identity.",
            duration=14,
        )

        r1 = MathTex(
            r"R_2 \to R_2 - 2R_1",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        result1 = MathTex(
            r"\left[\begin{array}{cc|cc}"
            r"2 & 1 & 1 & 0 \\"
            r"1 & 1 & -2 & 1"
            r"\end{array}\right]",
            font_size=HEADING_SIZE, color=WHITE,
        )
        group1 = VGroup(r1, result1).arrange(DOWN, buff=0.5)
        self.ly.center_in_content(group1)
        self.play(Write(r1), run_time=FAST)
        self.play(FadeIn(result1), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        r2 = MathTex(
            r"R_1 \to R_1 - R_2",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        result2 = MathTex(
            r"\left[\begin{array}{cc|cc}"
            r"1 & 0 & 3 & -1 \\"
            r"1 & 1 & -2 & 1"
            r"\end{array}\right]",
            font_size=HEADING_SIZE, color=WHITE,
        )
        group2 = VGroup(r2, result2).arrange(DOWN, buff=0.5)
        self.ly.center_in_content(group2)
        self.play(Write(r2), run_time=FAST)
        self.play(FadeIn(result2), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        # Final result
        self.add_subcaption(
            "Finally, R2 minus R1 gives us the identity "
            "on the left, and A inverse on the right. "
            "This method works for any size matrix, "
            "including 3 by 3 and larger.",
            duration=16,
        )

        r3 = MathTex(
            r"R_2 \to R_2 - R_1",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        final = MathTex(
            r"\left[\begin{array}{cc|cc}"
            r"1 & 0 & 3 & -1 \\"
            r"0 & 1 & -5 & 2"
            r"\end{array}\right]",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        group3 = VGroup(r3, final).arrange(DOWN, buff=0.5)
        self.ly.center_in_content(group3)
        self.play(Write(r3), run_time=FAST)
        self.play(FadeIn(final), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 7: Key Properties ──────────────────────────────────────
    def scene7_properties(self):
        self.add_subcaption(
            "Inverse matrices have several elegant properties "
            "that follow naturally from the definition.",
            duration=8,
        )

        self.ly.title("Properties of Inverses")

        # Property 1: Double inverse
        self.add_subcaption(
            "The inverse of the inverse is the original matrix. "
            "If you undo an undo, you get back to the start.",
            duration=10,
        )

        prop1_title = Text(
            "Double inverse", font_size=BODY_SIZE,
            color=PRIMARY, font=SANS, weight=BOLD,
        )
        prop1_formula = MathTex(
            r"(A^{-1})^{-1} = A",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop1 = VGroup(prop1_title, prop1_formula).arrange(RIGHT, buff=0.5)

        # Property 2: Product reversal
        self.add_subcaption(
            "The inverse of a product reverses the order. "
            "A B inverse equals B inverse A inverse. "
            "Order matters because matrix multiplication "
            "is not commutative.",
            duration=14,
        )

        prop2_title = Text(
            "Product reversal", font_size=BODY_SIZE,
            color=SECONDARY, font=SANS, weight=BOLD,
        )
        prop2_formula = MathTex(
            r"(AB)^{-1} = B^{-1} A^{-1}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop2 = VGroup(prop2_title, prop2_formula).arrange(RIGHT, buff=0.5)

        # Property 3: Transpose
        self.add_subcaption(
            "The inverse of a transpose equals the transpose "
            "of the inverse. This is a subtle and beautiful "
            "property that connects two operations.",
            duration=12,
        )

        prop3_title = Text(
            "Transpose", font_size=BODY_SIZE,
            color=ACCENT, font=SANS, weight=BOLD,
        )
        prop3_formula = MathTex(
            r"(A^T)^{-1} = (A^{-1})^T",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop3 = VGroup(prop3_title, prop3_formula).arrange(RIGHT, buff=0.5)

        # Property 4: Determinant of inverse
        self.add_subcaption(
            "The determinant of the inverse is one over "
            "the determinant of A. "
            "If A doubles areas, A inverse halves them.",
            duration=12,
        )

        prop4_title = Text(
            "Determinant", font_size=BODY_SIZE,
            color=RED, font=SANS, weight=BOLD,
        )
        prop4_formula = MathTex(
            r"\det(A^{-1}) = \frac{1}{\det(A)}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop4 = VGroup(prop4_title, prop4_formula).arrange(RIGHT, buff=0.5)

        # Progressive reveal
        items = [prop1, prop2, prop3, prop4]
        self.ly.progressive_reveal(items, start_from=None)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 8: Connection to Systems + Summary + Outro ─────────────
    def scene8_summary(self):
        self.add_subcaption(
            "Why do we care about inverses? "
            "Because they solve systems of equations. "
            "If A times x equals b, "
            "then x equals A inverse times b. "
            "This is the matrix form of dividing both sides by A.",
            duration=18,
        )

        self.ly.title("Solving Systems with Inverses")

        # Show Ax = b -> x = A⁻¹b
        system = MathTex(
            r"A \vec{x} = \vec{b}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        arrow = MathTex(
            r"\Longrightarrow",
            font_size=HEADING_SIZE, color=DIM,
        )
        solution = MathTex(
            r"\vec{x} = A^{-1} \vec{b}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        group = VGroup(system, arrow, solution).arrange(RIGHT, buff=0.5)
        self.ly.center_in_content(group)
        self.play(Write(system), run_time=FAST)
        self.play(Write(arrow), FadeIn(solution), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

        # Key takeaways
        self.add_subcaption(
            "Let us recap. A inverse is the transformation "
            "that undoes A. It exists only when the determinant "
            "is nonzero. For a 2 by 2 matrix, the formula swaps "
            "the diagonal and negates the off-diagonal, "
            "divided by the determinant. "
            "And inverses solve systems of equations.",
            duration=18,
        )

        self.ly.title("Key Takeaways")

        bullets = [
            Text(
                "1. A⁻¹ undoes the transformation of A",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. det(A) ≠ 0 ⟺ A⁻¹ exists",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "3. 2×2 formula: swap diagonal, negate off-diagonal",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "4. (AB)⁻¹ = B⁻¹A⁻¹ (order reverses!)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "5. Ax = b → x = A⁻¹b",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(bullets, run_time=0.6, wait_time=0.5)

        self.wait(1.0)
        self.ly.clear()

        # Outro
        self.add_subcaption(
            "Next time, we will dive deeper into systems of equations "
            "and learn the full matrix approach to solving them. "
            "See you then!",
            duration=10,
        )

        play_outro(self, "Systems of Equations", "Linear Algebra")
