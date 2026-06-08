"""
Video 32: Row Reduction and Echelon Form
Linear Algebra Playlist — Video 8 of 16

Covers: motivation beyond A^-1, three elementary row operations,
row echelon form (REF), forward elimination with a 3x3 example,
back substitution, reduced row echelon form (RREF), free variables,
and summary.

Render draft:  manim -ql scripts/undergraduate/video-32-row-reduction.py Video32_RowReduction
Render final:  manim -qh scripts/undergraduate/video-32-row-reduction.py Video32_RowReduction
Preview still: manim -ql --format=png -s scripts/undergraduate/video-32-row-reduction.py Video32_RowReduction
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


# ═══════════════════════════════════════════════════════════════════════
class Video32_RowReduction(Scene):
    """Full video: row reduction, Gaussian elimination, REF and RREF."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_why_row_operations_work()
        self.scene3_three_operations()
        self.scene4_echelon_form_definition()
        self.scene5_forward_elimination()
        self.scene6_back_substitution()
        self.scene7_rref()
        self.scene8_free_variables()
        self.scene9_summary()

    # ── Scene 1: Hook + ChannelIntro ─────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Last time we solved systems using the matrix inverse. "
            "But what if the matrix is not invertible? "
            "What if it is not even square? "
            "We need a more powerful and general tool: "
            "row reduction.",
            duration=16,
        )
        play_intro(self, "Row Reduction", "Linear Algebra")

        # Show A^-1 b approach and its limitation
        formula = MathTex(
            r"\vec{x} = A^{-1}\vec{b}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        question = Text(
            "What if A\u207B\u00B9 doesn\u2019t exist?",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        group = VGroup(formula, question).arrange(DOWN, buff=0.6)
        self.ly.center_in_content(group)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(0.5)
        self.play(Write(question), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 2: Why Row Operations Work ─────────────────────────────
    def scene2_why_row_operations_work(self):
        self.add_subcaption(
            "The key idea: certain operations on equations "
            "do not change the solutions. "
            "If we swap two equations, multiply one by a nonzero "
            "constant, or add a multiple of one to another, "
            "the solutions remain exactly the same.",
            duration=18,
        )

        self.ly.title("Preserving Solutions")

        # Original system
        orig = MathTex(
            r"x + 2y &= 5 \\",
            r"3x - y &= 1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(orig)
        self.play(Write(orig), run_time=NORMAL)
        self.wait(0.5)

        self.ly.clear()

        # Show operation and result
        self.add_subcaption(
            "For example, if we multiply the second equation "
            "by 2, we get 6x minus 2y equals 2. "
            "The solution is still x equals 1, y equals 2. "
            "The equations look different, but the solution is unchanged.",
            duration=18,
        )

        op = MathTex(
            r"R_2 \to 2 \cdot R_2",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        result = MathTex(
            r"x + 2y &= 5 \\",
            r"6x - 2y &= 2",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sol = Text(
            "Solution: (1, 2) \u2014 unchanged!",
            font_size=BODY_SIZE, color=SECONDARY, font=MONO,
        )

        group = VGroup(op, result, sol).arrange(DOWN, buff=0.5)
        ensure_fits(group, max_height=4.5)
        self.ly.center_in_content(group)
        self.play(Write(op), run_time=FAST)
        self.play(FadeIn(result), run_time=NORMAL)
        self.play(FadeIn(sol), run_time=FAST)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 3: The Three Elementary Row Operations ─────────────────
    def scene3_three_operations(self):
        self.add_subcaption(
            "There are exactly three elementary row operations. "
            "Together, they are the building blocks "
            "of Gaussian elimination.",
            duration=10,
        )

        self.ly.title("Three Elementary Row Operations")

        # Operation 1
        op1_title = Text(
            "1. Row Swap", font_size=BODY_SIZE,
            color=PRIMARY, font=MONO, weight=BOLD,
        )
        op1_formula = MathTex(
            r"R_i \leftrightarrow R_j",
            font_size=HEADING_SIZE, color=WHITE,
        )
        op1_desc = Text(
            "Swap two rows",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        op1 = VGroup(op1_title, op1_formula, op1_desc).arrange(DOWN, buff=0.15)

        # Operation 2
        self.add_subcaption(
            "Operation 1: swap two rows. "
            "Operation 2: multiply a row by a nonzero constant. "
            "Operation 3: add a multiple of one row to another. "
            "Each preserves the solution set.",
            duration=16,
        )

        op2_title = Text(
            "2. Scale Row", font_size=BODY_SIZE,
            color=SECONDARY, font=MONO, weight=BOLD,
        )
        op2_formula = MathTex(
            r"R_i \to c \cdot R_i \quad (c \neq 0)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        op2_desc = Text(
            "Multiply row by nonzero scalar",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        op2 = VGroup(op2_title, op2_formula, op2_desc).arrange(DOWN, buff=0.15)

        # Operation 3
        op3_title = Text(
            "3. Row Addition", font_size=BODY_SIZE,
            color=ACCENT, font=MONO, weight=BOLD,
        )
        op3_formula = MathTex(
            r"R_i \to R_i + c \cdot R_j",
            font_size=HEADING_SIZE, color=WHITE,
        )
        op3_desc = Text(
            "Add multiple of row j to row i",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        op3 = VGroup(op3_title, op3_formula, op3_desc).arrange(DOWN, buff=0.15)

        items = [op1, op2, op3]
        self.ly.progressive_reveal(items, start_from=None)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 4: Echelon Form — The Goal ─────────────────────────────
    def scene4_echelon_form_definition(self):
        self.add_subcaption(
            "The goal of forward elimination is to reach "
            "row echelon form. This is a staircase pattern "
            "where each pivot step is to the right "
            "of the one above it.",
            duration=14,
        )

        self.ly.title("Row Echelon Form (REF)")

        # Definition
        def1 = Text(
            "\u2713 All zero rows at the bottom",
            font_size=BODY_SIZE, color=WHITE, font=MONO,
        )
        def2 = Text(
            "\u2713 Each leading entry is right of the one above",
            font_size=BODY_SIZE, color=WHITE, font=MONO,
        )
        def3 = Text(
            "\u2713 Each pivot is a nonzero number",
            font_size=BODY_SIZE, color=WHITE, font=MONO,
        )

        items = [def1, def2, def3]
        self.ly.progressive_reveal(items, start_from=None)
        self.wait(1.0)

        self.ly.clear()

        # Show example REF matrix
        self.add_subcaption(
            "Here is an example. Notice the staircase pattern. "
            "The pivots, marked in blue, step to the right "
            "as we go down the rows.",
            duration=12,
        )

        ref_example = MathTex(
            r"\begin{pmatrix}"
            r"\mathbf{1} & 3 & -1 & 2 \\"
            r"0 & \mathbf{2} & 4 & -1 \\"
            r"0 & 0 & \mathbf{3} & 5 \\"
            r"0 & 0 & 0 & 0"
            r"\end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ensure_fits(ref_example, max_height=3.0)
        self.ly.center_in_content(ref_example)
        self.play(Write(ref_example), run_time=SLOW)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 5: Forward Elimination Example ─────────────────────────
    def scene5_forward_elimination(self):
        self.add_subcaption(
            "Let us work through a full example. "
            "We will solve a system of three equations "
            "with three unknowns using Gaussian elimination.",
            duration=12,
        )

        self.ly.title("Forward Elimination Example")

        # Original system
        self.add_subcaption(
            "Here is the system: x plus 2y plus z equals 4. "
            "3x plus 8y plus z equals 12. "
            "2y plus 5z equals 3. "
            "We write this as an augmented matrix.",
            duration=16,
        )

        aug = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"1 & 2 & 1 & 4 \\"
            r"3 & 8 & 1 & 12 \\"
            r"0 & 2 & 5 & 3"
            r"\end{array}\right]",
            font_size=TITLE_SIZE, color=WHITE,
        )
        ensure_fits(aug, max_height=3.0)
        self.ly.center_in_content(aug)
        self.play(Write(aug), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        # Step 1: R2 -> R2 - 3R1
        self.add_subcaption(
            "Step 1: eliminate the 3 below the first pivot. "
            "Row 2 minus 3 times Row 1.",
            duration=8,
        )

        op1 = MathTex(
            r"R_2 \to R_2 - 3R_1",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        step1 = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"1 & 2 & 1 & 4 \\"
            r"0 & 2 & -2 & 0 \\"
            r"0 & 2 & 5 & 3"
            r"\end{array}\right]",
            font_size=HEADING_SIZE, color=WHITE,
        )
        group = VGroup(op1, step1).arrange(DOWN, buff=0.4)
        self.ly.center_in_content(group)
        self.play(Write(op1), run_time=FAST)
        self.play(Transform(aug, step1), run_time=NORMAL)
        self.wait(0.5)
        self.remove(aug)

        self.ly.clear()

        # Step 2: R3 -> R3 - R2
        self.add_subcaption(
            "Step 2: eliminate below the second pivot. "
            "Row 3 minus Row 2.",
            duration=8,
        )

        op2 = MathTex(
            r"R_3 \to R_3 - R_2",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        step2 = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"1 & 2 & 1 & 4 \\"
            r"0 & 2 & -2 & 0 \\"
            r"0 & 0 & 7 & 3"
            r"\end{array}\right]",
            font_size=HEADING_SIZE, color=WHITE,
        )
        group2 = VGroup(op2, step2).arrange(DOWN, buff=0.4)
        self.ly.center_in_content(group2)
        self.play(Write(op2), run_time=FAST)
        self.play(FadeIn(step2), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        # Announce REF reached
        self.add_subcaption(
            "We have reached row echelon form! "
            "Notice the staircase pattern of the pivots: "
            "1, 2, 7. Now we can solve by back substitution.",
            duration=14,
        )

        ref_label = Text(
            "Row Echelon Form reached!",
            font_size=HEADING_SIZE, color=SECONDARY, font=MONO, weight=BOLD,
        )
        ref_final = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"\mathbf{1} & 2 & 1 & 4 \\"
            r"0 & \mathbf{2} & -2 & 0 \\"
            r"0 & 0 & \mathbf{7} & 3"
            r"\end{array}\right]",
            font_size=HEADING_SIZE, color=WHITE,
        )
        group3 = VGroup(ref_label, ref_final).arrange(DOWN, buff=0.4)
        self.ly.center_in_content(group3)
        self.play(Write(ref_label), FadeIn(ref_final), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 6: Back Substitution ───────────────────────────────────
    def scene6_back_substitution(self):
        self.add_subcaption(
            "Now we solve by back substitution, "
            "starting from the last row and working upward.",
            duration=8,
        )

        self.ly.title("Back Substitution")

        # z from row 3
        self.add_subcaption(
            "From the third row: 7z equals 3, so z equals 3/7. "
            "From the second row: 2y minus 2z equals 0. "
            "Substituting z: 2y equals 6/7, so y equals 3/7.",
            duration=16,
        )

        step1 = MathTex(
            r"7z = 3 \implies z = \frac{3}{7}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(step1)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        # y from row 2
        step2 = MathTex(
            r"2y - 2\!\left(\frac{3}{7}\right) = 0 "
            r"\implies y = \frac{3}{7}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(step2)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        # x from row 1
        self.add_subcaption(
            "From the first row: x plus 2y plus z equals 4. "
            "Substituting y and z: x plus 6/7 plus 3/7 equals 4. "
            "So x equals 4 minus 9/7 equals 19/7.",
            duration=16,
        )

        step3 = MathTex(
            r"x + 2\!\left(\frac{3}{7}\right) + \frac{3}{7} = 4 "
            r"\implies x = \frac{19}{7}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(step3)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        # Final solution
        self.add_subcaption(
            "The solution is x equals 19/7, "
            "y equals 3/7, z equals 3/7.",
            duration=8,
        )

        solution = MathTex(
            r"\vec{x} = \begin{pmatrix} 19/7 \\ 3/7 \\ 3/7 \end{pmatrix}",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        box = SurroundingRectangle(
            solution, color=ACCENT, buff=0.25,
            stroke_width=3, corner_radius=0.1,
        )
        group = VGroup(solution, box)
        self.ly.center_in_content(group)
        self.play(Write(solution), Create(box), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 7: Reduced Row Echelon Form ────────────────────────────
    def scene7_rref(self):
        self.add_subcaption(
            "We can go one step further. "
            "Reduced row echelon form, or RREF, "
            "requires each pivot to be 1 "
            "and all entries above and below each pivot to be 0. "
            "The solution becomes directly readable.",
            duration=18,
        )

        self.ly.title("Reduced Row Echelon Form (RREF)")

        # Show REF → RREF
        ref = MathTex(
            r"\text{REF:}\quad "
            r"\begin{pmatrix}"
            r"1 & 2 & 1 \\"
            r"0 & 2 & -2 \\"
            r"0 & 0 & 7"
            r"\end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )

        rref = MathTex(
            r"\text{RREF:}\quad "
            r"\begin{pmatrix}"
            r"\mathbf{1} & 0 & 0 \\"
            r"0 & \mathbf{1} & 0 \\"
            r"0 & 0 & \mathbf{1}"
            r"\end{pmatrix}",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        arrow = MathTex(
            r"\Longrightarrow",
            font_size=HEADING_SIZE, color=DIM,
        )

        group = VGroup(ref, arrow, rref).arrange(RIGHT, buff=0.4)
        ensure_fits(group, max_height=3.0)
        self.ly.center_in_content(group)
        self.play(Write(ref), run_time=NORMAL)
        self.play(Write(arrow), run_time=FAST)
        self.play(FadeIn(rref), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

        # RREF definition
        self.add_subcaption(
            "In RREF, each pivot column is a standard basis vector. "
            "This means the identity matrix appears in the pivot columns. "
            "The solution is read directly from the last column "
            "of the augmented matrix.",
            duration=16,
        )

        items = [
            Text(
                "1. Each pivot = 1",
                font_size=BODY_SIZE, color=WHITE, font=MONO,
            ),
            Text(
                "2. Zeros above AND below each pivot",
                font_size=BODY_SIZE, color=WHITE, font=MONO,
            ),
            Text(
                "3. Solution = last column of augmented matrix",
                font_size=BODY_SIZE, color=ACCENT, font=MONO,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=None)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 8: Free Variables ──────────────────────────────────────
    def scene8_free_variables(self):
        self.add_subcaption(
            "What happens when the system has infinitely many solutions? "
            "Row reduction reveals this through free variables.",
            duration=10,
        )

        self.ly.title("Free Variables")

        # Show a system that gives a row of zeros
        self.add_subcaption(
            "Consider this system. After row reduction, "
            "the third row becomes all zeros. "
            "This means one equation was redundant. "
            "We have only 2 independent equations "
            "for 3 unknowns. One variable is free.",
            duration=18,
        )

        ref_free = MathTex(
            r"\left[\begin{array}{ccc|c}"
            r"1 & 0 & 2 & 3 \\"
            r"0 & 1 & -1 & 1 \\"
            r"0 & 0 & 0 & 0"
            r"\end{array}\right]",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(ref_free)
        self.play(Write(ref_free), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

        # Parameterize
        self.add_subcaption(
            "Column 3 has no pivot, so z is a free variable. "
            "Let z equal t, where t can be any real number. "
            "Then x equals 3 minus 2t, "
            "and y equals 1 plus t.",
            duration=18,
        )

        free_label = Text(
            "z is free \u2192 let z = t",
            font_size=BODY_SIZE, color=PRIMARY, font=MONO, weight=BOLD,
        )
        param_sol = MathTex(
            r"\vec{x} = \begin{pmatrix} 3 - 2t \\ 1 + t \\ t \end{pmatrix}"
            r"= \begin{pmatrix} 3 \\ 1 \\ 0 \end{pmatrix}"
            r"+ t \begin{pmatrix} -2 \\ 1 \\ 1 \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ensure_fits(param_sol, max_height=2.5)
        group = VGroup(free_label, param_sol).arrange(DOWN, buff=0.5)
        self.ly.center_in_content(group)
        self.play(Write(free_label), run_time=FAST)
        self.play(Write(param_sol), run_time=SLOW)
        self.wait(2.0)

        self.ly.clear()

        # Geometric meaning
        self.add_subcaption(
            "Geometrically, this is a line in 3D space. "
            "Every value of t gives a different point on the line. "
            "The number of free variables tells us the dimension "
            "of the solution set.",
            duration=16,
        )

        insight = Text(
            "Free variables = dimension of solution space",
            font_size=HEADING_SIZE, color=ACCENT, font=MONO, weight=BOLD,
        )
        box = SurroundingRectangle(
            insight, color=ACCENT, buff=0.2,
            stroke_width=2, corner_radius=0.1,
        )
        group = VGroup(insight, box)
        self.ly.center_in_content(group)
        self.play(Write(insight), Create(box), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 9: Summary + Outro ─────────────────────────────────────
    def scene9_summary(self):
        self.add_subcaption(
            "Let us recap. Row reduction is the universal "
            "method for solving linear systems. "
            "It works whether or not the matrix is invertible.",
            duration=12,
        )

        self.ly.title("Key Takeaways")

        items = [
            Text(
                "1. 3 row ops preserve solutions",
                font_size=BODY_SIZE, color=WHITE, font=MONO,
            ),
            Text(
                "2. Forward elimination \u2192 REF (staircase)",
                font_size=BODY_SIZE, color=WHITE, font=MONO,
            ),
            Text(
                "3. Back substitution solves from REF",
                font_size=BODY_SIZE, color=WHITE, font=MONO,
            ),
            Text(
                "4. RREF: pivots = 1, zeros elsewhere",
                font_size=BODY_SIZE, color=SECONDARY, font=MONO,
            ),
            Text(
                "5. Free vars \u2192 infinitely many solutions",
                font_size=BODY_SIZE, color=ACCENT, font=MONO,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=None)
        self.wait(1.0)

        self.ly.clear()

        # Outro
        self.add_subcaption(
            "Next time, we will explore the null space "
            "and column space. These are the fundamental "
            "subspaces that reveal the deep structure "
            "behind every matrix. See you then!",
            duration=14,
        )

        play_outro(self, "Null Space and Column Space", "Linear Algebra")
