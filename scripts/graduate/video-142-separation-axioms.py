"""
Video 142: Separation Axioms (Hausdorff) -- Topology Playlist
TEMPLATE v2 -- Professional quality Manim script

Playlist: Topology (Video 7 of 12)
Class: Video142_SeparationAxioms

Topics: Separation axioms T0-T4, Kolmogorov, Frechet, Hausdorff,
         regular, normal spaces, Urysohn's lemma, separation hierarchy.

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


class Video142_SeparationAxioms(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_t0()
        self.scene3_t1()
        self.scene4_t2_hausdorff()
        self.scene5_hierarchy()
        self.scene6_normal_urysohn()
        self.scene7_summary()

    # --- Scene 1: Hook -- "How Separated Are Your Points?" ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "Consider two distinct points in a topological space. "
            "Can your topology tell them apart? In some spaces, "
            "every open set containing one point also contains the "
            "other. In better spaces, we can find disjoint "
            "neighborhoods that keep them apart. This is the "
            "world of separation axioms, a hierarchy of conditions "
            "that describe how well a topology distinguishes "
            "between points and sets.",
            duration=50,
        )
        play_intro(self, "Separation Axioms", "Topology")

        # Two points that cannot be separated
        title = self.ly.title("Can Your Topology Tell Points Apart?", color=PRIMARY)
        self.wait(0.3)

        # Show two close points on a line
        line = NumberLine(x_range=[0, 4, 1], length=9, color=DIM, include_numbers=False)
        self.ly.center_in_content(line)
        self.play(Create(line), run_time=FAST)
        self.wait(0.3)

        pt_a = Dot(line.n2p(1.8), radius=0.08, color=PRIMARY)
        pt_b = Dot(line.n2p(2.2), radius=0.08, color=SECONDARY)
        label_a = Text("x", font_size=LABEL_SIZE, color=PRIMARY, font=MONO).next_to(pt_a, UP, buff=0.15)
        label_b = Text("y", font_size=LABEL_SIZE, color=SECONDARY, font=MONO).next_to(pt_b, UP, buff=0.15)
        self.play(FadeIn(pt_a), FadeIn(pt_b), FadeIn(label_a), FadeIn(label_b), run_time=FAST)
        self.wait(0.5)

        # Overlapping neighborhoods
        u_overlap = Circle(radius=0.7, color=PRIMARY, fill_opacity=0.12, stroke_width=2).move_to(pt_a)
        v_overlap = Circle(radius=0.7, color=SECONDARY, fill_opacity=0.12, stroke_width=2).move_to(pt_b)
        bad_label = Text("Neighborhoods overlap -- cannot separate!", font_size=BODY_SIZE, color=RED, font=SANS)
        bad_label.next_to(line, DOWN, buff=0.5)
        self.play(FadeIn(u_overlap), FadeIn(v_overlap), run_time=FAST)
        self.play(FadeIn(bad_label, shift=UP * 0.15), run_time=FAST)
        self.wait(1.0)
        self.play(FadeOut(bad_label), FadeOut(u_overlap), FadeOut(v_overlap), run_time=FAST)

        # Disjoint neighborhoods (Hausdorff)
        u_sep = Circle(radius=0.55, color=PRIMARY, fill_opacity=0.15, stroke_width=2).move_to(pt_a)
        v_sep = Circle(radius=0.55, color=SECONDARY, fill_opacity=0.15, stroke_width=2).move_to(pt_b)
        good_label = Text("Disjoint neighborhoods -- Hausdorff!", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD)
        good_label.next_to(line, DOWN, buff=0.5)
        self.play(FadeIn(u_sep), FadeIn(v_sep), run_time=FAST)
        self.play(FadeIn(good_label, shift=UP * 0.15), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 2: T0 -- Kolmogorov Spaces ~50s

    def scene2_t0(self):
        self.add_subcaption(
            "The weakest separation axiom is T0, named after Kolmogorov. "
            "A space is T0 if for any two distinct points, there exists an "
            "open set containing one but not the other. The Sierpinski space "
            "is the simplest example. It has two points and a topology that "
            "contains an open set with just one point, so it is T0 but not T1.",
            duration=50,
        )
        self.ly.section_divider("1", "T0 -- Kolmogorov")

        self.ly.title("T0: Kolmogorov Space", color=PRIMARY)
        defn = MathTex(
            r"\forall x \neq y, \; \exists U \text{ open: }",
            r"x \in U, \, y \notin U",
            r"\text{ or }",
            r"y \in U, \, x \notin U",
        )
        defn[0].set_color(DIM)
        defn[1].set_color(PRIMARY)
        defn[2].set_color(DIM)
        defn[3].set_color(SECONDARY)
        self.ly.center_in_content(defn)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        self.ly.title("Example: Sierpinski Space", color=SECONDARY)
        s_items = [
            Text("X = {0, 1}", font_size=BODY_SIZE, color=WHITE, font=MONO),
            Text(r"Topology: \emptyset, {0}, {0,1}", font_size=BODY_SIZE, color=WHITE, font=MONO),
            Text("Open set {0} contains 0 but not 1", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("=> T0 (but NOT T1!)", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(
            s_items, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=1.0,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 3: T1 -- Frechet Spaces ~50s

    def scene3_t1(self):
        self.add_subcaption(
            "T1 is stronger than T0. A space is T1 if for any two distinct "
            "points, each one has a neighborhood not containing the other. "
            "This is equivalent to saying every singleton set is closed. "
            "The cofinite topology on an infinite set is T1 but not Hausdorff.",
            duration=50,
        )
        self.ly.section_divider("2", "T1 -- Frechet")

        self.ly.title("T1: Frechet Space", color=PRIMARY)
        defn = MathTex(
            r"\forall x \neq y, \; \exists U, V \text{ open:}",
            r"x \in U, \, y \notin U",
            r"\text{ and }",
            r"y \in V, \, x \notin V",
        )
        defn[0].set_color(DIM)
        defn[1].set_color(PRIMARY)
        defn[2].set_color(DIM)
        defn[3].set_color(SECONDARY)
        self.ly.center_in_content(defn)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        self.ly.title("Equivalent Characterization", color=ACCENT)
        eq = MathTex(
            r"T_1 \iff \{x\} \text{ is closed for every } x",
        )
        eq.set_color(ACCENT)
        self.ly.center_in_content(eq)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        self.ly.title("Example: Cofinite Topology", color=SECONDARY)
        cf_items = [
            Text("Open sets = complements of finite sets", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("On an infinite set X:", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Singletons are finite => complements are open", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("=> Every singleton is closed => T1", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("But any two nonempty open sets overlap!", font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(
            cf_items, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=1.0,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 4: T2 -- Hausdorff Spaces ~70s

    def scene4_t2_hausdorff(self):
        self.add_subcaption(
            "Hausdorff, also called T2, is the most commonly assumed "
            "separation axiom. It requires that any two distinct points "
            "have disjoint neighborhoods. In Hausdorff spaces, sequences "
            "have at most one limit, and compact subsets are closed. "
            "Most spaces you work with in analysis are Hausdorff, including "
            "all metric spaces and R^n.",
            duration=70,
        )
        self.ly.section_divider("3", "T2 -- Hausdorff")

        self.ly.title("T2: Hausdorff Space", color=ACCENT)
        defn = MathTex(
            r"\forall x \neq y, \; \exists U, V \text{ open, } U \cap V = \emptyset:",
            r"x \in U, \; y \in V",
        )
        defn[0].set_color(ACCENT)
        defn[1].set_color(WHITE)
        stacked = VGroup(*defn).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.ly.center_in_content(stacked)
        self.play(Write(defn[0]), run_time=NORMAL)
        self.play(Write(defn[1]), run_time=FAST)
        self.wait(1.0)
        self.ly.clear()

        # Visual: disjoint neighborhoods
        self.ly.title("Visual: Disjoint Neighborhoods", color=PRIMARY)
        pt_x = Dot(LEFT * 1.5, radius=0.08, color=PRIMARY)
        pt_y = Dot(RIGHT * 1.5, radius=0.08, color=SECONDARY)
        lbl_x = Text("x", font_size=BODY_SIZE, color=PRIMARY, font=MONO).next_to(pt_x, UP, buff=0.2)
        lbl_y = Text("y", font_size=BODY_SIZE, color=SECONDARY, font=MONO).next_to(pt_y, UP, buff=0.2)
        u_hood = Circle(radius=1.0, color=PRIMARY, fill_opacity=0.12, stroke_width=2).move_to(pt_x)
        v_hood = Circle(radius=1.0, color=SECONDARY, fill_opacity=0.12, stroke_width=2).move_to(pt_y)
        u_lbl = Text("U", font_size=LABEL_SIZE, color=PRIMARY, font=MONO).next_to(u_hood, DOWN, buff=0.1)
        v_lbl = Text("V", font_size=LABEL_SIZE, color=SECONDARY, font=MONO).next_to(v_hood, DOWN, buff=0.1)
        disjoint = Text(r"U \cap V = \emptyset", font_size=BODY_SIZE, color=ACCENT, font=MONO)

        pair = VGroup(pt_x, lbl_x, u_hood, u_lbl, pt_y, lbl_y, v_hood, v_lbl)
        self.ly.center_in_content(pair)
        self.play(
            FadeIn(pt_x), FadeIn(pt_y), FadeIn(lbl_x), FadeIn(lbl_y),
            FadeIn(u_hood), FadeIn(v_hood),
            FadeIn(u_lbl), FadeIn(v_lbl),
            run_time=NORMAL,
        )
        disjoint.next_to(pair, DOWN, buff=0.4)
        self.play(FadeIn(disjoint, shift=UP * 0.15), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

        # Why Hausdorff matters
        self.ly.title("Why Hausdorff Matters", color=ACCENT)
        importance = [
            Text("Sequences have at most ONE limit", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Compact subsets are CLOSED", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("All metric spaces are Hausdorff", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("R^n with standard topology is Hausdorff", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            importance, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=1.0,
        )
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 5: The Separation Hierarchy ~50s

    def scene5_hierarchy(self):
        self.add_subcaption(
            "The separation axioms form a hierarchy. Each stronger condition "
            "implies all weaker ones. T4 implies T3 implies T2 implies T1 "
            "implies T0. T3 means regular plus T1: you can separate a point "
            "from a closed set. T4 means normal plus T1: you can separate "
            "two disjoint closed sets. Each implication is strict.",
            duration=50,
        )
        self.ly.section_divider("4", "The Separation Hierarchy")

        self.ly.title("Separation Axiom Hierarchy", color=ACCENT)

        chain_items = [
            Text("T4 (Normal + T1)", font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD),
            Text(r"\Downarrow", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("T3 (Regular + T1)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text(r"\Downarrow", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("T2 (Hausdorff)", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD),
            Text(r"\Downarrow", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("T1 (Frechet)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text(r"\Downarrow", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("T0 (Kolmogorov)", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        chain = VGroup(*chain_items).arrange(DOWN, buff=0.15)
        self.ly.center_in_content(chain)
        for item in chain_items:
            self.play(FadeIn(item, shift=LEFT * 0.15), run_time=0.3)
        self.wait(1.0)
        self.ly.clear()

        self.ly.title("T3 and T4 Definitions", color=PRIMARY)
        t3_text = Text("T3 (Regular + T1):", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD)
        t3_def = Text("Separate a point from a closed set", font_size=BODY_SIZE, color=WHITE, font=SANS)
        t4_text = Text("T4 (Normal + T1):", font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD)
        t4_def = Text("Separate two disjoint closed sets", font_size=BODY_SIZE, color=WHITE, font=SANS)
        sep_group = VGroup(t3_text, t3_def, t4_text, t4_def).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        self.ly.center_in_content(sep_group)
        self.play(
            FadeIn(t3_text, shift=LEFT * 0.15), FadeIn(t3_def, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.play(
            FadeIn(t4_text, shift=LEFT * 0.15), FadeIn(t4_def, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 6: Normal Spaces and Urysohn's Lemma ~60s

    def scene6_normal_urysohn(self):
        self.add_subcaption(
            "Normal spaces, also called T4, can separate any two disjoint "
            "closed sets with disjoint open neighborhoods. Urysohn's lemma "
            "states that in a normal space, given two disjoint closed sets "
            "A and B, there exists a continuous function equal to zero on "
            "A and one on B. This is one of the most powerful tools in all "
            "of topology, used for partitions of unity and metrization.",
            duration=60,
        )
        self.ly.section_divider("5", "Normal Spaces & Urysohn's Lemma")

        self.ly.title("Urysohn's Lemma", color=RED)
        s1 = Text("If X is normal and A, B are disjoint closed sets:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        formula = MathTex(
            r"\exists f: X \to [0,1] \text{ continuous, } f(A) = 0, \; f(B) = 1",
        )
        formula.set_color(ACCENT)
        ury = VGroup(s1, formula).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.center_in_content(ury)
        self.play(FadeIn(s1, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Visual: continuous function from 0 to 1
        self.ly.title("Visual: The Interpolating Function", color=PRIMARY)
        ax = Axes(
            x_range=[-3, 3, 1], y_range=[-0.5, 1.5, 0.5],
            x_length=8, y_length=3.5,
            axis_config={"color": DIM, "include_numbers": False},
        )
        ax_labels = ax.get_axis_labels(
            x_label=Text("X", font_size=LABEL_SIZE, color=DIM, font=MONO),
            y_label=Text("f", font_size=LABEL_SIZE, color=DIM, font=MONO),
        )
        graph = ax.plot(
            lambda x: np.clip(1 / (1 + np.exp(-3 * x)), 0, 1),
            color=ACCENT, stroke_width=3,
        )
        # Mark A (left, f=0) and B (right, f=1)
        a_dot = Dot(ax.c2p(-2, 0), radius=0.07, color=PRIMARY)
        b_dot = Dot(ax.c2p(2, 1), radius=0.07, color=SECONDARY)
        a_lbl = Text("A (f=0)", font_size=LABEL_SIZE, color=PRIMARY, font=SANS).next_to(a_dot, DOWN, buff=0.15)
        b_lbl = Text("B (f=1)", font_size=LABEL_SIZE, color=SECONDARY, font=SANS).next_to(b_dot, UP, buff=0.15)
        vis = VGroup(ax, ax_labels, graph, a_dot, b_dot, a_lbl, b_lbl)
        self.ly.center_in_content(vis)
        self.play(Create(ax), FadeIn(ax_labels), run_time=FAST)
        self.play(Create(graph), run_time=NORMAL)
        self.play(FadeIn(a_dot), FadeIn(b_dot), FadeIn(a_lbl), FadeIn(b_lbl), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 7: Summary ~40s

    def scene7_summary(self):
        self.add_subcaption(
            "Let us recap. Separation axioms describe how well a topology "
            "distinguishes between points and sets. T0 is the weakest, "
            "requiring just one open set to distinguish any two points. "
            "T1 makes every singleton closed. T2, Hausdorff, requires "
            "disjoint neighborhoods and is the most commonly used condition. "
            "T3 and T4 allow separating points from closed sets and closed "
            "sets from each other. Urysohn's lemma is the payoff.",
            duration=40,
        )
        self.ly.section_divider("6", "Summary")

        self.ly.title("Separation Axioms Recap", color=ACCENT)
        recap = [
            Text("T0: at least one open set distinguishes any two points", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("T1: every singleton is closed", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("T2 (Hausdorff): disjoint neighborhoods, unique limits", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("T3 (Regular): separate point from closed set", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("T4 (Normal): Urysohn's lemma, partitions of unity", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(
            recap, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()
        play_outro(self, next_video="Product Topology", next_playlist="Topology")
