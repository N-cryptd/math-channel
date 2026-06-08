"""
Video 27: Matrices as Transformations
Linear Algebra Playlist — Video 3 of 16

Covers: linear transformations as functions, basis vector tracking,
matrix columns encode where basis vectors land, rotation and shear examples,
and matrix-vector multiplication as applying a transformation.

Render draft:  manim -ql scripts/undergraduate/video-27-matrices-as-transformations.py Video27_MatricesAsTransformations
Render final:  manim -qh scripts/undergraduate/video-27-matrices-as-transformations.py Video27_MatricesAsTransformations

v2 rewrite: setup_background, SANS font, progressive_reveal, section_divider,
formula_box, split crowded scenes, content budgets, LayoutEngine v2.
"""

from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits, clamp_position


# ── Helpers ───────────────────────────────────────────────────────────
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
    """Return i-hat, i-label, j-hat, j-label on the given plane."""
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


# ═══════════════════════════════════════════════════════════════════════
class Video27_MatricesAsTransformations(Scene):
    """Full video: 9+ scenes on matrices as transformations. v2 quality."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_what_is_transformation()
        self.scene2b_linear_intro()
        self.scene3_linear_vs_nonlinear()
        self.scene4_following_basis()
        self.scene4b_insight()
        self.scene5_matrix_encodes()
        self.scene5b_fill()
        self.scene6_rotation_example()
        self.scene6b_verify()
        self.scene7_shear_example()
        self.scene8_matrix_vector_mult()
        self.scene8b_connection()
        self.scene8c_example()
        self.scene9_summary()

    # ── Scene 1: Hook + Intro ─────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Welcome back to Linear Algebra. So far we have talked about vectors "
            "and linear combinations. Today we answer one of the biggest questions: "
            "what does a matrix actually do?",
            duration=12,
        )
        play_intro(self, "Matrices as Transformations", "Linear Algebra")

        self.add_subcaption(
            "You have probably seen matrices before: grids of numbers. "
            "But what do those numbers mean? "
            "A matrix is a transformation of space.",
            duration=12,
        )

        matrix_mob = Matrix(
            [[1, 2], [3, 4]],
            bracket_h_buff=0.2, bracket_v_buff=0.25,
        ).scale(1.2)
        q_mark = Text(
            "?", font_size=72, color=ACCENT, font=SANS, weight=BOLD,
        ).next_to(matrix_mob, RIGHT, buff=0.5)

        self.ly.center_in_content(matrix_mob)
        self.ly.safe_place(q_mark, direction=RIGHT, anchor=matrix_mob, buff=0.5)
        self.play(Write(matrix_mob), run_time=NORMAL)
        self.play(Write(q_mark), run_time=FAST)
        self.wait(1.5)

        # Reframe
        self.play(FadeOut(q_mark), FadeOut(matrix_mob), run_time=0.5)
        reframe = Text(
            "A matrix is a transformation of space.",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(reframe)
        self.play(Write(reframe), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 2: What is a Transformation? ───────────────────────────
    def scene2_what_is_transformation(self):
        self.ly.section_divider(1, "What is a Transformation?")

        self.add_subcaption(
            "A transformation is just a function. It takes every point in space "
            "and moves it somewhere new. Think of it as picking up the "
            "entire plane and moving it around.",
            duration=14,
        )

        func = MathTex(
            r"T : \mathbb{R}^2 \to \mathbb{R}^2",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(func)
        self.play(Write(func), run_time=NORMAL)
        self.wait(1.0)

        # Visual: grid of dots
        dots = VGroup(*[
            Dot(np.array([x * 0.7, y * 0.7, 0]), radius=0.04,
                 color=WHITE, fill_opacity=0.5)
            for x in range(-3, 4)
            for y in range(-3, 4)
        ])
        self.ly.center_in_content(dots)
        self.play(FadeIn(dots, scale=0.8), run_time=FAST)
        self.wait(0.5)

        # "Move" the dots
        moved_dots = dots.copy().rotate(PI / 12).shift(RIGHT * 0.5 + UP * 0.3)

        self.add_subcaption(
            "Under a transformation, every dot moves to a new position. "
            "The key question is: what rule determines where each point goes?",
            duration=10,
        )
        self.play(Transform(dots, moved_dots), run_time=2.0)
        self.wait(1.5)
        self.ly.clear()

    def scene2b_linear_intro(self):
        self.add_subcaption(
            "There are infinitely many possible transformations. "
            "But mathematicians focus on a special kind: linear transformations.",
            duration=10,
        )

        many = Text(
            "Infinitely many transformations... But one kind is special:",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(many)
        self.play(Write(many), run_time=NORMAL)
        self.wait(1.0)

        special = Text(
            "LINEAR transformations",
            font_size=TITLE_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(special, direction=DOWN, anchor=many, buff=0.5)
        self.play(Write(special), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 3: Linear vs Non-Linear ──────────────────────────────
    def scene3_linear_vs_nonlinear(self):
        self.ly.section_divider(2, "Linear vs Non-Linear")

        self.add_subcaption(
            "A linear transformation has two simple rules. "
            "First, grid lines must remain straight and evenly spaced. "
            "Second, the origin must stay in place.",
            duration=14,
        )

        plane = make_plane(length=6, shift=LEFT * 3.5)
        i_hat, i_label, j_hat, j_label = make_basis_arrows(plane)

        self.play(Create(plane), run_time=FAST)
        self.play(
            GrowArrow(i_hat), Write(i_label),
            GrowArrow(j_hat), Write(j_label),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Linear: 90-degree rotation
        rot_mat = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
        t_plane = plane.copy().apply_matrix(rot_mat)

        new_i = Arrow(
            plane.c2p(0, 0), plane.c2p(0, 1),
            buff=0, stroke_width=5, color=PRIMARY,
            max_tip_length_to_length_ratio=0.2,
        )
        new_i_label = MathTex(r"\hat{\imath}", font_size=LABEL_SIZE, color=PRIMARY)
        new_i_label.next_to(new_i.get_end(), RIGHT, buff=0.15)
        new_j = Arrow(
            plane.c2p(0, 0), plane.c2p(-1, 0),
            buff=0, stroke_width=5, color=SECONDARY,
            max_tip_length_to_length_ratio=0.2,
        )
        new_j_label = MathTex(r"\hat{\jmath}", font_size=LABEL_SIZE, color=SECONDARY)
        new_j_label.next_to(new_j.get_end(), DOWN, buff=0.15)

        lin_label = Text("LINEAR", font_size=HEADING_SIZE, color=SECONDARY,
                          font=SANS, weight=BOLD)
        lin_label.move_to(RIGHT * 3 + UP * 1.5)

        self.add_subcaption(
            "Here is a linear transformation: a rotation. "
            "Grid lines stay straight, evenly spaced, and the origin is fixed.",
            duration=10,
        )
        self.play(Write(lin_label), run_time=FAST)
        self.play(
            Transform(plane, t_plane),
            Transform(i_hat, new_i), Transform(i_label, new_i_label),
            Transform(j_hat, new_j), Transform(j_label, new_j_label),
            run_time=2.0,
        )
        self.wait(1.5)

        self.play(FadeOut(plane), FadeOut(i_hat), FadeOut(i_label),
                  FadeOut(j_hat), FadeOut(j_label), FadeOut(lin_label),
                  run_time=0.5)

        # Non-linear: curved grid
        self.add_subcaption(
            "A non-linear transformation breaks these rules. "
            "Grid lines can curve, and the origin might move.",
            duration=8,
        )

        nlin_label = Text("NON-LINEAR", font_size=HEADING_SIZE, color=RED,
                          font=SANS, weight=BOLD)
        nlin_label.move_to(LEFT * 3 + UP * 2)

        curves = VGroup()
        for y_val in np.linspace(-2.5, 2.5, 6):
            points = [
                np.array([x, y_val + 0.3 * np.sin(x), 0])
                for x in np.linspace(-3.5, 3.5, 30)
            ]
            curve = VMobject()
            curve.set_points_smoothly(points)
            curve.set_stroke(color=PLANE_BG, width=1)
            curves.add(curve)
        for x_val in np.linspace(-3, 3, 7):
            points = [
                np.array([x_val, y + 0.3 * np.sin(x_val), 0])
                for y in np.linspace(-3, 3, 30)
            ]
            curve = VMobject()
            curve.set_points_smoothly(points)
            curve.set_stroke(color=PLANE_BG, width=1)
            curves.add(curve)
        curves.shift(LEFT * 3.5)

        self.play(Write(nlin_label), run_time=FAST)
        self.play(Create(curves), run_time=NORMAL)
        self.wait(1.5)

        # Rules — progressive reveal
        rules = [
            Text("Linear transformations:", font_size=BODY_SIZE,
                 color=WHITE, font=SANS, weight=BOLD),
            Text("1. Grid lines stay straight", font_size=BODY_SIZE,
                 color=SECONDARY, font=SANS),
            Text("2. Spacing stays even", font_size=BODY_SIZE,
                 color=SECONDARY, font=SANS),
            Text("3. Origin stays fixed", font_size=BODY_SIZE,
                 color=SECONDARY, font=SANS),
        ]
        # Position on right side
        rules_vg = VGroup(*rules).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        rules_vg.move_to(RIGHT * 2.5 + UP * 0.5)
        self.ly.progressive_reveal(rules, reveal_anim=FadeIn, run_time=0.6, wait_time=0.6)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 4: Following the Basis Vectors ──────────────────────────
    def scene4_following_basis(self):
        self.ly.section_divider(3, "Following the Basis Vectors")

        self.add_subcaption(
            "Here is the beautiful insight. "
            "If you know where i-hat and j-hat land, you know where "
            "EVERY vector lands.",
            duration=10,
        )

        plane = make_plane(length=6, shift=LEFT * 2.5)
        i_hat, i_label, j_hat, j_label = make_basis_arrows(plane)

        self.play(Create(plane), run_time=FAST)
        self.play(
            GrowArrow(i_hat), Write(i_label),
            GrowArrow(j_hat), Write(j_label),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Arbitrary vector
        vec = Arrow(
            plane.c2p(0, 0), plane.c2p(2, 1),
            buff=0, stroke_width=4, color=ACCENT,
            max_tip_length_to_length_ratio=0.15,
        )
        vec_label = MathTex(r"\vec{v} = (2, 1)", font_size=LABEL_SIZE, color=ACCENT)
        vec_label.next_to(vec.get_end(), UR, buff=0.1)

        self.play(GrowArrow(vec), Write(vec_label), run_time=NORMAL)

        # Decompose
        decomp = MathTex(
            r"\vec{v} = 2\hat{\imath} + 1\hat{\jmath}",
            font_size=BODY_SIZE, color=WHITE,
        )
        decomp.move_to(RIGHT * 3 + UP * 2)

        self.add_subcaption(
            "Take vector v equals 2 times i-hat plus 1 times j-hat. "
            "If the transformation is linear, it preserves this combination. "
            "So T of v equals 2 times T of i-hat, plus 1 times T of j-hat.",
            duration=16,
        )
        self.play(Write(decomp), run_time=NORMAL)
        self.wait(1.0)

        result = MathTex(
            r"T(\vec{v}) = 2\,T(\hat{\imath}) + 1\,T(\hat{\jmath})",
            font_size=BODY_SIZE, color=ACCENT,
        )
        result.next_to(decomp, DOWN, buff=0.5)
        self.play(Write(result), run_time=SLOW)
        self.wait(1.0)

        # Animate transformation (rotation example)
        new_i = Arrow(
            plane.c2p(0, 0), plane.c2p(0, 1),
            buff=0, stroke_width=5, color=PRIMARY,
            max_tip_length_to_length_ratio=0.2,
        )
        new_i_label = MathTex(r"T(\hat{\imath})", font_size=LABEL_SIZE, color=PRIMARY)
        new_i_label.next_to(new_i.get_end(), RIGHT, buff=0.15)
        new_j = Arrow(
            plane.c2p(0, 0), plane.c2p(-1, 0),
            buff=0, stroke_width=5, color=SECONDARY,
            max_tip_length_to_length_ratio=0.2,
        )
        new_j_label = MathTex(r"T(\hat{\jmath})", font_size=LABEL_SIZE, color=SECONDARY)
        new_j_label.next_to(new_j.get_end(), DOWN, buff=0.15)

        # v lands at 2*(0,1) + 1*(-1,0) = (-1, 2)
        new_vec = Arrow(
            plane.c2p(0, 0), plane.c2p(-1, 2),
            buff=0, stroke_width=4, color=ACCENT,
            max_tip_length_to_length_ratio=0.15,
        )
        new_vec_label = MathTex(r"T(\vec{v})", font_size=LABEL_SIZE, color=ACCENT)
        new_vec_label.next_to(new_vec.get_end(), UL, buff=0.1)

        # Fade out formula text for budget
        self.play(FadeOut(decomp), FadeOut(result), run_time=0.3)

        self.play(
            Transform(i_hat, new_i), Transform(i_label, new_i_label),
            Transform(j_hat, new_j), Transform(j_label, new_j_label),
            Transform(vec, new_vec), Transform(vec_label, new_vec_label),
            run_time=2.0,
        )
        self.wait(1.5)
        self.ly.clear()

    def scene4b_insight(self):
        """Key insight — separate for budget."""
        self.add_subcaption(
            "The transformation of any vector is determined by "
            "where i-hat and j-hat go. The basis vectors determine "
            "EVERYTHING about a linear transformation.",
            duration=10,
        )

        insight_items = [
            Text("Key Insight", font_size=HEADING_SIZE, color=ACCENT,
                 font=SANS, weight=BOLD),
            Text("The basis vectors determine", font_size=BODY_SIZE,
                 color=WHITE, font=SANS),
            Text("EVERYTHING about a linear", font_size=BODY_SIZE,
                 color=WHITE, font=SANS),
            Text("transformation.", font_size=BODY_SIZE,
                 color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(insight_items, run_time=0.7, wait_time=0.8)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 5: The Matrix Encodes the Transformation ─────────────────
    def scene5_matrix_encodes(self):
        self.ly.section_divider(4, "The Matrix")

        self.add_subcaption(
            "A linear transformation is completely determined by "
            "where i-hat and j-hat land. "
            "A matrix is just a compact way to record those two destinations.",
            duration=14,
        )

        plane = make_plane(length=5, shift=LEFT * 3.5)
        i_hat, i_label, j_hat, j_label = make_basis_arrows(plane)

        self.play(Create(plane), run_time=FAST)
        self.play(
            GrowArrow(i_hat), Write(i_label),
            GrowArrow(j_hat), Write(j_label),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Blank matrix on right
        mat_title = Text("The Matrix", font_size=HEADING_SIZE, color=PRIMARY,
                         font=SANS, weight=BOLD)
        mat_title.move_to(RIGHT * 2.5 + UP * 2.5)

        mat_mob = MathTex(
            r"\begin{pmatrix} ? & ? \\ ? & ? \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        mat_mob.next_to(mat_title, DOWN, buff=0.5)

        self.play(Write(mat_title), run_time=FAST)
        self.play(Write(mat_mob), run_time=NORMAL)
        self.wait(0.5)

        self.add_subcaption(
            "The first column records where i-hat goes. "
            "The second column records where j-hat goes.",
            duration=10,
        )

        col1_label = MathTex(
            r"\leftarrow T(\hat{\imath})", font_size=LABEL_SIZE, color=PRIMARY,
        )
        col1_label.next_to(mat_mob, RIGHT, buff=0.1).shift(UP * 0.3)
        col2_label = MathTex(
            r"\leftarrow T(\hat{\jmath})", font_size=LABEL_SIZE, color=SECONDARY,
        )
        col2_label.next_to(mat_mob, RIGHT, buff=0.1).shift(DOWN * 0.3)

        self.play(Write(col1_label), Write(col2_label), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

    def scene5b_fill(self):
        """Fill in the matrix with concrete values."""
        self.add_subcaption(
            "Suppose i-hat lands at (1, 2) and j-hat lands at (3, 4). "
            "Then our matrix becomes:",
            duration=10,
        )

        # Show filled matrix
        mat_filled = MathTex(
            r"\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        mat_group = self.ly.formula_box(mat_filled, color=PRIMARY)
        self.ly.center_in_content(mat_group)
        self.play(Write(mat_group), run_time=NORMAL)
        self.wait(1.0)

        # Summary
        summary_items = [
            Text("Column 1 = where i-hat lands", font_size=BODY_SIZE,
                 color=PRIMARY, font=SANS),
            Text("Column 2 = where j-hat lands", font_size=BODY_SIZE,
                 color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(summary_items, start_from=mat_group,
                                    run_time=0.6, wait_time=0.8)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 6: Rotation by 90° ──────────────────────────────────────
    def scene6_rotation_example(self):
        self.ly.section_divider(5, "Example: Rotation")

        self.add_subcaption(
            "Let us look at a classic example: rotation by 90 degrees "
            "counterclockwise. I-hat goes from (1, 0) to (0, 1). "
            "J-hat goes from (0, 1) to (-1, 0).",
            duration=14,
        )

        plane = make_plane(length=6.5, shift=ORIGIN)
        i_hat, i_label, j_hat, j_label = make_basis_arrows(plane)

        self.play(Create(plane), run_time=FAST)
        self.play(
            GrowArrow(i_hat), Write(i_label),
            GrowArrow(j_hat), Write(j_label),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Unit square
        square = Polygon(
            plane.c2p(0, 0), plane.c2p(1, 0),
            plane.c2p(1, 1), plane.c2p(0, 1),
            color=ACCENT, fill_opacity=0.15, stroke_width=2,
        )
        self.play(Create(square), run_time=FAST)
        self.wait(0.5)

        # Matrix
        rot_mat = MathTex(
            r"\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        rot_mat.to_edge(UR, buff=0.3)

        new_i = Arrow(
            plane.c2p(0, 0), plane.c2p(0, 1),
            buff=0, stroke_width=5, color=PRIMARY,
            max_tip_length_to_length_ratio=0.2,
        )
        new_i_label = MathTex(r"(0,1)", font_size=LABEL_SIZE, color=PRIMARY)
        new_i_label.next_to(new_i.get_end(), RIGHT, buff=0.15)
        new_j = Arrow(
            plane.c2p(0, 0), plane.c2p(-1, 0),
            buff=0, stroke_width=5, color=SECONDARY,
            max_tip_length_to_length_ratio=0.2,
        )
        new_j_label = MathTex(r"(-1,0)", font_size=LABEL_SIZE, color=SECONDARY)
        new_j_label.next_to(new_j.get_end(), DOWN, buff=0.15)

        para = Polygon(
            plane.c2p(0, 0), plane.c2p(0, 1),
            plane.c2p(-1, 1), plane.c2p(-1, 0),
            color=ACCENT, fill_opacity=0.15, stroke_width=2,
        )

        rot_3x3 = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
        t_plane = plane.copy().apply_matrix(rot_3x3)

        self.play(Write(rot_mat), run_time=NORMAL)
        self.play(
            Transform(plane, t_plane),
            Transform(i_hat, new_i), Transform(i_label, new_i_label),
            Transform(j_hat, new_j), Transform(j_label, new_j_label),
            Transform(square, para),
            run_time=2.0,
        )
        self.wait(1.5)
        self.ly.clear()

    def scene6b_verify(self):
        """Verify rotation with a vector — separate for budget."""
        self.add_subcaption(
            "Notice the unit square becomes another square. "
            "Rotation preserves shape and area. "
            "Let us check: vector (2, 1) rotated becomes (-1, 2).",
            duration=12,
        )

        verify_items = [
            Text("Check: (2, 1) rotated:", font_size=BODY_SIZE,
                 color=WHITE, font=SANS),
            Text("The unit square stays a square", font_size=BODY_SIZE,
                 color=SECONDARY, font=SANS),
            Text("Rotation preserves shape and area", font_size=BODY_SIZE,
                 color=ACCENT, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(verify_items, run_time=0.6, wait_time=1.0)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Shear Example ───────────────────────────────────────
    def scene7_shear_example(self):
        self.ly.section_divider(6, "Example: Shear")

        self.add_subcaption(
            "Now a shear transformation. "
            "This pushes everything horizontally by an amount "
            "proportional to its height. I-hat stays at (1, 0). "
            "J-hat slides to (1, 1).",
            duration=14,
        )

        plane = make_plane(length=6.5, shift=ORIGIN)
        i_hat, i_label, j_hat, j_label = make_basis_arrows(plane)

        self.play(Create(plane), run_time=FAST)
        self.play(
            GrowArrow(i_hat), Write(i_label),
            GrowArrow(j_hat), Write(j_label),
            run_time=NORMAL,
        )
        self.wait(0.5)

        square = Polygon(
            plane.c2p(0, 0), plane.c2p(1, 0),
            plane.c2p(1, 1), plane.c2p(0, 1),
            color=ACCENT, fill_opacity=0.15, stroke_width=2,
        )
        self.play(Create(square), run_time=FAST)

        shear_mat = MathTex(
            r"\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        shear_mat.to_edge(UR, buff=0.3)

        new_i = Arrow(
            plane.c2p(0, 0), plane.c2p(1, 0),
            buff=0, stroke_width=5, color=PRIMARY,
            max_tip_length_to_length_ratio=0.2,
        )
        new_i_label = MathTex(r"(1,0)", font_size=LABEL_SIZE, color=PRIMARY)
        new_i_label.next_to(new_i.get_end(), DOWN, buff=0.15)
        new_j = Arrow(
            plane.c2p(0, 0), plane.c2p(1, 1),
            buff=0, stroke_width=5, color=SECONDARY,
            max_tip_length_to_length_ratio=0.15,
        )
        new_j_label = MathTex(r"(1,1)", font_size=LABEL_SIZE, color=SECONDARY)
        new_j_label.next_to(new_j.get_end(), UR, buff=0.1)

        para = Polygon(
            plane.c2p(0, 0), plane.c2p(1, 0),
            plane.c2p(2, 1), plane.c2p(1, 1),
            color=ACCENT, fill_opacity=0.15, stroke_width=2,
        )

        shear_3x3 = np.array([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
        t_plane = plane.copy().apply_matrix(shear_3x3)

        self.add_subcaption(
            "Watch how the entire grid shears. "
            "The x-axis stays put, but every row slides more to the right.",
            duration=10,
        )
        self.play(Write(shear_mat), run_time=NORMAL)
        self.play(
            Transform(plane, t_plane),
            Transform(i_hat, new_i), Transform(i_label, new_i_label),
            Transform(j_hat, new_j), Transform(j_label, new_j_label),
            Transform(square, para),
            run_time=2.0,
        )
        self.wait(1.5)

        self.add_subcaption(
            "The unit square becomes a parallelogram. "
            "Area is preserved, but shape changes. "
            "This is a key property of shear transformations.",
            duration=10,
        )

        area_note = Text(
            "Area preserved, shape changed",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(area_note, direction=DOWN, anchor=plane, buff=0.3)
        self.play(Write(area_note), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 8: Matrix-Vector Multiplication ─────────────────────────
    def scene8_matrix_vector_mult(self):
        self.ly.section_divider(7, "Matrix-Vector Multiplication")

        self.add_subcaption(
            "When you multiply a matrix by a vector, "
            "you are applying the transformation to that vector.",
            duration=10,
        )

        self.ly.title("Matrix-Vector Multiplication")

        self.add_subcaption(
            "To compute A times v, scale the first column of A "
            "by the first component of v, scale the second column "
            "by the second component, and add them up.",
            duration=14,
        )

        gen_formula = MathTex(
            r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}"
            r"\begin{pmatrix} x \\ y \end{pmatrix}"
            r"= x \begin{pmatrix} a \\ c \end{pmatrix}"
            r"+ y \begin{pmatrix} b \\ d \end{pmatrix}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.center_in_content(gen_formula)
        self.play(Write(gen_formula), run_time=SLOW)
        self.wait(1.5)

        # Highlight columns
        col1_box = SurroundingRectangle(
            gen_formula[0][0:4], color=PRIMARY, buff=0.08, stroke_width=2.5,
        )
        col2_box = SurroundingRectangle(
            gen_formula[0][5:9], color=SECONDARY, buff=0.08, stroke_width=2.5,
        )
        self.play(Create(col1_box), Create(col2_box), run_time=FAST)
        self.wait(0.5)

        col1_text = Text("Column 1: T(i-hat)", font_size=BODY_SIZE,
                          color=PRIMARY, font=SANS)
        col1_text.next_to(col1_box, DOWN, buff=0.4)
        self.play(Write(col1_text), run_time=FAST)
        self.wait(0.5)

        col2_text = Text("Column 2: T(j-hat)", font_size=BODY_SIZE,
                          color=SECONDARY, font=SANS)
        col2_text.next_to(col2_box, DOWN, buff=0.4)
        self.play(Write(col2_text), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    def scene8b_connection(self):
        """Connect to linear combinations."""
        self.add_subcaption(
            "This is a linear combination of the matrix columns! "
            "The components of the vector are the scalars. "
            "This connects directly to linear combinations and span.",
            duration=14,
        )

        connection = MathTex(
            r"A\vec{v} = v_1 \cdot (\text{col}_1) + v_2 \cdot (\text{col}_2)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        conn_group = self.ly.formula_box(connection, color=ACCENT)
        self.ly.center_in_content(conn_group)
        self.play(Write(conn_group), run_time=SLOW)
        self.wait(2.0)
        self.ly.clear()

    def scene8c_example(self):
        """Numerical example — separate for budget."""
        self.add_subcaption(
            "Let us work through a concrete example. "
            "Apply the rotation matrix to the vector (3, 2).",
            duration=10,
        )

        steps = [
            MathTex(
                r"\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}"
                r"\begin{pmatrix} 3 \\ 2 \end{pmatrix}",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            MathTex(
                r"= 3 \begin{pmatrix} 0 \\ 1 \end{pmatrix}"
                r"+ 2 \begin{pmatrix} -1 \\ 0 \end{pmatrix}",
                font_size=HEADING_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"= \begin{pmatrix} 0 \\ 3 \end{pmatrix}"
                r"+ \begin{pmatrix} -2 \\ 0 \end{pmatrix}"
                r"= \begin{pmatrix} -2 \\ 3 \end{pmatrix}",
                font_size=HEADING_SIZE, color=SECONDARY,
            ),
        ]
        self.ly.progressive_reveal(steps, run_time=0.8, wait_time=1.0)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 9: Summary + Outro ─────────────────────────────────────
    def scene9_summary(self):
        self.ly.section_divider("", "Key Takeaways")

        self.add_subcaption(
            "A matrix is not just a grid of numbers. "
            "It is a transformation of space. The columns tell you "
            "where the basis vectors land.",
            duration=12,
        )

        bullets = [
            Text("1. A matrix = a linear transformation of space",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. Column 1 = where i-hat lands",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("3. Column 2 = where j-hat lands",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("4. Matrix-vector mult = apply the transformation",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5. Linear transforms preserve lines and origin",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(bullets, run_time=0.6, wait_time=0.5)
        self.wait(1.0)
        self.ly.clear()

        # Teaser
        self.add_subcaption(
            "What happens if we apply two transformations in a row? "
            "That is matrix multiplication, coming next.",
            duration=8,
        )

        teaser = Text(
            "Next: Two transformations = matrix multiplication",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(teaser)
        self.play(FadeIn(teaser, shift=UP * 0.3), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear(run_time=0.3)

        # Outro
        play_outro(self, "Matrix Multiplication", "Linear Algebra")
