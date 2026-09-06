"""
Video 29: Determinants
Linear Algebra Playlist — Video 5 of 16

Covers: geometric meaning of determinant as area scaling factor,
the 2x2 formula (ad - bc), signed area and orientation,
det = 0 (non-invertible), worked examples, and key properties.

Render draft:  manim -ql scripts/undergraduate/video-29-determinants.py Video29_Determinants
Render final:  manim -qh scripts/undergraduate/video-29-determinants.py Video29_Determinants
Preview still: manim -ql --format=png -s scripts/undergraduate/video-29-determinants.py Video29_Determinants
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


def make_unit_square(plane):
    """Create a filled unit square on the given plane."""
    sq = Polygon(
        plane.c2p(0, 0), plane.c2p(1, 0),
        plane.c2p(1, 1), plane.c2p(0, 1),
        fill_color=ACCENT, fill_opacity=0.25,
        stroke_color=ACCENT, stroke_width=2,
    )
    return sq


def make_parallelogram(plane, mat2x2):
    """Create a filled parallelogram from the transformed unit square."""
    a, b = mat2x2[0][0], mat2x2[0][1]
    c, d = mat2x2[1][0], mat2x2[1][1]
    para = Polygon(
        plane.c2p(0, 0), plane.c2p(a, c),
        plane.c2p(a + b, c + d), plane.c2p(b, d),
        fill_color=PRIMARY, fill_opacity=0.2,
        stroke_color=PRIMARY, stroke_width=2,
    )
    return para


# ═══════════════════════════════════════════════════════════════════════
class Video29_Determinants(Scene):
    """Full video: determinants as area scaling factor of transformations."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_area_scaling()
        self.scene3_two_by_two_formula()
        self.scene4_signed_area()
        self.scene5_det_zero()
        self.scene6_worked_example()
        self.scene7_properties()
        self.scene8_summary()

    # ── Scene 1: Hook + ChannelIntro ─────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Every matrix transformation stretches, squishes, "
            "or flips space. The determinant is the single number "
            "that tells you exactly how much.",
            duration=9.6,
        )
        play_intro(self, "Determinants", "Linear Algebra")

        # Show a dramatic visual: "area changes by what factor?"
        mat_tex = MathTex(
            r"A = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        question = Text(
            "How much does area change?",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )

        self.ly.center_in_content(VGroup(mat_tex, question).arrange(DOWN, buff=0.6))
        self.play(Write(mat_tex), run_time=NORMAL)
        self.wait(0.5)
        self.play(Write(question), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 2: Area Scaling — The Geometric Meaning ────────────────
    def scene2_area_scaling(self):
        self.add_subcaption(
            "Here is the key idea. Start with the unit square, "
            "which has area 1. Apply a matrix transformation. "
            "The square becomes a parallelogram. "
            "The determinant is the area of that parallelogram.",
            duration=13.4,
        )

        self.ly.title("The Geometric Meaning")

        plane = make_plane(length=6, shift=LEFT * 0.3)
        self.play(Create(plane), run_time=FAST)

        # Unit square
        sq = make_unit_square(plane)
        sq_label = Text(
            "Area = 1", font_size=LABEL_SIZE,
            color=ACCENT, font=SANS,
        )
        sq_label.next_to(sq, RIGHT, buff=0.3)

        self.play(FadeIn(sq), run_time=NORMAL)
        self.play(Write(sq_label), run_time=FAST)
        self.wait(11.2)  # pacing: caption 2 slot (natural 12.65s)

        # Apply transformation A = [[3,1],[0,2]]
        # det = 3*2 - 1*0 = 6, so area = 6
        mat_a = [[3, 1], [0, 2]]
        t_plane = apply_to_plane(plane, mat_a)
        para = make_parallelogram(plane, mat_a)

        self.add_subcaption(
            "Now apply the transformation. "
            "The unit square stretches into a parallelogram. "
            "The determinant of this matrix is 6, "
            "so the new area is 6 times the original.",
            duration=11.1,
        )

        self.play(
            Transform(plane, t_plane),
            Transform(sq, para),
            run_time=1.8,
        )

        # Update label
        new_label = Text(
            "Area = 6", font_size=LABEL_SIZE,
            color=PRIMARY, font=SANS,
        ).next_to(para, RIGHT, buff=0.3)
        self.play(
            Transform(sq_label, new_label),
            run_time=FAST,
        )
        self.wait(9.5)  # pacing: caption 3 slot (natural 10.34s)

        # Key insight box
        self.add_subcaption(
            "In general, det of A equals the area scaling factor. "
            "If det of A is 2, areas double. "
            "If det of A is one half, areas halve.",
            duration=10.5,
        )

        formula = MathTex(
            r"\det(A) = \frac{\text{area after}}{\text{area before}}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        box = SurroundingRectangle(formula, color=ACCENT, buff=0.2, stroke_width=2)
        formula_group = VGroup(formula, box)
        formula_group.move_to(DOWN * 2.5)
        self.play(Write(formula), Create(box), run_time=NORMAL)
        self.wait(9.1)  # pacing: caption 4 slot (natural 9.72s)

        self.ly.clear()

    # ── Scene 3: The 2x2 Formula ─────────────────────────────────────
    def scene3_two_by_two_formula(self):
        self.add_subcaption(
            "So how do we compute this area scaling factor? "
            "Consider a general 2 by 2 matrix with entries a, b, c, d. "
            "The columns give us two vectors: (a, c) and (b, d).",
            duration=14.6,
        )

        self.ly.title("The 2 by 2 Formula")

        # Show the matrix
        mat = MathTex(
            r"A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(mat)
        self.play(Write(mat), run_time=NORMAL)
        self.wait(12.5)  # pacing: caption 5 slot (natural 13.87s)

        # Show columns as vectors
        self.ly.clear()

        self.add_subcaption(
            "Column 1 is the vector (a, c) and column 2 is (b, d). "
            "The parallelogram formed by these two vectors "
            "has area equal to the absolute value of a d minus b c.",
            duration=14.7,
        )

        cols = MathTex(
            r"\text{col}_1 = \begin{pmatrix} a \\ c \end{pmatrix}"
            r"\quad\quad"
            r"\text{col}_2 = \begin{pmatrix} b \\ d \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(cols)
        self.play(Write(cols), run_time=NORMAL)
        self.wait(13.3)  # pacing: caption 6 slot (natural 13.94s)

        self.ly.clear()

        # Derive the formula
        self.add_subcaption(
            "The area of a parallelogram formed by two vectors "
            "is the magnitude of their cross product. "
            "This gives the determinant formula.",
            duration=9.0,
        )

        # Show derivation step by step
        cross = MathTex(
            r"|\vec{v}_1 \times \vec{v}_2| "
            r"= |a \cdot d - b \cdot c|",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(cross)
        self.play(Write(cross), run_time=SLOW)
        self.wait(6.8)  # pacing: caption 7 slot (natural 8.21s)

        self.ly.clear()

        # The formula — big reveal
        self.add_subcaption(
            "So the determinant of a 2 by 2 matrix is simply "
            "a times d minus b times c. "
            "This is one of the most important formulas in linear algebra.",
            duration=10.3,
        )

        formula = MathTex(
            r"\det\!\begin{pmatrix} a & b \\ c & d \end{pmatrix}"
            r"= ad - bc",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(formula)
        box = SurroundingRectangle(
            formula, color=ACCENT, buff=0.25, stroke_width=3,
            corner_radius=0.1,
        )
        self.play(Write(formula), run_time=NORMAL)
        self.play(Create(box), run_time=FAST)
        self.wait(8.4)  # pacing: caption 8 slot (natural 9.60s)

        self.ly.clear()

    # ── Scene 4: Signed Area — Orientation Matters ───────────────────
    def scene4_signed_area(self):
        self.add_subcaption(
            "But the determinant is not just area. "
            "It is signed area. When the determinant is positive, "
            "orientation is preserved. "
            "When it is negative, orientation gets flipped.",
            duration=11.8,
        )

        self.ly.title("Signed Area and Orientation")

        # Case 1: det > 0
        plane_left = make_plane(length=4.5, shift=LEFT * 3.5)
        plane_right = make_plane(length=4.5, shift=RIGHT * 3.5)

        self.play(Create(plane_left), Create(plane_right), run_time=FAST)

        # Left: expansion det=2
        sq_left = make_unit_square(plane_left)
        para_left = make_parallelogram(plane_left, [[2, 0], [0, 1]])
        label_left = Text(
            "det = 2 > 0", font_size=LABEL_SIZE,
            color=SECONDARY, font=SANS, weight=BOLD,
        ).move_to(LEFT * 3.5 + DOWN * 3)

        # Right: reflection det=-1
        sq_right = make_unit_square(plane_right)
        para_right = Polygon(
            plane_right.c2p(0, 0), plane_right.c2p(0, 1),
            plane_right.c2p(1, 1), plane_right.c2p(1, 0),
            fill_color=RED, fill_opacity=0.2,
            stroke_color=RED, stroke_width=2,
        )
        label_right = Text(
            "det = -1 < 0", font_size=LABEL_SIZE,
            color=RED, font=SANS, weight=BOLD,
        ).move_to(RIGHT * 3.5 + DOWN * 3)

        self.play(
            FadeIn(sq_left), FadeIn(sq_right),
            Write(label_left), Write(label_right),
            run_time=FAST,
        )
        self.wait(10.6)  # pacing: caption 9 slot (natural 11.09s)

        # Transform left: stretch horizontally (det = 2)
        t_left = apply_to_plane(plane_left, [[2, 0], [0, 1]])
        self.add_subcaption(
            "On the left, stretching horizontally doubles the area. "
            "The determinant is positive 2. "
            "Orientation is preserved: i-hat still points right, "
            "j-hat still points up.",
            duration=12.2,
        )
        self.play(
            Transform(plane_left, t_left),
            Transform(sq_left, para_left),
            run_time=1.5,
        )
        self.wait(11.3)  # pacing: caption 10 slot (natural 11.45s)

        # Transform right: reflect across y=x (det = -1)
        t_right = apply_to_plane(plane_right, [[0, 1], [1, 0]])
        self.add_subcaption(
            "On the right, we reflect across the line y equals x. "
            "The area is still 1, but the determinant is negative 1. "
            "Orientation is flipped: i-hat and j-hat have swapped.",
            duration=13.1,
        )
        self.play(
            Transform(plane_right, t_right),
            Transform(sq_right, para_right),
            run_time=1.5,
        )
        self.wait(1.0)

        # Key summary
        summary = Text(
            "det > 0 : preserved     det < 0 : flipped",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        ).move_to(DOWN * 2.8)
        self.play(Write(summary), run_time=NORMAL)
        self.wait(9.2)  # pacing: caption 11 slot (natural 12.34s)

        self.ly.clear()

    # ── Scene 5: det = 0 — The Crucial Case ─────────────────────────
    def scene5_det_zero(self):
        self.add_subcaption(
            "Now for the most important case. "
            "When the determinant is zero, "
            "something dramatic happens. "
            "The transformation squishes all of 2D space "
            "into a lower dimension.",
            duration=11.8,
        )

        self.ly.title("det = 0 : Space Collapses")

        plane = make_plane(length=6, shift=ORIGIN)
        self.play(Create(plane), run_time=FAST)

        # Unit square
        sq = make_unit_square(plane)
        self.play(FadeIn(sq), run_time=FAST)

        # i-hat and j-hat
        i_hat, i_label, j_hat, j_label = make_basis_arrows(plane)
        self.play(
            GrowArrow(i_hat), Write(i_label),
            GrowArrow(j_hat), Write(j_label),
            run_time=FAST,
        )
        self.wait(9.9)  # pacing: caption 12 slot (natural 11.02s)

        # Apply [[1,2],[2,4]] — det = 1*4 - 2*2 = 0, squishes to line y=2x
        self.add_subcaption(
            "This matrix has determinant zero: "
            "1 times 4 minus 2 times 2 equals 0. "
            "Watch what happens to the grid. "
            "The entire 2D plane collapses onto a single line.",
            duration=12.5,
        )

        zero_mat = [[1, 2], [2, 4]]
        t_plane = apply_to_plane(plane, zero_mat)

        # Transformed shapes
        new_sq = Polygon(
            plane.c2p(0, 0), plane.c2p(1, 2),
            plane.c2p(3, 6), plane.c2p(2, 4),
            fill_color=RED, fill_opacity=0.3,
            stroke_color=RED, stroke_width=2,
        )
        new_i = Arrow(
            plane.c2p(0, 0), plane.c2p(1, 2),
            buff=0, stroke_width=5, color=PRIMARY,
            max_tip_length_to_length_ratio=0.2,
        )
        new_i_l = MathTex(r"\hat{\imath}", font_size=LABEL_SIZE, color=PRIMARY)
        new_i_l.next_to(new_i.get_end(), RIGHT, buff=0.1)
        new_j = Arrow(
            plane.c2p(0, 0), plane.c2p(2, 4),
            buff=0, stroke_width=5, color=SECONDARY,
            max_tip_length_to_length_ratio=0.1,
        )
        new_j_l = MathTex(r"\hat{\jmath}", font_size=LABEL_SIZE, color=SECONDARY)
        new_j_l.next_to(new_j.get_end(), RIGHT, buff=0.1)

        self.play(
            Transform(plane, t_plane),
            Transform(sq, new_sq),
            Transform(i_hat, new_i), Transform(i_label, new_i_l),
            Transform(j_hat, new_j), Transform(j_label, new_j_l),
            run_time=2.0,
        )
        self.wait(1.0)

        # Label
        zero_label = Text(
            "det = 0 : 2D collapses to a line!",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        ).move_to(DOWN * 2.5)
        self.play(Write(zero_label), run_time=NORMAL)
        self.wait(8.9)  # pacing: caption 13 slot (natural 11.71s)

        # Connection to invertibility
        self.add_subcaption(
            "When the determinant is zero, the matrix is not invertible. "
            "You cannot undo the transformation because information "
            "was lost. Every point on that line came from multiple "
            "original points.",
            duration=13.2,
        )

        invert = MathTex(
            r"\det(A) = 0 \iff A \text{ is not invertible}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        invert_box = SurroundingRectangle(invert, color=ACCENT, buff=0.2, stroke_width=2)
        VGroup(invert, invert_box).move_to(UP * 2.5)
        self.play(Write(invert), Create(invert_box), run_time=NORMAL)
        self.wait(11.8)  # pacing: caption 14 slot (natural 12.43s)

        self.ly.clear()

    # ── Scene 6: Worked Example ───────────────────────────────────────
    def scene6_worked_example(self):
        self.add_subcaption(
            "Let's compute a determinant step by step. "
            "Take the matrix with rows 2, 1 and 5, 3. "
            "We apply the formula: a times d minus b times c.",
            duration=12.0,
        )

        self.ly.title("Worked Example")

        # Example 1: det = 1
        mat = MathTex(
            r"A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        self.ly.center_in_content(mat)
        self.play(Write(mat), run_time=NORMAL)
        self.wait(9.9)  # pacing: caption 15 slot (natural 11.23s)

        self.ly.clear()

        self.add_subcaption(
            "The determinant is 2 times 3 minus 1 times 5, "
            "which equals 6 minus 5, which equals 1. "
            "This transformation preserves area.",
            duration=10.8,
        )

        # Computation
        step1 = MathTex(
            r"\det(A) = (2)(3) - (1)(5)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(step1)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        step2 = MathTex(
            r"= 6 - 5 = 1",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.center_in_content(step2)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(1.0)

        result_label = Text(
            "Area is preserved!",
            font_size=HEADING_SIZE, color=SECONDARY,
            font=SANS, weight=BOLD,
        ).next_to(step2, DOWN, buff=0.5)
        self.play(Write(result_label), run_time=FAST)
        self.wait(4.9)  # pacing: caption 16 slot (natural 10.08s)

        self.ly.clear()

        # Example 2: det = 0
        self.add_subcaption(
            "Now a second example. "
            "Matrix with rows 1, 2 and 3, 6. "
            "The determinant is 1 times 6 minus 2 times 3, "
            "equals 6 minus 6, equals 0.",
            duration=13.1,
        )

        mat2 = MathTex(
            r"B = \begin{pmatrix} 1 & 2 \\ 3 & 6 \end{pmatrix}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        self.ly.center_in_content(mat2)
        self.play(Write(mat2), run_time=NORMAL)
        self.wait(0.5)

        self.ly.clear()

        comp2 = MathTex(
            r"\det(B) = (1)(6) - (2)(3) = 6 - 6 = 0",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.center_in_content(comp2)
        self.play(Write(comp2), run_time=NORMAL)

        zero_note = Text(
            "Not invertible!",
            font_size=HEADING_SIZE, color=RED,
            font=SANS, weight=BOLD,
        ).next_to(comp2, DOWN, buff=0.5)
        self.play(Write(zero_note), run_time=FAST)
        self.wait(8.7)  # pacing: caption 17 slot (natural 12.34s)

        self.ly.clear()

    # ── Scene 7: Key Properties ───────────────────────────────────────
    def scene7_properties(self):
        self.add_subcaption(
            "The determinant has several beautiful properties "
            "that follow from its geometric meaning.",
            duration=5.6,
        )

        title = self.ly.title("Key Properties")
        self.wait(6.3)  # pacing: caption 18 slot (natural 4.90s) — title on screen

        # Property 1: Identity
        self.add_subcaption(
            "The determinant of the identity matrix is 1, "
            "because the identity does not change area.",
            duration=6.7,
        )

        prop1_title = Text(
            "Identity", font_size=BODY_SIZE, color=PRIMARY,
            font=SANS, weight=BOLD,
        )
        prop1_formula = MathTex(
            r"\det(I) = 1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop1 = VGroup(prop1_title, prop1_formula).arrange(RIGHT, buff=0.5)
        self.ly.safe_place(prop1, direction=DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(prop1, shift=LEFT * 0.2), run_time=0.8)
        self.wait(6.6)  # pacing: caption 19 slot (natural 5.95s)

        # Property 2: Multiplicativity
        self.add_subcaption(
            "The determinant of a product equals the product "
            "of the determinants. "
            "Area scaling factors compose by multiplication.",
            duration=8.4,
        )

        prop2_title = Text(
            "Multiplicative", font_size=BODY_SIZE, color=SECONDARY,
            font=SANS, weight=BOLD,
        )
        prop2_formula = MathTex(
            r"\det(AB) = \det(A) \cdot \det(B)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop2 = VGroup(prop2_title, prop2_formula).arrange(RIGHT, buff=0.5)
        self.ly.safe_place(prop2, direction=DOWN, anchor=prop1, buff=0.4)
        self.play(FadeIn(prop2, shift=LEFT * 0.2), run_time=0.8)
        self.wait(8.3)  # pacing: caption 20 slot (natural 7.66s)

        # Property 3: Transpose
        self.add_subcaption(
            "The determinant of a transpose equals the determinant "
            "of the original matrix. "
            "Swapping rows for columns does not change area scaling.",
            duration=9.5,
        )

        prop3_title = Text(
            "Transpose", font_size=BODY_SIZE, color=ACCENT,
            font=SANS, weight=BOLD,
        )
        prop3_formula = MathTex(
            r"\det(A^T) = \det(A)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop3 = VGroup(prop3_title, prop3_formula).arrange(RIGHT, buff=0.5)
        self.ly.safe_place(prop3, direction=DOWN, anchor=prop2, buff=0.4)
        self.play(FadeIn(prop3, shift=LEFT * 0.2), run_time=0.8)
        self.wait(9.4)  # pacing: caption 21 slot (natural 8.74s)

        # Property 4: Scalar multiple
        self.add_subcaption(
            "Scaling a row by a constant c "
            "multiplies the determinant by c. "
            "Scaling the entire matrix by c multiplies "
            "the determinant by c squared for a 2 by 2 matrix.",
            duration=12.0,
        )

        prop4_title = Text(
            "Scalar multiple", font_size=BODY_SIZE, color=RED,
            font=SANS, weight=BOLD,
        )
        prop4_formula = MathTex(
            r"\det(cA) = c^n \det(A) \text{ for } n \times n",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop4 = VGroup(prop4_title, prop4_formula).arrange(RIGHT, buff=0.5)
        self.ly.safe_place(prop4, direction=DOWN, anchor=prop3, buff=0.4)
        self.play(FadeIn(prop4, shift=LEFT * 0.2), run_time=0.8)
        self.wait(11.9)  # pacing: caption 22 slot (natural 11.23s)

        # Property 5: Row swap
        self.add_subcaption(
            "Swapping two rows of a matrix "
            "changes the sign of the determinant. "
            "This corresponds to flipping orientation.",
            duration=8.3,
        )

        prop5_title = Text(
            "Row swap", font_size=BODY_SIZE, color=PRIMARY,
            font=SANS, weight=BOLD,
        )
        prop5_formula = MathTex(
            r"\text{swap rows } \Rightarrow \det \to -\det",
            font_size=HEADING_SIZE, color=WHITE,
        )
        prop5 = VGroup(prop5_title, prop5_formula).arrange(RIGHT, buff=0.5)
        self.ly.safe_place(prop5, direction=DOWN, anchor=prop4, buff=0.4)
        self.play(FadeIn(prop5, shift=LEFT * 0.2), run_time=0.8)
        self.wait(8.2)  # pacing: caption 23 slot (natural 7.54s)

        self.ly.clear()

    # ── Scene 8: Summary + Outro ─────────────────────────────────────
    def scene8_summary(self):
        self.add_subcaption(
            "Let's recap. The determinant measures how much "
            "a transformation scales area. "
            "It is positive when orientation is preserved, "
            "negative when flipped, and zero when space collapses.",
            duration=12.4,
        )

        self.ly.title("Key Takeaways")

        bullets = [
            Text("1. det(A) = area scaling factor of the transformation",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text(r"2. 2x2 formula: det = ad - bc",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3. det > 0: preserved, det < 0: flipped",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("4. det = 0 means not invertible",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("5. det(AB) = det(A) det(B)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(bullets, run_time=0.6, wait_time=0.5)

        self.wait(6.2)  # pacing: caption 24 slot (natural 11.69s)
        self.ly.clear()

        # Teaser
        self.add_subcaption(
            "Next time, we will explore inverse matrices: "
            "the transformation that undoes your transformation. "
            "And we will see exactly why det = 0 "
            "means no inverse exists. See you then!",
            duration=13.5,
        )

        teaser = Text(
            "Can every transformation be undone?",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(teaser)
        self.play(FadeIn(teaser, shift=LEFT * 0.15), run_time=0.5)
        self.wait(6.0)  # pacing: caption 25 slot (natural 12.74s) — teaser card holds
        self.play(FadeOut(teaser), run_time=0.5)

        play_outro(self, "Inverse Matrices", "Linear Algebra")
