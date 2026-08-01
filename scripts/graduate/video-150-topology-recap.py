"""
Video 150: Topology Recap & What's Next -- Topology Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video150_TopologyRecap

Topics: Recap of entire topology playlist, key themes, invariants,
         what comes next in mathematics.

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


class Video150_TopologyRecap(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_review()
        self.scene3_themes()
        self.scene4_next()
        self.scene5_final()

    # --- Scene 1: Hook ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "We have journeyed through the landscape of topology, from "
            "the basic definitions of open sets and continuous maps to "
            "the classification of compact surfaces. Along the way we "
            "encountered compactness, separation axioms, the fundamental "
            "group, and covering spaces. Let us look back at what we "
            "have learned and where mathematics goes next.",
            duration=50,
        )
        play_intro(self, "Topology Recap", "Topology")

        title = self.ly.title("Our Journey Through Topology", color=ACCENT)
        self.wait(0.3)
        topics = [
            Text("12 videos, from basics to classification", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Connectedness, Compactness, Separation Axioms", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Product & Quotient constructions", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Fundamental group & Covering spaces", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            topics, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.6,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 2: What We Learned ~70s

    def scene2_review(self):
        self.add_subcaption(
            "We started with topological spaces, open sets, and continuous "
            "maps. Then we explored connectedness, the idea that a space "
            "is in one piece. Compactness captured the notion that every "
            "open cover has a finite subcover. Separation axioms told us "
            "how well points can be distinguished. The product and "
            "quotient constructions built new spaces from old ones.",
            duration=70,
        )
        self.ly.section_divider("1", "What We Learned")

        self.ly.title("Foundations", color=PRIMARY)
        found = [
            Text("Topological spaces, open sets, continuous maps", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Connectedness and path-connectedness", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Compactness: finite subcover property", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Separation axioms: T0 through T4 (Hausdorff)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Product and quotient topologies", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(
            found, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.5,
        )
        self.wait(0.5)
        self.ly.clear()

        self.ly.title("Advanced Topics", color=SECONDARY)
        adv = [
            Text("Metric spaces and metrization theorems", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Completeness, Banach fixed point, Baire category", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Fundamental group: loops and holes", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Covering spaces and universal covers", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Classification of compact surfaces", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(
            adv, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.5,
        )
        self.wait(0.5)
        self.ly.clear()

    # --- Scene 3: Key Themes ~60s

    def scene3_themes(self):
        self.add_subcaption(
            "Three themes run through all of topology. First, topological "
            "invariants: properties preserved by homeomorphisms, like "
            "connectedness, compactness, and the fundamental group. "
            "Second, constructions: building new spaces via products, "
            "quotients, and completions. Third, classification: "
            "understanding all spaces with a given set of properties.",
            duration=60,
        )
        self.ly.section_divider("2", "Key Themes")

        self.ly.title("Three Big Ideas", color=ACCENT)
        themes = [
            Text("1. Invariants: properties preserved by homeomorphisms", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Constructions: building spaces (products, quotients)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Classification: understanding all spaces in a class", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            themes, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=1.0,
        )
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 4: What's Next ~60s

    def scene4_next(self):
        self.add_subcaption(
            "Topology opens doors to many areas of advanced mathematics. "
            "Algebraic topology studies homology and cohomology groups "
            "that detect higher-dimensional holes. Differential topology "
            "studies smooth manifolds and Morse theory. Knot theory "
            "classifies embeddings of circles in three-dimensional "
            "space. Geometric topology studies the geometry of manifolds "
            "in dimensions three and four.",
            duration=60,
        )
        self.ly.section_divider("3", "What Comes Next")

        self.ly.title("Frontiers of Topology", color=RED)
        frontiers = [
            Text("Algebraic topology: homology, cohomology", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Differential topology: smooth manifolds", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Knot theory: classifying embeddings of S^1 in R^3", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Geometric topology: 3D and 4D manifolds", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Applications: physics, data analysis, robotics", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(
            frontiers, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 5: Final Outro ~30s

    def scene5_final(self):
        self.add_subcaption(
            "Thank you for joining us on this journey through topology. "
            "You now have a solid foundation in one of the most beautiful "
            "and powerful branches of mathematics. Keep exploring, keep "
            "asking questions, and remember that mathematics is about "
            "understanding the deep structure of space itself.",
            duration=30,
        )
        self.ly.section_divider("", "Thank You")

        final = Text("Topology: the mathematics of shape and space.", font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD)
        self.ly.center_in_content(final)
        self.play(Write(final), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()
        play_outro(self, next_video="Next Playlist", next_playlist="Explore More")
