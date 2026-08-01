"""
Video 145: Metric Spaces and Metrization -- Topology Playlist
TEMPLATE v2 -- Professional quality Manim script

Playlist: Topology (Video 10 of 12)
Class: Video145_MetricSpaces

Topics: Metric spaces, metric topology, open balls, metrization,
         Urysohn's Metrization Theorem, non-metrizable spaces.

Quality Rules (mandatory):
1. Max 5 visible elements per scene at any time
2. Use LayoutEngine for ALL positioning -- no manual .shift() or .to_edge()
3. Progressive disclosure: add items one at a time
4. Each add_subcaption() duration = words / 2.5 seconds (12 words = 5s)
5. Call ly.clear() between scenes
6. Use consistent animation vocabulary from channel_branding.py
7. MathTex: raw strings with single backslashes
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


class Video145_MetricSpaces(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_metric_spaces()
        self.scene3_metric_topology()
        self.scene4_examples()
        self.scene5_metrization()
        self.scene6_summary()

    # --- Scene 1: Hook ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "Can every topological space arise from measuring distances? "
            "A metric gives us a precise notion of distance, and every "
            "metric naturally defines open sets via open balls. But not "
            "every topology comes from a metric. Understanding which "
            "topologies are metrizable and which are not is one of the "
            "central questions in topology.",
            duration=50,
        )
        play_intro(self, "Metric Spaces & Metrization", "Topology")

        # Visual: two points with distance
        pt_a = Dot(LEFT * 2, radius=0.08, color=PRIMARY)
        pt_b = Dot(RIGHT * 2, radius=0.08, color=SECONDARY)
        dist_line = Line(LEFT * 2, RIGHT * 2, color=DIM, stroke_width=1)
        dist_label = MathTex(r"d(x, y) = \text{distance}", font_size=BODY_SIZE, color=ACCENT)
        vis = VGroup(pt_a, dist_line, pt_b, dist_label).arrange(DOWN, buff=0.2)
        self.ly.center_in_content(vis)
        self.play(Create(dist_line), FadeIn(pt_a), FadeIn(pt_b), run_time=FAST)
        self.play(FadeIn(dist_label, shift=UP * 0.15), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 2: Metric Spaces ~60s

    def scene2_metric_spaces(self):
        self.add_subcaption(
            "A metric space is a set X together with a distance function "
            "d from X times X to the real numbers. This function must "
            "satisfy three axioms. First, the distance between two points "
            "is zero if and only if the points are the same. Second, "
            "distance is symmetric. Third, the triangle inequality holds.",
            duration=60,
        )
        self.ly.section_divider("1", "Metric Spaces")

        self.ly.title("Definition of a Metric", color=PRIMARY)
        axioms = [
            MathTex(r"d(x, y) \geq 0, \; d(x, y) = 0 \iff x = y", color=WHITE),
            MathTex(r"d(x, y) = d(y, x)", color=WHITE),
            MathTex(r"d(x, z) \leq d(x, y) + d(y, z)", color=ACCENT),
        ]
        labels = [
            Text("Non-negativity + identity", font_size=LABEL_SIZE, color=DIM, font=SANS),
            Text("Symmetry", font_size=LABEL_SIZE, color=DIM, font=SANS),
            Text("Triangle inequality", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ]
        items = []
        for axiom, label in zip(axioms, labels):
            pair = VGroup(axiom, label).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            items.append(pair)
        self.ly.progressive_reveal(
            items, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=1.0, wait_time=1.0,
        )
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 3: Metric Induces a Topology ~60s

    def scene3_metric_topology(self):
        self.add_subcaption(
            "Every metric space has a natural topology. The open balls "
            "form a basis. An open ball centered at x with radius r "
            "contains all points within distance r of x. The metric "
            "topology is always Hausdorff, first countable, and normal.",
            duration=60,
        )
        self.ly.section_divider("2", "Metric Topology")

        self.ly.title("Open Balls", color=PRIMARY)
        ball_def = MathTex(
            r"B(x, r) = \{y \in X : d(x, y) < r\}",
        )
        ball_def.set_color(ACCENT)
        self.ly.center_in_content(ball_def)
        self.play(Write(ball_def), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        # Visual: open balls
        self.ly.title("Open Balls Form a Basis", color=SECONDARY)
        center = Dot(ORIGIN, radius=0.06, color=WHITE)
        ball1 = Circle(radius=1.5, color=PRIMARY, fill_opacity=0.08, stroke_width=2)
        ball2 = Circle(radius=1.0, color=SECONDARY, fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 0.8 + UP * 0.4)
        ball3 = Circle(radius=0.8, color=ACCENT, fill_opacity=0.08, stroke_width=2).move_to(LEFT * 1.0 + DOWN * 0.3)
        vis = VGroup(center, ball1, ball2, ball3)
        self.ly.center_in_content(vis)
        self.play(
            FadeIn(center), FadeIn(ball1),
            FadeIn(ball2), FadeIn(ball3),
            run_time=NORMAL,
        )
        self.wait(1.0)
        props = Text("Metric topology is always Hausdorff and first-countable", font_size=BODY_SIZE, color=ACCENT, font=SANS)
        props.next_to(vis, DOWN, buff=0.5)
        self.play(FadeIn(props, shift=UP * 0.15), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 4: Examples and Non-Examples ~60s

    def scene4_examples(self):
        self.add_subcaption(
            "The standard Euclidean metric on R^n gives the usual "
            "topology. The discrete metric, where every distinct pair "
            "has distance one, gives the discrete topology. But the "
            "cofinite topology on an infinite set cannot come from any "
            "metric. It is not Hausdorff, and every metric space is "
            "Hausdorff.",
            duration=60,
        )
        self.ly.section_divider("3", "Examples & Non-Examples")

        self.ly.title("Metric Topologies", color=SECONDARY)
        examples = [
            Text("R^n with Euclidean distance", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Discrete metric: d(x,y) = 1 if x != y", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("L^p spaces with ||f - g||_p", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(
            examples, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()

        self.ly.title("Non-Metrizable Example", color=RED)
        non_ex = [
            Text("Cofinite topology on infinite set", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Not Hausdorff (any two nonempty opens overlap)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Every metric space IS Hausdorff", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD),
            Text("=> Cofinite topology is NOT metrizable", font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(
            non_ex, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 5: Metrization Theorem ~70s

    def scene5_metrization(self):
        self.add_subcaption(
            "Urysohn's Metrization Theorem gives necessary and sufficient "
            "conditions for a topological space to be metrizable. A space "
            "is metrizable if and only if it is regular, second countable, "
            "and T1. This uses Urysohn's lemma to construct an embedding "
            "into a countable product of intervals, which is metrizable.",
            duration=70,
        )
        self.ly.section_divider("4", "Urysohn's Metrization Theorem")

        self.ly.title("Urysohn's Metrization Theorem", color=ACCENT)
        statement = MathTex(
            r"X \text{ is metrizable} \iff X \text{ is } T_3 + T_1 + \text{ second countable}",
        )
        statement.set_color(WHITE)
        self.ly.center_in_content(statement)
        self.play(Write(statement), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        self.ly.title("Breaking It Down", color=PRIMARY)
        parts = [
            Text("T3 + T1: regular and points are closed", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Second countable: countable basis", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("=> Embed X into [0,1]^N (Hilbert cube)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("[0,1]^N is metrizable => X is metrizable", font_size=BODY_SIZE, color=WHITE, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(
            parts, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=1.0,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 6: Summary ~40s

    def scene6_summary(self):
        self.add_subcaption(
            "A metric measures distance and induces a topology via open "
            "balls. Not every topology comes from a metric. Urysohn's "
            "Metrization Theorem says that a space is metrizable precisely "
            "when it is regular, second countable, and T1. Most spaces "
            "encountered in analysis ARE metrizable.",
            duration=40,
        )
        self.ly.section_divider("5", "Summary")

        self.ly.title("Metric Spaces Recap", color=ACCENT)
        recap = [
            Text("Metric => topology via open balls", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Metric spaces are always Hausdorff", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Not every topology is metrizable", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Urysohn: metrizable <=> T3 + T1 + 2nd countable", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            recap, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()
        play_outro(self, next_video="Completeness and Completion", next_playlist="Topology")
