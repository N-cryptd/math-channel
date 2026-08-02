"""
Video 152: Sigma-Algebras -- Measure Theory Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video152_SigmaAlgebras

Topics: Algebras vs sigma-algebras, Borel sigma-algebra,
        generated sigma-algebras, measurable spaces.

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
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits, clamp_position


class Video152_SigmaAlgebras(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_algebra_to_sigma()
        self.scene3_formal_definition()
        self.scene4_examples()
        self.scene5_borel()
        self.scene6_generated()
        self.scene7_measurable_spaces()
        self.scene8_summary()

    # --- Scene 1: Hook -- "Measuring Sets" ~50s ---

    def scene1_hook(self):
        self.add_subcaption(
            "In probability theory, we want to assign a number to "
            "every event. In integration theory, we want to assign "
            "a measure to every set. But not every collection of "
            "sets allows a consistent measure. We need a family of "
            "sets that is rich enough to be useful, yet well-behaved "
            "enough to avoid paradoxes.",
            duration=50,
        )
        play_intro(self, "Sigma-Algebras", "Measure Theory")

        title = self.ly.title("Measuring Sets", color=ACCENT)

        items = [
            Text("Probability: assign numbers to events", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Integration: assign measures to sets", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Problem: not every collection works", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Solution: the sigma-algebra", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(
            items, start_from=title, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.7, wait_time=1.2,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 2: From Algebras to Sigma-Algebras ~70s ---

    def scene2_algebra_to_sigma(self):
        self.add_subcaption(
            "Suppose we have a set X. What properties should a "
            "useful family of subsets have? First, it should contain "
            "X itself and the empty set. Second, it should be closed "
            "under complements. Third, it should be closed under "
            "unions. These three properties define an algebra of "
            "sets. But for measure theory we need closure under "
            "countably infinite unions, not just finite ones.",
            duration=70,
        )

        title = self.ly.title("From Algebras to Sigma-Algebras", color=PRIMARY)

        axiom1 = Text(
            "1.  Contains X and the empty set",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        axiom2 = Text(
            "2.  Closed under complements: A in F implies A^c in F",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        axiom3 = Text(
            "3.  Closed under finite unions",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.progressive_reveal(
            [axiom1, axiom2, axiom3], start_from=title, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.7, wait_time=1.5,
        )

        self.wait(0.5)

        label = Text(
            "These define an ALGEBRA of sets",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        label.move_to(ORIGIN)
        ensure_fits(label)
        self.ly.center_in_content(label)

        self.play(
            *[FadeOut(m) for m in [axiom1, axiom2, axiom3]],
            FadeIn(label, shift=UP * 0.2),
            run_time=0.8,
        )
        self.wait(1.5)

        self.play(FadeOut(label), run_time=0.4)

        upgrade = Text(
            "But we need COUNTABLE unions!",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        ensure_fits(upgrade)
        self.ly.center_in_content(upgrade)
        self.play(Write(upgrade), run_time=0.8)
        self.wait(1.5)

        sigma_label = Text(
            "This upgrade: from Algebra to SIGMA-ALGEBRA",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        ensure_fits(sigma_label)
        sigma_label.next_to(upgrade, DOWN, buff=0.6)
        clamp_position(sigma_label)
        self.play(FadeIn(sigma_label, shift=LEFT * 0.15), run_time=0.7)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 3: Formal Definition ~60s ---

    def scene3_formal_definition(self):
        self.add_subcaption(
            "A sigma-algebra F on a set X is a collection of "
            "subsets satisfying three axioms. One: X belongs to F, "
            "and hence the empty set too. Two: if A is in F, then "
            "its complement A complement is in F. Three: if A one, "
            "A two, A three, and so on are all in F, then their "
            "countable union is in F. From these we can derive "
            "countable intersections and set differences.",
            duration=60,
        )

        title = self.ly.title("Definition of a Sigma-Algebra", color=PRIMARY)

        # Definition box background
        def_text = MathTex(
            r"\mathcal{F} \subseteq \mathcal{P}(X)",
            " is a ",
            r"\sigma",
            r"-algebra",
            " if:",
            font_size=BODY_SIZE,
        )
        def_text[2].set_color(ACCENT)
        def_text[3].set_color(ACCENT)
        ensure_fits(def_text)
        self.ly.safe_place(def_text, anchor=title, buff=0.5)
        self.play(Write(def_text), run_time=1.0)
        self.wait(0.5)

        ax1 = MathTex(
            r"(1)", r"\;", r"X \in \mathcal{F}",
            font_size=BODY_SIZE,
        )
        ax1[0].set_color(PRIMARY)
        ax1[2].set_color(WHITE)
        ensure_fits(ax1)
        self.ly.safe_place(ax1, anchor=def_text, buff=0.4)
        self.play(FadeIn(ax1, shift=LEFT * 0.15), run_time=0.6)
        self.wait(0.8)

        ax2 = MathTex(
            r"(2)", r"\;", r"A \in \mathcal{F}",
            r" \Rightarrow ",
            r"A^c \in \mathcal{F}",
            font_size=BODY_SIZE,
        )
        ax2[0].set_color(SECONDARY)
        ax2[2].set_color(WHITE)
        ax2[4].set_color(SECONDARY)
        ensure_fits(ax2)
        self.ly.safe_place(ax2, anchor=ax1, buff=0.35)
        self.play(FadeIn(ax2, shift=LEFT * 0.15), run_time=0.6)
        self.wait(0.8)

        ax3 = MathTex(
            r"(3)", r"\;", r"A_1, A_2, A_3, \ldots \in \mathcal{F}",
            r" \Rightarrow ",
            r"\bigcup_{i=1}^{\infty} A_i \in \mathcal{F}",
            font_size=BODY_SIZE,
        )
        ax3[0].set_color(ACCENT)
        ax3[2].set_color(WHITE)
        ax3[4].set_color(ACCENT)
        ensure_fits(ax3)
        self.ly.safe_place(ax3, anchor=ax2, buff=0.35)
        self.play(FadeIn(ax3, shift=LEFT * 0.15), run_time=0.6)
        self.wait(1.5)

        # Derived properties
        derived = Text(
            "Derived: countable intersections (De Morgan), differences",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        ensure_fits(derived)
        self.ly.safe_place(derived, anchor=ax3, buff=0.5)
        self.play(FadeIn(derived), run_time=0.5)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 4: Examples ~70s ---

    def scene4_examples(self):
        self.add_subcaption(
            "Let us look at three examples of sigma-algebras. "
            "The trivial sigma-algebra contains only the empty "
            "set and X itself. The power set contains every "
            "possible subset. The countable and co-countable "
            "sigma-algebra on the real line contains all "
            "countable sets and all sets whose complement is "
            "countable.",
            duration=70,
        )

        title = self.ly.title("Examples of Sigma-Algebras", color=PRIMARY)

        ex1_label = Text(
            "Trivial:  F = { empty set, X }",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        ex1_note = Text(
            "Smallest possible — not very useful",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        ex1 = VGroup(ex1_label, ex1_note).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        ensure_fits(ex1)
        self.ly.safe_place(ex1, anchor=title, buff=0.6)
        self.play(FadeIn(ex1, shift=LEFT * 0.15), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(ex1), run_time=0.4)

        ex2_label = Text(
            "Power set:  F = P(X)  (all subsets)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        ex2_note = Text(
            "Largest possible — always a sigma-algebra",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        ex2 = VGroup(ex2_label, ex2_note).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        ensure_fits(ex2)
        self.ly.safe_place(ex2, anchor=title, buff=0.6)
        self.play(FadeIn(ex2, shift=LEFT * 0.15), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(ex2), run_time=0.4)

        ex3_label = Text(
            "Countable / co-countable on R",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        ex3_desc = Text(
            "F = { A : A is countable } union { A : A^c is countable }",
            font_size=LABEL_SIZE, color=WHITE, font=SANS,
        )
        ex3 = VGroup(ex3_label, ex3_desc).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        ensure_fits(ex3)
        self.ly.safe_place(ex3, anchor=title, buff=0.6)
        self.play(FadeIn(ex3, shift=LEFT * 0.15), run_time=0.7)
        self.wait(1.0)

        verify = Text(
            "Verify: countable union of countable sets is countable",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        ensure_fits(verify)
        self.ly.safe_place(verify, anchor=ex3, buff=0.5)
        self.play(FadeIn(verify), run_time=0.5)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 5: The Borel Sigma-Algebra ~70s ---

    def scene5_borel(self):
        self.add_subcaption(
            "The most important sigma-algebra is the Borel "
            "sigma-algebra on the real line. The power set is "
            "too large because it contains non-measurable sets "
            "like Vitali sets. We need the smallest sigma-algebra "
            "containing all open intervals. This is B of R. "
            "It contains all open sets, all closed sets, "
            "and is closed under countable unions and "
            "intersections.",
            duration=70,
        )

        title = self.ly.title("The Borel Sigma-Algebra", color=ACCENT)

        motivation = Text(
            "Problem: P(R) is too large — contains non-measurable sets",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        ensure_fits(motivation)
        self.ly.safe_place(motivation, anchor=title, buff=0.6)
        self.play(FadeIn(motivation, shift=LEFT * 0.15), run_time=0.7)
        self.wait(1.0)

        solution = Text(
            "Solution: smallest sigma-algebra containing all open sets",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        ensure_fits(solution)
        self.ly.safe_place(solution, anchor=motivation, buff=0.5)
        self.play(FadeIn(solution, shift=LEFT * 0.15), run_time=0.7)
        self.wait(1.0)

        self.play(FadeOut(motivation), FadeOut(solution), run_time=0.4)

        borel_def = MathTex(
            r"\mathcal{B}(\mathbb{R})",
            r" = \sigma",
            r"(\text{open sets of } \mathbb{R})",
            font_size=HEADING_SIZE,
        )
        borel_def[0].set_color(ACCENT)
        borel_def[1].set_color(ACCENT)
        ensure_fits(borel_def)
        self.ly.center_in_content(borel_def)
        self.play(Write(borel_def), run_time=1.0)
        self.wait(1.0)

        generators = Text(
            "Equivalently generated by: open intervals, closed intervals, or half-open",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        ensure_fits(generators)
        self.ly.safe_place(generators, anchor=borel_def, buff=0.5)
        self.play(FadeIn(generators), run_time=0.5)
        self.wait(1.0)

        contains = Text(
            "Contains: open, closed, F-sigma, G-delta sets",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        ensure_fits(contains)
        self.ly.safe_place(contains, anchor=generators, buff=0.4)
        self.play(FadeIn(contains, shift=LEFT * 0.15), run_time=0.6)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 6: Generated Sigma-Algebras ~60s ---

    def scene6_generated(self):
        self.add_subcaption(
            "Given any collection C of subsets, there exists "
            "a smallest sigma-algebra containing C. We write "
            "this as sigma of C and define it as the intersection "
            "of all sigma-algebras that contain C. This is "
            "well-defined because the intersection of any "
            "family of sigma-algebras is itself a sigma-algebra. "
            "The Borel sigma-algebra is exactly sigma of the "
            "open intervals.",
            duration=60,
        )

        title = self.ly.title("Generated Sigma-Algebras", color=PRIMARY)

        gen_def = MathTex(
            r"\sigma(\mathcal{C})",
            r" = \bigcap \{ \mathcal{F} : \mathcal{C} \subseteq \mathcal{F}, \; \mathcal{F} \text{ is a } \sigma\text{-algebra} \}",
            font_size=BODY_SIZE,
        )
        gen_def[0].set_color(ACCENT)
        ensure_fits(gen_def)
        self.ly.safe_place(gen_def, anchor=title, buff=0.6)
        self.play(Write(gen_def), run_time=1.0)
        self.wait(1.0)

        well_def = Text(
            "Well-defined: intersection of sigma-algebras is a sigma-algebra",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        ensure_fits(well_def)
        self.ly.safe_place(well_def, anchor=gen_def, buff=0.5)
        self.play(FadeIn(well_def, shift=LEFT * 0.15), run_time=0.7)
        self.wait(1.0)

        proof1 = Text(
            "X is in every sigma-algebra, so X is in the intersection",
            font_size=LABEL_SIZE, color=WHITE, font=SANS,
        )
        ensure_fits(proof1)
        self.ly.safe_place(proof1, anchor=well_def, buff=0.4)
        self.play(FadeIn(proof1), run_time=0.5)
        self.wait(0.8)

        proof2 = Text(
            "Complements and countable unions pass through intersections",
            font_size=LABEL_SIZE, color=WHITE, font=SANS,
        )
        ensure_fits(proof2)
        self.ly.safe_place(proof2, anchor=proof1, buff=0.3)
        self.play(FadeIn(proof2), run_time=0.5)
        self.wait(1.0)

        borel_link = MathTex(
            r"\mathcal{B}(\mathbb{R}) = \sigma(\{ (a,b) : a < b \})",
            font_size=BODY_SIZE,
        )
        borel_link.set_color(ACCENT)
        ensure_fits(borel_link)
        self.ly.safe_place(borel_link, anchor=proof2, buff=0.5)
        self.play(Write(borel_link), run_time=0.8)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 7: Measurable Spaces ~45s ---

    def scene7_measurable_spaces(self):
        self.add_subcaption(
            "A measurable space is a pair X comma F where F is "
            "a sigma-algebra on X. We have not defined any "
            "measure yet. We are only specifying which sets are "
            "allowed to be measured. Think of a sigma-algebra "
            "as a menu and a measurable space as the restaurant. "
            "Different measures can live on the same measurable "
            "space, such as the Lebesgue measure, a probability "
            "measure, or the counting measure.",
            duration=45,
        )

        title = self.ly.title("Measurable Spaces", color=PRIMARY)

        defn = MathTex(
            r"(X, \mathcal{F})",
            r" \text{ is a measurable space}",
            font_size=HEADING_SIZE,
        )
        defn[0].set_color(PRIMARY)
        defn[1].set_color(WHITE)
        ensure_fits(defn)
        self.ly.safe_place(defn, anchor=title, buff=0.6)
        self.play(Write(defn), run_time=0.8)
        self.wait(0.8)

        note1 = Text(
            "Elements of F are called MEASURABLE sets",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        ensure_fits(note1)
        self.ly.safe_place(note1, anchor=defn, buff=0.5)
        self.play(FadeIn(note1, shift=LEFT * 0.15), run_time=0.7)
        self.wait(1.0)

        note2 = Text(
            "No measure defined yet — just the domain",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        ensure_fits(note2)
        self.ly.safe_place(note2, anchor=note1, buff=0.4)
        self.play(FadeIn(note2, shift=LEFT * 0.15), run_time=0.7)
        self.wait(1.0)

        analogy = Text(
            "Sigma-algebra = menu | Measurable space = restaurant | Measure = prices",
            font_size=LABEL_SIZE, color=ACCENT, font=SANS,
        )
        ensure_fits(analogy)
        self.ly.safe_place(analogy, anchor=note2, buff=0.5)
        self.play(FadeIn(analogy), run_time=0.5)
        self.wait(1.0)

        measures = Text(
            "Same space, different measures: Lebesgue, probability, counting",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        ensure_fits(measures)
        self.ly.safe_place(measures, anchor=analogy, buff=0.4)
        self.play(FadeIn(measures), run_time=0.5)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 8: Summary ~40s ---

    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap. An algebra of sets is closed under "
            "finite unions and complements. A sigma-algebra "
            "upgrades this to countable unions. The Borel "
            "sigma-algebra is the smallest sigma-algebra "
            "containing all open sets of the real line. The "
            "generated sigma-algebra sigma of C is the "
            "smallest sigma-algebra containing a given "
            "collection. And a measurable space is the "
            "pair X comma F that serves as the domain for "
            "measures. Next video: we define measures and "
            "integration on sigma-algebras.",
            duration=40,
        )

        title = self.ly.title("Summary", color=ACCENT)

        items = [
            Text("Algebra: finite unions + complements", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Sigma-algebra: COUNTABLE unions + complements", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("B(R): smallest sigma-algebra with open sets", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("sigma(C): generated by a collection C", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Measurable space (X, F): the domain for measures", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(
            items, start_from=title, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.8,
        )
        self.wait(1.0)

        self.ly.clear()
        play_outro(self)
