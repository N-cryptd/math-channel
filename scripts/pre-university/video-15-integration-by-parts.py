"""
Video 15: Integration by Parts
Calculus I — the formula, LIATE rule, repeated application, tabular method.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, proper narration timing, SANS font for body.

Render draft:  manim -ql scripts/pre-university/video-15-integration-by-parts.py Video15_IntegrationByParts
Render final:  manim -qh scripts/pre-university/video-15-integration-by-parts.py Video15_IntegrationByParts

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


class Video15_IntegrationByParts(Scene):
    """Full video: 7 scenes — hook, formula, example, repeated, LIATE, recap."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_formula()
        self.scene3_example()
        self.scene4_repeated()
        self.scene5_liate()
        self.scene6_recap()

    # ── Scene 1: Hook ───────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "How do you integrate x times e to the x? "
            "Neither u-sub nor basic formulas work. "
            "Integration by parts splits the integrand and swaps the problem.",
            duration=6,
        )
        play_intro(self, "Integration by Parts", "Calculus I")

        problem = MathTex(
            r"\int x e^x \, dx = \; ?",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 2: The Formula ───────────────────────────────────
    def scene2_formula(self):
        self.add_subcaption(
            "From the product rule: u v equals integral u prime v dx "
            "plus integral u v prime dx. Rearranging gives "
            "integral u dv equals u v minus integral v du.",
            duration=8,
        )

        self.ly.section_divider(1, "The Formula")

        product_rule = MathTex(
            r"(uv)' = u'v + uv'",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(product_rule, anchor=None)
        self.play(Write(product_rule), run_time=FAST)
        self.wait(0.5)

        integral_form = MathTex(
            r"\Rightarrow \int u\,dv = uv - \int v\,du",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(integral_form, color=ACCENT)
        self.ly.safe_place(integral_form, direction=DOWN, anchor=product_rule, buff=0.5)
        self.play(Write(integral_form), run_time=SLOW)
        self.wait(0.5)

        note = Text(
            "Choose u and dv, then compute du and v",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=integral_form, buff=0.4)
        self.play(Write(note), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 3: Example — x e^x ────────────────────────────────
    def scene3_example(self):
        self.add_subcaption(
            "Let u equal x, dv equals e to the x dx. "
            "Then du equals dx and v equals e to the x. "
            "Apply: x e to the x minus integral of e to the x equals x e to the x minus e to the x.",
            duration=8,
        )

        self.ly.section_divider(2, r"Example: $\int x e^x\,dx$")

        problem = MathTex(
            r"\int x e^x\,dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        choice = MathTex(
            r"u = x, \quad dv = e^x\,dx \Rightarrow du = dx, \quad v = e^x",
            font_size=LABEL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(choice, direction=DOWN, anchor=problem, buff=0.4)
        self.play(Write(choice), run_time=FAST)
        self.wait(0.5)

        result = MathTex(
            r"= x e^x - \int e^x\,dx = x e^x - e^x + C = e^x(x-1) + C",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=choice, buff=0.4)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 4: Repeated Application ──────────────────────────
    def scene4_repeated(self):
        self.add_subcaption(
            "Sometimes apply integration by parts twice. "
            "Integral of x squared e to the x: apply twice, "
            "polynomial degree drops each time until it vanishes.",
            duration=8,
        )

        self.ly.section_divider(3, r"Repeated: $\int x^2 e^x\,dx$")

        problem = MathTex(
            r"\int x^2 e^x\,dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        step1 = MathTex(
            r"u{=}x^2, \; dv{=}e^x\,dx \Rightarrow x^2 e^x - \int 2x e^x\,dx",
            font_size=LABEL_SIZE, color=DIM,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=problem, buff=0.4)
        self.play(Write(step1), run_time=FAST)
        self.wait(0.5)

        step2 = MathTex(
            r"\text{Apply again: } = x^2 e^x - 2x e^x + 2e^x + C",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.4)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.5)

        final = MathTex(
            r"= e^x(x^2 - 2x + 2) + C",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(final, direction=DOWN, anchor=step2, buff=0.3)
        self.play(Write(final), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 5: LIATE Rule ───────────────────────────────────
    def scene5_liate(self):
        self.add_subcaption(
            "How to choose u? Use LIATE: Logarithmic, Inverse trig, "
            "Algebraic, Trig, Exponential. Pick u from the highest on the list.",
            duration=6,
        )

        self.ly.section_divider(4, "The LIATE Rule")

        liate = Text(
            "LIATE",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(liate, anchor=None)
        self.play(Write(liate), run_time=SLOW)
        self.wait(0.5)

        items = [
            Text("L — Logarithmic", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("I — Inverse trig", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("A — Algebraic (polynomials)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("T — Trigonometric", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("E — Exponential", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=liate, run_time=FAST)
        self.wait(0.5)

        rule = Text(
            "Pick u from the HIGHEST type in the integrand",
            font_size=LABEL_SIZE, color=WHITE, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(rule, direction=DOWN, anchor=None, buff=0.4)
        self.play(Write(rule), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 6: Recap + Outro ─────────────────────────────────
    def scene6_recap(self):
        self.add_subcaption(
            "Integration by parts: integral u dv equals u v minus integral v du. "
            "Use LIATE to choose u. May need repeated application. "
            "Next: Applications of Integrals.",
            duration=6,
        )

        title = self.ly.title("Summary")

        recap = [
            MathTex(r"\int u\,dv = uv - \int v\,du", font_size=BODY_SIZE, color=WHITE),
            Text("LIATE rule for choosing u", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("May apply multiple times", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(recap, start_from=title, run_time=FAST)
        self.wait(1.0)

        play_outro(self, "Applications of Integrals", "Calculus I")
