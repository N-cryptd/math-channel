"""
Video 108: Fundamental Theorem of Calculus (Proof)
TEMPLATE v2 -- Professional quality Manim script

Playlist: Real Analysis I (Video 10 of 12)
Class: Video108_FTCProof

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


class Video108_FTCProof(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_accumulation()
        self.scene4_mvt_integrals()
        self.scene5_ftc1_statement()
        self.scene6_ftc1_proof()
        self.scene7_ftc2_statement()
        self.scene8_ftc2_proof()
        self.scene9_example()
        self.scene10_summary()

    # --- Scene 1: Hook -- The Bridge Between Calculus ---
    def scene1_hook(self):
        self.add_subcaption(
            "Everything in calculus revolves around two "
            "operations. Differentiation finds the rate of "
            "change. Integration finds the total "
            "accumulation. These seem like opposites. And "
            "they are. The Fundamental Theorem of Calculus "
            "proves it. Today we prove both parts of the "
            "FTC rigorously, using the Riemann integral "
            "and the Mean Value Theorem.",
            duration=22.1,
        )
        play_intro(self, "Fundamental Theorem of Calculus", "Real Analysis I")

        title = self.ly.title("The Bridge")

        # Two pillars and a bridge
        diff_label = Text(
            "Differentiation", font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(diff_label, direction=LEFT, anchor=title, buff=1.0)
        clamp_position(diff_label)
        self.play(Write(diff_label), run_time=NORMAL)

        int_label = Text(
            "Integration", font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(int_label, direction=RIGHT, anchor=title, buff=1.0)
        clamp_position(int_label)
        self.play(Write(int_label), run_time=NORMAL)

        # Arrow connecting them
        arrow = Arrow(
            diff_label.get_right() + 0.3 * RIGHT,
            int_label.get_left() - 0.3 * RIGHT,
            buff=0.1, stroke_width=3, color=SECONDARY,
        )
        self.play(Create(arrow), run_time=NORMAL)

        bridge_label = Text(
            "FTC", font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(bridge_label, direction=DOWN, anchor=arrow, buff=0.1)
        self.play(Write(bridge_label), run_time=NORMAL)

        insight = Text(
            "Differentiation and integration are inverses!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=bridge_label, buff=0.3)
        self.play(Write(insight), run_time=NORMAL)
        # pacing: extends previous caption slot (seg#0 natural 22.1s, slot 19.1s -> 27.7s, Δ=8.6)
        self.wait(10.1)
        self.ly.clear()

    # --- Scene 2: Section Divider ---
    def scene2_intro(self):
        self.ly.section_divider("1", "The Accumulation Function")
        self.ly.clear()

    # --- Scene 3: The Accumulation Function ---
    def scene3_accumulation(self):
        self.add_subcaption(
            "Let f be continuous on the interval a to b. "
            "Fix a. Define the accumulation function F of x "
            "as the integral from a to x of f of t dt. "
            "This function measures the signed area under f "
            "from a to x. As x increases, F accumulates "
            "more area. What is the rate of change of "
            "this accumulation? In other words, what is "
            "F prime of x? This question leads to FTC "
            "Part 1.",
            duration=26.9,
        )

        title = self.ly.title("The Accumulation Function")

        # Define F(x)
        defn = MathTex(
            r"F(x) = \int_a^x f(t)\, dt",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(defn, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(defn), run_time=SLOW)
        self.wait(0.5)

        # Graph of f(t) with shaded area
        axes = Axes(
            x_range=[-0.3, 4.5, 1], y_range=[-0.3, 4.0, 1],
            x_length=5.5, y_length=2.5,
            axis_config={"include_numbers": False, "font_size": 16, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.remove(title, defn)
        self.play(Create(axes), run_time=NORMAL)

        # The function f(t)
        def f_func(x):
            return 0.5 * x + 1.0 + 0.4 * np.sin(x)

        graph = axes.plot(f_func, x_range=[0.5, 4], color=PRIMARY)
        self.play(Create(graph), run_time=NORMAL)

        # Labels
        a_dot = Dot(axes.c2p(0.5, 0), color=ACCENT, radius=0.06)
        a_lbl = MathTex(r"a", font_size=SMALL_SIZE, color=ACCENT)
        a_lbl.next_to(a_dot, DOWN, buff=0.15)
        self.play(FadeIn(a_dot), Write(a_lbl), run_time=FAST)

        # Moving x point
        x_dot = Dot(axes.c2p(2.5, 0), color=RED, radius=0.06)
        x_lbl = MathTex(r"x", font_size=SMALL_SIZE, color=RED)
        x_lbl.next_to(x_dot, DOWN, buff=0.15)
        self.play(FadeIn(x_dot), Write(x_lbl), run_time=FAST)

        # Shaded area from a to x (using Polygon)
        x_pos = 2.5
        x_a = 0.5
        n_pts = 30
        xs = np.linspace(x_a, x_pos, n_pts)
        area_points = [axes.c2p(x_a, 0)]
        for xi in xs:
            area_points.append(axes.c2p(xi, f_func(xi)))
        area_points.append(axes.c2p(x_pos, 0))
        shaded = Polygon(*area_points, fill_color=SECONDARY, fill_opacity=0.35, stroke_width=0)
        self.play(FadeIn(shaded), run_time=NORMAL)

        f_label = MathTex(r"y = f(t)", font_size=SMALL_SIZE, color=PRIMARY)
        self.ly.safe_place(f_label, direction=UP, anchor=axes, buff=0.05)
        clamp_position(f_label)
        self.play(Write(f_label), run_time=FAST)

        area_label = MathTex(
            r"F(x)", font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(area_label, direction=DOWN, anchor=axes, buff=0.1)
        self.play(Write(area_label), run_time=FAST)

        # Question
        question = MathTex(
            r"F'(x) = \, ?", font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(question, direction=RIGHT, anchor=area_label, buff=0.5)
        self.play(Write(question), run_time=NORMAL)
        # pacing: extends previous caption slot (seg#1 natural 26.9s, slot 12.7s -> 33.7s, Δ=21.0)
        self.wait(22.5)
        self.ly.clear()

    # --- Scene 4: MVT for Integrals ---
    def scene4_mvt_integrals(self):
        self.add_subcaption(
            "Before proving the FTC, we need a key lemma. "
            "The Mean Value Theorem for Integrals says: if f "
            "is continuous on a to b, there exists c in the "
            "open interval a to b such that the integral "
            "equals f of c times b minus a. Geometrically, "
            "the area under the curve equals the area of a "
            "rectangle with height f of c. Proof: by the "
            "Extreme Value Theorem, f attains its minimum m "
            "and maximum M. So m times b minus a is at most "
            "the integral, which is at most M times b minus a. "
            "Dividing by b minus a and applying the "
            "Intermediate Value Theorem gives the result.",
            duration=40.6,
        )
        self.ly.section_divider("2", "MVT for Integrals")
        self.ly.clear()

        title = self.ly.title("Lemma: MVT for Integrals")

        statement = MathTex(
            r"\exists\, c \in (a,b) : \int_a^b f(t)\, dt = f(c)(b - a)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(statement, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(statement), run_time=SLOW)
        self.wait(0.5)

        # Visual: function with rectangle
        axes = Axes(
            x_range=[-0.3, 4.5, 1], y_range=[-0.3, 4.0, 1],
            x_length=4.5, y_length=2.0,
            axis_config={"include_numbers": False, "font_size": 14, "stroke_width": 1.2},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.remove(title, statement)
        self.play(Create(axes), run_time=NORMAL)

        def g_func(x):
            return 1.5 + 0.8 * np.sin(1.2 * (x - 0.5))

        g_graph = axes.plot(g_func, x_range=[0.5, 4], color=PRIMARY)
        self.play(Create(g_graph), run_time=NORMAL)

        # Rectangle with height f(c)
        c_val = 2.2
        h_val = g_func(c_val)
        rect = Rectangle(
            width=axes.c2p(3.5, 0)[0] - axes.c2p(0, 0)[0],
            height=axes.c2p(0, h_val)[1] - axes.c2p(0, 0)[1],
        ).move_to(axes.c2p(0.5 + 1.75, h_val / 2))
        rect.set_stroke(color=ACCENT, width=1.5)
        rect.set_fill(color=ACCENT, opacity=0.25)
        self.play(FadeIn(rect), run_time=NORMAL)

        c_dot = Dot(axes.c2p(c_val, h_val), color=RED, radius=0.06)
        self.play(FadeIn(c_dot), run_time=FAST)

        c_lbl = MathTex(r"c", font_size=SMALL_SIZE, color=RED)
        c_lbl.next_to(c_dot, DOWN, buff=0.15)
        self.play(Write(c_lbl), run_time=FAST)

        fc_lbl = MathTex(r"f(c)", font_size=SMALL_SIZE, color=ACCENT)
        fc_lbl.next_to(c_dot, UP, buff=0.15)
        self.play(Write(fc_lbl), run_time=FAST)

        # Proof steps
        step1 = MathTex(
            r"m(b-a) \leq \int_a^b f \leq M(b-a)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=axes, buff=0.1)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)
        self.ly.clear()

        # Conclude
        title2 = self.ly.title("Proof (sketch)")

        s1 = MathTex(
            r"\text{EVT: } m \leq f(x) \leq M \text{ on } [a,b]",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(s1, direction=DOWN, anchor=title2, buff=0.4)
        self.play(Write(s1), run_time=NORMAL)
        self.wait(0.3)

        s2 = MathTex(
            r"\Rightarrow m \leq \frac{1}{b-a}\int_a^b f \leq M",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(s2, direction=DOWN, anchor=s1, buff=0.25)
        self.play(Write(s2), run_time=NORMAL)
        self.wait(0.3)

        s3 = MathTex(
            r"\text{IVT: } \exists\, c \in (a,b) : f(c) = \frac{1}{b-a}\int_a^b f",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(s3, direction=DOWN, anchor=s2, buff=0.25)
        self.play(Write(s3), run_time=NORMAL)
        # pacing: extends previous caption slot (seg#2 natural 40.6s, slot 22.1s -> 50.9s, Δ=28.8)
        self.wait(30.3)
        self.ly.clear()

    # --- Scene 5: FTC Part 1 — Statement ---
    def scene5_ftc1_statement(self):
        self.add_subcaption(
            "FTC Part 1. If f is continuous on a to b, and "
            "F of x is the integral from a to x of f of t "
            "dt, then F is differentiable on the open "
            "interval a to b, and F prime of x equals f of "
            "x. The integral function is an antiderivative "
            "of the integrand. Differentiating the "
            "accumulation function gives back the original "
            "function.",
            duration=23.9,
        )
        self.ly.section_divider("3", "FTC Part 1")
        self.ly.clear()

        title = self.ly.title("FTC Part 1")

        theorem = MathTex(
            r"F'(x) = f(x) \quad \text{where } F(x) = \int_a^x f(t)\, dt",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(theorem, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(theorem), run_time=SLOW)
        self.wait(0.5)

        insight = Text(
            "Differentiating the integral gives back the function!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=theorem, buff=0.3)
        self.play(Write(insight), run_time=NORMAL)
        # pacing: extends previous caption slot (seg#3 natural 24.0s, slot 10.5s -> 30.0s, Δ=19.5)
        self.wait(21.0)
        self.ly.clear()

    # --- Scene 6: FTC Part 1 — Proof ---
    def scene6_ftc1_proof(self):
        self.add_subcaption(
            "Proof. Fix x in the open interval a to b. "
            "Consider the difference quotient. F of x plus "
            "h minus F of x equals the integral from a to x "
            "plus h of f, minus the integral from a to x of "
            "f. By additivity of the integral, this equals "
            "the integral from x to x plus h of f of t dt. "
            "Now apply the MVT for integrals. Since f is "
            "continuous, there exists c sub h in the open "
            "interval x to x plus h such that this integral "
            "equals f of c sub h times h. Divide by h to get "
            "the difference quotient equals f of c sub h. As "
            "h approaches zero, c sub h is squeezed toward x. "
            "Since f is continuous, f of c sub h approaches "
            "f of x. Therefore F prime of x equals f of x.",
            duration=52.9,
        )

        title = self.ly.title("Proof of FTC Part 1")

        step1 = MathTex(
            r"\frac{F(x+h) - F(x)}{h} = \frac{1}{h}\int_x^{x+h} f(t)\, dt",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)

        # Visual: thin slice
        axes = Axes(
            x_range=[-0.3, 4.5, 1], y_range=[-0.3, 4.0, 1],
            x_length=4.0, y_length=1.8,
            axis_config={"include_numbers": False, "font_size": 14, "stroke_width": 1.0},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.remove(title, step1)
        self.play(Create(axes), run_time=NORMAL)

        def h_func(x):
            return 0.5 * x + 1.0 + 0.3 * np.sin(x)

        h_graph = axes.plot(h_func, x_range=[0.5, 4], color=PRIMARY)
        self.play(Create(h_graph), run_time=NORMAL)

        # Thin slice [x, x+h]
        x_start = 1.8
        x_end = 2.6
        n_pts = 15
        xs = np.linspace(x_start, x_end, n_pts)
        area_points = [axes.c2p(x_start, 0)]
        for xi in xs:
            area_points.append(axes.c2p(xi, h_func(xi)))
        area_points.append(axes.c2p(x_end, 0))
        thin_slice = Polygon(
            *area_points, fill_color=SECONDARY, fill_opacity=0.4, stroke_width=0,
        )
        self.play(FadeIn(thin_slice), run_time=NORMAL)

        # Labels
        x_mark = MathTex(r"x", font_size=SMALL_SIZE, color=ACCENT)
        x_mark.next_to(axes.c2p(x_start, 0), DOWN, buff=0.15)
        self.play(Write(x_mark), run_time=FAST)

        xh_mark = MathTex(r"x+h", font_size=SMALL_SIZE, color=ACCENT)
        xh_mark.next_to(axes.c2p(x_end, 0), DOWN, buff=0.15)
        self.play(Write(xh_mark), run_time=FAST)

        # Back to proof steps
        self.ly.clear()

        title2 = self.ly.title("Applying MVT for Integrals")

        step2 = MathTex(
            r"= f(c_h) \cdot \frac{h}{h} = f(c_h), \quad c_h \in (x, x+h)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=title2, buff=0.4)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.5)

        step3 = MathTex(
            r"h \to 0 \implies c_h \to x \implies f(c_h) \to f(x)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(step3, direction=DOWN, anchor=step2, buff=0.3)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(0.3)

        step4 = MathTex(
            r"\therefore F'(x) = f(x) \qquad \blacksquare",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(step4, direction=DOWN, anchor=step3, buff=0.3)
        self.play(Write(step4), run_time=SLOW)
        # pacing: extends previous caption slot (seg#4 natural 52.9s, slot 16.2s -> 66.2s, Δ=50.0)
        self.wait(51.5)
        self.ly.clear()

    # --- Scene 7: FTC Part 2 — Statement ---
    def scene7_ftc2_statement(self):
        self.add_subcaption(
            "FTC Part 2. If f is integrable on a to b and F "
            "is an antiderivative of f, meaning F prime "
            "equals f, then the integral from a to b of f "
            "of x dx equals F of b minus F of a. This is "
            "the computation theorem. Instead of computing "
            "Riemann sums, just find any antiderivative F "
            "and evaluate it at the endpoints. The proof "
            "connects Riemann sums to antiderivatives via "
            "the Mean Value Theorem.",
            duration=29.0,
        )
        self.ly.section_divider("4", "FTC Part 2")
        self.ly.clear()

        title = self.ly.title("FTC Part 2")

        theorem = MathTex(
            r"\int_a^b f(x)\, dx = F(b) - F(a)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(theorem, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(theorem), run_time=SLOW)
        self.wait(0.3)

        condition = MathTex(
            r"\text{where } F'(x) = f(x)",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(condition, direction=DOWN, anchor=theorem, buff=0.3)
        self.play(Write(condition), run_time=NORMAL)
        self.wait(0.5)

        insight = Text(
            "Evaluate integrals using antiderivatives!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=condition, buff=0.3)
        self.play(Write(insight), run_time=NORMAL)
        # pacing: extends previous caption slot (seg#5 natural 29.0s, slot 12.0s -> 36.4s, Δ=24.4)
        self.wait(25.9)
        self.ly.clear()

    # --- Scene 8: FTC Part 2 — Proof ---
    def scene8_ftc2_proof(self):
        self.add_subcaption(
            "Proof. Let P be a partition of a to b. By the "
            "Mean Value Theorem from Video 106, on each "
            "subinterval there exists c sub i such that F of "
            "x sub i minus F of x sub i minus 1 equals F "
            "prime of c sub i times delta x sub i, which "
            "equals f of c sub i times delta x sub i. Sum "
            "over all subintervals. The left side telescopes. "
            "All interior terms cancel, leaving F of b minus F "
            "of a. The right side is a Riemann sum for f. "
            "As the mesh goes to zero, the Riemann sum "
            "approaches the integral. Therefore the integral "
            "equals F of b minus F of a.",
            duration=39.5,
        )

        title = self.ly.title("Proof of FTC Part 2")

        step1 = MathTex(
            r"\text{MVT: } F(x_i) - F(x_{i-1}) = f(c_i)\, \Delta x_i",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)

        # Visual: F(x) curve with partition and tangent
        axes = Axes(
            x_range=[-0.3, 4.5, 1], y_range=[-0.3, 4.5, 1],
            x_length=4.5, y_length=2.0,
            axis_config={"include_numbers": False, "font_size": 14, "stroke_width": 1.0},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.remove(title, step1)
        self.play(Create(axes), run_time=NORMAL)

        def F_func(x):
            return 0.3 * x ** 2 + 0.5

        F_graph = axes.plot(F_func, x_range=[0.5, 4], color=ACCENT)
        self.play(Create(F_graph), run_time=NORMAL)

        # Partition points on x-axis
        partition_xs = [0.5, 1.5, 2.5, 3.5, 4.0]
        for px in partition_xs:
            p_dot = Dot(axes.c2p(px, 0), color=DIM, radius=0.04)
            self.play(FadeIn(p_dot), run_time=FAST)

        F_lbl = MathTex(r"F(x)", font_size=SMALL_SIZE, color=ACCENT)
        self.ly.safe_place(F_lbl, direction=UP, anchor=axes, buff=0.05)
        clamp_position(F_lbl)
        self.play(Write(F_lbl), run_time=FAST)

        self.ly.clear()

        title2 = self.ly.title("Summing Over All Subintervals")

        step2 = MathTex(
            r"\sum_{i=1}^{n} [F(x_i) - F(x_{i-1})]"
            r" = \sum_{i=1}^{n} f(c_i)\, \Delta x_i",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=title2, buff=0.4)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.5)

        self.ly.clear()

        title3 = self.ly.title("Telescoping")

        step3 = MathTex(
            r"\text{LHS: } F(x_n) - F(x_0) = F(b) - F(a)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step3, direction=DOWN, anchor=title3, buff=0.4)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(0.3)

        # Telescoping visual: show terms cancelling
        cancel = MathTex(
            r"+F(x_1) - F(x_1) + F(x_2) - F(x_2) + \cdots",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(cancel, direction=DOWN, anchor=step3, buff=0.25)
        self.play(Write(cancel), run_time=NORMAL)
        self.wait(0.5)

        step4 = MathTex(
            r"\text{RHS: Riemann sum for } f \to \int_a^b f \text{ as } \|P\| \to 0",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step4, direction=DOWN, anchor=cancel, buff=0.25)
        self.play(Write(step4), run_time=NORMAL)
        self.wait(0.5)

        result = MathTex(
            r"\therefore \int_a^b f(x)\, dx = F(b) - F(a) \qquad \blacksquare",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=step4, buff=0.3)
        self.play(Write(result), run_time=SLOW)
        # pacing: extends previous caption slot (seg#6 natural 39.5s, slot 22.3s -> 49.5s, Δ=27.2)
        self.wait(28.7)
        self.ly.clear()

    # --- Scene 9: Example ---
    def scene9_example(self):
        self.add_subcaption(
            "Example. Evaluate the integral from zero to two "
            "of x squared dx. Step one: find an "
            "antiderivative. F of x equals x cubed over "
            "three, since F prime of x equals x squared. "
            "Step two: apply FTC Part 2. The integral "
            "equals F of two minus F of zero, which equals "
            "eight thirds minus zero, which equals eight "
            "thirds. What took pages of Riemann sum "
            "computation, FTC solves in two lines. This is "
            "why the Fundamental Theorem is fundamental.",
            duration=33.5,
        )
        self.ly.section_divider("5", "Example")
        self.ly.clear()

        title = self.ly.title("Evaluating an Integral")

        problem = MathTex(
            r"\int_0^2 x^2\, dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        # Visual: graph of x^2
        axes = Axes(
            x_range=[-0.3, 2.8, 1], y_range=[-0.3, 5, 1],
            x_length=4.0, y_length=2.5,
            axis_config={"include_numbers": False, "font_size": 14, "stroke_width": 1.0},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.remove(title, problem)
        self.play(Create(axes), run_time=NORMAL)

        sq_graph = axes.plot(lambda x: x ** 2, x_range=[0, 2.3], color=PRIMARY)
        self.play(Create(sq_graph), run_time=NORMAL)

        # Shaded area under x^2 from 0 to 2
        xs = np.linspace(0, 2, 20)
        area_points = [axes.c2p(0, 0)]
        for xi in xs:
            area_points.append(axes.c2p(xi, xi ** 2))
        area_points.append(axes.c2p(2, 0))
        shaded = Polygon(
            *area_points, fill_color=SECONDARY, fill_opacity=0.3, stroke_width=0,
        )
        self.play(FadeIn(shaded), run_time=NORMAL)

        self.ly.clear()

        title2 = self.ly.title("Solution")

        s1 = MathTex(
            r"\text{Step 1: } F(x) = \frac{x^3}{3}, \quad F'(x) = x^2",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(s1, direction=DOWN, anchor=title2, buff=0.4)
        self.play(Write(s1), run_time=NORMAL)
        self.wait(0.3)

        s2 = MathTex(
            r"\text{Step 2: } \int_0^2 x^2\, dx = F(2) - F(0)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(s2, direction=DOWN, anchor=s1, buff=0.25)
        self.play(Write(s2), run_time=NORMAL)
        self.wait(0.3)

        s3 = MathTex(
            r"= \frac{8}{3} - 0 = \frac{8}{3}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(s3, direction=DOWN, anchor=s2, buff=0.25)
        self.play(Write(s3), run_time=NORMAL)
        self.wait(0.5)

        punchline = Text(
            "Riemann sums in one step -- this is why it's FUNDAMENTAL!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(punchline, direction=DOWN, anchor=s3, buff=0.3)
        self.play(Write(punchline), run_time=NORMAL)
        # pacing: extends previous caption slot (seg#7 natural 33.5s, slot 19.5s -> 42.0s, Δ=22.5)
        self.wait(24.0)
        self.ly.clear()

    # --- Scene 10: Summary + Outro ---
    def scene10_summary(self):
        self.add_subcaption(
            "Key takeaways. "
            "FTC Part 1: the integral function F of x is an "
            "antiderivative of f. Differentiating the "
            "accumulation gives back the function. "
            "FTC Part 2: the integral equals F of b minus F "
            "of a for any antiderivative F. Evaluate "
            "integrals using antiderivatives. "
            "The MVT for integrals is the key lemma in both "
            "proofs. "
            "The Riemann integral and the derivative are "
            "genuinely inverse operations. "
            "FTC closes the loop of calculus. "
            "Next time: pointwise and uniform convergence.",
            duration=35.5,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "1. FTC Part 1: d/dx [integral of f] = f(x)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "2. FTC Part 2: integral of f = F(b) - F(a)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "3. MVT for integrals is the key lemma",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "4. Derivatives and integrals are inverses",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "5. FTC closes the loop of calculus!",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        # pacing: extends final caption slot (seg#8 natural 35.5s, slot 15.7s -> 44.4s, Δ=28.7)
        self.wait(29.7)

        play_outro(self, "Pointwise vs Uniform Convergence", "Real Analysis I")
