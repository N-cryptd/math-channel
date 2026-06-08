"""
Video 13: Antiderivatives & Basic Integration
Calculus I — power rule for integrals, basic antiderivatives, definite integrals.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, proper narration timing, SANS font for body.

Render draft:  manim -ql scripts/pre-university/video-13-antiderivatives.py Video13_Antiderivatives
Render final:  manim -qh scripts/pre-university/video-13-antiderivatives.py Video13_Antiderivatives

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


class Video13_Antiderivatives(Scene):
    """Full video: 6 scenes — hook, definition, power rule, formulas, examples, recap."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_power_rule()
        self.scene4_formulas()
        self.scene5_examples()
        self.scene6_recap()

    # ── Scene 1: Hook ───────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Differentiation takes a function to its rate of change. "
            "Antidifferentiation reverses this: from the rate of change, "
            "find the original function.",
            duration=6,
        )
        play_intro(self, "Antiderivatives", "Calculus I")

        deriv = MathTex(
            r"x^2 \xrightarrow{\frac{d}{dx}} 2x",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(deriv, anchor=None)
        self.play(Write(deriv), run_time=NORMAL)
        self.wait(0.5)

        antid = MathTex(
            r"2x \xleftarrow{\int} x^2",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(antid, direction=DOWN, anchor=deriv, buff=0.5)
        self.play(Write(antid), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 2: What is an Antiderivative? ────────────────────
    def scene2_definition(self):
        self.add_subcaption(
            "An antiderivative of f is a function F where F prime equals f. "
            "Antiderivatives differ by a constant, since derivatives kill constants.",
            duration=6,
        )

        self.ly.section_divider(1, "What is an Antiderivative?")

        definition = MathTex(
            r"F'(x) = f(x) \iff F(x) = \int f(x)\,dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(definition, anchor=None)
        self.play(Write(definition), run_time=NORMAL)
        self.wait(0.5)

        note = MathTex(
            r"\frac{d}{dx}[x^2 + 3] = 2x, \quad \frac{d}{dx}[x^2 - 7] = 2x",
            font_size=LABEL_SIZE, color=DIM,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=definition, buff=0.4)
        self.play(Write(note), run_time=FAST)
        self.wait(0.5)

        key = Text(
            "Derivative kills constants — always add +C",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=note, buff=0.4)
        self.play(Write(key), run_time=FAST)
        self.wait(0.5)

        result = MathTex(
            r"\int 2x\,dx = x^2 + C",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(result, color=ACCENT)
        self.ly.safe_place(result, direction=DOWN, anchor=key, buff=0.4)
        self.play(Write(result), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 3: Power Rule ────────────────────────────────────
    def scene3_power_rule(self):
        self.add_subcaption(
            "The power rule for integration: the integral of x to the n "
            "equals x to the n plus 1 over n plus 1, plus C, for n not negative 1.",
            duration=6,
        )

        self.ly.section_divider(2, "Power Rule for Integration")

        rule = MathTex(
            r"\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(rule, color=ACCENT)
        self.ly.safe_place(rule, anchor=None)
        self.play(Write(rule), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

        # Examples
        self.add_subcaption(
            "Examples: integral of x cubed, square root of x, and one over x squared.",
            duration=5,
        )

        title3 = self.ly.title("Examples")

        ex1 = MathTex(
            r"\int x^3 \, dx = \frac{x^4}{4} + C",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex1, direction=DOWN, anchor=title3, buff=0.4)
        self.play(Write(ex1), run_time=NORMAL)
        self.wait(0.5)

        ex2 = MathTex(
            r"\int \sqrt{x} \, dx = \frac{2}{3}x^{3/2} + C",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex2, direction=DOWN, anchor=ex1, buff=0.3)
        self.play(Write(ex2), run_time=NORMAL)
        self.wait(0.5)

        ex3 = MathTex(
            r"\int \frac{1}{x^2} \, dx = -\frac{1}{x} + C",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex3, direction=DOWN, anchor=ex2, buff=0.3)
        self.play(Write(ex3), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 4: Basic Formulas ────────────────────────────────
    def scene4_formulas(self):
        self.add_subcaption(
            "Key formulas: integral of one over x is natural log of absolute x. "
            "Exponentials integrate to themselves. Trig integrals follow from derivatives.",
            duration=6,
        )

        self.ly.section_divider(3, "Basic Integration Formulas")

        formulas = [
            MathTex(r"\int \frac{1}{x}\,dx = \ln|x| + C", font_size=BODY_SIZE, color=ACCENT),
            MathTex(r"\int e^x\,dx = e^x + C", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"\int \sin(x)\,dx = -\cos(x) + C", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"\int \cos(x)\,dx = \sin(x) + C", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"\int \sec^2(x)\,dx = \tan(x) + C", font_size=BODY_SIZE, color=DIM),
        ]
        self.ly.progressive_reveal(formulas, start_from=None, run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 5: Definite Integrals via FTC ─────────────────────
    def scene5_examples(self):
        self.add_subcaption(
            "Use the Fundamental Theorem to evaluate definite integrals. "
            "Find the antiderivative, plug in bounds, subtract. "
            "The constant C cancels out.",
            duration=8,
        )

        self.ly.section_divider(4, "Definite Integrals via FTC")

        ex1 = MathTex(
            r"\int_0^3 x^2\,dx = \left[\frac{x^3}{3}\right]_0^3 = 9 - 0 = 9",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex1, anchor=None)
        self.play(Write(ex1), run_time=NORMAL)
        self.wait(0.5)

        ex2 = MathTex(
            r"\int_1^4 \sqrt{x}\,dx = \left[\frac{2}{3}x^{3/2}\right]_1^4 = \frac{14}{3}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex2, direction=DOWN, anchor=ex1, buff=0.5)
        self.play(Write(ex2), run_time=NORMAL)
        self.wait(0.5)

        note = Text(
            "+C cancels in definite integrals! Only indefinite need it.",
            font_size=LABEL_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=ex2, buff=0.4)
        self.play(Write(note), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 6: Recap + Outro ────────────────────────────────
    def scene6_recap(self):
        self.add_subcaption(
            "Antiderivatives reverse differentiation with a plus C. "
            "The Fundamental Theorem computes definite integrals. "
            "Next: u-substitution.",
            duration=6,
        )

        title = self.ly.title("Summary")

        recap = [
            MathTex(r"\int x^n\,dx = \frac{x^{n+1}}{n+1} + C", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"\int \frac{1}{x}\,dx = \ln|x| + C", font_size=BODY_SIZE, color=WHITE),
            Text("Definite: F(b) - F(a), C cancels", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(recap, start_from=title, run_time=FAST)
        self.wait(1.0)

        play_outro(self, "U-Substitution", "Calculus I")
