"""
Video 11: L'Hopital's Rule
Calculus I — indeterminate forms, L'Hopital's rule, examples.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, proper narration timing, SANS font for body.

Render draft:  manim -ql scripts/pre-university/video-11-lhopital.py Video11_LHopital
Render final:  manim -qh scripts/pre-university/video-11-lhopital.py Video11_LHopital

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


class Video11_LHopital(Scene):
    """Full video: 6 scenes — hook, indeterminate forms, the rule, examples, advanced forms, recap."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_indeterminate_forms()
        self.scene3_the_rule()
        self.scene4_example1()
        self.scene5_example2()
        self.scene6_advanced_forms()
        self.scene7_recap()

    # ── Scene 1: Hook ───────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "What is the limit of sine x over x as x approaches zero? "
            "Both numerator and denominator go to zero — indeterminate!",
            duration=6,
        )
        play_intro(self, "L'Hopital's Rule", "Calculus I")

        self.add_subcaption(
            "L'Hopital's Rule turns indeterminate forms into solvable limits "
            "by differentiating the top and bottom separately.",
            duration=6,
        )

        problem = MathTex(
            r"\lim_{x \to 0} \frac{\sin(x)}{x} = \frac{0}{0} = \; ?",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        answer = Text(
            "Differentiate top and bottom to solve!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(answer, direction=DOWN, anchor=problem, buff=0.5)
        self.play(Write(answer), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 2: Indeterminate Forms ──────────────────────────────
    def scene2_indeterminate_forms(self):
        self.add_subcaption(
            "Zero over one is zero, five over zero is infinity, but "
            "zero over zero and infinity over infinity are indeterminate. "
            "The answer depends on the rates.",
            duration=8,
        )

        self.ly.section_divider(1, "Indeterminate Forms")

        not_indet = MathTex(
            r"\frac{0}{1} = 0, \quad \frac{5}{0} = \infty, \quad \frac{1}{\infty} = 0",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(not_indet, anchor=None)
        label_not = Text(
            "NOT indeterminate — these have definite answers:",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(label_not, direction=UP, anchor=not_indet, buff=0.4)
        self.play(FadeIn(label_not), run_time=FAST)
        self.play(Write(not_indet), run_time=NORMAL)
        self.wait(0.5)

        self.ly.clear()

        # Second part: indeterminate forms
        self.add_subcaption(
            "The indeterminate forms are zero over zero, infinity over infinity, "
            "zero times infinity, infinity minus infinity, and the power forms.",
            duration=8,
        )

        title2 = self.ly.title("The Indeterminate Forms")

        indet_formula = MathTex(
            r"\frac{0}{0}, \quad \frac{\infty}{\infty}, \quad 0 \cdot \infty, \quad \infty - \infty, \quad 1^{\infty}, \quad 0^0, \quad \infty^0",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(indet_formula, direction=DOWN, anchor=title2, buff=0.4)
        self.play(Write(indet_formula), run_time=NORMAL)
        self.wait(0.5)

        key = Text(
            "The answer depends on how FAST top and bottom change.",
            font_size=LABEL_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=indet_formula, buff=0.4)
        self.play(Write(key), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 3: The Rule ───────────────────────────────────────
    def scene3_the_rule(self):
        self.add_subcaption(
            "If the limit gives zero over zero or infinity over infinity, "
            "L'Hopital says the limit equals the limit of the derivatives.",
            duration=6,
        )

        self.ly.section_divider(2, "L'Hopital's Rule")

        condition = MathTex(
            r"\text{If } \lim_{x \to a} \frac{f(x)}{g(x)} = \frac{0}{0} \text{ or } \frac{\pm\infty}{\pm\infty}",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(condition, anchor=None)
        self.play(Write(condition), run_time=NORMAL)
        self.wait(0.5)

        result = MathTex(
            r"\Rightarrow \lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(result, color=ACCENT)
        self.ly.safe_place(result, direction=DOWN, anchor=condition, buff=0.5)
        self.play(Write(result), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

        # Caveats in separate sub-scene
        self.add_subcaption(
            "Key points: only works for indeterminate forms. "
            "Differentiate separately, not the quotient rule. "
            "Can apply repeatedly.",
            duration=8,
        )

        title3 = self.ly.title("Key Points")

        caveats = [
            Text("Only for 0/0 or inf/inf forms", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Differentiate top and bottom SEPARATELY", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD),
            Text("NOT the quotient rule!", font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD),
            Text("Apply repeatedly if still indeterminate", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(caveats, start_from=title3, run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 4: Example 1 — sin(x)/x ──────────────────────────
    def scene4_example1(self):
        self.add_subcaption(
            "Example one: limit of sine x over x as x approaches zero. "
            "Differentiating gives cosine x over one, which equals one.",
            duration=8,
        )

        self.ly.section_divider(3, r"Example 1: $\frac{\sin x}{x}$")

        problem = MathTex(
            r"\lim_{x \to 0} \frac{\sin(x)}{x} \; \left[ \frac{0}{0} \right]",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        step = MathTex(
            r"= \lim_{x \to 0} \frac{\cos(x)}{1} = \cos(0) = 1",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step, direction=DOWN, anchor=problem, buff=0.5)
        self.play(Write(step), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 5: Example 2 — x^2/e^x ──────────────────────────
    def scene5_example2(self):
        self.add_subcaption(
            "Example two: limit of x squared over e to the x as x goes to infinity. "
            "Infinity over infinity. Apply L'Hopital twice to get zero.",
            duration=8,
        )

        self.ly.section_divider(4, r"Example 2: $\frac{x^2}{e^x}$")

        problem = MathTex(
            r"\lim_{x \to \infty} \frac{x^2}{e^x} \; \left[ \frac{\infty}{\infty} \right]",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        step1 = MathTex(
            r"= \lim_{x \to \infty} \frac{2x}{e^x} \; \left[ \frac{\infty}{\infty} \right]",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=problem, buff=0.4)
        self.play(Write(step1), run_time=FAST)
        self.wait(0.5)

        step2 = MathTex(
            r"= \lim_{x \to \infty} \frac{2}{e^x} = 0",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.3)
        self.play(Write(step2), run_time=FAST)
        self.wait(0.5)

        insight = Text(
            "Exponentials always beat polynomials!",
            font_size=LABEL_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=step2, buff=0.4)
        self.play(Write(insight), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 6: Advanced Forms ──────────────────────────────────
    def scene6_advanced_forms(self):
        self.add_subcaption(
            "Other indeterminate forms can be converted. "
            "Rewrite products as quotients, differences with common denominators, "
            "and powers using exponentials and logarithms.",
            duration=8,
        )

        self.ly.section_divider(5, "Handling Other Forms")

        form1 = Text(
            "0 * inf: rewrite as a fraction",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(form1, anchor=None)
        self.play(Write(form1), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

        title6 = self.ly.title("Power Forms")

        power_formula = MathTex(
            r"f(x)^{g(x)} = e^{g(x) \cdot \ln(f(x))}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(power_formula, direction=DOWN, anchor=title6, buff=0.4)
        self.play(Write(power_formula), run_time=NORMAL)
        self.wait(0.5)

        steps = [
            Text("Take natural log of both sides", font_size=LABEL_SIZE, color=WHITE, font=SANS),
            Text("Apply L'Hopital to the exponent", font_size=LABEL_SIZE, color=SECONDARY, font=SANS),
            Text("Exponentiate back to get the answer", font_size=LABEL_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(steps, start_from=power_formula, run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 7: Recap + Outro ──────────────────────────────────
    def scene7_recap(self):
        self.add_subcaption(
            "L'Hopital's Rule solves indeterminate limits "
            "by differentiating top and bottom separately. "
            "Next: Introduction to Integration.",
            duration=6,
        )

        title = self.ly.title("Summary")

        recap = [
            Text("Only for 0/0 and inf/inf forms", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Differentiate top and bottom separately", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Can apply repeatedly", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Other forms: convert to 0/0 or inf/inf", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(recap, start_from=title, run_time=FAST)
        self.wait(1.0)

        play_outro(self, "Introduction to Integration", "Calculus I")
