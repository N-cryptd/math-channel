"""
Video 12: Introduction to Integration
Calculus I — area under a curve, Riemann sums, the definite integral.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, proper narration timing, SANS font for body.

Render draft:  manim -ql scripts/pre-university/video-12-intro-integration.py Video12_IntroIntegration
Render final:  manim -qh scripts/pre-university/video-12-intro-integration.py Video12_IntroIntegration

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


class Video12_IntroIntegration(Scene):
    """Full video: 7 scenes — hook, area problem, Riemann sums, refinement, FTC, recap."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_area_problem()
        self.scene3_riemann_sums()
        self.scene4_refinement()
        self.scene5_fundamental_theorem()
        self.scene6_recap()

    # ── Scene 1: Hook ───────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "How do you find the area under a curve? "
            "Rectangles approximate it. More rectangles, better approximation. "
            "The limit gives exact area — that is integration.",
            duration=8,
        )
        play_intro(self, "Introduction to Integration", "Calculus I")

        question = Text(
            "What is the area under this curve?",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(question, anchor=None)
        self.play(Write(question), run_time=NORMAL)
        self.wait(0.5)

        # Quick visual: axes + curve + shaded area
        axes = Axes(
            x_range=[0, 4, 1], y_range=[0, 5, 1],
            x_length=5, y_length=3,
            axis_config={"color": DIM},
        )
        self.ly.center_in_content(axes)
        self.play(Create(axes), run_time=FAST)

        curve = axes.plot(lambda x: 0.3 * x**2 + 0.5, x_range=[0.5, 3.5],
                          color=PRIMARY, stroke_width=2)
        area = axes.get_area(curve, x_range=[0.5, 3.5], color=SECONDARY, opacity=0.3)
        self.play(Create(curve), FadeIn(area), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 2: The Area Problem ──────────────────────────────
    def scene2_area_problem(self):
        self.add_subcaption(
            "Find the signed area between the graph and the x-axis, "
            "from a to b. Area above is positive, below is negative.",
            duration=6,
        )

        self.ly.section_divider(1, "The Area Problem")

        integral = MathTex(
            r"A = \int_{a}^{b} f(x) \, dx",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(integral, color=ACCENT)
        self.ly.safe_place(integral, anchor=None)
        self.play(Write(integral), run_time=SLOW)
        self.wait(0.5)

        info = [
            Text("Signed area: above = positive, below = negative", font_size=LABEL_SIZE, color=WHITE, font=SANS),
            Text("Read: 'integral from a to b of f of x dx'", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(info, start_from=integral, run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 3: Riemann Sums ────────────────────────────────────
    def scene3_riemann_sums(self):
        self.add_subcaption(
            "Riemann sums approximate area with rectangles. "
            "Left Riemann uses the left endpoint for height. "
            "Delta x is the width of each rectangle.",
            duration=8,
        )

        self.ly.section_divider(2, "Riemann Sums")

        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 5, 1],
            x_length=6, y_length=3.5,
            axis_config={"color": DIM},
        )
        self.ly.center_in_content(axes)
        self.play(Create(axes), run_time=FAST)

        curve = axes.plot(lambda x: 0.2 * x**2 + 0.5, x_range=[0.5, 4.5],
                          color=PRIMARY, stroke_width=2)
        self.play(Create(curve), run_time=FAST)

        # 4 rectangles
        n = 4
        x_min, x_max = 0.5, 4.5
        dx = (x_max - x_min) / n
        rects = VGroup()
        for i in range(n):
            x_left = x_min + i * dx
            x_right = x_left + dx
            y_val = 0.2 * x_left**2 + 0.5
            bl = axes.c2p(x_left, 0)
            br = axes.c2p(x_right, 0)
            tr = axes.c2p(x_right, y_val)
            tl = axes.c2p(x_left, y_val)
            rect = Polygon(bl, br, tr, tl, color=SECONDARY,
                           fill_color=SECONDARY, fill_opacity=0.3, stroke_width=2)
            rects.add(rect)

        self.play(Create(rects), run_time=NORMAL)
        self.wait(0.5)

        formula = MathTex(
            r"L_n = \sum_{i=0}^{n-1} f(x_i) \Delta x, \quad \Delta x = \frac{b-a}{n}",
            font_size=LABEL_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, direction=DOWN, anchor=axes, buff=0.3)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 4: Refinement ─────────────────────────────────────
    def scene4_refinement(self):
        self.add_subcaption(
            "More rectangles give better approximation. "
            "In the limit, infinitely many rectangles of zero width "
            "give the exact area.",
            duration=8,
        )

        self.ly.section_divider(3, "More Rectangles = Better")

        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 5, 1],
            x_length=6, y_length=3.5,
            axis_config={"color": DIM},
        )
        self.ly.center_in_content(axes)
        self.play(Create(axes), run_time=FAST)

        curve = axes.plot(lambda x: 0.2 * x**2 + 0.5, x_range=[0.5, 4.5],
                          color=PRIMARY, stroke_width=2)
        self.play(Create(curve), run_time=FAST)

        x_min, x_max = 0.5, 4.5
        old_rects = VGroup()

        for n in [4, 8, 20]:
            dx = (x_max - x_min) / n
            rects = VGroup()
            for i in range(n):
                x_left = x_min + i * dx
                x_right = x_left + dx
                y_val = 0.2 * x_left**2 + 0.5
                bl = axes.c2p(x_left, 0)
                br = axes.c2p(x_right, 0)
                tr = axes.c2p(x_right, y_val)
                tl = axes.c2p(x_left, y_val)
                rect = Polygon(bl, br, tr, tl, color=SECONDARY,
                               fill_color=SECONDARY,
                               fill_opacity=0.3 if n <= 8 else 0.2, stroke_width=1)
                rects.add(rect)

            if len(old_rects) > 0:
                self.play(FadeOut(old_rects), run_time=FAST)
            old_rects = rects

            n_label = Text(f"n = {n}", font_size=LABEL_SIZE, color=ACCENT, font=SANS)
            self.ly.safe_place(n_label, direction=UP, anchor=axes, buff=0.2)
            self.play(Create(rects), FadeIn(n_label), run_time=FAST if n > 8 else NORMAL)
            self.wait(0.8)

        self.ly.clear()

        # The limit definition
        limit = MathTex(
            r"\int_{a}^{b} f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(limit, color=ACCENT)
        self.ly.safe_place(limit, anchor=None)
        self.play(Write(limit), run_time=SLOW)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 5: Fundamental Theorem ────────────────────────────
    def scene5_fundamental_theorem(self):
        self.add_subcaption(
            "The Fundamental Theorem of Calculus: "
            "if F prime equals f, then the integral equals F of b minus F of a. "
            "No need to compute limits directly.",
            duration=8,
        )

        self.ly.section_divider(4, "The Fundamental Theorem")

        theorem = MathTex(
            r"\text{If } F'(x) = f(x), \quad \int_{a}^{b} f(x)\,dx = F(b) - F(a)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.formula_box(theorem, color=ACCENT)
        self.ly.safe_place(theorem, anchor=None)
        self.play(Write(theorem), run_time=SLOW)
        self.wait(0.5)

        self.ly.clear()

        # Example
        self.add_subcaption(
            "Example: integral of x squared from 0 to 2 "
            "equals x cubed over 3 from 0 to 2, which is 8 thirds.",
            duration=6,
        )

        title5 = self.ly.title("Example")

        problem = MathTex(
            r"\int_{0}^{2} x^2\,dx = \left[ \frac{x^3}{3} \right]_0^2 = \frac{8}{3} - 0 = \frac{8}{3}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(problem, direction=DOWN, anchor=title5, buff=0.5)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        insight = Text(
            "Differentiation undoes integration!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=problem, buff=0.5)
        self.play(Write(insight), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 6: Recap + Outro ─────────────────────────────────
    def scene6_recap(self):
        self.add_subcaption(
            "Integration finds area under a curve using Riemann sums. "
            "The Fundamental Theorem lets us compute integrals using antiderivatives. "
            "Next: Antiderivatives.",
            duration=8,
        )

        title = self.ly.title("Summary")

        recap = [
            Text("Integral = signed area under the curve", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Riemann sums: rectangles converging to the integral", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("FTC: integral = F(b) - F(a)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Differentiation and integration are inverses", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(recap, start_from=title, run_time=FAST)
        self.wait(1.0)

        play_outro(self, "Antiderivatives", "Calculus I")
