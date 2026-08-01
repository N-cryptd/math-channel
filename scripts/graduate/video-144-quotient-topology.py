"""
Video 144: Quotient Topology -- Topology Playlist
TEMPLATE v2 -- Professional quality Manim script

Playlist: Topology (Video 9 of 12)
Class: Video144_QuotientTopology

Topics: Quotient topology, equivalence relations, quotient maps,
         torus as quotient, Klein bottle, projective plane,
         universal property of quotient maps.

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


class Video144_QuotientTopology(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_equivalence()
        self.scene3_quotient_topology()
        self.scene4_circle_example()
        self.scene5_torus()
        self.scene6_klein_projective()
        self.scene7_summary()

    # --- Scene 1: Hook -- "Gluing Spaces Together" ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "What if you could take a topological space and glue some of "
            "its points together? The quotient topology lets us do exactly "
            "that. Identify the two ends of a strip, and you get a circle. "
            "Identify opposite edges of a square, and you get a torus. "
            "Add a twist, and you get a Klein bottle. The quotient "
            "construction is one of the most creative tools in topology.",
            duration=50,
        )
        play_intro(self, "Quotient Topology", "Topology")

        # Visual: interval with endpoints being glued
        interval = Line(LEFT * 3, RIGHT * 3, color=SECONDARY, stroke_width=6)
        self.ly.center_in_content(interval)
        self.play(Create(interval), run_time=NORMAL)
        self.wait(0.3)

        # Endpoints
        pt_a = Dot(LEFT * 3, radius=0.1, color=PRIMARY)
        pt_b = Dot(RIGHT * 3, radius=0.1, color=PRIMARY)
        lbl_a = Text("0", font_size=BODY_SIZE, color=PRIMARY, font=MONO).next_to(pt_a, DOWN, buff=0.2)
        lbl_b = Text("1", font_size=BODY_SIZE, color=PRIMARY, font=MONO).next_to(pt_b, DOWN, buff=0.2)
        self.play(FadeIn(pt_a), FadeIn(pt_b), FadeIn(lbl_a), FadeIn(lbl_b), run_time=FAST)
        self.wait(0.5)

        # Show glue
        glue_text = Text("Glue 0 ~ 1", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD)
        glue_text.next_to(interval, DOWN, buff=1.0)
        self.play(FadeIn(glue_text, shift=UP * 0.15), run_time=FAST)
        self.wait(0.5)

        # Circle result
        circle_result = Circle(radius=1.2, color=ACCENT, stroke_width=3)
        circle_result.move_to(RIGHT * 3.5 + DOWN * 1.5)
        circle_lbl = Text("= S^1", font_size=BODY_SIZE, color=ACCENT, font=MONO)
        circle_lbl.next_to(circle_result, DOWN, buff=0.2)
        arrow = MathTex(r"\Rightarrow", font_size=HEADING_SIZE, color=ACCENT)
        arrow.move_to(DOWN * 1.5 + RIGHT * 1.5)
        self.play(Write(arrow), FadeIn(circle_result), FadeIn(circle_lbl), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 2: Equivalence Relations and Quotient Sets ~60s

    def scene2_equivalence(self):
        self.add_subcaption(
            "To build a quotient space, we start with an equivalence relation "
            "on X. This partitions X into equivalence classes. The quotient "
            "set X tilde is the set of all equivalence classes. The quotient "
            "map q sends each point to its equivalence class.",
            duration=60,
        )
        self.ly.section_divider("1", "Equivalence Relations")

        self.ly.title("Equivalence Relation on X", color=PRIMARY)
        props = [
            Text("Reflexive: x ~ x", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Symmetric: x ~ y => y ~ x", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Transitive: x ~ y, y ~ z => x ~ z", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(
            props, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()

        self.ly.title("Quotient Set", color=SECONDARY)
        defn = MathTex(
            r"X/{\sim} = \{[x] : x \in X\}",
            r"\text{ where } [x] = \{y \in X : y \sim x\}",
        )
        defn[0].set_color(ACCENT)
        defn[1].set_color(DIM)
        qset = VGroup(*defn).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.ly.center_in_content(qset)
        self.play(Write(defn[0]), run_time=NORMAL)
        self.play(Write(defn[1]), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 3: The Quotient Topology ~70s

    def scene3_quotient_topology(self):
        self.add_subcaption(
            "The quotient topology on X tilde is the finest topology that "
            "makes the quotient map q continuous. A subset of X tilde is "
            "open if and only if its preimage under q is open in X. This "
            "means we collapse equivalence classes into single points and "
            "inherit the topology from X.",
            duration=70,
        )
        self.ly.section_divider("2", "The Quotient Topology")

        self.ly.title("Quotient Topology", color=ACCENT)
        q_map = MathTex(r"q : X \to X/{\sim}")
        q_map.set_color(PRIMARY)
        self.ly.center_in_content(q_map)
        self.play(Write(q_map), run_time=FAST)
        self.wait(0.5)
        self.ly.clear()

        self.ly.title("Definition", color=PRIMARY)
        defn1 = Text("V is open in X/~ if and only if:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        defn2 = MathTex(r"q^{-1}(V) \text{ is open in } X")
        defn2.set_color(ACCENT)
        topo_def = VGroup(defn1, defn2).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.center_in_content(topo_def)
        self.play(FadeIn(defn1, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(defn2), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        self.ly.title("Key Property", color=SECONDARY)
        finest = Text("Quotient topology = FINEST topology making q continuous", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.center_in_content(finest)
        self.play(FadeIn(finest, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 4: Classic Example -- The Circle ~60s

    def scene4_circle_example(self):
        self.add_subcaption(
            "Our first example: identify the endpoints of the interval "
            "zero one. The equivalence relation is zero tilde one, with "
            "all other points equivalent only to themselves. The quotient "
            "is the circle S one. The quotient map wraps the interval "
            "around the circle.",
            duration=60,
        )
        self.ly.section_divider("3", "Example: The Circle")

        self.ly.title("[0, 1] / {0 ~ 1} = S^1", color=ACCENT)
        eq_rel = MathTex(r"0 \sim 1, \; x \sim x \text{ for } x \in (0,1)")
        eq_rel.set_color(WHITE)
        self.ly.center_in_content(eq_rel)
        self.play(Write(eq_rel), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        # Visual: interval wrapping to circle
        self.ly.title("Visual: Wrapping", color=PRIMARY)
        line_seg = Line(LEFT * 2.5, RIGHT * 2.5, color=SECONDARY, stroke_width=4)
        circle_viz = Circle(radius=1.5, color=ACCENT, stroke_width=3)
        line_seg.move_to(LEFT * 2.5)
        circle_viz.move_to(RIGHT * 2.5 + DOWN * 0.3)
        arrow = MathTex(r"\Rightarrow", font_size=HEADING_SIZE, color=DIM)
        arrow.move_to(ORIGIN + DOWN * 0.3)
        self.play(Create(line_seg), run_time=FAST)
        self.play(Write(arrow), run_time=FAST)
        self.play(Create(circle_viz), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 5: The Torus as a Quotient ~70s

    def scene5_torus(self):
        self.add_subcaption(
            "The torus is obtained from the unit square by identifying "
            "opposite edges. First, identify the left and right edges to "
            "form a cylinder. Then identify the top and bottom edges of "
            "the cylinder to close it into a torus. Algebraically, this "
            "is R squared modulo Z squared.",
            duration=70,
        )
        self.ly.section_divider("4", "The Torus")

        self.ly.title("Torus: [0,1]^2 with Edge Identifications", color=ACCENT)

        # Square with arrows
        square = Square(side_length=3, color=SECONDARY, stroke_width=2)
        self.ly.center_in_content(square)
        self.play(Create(square), run_time=FAST)
        self.wait(0.3)

        # Left-right arrows (same direction)
        ar_lr = MathTex(r"\longleftrightarrow", font_size=HEADING_SIZE, color=PRIMARY)
        ar_lr.move_to(square.get_left() + LEFT * 0.4)
        ar_lr2 = MathTex(r"\longleftrightarrow", font_size=HEADING_SIZE, color=PRIMARY)
        ar_lr2.move_to(square.get_right() + RIGHT * 0.4)
        # Top-bottom arrows (same direction)
        ar_tb = MathTex(r"\uparrow\downarrow", font_size=HEADING_SIZE, color=SECONDARY)
        ar_tb.move_to(square.get_top() + UP * 0.3)
        ar_tb2 = MathTex(r"\uparrow\downarrow", font_size=HEADING_SIZE, color=SECONDARY)
        ar_tb2.move_to(square.get_bottom() + DOWN * 0.3)

        self.play(
            FadeIn(ar_lr), FadeIn(ar_lr2),
            FadeIn(ar_tb), FadeIn(ar_tb2),
            run_time=NORMAL,
        )

        # Labels
        a_lbl = Text("a", font_size=BODY_SIZE, color=PRIMARY, font=MONO)
        a_lbl.move_to(square.get_top() + UP * 0.8)
        b_lbl = Text("b", font_size=BODY_SIZE, color=SECONDARY, font=MONO)
        b_lbl.move_to(square.get_right() + RIGHT * 0.9)
        self.play(FadeIn(a_lbl), FadeIn(b_lbl), run_time=FAST)

        result = Text("= Torus T^2", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD)
        result.move_to(square.get_bottom() + DOWN * 0.9)
        self.play(FadeIn(result, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        self.ly.title("Algebraic View", color=PRIMARY)
        alg = MathTex(r"T^2 \cong \mathbb{R}^2 / \mathbb{Z}^2")
        alg.set_color(ACCENT)
        self.ly.center_in_content(alg)
        self.play(Write(alg), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 6: Klein Bottle and Projective Plane ~60s

    def scene6_klein_projective(self):
        self.add_subcaption(
            "Changing the direction of edge identifications gives different "
            "surfaces. The Klein bottle reverses one pair of arrows, giving "
            "a non-orientable surface that cannot exist in three dimensions. "
            "The real projective plane identifies antipodal points of S two, "
            "creating a non-orientable surface with fundamental group Z two.",
            duration=60,
        )
        self.ly.section_divider("5", "Klein Bottle & Projective Plane")

        self.ly.title("Klein Bottle", color=RED)
        kb_text = Text("Reverse ONE pair of edge identifications", font_size=BODY_SIZE, color=WHITE, font=SANS)
        kb_result = Text("=> Non-orientable, cannot embed in R^3!", font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD)
        kb = VGroup(kb_text, kb_result).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.ly.center_in_content(kb)
        self.play(FadeIn(kb_text, shift=LEFT * 0.15), FadeIn(kb_result, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        self.ly.title("Real Projective Plane RP^2", color=SECONDARY)
        rp_def = MathTex(
            r"\mathbb{R}P^2 = S^2 / \{x \sim -x\}",
        )
        rp_def.set_color(ACCENT)
        rp_text = Text("Identify antipodal points on the sphere", font_size=BODY_SIZE, color=WHITE, font=SANS)
        rp = VGroup(rp_def, rp_text).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.center_in_content(rp)
        self.play(Write(rp_def), run_time=NORMAL)
        self.play(FadeIn(rp_text, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 7: Summary ~40s

    def scene7_summary(self):
        self.add_subcaption(
            "The quotient topology lets us construct new spaces by "
            "identifying points. The quotient map collapses equivalence "
            "classes into single points. Classic examples include the "
            "circle from an interval, the torus from a square, and the "
            "projective plane from a sphere. Changing identification "
            "patterns creates an enormous variety of spaces.",
            duration=40,
        )
        self.ly.section_divider("6", "Summary")

        self.ly.title("Quotient Topology Recap", color=ACCENT)
        recap = [
            Text("Identify points via equivalence relation", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("V open in X/~ iff q^(-1)(V) open in X", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("[0,1] / {0~1} = S^1 (circle)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("[0,1]^2 / edges = T^2 (torus)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("S^2 / {x~-x} = RP^2 (projective plane)", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(
            recap, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()
        play_outro(self, next_video="Metric Spaces and Metrization", next_playlist="Topology")
