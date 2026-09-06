"""
Video 102: Limits of Functions (Epsilon-Delta)
TEMPLATE v2 -- Professional quality Manim script

Playlist: Real Analysis I (Video 4 of 12)
Class: Video102_LimitsOfFunctions

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


class Video102_LimitsOfFunctions(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_intuition()
        self.scene4_divider_definition()
        self.scene5_formal_definition()
        self.scene6_divider_proof()
        self.scene7_proof_example()
        self.scene8_divider_sequential()
        self.scene9_sequential_characterization()
        self.scene10_summary_outro()

    # --- Scene 1: Hook -- Three Functions, One Question ---
    def scene1_hook(self):
        self.add_subcaption(
            "In calculus, you learned that the limit of f of x "
            "as x approaches a tells you what f does near a. "
            "But what does approaching actually mean? "
            "Can we make this idea mathematically precise? "
            "And what happens when the function misbehaves? "
            "Today we define the limit of a function rigorously.",
            duration=20.0,  # pacing: declared ~= 1.15x natural TTS (17.35s)
        )
        play_intro(self, "Limits of Functions", "Real Analysis I")

        title = self.ly.title("Three Functions, One Question")

        # Three mini function graphs
        # f(x) = x^2
        g1 = Axes(
            x_range=[-3, 3, 1], y_range=[-1, 9, 1],
            x_length=3.2, y_length=2.8,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        )
        g1.move_to(LEFT * 4.5 + DOWN * 0.5)
        p1 = g1.plot(lambda x: x**2, x_range=[-2.5, 2.5], color=PRIMARY)
        l1 = MathTex("x^2", font_size=LABEL_SIZE, color=PRIMARY)
        l1.next_to(g1, UP, buff=0.15)

        # f(x) = (x^2 - 4)/(x - 2)  (removable discontinuity)
        g2 = Axes(
            x_range=[-1, 5, 1], y_range=[-1, 9, 1],
            x_length=3.2, y_length=2.8,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        )
        g2.move_to(ORIGIN + DOWN * 0.5)
        p2 = g2.plot(lambda x: x + 2 if abs(x - 2) > 0.01 else 0, x_range=[-0.5, 4.5], color=SECONDARY)
        l2 = MathTex(r"\frac{x^2-4}{x-2}", font_size=LABEL_SIZE, color=SECONDARY)
        l2.next_to(g2, UP, buff=0.15)

        # f(x) = sin(pi/x)
        g3 = Axes(
            x_range=[-0.5, 0.5, 0.1], y_range=[-1.5, 1.5, 0.5],
            x_length=3.2, y_length=2.8,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        )
        g3.move_to(RIGHT * 4.5 + DOWN * 0.5)
        p3 = g3.plot(lambda x: np.sin(np.pi / x) if abs(x) > 0.01 else 0, x_range=[-0.4, 0.4], color=RED)
        l3 = MathTex(r"\sin(\pi/x)", font_size=LABEL_SIZE, color=RED)
        l3.next_to(g3, UP, buff=0.15)

        # Show them one by one
        vis1 = VGroup(g1, p1, l1)
        vis2 = VGroup(g2, p2, l2)
        vis3 = VGroup(g3, p3, l3)

        self.play(
            FadeIn(vis1, scale=0.8),
            FadeIn(vis2, scale=0.8),
            FadeIn(vis3, scale=0.8),
            run_time=NORMAL, lag_ratio=0.2,
        )
        self.wait(0.5)

        # Question
        question = Text(
            "What does f(x) APPROACH as x nears the point?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(question)
        question.shift(DOWN * 2.8)
        clamp_position(question)
        self.play(FadeIn(question, shift=UP * 0.1), run_time=NORMAL)
        self.wait(11.9)  # pacing: extends caption slot (Δ=+9.9)

        self.ly.clear()

    # --- Scene 2: Intro + Section Divider ---
    def scene2_intro(self):
        self.add_subcaption(
            "We will build the intuition first, "
            "then state the formal epsilon-delta definition, "
            "work through a proof, "
            "and connect function limits back to sequences.",
            duration=11.1,  # pacing: declared ~= 1.15x natural TTS (9.62s)
        )
        self.ly.section_divider(1, "The Intuition", hold=9.9)  # pacing: hold=0.8+9.1 extends caption slot
        self.ly.clear()

    # --- Scene 3: What Does f(x) Approach? -- Intuition ---
    def scene3_intuition(self):
        self.add_subcaption(
            "In calculus, we said the limit of f of x as x approaches a is L "
            "if f of x gets arbitrarily close to L "
            "as x gets close to a. "
            "But this is vague. How close is close enough? "
            "Consider f of x equals x squared minus four divided by x minus two. "
            "At x equals two, this function is undefined. Zero over zero. "
            "But for every other x near two, f of x equals x plus two, "
            "which approaches four. "
            "The limit does not depend on the value of f at a. "
            "It only depends on values near a. "
            "This is what makes limits powerful. "
            "We can talk about behavior near a point "
            "without ever evaluating at that point.",
            duration=47.3,  # pacing: declared ~= 1.15x natural TTS (41.11s)
        )

        title = self.ly.title("What Does f(x) Approach?")

        # Graph of f(x) = (x^2 - 4)/(x - 2) = x + 2, x != 2
        axes = Axes(
            x_range=[-1, 5, 1], y_range=[-1, 9, 1],
            x_length=8, y_length=4,
            axis_config={"include_numbers": True, "font_size": 20, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        axes.shift(UP * 0.3)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        # The function (line y = x + 2, with gap at x = 2)
        graph = axes.plot(lambda x: x + 2, x_range=[-0.5, 1.95], color=SECONDARY)
        graph2 = axes.plot(lambda x: x + 2, x_range=[2.05, 4.5], color=SECONDARY)
        self.play(Create(graph), Create(graph2), run_time=NORMAL)

        # Open circle at (2, 4)
        open_dot = Circle(radius=0.1, stroke_color=RED, fill_opacity=0, stroke_width=2.5)
        open_dot.move_to(axes.c2p(2, 4))
        self.play(FadeIn(open_dot), run_time=FAST)

        # Point approaching from left
        moving_dot = Dot(axes.c2p(1.0, 3.0), color=PRIMARY, radius=0.06)
        moving_label = MathTex("x", font_size=LABEL_SIZE, color=PRIMARY)
        moving_label.next_to(moving_dot, DOWN, buff=0.2)
        self.play(FadeIn(moving_dot), Write(moving_label), run_time=FAST)

        # Animate moving dot approaching x=2
        for xv in [1.3, 1.5, 1.7, 1.85, 1.95]:
            new_pos = axes.c2p(xv, xv + 2)
            self.play(
                moving_dot.animate.move_to(new_pos),
                moving_label.animate.move_to(axes.c2p(xv, 0) + DOWN * 0.2),
                run_time=0.5,
            )

        self.wait(0.3)

        # L label on y-axis
        l_dot = Dot(axes.c2p(0, 4), color=ACCENT, radius=0.07)
        l_label = MathTex("L = 4", font_size=BODY_SIZE, color=ACCENT)
        l_label.next_to(l_dot, LEFT, buff=0.15)
        self.play(FadeIn(l_dot), Write(l_label), run_time=NORMAL)
        self.wait(0.5)

        # Key insight
        insight = Text(
            "The limit does NOT depend on f(a) itself!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=axes, buff=0.3)
        self.play(FadeIn(insight, shift=UP * 0.1), run_time=NORMAL)
        self.wait(41.3)  # pacing: extends caption slot (Δ=+39.3)

        self.ly.clear()

    # --- Scene 4: Section Divider -- Formal Definition ---
    def scene4_divider_definition(self):
        self.add_subcaption(
            "Let us translate this intuition "
            "into the precise language of real analysis.",
            duration=6.8,  # pacing: declared ~= 1.15x natural TTS (5.86s)
        )
        self.ly.section_divider(2, "The Epsilon-Delta Definition", hold=5.2)  # pacing: hold=0.8+4.4 extends caption slot
        self.ly.clear()

    # --- Scene 5: The Formal Definition ---
    def scene5_formal_definition(self):
        self.add_subcaption(
            "We define the limit of f of x as x approaches a equals L "
            "if for every epsilon greater than zero, "
            "there exists a delta greater than zero, "
            "such that whenever zero is less than the absolute value of x minus a, "
            "which is less than delta, "
            "then the absolute value of f of x minus L is less than epsilon. "
            "Epsilon is how close we demand f of x to be to L. "
            "Delta is how close x must be to a to guarantee that. "
            "The condition zero less than x minus a means x is not equal to a. "
            "The limit ignores the point itself. "
            "The key is the quantifier order. "
            "For every epsilon, there exists delta. "
            "Epsilon comes first. You challenge me with any tolerance, "
            "and I must find a delta that works.",
            duration=54.2,  # pacing: declared ~= 1.15x natural TTS (47.09s)
        )

        title = self.ly.title("The Epsilon-Delta Definition")

        # The definition in a formula box
        defn = MathTex(
            r"\lim_{x \to a} f(x) = L",
            font_size=HEADING_SIZE, color=WHITE,
        )

        cond = MathTex(
            r"\iff \forall \varepsilon > 0,\; \exists \delta > 0:",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        implies = MathTex(
            r"0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon",
            font_size=BODY_SIZE, color=SECONDARY,
        )

        defn_group = VGroup(defn, cond, implies).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        box = SurroundingRectangle(defn_group, color=ACCENT, buff=0.3, stroke_width=2, corner_radius=0.1)
        formula = VGroup(defn_group, box)
        self.ly.center_in_content(formula)
        formula.shift(UP * 0.5)
        clamp_position(formula)
        self.play(Write(defn), run_time=NORMAL)
        self.play(Write(cond), run_time=NORMAL)
        self.play(Write(implies), run_time=NORMAL)
        self.play(Create(box), run_time=FAST)
        self.wait(1)

        # Now show the geometric interpretation
        self.play(
            FadeOut(formula), FadeOut(title),
            run_time=0.6,
        )

        geo_title = self.ly.title("Geometric Interpretation")

        # Function graph: f(x) = 3x - 1
        geo_axes = Axes(
            x_range=[0, 4, 1], y_range=[0, 8, 1],
            x_length=6, y_length=4,
            axis_config={"include_numbers": True, "font_size": 18, "stroke_width": 1.5},
        )
        self.ly.center_in_content(geo_axes)
        geo_axes.shift(UP * 0.2)
        clamp_position(geo_axes)
        self.play(Create(geo_axes), run_time=NORMAL)

        geo_graph = geo_axes.plot(lambda x: 3 * x - 1, x_range=[0.5, 3.5], color=SECONDARY)
        self.play(Create(geo_graph), run_time=NORMAL)

        # Points: a=2, L=5
        a_point = geo_axes.c2p(2, 0)
        L_point = geo_axes.c2p(0, 5)

        # Epsilon band (horizontal)
        eps_top = DashedLine(
            geo_axes.c2p(0.5, 6), geo_axes.c2p(3.5, 6),
            color=PRIMARY, stroke_width=1.5,
        )
        eps_bot = DashedLine(
            geo_axes.c2p(0.5, 4), geo_axes.c2p(3.5, 4),
            color=PRIMARY, stroke_width=1.5,
        )
        eps_label = MathTex(r"\varepsilon", font_size=BODY_SIZE, color=PRIMARY)
        eps_label.next_to(eps_top, RIGHT, buff=0.1)
        eps_bracket = Brace(
            VGroup(eps_top, eps_bot), RIGHT, buff=0.05,
            stroke_color=PRIMARY,
        )

        # Delta tube (vertical)
        del_right = DashedLine(
            geo_axes.c2p(2.5, 0), geo_axes.c2p(2.5, 7),
            color=RED, stroke_width=1.5,
        )
        del_left = DashedLine(
            geo_axes.c2p(1.5, 0), geo_axes.c2p(1.5, 7),
            color=RED, stroke_width=1.5,
        )
        del_label = MathTex(r"\delta", font_size=BODY_SIZE, color=RED)
        del_label.next_to(del_right, UP, buff=0.1)
        del_bracket = Brace(
            VGroup(del_left, del_right), UP, buff=0.05,
            stroke_color=RED,
        )

        self.play(
            Create(eps_top), Create(eps_bot), run_time=NORMAL,
        )
        self.play(FadeIn(eps_label), run_time=FAST)
        self.wait(0.3)

        self.play(
            Create(del_left), Create(del_right), run_time=NORMAL,
        )
        self.play(FadeIn(del_label), run_time=FAST)
        self.wait(0.5)

        # Point on graph at (2, 5)
        graph_point = Dot(geo_axes.c2p(2, 5), color=ACCENT, radius=0.08)
        gp_label = MathTex("(a, L)", font_size=LABEL_SIZE, color=ACCENT)
        gp_label.next_to(graph_point, UR, buff=0.15)
        self.play(FadeIn(graph_point), Write(gp_label), run_time=FAST)
        self.wait(1)

        # Key text
        key_text = Text(
            "If x is inside the delta-tube, then f(x) is inside the epsilon-band.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(key_text, direction=DOWN, anchor=geo_axes, buff=0.3)
        self.play(FadeIn(key_text, shift=UP * 0.1), run_time=NORMAL)
        self.wait(42.1)  # pacing: extends caption slot (Δ=+40.1)

        self.ly.clear()

    # --- Scene 6: Section Divider -- Proof ---
    def scene6_divider_proof(self):
        self.add_subcaption(
            "Now let us prove a limit using epsilon-delta.",
            duration=3.6,  # pacing: declared ~= 1.15x natural TTS (3.05s)
        )
        self.ly.section_divider(3, "Proof Example", hold=1.7)  # pacing: hold=0.8+0.9 extends caption slot
        self.ly.clear()

    # --- Scene 7: Proof -- lim 3x-1 = 5 as x->2 ---
    def scene7_proof_example(self):
        self.add_subcaption(
            "Claim: the limit as x approaches 2 of 3x minus 1 equals 5. "
            "Let epsilon be positive. "
            "We need to find a delta such that "
            "whenever x is within delta of 2, "
            "f of x is within epsilon of 5. "
            "Working backwards: "
            "f of x minus 5 equals 3x minus 1 minus 5, "
            "which simplifies to 3x minus 6, which is 3 times x minus 2. "
            "We want this to be less than epsilon, "
            "so we need x minus 2 to be less than epsilon over 3. "
            "Therefore choose delta equals epsilon over 3. "
            "Now verify forwards. "
            "If zero less than x minus 2 less than delta, "
            "then f of x minus 5 equals 3 times x minus 2, "
            "which is less than 3 times delta, "
            "equals 3 times epsilon over 3, equals epsilon. "
            "Proof complete.",
            duration=62.4,  # pacing: declared ~= 1.15x natural TTS (54.22s)
        )

        title = self.ly.title("Proof: lim 3x-1 = 5")

        # Claim
        claim = MathTex(
            r"\lim_{x \to 2} (3x - 1) = 5",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(claim, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(claim), run_time=NORMAL)
        self.wait(0.5)

        # Step 1
        step1 = MathTex(
            r"\text{Let } \varepsilon > 0.",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=claim, buff=0.3)
        self.play(FadeIn(step1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Step 2: choose delta
        step2 = MathTex(
            r"\text{Choose } \delta = \frac{\varepsilon}{3}.",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.3)
        self.play(FadeIn(step2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Remove claim and step1 to make room
        self.play(FadeOut(claim), FadeOut(step1), run_time=0.4)

        # Step 3: Suppose
        step3 = MathTex(
            r"0 < |x - 2| < \delta",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(step3, direction=DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(step3, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Step 4: Then
        step4 = MathTex(
            r"|f(x) - 5| = |3x - 6| = 3|x - 2|",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(step4, direction=DOWN, anchor=step3, buff=0.3)
        self.play(FadeIn(step4, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Step 5: conclusion
        step5 = MathTex(
            r"< 3\delta = 3 \cdot \frac{\varepsilon}{3} = \varepsilon \;\checkmark",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step5, direction=DOWN, anchor=step4, buff=0.3)
        self.play(FadeIn(step5, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # QED
        qed = MathTex("QED", font_size=HEADING_SIZE, color=ACCENT)
        self.ly.safe_place(qed, direction=DOWN, anchor=step5, buff=0.3)
        self.play(Write(qed), run_time=FAST)
        self.wait(0.5)

        # Key insight
        self.play(
            FadeOut(step2), FadeOut(step3), FadeOut(step4), FadeOut(step5), FadeOut(qed),
            run_time=0.5,
        )
        insight = Text(
            "Work backwards to find delta, then verify forwards!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(insight)
        self.play(FadeIn(insight, shift=UP * 0.1), run_time=NORMAL)
        self.wait(53.9)  # pacing: extends caption slot (Δ=+51.9)

        self.ly.clear()

    # --- Scene 8: Section Divider -- Sequential Characterization ---
    def scene8_divider_sequential(self):
        self.add_subcaption(
            "There is a beautiful connection between limits of functions "
            "and limits of sequences.",
            duration=6.1,  # pacing: declared ~= 1.15x natural TTS (5.23s)
        )
        self.ly.section_divider(4, "Limits and Sequences", hold=4.4)  # pacing: hold=0.8+3.6 extends caption slot
        self.ly.clear()

    # --- Scene 9: Sequential Characterization ---
    def scene9_sequential_characterization(self):
        self.add_subcaption(
            "Theorem: the limit of f of x as x approaches a equals L "
            "if and only if for every sequence x sub n converging to a, "
            "with x sub n not equal to a, "
            "the sequence f of x sub n converges to L. "
            "This connects everything we learned about sequences "
            "to limits of functions. "
            "The power of this theorem is in its contrapositive. "
            "To show that a limit does NOT exist, "
            "just find two sequences approaching a "
            "that give different limits for f of x sub n. "
            "Consider f of x equals sine of pi over x "
            "as x approaches zero. "
            "If we pick x sub n equals one over n, "
            "then f of x sub n equals sine of n pi, which is zero for all n. "
            "But if we pick y sub n equals two over 2n plus 1, "
            "then f of y sub n equals sine of 2n plus 1 times pi over 2, "
            "which alternates between 1 and negative 1. "
            "Two sequences approaching zero give different outputs. "
            "Therefore the limit does not exist.",
            duration=71.6,  # pacing: declared ~= 1.15x natural TTS (62.23s)
        )

        # Part 1: Theorem statement
        title = self.ly.title("Sequential Characterization")

        theorem = MathTex(
            r"\lim_{x \to a} f(x) = L \iff",
            font_size=BODY_SIZE, color=WHITE,
        )
        condition = MathTex(
            r"\forall (x_n) \to a \;(x_n \neq a):\; f(x_n) \to L",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        thm_group = VGroup(theorem, condition).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        box = SurroundingRectangle(thm_group, color=ACCENT, buff=0.25, stroke_width=2, corner_radius=0.1)
        formula = VGroup(thm_group, box)
        self.ly.center_in_content(formula)
        formula.shift(UP * 0.5)
        clamp_position(formula)
        self.play(Write(theorem), run_time=NORMAL)
        self.play(Write(condition), run_time=NORMAL)
        self.play(Create(box), run_time=FAST)
        self.wait(1)

        # Transition to application
        self.play(
            FadeOut(formula), FadeOut(title),
            run_time=0.6,
        )

        app_title = self.ly.title("Application: sin(pi/x) has no limit at 0")

        # Graph of sin(pi/x) near 0
        app_axes = Axes(
            x_range=[-0.5, 0.5, 0.1], y_range=[-1.5, 1.5, 0.5],
            x_length=7, y_length=3.5,
            axis_config={"include_numbers": True, "font_size": 18, "stroke_width": 1.5},
        )
        self.ly.center_in_content(app_axes)
        app_axes.shift(UP * 0.2)
        clamp_position(app_axes)
        self.play(Create(app_axes), run_time=NORMAL)

        app_graph = app_axes.plot(
            lambda x: np.sin(np.pi / x) if abs(x) > 0.01 else 0,
            x_range=[-0.4, -0.01], color=PRIMARY,
        )
        app_graph2 = app_axes.plot(
            lambda x: np.sin(np.pi / x) if abs(x) > 0.01 else 0,
            x_range=[0.01, 0.4], color=PRIMARY,
        )
        self.play(Create(app_graph), Create(app_graph2), run_time=NORMAL)
        self.wait(0.5)

        # Sequence 1: x_n = 1/n -> f(x_n) = sin(n*pi) = 0
        seq1_label = MathTex(
            r"x_n = \frac{1}{n} \implies f(x_n) = \sin(n\pi) = 0",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(seq1_label, direction=DOWN, anchor=app_axes, buff=0.3)
        self.play(FadeIn(seq1_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Sequence 2: y_n -> f(y_n) = +-1
        seq2_label = MathTex(
            r"y_n = \frac{2}{2n+1} \implies f(y_n) = \pm 1",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(seq2_label, direction=DOWN, anchor=seq1_label, buff=0.3)
        self.play(FadeIn(seq2_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Conclusion
        self.play(FadeOut(seq1_label), FadeOut(seq2_label), run_time=0.4)
        conclusion = Text(
            "Different sequences -> different limits.\nTherefore: the limit does NOT exist!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(conclusion, direction=DOWN, anchor=app_axes, buff=0.3)
        self.play(FadeIn(conclusion, shift=UP * 0.1), run_time=NORMAL)
        self.wait(64.0)  # pacing: extends caption slot (Δ=+62.0)

        self.ly.clear()

    # --- Scene 10: Summary + Outro ---
    def scene10_summary_outro(self):
        self.add_subcaption(
            "Five things to remember. "
            "The epsilon-delta definition makes the idea of f of x approaching L "
            "mathematically precise. "
            "The quantifier order is crucial: "
            "for every epsilon, there exists a delta. "
            "Epsilon is given to you, and you must find the matching delta. "
            "The limit at a point does not depend on the function value at that point. "
            "The sequential characterization says a function limit exists "
            "if and only if every sequence converging to a "
            "gives f of x sub n converging to L. "
            "And to prove a limit does not exist, "
            "just find two sequences approaching a that give different outputs. "
            "Next time, we use limits to define continuity.",
            duration=47.8,  # pacing: declared ~= 1.15x natural TTS (41.50s)
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text(
                "1. Epsilon-delta makes \"approaching\" precise",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. Quantifier order matters: eps -> delta",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3. The limit ignores the value f(a)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "4. Sequential criterion connects to sequences",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "5. To show no limit: find two sequences, different outputs",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(takeaways, start_from=title)
        self.wait(36.8)  # pacing: extends caption slot (Δ=+35.8)

        self.ly.clear()

        # Outro
        play_outro(self, next_video="Continuity (Epsilon-Delta)", next_playlist="Real Analysis I")
