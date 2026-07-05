"""
Video 103: Continuity (Epsilon-Delta Definition)
TEMPLATE v2 -- Professional quality Manim script

Playlist: Real Analysis I (Video 5 of 12)
Class: Video103_Continuity

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


class Video103_Continuity(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_key_idea()
        self.scene4_divider_definition()
        self.scene5_epsilon_delta_animated()
        self.scene6_divider_proof()
        self.scene7_proof_example()
        self.scene8_divider_sequential()
        self.scene9_sequential_discontinuities()
        self.scene10_summary_outro()

    # --- Scene 1: Hook --- Two Functions, One Question ---
    def scene1_hook(self):
        self.add_subcaption(
            "In calculus, your teacher said a function is continuous "
            "if you can draw its graph without lifting your pen. "
            "That intuition is useful, but can we make it rigorous? "
            "What exactly does it mean for a function to have no breaks?",
            duration=22,
        )
        play_intro(self, "Continuity", "Real Analysis I")

        title = self.ly.title("The Graph You Can Draw Without Lifting Your Pen")

        # Two function graphs side by side
        g1 = Axes(
            x_range=[-3, 3, 1], y_range=[-1, 9, 1],
            x_length=3.8, y_length=3.0,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        )
        g1.move_to(LEFT * 3.8 + DOWN * 0.3)
        p1 = g1.plot(lambda x: x**2, x_range=[-2.5, 2.5], color=PRIMARY)
        l1 = MathTex("x^2", font_size=LABEL_SIZE, color=PRIMARY)
        l1.next_to(g1, UP, buff=0.15)

        g2 = Axes(
            x_range=[-3, 3, 1], y_range=[-1.5, 1.5, 0.5],
            x_length=3.8, y_length=3.0,
            axis_config={"include_numbers": False, "stroke_width": 1.5},
        )
        g2.move_to(RIGHT * 3.8 + DOWN * 0.3)
        p2a = g2.plot(lambda x: -1, x_range=[-2.5, -0.05], color=RED)
        p2b = g2.plot(lambda x: 1, x_range=[0.05, 2.5], color=RED)
        l2 = MathTex(r"\frac{|x|}{x}", font_size=LABEL_SIZE, color=RED)
        l2.next_to(g2, UP, buff=0.15)

        self.play(FadeIn(VGroup(g1, p1, l1), shift=LEFT * 0.15, run_time=NORMAL))
        self.wait(0.3)
        self.play(FadeIn(VGroup(g2, p2a, p2b, l2), shift=LEFT * 0.15, run_time=NORMAL))
        self.wait(0.5)

        question = Text(
            "What does NO BREAKS mean rigorously?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(question, direction=DOWN, anchor=g1, buff=0.4)
        self.play(Write(question), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # --- Scene 2: Intro + Section Divider ---
    def scene2_intro(self):
        self.add_subcaption(
            "To answer that, we will build on the epsilon-delta "
            "definition of limits from our last video.",
            duration=6,
        )
        self.ly.section_divider("1", "From Limits to Continuity")
        self.ly.clear()

    # --- Scene 3: Key Idea --- Continuity = Limit Equals Value ---
    def scene3_key_idea(self):
        self.add_subcaption(
            "The key insight is beautifully simple. "
            "A function f is continuous at a point a, "
            "if the limit of f of x as x approaches a, equals f of a. "
            "The limit captures the predicted value near the point. "
            "Continuity says the prediction is exactly right.",
            duration=25,
        )

        title = self.ly.title("Continuity = Limit Equals Value")

        items = [
            Text("The limit of f(x) as x approaches a", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("predicts what f does NEAR a", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Continuity: the prediction is CORRECT", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(0.5)

        # Definition formula
        definition = MathTex(
            r"\lim_{x \to a} f(x) = f(a)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(definition, ACCENT)
        self.wait(1)
        self.ly.clear()

    # --- Scene 4: Section Divider ---
    def scene4_divider_definition(self):
        self.add_subcaption(
            "Now let's see the formal epsilon-delta definition.",
            duration=4,
        )
        self.ly.section_divider("2", "The Formal Definition")
        self.ly.clear()

    # --- Scene 5: Epsilon-Delta Definition Animated ---
    def scene5_epsilon_delta_animated(self):
        self.add_subcaption(
            "We say f is continuous at a if for every epsilon "
            "greater than zero, there exists a delta greater than zero, "
            "such that whenever the absolute value of x minus a is "
            "less than delta, the absolute value of f(x) minus f(a) "
            "is less than epsilon. "
            "Notice the key difference from the limit definition: "
            "we include x equals a. The limit excludes the point itself. "
            "Continuity includes it.",
            duration=30,
        )

        title = self.ly.title("Epsilon-Delta Definition")

        # Definition formula
        def_tex = MathTex(
            r"\forall \varepsilon > 0, \exists \delta > 0, "
            r"|x - a| < \delta \implies |f(x) - f(a)| < \varepsilon",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(def_tex, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(def_tex), run_time=NORMAL)
        self.wait(1)

        # Key difference note
        diff1 = MathTex(r"|x - a| < \delta", font_size=BODY_SIZE, color=PRIMARY)
        diff2 = MathTex(r"0 < |x - a| < \delta", font_size=BODY_SIZE, color=RED)
        diff_label = Text(
            "Continuity INCLUDES the point (left)",
            font_size=SMALL_SIZE, color=PRIMARY, font=SANS,
        )
        diff_label2 = Text(
            "Limit EXCLUDES the point (right)",
            font_size=SMALL_SIZE, color=RED, font=SANS,
        )

        col_left = VGroup(diff1, diff_label).arrange(DOWN, buff=0.1)
        col_right = VGroup(diff2, diff_label2).arrange(DOWN, buff=0.1)

        self.ly.two_columns(
            [col_left], [col_right], start_from=title,
        )
        self.wait(1.5)
        self.ly.clear()

        # Now show continuous function visualization
        self.add_subcaption(
            "Here is what continuity looks like visually. "
            "The delta-tube around x equals a always maps "
            "inside the epsilon-band around f of a. "
            "No matter how small epsilon gets, we can find a delta that works.",
            duration=18,
        )

        title2 = self.ly.title("Continuous: Tube Maps Into Band")

        axes = Axes(
            x_range=[-1, 5, 1], y_range=[-1, 9, 1],
            x_length=7, y_length=4,
            axis_config={"include_numbers": True, "font_size": 20, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        graph = axes.plot(lambda x: x**2, x_range=[0.3, 2.7], color=SECONDARY)
        self.play(Create(graph), run_time=NORMAL)

        # Mark the point a=2, f(a)=4
        a_dot = Dot(axes.c2p(2, 4), color=ACCENT, radius=0.06)
        a_label = MathTex("a=2, f(a)=4", font_size=SMALL_SIZE, color=ACCENT)
        a_label.next_to(a_dot, RIGHT, buff=0.15)
        self.play(FadeIn(a_dot), Write(a_label), run_time=FAST)

        # Epsilon-band (horizontal dashed lines)
        eps_line1 = DashedLine(
            axes.c2p(0, 3.5), axes.c2p(4, 3.5),
            color=PRIMARY, stroke_width=1.5,
        )
        eps_line2 = DashedLine(
            axes.c2p(0, 4.5), axes.c2p(4, 4.5),
            color=PRIMARY, stroke_width=1.5,
        )
        eps_label = MathTex(r"\varepsilon", font_size=SMALL_SIZE, color=PRIMARY)
        eps_label.next_to(eps_line2, RIGHT, buff=0.1)

        self.play(
            FadeIn(eps_line1), FadeIn(eps_line2), Write(eps_label),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Delta-tube (vertical dashed lines)
        delta_line1 = DashedLine(
            axes.c2p(1.5, 0), axes.c2p(1.5, 5),
            color=SECONDARY, stroke_width=1.5,
        )
        delta_line2 = DashedLine(
            axes.c2p(2.5, 0), axes.c2p(2.5, 5),
            color=SECONDARY, stroke_width=1.5,
        )
        delta_label = MathTex(r"\delta", font_size=SMALL_SIZE, color=SECONDARY)
        delta_label.next_to(axes.c2p(1.5, 0), DOWN, buff=0.15)

        self.play(
            FadeIn(delta_line1), FadeIn(delta_line2), Write(delta_label),
            run_time=NORMAL,
        )
        self.wait(1)

        insight = Text(
            "The tube always fits inside the band!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=axes, buff=0.3)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # --- Scene 6: Section Divider ---
    def scene6_divider_proof(self):
        self.add_subcaption(
            "Let's prove continuity for a concrete function.",
            duration=4,
        )
        self.ly.section_divider("3", "Proving Continuity")
        self.ly.clear()

    # --- Scene 7: Proof -- f(x) = x^2 is continuous at a=2 ---
    def scene7_proof_example(self):
        self.add_subcaption(
            "Claim: f of x equals x squared is continuous at a equals 2. "
            "Let epsilon be greater than zero. "
            "Choose delta equal to the minimum of 1 and epsilon over 5. "
            "Suppose the absolute value of x minus 2 is less than delta. "
            "Then the absolute value of f(x) minus f(2) "
            "equals x squared minus 4, "
            "which equals the absolute value of x plus 2, times x minus 2. "
            "Since x minus 2 is less than delta which is at most 1, "
            "we have 1 less than x less than 3, so x plus 2 is less than 5. "
            "Therefore the whole expression is less than "
            "5 times delta, which is less than epsilon. QED.",
            duration=40,
        )

        title = self.ly.title(r"Proof: $f(x) = x^2$ at $a = 2$")

        # Claim
        claim = MathTex(
            r"\lim_{x \to 2} x^2 = 2^2 = 4",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(claim, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(claim), run_time=NORMAL)
        self.wait(0.5)

        # Proof steps
        steps = [
            MathTex(r"\varepsilon > 0 \text{ given}", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"\delta = \min(1, \varepsilon / 5)", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"|x-2| < \delta", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"|x^2 - 4| = |x+2| \cdot |x-2| < 5\delta", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"5\delta \leq 5 \cdot \frac{\varepsilon}{5} = \varepsilon", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"\therefore |x^2 - 4| < \varepsilon \quad \blacksquare", font_size=BODY_SIZE, color=SECONDARY),
        ]

        # Progressive reveal of steps
        visible = [claim]
        for step in steps:
            self.ly.safe_place(step, direction=DOWN, anchor=visible[-1], buff=0.2)
            self.play(FadeIn(step, shift=LEFT * 0.15), run_time=FAST)
            visible.append(step)
            if len(visible) > 5:
                self.play(FadeOut(visible[0]), run_time=FAST)
                visible = visible[1:]

        self.wait(0.5)

        # Key insight
        self.ly.clear()
        title2 = self.ly.title("Key Technique")

        insight = Text(
            "The min(1, eps/5) trick:",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        items = [
            insight,
            Text("Bound one factor by a constant", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Use delta to control the other", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("This gives us a finite bound on |x+2|", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(1)
        self.ly.clear()

    # --- Scene 8: Section Divider ---
    def scene8_divider_sequential(self):
        self.add_subcaption(
            "Now let's connect continuity to sequences.",
            duration=4,
        )
        self.ly.section_divider("4", "Sequences and Discontinuities")
        self.ly.clear()

    # --- Scene 9: Sequential Criterion + Types of Discontinuity ---
    def scene9_sequential_discontinuities(self):
        self.add_subcaption(
            "Theorem: f is continuous at a if and only if "
            "for every sequence x sub n converging to a, "
            "f of x sub n converges to f of a. "
            "This follows directly from the limit definition "
            "and the sequential criterion for limits. "
            "Now let's look at four types of discontinuity. "
            "Removable: the limit exists but f(a) is undefined or wrong. "
            "Jump: the left and right limits exist but differ. "
            "Infinite: the function blows up near the point. "
            "Oscillation: the function oscillates wildly with no limit.",
            duration=40,
        )

        title = self.ly.title("Theorem: Sequential Criterion")

        theorem = MathTex(
            r"f \text{ continuous at } a \iff "
            r"x_n \to a \implies f(x_n) \to f(a)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(theorem, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(theorem), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # Types of discontinuity
        title2 = self.ly.title("Four Types of Discontinuity")

        items = [
            Text("Removable: limit exists, f(a) wrong/undefined", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Jump: left and right limits differ", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Infinite: function blows up", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Oscillation: no limit exists", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(0.5)

        # Examples
        self.ly.clear()
        title3 = self.ly.title("Examples")

        examples = [
            MathTex(r"f(x) = \frac{x^2-4}{x-2} \text{ at } x=2", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"f(x) = \frac{|x|}{x} \text{ at } x=0", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"f(x) = \frac{1}{x} \text{ at } x=0", font_size=BODY_SIZE, color=RED),
            MathTex(r"f(x) = \sin(1/x) \text{ at } x=0", font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(examples, start_from=title3)
        self.wait(0.5)

        # Common theme
        common = Text(
            "In each case, the epsilon-delta definition FAILS.",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(common, direction=DOWN, anchor=examples[-1], buff=0.3)
        self.play(Write(common), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # --- Scene 10: Summary + Outro ---
    def scene10_summary_outro(self):
        self.add_subcaption(
            "Five things to remember. "
            "Continuity means the limit of f of x as x approaches a "
            "equals f of a. The function's predicted value at a "
            "matches its actual value. "
            "In the epsilon-delta definition, we include x equals a, "
            "unlike the limit definition which excludes it. "
            "The sequential criterion says f is continuous at a "
            "if and only if for every sequence converging to a, "
            "f of x sub n converges to f of a. "
            "There are four types of discontinuities: "
            "removable, jump, infinite, and oscillation. "
            "And continuity is a local property, defined point by point. "
            "Next time, we explore uniform continuity, where continuity is global.",
            duration=40,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text("Continuity: lim f(x) = f(a)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Epsilon-delta includes x = a", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Sequential: x_n -> a implies f(x_n) -> f(a)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("4 discontinuities: removable, jump, infinite, oscillation", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Continuity is a LOCAL property", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title)
        self.wait(1)
        self.ly.clear()

        play_outro(self, "Uniform Continuity", "Real Analysis I")
