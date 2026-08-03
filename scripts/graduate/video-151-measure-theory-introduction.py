"""
Video 151: Measure Theory Introduction ("Why Measure Theory?")
TEMPLATE v2 -- Professional quality Manim script

Class: Video151_MeasureTheoryIntro

Topics: Motivation for measure theory, the Riemann integral's limitations,
        examples of measures, the measure theory roadmap.

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


class Video151_MeasureTheoryIntro(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_what_is_measure()
        self.scene3_riemann_limits()
        self.scene4_examples_of_measures()
        self.scene5_roadmap()
        self.scene6_why_matters()
        self.scene7_summary()

    # --- Scene 1: Hook — "The Problem of Size" ~50s ---

    def scene1_hook(self):
        self.add_subcaption(
            "Every civilization that studied mathematics asked the "
            "same question. How big is this shape? The Greeks measured "
            "lengths and areas. Newton and Leibniz gave us calculus "
            "to measure curves. But what about the size of more "
            "general sets? Today we begin the story of measure "
            "theory, the mathematics of size itself.",
            duration=50,
        )
        play_intro(self, "Why Measure Theory?", "Measure Theory")

        title = self.ly.title("The Problem of Size", color=ACCENT)

        items = [
            Text("Ancient Egypt: surveying land after the Nile floods",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Greek geometry: lengths, areas, and volumes",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Calculus: measuring curves and areas under curves",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Measure theory: the mathematics of SIZE itself",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(
            items, start_from=title, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.7, wait_time=1.2,
        )
        self.wait(1.0)
        self.ly.clear()

    # --- Scene 2: What is a Measure? — Intuition First ~60s ---

    def scene2_what_is_measure(self):
        self.add_subcaption(
            "A measure is a function that assigns a non-negative "
            "number to a set, representing its size. Think of "
            "length for intervals on a line, area for shapes in "
            "the plane, or probability for events. There are "
            "three simple requirements. The measure of nothing "
            "is zero. Measures are never negative. And the "
            "measure of a disjoint union is the sum of the "
            "individual measures. These three ideas are the "
            "foundation of all measure theory.",
            duration=60,
        )
        self.ly.section_divider(1, "What is a Measure?")

        title = self.ly.title("What is a Measure?", color=PRIMARY)

        defn = Text(
            "A measure assigns a non-negative number to a set",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        ensure_fits(defn)
        self.ly.safe_place(defn, anchor=title, buff=0.5)
        self.play(FadeIn(defn, shift=LEFT * 0.15), run_time=0.7)
        self.wait(0.8)

        # Number line visualization with highlighted interval
        ax = NumberLine(
            x_range=[0, 5, 1], length=6,
            color=DIM, font_size=LABEL_SIZE,
        )
        # Highlighted interval [1, 3] using a rectangle overlay
        interval_rect = Rectangle(
            width=2.4, height=0.3,
            color=PRIMARY, fill_opacity=0.4,
            stroke_width=0,
        )
        interval_rect.move_to(ax.n2p(2))

        length_label = MathTex(
            r"\mu([1, 3]) = 2",
            font_size=BODY_SIZE,
        )
        length_label[0].set_color(ACCENT)
        self.ly.safe_place(length_label, anchor=ax, direction=DOWN, buff=0.5)

        group = VGroup(ax, interval_rect, length_label)
        ensure_fits(group)
        self.ly.safe_place(group, anchor=defn, buff=0.6)

        self.play(
            FadeOut(defn),
            Create(ax),
            FadeIn(interval_rect),
            run_time=0.8,
        )
        self.play(Write(length_label), run_time=0.6)
        self.wait(1.0)

        # Three axioms — formal definition with formula_box
        self.play(
            FadeOut(group),
            run_time=0.5,
        )
        self.wait(0.3)

        axioms = MathTex(
            r"\mu(\emptyset) = 0",
            r",\;\;",
            r"\mu(A) \geq 0",
            r",\;\;",
            r"\mu\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} \mu(A_i)",
            font_size=BODY_SIZE,
        )
        axioms[0].set_color(ACCENT)
        axioms[2].set_color(SECONDARY)
        axioms[4].set_color(PRIMARY)
        axioms_box = self.ly.formula_box(axioms, color=ACCENT)
        ensure_fits(axioms_box)
        self.ly.center_in_content(axioms_box)
        self.play(Write(axioms_box), run_time=1.2)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 3: The Riemann Integral's Limitations ~70s ---

    def scene3_riemann_limits(self):
        self.add_subcaption(
            "You already know one measure: the Riemann integral "
            "gives the area under a curve. But the Riemann "
            "integral has a fatal flaw. It only works for "
            "nice functions. Consider the Dirichlet function on "
            "the interval zero to one. It equals one at every "
            "rational number and zero at every irrational number. "
            "Every Riemann sum is one, but the function is zero "
            "almost everywhere. The Riemann integral says the "
            "area is one, but the function is essentially zero. "
            "This makes no sense. We need a better theory.",
            duration=70,
        )
        self.ly.section_divider(2, "The Riemann Integral's Flaw")

        title = self.ly.title("The Riemann Integral's Flaw", color=RED)

        # Show Riemann working well
        riemann_ok = Text(
            "For smooth functions, Riemann integration works perfectly",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        ensure_fits(riemann_ok)
        self.ly.safe_place(riemann_ok, anchor=title, buff=0.5)
        self.play(FadeIn(riemann_ok, shift=LEFT * 0.15), run_time=0.7)
        self.wait(1.0)
        self.play(FadeOut(riemann_ok), run_time=0.4)

        # Introduce the Dirichlet function
        problem = Text(
            "But what about the Dirichlet function?",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        ensure_fits(problem)
        self.ly.safe_place(problem, anchor=title, buff=0.5)
        self.play(Write(problem), run_time=0.8)
        self.wait(0.5)

        # The Dirichlet function definition
        dirichlet = MathTex(
            r"f(x) = \begin{cases} 1 & \text{if } x \in \mathbb{Q} \\ 0 & \text{if } x \notin \mathbb{Q} \end{cases}",
            font_size=BODY_SIZE,
        )
        dirichlet[0].set_color(WHITE)
        dirichlet_box = self.ly.formula_box(dirichlet, color=RED)
        ensure_fits(dirichlet_box)
        self.ly.safe_place(dirichlet_box, anchor=problem, buff=0.5)
        self.play(Write(dirichlet_box), run_time=1.0)
        self.wait(0.8)

        # The contradiction
        contradiction = Text(
            "Riemann integral = 1  (every sum picks rationals)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        ensure_fits(contradiction)
        self.ly.safe_place(contradiction, anchor=dirichlet, buff=0.5)
        self.play(FadeIn(contradiction, shift=LEFT * 0.15), run_time=0.6)
        self.wait(0.8)

        but = Text(
            "But f(x) = 0 almost everywhere (rationals are measure zero!)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        ensure_fits(but)
        self.ly.safe_place(but, anchor=contradiction, buff=0.4)
        self.play(FadeIn(but, shift=LEFT * 0.15), run_time=0.6)
        self.wait(1.0)

        conclusion = Text(
            "The Riemann integral CANNOT handle this!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        ensure_fits(conclusion)
        self.ly.center_in_content(conclusion)
        self.play(
            *[FadeOut(m) for m in [problem, dirichlet_box, contradiction, but]],
            Write(conclusion),
            run_time=0.8,
        )
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 4: Examples of Measures ~70s ---

    def scene4_examples_of_measures(self):
        self.add_subcaption(
            "Let us look at three examples of measures. The "
            "counting measure simply counts the number of "
            "elements in a set. The Lebesgue measure on the "
            "real line gives the total length of a set. And "
            "the probability measure assigns sizes to events, "
            "with the whole sample space having measure one. "
            "Each satisfies the same three properties, but "
            "they measure very different kinds of size. The "
            "power of measure theory is that one framework "
            "handles all of these.",
            duration=70,
        )
        self.ly.section_divider(3, "Examples of Measures")

        title = self.ly.title("Examples of Measures", color=PRIMARY)

        # Example 1: Counting measure
        ex1_label = Text(
            "1. Counting Measure",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        ex1_formula = MathTex(
            r"\mu(A) = |A|", r"  (number of elements)",
            font_size=BODY_SIZE,
        )
        ex1_formula[0].set_color(ACCENT)
        ex1_note = Text(
            "Works for any set, finite or infinite",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        ex1_group = VGroup(ex1_label, ex1_formula, ex1_note).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT,
        )
        ensure_fits(ex1_group)
        self.ly.safe_place(ex1_group, anchor=title, buff=0.5)
        self.play(FadeIn(ex1_group, shift=LEFT * 0.15), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(ex1_group), run_time=0.4)

        # Example 2: Lebesgue measure
        ex2_label = Text(
            "2. Lebesgue Measure",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        ex2_formula = MathTex(
            r"m(A)", r" = total length of A on the real line",
            font_size=BODY_SIZE,
        )
        ex2_formula[0].set_color(ACCENT)
        ex2_note = Text(
            "The natural generalization of length, area, volume",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        ex2_group = VGroup(ex2_label, ex2_formula, ex2_note).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT,
        )
        ensure_fits(ex2_group)
        self.ly.safe_place(ex2_group, anchor=title, buff=0.5)
        self.play(FadeIn(ex2_group, shift=LEFT * 0.15), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(ex2_group), run_time=0.4)

        # Example 3: Probability measure
        ex3_label = Text(
            "3. Probability Measure",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        ex3_formula = MathTex(
            r"P(\Omega) = 1", r",  P(A) \in [0, 1]",
            font_size=BODY_SIZE,
        )
        ex3_formula[0].set_color(ACCENT)
        ex3_note = Text(
            "All of probability theory is measure theory!",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        ex3_group = VGroup(ex3_label, ex3_formula, ex3_note).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT,
        )
        ensure_fits(ex3_group)
        self.ly.safe_place(ex3_group, anchor=title, buff=0.5)
        self.play(FadeIn(ex3_group, shift=LEFT * 0.15), run_time=0.7)
        self.wait(1.5)

        # Unifying point
        unify = Text(
            "One framework handles ALL of these!",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        unify_box = self.ly.formula_box(unify, color=ACCENT)
        ensure_fits(unify_box)
        self.ly.safe_place(unify_box, anchor=ex3_group, buff=0.6)
        self.play(Write(unify_box), run_time=0.6)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 5: The Measure Theory Roadmap ~60s ---

    def scene5_roadmap(self):
        self.add_subcaption(
            "Here is our journey through measure theory. "
            "First, sigma-algebras tell us which sets we are "
            "allowed to measure. Then we define the measure "
            "function itself. After that, measurable functions "
            "are the functions compatible with our measure. "
            "The Lebesgue integral is a better integral that "
            "fixes the Riemann integral's flaws. Convergence "
            "theorems tell us when we can swap limits and "
            "integrals. And finally, Lp spaces give us "
            "complete function spaces with measures.",
            duration=60,
        )
        self.ly.section_divider(4, "The Measure Theory Roadmap")

        title = self.ly.title("The Measure Theory Roadmap", color=ACCENT)

        items = [
            Text("1. Sigma-Algebras: which sets can we measure?",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Measures: the function that assigns sizes",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Measurable Functions: compatible with our measure",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("4. The Lebesgue Integral: fixing Riemann's flaws",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("5. Convergence Theorems: limits and integrals",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(
            items, start_from=title, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.8,
        )
        self.wait(1.0)

        # Additional items
        more = [
            Text("6. Lp Spaces: complete function spaces",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(
            more, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.8,
        )
        self.wait(1.0)

        foundation = Text(
            "This is the foundation of modern analysis and probability!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        ensure_fits(foundation)
        self.ly.center_in_content(foundation)
        self.play(
            *[FadeOut(m) for m in self.mobjects if not hasattr(m, '_is_background')],
            Write(foundation),
            run_time=0.8,
        )
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 6: Why This Matters ~50s ---

    def scene6_why_matters(self):
        self.add_subcaption(
            "Measure theory is not abstract for its own sake. "
            "Probability theory is built entirely on measure "
            "theory, as Kolmogorov showed in nineteen thirty "
            "three. Quantum mechanics uses measures to define "
            "expectation values. Signal processing relies on "
            "Lebesgue integration. And machine learning and "
            "statistics need measure-theoretic foundations. "
            "If you want to understand probability rigorously, "
            "you need measure theory.",
            duration=50,
        )
        self.ly.section_divider(5, "Why This Matters")

        title = self.ly.title("Why This Matters", color=RED)

        items = [
            Text("Probability theory is built on measure theory (Kolmogorov, 1933)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Quantum mechanics uses measures for expectation values",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Signal processing relies on Lebesgue integration",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Machine learning and statistics need measure-theoretic foundations",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(
            items, start_from=title, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.7, wait_time=1.0,
        )
        self.wait(1.0)

        takeaway = Text(
            "To understand probability rigorously, you need measure theory",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        ensure_fits(takeaway)
        self.ly.center_in_content(takeaway)
        self.play(
            *[FadeOut(m) for m in self.mobjects if not hasattr(m, '_is_background')],
            Write(takeaway),
            run_time=0.8,
        )
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 7: Summary and Next Steps ~45s ---

    def scene7_summary(self):
        self.add_subcaption(
            "Let us recap. A measure assigns a size to a set. "
            "The Riemann integral is one measure, but it has "
            "serious limitations. Measure theory provides a "
            "unified framework for length, area, probability, "
            "and more. We need sigma-algebras to define which "
            "sets we can measure. Next video: sigma-algebras, "
            "the family of sets we are allowed to measure.",
            duration=45,
        )
        self.ly.section_divider(6, "Summary")

        title = self.ly.title("Summary", color=ACCENT)

        items = [
            Text("A measure assigns a SIZE to a set",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The Riemann integral is one measure with limitations",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Measure theory unifies length, area, probability, and more",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("We need sigma-algebras to define which sets to measure",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Next: Sigma-Algebras",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            items, start_from=title, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()
        play_outro(self)
