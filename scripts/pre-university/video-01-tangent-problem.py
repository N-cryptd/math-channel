"""
Video 01: The Tangent Problem
Covers: average vs instantaneous speed, secant lines, tangent line as limit,
Leibniz/Lagrange notation, and computing the derivative of x².

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, proper narration timing.

Render draft:  manim -ql scripts/pre-university/video-01-tangent-problem.py Video01_TangentProblem
Render final:  manim -qh scripts/pre-university/video-01-tangent-problem.py Video01_TangentProblem

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


class Video01_TangentProblem(Scene):
    """Full video: 7 scenes — the tangent problem, derivative definition, first example."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_average_speed()
        self.scene3_problem_harder()
        self.scene4_aha_moment()
        self.scene5_notation()
        self.scene6_example()
        self.scene7_recap()

    # ── Scene 1: The Hook ───────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Welcome. Today we explore the tangent problem — "
            "what does it mean to go 60 miles per hour at a single instant?",
            duration=8,
        )
        play_intro(self, "The Tangent Problem", "Calculus I")

        self.add_subcaption(
            "If you drive 60 miles in one hour, your average speed is 60 mph. "
            "But what about this exact moment?",
            duration=8,
        )

        # Central question — use safe_place instead of hardcoded .to_edge()
        question = Text(
            "What does it mean to go 60 mph\nat a single instant?",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(question, anchor=None)
        self.play(Write(question), run_time=NORMAL)
        self.wait(0.5)

        # Number line with moving dot — graph element, manual positioning OK
        line = NumberLine(
            x_range=[0, 10, 1], length=8,
            color=DIM, include_numbers=True,
        )
        self.ly.safe_place(line, direction=DOWN, anchor=question, buff=1.0)
        dot = Dot(line.n2p(0), color=PRIMARY, radius=0.1)
        self.play(Create(line), run_time=NORMAL)
        self.wait(0.3)

        trail = TracedPath(dot.get_center, stroke_color=PRIMARY, stroke_opacity=0.3)
        self.add(trail)
        self.play(dot.animate.move_to(line.n2p(8)), run_time=4)
        self.wait(0.3)

        # Transition: fade number line, show position-time graph
        self.play(
            FadeOut(question), FadeOut(dot), FadeOut(trail), FadeOut(line),
            run_time=0.5,
        )
        self.wait(0.3)

        self.add_subcaption(
            "A position-time graph. The curve is p of t equals t squared. "
            "How fast is the object at t equals 3?",
            duration=10,
        )

        # Position-time graph
        graph_axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 25, 5],
            x_length=5, y_length=3,
            axis_config={"color": DIM, "include_numbers": True},
        )
        self.ly.center_in_content(graph_axes)

        curve = graph_axes.plot(lambda t: t**2, color=PRIMARY, stroke_width=3)
        curve_label = MathTex(r"p(t) = t^2", font_size=LABEL_SIZE, color=PRIMARY)
        curve_label.next_to(curve, RIGHT, buff=0.3)

        self.play(Create(graph_axes), run_time=NORMAL)
        self.play(Create(curve), run_time=NORMAL)
        self.play(Write(curve_label), run_time=FAST)
        self.wait(0.5)

        # "How fast at t=3?"
        t3_label = MathTex(r"t = 3?", font_size=HEADING_SIZE, color=ACCENT)
        t3_label.next_to(curve.point_from_proportion(0.6), UP, buff=0.5)
        self.play(Write(t3_label), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 2: Average Speed ──────────────────────────────────────
    def scene2_average_speed(self):
        self.add_subcaption(
            "Average speed over an interval is just rise over run — "
            "the slope of a secant line.",
            duration=10,
        )
        self.ly.section_divider(1, "Average Speed")

        # Graph — positioned left
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 25, 5],
            x_length=5.5, y_length=3.5,
            axis_config={"color": DIM, "include_numbers": True},
        )
        axes.shift(LEFT * 2.5 + DOWN * 0.3)
        curve = axes.plot(lambda t: t**2, color=PRIMARY, stroke_width=3)

        self.play(Create(axes), run_time=NORMAL)
        self.play(Create(curve), run_time=NORMAL)
        self.wait(0.3)

        # Two points on curve
        p1 = axes.c2p(2, 4)
        p2 = axes.c2p(5, 25)
        dot1 = Dot(p1, color=SECONDARY, radius=0.08)
        dot2 = Dot(p2, color=SECONDARY, radius=0.08)
        label1 = MathTex(r"(2, 4)", font_size=LABEL_SIZE, color=SECONDARY)
        label1.next_to(dot1, DOWN, buff=0.2)
        label2 = MathTex(r"(5, 25)", font_size=LABEL_SIZE, color=SECONDARY)
        label2.next_to(dot2, DOWN, buff=0.2)

        self.play(FadeIn(dot1), FadeIn(dot2), run_time=FAST)
        self.play(Write(label1), Write(label2), run_time=FAST)

        # Secant line through both points
        secant = Line(p1, p2, color=SECONDARY, stroke_width=2)
        self.play(Create(secant), run_time=NORMAL)

        # Formula on the right — use formula_box for the key result
        self.add_subcaption(
            "Twenty-one divided by three equals seven. "
            "The secant slope is the average speed.",
            duration=8,
        )
        avg_formula = MathTex(
            r"v_{avg} = \frac{\Delta y}{\Delta x}"
            r"= \frac{25 - 4}{5 - 2}"
            r"= \frac{21}{3} = 7",
            font_size=LABEL_SIZE,
        )
        fb = self.ly.formula_box(avg_formula, color=SECONDARY)
        fb.move_to(RIGHT * 3.0 + UP * 0.5)
        self.play(Write(avg_formula), run_time=SLOW)
        self.wait(1.0)

        # Moving secant lines converge toward the tangent
        self.add_subcaption(
            "As the second point slides closer, "
            "the secant lines converge toward a limit.",
            duration=8,
        )
        t_vals = [4.0, 3.5, 3.0, 2.5, 2.1]
        ghost_lines = VGroup()
        for t_val in t_vals:
            p_new = axes.c2p(t_val, t_val**2)
            gl = Line(p1, p_new, color=SECONDARY, stroke_width=1, stroke_opacity=0.3)
            ghost_lines.add(gl)

        self.play(
            LaggedStart(*[Create(gl) for gl in ghost_lines], lag_ratio=0.3),
            run_time=4,
        )
        self.play(dot2.animate.move_to(axes.c2p(2.1, 2.1**2)), run_time=3)
        self.wait(0.5)

        self.ly.clear()

    # ── Scene 3: Problem Gets Harder ────────────────────────────────
    def scene3_problem_harder(self):
        self.add_subcaption(
            "As the interval shrinks to zero, "
            "we hit a wall: dividing by zero is undefined.",
            duration=8,
        )
        self.ly.section_divider(2, "The Shrinking Interval")

        # Graph
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 25, 5],
            x_length=5, y_length=3.5,
            axis_config={"color": DIM, "include_numbers": True},
        )
        axes.shift(LEFT * 2.5 + DOWN * 0.3)
        curve = axes.plot(lambda t: t**2, color=PRIMARY, stroke_width=3)

        self.play(Create(axes), Create(curve), run_time=NORMAL)
        self.wait(0.2)

        # Fixed point at t=2
        p_fixed = axes.c2p(2, 4)
        dot_fixed = Dot(p_fixed, color=ACCENT, radius=0.08)
        self.play(FadeIn(dot_fixed), run_time=FAST)

        # Shrinking intervals — progressive reveal (enforces 5-item budget)
        self.add_subcaption(
            "Watch the slope values as delta t shrinks: "
            "five, four-point-one, four-point-zero-one. "
            "They approach four.",
            duration=10,
        )
        dt_items = [
            MathTex(
                r"\Delta t = 1.0 \Rightarrow v = 5.0",
                font_size=LABEL_SIZE, color=SECONDARY,
            ),
            MathTex(
                r"\Delta t = 0.1 \Rightarrow v = 4.1",
                font_size=LABEL_SIZE, color=SECONDARY,
            ),
            MathTex(
                r"\Delta t = 0.01 \Rightarrow v = 4.01",
                font_size=LABEL_SIZE, color=SECONDARY,
            ),
            MathTex(
                r"\Delta t \to 0 \Rightarrow v \to \, ?",
                font_size=LABEL_SIZE, color=ACCENT,
            ),
        ]
        self.ly.progressive_reveal(
            dt_items, spacing=0.35,
            anim_kwargs={"shift": LEFT * 0.15},
        )

        # Animate secant lines for each delta t
        for dt_val in [1.0, 0.1, 0.01]:
            t_val = 2 + dt_val
            p_move = axes.c2p(t_val, t_val**2)
            sec = Line(p_fixed, p_move, color=SECONDARY, stroke_width=1.5)
            self.play(Create(sec), run_time=FAST)
            sec.set_opacity(0.25)
        self.wait(0.5)

        # The problem — can't divide by zero
        self.add_subcaption(
            "But setting delta t to zero means dividing by zero. We need a new idea.",
            duration=6,
        )
        problem = Text(
            "But Δt = 0 means\nwe divide by zero!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 4: AHA — Tangent as Limit ─────────────────────────────
    def scene4_aha_moment(self):
        self.add_subcaption(
            "The tangent line is the limit of secant lines. "
            "Its slope is the derivative — your instantaneous speed.",
            duration=10,
        )
        self.ly.section_divider(3, "The Derivative")

        # Graph with ghost secants
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 25, 5],
            x_length=6, y_length=3.5,
            axis_config={"color": DIM, "include_numbers": True},
        )
        axes.shift(LEFT * 2.0 + DOWN * 0.3)
        curve = axes.plot(lambda t: t**2, color=PRIMARY, stroke_width=3)

        self.play(Create(axes), Create(curve), run_time=NORMAL)

        # Ghost secant lines converging to tangent
        p_fixed = axes.c2p(2, 4)
        for dt in [3.0, 2.0, 1.0, 0.5, 0.2, 0.05]:
            p2 = axes.c2p(2 + dt, (2 + dt)**2)
            sec = Line(
                p_fixed, p2, color=SECONDARY, stroke_width=1,
                stroke_opacity=0.15 + 0.1 * (3.0 / dt),
            )
            self.add(sec)
        self.wait(0.5)

        # THE tangent line — bright gold
        tangent = axes.plot(
            lambda x: 4 * x - 4, x_range=[0.5, 3.5],
            color=ACCENT, stroke_width=4,
        )
        dot_tangent = Dot(p_fixed, color=ACCENT, radius=0.1)

        self.play(
            Create(tangent), FadeIn(dot_tangent),
            run_time=SLOW,
        )
        self.wait(0.8)

        # Derivative definition — highlighted formula box
        deriv_def = MathTex(
            r"\frac{dy}{dx} = \lim_{\Delta t \to 0}"
            r"\frac{f(t_0 + \Delta t) - f(t_0)}{\Delta t}",
            font_size=LABEL_SIZE, color=ACCENT,
        )
        fb = self.ly.formula_box(deriv_def, color=ACCENT)
        fb.move_to(RIGHT * 2.8 + UP * 1.0)

        label = Text(
            "THE DERIVATIVE", font_size=HEADING_SIZE,
            color=ACCENT, font=SANS, weight=BOLD,
        )
        label.next_to(fb, UP, buff=0.3)

        self.play(Write(label), run_time=NORMAL)
        self.play(Write(deriv_def), run_time=SLOW)
        self.wait(1.0)

        # Back to car analogy
        self.add_subcaption(
            "Your speed at a single instant equals "
            "the derivative of your position function at that instant.",
            duration=8,
        )
        analogy = Text(
            "Speed at t = 3 = derivative of position at t = 3",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(analogy, direction=DOWN, anchor=fb, buff=1.2)
        self.play(FadeIn(analogy, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 5: Notation ───────────────────────────────────────────
    def scene5_notation(self):
        self.add_subcaption(
            "Two notations for the same idea: "
            "Leibniz writes dy over dx, Lagrange writes f prime of x.",
            duration=8,
        )
        self.ly.section_divider(4, "Notation")

        title = self.ly.title("Two Ways to Write It")

        # Two-column layout: Leibniz vs Lagrange
        leibniz_items = [
            Text("Leibniz", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
            MathTex(r"\frac{\Delta y}{\Delta x}", font_size=BODY_SIZE, color=DIM),
            MathTex(r"\downarrow", font_size=BODY_SIZE, color=ACCENT),
            MathTex(r"\frac{dy}{dx}", font_size=BODY_SIZE, color=PRIMARY),
        ]
        lagrange_items = [
            Text("Lagrange", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
            MathTex(r"f'(x)", font_size=48, color=PRIMARY),
            Text('"f-prime of x"', font_size=LABEL_SIZE, color=DIM, font=SANS),
        ]

        left_col, right_col = self.ly.two_columns(
            leibniz_items, lagrange_items,
            start_from=title,
        )
        self.play(FadeIn(left_col, shift=RIGHT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeIn(right_col, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Equivalence symbol
        equiv = MathTex(r"\equiv", font_size=36, color=ACCENT)
        equiv.move_to(DOWN * 1.5)
        equiv_label = Text(
            "Same thing", font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        equiv_label.next_to(equiv, DOWN, buff=0.3)

        self.play(Write(equiv), Write(equiv_label), run_time=FAST)
        self.wait(1.0)

        # Higher derivatives — progressive reveal (3 items, under budget)
        self.add_subcaption(
            "Both notations extend to higher derivatives: "
            "second derivative, third derivative, and so on.",
            duration=7,
        )
        higher = VGroup(
            MathTex(r"f''(x),\ f'''(x)", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(
                r"\frac{d^2y}{dx^2},\ \frac{d^3y}{dx^3}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
        ).arrange(DOWN, buff=0.3)
        self.ly.safe_place(higher, direction=DOWN, anchor=equiv_label, buff=0.6)
        self.play(Write(higher), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 6: First Example — f(x) = x² ─────────────────────────
    def scene6_example(self):
        self.add_subcaption(
            "Let's compute the derivative of x squared using the limit definition.",
            duration=7,
        )
        self.ly.section_divider(5, "Example: f(x) = x²")

        # Derivation steps — progressive reveal enforces 5-item budget
        # As new steps appear, oldest ones fade out automatically
        steps = [
            MathTex(
                r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}",
                font_size=LABEL_SIZE,
            ),
            MathTex(
                r"= \lim_{h \to 0} \frac{(x+h)^2 - x^2}{h}",
                font_size=LABEL_SIZE,
            ),
            MathTex(
                r"= \lim_{h \to 0} \frac{x^2 + 2xh + h^2 - x^2}{h}",
                font_size=LABEL_SIZE,
            ),
            MathTex(
                r"= \lim_{h \to 0} \frac{2xh + h^2}{h}",
                font_size=LABEL_SIZE,
            ),
            MathTex(
                r"= \lim_{h \to 0} (2x + h)",
                font_size=LABEL_SIZE,
            ),
            MathTex(
                r"= 2x",
                font_size=HEADING_SIZE, color=ACCENT,
            ),
        ]

        title = self.ly.title("Derivative of x²")
        self.ly.progressive_reveal(
            steps, start_from=title,
            spacing=0.35,
            anim_kwargs={"shift": LEFT * 0.15},
        )

        # Now show graph with tangent lines to verify visually
        self.add_subcaption(
            "The tangent line at x equals 1 has slope 2. "
            "At x equals 3, the slope is 6.",
            duration=7,
        )
        self.ly.clear()

        # Graph verification — separate sub-scene
        axes = Axes(
            x_range=[-1, 4, 1], y_range=[-1, 10, 2],
            x_length=4.5, y_length=3.5,
            axis_config={"color": DIM, "include_numbers": True},
        )
        axes.shift(LEFT * 2.0 + DOWN * 0.3)
        curve = axes.plot(
            lambda x: x**2, x_range=[-0.5, 3.2],
            color=PRIMARY, stroke_width=3,
        )

        self.play(Create(axes), Create(curve), run_time=NORMAL)

        # Tangent at x=1, slope=2
        t1 = axes.plot(
            lambda x: 2 * x - 1, x_range=[0, 2.5],
            color=SECONDARY, stroke_width=2,
        )
        dot1 = Dot(axes.c2p(1, 1), color=SECONDARY, radius=0.08)
        lbl1 = MathTex(r"m=2", font_size=LABEL_SIZE, color=SECONDARY)
        lbl1.next_to(dot1, UP, buff=0.2)

        self.play(Create(t1), FadeIn(dot1), Write(lbl1), run_time=NORMAL)
        self.wait(0.5)

        # Tangent at x=3, slope=6
        t3 = axes.plot(
            lambda x: 6 * x - 9, x_range=[1.5, 3.5],
            color=ACCENT, stroke_width=2,
        )
        dot3 = Dot(axes.c2p(3, 9), color=ACCENT, radius=0.08)
        lbl3 = MathTex(r"m=6", font_size=LABEL_SIZE, color=ACCENT)
        lbl3.next_to(dot3, UP, buff=0.2)

        self.play(Create(t3), FadeIn(dot3), Write(lbl3), run_time=NORMAL)
        self.wait(0.5)

        # Result highlight
        result = Text(
            "f'(x) = 2x", font_size=HEADING_SIZE,
            color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(result, direction=RIGHT, anchor=None)
        self.play(Write(result), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 7: Recap + Preview ────────────────────────────────────
    def scene7_recap(self):
        self.add_subcaption(
            "The derivative captures instantaneous change. "
            "Next time: the power rule and beyond.",
            duration=8,
        )

        title = self.ly.title("What We Learned")

        bullets = [
            Text(
                "The derivative = slope of the tangent line",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "It's the limit of secant line slopes",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            MathTex(
                r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            Text(
                "The derivative of x² is 2x",
                font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
            ),
        ]
        self.ly.progressive_reveal(
            bullets, start_from=title,
            anim_kwargs={"shift": LEFT * 0.15},
        )

        self.wait(1.0)
        play_outro(self, "The Power Rule", "Calculus I")
