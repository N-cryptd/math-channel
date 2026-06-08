"""
Video 05: Implicit Differentiation & Related Rates
Calculus I — finding dy/dx without solving for y.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, formula_box, proper narration timing.

Render draft:  manim -ql scripts/pre-university/video-05-implicit-related.py Video05_ImplicitRelated
Render final:  manim -qh scripts/pre-university/video-05-implicit-related.py Video05_ImplicitRelated

QUALITY RULES (enforced):
  1. Max 5 visible elements per scene at any time
  2. Use LayoutEngine for ALL text/formula positioning — no raw .shift() or .to_edge() for content
  3. Progressive disclosure: add items one at a time
  4. Consistent animation vocabulary (Write for titles, FadeIn for body)
  5. Narration: ~12 words per 5 seconds
  6. ly.clear() between scenes
  7. setup_background() for dot grid in construct()
  8. SANS for body/titles, MONO only for code/labels
"""

from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video05_ImplicitRelated(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_technique()
        self.scene3_differentiate()
        self.scene4_solve_for_dydx()
        self.scene5_verify_on_circle()
        self.scene6_ladder_setup()
        self.scene7_ladder_solve()
        self.scene8_ripple_problem()
        self.scene9_strategy()
        self.scene10_recap()

    # ── Scene 1: Hook — "What's dy/dx on a circle?" ──────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "What is dy/dx at the point (3,4) on the circle x squared plus y squared equals 25?",
            duration=8,
        )
        play_intro(self, "Implicit & Related Rates", "Calculus I")

        # The circle equation
        eq = MathTex(
            r"x^2 + y^2 = 25",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(eq)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(0.5)

        # The question
        question = Text(
            "What is dy/dx at (3,4)?",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(question, direction=DOWN, anchor=eq, buff=0.8)
        self.play(Write(question), run_time=NORMAL)
        self.wait(0.5)

        # We can't easily solve for y
        note = Text(
            "Can't solve for y as a single function...",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=question)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.0)

        # Punchline
        punchline = Text(
            "We need implicit differentiation!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(punchline, direction=DOWN, anchor=note)
        self.play(Write(punchline), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 2: The Technique — Concept ─────────────────────────────
    def scene2_technique(self):
        self.ly.section_divider(1, "The Technique")

        self.add_subcaption(
            "Implicit differentiation: differentiate both sides with respect to x, "
            "treating y as a function of x. The chain rule handles the y terms.",
            duration=10,
        )

        title = self.ly.title("Implicit Differentiation")

        items = [
            Text("Differentiate both sides with respect to x", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Treat y as a function of x", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Chain rule applies to every y term", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Solve for dy/dx", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 3: Differentiate x² + y² = 25 ────────────────────────
    def scene3_differentiate(self):
        self.ly.section_divider(2, "Differentiate Both Sides")

        self.add_subcaption(
            "Starting with x squared plus y squared equals 25, "
            "we differentiate each term. The chain rule gives us 2y times dy/dx for the y squared term.",
            duration=10,
        )

        title = self.ly.title("Step by Step")

        # Original equation
        eq = MathTex(
            r"x^2 + y^2 = 25",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(eq, direction=DOWN, anchor=title)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(0.5)

        # Differentiate both sides
        diff = MathTex(
            r"\frac{d}{dx}\big[x^2\big] + \frac{d}{dx}\big[y^2\big] = \frac{d}{dx}[25]",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(diff, direction=DOWN, anchor=eq)
        self.play(Write(diff), run_time=NORMAL)
        self.wait(0.5)

        # Apply chain rule
        self.add_subcaption(
            "Applying the chain rule to y squared gives 2y times dy/dx.",
            duration=5,
        )
        result = MathTex(
            r"2x + 2y \cdot \frac{dy}{dx} = 0",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=diff)
        self.play(Write(result), run_time=NORMAL)

        # Chain rule callout
        callout = Text(
            "chain rule: d/dx[y²] = 2y · dy/dx",
            font_size=LABEL_SIZE, color=SECONDARY, font=MONO,
        )
        self.ly.safe_place(callout, direction=DOWN, anchor=result, buff=0.3)
        self.play(FadeIn(callout, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 4: Solve for dy/dx ────────────────────────────────────
    def scene4_solve_for_dydx(self):
        self.ly.section_divider(3, "Solve for dy/dx")

        self.add_subcaption(
            "Rearranging: 2y dy/dx equals negative 2x, "
            "so dy/dx equals negative x over y.",
            duration=8,
        )

        # Step 1: Isolate dy/dx
        step1 = MathTex(
            r"2y \cdot \frac{dy}{dx} = -2x",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.center_in_content(step1)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)

        # Step 2: Divide
        step2 = MathTex(
            r"\frac{dy}{dx} = -\frac{x}{y}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.8)
        self.play(Write(step2), run_time=SLOW)

        # Highlight the result with formula box
        box = SurroundingRectangle(step2, color=ACCENT, buff=0.2, stroke_width=2)
        self.play(Create(box), run_time=FAST)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 5: Verify on the Circle at (3,4) ──────────────────────
    def scene5_verify_on_circle(self):
        self.ly.section_divider(4, "Verify at (3,4)")

        self.add_subcaption(
            "Plugging in x=3 and y=4 gives dy/dx equals negative 3/4. "
            "The tangent line is perpendicular to the radius — our answer checks out.",
            duration=10,
        )

        title = self.ly.title("Verification")

        # Plug in the point
        plug = MathTex(
            r"\frac{dy}{dx}\bigg|_{(3,4)} = -\frac{3}{4}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(plug, direction=DOWN, anchor=title)
        self.play(Write(plug), run_time=NORMAL)
        self.wait(0.5)

        # Draw axes + circle + point
        axes = Axes(
            x_range=[-6, 6, 1], y_range=[-6, 6, 1],
            x_length=5, y_length=5,
            axis_config={"color": DIM, "include_numbers": False},
        )
        self.ly.safe_place(axes, direction=DOWN, anchor=plug, buff=0.5)
        circle_graph = Circle(
            radius=2.5, color=PRIMARY, stroke_width=3,
        ).move_to(axes.get_center())

        self.play(Create(axes), run_time=FAST)
        self.play(Create(circle_graph), run_time=NORMAL)

        # Point
        point_coord = axes.coords_to_point(3, 4)
        dot_point = Dot(point_coord, color=ACCENT, radius=0.1)
        point_label = MathTex(
            r"(3,4)", font_size=LABEL_SIZE, color=ACCENT,
        ).next_to(dot_point, UR, buff=0.15)
        self.play(FadeIn(dot_point, scale=0.5), run_time=FAST)
        self.play(Write(point_label), run_time=FAST)

        # Tangent line: y = -0.75x + 6.25
        def tangent_func(x):
            return -0.75 * x + 6.25
        tangent = axes.plot(tangent_func, x_range=[-4, 10], color=ACCENT, stroke_width=3)
        self.play(Create(tangent), run_time=NORMAL)

        # Perpendicular label
        perp = Text(
            "Tangent ⊥ Radius ✓",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(perp, direction=DOWN, anchor=axes, buff=0.3)
        self.play(Write(perp), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 6: Related Rates — Ladder Setup ────────────────────────
    def scene6_ladder_setup(self):
        self.ly.section_divider(5, "Related Rates: Sliding Ladder")

        self.add_subcaption(
            "A 10 foot ladder slides down a wall. The top moves down at 2 feet per second. "
            "How fast does the bottom move when the top is 6 feet high?",
            duration=12,
        )

        title = self.ly.title("The Ladder Problem")

        # Draw the right triangle
        base = LEFT * 3 + DOWN * 1.0
        wall = Line(base, base + UP * 3, color=WHITE, stroke_width=4)
        ground = Line(base, base + RIGHT * 4, color=WHITE, stroke_width=4)
        ladder = Line(base, base + UP * 3 + RIGHT * 4, color=ACCENT, stroke_width=5)

        self.play(Create(wall), run_time=FAST)
        self.play(Create(ground), run_time=FAST)
        self.play(Create(ladder), run_time=NORMAL)
        self.wait(0.5)

        # Equation and given
        eq = MathTex(
            r"x^2 + y^2 = 100",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(eq, direction=DOWN, anchor=ground, buff=0.4)
        self.play(Write(eq), run_time=FAST)

        given = Text(
            "dy/dt = -2 ft/s, find dx/dt when y=6",
            font_size=LABEL_SIZE, color=SECONDARY, font=MONO,
        )
        self.ly.safe_place(given, direction=DOWN, anchor=eq)
        self.play(FadeIn(given, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 7: Ladder Solution ─────────────────────────────────────
    def scene7_ladder_solve(self):
        self.ly.section_divider(6, "Ladder: Solution")

        self.add_subcaption(
            "Differentiating implicitly with respect to time: "
            "2x dx/dt plus 2y dy/dt equals 0. "
            "Solving and plugging in x=8, y=6 gives dx/dt equals 1.5 feet per second.",
            duration=12,
        )

        title = self.ly.title("Differentiate w.r.t. Time")

        # Differentiate
        diff = MathTex(
            r"2x\cdot\frac{dx}{dt} + 2y\cdot\frac{dy}{dt} = 0",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(diff, direction=DOWN, anchor=title)
        self.play(Write(diff), run_time=NORMAL)
        self.wait(0.5)

        # Solve for dx/dt
        solve = MathTex(
            r"\frac{dx}{dt} = -\frac{y}{x}\cdot\frac{dy}{dt}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(solve, direction=DOWN, anchor=diff)
        self.play(Write(solve), run_time=NORMAL)
        self.wait(0.5)

        # Plug in
        plug = MathTex(
            r"= -\frac{6}{8}\cdot(-2) = \frac{12}{8}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(plug, direction=DOWN, anchor=solve)
        self.play(Write(plug), run_time=NORMAL)
        self.wait(0.5)

        # Answer
        answer_tex = MathTex(
            r"\frac{dx}{dt} = 1.5\ \text{ft/s}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        answer_boxed = self.ly.formula_box(answer_tex)
        self.ly.safe_place(answer_boxed, direction=DOWN, anchor=plug, buff=0.5)
        self.play(Write(answer_boxed), run_time=SLOW)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 8: Expanding Ripple ────────────────────────────────────
    def scene8_ripple_problem(self):
        self.ly.section_divider(7, "Related Rates: Expanding Ripple")

        self.add_subcaption(
            "A stone creates a ripple expanding at 2 feet per second. "
            "How fast does the area increase when the radius is 5 feet?",
            duration=10,
        )

        title = self.ly.title("Area of a Circle")

        # Formula
        area = MathTex(
            r"A = \pi r^2",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(area, direction=DOWN, anchor=title)
        self.play(Write(area), run_time=NORMAL)
        self.wait(0.5)

        # Given
        given = Text(
            "dr/dt = 2 ft/s, find dA/dt when r = 5",
            font_size=LABEL_SIZE, color=SECONDARY, font=MONO,
        )
        self.ly.safe_place(given, direction=DOWN, anchor=area)
        self.play(FadeIn(given, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Differentiate
        self.add_subcaption(
            "Differentiating: dA/dt equals 2 pi r times dr/dt. "
            "Plugging in r=5 and dr/dt=2 gives 20 pi square feet per second.",
            duration=10,
        )
        diff = MathTex(
            r"\frac{dA}{dt} = 2\pi r \cdot \frac{dr}{dt}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(diff, direction=DOWN, anchor=given)
        self.play(Write(diff), run_time=NORMAL)
        self.wait(0.5)

        # Answer
        answer_tex = MathTex(
            r"\frac{dA}{dt} = 2\pi(5)(2) = 20\pi\ \text{ft}^2/\text{s}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(answer_tex, direction=DOWN, anchor=diff)
        self.play(Write(answer_tex), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 9: General Strategy ───────────────────────────────────
    def scene9_strategy(self):
        self.ly.section_divider(8, "Related Rates Strategy")

        self.add_subcaption(
            "The general strategy: draw a diagram, write an equation, "
            "differentiate implicitly, plug in values, and solve.",
            duration=8,
        )

        title = self.ly.title("5-Step Strategy")

        steps = [
            Text("1. Draw a diagram", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. Write an equation relating the variables", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3. Differentiate implicitly w.r.t. time", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("4. Plug in known values", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5. Solve for the unknown rate", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(steps, start_from=title)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 10: Recap + Outro ────────────────────────────────────
    def scene10_recap(self):
        self.add_subcaption(
            "Implicit differentiation lets us find dy/dx when y is not isolated. "
            "Related rates extend this to variables changing over time.",
            duration=8,
        )

        title = self.ly.title("What We Learned")

        bullets = [
            Text("Differentiate both sides, solve for dy/dx", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("For x²+y²=25: dy/dx = -x/y", font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("Related rates: variables change with time", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(bullets, start_from=title)
        self.wait(1.0)

        self.ly.clear()

        # Outro
        self.add_subcaption(
            "Thank you for watching. See you next time.",
            duration=5,
        )
        play_outro(self, "Exp & Log Derivatives", "Calculus I")
