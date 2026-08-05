"""
Video 158: L^p Spaces — Measure Theory Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video158_LpSpaces

Topics: Measuring function "size" with L^p norms,
        From L^1 and L^2 to general L^p,
        Formal definition of L^p norm and L^p spaces,
        Examples: power functions, exponential decay,
        Holder's inequality (conjugate exponents),
        Minkowski's inequality (triangle inequality),
        Riesz-Fischer theorem (completeness = Banach spaces),
        L^2 is a Hilbert space,
        Big picture: nesting and connections to convergence theorems.

Prerequisites: Videos 151-157 (Measure Theory Intro through Convergence Theorems).

Competitive insights (from channel-analysis/improvements.md):
- Unlike TBSOM's static lecture format, we ANIMATE the p-norm concept
- Following 3B1B's intuition-first approach, we start with geometric motivation
- Connect to everything learned so far (Lebesgue integral, convergence theorems)
- Progressive disclosure: never more than 5 visual elements on screen

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


class Video158_LpSpaces(Scene):
    """L^p Spaces: Measuring the 'size' of a function"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_from_l1_to_l2()
        self.scene3_lp_norm_definition()
        self.scene4_examples()
        self.scene5_holder()
        self.scene6_minkowski()
        self.scene7_riesz_fischer()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook — Measuring the "size" of a function
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: How do we measure the 'size' of a function?"""
        self.add_subcaption(
            "In calculus, we measure a function's size by its integral. "
            "But what if the integral diverges? We need a richer framework.",
            duration=6,
        )
        play_intro(self, "L^p Spaces", "Measure Theory")

        title = self.ly.title("How do we measure the 'size' of a function?")

        items = [
            Text("L\u00B9 = area under the curve", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("L\u00B2 = energy of the function", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("L\u1D56 = the full generalization", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, wait_time=0.8)

        question = Text(
            "What makes a function 'small enough' to integrate?",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(question, direction=DOWN, anchor=items[-1], buff=0.4)
        self.play(FadeIn(question, shift=LEFT * 0.15))
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: From L^1 to L^2 — Building Intuition
    # ------------------------------------------------------------------
    def scene2_from_l1_to_l2(self):
        """Intuition: L^1 is area, L^2 is energy"""
        self.ly.section_divider(2, "From L\u00B9 to L\u00B2")

        self.add_subcaption(
            "We already know L\u00B9 \u2014 the Lebesgue integral. "
            "L\u00B2 appears everywhere in physics and signal processing.",
            duration=5,
        )

        title = self.ly.title("Two familiar spaces")

        l1_label = Text("L\u00B9", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        l1_formula = MathTex(
            r"\| f \|_1 = \int |f| \, d\mu",
            font_size=BODY_SIZE,
        )
        l1_desc = Text("measures area under |f|", font_size=LABEL_SIZE, color=DIM, font=SANS)
        l1_group = VGroup(l1_label, l1_formula, l1_desc).arrange(DOWN, buff=0.15)

        l2_label = Text("L\u00B2", font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        l2_formula = MathTex(
            r"\| f \|_2 = \left( \int |f|^2 \, d\mu \right)^{1/2}",
            font_size=BODY_SIZE,
        )
        l2_desc = Text("measures energy of f", font_size=LABEL_SIZE, color=DIM, font=SANS)
        l2_group = VGroup(l2_label, l2_formula, l2_desc).arrange(DOWN, buff=0.15)

        ensure_fits(l1_group, MAX_HALF_WIDTH, 2.5)
        ensure_fits(l2_group, MAX_HALF_WIDTH, 2.5)

        columns = self.ly.two_columns(
            [l1_group], [l2_group], start_from=title,
        )

        self.play(
            FadeIn(l1_group, shift=LEFT * 0.15),
            FadeIn(l2_group, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1)

        bridge = Text(
            "Can we generalize to any p?",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(bridge, direction=DOWN, anchor=l1_group, buff=0.6)
        self.play(Write(bridge), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: The L^p Norm — Definition
    # ------------------------------------------------------------------
    def scene3_lp_norm_definition(self):
        """Formal definition of L^p norm and L^p spaces"""
        self.ly.section_divider(3, "The L\u1D56 Norm")

        self.add_subcaption(
            "For a measurable function f and parameter p between 1 and infinity, "
            "we define the L to the p norm.",
            duration=5,
        )

        title = self.ly.title("Definition: L\u1D56 Norm")

        # Main definition
        def_formula = MathTex(
            r"\| f \|_p = \left( \int |f|^p \, d\mu \right)^{1/p}",
            font_size=HEADING_SIZE,
        )
        formula_box = self.ly.formula_box(def_formula, PRIMARY)
        self.ly.safe_place(formula_box, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(def_formula), run_time=NORMAL)
        self.wait(0.5)

        # Conditions
        conditions = [
            Text("f is measurable", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text(r"1 \leq p < \infty", font_size=BODY_SIZE, color=SECONDARY, font=MONO),
            Text(r"\int |f|^p \, d\mu < \infty", font_size=BODY_SIZE, color=ACCENT, font=MONO),
        ]
        self.ly.progressive_reveal(conditions, start_from=formula_box, wait_time=0.6)
        self.wait(1)

        # L^infinity case
        linf_label = Text("For p = \u221E:", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        linf_formula = MathTex(
            r"\| f \|_\infty = \text{ess\,sup}\, |f|",
            font_size=HEADING_SIZE,
        )
        self.ly.safe_place(linf_label, direction=DOWN, anchor=conditions[-1], buff=0.4)
        self.ly.safe_place(linf_formula, direction=DOWN, anchor=linf_label, buff=0.2)
        self.play(FadeIn(linf_label, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(linf_formula), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Key Examples
    # ------------------------------------------------------------------
    def scene4_examples(self):
        """Examples showing which L^p spaces different functions belong to"""
        self.ly.section_divider(4, "Examples")

        self.add_subcaption(
            "Let's see concrete examples. A function like x to the minus one-third "
            "lives in L to the p only when p is less than three.",
            duration=6,
        )

        title = self.ly.title("Which L\u1D56 spaces contain f?")

        # Example 1: power function
        ex1_label = Text("Example 1:", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        ex1_func = MathTex(r"f(x) = x^{-1/3}", r"\text{ on } (0, 1)", font_size=BODY_SIZE)
        ex1_result = MathTex(
            r"\int_0^1 x^{-p/3} \, dx < \infty",
            r"\iff",
            r"p < 3",
            font_size=BODY_SIZE,
        )
        ex1_conclusion = Text(
            "In L\u00B9 and L\u00B2, but NOT in L\u00B3 or L\u2074",
            font_size=LABEL_SIZE, color=RED, font=SANS,
        )

        items1 = [ex1_label, ex1_func, ex1_result, ex1_conclusion]
        self.ly.progressive_reveal(items1, start_from=title, wait_time=0.6)
        self.wait(1)

        self.ly.clear()

        # Example 2: exponential
        self.add_subcaption(
            "An exponentially decaying function lives in every L to the p space. "
            "Fast decay always helps.",
            duration=5,
        )

        title2 = self.ly.title("A function in ALL L\u1D56 spaces")

        ex2_label = Text("Example 2:", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        ex2_func = MathTex(r"f(x) = e^{-x}", r"\text{ on } [0, \infty)", font_size=BODY_SIZE)
        ex2_result = MathTex(
            r"\int_0^\infty e^{-px} \, dx = \frac{1}{p} < \infty",
            font_size=BODY_SIZE,
        )
        ex2_conclusion = Text(
            "Decays fast enough for ALL p \u2265 1",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )

        items2 = [ex2_label, ex2_func, ex2_result, ex2_conclusion]
        self.ly.progressive_reveal(items2, start_from=title2, wait_time=0.6)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Holder's Inequality
    # ------------------------------------------------------------------
    def scene5_holder(self):
        """Holder's inequality with conjugate exponents"""
        self.ly.section_divider(5, "Holder's Inequality")

        self.add_subcaption(
            "Holder's inequality is the engine behind L to the p spaces. "
            "It says the product of an L to the p and L to the q function is integrable.",
            duration=6,
        )

        title = self.ly.title("Holder's Inequality")

        # The statement
        holder_formula = MathTex(
            r"\| fg \|_1 \leq \| f \|_p \cdot \| g \|_q",
            font_size=HEADING_SIZE,
        )
        formula_box = self.ly.formula_box(holder_formula, PRIMARY)
        self.ly.safe_place(formula_box, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(holder_formula), run_time=NORMAL)
        self.wait(0.5)

        # Conjugate exponent condition
        conj_label = Text("Conjugate exponents:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        conj_formula = MathTex(
            r"\frac{1}{p} + \frac{1}{q} = 1",
            r"\quad",
            r"p, q \geq 1",
            font_size=BODY_SIZE,
        )
        self.ly.safe_place(conj_label, direction=DOWN, anchor=formula_box, buff=0.4)
        self.ly.safe_place(conj_formula, direction=DOWN, anchor=conj_label, buff=0.2)
        self.play(FadeIn(conj_label, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(conj_formula), run_time=NORMAL)
        self.wait(1)

        # Special case: Cauchy-Schwarz
        self.ly.clear()

        self.add_subcaption(
            "The special case when p equals q equals 2 gives us "
            "the Cauchy-Schwarz inequality for L squared.",
            duration=5,
        )

        title2 = self.ly.title("Special Case: Cauchy-Schwarz")

        cs_label = Text("When p = q = 2:", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        cs_formula = MathTex(
            r"\int |fg| \, d\mu \leq \left(\int |f|^2\right)^{1/2}"
            r"\left(\int |g|^2\right)^{1/2}",
            font_size=HEADING_SIZE,
        )
        cs_box = self.ly.formula_box(cs_formula, SECONDARY)
        self.ly.safe_place(cs_label, direction=DOWN, anchor=title2, buff=0.4)
        self.ly.safe_place(cs_box, direction=DOWN, anchor=cs_label, buff=0.2)
        self.play(FadeIn(cs_label, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(cs_formula), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Minkowski's Inequality
    # ------------------------------------------------------------------
    def scene6_minkowski(self):
        """Minkowski's inequality: the triangle inequality for L^p"""
        self.ly.section_divider(6, "Minkowski's Inequality")

        self.add_subcaption(
            "Minkowski's inequality is the triangle inequality for L to the p. "
            "This is what makes L to the p a genuine normed space.",
            duration=6,
        )

        title = self.ly.title("The Triangle Inequality for L\u1D56")

        mink_formula = MathTex(
            r"\| f + g \|_p \leq \| f \|_p + \| g \|_p",
            font_size=HEADING_SIZE,
        )
        formula_box = self.ly.formula_box(mink_formula, ACCENT)
        self.ly.safe_place(formula_box, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(mink_formula), run_time=NORMAL)
        self.wait(0.5)

        # Key insight: relies on Holder
        insight = Text(
            "Proof relies on Holder's inequality",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        normed = Text(
            "L\u1D56 is a Normed Vector Space!",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=formula_box, buff=0.4)
        self.ly.safe_place(normed, direction=DOWN, anchor=insight, buff=0.4)
        self.play(
            FadeIn(insight, shift=LEFT * 0.15),
            FadeIn(normed, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Riesz-Fischer — L^p is Complete
    # ------------------------------------------------------------------
    def scene7_riesz_fischer(self):
        """Completeness: Riesz-Fischer Theorem"""
        self.ly.section_divider(7, "Riesz-Fischer Theorem")

        self.add_subcaption(
            "A deep result: every Cauchy sequence in L to the p converges. "
            "This means L to the p is a Banach space.",
            duration=5,
        )

        title = self.ly.title("L\u1D56 is Complete")

        theorem = Text(
            "Every Cauchy sequence in L\u1D56 converges to a limit in L\u1D56.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        consequence1 = Text(
            "L\u1D56 is a Banach space (complete normed space)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        consequence2 = Text(
            "L\u00B2 is a Hilbert space (has an inner product!)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        inner_product = MathTex(
            r"\langle f, g \rangle = \int f \cdot \bar{g} \, d\mu",
            font_size=BODY_SIZE,
        )

        items = [theorem, consequence1, consequence2, inner_product]
        self.ly.progressive_reveal(items, start_from=title, wait_time=0.8)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Summary + Outro
    # ------------------------------------------------------------------
    def scene8_summary_outro(self):
        """Big picture and outro"""
        self.add_subcaption(
            "On finite measure spaces, L to the p spaces nest inside each other. "
            "Combined with the convergence theorems, L to the p is the natural home for analysis.",
            duration=6,
        )

        title = self.ly.title("The Big Picture")

        # Nesting on finite measure
        nesting = MathTex(
            r"L^\infty \hookrightarrow L^q \hookrightarrow L^p \hookrightarrow L^1",
            font_size=BODY_SIZE,
        )
        condition = Text("(for finite measure, when q > p)", font_size=LABEL_SIZE, color=DIM, font=SANS)

        # Key takeaways
        takeaways = [
            Text("L\u1D56 norm measures function 'size' via |f|^p", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Holder \u2192 Minkowski \u2192 completeness", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("L\u00B2 is a Hilbert space \u2014 central to quantum mechanics", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]

        self.ly.safe_place(nesting, direction=DOWN, anchor=title, buff=0.4)
        self.ly.safe_place(condition, direction=DOWN, anchor=nesting, buff=0.15)
        self.play(Write(nesting), FadeIn(condition, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        self.ly.progressive_reveal(takeaways, start_from=condition, wait_time=0.7)
        self.wait(1)

        self.ly.clear()

        play_outro(self, "Radon-Nikodym Theorem", "Measure Theory")
