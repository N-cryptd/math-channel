"""
Video 148: Covering Spaces -- Topology Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video148_CoveringSpaces

Topics: Covering spaces, covering maps, local homeomorphisms,
         lifting property, relationship to fundamental group,
         universal cover.

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


class Video148_CoveringSpaces(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_examples()
        self.scene4_lifting()
        self.scene5_fundamental_group()
        self.scene6_summary()

    # --- Scene 1: Hook ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "The real line wraps around the circle infinitely many times. "
            "Every point on the circle has infinitely many preimages on the "
            "line, each one looking exactly the same locally. This is a "
            "covering space. Covering spaces are one of the deepest ideas "
            "in topology, connecting geometry, algebra, and analysis.",
            duration=50,
        )
        play_intro(self, "Covering Spaces", "Topology")

        title = self.ly.title("The Real Line Covers the Circle", color=PRIMARY)
        self.wait(0.3)

        # Visual: line and circle
        line = NumberLine(x_range=[-4, 4, 2 * PI], length=9, color=PRIMARY, include_numbers=False)
        circle = Circle(radius=1.5, color=SECONDARY, stroke_width=3)
        line.move_to(UP * 1.0)
        circle.move_to(DOWN * 1.2)
        arrow = MathTex(r"\exp(it)", font_size=BODY_SIZE, color=ACCENT)
        arrow.move_to(RIGHT * 3.5)
        self.play(Create(line), run_time=FAST)
        self.play(Create(circle), run_time=FAST)
        self.play(Write(arrow), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 2: Covering Space Definition ~60s

    def scene2_definition(self):
        self.add_subcaption(
            "A covering map p from E to X is a continuous surjection "
            "where every point of X has a neighborhood that is evenly "
            "covered. This means the preimage is a disjoint union of open "
            "sets, each mapped homeomorphically onto the neighborhood.",
            duration=60,
        )
        self.ly.section_divider("1", "Covering Space Definition")

        self.ly.title("Covering Map", color=ACCENT)
        defn = MathTex(
            r"p : \tilde{X} \to X \text{ is a covering map if}",
        )
        defn.set_color(WHITE)
        even = MathTex(
            r"\forall x \in X, \; \exists U \text{ open: } p^{-1}(U) = \bigcup U_\alpha",
        )
        even.set_color(ACCENT)
        homeo = Text("Each U_alpha maps homeomorphically to U", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        items = VGroup(defn, even, homeo).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        self.ly.center_in_content(items)
        self.play(Write(defn), run_time=FAST)
        self.play(Write(even), run_time=NORMAL)
        self.play(FadeIn(homeo, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 3: Key Examples ~70s

    def scene3_examples(self):
        self.add_subcaption(
            "The real line covers the circle via the exponential map. "
            "The circle covers itself by winding n times. The plane "
            "covers the torus by wrapping R squared around it. Each "
            "of these is a covering space where the covering map wraps "
            "the larger space around the smaller one.",
            duration=70,
        )
        self.ly.section_divider("2", "Key Examples")

        self.ly.title("Classic Covering Spaces", color=PRIMARY)
        examples = [
            Text("R -> S^1 via t -> e^(it) (infinite sheet)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("S^1 -> S^1 via z -> z^n (n-fold cover)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("R^2 -> T^2 via (s,t) -> (e^(is), e^(it))", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("S^3 -> SO(3) via quaternions (double cover)", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(
            examples, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=1.0,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 4: Lifting Property ~60s

    def scene4_lifting(self):
        self.add_subcaption(
            "The lifting property says that paths in the base space can "
            "be lifted to the covering space, uniquely once a starting "
            "point is chosen. Homotopies also lift. This means that if "
            "two paths are homotopic in the base, their lifts are "
            "homotopic in the cover. This connects covering spaces "
            "directly to the fundamental group.",
            duration=60,
        )
        self.ly.section_divider("3", "The Lifting Property")

        self.ly.title("Path Lifting", color=PRIMARY)
        lift_text = Text("Every path in X lifts uniquely to tilde X", font_size=BODY_SIZE, color=WHITE, font=SANS)
        lift_cond = Text("(once the starting point is chosen)", font_size=BODY_SIZE, color=DIM, font=SANS)
        lift = VGroup(lift_text, lift_cond).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.ly.center_in_content(lift)
        self.play(FadeIn(lift_text, shift=LEFT * 0.15), FadeIn(lift_cond, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        self.ly.title("Homotopy Lifting", color=SECONDARY)
        homo_text = Text("If gamma ~ sigma, their lifts are also homotopic", font_size=BODY_SIZE, color=ACCENT, font=SANS)
        self.ly.center_in_content(homo_text)
        self.play(FadeIn(homo_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 5: Connection to Fundamental Group ~70s

    def scene5_fundamental_group(self):
        self.add_subcaption(
            "Covering spaces are deeply connected to the fundamental "
            "group. The subgroups of the fundamental group of X "
            "correspond bijectively to covering spaces of X, up to "
            "isomorphism. The universal cover is the simply connected "
            "covering space that covers all others.",
            duration=70,
        )
        self.ly.section_divider("4", "Covering Spaces & pi_1")

        self.ly.title("Classification", color=ACCENT)
        class_thm = Text("Subgroups of pi_1(X) <=> Covering spaces of X", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD)
        self.ly.center_in_content(class_thm)
        self.play(FadeIn(class_thm, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        self.ly.title("Universal Cover", color=PRIMARY)
        uni_def = Text("Simply connected covering space", font_size=BODY_SIZE, color=WHITE, font=SANS)
        uni_examples = [
            Text("Universal cover of S^1 = R", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Universal cover of T^2 = R^2", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Universal cover of S^n = S^n for n >= 2", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            [uni_def] + uni_examples, start_from=None,
            reveal_anim=FadeIn, anim_kwargs={"shift": LEFT * 0.15},
            run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 6: Summary ~40s

    def scene6_summary(self):
        self.add_subcaption(
            "Covering spaces are spaces that wrap around other spaces "
            "like the real line wraps around the circle. They have a "
            "local homeomorphism property and support path and homotopy "
            "lifting. The fundamental group classifies covering spaces "
            "through its subgroups, and the universal cover is the "
            "largest simply connected covering space.",
            duration=40,
        )
        self.ly.section_divider("5", "Summary")

        self.ly.title("Covering Spaces Recap", color=ACCENT)
        recap = [
            Text("Covering map: locally like identity, globally wraps", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("R covers S^1, S^1 covers itself n-fold", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Paths and homotopies lift uniquely", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Subgroups of pi_1 <=> covering spaces", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            recap, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()
        play_outro(self, next_video="Surfaces and Classification", next_playlist="Topology")
