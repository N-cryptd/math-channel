"""
Video 47: Gradient and Directional Derivatives
Calculus III -- Multivariable Playlist -- Video 7 of 14

Covers: gradient vector definition, directional derivative (limit definition),
gradient dot product formula D_u f = grad(f) . u, geometric meaning
(steepest ascent, perpendicular to level curves), worked example.

Render draft:  manim -ql scripts/undergraduate/video-47-gradient-directional.py Video47_GradientDirectional
Render final:  manim -qh scripts/undergraduate/video-47-gradient-directional.py Video47_GradientDirectional
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


class Video47_GradientDirectional(Scene):
    """Full video: Gradient and Directional Derivatives."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_gradient_def()
        self.scene3_directional_def()
        self.scene4_gradient_shortcut()
        self.scene5_geometric_meaning()
        self.scene6_worked_example()
        self.scene7_summary()

    # ── Scene 1: Hook — The Mountain Problem ────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Imagine you're standing on a hillside. You want to climb as "
            "fast as possible. Which direction do you walk? The answer "
            "involves a special vector called the gradient.",
            duration=18,
        )
        play_intro(self, "Gradient and Directional Derivatives",
                   "Calculus III -- Multivariable")

        # Mountain metaphor question
        question = Text(
            "You're on a hill. Which way is uphill the fastest?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(question)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        # Answer teaser
        answer = Text(
            "Answer: follow the gradient vector",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        answer.next_to(question, DOWN, buff=0.6)
        ensure_fits(answer)
        self.play(FadeIn(answer, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2.5)
        self.ly.clear()

    # ── Scene 2: Defining the Gradient ──────────────────────────────
    def scene2_gradient_def(self):
        self.add_subcaption(
            "The gradient of a scalar function f is a vector whose "
            "components are the partial derivatives. It collects all "
            "the directional rate of change information into one vector.",
            duration=18,
        )
        self.ly.section_divider(1, "The Gradient Vector")

        title = self.ly.title("Definition")

        # Gradient definition
        grad_def = MathTex(
            r"\nabla f = \left\langle \frac{\partial f}{\partial x},\;"
            r"\frac{\partial f}{\partial y} \right\rangle",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(grad_def, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(grad_def), run_time=SLOW)
        self.wait(1.0)

        # Alternative notations
        self.ly.clear()

        title2 = self.ly.title("Notation")

        notations = MathTex(
            r"\nabla f = \text{grad}\, f "
            r"= \left\langle f_x,\, f_y \right\rangle",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(notations, direction=DOWN, anchor=title2, buff=0.6)
        self.play(Write(notations), run_time=NORMAL)
        self.wait(0.8)

        # Quick example
        self.play(FadeOut(notations), run_time=0.3)

        ex_label = Text(
            "Example: f(x,y) = x^2 y + y^3",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        ex_label.next_to(title2, DOWN, buff=0.5)
        ensure_fits(ex_label)
        self.play(FadeIn(ex_label, shift=LEFT * 0.15), run_time=FAST)

        ex_grad = MathTex(
            r"\nabla f = \langle 2xy,\; x^2 + 3y^2 \rangle",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        ex_grad.next_to(ex_label, DOWN, buff=0.5)
        ensure_fits(ex_grad)
        self.play(Write(ex_grad), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 3: Directional Derivative — Definition ────────────────
    def scene3_directional_def(self):
        self.add_subcaption(
            "Partial derivatives give us the slope only in the x or y "
            "directions. But what if we want the slope in any arbitrary "
            "direction? That's the directional derivative. We move along "
            "a unit vector u and measure the rate of change.",
            duration=18,
        )
        self.ly.section_divider(2, "Directional Derivatives")

        title = self.ly.title("From Partial to Any Direction")

        # Motivation text
        mot = Text(
            "Partial derivatives: slope in x or y only.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(mot, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(mot, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        mot2 = Text(
            "Directional derivative: slope in ANY direction.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        mot2.next_to(mot, DOWN, buff=0.4)
        ensure_fits(mot2)
        self.play(FadeIn(mot2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.0)

        # Formal definition
        self.ly.clear()

        title2 = self.ly.title("Formal Definition")

        def_label = Text(
            "u must be a unit vector!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(def_label, direction=DOWN, anchor=title2, buff=0.4)
        self.play(FadeIn(def_label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        def_formula = MathTex(
            r"D_{\hat{u}} f = \lim_{h \to 0} "
            r"\frac{f(x + h u_1,\, y + h u_2) - f(x,\, y)}{h}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        def_formula.next_to(def_label, DOWN, buff=0.5)
        ensure_fits(def_formula)
        self.play(Write(def_formula), run_time=SLOW)
        self.wait(0.5)

        # Unit vector notation
        u_note = MathTex(
            r"\hat{u} = \langle u_1,\, u_2 \rangle,"
            r"\quad |\hat{u}| = 1",
            font_size=BODY_SIZE, color=DIM,
        )
        u_note.next_to(def_formula, DOWN, buff=0.5)
        ensure_fits(u_note)
        self.play(Write(u_note), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 4: The Gradient Shortcut ─────────────────────────────
    def scene4_gradient_shortcut(self):
        self.add_subcaption(
            "Here is the beautiful shortcut. The directional derivative "
            "in the direction u equals the dot product of the gradient "
            "with u. Once you compute the gradient, you can find the "
            "rate of change in any direction with a single dot product.",
            duration=18,
        )
        self.ly.section_divider(3, "The Gradient Formula")

        title = self.ly.title("Key Theorem")

        # The formula in a box
        formula = MathTex(
            r"D_{\hat{u}} f = \nabla f \cdot \hat{u}",
            font_size=56, color=ACCENT,
        )
        formula_box = self.ly.formula_box(formula, color=ACCENT, buff=0.3)
        self.ly.center_in_content(formula_box)
        self.play(Write(formula_box), run_time=SLOW)
        self.wait(1.5)

        # Explain what this means
        self.ly.clear()

        title2 = self.ly.title("Why This Works")

        items = [
            Text(
                "The limit definition expands to a dot product",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Compute gradient once, reuse for any direction",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Only requirement: u must be a unit vector",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(1.5)

        # Show expanded form
        self.ly.clear()

        title3 = self.ly.title("Expanded Form")

        expanded = MathTex(
            r"\nabla f \cdot \hat{u} = "
            r"|\nabla f|\, |\hat{u}|\, \cos\theta "
            r"= |\nabla f| \cos\theta",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(expanded, direction=DOWN, anchor=title3, buff=0.6)
        self.play(Write(expanded), run_time=SLOW)
        self.wait(0.5)

        # Key insight from this form
        insight = Text(
            "Maximum when cos(theta) = 1, i.e. theta = 0",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        insight.next_to(expanded, DOWN, buff=0.5)
        ensure_fits(insight)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 5: Geometric Meaning ──────────────────────────────────
    def scene5_geometric_meaning(self):
        self.add_subcaption(
            "The gradient has three beautiful geometric properties. "
            "First, its magnitude equals the maximum rate of change. "
            "Second, it points in the direction of steepest ascent. "
            "Third, it is perpendicular to the level curves, the "
            "lines of constant height on a contour map.",
            duration=18,
        )
        self.ly.section_divider(4, "What Does the Gradient Mean?")

        title = self.ly.title("Three Geometric Properties")

        items = [
            Text(
                "1. |grad f| = maximum rate of change of f",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "2. Direction of grad f = steepest ascent",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3. grad f is perpendicular to level curves",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.5)

        # Visualize contour map with gradient
        self.ly.clear()

        title2 = self.ly.title("Gradient on a Contour Map")

        # Draw contour lines (circles of varying radii)
        contours = VGroup()
        contour_colors = [
            "#2a2555", "#332d66", "#3d3677", "#474088",
            "#514a99", "#5b54aa", "#655ebb",
        ]
        for i, radius in enumerate([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]):
            circle = Circle(
                radius=radius,
                color=contour_colors[i],
                stroke_width=1.5,
            )
            contours.add(circle)
        self.ly.center_in_content(contours)
        self.play(Create(contours), run_time=2.0, lag_ratio=0.15)
        self.wait(0.5)

        # Label the contours
        label_c = Text(
            "Contour lines (level curves of f)",
            font_size=LABEL_SIZE, color=DIM, font=MONO,
        )
        label_c.to_corner(UR, buff=0.3)
        self.play(FadeIn(label_c), run_time=FAST)
        self.wait(0.5)

        # Draw gradient arrow at a point — perpendicular to contour
        point = Dot(ORIGIN + RIGHT * 1.5 + UP * 1.0, color=WHITE, radius=0.06)
        self.play(FadeIn(point), run_time=FAST)

        # Gradient arrow pointing outward (perpendicular to nearest contour)
        grad_arrow = Arrow(
            start=RIGHT * 1.5 + UP * 1.0,
            end=RIGHT * 3.0 + UP * 2.0,
            color=PRIMARY,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )
        self.play(Create(grad_arrow), run_time=NORMAL)
        self.wait(0.5)

        # Tangent to contour line at that point
        tangent_arrow = Arrow(
            start=RIGHT * 1.5 + UP * 1.0,
            end=RIGHT * 2.2 + UP * 0.3,
            color=SECONDARY,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.2,
        )
        self.play(Create(tangent_arrow), run_time=NORMAL)
        self.wait(0.5)

        # Labels
        grad_label = Text(
            "grad f (perpendicular to contour)",
            font_size=LABEL_SIZE, color=PRIMARY, font=MONO,
        )
        grad_label.next_to(grad_arrow.get_end(), RIGHT, buff=0.15)
        ensure_fits(grad_label)
        self.play(FadeIn(grad_label), run_time=FAST)

        tang_label = Text(
            "tangent to contour",
            font_size=LABEL_SIZE, color=SECONDARY, font=MONO,
        )
        tang_label.next_to(tangent_arrow.get_end(), DOWN, buff=0.1)
        ensure_fits(tang_label)
        self.play(FadeIn(tang_label), run_time=FAST)
        self.wait(2.5)

        # Clean up
        self.play(
            FadeOut(contours),
            FadeOut(point),
            FadeOut(grad_arrow),
            FadeOut(tangent_arrow),
            FadeOut(grad_label),
            FadeOut(tang_label),
            FadeOut(label_c),
            run_time=1.0,
        )
        self.ly.clear()

    # ── Scene 6: Worked Example ─────────────────────────────────────
    def scene6_worked_example(self):
        self.add_subcaption(
            "Let's work through an example. For f of x, y equals "
            "x squared plus y squared, the gradient is 2x, 2y. "
            "At the point 1, 2, the gradient is 2, 4. To find the "
            "directional derivative at 45 degrees, we take the dot "
            "product of the gradient with the unit vector.",
            duration=18,
        )
        self.ly.section_divider(5, "Worked Example")

        title = self.ly.title("Example: f(x,y) = x^2 + y^2")

        # Step 1: Function
        func = MathTex(
            r"f(x,y) = x^2 + y^2",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(func, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(func), run_time=NORMAL)
        self.wait(0.5)

        # Step 2: Gradient
        step1 = Text(
            "Step 1: Compute the gradient",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        step1.next_to(func, DOWN, buff=0.5)
        ensure_fits(step1)
        self.play(FadeIn(step1, shift=LEFT * 0.15), run_time=FAST)

        grad = MathTex(
            r"\nabla f = \langle 2x,\, 2y \rangle",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        grad.next_to(step1, DOWN, buff=0.4)
        ensure_fits(grad)
        self.play(Write(grad), run_time=NORMAL)
        self.wait(1.0)

        # Transition to evaluating at point
        self.play(
            FadeOut(step1),
            FadeOut(grad),
            run_time=0.4,
        )

        # Step 3: Evaluate at (1,2)
        step2 = Text(
            "Step 2: Evaluate at (1, 2)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        step2.next_to(func, DOWN, buff=0.5)
        ensure_fits(step2)
        self.play(FadeIn(step2, shift=LEFT * 0.15), run_time=FAST)

        eval_grad = MathTex(
            r"\nabla f(1,2) = \langle 2,\, 4 \rangle",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        eval_grad.next_to(step2, DOWN, buff=0.4)
        ensure_fits(eval_grad)
        self.play(Write(eval_grad), run_time=NORMAL)
        self.wait(1.0)

        # Transition
        self.play(
            FadeOut(step2),
            FadeOut(eval_grad),
            run_time=0.4,
        )

        # Step 4: Directional derivative
        step3 = Text(
            "Step 3: Directional derivative at 45 degrees",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        step3.next_to(func, DOWN, buff=0.5)
        ensure_fits(step3)
        self.play(FadeIn(step3, shift=LEFT * 0.15), run_time=FAST)

        u_vec = MathTex(
            r"\hat{u} = \left\langle \frac{1}{\sqrt{2}},\,"
            r"\frac{1}{\sqrt{2}} \right\rangle",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        u_vec.next_to(step3, DOWN, buff=0.4)
        ensure_fits(u_vec)
        self.play(Write(u_vec), run_time=NORMAL)
        self.wait(0.5)

        # Dot product
        dot_prod = MathTex(
            r"D_{\hat{u}} f = \langle 2, 4 \rangle \cdot "
            r"\left\langle \frac{1}{\sqrt{2}},\,"
            r"\frac{1}{\sqrt{2}} \right\rangle"
            r"= \frac{6}{\sqrt{2}} = 3\sqrt{2}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        dot_prod.next_to(u_vec, DOWN, buff=0.5)
        ensure_fits(dot_prod)
        self.play(Write(dot_prod), run_time=SLOW)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Summary + Outro ───────────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "To summarize: the gradient packages all partial derivatives "
            "into a vector. The directional derivative in any direction "
            "equals the gradient dot product with that direction. The "
            "gradient points in the direction of steepest ascent and is "
            "perpendicular to level curves.",
            duration=18,
        )

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                r"1. grad f = (f_x, f_y): vector of partial derivatives",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                r"2. D_u f = grad f . u: dot product formula",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                r"3. |grad f| = maximum rate of change",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                r"4. grad f is perpendicular to level curves",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)

        self.ly.clear()

        # Channel outro
        self.add_subcaption(
            "Thank you for watching! In the next video, we'll "
            "explore Lagrange multipliers, a powerful optimization "
            "technique that uses the gradient.",
            duration=8,
        )
        play_outro(
            self,
            next_video="Lagrange Multipliers",
            next_playlist="Calculus III -- Multivariable",
        )
