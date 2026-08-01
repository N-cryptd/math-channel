"""
Video 146: Completeness and Completion -- Topology Playlist
TEMPLATE v2 -- Professional quality Manim script

Playlist: Topology (Video 11 of 12)
Class: Video146_Completeness

Topics: Complete metric spaces, Cauchy sequences, completion,
         Banach fixed point theorem, Baire Category Theorem.

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


class Video146_Completeness(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_complete_spaces()
        self.scene3_contraction()
        self.scene4_completion()
        self.scene5_baire()
        self.scene6_summary()

    # --- Scene 1: Hook ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "Some metric spaces have a special property: every Cauchy "
            "sequence converges. These are called complete metric spaces. "
            "The rational numbers are NOT complete, but the real numbers "
            "are. This idea of filling in the gaps leads to the completion "
            "construction and the powerful Banach fixed point theorem.",
            duration=50,
        )
        play_intro(self, "Completeness & Completion", "Topology")

        title = self.ly.title("Do All Cauchy Sequences Converge?", color=PRIMARY)
        self.wait(0.3)

        # Visual: sequence converging on number line
        line = NumberLine(x_range=[-0.5, 3, 1], length=9, color=DIM, include_numbers=True, font_size=LABEL_SIZE)
        self.ly.center_in_content(line)
        self.play(Create(line), run_time=FAST)
        self.wait(0.3)

        seq_pos = [0.5, 1.5, 0.8, 1.2, 0.95, 1.05, 0.99, 1.01, 1.0]
        dots = VGroup()
        for p in seq_pos:
            d = Dot(line.n2p(p), radius=0.05, color=PRIMARY)
            dots.add(d)
        self.play(*[FadeIn(d) for d in dots], run_time=2.0, lag_ratio=0.15)
        self.wait(0.5)

        limit = Dot(line.n2p(1.0), radius=0.1, color=ACCENT)
        lim_lbl = Text("limit = 1", font_size=LABEL_SIZE, color=ACCENT, font=MONO)
        lim_lbl.next_to(limit, UP, buff=0.2)
        self.play(FadeIn(limit), FadeIn(lim_lbl), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 2: Complete Metric Spaces ~60s

    def scene2_complete_spaces(self):
        self.add_subcaption(
            "A metric space is complete if every Cauchy sequence converges "
            "to a point in the space. The real numbers are complete, but "
            "the rationals are not. A sequence of rationals converging to "
            "the square root of two has no limit in the rationals. "
            "Completeness is essential for analysis.",
            duration=60,
        )
        self.ly.section_divider("1", "Complete Metric Spaces")

        self.ly.title("Definition", color=PRIMARY)
        defn = MathTex(
            r"(X, d) \text{ is complete if every Cauchy sequence converges in } X",
        )
        defn.set_color(WHITE)
        self.ly.center_in_content(defn)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        self.ly.title("Examples", color=SECONDARY)
        examples = [
            Text("R is complete", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Q is NOT complete (sqrt(2) missing)", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("R^n is complete (in any L^p metric)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("C[a,b] with sup norm is complete (Banach space)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            examples, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=1.0,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 3: Banach Contraction Mapping ~60s

    def scene3_contraction(self):
        self.add_subcaption(
            "The Banach fixed point theorem is one of the most important "
            "results about complete metric spaces. If a map from a complete "
            "metric space to itself is a contraction, meaning it shrinks "
            "distances by a constant factor less than one, then it has "
            "exactly one fixed point, and iterating the map converges to it.",
            duration=60,
        )
        self.ly.section_divider("2", "Banach Fixed Point Theorem")

        self.ly.title("Contraction Mapping", color=ACCENT)
        defn = MathTex(
            r"d(f(x), f(y)) \leq c \cdot d(x, y) \text{ for some } 0 \leq c < 1",
        )
        defn.set_color(ACCENT)
        self.ly.center_in_content(defn)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        self.ly.title("Banach Fixed Point Theorem", color=PRIMARY)
        result = MathTex(
            r"f \text{ has a UNIQUE fixed point } x^*",
        )
        result.set_color(SECONDARY)
        method = Text("Found by iterating: x, f(x), f(f(x)), ...", font_size=BODY_SIZE, color=WHITE, font=SANS)
        pair = VGroup(result, method).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.center_in_content(pair)
        self.play(Write(result), run_time=NORMAL)
        self.play(FadeIn(method, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # --- Scene 4: Completion ~70s

    def scene4_completion(self):
        self.add_subcaption(
            "Every metric space can be completed. The completion of X "
            "is a complete metric space containing X as a dense subspace. "
            "The construction works by taking Cauchy sequences in X and "
            "identifying sequences whose difference converges to zero. "
            "The completion of Q is R, the reals.",
            duration=70,
        )
        self.ly.section_divider("3", "Completion of Metric Spaces")

        self.ly.title("The Completion Theorem", color=ACCENT)
        thm = MathTex(
            r"\bar{X} \text{ is a complete metric space, } X \subseteq \bar{X} \text{ dense}",
        )
        thm.set_color(WHITE)
        self.ly.center_in_content(thm)
        self.play(Write(thm), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        self.ly.title("How It Works", color=PRIMARY)
        steps = [
            Text("Take all Cauchy sequences in X", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Identify sequences that converge to same limit", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Define metric on equivalence classes", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Result: complete space containing X densely", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Example: completion of Q = R", font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(
            steps, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 5: Baire Category Theorem ~50s

    def scene5_baire(self):
        self.add_subcaption(
            "The Baire Category Theorem states that in a complete metric "
            "space, the countable intersection of dense open sets is still "
            "dense. This means complete spaces cannot be too small. "
            "It has profound applications in functional analysis and "
            "proves that R is uncountable.",
            duration=50,
        )
        self.ly.section_divider("4", "Baire Category Theorem")

        self.ly.title("Baire Category Theorem", color=RED)
        thm = MathTex(
            r"\bigcap_{n=1}^{\infty} U_n \text{ is dense}",
        )
        thm.set_color(ACCENT)
        condition = Text("if X is complete and each U_n is dense open", font_size=BODY_SIZE, color=WHITE, font=SANS)
        pair = VGroup(thm, condition).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.center_in_content(pair)
        self.play(Write(thm), run_time=NORMAL)
        self.play(FadeIn(condition, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 6: Summary ~40s

    def scene6_summary(self):
        self.add_subcaption(
            "Completeness means every Cauchy sequence converges. Complete "
            "spaces support the Banach fixed point theorem and the Baire "
            "Category Theorem. Every metric space has a completion, and "
            "the completion of Q is R.",
            duration=40,
        )
        self.ly.section_divider("5", "Summary")

        self.ly.title("Completeness Recap", color=ACCENT)
        recap = [
            Text("Complete: every Cauchy sequence converges", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("R is complete, Q is not", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Banach fixed point theorem in complete spaces", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Every metric space has a completion", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            recap, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()
        play_outro(self, next_video="Fundamental Group", next_playlist="Topology")
