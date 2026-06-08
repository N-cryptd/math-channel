"""
Video 10: Curve Sketching
Calculus I — putting it all together: domain, intercepts, symmetry, asymptotes,
increasing/decreasing, concavity, and sketching.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, proper narration timing, SANS font for body.

Render draft:  manim -ql scripts/pre-university/video-10-curve-sketching.py Video10_CurveSketching
Render final:  manim -qh scripts/pre-university/video-10-curve-sketching.py Video10_CurveSketching

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


class Video10_CurveSketching(Scene):
    """Full video: 6 scenes — checklist, setup, analysis, sketch, recap."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_checklist()
        self.scene3_setup()
        self.scene4_analysis()
        self.scene5_sketch()
        self.scene6_recap()

    # ── Scene 1: Hook ───────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Curve sketching brings together limits, derivatives, and tests "
            "into a systematic approach.",
            duration=6,
        )
        play_intro(self, "Curve Sketching", "Calculus I")

        self.add_subcaption(
            "Draw accurate graphs using calculus. No more plotting a million points.",
            duration=6,
        )

        goal = Text(
            "Draw accurate graphs using calculus.",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(goal, anchor=None)
        self.play(Write(goal), run_time=NORMAL)
        self.wait(0.5)

        sub = Text(
            "No more plotting a million points.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(sub, direction=DOWN, anchor=goal, buff=0.4)
        self.play(Write(sub), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 2: The Checklist ──────────────────────────────────
    def scene2_checklist(self):
        self.add_subcaption(
            "Follow this checklist: domain, intercepts, symmetry, asymptotes, "
            "first derivative for increasing and decreasing, "
            "second derivative for concavity, then sketch.",
            duration=10,
        )

        self.ly.section_divider(1, "The Curve Sketching Checklist")

        # Show 4 items at a time via progressive_reveal (7 total)
        items = [
            Text("1. Domain", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. Intercepts", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3. Symmetry (even/odd)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("4. Asymptotes", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5. 1st deriv: inc/dec, extrema", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("6. 2nd deriv: concavity", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("7. Sketch!", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(items, start_from=None, run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 3: Example Setup ──────────────────────────────────
    def scene3_setup(self):
        self.add_subcaption(
            "Let's sketch x squared over x squared minus 1. "
            "Domain excludes plus and minus 1. "
            "Even function with horizontal asymptote at y equals 1.",
            duration=10,
        )

        self.ly.section_divider(2, r"Example: $f(x) = \frac{x^2}{x^2 - 1}$")

        func = MathTex(
            r"f(x) = \frac{x^2}{x^2 - 1}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(func, anchor=None)
        self.play(Write(func), run_time=SLOW)
        self.wait(0.5)

        # Domain and asymptotes
        info_items = [
            MathTex(r"x \neq \pm 1 \text{ (vertical asymptotes)}", font_size=LABEL_SIZE, color=RED),
            MathTex(r"\lim_{x \to \pm\infty} f(x) = 1 \text{ (horizontal)}", font_size=LABEL_SIZE, color=SECONDARY),
            Text("Even function (symmetric about y-axis)", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(info_items, start_from=func, run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 4: Derivative Analysis ──────────────────────────────
    def scene4_analysis(self):
        self.add_subcaption(
            "The first derivative is negative 2x over x squared minus 1 squared. "
            "Critical point at x equals 0 (local max). "
            "Concave down between the asymptotes.",
            duration=10,
        )

        self.ly.section_divider(3, "Derivative Analysis")

        f_prime = MathTex(
            r"f'(x) = \frac{-2x}{(x^2-1)^2}, \quad f'(0) = 0",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(f_prime, anchor=None)
        self.play(Write(f_prime), run_time=NORMAL)
        self.wait(0.5)

        # Sign analysis
        sign = Text(
            "x < 0: increasing  |  x > 0: decreasing",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(sign, direction=DOWN, anchor=f_prime, buff=0.4)
        self.play(Write(sign), run_time=FAST)
        self.wait(0.5)

        result = Text(
            "(0, 0) is a local maximum",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=sign, buff=0.4)
        self.play(Write(result), run_time=FAST)
        self.wait(0.5)

        # Concavity
        concav = Text(
            "Concave down on (-1, 1), concave up elsewhere",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(concav, direction=DOWN, anchor=result, buff=0.3)
        self.play(Write(concav), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 5: The Sketch ─────────────────────────────────────
    def scene5_sketch(self):
        self.add_subcaption(
            "Now we sketch the graph using all the information we gathered. "
            "Vertical asymptotes at plus and minus 1, "
            "horizontal asymptote at y equals 1.",
            duration=8,
        )

        self.ly.section_divider(4, "The Sketch")

        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-1, 4, 1],
            x_length=7, y_length=4.5,
            axis_config={"color": DIM, "include_numbers": True},
        )
        self.ly.center_in_content(axes)
        self.play(Create(axes), run_time=NORMAL)

        # Asymptotes
        va1 = DashedLine(axes.c2p(1, -1), axes.c2p(1, 4), color=RED, stroke_width=2)
        va2 = DashedLine(axes.c2p(-1, -1), axes.c2p(-1, 4), color=RED, stroke_width=2)
        ha = DashedLine(axes.c2p(-3, 1), axes.c2p(3, 1), color=SECONDARY, stroke_width=2)
        self.play(Create(va1), Create(va2), Create(ha), run_time=FAST)
        self.wait(0.3)

        # Three branches
        mid_branch = axes.plot(lambda x: x**2 / (x**2 - 1), x_range=[-0.85, 0.85],
                               color=PRIMARY, stroke_width=3)
        left_branch = axes.plot(lambda x: x**2 / (x**2 - 1), x_range=[-3, -1.15],
                                color=PRIMARY, stroke_width=3)
        right_branch = axes.plot(lambda x: x**2 / (x**2 - 1), x_range=[1.15, 3],
                                color=PRIMARY, stroke_width=3)

        self.play(Create(mid_branch), run_time=NORMAL)
        self.play(Create(left_branch), Create(right_branch), run_time=NORMAL)

        # Mark local max
        max_dot = Dot(axes.c2p(0, 0), color=ACCENT, radius=0.1)
        self.play(FadeIn(max_dot), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 6: Recap + Outro ──────────────────────────────────
    def scene6_recap(self):
        self.add_subcaption(
            "Curve sketching combines domain, intercepts, asymptotes, "
            "and both derivative tests. Next: L'Hopital's Rule.",
            duration=6,
        )

        title = self.ly.title("Summary")

        recap = [
            Text("1. Domain + intercepts + symmetry", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. Asymptotes (vertical, horizontal)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3. 1st deriv: increasing/decreasing", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("4. 2nd deriv: concavity", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("5. Sketch!", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(recap, start_from=title, run_time=FAST)
        self.wait(1.0)

        play_outro(self, "L'Hopital's Rule", "Calculus I")
