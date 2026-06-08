"""
Video 17: Introduction to Sequences
Calculus II — definition, convergence, bounded/monotone sequences, examples.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, proper narration timing, SANS font for body.

Render draft:  manim -ql scripts/pre-university/video-17-sequences.py Video17_Sequences
Render final:  manim -qh scripts/pre-university/video-17-sequences.py Video17_Sequences

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


class Video17_Sequences(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_convergence()
        self.scene4_graphical()
        self.scene5_bounded_monotone()
        self.scene6_example()
        self.scene7_summary()

    # ── Scene 1: Hook ───────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "What happens when you keep applying a rule? "
            "Does it settle down or spiral out of control? "
            "Sequences are the foundation of Calculus II.",
            duration=6,
        )

        play_intro(self, "Introduction to Sequences", "Calculus II")

        question = self.ly.title("What happens when you iterate?")
        self.wait(0.5)

        # Dots converging to a target
        dots = VGroup(*[
            Dot(UP * (3.0 - 0.3 * i), radius=0.06, color=PRIMARY)
            for i in range(10)
        ])
        self.ly.safe_place(dots, anchor=None)
        for d in dots:
            self.play(FadeIn(d, scale=0.5), run_time=0.15)

        target_line = DashedLine(
            UP * 0.2, UP * 0.2 + RIGHT * 0.5,
            color=ACCENT, stroke_width=2,
        )
        self.ly.safe_place(target_line, direction=RIGHT, anchor=dots, buff=0.5)
        target_label = Text("limit?", font_size=LABEL_SIZE, color=ACCENT, font=SANS)
        self.ly.safe_place(target_label, direction=RIGHT, anchor=target_line, buff=0.2)
        self.play(Create(target_line), Write(target_label), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 2: Definition ─────────────────────────────────────
    def scene2_definition(self):
        self.add_subcaption(
            "A sequence is an ordered list of numbers — "
            "a function from natural numbers to real numbers. "
            "We write a sub n for the n-th term.",
            duration=6,
        )

        self.ly.section_divider(1, "What is a Sequence?")

        defn = MathTex(
            r"\{a_n\}_{n=1}^{\infty} = a_1, a_2, a_3, \ldots",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(defn, anchor=None)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(0.5)

        func = MathTex(
            r"a_n = f(n), \quad n \in \mathbb{N}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(func, direction=DOWN, anchor=defn, buff=0.4)
        self.play(Write(func), run_time=NORMAL)
        self.wait(0.5)

        examples = [
            MathTex(r"a_n = \frac{1}{n}", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"a_n = \left(\frac{1}{2}\right)^n", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"a_n = (-1)^n", font_size=BODY_SIZE, color=SECONDARY),
        ]
        self.ly.progressive_reveal(examples, start_from=func, run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 3: Convergence ────────────────────────────────────
    def scene3_convergence(self):
        self.add_subcaption(
            "A sequence converges to L if terms get arbitrarily close. "
            "Formally: for every epsilon, there exists N such that "
            "for all n greater than N, a sub n is within epsilon of L.",
            duration=8,
        )

        self.ly.section_divider(2, "Convergence")

        informal = Text(
            "The terms get closer and closer to a limit L.",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(informal, anchor=None)
        self.play(Write(informal), run_time=NORMAL)
        self.wait(0.5)

        formal = MathTex(
            r"\lim_{n \to \infty} a_n = L \iff "
            r"\forall \varepsilon > 0,\; \exists N: "
            r"n > N \Rightarrow |a_n - L| < \varepsilon",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(formal, direction=DOWN, anchor=informal, buff=0.5)
        self.play(Write(formal), run_time=SLOW)
        self.wait(0.5)

        key = Text(
            "Eventually, all terms are within any tiny distance of L",
            font_size=LABEL_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=formal, buff=0.5)
        self.play(Write(key), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 4: Visualizing Convergence ──────────────────────────
    def scene4_graphical(self):
        self.add_subcaption(
            "Think of a sequence as points on a number line. "
            "For a sub n equals 1 over n, the terms cluster around zero. "
            "All terms after some N are within epsilon of the limit.",
            duration=8,
        )

        self.ly.section_divider(3, "Visualizing Convergence")

        line = NumberLine(
            x_range=[-0.2, 1.3, 0.1],
            length=10,
            color=DIM,
            font_size=LABEL_SIZE,
        )
        self.ly.center_in_content(line)
        self.play(Create(line), run_time=FAST)

        n_vals = [1, 2, 3, 4, 5, 6, 8, 10, 15, 20]
        dots = VGroup()
        for n in n_vals:
            val = 1.0 / n
            dot = Dot(line.n2p(val), radius=0.08, color=PRIMARY)
            dots.add(dot)

        for dot in dots:
            self.play(FadeIn(dot, scale=0.5), run_time=0.15)
        self.wait(0.3)

        limit_dot = Dot(line.n2p(0), radius=0.1, color=ACCENT)
        limit_label = MathTex(r"L = 0", font_size=HEADING_SIZE, color=ACCENT)
        self.ly.safe_place(limit_label, direction=UP, anchor=limit_dot, buff=0.2)
        self.play(FadeIn(limit_dot), Write(limit_label), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

        # Divergent example
        self.add_subcaption(
            "But a sub n equals negative 1 to the n oscillates forever "
            "between minus 1 and 1 — no limit exists.",
            duration=6,
        )

        title4b = self.ly.title("Divergent Example")

        line2 = NumberLine(
            x_range=[-1.5, 1.5, 0.5],
            length=8,
            color=DIM,
            font_size=LABEL_SIZE,
        )
        self.ly.safe_place(line2, direction=DOWN, anchor=title4b, buff=0.5)
        self.play(Create(line2), run_time=FAST)

        alt_dots = VGroup()
        for i in range(10):
            val = (-1) ** (i + 1)
            dot = Dot(line2.n2p(val), radius=0.08,
                      color=RED if val < 0 else SECONDARY)
            alt_dots.add(dot)

        for dot in alt_dots:
            self.play(FadeIn(dot, scale=0.5), run_time=0.15)
        self.wait(0.3)

        diverges = Text(
            "Oscillates forever — no limit exists!",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(diverges, direction=DOWN, anchor=line2, buff=0.3)
        self.play(Write(diverges), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 5: Bounded & Monotone ──────────────────────────────
    def scene5_bounded_monotone(self):
        self.add_subcaption(
            "A sequence is bounded if all terms stay within some range. "
            "Monotone means always increasing or always decreasing. "
            "Bounded plus monotone always converges.",
            duration=8,
        )

        self.ly.section_divider(4, "Bounded & Monotone")

        bounded = [
            MathTex(r"\exists\, M : a_n \leq M \;\forall\, n \text{ (bounded above)}", font_size=LABEL_SIZE, color=PRIMARY),
            MathTex(r"\exists\, m : a_n \geq m \;\forall\, n \text{ (bounded below)}", font_size=LABEL_SIZE, color=PRIMARY),
            Text("Monotone: a_n <= a_{n+1} (inc) or a_n >= a_{n+1} (dec)", font_size=LABEL_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(bounded, start_from=None, run_time=FAST)
        self.wait(0.5)

        theorem = MathTex(
            r"\text{Bounded} + \text{Monotone} \Rightarrow \text{Converges}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(theorem, color=ACCENT)
        self.ly.safe_place(theorem, direction=DOWN, anchor=None, buff=0.5)
        self.play(Write(theorem), run_time=SLOW)
        self.wait(0.5)

        name = Text(
            "Monotone Convergence Theorem",
            font_size=LABEL_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(name, direction=DOWN, anchor=theorem, buff=0.3)
        self.play(Write(name), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 6: Example ────────────────────────────────────────
    def scene6_example(self):
        self.add_subcaption(
            "Example: a sub n equals n over n plus 1. "
            "Divide by n: 1 over 1 plus 1 over n. "
            "As n goes to infinity, the limit is 1.",
            duration=6,
        )

        self.ly.section_divider(5, r"Example: $a_n = \frac{n}{n+1}$")

        problem = MathTex(
            r"a_n = \frac{n}{n+1}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        step = MathTex(
            r"= \frac{1}{1 + 1/n} \xrightarrow{n \to \infty} 1",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step, direction=DOWN, anchor=problem, buff=0.5)
        self.play(Write(step), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 7: Summary + Outro ─────────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "Sequences are functions from N to R. "
            "Convergence means terms approach a limit. "
            "Bounded plus monotone guarantees convergence. "
            "Next: Infinite Series.",
            duration=6,
        )

        title = self.ly.title("Summary")

        recap = [
            Text("A sequence is a function from N to R", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Convergence: terms approach a limit L", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Epsilon-N definition makes this precise", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Bounded + Monotone => Converges", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(recap, start_from=title, run_time=FAST)
        self.wait(1.0)

        play_outro(self, "Infinite Series", "Calculus II")
