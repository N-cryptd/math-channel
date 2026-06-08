"""
Video 07: Trigonometric Derivatives
Calculus I — derivatives of sin(x), cos(x), tan(x), and more.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, proper narration timing, SANS font for body.

Render draft:  manim -ql scripts/pre-university/video-07-trig-derivatives.py Video07_TrigonometricDerivatives
Render final:  manim -qh scripts/pre-university/video-07-trig-derivatives.py Video07_TrigonometricDerivatives

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


class Video07_TrigonometricDerivatives(Scene):
    """Full video: 8 scenes — special limits, sin, cos, other trig derivatives."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_special_limit_1()
        self.scene3_special_limit_2()
        self.scene4_derivative_sin()
        self.scene5_derivative_cos()
        self.scene6_other_trig()
        self.scene7_examples()
        self.scene8_recap()

    # ── Scene 1: Hook ────────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "What is the derivative of sine x? "
            "We need the limit definition and two special limits.",
            duration=6,
        )
        play_intro(self, "Trigonometric Derivatives", "Calculus I")

        self.add_subcaption(
            "To differentiate sine x, we use the limit definition. "
            "But first, we need two fundamental trigonometric limits.",
            duration=8,
        )

        title = self.ly.title("The Goal")
        self.wait(0.3)

        question = MathTex(
            r"\frac{d}{dx}[\sin(x)] = \;?",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(question, anchor=None)
        self.play(Write(question), run_time=NORMAL)
        self.wait(0.5)

        # The two special limits we need
        limit1 = MathTex(
            r"\lim_{h \to 0} \frac{\sin(h)}{h} = 1",
            font_size=BODY_SIZE, color=ACCENT,
        )
        limit2 = MathTex(
            r"\lim_{h \to 0} \frac{\cos(h) - 1}{h} = 0",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(limit1, direction=DOWN, anchor=question, buff=0.6)
        self.ly.safe_place(limit2, direction=DOWN, anchor=limit1, buff=0.3)
        self.play(Write(limit1), run_time=FAST)
        self.play(Write(limit2), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 2: Special Limit #1 — sin(h)/h → 1 ────────────────
    def scene2_special_limit_1(self):
        self.add_subcaption(
            "The first special limit: sine h over h approaches 1 as h goes to zero. "
            "We see this geometrically on the unit circle.",
            duration=8,
        )

        self.ly.section_divider(1, "Special Limit #1")

        # Geometric argument: unit circle
        circle = Circle(radius=1.5, color=WHITE, stroke_width=2)
        self.ly.center_in_content(circle)
        h_angle = 0.5

        # Angle arc
        arc = Arc(radius=0.4, start_angle=0, angle=h_angle, color=ACCENT, arc_center=circle.get_center())
        h_label = MathTex(r"h", font_size=LABEL_SIZE, color=ACCENT)
        self.ly.safe_place(h_label, direction=RIGHT, anchor=arc, buff=0.1)

        # sin(h) vertical line
        p_on_circle = circle.get_center() + RIGHT * 1.5 * np.cos(h_angle) + UP * 1.5 * np.sin(h_angle)
        p_base = circle.get_center() + RIGHT * 1.5 * np.cos(h_angle)
        sin_line = Line(p_base, p_on_circle, color=SECONDARY, stroke_width=3)
        sin_label = MathTex(r"\sin(h)", font_size=LABEL_SIZE, color=SECONDARY)
        self.ly.safe_place(sin_label, direction=RIGHT, anchor=sin_line, buff=0.1)

        self.play(Create(circle), run_time=NORMAL)
        self.play(Create(arc), Write(h_label), run_time=FAST)
        self.play(Create(sin_line), Write(sin_label), run_time=FAST)
        self.wait(0.5)

        # Key insight text
        self.play(FadeOut(circle), FadeOut(arc), FadeOut(h_label),
                  FadeOut(sin_line), FadeOut(sin_label), run_time=0.3)

        insight = Text(
            "For small h: arc length ≈ sin(h)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(insight)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)
        self.play(FadeOut(insight), run_time=0.3)

        result = MathTex(
            r"\lim_{h \to 0} \frac{\sin(h)}{h} = 1",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(result, color=ACCENT)
        self.play(Write(result), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 3: Special Limit #2 — (cos h - 1)/h → 0 ───────────
    def scene3_special_limit_2(self):
        self.add_subcaption(
            "The second special limit uses a trick. "
            "Multiply by the conjugate to show it equals zero.",
            duration=6,
        )

        self.ly.section_divider(2, "Special Limit #2")

        limit = MathTex(
            r"\lim_{h \to 0} \frac{\cos(h) - 1}{h} = 0",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(limit, anchor=None)
        self.play(Write(limit), run_time=NORMAL)
        self.wait(0.5)

        # Multiply by conjugate
        self.add_subcaption(
            "Multiply numerator and denominator by cos h plus 1. "
            "Then use the Pythagorean identity.",
            duration=8,
        )
        trick = MathTex(
            r"\frac{\cos(h)-1}{h} \cdot \frac{\cos(h)+1}{\cos(h)+1}"
            r" = \frac{-\sin^2(h)}{h(\cos(h)+1)}",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(trick, direction=DOWN, anchor=limit, buff=0.5)
        self.play(Write(trick), run_time=NORMAL)
        self.wait(0.5)

        # Apply the limit
        result = MathTex(
            r"= \frac{\sin(h)}{h} \cdot \frac{-\sin(h)}{\cos(h)+1}"
            r" \to 1 \cdot 0 = 0",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=trick, buff=0.4)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 4: Derivative of sin(x) ────────────────────────────
    def scene4_derivative_sin(self):
        self.add_subcaption(
            "Using the angle addition formula and the two special limits, "
            "we prove the derivative of sine x is cosine x.",
            duration=8,
        )

        self.ly.section_divider(3, r"d/dx$[\sin(x)] = \cos(x)$")

        # Angle addition identity
        identity = MathTex(
            r"\sin(x+h) = \sin(x)\cos(h) + \cos(x)\sin(h)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(identity, anchor=None)
        self.play(Write(identity), run_time=NORMAL)
        self.wait(0.5)

        # Apply limits
        self.add_subcaption(
            "Substitute into the limit definition. "
            "Group the sin x and cos x terms and apply our special limits.",
            duration=8,
        )
        step = MathTex(
            r"= \sin(x) \cdot 0 + \cos(x) \cdot 1 = \cos(x)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step, direction=DOWN, anchor=identity, buff=0.5)
        self.play(Write(step), run_time=NORMAL)
        self.wait(0.5)

        # Box the result
        self.play(FadeOut(identity), FadeOut(step), run_time=0.3)

        result = MathTex(
            r"\frac{d}{dx}[\sin(x)] = \cos(x)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(result, color=ACCENT)
        self.play(Write(result), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 5: Derivative of cos(x) ────────────────────────────
    def scene5_derivative_cos(self):
        self.add_subcaption(
            "By the same method, the derivative of cosine x is negative sine x.",
            duration=6,
        )

        self.ly.section_divider(4, r"d/dx$[\cos(x)] = -\sin(x)$")

        identity = MathTex(
            r"\cos(x+h) = \cos(x)\cos(h) - \sin(x)\sin(h)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(identity, anchor=None)
        self.play(Write(identity), run_time=NORMAL)
        self.wait(0.5)

        step = MathTex(
            r"= \cos(x) \cdot 0 - \sin(x) \cdot 1 = -\sin(x)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step, direction=DOWN, anchor=identity, buff=0.5)
        self.play(Write(step), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(identity), FadeOut(step), run_time=0.3)

        result = MathTex(
            r"\frac{d}{dx}[\cos(x)] = -\sin(x)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(result, color=ACCENT)
        self.play(Write(result), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 6: Other Trig Derivatives ───────────────────────────
    def scene6_other_trig(self):
        self.add_subcaption(
            "Using the quotient rule with sine and cosine, "
            "we derive all six trigonometric derivatives.",
            duration=8,
        )

        self.ly.section_divider(5, "All Six Trig Derivatives")

        # Derive tan(x) quickly
        tan_expr = MathTex(
            r"\tan(x) = \frac{\sin(x)}{\cos(x)}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(tan_expr, anchor=None)
        self.play(Write(tan_expr), run_time=NORMAL)
        self.wait(0.5)

        tan_result = MathTex(
            r"\frac{d}{dx}[\tan(x)] = \sec^2(x)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(tan_result, direction=DOWN, anchor=tan_expr, buff=0.4)
        self.play(Write(tan_result), run_time=NORMAL)
        self.wait(0.5)

        # Full table via progressive reveal
        self.add_subcaption(
            "Here are all six trigonometric derivatives at a glance. "
            "Notice the patterns: cofunction derivatives have negative signs.",
            duration=8,
        )
        self.play(FadeOut(tan_expr), FadeOut(tan_result), run_time=0.3)

        derivs = [
            MathTex(r"d/dx[\sin(x)] = \cos(x)", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"d/dx[\cos(x)] = -\sin(x)", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"d/dx[\tan(x)] = \sec^2(x)", font_size=BODY_SIZE, color=ACCENT),
            MathTex(r"d/dx[\cot(x)] = -\csc^2(x)", font_size=BODY_SIZE, color=DIM),
            MathTex(r"d/dx[\sec(x)] = \sec(x)\tan(x)", font_size=BODY_SIZE, color=DIM),
            MathTex(r"d/dx[\csc(x)] = -\csc(x)\cot(x)", font_size=BODY_SIZE, color=DIM),
        ]
        self.ly.progressive_reveal(derivs, start_from=None, run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 7: Chain Rule Examples ─────────────────────────────
    def scene7_examples(self):
        self.add_subcaption(
            "Let's practice applying the chain rule with trig functions.",
            duration=4,
        )

        self.ly.section_divider(6, "Chain Rule Examples")

        # Example 1: sin(3x)
        self.add_subcaption(
            "Example 1: the derivative of sine of 3x is 3 cosine of 3x.",
            duration=6,
        )
        ex1 = MathTex(
            r"\frac{d}{dx}[\sin(3x)] = \cos(3x) \cdot 3 = 3\cos(3x)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex1, anchor=None)
        self.play(Write(ex1), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(ex1), run_time=0.3)

        # Example 2: x²·sin(x) — product rule
        self.add_subcaption(
            "Example 2: use the product rule for x squared sine x.",
            duration=6,
        )
        ex2 = MathTex(
            r"\frac{d}{dx}[x^2 \sin(x)] = 2x\sin(x) + x^2\cos(x)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex2, anchor=None)
        self.play(Write(ex2), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(ex2), run_time=0.3)

        # Example 3: tan(2x+1)
        self.add_subcaption(
            "Example 3: chain rule on tangent of 2x plus 1.",
            duration=6,
        )
        ex3 = MathTex(
            r"\frac{d}{dx}[\tan(2x+1)] = \sec^2(2x+1) \cdot 2 = 2\sec^2(2x+1)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex3, anchor=None)
        self.play(Write(ex3), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 8: Recap + Outro ────────────────────────────────────
    def scene8_recap(self):
        self.add_subcaption(
            "Today we derived all six trigonometric derivatives. "
            "Next up: the Mean Value Theorem.",
            duration=6,
        )

        title = self.ly.title("Summary")

        recap = [
            MathTex(r"d/dx[\sin(x)] = \cos(x)", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"d/dx[\cos(x)] = -\sin(x)", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"d/dx[\tan(x)] = \sec^2(x)", font_size=BODY_SIZE, color=WHITE),
            Text("Cofunctions get negative signs", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(recap, start_from=title, run_time=FAST)
        self.wait(1.0)

        play_outro(self, "Mean Value Theorem", "Calculus I")
