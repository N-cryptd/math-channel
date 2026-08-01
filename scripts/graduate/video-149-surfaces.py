"""
Video 149: Surfaces and Classification -- Topology Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video149_Surfaces

Topics: Compact surfaces, classification of compact surfaces,
         orientability, Euler characteristic, genus.

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


class Video149_Surfaces(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_compact_surfaces()
        self.scene3_classification()
        self.scene4_euler()
        self.scene5_summary()

    # --- Scene 1: Hook ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "How many different surfaces are there? The sphere, the torus, "
            "the double torus, the Klein bottle, the projective plane. "
            "It turns out there is a complete classification. Every "
            "compact surface is homeomorphic to exactly one from a short "
            "list. This classification theorem is one of the most "
            "beautiful results in all of topology.",
            duration=50,
        )
        play_intro(self, "Surfaces & Classification", "Topology")

        title = self.ly.title("The Zoo of Surfaces", color=PRIMARY)
        self.wait(0.3)

        surfaces = [
            Text("Sphere S^2", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Torus T^2", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Klein Bottle", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Projective Plane RP^2", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Double Torus", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(
            surfaces, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.5, wait_time=0.5,
        )
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 2: Compact Surfaces ~60s

    def scene2_compact_surfaces(self):
        self.add_subcaption(
            "A surface is a two-dimensional topological manifold. "
            "Compact surfaces without boundary are the ones we classify. "
            "A surface is orientable if it has a consistent notion of "
            "inside and outside, like the sphere and the torus. "
            "Non-orientable surfaces like the Klein bottle do not.",
            duration=60,
        )
        self.ly.section_divider("1", "Compact Surfaces")

        self.ly.title("What is a Surface?", color=PRIMARY)
        defn = Text("A compact 2-dimensional manifold without boundary", font_size=BODY_SIZE, color=WHITE, font=SANS)
        self.ly.center_in_content(defn)
        self.play(FadeIn(defn, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        self.ly.title("Orientability", color=SECONDARY)
        orient = [
            Text("Orientable: sphere, torus, double torus", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Non-orientable: Klein bottle, projective plane", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Orientability is a topological invariant", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            orient, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=1.0,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 3: Classification Theorem ~70s

    def scene3_classification(self):
        self.add_subcaption(
            "The classification theorem for compact surfaces states that "
            "every compact connected surface is homeomorphic to exactly "
            "one of the following: a sphere, a connected sum of g tori "
            "for some genus g, or a connected sum of k projective planes "
            "for some k. Orientable surfaces are classified by genus. "
            "Non-orientable surfaces are classified by the number of "
            "cross-caps.",
            duration=70,
        )
        self.ly.section_divider("2", "Classification Theorem")

        self.ly.title("Classification of Compact Surfaces", color=ACCENT)
        orientable = MathTex(
            r"\text{Orientable: } S^2, \; T^2, \; T^2 \# T^2, \; \ldots, \; \#_g T^2",
        )
        orientable.set_color(SECONDARY)
        self.ly.center_in_content(orientable)
        self.play(Write(orientable), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        non_orient = MathTex(
            r"\text{Non-orientable: } \mathbb{R}P^2, \; \mathbb{R}P^2 \# \mathbb{R}P^2, \; \ldots, \; \#_k \mathbb{R}P^2",
        )
        non_orient.set_color(RED)
        self.ly.title("Non-Orientable Case", color=RED)
        self.ly.center_in_content(non_orient)
        self.play(Write(non_orient), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        self.ly.title("The Key Insight", color=PRIMARY)
        key = Text("Genus g = number of 'handles' on the surface", font_size=BODY_SIZE, color=ACCENT, font=SANS)
        key2 = Text("Euler characteristic = 2 - 2g (orientable)", font_size=BODY_SIZE, color=WHITE, font=SANS)
        kg = VGroup(key, key2).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.ly.center_in_content(kg)
        self.play(FadeIn(key, shift=LEFT * 0.15), FadeIn(key2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 4: Euler Characteristic ~60s

    def scene4_euler(self):
        self.add_subcaption(
            "The Euler characteristic is a topological invariant computed "
            "from any triangulation of the surface. It equals V minus E "
            "plus F, where V is vertices, E is edges, and F is faces. "
            "For orientable surfaces of genus g, the Euler characteristic "
            "is two minus two g. The sphere has chi equals two, the "
            "torus has chi equals zero.",
            duration=60,
        )
        self.ly.section_divider("3", "Euler Characteristic")

        self.ly.title("Euler Characteristic", color=PRIMARY)
        chi = MathTex(
            r"\chi = V - E + F",
        )
        chi.set_color(ACCENT)
        self.ly.center_in_content(chi)
        self.play(Write(chi), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        self.ly.title("Values", color=SECONDARY)
        values = [
            Text("Sphere: chi = 2", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Torus: chi = 0", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Double torus (g=2): chi = -2", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Genus g: chi = 2 - 2g", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(
            values, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 5: Summary ~40s

    def scene5_summary(self):
        self.add_subcaption(
            "The classification theorem says every compact surface is "
            "either a sphere, a connected sum of tori, or a connected sum "
            "of projective planes. Orientable surfaces are classified by "
            "their genus, which is encoded by the Euler characteristic. "
            "This is one of the most complete classification results "
            "in all of mathematics.",
            duration=40,
        )
        self.ly.section_divider("4", "Summary")

        self.ly.title("Surfaces Recap", color=ACCENT)
        recap = [
            Text("Compact surfaces classified by orientability and genus", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Orientable: sphere, torus, g-holed torus", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Euler characteristic: chi = 2 - 2g", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("One of the most beautiful theorems in topology", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(
            recap, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()
        play_outro(self, next_video="Topology Recap", next_playlist="Topology")
