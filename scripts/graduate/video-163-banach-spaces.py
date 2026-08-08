"""
Video 163: Banach Spaces — Functional Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video163_BanachSpaces

Topics: The gap in Q as motivation,
        Cauchy sequences (definition and intuition),
        Definition of a Banach space (complete normed space),
        Examples: R, R^n, C[a,b] are Banach,
        Non-examples: Q, C[0,1] with L1 norm,
        Why completeness matters for analysis.

Prerequisites: Video 162 (Normed Spaces), Real Analysis (Sequences, Cauchy),
               Measure Theory (L^p spaces).

Competitive insights:
- Abide By Reason: "Weird spaces where pi=4" (286K views, Manim animated)
- Key insight: completeness depends on the NORM chosen, not just the space.

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
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits, clamp_position, MAX_HALF_WIDTH


class Video163_BanachSpaces(Scene):
    """Banach Spaces: Complete Normed Spaces"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_cauchy_sequences()
        self.scene3_definition()
        self.scene4_examples()
        self.scene5_non_examples()
        self.scene6_why_completeness()
        self.scene7_summary_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook — The Holes in Q
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: Q has holes, Banach spaces don't"""
        self.add_subcaption(
            "Consider the sequence 3, 3.1, 3.14, 3.141, 3.1415, "
            "approaching pi. In the rational numbers, this sequence "
            "gets closer and closer, but never reaches its limit. "
            "Pi is simply not a rational number.",
            duration=10,
        )
        play_intro(self, "Banach Spaces", "Functional Analysis")

        title = self.ly.title("The Holes in the Rational Numbers")

        items = [
            Text("Sequence: 3, 3.1, 3.14, 3.141, 3.1415, ...",
                 font_size=BODY_SIZE, color=PRIMARY, font=MONO),
            Text("This sequence is Cauchy (terms get closer)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("But pi is not in Q — the limit escapes!",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Cauchy Sequences
    # ------------------------------------------------------------------
    def scene2_cauchy_sequences(self):
        """Definition and intuition of Cauchy sequences"""
        self.ly.section_divider(2, "Cauchy Sequences")

        self.add_subcaption(
            "A Cauchy sequence is one where the terms get arbitrarily "
            "close to each other. Formally, for any positive epsilon, "
            "there is a point after which all terms are within epsilon "
            "of each other.",
            duration=8,
        )

        title = self.ly.title("Cauchy Sequences")

        # Formal definition
        def_label = Text("Definition:", font_size=BODY_SIZE, color=DIM, font=SANS)
        formula = MathTex(
            r"\forall \, \epsilon > 0, \; \exists N : \; n, m \geq N \implies \|x_n - x_m\| < \epsilon",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(def_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(formula, direction=DOWN, anchor=def_label, buff=0.1)
        self.play(
            FadeIn(def_label, shift=LEFT * 0.15),
            Write(formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(def_label), run_time=FAST)

        # Intuition
        int1 = Text(
            "The terms get arbitrarily close to each other",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(int1, direction=DOWN, anchor=formula, buff=0.3)
        self.play(FadeIn(int1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(int1), run_time=FAST)

        int2 = Text(
            "In a COMPLETE space, Cauchy = convergent",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(int2, direction=DOWN, anchor=formula, buff=0.3)
        self.play(FadeIn(int2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Definition of a Banach Space
    # ------------------------------------------------------------------
    def scene3_definition(self):
        """Banach = complete normed space"""
        self.ly.section_divider(3, "Definition: Banach Space")

        self.add_subcaption(
            "A Banach space is simply a normed space where every "
            "Cauchy sequence converges to a limit that lives inside "
            "the same space. Nothing escapes. There are no holes.",
            duration=8,
        )

        title = self.ly.title("Banach Space = Complete Normed Space")

        # Two parts
        part1 = VGroup(
            Text("1. (V, ||.||) is a normed space", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("   (from Video 162: three axioms hold)", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)

        part2 = VGroup(
            Text("2. V is COMPLETE:", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("   every Cauchy sequence converges in V", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)

        self.ly.safe_place(part1, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(part2, direction=DOWN, anchor=part1, buff=0.2)
        self.play(
            FadeIn(part1, shift=LEFT * 0.15),
            FadeIn(part2, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Key formula
        key = MathTex(
            r"\text{If } (x_n) \text{ is Cauchy} \implies \exists \, x \in V : x_n \to x",
            font_size=BODY_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(key, ACCENT)
        self.ly.safe_place(boxed, direction=DOWN, anchor=part2, buff=0.3)
        self.play(Write(key), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Examples — Banach Spaces
    # ------------------------------------------------------------------
    def scene4_examples(self):
        """Three examples of Banach spaces"""
        self.ly.section_divider(4, "Examples: Banach Spaces")

        self.add_subcaption(
            "Many familiar spaces are Banach. The real numbers, "
            "Euclidean space, and continuous functions with the "
            "sup-norm are all complete. Every Cauchy sequence "
            "converges to a limit that stays in the space.",
            duration=8,
        )

        title = self.ly.title("These Spaces ARE Banach")

        # Example 1
        ex1 = Text(
            "R with absolute value |x| is complete",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(ex1, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(ex1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.play(FadeOut(ex1), run_time=FAST)

        # Example 2
        ex2 = Text(
            "R^n with Euclidean norm is complete",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(ex2, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(ex2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.play(FadeOut(ex2), run_time=FAST)

        # Example 3
        ex3 = Text(
            "C[a,b] with sup-norm is complete",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(ex3, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(ex3, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Explanation
        ex3_detail = Text(
            "Uniform limit of continuous functions is continuous",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(ex3_detail, direction=DOWN, anchor=ex3, buff=0.1)
        self.play(FadeIn(ex3_detail, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Non-Examples — NOT Banach
    # ------------------------------------------------------------------
    def scene5_non_examples(self):
        """Spaces that are NOT complete"""
        self.ly.section_divider(5, "Non-Examples: NOT Banach")

        self.add_subcaption(
            "Not every normed space is Banach. The rational numbers "
            "have holes. And the same vector space can be Banach under "
            "one norm but not under another. Completeness depends on "
            "the norm you choose.",
            duration=8,
        )

        title = self.ly.title("These Spaces are NOT Banach")

        # Non-example 1: Q
        ne1 = Text(
            "Q with |x| is NOT complete",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        ne1_detail = Text(
            "Cauchy sequence for sqrt(2) has no limit in Q",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(ne1, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ne1_detail, direction=DOWN, anchor=ne1, buff=0.1)
        self.play(
            FadeIn(ne1, shift=LEFT * 0.15),
            FadeIn(ne1_detail, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1)
        self.play(FadeOut(ne1), FadeOut(ne1_detail), run_time=FAST)

        # Non-example 2: C[0,1] with L1 norm
        ne2 = Text(
            "C[0,1] with L1 norm is NOT complete",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        ne2_detail = Text(
            "Cauchy sequences can converge to discontinuous functions",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(ne2, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ne2_detail, direction=DOWN, anchor=ne2, buff=0.1)
        self.play(
            FadeIn(ne2, shift=LEFT * 0.15),
            FadeIn(ne2_detail, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1)

        # Key insight
        insight = Text(
            "Completeness depends on the norm!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=ne2_detail, buff=0.3)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Why Completeness Matters
    # ------------------------------------------------------------------
    def scene6_why_completeness(self):
        """Practical importance of completeness"""
        self.ly.section_divider(6, "Why Completeness Matters")

        self.add_subcaption(
            "Why do we care about completeness? The most powerful "
            "theorems in functional analysis require it. The Banach "
            "fixed point theorem, the open mapping theorem, and the "
            "closed graph theorem all need completeness to work.",
            duration=8,
        )

        title = self.ly.title("Completeness Powers Analysis")

        items = [
            Text("Banach Fixed Point Theorem needs completeness",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Open Mapping Theorem needs completeness",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Limits exist and stay in the space",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        # Final point
        final = Text(
            "Without completeness, limits can escape the space!",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        visible = self.mobjects.copy()
        last_item = None
        for m in visible:
            if isinstance(m, Text) and m not in [final, title]:
                last_item = m
        if last_item:
            self.ly.safe_place(final, direction=DOWN, anchor=last_item, buff=0.3)
        self.play(FadeIn(final, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Summary + Outro
    # ------------------------------------------------------------------
    def scene7_summary_outro(self):
        """Summary and preview"""
        self.add_subcaption(
            "To recap: a Banach space is a complete normed space "
            "where every Cauchy sequence converges within the space. "
            "Familiar spaces like R and C of a b are Banach, but "
            "the rationals are not. Completeness is essential for "
            "the major theorems of functional analysis.",
            duration=10,
        )

        title = self.ly.title("Summary + What's Next")

        items = [
            Text("Banach space = complete normed space",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Cauchy = convergent in a Banach space",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Completeness depends on the norm chosen",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        play_outro(self, "Inner Product Spaces", "Functional Analysis")
