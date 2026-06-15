"""Video 64: Systems of ODEs
Ordinary Differential Equations -- Video 11 of N

Covers: coupled systems motivation, matrix form, eigenvalue method,
worked example (two-tank system), phase plane basics, equilibrium
classification preview.

Competitive analysis: channel-analysis/improvements.md "2026-06-13 -- Systems of ODEs"
Plan: planning/video-64-systems-of-odes.md

Render draft:  manim -ql scripts/undergraduate/video-64-systems-of-odes.py Video64_SystemsOfODEs
Render final:  manim -qh scripts/undergraduate/video-64-systems-of-odes.py Video64_SystemsOfODEs
"""

from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, BG_LIGHT, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video64_SystemsOfODEs(Scene):
    """Full video: Systems of ODEs -- coupled systems, matrix form,
    eigenvalue method, phase plane basics."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_matrix_form()
        self.scene3_eigenvalue_method()
        self.scene4_worked_example()
        self.scene5_phase_plane()
        self.scene6_summary()

    # -- Scene 1: Hook -- Why Systems? --
    def scene1_hook(self):
        self.add_subcaption(
            "So far every differential equation we have solved involved "
            "a single unknown function. But in the real world, quantities "
            "interact with each other.",
            duration=18,
        )
        play_intro(self, "Systems of ODEs",
                   "Ordinary Differential Equations")

        title = self.ly.title("Why Systems?")
        self.wait(1)

        self.add_subcaption(
            "Imagine two tanks connected by pipes. The amount of salt in "
            "tank A depends on what flows in from tank B, and vice versa. "
            "We cannot solve them independently.",
            duration=18,
        )

        # Two-tank diagram
        tank_a_label = Text("Tank A", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        tank_b_label = Text("Tank B", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        tank_a_box = RoundedRectangle(
            corner_radius=0.15, width=2.0, height=1.4,
            stroke_color=PRIMARY, stroke_width=2,
            fill_color=BG, fill_opacity=0.8,
        )
        tank_b_box = RoundedRectangle(
            corner_radius=0.15, width=2.0, height=1.4,
            stroke_color=SECONDARY, stroke_width=2,
            fill_color=BG, fill_opacity=0.8,
        )
        tank_a_label.move_to(tank_a_box.get_center())
        tank_b_label.move_to(tank_b_box.get_center())
        tank_a = VGroup(tank_a_box, tank_a_label)
        tank_b = VGroup(tank_b_box, tank_b_label)

        tank_a.shift(LEFT * 2.5)
        tank_b.shift(RIGHT * 2.5)

        # Arrows between tanks
        arrow_ab = Arrow(
            tank_a.get_right(), tank_b.get_left(),
            buff=0.2, color=ACCENT, stroke_width=2,
            max_tip_length_to_length_ratio=0.15,
        )
        arrow_ba = Arrow(
            tank_b.get_left(), tank_a.get_right(),
            buff=0.2, color=RED, stroke_width=2,
            max_tip_length_to_length_ratio=0.15,
        )
        arrow_ba.shift(DOWN * 0.35)
        arrow_ab.shift(UP * 0.35)

        diagram = VGroup(tank_a, tank_b, arrow_ab, arrow_ba)
        self.ly.center_in_content(diagram)
        self.play(
            FadeIn(tank_a, shift=LEFT * 0.15),
            FadeIn(tank_b, shift=RIGHT * 0.15),
            run_time=NORMAL,
        )
        self.play(Create(arrow_ab), Create(arrow_ba), run_time=NORMAL)
        self.wait(2)

        self.add_subcaption(
            "Each tank's rate of change depends on the other tank. "
            "This gives us a system of coupled differential equations.",
            duration=16,
        )

        coupled = MathTex(
            r"x' = ax + by",
            r"\qquad",
            r"y' = cx + dy",
            font_size=HEADING_SIZE, color=WHITE,
        )
        coupled[0].set_color(PRIMARY)
        coupled[2].set_color(SECONDARY)
        self.ly.safe_place(coupled, DOWN, anchor=diagram, buff=0.5)
        self.play(Write(coupled), run_time=NORMAL)
        self.wait(2)

        self.add_subcaption(
            "We need a method that handles both equations at once. "
            "The answer: write the system as a matrix equation.",
            duration=16,
        )

        question = Text(
            "Can we solve both at once?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(question, DOWN, anchor=coupled, buff=0.3)
        self.wait(2)

        self.ly.clear()

    # -- Scene 2: From Equations to Matrices --
    def scene2_matrix_form(self):
        self.ly.section_divider(1, "Matrix Form")

        self.add_subcaption(
            "Let us write the coupled system in vector notation. "
            "Define the vector x as the column vector x, y. "
            "Then the derivative x prime is also a column vector.",
            duration=18,
        )

        title = self.ly.title("From Equations to Matrices")

        # Component form
        comp = MathTex(
            r"x' = ax + by",
            r", \quad",
            r"y' = cx + dy",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.play(Write(comp), run_time=NORMAL)
        self.ly.safe_place(comp, DOWN, anchor=title)
        self.wait(1)

        self.add_subcaption(
            "Let x be the vector x, y. Then the system becomes "
            "x prime equals the matrix A times x, where A is the "
            "coefficient matrix with entries a, b on the first row "
            "and c, d on the second row.",
            duration=22,
        )

        # Vector notation
        vec = MathTex(
            r"\vec{x}' = A\vec{x}",
            r", \quad",
            r"\vec{x} = \begin{bmatrix} x \\ y \end{bmatrix}",
            r", \quad",
            r"A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}",
            font_size=HEADING_SIZE,
        )
        vec[0].set_color(ACCENT)
        vec[1].set_color(DIM)
        vec[2].set_color(WHITE)
        vec[3].set_color(DIM)
        vec[4].set_color(PRIMARY)
        self.play(Transform(comp, vec), run_time=NORMAL)
        self.wait(2)

        self.add_subcaption(
            "This compact matrix form x prime equals A x hides all "
            "the structure. To solve it, we need to know how to "
            "exponentiate a matrix. The key: eigenvectors give us "
            "special directions where the system simplifies.",
            duration=20,
        )

        insight = Text(
            "Eigenvectors: special directions where A*x = lambda*x",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(insight, DOWN, anchor=vec, buff=0.3)
        self.wait(2)

        self.ly.clear()

    # -- Scene 3: The Eigenvalue Method --
    def scene3_eigenvalue_method(self):
        self.ly.section_divider(2, "The Eigenvalue Method")

        self.add_subcaption(
            "The eigenvalue method is the standard technique for "
            "solving linear systems of ODEs with constant coefficients. "
            "We assume the solution has a special exponential form.",
            duration=20,
        )

        title = self.ly.title("The Eigenvalue Method")

        # Assumption
        assumption = MathTex(
            r"\vec{x}(t)",
            r"=",
            r"e^{\lambda t}",
            r"\vec{v}",
            font_size=HEADING_SIZE,
        )
        assumption[2].set_color(ACCENT)
        self.play(Write(assumption), run_time=NORMAL)
        self.ly.safe_place(assumption, DOWN, anchor=title)
        self.wait(2)

        self.add_subcaption(
            "Substitute into x prime equals A x. The derivative of "
            "e to the lambda t times v is lambda e to the lambda t "
            "times v. So we get lambda e to the lambda t v equals "
            "A e to the lambda t v.",
            duration=22,
        )

        # Substitute
        subst = MathTex(
            r"\lambda e^{\lambda t}\vec{v}",
            r"=",
            r"A\,e^{\lambda t}\vec{v}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.play(Transform(assumption, subst), run_time=NORMAL)
        self.wait(1)

        self.add_subcaption(
            "Cancel the common factor e to the lambda t from both "
            "sides. This leaves us with A v equals lambda v.",
            duration=14,
        )

        # Cancel e^{lambda*t}
        cancel = MathTex(
            r"A\vec{v}",
            r"=",
            r"\lambda\vec{v}",
            font_size=HEADING_SIZE,
        )
        cancel[0].set_color(PRIMARY)
        cancel[2].set_color(ACCENT)
        self.play(Transform(subst, cancel), run_time=NORMAL)
        self.wait(2)

        # Box the eigenvalue equation
        box = SurroundingRectangle(
            cancel, color=ACCENT, buff=0.25,
            stroke_width=2, corner_radius=0.1,
        )
        self.play(Create(box), run_time=NORMAL)

        self.add_subcaption(
            "This is the eigenvalue equation! Lambda is an eigenvalue "
            "and v is an eigenvector of the matrix A.",
            duration=12,
        )

        label = Text(
            "The eigenvalue equation!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
            weight=BOLD,
        )
        self.play(FadeIn(label, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(label, DOWN, anchor=cancel, buff=0.3)
        self.wait(2)

        self.play(FadeOut(box), FadeOut(label), run_time=FAST)

        self.add_subcaption(
            "To find the eigenvalues, we solve the characteristic "
            "equation: the determinant of A minus lambda I equals "
            "zero. This gives a quadratic in lambda.",
            duration=18,
        )

        # Characteristic equation
        char_eq = MathTex(
            r"\det(A - \lambda I) = 0",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.play(Transform(cancel, char_eq), run_time=NORMAL)
        self.wait(2)

        self.add_subcaption(
            "For each eigenvalue, we find the corresponding eigenvector. "
            "Each pair gives one solution: e to the lambda t times v. "
            "The general solution is a linear combination of these.",
            duration=18,
        )

        gen_sol = MathTex(
            r"\vec{x}(t) = c_1\, e^{\lambda_1 t}\,\vec{v}_1",
            r"+",
            r"c_2\, e^{\lambda_2 t}\,\vec{v}_2",
            font_size=HEADING_SIZE,
        )
        gen_sol[0].set_color(PRIMARY)
        gen_sol[1].set_color(DIM)
        gen_sol[2].set_color(SECONDARY)
        self.play(Transform(char_eq, gen_sol), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # -- Scene 4: Worked Example -- Two Coupled Tanks --
    def scene4_worked_example(self):
        self.ly.section_divider(3, "Worked Example")

        self.add_subcaption(
            "Let us apply the eigenvalue method to a concrete system. "
            "Consider two tanks where x prime equals negative 3 x "
            "plus y, and y prime equals 2 x minus 4 y.",
            duration=20,
        )

        title = self.ly.title("Example: Two Coupled Tanks")

        # System
        system = MathTex(
            r"x' = -3x + y",
            r", \quad",
            r"y' = 2x - 4y",
            font_size=HEADING_SIZE, color=WHITE,
        )
        system[0].set_color(PRIMARY)
        system[2].set_color(SECONDARY)
        self.play(Write(system), run_time=NORMAL)
        self.ly.safe_place(system, DOWN, anchor=title)
        self.wait(2)

        self.add_subcaption(
            "In matrix form, x prime equals A x where A is the "
            "matrix with entries negative 3, 1 on the first row and "
            "2, negative 4 on the second row.",
            duration=16,
        )

        # Matrix
        mat = MathTex(
            r"\vec{x}' = \begin{bmatrix} -3 & 1 \\ 2 & -4 \end{bmatrix}\vec{x}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.play(Transform(system, mat), run_time=NORMAL)
        self.wait(2)

        # Step 1: Characteristic equation
        self.add_subcaption(
            "Step one: find the eigenvalues. The characteristic "
            "equation is the determinant of A minus lambda I. "
            "For our matrix, this gives lambda squared plus 7 "
            "lambda plus 10 equals zero.",
            duration=20,
        )

        step1 = Text(
            "Step 1: Find eigenvalues",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.play(FadeIn(step1, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(step1, DOWN, anchor=mat, buff=0.3)
        self.wait(1)

        char_eq = MathTex(
            r"\lambda^2 + 7\lambda + 10 = 0",
            r"\quad\Rightarrow\quad",
            r"(\lambda+2)(\lambda+5) = 0",
            font_size=HEADING_SIZE,
        )
        char_eq[0].set_color(WHITE)
        char_eq[2].set_color(ACCENT)
        self.play(Write(char_eq), run_time=NORMAL)
        self.ly.safe_place(char_eq, DOWN, anchor=step1, buff=0.3)
        self.wait(2)

        eigenvalues = MathTex(
            r"\lambda_1 = -2",
            r", \quad",
            r"\lambda_2 = -5",
            font_size=HEADING_SIZE,
        )
        eigenvalues[0].set_color(PRIMARY)
        eigenvalues[2].set_color(SECONDARY)
        self.play(Transform(char_eq, eigenvalues), run_time=NORMAL)
        self.wait(2)

        self.play(FadeOut(step1), run_time=FAST)

        # Step 2: Eigenvectors
        self.add_subcaption(
            "Step two: find the eigenvectors. For lambda 1 equals "
            "negative 2, we solve A plus 2 I times v equals zero. "
            "This gives the eigenvector v 1 equals 1, 1.",
            duration=20,
        )

        step2 = Text(
            "Step 2: Find eigenvectors",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.play(Transform(step1, step2), run_time=FAST)
        self.ly.safe_place(step2, DOWN, anchor=mat, buff=0.3)
        self.wait(1)

        eigvec1 = MathTex(
            r"\lambda_1 = -2:",
            r"\quad",
            r"\vec{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}",
            font_size=HEADING_SIZE,
        )
        eigvec1[0].set_color(PRIMARY)
        eigvec1[2].set_color(PRIMARY)
        self.play(Transform(eigenvalues, eigvec1), run_time=NORMAL)
        self.wait(2)

        self.add_subcaption(
            "For lambda 2 equals negative 5, we solve A plus 5 I "
            "times v equals zero. This gives the eigenvector "
            "v 2 equals 1, negative 2.",
            duration=18,
        )

        eigvec2 = MathTex(
            r"\lambda_2 = -5:",
            r"\quad",
            r"\vec{v}_2 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}",
            font_size=HEADING_SIZE,
        )
        eigvec2[0].set_color(SECONDARY)
        eigvec2[2].set_color(SECONDARY)
        self.play(Transform(eigvec1, eigvec2), run_time=NORMAL)
        self.wait(2)

        self.play(FadeOut(step2), run_time=FAST)

        # Step 3: General solution
        self.add_subcaption(
            "Step three: write the general solution as a linear "
            "combination. Both eigenvalues are negative, so every "
            "solution decays to zero over time.",
            duration=16,
        )

        step3 = Text(
            "Step 3: General solution",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.play(Transform(step2, step3), run_time=FAST)
        self.ly.safe_place(step3, DOWN, anchor=mat, buff=0.3)
        self.wait(1)

        general = MathTex(
            r"\vec{x}(t) = c_1 e^{-2t}\!\begin{bmatrix}1\\1\end{bmatrix}",
            r"+",
            r"c_2 e^{-5t}\!\begin{bmatrix}1\\-2\end{bmatrix}",
            font_size=HEADING_SIZE,
        )
        general[0].set_color(PRIMARY)
        general[1].set_color(DIM)
        general[2].set_color(SECONDARY)
        self.play(Transform(eigvec2, general), run_time=NORMAL)
        self.wait(2)

        self.add_subcaption(
            "Since both eigenvalues are negative, as t goes to "
            "infinity, both exponential terms go to zero. The "
            "system approaches the origin -- a stable equilibrium.",
            duration=16,
        )

        stable = Text(
            "Both eigenvalues negative -> stable node",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.play(FadeIn(stable, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(stable, DOWN, anchor=general, buff=0.3)
        self.wait(2)

        self.ly.clear()

    # -- Scene 5: Phase Plane Basics --
    def scene5_phase_plane(self):
        self.ly.section_divider(4, "The Phase Plane")

        self.add_subcaption(
            "Instead of plotting x and y against time, we can plot "
            "them against each other. This is called the phase plane. "
            "Each point represents a state of the system.",
            duration=20,
        )

        title = self.ly.title("Visualizing Solutions")

        # Phase plane axes
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5.5,
            y_length=5.5,
            background_line_style={
                "stroke_color": BG_LIGHT,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            },
            axis_config={
                "font_size": LABEL_SIZE,
                "color": DIM,
            },
            faded_line_style={
                "stroke_color": BG_LIGHT,
                "stroke_width": 0.5,
                "stroke_opacity": 0.3,
            },
        )
        self.ly.center_in_content(plane)

        x_label = MathTex("x", font_size=LABEL_SIZE, color=PRIMARY).next_to(
            plane.get_right(), RIGHT, buff=0.2
        )
        y_label = MathTex("y", font_size=LABEL_SIZE, color=SECONDARY).next_to(
            plane.get_top(), UP, buff=0.15
        )

        self.play(Create(plane), run_time=NORMAL)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=FAST)
        self.wait(1)

        # Eigenvector directions
        self.add_subcaption(
            "The eigenvectors give us special directions. "
            "Along v 1 equals 1, 1, the solution decays as "
            "e to the negative 2 t. Along v 2 equals 1, negative 2, "
            "it decays faster as e to the negative 5 t.",
            duration=22,
        )

        # Eigenvector v1 = [1,1] direction
        ev1_line = Line(
            plane.c2p(-2.5, -2.5), plane.c2p(2.5, 2.5),
            color=PRIMARY, stroke_width=2.5,
        )
        ev1_label = MathTex(
            r"\vec{v}_1", font_size=LABEL_SIZE, color=PRIMARY,
        ).next_to(plane.c2p(2.0, 2.0), RIGHT, buff=0.15)

        self.play(Create(ev1_line), run_time=NORMAL)
        self.play(Write(ev1_label), run_time=FAST)
        self.wait(1)

        # Eigenvector v2 = [1,-2] direction
        ev2_line = Line(
            plane.c2p(-1.5, 3.0), plane.c2p(1.5, -3.0),
            color=SECONDARY, stroke_width=2.5,
        )
        ev2_label = MathTex(
            r"\vec{v}_2", font_size=LABEL_SIZE, color=SECONDARY,
        ).next_to(plane.c2p(1.5, -3.0), RIGHT, buff=0.15)

        self.play(Create(ev2_line), run_time=NORMAL)
        self.play(Write(ev2_label), run_time=FAST)
        self.wait(2)

        # Origin dot
        origin_dot = Dot(plane.c2p(0, 0), color=WHITE, radius=0.06)
        self.play(FadeIn(origin_dot), run_time=FAST)
        self.wait(1)

        # Trajectories along eigenvector directions
        self.add_subcaption(
            "Solutions along the eigenvectors are straight lines. "
            "Other solutions are curves that are pulled toward the "
            "slower decaying eigenvector direction as t increases.",
            duration=18,
        )

        # Trajectories along eigenvector directions (static curves)
        self.add_subcaption(
            "Solutions along the eigenvectors are straight lines. "
            "Other solutions are curves that are pulled toward the "
            "slower decaying eigenvector direction as t increases.",
            duration=14,
        )

        # Pre-drawn trajectories instead of TracedPath
        tr1 = Line(
            plane.c2p(2.0, 2.0), plane.c2p(0.1, 0.1),
            color=PRIMARY, stroke_width=2,
        )
        dot1 = Dot(plane.c2p(0.1, 0.1), color=PRIMARY, radius=0.04)
        self.play(Create(tr1), FadeIn(dot1), run_time=1.5)
        self.wait(1)

        tr2 = Line(
            plane.c2p(-1.0, 2.0), plane.c2p(0.05, -0.1),
            color=SECONDARY, stroke_width=2,
        )
        dot2 = Dot(plane.c2p(0.05, -0.1), color=SECONDARY, radius=0.04)
        self.play(Create(tr2), FadeIn(dot2), run_time=1.2)
        self.wait(1)

        # Curved trajectory (general solution)
        self.add_subcaption(
            "A general solution is a combination of both eigenvectors. "
            "The trajectory curves toward the origin, asymptotically "
            "approaching the slower eigenvector direction.",
            duration=14,
        )

        # Pre-drawn curved trajectory using ParametricFunction
        def curved_traj(t_val):
            # x(t) = c1*e^{-2t} + c2*e^{-5t}, y(t) = c1*e^{-2t} - 2*c2*e^{-5t}
            c1, c2 = 1.0, 0.8
            x = c1 * np.exp(-2 * t_val) + c2 * np.exp(-5 * t_val)
            y = c1 * np.exp(-2 * t_val) - 2 * c2 * np.exp(-5 * t_val)
            return plane.c2p(x, y)

        tr3 = ParametricFunction(
            curved_traj, t_range=[0, 1.2],
            color=ACCENT, stroke_width=2,
        )
        dot3 = Dot(curved_traj(1.2), color=ACCENT, radius=0.04)
        self.play(Create(tr3), FadeIn(dot3), run_time=1.5)
        self.wait(1)

        # Classification
        self.add_subcaption(
            "Because both eigenvalues are negative, the origin is "
            "a stable node. All trajectories approach the origin. "
            "If eigenvalues had opposite signs, we would get a "
            "saddle point instead.",
            duration=20,
        )

        # Classification box
        class_text = Text(
            "Stable node: both eigenvalues < 0",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        box = SurroundingRectangle(
            class_text, color=ACCENT, buff=0.2,
            stroke_width=1.5, corner_radius=0.1,
        )
        class_group = VGroup(class_text, box)
        class_group.next_to(plane, DOWN, buff=0.4)

        self.play(Write(class_text), Create(box), run_time=NORMAL)
        self.wait(2)

        # Brief classification overview
        self.add_subcaption(
            "Other possibilities include unstable nodes when both "
            "eigenvalues are positive, saddle points when they have "
            "opposite signs, and spiral points when eigenvalues are "
            "complex. We will explore these in detail next.",
            duration=20,
        )

        classifications = VGroup(
            Text("Stable node", font_size=LABEL_SIZE, color=SECONDARY, font=SANS),
            Text("Unstable node", font_size=LABEL_SIZE, color=RED, font=SANS),
            Text("Saddle", font_size=LABEL_SIZE, color=ACCENT, font=SANS),
            Text("Spiral", font_size=LABEL_SIZE, color=PRIMARY, font=SANS),
        ).arrange(RIGHT, buff=0.8)
        classifications.next_to(class_group, DOWN, buff=0.3)

        self.play(FadeIn(classifications, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # -- Scene 6: Summary + Preview --
    def scene6_summary(self):
        self.add_subcaption(
            "Let us recap what we have learned about systems of "
            "ordinary differential equations.",
            duration=10,
        )

        title = self.ly.title("What We Learned")

        points1 = [
            Text(
                "1. Coupled systems: x' = Ax in matrix form",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(points1, start_from=title)
        self.wait(1)

        self.add_subcaption(
            "The eigenvalue method transforms the matrix system into "
            "a familiar eigenvalue problem.",
            duration=10,
        )

        points2 = [
            Text(
                "2. Eigenvalue method: det(A - lambda*I) = 0",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(points2, start_from=title)
        self.wait(1)

        self.add_subcaption(
            "Each eigenvalue-eigenvector pair gives one solution. "
            "The general solution combines them.",
            duration=10,
        )

        points3 = [
            Text(
                "3. General solution: sum of c_i * e^{lambda_i*t} * v_i",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(points3, start_from=title)
        self.wait(1)

        self.add_subcaption(
            "The phase plane visualizes all solutions as trajectories "
            "in the x-y plane, with eigenvectors giving the "
            "asymptotic directions.",
            duration=14,
        )

        points4 = [
            Text(
                "4. Phase plane: trajectories from eigenvector directions",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(points4, start_from=title)
        self.wait(2)

        self.ly.clear()

        self.add_subcaption(
            "Thank you for watching! In the next video, we will "
            "classify all equilibrium point types and draw complete "
            "phase portraits for any linear system.",
            duration=14,
        )

        play_outro(self, "Phase Portraits",
                   "Ordinary Differential Equations")