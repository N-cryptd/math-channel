"""
Video 06: Exponential & Logarithmic Derivatives
Calculus I — e^x, ln(x), a^x, and logarithmic differentiation.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, proper narration timing, SANS font for body.

Render draft:  manim -ql scripts/pre-university/video-06-exp-log.py Video06_ExpLogDerivatives
Render final:  manim -qh scripts/pre-university/video-06-exp-log.py Video06_ExpLogDerivatives

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


class Video06_ExpLogDerivatives(Scene):
    """Full video: 8 scenes — e^x derivative, general base, ln(x), log differentiation."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_number_e()
        self.scene3_exponential_graphs()
        self.scene4_derivative_e_x()
        self.scene5_derivative_a_x()
        self.scene6_derivative_ln_x()
        self.scene7_log_diff()
        self.scene8_recap()

    # ── Scene 1: Hook ────────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "What function is its own derivative? "
            "The answer is e to the x.",
            duration=6,
        )
        play_intro(self, "Exponential & Log Derivatives", "Calculus I")

        self.add_subcaption(
            "Consider x squared — its derivative is 2x, not x squared. "
            "Sine gives cosine, not sine. "
            "But e to the x is special.",
            duration=10,
        )

        title = self.ly.title("The Self-Derivative Function")
        self.wait(0.3)

        # Candidate 1: x^2
        cand1 = MathTex(
            r"x^2 \to 2x",
            font_size=LABEL_SIZE, color=DIM,
        )
        self.ly.safe_place(cand1, direction=DOWN, anchor=title, buff=0.8)
        self.play(FadeIn(cand1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        # Candidate 2: sin(x)
        cand2 = MathTex(
            r"\sin(x) \to \cos(x)",
            font_size=LABEL_SIZE, color=DIM,
        )
        self.ly.safe_place(cand2, direction=DOWN, anchor=cand1, buff=0.3)
        self.play(FadeIn(cand2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        # The answer
        self.play(FadeOut(cand1), FadeOut(cand2), run_time=0.3)

        self.add_subcaption(
            "The derivative of e to the x is e to the x. It reproduces itself.",
            duration=6,
        )
        answer = MathTex(
            r"f(x) = e^x \implies f'(x) = e^x",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(answer)
        self.play(Write(answer), run_time=SLOW)
        self.wait(1.0)

        note = Text(
            "Its own derivative!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=answer, buff=0.5)
        self.play(Write(note), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 2: The Number e (definition) ───────────────────────
    def scene2_number_e(self):
        self.add_subcaption(
            "The number e is defined as a limit. "
            "It approaches approximately 2.71828.",
            duration=8,
        )

        self.ly.section_divider(1, "The Number e")

        limit_def = MathTex(
            r"e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.formula_box(limit_def, color=PRIMARY)
        self.play(Write(limit_def), run_time=NORMAL)
        self.wait(0.5)

        # Approximation values — progressive reveal
        self.add_subcaption(
            "For n equals 1 we get 2. For n equals 10, about 2.59. "
            "For n equals 100, about 2.70. The limit converges to e.",
            duration=10,
        )
        approx_items = [
            MathTex(r"n=1:\;(1+1)^1 = 2", font_size=LABEL_SIZE, color=DIM),
            MathTex(r"n=10:\;(1.1)^{10} \approx 2.59", font_size=LABEL_SIZE, color=DIM),
            MathTex(r"n=100:\;(1.01)^{100} \approx 2.70", font_size=LABEL_SIZE, color=DIM),
            MathTex(r"n \to \infty:\;e \approx 2.71828...", font_size=LABEL_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(approx_items, start_from=limit_def, run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 3: Exponential Graphs (geometric intuition) ────────
    def scene3_exponential_graphs(self):
        self.add_subcaption(
            "For y equals a to the x, the slope at x equals 0 is the natural log of a. "
            "Only for e does this slope equal 1.",
            duration=10,
        )

        self.ly.section_divider(2, "Why e is Special")

        # Geometric meaning text
        geo_text = Text(
            "For y = a^x, slope at x=0 is ln(a)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(geo_text, anchor=None)
        self.play(FadeIn(geo_text, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Remove text, show graph
        self.play(FadeOut(geo_text), run_time=0.3)

        # Create axes
        axes = Axes(
            x_range=[-1.5, 2.5, 0.5], y_range=[0, 5, 1],
            x_length=6, y_length=3.5,
            axis_config={"color": DIM, "include_numbers": True, "font_size": 18},
        )
        self.ly.center_in_content(axes)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(axes_labels), run_time=FAST)
        self.wait(0.3)

        # Plot curves one at a time with progressive removal
        # 2^x
        curve_2 = axes.plot(lambda x: 2**x, x_range=[-1.5, 2.5], color="#e07a5f", stroke_width=2)
        label_2 = MathTex(r"2^x", font_size=LABEL_SIZE, color="#e07a5f").next_to(curve_2.get_end(), RIGHT, buff=0.1)
        self.play(Create(curve_2), Write(label_2), run_time=NORMAL)
        self.wait(0.3)

        # 3^x
        curve_3 = axes.plot(lambda x: 3**x, x_range=[-1.5, 2.5], color="#81b29a", stroke_width=2)
        label_3 = MathTex(r"3^x", font_size=LABEL_SIZE, color="#81b29a").next_to(curve_3.get_end(), RIGHT, buff=0.1)
        self.play(Create(curve_3), Write(label_3), run_time=NORMAL)
        self.wait(0.3)

        # e^x — highlight
        self.play(FadeOut(label_2), FadeOut(label_3), run_time=0.3)
        curve_e = axes.plot(lambda x: np.exp(x), x_range=[-1.5, 2.5], color=ACCENT, stroke_width=3)
        label_e = MathTex(r"e^x", font_size=LABEL_SIZE, color=ACCENT).next_to(curve_e.get_end(), RIGHT, buff=0.1)
        self.play(Create(curve_e), Write(label_e), run_time=NORMAL)
        self.wait(0.3)

        # Dot at (0,1)
        dot = Dot(axes.coords_to_point(0, 1), color=WHITE, radius=0.08)
        self.play(FadeIn(dot), run_time=FAST)
        self.wait(0.3)

        # Tangent line for e^x (slope = 1)
        self.play(FadeOut(curve_2), FadeOut(curve_3), run_time=0.3)
        tan_e = axes.plot(lambda x: 1 + 1.0 * x, x_range=[-1.0, 1.2], color=ACCENT, stroke_width=2)
        self.play(Create(tan_e), run_time=NORMAL)
        self.wait(0.5)

        # Key insight
        self.play(FadeOut(axes), FadeOut(axes_labels), FadeOut(dot),
                  FadeOut(tan_e), FadeOut(label_e), run_time=0.3)

        insight = MathTex(
            r"\text{slope at }x{=}0:\quad \ln(e) = 1",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(insight, color=ACCENT)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 4: Proving d/dx[e^x] = e^x ───────────────────────
    def scene4_derivative_e_x(self):
        self.add_subcaption(
            "We prove the derivative of e to the x using the limit definition. "
            "The key step uses a fundamental limit.",
            duration=8,
        )

        self.ly.section_divider(3, r"d/dx$[e^x] = e^x$")

        # Step 1: Limit definition
        step1 = MathTex(
            r"\frac{d}{dx}[e^x] = \lim_{h \to 0} \frac{e^{x+h} - e^x}{h}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1, anchor=None)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)

        # Step 2: Factor e^x
        self.add_subcaption(
            "Factor out e to the x using exponent rules. "
            "This gives e to the x times the limit of e to the h minus 1 over h.",
            duration=8,
        )
        step2 = MathTex(
            r"= e^x \cdot \lim_{h \to 0} \frac{e^h - 1}{h}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.5)
        self.play(Transform(step1.copy(), step2), run_time=NORMAL)
        # Show step2 properly
        self.remove(step1)
        self.add(step2)
        self.wait(0.5)

        # The key limit
        self.add_subcaption(
            "The key limit: e to the h minus 1 over h equals 1. "
            "This is because e to the h is approximately 1 plus h for small h.",
            duration=8,
        )
        key_limit = MathTex(
            r"\lim_{h \to 0} \frac{e^h - 1}{h} = 1",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(key_limit, color=ACCENT)
        self.play(Write(key_limit), run_time=SLOW)
        self.wait(0.5)

        # Approximation note
        approx = Text(
            "e^h ≈ 1 + h for small h  →  limit = 1",
            font_size=LABEL_SIZE, color=DIM, font=MONO,
        )
        self.ly.safe_place(approx, direction=DOWN, anchor=key_limit, buff=0.4)
        self.play(Write(approx), run_time=FAST)
        self.wait(0.5)

        # Final result
        self.play(FadeOut(step2), FadeOut(approx), run_time=0.3)

        self.add_subcaption(
            "Therefore the derivative of e to the x is e to the x times 1, "
            "which equals e to the x.",
            duration=6,
        )
        result = MathTex(
            r"\frac{d}{dx}[e^x] = e^x \cdot 1 = e^x",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(result, color=ACCENT)
        self.play(Transform(key_limit, result), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 5: Derivative of a^x (general base) ───────────────
    def scene5_derivative_a_x(self):
        self.add_subcaption(
            "For any base a, rewrite a to the x using e. "
            "Then apply the chain rule to find the derivative.",
            duration=8,
        )

        self.ly.section_divider(4, r"General Base: $a^x$")

        # The trick
        trick = MathTex(
            r"a^x = e^{x \cdot \ln(a)}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(trick, anchor=None)
        self.play(Write(trick), run_time=NORMAL)
        self.wait(0.5)

        # Chain rule application
        self.add_subcaption(
            "Differentiate using the chain rule. "
            "The outer function gives e to x ln a, "
            "times the inner derivative ln a.",
            duration=8,
        )
        chain_step = MathTex(
            r"\frac{d}{dx}[a^x] = e^{x \cdot \ln(a)} \cdot \ln(a)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(chain_step, direction=DOWN, anchor=trick, buff=0.5)
        self.play(Write(chain_step), run_time=NORMAL)
        self.wait(0.5)

        # Final result
        result = MathTex(
            r"= a^x \cdot \ln(a)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(result, color=ACCENT)
        self.play(Transform(chain_step, result), run_time=NORMAL)
        self.wait(0.5)

        # Note: when a = e
        note = Text(
            "When a = e:  ln(e) = 1  →  back to e^x",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=result, buff=0.5)
        self.play(Write(note), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 6: Derivative of ln(x) ────────────────────────────
    def scene6_derivative_ln_x(self):
        self.add_subcaption(
            "To find the derivative of the natural log, "
            "we use implicit differentiation on e to the y equals x.",
            duration=8,
        )

        self.ly.section_divider(5, r"Derivative of $\ln(x)$")

        # Setup: implicit differentiation
        setup1 = MathTex(
            r"y = \ln(x) \implies e^{y} = x",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(setup1, anchor=None)
        self.play(Write(setup1), run_time=NORMAL)
        self.wait(0.5)

        # Differentiate both sides
        self.add_subcaption(
            "Differentiate both sides with respect to x. "
            "The left side needs the chain rule.",
            duration=6,
        )
        step1 = MathTex(
            r"e^{y} \cdot \frac{dy}{dx} = 1",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=setup1, buff=0.5)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)

        # Solve for dy/dx
        self.add_subcaption(
            "Solve for dy/dx. Since e to the y equals x, "
            "we get 1 over x.",
            duration=6,
        )
        step2 = MathTex(
            r"\frac{dy}{dx} = \frac{1}{e^{y}} = \frac{1}{x}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.4)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.5)

        # Final boxed result
        self.play(FadeOut(setup1), FadeOut(step1), FadeOut(step2), run_time=0.3)

        result = MathTex(
            r"\frac{d}{dx}[\ln(x)] = \frac{1}{x}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(result, color=ACCENT)
        self.play(Write(result), run_time=SLOW)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 7: Logarithmic Differentiation ─────────────────────
    def scene7_log_diff(self):
        self.add_subcaption(
            "For functions like x to the x, "
            "take the natural log of both sides, differentiate, "
            "then solve for the derivative.",
            duration=8,
        )

        self.ly.section_divider(6, "Logarithmic Differentiation")

        # The problem
        problem = MathTex(
            r"y = x^x",
            font_size=HEADING_SIZE, color=WHITE,
        )
        question = Text(
            "What is dy/dx?",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(problem, anchor=None)
        self.play(Write(problem), run_time=NORMAL)
        self.ly.safe_place(question, direction=RIGHT, anchor=problem, buff=0.5)
        self.play(Write(question), run_time=FAST)
        self.wait(0.5)

        # Step 1: Take ln
        self.add_subcaption(
            "Step one: take the natural log of both sides. "
            "This gives ln y equals x ln x.",
            duration=6,
        )
        self.play(FadeOut(question), run_time=0.3)
        step1_label = Text(
            "Step 1: Take ln of both sides",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        step1 = MathTex(
            r"\ln(y) = x \cdot \ln(x)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1_label, direction=DOWN, anchor=problem, buff=0.4)
        self.ly.safe_place(step1, direction=DOWN, anchor=step1_label, buff=0.3)
        self.play(FadeIn(step1_label, shift=LEFT * 0.15), Write(step1), run_time=NORMAL)
        self.wait(0.5)

        # Step 2: Differentiate
        self.add_subcaption(
            "Step two: differentiate both sides. "
            "Use the product rule on the right and chain rule on the left.",
            duration=6,
        )
        self.play(FadeOut(problem), FadeOut(step1_label), run_time=0.3)
        step2 = MathTex(
            r"\frac{1}{y} \cdot \frac{dy}{dx} = \ln(x) + 1",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step2, anchor=None)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.5)

        # Step 3: Solve
        self.add_subcaption(
            "Step three: multiply both sides by y, "
            "then substitute y equals x to the x.",
            duration=6,
        )
        step3 = MathTex(
            r"\frac{dy}{dx} = x^x \cdot (\ln(x) + 1)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(step3, color=ACCENT)
        self.play(Transform(step2, step3), run_time=SLOW)
        self.wait(0.5)

        # Usage note
        note = Text(
            "Use for: f(x)^g(x) forms and messy products",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=step3, buff=0.5)
        self.play(Write(note), run_time=FAST)
        self.wait(1.0)

        self.ly.clear()

    # ── Scene 8: Recap + Outro ───────────────────────────────────
    def scene8_recap(self):
        self.add_subcaption(
            "Today we covered derivatives of exponentials and logarithms. "
            "Next up: trigonometric derivatives.",
            duration=6,
        )

        title = self.ly.title("Summary")

        recap_items = [
            Text("d/dx[e^x] = e^x  — its own derivative!", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("d/dx[a^x] = a^x · ln(a)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("d/dx[ln(x)] = 1/x", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Log diff: ln both sides, differentiate, solve", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(recap_items, start_from=title, run_time=FAST)
        self.wait(1.0)

        play_outro(self, "Trig Derivatives", "Calculus I")
