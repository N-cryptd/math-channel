"""Video 66: Numerical Methods (Euler, RK4)
Ordinary Differential Equations -- Video 13 of 13

Covers: why numerical methods, Euler's method, error analysis,
improved Euler (Heun's), RK4, comparison.

Competitive analysis: channel-analysis/improvements.md "2026-06-14 -- Numerical Methods"
Plan: planning/video-66-numerical-methods.md

Render draft:  manim -ql scripts/undergraduate/video-66-numerical-methods.py Video66_NumericalMethods
Render final:  manim -qh scripts/undergraduate/video-66-numerical-methods.py Video66_NumericalMethods
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


class Video66_NumericalMethods(Scene):
    """Full video: Numerical Methods -- Euler, improved Euler, RK4."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_euler_method()
        self.scene3_euler_error()
        self.scene4_improved_euler()
        self.scene5_rk4()
        self.scene6_comparison()
        self.scene7_summary()

    # -- Scene 1: Hook --
    def scene1_hook(self):
        self.add_subcaption(
            "Most differential equations cannot be solved analytically. "
            "The Laplace transform works for linear equations with "
            "constant coefficients, but real-world problems are often "
            "nonlinear. We need a different approach.",
            duration=18,
        )
        play_intro(self, "Numerical Methods",
                   "Ordinary Differential Equations")

        title = self.ly.title("Why Numerical Methods?")
        self.wait(3)

        self.add_subcaption(
            "Consider dy dx equals sine of x squared. This has no "
            "closed-form solution. We cannot write y as a function "
            "of x using elementary functions.",
            duration=16,
        )

        # Motivating example: no closed form
        problem = MathTex(
            r"\frac{dy}{dx} = \sin(x^2)",
            r", \quad y(0) = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        problem[0].set_color(RED)
        self.ly.safe_place(problem, DOWN, anchor=title, buff=0.5)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "Instead of solving, we approximate the solution step "
            "by step. At each point, we compute the slope and take "
            "a small step in that direction.",
            duration=16,
        )

        idea = Text(
            "Step forward using the slope at each point",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(idea, DOWN, anchor=problem, buff=0.3)
        self.play(FadeIn(idea, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # -- Scene 2: Euler's Method --
    def scene2_euler_method(self):
        self.ly.section_divider(1, "Euler's Method")

        self.add_subcaption(
            "Euler's method is the simplest numerical approach. At "
            "each point, we follow the tangent line for a small "
            "step of size h.",
            duration=16,
        )

        title = self.ly.title("Euler's Method: Follow the Tangent")

        # The formula
        formula = MathTex(
            r"y_{n+1} = y_n + h \cdot f(x_n, y_n)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=title, buff=0.5)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "Here y sub n is the current value, h is the step size, "
            "and f of x sub n, y sub n gives the slope of the "
            "tangent line at the current point.",
            duration=16,
        )

        items = [
            Text(
                "y_n = current approximation",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "h = step size (small)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "f(x_n, y_n) = slope from the ODE",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=formula)
        self.wait(4)

        self.add_subcaption(
            "Geometrically, Euler's method draws a straight line from "
            "the current point in the direction of the tangent. "
            "At the new point, we compute a new tangent and repeat.",
            duration=16,
        )

        self.ly.clear()

        # Sub-scene: Visual stepping
        self.add_subcaption(
            "Let us visualize this. Starting at x zero, we compute "
            "the slope, take a step, and repeat.",
            duration=12,
        )

        # Create a smooth curve (true solution)
        axes = Axes(
            x_range=[0, 3, 0.5], y_range=[0, 3, 0.5],
            x_length=6, y_length=4,
            axis_config={"color": DIM, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)

        # True solution: approximately y = 1 - cos(x) (for dy/dx = sin(x))
        true_points = []
        for i in range(100):
            t = i * 0.03
            px = t
            py = 1 - np.cos(t)
            true_points.append(axes.c2p(px, py))

        true_curve = VMobject(color=PRIMARY, stroke_width=2.5)
        true_curve.set_points_smoothly(true_points)

        x_label = MathTex("x", font_size=LABEL_SIZE, color=WHITE)
        y_label = MathTex("y", font_size=LABEL_SIZE, color=WHITE)
        x_label.next_to(axes.x_axis.get_right(), RIGHT, buff=0.1)
        y_label.next_to(axes.y_axis.get_top(), UP, buff=0.1)

        self.play(
            FadeIn(axes), FadeIn(x_label), FadeIn(y_label),
            run_time=NORMAL,
        )
        self.play(Create(true_curve), run_time=2 * NORMAL)
        self.wait(2)

        # Euler steps: dy/dx = sin(x), y(0) = 0, h = 0.7
        euler_steps = []
        x_curr, y_curr = 0.0, 0.0
        h = 0.7
        for step in range(4):
            x_next = x_curr + h
            slope = np.sin(x_curr)
            y_next = y_curr + h * slope
            start_p = axes.c2p(x_curr, y_curr)
            end_p = axes.c2p(x_next, y_next)
            seg = Line(start_p, end_p, color=RED, stroke_width=2)
            euler_steps.append(seg)
            x_curr, y_curr = x_next, y_next

        for seg in euler_steps:
            self.play(Create(seg), run_time=NORMAL)
        self.wait(3)

        legend_e = Text(
            "Blue = true,  Red = Euler",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(legend_e, DOWN, anchor=axes, buff=0.2)
        self.play(FadeIn(legend_e), run_time=FAST)
        self.wait(3)

        self.ly.clear()

    # -- Scene 3: Error in Euler's Method --
    def scene3_euler_error(self):
        self.ly.section_divider(2, "Error Analysis")

        self.add_subcaption(
            "Euler's method has a problem. Each step introduces error, "
            "and the errors accumulate over many steps. The method "
            "is first-order accurate.",
            duration=16,
        )

        title = self.ly.title("Error in Euler's Method")

        items = [
            Text(
                "Local error per step: proportional to h squared",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Global error over interval: proportional to h",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "First-order: halving step halves the error",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Convergence is slow for high accuracy",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(6)

        self.add_subcaption(
            "We can do better. Instead of using just one slope "
            "evaluation per step, what if we evaluate the slope "
            "at both ends and average?",
            duration=14,
        )

        question = Text(
            "Can we be smarter about choosing the slope?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(question, DOWN, anchor=items[-1], buff=0.3)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # -- Scene 4: Improved Euler (Heun's Method) --
    def scene4_improved_euler(self):
        self.ly.section_divider(3, "Improved Euler (Heun's Method)")

        self.add_subcaption(
            "The improved Euler method evaluates the slope twice per "
            "step. First at the start, then at a predicted endpoint, "
            "and averages the two slopes.",
            duration=16,
        )

        title = self.ly.title("Improved Euler: Average the Slopes")

        # Predictor step
        self.add_subcaption(
            "Step one: the predictor. Compute the slope at the "
            "current point and take a trial step.",
            duration=12,
        )

        k1 = MathTex(
            r"k_1 = f(x_n, y_n)",
            r", \quad",
            r"\tilde{y} = y_n + h \cdot k_1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        k1[0].set_color(PRIMARY)
        k1[2].set_color(DIM)
        self.ly.safe_place(k1, DOWN, anchor=title, buff=0.4)
        self.play(Write(k1), run_time=NORMAL)
        self.wait(3)

        # Corrector step
        self.add_subcaption(
            "Step two: the corrector. Evaluate the slope at the "
            "predicted point and average with the first slope.",
            duration=14,
        )

        k2 = MathTex(
            r"k_2 = f(x_n + h, \tilde{y})",
            r", \quad",
            r"y_{n+1} = y_n + \frac{h}{2}(k_1 + k_2)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        k2[0].set_color(SECONDARY)
        k2[2].set_color(ACCENT)
        self.ly.safe_place(k2, DOWN, anchor=k1, buff=0.3)
        self.play(Write(k2), run_time=NORMAL)
        self.wait(4)

        # Result
        self.add_subcaption(
            "This averaging makes the method second-order accurate. "
            "The global error is now proportional to h squared, "
            "which converges much faster than Euler.",
            duration=16,
        )

        result = Text(
            "Second-order: O(h^2) global error",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(result, DOWN, anchor=k2, buff=0.3)
        self.play(FadeIn(result, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # -- Scene 5: RK4 --
    def scene5_rk4(self):
        self.ly.section_divider(4, "RK4: The Gold Standard")

        self.add_subcaption(
            "The Runge-Kutta fourth order method, or RK4, takes this "
            "idea further. It evaluates the slope four times per "
            "step at strategically chosen points.",
            duration=16,
        )

        title = self.ly.title("Runge-Kutta 4th Order")

        # Four slopes (show them progressively)
        self.add_subcaption(
            "The first slope is the slope at the current point. "
            "The second and third slopes are evaluated at the "
            "midpoint using the first and second slopes respectively.",
            duration=16,
        )

        slopes = MathTex(
            r"k_1 = f(x_n, y_n)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(slopes, DOWN, anchor=title, buff=0.4)
        self.play(Write(slopes), run_time=NORMAL)
        self.wait(3)

        slopes2 = MathTex(
            r"k_2 = f(x_n + \tfrac{h}{2},\; y_n + \tfrac{h}{2}k_1)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(slopes2, DOWN, anchor=slopes, buff=0.3)
        self.play(Write(slopes2), run_time=NORMAL)
        self.wait(3)

        slopes3 = MathTex(
            r"k_3 = f(x_n + \tfrac{h}{2},\; y_n + \tfrac{h}{2}k_2)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(slopes3, DOWN, anchor=slopes2, buff=0.3)
        self.play(Write(slopes3), run_time=NORMAL)
        self.wait(3)

        self.add_subcaption(
            "The fourth slope is evaluated at the predicted endpoint "
            "using the third slope.",
            duration=10,
        )

        slopes4 = MathTex(
            r"k_4 = f(x_n + h,\; y_n + h \cdot k_3)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(slopes4, DOWN, anchor=slopes3, buff=0.3)
        self.play(Write(slopes4), run_time=NORMAL)
        self.wait(3)

        # Final formula
        self.add_subcaption(
            "The update formula combines all four slopes with "
            "weights 1, 2, 2, 1 divided by 6. These weights come "
            "from matching Taylor expansion coefficients up to "
            "fourth order.",
            duration=18,
        )

        # Remove old slopes to make room
        self.play(
            FadeOut(slopes), FadeOut(slopes2),
            FadeOut(slopes3), FadeOut(slopes4),
            run_time=FAST,
        )

        final = MathTex(
            r"y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        final.set_color_by_tex(r"k_1", PRIMARY)
        final.set_color_by_tex(r"k_2", SECONDARY)
        final.set_color_by_tex(r"k_3", SECONDARY)
        final.set_color_by_tex(r"k_4", ACCENT)
        self.ly.safe_place(final, DOWN, anchor=title, buff=0.5)
        self.play(Write(final), run_time=NORMAL)
        self.wait(5)

        # Result
        self.add_subcaption(
            "RK4 is fourth-order accurate. The global error is "
            "proportional to h to the fourth. This is the "
            "workhorse method used in most ODE solvers today.",
            duration=16,
        )

        result = Text(
            "Fourth-order: O(h^4) global error",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(result, DOWN, anchor=final, buff=0.3)
        self.play(FadeIn(result, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # -- Scene 6: Comparison --
    def scene6_comparison(self):
        self.ly.section_divider(5, "Method Comparison")

        self.add_subcaption(
            "Let us compare the three methods side by side.",
            duration=8,
        )

        title = self.ly.title("Comparison Table")

        items = [
            Text(
                "Euler:        O(h) error,    1 evaluation/step",
                font_size=BODY_SIZE, color=RED, font=MONO,
            ),
            Text(
                "Improved Euler: O(h^2) error, 2 evaluations/step",
                font_size=BODY_SIZE, color=SECONDARY, font=MONO,
            ),
            Text(
                "RK4:              O(h^4) error, 4 evaluations/step",
                font_size=BODY_SIZE, color=ACCENT, font=MONO,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)

        self.add_subcaption(
            "RK4 is four times more work per step, but it is so much "
            "more accurate that you can use much larger step sizes "
            "and still get better results than Euler with tiny steps.",
            duration=16,
        )

        insight = Text(
            "In practice: use RK4 or adaptive methods like ode45",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=items[-1], buff=0.3)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # -- Scene 7: Summary --
    def scene7_summary(self):
        self.add_subcaption(
            "Numerical methods let us solve any differential equation, "
            "even when no closed-form solution exists.",
            duration=12,
        )

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "1. Euler: follow the tangent, simple but slow",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "2. Error accumulates: Euler is first-order",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "3. Improved Euler: average slopes, second-order",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "4. RK4: four evaluations, fourth-order standard",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "5. In practice: use adaptive methods (ode45)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(6)

        self.ly.clear()
        play_outro(
            self,
            "Probability & Statistics",
            "Next Playlist",
        )
