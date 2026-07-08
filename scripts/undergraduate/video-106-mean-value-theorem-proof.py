"""
Video 106: Mean Value Theorem (Proof)
TEMPLATE v2 -- Professional quality Manim script

Playlist: Real Analysis I (Video 8 of 12)
Class: Video106_MeanValueTheoremProof

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


class Video106_MeanValueTheoremProof(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_fermat_theorem()
        self.scene4_rolle_theorem()
        self.scene5_mvt_statement()
        self.scene6_auxiliary_function()
        self.scene7_mvt_proof()
        self.scene8_counterexamples()
        self.scene9_consequences()
        self.scene10_summary_outro()

    # --- Scene 1: Hook --- The Driving Intuition ---
    def scene1_hook(self):
        self.add_subcaption(
            "Imagine driving 120 miles in 2 hours. Your average "
            "speed is 60 miles per hour. At some moment during "
            "the trip, your speedometer must have read exactly "
            "60 miles per hour. The Mean Value Theorem proves "
            "this is always true for nice functions. If f is "
            "continuous on a closed interval and differentiable "
            "on the open interval, then there is a point where "
            "the instantaneous rate of change equals the "
            "average rate of change.",
            duration=40,
        )
        play_intro(self, "Mean Value Theorem (Proof)", "Real Analysis I")

        title = self.ly.title("The Driving Intuition")

        # Distance vs time graph
        axes = Axes(
            x_range=[-0.2, 2.5, 1], y_range=[-0.2, 130, 30],
            x_length=6.0, y_length=3.2,
            axis_config={"include_numbers": True, "font_size": 18, "stroke_width": 1.5},
            x_label="time (hours)", y_label="distance (miles)",
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        # Curve: distance function, slightly curved (accelerate then decelerate)
        def dist_func(t):
            return 60 * t + 10 * np.sin(2 * np.pi * t / 2)

        graph = axes.plot(dist_func, x_range=[0, 2], color=PRIMARY, stroke_width=3)
        self.play(Create(graph), run_time=NORMAL)

        # Mark endpoints
        p_a = Dot(axes.c2p(0, 0), color=WHITE, radius=0.06)
        p_b = Dot(axes.c2p(2, 120), color=WHITE, radius=0.06)
        self.play(FadeIn(p_a), FadeIn(p_b), run_time=FAST)

        # Secant line (average speed = 60)
        secant = Line(
            axes.c2p(-0.1, -6), axes.c2p(2.3, 138),
            color=SECONDARY, stroke_width=2.5,
        )
        self.play(Create(secant), run_time=NORMAL)
        secant_label = MathTex(
            r"\text{avg speed} = 60\ \text{mph}",
            font_size=SMALL_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(secant_label, direction=DOWN, anchor=axes, buff=0.1)
        self.play(Write(secant_label), run_time=FAST)
        self.wait(0.5)

        # Tangent at MVT point (around t=0.5 where slope = 60)
        mvt_t = 0.5
        mvt_y = dist_func(mvt_t)
        p_c = Dot(axes.c2p(mvt_t, mvt_y), color=ACCENT, radius=0.08)
        self.play(FadeIn(p_c), run_time=FAST)

        # Compute tangent slope at t=0.5
        h = 0.001
        tangent_slope = (dist_func(mvt_t + h) - dist_func(mvt_t - h)) / (2 * h)
        tangent = Line(
            axes.c2p(mvt_t - 0.4, mvt_y - 0.4 * tangent_slope),
            axes.c2p(mvt_t + 0.4, mvt_y + 0.4 * tangent_slope),
            color=ACCENT, stroke_width=3,
        )
        self.play(Create(tangent), run_time=NORMAL)

        tangent_label = MathTex(
            r"\text{inst. speed} = f'(c) = 60",
            font_size=SMALL_SIZE, color=ACCENT,
        )
        self.ly.safe_place(tangent_label, direction=RIGHT, anchor=p_c, buff=0.2)
        self.play(Write(tangent_label), run_time=FAST)
        self.wait(0.5)

        # Key insight text
        self.ly.clear()
        title2 = self.ly.title("The Key Idea")

        items = [
            Text("Average rate of change = secant slope", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Instantaneous rate = tangent slope", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("MVT: They must be equal somewhere!", font_size=HEADING_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(1)
        self.ly.clear()

    # --- Scene 2: Intro + Section Divider ---
    def scene2_intro(self):
        self.add_subcaption(
            "We build up to the Mean Value Theorem through "
            "two prerequisite theorems: Fermat's Theorem "
            "and Rolle's Theorem.",
            duration=6,
        )
        self.ly.section_divider("1", "Fermat's Theorem")
        self.ly.clear()

    # --- Scene 3: Fermat's Theorem ---
    def scene3_fermat_theorem(self):
        self.add_subcaption(
            "Fermat's Theorem says that if f has a local "
            "maximum or minimum at a point c inside the "
            "interval, and the derivative exists at c, then "
            "f prime of c equals zero. "
            "The idea: at a local maximum, the function goes "
            "up on the left and down on the right. The "
            "difference quotients have opposite signs. Since "
            "both one-sided limits must equal f prime of c, "
            "the only possibility is zero. "
            "The same argument works for a local minimum.",
            duration=48,
        )

        title = self.ly.title("Fermat's Theorem")

        statement = Text(
            "If f has a local extremum at c in (a,b) and f'(c) exists,",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(statement, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(statement), run_time=NORMAL)

        conclusion = MathTex(
            r"\text{then } f'(c) = 0",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(conclusion, direction=DOWN, anchor=statement, buff=0.4)
        self.play(Write(conclusion), run_time=NORMAL)
        self.wait(0.5)

        # Graph with local maximum
        self.ly.clear()
        title2 = self.ly.title("Proof Idea: Local Maximum")

        axes = Axes(
            x_range=[-0.5, 4.5, 1], y_range=[-0.5, 4, 1],
            x_length=6.0, y_length=2.8,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=FAST)

        # Bell-like curve with a peak
        curve_func = lambda x: 3 * np.exp(-0.5 * ((x - 2) / 0.8) ** 2)
        graph = axes.plot(curve_func, x_range=[0, 4], color=PRIMARY, stroke_width=3)
        self.play(Create(graph), run_time=NORMAL)

        c_val = 2.0
        p_c = Dot(axes.c2p(c_val, curve_func(c_val)), color=ACCENT, radius=0.08)
        self.play(FadeIn(p_c), run_time=FAST)

        # Right side slopes negative
        right_line = Line(
            axes.c2p(2.0, 3.0), axes.c2p(2.8, 1.8),
            color=RED, stroke_width=2.5,
        )
        self.play(Create(right_line), run_time=FAST)
        right_text = MathTex(
            r"\frac{f(c+h) - f(c)}{h} \leq 0",
            font_size=SMALL_SIZE, color=RED,
        )
        self.ly.safe_place(right_text, direction=DOWN, anchor=axes, buff=0.1)
        self.play(Write(right_text), run_time=FAST)
        self.wait(0.5)

        # Left side slopes positive
        left_line = Line(
            axes.c2p(1.2, 1.8), axes.c2p(2.0, 3.0),
            color=PRIMARY, stroke_width=2.5,
        )
        self.play(
            FadeOut(right_line), FadeOut(right_text),
            Create(left_line), run_time=NORMAL,
        )
        left_text = MathTex(
            r"\frac{f(c+h) - f(c)}{h} \geq 0 \text{ (for } h < 0\text{)}",
            font_size=SMALL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(left_text, direction=DOWN, anchor=axes, buff=0.1)
        self.play(Write(left_text), run_time=FAST)
        self.wait(0.5)

        # Conclusion
        result = MathTex(
            r"0 \leq f'(c) \leq 0 \implies f'(c) = 0",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=left_text, buff=0.3)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # --- Scene 4: Rolle's Theorem ---
    def scene4_rolle_theorem(self):
        self.add_subcaption(
            "Rolle's Theorem says: if f is continuous on the "
            "closed interval a b, differentiable on the open "
            "interval, and f of a equals f of b, then there "
            "exists c in the open interval with f prime of c "
            "equals zero. "
            "The proof uses the Extreme Value Theorem: f "
            "attains a maximum and minimum on the closed "
            "interval. If they are equal, f is constant and "
            "any point works. If they differ, at least one "
            "extreme is at an interior point, and Fermat's "
            "Theorem gives f prime equals zero there.",
            duration=50,
        )
        self.ly.section_divider("2", "Rolle's Theorem")

        # Statement
        title = self.ly.title("Rolle's Theorem")

        # Geometric picture
        axes = Axes(
            x_range=[-0.5, 4.5, 1], y_range=[-0.5, 4, 1],
            x_length=5.5, y_length=2.5,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=FAST)

        # Curve that starts and ends at same height
        def rolle_func(x):
            return 2 + 1.5 * np.sin(np.pi * x / 4)

        graph = axes.plot(rolle_func, x_range=[0.3, 3.7], color=PRIMARY, stroke_width=3)
        self.play(Create(graph), run_time=NORMAL)

        # Mark equal heights
        p_a = Dot(axes.c2p(0.3, rolle_func(0.3)), color=SECONDARY, radius=0.06)
        p_b = Dot(axes.c2p(3.7, rolle_func(3.7)), color=SECONDARY, radius=0.06)
        self.play(FadeIn(p_a), FadeIn(p_b), run_time=FAST)

        # Mark a,b labels
        a_label = MathTex(r"a", font_size=SMALL_SIZE, color=SECONDARY)
        b_label = MathTex(r"b", font_size=SMALL_SIZE, color=SECONDARY)
        a_label.next_to(p_a, DOWN, buff=0.15)
        b_label.next_to(p_b, DOWN, buff=0.15)
        self.play(Write(a_label), Write(b_label), run_time=FAST)

        # Dashed line showing f(a) = f(b)
        eq_line = DashedLine(
            axes.c2p(0.3, rolle_func(0.3)),
            axes.c2p(3.7, rolle_func(3.7)),
            color=DIM, stroke_width=1.5,
        )
        self.play(Create(eq_line), run_time=FAST)
        self.wait(0.5)

        # Horizontal tangent at interior point
        c_val = 2.0
        c_y = rolle_func(c_val)
        p_c = Dot(axes.c2p(c_val, c_y), color=ACCENT, radius=0.08)
        horiz = Line(
            axes.c2p(1.2, c_y), axes.c2p(2.8, c_y),
            color=ACCENT, stroke_width=3,
        )
        self.play(FadeIn(p_c), Create(horiz), run_time=NORMAL)

        h_label = MathTex(
            r"f'(c) = 0",
            font_size=SMALL_SIZE, color=ACCENT,
        )
        self.ly.safe_place(h_label, direction=RIGHT, anchor=p_c, buff=0.15)
        self.play(Write(h_label), run_time=FAST)
        self.wait(1)

        # Proof
        self.ly.clear()
        title2 = self.ly.title("Proof of Rolle's Theorem")

        step1 = Text(
            "By Extreme Value Theorem: f attains max M and min m on [a,b]",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.3)

        step2 = Text(
            "Case 1: M = m => f is constant => f'(c) = 0 everywhere",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.4)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.3)

        step3 = Text(
            "Case 2: M > m => at least one extreme at interior point c",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(step3, direction=DOWN, anchor=step2, buff=0.4)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(0.3)

        step4 = Text(
            "Apply Fermat's Theorem: f'(c) = 0. QED.",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(step4, direction=DOWN, anchor=step3, buff=0.4)
        self.play(Write(step4), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # --- Scene 5: MVT Statement ---
    def scene5_mvt_statement(self):
        self.add_subcaption(
            "Now we state the Mean Value Theorem. "
            "If f is continuous on the closed interval a b "
            "and differentiable on the open interval, then "
            "there exists a point c in the open interval such "
            "that f prime of c equals the slope of the "
            "secant line from a to b, that is, f of b minus "
            "f of a over b minus a.",
            duration=20,
        )
        self.ly.section_divider("3", "The Mean Value Theorem")

        title = self.ly.title("Mean Value Theorem")

        # Condition 1
        cond1 = Text(
            "f is continuous on [a, b]",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(cond1, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(cond1), run_time=NORMAL)
        self.wait(0.3)

        # Condition 2
        cond2 = Text(
            "f is differentiable on (a, b)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(cond2, direction=DOWN, anchor=cond1, buff=0.4)
        self.play(Write(cond2), run_time=NORMAL)
        self.wait(0.3)

        # Conclusion formula
        conclusion = MathTex(
            r"\exists\, c \in (a,b): \quad f'(c) = \frac{f(b) - f(a)}{b - a}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(conclusion, direction=DOWN, anchor=cond2, buff=0.5)
        self.play(Write(conclusion), run_time=SLOW)
        self.wait(0.5)

        # Geometric reading
        geo = Text(
            "The tangent slope equals the secant slope somewhere!",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(geo, direction=DOWN, anchor=conclusion, buff=0.4)
        self.play(Write(geo), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # --- Scene 6: Auxiliary Function (Key Insight) ---
    def scene6_auxiliary_function(self):
        self.add_subcaption(
            "The proof strategy is beautiful. We construct an "
            "auxiliary function that lets us apply Rolle's "
            "Theorem. "
            "Start with f of x. Draw the secant line L of x "
            "through the endpoints a and b. "
            "Define h of x equals f of x minus L of x, the "
            "difference between the curve and the secant. "
            "At the endpoints, h of a equals f of a minus "
            "L of a, which is f of a minus f of a, equals "
            "zero. Similarly h of b equals zero. "
            "So h of a equals h of b equals zero! "
            "Rolle's Theorem applies to h, giving us h prime "
            "of c equals zero for some c in the open "
            "interval. From there, the MVT follows.",
            duration=65,
        )

        title = self.ly.title("The Key Insight: Auxiliary Function")

        # Step 1: Show f(x)
        axes = Axes(
            x_range=[-0.3, 3.8, 1], y_range=[-0.5, 5, 1],
            x_length=6.0, y_length=3.0,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=FAST)

        # f(x) - a nice curve
        def f_func(x):
            return 1.5 + 0.8 * x + 0.5 * np.sin(x) * x

        a_val, b_val = 0.5, 3.5
        f_a = f_func(a_val)
        f_b = f_func(b_val)

        graph_f = axes.plot(f_func, x_range=[0.2, 3.7], color=PRIMARY, stroke_width=3)
        self.play(Create(graph_f), run_time=NORMAL)

        f_label = MathTex(r"f(x)", font_size=SMALL_SIZE, color=PRIMARY)
        f_label.next_to(graph_f, UP, buff=0.1)
        self.play(Write(f_label), run_time=FAST)
        self.wait(0.3)

        # Step 2: Draw secant line
        slope = (f_b - f_a) / (b_val - a_val)
        secant = Line(
            axes.c2p(a_val - 0.3, f_a - 0.3 * slope),
            axes.c2p(b_val + 0.3, f_b + 0.3 * slope),
            color=SECONDARY, stroke_width=2.5,
        )
        self.play(Create(secant), run_time=NORMAL)

        # Mark endpoints
        p_a = Dot(axes.c2p(a_val, f_a), color=WHITE, radius=0.06)
        p_b = Dot(axes.c2p(b_val, f_b), color=WHITE, radius=0.06)
        a_lbl = MathTex(r"a", font_size=SMALL_SIZE, color=WHITE)
        b_lbl = MathTex(r"b", font_size=SMALL_SIZE, color=WHITE)
        a_lbl.next_to(p_a, DOWN, buff=0.1)
        b_lbl.next_to(p_b, DOWN, buff=0.1)
        self.play(FadeIn(p_a), FadeIn(p_b), Write(a_lbl), Write(b_lbl), run_time=FAST)

        L_label = MathTex(r"L(x)", font_size=SMALL_SIZE, color=SECONDARY)
        L_label.next_to(secant, UP, buff=0.1)
        self.play(Write(L_label), run_time=FAST)
        self.wait(0.5)

        # Step 3: Define h(x) = f(x) - L(x)
        self.ly.clear()
        title2 = self.ly.title("Construct h(x) = f(x) - L(x)")

        # Show both f and secant again, then "subtract"
        axes2 = Axes(
            x_range=[-0.3, 3.8, 1], y_range=[-0.5, 5, 1],
            x_length=6.0, y_length=3.0,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes2)
        clamp_position(axes2)
        self.play(Create(axes2), run_time=FAST)

        graph_f2 = axes2.plot(f_func, x_range=[0.2, 3.7], color=PRIMARY, stroke_width=3)
        self.play(Create(graph_f2), run_time=NORMAL)

        secant2 = Line(
            axes2.c2p(a_val - 0.3, f_a - 0.3 * slope),
            axes2.c2p(b_val + 0.3, f_b + 0.3 * slope),
            color=SECONDARY, stroke_width=2.5,
        )
        self.play(Create(secant2), run_time=NORMAL)
        self.wait(0.3)

        # Subtract secant to get h(x)
        h_func = lambda x: f_func(x) - (f_a + slope * (x - a_val))
        graph_h = axes2.plot(h_func, x_range=[0.2, 3.7], color=ACCENT, stroke_width=3)

        # Animate: fade out f and secant, show h
        self.play(
            FadeOut(graph_f2), FadeOut(secant2),
            Transform(axes2.copy(), axes2),
            run_time=NORMAL,
        )
        self.remove(*[m for m in self.mobjects if m not in [axes2]])
        # Recreate axes cleanly
        self.ly.clear()

        title3 = self.ly.title("h(x) = f(x) - L(x)")

        axes3 = Axes(
            x_range=[-0.3, 3.8, 1], y_range=[-1.5, 2.5, 1],
            x_length=6.0, y_length=3.0,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes3)
        clamp_position(axes3)
        self.play(Create(axes3), run_time=FAST)

        graph_h2 = axes3.plot(h_func, x_range=[0.2, 3.7], color=ACCENT, stroke_width=3)
        self.play(Create(graph_h2), run_time=NORMAL)

        # Mark h(a) = 0 and h(b) = 0
        p_ha = Dot(axes3.c2p(a_val, 0), color=RED, radius=0.08)
        p_hb = Dot(axes3.c2p(b_val, 0), color=RED, radius=0.08)
        self.play(FadeIn(p_ha), FadeIn(p_hb), run_time=FAST)

        ha_label = MathTex(r"h(a) = 0", font_size=SMALL_SIZE, color=RED)
        hb_label = MathTex(r"h(b) = 0", font_size=SMALL_SIZE, color=RED)
        ha_label.next_to(p_ha, DOWN, buff=0.1)
        hb_label.next_to(p_hb, DOWN, buff=0.1)
        self.play(Write(ha_label), Write(hb_label), run_time=FAST)
        self.wait(0.5)

        # Highlight: Rolle's applies!
        rolle_text = Text(
            "h(a) = h(b) = 0 => Rolle's Theorem applies!",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(rolle_text, direction=DOWN, anchor=axes3, buff=0.15)
        self.play(Write(rolle_text), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # --- Scene 7: MVT Formal Proof ---
    def scene7_mvt_proof(self):
        self.add_subcaption(
            "Now the formal proof. Define h of x equals f of x "
            "minus f of a minus the fraction f of b minus f of "
            "a over b minus a, times x minus a. "
            "This function is continuous on a b because f is "
            "continuous and the rest is a polynomial. It is "
            "differentiable on the open interval. "
            "Checking the endpoints: h of a is zero by "
            "direct substitution, and h of b is also zero. "
            "By Rolle's Theorem, there exists c in the open "
            "interval with h prime of c equals zero. "
            "Taking the derivative: h prime of x equals f "
            "prime of x minus the secant slope. Setting to "
            "zero and solving: f prime of c equals f of b "
            "minus f of a over b minus a. QED.",
            duration=65,
        )

        title = self.ly.title("Formal Proof")

        # Define h
        step1 = MathTex(
            r"h(x) = f(x) - f(a) - \frac{f(b)-f(a)}{b-a}(x-a)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(step1), run_time=SLOW)
        self.wait(0.5)

        # Verify conditions
        self.ly.clear()
        title2 = self.ly.title("Verify Rolle's Conditions")

        check1 = MathTex(
            r"h \text{ continuous on } [a,b] \checkmark",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(check1, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(check1), run_time=NORMAL)
        self.wait(0.3)

        check2 = MathTex(
            r"h \text{ differentiable on } (a,b) \checkmark",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(check2, direction=DOWN, anchor=check1, buff=0.4)
        self.play(Write(check2), run_time=NORMAL)
        self.wait(0.3)

        check3 = MathTex(
            r"h(a) = 0, \quad h(b) = 0 \checkmark",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(check3, direction=DOWN, anchor=check2, buff=0.4)
        self.play(Write(check3), run_time=NORMAL)
        self.wait(0.5)

        # Apply Rolle and conclude
        self.ly.clear()
        title3 = self.ly.title("Apply Rolle's Theorem")

        rolle = Text(
            "By Rolle's: exists c in (a,b) with h'(c) = 0",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(rolle, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(rolle), run_time=NORMAL)
        self.wait(0.3)

        deriv = MathTex(
            r"h'(x) = f'(x) - \frac{f(b)-f(a)}{b-a}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(deriv, direction=DOWN, anchor=rolle, buff=0.4)
        self.play(Write(deriv), run_time=NORMAL)
        self.wait(0.3)

        set_zero = MathTex(
            r"h'(c) = 0 \implies f'(c) = \frac{f(b)-f(a)}{b-a}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(set_zero, direction=DOWN, anchor=deriv, buff=0.5)
        self.play(Write(set_zero), run_time=SLOW)
        self.wait(0.5)

        qed = Text(
            "QED  --  The Mean Value Theorem is proved!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(qed, direction=DOWN, anchor=set_zero, buff=0.5)
        self.play(Write(qed), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # --- Scene 8: Counterexamples ---
    def scene8_counterexamples(self):
        self.add_subcaption(
            "Both conditions of the Mean Value Theorem are "
            "necessary. If we drop either one, the theorem "
            "fails. "
            "First: suppose f is not continuous on the closed "
            "interval. A jump discontinuity means the "
            "function can skip past every secant slope. "
            "Second: suppose f is not differentiable at one "
            "point. A sharp corner can prevent any tangent "
            "from matching the secant slope.",
            duration=38,
        )

        title = self.ly.title("Why Conditions Are Necessary")

        # Counterexample 1: Not continuous
        sub1 = Text(
            "Counterexample 1: f not continuous on [a,b]",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(sub1, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(sub1), run_time=NORMAL)

        axes1 = Axes(
            x_range=[-0.3, 3.3, 1], y_range=[-0.5, 3.5, 1],
            x_length=4.5, y_length=2.2,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        )
        self.ly.safe_place(axes1, direction=DOWN, anchor=sub1, buff=0.3)
        clamp_position(axes1)
        self.play(Create(axes1), run_time=FAST)

        # Function with jump: low on left, jumps up on right
        g1_left = axes1.plot(lambda x: 0.5 + x, x_range=[0.2, 1.4], color=PRIMARY, stroke_width=3)
        g1_right = axes1.plot(lambda x: 2.5 + 0.3 * (x - 1.5), x_range=[1.6, 2.8], color=PRIMARY, stroke_width=3)
        self.play(Create(g1_left), Create(g1_right), run_time=NORMAL)

        # Open/closed dots at jump
        dot_open = Dot(axes1.c2p(1.4, 1.9), color=RED, radius=0.06)
        dot_open2 = Circle(axes1.c2p(1.4, 1.9), radius=0.1, color=RED, stroke_width=2)
        dot_solid = Dot(axes1.c2p(1.6, 2.58), color=PRIMARY, radius=0.06)
        self.play(FadeIn(dot_open), FadeIn(dot_solid), run_time=FAST)

        fail1 = Text(
            "No tangent matches the secant slope!",
            font_size=SMALL_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(fail1, direction=DOWN, anchor=axes1, buff=0.1)
        self.play(Write(fail1), run_time=FAST)
        self.wait(0.5)

        # Counterexample 2: Not differentiable
        self.ly.clear()
        title2 = self.ly.title("Why Conditions Are Necessary")

        sub2 = Text(
            "Counterexample 2: f not differentiable at a point",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(sub2, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(sub2), run_time=NORMAL)

        axes2 = Axes(
            x_range=[-0.3, 3.3, 1], y_range=[-0.5, 3.5, 1],
            x_length=4.5, y_length=2.2,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        )
        self.ly.safe_place(axes2, direction=DOWN, anchor=sub2, buff=0.3)
        clamp_position(axes2)
        self.play(Create(axes2), run_time=FAST)

        # V-shaped function (|x| style corner)
        corner_x = 1.5
        g2_left = axes2.plot(lambda x: 2.5 - abs(x - corner_x), x_range=[0.2, corner_x], color=PRIMARY, stroke_width=3)
        g2_right = axes2.plot(lambda x: 2.5 - abs(x - corner_x), x_range=[corner_x, 2.8], color=PRIMARY, stroke_width=3)
        self.play(Create(g2_left), Create(g2_right), run_time=NORMAL)

        corner_dot = Dot(axes2.c2p(corner_x, 2.5), color=RED, radius=0.08)
        self.play(FadeIn(corner_dot), run_time=FAST)

        fail2 = Text(
            "The corner prevents any matching tangent!",
            font_size=SMALL_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(fail2, direction=DOWN, anchor=axes2, buff=0.1)
        self.play(Write(fail2), run_time=FAST)
        self.wait(0.5)

        summary = Text(
            "Both continuity AND differentiability are required.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(summary, direction=DOWN, anchor=fail2, buff=0.3)
        self.play(Write(summary), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # --- Scene 9: Consequences ---
    def scene9_consequences(self):
        self.add_subcaption(
            "The Mean Value Theorem has powerful consequences. "
            "First: if f prime equals zero everywhere on an "
            "interval, then f is constant. By the MVT, for "
            "any a and b, f of b minus f of a equals f prime "
            "of c times b minus a, which is zero times b "
            "minus a, equals zero. "
            "Second: if f prime is positive everywhere, then "
            "f is strictly increasing. If f prime is "
            "negative, then f is strictly decreasing. "
            "Third: if the absolute value of f prime is "
            "bounded by M, then f is Lipschitz with constant "
            "M. This connects back to our earlier hierarchy: "
            "bounded derivative implies Lipschitz implies "
            "uniformly continuous implies continuous.",
            duration=60,
        )

        title = self.ly.title("Consequences of the MVT")

        # Consequence 1
        c1_title = Text(
            "1.  f'(x) = 0 for all x  =>  f is constant",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(c1_title, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(c1_title), run_time=NORMAL)

        c1_proof = MathTex(
            r"f(b) - f(a) = f'(c)(b-a) = 0 \cdot (b-a) = 0",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(c1_proof, direction=DOWN, anchor=c1_title, buff=0.3)
        self.play(Write(c1_proof), run_time=FAST)
        self.wait(0.5)

        # Consequence 2
        self.ly.clear()
        title2 = self.ly.title("Consequences of the MVT")

        c2_title = Text(
            "2.  f'(x) > 0  =>  f is strictly increasing",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(c2_title, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(c2_title), run_time=NORMAL)

        c2_proof = MathTex(
            r"f(b) - f(a) = f'(c)(b-a) > 0 \text{ when } a < b",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(c2_proof, direction=DOWN, anchor=c2_title, buff=0.3)
        self.play(Write(c2_proof), run_time=FAST)
        self.wait(0.5)

        c2b = Text(
            "f'(x) < 0  =>  f is strictly decreasing (same argument)",
            font_size=SMALL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(c2b, direction=DOWN, anchor=c2_proof, buff=0.3)
        self.play(Write(c2b), run_time=FAST)
        self.wait(0.5)

        # Consequence 3: Lipschitz
        self.ly.clear()
        title3 = self.ly.title("Consequences of the MVT")

        c3_title = Text(
            "3.  Bounded derivative  =>  Lipschitz",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(c3_title, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(c3_title), run_time=NORMAL)

        c3_eq = MathTex(
            r"|f'(x)| \leq M \implies |f(x)-f(y)| = |f'(c)|\,|x-y| \leq M|x-y|",
            font_size=SMALL_SIZE, color=WHITE,
        )
        self.ly.safe_place(c3_eq, direction=DOWN, anchor=c3_title, buff=0.4)
        self.play(Write(c3_eq), run_time=NORMAL)
        self.wait(0.5)

        cascade = Text(
            "Bounded f' => Lipschitz => Uniformly Continuous => Continuous",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(cascade, direction=DOWN, anchor=c3_eq, buff=0.4)
        self.play(Write(cascade), run_time=NORMAL)

        ref = Text(
            "(Connects to Videos 104 and 105!)",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(ref, direction=DOWN, anchor=cascade, buff=0.3)
        self.play(Write(ref), run_time=FAST)
        self.wait(1)
        self.ly.clear()

    # --- Scene 10: Summary + Outro ---
    def scene10_summary_outro(self):
        self.add_subcaption(
            "Let's recap. The proof chain builds from Fermat's "
            "Theorem through Rolle's Theorem to the Mean "
            "Value Theorem. "
            "The key technique is constructing the auxiliary "
            "function h of x equals f of x minus the secant "
            "line, which satisfies Rolle's conditions. "
            "Both continuity and differentiability are "
            "necessary. "
            "The consequences include: derivative zero means "
            "constant, positive derivative means increasing, "
            "and bounded derivative implies Lipschitz. "
            "Next time: the Riemann Integral.",
            duration=40,
        )

        title = self.ly.title("Proof Chain")

        # Chain diagram
        chain_items = [
            Text("Fermat's Theorem", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("     =>  Rolle's Theorem", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("     =>  Mean Value Theorem", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(chain_items, start_from=title)
        self.wait(0.5)

        # Key takeaways
        self.ly.clear()
        title2 = self.ly.title("Key Takeaways")

        takeaways = [
            Text("MVT: exists c with f'(c) = secant slope", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Proof: h(x) = f(x) - L(x), then apply Rolle's", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Both continuity and differentiability are needed", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("f'=0 => constant, f'>0 => increasing", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Bounded derivative => Lipschitz => Uniformly Continuous", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title2)
        self.wait(1)
        self.ly.clear()

        play_outro(self, "The Riemann Integral", "Real Analysis I")
