"""
Video 139: Introduction to Topology -- Topology Playlist
TEMPLATE v2 -- Professional quality Manim script

Playlist: Topology (Video 1 of 12)
Class: Video139_IntroductionTopology

Topics: What is topology, continuous deformation, metric spaces vs topological
         spaces, topological space definition (open sets, three axioms),
         examples (standard, discrete, trivial), continuity in topological terms,
         homeomorphisms, topological equivalence.

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


class Video139_IntroductionTopology(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_metric_to_topology()
        self.scene3_definition()
        self.scene4_examples()
        self.scene5_continuity()
        self.scene6_homeomorphisms()
        self.scene7_summary()

    # --- Scene 1: Hook -- "The Mathematics of Shape" ~55s

    def scene1_hook(self):
        self.add_subcaption(
            "What does a coffee mug have in common with a donut? "
            "At first, nothing. But to a topologist, they are the same "
            "shape. You can stretch a donut into a coffee mug without "
            "tearing it or gluing anything together. Topology studies "
            "properties that survive continuous deformation. We can "
            "stretch, bend, and twist, but we can never tear or glue. "
            "This is the first video in our new Topology playlist.",
            duration=55,
        )
        play_intro(self, "Introduction to Topology", "Topology")

        # The classic question
        question = Text(
            "Coffee mug = donut?",
            font_size=TITLE_SIZE, color=WHITE, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(question)
        self.play(Write(question), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        # Visual: circle and blob connected by arrow
        circle = Circle(radius=0.8, color=SECONDARY, stroke_width=3)
        self.ly.center_in_content(circle)
        self.play(Create(circle), run_time=NORMAL)

        # Blob shape (irregular)
        blob = VMobject(color=ACCENT, stroke_width=3)
        blob_points = [
            [1.0, 0.3, 0], [1.4, 1.2, 0], [0.7, 2.0, 0],
            [-0.3, 2.1, 0], [-1.1, 1.5, 0], [-1.3, 0.5, 0],
            [-0.8, -0.2, 0], [0.0, -0.4, 0], [0.6, -0.1, 0],
        ]
        blob.set_points_smoothly([np.array(p) for p in blob_points])
        blob.next_to(circle, RIGHT, buff=2.0)
        ensure_fits(blob)
        clamp_position(blob)
        self.play(Create(blob), run_time=NORMAL)

        # Wavy arrow connecting them
        arrow_path = VMobject(color=PRIMARY, stroke_width=2)
        arrow_path.set_points_smoothly([
            circle.get_center() + RIGHT * 1.0,
            circle.get_center() + RIGHT * 1.3 + UP * 0.3,
            (circle.get_center() + blob.get_center()) / 2 + UP * 0.5,
            blob.get_center() + LEFT * 1.3 - UP * 0.2,
            blob.get_center() + LEFT * 1.0,
        ])
        self.play(Create(arrow_path), run_time=NORMAL)

        # Label
        label = Text(
            "no tearing!",
            font_size=LABEL_SIZE, color=PRIMARY, font=SANS,
        )
        label.next_to(arrow_path, UP, buff=0.15)
        clamp_position(label)
        self.play(Write(label), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Key idea
        idea = Text(
            "Topology studies properties that",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(idea)
        self.play(FadeIn(idea, shift=LEFT * 0.15), run_time=FAST)

        idea2 = Text(
            "survive continuous deformation",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(idea2, DOWN, anchor=idea, buff=0.3)
        self.play(FadeIn(idea2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Rules of deformation
        rules = [
            Text("Stretch  ✓", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Bend    ✓", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Twist   ✓", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Tear    ✗", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Glue    ✗", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        rules_title = self.ly.title("The Rules")
        self.ly.progressive_reveal(rules, start_from=rules_title)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: From Metric Spaces to Topology ~65s

    def scene2_metric_to_topology(self):
        self.add_subcaption(
            "We have already studied metric spaces in Real Analysis. "
            "A metric gives us a notion of distance, and from distance "
            "we define open sets: an open ball centered at x with radius "
            "r. Every metric space has a natural topology: the collection "
            "of all open sets. But what if we want to study spaces where "
            "there is no natural distance? What if we want to study "
            "convergence, continuity, and closeness without a metric? "
            "Topology abstracts away the distance and keeps only the "
            "structure of open sets.",
            duration=65,
        )
        self.ly.section_divider(1, "From Metric Spaces to Topology")

        # We've studied metric spaces
        title = Text(
            "We studied metric spaces in Real Analysis",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(title)
        self.play(FadeIn(title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        self.ly.clear()

        # Standard distance on R
        metric = MathTex(
            r"d(x, y) = |x - y|",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(metric)
        self.play(Write(metric), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        # From distance to open sets
        step1 = Text(
            "Distance → open balls → open sets",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.center_in_content(step1)
        self.play(FadeIn(step1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        self.ly.clear()

        # Open ball visualization on number line
        line = NumberLine(
            x_range=[-2, 4, 1], length=8,
            color=DIM, include_numbers=True,
            font_size=LABEL_SIZE,
        )
        self.ly.center_in_content(line)
        self.play(Create(line), run_time=NORMAL)
        self.wait(0.5)

        # Point
        dot = Dot(line.n2p(1), color=ACCENT, radius=0.06)
        self.play(FadeIn(dot), run_time=FAST)

        # Open ball (shaded region) — use a rectangle to represent interval
        ball_left = line.n2p(0)
        ball_right = line.n2p(2)
        ball_region = Rectangle(
            width=ball_right[0] - ball_left[0],
            height=0.8,
            color=SECONDARY, fill_opacity=0.25, stroke_width=0,
        )
        ball_region.move_to(line.n2p(1))
        self.play(FadeIn(ball_region), run_time=NORMAL)

        ball_label = MathTex(
            r"B(1,\, 1)", font_size=BODY_SIZE, color=SECONDARY,
        )
        ball_label.next_to(ball_region, UP, buff=0.2)
        clamp_position(ball_label)
        self.play(Write(ball_label), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # The key question
        question = Text(
            "What if there is no natural distance?",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(question)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        question2 = Text(
            "Keep the open sets, drop the metric.",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(question2, DOWN, anchor=question, buff=0.4)
        self.play(FadeIn(question2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 3: The Definition of a Topological Space ~60s

    def scene3_definition(self):
        self.add_subcaption(
            "A topological space is a set X together with a collection "
            "tau of subsets of X, called open sets. This collection "
            "must satisfy three axioms. First: the set X itself and the "
            "empty set are both open. Second: the union of any collection "
            "of open sets is open. This can be an infinite union. Third: "
            "the intersection of any finite collection of open sets is "
            "open. Note: only finite intersections. Infinite intersections "
            "can break things. The pair of X and tau is called a "
            "topological space, and tau is called the topology of X.",
            duration=60,
        )
        self.ly.section_divider(2, "Definition: Topological Space")

        # Definition
        defn_title = Text(
            "A topological space",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(defn_title)
        self.play(Write(defn_title), run_time=FAST)
        self.wait(1)

        defn_body = Text(
            "A set X with a collection τ of subsets",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(defn_body, DOWN, anchor=defn_title, buff=0.3)
        self.play(FadeIn(defn_body, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        self.ly.clear()

        # Three axioms
        axioms_title = self.ly.title("Three Axioms")
        self.wait(1)

        axioms = [
            Text("1. ∅ and X are in τ", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("2. Union of any subcollection of τ is in τ", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("3. Intersection of FINITE subcollection of τ is in τ", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(axioms, start_from=axioms_title)
        self.wait(4)

        self.ly.clear()

        # Key note about finite
        note = Text(
            "Only finite intersections are guaranteed!",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(note)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        note2 = Text(
            "Infinite intersections can produce non-open sets",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note2, DOWN, anchor=note, buff=0.3)
        self.play(FadeIn(note2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 4: Examples of Topological Spaces ~65s

    def scene4_examples(self):
        self.add_subcaption(
            "Let us look at three examples of topologies on the same "
            "set. First, the standard topology on R. The open sets are "
            "arbitrary unions of open intervals. This is the topology "
            "we get from the usual metric. Second, the discrete topology "
            "on any set X. Every subset of X is open. Every point is "
            "isolated. Third, the trivial topology. Only two open sets: "
            "the empty set and X itself. This is the coarsest possible "
            "topology. Same set, three wildly different topologies.",
            duration=65,
        )
        self.ly.section_divider(3, "Examples of Topologies")

        # Same set, different topologies
        header = Text(
            "Same set X — three different topologies:",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(header)
        self.play(FadeIn(header, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        self.ly.clear()

        # Example 1: Standard topology
        ex1_title = Text(
            "Standard topology on R",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(ex1_title)
        self.play(FadeIn(ex1_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        ex1_desc = [
            Text("Open sets = unions of open intervals", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("From the usual metric d(x,y) = |x-y|", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(ex1_desc, start_from=ex1_title)
        self.wait(3)

        self.ly.clear()

        # Example 2: Discrete topology
        ex2_title = Text(
            "Discrete topology",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(ex2_title)
        self.play(FadeIn(ex2_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        ex2_desc = [
            Text("τ = all subsets of X", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Every set is open — every point isolated", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(ex2_desc, start_from=ex2_title)
        self.wait(3)

        self.ly.clear()

        # Example 3: Trivial topology
        ex3_title = Text(
            "Trivial topology",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(ex3_title)
        self.play(FadeIn(ex3_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        ex3_desc = [
            Text("τ = {∅, X}", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Only two open sets — the coarsest possible", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(ex3_desc, start_from=ex3_title)
        self.wait(5)

        self.ly.clear()

        # Comparison insight
        insight = Text(
            "Standard: rich structure    Trivial: almost no structure",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        box = self.ly.formula_box(insight, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 5: Continuity in Topological Terms ~60s

    def scene5_continuity(self):
        self.add_subcaption(
            "In calculus and Real Analysis, continuity was defined "
            "using epsilon and delta. For every epsilon, there exists "
            "a delta such that if x is within delta of a, then f of x "
            "is within epsilon of f of a. But topology gives us a more "
            "powerful definition. A function f from X to Y is continuous "
            "if the preimage of every open set is open. That is, if U "
            "is open in Y, then the preimage f inverse of U is open in "
            "X. This definition works without any metric! It captures "
            "the essence of continuity: nearby points map to nearby points.",
            duration=60,
        )
        self.ly.section_divider(4, "Continuity in Topological Terms")

        # Epsilon-delta回忆
        eps_delta = Text(
            "In Real Analysis: ε-δ definition",
            font_size=HEADING_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(eps_delta)
        self.play(FadeIn(eps_delta, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        self.ly.clear()

        # Topological definition
        topo_def_title = Text(
            "Topological definition:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(topo_def_title)
        self.play(FadeIn(topo_def_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        # The formula
        formula = MathTex(
            r"U \text{ open in } Y",
            r"\;\Longrightarrow\;",
            r"f^{-1}(U) \text{ open in } X",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([SECONDARY, DIM, ACCENT]):
            if i < len(formula):
                formula[i].set_color(col)
        box = self.ly.formula_box(formula, color=ACCENT)
        self.ly.safe_place(box, DOWN, anchor=topo_def_title, buff=0.4)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Why this is powerful
        why = [
            Text("No metric required!", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Works for any topological space", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Captures: nearby points → nearby points", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        why_title = self.ly.title("Why This Is Powerful")
        self.ly.progressive_reveal(why, start_from=why_title)
        self.wait(5)

        self.ly.clear()

    # --- Scene 6: Homeomorphisms ~60s

    def scene6_homeomorphisms(self):
        self.add_subcaption(
            "In topology, a homeomorphism is an isomorphism of "
            "topological spaces. A function f from X to Y is a "
            "homeomorphism if f is continuous, bijective, and its "
            "inverse f inverse is also continuous. A homeomorphism is "
            "a continuous deformation. You can stretch but never tear "
            "or glue. The coffee mug and donut are homeomorphic. This "
            "is what the famous joke means. Homeomorphic spaces are "
            "topologically the same. They share all topological "
            "properties.",
            duration=60,
        )
        self.ly.section_divider(5, "Homeomorphisms")

        # Definition
        title = Text(
            "Homeomorphism: the topology isomorphism",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(title)
        self.play(FadeIn(title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        # Conditions
        conditions = [
            Text("f is continuous", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("f is bijective (one-to-one and onto)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("f^{-1} is also continuous", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(conditions, start_from=title)
        self.wait(4)

        self.ly.clear()

        # Visual: two spaces connected
        space_x = MathTex(r"X", font_size=HEADING_SIZE, color=SECONDARY)
        space_y = MathTex(r"Y", font_size=HEADING_SIZE, color=ACCENT)
        left_col = VGroup(space_x)
        right_col = VGroup(space_y)

        # Arrow f
        arrow_f = MathTex(
            r"\xrightarrow{f}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        # Arrow f^{-1}
        arrow_inv = MathTex(
            r"\xleftarrow{f^{-1}}",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        pair_f = VGroup(space_x, arrow_f, space_y).arrange(RIGHT, buff=0.5)
        pair_inv = VGroup(space_y, arrow_inv, space_x).arrange(RIGHT, buff=0.5)

        self.ly.center_in_content(pair_f)
        self.play(Write(pair_f), run_time=NORMAL)
        self.wait(1)

        self.ly.safe_place(pair_inv, DOWN, anchor=pair_f, buff=0.5)
        self.play(Write(pair_inv), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Coffee mug = donut payoff
        payoff_title = Text(
            "The famous joke, explained:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(payoff_title)
        self.play(FadeIn(payoff_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        payoff = Text(
            "Coffee mug and donut are homeomorphic!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(payoff, DOWN, anchor=payoff_title, buff=0.4)
        self.play(FadeIn(payoff, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        meaning = Text(
            "They share all topological properties",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(meaning, DOWN, anchor=payoff, buff=0.3)
        self.play(FadeIn(meaning, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 7: Summary and Preview ~45s

    def scene7_summary(self):
        self.add_subcaption(
            "Let us recap what we have learned. We started with "
            "deformation: the coffee mug and the donut are the same "
            "in topology. We saw how topology generalizes metric spaces "
            "by keeping open sets and dropping the distance. A "
            "topological space is a set with a collection of open sets "
            "satisfying three axioms. We explored three examples: "
            "standard, discrete, and trivial. Continuity became: "
            "preimages of open sets are open. And homeomorphisms tell "
            "us when two spaces are topologically equivalent. Next "
            "time: connectedness.",
            duration=45,
        )
        self.ly.section_divider(6, "Summary")

        title = self.ly.title("What We Learned")
        self.wait(1)

        points = [
            Text("Topology: properties surviving deformation", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Generalizes metric spaces → keeps open sets", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("3 axioms: ∅, X ∈ τ; unions open; finite intersections open", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Continuity: f^{-1}(open) = open", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Homeomorphism = continuous isomorphism", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        self.wait(4)

        self.ly.clear()

        # Preview
        preview = Text(
            "Next: Connectedness",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(preview)
        self.play(FadeIn(preview, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        preview2 = Text(
            "Can we split a space into two open parts?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(preview2, DOWN, anchor=preview, buff=0.3)
        self.play(FadeIn(preview2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()
        play_outro(self, "", "Topology")
