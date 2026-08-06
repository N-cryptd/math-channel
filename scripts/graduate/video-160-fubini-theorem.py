"""
Video 160: Fubini's Theorem — Measure Theory Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video160_FubiniTheorem

Topics: Motivation: double integrals in measure theory,
        Product sigma-algebras (Sigma_X tensor Sigma_Y),
        Construction of product measures,
        Fubini's Theorem (L^1 functions, iterated integrals),
        Tonelli's Theorem (non-negative measurable functions),
        Fubini-Tonelli strategy (when to apply which),
        Worked example: Gaussian double integral,
        Counterexample: when Fubini fails (non-integrable case),
        Summary and connection to Lebesgue vs Riemann.

Prerequisites: Videos 151-158 (Measure Theory through L^p Spaces),
              Video 159 (Radon-Nikodym Theorem).

Competitive insights: Analysis skipped (youtubei.js search returned minimal data).
Plan draws on standard exposition (Folland, Royden, Rudin).

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


class Video160_FubiniTheorem(Scene):
    """Product Measures and Fubini's Theorem"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_product_sigma_algebra()
        self.scene3_product_measures()
        self.scene4_fubini_theorem()
        self.scene5_tonelli_theorem()
        self.scene6_strategy()
        self.scene7_worked_example()
        self.scene8_counterexample()
        self.scene9_summary_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook — The Double Integral Question
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: When can we swap the order of integration?"""
        self.add_subcaption(
            "In calculus, we computed double integrals by iterating. "
            "But when does this actually work in the Lebesgue setting?",
            duration=6,
        )
        play_intro(self, "Fubini's Theorem", "Measure Theory")

        title = self.ly.title("Can we swap the order of integration?")

        # Motivation: two ways to integrate
        formula1 = MathTex(
            r"\int_{X} \!\int_{Y} f \; d\nu \; d\mu",
            font_size=HEADING_SIZE,
            color=PRIMARY,
        )
        vs = Text("  vs  ", font_size=BODY_SIZE, color=DIM, font=SANS)
        formula2 = MathTex(
            r"\int_{Y} \!\int_{X} f \; d\mu \; d\nu",
            font_size=HEADING_SIZE,
            color=SECONDARY,
        )
        row = VGroup(formula1, vs, formula2).arrange(RIGHT, buff=0.2)
        ensure_fits(row, MAX_HALF_WIDTH, 1.0)
        self.ly.safe_place(row, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(formula1), Write(formula2), run_time=NORMAL)
        self.wait(0.5)

        # Three key questions
        items = [
            Text("Do iterated integrals equal the product integral?", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Can we swap the order of integration?", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("What conditions guarantee this?", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=row, wait_time=0.8)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Product Sigma-Algebras
    # ------------------------------------------------------------------
    def scene2_product_sigma_algebra(self):
        """Definition of product sigma-algebra"""
        self.ly.section_divider(2, "Product Sigma-Algebras")

        self.add_subcaption(
            "To integrate over a product space, we first need "
            "a sigma-algebra on X cross Y.",
            duration=5,
        )

        title = self.ly.title("Sigma-X tensor Sigma-Y")

        # Definition
        def_text = Text("Definition:", font_size=HEADING_SIZE, color=WHITE, font=SANS)
        def_formula = MathTex(
            r"\Sigma_X \otimes \Sigma_Y "
            r"= \sigma\!\left(\{A \times B : A \in \Sigma_X,\; B \in \Sigma_Y\}\right)",
            font_size=BODY_SIZE,
            color=PRIMARY,
        )
        formula_box = self.ly.formula_box(def_formula, PRIMARY)
        self.ly.safe_place(def_text, direction=DOWN, anchor=title, buff=0.4)
        self.ly.safe_place(formula_box, direction=DOWN, anchor=def_text, buff=0.3)
        self.play(FadeIn(def_text, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(def_formula), run_time=NORMAL)
        self.wait(0.5)

        # Key properties
        self.play(FadeOut(def_text))

        prop1 = Text(
            "Smallest sigma-algebra containing all measurable rectangles",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        prop2 = Text(
            "Generates the product topology for topological spaces",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.progressive_reveal([prop1, prop2], start_from=formula_box, wait_time=0.6)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Product Measures
    # ------------------------------------------------------------------
    def scene3_product_measures(self):
        """Construction of product measures"""
        self.ly.section_divider(3, "Product Measures")

        self.add_subcaption(
            "A product measure assigns to each rectangle the product "
            "of its side measures, then extends via Caratheodory.",
            duration=6,
        )

        title = self.ly.title("Building mu times nu")

        # Core definition
        core_label = Text("On measurable rectangles:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        core_formula = MathTex(
            r"(\mu \times \nu)(A \times B) = \mu(A) \cdot \nu(B)",
            font_size=HEADING_SIZE,
            color=PRIMARY,
        )
        formula_box = self.ly.formula_box(core_formula, PRIMARY)
        self.ly.safe_place(core_label, direction=DOWN, anchor=title, buff=0.4)
        self.ly.safe_place(formula_box, direction=DOWN, anchor=core_label, buff=0.3)
        self.play(
            FadeIn(core_label, shift=LEFT * 0.15),
            Write(core_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Extension
        self.play(FadeOut(core_label))

        ext1 = Text(
            "Extended to all of Sigma-X tensor Sigma-Y via Caratheodory",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(ext1, direction=DOWN, anchor=formula_box, buff=0.4)
        self.play(FadeIn(ext1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Sigma-finite condition
        ext2 = Text(
            "Unique when both mu and nu are sigma-finite",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(ext2, direction=DOWN, anchor=ext1, buff=0.3)
        self.play(FadeIn(ext2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Fubini's Theorem
    # ------------------------------------------------------------------
    def scene4_fubini_theorem(self):
        """Statement of Fubini's theorem"""
        self.ly.section_divider(4, "Fubini's Theorem")

        self.add_subcaption(
            "Fubini's theorem says that for integrable functions, "
            "the iterated integrals equal the product integral, "
            "and the order can be swapped.",
            duration=7,
        )

        title = self.ly.title("Fubini's Theorem")

        # Hypotheses
        hyp1 = Text("(X, Sigma-X, mu) and (Y, Sigma-Y, nu) are sigma-finite", font_size=BODY_SIZE, color=WHITE, font=SANS)
        hyp2 = Text("f in L-one of mu times nu", font_size=BODY_SIZE, color=WHITE, font=SANS)

        self.ly.progressive_reveal([hyp1, hyp2], start_from=title, wait_time=0.6)
        self.wait(0.3)

        # The theorem statement
        theorem = MathTex(
            r"\int_{X \times Y} f \; d(\mu \times \nu)",
            font_size=HEADING_SIZE,
            color=PRIMARY,
        )
        equals = MathTex(r"=", font_size=HEADING_SIZE, color=WHITE)
        iterated = MathTex(
            r"\int_{X}\!\left[\int_{Y} f(x,y) \; d\nu(y)\right] d\mu(x)",
            font_size=HEADING_SIZE,
            color=SECONDARY,
        )
        row = VGroup(theorem, equals, iterated).arrange(RIGHT, buff=0.2)
        ensure_fits(row, MAX_HALF_WIDTH, 1.5)
        boxed = self.ly.formula_box(row, PRIMARY)
        self.ly.safe_place(boxed, direction=DOWN, anchor=hyp2, buff=0.5)
        self.play(Write(row), run_time=NORMAL)
        self.wait(0.5)

        # Swap property
        self.play(FadeOut(hyp1), FadeOut(hyp2))

        swap = Text(
            "Order can be swapped: dx dy = dy dx",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(swap, direction=DOWN, anchor=boxed, buff=0.4)
        self.play(FadeIn(swap, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        caveat = Text(
            "Integrand is mu-a.e. and nu-a.e. measurable as a slice function",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(caveat, direction=DOWN, anchor=swap, buff=0.2)
        self.play(FadeIn(caveat, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Tonelli's Theorem
    # ------------------------------------------------------------------
    def scene5_tonelli_theorem(self):
        """Tonelli's theorem for non-negative functions"""
        self.ly.section_divider(5, "Tonelli's Theorem")

        self.add_subcaption(
            "Tonelli's theorem handles non-negative measurable functions. "
            "It doesn't require integrability, but guarantees that "
            "all iterated integrals are well-defined and equal.",
            duration=8,
        )

        title = self.ly.title("Tonelli's Theorem")

        # Key difference
        diff = Text(
            "For f >= 0 measurable (not necessarily integrable!):",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(diff, direction=DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(diff, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Theorem statement
        theorem = MathTex(
            r"\int f \; d(\mu \times \nu)"
            r"= \int_X\!\left[\int_Y f \; d\nu\right] d\mu"
            r"= \int_Y\!\left[\int_X f \; d\mu\right] d\nu",
            font_size=BODY_SIZE,
            color=SECONDARY,
        )
        boxed = self.ly.formula_box(theorem, SECONDARY)
        self.ly.safe_place(boxed, direction=DOWN, anchor=diff, buff=0.4)
        self.play(Write(theorem), run_time=NORMAL)
        self.wait(0.5)

        # Complementarity note
        self.play(FadeOut(diff))

        note_label = Text("Complementary roles:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        note_tonelli = Text(
            "Tonelli: proves integrability (finite value)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        note_fubini = Text(
            "Fubini: computes the value and swaps order",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(note_label, direction=DOWN, anchor=boxed, buff=0.4)
        self.ly.progressive_reveal([note_tonelli, note_fubini], start_from=note_label, wait_time=0.6)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Fubini-Tonelli Strategy
    # ------------------------------------------------------------------
    def scene6_strategy(self):
        """Practical strategy for applying both theorems"""
        self.ly.section_divider(6, "Fubini-Tonelli Strategy")

        self.add_subcaption(
            "In practice, you combine both theorems. "
            "Use Tonelli on the absolute value first to check integrability, "
            "then apply Fubini to compute and swap.",
            duration=7,
        )

        title = self.ly.title("The Practical Workflow")

        # Step 1
        step1 = VGroup(
            Text("Step 1: ", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Check f >= 0?", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ).arrange(RIGHT, buff=0.1)
        detail1 = Text(
            "Apply Tonelli on |f| to test integrability",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        g1 = VGroup(step1, detail1).arrange(DOWN, buff=0.05)

        # Step 2
        step2 = VGroup(
            Text("Step 2: ", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Is f in L-one?", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ).arrange(RIGHT, buff=0.1)
        detail2 = Text(
            "Apply Fubini to swap and compute freely",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        g2 = VGroup(step2, detail2).arrange(DOWN, buff=0.05)

        # Step 3
        step3 = VGroup(
            Text("Step 3: ", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Sign-changing f?", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ).arrange(RIGHT, buff=0.1)
        detail3 = Text(
            "Tonelli on |f| first, then Fubini on f",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        g3 = VGroup(step3, detail3).arrange(DOWN, buff=0.05)

        items = [g1, g2, g3]
        self.ly.progressive_reveal(items, start_from=title, wait_time=0.8)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Worked Example
    # ------------------------------------------------------------------
    def scene7_worked_example(self):
        """Gaussian double integral example"""
        self.ly.section_divider(7, "Worked Example")

        self.add_subcaption(
            "Let's compute the Gaussian double integral "
            "over R-squared using Fubini's theorem.",
            duration=5,
        )

        title = self.ly.title("Gaussian on R-squared")

        # Setup
        setup = MathTex(
            r"I = \int_{\mathbb{R}^2} e^{-(x^2+y^2)} \; d(x \times \lambda)",
            font_size=HEADING_SIZE,
            color=PRIMARY,
        )
        formula_box = self.ly.formula_box(setup, PRIMARY)
        self.ly.safe_place(formula_box, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(setup), run_time=NORMAL)
        self.wait(0.5)

        # Factor
        factor = MathTex(
            r"= \int_{\mathbb{R}} e^{-x^2} dx \;\cdot\; "
            r"\int_{\mathbb{R}} e^{-y^2} dy "
            r"= \left(\sqrt{\pi}\right)^2 = \pi",
            font_size=BODY_SIZE,
            color=SECONDARY,
        )
        self.ly.safe_place(factor, direction=DOWN, anchor=formula_box, buff=0.4)
        self.play(Write(factor), run_time=NORMAL)
        self.wait(0.5)

        # Inner integral
        self.play(FadeOut(factor))

        inner_label = Text("The inner integral (Gaussian):", font_size=BODY_SIZE, color=WHITE, font=SANS)
        inner_formula = MathTex(
            r"\int_{-\infty}^{\infty} e^{-t^2} \; dt = \sqrt{\pi}",
            font_size=HEADING_SIZE,
            color=ACCENT,
        )
        boxed2 = self.ly.formula_box(inner_formula, ACCENT)
        self.ly.safe_place(inner_label, direction=DOWN, anchor=formula_box, buff=0.4)
        self.ly.safe_place(boxed2, direction=DOWN, anchor=inner_label, buff=0.3)
        self.play(
            FadeIn(inner_label, shift=LEFT * 0.15),
            Write(inner_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Note about Tonelli
        self.play(FadeOut(inner_label))

        note = Text(
            "Tonelli applies: e^(-x^2-y^2) >= 0 everywhere",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=boxed2, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Counterexample — When Fubini Fails
    # ------------------------------------------------------------------
    def scene8_counterexample(self):
        """Counterexample showing L-one hypothesis is essential"""
        self.ly.section_divider(8, "When Fubini Fails")

        self.add_subcaption(
            "If f is not integrable, the iterated integrals can "
            "give different values! Here's a famous counterexample.",
            duration=6,
        )

        title = self.ly.title("A Counterexample")

        # The function
        func_label = Text("On [0,1] x [0,1], let:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        func_formula = MathTex(
            r"f(x,y) = \frac{x^2 - y^2}{(x^2 + y^2)^2}",
            font_size=HEADING_SIZE,
            color=RED,
        )
        boxed = self.ly.formula_box(func_formula, RED)
        self.ly.safe_place(func_label, direction=DOWN, anchor=title, buff=0.4)
        self.ly.safe_place(boxed, direction=DOWN, anchor=func_label, buff=0.3)
        self.play(
            FadeIn(func_label, shift=LEFT * 0.15),
            Write(func_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # The two iterated integrals
        self.play(FadeOut(func_label))

        int1 = MathTex(
            r"\int_0^1\!\!\int_0^1 f \; dy\,dx = \frac{\pi}{4}",
            font_size=BODY_SIZE,
            color=PRIMARY,
        )
        int2 = MathTex(
            r"\int_0^1\!\!\int_0^1 f \; dx\,dy = -\frac{\pi}{4}",
            font_size=BODY_SIZE,
            color=SECONDARY,
        )
        self.ly.safe_place(int1, direction=DOWN, anchor=boxed, buff=0.4)
        self.ly.safe_place(int2, direction=DOWN, anchor=int1, buff=0.2)
        self.play(Write(int1), Write(int2), run_time=NORMAL)
        self.wait(0.5)

        # Why?
        self.play(FadeOut(int1), FadeOut(int2))

        why = Text(
            "f is NOT in L-one: the integral of |f| diverges!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(why, direction=DOWN, anchor=boxed, buff=0.4)
        self.play(FadeIn(why, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        lesson = Text(
            "The L-one hypothesis in Fubini is essential",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(lesson, direction=DOWN, anchor=why, buff=0.3)
        self.play(FadeIn(lesson, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Summary + Outro
    # ------------------------------------------------------------------
    def scene9_summary_outro(self):
        """Summary and next video tease"""
        self.ly.section_divider(9, "Summary")

        self.add_subcaption(
            "Fubini and Tonelli give us the measure-theoretic "
            "foundation for iterated integrals and swapping orders. "
            "These theorems generalize everything from multivariable calculus.",
            duration=8,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text("Product sigma-algebra generated by measurable rectangles", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Tonelli: non-negative functions, establishes integrability", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Fubini: L-one functions, equals product integral + swap", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Strategy: Tonelli on |f|, then Fubini on f", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title, wait_time=0.8)
        self.wait(1.5)

        self.ly.clear()

        play_outro(self, "Lebesgue vs Riemann", "Measure Theory")
