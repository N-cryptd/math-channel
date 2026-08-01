"""
Video 147: Fundamental Group Intro -- Topology Playlist
TEMPLATE v2 -- Professional quality Manim script

Playlist: Topology (Video 12 of 12)
Class: Video147_FundamentalGroup

Topics: Homotopy of paths, fundamental group pi_1, loop spaces,
         examples (pi_1 of R^n, S^1), properties and functoriality.

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


class Video147_FundamentalGroup(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_homotopy()
        self.scene3_fundamental_group()
        self.scene4_examples()
        self.scene5_properties()
        self.scene6_summary()

    # --- Scene 1: Hook ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "Imagine walking on a surface and returning to where you "
            "started. On a plane, you can always shrink your path to a "
            "point. But on a circle, a loop that goes all the way around "
            "cannot be shrunk. The number of times you wind around the "
            "circle is captured by the integers. This winding number is "
            "the fundamental group of the circle.",
            duration=50,
        )
        play_intro(self, "Fundamental Group", "Topology")

        title = self.ly.title("Loops That Cannot Be Shrunk", color=PRIMARY)
        self.wait(0.3)

        # Visual: circle with loop that can't shrink
        circle = Circle(radius=1.8, color=SECONDARY, stroke_width=3)
        self.ly.center_in_content(circle)
        self.play(Create(circle), run_time=NORMAL)
        self.wait(0.3)

        # Draw a loop around the circle
        loop = Circle(radius=2.2, color=ACCENT, stroke_width=2, fill_opacity=0)
        self.play(Create(loop), run_time=NORMAL)
        self.wait(0.5)

        cannot = Text("This loop CANNOT be shrunk to a point!", font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD)
        cannot.next_to(circle, DOWN, buff=0.8)
        self.play(FadeIn(cannot, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 2: Homotopy of Paths ~60s

    def scene2_homotopy(self):
        self.add_subcaption(
            "A homotopy is a continuous deformation of one path into "
            "another. Two paths are homotopic if you can smoothly morph "
            "one into the other while keeping the endpoints fixed. Formally, "
            "a homotopy between paths gamma and sigma is a continuous map "
            "from the unit square to the space.",
            duration=60,
        )
        self.ly.section_divider("1", "Homotopy of Paths")

        self.ly.title("What is a Homotopy?", color=PRIMARY)
        defn = MathTex(
            r"\gamma, \sigma : [0,1] \to X \text{ are homotopic if }",
            r"\exists H: [0,1]^2 \to X \text{ continuous}",
        )
        defn[0].set_color(WHITE)
        defn[1].set_color(ACCENT)
        h_def = VGroup(*defn).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.ly.center_in_content(h_def)
        self.play(Write(defn[0]), run_time=NORMAL)
        self.play(Write(defn[1]), run_time=FAST)
        self.wait(1.0)
        self.ly.clear()

        self.ly.title("Visual: Deformation", color=SECONDARY)
        # Square representing [0,1]^2
        sq = Square(side_length=2.5, color=DIM, stroke_width=1)
        self.ly.center_in_content(sq)
        self.play(Create(sq), run_time=FAST)
        self.wait(0.3)

        # Path labels
        bot = Text("gamma (s, 0)", font_size=LABEL_SIZE, color=PRIMARY, font=MONO)
        bot.next_to(sq.get_bottom(), DOWN, buff=0.15)
        top = Text("sigma (s, 1)", font_size=LABEL_SIZE, color=SECONDARY, font=MONO)
        top.next_to(sq.get_top(), UP, buff=0.15)
        time_lbl = Text("t goes from 0 to 1", font_size=LABEL_SIZE, color=DIM, font=SANS)
        time_lbl.next_to(sq.get_right(), RIGHT, buff=0.3)
        self.play(FadeIn(bot), FadeIn(top), FadeIn(time_lbl), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 3: The Fundamental Group ~70s

    def scene3_fundamental_group(self):
        self.add_subcaption(
            "The fundamental group of a space X at a base point x zero is "
            "the set of all loops based at x zero, modulo homotopy. The "
            "group operation is concatenation of loops. The identity is the "
            "constant loop. The inverse of a loop is the same path traversed "
            "backwards. This gives a group structure on loops.",
            duration=70,
        )
        self.ly.section_divider("2", "The Fundamental Group")

        self.ly.title("Fundamental Group", color=ACCENT)
        defn = MathTex(
            r"\pi_1(X, x_0) = \{[\gamma] : \gamma \text{ is a loop at } x_0\}",
        )
        defn.set_color(ACCENT)
        self.ly.center_in_content(defn)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        self.ly.title("Group Structure", color=PRIMARY)
        ops = [
            Text("Identity: constant loop at x_0", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Product: concatenate two loops", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Inverse: traverse the loop backwards", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("[gamma][sigma] = [gamma * sigma] (homotopy classes)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            ops, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=1.0,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 4: Examples ~70s

    def scene4_examples(self):
        self.add_subcaption(
            "The fundamental group of R^n is trivial, the zero group. "
            "Every loop can be shrunk to a point. But the fundamental "
            "group of the circle is the integers. The winding number "
            "classifies loops on the circle. This is one of the most "
            "important computations in algebraic topology.",
            duration=70,
        )
        self.ly.section_divider("3", "Key Examples")

        self.ly.title("R^n is Simply Connected", color=SECONDARY)
        trivial = MathTex(
            r"\pi_1(\mathbb{R}^n) = \{e\} \text{ (trivial group)}",
        )
        trivial.set_color(SECONDARY)
        reason = Text("Every loop can be shrunk to a point", font_size=BODY_SIZE, color=DIM, font=SANS)
        pair = VGroup(trivial, reason).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.center_in_content(pair)
        self.play(Write(trivial), FadeIn(reason, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        self.ly.title("The Circle: pi_1(S^1) = Z", color=ACCENT)
        circ_def = MathTex(
            r"\pi_1(S^1) \cong \mathbb{Z}",
        )
        circ_def.set_color(ACCENT)
        wind = Text("Winding number: how many times the loop wraps around", font_size=BODY_SIZE, color=WHITE, font=SANS)
        pair2 = VGroup(circ_def, wind).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.center_in_content(pair2)
        self.play(Write(circ_def), FadeIn(wind, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        self.ly.title("More Examples", color=PRIMARY)
        more = [
            Text("pi_1(S^2) = 0 (simply connected sphere)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("pi_1(T^2) = Z x Z (torus)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("pi_1(Klein bottle) = non-abelian group", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(
            more, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 5: Properties ~50s

    def scene5_properties(self):
        self.add_subcaption(
            "The fundamental group is a homotopy invariant. If two spaces "
            "are homotopy equivalent, they have isomorphic fundamental "
            "groups. Continuous maps induce group homomorphisms. This "
            "makes the fundamental group a functor from topology to "
            "group theory.",
            duration=50,
        )
        self.ly.section_divider("4", "Properties")

        self.ly.title("Functoriality", color=PRIMARY)
        props = [
            Text("Homotopy invariant: X ~ Y => pi_1(X) = pi_1(Y)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("f: X -> Y continuous => f_*: pi_1(X) -> pi_1(Y)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Different base points => isomorphic groups (if path-connected)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Product: pi_1(X x Y) = pi_1(X) x pi_1(Y)", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(
            props, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 6: Summary ~40s

    def scene6_summary(self):
        self.add_subcaption(
            "The fundamental group measures the holes in a space by "
            "studying loops that cannot be shrunk. It is a group whose "
            "elements are homotopy classes of loops. The circle has "
            "fundamental group Z, capturing winding number. The fundamental "
            "group is a powerful homotopy invariant and a bridge between "
            "topology and algebra.",
            duration=40,
        )
        self.ly.section_divider("5", "Summary")

        self.ly.title("Fundamental Group Recap", color=ACCENT)
        recap = [
            Text("Loops at base point, modulo homotopy", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("pi_1(R^n) = 0, pi_1(S^1) = Z", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Homotopy invariant and functorial", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Bridge from topology to algebra", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(
            recap, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()
        play_outro(self, next_video="Covering Spaces", next_playlist="Topology")
