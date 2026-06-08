"""
Video 14: u-Substitution
Calculus I — the reverse chain rule, recognizing patterns, definite integrals with u-sub.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, proper narration timing, SANS font for body.

Render draft:  manim -ql scripts/pre-university/video-14-u-substitution.py Video14_USubstitution
Render final:  manim -qh scripts/pre-university/video-14-u-substitution.py Video14_USubstitution

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


class Video14_USubstitution(Scene):
    """Full video: 6 scenes — hook, idea, examples, definite, tricky, recap."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_idea()
        self.scene3_example1()
        self.scene4_example2()
        self.scene5_definite()
        self.scene6_tricky()
        self.scene7_recap()

    # ── Scene 1: Hook ───────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "How do you integrate 2x cosine of x squared? "
            "The chain rule in reverse: let u equal x squared.",
            duration=6,
        )
        play_intro(self, "U-Substitution", "Calculus I")

        problem = MathTex(
            r"\int 2x \cos(x^2)\,dx = \; ?",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        hint = Text(
            "Let u = x squared, then du = 2x dx",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(hint, direction=DOWN, anchor=problem, buff=0.5)
        self.play(Write(hint), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 2: The Idea ────────────────────────────────────────
    def scene2_idea(self):
        self.add_subcaption(
            "u-substitution is the reverse of the chain rule. "
            "Identify the inner function, substitute, integrate, substitute back.",
            duration=6,
        )

        self.ly.section_divider(1, "The Idea: Reverse Chain Rule")

        steps = [
            MathTex(r"1. \text{ Pick } u = g(x), \text{ find } du = g'(x)\,dx", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"2. \text{ Substitute: } \int f(u)\,du", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"3. \text{ Integrate in terms of } u", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"4. \text{ Substitute back } u = g(x)", font_size=BODY_SIZE, color=SECONDARY),
        ]
        self.ly.progressive_reveal(steps, start_from=None, run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 3: Example 1 — 2x cos(x^2) ───────────────────────
    def scene3_example1(self):
        self.add_subcaption(
            "Let u equal x squared. Then du equals 2x dx. "
            "The integral becomes cosine u du, which is sine u plus C, "
            "or sine of x squared plus C.",
            duration=8,
        )

        self.ly.section_divider(2, r"Example: $\int 2x \cos(x^2)\,dx$")

        problem = MathTex(
            r"\int 2x \cos(x^2)\,dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        sub = MathTex(
            r"u = x^2 \Rightarrow du = 2x\,dx",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(sub, direction=DOWN, anchor=problem, buff=0.4)
        self.play(Write(sub), run_time=FAST)
        self.wait(0.5)

        result = MathTex(
            r"= \int \cos(u)\,du = \sin(u) + C = \sin(x^2) + C",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=sub, buff=0.4)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 4: Example 2 — 2x/(1+x^2) ────────────────────────
    def scene4_example2(self):
        self.add_subcaption(
            "Integral of 2x over 1 plus x squared. "
            "Let u equal 1 plus x squared. "
            "Becomes integral of 1 over u du, which is natural log of u plus C.",
            duration=8,
        )

        self.ly.section_divider(3, r"Example: $\int \frac{2x}{1+x^2}\,dx$")

        problem = MathTex(
            r"\int \frac{2x}{1 + x^2}\,dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        sub = MathTex(
            r"u = 1 + x^2, \quad du = 2x\,dx",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(sub, direction=DOWN, anchor=problem, buff=0.4)
        self.play(Write(sub), run_time=FAST)
        self.wait(0.5)

        result = MathTex(
            r"= \int \frac{1}{u}\,du = \ln|u| + C = \ln(1+x^2) + C",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=sub, buff=0.4)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 5: Definite Integral with u-sub ───────────────────
    def scene5_definite(self):
        self.add_subcaption(
            "For definite integrals, change the limits when you substitute u. "
            "No need to substitute back if you change bounds correctly.",
            duration=6,
        )

        self.ly.section_divider(4, r"Definite: $\int_0^2 2x e^{x^2}\,dx$")

        problem = MathTex(
            r"\int_0^2 2x e^{x^2}\,dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        sub = MathTex(
            r"u = x^2, \quad x{=}0 \Rightarrow u{=}0, \quad x{=}2 \Rightarrow u{=}4",
            font_size=LABEL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(sub, direction=DOWN, anchor=problem, buff=0.4)
        self.play(Write(sub), run_time=FAST)
        self.wait(0.5)

        result = MathTex(
            r"= \int_0^4 e^u\,du = \left[e^u\right]_0^4 = e^4 - 1",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.formula_box(result, color=ACCENT)
        self.ly.safe_place(result, direction=DOWN, anchor=sub, buff=0.4)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 6: Tricky Cases ──────────────────────────────────
    def scene6_tricky(self):
        self.add_subcaption(
            "If du doesn't match exactly, pull out constant factors. "
            "Missing a constant? Divide and multiply to create it.",
            duration=6,
        )

        self.ly.section_divider(5, "Constant Adjustment")

        problem = MathTex(
            r"\int x e^{x^2}\,dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        sub = MathTex(
            r"u = x^2, \quad du = 2x\,dx \Rightarrow x\,dx = \frac{du}{2}",
            font_size=LABEL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(sub, direction=DOWN, anchor=problem, buff=0.4)
        self.play(Write(sub), run_time=FAST)
        self.wait(0.5)

        result = MathTex(
            r"= \frac{1}{2}\int e^u\,du = \frac{1}{2}e^{x^2} + C",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=sub, buff=0.4)
        self.play(Write(result), run_time=NORMAL)
        self.wait(0.5)

        tip = Text(
            "Constant factors pull out — always check!",
            font_size=LABEL_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(tip, direction=DOWN, anchor=result, buff=0.4)
        self.play(Write(tip), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 7: Recap + Outro ─────────────────────────────────
    def scene7_recap(self):
        self.add_subcaption(
            "u-substitution is the chain rule in reverse. "
            "Pick the inner function as u, find du, integrate, substitute back. "
            "Next: Integration by Parts.",
            duration=6,
        )

        title = self.ly.title("Summary")

        recap = [
            Text("u-sub = reverse chain rule", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("du must appear in the integrand", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Pull out constant factors if needed", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Definite integrals: change limits", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(recap, start_from=title, run_time=FAST)
        self.wait(1.0)

        play_outro(self, "Integration by Parts", "Calculus I")
