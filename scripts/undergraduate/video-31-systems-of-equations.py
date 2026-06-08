"""
Video 31: Systems of Equations (Matrix Form)
Linear Algebra Playlist — Video 7 of 16

Covers: from equations to Ax=b, geometric meaning (column/row picture),
classification (unique/infinite/no solution), connection to column space,
worked example using matrix inverse, and summary.

Render draft:  manim -ql scripts/undergraduate/video-31-systems-of-equations.py Video31_SystemsOfEquations
Render final:  manim -qh scripts/undergraduate/video-31-systems-of-equations.py Video31_SystemsOfEquations
Preview still: manim -ql --format=png -s scripts/undergraduate/video-31-systems-of-equations.py Video31_SystemsOfEquations
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


# ═══════════════════════════════════════════════════════════════════════
class Video31_SystemsOfEquations(Scene):
    """Full video: systems of linear equations in matrix form Ax = b."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_equations_to_matrices()
        self.scene3_geometric_meaning()
        self.scene4_classification()
        self.scene5_column_space_connection()
        self.scene6_worked_example()
        self.scene7_summary()

    # ── Scene 1: Hook + ChannelIntro ─────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Every system of linear equations hides a geometric secret. "
            "Lines intersecting, planes colliding, dimensions collapsing. "
            "Today we learn how matrices reveal what your equations "
            "are really doing.",
            duration=16,
        )
        play_intro(self, "Systems of Equations", "Linear Algebra")

        # Motivating question
        question = Text(
            "What do equations have to do with matrices?",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(question)
        self.play(Write(question), run_time=NORMAL)
        self.wait(1.5)

        # Simple system preview
        system_tex = MathTex(
            r"2x + y &= 5 \\",
            r"x - 3y &= 1",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        ensure_fits(system_tex, max_height=2.0)
        system_tex.next_to(question, DOWN, buff=0.6)
        self.play(Write(system_tex), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 2: From Equations to Matrices ───────────────────────────
    def scene2_equations_to_matrices(self):
        self.add_subcaption(
            "Consider our system again. Two equations, two unknowns. "
            "We can rewrite this compactly as a matrix equation. "
            "A times x equals b, where A holds the coefficients, "
            "x holds the variables, and b holds the constants.",
            duration=18,
        )

        self.ly.title("From Equations to Ax = b")

        # Show the system
        system = MathTex(
            r"2x + y &= 5 \\",
            r"x - 3y &= 1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ensure_fits(system, max_height=1.5)
        self.ly.center_in_content(system)
        self.play(Write(system), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        # Now show A, x, b
        self.add_subcaption(
            "The matrix A contains the coefficients. "
            "The vector x contains the unknowns. "
            "The vector b contains the right-hand side constants.",
            duration=14,
        )

        mat_a = MathTex(
            r"A = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        vec_x = MathTex(
            r"\vec{x} = \begin{pmatrix} x \\ y \end{pmatrix}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        vec_b = MathTex(
            r"\vec{b} = \begin{pmatrix} 5 \\ 1 \end{pmatrix}",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        items = [mat_a, vec_x, vec_b]
        self.ly.progressive_reveal(items, start_from=None)
        self.wait(1.0)

        self.ly.clear()

        # Show Ax = b
        self.add_subcaption(
            "Put them together, and we get the matrix equation "
            "A times x equals b. This compact form "
            "works for any number of equations and unknowns.",
            duration=14,
        )

        ax_eq_b = MathTex(
            r"A\,\vec{x} = \vec{b}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        group = VGroup(ax_eq_b)
        self.ly.center_in_content(group)
        self.play(Write(ax_eq_b), run_time=NORMAL)
        self.wait(1.0)

        # Expand to show multiplication
        expansion = MathTex(
            r"\begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix}"
            r"\begin{pmatrix} x \\ y \end{pmatrix}"
            r"= \begin{pmatrix} 5 \\ 1 \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ensure_fits(expansion, max_height=2.5)
        expansion.next_to(ax_eq_b, DOWN, buff=0.5)
        self.play(FadeIn(expansion), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 3: What Does Ax=b Really Mean? ─────────────────────────
    def scene3_geometric_meaning(self):
        self.ly.title("What Does Ax = b Mean?")

        # Column picture
        self.add_subcaption(
            "There are two ways to picture this equation. "
            "First, the column picture. "
            "A times x is a linear combination of the columns of A, "
            "scaled by the components of x.",
            duration=16,
        )

        # Show columns of A
        col_pic = MathTex(
            r"x \begin{pmatrix} 2 \\ 1 \end{pmatrix}"
            r"+ y \begin{pmatrix} 1 \\ -3 \end{pmatrix}"
            r"= \begin{pmatrix} 5 \\ 1 \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ensure_fits(col_pic, max_height=2.0)
        self.ly.center_in_content(col_pic)
        self.play(Write(col_pic), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

        # Row picture - show on a plane
        self.add_subcaption(
            "Second, the row picture. Each equation defines a line "
            "in 2D space. The first equation, 2x plus y equals 5, "
            "is a line. The second equation, x minus 3y equals 1, "
            "is another line. Their intersection is the solution.",
            duration=20,
        )

        plane = make_plane(length=5.0, shift=ORIGIN)
        self.play(Create(plane), run_time=FAST)

        # Line 1: 2x + y = 5 → y = -2x + 5
        line1 = plane.plot(lambda x_val: -2 * x_val + 5, color=PRIMARY)
        label1 = Text(
            "2x + y = 5",
            font_size=LABEL_SIZE, color=PRIMARY, font=MONO,
        ).next_to(line1.get_end(), RIGHT, buff=0.2)

        # Line 2: x - 3y = 1 → y = (x-1)/3
        line2 = plane.plot(lambda x_val: (x_val - 1) / 3, x_range=[-2, 4], color=ACCENT)
        label2 = Text(
            "x - 3y = 1",
            font_size=LABEL_SIZE, color=ACCENT, font=MONO,
        ).next_to(line2.get_end(), RIGHT, buff=0.2)

        self.play(Create(line1), run_time=NORMAL)
        self.play(FadeIn(label1), run_time=FAST)
        self.play(Create(line2), run_time=NORMAL)
        self.play(FadeIn(label2), run_time=FAST)

        # Solution point: x=2, y=1
        sol_point = Dot(plane.c2p(2, 1), color=RED, radius=0.08)
        sol_label = Text(
            "(2, 1)",
            font_size=LABEL_SIZE, color=RED, font=MONO,
        ).next_to(sol_point, UP + RIGHT, buff=0.15)

        self.add_subcaption(
            "The two lines intersect at the point (2, 1). "
            "This means x equals 2 and y equals 1. "
            "Plugging in: 2 times 2 plus 1 equals 5. Correct! "
            "And 2 minus 3 equals negative 1. Correct!",
            duration=18,
        )
        self.play(FadeIn(sol_point), FadeIn(sol_label), run_time=FAST)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 4: Classification — Unique, Infinite, or None ──────────
    def scene4_classification(self):
        self.add_subcaption(
            "Not every system has a unique solution. "
            "There are exactly three possibilities.",
            duration=8,
        )

        self.ly.title("Three Possibilities")

        # Case 1: Unique solution
        self.add_subcaption(
            "Case one: a unique solution. "
            "The lines cross at exactly one point. "
            "This happens when the determinant of A is nonzero, "
            "meaning A is invertible.",
            duration=14,
        )

        # Small planes for each case
        plane1 = make_plane(length=2.8, shift=LEFT * 3.5 + DOWN * 0.5)
        line1a = plane1.plot(lambda x: -x + 2, color=PRIMARY)
        line1b = plane1.plot(lambda x: 0.5 * x - 0.5, color=ACCENT)
        dot1 = Dot(plane1.c2p(5/3, 1/3), color=RED, radius=0.06)
        label1 = Text(
            "Unique Solution",
            font_size=LABEL_SIZE, color=SECONDARY, font=MONO, weight=BOLD,
        ).next_to(plane1, UP, buff=0.2)
        det1 = MathTex(
            r"\det(A) \neq 0",
            font_size=LABEL_SIZE, color=SECONDARY,
        ).next_to(plane1, DOWN, buff=0.2)

        self.play(Create(plane1), run_time=FAST)
        self.play(Create(line1a), Create(line1b), run_time=NORMAL)
        self.play(FadeIn(dot1), run_time=FAST)
        self.play(FadeIn(label1), FadeIn(det1), run_time=FAST)
        self.wait(0.5)

        # Case 2: Infinitely many solutions
        self.add_subcaption(
            "Case two: infinitely many solutions. "
            "The two equations describe the same line. "
            "Every point on the line is a solution.",
            duration=12,
        )

        plane2 = make_plane(length=2.8, shift=ORIGIN + DOWN * 0.5)
        line2a = plane2.plot(lambda x: -x + 2, color=PRIMARY)
        line2b = plane2.plot(lambda x: -x + 2, color=ACCENT)
        label2 = Text(
            "Infinite Solutions",
            font_size=LABEL_SIZE, color=ACCENT, font=MONO, weight=BOLD,
        ).next_to(plane2, UP, buff=0.2)
        det2 = MathTex(
            r"\det(A) = 0",
            font_size=LABEL_SIZE, color=ACCENT,
        ).next_to(plane2, DOWN, buff=0.2)

        self.play(Create(plane2), run_time=FAST)
        self.play(Create(line2a), Create(line2b), run_time=NORMAL)
        self.play(FadeIn(label2), FadeIn(det2), run_time=FAST)
        self.wait(0.5)

        # Case 3: No solution
        self.add_subcaption(
            "Case three: no solution. "
            "The lines are parallel and never meet. "
            "The system is inconsistent.",
            duration=10,
        )

        plane3 = make_plane(length=2.8, shift=RIGHT * 3.5 + DOWN * 0.5)
        line3a = plane3.plot(lambda x: -x + 1, color=PRIMARY)
        line3b = plane3.plot(lambda x: -x + 3, color=ACCENT)
        label3 = Text(
            "No Solution",
            font_size=LABEL_SIZE, color=RED, font=MONO, weight=BOLD,
        ).next_to(plane3, UP, buff=0.2)
        det3 = MathTex(
            r"\det(A) = 0",
            font_size=LABEL_SIZE, color=RED,
        ).next_to(plane3, DOWN, buff=0.2)

        self.play(Create(plane3), run_time=FAST)
        self.play(Create(line3a), Create(line3b), run_time=NORMAL)
        self.play(FadeIn(label3), FadeIn(det3), run_time=FAST)
        self.wait(2.0)

        self.ly.clear()

        # Key connection
        self.add_subcaption(
            "The key insight: for square matrices, "
            "a nonzero determinant guarantees a unique solution. "
            "When the determinant is zero, we could have "
            "infinitely many solutions or none at all.",
            duration=16,
        )

        condition = MathTex(
            r"\det(A) \neq 0 \implies \text{unique solution exists}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        box = SurroundingRectangle(
            condition, color=SECONDARY, buff=0.2,
            stroke_width=2, corner_radius=0.1,
        )
        group = VGroup(condition, box)
        self.ly.center_in_content(group)
        self.play(Write(condition), Create(box), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 5: Connection to Column Space ──────────────────────────
    def scene5_column_space_connection(self):
        self.add_subcaption(
            "Here is a powerful way to think about it. "
            "A times x equals b has a solution "
            "if and only if b lives in the column space of A.",
            duration=14,
        )

        self.ly.title("The Column Space Connection")

        # Show column space concept
        plane = make_plane(length=5.0, shift=ORIGIN)
        self.play(Create(plane), run_time=FAST)

        # Draw column vectors of A = [[2, 1], [1, -3]]
        col1_end = plane.c2p(2, 1)
        col2_end = plane.c2p(1, -3)
        col1_arrow = Arrow(
            plane.c2p(0, 0), col1_end,
            buff=0, color=PRIMARY, stroke_width=3, max_tip_length_to_length_ratio=0.1,
        )
        col2_arrow = Arrow(
            plane.c2p(0, 0), col2_end,
            buff=0, color=SECONDARY, stroke_width=3, max_tip_length_to_length_ratio=0.1,
        )
        col1_label = Text(
            "col 1", font_size=SMALL_SIZE, color=PRIMARY, font=MONO,
        ).next_to(col1_end, RIGHT, buff=0.1)
        col2_label = Text(
            "col 2", font_size=SMALL_SIZE, color=SECONDARY, font=MONO,
        ).next_to(col2_end, LEFT, buff=0.1)

        self.play(
            Create(col1_arrow), FadeIn(col1_label),
            Create(col2_arrow), FadeIn(col2_label),
            run_time=NORMAL,
        )
        self.wait(0.5)

        self.add_subcaption(
            "The column space is every possible vector you can reach "
            "by taking linear combinations of these column vectors. "
            "Since these two columns point in different directions, "
            "they span the entire 2D plane.",
            duration=18,
        )

        # Column space label
        cs_label = Text(
            "Column Space = all of R\u00B2",
            font_size=BODY_SIZE, color=ACCENT, font=MONO, weight=BOLD,
        )
        cs_label.to_corner(UR, buff=0.4)
        self.play(FadeIn(cs_label), run_time=FAST)

        # Show b = (5, 1) as a reachable point
        b_point = Dot(plane.c2p(5, 1), color=RED, radius=0.08)
        b_label = Text(
            "b = (5, 1)",
            font_size=LABEL_SIZE, color=RED, font=MONO,
        ).next_to(b_point, RIGHT, buff=0.15)

        self.add_subcaption(
            "The vector b equals (5, 1) is in the column space. "
            "That means we can find scalars x and y such that "
            "x times column 1 plus y times column 2 equals b. "
            "The solution is x equals 2, y equals 1.",
            duration=18,
        )

        self.play(FadeIn(b_point), FadeIn(b_label), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

        # Summary of column space idea
        self.add_subcaption(
            "In general: A solution exists if b is in the column space. "
            "For a square invertible matrix, the column space "
            "is all of R to the n, so a solution always exists.",
            duration=14,
        )

        theorem = MathTex(
            r"A\vec{x} = \vec{b} \text{ has a solution }"
            r"\iff \vec{b} \in \text{Col}(A)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        box = SurroundingRectangle(
            theorem, color=ACCENT, buff=0.25,
            stroke_width=3, corner_radius=0.1,
        )
        group = VGroup(theorem, box)
        self.ly.center_in_content(group)
        self.play(Write(theorem), Create(box), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 6: Worked Example ──────────────────────────────────────
    def scene6_worked_example(self):
        self.add_subcaption(
            "Let us solve a concrete system. "
            "3x plus 2y equals 8, and x minus y equals 1. "
            "We write this as A times x equals b.",
            duration=14,
        )

        self.ly.title("Worked Example")

        # Show the system
        system = MathTex(
            r"3x + 2y &= 8 \\",
            r"x - y &= 1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(system)
        self.play(Write(system), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        # Show A, b
        self.add_subcaption(
            "The coefficient matrix is A with entries 3, 2, 1, minus 1. "
            "The constant vector is b equals (8, 1).",
            duration=10,
        )

        mat_a = MathTex(
            r"A = \begin{pmatrix} 3 & 2 \\ 1 & -1 \end{pmatrix}, \quad "
            r"\vec{b} = \begin{pmatrix} 8 \\ 1 \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ensure_fits(mat_a, max_height=2.5)
        self.ly.center_in_content(mat_a)
        self.play(Write(mat_a), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        # Compute determinant
        self.add_subcaption(
            "First, check the determinant. "
            "3 times negative 1 minus 2 times 1 equals negative 5. "
            "Since the determinant is nonzero, "
            "a unique solution exists.",
            duration=16,
        )

        det = MathTex(
            r"\det(A) = (3)(-1) - (2)(1) = -3 - 2 = -5 \neq 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(det)
        self.play(Write(det), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

        # Apply inverse formula
        self.add_subcaption(
            "Since A is invertible, the solution is "
            "x equals A inverse times b. "
            "Using the 2 by 2 inverse formula: "
            "swap the diagonal, negate the off-diagonal, "
            "divide by the determinant.",
            duration=18,
        )

        inv = MathTex(
            r"A^{-1} = \frac{1}{-5}"
            r"\begin{pmatrix} -1 & -2 \\ -1 & 3 \end{pmatrix}"
            r"= \begin{pmatrix} 1/5 & 2/5 \\ 1/5 & -3/5 \end{pmatrix}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        ensure_fits(inv, max_height=2.5)
        self.ly.center_in_content(inv)
        self.play(Write(inv), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

        # Compute x = A⁻¹b
        self.add_subcaption(
            "Now multiply A inverse by b. "
            "x equals (1/5 times 8 plus 2/5 times 1), "
            "which is 10/5 equals 2. "
            "y equals (1/5 times 8 minus 3/5 times 1), "
            "which is 5/5 equals 1.",
            duration=20,
        )

        solution = MathTex(
            r"\vec{x} = A^{-1}\vec{b} = "
            r"\begin{pmatrix} 1/5 & 2/5 \\ 1/5 & -3/5 \end{pmatrix}"
            r"\begin{pmatrix} 8 \\ 1 \end{pmatrix}"
            r"= \begin{pmatrix} 2 \\ 1 \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ensure_fits(solution, max_height=2.5)
        self.ly.center_in_content(solution)
        self.play(Write(solution), run_time=SLOW)
        self.wait(1.5)

        self.ly.clear()

        # Verify
        self.add_subcaption(
            "Always verify! 3 times 2 plus 2 times 1 equals 8. "
            "And 2 minus 1 equals 1. Both equations check out.",
            duration=12,
        )

        verify = MathTex(
            r"3(2) + 2(1) = 8 \;\checkmark \qquad "
            r"(2) - (1) = 1 \;\checkmark",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.center_in_content(verify)
        self.play(Write(verify), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 7: Summary + Outro ─────────────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "Let us recap everything we have learned. "
            "Every linear system can be written as A x equals b. "
            "This means: find the vector x that A transforms into b.",
            duration=14,
        )

        self.ly.title("Key Takeaways")

        items = [
            Text(
                "1. Any linear system = Ax = b",
                font_size=BODY_SIZE, color=WHITE, font=MONO,
            ),
            Text(
                "2. Solving = finding x that A maps to b",
                font_size=BODY_SIZE, color=WHITE, font=MONO,
            ),
            Text(
                "3. Three outcomes: unique / infinite / none",
                font_size=BODY_SIZE, color=WHITE, font=MONO,
            ),
            Text(
                "4. det(A) \u2260 0 \u2192 unique solution guaranteed",
                font_size=BODY_SIZE, color=SECONDARY, font=MONO,
            ),
            Text(
                "5. Solution exists \u2194 b is in Col(A)",
                font_size=BODY_SIZE, color=ACCENT, font=MONO,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=None)
        self.wait(1.0)

        self.ly.clear()

        # Final formula
        self.add_subcaption(
            "For invertible matrices, the solution is elegant. "
            "Multiply both sides by A inverse. "
            "x equals A inverse times b. "
            "This is the matrix version of dividing both sides.",
            duration=16,
        )

        formula = MathTex(
            r"A\vec{x} = \vec{b} \quad \Longrightarrow \quad "
            r"\vec{x} = A^{-1}\vec{b}",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        box = SurroundingRectangle(
            formula, color=ACCENT, buff=0.25,
            stroke_width=3, corner_radius=0.1,
        )
        group = VGroup(formula, box)
        self.ly.center_in_content(group)
        self.play(Write(formula), Create(box), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

        # Outro
        self.add_subcaption(
            "Next time, we will learn a systematic method "
            "for solving any system, even when the matrix "
            "is not invertible. It is called row reduction. "
            "See you then!",
            duration=14,
        )

        play_outro(self, "Row Reduction", "Linear Algebra")
