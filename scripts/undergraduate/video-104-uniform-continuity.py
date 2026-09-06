"""
Video 104: Uniform Continuity
TEMPLATE v2 -- Professional quality Manim script

Playlist: Real Analysis I (Video 6 of 12)
Class: Video104_UniformContinuity

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


class Video104_UniformContinuity(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_pointwise_visual()
        self.scene4_divider_definition()
        self.scene5_formal_definition()
        self.scene6_divider_counterexample()
        self.scene7_counterexample()
        self.scene8_divider_heine_cantor()
        self.scene9_heine_cantor_lipschitz()
        self.scene10_summary_outro()

    # --- Scene 1: Hook --- Same Word, Different Meaning ---
    def scene1_hook(self):
        self.add_subcaption(
            "Last time we defined continuity at a point using "
            "epsilon and delta. The delta we found depended on "
            "both the point and epsilon. "
            "What if we need one delta that works for every "
            "point simultaneously? That is uniform continuity, "
            "and it changes everything.",
            duration=16.3,
        )
        play_intro(self, "Uniform Continuity", "Real Analysis I")

        title = self.ly.title("Same Word, Different Meaning")

        # Recall the continuity definition
        def_tex = MathTex(
            r"\forall \varepsilon > 0, \exists \delta > 0:",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(def_tex, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(def_tex), run_time=NORMAL)
        self.wait(0.3)

        implication = MathTex(
            r"|x - a| < \delta \implies |f(x) - f(a)| < \varepsilon",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(implication, direction=DOWN, anchor=def_tex, buff=0.3)
        self.play(Write(implication), run_time=NORMAL)
        self.wait(0.5)

        # Highlight the key dependency
        key1 = Text(
            "delta depends on BOTH a and epsilon",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(key1, direction=DOWN, anchor=implication, buff=0.4)
        self.play(FadeIn(key1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        key2 = Text(
            "What if ONE delta works for ALL points?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(key2, direction=DOWN, anchor=key1, buff=0.4)
        self.play(FadeIn(key2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4.1)  # pacing: extends previous caption slot (+3.1s)
        self.ly.clear()

    # --- Scene 2: Intro + Section Divider ---
    def scene2_intro(self):
        self.add_subcaption(
            "Let's start by seeing what pointwise continuity "
            "looks like visually, and why the deltas can differ.",
            duration=5.9,
        )
        self.ly.section_divider("1", "Pointwise vs Uniform", hold=3.7)  # pacing: extends previous caption slot (+2.9s)
        self.ly.clear()

    # --- Scene 3: Visual Comparison --- Pointwise Continuity ---
    def scene3_pointwise_visual(self):
        self.add_subcaption(
            "Consider f of x equals x squared. "
            "At x equals 1 the slope is gentle, so a large "
            "delta tube fits. At x equals 3 the function is "
            "steeper, so we need a smaller delta. At x equals 5 "
            "the slope is even steeper, and delta must be tiny. "
            "Each point needs its own delta. "
            "This is perfectly fine for pointwise continuity.",
            duration=23.3,
        )

        title = self.ly.title("Pointwise: Different Points, Different Deltas")

        # Graph of x^2
        axes = Axes(
            x_range=[-0.5, 7, 1], y_range=[-1, 30, 5],
            x_length=7, y_length=4,
            axis_config={"include_numbers": True, "font_size": 18, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        graph = axes.plot(lambda x: x**2, x_range=[0.2, 5.5], color=SECONDARY)
        self.play(Create(graph), run_time=NORMAL)

        # Three marked points
        p1 = Dot(axes.c2p(1, 1), color=PRIMARY, radius=0.06)
        p2 = Dot(axes.c2p(3, 9), color=ACCENT, radius=0.06)
        p3 = Dot(axes.c2p(5, 25), color=RED, radius=0.06)

        l1 = MathTex(r"\delta_1", font_size=SMALL_SIZE, color=PRIMARY)
        l1.next_to(p1, DOWN, buff=0.1)
        l2 = MathTex(r"\delta_2", font_size=SMALL_SIZE, color=ACCENT)
        l2.next_to(p2, DOWN, buff=0.1)
        l3 = MathTex(r"\delta_3", font_size=SMALL_SIZE, color=RED)
        l3.next_to(p3, DOWN, buff=0.1)

        self.play(
            FadeIn(p1), Write(l1),
            run_time=FAST,
        )
        self.wait(0.3)
        self.play(
            FadeIn(p2), Write(l2),
            run_time=FAST,
        )
        self.wait(0.3)
        self.play(
            FadeIn(p3), Write(l3),
            run_time=FAST,
        )
        self.wait(0.5)

        # Delta tubes (vertical bands) of different widths
        # Large tube at x=1
        d1_left = DashedLine(axes.c2p(0.3, 0), axes.c2p(0.3, 4), color=PRIMARY, stroke_width=1.2)
        d1_right = DashedLine(axes.c2p(1.7, 0), axes.c2p(1.7, 4), color=PRIMARY, stroke_width=1.2)
        # Medium tube at x=3
        d2_left = DashedLine(axes.c2p(2.4, 4), axes.c2p(2.4, 14), color=ACCENT, stroke_width=1.2)
        d2_right = DashedLine(axes.c2p(3.6, 4), axes.c2p(3.6, 14), color=ACCENT, stroke_width=1.2)
        # Small tube at x=5
        d3_left = DashedLine(axes.c2p(4.7, 16), axes.c2p(4.7, 30), color=RED, stroke_width=1.2)
        d3_right = DashedLine(axes.c2p(5.3, 16), axes.c2p(5.3, 30), color=RED, stroke_width=1.2)

        self.play(
            FadeIn(d1_left), FadeIn(d1_right),
            run_time=FAST,
        )
        self.wait(0.2)
        self.play(
            FadeIn(d2_left), FadeIn(d2_right),
            run_time=FAST,
        )
        self.wait(0.2)
        self.play(
            FadeIn(d3_left), FadeIn(d3_right),
            run_time=FAST,
        )
        self.wait(0.5)

        insight = Text(
            "Gentle slope = large delta. Steep slope = small delta.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=axes, buff=0.3)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(14.9)  # pacing: extends previous caption slot (+13.9s)
        self.ly.clear()

    # --- Scene 4: Section Divider ---
    def scene4_divider_definition(self):
        self.add_subcaption(
            "Now let's see the formal definition of "
            "uniform continuity.",
            duration=3.9,
        )
        self.ly.section_divider("2", "The Definition", hold=1.5)  # pacing: extends previous caption slot (+0.7s)
        self.ly.clear()

    # --- Scene 5: Formal Definition + Visual ---
    def scene5_formal_definition(self):
        self.add_subcaption(
            "The definition of uniform continuity is similar to "
            "ordinary continuity, with one crucial change. "
            "We say f is uniformly continuous on S if for every "
            "epsilon greater than zero, there exists a delta "
            "greater than zero, such that for all x and y in S, "
            "the absolute value of x minus y less than delta "
            "implies the absolute value of f(x) minus f(y) "
            "less than epsilon. "
            "Notice we use x and y, two arbitrary points, not "
            "x and a fixed point. "
            "Uniform continuity is about pairs of points.",
            duration=36.7,
        )

        title = self.ly.title("Side by Side: Pointwise vs Uniform")

        # Left: pointwise definition
        pw_title = Text("Pointwise", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        pw_def = MathTex(
            r"\forall \varepsilon > 0, \exists \delta(a, \varepsilon) > 0:",
            font_size=SMALL_SIZE, color=WHITE,
        )
        pw_impl = MathTex(
            r"|x - a| < \delta \implies |f(x) - f(a)| < \varepsilon",
            font_size=SMALL_SIZE, color=WHITE,
        )
        pw_col = VGroup(pw_title, pw_def, pw_impl).arrange(DOWN, buff=0.2)

        # Right: uniform definition
        uc_title = Text("Uniform", font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        uc_def = MathTex(
            r"\forall \varepsilon > 0, \exists \delta(\varepsilon) > 0:",
            font_size=SMALL_SIZE, color=WHITE,
        )
        uc_impl = MathTex(
            r"\forall x,y \in S: |x-y|<\delta \implies |f(x)-f(y)|<\varepsilon",
            font_size=SMALL_SIZE, color=WHITE,
        )
        uc_col = VGroup(uc_title, uc_def, uc_impl).arrange(DOWN, buff=0.2)

        cols = self.ly.two_columns([pw_col], [uc_col], start_from=title)
        self.wait(7.0)  # pacing: extends caption slot (+6.0s)

        # Highlight key differences
        self.ly.clear()
        title2 = self.ly.title("The Key Differences")

        items = [
            Text("Pointwise: delta depends on a AND epsilon", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Uniform: delta depends on epsilon ONLY", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Uniform uses x,y (two arbitrary points)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("ONE delta tube works EVERYWHERE on the domain", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(7.0)  # pacing: extends caption slot (+6.0s)

        # Visual: sliding delta tube
        self.ly.clear()
        title3 = self.ly.title("Uniform: ONE Tube Fits Everywhere")

        axes = Axes(
            x_range=[-0.5, 5, 1], y_range=[-0.5, 4, 0.5],
            x_length=7, y_length=3.5,
            axis_config={"include_numbers": True, "font_size": 18, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        # Use a bounded function for this visual (e.g. sin(x) on [0, 2pi])
        graph = axes.plot(lambda x: 1 + 1.5 * np.sin(x), x_range=[0.1, 6.1], color=SECONDARY)
        self.play(Create(graph), run_time=NORMAL)

        # Sliding epsilon band
        eps_upper = DashedLine(
            axes.c2p(0, 2.8), axes.c2p(6, 2.8),
            color=PRIMARY, stroke_width=1.5,
        )
        eps_lower = DashedLine(
            axes.c2p(0, -0.2), axes.c2p(6, -0.2),
            color=PRIMARY, stroke_width=1.5,
        )
        self.play(FadeIn(eps_upper), FadeIn(eps_lower), run_time=FAST)
        self.wait(0.3)

        # Delta tube at position 1
        tube1_l = DashedLine(axes.c2p(0.8, -0.5), axes.c2p(0.8, 3.5), color=SECONDARY, stroke_width=1.5)
        tube1_r = DashedLine(axes.c2p(2.2, -0.5), axes.c2p(2.2, 3.5), color=SECONDARY, stroke_width=1.5)
        self.play(FadeIn(tube1_l), FadeIn(tube1_r), run_time=FAST)
        self.wait(0.3)

        # Slide to position 2
        tube2_l = DashedLine(axes.c2p(2.5, -0.5), axes.c2p(2.5, 3.5), color=SECONDARY, stroke_width=1.5)
        tube2_r = DashedLine(axes.c2p(3.9, -0.5), axes.c2p(3.9, 3.5), color=SECONDARY, stroke_width=1.5)
        self.play(
            FadeOut(tube1_l), FadeOut(tube1_r),
            FadeIn(tube2_l), FadeIn(tube2_r),
            run_time=NORMAL,
        )
        self.wait(0.3)

        # Slide to position 3
        tube3_l = DashedLine(axes.c2p(4.2, -0.5), axes.c2p(4.2, 3.5), color=SECONDARY, stroke_width=1.5)
        tube3_r = DashedLine(axes.c2p(5.6, -0.5), axes.c2p(5.6, 3.5), color=SECONDARY, stroke_width=1.5)
        self.play(
            FadeOut(tube2_l), FadeOut(tube2_r),
            FadeIn(tube3_l), FadeIn(tube3_r),
            run_time=NORMAL,
        )
        self.wait(0.3)

        label = Text(
            "Same delta tube, sliding across the domain!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(label, direction=DOWN, anchor=axes, buff=0.3)
        self.play(Write(label), run_time=NORMAL)
        self.wait(8.0)  # pacing: extends caption slot (+7.0s)
        self.ly.clear()

    # --- Scene 6: Section Divider ---
    def scene6_divider_counterexample(self):
        self.add_subcaption(
            "Not every continuous function is uniformly continuous. "
            "Let's see a famous counterexample.",
            duration=6.1,
        )
        self.ly.section_divider("3", "Continuous but Not Uniformly Continuous", hold=3.9)  # pacing: extends previous caption slot (+3.1s)
        self.ly.clear()

    # --- Scene 7: Counterexample --- f(x) = 1/x on (0,1) ---
    def scene7_counterexample(self):
        self.add_subcaption(
            "The classic counterexample: f of x equals one over x "
            "on the open interval from 0 to 1. "
            "This function IS continuous at every point in the "
            "interval. But is it uniformly continuous? "
            "Pick epsilon equal to 1. Near x equals 0.01, "
            "we need delta less than 0.0001. "
            "As x approaches 0, the required delta shrinks "
            "to zero. No single delta works for the entire interval.",
            duration=29.8,
        )

        title = self.ly.title(r"Counterexample: $f(x) = 1/x$ on $(0,1)$")

        # Graph of 1/x on (0.05, 1)
        axes = Axes(
            x_range=[0, 1.2, 0.2], y_range=[0, 12, 2],
            x_length=6, y_length=4,
            axis_config={"include_numbers": True, "font_size": 18, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        graph = axes.plot(lambda x: 1 / x, x_range=[0.08, 1.1], color=SECONDARY)
        self.play(Create(graph), run_time=NORMAL)

        # Mark a point near x=1 (gentle)
        p_gentle = Dot(axes.c2p(0.9, 1.11), color=PRIMARY, radius=0.06)
        l_gentle = MathTex("x=0.9", font_size=SMALL_SIZE, color=PRIMARY)
        l_gentle.next_to(p_gentle, DOWN, buff=0.1)
        self.play(FadeIn(p_gentle), Write(l_gentle), run_time=FAST)
        self.wait(0.3)

        # Delta tube near x=1 (wide, works fine)
        dg_l = DashedLine(axes.c2p(0.7, 0), axes.c2p(0.7, 2), color=PRIMARY, stroke_width=1.5)
        dg_r = DashedLine(axes.c2p(1.1, 0), axes.c2p(1.1, 2), color=PRIMARY, stroke_width=1.5)
        self.play(FadeIn(dg_l), FadeIn(dg_r), run_time=FAST)
        self.wait(0.5)

        fits = Text("Fits easily here!", font_size=SMALL_SIZE, color=PRIMARY, font=SANS)
        fits.next_to(dg_r, RIGHT, buff=0.15)
        self.play(Write(fits), run_time=FAST)
        self.wait(0.5)

        # Now try near x=0.1
        self.play(
            FadeOut(dg_l), FadeOut(dg_r), FadeOut(fits),
            run_time=FAST,
        )

        p_steep = Dot(axes.c2p(0.1, 10), color=RED, radius=0.06)
        l_steep = MathTex("x=0.1", font_size=SMALL_SIZE, color=RED)
        l_steep.next_to(p_steep, LEFT, buff=0.1)
        self.play(FadeIn(p_steep), Write(l_steep), run_time=FAST)
        self.wait(0.3)

        # Very narrow delta tube near x=0.1
        ds_l = DashedLine(axes.c2p(0.09, 0), axes.c2p(0.09, 12), color=RED, stroke_width=1.5)
        ds_r = DashedLine(axes.c2p(0.11, 0), axes.c2p(0.11, 12), color=RED, stroke_width=1.5)
        self.play(FadeIn(ds_l), FadeIn(ds_r), run_time=FAST)
        self.wait(0.5)

        fails = Text("Delta must be tiny!", font_size=SMALL_SIZE, color=RED, font=SANS)
        fails.next_to(ds_r, RIGHT, buff=0.15)
        self.play(Write(fails), run_time=FAST)
        self.wait(0.5)

        # Show the problem gets worse closer to 0
        self.play(
            FadeOut(ds_l), FadeOut(ds_r), FadeOut(fails),
            FadeOut(p_steep), FadeOut(l_steep),
            run_time=FAST,
        )

        p_worse = Dot(axes.c2p(0.05, 20), color=RED, radius=0.06)
        # The point goes off-screen for very small x, so let's just note it
        # Instead, show it at x=0.05 which is at y=20 (off the visible graph)
        # Let's use x=0.07, y≈14
        p_worse = Dot(axes.c2p(0.07, 14), color=RED, radius=0.06)
        l_worse = MathTex("x=0.07", font_size=SMALL_SIZE, color=RED)
        l_worse.next_to(p_worse, LEFT, buff=0.1)

        dw_l = DashedLine(axes.c2p(0.068, 0), axes.c2p(0.068, 12), color=RED, stroke_width=1.2)
        dw_r = DashedLine(axes.c2p(0.072, 0), axes.c2p(0.072, 12), color=RED, stroke_width=1.2)
        self.play(
            FadeIn(p_worse), Write(l_worse),
            FadeIn(dw_l), FadeIn(dw_r),
            run_time=FAST,
        )
        self.wait(0.3)

        worse = Text("Even tinier delta needed!", font_size=SMALL_SIZE, color=RED, font=SANS)
        worse.next_to(dw_r, RIGHT, buff=0.15)
        self.play(Write(worse), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

        # Summary insight
        title2 = self.ly.title("Why It Fails")
        items = [
            Text("f(x) = 1/x is continuous at every point in (0,1)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("But near x=0, required delta shrinks to zero", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("No SINGLE delta works for the entire interval", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Problem: (0,1) is open; f is unbounded near 0", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(0.5)

        # Brief mention of x^2 on R
        self.ly.clear()
        title3 = self.ly.title("Another Example")
        items2 = [
            Text("f(x) = x^2 on ALL of R", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Continuous everywhere, but slope grows without bound", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Also NOT uniformly continuous on R", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("(But IS uniformly continuous on any bounded interval)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title3)
        self.wait(5.7)  # pacing: extends previous caption slot (+4.7s)
        self.ly.clear()

    # --- Scene 8: Section Divider ---
    def scene8_divider_heine_cantor(self):
        self.add_subcaption(
            "So when does continuity imply uniform continuity? "
            "The Heine-Cantor theorem gives the answer.",
            duration=6.0,
        )
        self.ly.section_divider("4", "Heine-Cantor Theorem", hold=3.9)  # pacing: extends previous caption slot (+3.1s)
        self.ly.clear()

    # --- Scene 9: Heine-Cantor Theorem Sketch + Lipschitz ---
    def scene9_heine_cantor_lipschitz(self):
        self.add_subcaption(
            "The Heine-Cantor theorem states that if f is "
            "continuous on a closed and bounded interval a b, "
            "then f is uniformly continuous on a b. "
            "The proof sketch goes like this. "
            "By continuity, each point c in the interval has "
            "its own delta. These delta neighborhoods form an "
            "open cover. By the Heine-Borel theorem, a finite "
            "subcover exists. Take delta as the minimum of all "
            "these deltas. This one delta works everywhere. "
            "The key insight is that compactness guarantees "
            "infinitely many local deltas reduce to a single "
            "global delta. "
            "Now, a stronger condition is Lipschitz continuity. "
            "We say f is Lipschitz if there exists a constant L "
            "such that the absolute value of f(x) minus f(y) "
            "is at most L times the absolute value of x minus y, "
            "for all x and y. "
            "Lipschitz implies uniform continuity: just take "
            "delta equal to epsilon over L. "
            "The absolute value function is Lipschitz with "
            "L equal to 1. x squared is not Lipschitz on R, "
            "but is Lipschitz on any bounded interval.",
            duration=68.4,
        )

        # Part 1: Heine-Cantor Theorem
        title = self.ly.title("Heine-Cantor Theorem")

        theorem = Text(
            "Continuous on [a,b] => Uniformly Continuous",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(theorem, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(theorem, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Proof sketch steps
        steps = [
            Text("Each point c has its own delta(c) by continuity", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("These neighborhoods form an open cover", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Heine-Borel: finite subcover exists", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Take delta = min(delta_1, delta_2, ..., delta_n)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(steps, start_from=theorem)
        self.wait(0.5)

        insight = Text(
            "Compactness: infinitely many local deltas = one global delta",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=steps[-1], buff=0.3)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(26.0)  # pacing: extends caption slot (+25.0s)
        self.ly.clear()

        # Part 2: Lipschitz Connection
        title2 = self.ly.title("Lipschitz Continuity")

        # Lipschitz definition
        lipschitz_def = MathTex(
            r"|f(x) - f(y)| \leq L \, |x - y| \quad \forall x, y",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(lipschitz_def, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(lipschitz_def), run_time=NORMAL)
        self.wait(0.5)

        # Implication
        implies = MathTex(
            r"\delta = \frac{\varepsilon}{L} \implies \text{uniformly continuous}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(implies, direction=DOWN, anchor=lipschitz_def, buff=0.4)
        self.play(Write(implies), run_time=NORMAL)
        self.wait(9.0)  # pacing: extends caption slot (+8.5s)

        # Examples
        self.ly.clear()
        title3 = self.ly.title("Examples")

        items = [
            Text("|x| is Lipschitz (L = 1)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("x^2 is NOT Lipschitz on R (slope grows)", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("x^2 IS Lipschitz on any bounded interval", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title3)
        self.wait(8.8)  # pacing: extends caption slot (+8.3s)

        # Hierarchy
        self.ly.clear()
        title4 = self.ly.title("The Hierarchy")

        # Hierarchy: Lipschitz -> Uniform -> Continuous
        lip = Text("Lipschitz", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        arrow1 = MathTex(r"\Longrightarrow", font_size=HEADING_SIZE, color=DIM)
        uni = Text("Uniformly Continuous", font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        arrow2 = MathTex(r"\Longrightarrow", font_size=HEADING_SIZE, color=DIM)
        con = Text("Continuous", font_size=HEADING_SIZE, color=WHITE, font=SANS)

        hierarchy = VGroup(lip, arrow1, uni, arrow2, con).arrange(RIGHT, buff=0.3)
        self.ly.center_in_content(hierarchy)
        clamp_position(hierarchy)
        self.play(
            FadeIn(lip, shift=LEFT * 0.15),
            FadeIn(arrow1),
            FadeIn(uni, shift=LEFT * 0.15),
            FadeIn(arrow2),
            FadeIn(con, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(8.0)  # pacing: extends caption slot (+7.0s)
        self.ly.clear()

    # --- Scene 10: Summary + Outro ---
    def scene10_summary_outro(self):
        self.add_subcaption(
            "Five things to remember about uniform continuity. "
            "Pointwise continuity means delta depends on epsilon "
            "and the point. Uniform continuity means one delta "
            "works for all points. "
            "The function one over x on the open interval from "
            "0 to 1 is continuous but not uniformly continuous. "
            "The Heine-Cantor theorem says continuous on a "
            "closed interval implies uniformly continuous. "
            "And the hierarchy goes: Lipschitz implies uniform "
            "implies continuous. "
            "Next time, we rigorously define the derivative.",
            duration=34.1,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text("Pointwise: delta depends on epsilon AND the point", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Uniform: ONE delta works for ALL points", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("1/x on (0,1): continuous but NOT uniformly continuous", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Heine-Cantor: continuous on [a,b] => uniformly continuous", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Hierarchy: Lipschitz -> Uniform -> Continuous", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title)
        self.wait(21.7)  # pacing: extends previous caption slot (+20.7s)
        self.ly.clear()

        play_outro(self, "The Derivative (Rigorous)", "Real Analysis I")
