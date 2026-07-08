"""
Video 107: The Riemann Integral
TEMPLATE v2 -- Professional quality Manim script

Playlist: Real Analysis I (Video 9 of 12)
Class: Video107_RiemannIntegral

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


class Video107_RiemannIntegral(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_partitions()
        self.scene3_riemann_sums()
        self.scene4_darboux_sums()
        self.scene5_integrability()
        self.scene6_continuous_integrable()
        self.scene7_dirichlet()
        self.scene8_properties()
        self.scene9_recap()
        self.scene10_summary()

    # --- Scene 1: Hook -- The Area Problem ---
    def scene1_hook(self):
        self.add_subcaption(
            "What is the area under a curve? "
            "In calculus you learned that the integral "
            "computes it. But what IS area? "
            "Today we make this rigorous using partitions, "
            "Riemann sums, and the Darboux criterion. "
            "We will see exactly what it means for a "
            "function to be Riemann integrable, prove that "
            "continuous functions are integrable, and "
            "encounter a function so wild it is NOT "
            "integrable.",
            duration=22,
        )
        play_intro(self, "The Riemann Integral", "Real Analysis I")

        title = self.ly.title("The Area Problem")

        axes = Axes(
            x_range=[-0.3, 4.5, 1], y_range=[-0.3, 4.5, 1],
            x_length=6.0, y_length=3.0,
            axis_config={"include_numbers": False, "font_size": 16, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        graph = axes.plot(lambda x: 0.6 * x + 0.8 + 0.3 * np.sin(x), x_range=[0.5, 4], color=SECONDARY)
        self.play(Create(graph), run_time=NORMAL)

        # Riemann rectangles (4, then refine)
        n_rects_list = [4, 8, 16]
        for n_rects in n_rects_list:
            dx = 3.5 / n_rects
            rects = VGroup()
            for i in range(n_rects):
                x_left = 0.5 + i * dx
                x_right = x_left + dx
                x_mid = (x_left + x_right) / 2
                h = 0.6 * x_mid + 0.8 + 0.3 * np.sin(x_mid)
                rect = Rectangle(
                    width=axes.c2p(dx, 0)[0] - axes.c2p(0, 0)[0],
                    height=axes.c2p(0, h)[1] - axes.c2p(0, 0)[1],
                ).move_to(axes.c2p(x_mid, h / 2))
                rect.set_stroke(color=ACCENT, width=1.5)
                rect.set_fill(color=ACCENT, opacity=0.3)
                rects.add(rect)
            self.play(Transform(graph, graph), run_time=FAST)
            self.play(FadeIn(rects), run_time=NORMAL)
            self.wait(0.3)
            if n_rects < 16:
                self.play(FadeOut(rects), run_time=FAST)

        caption = Text(
            "Rectangles converge to the true area!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(caption, direction=DOWN, anchor=axes, buff=0.1)
        self.play(Write(caption), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 2: Partitions and Norm ---
    def scene2_partitions(self):
        self.add_subcaption(
            "A partition divides the interval a b into "
            "subintervals. "
            "A partition P is a set of points x zero, x one, "
            "up to x n, starting at a and ending at b, "
            "strictly increasing. "
            "The mesh or norm of a partition is the width "
            "of the largest subinterval. "
            "As the mesh goes to zero, every subinterval "
            "becomes arbitrarily small.",
            duration=22,
        )
        self.ly.section_divider("1", "Partitions")
        self.ly.clear()

        title = self.ly.title("Partitions of [a, b]")

        # Number line
        nl = NumberLine(
            x_range=[0, 6, 1], length=8.0, include_numbers=False,
            font_size=SMALL_SIZE,
        )
        self.ly.center_in_content(nl)
        clamp_position(nl)
        self.play(Create(nl), run_time=NORMAL)

        # Labels a and b
        a_lbl = MathTex(r"a = x_0", font_size=SMALL_SIZE, color=PRIMARY)
        a_lbl.next_to(nl.n2p(0), DOWN, buff=0.2)
        b_lbl = MathTex(r"x_n = b", font_size=SMALL_SIZE, color=PRIMARY)
        b_lbl.next_to(nl.n2p(6), DOWN, buff=0.2)
        self.play(Write(a_lbl), Write(b_lbl), run_time=FAST)

        # Interior partition points
        pts = [1.5, 3.0, 4.5]
        for p in pts:
            dot = Dot(nl.n2p(p), color=ACCENT, radius=0.06)
            self.play(FadeIn(dot), run_time=FAST)

        # Mesh label
        mesh_def = MathTex(
            r"\|P\| = \max_i (x_i - x_{i-1})",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(mesh_def, direction=DOWN, anchor=nl, buff=0.5)
        self.play(Write(mesh_def), run_time=NORMAL)
        self.wait(1)

        # Formal partition definition
        part_def = MathTex(
            r"P = \{x_0, x_1, x_2, \ldots, x_n\}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(part_def, direction=DOWN, anchor=mesh_def, buff=0.3)
        self.play(Write(part_def), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # Refinement animation
        title2 = self.ly.title("Refining the Partition")

        nl2 = NumberLine(x_range=[0, 6, 1], length=8.0, include_numbers=False)
        self.ly.center_in_content(nl2)
        clamp_position(nl2)
        self.play(Create(nl2), run_time=NORMAL)

        for n_pts in [3, 6, 12]:
            xs = np.linspace(0.5, 5.5, n_pts)
            dots = VGroup(*[Dot(nl2.n2p(x), color=ACCENT, radius=0.05) for x in xs])
            n_label = Text(f"n = {n_pts}", font_size=SMALL_SIZE, color=ACCENT, font=SANS)
            self.ly.safe_place(n_label, direction=DOWN, anchor=nl2, buff=0.3)
            self.play(FadeIn(dots), Write(n_label), run_time=FAST)
            self.wait(0.3)
            if n_pts < 12:
                self.play(FadeOut(dots), FadeOut(n_label), run_time=FAST)

        mesh_note = Text(
            "Mesh -> 0  =>  every subinterval shrinks",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(mesh_note, direction=DOWN, anchor=nl2, buff=0.6)
        self.play(Write(mesh_note), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 3: Riemann Sums ---
    def scene3_riemann_sums(self):
        self.add_subcaption(
            "Given a partition and a choice of sample point "
            "t i in each subinterval, the Riemann sum is the "
            "sum of f of t i times delta x i. "
            "Each rectangle has width delta x i and height "
            "f of t i. "
            "The Riemann sum approximates the signed area "
            "under the curve. "
            "We say f is Riemann integrable if these sums "
            "converge to a unique limit as the mesh goes "
            "to zero, regardless of the sample points.",
            duration=28,
        )
        self.ly.section_divider("2", "Riemann Sums")
        self.ly.clear()

        title = self.ly.title("Riemann Sums")

        formula = MathTex(
            r"R(f, P, \{t_i\}) = \sum_{i=1}^{n} f(t_i)\, \Delta x_i",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(formula), run_time=SLOW)
        self.wait(0.5)

        note = MathTex(
            r"\Delta x_i = x_i - x_{i-1}, \quad t_i \in [x_{i-1}, x_i]",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=formula, buff=0.3)
        self.play(Write(note), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # Graphical Riemann sum
        title2 = self.ly.title("Visualizing the Sum")

        axes = Axes(
            x_range=[-0.3, 4.5, 1], y_range=[-0.3, 4.5, 1],
            x_length=6.0, y_length=2.8,
            axis_config={"include_numbers": False, "font_size": 16, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        graph = axes.plot(lambda x: 0.5 * x + 1.0, x_range=[0.5, 4], color=SECONDARY)
        self.play(Create(graph), run_time=NORMAL)

        # Midpoint rectangles
        n_rects = 5
        dx = 3.5 / n_rects
        rects = VGroup()
        for i in range(n_rects):
            x_left = 0.5 + i * dx
            x_mid = x_left + dx / 2
            h = 0.5 * x_mid + 1.0
            rect = Rectangle(
                width=axes.c2p(dx, 0)[0] - axes.c2p(0, 0)[0],
                height=axes.c2p(0, h)[1] - axes.c2p(0, 0)[1],
            ).move_to(axes.c2p(x_mid, h / 2))
            rect.set_stroke(color=ACCENT, width=1.5)
            rect.set_fill(color=ACCENT, opacity=0.35)
            rects.add(rect)
        self.play(FadeIn(rects), run_time=NORMAL)

        label = MathTex(
            r"\sum f(t_i) \Delta x_i",
            font_size=SMALL_SIZE, color=ACCENT,
        )
        self.ly.safe_place(label, direction=DOWN, anchor=axes, buff=0.1)
        self.play(Write(label), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 4: Upper and Lower Darboux Sums ---
    def scene4_darboux_sums(self):
        self.add_subcaption(
            "Darboux refined Riemann's idea using the "
            "supremum and infimum on each subinterval. "
            "The upper sum uses M i, the supremum of f "
            "on the subinterval. "
            "The lower sum uses m i, the infimum. "
            "The upper sum overestimates the area. "
            "The lower sum underestimates it. "
            "The true area is trapped between them. "
            "This squeeze is the key to the Darboux "
            "criterion for integrability.",
            duration=28,
        )
        self.ly.section_divider("3", "Darboux Sums")
        self.ly.clear()

        title = self.ly.title("Upper and Lower Sums")

        upper_f = MathTex(
            r"U(f, P) = \sum_{i=1}^{n} M_i \, \Delta x_i",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(upper_f, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(upper_f), run_time=NORMAL)
        self.wait(0.3)

        lower_f = MathTex(
            r"L(f, P) = \sum_{i=1}^{n} m_i \, \Delta x_i",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(lower_f, direction=DOWN, anchor=upper_f, buff=0.3)
        self.play(Write(lower_f), run_time=NORMAL)
        self.wait(0.3)

        defs = MathTex(
            r"M_i = \sup\{f(x) : x \in [x_{i-1}, x_i]\}, \quad "
            r"m_i = \inf\{f(x) : x \in [x_{i-1}, x_i]\}",
            font_size=SMALL_SIZE, color=DIM,
        )
        self.ly.safe_place(defs, direction=DOWN, anchor=lower_f, buff=0.3)
        self.play(Write(defs), run_time=NORMAL)
        self.wait(0.5)

        inequality = MathTex(
            r"L(f, P) \leq \text{Area} \leq U(f, P)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(inequality, direction=DOWN, anchor=defs, buff=0.3)
        self.play(Write(inequality), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Visual: upper and lower rectangles
        title2 = self.ly.title("Squeezing the Area")

        axes = Axes(
            x_range=[-0.3, 4.5, 1], y_range=[-0.3, 5, 1],
            x_length=5.5, y_length=2.5,
            axis_config={"include_numbers": False, "font_size": 16, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        # Non-monotonic curve for interesting sup/inf
        graph = axes.plot(
            lambda x: 2.5 + 1.2 * np.sin(1.5 * (x - 0.5)) + 0.2 * x,
            x_range=[0.5, 4], color=SECONDARY,
        )
        self.play(Create(graph), run_time=NORMAL)

        # Upper rectangles
        n_rects = 6
        dx = 3.5 / n_rects
        upper_rects = VGroup()
        lower_rects = VGroup()
        for i in range(n_rects):
            x_left = 0.5 + i * dx
            x_right = x_left + dx
            xs = np.linspace(x_left, x_right, 20)
            ys = 2.5 + 1.2 * np.sin(1.5 * (xs - 0.5)) + 0.2 * xs
            h_max = max(ys)
            h_min = min(ys)
            ur = Rectangle(
                width=axes.c2p(dx, 0)[0] - axes.c2p(0, 0)[0],
                height=axes.c2p(0, h_max)[1] - axes.c2p(0, 0)[1],
            ).move_to(axes.c2p((x_left + x_right) / 2, h_max / 2))
            ur.set_stroke(color=RED, width=1.5)
            ur.set_fill(color=RED, opacity=0.2)
            upper_rects.add(ur)

            lr = Rectangle(
                width=axes.c2p(dx, 0)[0] - axes.c2p(0, 0)[0],
                height=axes.c2p(0, h_min)[1] - axes.c2p(0, 0)[1],
            ).move_to(axes.c2p((x_left + x_right) / 2, h_min / 2))
            lr.set_stroke(color=PRIMARY, width=1.5)
            lr.set_fill(color=PRIMARY, opacity=0.2)
            lower_rects.add(lr)

        self.play(FadeIn(upper_rects), run_time=NORMAL)
        u_lbl = Text("U(f,P): overestimate", font_size=SMALL_SIZE, color=RED, font=SANS)
        self.ly.safe_place(u_lbl, direction=DOWN, anchor=axes, buff=0.1)
        self.play(Write(u_lbl), run_time=FAST)
        self.wait(0.5)

        self.play(FadeIn(lower_rects), run_time=NORMAL)
        l_lbl = Text("L(f,P): underestimate", font_size=SMALL_SIZE, color=PRIMARY, font=SANS)
        self.ly.safe_place(l_lbl, direction=DOWN, anchor=u_lbl, buff=0.05)
        self.play(Write(l_lbl), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 5: The Integrability Condition ---
    def scene5_integrability(self):
        self.add_subcaption(
            "When is a function Riemann integrable? "
            "Define the upper integral as the infimum of "
            "all upper sums. "
            "Define the lower integral as the supremum of "
            "all lower sums. "
            "The function is integrable if and only if these "
            "two numbers are equal. "
            "Their common value is the Riemann integral. "
            "Equivalently, by the Darboux criterion, f is "
            "integrable if for every epsilon greater than "
            "zero, there exists a partition P with the "
            "difference of upper and lower sums less than "
            "epsilon.",
            duration=35,
        )
        self.ly.section_divider("4", "The Integrability Condition")
        self.ly.clear()

        title = self.ly.title("When is f Riemann Integrable?")

        upper_int = MathTex(
            r"\overline{\int_a^b} f = \inf_P U(f, P)",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(upper_int, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(upper_int), run_time=NORMAL)
        self.wait(0.3)

        lower_int = MathTex(
            r"\underline{\int_a^b} f = \sup_P L(f, P)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(lower_int, direction=DOWN, anchor=upper_int, buff=0.3)
        self.play(Write(lower_int), run_time=NORMAL)
        self.wait(0.5)

        criterion = MathTex(
            r"f \text{ integrable} \iff \overline{\int_a^b} f = \underline{\int_a^b} f",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(criterion, direction=DOWN, anchor=lower_int, buff=0.3)
        self.play(Write(criterion), run_time=NORMAL)
        self.wait(0.5)

        self.ly.clear()
        title2 = self.ly.title("Darboux Criterion")

        dc = MathTex(
            r"\forall \varepsilon > 0,\ \exists\, P :",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(dc, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(dc), run_time=NORMAL)
        self.wait(0.3)

        dc2 = MathTex(
            r"U(f, P) - L(f, P) < \varepsilon",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(dc2, direction=DOWN, anchor=dc, buff=0.3)
        self.play(Write(dc2), run_time=SLOW)
        self.wait(0.5)

        insight = Text(
            "Overestimate and underestimate can be made arbitrarily close!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=dc2, buff=0.3)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 6: Continuous => Integrable ---
    def scene6_continuous_integrable(self):
        self.add_subcaption(
            "The main theorem: if f is continuous on the "
            "closed interval a b, then f is Riemann integrable. "
            "Proof idea. "
            "Since f is continuous on a compact set, it is "
            "uniformly continuous. "
            "For any epsilon, choose delta so that when x "
            "and y are within delta, f of x and f of y are "
            "within epsilon over b minus a. "
            "Take a partition with mesh less than delta. "
            "Then on each subinterval, the oscillation M i "
            "minus m i is less than epsilon over b minus a. "
            "The total difference U minus L is less than "
            "epsilon. "
            "This is exactly WHY we needed uniform continuity "
            "from Video 104.",
            duration=42,
        )
        self.ly.section_divider("5", "Continuous Implies Integrable")
        self.ly.clear()

        title = self.ly.title("Theorem: Continuous => Integrable")

        statement = MathTex(
            r"f \in C[a,b] \implies f \in \mathcal{R}[a,b]",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(statement, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(statement), run_time=NORMAL)
        self.wait(0.5)

        step1 = MathTex(
            r"\text{Step 1: } f \text{ unif. continuous} \implies \exists\, \delta",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=statement, buff=0.3)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.3)

        step2 = MathTex(
            r"|x - y| < \delta \implies |f(x) - f(y)| < \frac{\varepsilon}{b-a}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.25)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.3)

        step3 = MathTex(
            r"\text{Step 2: } \|P\| < \delta \implies M_i - m_i < \frac{\varepsilon}{b-a}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(step3, direction=DOWN, anchor=step2, buff=0.25)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(0.3)

        step4 = MathTex(
            r"U(f,P) - L(f,P) = \sum (M_i - m_i)\Delta x_i < \varepsilon",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(step4, direction=DOWN, anchor=step3, buff=0.25)
        self.play(Write(step4), run_time=NORMAL)
        self.wait(0.5)

        connection = Text(
            "This is WHY we needed uniform continuity (Video 104)!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(connection, direction=DOWN, anchor=step4, buff=0.3)
        self.play(Write(connection), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 7: The Dirichlet Function ---
    def scene7_dirichlet(self):
        self.add_subcaption(
            "What fails? The Dirichlet function: f of x "
            "equals one if x is rational, and zero if x "
            "is irrational. "
            "On every subinterval, rationals and irrationals "
            "are both dense. "
            "So the supremum M i equals one and the infimum "
            "m i equals zero on every subinterval. "
            "The upper sum equals b minus a. "
            "The lower sum equals zero. "
            "They can never be close. "
            "The Dirichlet function is NOT Riemann integrable.",
            duration=28,
        )
        self.ly.section_divider("6", "A Non-Integrable Function")
        self.ly.clear()

        title = self.ly.title("The Dirichlet Function")

        defn = MathTex(
            r"f(x) = \begin{cases} 1 & x \in \mathbb{Q} \\ 0 & x \notin \mathbb{Q} \end{cases}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(defn, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(defn), run_time=SLOW)
        self.wait(0.5)

        chaos = Text(
            "1 on rationals, 0 on irrationals — both dense!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(chaos, direction=DOWN, anchor=defn, buff=0.3)
        self.play(Write(chaos), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        title2 = self.ly.title("Why It Fails")

        s1 = MathTex(
            r"M_i = 1, \quad m_i = 0 \quad \text{on every subinterval}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(s1, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(s1), run_time=NORMAL)
        self.wait(0.3)

        s2 = MathTex(
            r"U(f, P) = \sum 1 \cdot \Delta x_i = b - a",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(s2, direction=DOWN, anchor=s1, buff=0.25)
        self.play(Write(s2), run_time=NORMAL)
        self.wait(0.3)

        s3 = MathTex(
            r"L(f, P) = \sum 0 \cdot \Delta x_i = 0",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(s3, direction=DOWN, anchor=s2, buff=0.25)
        self.play(Write(s3), run_time=NORMAL)
        self.wait(0.3)

        s4 = MathTex(
            r"\overline{\int} f = b-a \neq 0 = \underline{\int} f",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(s4, direction=DOWN, anchor=s3, buff=0.25)
        self.play(Write(s4), run_time=NORMAL)
        self.wait(0.3)

        concl = Text(
            "NOT Riemann integrable!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(concl, direction=DOWN, anchor=s4, buff=0.25)
        self.play(Write(concl), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 8: Properties ---
    def scene8_properties(self):
        self.add_subcaption(
            "The Riemann integral satisfies key properties. "
            "Linearity: the integral of f plus g is the "
            "integral of f plus the integral of g. "
            "Monotonicity: if f is at most g, the integral "
            "of f is at most the integral of g. "
            "Additivity over intervals: the integral from "
            "a to c plus c to b equals the integral from "
            "a to b. "
            "And the absolute value of the integral is at "
            "most the integral of the absolute value.",
            duration=28,
        )
        self.ly.section_divider("7", "Properties")
        self.ly.clear()

        title = self.ly.title("Properties of the Integral")

        items = [
            MathTex(
                r"\int_a^b (f + g) = \int_a^b f + \int_a^b g",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"\int_a^b c \cdot f = c \int_a^b f",
                font_size=BODY_SIZE, color=SECONDARY,
            ),
            MathTex(
                r"f \leq g \implies \int_a^b f \leq \int_a^b g",
                font_size=BODY_SIZE, color=ACCENT,
            ),
            MathTex(
                r"\int_a^c f + \int_c^b f = \int_a^b f",
                font_size=BODY_SIZE, color=WHITE,
            ),
            MathTex(
                r"\left|\int_a^b f\right| \leq \int_a^b |f|",
                font_size=BODY_SIZE, color=RED,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 9: Geometric Recap ---
    def scene9_recap(self):
        self.add_subcaption(
            "Let's see the whole idea come together. "
            "We partition the interval. "
            "We form upper and lower sums. "
            "As the partition gets finer, the upper and "
            "lower sums squeeze toward each other. "
            "If they converge to the same value, the "
            "function is integrable, and that value is "
            "the integral.",
            duration=20,
        )
        title = self.ly.title("The Squeeze")

        axes = Axes(
            x_range=[-0.3, 4.5, 1], y_range=[-0.3, 4.5, 1],
            x_length=5.5, y_length=2.8,
            axis_config={"include_numbers": False, "font_size": 16, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        graph = axes.plot(lambda x: 0.8 * x + 0.5 + 0.5 * np.sin(x), x_range=[0.5, 4], color=SECONDARY)
        self.play(Create(graph), run_time=NORMAL)

        for n_rects in [4, 8]:
            dx = 3.5 / n_rects
            upper_rects = VGroup()
            lower_rects = VGroup()
            for i in range(n_rects):
                x_left = 0.5 + i * dx
                x_right = x_left + dx
                xs = np.linspace(x_left, x_right, 15)
                ys = 0.8 * xs + 0.5 + 0.5 * np.sin(xs)
                h_max = max(ys)
                h_min = min(ys)
                ur = Rectangle(
                    width=axes.c2p(dx, 0)[0] - axes.c2p(0, 0)[0],
                    height=axes.c2p(0, h_max)[1] - axes.c2p(0, 0)[1],
                ).move_to(axes.c2p((x_left + x_right) / 2, h_max / 2))
                ur.set_stroke(color=RED, width=1)
                ur.set_fill(color=RED, opacity=0.15)
                upper_rects.add(ur)
                lr = Rectangle(
                    width=axes.c2p(dx, 0)[0] - axes.c2p(0, 0)[0],
                    height=axes.c2p(0, h_min)[1] - axes.c2p(0, 0)[1],
                ).move_to(axes.c2p((x_left + x_right) / 2, h_min / 2))
                lr.set_stroke(color=PRIMARY, width=1)
                lr.set_fill(color=PRIMARY, opacity=0.15)
                lower_rects.add(lr)
            self.play(FadeIn(upper_rects), FadeIn(lower_rects), run_time=NORMAL)
            self.wait(0.5)
            self.play(FadeOut(upper_rects), FadeOut(lower_rects), run_time=FAST)

        conclusion = Text(
            "U and L converge => f is integrable!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(conclusion, direction=DOWN, anchor=axes, buff=0.1)
        self.play(Write(conclusion), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 10: Summary + Outro ---
    def scene10_summary(self):
        self.add_subcaption(
            "Key takeaways. "
            "One: partitions divide the interval, and the "
            "mesh is the largest subinterval width. "
            "Two: the Riemann sum approximates area using "
            "sampled rectangles. "
            "Three: upper and lower Darboux sums squeeze "
            "the true area. "
            "Four: f is integrable when the upper and lower "
            "integrals agree. "
            "Five: continuous functions are integrable, "
            "thanks to uniform continuity. "
            "Six: the Dirichlet function is not integrable. "
            "Next time: the Fundamental Theorem of Calculus, "
            "connecting derivatives and integrals.",
            duration=35,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("1. Partitions: divide [a,b], mesh = max width",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Riemann sum: Σ f(tᵢ)Δxᵢ approximates area",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Darboux: upper (sup) and lower (inf) sums",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Integrable iff upper integral = lower integral",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5. Continuous => uniformly continuous => integrable",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("6. Dirichlet function: NOT integrable",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        play_outro(self, "Fundamental Theorem of Calculus", "Real Analysis I")
