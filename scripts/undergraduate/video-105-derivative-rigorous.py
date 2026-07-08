"""
Video 105: The Derivative (Rigorous)
TEMPLATE v2 -- Professional quality Manim script

Playlist: Real Analysis I (Video 7 of 12)
Class: Video105_DerivativeRigorous

QUALITY RULES (enforced):
  1. Max 5 visible elements per scene at any time
  2. Use LayoutEngine for ALL positioning -- no manual .shift() or .to_edge()
  3. Progressive disclosure: add items one at a time
  4. Use consistent animation vocabulary (Write, FadeIn, Create, etc.)
  5. Each add_subcaption() duration ~ words / 2.5 seconds
  6. Call ly.clear() between scenes
  7. Raw strings for MathTex with single backslashes
  8. No font= parameter on MathTex (only on Text)
"""

from manim import *
import numpy as np
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits, clamp_position


class Video105_DerivativeRigorous(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_formal_definition()
        self.scene4_divider_diff_cont()
        self.scene5_diff_implies_continuous()
        self.scene6_divider_converse()
        self.scene7_counterexample_abs_x()
        self.scene8_divider_rules()
        self.scene9_derivative_rules()
        self.scene10_intervals_lipschitz()
        self.scene11_summary_outro()

    # --- Scene 1: Hook --- From Secant to Tangent ---
    def scene1_hook(self):
        self.add_subcaption(
            "In calculus you learned that the derivative is the "
            "slope of the tangent line. Today we make this "
            "rigorous. We define the derivative as a limit of "
            "difference quotients, prove that differentiability "
            "implies continuity, derive the basic rules from "
            "the limit definition, and connect derivatives to "
            "Lipschitz continuity and uniform continuity.",
            duration=25,
        )
        play_intro(self, "The Derivative (Rigorous)", "Real Analysis I")

        title = self.ly.title("From Secant to Tangent")

        # Graph of x^2
        axes = Axes(
            x_range=[-0.5, 4, 1], y_range=[-0.5, 10, 2],
            x_length=6.5, y_length=3.5,
            axis_config={"include_numbers": True, "font_size": 18, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        graph = axes.plot(lambda x: x ** 2, x_range=[0.1, 3.2], color=SECONDARY)
        self.play(Create(graph), run_time=NORMAL)

        # Fixed point at (1, 1)
        a_val = 1.0
        p_a = Dot(axes.c2p(a_val, a_val ** 2), color=PRIMARY, radius=0.06)
        self.play(FadeIn(p_a), run_time=FAST)

        # Secant line for h = 2
        h_vals = [2.0, 1.0, 0.5, 0.2]
        secant_lines = []
        for h in h_vals:
            x1 = a_val
            y1 = a_val ** 2
            x2 = a_val + h
            y2 = x2 ** 2
            slope = (y2 - y1) / (x2 - x1) if x2 != x1 else 0
            line = Line(
                axes.c2p(x1 - 0.3, y1 - 0.3 * slope),
                axes.c2p(x2 + 0.3, y2 + 0.3 * slope),
                color=PRIMARY, stroke_width=2.5,
            )
            secant_lines.append((line, h, slope))

        # Show first secant
        sec0, h0, slope0 = secant_lines[0]
        self.play(Create(sec0), run_time=NORMAL)

        # Difference quotient label
        dq = MathTex(
            r"\frac{f(1+2) - f(1)}{2} = \frac{9 - 1}{2} = 4",
            font_size=SMALL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(dq, direction=DOWN, anchor=axes, buff=0.2)
        self.play(Write(dq), run_time=NORMAL)
        self.wait(0.5)

        # Animate convergence: replace secant lines with progressively closer ones
        for i in range(1, len(secant_lines)):
            sec_new, h_new, slope_new = secant_lines[i]
            dq_new = MathTex(
                rf"\frac{{f(1+{h_new}) - f(1)}}{{{h_new}}} = {slope_new:.1f}",
                font_size=SMALL_SIZE, color=PRIMARY,
            )
            self.ly.safe_place(dq_new, direction=DOWN, anchor=axes, buff=0.2)
            self.play(
                Transform(sec0, sec_new),
                Transform(dq, dq_new),
                run_time=NORMAL,
            )
            self.wait(0.4)

        # Highlight: the limit
        limit_label = Text(
            "As h -> 0, the secant becomes the tangent!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(limit_label, direction=DOWN, anchor=dq, buff=0.3)
        self.play(Write(limit_label), run_time=NORMAL)
        self.wait(0.5)

        # Show tangent line (slope = 2 for x^2 at x=1)
        tangent = Line(
            axes.c2p(0.0, -1.0),
            axes.c2p(2.5, 4.0),
            color=SECONDARY, stroke_width=3,
        )
        self.play(
            Transform(sec0, tangent),
            FadeOut(dq), FadeOut(limit_label),
            run_time=NORMAL,
        )

        tangent_label = MathTex(
            r"\text{slope} = f'(1) = 2",
            font_size=SMALL_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(tangent_label, direction=DOWN, anchor=axes, buff=0.2)
        self.play(Write(tangent_label), run_time=FAST)
        self.wait(1)
        self.ly.clear()

    # --- Scene 2: Intro + Section Divider ---
    def scene2_intro(self):
        self.add_subcaption(
            "Let's start with the formal definition.",
            duration=3,
        )
        self.ly.section_divider("1", "The Formal Definition")
        self.ly.clear()

    # --- Scene 3: Formal Definition ---
    def scene3_formal_definition(self):
        self.add_subcaption(
            "The derivative captures instantaneous rate of change. "
            "We define it as the limit of the difference quotient. "
            "Let a be a point in the domain of f. We say f is "
            "differentiable at a if the limit as h approaches zero "
            "of the quotient f of a plus h minus f of a, all over "
            "h, exists and is finite. We denote this limit as "
            "f prime of a. "
            "An equivalent form uses x approaching a: the limit "
            "as x approaches a of f of x minus f of a over "
            "x minus a. Both forms give the same result. "
            "The key requirement is that the limit must exist "
            "and be finite, meaning both the left-hand and "
            "right-hand limits must agree.",
            duration=55,
        )
        title = self.ly.title("Definition: The Derivative")

        # Main definition
        def_main = MathTex(
            r"f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(def_main, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(def_main), run_time=SLOW)
        self.wait(0.5)

        # Condition
        condition = MathTex(
            r"\text{(limit exists and is finite)}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(condition, direction=DOWN, anchor=def_main, buff=0.4)
        self.play(Write(condition), run_time=NORMAL)
        self.wait(0.5)

        # Geometric reading
        geo = Text(
            "Geometrically: slope of the tangent line at (a, f(a))",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(geo, direction=DOWN, anchor=condition, buff=0.4)
        self.play(Write(geo), run_time=NORMAL)
        self.wait(0.5)

        # Equivalent form
        equiv = MathTex(
            r"f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(equiv, direction=DOWN, anchor=geo, buff=0.4)
        self.play(Write(equiv), run_time=NORMAL)
        self.wait(0.5)

        # Key requirement
        key = Text(
            "Both left and right limits must agree",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=equiv, buff=0.4)
        self.play(Write(key), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # --- Scene 4: Section Divider ---
    def scene4_divider_diff_cont(self):
        self.add_subcaption(
            "An important theorem: if a function is differentiable "
            "at a point, then it is continuous at that point.",
            duration=5,
        )
        self.ly.section_divider("2", "Differentiable Implies Continuous")
        self.ly.clear()

    # --- Scene 5: Theorem + Proof ---
    def scene5_diff_implies_continuous(self):
        self.add_subcaption(
            "Theorem: if f is differentiable at a, then f is "
            "continuous at a. "
            "Geometrically, if the tangent line exists, the "
            "function cannot have a jump. "
            "Here is the proof. We need to show that the limit "
            "as x approaches a of f of x equals f of a. "
            "The key trick is to factor the difference. "
            "We write f of x minus f of a as the quotient "
            "f of x minus f of a over x minus a, times "
            "x minus a. "
            "Now take the limit as x approaches a. "
            "The first factor approaches f prime of a, which "
            "exists by hypothesis. The second factor approaches "
            "zero. So the product approaches f prime of a "
            "times zero, which is zero. "
            "Therefore f of x approaches f of a, and f is "
            "continuous at a.",
            duration=65,
        )

        # Part 1: Geometric motivation
        title = self.ly.title("Theorem: Differentiable => Continuous")

        theorem_text = Text(
            "If f is differentiable at a, then f is continuous at a.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(theorem_text, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(theorem_text), run_time=NORMAL)
        self.wait(0.5)

        geo_insight = Text(
            "If the tangent line exists, the function can't jump!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(geo_insight, direction=DOWN, anchor=theorem_text, buff=0.4)
        self.play(Write(geo_insight), run_time=NORMAL)
        self.wait(1)

        # Part 2: Algebraic proof
        self.ly.clear()
        title2 = self.ly.title("Proof")

        # Need to show
        step1 = MathTex(
            r"\text{Show: } \lim_{x \to a} f(x) = f(a)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.3)

        # Factor the difference
        step2 = MathTex(
            r"f(x) - f(a) = \frac{f(x) - f(a)}{x - a} \cdot (x - a)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.4)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.5)

        # Take limits
        step3 = MathTex(
            r"\lim_{x \to a} [f(x) - f(a)] "
            r"= \underbrace{\lim_{x \to a} \frac{f(x) - f(a)}{x - a}}_{f'(a)} "
            r"\cdot \underbrace{\lim_{x \to a} (x - a)}_{0}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(step3, direction=DOWN, anchor=step2, buff=0.4)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(0.5)

        # Conclusion
        step4 = MathTex(
            r"= f'(a) \cdot 0 = 0 \implies f(x) \to f(a) \quad \text{QED}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step4, direction=DOWN, anchor=step3, buff=0.4)
        self.play(Write(step4), run_time=NORMAL)
        self.wait(0.5)

        insight = Text(
            "Key trick: factor into (difference quotient) times (x - a)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=step4, buff=0.4)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # --- Scene 6: Section Divider ---
    def scene6_divider_converse(self):
        self.add_subcaption(
            "But the converse is false. Being continuous does "
            "not guarantee being differentiable.",
            duration=4,
        )
        self.ly.section_divider("3", "The Converse Fails")
        self.ly.clear()

    # --- Scene 7: Counterexample |x| at 0 ---
    def scene7_counterexample_abs_x(self):
        self.add_subcaption(
            "The classic counterexample: f of x equals the absolute "
            "value of x at x equals zero. "
            "The graph is a V shape. From the right side, the "
            "secant slope approaches positive 1. From the left "
            "side, it approaches negative 1. The left and right "
            "limits disagree, so the derivative does not exist. "
            "Visually there is a corner, and no unique tangent "
            "line. Yet the function is continuous: the limit as "
            "x approaches zero of absolute value of x is zero, "
            "which equals f of zero.",
            duration=38,
        )
        title = self.ly.title(r"Counterexample: $f(x) = |x|$ at $x = 0$")

        # Graph of |x|
        axes = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-0.5, 3, 1],
            x_length=6.5, y_length=3.5,
            axis_config={"include_numbers": True, "font_size": 18, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        graph = axes.plot(
            lambda x: abs(x), x_range=[-2.3, 2.3],
            color=SECONDARY,
        )
        self.play(Create(graph), run_time=NORMAL)

        # Mark the origin
        p0 = Dot(axes.c2p(0, 0), color=ACCENT, radius=0.08)
        self.play(FadeIn(p0), run_time=FAST)

        # Right secant line (slope -> +1)
        sec_right = Line(
            axes.c2p(-0.3, -0.3), axes.c2p(2.5, 2.5),
            color=PRIMARY, stroke_width=2.5,
        )
        self.play(Create(sec_right), run_time=NORMAL)
        right_label = MathTex(
            r"\text{Right slope} \to +1",
            font_size=SMALL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(right_label, direction=DOWN, anchor=axes, buff=0.15)
        self.play(Write(right_label), run_time=FAST)
        self.wait(0.5)

        # Left secant line (slope -> -1)
        sec_left = Line(
            axes.c2p(-2.5, 2.5), axes.c2p(0.3, -0.3),
            color=RED, stroke_width=2.5,
        )
        self.play(Create(sec_left), run_time=NORMAL)
        left_label = MathTex(
            r"\text{Left slope} \to -1",
            font_size=SMALL_SIZE, color=RED,
        )
        self.ly.safe_place(left_label, direction=DOWN, anchor=axes, buff=0.15)
        self.play(
            FadeOut(right_label),
            Write(left_label),
            run_time=FAST,
        )
        self.wait(0.5)

        # Problem
        self.ly.clear()
        title2 = self.ly.title("Why It Fails")

        items = [
            Text("Right limit: slope -> +1", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Left limit: slope -> -1", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Limits disagree: derivative does NOT exist", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("But f(x) = |x| IS continuous at x = 0", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Continuous does NOT imply differentiable!", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(1)
        self.ly.clear()

    # --- Scene 8: Section Divider ---
    def scene8_divider_rules(self):
        self.add_subcaption(
            "All the derivative rules you know from calculus "
            "can be proved from the limit definition.",
            duration=4,
        )
        self.ly.section_divider("4", "Derivative Rules from the Definition")
        self.ly.clear()

    # --- Scene 9: Linearity and Product Rule ---
    def scene9_derivative_rules(self):
        self.add_subcaption(
            "We start with linearity. The derivative of f "
            "plus g at a equals the limit of the difference "
            "quotient for f plus g. By limit laws for sums, "
            "this splits into f prime of a plus g prime of a. "
            "Similarly, the scalar multiple rule says c times "
            "f prime of a. "
            "For the product rule, we need a trick. "
            "We expand f of a plus h times g of a plus h "
            "minus f of a times g of a, all over h. "
            "We add and subtract f of a plus h times g of a "
            "to split the expression. "
            "This gives us f of a plus h times the difference "
            "quotient for g, plus the difference quotient for "
            "f times g of a. "
            "Taking limits and using the continuity of f at a, "
            "we get f of a times g prime of a plus f prime of a "
            "times g of a. That is the product rule.",
            duration=80,
        )

        # Part 1: Linearity
        title = self.ly.title("Sum Rule (Linearity)")

        step1 = MathTex(
            r"(f + g)'(a) = \lim_{h \to 0} \frac{[f(a+h) + g(a+h)] - [f(a) + g(a)]}{h}",
            font_size=SMALL_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.3)

        step2 = MathTex(
            r"= \underbrace{\lim_{h \to 0} \frac{f(a+h) - f(a)}{h}}_{f'(a)}"
            r" + \underbrace{\lim_{h \to 0} \frac{g(a+h) - g(a)}{h}}_{g'(a)}",
            font_size=SMALL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.4)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.3)

        result1 = Text(
            "= f'(a) + g'(a)   [just limit laws for sums!]",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(result1, direction=DOWN, anchor=step2, buff=0.4)
        self.play(Write(result1), run_time=NORMAL)
        self.wait(0.5)

        scalar = MathTex(
            r"(cf)'(a) = c \cdot f'(a) \qquad [\text{scalar multiple rule}]",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(scalar, direction=DOWN, anchor=result1, buff=0.4)
        self.play(Write(scalar), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # Part 2: Product Rule
        title2 = self.ly.title("Product Rule")

        pr_setup = MathTex(
            r"(fg)'(a) = \lim_{h \to 0} \frac{f(a+h)\,g(a+h) - f(a)\,g(a)}{h}",
            font_size=SMALL_SIZE, color=WHITE,
        )
        self.ly.safe_place(pr_setup, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(pr_setup), run_time=NORMAL)
        self.wait(0.5)
        self.ly.clear()

        title3 = self.ly.title("Product Rule: The Trick")

        trick = MathTex(
            r"\text{Add and subtract } f(a+h)\,g(a)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(trick, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(trick), run_time=NORMAL)
        self.wait(0.5)

        pr_expand = MathTex(
            r"= f(a+h) \cdot \frac{g(a+h) - g(a)}{h}"
            r" + \frac{f(a+h) - f(a)}{h} \cdot g(a)",
            font_size=SMALL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(pr_expand, direction=DOWN, anchor=trick, buff=0.4)
        self.play(Write(pr_expand), run_time=NORMAL)
        self.wait(0.5)

        pr_result = MathTex(
            r"= f(a)\,g'(a) + f'(a)\,g(a)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(pr_result, direction=DOWN, anchor=pr_expand, buff=0.5)
        self.play(Write(pr_result), run_time=NORMAL)
        self.wait(0.5)

        note = Text(
            "Used: continuity of f at a (so f(a+h) -> f(a))",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=pr_result, buff=0.3)
        self.play(Write(note), run_time=FAST)
        self.wait(1)
        self.ly.clear()

    # --- Scene 10: Differentiability on Intervals + Lipschitz ---
    def scene10_intervals_lipschitz(self):
        self.add_subcaption(
            "We say f is differentiable on an open interval "
            "if it is differentiable at every point. "
            "On a closed interval, we also require one-sided "
            "derivatives at the endpoints. "
            "Now the key connection to our earlier topics. "
            "If f is differentiable on the closed interval "
            "a b and the absolute value of f prime of x is "
            "bounded by M for all x, then f is Lipschitz "
            "with constant M on a b. "
            "By the Mean Value Theorem, for any x and y, "
            "the absolute value of f of x minus f of y "
            "equals the absolute value of f prime of c times "
            "x minus y, which is at most M times the absolute "
            "value of x minus y. "
            "This gives us a cascade: differentiable with "
            "bounded derivative implies Lipschitz implies "
            "uniformly continuous implies continuous. "
            "This extends the hierarchy from our last video, "
            "with differentiability at the top.",
            duration=80,
        )
        title = self.ly.title("Differentiability on Intervals")

        # Definition
        def_open = Text(
            "Differentiable on (a,b): differentiable at EVERY point",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(def_open, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(def_open), run_time=NORMAL)
        self.wait(0.3)

        # One-sided derivatives
        os_def = MathTex(
            r"f'_+(a) = \lim_{h \to 0^+} \frac{f(a+h) - f(a)}{h} "
            r"\qquad "
            r"f'_-(b) = \lim_{h \to 0^-} \frac{f(b+h) - f(b)}{h}",
            font_size=SMALL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(os_def, direction=DOWN, anchor=def_open, buff=0.4)
        self.play(Write(os_def), run_time=NORMAL)
        self.wait(0.5)

        def_closed = Text(
            "Differentiable on [a,b]: also need one-sided derivatives at endpoints",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(def_closed, direction=DOWN, anchor=os_def, buff=0.3)
        self.play(Write(def_closed), run_time=NORMAL)
        self.wait(1)

        # Lipschitz Connection
        self.ly.clear()
        title2 = self.ly.title("The Lipschitz Connection")

        theorem = Text(
            "If f is differentiable on [a,b] and |f'(x)| <= M,",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(theorem, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(theorem), run_time=NORMAL)
        self.wait(0.3)

        theorem2 = Text(
            "then f is Lipschitz on [a,b] with constant M.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(theorem2, direction=DOWN, anchor=theorem, buff=0.3)
        self.play(Write(theorem2), run_time=NORMAL)
        self.wait(0.5)

        # Sketch
        sketch = MathTex(
            r"|f(x) - f(y)| = |f'(c)|\,|x-y| \leq M\,|x-y|",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(sketch, direction=DOWN, anchor=theorem2, buff=0.4)
        self.play(Write(sketch), run_time=NORMAL)
        self.wait(0.5)

        mvt_note = Text(
            "(by the Mean Value Theorem, for some c between x and y)",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(mvt_note, direction=DOWN, anchor=sketch, buff=0.3)
        self.play(Write(mvt_note), run_time=FAST)
        self.wait(1)

        # Cascade
        self.ly.clear()
        title3 = self.ly.title("The Cascade")

        cascade = [
            Text("Differentiable (bounded derivative on [a,b])", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("       => Lipschitz", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("       => Uniformly Continuous", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("       => Continuous", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(cascade, start_from=title3)
        self.wait(0.5)

        from_video = Text(
            "(Builds on Video 104's hierarchy!)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(from_video, direction=DOWN, anchor=cascade[-1], buff=0.3)
        self.play(Write(from_video), run_time=FAST)
        self.wait(1)
        self.ly.clear()

    # --- Scene 11: Summary + Outro ---
    def scene11_summary_outro(self):
        self.add_subcaption(
            "Let's review what we covered today. "
            "The derivative is the limit of the difference "
            "quotient f of a plus h minus f of a over h "
            "as h approaches zero. "
            "Differentiable at a point implies continuous at "
            "that point, but the converse fails as shown by "
            "the absolute value function at zero. "
            "All derivative rules follow from the limit "
            "definition using limit laws. "
            "On a closed interval, a bounded derivative "
            "implies Lipschitz implies uniformly continuous. "
            "Next time we will cover the Mean Value Theorem "
            "and its consequences.",
            duration=42,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text("Derivative = limit of [f(a+h) - f(a)] / h as h -> 0", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Differentiable => continuous (converse fails: |x| at 0)", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("All rules follow from the limit definition + limit laws", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Bounded derivative on [a,b] => Lipschitz => Uniformly Continuous", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title)
        self.wait(1)
        self.ly.clear()

        play_outro(self, "The Mean Value Theorem", "Real Analysis I")
