"""
Video 08: Mean Value Theorem & Applications
Calculus I — Rolle's Theorem, MVT, increasing/decreasing, First Derivative Test.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, proper narration timing, SANS font for body.

Render draft:  manim -ql scripts/pre-university/video-08-mvt-applications.py Video08_MVTApplications
Render final:  manim -qh scripts/pre-university/video-08-mvt-applications.py Video08_MVTApplications

QUALITY RULES (enforced):
  1. Max 5 visible elements per scene at any time
  2. Use LayoutEngine for ALL text/formula positioning — no raw .shift() or .to_edge()
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


class Video08_MVTApplications(Scene):
    """Full video: 8 scenes — speeding ticket hook, MVT visual, Rolle's, proof, inc/dec, 1st deriv test."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_visual_mvt()
        self.scene3_rolle()
        self.scene4_proof_intuition()
        self.scene5_increasing_decreasing()
        self.scene6_first_derivative_test()
        self.scene7_recap()

    # ── Scene 1: Hook — The Speeding Ticket ────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "If you drive 60 miles in exactly 1 hour, "
            "your average speed is 60 mph. "
            "At some instant, your speedometer read exactly 60.",
            duration=8,
        )
        play_intro(self, "Mean Value Theorem", "Calculus I")

        self.add_subcaption(
            "This everyday observation is actually a deep mathematical theorem.",
            duration=4,
        )

        scenario = Text(
            "You drive 60 miles in 1 hour.",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(scenario, anchor=None)
        self.play(Write(scenario), run_time=NORMAL)
        self.wait(0.5)

        avg = MathTex(
            r"\text{Average} = \frac{60}{1} = 60 \text{ mph}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(avg, direction=DOWN, anchor=scenario, buff=0.5)
        self.play(Write(avg), run_time=NORMAL)
        self.wait(0.5)

        conclusion = Text(
            "At some instant, speedometer = 60 mph",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(conclusion, direction=DOWN, anchor=avg, buff=0.5)
        self.play(Write(conclusion), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 2: Visual — Secant and Tangent ──────────────────
    def scene2_visual_mvt(self):
        self.add_subcaption(
            "For any smooth curve connecting two points, "
            "there is always a point where the tangent line "
            "is parallel to the secant line between the endpoints.",
            duration=8,
        )

        self.ly.section_divider(1, "The Geometric Picture")

        # Create graph
        axes = Axes(
            x_range=[0, 4, 1], y_range=[0, 5, 1],
            x_length=7, y_length=4.5,
            axis_config={"color": DIM, "include_numbers": True},
        )
        self.ly.center_in_content(axes)
        self.play(Create(axes), run_time=NORMAL)

        # Curve
        curve = axes.plot(lambda x: 0.3 * x**2 - 0.2 * x + 0.9,
                          x_range=[1, 3], color=PRIMARY, stroke_width=3)
        self.play(Create(curve), run_time=NORMAL)
        self.wait(0.3)

        # Endpoint dots
        a_point = axes.c2p(1, 1.0)
        b_point = axes.c2p(3, 4.0)
        dot_a = Dot(a_point, color=SECONDARY, radius=0.08)
        dot_b = Dot(b_point, color=SECONDARY, radius=0.08)
        self.play(FadeIn(dot_a), FadeIn(dot_b), run_time=FAST)
        self.wait(0.3)

        # Secant line
        secant = Line(a_point, b_point, color=DIM, stroke_width=2)
        self.play(Create(secant), run_time=NORMAL)
        self.wait(0.3)

        # Tangent at c (slope = 1.5, x ≈ 2.83)
        c_val = 17 / 6
        c_y = 0.3 * c_val**2 - 0.2 * c_val + 0.9
        c_point = axes.c2p(c_val, c_y)
        dot_c = Dot(c_point, color=ACCENT, radius=0.1)
        self.play(FadeIn(dot_c), run_time=FAST)

        tangent_len = 1.0
        t_start = axes.c2p(c_val - tangent_len, c_y - 1.5 * tangent_len)
        t_end = axes.c2p(c_val + tangent_len, c_y + 1.5 * tangent_len)
        tangent = Line(t_start, t_end, color=ACCENT, stroke_width=3)
        self.play(Create(tangent), run_time=NORMAL)
        self.wait(0.5)

        # Remove graph, show formula
        self.play(FadeOut(axes), FadeOut(curve), FadeOut(dot_a), FadeOut(dot_b),
                  FadeOut(secant), FadeOut(dot_c), FadeOut(tangent), run_time=0.3)

        result = MathTex(
            r"f'(c) = \frac{f(b) - f(a)}{b - a}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(result, color=ACCENT)
        self.play(Write(result), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 3: Rolle's Theorem ────────────────────────────────
    def scene3_rolle(self):
        self.add_subcaption(
            "Rolle's Theorem is a special case where "
            "f of a equals f of b. "
            "There must be a point where the tangent is horizontal.",
            duration=8,
        )

        self.ly.section_divider(2, "Rolle's Theorem")

        # Statement — progressive reveal
        lines = [
            Text("If f is continuous on [a,b], differentiable on (a,b),",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("and f(a) = f(b),",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("then ∃ c ∈ (a,b) such that f'(c) = 0",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(lines, start_from=None, run_time=FAST)
        self.wait(0.5)

        # Show result boxed
        self.play(FadeOut(lines[0]), FadeOut(lines[1]), run_time=0.3)

        rolle_result = MathTex(
            r"f(a) = f(b) \implies f'(c) = 0",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(rolle_result, color=ACCENT)
        self.play(Write(rolle_result), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 4: Proof Intuition ──────────────────────────────
    def scene4_proof_intuition(self):
        self.add_subcaption(
            "To prove the MVT, subtract the secant line from the function. "
            "Apply Rolle's Theorem to the result.",
            duration=8,
        )

        self.ly.section_divider(3, "Proof Intuition")

        secant_eq = MathTex(
            r"L(x) = f(a) + \frac{f(b)-f(a)}{b-a}(x - a)",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(secant_eq, anchor=None)
        self.play(Write(secant_eq), run_time=NORMAL)
        self.wait(0.5)

        g_def = MathTex(
            r"g(x) = f(x) - L(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(g_def, direction=DOWN, anchor=secant_eq, buff=0.5)
        self.play(Write(g_def), run_time=NORMAL)
        self.wait(0.3)

        # Key: g(a) = g(b) = 0
        check = MathTex(
            r"g(a) = g(b) = 0 \implies g'(c) = 0",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(check, direction=DOWN, anchor=g_def, buff=0.4)
        self.play(Write(check), run_time=NORMAL)
        self.wait(0.5)

        # Unroll to get MVT
        self.play(FadeOut(secant_eq), FadeOut(g_def), FadeOut(check), run_time=0.3)

        final = MathTex(
            r"f'(c) = \frac{f(b) - f(a)}{b - a}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(final, color=ACCENT)
        self.play(Write(final), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 5: Increasing/Decreasing ────────────────────────
    def scene5_increasing_decreasing(self):
        self.add_subcaption(
            "If f prime is positive, the function increases. "
            "If f prime is negative, it decreases. "
            "Where f prime is zero, we have critical points.",
            duration=8,
        )

        self.ly.section_divider(4, "Increasing & Decreasing")

        rules = [
            Text("f'(x) > 0  →  f is increasing", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("f'(x) < 0  →  f is decreasing", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("f'(x) = 0  →  critical point", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(rules, start_from=None, run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 6: First Derivative Test ────────────────────────
    def scene6_first_derivative_test(self):
        self.add_subcaption(
            "The First Derivative Test classifies critical points "
            "by checking sign changes in the derivative.",
            duration=6,
        )

        self.ly.section_divider(5, "First Derivative Test")

        test_rules = [
            Text("f' changes + → −  →  local maximum", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("f' changes − → +  →  local minimum", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("f' does not change  →  neither", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(test_rules, start_from=None, run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 7: Recap + Outro ─────────────────────────────────
    def scene7_recap(self):
        self.add_subcaption(
            "Today we covered Rolle's Theorem, the Mean Value Theorem, "
            "increasing and decreasing functions, "
            "and the First Derivative Test.",
            duration=6,
        )

        title = self.ly.title("Summary")

        recap = [
            Text("Rolle: f(a)=f(b) → f'(c)=0", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("MVT: f'(c) = [f(b)−f(a)] / (b−a)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("f'>0: increasing, f'<0: decreasing", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("1st Derivative Test classifies extrema", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(recap, start_from=title, run_time=FAST)
        self.wait(1.0)

        play_outro(self, "Concavity & 2nd Derivative", "Calculus I")
