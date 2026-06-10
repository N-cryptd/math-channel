"""
Video 55: What is a Differential Equation?
Ordinary Differential Equations -- Video 1 of 1 (Course Opener)

Covers: introduction via population growth, definition of DEs, ODE vs PDE,
classification by order and linearity, slope field visualization as the
central visual metaphor, real-world examples (falling, spring, logistic),
and course preview.

Render draft:  manim -ql scripts/undergraduate/video-55-what-is-a-differential-equation.py Video55_WhatIsADifferentialEquation
Render final:  manim -qh scripts/undergraduate/video-55-what-is-a-differential-equation.py Video55_WhatIsADifferentialEquation
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


class Video55_WhatIsADifferentialEquation(Scene):
    """Full video: What is a Differential Equation? -- ODE course opener."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_classification()
        self.scene4_slope_field()
        self.scene5_physical_examples()
        self.scene6_course_preview()

    # ── Scene 1: Hook — Population Growth ────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Imagine you're tracking a population of bacteria in a petri dish. "
            "You start with 500 bacteria, and every hour the population doubles. "
            "After a few hours you have thousands. But what exactly is the "
            "relationship between the population and its rate of change?",
            duration=24,
        )
        play_intro(self, "What is a Differential Equation?",
                   "Ordinary Differential Equations")

        title = self.ly.title("A Simple Question")

        # Population numbers growing
        pop_items = [
            Text(
                "t = 0:  500 bacteria",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "t = 1:  1,000 bacteria",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "t = 2:  2,000 bacteria",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "t = 3:  4,000 bacteria ...",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(pop_items, start_from=title)
        self.wait(1.5)

        self.ly.clear()

        self.add_subcaption(
            "The key insight is that the rate of change of the population "
            "depends on the population itself. More bacteria means faster growth. "
            "This gives us our first differential equation: dN over dt "
            "equals r times N, where r is the growth rate.",
            duration=20,
        )

        title2 = self.ly.title("The Rate Depends on the Value")

        # N(t) notation
        n_func = MathTex(
            r"N(t)", r"=", r"\text{population at time } t",
            font_size=HEADING_SIZE, color=WHITE,
        )
        n_func[0].set_color(PRIMARY)
        self.ly.safe_place(n_func, DOWN, anchor=title2, buff=0.5)
        self.play(Write(n_func), run_time=NORMAL)
        self.wait(1)

        # The DE
        self.play(FadeOut(n_func), run_time=FAST)

        question = Text(
            "What is dN/dt?",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(question)
        self.play(FadeIn(question, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1)

        # The differential equation
        de = MathTex(
            r"\frac{dN}{dt}", r"=", r"rN",
            font_size=TITLE_SIZE, color=WHITE,
        )
        de[0].set_color(PRIMARY)
        de[2].set_color(ACCENT)
        self.ly.center_in_content(de)
        self.play(Transform(question, de), run_time=SLOW)
        self.wait(1)

        # Label
        label = Text(
            "Your first differential equation!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(label, DOWN, anchor=de, buff=0.5)
        self.play(FadeIn(label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 2: Definition — What is a DE? ────────────────────────
    def scene2_definition(self):
        self.add_subcaption(
            "A differential equation is simply an equation that involves "
            "derivatives of an unknown function. The unknown is not a number, "
            "but a function itself. In our example, N of t was the unknown "
            "function, and the equation told us something about its derivative.",
            duration=24,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("What is a Differential Equation?")

        # Formal definition
        defn = MathTex(
            r"\text{An equation involving derivatives}",
            r"\text{ of an unknown function } y(x)",
            font_size=BODY_SIZE, color=WHITE,
        )
        defn[0].set_color(PRIMARY)
        defn[1].set_color(SECONDARY)
        self.ly.safe_place(defn, DOWN, anchor=title, buff=0.5)
        ensure_fits(defn)
        self.play(Write(defn), run_time=SLOW)
        self.wait(1.5)

        self.play(FadeOut(defn), run_time=FAST)

        self.add_subcaption(
            "If the derivatives are with respect to a single variable, "
            "we call it an ordinary differential equation, or ODE. If they "
            "involve partial derivatives with respect to multiple variables, "
            "it's a partial differential equation, or PDE. This course "
            "focuses on ODEs.",
            duration=24,
        )

        # ODE vs PDE
        ode_label = Text(
            "ODE: derivatives w.r.t. ONE variable",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        pde_label = Text(
            "PDE: partial derivatives w.r.t. MULTIPLE variables",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )

        left_items = [ode_label]
        right_items = [pde_label]

        left_group, right_group = self.ly.two_columns(
            left_items, right_items, start_from=title,
        )
        self.play(
            FadeIn(left_group, shift=LEFT * 0.15),
            FadeIn(right_group, shift=RIGHT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1.5)

        # Notation
        self.ly.clear()
        title2 = self.ly.title("Notation")

        notations = [
            Text(
                "y'  (prime notation)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "dy/dx  (Leibniz notation)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "y''  (second derivative)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(notations, start_from=title2)
        self.wait(1)

        # Key insight
        self.ly.clear()
        title3 = self.ly.title("The Key Idea")

        key = Text(
            "The unknown is a FUNCTION, not a number.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(key)
        self.play(FadeIn(key, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 3: Classification — Order and Linearity ──────────────
    def scene3_classification(self):
        self.add_subcaption(
            "We classify differential equations by two key properties. "
            "The order is the highest derivative that appears. A first-order "
            "equation involves only the first derivative. A second-order "
            "equation involves the second derivative or higher.",
            duration=24,
        )
        self.ly.section_divider(2, "Classification")

        title = self.ly.title("Order: Highest Derivative Present")

        # Order examples
        order_items = [
            Text(
                "1st order:  dy/dx = f(x, y)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2nd order:  d\u00b2y/dx\u00b2 = f(x, y, dy/dx)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3rd order:  d\u00b3y/dx\u00b3 + y = 0",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(order_items, start_from=title)
        self.wait(1.5)

        self.ly.clear()

        self.add_subcaption(
            "Linearity is the second classification. A differential equation "
            "is linear if the unknown function and its derivatives appear only "
            "to the first power, and are not multiplied together. If the "
            "equation has terms like y squared or y times dy/dx, it's "
            "nonlinear.",
            duration=24,
        )

        title2 = self.ly.title("Linearity")

        # Linear example
        lin_label = Text(
            "Linear:",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(lin_label, DOWN, anchor=title2, buff=0.4)
        self.play(FadeIn(lin_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        lin_eq = MathTex(
            r"\frac{d^2 y}{dx^2}",
            r"+ 3 \frac{dy}{dx}",
            r"+ 2y",
            r"= \sin(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        lin_eq[0].set_color(PRIMARY)
        lin_eq[1].set_color(PRIMARY)
        lin_eq[2].set_color(PRIMARY)
        lin_eq[3].set_color(ACCENT)
        self.ly.safe_place(lin_eq, DOWN, anchor=lin_label, buff=0.4)
        ensure_fits(lin_eq)
        self.play(Write(lin_eq), run_time=SLOW)
        self.wait(1.5)

        # Transition
        self.play(FadeOut(lin_label), FadeOut(lin_eq), run_time=FAST)

        # Nonlinear example
        nlin_label = Text(
            "Nonlinear:",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(nlin_label, DOWN, anchor=title2, buff=0.4)
        self.play(FadeIn(nlin_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        nlin_eq = MathTex(
            r"\frac{dy}{dx}", r"=", r"y^2",
            font_size=HEADING_SIZE, color=WHITE,
        )
        nlin_eq[0].set_color(PRIMARY)
        nlin_eq[2].set_color(RED)
        self.ly.safe_place(nlin_eq, DOWN, anchor=nlin_label, buff=0.4)
        self.play(Write(nlin_eq), run_time=SLOW)
        self.wait(0.5)

        # Why nonlinear
        why = Text(
            "The y\u00b2 makes it nonlinear",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(why, DOWN, anchor=nlin_eq, buff=0.4)
        self.play(FadeIn(why, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 4: Visual — Slope Fields ──────────────────────────────
    def scene4_slope_field(self):
        self.add_subcaption(
            "One of the most powerful ways to understand differential equations "
            "is through slope fields. At every point in the xy plane, the "
            "equation tells us the slope of a solution passing through that "
            "point. We draw a short line segment with that slope, creating "
            "a field of tiny slopes.",
            duration=24,
        )
        self.ly.section_divider(3, "Slope Fields")

        title = self.ly.title("Visualizing a First-Order ODE")

        # The DE we'll visualize
        de_text = MathTex(
            r"\frac{dy}{dx}", r"=", r"x",
            font_size=HEADING_SIZE, color=WHITE,
        )
        de_text[0].set_color(PRIMARY)
        de_text[2].set_color(ACCENT)
        self.ly.safe_place(de_text, DOWN, anchor=title, buff=0.5)
        self.play(Write(de_text), run_time=NORMAL)
        self.wait(1)

        self.add_subcaption(
            "At each point x, y in the plane, the slope of a solution "
            "equals x. So when x is positive, slopes point upward. When x "
            "is negative, slopes point downward. Along the y-axis, slopes "
            "are zero, perfectly flat.",
            duration=24,
        )

        self.play(FadeOut(de_text), run_time=FAST)

        # Draw axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=5,
            color=DIM,
            stroke_width=1.5,
            axis_config={"include_numbers": False},
        )
        axes.move_to(ORIGIN)
        self.ly.center_in_content(axes)
        self.play(Create(axes), run_time=SLOW)
        self.wait(0.5)

        # Draw slope field segments for dy/dx = x
        slope_segments = VGroup()
        for xi in range(-3, 4):
            for yi in range(-3, 4):
                x_val = xi
                slope = x_val * 0.3  # scaled for visual
                length = 0.2
                x_pos = axes.c2p(x_val, yi)[0]
                y_pos = axes.c2p(x_val, yi)[1]
                # Line segment centered at (x_pos, y_pos) with given slope
                dx = length / 2
                dy = slope * dx
                start = np.array([x_pos - dx, y_pos - dy, 0])
                end = np.array([x_pos + dx, y_pos + dy, 0])
                seg = Line(start, end, color=SECONDARY, stroke_width=1.5)
                slope_segments.add(seg)

        self.play(
            *[FadeIn(seg, run_time=0.02) for seg in slope_segments],
            run_time=2,
            lag_ratio=0.01,
        )
        self.wait(1)

        self.add_subcaption(
            "A solution curve is a path that follows these slopes at every "
            "point. Think of it like a river current. The slope field defines "
            "the terrain, and solution curves are paths flowing through it. "
            "Different starting points give different solution curves.",
            duration=24,
        )

        # Overlay a solution curve (y = x^2/2 + C, using C=0)
        curve_points = [
            axes.c2p(x, x * x / 2) for x in
            [i / 10 for i in range(-25, 26)]
        ]
        solution_curve = VMobject()
        solution_curve.set_points_smoothly(curve_points)
        solution_curve.set_color(PRIMARY)
        solution_curve.set_stroke(width=3)

        self.play(Create(solution_curve), run_time=SLOW)
        self.wait(1)

        # Another solution curve shifted up
        curve_points_2 = [
            axes.c2p(x, x * x / 2 + 2) for x in
            [i / 10 for i in range(-25, 26)]
        ]
        solution_curve_2 = VMobject()
        solution_curve_2.set_points_smoothly(curve_points_2)
        solution_curve_2.set_color(ACCENT)
        solution_curve_2.set_stroke(width=3)

        self.play(Create(solution_curve_2), run_time=SLOW)
        self.wait(1)

        # Insight text
        insight = Text(
            "Different starting points = different curves",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        insight.move_to(UP * (self.ly.content_bottom + 0.5))
        clamp_position(insight)
        self.play(FadeIn(insight, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 5: Physical Examples — Why DEs Matter ────────────────
    def scene5_physical_examples(self):
        self.add_subcaption(
            "Differential equations appear everywhere in science and "
            "engineering. Newton's second law gives us the equation for a "
            "falling object. Hooke's law describes a spring-mass system. "
            "And the logistic equation models population growth with a "
            "carrying capacity.",
            duration=24,
        )
        self.ly.section_divider(4, "Real-World DEs")

        title = self.ly.title("Differential Equations Everywhere")

        # Example 1: Falling
        ex1_label = Text(
            "Falling object (Newton's 2nd Law):",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(ex1_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(ex1_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        ex1_eq = MathTex(
            r"\frac{d^2 y}{dt^2}", r"=", r"-g",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ex1_eq[0].set_color(PRIMARY)
        ex1_eq[2].set_color(ACCENT)
        self.ly.safe_place(ex1_eq, DOWN, anchor=ex1_label, buff=0.3)
        ensure_fits(ex1_eq)
        self.play(Write(ex1_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ex1_label), FadeOut(ex1_eq), run_time=FAST)

        # Example 2: Spring
        ex2_label = Text(
            "Spring-mass system (Hooke's Law):",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(ex2_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(ex2_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        ex2_eq = MathTex(
            r"m \frac{d^2 x}{dt^2}", r"+", r"kx", r"= 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ex2_eq[0].set_color(PRIMARY)
        ex2_eq[2].set_color(ACCENT)
        self.ly.safe_place(ex2_eq, DOWN, anchor=ex2_label, buff=0.3)
        ensure_fits(ex2_eq)
        self.play(Write(ex2_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(ex2_label), FadeOut(ex2_eq), run_time=FAST)

        # Example 3: Logistic growth
        ex3_label = Text(
            "Logistic growth (with carrying capacity):",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(ex3_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(ex3_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        ex3_eq = MathTex(
            r"\frac{dP}{dt}", r"=", r"rP",
            r"\left(1 - \frac{P}{K}\right)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ex3_eq[0].set_color(PRIMARY)
        ex3_eq[2].set_color(ACCENT)
        ex3_eq[3].set_color(SECONDARY)
        self.ly.safe_place(ex3_eq, DOWN, anchor=ex3_label, buff=0.3)
        ensure_fits(ex3_eq)
        self.play(Write(ex3_eq), run_time=NORMAL)
        self.wait(1)

        self.ly.clear()

        # Summary
        title2 = self.ly.title("Same Concept, Different Applications")
        summary = Text(
            "All of these are ordinary differential equations.",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(summary)
        self.play(FadeIn(summary, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 6: Course Preview + Summary ──────────────────────────
    def scene6_course_preview(self):
        self.add_subcaption(
            "In this course, we'll learn to solve and understand "
            "differential equations. We'll cover separable equations, "
            "first-order linear equations, second-order equations with "
            "constant coefficients, Laplace transforms, and systems of "
            "equations with phase portraits.",
            duration=24,
        )

        title = self.ly.title("In This Course")

        items = [
            Text(
                "Separable equations",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "First-order linear equations",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Second-order constant coefficients",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Laplace transforms",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Systems and phase portraits",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        self.ly.clear()

        self.add_subcaption(
            "The central theme of differential equations is this: they "
            "describe how things change, not just what they are. Where "
            "regular algebra gives you a number, differential equations "
            "give you a function, a story about how a system evolves over "
            "time.",
            duration=24,
        )

        # Final insight
        final_title = self.ly.title("The Big Picture")

        final = Text(
            "DEs describe HOW things change,",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(final)
        self.play(FadeIn(final, shift=UP * 0.15), run_time=NORMAL)
        self.wait(0.5)

        final2 = Text(
            "not just WHAT they are.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(final2, DOWN, anchor=final, buff=0.3)
        self.play(FadeIn(final2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        play_outro(
            self,
            next_video="Separable Equations",
            next_playlist="ODE",
        )
