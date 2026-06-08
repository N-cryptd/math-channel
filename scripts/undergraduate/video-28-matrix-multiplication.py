"""
Video 28: Matrix Multiplication
Linear Algebra Playlist — Video 4 of 16

Covers: composition of transformations, deriving the matrix multiplication
formula from geometric intuition, the standard row-column algorithm, worked
example, non-commutativity, and key properties.

Render draft:  manim -ql scripts/undergraduate/video-28-matrix-multiplication.py Video28_MatrixMultiplication
Render final:  manim -qh scripts/undergraduate/video-28-matrix-multiplication.py Video28_MatrixMultiplication
Preview still: manim -ql --format=png -s scripts/undergraduate/video-28-matrix-multiplication.py Video28_MatrixMultiplication
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
from layout import LayoutEngine, ensure_fits, clamp_position
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


def make_basis_arrows(plane):
    """Return i-hat arrow, i-hat label, j-hat arrow, j-hat label."""
    i_hat = Arrow(
        plane.c2p(0, 0), plane.c2p(1, 0),
        buff=0, stroke_width=5, color=PRIMARY,
        max_tip_length_to_length_ratio=0.2,
    )
    i_label = MathTex(r"\hat{\imath}", font_size=LABEL_SIZE, color=PRIMARY)
    i_label.next_to(i_hat.get_end(), DOWN, buff=0.15)

    j_hat = Arrow(
        plane.c2p(0, 0), plane.c2p(0, 1),
        buff=0, stroke_width=5, color=SECONDARY,
        max_tip_length_to_length_ratio=0.2,
    )
    j_label = MathTex(r"\hat{\jmath}", font_size=LABEL_SIZE, color=SECONDARY)
    j_label.next_to(j_hat.get_end(), LEFT, buff=0.15)

    return i_hat, i_label, j_hat, j_label


def apply_to_plane(plane, mat2x2):
    """Apply a 2x2 matrix to a plane copy, returning the transformed plane."""
    mat3x3 = np.array([
        [mat2x2[0][0], mat2x2[0][1], 0],
        [mat2x2[1][0], mat2x2[1][1], 0],
        [0, 0, 1],
    ])
    return plane.copy().apply_matrix(mat3x3)


def style_matrix(tex, scale_val=1.0):
    """Return a MathTex matrix with consistent styling."""
    tex.scale(scale_val)
    return tex


# ═══════════════════════════════════════════════════════════════════════
class Video28_MatrixMultiplication(Scene):
    """Full video: matrix multiplication as composition of transformations."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_composition_idea()
        self.scene3_tracking_basis()
        self.scene4_deriving_formula()
        self.scene5_standard_algorithm()
        self.scene6_worked_example()
        self.scene7_non_commutativity()
        self.scene8_properties()
        self.scene9_summary()

    # ── Scene 1: Hook + ChannelIntro ─────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Welcome back to Linear Algebra. "
            "Last time we saw that a matrix is a transformation of space. "
            "But what happens when you apply two transformations in a row?",
            duration=14,
        )
        play_intro(self, "Matrix Multiplication", "Linear Algebra")

        # Show two mystery matrices with a composition arrow
        mat_a = MathTex(
            r"A", font_size=TITLE_SIZE, color=PRIMARY,
        )
        then_text = Text(
            "then", font_size=HEADING_SIZE, color=DIM, font=SANS,
        )
        mat_b = MathTex(
            r"B", font_size=TITLE_SIZE, color=SECONDARY,
        )
        question = MathTex(
            r"= \; ?", font_size=TITLE_SIZE, color=ACCENT,
        )

        chain = VGroup(mat_a, then_text, mat_b, question).arrange(
            RIGHT, buff=0.5,
        )
        self.ly.center_in_content(chain)

        self.play(Write(mat_a), run_time=FAST)
        self.play(Write(then_text), run_time=FAST)
        self.play(Write(mat_b), run_time=FAST)
        self.play(Write(question), run_time=FAST)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 2: Composition of Transformations ──────────────────────
    def scene2_composition_idea(self):
        self.add_subcaption(
            "Think about it geometrically. "
            "A matrix is a transformation of space. "
            "If we apply transformation A and then transformation B, "
            "the net effect is a single combined transformation.",
            duration=15,
        )

        self.ly.title("Composition of Transformations")

        plane = make_plane(length=6, shift=LEFT * 2.8)
        i_hat, i_label, j_hat, j_label = make_basis_arrows(plane)

        self.play(Create(plane), run_time=FAST)
        self.play(
            GrowArrow(i_hat), Write(i_label),
            GrowArrow(j_hat), Write(j_label),
            run_time=FAST,
        )

        # Label on the right
        step1 = Text(
            "Step 1: Original space", font_size=BODY_SIZE,
            color=WHITE, font=SANS,
        ).move_to(RIGHT * 3.2 + UP * 2.5)
        self.play(Write(step1), run_time=FAST)
        self.wait(0.5)

        # Transformation A: shear
        # A = [[1, 1], [0, 1]]
        shear_2x2 = [[1, 1], [0, 1]]
        t_plane_a = apply_to_plane(plane, shear_2x2)

        new_i_a = Arrow(
            plane.c2p(0, 0), plane.c2p(1, 0),
            buff=0, stroke_width=5, color=PRIMARY,
            max_tip_length_to_length_ratio=0.2,
        )
        new_i_label_a = MathTex(r"\hat{\imath}", font_size=LABEL_SIZE, color=PRIMARY)
        new_i_label_a.next_to(new_i_a.get_end(), DOWN, buff=0.15)

        new_j_a = Arrow(
            plane.c2p(0, 0), plane.c2p(1, 1),
            buff=0, stroke_width=5, color=SECONDARY,
            max_tip_length_to_length_ratio=0.15,
        )
        new_j_label_a = MathTex(r"\hat{\jmath}", font_size=LABEL_SIZE, color=SECONDARY)
        new_j_label_a.next_to(new_j_a.get_end(), UR, buff=0.1)

        self.add_subcaption(
            "First, apply transformation A: a shear. "
            "The grid slants to the right.",
            duration=8,
        )

        self.play(
            Transform(plane, t_plane_a),
            Transform(i_hat, new_i_a),
            Transform(i_label, new_i_label_a),
            Transform(j_hat, new_j_a),
            Transform(j_label, new_j_label_a),
            run_time=1.8,
        )
        self.wait(0.3)

        # Update step label
        self.play(
            Transform(step1, Text(
                "Step 2: After A (shear)", font_size=BODY_SIZE,
                color=PRIMARY, font=SANS,
            ).move_to(RIGHT * 3.2 + UP * 2.5)),
            run_time=FAST,
        )
        self.wait(0.5)

        # Transformation B: rotation 90 degrees
        # B = [[0, -1], [1, 0]]
        rot_2x2 = [[0, -1], [1, 0]]
        # Combined: B * A = [[0*1+(-1)*0, 0*1+(-1)*1], [1*1+0*0, 1*1+0*1]]
        #          = [[0, -1], [1, 1]]
        combined_2x2 = [[0, -1], [1, 1]]
        t_plane_b = apply_to_plane(plane, combined_2x2)

        new_i_b = Arrow(
            plane.c2p(0, 0), plane.c2p(0, 1),
            buff=0, stroke_width=5, color=PRIMARY,
            max_tip_length_to_length_ratio=0.2,
        )
        new_i_label_b = MathTex(r"\hat{\imath}", font_size=LABEL_SIZE, color=PRIMARY)
        new_i_label_b.next_to(new_i_b.get_end(), RIGHT, buff=0.15)

        new_j_b = Arrow(
            plane.c2p(0, 0), plane.c2p(-1, 1),
            buff=0, stroke_width=5, color=SECONDARY,
            max_tip_length_to_length_ratio=0.12,
        )
        new_j_label_b = MathTex(r"\hat{\jmath}", font_size=LABEL_SIZE, color=SECONDARY)
        new_j_label_b.next_to(new_j_b.get_end(), LEFT, buff=0.1)

        self.add_subcaption(
            "Then apply transformation B: a 90 degree rotation. "
            "The sheared grid rotates into a new shape.",
            duration=10,
        )

        self.play(
            Transform(plane, t_plane_b),
            Transform(i_hat, new_i_b),
            Transform(i_label, new_i_label_b),
            Transform(j_hat, new_j_b),
            Transform(j_label, new_j_label_b),
            run_time=1.8,
        )
        self.wait(0.3)

        self.play(
            Transform(step1, Text(
                "Step 3: After B then A", font_size=BODY_SIZE,
                color=SECONDARY, font=SANS,
            ).move_to(RIGHT * 3.2 + UP * 2.5)),
            run_time=FAST,
        )
        self.wait(1.0)

        # Key insight
        insight = Text(
            "One transformation doing BOTH",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        ).move_to(RIGHT * 3.2 + UP * 0.5)

        self.add_subcaption(
            "The result looks like a single transformation was applied. "
            "And that is exactly what matrix multiplication computes: "
            "the single matrix that does both at once.",
            duration=14,
        )

        self.play(Write(insight), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 3: Tracking the Basis Vectors ──────────────────────────
    def scene3_tracking_basis(self):
        self.add_subcaption(
            "So how do we find the matrix for this combined transformation? "
            "We track the basis vectors. "
            "Where does i-hat go after both A and B?",
            duration=14,
        )

        self.ly.title("Tracking Basis Vectors")

        # Show the idea with formulas
        # After A: i-hat -> first column of A
        # After B: T_A(i-hat) -> B * (first column of A)

        step1_tex = MathTex(
            r"\hat{\imath} \xrightarrow{A} T_A(\hat{\imath}) \xrightarrow{B} T_B(T_A(\hat{\imath}))",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(step1_tex)
        self.play(Write(step1_tex), run_time=SLOW)
        self.wait(1.5)

        self.ly.clear()

        self.add_subcaption(
            "After A, i-hat lands at the first column of A. "
            "Then B takes that vector and transforms it again. "
            "The result is the first column of B times A.",
            duration=14,
        )

        # Show the column interpretation
        a_mat = MathTex(
            r"A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        b_mat = MathTex(
            r"B = \begin{pmatrix} e & f \\ g & h \end{pmatrix}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )

        self.ly.center_in_content(a_mat)
        self.play(Write(a_mat), run_time=NORMAL)
        self.wait(0.5)

        self.add_subcaption(
            "After transformation A, i-hat lands at (a, c), the first column. "
            "Now transformation B acts on this vector.",
            duration=12,
        )

        # First column of A highlighted
        col_a1 = MathTex(
            r"T_A(\hat{\imath}) = \begin{pmatrix} a \\ c \end{pmatrix}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(col_a1)
        self.play(
            FadeOut(a_mat),
            Write(col_a1), run_time=NORMAL,
        )
        self.wait(1.0)

        self.ly.clear()

        # Now apply B to this column
        self.add_subcaption(
            "Applying B to (a, c) means multiplying B by this column vector. "
            "Using matrix-vector multiplication from last time.",
            duration=12,
        )

        apply_b = MathTex(
            r"T_B\!\begin{pmatrix} a \\ c \end{pmatrix}"
            r"= \begin{pmatrix} e & f \\ g & h \end{pmatrix}"
            r"\begin{pmatrix} a \\ c \end{pmatrix}"
            r"= \begin{pmatrix} ea + fc \\ ga + hc \end{pmatrix}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.center_in_content(apply_b)
        self.play(Write(apply_b), run_time=SLOW)
        self.wait(2.0)

        self.ly.clear()

        # Same for j-hat
        self.add_subcaption(
            "Similarly, j-hat goes through A then B. "
            "After A, j-hat lands at (b, d). "
            "After B, it lands at (eb plus fd, gb plus hd).",
            duration=14,
        )

        apply_b_j = MathTex(
            r"T_B\!\begin{pmatrix} b \\ d \end{pmatrix}"
            r"= \begin{pmatrix} e & f \\ g & h \end{pmatrix}"
            r"\begin{pmatrix} b \\ d \end{pmatrix}"
            r"= \begin{pmatrix} eb + fd \\ gb + hd \end{pmatrix}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.center_in_content(apply_b_j)
        self.play(Write(apply_b_j), run_time=SLOW)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 4: Deriving the Formula ─────────────────────────────────
    def scene4_deriving_formula(self):
        self.add_subcaption(
            "Putting it all together, the combined matrix B times A has these "
            "two columns we just computed. This IS the matrix multiplication formula.",
            duration=14,
        )

        self.ly.title("Deriving the Formula")

        # Show the result matrix
        result = MathTex(
            r"BA = \begin{pmatrix} ea+fc & eb+fd \\ ga+hc & gb+hd \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(result)
        self.play(Write(result), run_time=SLOW)
        self.wait(1.5)

        # Break down each entry
        self.add_subcaption(
            "Look at the top-left entry: e times a plus f times c. "
            "That is the dot product of the first row of B "
            "with the first column of A.",
            duration=12,
        )

        self.ly.clear()

        # Show the dot-product interpretation
        row_col = MathTex(
            r"(BA)_{11} = (e, f) \cdot (a, c) = ea + fc",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(row_col)
        self.play(Write(row_col), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

        self.add_subcaption(
            "The top-right entry is the dot product of the first row of B "
            "with the second column of A. "
            "And so on for every entry.",
            duration=12,
        )

        # General pattern
        general = MathTex(
            r"(BA)_{ij} = \sum_{k=1}^{2} b_{ik} \, a_{kj}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(general)
        self.play(Write(general), run_time=SLOW)
        self.wait(1.0)

        # Label
        label = Text(
            "Row i of B  dot  Column j of A",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        label.next_to(general, DOWN, buff=0.5)
        self.play(Write(label), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 5: The Standard Algorithm ───────────────────────────────
    def scene5_standard_algorithm(self):
        self.add_subcaption(
            "Here is the standard algorithm for matrix multiplication. "
            "To find each entry, take a row from the first matrix "
            "and a column from the second matrix, and compute their dot product.",
            duration=16,
        )

        self.ly.title("The Row-Column Algorithm")

        # Show two matrices side by side with a multiplication sign
        left_mat = MathTex(
            r"\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        times = MathTex(r"\times", font_size=HEADING_SIZE, color=DIM)
        right_mat = MathTex(
            r"\begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )

        m_group = VGroup(left_mat, times, right_mat).arrange(RIGHT, buff=0.6)
        self.ly.center_in_content(m_group)

        self.play(Write(left_mat), run_time=FAST)
        self.play(Write(times), run_time=FAST)
        self.play(Write(right_mat), run_time=FAST)
        self.wait(1.0)

        # Highlight the row and column
        self.add_subcaption(
            "For the top-left entry: take row 1 of the left matrix "
            "and column 1 of the right matrix. "
            "Their dot product is 1 times 5 plus 2 times 7, equals 19.",
            duration=14,
        )

        row_box = SurroundingRectangle(
            left_mat, color=RED, buff=0.1, stroke_width=2.5,
        )
        col_box = SurroundingRectangle(
            right_mat, color=RED, buff=0.1, stroke_width=2.5,
        )
        self.play(Create(row_box), Create(col_box), run_time=FAST)
        self.wait(0.5)

        # Show the computation
        comp = MathTex(
            r"1 \times 5 + 2 \times 7 = 19",
            font_size=HEADING_SIZE, color=RED,
        )
        comp.next_to(m_group, DOWN, buff=0.6)
        self.play(Write(comp), run_time=NORMAL)
        self.wait(1.5)

        # Fill in the result
        self.ly.clear()

        self.add_subcaption(
            "Repeat for each entry: row 1 dot column 2, "
            "row 2 dot column 1, row 2 dot column 2.",
            duration=10,
        )

        # Show all four computations
        result = MathTex(
            r"\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}"
            r"\begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}"
            r"= \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(result)
        self.play(Write(result), run_time=SLOW)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 6: Worked Example ───────────────────────────────────────
    def scene6_worked_example(self):
        self.add_subcaption(
            "Let us work through a more interesting example "
            "using our transformation intuition. "
            "We will compose a shear with a 90 degree rotation.",
            duration=12,
        )

        self.ly.title("Worked Example: Shear then Rotation")

        # Show A (shear) and B (rotation)
        a_label = MathTex(
            r"A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        b_label = MathTex(
            r"B = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )

        ab_group = VGroup(a_label, b_label).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        ab_group.move_to(LEFT * 3.5)
        self.play(Write(a_label), run_time=NORMAL)
        self.play(Write(b_label), run_time=NORMAL)

        # Describe what they do
        desc_a = Text(
            "A: shear (slide right)", font_size=BODY_SIZE,
            color=PRIMARY, font=SANS,
        )
        desc_b = Text(
            "B: rotate 90 degrees", font_size=BODY_SIZE,
            color=SECONDARY, font=SANS,
        )
        descs = VGroup(desc_a, desc_b).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        descs.next_to(ab_group, RIGHT, buff=0.8)

        self.play(Write(desc_a), Write(desc_b), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        # Compute B*A
        self.add_subcaption(
            "We want B times A: first apply A, then B. "
            "The first column of A is (1, 0). "
            "Applying B gives (0, 1).",
            duration=12,
        )

        step1 = MathTex(
            r"\text{Column 1 of } BA = B \begin{pmatrix} 1 \\ 0 \end{pmatrix}"
            r"= \begin{pmatrix} 0 \cdot 1 + (-1) \cdot 0 \\ 1 \cdot 1 + 0 \cdot 0 \end{pmatrix}"
            r"= \begin{pmatrix} 0 \\ 1 \end{pmatrix}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.center_in_content(step1)
        self.play(Write(step1), run_time=SLOW)
        self.wait(1.5)

        self.ly.clear()

        self.add_subcaption(
            "The second column of A is (1, 1). "
            "Applying B gives (-1, 1).",
            duration=8,
        )

        step2 = MathTex(
            r"\text{Column 2 of } BA = B \begin{pmatrix} 1 \\ 1 \end{pmatrix}"
            r"= \begin{pmatrix} 0 + (-1) \\ 1 + 0 \end{pmatrix}"
            r"= \begin{pmatrix} -1 \\ 1 \end{pmatrix}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.center_in_content(step2)
        self.play(Write(step2), run_time=SLOW)
        self.wait(1.5)

        self.ly.clear()

        # Show the final result
        self.add_subcaption(
            "So B times A equals this matrix. "
            "This single matrix performs the shear followed by the rotation.",
            duration=10,
        )

        final_result = MathTex(
            r"BA = \begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix}",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(final_result)
        box = SurroundingRectangle(
            final_result, color=ACCENT, buff=0.2, stroke_width=2.5,
        )
        self.play(Write(final_result), run_time=NORMAL)
        self.play(Create(box), run_time=FAST)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 7: Non-Commutativity ────────────────────────────────────
    def scene7_non_commutativity(self):
        self.add_subcaption(
            "Now here is something crucial. "
            "Matrix multiplication is generally NOT commutative. "
            "A times B is not the same as B times A.",
            duration=12,
        )

        self.ly.title("Order Matters!")

        # Show both products
        ba_label = MathTex(
            r"BA = \begin{pmatrix} 0 & -1 \\ 1 & 1 \end{pmatrix}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        ab_label = MathTex(
            r"AB = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )

        products = VGroup(ba_label, ab_label).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        self.ly.center_in_content(products)

        self.play(Write(ba_label), run_time=NORMAL)
        self.wait(0.5)
        self.play(Write(ab_label), run_time=NORMAL)
        self.wait(1.0)

        # Highlight the difference
        neq = MathTex(
            r"\neq", font_size=TITLE_SIZE, color=RED,
        )
        neq.move_to((ba_label.get_center() + ab_label.get_center()) / 2)

        self.add_subcaption(
            "These are completely different matrices! "
            "B times A gives a different transformation than A times B.",
            duration=10,
        )

        self.play(Write(neq), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

        # Visual: show two grids side by side
        self.add_subcaption(
            "Geometrically, this makes sense. "
            "Shearing then rotating gives a different shape "
            "than rotating then shearing. The order of operations matters.",
            duration=14,
        )

        plane_left = make_plane(length=4.5, shift=LEFT * 3.2)
        plane_right = make_plane(length=4.5, shift=RIGHT * 3.2)

        # BA result: [[0, -1], [1, 1]]
        ba_transformed = apply_to_plane(plane_left, [[0, -1], [1, 1]])
        # AB result: [[1, -1], [1, 0]]
        ab_transformed = apply_to_plane(plane_right, [[1, -1], [1, 0]])

        label_l = Text(
            "B then A", font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        ).move_to(LEFT * 3.2 + UP * 2.8)
        label_r = Text(
            "A then B", font_size=LABEL_SIZE, color=PRIMARY, font=SANS,
        ).move_to(RIGHT * 3.2 + UP * 2.8)

        self.play(
            Create(plane_left), Create(plane_right),
            Write(label_l), Write(label_r),
            run_time=FAST,
        )

        self.play(
            Transform(plane_left, ba_transformed),
            Transform(plane_right, ab_transformed),
            run_time=1.8,
        )

        # Add basis vectors to both
        i_l, il_l, j_l, jl_l = make_basis_arrows(plane_left)
        i_r, il_r, j_r, jl_r = make_basis_arrows(plane_right)

        # BA: i-hat -> (0,1), j-hat -> (-1,1)
        new_i_l = Arrow(
            plane_left.c2p(0, 0), plane_left.c2p(0, 1),
            buff=0, stroke_width=4, color=PRIMARY,
            max_tip_length_to_length_ratio=0.2,
        )
        new_j_l = Arrow(
            plane_left.c2p(0, 0), plane_left.c2p(-1, 1),
            buff=0, stroke_width=4, color=SECONDARY,
            max_tip_length_to_length_ratio=0.12,
        )
        # AB: i-hat -> (1,1), j-hat -> (-1,0)
        new_i_r = Arrow(
            plane_right.c2p(0, 0), plane_right.c2p(1, 1),
            buff=0, stroke_width=4, color=PRIMARY,
            max_tip_length_to_length_ratio=0.15,
        )
        new_j_r = Arrow(
            plane_right.c2p(0, 0), plane_right.c2p(-1, 0),
            buff=0, stroke_width=4, color=SECONDARY,
            max_tip_length_to_length_ratio=0.2,
        )

        self.play(
            GrowArrow(new_i_l), GrowArrow(new_j_l),
            GrowArrow(new_i_r), GrowArrow(new_j_r),
            run_time=FAST,
        )
        self.wait(2.0)

        # Key reminder
        reminder = Text(
            "Function composition is not commutative!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        ).move_to(DOWN * 2.5)
        self.play(Write(reminder), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 8: Properties ───────────────────────────────────────────
    def scene8_properties(self):
        self.add_subcaption(
            "Before we wrap up, let us note some important properties "
            "of matrix multiplication that will be useful later.",
            duration=10,
        )

        self.ly.title("Properties of Matrix Multiplication")

        # Property 1: Associative
        prop1_title = Text(
            "Associative", font_size=BODY_SIZE, color=PRIMARY,
            font=SANS, weight=BOLD,
        )
        prop1_formula = MathTex(
            r"(AB)C = A(BC)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop1 = VGroup(prop1_title, prop1_formula).arrange(RIGHT, buff=0.5)

        # Property 2: Not commutative
        prop2_title = Text(
            "Not Commutative", font_size=BODY_SIZE, color=RED,
            font=SANS, weight=BOLD,
        )
        prop2_formula = MathTex(
            r"AB \neq BA \text{ (in general)}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop2 = VGroup(prop2_title, prop2_formula).arrange(RIGHT, buff=0.5)

        # Property 3: Identity
        prop3_title = Text(
            "Identity", font_size=BODY_SIZE, color=SECONDARY,
            font=SANS, weight=BOLD,
        )
        prop3_formula = MathTex(
            r"AI = IA = A",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop3 = VGroup(prop3_title, prop3_formula).arrange(RIGHT, buff=0.5)

        # Property 4: Dimension rule
        prop4_title = Text(
            "Dimensions", font_size=BODY_SIZE, color=ACCENT,
            font=SANS, weight=BOLD,
        )
        prop4_formula = MathTex(
            r"(m \times n)(n \times p) = (m \times p)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop4 = VGroup(prop4_title, prop4_formula).arrange(RIGHT, buff=0.5)

        props = VGroup(prop1, prop2, prop3, prop4).arrange(
            DOWN, buff=0.6, aligned_edge=LEFT,
        )
        props.move_to(DOWN * 0.5)

        for prop in props:
            self.play(FadeIn(prop, shift=LEFT * 0.2), run_time=FAST)
            self.wait(0.8)

        self.add_subcaption(
            "Notice the dimension rule: the inner dimensions must match. "
            "An m by n matrix can multiply an n by p matrix, "
            "giving an m by p result.",
            duration=12,
        )
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 9: Summary + Outro ─────────────────────────────────────
    def scene9_summary(self):
        self.add_subcaption(
            "Let us recap what we have learned about matrix multiplication. "
            "It is not just a mechanical algorithm. "
            "It is composition of transformations.",
            duration=12,
        )

        self.ly.title("Key Takeaways")

        bullets = [
            Text("1. Matrix multiplication = composing transformations",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. Each column of the result is a column of the first "
                 "matrix transformed by the second",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3. The standard algorithm: row dot column",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("4. Order matters: AB is generally not equal to BA",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("5. Dimensions must match: (m x n)(n x p) = (m x p)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(bullets, run_time=0.6, wait_time=0.5)
        self.wait(1.0)

        # Teaser
        self.add_subcaption(
            "Next time, we will learn about determinants: "
            "a single number that tells you how a transformation "
            "scales area. See you then!",
            duration=12,
        )

        self.ly.clear()

        play_outro(self, "Determinants", "Linear Algebra")
