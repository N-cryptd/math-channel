"""Video 65: Phase Portraits
Ordinary Differential Equations -- Video 12 of 13

Covers: phase plane concept, vector fields, equilibrium points,
eigenvalue classification (node, saddle, spiral, center), nullclines,
worked example.

Competitive analysis: channel-analysis/improvements.md "2026-06-14 -- Phase Portraits"
Plan: planning/video-65-phase-portraits.md

Render draft:  manim -ql scripts/undergraduate/video-65-phase-portraits.py Video65_PhasePortraits
Render final:  manim -qh scripts/undergraduate/video-65-phase-portraits.py Video65_PhasePortraits
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


class Video65_PhasePortraits(Scene):
    """Full video: Phase Portraits -- phase plane, vector fields,
    equilibrium classification, nullclines."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_phase_plane()
        self.scene3_vector_fields()
        self.scene4_equilibria()
        self.scene5_classification()
        self.scene6_worked_example()
        self.scene7_nullclines()
        self.scene8_summary()

    # -- Scene 1: Hook -- Why Phase Portraits? --
    def scene1_hook(self):
        self.add_subcaption(
            "In the last video we saw how to write coupled ODEs in "
            "matrix form. But there is a completely different way to "
            "understand these systems, one that does not require "
            "solving anything at all.",
            duration=18,
        )
        play_intro(self, "Phase Portraits",
                   "Ordinary Differential Equations")

        title = self.ly.title("Why Phase Portraits?")
        self.wait(3)

        self.add_subcaption(
            "What if you could see the entire behavior of a system, "
            "every possible solution, in a single picture?",
            duration=14,
        )

        question = Text(
            "See every solution at a glance?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(question, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "That is exactly what a phase portrait does. It is a map "
            "of arrows showing where the system flows.",
            duration=14,
        )
        answer = Text(
            "A phase portrait: the map of all solutions.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(answer, DOWN, anchor=question, buff=0.3)
        self.play(FadeIn(answer, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # -- Scene 2: From Time Series to Phase Plane --
    def scene2_phase_plane(self):
        self.ly.section_divider(1, "The Phase Plane")

        self.add_subcaption(
            "Consider two coupled variables, x of t and y of t. "
            "We can plot each one versus time separately. But what "
            "if we plot them together?",
            duration=16,
        )

        title = self.ly.title("From Time Series to Phase Plane")

        # Show the coupled system
        system = MathTex(
            r"x' = -2x + y",
            r", \quad",
            r"y' = x - 2y",
            font_size=HEADING_SIZE, color=WHITE,
        )
        system[0].set_color(PRIMARY)
        system[2].set_color(SECONDARY)
        self.ly.safe_place(system, DOWN, anchor=title, buff=0.4)
        self.play(Write(system), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "Instead of two separate time plots, combine them into "
            "a single picture. The horizontal axis is x, the "
            "vertical axis is y, and each point represents a "
            "snapshot of the system at one instant.",
            duration=18,
        )

        # Axes for phase plane
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=4.5, y_length=4.5,
            axis_config={"color": DIM, "stroke_width": 1.5},
        )
        x_label = MathTex("x", font_size=LABEL_SIZE, color=PRIMARY)
        y_label = MathTex("y", font_size=LABEL_SIZE, color=SECONDARY)
        x_label.next_to(axes.x_axis.get_right(), RIGHT, buff=0.15)
        y_label.next_to(axes.y_axis.get_top(), UP, buff=0.15)

        self.ly.center_in_content(axes)
        self.ly.safe_place(x_label, DOWN, anchor=axes, buff=-0.3)
        self.ly.safe_place(y_label, DOWN, anchor=axes, buff=-0.3)

        self.play(FadeOut(system), run_time=FAST)
        self.play(
            FadeIn(axes, shift=LEFT * 0.15),
            FadeIn(x_label), FadeIn(y_label),
            run_time=NORMAL,
        )
        self.wait(3)

        self.add_subcaption(
            "As time advances, the point x, y traces out a curve. "
            "This curve is called a trajectory, or orbit.",
            duration=14,
        )

        # Draw a spiral trajectory (stable node -> inward spiral)
        traj_points = []
        for i in range(100):
            t = i * 0.08
            r = 2.5 * np.exp(-0.3 * t)
            theta = t * 1.5
            px = r * np.cos(theta)
            py = r * np.sin(theta)
            traj_points.append(axes.c2p(px, py))

        traj = VMobject(color=PRIMARY, stroke_width=2)
        traj.set_points_smoothly(traj_points)

        self.play(Create(traj), run_time=4 * NORMAL)
        self.wait(3)

        self.add_subcaption(
            "Each point on this curve is both coordinates at one "
            "moment in time. The whole picture is the phase plane, "
            "and the collection of all possible trajectories is "
            "the phase portrait.",
            duration=16,
        )

        traj_label = Text(
            "Trajectory = solution curve in (x, y) space",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(traj_label, DOWN, anchor=axes, buff=0.3)
        self.play(FadeIn(traj_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # -- Scene 3: Vector Fields --
    def scene3_vector_fields(self):
        self.ly.section_divider(2, "Vector Fields")

        self.add_subcaption(
            "A phase portrait is built from a vector field. At every "
            "point x, y, we draw an arrow showing the direction and "
            "speed of the system.",
            duration=16,
        )

        title = self.ly.title("Vector Fields: The Map")

        # The vector field formula
        vfield = MathTex(
            r"\vec{F}(x,y) = \langle f(x,y),\, g(x,y) \rangle",
            font_size=HEADING_SIZE, color=WHITE,
        )
        vfield[0].set_color(ACCENT)
        self.ly.safe_place(vfield, DOWN, anchor=title, buff=0.5)
        self.play(Write(vfield), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "The first component f gives the horizontal velocity, "
            "and the second component g gives the vertical velocity. "
            "Together they form an arrow at each point.",
            duration=16,
        )

        # Simple axes with a few arrows
        small_axes = Axes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1],
            x_length=3.5, y_length=3.5,
            axis_config={"color": DIM, "stroke_width": 1.5},
        )
        self.ly.center_in_content(small_axes)

        self.play(FadeOut(vfield), run_time=FAST)
        self.play(FadeIn(small_axes, shift=LEFT * 0.15), run_time=NORMAL)

        # Place a few representative arrows (pointing toward origin)
        arrow_positions = [
            (1.5, 1.0, -0.6, -0.4),
            (1.0, 1.5, -0.4, -0.6),
            (-1.5, -1.0, 0.6, 0.4),
            (-1.0, -1.5, 0.4, 0.6),
            (1.5, -1.0, -0.6, 0.4),
            (-1.5, 1.0, 0.6, -0.4),
            (0.0, 1.5, 0.0, -0.6),
            (0.0, -1.5, 0.0, 0.6),
            (1.5, 0.0, -0.6, 0.0),
            (-1.5, 0.0, 0.6, 0.0),
        ]

        arrows_list = []
        for (ax, ay, dx, dy) in arrow_positions:
            start = small_axes.c2p(ax, ay)
            end = small_axes.c2p(ax + dx, ay + dy)
            arr = Arrow(
                start, end, buff=0,
                color=SECONDARY, stroke_width=2,
                max_tip_length_to_length_ratio=0.25,
            )
            arrows_list.append(arr)

        arrow_group = VGroup(*arrows_list)

        self.add_subcaption(
            "Each arrow tells you: if the system is at this point, "
            "it moves in this direction. A solution curve simply "
            "follows the arrows, like a leaf on a river.",
            duration=16,
        )

        for arr in arrows_list:
            self.play(Create(arr), run_time=FAST)
        self.wait(4)

        # Origin equilibrium dot
        eq_dot = Dot(small_axes.c2p(0, 0), radius=0.06, color=ACCENT)
        eq_label = Text(
            "Equilibrium", font_size=LABEL_SIZE, color=ACCENT, font=SANS,
        )
        eq_label.next_to(eq_dot, DOWN + RIGHT, buff=0.15)

        self.play(FadeIn(eq_dot), run_time=FAST)
        self.play(FadeIn(eq_label), run_time=FAST)
        self.wait(3)

        self.ly.clear()

    # -- Scene 4: Equilibrium Points --
    def scene4_equilibria(self):
        self.ly.section_divider(3, "Equilibrium Points")

        self.add_subcaption(
            "Some points in the phase plane have no arrow at all. "
            "These are equilibrium points, where both derivatives "
            "are zero and the system stays at rest forever.",
            duration=16,
        )

        title = self.ly.title("Where Everything Stops")

        # Definition
        eq_def = MathTex(
            r"f(x^*, y^*) = 0",
            r", \quad",
            r"g(x^*, y^*) = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        eq_def[0].set_color(PRIMARY)
        eq_def[2].set_color(SECONDARY)
        self.ly.safe_place(eq_def, DOWN, anchor=title, buff=0.5)
        self.play(Write(eq_def), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "At an equilibrium point, the system does not move. "
            "If you start there, you stay there. The key question "
            "is: what happens to nearby trajectories?",
            duration=16,
        )

        items = [
            Text(
                "Start at equilibrium: stay forever",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Start nearby: approach or diverge?",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "This depends on the eigenvalues",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=eq_def)
        self.wait(4)

        self.ly.clear()

    # -- Scene 5: Classification --
    def scene5_classification(self):
        self.ly.section_divider(4, "Classifying Equilibria")

        self.add_subcaption(
            "The behavior near an equilibrium depends on the "
            "eigenvalues of the Jacobian matrix evaluated at "
            "that point.",
            duration=14,
        )

        title = self.ly.title("The Classification Table")

        # Jacobian
        jacobian = MathTex(
            r"J = \begin{pmatrix}"
            r"\partial f/\partial x & \partial f/\partial y \\"
            r"\partial g/\partial x & \partial g/\partial y"
            r"\end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(jacobian, DOWN, anchor=title, buff=0.4)
        self.play(Write(jacobian), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "The eigenvalues tell us what kind of equilibrium we have. "
            "If both eigenvalues are real and negative, trajectories "
            "approach from all directions: a stable node.",
            duration=18,
        )

        # Classification items (progressive reveal)
        self.play(FadeOut(jacobian), run_time=FAST)

        items = [
            Text(
                "Real, both negative  =  Stable Node",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Real, both positive  =  Unstable Node",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Real, opposite signs  =  Saddle Point",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Complex, Re < 0  =  Stable Spiral",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Complex, Re > 0  =  Unstable Spiral",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Complex, Re = 0  =  Center",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(6)

        self.ly.clear()

    # -- Scene 6: Worked Example --
    def scene6_worked_example(self):
        self.ly.section_divider(5, "Worked Example")

        self.add_subcaption(
            "Let us classify the equilibrium of a specific system. "
            "Consider x prime equals minus 2 x plus y, y prime "
            "equals x minus 2 y.",
            duration=16,
        )

        title = self.ly.title("Example: Stable Node")

        # The system
        system = MathTex(
            r"x' = -2x + y",
            r", \quad",
            r"y' = x - 2y",
            font_size=HEADING_SIZE, color=WHITE,
        )
        system[0].set_color(PRIMARY)
        system[2].set_color(SECONDARY)
        self.ly.safe_place(system, DOWN, anchor=title, buff=0.4)
        self.play(Write(system), run_time=NORMAL)
        self.wait(3)

        # Step 1: Equilibrium
        self.add_subcaption(
            "Setting both derivatives to zero gives x equals y and "
            "x minus 2 y equals zero, so the only equilibrium is "
            "at the origin.",
            duration=16,
        )

        step1 = Text(
            "Equilibrium: (0, 0)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(step1, DOWN, anchor=system, buff=0.3)
        self.play(FadeIn(step1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        # Step 2: Jacobian
        self.add_subcaption(
            "The Jacobian matrix is the constant matrix of "
            "coefficients: minus 2, 1, 1, minus 2.",
            duration=12,
        )

        step2 = MathTex(
            r"J = \begin{pmatrix} -2 & 1 \\ 1 & -2 \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(step2, DOWN, anchor=step1, buff=0.3)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(4)

        # Step 3: Eigenvalues
        self.add_subcaption(
            "The characteristic equation is lambda squared plus "
            "4 lambda plus 3 equals zero. Factoring gives "
            "lambda plus 1 times lambda plus 3 equals zero.",
            duration=16,
        )

        step3 = MathTex(
            r"\lambda^2 + 4\lambda + 3 = 0",
            r" \Rightarrow ",
            r"\lambda_1 = -1, \; \lambda_2 = -3",
            font_size=HEADING_SIZE, color=WHITE,
        )
        step3[0].set_color(DIM)
        step3[2].set_color(ACCENT)
        self.ly.safe_place(step3, DOWN, anchor=step2, buff=0.3)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(4)

        # Step 4: Classification
        self.add_subcaption(
            "Both eigenvalues are real and negative. The equilibrium "
            "at the origin is a stable node. All trajectories "
            "converge to the origin.",
            duration=16,
        )

        result = Text(
            "Both real, both negative = Stable Node",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(result, DOWN, anchor=step3, buff=0.3)
        self.play(FadeIn(result, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # -- Scene 7: Nullclines --
    def scene7_nullclines(self):
        self.ly.section_divider(6, "Nullclines")

        self.add_subcaption(
            "There is a shortcut for sketching phase portraits "
            "without computing eigenvalues: nullclines.",
            duration=12,
        )

        title = self.ly.title("Nullclines: Reading the Landscape")

        items = [
            Text(
                "x-nullcline: where dx/dt = 0  (vertical arrows)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "y-nullcline: where dy/dt = 0  (horizontal arrows)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Intersections = equilibrium points",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Divide the plane into regions with arrow directions",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4)

        self.add_subcaption(
            "For our example, x prime equals zero when y equals "
            "2 x, a straight line. And y prime equals zero when "
            "x equals 2 y, another straight line. They cross "
            "at the origin, confirming our equilibrium.",
            duration=20,
        )

        example = MathTex(
            r"x'\!=\!0 \Rightarrow y=2x",
            r", \quad",
            r"y'\!=\!0 \Rightarrow x=2y",
            font_size=HEADING_SIZE, color=WHITE,
        )
        example[0].set_color(PRIMARY)
        example[2].set_color(SECONDARY)
        self.ly.safe_place(example, DOWN, anchor=items[-1], buff=0.3)
        self.play(Write(example), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # -- Scene 8: Summary --
    def scene8_summary(self):
        self.add_subcaption(
            "Phase portraits give us a complete picture of a system's "
            "behavior without solving any equations analytically.",
            duration=14,
        )

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "1. Phase plane: (x, y) space for trajectories",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. Vector field: arrows show flow direction",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3. Equilibria: where the flow stops",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "4. Eigenvalues classify equilibrium type",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "5. Nullclines help sketch without eigenvalues",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(6)

        self.ly.clear()
        play_outro(
            self,
            "Numerical Methods (Euler, RK4)",
            "Ordinary Differential Equations",
        )
