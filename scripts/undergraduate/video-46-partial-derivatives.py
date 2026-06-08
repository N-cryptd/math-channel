"""
Video 46: Partial Derivatives
Calculus III -- Multivariable Playlist -- Video 6 of 14

Covers: motivation from single-variable calculus, geometric intuition
(slicing a surface), formal limit definition, notation, worked examples
(polynomial and exponential/trig), higher-order partial derivatives,
Clairaut's theorem on equality of mixed partials.

Render draft:  manim -ql scripts/undergraduate/video-46-partial-derivatives.py Video46_PartialDerivatives
Render final:  manim -qh scripts/undergraduate/video-46-partial-derivatives.py Video46_PartialDerivatives
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


class Video46_PartialDerivatives(ThreeDScene):
    """Full video: Partial Derivatives."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        # Start in 2D-like view for non-3D scenes
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)

        self.scene1_hook()
        self.scene2_motivation()
        self.scene3_geometric()
        self.scene4_definition()
        self.scene5_example1()
        self.scene6_example2()
        self.scene7_higher_order()
        self.scene8_summary()

    # ── Scene 1: Hook + Channel Intro ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "When a function depends on more than one variable, how do we "
            "differentiate it? A partial derivative measures the rate of "
            "change in just one direction, while holding everything else constant.",
            duration=18,
        )
        play_intro(self, "Partial Derivatives", "Calculus III — Multivariable")

        bridge = Text(
            "How do you differentiate a function of two variables?",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(bridge)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3.0)
        self.ly.clear()

    # ── Scene 2: Motivation — From 1D to 2D ────────────────────────
    def scene2_motivation(self):
        self.add_subcaption(
            "In single-variable calculus, the derivative tells us the rate "
            "of change of f of x. But what if our function has two inputs, "
            "x and y? We take a partial derivative: differentiate with respect "
            "to one variable while treating the other as constant.",
            duration=18,
        )

        self.ly.section_divider(1, "From One Variable to Two")

        title = self.ly.title("Review: Ordinary Derivative")

        # Show dy/dx
        formula1 = MathTex(
            r"\frac{dy}{dx} = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(formula1, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(formula1), run_time=NORMAL)
        self.wait(0.8)

        # Now introduce f(x,y)
        self.play(FadeOut(formula1), run_time=0.3)

        new_title = Text(
            "Now: f(x, y) — two inputs, one output",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        new_title.next_to(title, DOWN, buff=0.5)
        ensure_fits(new_title)
        self.play(FadeIn(new_title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Key idea
        key_idea = Text(
            "Solution: take the derivative one variable at a time",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        key_idea.next_to(new_title, DOWN, buff=0.5)
        ensure_fits(key_idea)
        self.play(FadeIn(key_idea, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 3: Geometric Intuition — Slicing a Surface ────────────
    def scene3_geometric(self):
        self.add_subcaption(
            "Imagine a surface in 3D, like a paraboloid. If we fix y at some "
            "constant value and slice the surface, we get a 2D curve. The slope "
            "of that curve is the partial derivative with respect to x. "
            "Similarly, fixing x gives us the partial derivative with respect to y.",
            duration=18,
        )

        self.ly.section_divider(2, "Geometric Intuition")

        title = self.ly.title("Slicing a Surface")

        # Create a paraboloid surface
        resolution_fa = 20
        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                u**2 + v**2,
            ]),
            resolution=(resolution_fa, resolution_fa),
            u_range=[-2, 2],
            v_range=[-2, 2],
            fill_opacity=0.6,
        )
        surface.scale(0.5)
        # Color the surface with a gradient
        surface.set_color(PRIMARY)
        surface.move_to(ORIGIN)

        # Set up 3D camera
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(surface), run_time=2.0)
        self.wait(1.0)

        # Label: f(x,y) = x² + y²
        label_func = MathTex(
            r"f(x,y) = x^2 + y^2",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        label_func.to_corner(UL, buff=0.5)
        self.add_fixed_in_frame_mobjects(label_func)
        self.play(Write(label_func), run_time=NORMAL)
        self.wait(1.0)

        # Show x-direction slice (y = 1, a plane)
        # The curve on the surface when y=1: z = x² + 1
        slice_x = ParametricFunction(
            lambda t: np.array([
                t * 0.5,
                0.5,
                (t**2 + 1) * 0.5,
            ]),
            t_range=[-2, 2],
            color=PRIMARY,
            stroke_width=4,
        )
        self.play(Create(slice_x), run_time=1.5)
        self.wait(0.5)

        # Label the slice
        slice_label_x = Text(
            "y = const: curve in x-direction",
            font_size=LABEL_SIZE, color=PRIMARY, font=SANS,
        )
        slice_label_x.to_corner(UR, buff=0.5)
        self.add_fixed_in_frame_mobjects(slice_label_x)
        self.play(FadeIn(slice_label_x), run_time=FAST)
        self.wait(1.5)

        # Explanation text
        explain1 = Text(
            r"Slope of this curve = \(\partial f / \partial x\)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        explain1.to_corner(DR, buff=0.5)
        self.add_fixed_in_frame_mobjects(explain1)
        self.play(FadeIn(explain1), run_time=FAST)
        self.wait(2.0)

        # Clear 3D labels and show y-direction slice
        self.play(
            FadeOut(slice_label_x),
            FadeOut(explain1),
            run_time=0.3,
        )

        # Show y-direction slice (x = 1)
        slice_y = ParametricFunction(
            lambda t: np.array([
                0.5,
                t * 0.5,
                (1 + t**2) * 0.5,
            ]),
            t_range=[-2, 2],
            color=SECONDARY,
            stroke_width=4,
        )
        self.play(Create(slice_y), run_time=1.5)
        self.wait(0.5)

        slice_label_y = Text(
            "x = const: curve in y-direction",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        slice_label_y.to_corner(UR, buff=0.5)
        self.add_fixed_in_frame_mobjects(slice_label_y)
        self.play(FadeIn(slice_label_y), run_time=FAST)
        self.wait(1.5)

        explain2 = Text(
            r"Slope of this curve = \(\partial f / \partial y\)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        explain2.to_corner(DR, buff=0.5)
        self.add_fixed_in_frame_mobjects(explain2)
        self.play(FadeIn(explain2), run_time=FAST)
        self.wait(2.0)

        # Reset camera to 2D
        self.play(
            FadeOut(surface),
            FadeOut(slice_x),
            FadeOut(slice_y),
            FadeOut(label_func),
            FadeOut(slice_label_y),
            FadeOut(explain2),
            FadeOut(slice_label_x),
            run_time=1.0,
        )
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        self.wait(0.3)
        self.ly.clear()

    # ── Scene 4: Formal Definition ──────────────────────────────────
    def scene4_definition(self):
        self.add_subcaption(
            "The partial derivative of f with respect to x is defined as a limit. "
            "We take a small increment h only in the x-direction while y stays "
            "fixed. The formula mirrors the ordinary derivative, but now we have "
            "a function of two variables.",
            duration=18,
        )

        self.ly.section_divider(3, "Formal Definition")

        title = self.ly.title("Partial Derivative — Definition")

        # Definition box for ∂f/∂x
        def_x = MathTex(
            r"\frac{\partial f}{\partial x} = \lim_{h \to 0} "
            r"\frac{f(x+h,\, y) - f(x,\, y)}{h}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(def_x, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(def_x), run_time=SLOW)
        self.wait(1.0)

        # Label
        note_x = Text(
            "Treat y as a constant, differentiate w.r.t. x",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        note_x.next_to(def_x, DOWN, buff=0.5)
        ensure_fits(note_x)
        self.play(FadeIn(note_x, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        # Transition to ∂f/∂y definition
        self.play(
            FadeOut(def_x),
            FadeOut(note_x),
            run_time=0.4,
        )

        # Definition box for ∂f/∂y
        def_y = MathTex(
            r"\frac{\partial f}{\partial y} = \lim_{h \to 0} "
            r"\frac{f(x,\, y+h) - f(x,\, y)}{h}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(def_y, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(def_y), run_time=SLOW)
        self.wait(1.0)

        note_y = Text(
            "Treat x as a constant, differentiate w.r.t. y",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        note_y.next_to(def_y, DOWN, buff=0.5)
        ensure_fits(note_y)
        self.play(FadeIn(note_y, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        # Show alternative notations
        self.play(
            FadeOut(def_y),
            FadeOut(note_y),
            run_time=0.4,
        )

        not_title = Text(
            "Alternative Notations",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        not_title.next_to(title, DOWN, buff=0.5)
        ensure_fits(not_title)
        self.play(FadeIn(not_title, shift=LEFT * 0.15), run_time=FAST)

        notations = MathTex(
            r"\frac{\partial f}{\partial x} = f_x = \partial_x f"
            r" \qquad\qquad "
            r"\frac{\partial f}{\partial y} = f_y = \partial_y f",
            font_size=BODY_SIZE, color=WHITE,
        )
        notations.next_to(not_title, DOWN, buff=0.5)
        ensure_fits(notations)
        self.play(Write(notations), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 5: Example 1 — Polynomial ────────────────────────────
    def scene5_example1(self):
        self.add_subcaption(
            "Let's work through an example. For f of x, y equals 3x squared y "
            "plus 4 x y cubed plus y, we compute the partial derivative with "
            "respect to x by treating y as a constant. And we compute the "
            "partial derivative with respect to y by treating x as constant.",
            duration=18,
        )

        self.ly.section_divider(4, "Examples")

        title = self.ly.title("Example 1: Polynomial Function")

        # Show the function
        func = MathTex(
            r"f(x,y) = 3x^2 y + 4xy^3 + y",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(func, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(func), run_time=NORMAL)
        self.wait(0.8)

        # Part A: ∂f/∂x
        label_a = Text(
            "Partial with respect to x (treat y as constant):",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        label_a.next_to(func, DOWN, buff=0.5)
        ensure_fits(label_a)
        self.play(FadeIn(label_a, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        result_a = MathTex(
            r"\frac{\partial f}{\partial x} = 6xy + 4y^3",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        result_a.next_to(label_a, DOWN, buff=0.5)
        ensure_fits(result_a)
        self.play(Write(result_a), run_time=NORMAL)
        self.wait(1.5)

        # Transition
        self.play(
            FadeOut(label_a),
            FadeOut(result_a),
            run_time=0.4,
        )

        # Part B: ∂f/∂y
        label_b = Text(
            "Partial with respect to y (treat x as constant):",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        label_b.next_to(func, DOWN, buff=0.5)
        ensure_fits(label_b)
        self.play(FadeIn(label_b, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        result_b = MathTex(
            r"\frac{\partial f}{\partial y} = 3x^2 + 12xy^2 + 1",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        result_b.next_to(label_b, DOWN, buff=0.5)
        ensure_fits(result_b)
        self.play(Write(result_b), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 6: Example 2 — Exponential/Trig ──────────────────────
    def scene6_example2(self):
        self.add_subcaption(
            "For f of x, y equals e to the x y times sine of y, we need the "
            "product rule and chain rule. The partial with respect to x is y "
            "e to the x y sine y. The partial with respect to y is x e to the "
            "x y sine y plus e to the x y cosine y.",
            duration=18,
        )

        title = self.ly.title("Example 2: Exponential and Trig")

        # Show the function
        func = MathTex(
            r"f(x,y) = e^{xy} \sin(y)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(func, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(func), run_time=NORMAL)
        self.wait(0.8)

        # ∂f/∂x
        label_a = Text(
            "With respect to x:",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        label_a.next_to(func, DOWN, buff=0.5)
        ensure_fits(label_a)
        self.play(FadeIn(label_a, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        result_a = MathTex(
            r"\frac{\partial f}{\partial x} = y\, e^{xy} \sin(y)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        result_a.next_to(label_a, DOWN, buff=0.5)
        ensure_fits(result_a)
        self.play(Write(result_a), run_time=NORMAL)
        self.wait(1.5)

        self.play(
            FadeOut(label_a),
            FadeOut(result_a),
            run_time=0.4,
        )

        # ∂f/∂y (product rule needed)
        label_b = Text(
            "With respect to y (product rule!):",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        label_b.next_to(func, DOWN, buff=0.5)
        ensure_fits(label_b)
        self.play(FadeIn(label_b, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        result_b = MathTex(
            r"\frac{\partial f}{\partial y} = x\, e^{xy} \sin(y) + e^{xy} \cos(y)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        result_b.next_to(label_b, DOWN, buff=0.5)
        ensure_fits(result_b)
        self.play(Write(result_b), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Higher-Order Partial Derivatives ───────────────────
    def scene7_higher_order(self):
        self.add_subcaption(
            "Just as we take second derivatives in single-variable calculus, "
            "we can differentiate partial derivatives again. A second partial "
            "with respect to x is written f subscript x x. A mixed partial "
            "derivative is f subscript x y, differentiating first w.r.t. x, "
            "then y. Clairaut's theorem says mixed partials are equal when "
            "the function is sufficiently smooth.",
            duration=18,
        )

        self.ly.section_divider(5, "Higher-Order Derivatives")

        title = self.ly.title("Second Partial Derivatives")

        # Show the four second partials
        items = [
            MathTex(
                r"f_{xx} = \frac{\partial^2 f}{\partial x^2}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"f_{yy} = \frac{\partial^2 f}{\partial y^2}",
                font_size=BODY_SIZE, color=SECONDARY,
            ),
            MathTex(
                r"f_{xy} = \frac{\partial^2 f}{\partial x \partial y}",
                font_size=BODY_SIZE, color=ACCENT,
            ),
            MathTex(
                r"f_{yx} = \frac{\partial^2 f}{\partial y \partial x}",
                font_size=BODY_SIZE, color=ACCENT,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title, spacing=0.5)
        self.wait(1.0)

        # Clairaut's theorem
        self.ly.clear()

        title2 = self.ly.title("Clairaut's Theorem")

        clairaut = Text(
            "If f has continuous second partials, then:",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(clairaut, direction=DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(clairaut, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        formula_box = self.ly.formula_box(
            MathTex(
                r"f_{xy} = f_{yx}",
                font_size=HEADING_SIZE, color=ACCENT,
            ),
            color=ACCENT,
        )
        formula_box.next_to(clairaut, DOWN, buff=0.6)
        self.play(Write(formula_box), run_time=SLOW)
        self.wait(1.0)

        note = Text(
            "The order of differentiation doesn't matter!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        note.next_to(formula_box, DOWN, buff=0.5)
        ensure_fits(note)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 8: Summary + Outro ────────────────────────────────────
    def scene8_summary(self):
        self.add_subcaption(
            "To summarize: a partial derivative measures how a function changes "
            "in one variable direction while keeping the others fixed. "
            "Geometrically, it's the slope of a slice through the surface. "
            "You compute it by treating all other variables as constants. "
            "And mixed partials are equal under Clairaut's theorem.",
            duration=18,
        )

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                r"1. \(\partial f/\partial x\): rate of change in x-direction",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                r"2. Geometrically: slope of a slice through the surface",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                r"3. Compute: treat other variables as constants",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                r"4. Mixed partials: \(f_{xy} = f_{yx}\) (Clairaut's theorem)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)

        self.ly.clear()

        # Channel outro
        self.add_subcaption(
            "Thank you for watching! In the next video, we'll explore "
            "the gradient vector and directional derivatives.",
            duration=8,
        )
        play_outro(
            self,
            next_video="Gradient and Directional Derivatives",
            next_playlist="Calculus III — Multivariable",
        )
