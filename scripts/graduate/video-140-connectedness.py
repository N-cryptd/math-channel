"""
Video 140: Connectedness -- Topology Playlist
TEMPLATE v2 -- Professional quality Manim script

Playlist: Topology (Video 7 of 12)
Class: Video140_Connectedness

Topics: Connectedness definition, connected vs disconnected spaces,
         connected components, path-connectedness, the topologist's sine curve,
         relationship: path-connected => connected (converse fails).

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


class Video140_Connectedness(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_examples()
        self.scene4_components()
        self.scene5_path_connected()
        self.scene6_sine_curve()
        self.scene7_summary()

    # --- Scene 1: Hook -- "Can You Walk From Here to There?" ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "What does it mean for a space to be in one piece? "
            "Imagine you are standing on the number line at the point "
            "zero point five. Your friend is at two point five. Can you "
            "walk from where you are to where they are without jumping? "
            "On the whole real line, yes. But what about the space made "
            "of two separate intervals, zero to one and two to three? "
            "There is a gap between them. You would have to jump. "
            "This is the core idea of connectedness.",
            duration=50,
        )
        play_intro(self, "Connectedness", "Topology")

        # Walking metaphor on number line
        line = NumberLine(
            x_range=[-0.5, 4, 1], length=9,
            color=DIM, include_numbers=True, font_size=LABEL_SIZE,
        )
        self.ly.center_in_content(line)
        self.play(Create(line), run_time=NORMAL)
        self.wait(0.5)

        # Two intervals
        interval_a = line.copy().set_color(SECONDARY)
        interval_a = Line(line.n2p(0), line.n2p(1), color=SECONDARY, stroke_width=6)
        interval_b = Line(line.n2p(2), line.n2p(3), color=SECONDARY, stroke_width=6)
        self.play(Create(interval_a), run_time=FAST)
        self.play(Create(interval_b), run_time=FAST)

        # Dots
        dot_a = Dot(line.n2p(0.5), color=ACCENT, radius=0.06)
        dot_b = Dot(line.n2p(2.5), color=ACCENT, radius=0.06)
        self.play(FadeIn(dot_a), FadeIn(dot_b), run_time=FAST)

        # Gap label
        gap_label = Text(
            "Gap! Cannot walk across.",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        gap_label.move_to(UP * 2.2)
        ensure_fits(gap_label)
        clamp_position(gap_label)
        self.play(FadeIn(gap_label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Key question
        question = Text(
            "Can you walk from here to there?",
            font_size=TITLE_SIZE, color=WHITE, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(question)
        self.play(Write(question), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        # The core idea
        idea1 = Text(
            "Some spaces can be split into two pieces.",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.center_in_content(idea1)
        self.play(FadeIn(idea1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        self.ly.clear()

        idea2 = Text(
            "Others cannot.",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.center_in_content(idea2)
        self.play(FadeIn(idea2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        self.ly.clear()

        idea3 = Text(
            "Connectedness captures this distinction.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(idea3)
        self.play(FadeIn(idea3, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: Formal Definition of Connectedness ~60s

    def scene2_definition(self):
        self.add_subcaption(
            "A topological space X is connected if it cannot be written "
            "as the union of two disjoint non-empty open sets. Equivalently, "
            "there is no non-empty proper subset of X that is both open "
            "and closed. Such a set is called clopen. The intuition is: "
            "you cannot partition the space into two separated pieces "
            "using open sets. The whole space hangs together.",
            duration=60,
        )
        self.ly.section_divider(1, "Definition: Connectedness")

        # Informal definition first
        informal = Text(
            "A space is connected if it",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(informal)
        self.play(FadeIn(informal, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        informal2 = Text(
            "cannot be split into two open pieces.",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(informal2, DOWN, anchor=informal, buff=0.3)
        self.play(FadeIn(informal2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Formal definition
        def_title = Text(
            "Formal definition",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(def_title)
        self.play(FadeIn(def_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        formula = MathTex(
            r"X", r"\text{ is connected }",
            r"\;\Longleftrightarrow\;",
            r"\nexists\; \emptyset \subsetneq U \subsetneq X",
            r"\text{: } U \text{ is clopen}",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, DIM, DIM, SECONDARY, ACCENT]):
            if i < len(formula):
                formula[i].set_color(col)
        box = self.ly.formula_box(formula, color=ACCENT)
        self.ly.safe_place(box, DOWN, anchor=def_title, buff=0.4)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Clopen concept
        clopen_title = Text(
            "Clopen = both Open and Closed",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(clopen_title)
        self.play(FadeIn(clopen_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        clopen_items = [
            Text("No proper clopen set exists", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("The space cannot be partitioned", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(clopen_items, start_from=clopen_title)
        self.wait(5)

        self.ly.clear()

        # Visual: connected vs disconnected
        vs_title = self.ly.title("Connected vs Disconnected")
        self.wait(0.5)

        # Connected blob
        conn_blob = Circle(radius=1.0, color=SECONDARY, stroke_width=3, fill_opacity=0.15)
        conn_label = Text("Connected", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        conn_label.next_to(conn_blob, DOWN, buff=0.2)
        conn_group = VGroup(conn_blob, conn_label)
        conn_group.move_to(LEFT * 3 + DOWN * 0.8)
        clamp_position(conn_group)
        self.play(FadeIn(conn_group), run_time=NORMAL)

        # Disconnected: two blobs with gap
        disc1 = Circle(radius=0.7, color=RED, stroke_width=3, fill_opacity=0.15)
        disc2 = Circle(radius=0.7, color=RED, stroke_width=3, fill_opacity=0.15)
        disc2.next_to(disc1, RIGHT, buff=1.2)
        disc_label = Text("Disconnected", font_size=BODY_SIZE, color=RED, font=SANS)
        disc_group = VGroup(disc1, disc2, disc_label)
        disc_label.next_to(VGroup(disc1, disc2), DOWN, buff=0.2)
        disc_group.move_to(RIGHT * 3 + DOWN * 0.8)
        clamp_position(disc_group)
        self.play(FadeIn(disc_group), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 3: Examples ~70s

    def scene3_examples(self):
        self.add_subcaption(
            "Let us look at four examples. First, the closed interval "
            "zero one is connected. Any attempt to split it with open sets "
            "fails. Second, the union of zero one and two three is "
            "disconnected. The gap between them is a natural split. Third, "
            "the entire real line R is connected. You cannot partition it "
            "into two non-empty open subsets. Fourth, the rational numbers Q "
            "with the subspace topology are disconnected. Take any irrational "
            "number, like root two. The rationals less than root two form an "
            "open set, and the rationals greater than root two form another.",
            duration=70,
        )
        self.ly.section_divider(2, "Examples")

        # Example 1: [0,1]
        ex1_title = Text(
            "[0, 1] is connected",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(ex1_title)
        self.play(FadeIn(ex1_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        # Draw interval
        line1 = NumberLine(
            x_range=[-0.5, 1.5, 0.5], length=7,
            color=DIM, include_numbers=True, font_size=LABEL_SIZE,
        )
        interval_01 = Line(line1.n2p(0), line1.n2p(1), color=SECONDARY, stroke_width=6)
        # Endpoints
        dot0 = Dot(line1.n2p(0), color=SECONDARY, radius=0.05)
        dot1 = Dot(line1.n2p(1), color=SECONDARY, radius=0.05)
        group1 = VGroup(line1, interval_01, dot0, dot1)
        self.ly.center_in_content(group1)
        self.play(Create(line1), run_time=FAST)
        self.play(Create(interval_01), run_time=FAST)
        self.play(FadeIn(dot0), FadeIn(dot1), run_time=FAST)
        self.wait(2)

        reason1 = Text(
            "No open partition splits [0,1]",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(reason1, DOWN, anchor=group1, buff=0.3)
        self.play(FadeIn(reason1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Example 2: (0,1) ∪ (2,3)
        ex2_title = Text(
            "(0,1) ∪ (2,3) is disconnected",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(ex2_title)
        self.play(FadeIn(ex2_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        line2 = NumberLine(
            x_range=[-0.5, 4, 1], length=8,
            color=DIM, include_numbers=True, font_size=LABEL_SIZE,
        )
        int_a = Line(line2.n2p(0), line2.n2p(1), color=RED, stroke_width=6)
        int_b = Line(line2.n2p(2), line2.n2p(3), color=RED, stroke_width=6)
        group2 = VGroup(line2, int_a, int_b)
        self.ly.center_in_content(group2)
        self.play(Create(line2), run_time=FAST)
        self.play(Create(int_a), run_time=FAST)
        self.play(Create(int_b), run_time=FAST)

        # Show the gap
        gap_brace = BraceBetweenPoints(
            line2.n2p(1.1), line2.n2p(1.9), direction=UP,
            color=ACCENT,
        )
        gap_text = Text("gap", font_size=SMALL_SIZE, color=ACCENT, font=SANS)
        gap_text.next_to(gap_brace, UP, buff=0.1)
        self.play(Create(gap_brace), Write(gap_text), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Example 3: R is connected
        ex3_title = Text(
            "R is connected",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(ex3_title)
        self.play(FadeIn(ex3_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        line3 = NumberLine(
            x_range=[-10, 10, 2], length=9,
            color=SECONDARY, stroke_width=4,
            include_numbers=False,
        )
        self.ly.safe_place(line3, DOWN, anchor=ex3_title, buff=0.4)
        self.play(Create(line3), run_time=NORMAL)
        self.wait(2)

        reason3 = Text(
            "The real line cannot be partitioned by open sets",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(reason3, DOWN, anchor=line3, buff=0.3)
        self.play(FadeIn(reason3, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Example 4: Q is disconnected
        ex4_title = Text(
            "Q (rationals) is disconnected",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(ex4_title)
        self.play(FadeIn(ex4_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        split_formula = MathTex(
            r"Q = (Q \cap (-\infty, \sqrt{2})) \cup (Q \cap (\sqrt{2}, \infty))",
            font_size=HEADING_SIZE, color=WHITE,
        )
        box = self.ly.formula_box(split_formula, color=RED)
        self.ly.safe_place(box, DOWN, anchor=ex4_title, buff=0.4)
        self.play(Write(box), run_time=NORMAL)
        self.wait(2)

        reason4 = Text(
            "Both parts are open in Q -- a clopen partition!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(reason4, DOWN, anchor=box, buff=0.4)
        self.play(FadeIn(reason4, shift=LEFT * 0.15), run_time=FAST)
        self.wait(6)

        self.ly.clear()

    # --- Scene 4: Connected Components ~50s

    def scene4_components(self):
        self.add_subcaption(
            "Every topological space can be broken into maximal "
            "connected pieces called connected components. A connected "
            "component of a point x is the largest connected subset "
            "containing x. These components partition the space. Two "
            "points are in the same component if and only if they lie "
            "in some connected subset together. This is an equivalence "
            "relation.",
            duration=50,
        )
        self.ly.section_divider(3, "Connected Components")

        # Key idea
        idea = Text(
            "Every space breaks into maximal connected pieces",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(idea)
        self.play(FadeIn(idea, shift=LEFT * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Visual: space with colored components
        # Create 4 blobs representing components
        blob_a = Circle(radius=0.8, color=SECONDARY, stroke_width=3, fill_opacity=0.2)
        blob_b = Circle(radius=0.6, color=ACCENT, stroke_width=3, fill_opacity=0.2)
        blob_b.move_to(RIGHT * 3 + UP * 0.5)
        blob_c = Circle(radius=0.7, color=PRIMARY, stroke_width=3, fill_opacity=0.2)
        blob_c.move_to(LEFT * 2.5 + DOWN * 1.5)
        blob_d = Circle(radius=0.5, color=RED, stroke_width=3, fill_opacity=0.2)
        blob_d.move_to(RIGHT * 2 + DOWN * 2)
        blobs = VGroup(blob_a, blob_b, blob_c, blob_d)

        # Position all blobs to be on screen
        ensure_fits(blobs)
        clamp_position(blobs)

        for b in [blob_a, blob_b, blob_c, blob_d]:
            self.play(Create(b), run_time=FAST)
        self.wait(2)

        comp_label = Text(
            "Each color = one connected component",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        comp_label.move_to(DOWN * 3)
        clamp_position(comp_label)
        self.play(FadeIn(comp_label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Definition
        def_title = Text(
            "Connected component of x",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(def_title)
        self.play(FadeIn(def_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        def_body = Text(
            "The largest connected subset containing x",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(def_body, DOWN, anchor=def_title, buff=0.3)
        self.play(FadeIn(def_body, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        equiv = Text(
            "Equivalence relation: x ~ y iff connected subset contains both",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(equiv, DOWN, anchor=def_body, buff=0.3)
        self.play(FadeIn(equiv, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # --- Scene 5: Path-Connectedness ~60s

    def scene5_path_connected(self):
        self.add_subcaption(
            "Path-connectedness is a stronger notion. A space X is "
            "path-connected if for every pair of points a and b, there "
            "exists a continuous path gamma from a to b. Formally, gamma "
            "is a continuous function from the unit interval zero one "
            "into X, with gamma of zero equals a and gamma of one equals b. "
            "The key theorem is that every path-connected space is connected. "
            "The converse is false, as we will see with a famous counterexample.",
            duration=60,
        )
        self.ly.section_divider(4, "Path-Connectedness")

        # Motivation
        moto = Text(
            "A stronger notion: can you draw a path?",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(moto)
        self.play(FadeIn(moto, shift=LEFT * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Definition with formula
        def_title = Text(
            "Definition",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(def_title)
        self.play(FadeIn(def_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        path_formula = MathTex(
            r"\gamma : [0,1] \to X",
            r"\;\text{ continuous}",
            font_size=HEADING_SIZE,
        )
        path_formula[0].set_color(ACCENT)
        path_formula[1].set_color(DIM)
        box1 = self.ly.formula_box(path_formula, color=ACCENT)
        self.ly.safe_place(box1, DOWN, anchor=def_title, buff=0.4)
        self.play(Write(box1), run_time=NORMAL)
        self.wait(2)

        endpoints = MathTex(
            r"\gamma(0) = a",
            r"\qquad",
            r"\gamma(1) = b",
            font_size=HEADING_SIZE,
        )
        endpoints[0].set_color(ACCENT)
        endpoints[2].set_color(ACCENT)
        endpoints[1].set_color(DIM)
        self.ly.safe_place(endpoints, DOWN, anchor=box1, buff=0.4)
        self.play(Write(endpoints), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Animated path visualization
        path_title = Text(
            "Any two points connected by a path",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(path_title)
        self.play(FadeIn(path_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        # Start and end points
        point_a = Dot(LEFT * 3, color=ACCENT, radius=0.08)
        point_b = Dot(RIGHT * 3, color=ACCENT, radius=0.08)
        label_a = Text("a", font_size=BODY_SIZE, color=ACCENT, font=MONO)
        label_a.next_to(point_a, DOWN, buff=0.15)
        label_b = Text("b", font_size=BODY_SIZE, color=ACCENT, font=MONO)
        label_b.next_to(point_b, DOWN, buff=0.15)

        self.play(FadeIn(point_a), FadeIn(point_b), run_time=FAST)
        self.play(Write(label_a), Write(label_b), run_time=FAST)

        # Draw a curvy path
        path_curve = VMobject(color=SECONDARY, stroke_width=3)
        t_vals = np.linspace(0, 1, 100)
        path_points = []
        for t in t_vals:
            x_val = -3 + 6 * t
            y_val = np.sin(t * 2 * PI) * 0.8 - 1.5
            path_points.append([x_val, y_val, 0])
        path_curve.set_points_smoothly(path_points)
        ensure_fits(path_curve)
        clamp_position(path_curve)
        self.play(Create(path_curve), run_time=3)
        self.wait(4)

        self.ly.clear()

        # Key theorem
        theorem_title = self.ly.title("Key Theorem")
        self.wait(0.5)

        theorem_formula = MathTex(
            r"\text{path-connected}",
            r"\;\Longrightarrow\;",
            r"\text{connected}",
            font_size=HEADING_SIZE,
        )
        theorem_formula[0].set_color(ACCENT)
        theorem_formula[1].set_color(DIM)
        theorem_formula[2].set_color(SECONDARY)
        box2 = self.ly.formula_box(theorem_formula, color=SECONDARY)
        self.ly.safe_place(box2, DOWN, anchor=theorem_title, buff=0.5)
        self.play(Write(box2), run_time=NORMAL)
        self.wait(2)

        converse = Text(
            "Converse is FALSE -- next example!",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(converse, DOWN, anchor=box2, buff=0.4)
        self.play(FadeIn(converse, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # --- Scene 6: The Topologist's Sine Curve ~70s

    def scene6_sine_curve(self):
        self.add_subcaption(
            "Now for the star of the show. The topologist's sine curve "
            "is the set of all points x comma sin of one over x where x "
            "is strictly positive, together with the vertical segment "
            "from zero comma negative one to zero comma one. The curve "
            "oscillates infinitely as x approaches zero from the right. "
            "The whole set is connected, because the vertical segment is "
            "in the closure of the curve. But it is not path-connected. "
            "There is no continuous path from a point on the vertical "
            "segment to a point on the curve itself.",
            duration=70,
        )
        self.ly.section_divider(5, "A Remarkable Example")

        # Title of the example
        example_title = Text(
            "The Topologist's Sine Curve",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(example_title)
        self.play(FadeIn(example_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        self.ly.clear()

        # Formula
        formula_title = Text(
            "Definition",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(formula_title)
        self.play(FadeIn(formula_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        sine_formula = MathTex(
            r"S = \{(x, \sin\tfrac{1}{x}) : x > 0\} \cup \{(0,y) : -1 \le y \le 1\}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        ensure_fits(sine_formula)
        self.ly.safe_place(sine_formula, DOWN, anchor=formula_title, buff=0.4)
        self.play(Write(sine_formula), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Draw the curve
        axes = Axes(
            x_range=[-0.5, 5, 1],
            y_range=[-1.5, 1.5, 0.5],
            x_length=7,
            y_length=4,
            color=DIM,
        )
        self.ly.center_in_content(axes)
        self.play(Create(axes), run_time=NORMAL)
        self.wait(0.5)

        # Draw sin(1/x) for x in [0.05, 5] — oscillates near 0
        sine_points = []
        x_vals = np.linspace(0.05, 5, 2000)
        for x_val in x_vals:
            y_val = np.sin(1.0 / x_val)
            sine_points.append(axes.c2p(x_val, y_val))

        sine_curve = VMobject(color=SECONDARY, stroke_width=2.5)
        sine_curve.set_points_smoothly(sine_points)
        ensure_fits(sine_curve)
        clamp_position(sine_curve)
        self.play(Create(sine_curve), run_time=4)
        self.wait(2)

        # Vertical segment at x=0
        vert_segment = Line(
            axes.c2p(0, -1), axes.c2p(0, 1),
            color=ACCENT, stroke_width=3,
        )
        self.play(Create(vert_segment), run_time=NORMAL)
        self.wait(2)

        # Labels
        curve_label = Text(
            "sin(1/x), x > 0",
            font_size=SMALL_SIZE, color=SECONDARY, font=SANS,
        )
        curve_label.next_to(sine_curve, RIGHT, buff=0.15)
        clamp_position(curve_label)
        self.play(Write(curve_label), run_time=FAST)

        vert_label = Text(
            "vertical segment",
            font_size=SMALL_SIZE, color=ACCENT, font=SANS,
        )
        vert_label.next_to(vert_segment, LEFT, buff=0.15)
        clamp_position(vert_label)
        self.play(Write(vert_label), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Key result
        key1 = Text(
            "This set is CONNECTED",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(key1)
        self.play(FadeIn(key1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        reason = Text(
            "The vertical segment is in the closure of the curve",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(reason, DOWN, anchor=key1, buff=0.3)
        self.play(FadeIn(reason, shift=LEFT * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        key2 = Text(
            "But NOT path-connected",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(key2)
        self.play(FadeIn(key2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        why = Text(
            "No continuous path from the vertical segment to the curve",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(why, DOWN, anchor=key2, buff=0.3)
        self.play(FadeIn(why, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        intuition = Text(
            "Would need infinite oscillation in finite time",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(intuition, DOWN, anchor=why, buff=0.3)
        self.play(FadeIn(intuition, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 7: Summary ~40s

    def scene7_summary(self):
        self.add_subcaption(
            "Let us recap. A space is connected if it cannot be split "
            "into two non-empty open sets. A space is path-connected "
            "if any two points can be joined by a continuous path. "
            "Every path-connected space is connected, but the topologist's "
            "sine curve shows the converse is false. Connected components "
            "are the maximal connected pieces of a space. Next time, we "
            "study separation axioms.",
            duration=40,
        )
        self.ly.section_divider(6, "Summary")

        # Summary items
        summary_title = self.ly.title("Key Takeaways")
        self.wait(0.5)

        items = [
            Text("Connected: no clopen partition", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Path-connected: continuous path between any two points", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("path-connected => connected (not conversely!)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Connected components = maximal connected subsets", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=summary_title)
        self.wait(4)

        self.ly.clear()

        # The big relationship
        rel_formula = MathTex(
            r"\text{path-connected}",
            r"\;\Longrightarrow\;",
            r"\text{connected}",
            r"\;\not\!\Longleftrightarrow\;",
            font_size=HEADING_SIZE,
        )
        rel_formula[0].set_color(ACCENT)
        rel_formula[1].set_color(DIM)
        rel_formula[2].set_color(SECONDARY)
        rel_formula[3].set_color(RED)
        box = self.ly.formula_box(rel_formula, color=RED)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(3)

        counterex = Text(
            "Counterexample: topologist's sine curve",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(counterex, DOWN, anchor=box, buff=0.4)
        self.play(FadeIn(counterex, shift=LEFT * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        play_outro(self)
