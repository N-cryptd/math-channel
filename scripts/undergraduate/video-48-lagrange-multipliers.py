"""
Video 48: Lagrange Multipliers
Calculus III -- Multivariable Playlist -- Video 8 of 14

Covers: constrained optimization, geometric intuition (gradient parallelism),
Lagrange condition nabla f = lambda nabla g, the Lagrangian function,
worked examples (maximize area / minimize distance to line).

Render draft:  manim -ql scripts/undergraduate/video-48-lagrange-multipliers.py Video48_LagrangeMultipliers
Render final:  manim -qh scripts/undergraduate/video-48-lagrange-multipliers.py Video48_LagrangeMultipliers
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


class Video48_LagrangeMultipliers(Scene):
    """Full video: Lagrange Multipliers."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_geometry_of_constraints()
        self.scene3_lagrange_condition()
        self.scene4_lagrangian_function()
        self.scene5_worked_example_maximize()
        self.scene6_multiple_candidates()
        self.scene7_summary()

    # ── Scene 1: Hook — The Fence Problem ──────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Imagine you have 100 meters of fencing material and you need "
            "to build a rectangular pen. You want to maximize the area. "
            "But the perimeter must equal exactly 100 meters. This is "
            "constrained optimization.",
            duration=18,
        )
        play_intro(self, "Lagrange Multipliers",
                   "Calculus III -- Multivariable")

        # The fence problem
        question = Text(
            "You have 100m of fencing. Build a rectangular pen with MAXIMUM area.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(question)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        # Constraint emphasis
        constraint = Text(
            "Constraint: 2x + 2y = 100 (perimeter is fixed)",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        constraint.next_to(question, DOWN, buff=0.6)
        ensure_fits(constraint)
        self.play(FadeIn(constraint, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1.0)

        # Bridge from gradient video
        bridge = Text(
            "Last time: gradient points uphill.\n"
            "Now: what if we can only walk along a trail?",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        bridge.next_to(constraint, DOWN, buff=0.5)
        ensure_fits(bridge)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.5)
        self.ly.clear()

    # ── Scene 2: The Geometry of Constraints ───────────────────────
    def scene2_geometry_of_constraints(self):
        self.add_subcaption(
            "Imagine contour lines of our function f on a 2D plane. "
            "Each contour represents a constant value of f. The constraint "
            "is a curve on this same plane. The maximum occurs where a "
            "contour of f is tangent to the constraint curve.",
            duration=18,
        )
        self.ly.section_divider(1, "The Geometry of Constraints")

        title = self.ly.title("Contour Map + Constraint")

        # Draw contour lines (hyperbolas for f = xy)
        contours = VGroup()
        contour_colors = [
            "#2a2555", "#332d66", "#3d3677", "#474088",
            "#514a99", "#5b54aa", "#655ebb", "#7070cc",
        ]
        # Use ellipses as approximate contours of f(x,y) = xy
        for i, (a, b) in enumerate([
            (0.3, 0.8), (0.5, 1.2), (0.7, 1.6), (0.9, 2.0),
            (1.1, 2.4), (1.3, 2.8), (1.5, 3.2), (1.7, 3.5),
        ]):
            curve = Ellipse(
                width=a * 2, height=b * 2,
                color=contour_colors[i],
                stroke_width=1.5,
            )
            contours.add(curve)
        self.ly.center_in_content(contours)
        self.play(Create(contours), run_time=2.0, lag_ratio=0.15)
        self.wait(0.5)

        # Label contours
        c_label = Text(
            "Contours of f(x,y)",
            font_size=LABEL_SIZE, color=DIM, font=MONO,
        )
        c_label.to_corner(UL, buff=0.3)
        self.play(FadeIn(c_label), run_time=FAST)
        self.wait(0.3)

        # Draw constraint line (straight line 2x + 2y = 100, scaled)
        constraint_line = Line(
            LEFT * 4.5 + DOWN * 1.5,
            RIGHT * 4.5 + UP * 1.5,
            color=SECONDARY,
            stroke_width=2.5,
        )
        self.play(Create(constraint_line), run_time=NORMAL)

        g_label = Text(
            "g(x,y) = c  (constraint)",
            font_size=LABEL_SIZE, color=SECONDARY, font=MONO,
        )
        g_label.next_to(constraint_line.get_end(), UP, buff=0.15)
        ensure_fits(g_label)
        self.play(FadeIn(g_label), run_time=FAST)
        self.wait(1.0)

        # Show optimal point where contour is tangent to constraint
        opt_point = Dot(
            LEFT * 1.5 + UP * 0.5,
            color=ACCENT, radius=0.08,
        )
        self.play(FadeIn(opt_point), run_time=FAST)

        opt_label = Text(
            "Optimum: contour tangent to constraint",
            font_size=LABEL_SIZE, color=ACCENT, font=MONO,
        )
        opt_label.next_to(opt_point, DOWN, buff=0.3)
        ensure_fits(opt_label)
        self.play(FadeIn(opt_label), run_time=FAST)
        self.wait(1.0)

        # Show gradient arrows at optimal point
        grad_f_arrow = Arrow(
            LEFT * 1.5 + UP * 0.5,
            LEFT * 2.5 + UP * 1.5,
            color=PRIMARY,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )
        grad_g_arrow = Arrow(
            LEFT * 1.5 + UP * 0.5,
            LEFT * 2.3 + UP * 1.3,
            color=RED,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )
        self.play(Create(grad_f_arrow), run_time=NORMAL)
        self.play(Create(grad_g_arrow), run_time=NORMAL)

        gf_label = Text(
            "nabla f",
            font_size=LABEL_SIZE, color=PRIMARY, font=MONO,
        )
        gf_label.next_to(grad_f_arrow.get_end(), UP, buff=0.1)
        self.play(FadeIn(gf_label), run_time=FAST)

        gg_label = Text(
            "nabla g",
            font_size=LABEL_SIZE, color=RED, font=MONO,
        )
        gg_label.next_to(grad_g_arrow.get_start(), LEFT, buff=0.1)
        self.play(FadeIn(gg_label), run_time=FAST)
        self.wait(1.0)

        # Key insight text
        parallel_text = MathTex(
            r"\nabla f \parallel \nabla g",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        parallel_text.to_corner(DR, buff=0.4)
        self.play(Write(parallel_text), run_time=NORMAL)
        self.wait(2.5)

        # Clean up
        self.play(
            FadeOut(contours), FadeOut(constraint_line),
            FadeOut(opt_point), FadeOut(opt_label),
            FadeOut(grad_f_arrow), FadeOut(grad_g_arrow),
            FadeOut(gf_label), FadeOut(gg_label),
            FadeOut(c_label), FadeOut(g_label),
            FadeOut(parallel_text),
            run_time=1.0,
        )
        self.ly.clear()

    # ── Scene 3: The Lagrange Condition ─────────────────────────────
    def scene3_lagrange_condition(self):
        self.add_subcaption(
            "Since the gradients are parallel at the optimum, we can write "
            "nabla f equals lambda times nabla g. This gives us three "
            "equations in three unknowns. Lambda is the Lagrange multiplier.",
            duration=18,
        )
        self.ly.section_divider(2, "The Lagrange Condition")

        title = self.ly.title("From Parallelism to Equations")

        # The core condition in a formula box
        condition = MathTex(
            r"\nabla f = \lambda \, \nabla g",
            font_size=56, color=ACCENT,
        )
        condition_box = self.ly.formula_box(condition, color=ACCENT, buff=0.3)
        self.ly.center_in_content(condition_box)
        self.play(Write(condition_box), run_time=SLOW)
        self.wait(1.5)
        self.ly.clear()

        # The three equations
        title2 = self.ly.title("The System of Equations")

        eq_label = Text(
            "Three equations, three unknowns (x, y, lambda):",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(eq_label, direction=DOWN, anchor=title2, buff=0.4)
        self.play(FadeIn(eq_label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        eqs = VGroup(
            MathTex(
                r"\frac{\partial f}{\partial x} = \lambda \frac{\partial g}{\partial x}",
                font_size=HEADING_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"\frac{\partial f}{\partial y} = \lambda \frac{\partial g}{\partial y}",
                font_size=HEADING_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"g(x,y) = c",
                font_size=HEADING_SIZE, color=SECONDARY,
            ),
        )
        eqs.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        eqs.next_to(eq_label, DOWN, buff=0.5)
        ensure_fits(eqs)
        self.play(
            *[Write(eq) for eq in eqs],
            run_time=2.0, lag_ratio=0.3,
        )
        self.wait(1.0)

        # lambda label
        lambda_note = Text(
            "lambda = Lagrange multiplier",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        lambda_note.next_to(eqs, DOWN, buff=0.5)
        ensure_fits(lambda_note)
        self.play(FadeIn(lambda_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 4: The Lagrangian Function ───────────────────────────
    def scene4_lagrangian_function(self):
        self.add_subcaption(
            "There is an elegant way to package this system into a single "
            "function. We define the Lagrangian L equals f minus lambda "
            "times (g minus c). Taking partial derivatives of L and setting "
            "them equal to zero recovers the Lagrange equations.",
            duration=18,
        )
        self.ly.section_divider(3, "The Lagrangian Function")

        title = self.ly.title("One Function, Three Equations")

        # The Lagrangian definition
        lagrangian = MathTex(
            r"\mathcal{L}(x, y, \lambda) = f(x,y) - \lambda\big(g(x,y) - c\big)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(lagrangian, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(lagrangian), run_time=SLOW)
        self.wait(1.0)

        # Show partial derivatives recover the equations
        self.ly.clear()

        title2 = self.ly.title("Partial Derivatives Recover the System")

        derivs = VGroup(
            MathTex(
                r"\frac{\partial \mathcal{L}}{\partial x} = 0"
                r"\;\Rightarrow\; \frac{\partial f}{\partial x} = \lambda \frac{\partial g}{\partial x}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"\frac{\partial \mathcal{L}}{\partial y} = 0"
                r"\;\Rightarrow\; \frac{\partial f}{\partial y} = \lambda \frac{\partial g}{\partial y}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"\frac{\partial \mathcal{L}}{\partial \lambda} = 0"
                r"\;\Rightarrow\; g(x,y) = c",
                font_size=BODY_SIZE, color=SECONDARY,
            ),
        )
        derivs.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.safe_place(derivs, direction=DOWN, anchor=title2, buff=0.4)
        self.play(
            *[FadeIn(d, shift=LEFT * 0.15) for d in derivs],
            run_time=2.0, lag_ratio=0.2,
        )
        self.wait(2.5)
        self.ly.clear()

    # ── Scene 5: Worked Example — Maximize ─────────────────────────
    def scene5_worked_example_maximize(self):
        self.add_subcaption(
            "Let's solve the fence problem. Maximize the area f equals "
            "x times y, subject to 2x plus 2y equals 100. The gradients "
            "are nabla f equals (y, x) and nabla g equals (2, 2). "
            "Setting them parallel: y equals 2 lambda and x equals 2 "
            "lambda. So x equals y. The optimal rectangle is a square!",
            duration=22,
        )
        self.ly.section_divider(4, "Worked Example -- The Fence Problem")

        title = self.ly.title("Maximize f(x,y) = xy subject to 2x + 2y = 100")

        # Step 1: Gradients
        step1 = Text(
            "Step 1: Compute the gradients",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(step1, shift=LEFT * 0.15), run_time=FAST)

        grad_f = MathTex(
            r"\nabla f = \langle y,\, x \rangle",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        grad_f.next_to(step1, DOWN, buff=0.4)
        ensure_fits(grad_f)
        self.play(Write(grad_f), run_time=NORMAL)

        grad_g = MathTex(
            r"\nabla g = \langle 2,\, 2 \rangle",
            font_size=HEADING_SIZE, color=RED,
        )
        grad_g.next_to(grad_f, DOWN, buff=0.3)
        ensure_fits(grad_g)
        self.play(Write(grad_g), run_time=NORMAL)
        self.wait(1.0)

        # Step 2: Lagrange equations
        self.play(
            FadeOut(step1), FadeOut(grad_f), FadeOut(grad_g),
            run_time=0.4,
        )

        step2 = Text(
            "Step 2: Set nabla f = lambda nabla g",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(step2, shift=LEFT * 0.15), run_time=FAST)

        lag_eqs = VGroup(
            MathTex(
                r"y = 2\lambda",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            MathTex(
                r"x = 2\lambda",
                font_size=HEADING_SIZE, color=WHITE,
            ),
        )
        lag_eqs.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        lag_eqs.next_to(step2, DOWN, buff=0.4)
        ensure_fits(lag_eqs)
        self.play(
            *[FadeIn(eq, shift=LEFT * 0.15) for eq in lag_eqs],
            run_time=NORMAL, lag_ratio=0.2,
        )

        # Key deduction
        deduction = Text(
            "From eq 1 and 2:  x = y  (it's a square!)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        deduction.next_to(lag_eqs, DOWN, buff=0.4)
        ensure_fits(deduction)
        self.play(
            Indicate(lag_eqs),
            FadeIn(deduction, shift=UP * 0.15),
            run_time=NORMAL,
        )
        self.wait(1.0)

        # Step 3: Solve
        self.play(
            FadeOut(step2), FadeOut(lag_eqs), FadeOut(deduction),
            run_time=0.4,
        )

        step3 = Text(
            "Step 3: Substitute into constraint",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(step3, direction=DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(step3, shift=LEFT * 0.15), run_time=FAST)

        solve = MathTex(
            r"2x + 2x = 100 \;\Rightarrow\; 4x = 100 \;\Rightarrow\; x = 25",
            font_size=HEADING_SIZE, color=WHITE,
        )
        solve.next_to(step3, DOWN, buff=0.4)
        ensure_fits(solve)
        self.play(Write(solve), run_time=SLOW)
        self.wait(0.5)

        # Final result
        result = MathTex(
            r"A_{\max} = 25 \times 25 = 625",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        result.next_to(solve, DOWN, buff=0.4)
        ensure_fits(result)
        self.play(Write(result), run_time=NORMAL)
        self.wait(2.5)
        self.ly.clear()

    # ── Scene 6: Multiple Candidates (Minimize) ────────────────────
    def scene6_multiple_candidates(self):
        self.add_subcaption(
            "Now let's find the minimum. Minimize x squared plus y squared, "
            "subject to x plus y equals 4. Geometrically we are finding "
            "the closest point on the line to the origin. The gradients "
            "are nabla f equals (2x, 2y) and nabla g equals (1, 1). "
            "Setting them parallel gives x equals y equals 2.",
            duration=22,
        )
        self.ly.section_divider(5, "Multiple Candidates -- Minimize")

        title = self.ly.title("Minimize f(x,y) = x^2 + y^2 subject to x + y = 4")

        # Geometric motivation
        geo = Text(
            "Find the point on x + y = 4 closest to the origin",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(geo, direction=DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(geo, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.8)

        # Visual: line and circle
        line_group = VGroup()
        constraint_line = Line(
            LEFT * 3 + UP * 1.5,
            RIGHT * 3 + DOWN * 1.5,
            color=SECONDARY, stroke_width=2,
        )
        line_group.add(constraint_line)
        self.ly.center_in_content(line_group)
        self.play(Create(constraint_line), run_time=NORMAL)

        # Circle centered at origin, tangent to the line
        # Line is x + y = 4. Closest point: (2, 2), distance = 2*sqrt(2) ~ 2.83
        # Scale for display
        circle = Circle(
            radius=2.0,
            color=PRIMARY,
            stroke_width=1.5,
        )
        circle.move_to(ORIGIN + DOWN * 0.3)
        self.play(Create(circle), run_time=NORMAL)

        # Optimal point
        opt = Dot(
            RIGHT * 1.4 + UP * 1.4 + DOWN * 0.3,
            color=ACCENT, radius=0.07,
        )
        self.play(FadeIn(opt), run_time=FAST)

        line_label = Text(
            "x + y = 4",
            font_size=LABEL_SIZE, color=SECONDARY, font=MONO,
        )
        line_label.next_to(constraint_line.get_end(), RIGHT, buff=0.15)
        ensure_fits(line_label)
        self.play(FadeIn(line_label), run_time=FAST)

        dist_label = Text(
            "distance = 2",
            font_size=LABEL_SIZE, color=PRIMARY, font=MONO,
        )
        dist_label.next_to(circle, LEFT, buff=0.15)
        ensure_fits(dist_label)
        self.play(FadeIn(dist_label), run_time=FAST)
        self.wait(1.5)

        # Clean up visual, do algebra
        everything = VGroup(
            constraint_line, circle, opt,
            line_label, dist_label, geo,
        )
        self.play(FadeOut(everything), run_time=0.8)
        self.ly.clear()

        # Algebra
        title2 = self.ly.title("Solving with Lagrange Multipliers")

        step = Text(
            "nabla f = (2x, 2y),  nabla g = (1, 1)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(step, direction=DOWN, anchor=title2, buff=0.4)
        self.play(FadeIn(step, shift=LEFT * 0.15), run_time=FAST)

        eqs = VGroup(
            MathTex(
                r"2x = \lambda, \quad 2y = \lambda",
                font_size=HEADING_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"\Rightarrow x = y",
                font_size=HEADING_SIZE, color=ACCENT,
            ),
            MathTex(
                r"x + x = 4 \;\Rightarrow\; x = y = 2",
                font_size=HEADING_SIZE, color=WHITE,
            ),
        )
        eqs.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        eqs.next_to(step, DOWN, buff=0.4)
        ensure_fits(eqs)
        self.play(
            *[FadeIn(eq, shift=LEFT * 0.15) for eq in eqs],
            run_time=2.0, lag_ratio=0.2,
        )

        # Result
        min_result = MathTex(
            r"f_{\min} = 2^2 + 2^2 = 8",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        min_result.next_to(eqs, DOWN, buff=0.4)
        ensure_fits(min_result)
        self.play(Write(min_result), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Summary + Outro ──────────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "To summarize: Lagrange multipliers solve constrained "
            "optimization. At the optimum, the gradient of f is parallel "
            "to the gradient of g. We write nabla f equals lambda nabla g "
            "and solve together with the constraint. The Lagrangian "
            "packages all three equations into one elegant function.",
            duration=18,
        )
        self.ly.section_divider(6, "Key Takeaways")

        title = self.ly.title("Summary")

        items = [
            Text(
                "1. Constrained optimization: maximize/minimize f subject to g = c",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. At the optimum: nabla f = lambda nabla g (gradients parallel)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3. Solve 3 equations for (x, y, lambda) to find candidates",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "4. Lagrangian: L = f - lambda(g - c) packages everything",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)
        self.ly.clear()

        # Final formula recap
        title2 = self.ly.title("The Method in One Line")

        recap = MathTex(
            r"\nabla f = \lambda \, \nabla g",
            r"\quad \text{with} \quad",
            r"g(x,y) = c",
            font_size=48, color=ACCENT,
        )
        recap_box = self.ly.formula_box(recap, color=ACCENT, buff=0.3)
        self.ly.center_in_content(recap_box)
        self.play(Write(recap_box), run_time=SLOW)
        self.wait(2.0)
        self.ly.clear()

        # Channel outro
        self.add_subcaption(
            "Thank you for watching! In the next video, we will explore "
            "extreme values on closed and bounded regions.",
            duration=8,
        )
        play_outro(
            self,
            next_video="Extreme Values on Closed Regions",
            next_playlist="Calculus III -- Multivariable",
        )
