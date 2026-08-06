"""
Video 159: Radon-Nikodym Theorem — Measure Theory Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video159_RadonNikodym

Topics: Motivation: "derivative" of one measure w.r.t. another,
        Absolute continuity of measures (nu << mu),
        The Radon-Nikodym theorem (statement + uniqueness),
        Properties of the RN derivative (chain rule, linearity, inverse),
        Concrete example: probability density as RN derivative,
        Lebesgue decomposition theorem (brief bridge),
        Applications: change of measure, likelihood ratios, KL divergence,
        Summary and next steps.

Prerequisites: Videos 151-158 (Measure Theory Intro through L^p Spaces).

Competitive insights (from channel-analysis/improvements.md):
- Following Cofiber's motivation-first approach, we start with the density concept
- TBSOM's signed measures -> Hahn -> Lebesgue -> RN pipeline informs our structure
- Unlike Denis Potapov's chalk-and-talk, we ANIMATE absolute continuity
- Probability connection (dQ/dP) from Alon Sela makes it memorable
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


class Video159_RadonNikodym(Scene):
    """Radon-Nikodym Theorem: The Derivative of a Measure"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_absolute_continuity()
        self.scene3_theorem_statement()
        self.scene4_properties()
        self.scene5_probability_example()
        self.scene6_lebesgue_decomposition()
        self.scene7_applications()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook — The "Derivative" of a Measure
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: How do we differentiate a measure?"""
        self.add_subcaption(
            "In calculus, the derivative tells us how a function changes locally. "
            "What about measures? Can we define d nu over d mu?",
            duration=6,
        )
        play_intro(self, "Radon-Nikodym Theorem", "Measure Theory")

        title = self.ly.title("Can we differentiate a measure?")

        # The motivation equation
        motivation = MathTex(
            r"\nu(A) = \int_A f \; d\mu",
            font_size=HEADING_SIZE,
        )
        self.ly.safe_place(motivation, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(motivation), run_time=NORMAL)
        self.wait(0.5)

        # Three items
        items = [
            Text("If this holds, f = d\u03BD/d\u03BC", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("This f is the Radon-Nikodym derivative", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("When does such an f always exist?", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=motivation, wait_time=0.8)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Absolute Continuity of Measures
    # ------------------------------------------------------------------
    def scene2_absolute_continuity(self):
        """Definition and intuition for absolute continuity"""
        self.ly.section_divider(2, "Absolute Continuity")

        self.add_subcaption(
            "Before stating the theorem, we need the key condition: "
            "absolute continuity of measures.",
            duration=5,
        )

        title = self.ly.title("Absolute Continuity: \u03BD \u226A \u03BC")

        # Definition
        def_text = Text("Definition:", font_size=HEADING_SIZE, color=WHITE, font=SANS)
        def_formula = MathTex(
            r"\mu(A) = 0 \implies \nu(A) = 0",
            font_size=HEADING_SIZE,
            color=PRIMARY,
        )
        formula_box = self.ly.formula_box(def_formula, PRIMARY)
        self.ly.safe_place(def_text, direction=DOWN, anchor=title, buff=0.4)
        self.ly.safe_place(formula_box, direction=DOWN, anchor=def_text, buff=0.3)
        self.play(FadeIn(def_text, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(def_formula), run_time=NORMAL)
        self.wait(0.5)

        # Intuition
        intuition = Text(
            "\u03BD cannot detect sets that \u03BC ignores",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(intuition, direction=DOWN, anchor=formula_box, buff=0.4)
        self.play(FadeIn(intuition, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Key example
        self.play(FadeOut(def_text))

        example = Text("Example on \u211D:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        ex_formula = MathTex(
            r"d\nu = f \, d\mu \implies \nu \ll \mu",
            font_size=BODY_SIZE,
        )
        self.ly.safe_place(example, direction=DOWN, anchor=formula_box, buff=0.4)
        self.ly.safe_place(ex_formula, direction=DOWN, anchor=example, buff=0.2)
        self.play(
            FadeIn(example, shift=LEFT * 0.15),
            Write(ex_formula),
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: The Radon-Nikodym Theorem
    # ------------------------------------------------------------------
    def scene3_theorem_statement(self):
        """Statement of the Radon-Nikodym theorem"""
        self.ly.section_divider(3, "The Radon-Nikodym Theorem")

        self.add_subcaption(
            "The theorem guarantees the existence of a density function "
            "when one measure is absolutely continuous with respect to another.",
            duration=6,
        )

        title = self.ly.title("Radon-Nikodym Theorem")

        # Hypotheses
        hyp1 = Text("(X, \u03A3, \u03BC) is \u03C3-finite", font_size=BODY_SIZE, color=WHITE, font=SANS)
        hyp2 = Text("\u03BD is a finite (or \u03C3-finite signed) measure", font_size=BODY_SIZE, color=WHITE, font=SANS)
        hyp3 = Text("\u03BD \u226A \u03BC (absolute continuity)", font_size=BODY_SIZE, color=PRIMARY, font=SANS)

        self.ly.progressive_reveal([hyp1, hyp2, hyp3], start_from=title, wait_time=0.6)
        self.wait(0.5)

        # The theorem statement in a formula box
        theorem = MathTex(
            r"\exists ! f \geq 0 \text{ measurable: } \nu(A) = \int_A f \; d\mu \;\; \forall A \in \Sigma",
            font_size=BODY_SIZE,
            color=SECONDARY,
        )
        boxed_theorem = self.ly.formula_box(theorem, SECONDARY)
        self.ly.safe_place(boxed_theorem, direction=DOWN, anchor=hyp3, buff=0.5)
        self.play(Write(theorem), run_time=NORMAL)
        self.wait(0.5)

        # Clear hypotheses, show consequences
        self.play(FadeOut(hyp1), FadeOut(hyp2), FadeOut(hyp3))

        # RN derivative notation
        notation = MathTex(
            r"f = \frac{d\nu}{d\mu} \quad \text{(Radon-Nikodym derivative)}",
            font_size=HEADING_SIZE,
            color=ACCENT,
        )
        self.ly.safe_place(notation, direction=DOWN, anchor=boxed_theorem, buff=0.4)
        self.play(Write(notation), run_time=NORMAL)
        self.wait(0.5)

        # Uniqueness
        unique = Text(
            "Unique up to \u03BC-a.e. equivalence",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(unique, direction=DOWN, anchor=notation, buff=0.3)
        self.play(FadeIn(unique, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Properties of the RN Derivative
    # ------------------------------------------------------------------
    def scene4_properties(self):
        """Key properties: linearity, chain rule, inverse"""
        self.ly.section_divider(4, "Properties of d\u03BD/d\u03BC")

        self.add_subcaption(
            "The Radon-Nikodym derivative obeys rules that mirror "
            "ordinary calculus derivatives.",
            duration=5,
        )

        title = self.ly.title("Derivative-like Rules")

        # Property 1: Linearity
        prop1_label = Text("Linearity:", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        prop1_formula = MathTex(
            r"\frac{d(\alpha\nu + \beta\lambda)}{d\mu} "
            r"= \alpha \frac{d\nu}{d\mu} + \beta \frac{d\lambda}{d\mu}",
            font_size=BODY_SIZE,
        )
        self.ly.safe_place(prop1_label, direction=DOWN, anchor=title, buff=0.4)
        self.ly.safe_place(prop1_formula, direction=DOWN, anchor=prop1_label, buff=0.2)
        self.play(
            FadeIn(prop1_label, shift=LEFT * 0.15),
            Write(prop1_formula),
            run_time=NORMAL,
        )
        self.wait(1)

        self.ly.clear()

        # Property 2: Chain rule
        self.add_subcaption(
            "Just like the chain rule in calculus, the Radon-Nikodym derivative "
            "composes when you chain measures together.",
            duration=5,
        )

        title2 = self.ly.title("Chain Rule for Measures")

        prop2_label = Text("Chain rule:", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        prop2_formula = MathTex(
            r"\frac{d\rho}{d\mu} = \frac{d\rho}{d\nu} \cdot \frac{d\nu}{d\mu}",
            font_size=BODY_SIZE,
        )
        formula_box = self.ly.formula_box(prop2_formula, SECONDARY)
        self.ly.safe_place(prop2_label, direction=DOWN, anchor=title2, buff=0.4)
        self.ly.safe_place(formula_box, direction=DOWN, anchor=prop2_label, buff=0.3)
        self.play(
            FadeIn(prop2_label, shift=LEFT * 0.15),
            Write(prop2_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Property 3: Inverse
        prop3_label = Text("Inverse:", font_size=BODY_SIZE, color=ACCENT, font=SANS)
        prop3_formula = MathTex(
            r"\frac{d\mu}{d\nu} = \frac{1}{\, d\nu / d\mu \,}",
            font_size=BODY_SIZE,
        )
        self.ly.safe_place(prop3_label, direction=DOWN, anchor=formula_box, buff=0.5)
        self.ly.safe_place(prop3_formula, direction=DOWN, anchor=prop3_label, buff=0.2)
        self.play(
            FadeIn(prop3_label, shift=LEFT * 0.15),
            Write(prop3_formula),
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Probability Density = RN Derivative
    # ------------------------------------------------------------------
    def scene5_probability_example(self):
        """Concrete example: PDFs are RN derivatives"""
        self.ly.section_divider(5, "Example: Probability Density")

        self.add_subcaption(
            "Here's something you already know: probability density functions "
            "are Radon-Nikodym derivatives!",
            duration=6,
        )

        title = self.ly.title("PDFs are RN Derivatives")

        # Setup
        setup = Text("On \u211D with Lebesgue measure \u03BB:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        prob_formula = MathTex(
            r"P(A) = \int_A p(x) \; dx",
            font_size=HEADING_SIZE,
            color=PRIMARY,
        )
        formula_box = self.ly.formula_box(prob_formula, PRIMARY)
        self.ly.safe_place(setup, direction=DOWN, anchor=title, buff=0.4)
        self.ly.safe_place(formula_box, direction=DOWN, anchor=setup, buff=0.3)
        self.play(
            FadeIn(setup, shift=LEFT * 0.15),
            Write(prob_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # The connection
        connection = MathTex(
            r"p(x) = \frac{dP}{d\lambda}",
            font_size=HEADING_SIZE,
            color=SECONDARY,
        )
        box2 = self.ly.formula_box(connection, SECONDARY)
        self.ly.safe_place(box2, direction=DOWN, anchor=formula_box, buff=0.5)
        self.play(Write(connection), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(setup), FadeOut(formula_box))

        # CDF connection
        cdf_label = Text("The CDF connection:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        cdf_formula = MathTex(
            r"F(x) = P((-\infty, x]) = \int_{-\infty}^{x} p(t) \; dt",
            font_size=BODY_SIZE,
            color=ACCENT,
        )
        self.ly.safe_place(cdf_label, direction=DOWN, anchor=box2, buff=0.5)
        self.ly.safe_place(cdf_formula, direction=DOWN, anchor=cdf_label, buff=0.2)
        self.play(
            FadeIn(cdf_label, shift=LEFT * 0.15),
            Write(cdf_formula),
            run_time=NORMAL,
        )
        self.wait(1)

        # Punchline
        punchline = Text(
            "You've been using RN derivatives all along!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(punchline, direction=DOWN, anchor=cdf_formula, buff=0.4)
        self.play(FadeIn(punchline, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Lebesgue Decomposition
    # ------------------------------------------------------------------
    def scene6_lebesgue_decomposition(self):
        """Lebesgue decomposition theorem as bridge"""
        self.ly.section_divider(6, "Lebesgue Decomposition")

        self.add_subcaption(
            "What if nu is NOT absolutely continuous with respect to mu? "
            "The Lebesgue decomposition theorem handles this case.",
            duration=6,
        )

        title = self.ly.title("Decomposing Any Measure")

        # Statement
        decomposition = MathTex(
            r"\nu = \nu_{ac} + \nu_s",
            font_size=HEADING_SIZE,
            color=PRIMARY,
        )
        formula_box = self.ly.formula_box(decomposition, PRIMARY)
        self.ly.safe_place(formula_box, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(decomposition), run_time=NORMAL)
        self.wait(0.5)

        # The two parts
        part_ac = VGroup(
            Text("\u03BD_ac \u226A \u03BC", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("(absolutely continuous part)", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.1)

        part_s = VGroup(
            Text("\u03BD_s \u22A5 \u03BC", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("(singular: supported on \u03BC-null set)", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.1)

        ensure_fits(part_ac, MAX_HALF_WIDTH, 1.5)
        ensure_fits(part_s, MAX_HALF_WIDTH, 1.5)

        columns = self.ly.two_columns(
            [part_ac], [part_s], start_from=formula_box,
        )
        self.play(
            FadeIn(part_ac, shift=LEFT * 0.15),
            FadeIn(part_s, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1)

        # RN theorem handles the ac part
        self.play(FadeOut(part_s))

        rn_bridge = Text(
            "RN theorem gives: d\u03BD_ac/d\u03BC",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(rn_bridge, direction=DOWN, anchor=part_ac, buff=0.5)
        self.play(FadeIn(rn_bridge, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Applications
    # ------------------------------------------------------------------
    def scene7_applications(self):
        """Applications across probability, statistics, information theory"""
        self.ly.section_divider(7, "Applications")

        self.add_subcaption(
            "The Radon-Nikodym derivative appears everywhere: "
            "probability, statistics, and information theory.",
            duration=5,
        )

        title = self.ly.title("RN Derivatives in Practice")

        # Application 1: Probability
        app1_label = Text("Probability:", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        app1_desc = MathTex(
            r"\frac{dQ}{dP}",
            font_size=HEADING_SIZE,
            color=PRIMARY,
        )
        app1_detail = Text("Change of measure (Girsanov, Bayes)", font_size=LABEL_SIZE, color=DIM, font=SANS)

        app1_group = VGroup(app1_label, app1_desc, app1_detail).arrange(DOWN, buff=0.1)
        self.ly.safe_place(app1_group, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(app1_group, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        self.ly.clear()

        # Application 2: Statistics
        self.add_subcaption(
            "In statistics, the likelihood ratio between two hypotheses "
            "is a Radon-Nikodym derivative.",
            duration=5,
        )

        title2 = self.ly.title("Statistics & Information Theory")

        app2_label = Text("Likelihood ratio:", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        app2_formula = MathTex(
            r"\frac{dP_\theta}{dP_{\theta_0}} = \frac{L(\theta)}{L(\theta_0)}",
            font_size=BODY_SIZE,
            color=SECONDARY,
        )
        self.ly.safe_place(app2_label, direction=DOWN, anchor=title2, buff=0.4)
        self.ly.safe_place(app2_formula, direction=DOWN, anchor=app2_label, buff=0.2)
        self.play(
            FadeIn(app2_label, shift=LEFT * 0.15),
            Write(app2_formula),
            run_time=NORMAL,
        )
        self.wait(0.8)

        # Application 3: KL divergence
        app3_label = Text("KL divergence:", font_size=BODY_SIZE, color=ACCENT, font=SANS)
        app3_formula = MathTex(
            r"D_{KL}(P \| Q) = \int \log \frac{dP}{dQ} \; dP",
            font_size=BODY_SIZE,
            color=ACCENT,
        )
        self.ly.safe_place(app3_label, direction=DOWN, anchor=app2_formula, buff=0.4)
        self.ly.safe_place(app3_formula, direction=DOWN, anchor=app3_label, buff=0.2)
        self.play(
            FadeIn(app3_label, shift=LEFT * 0.15),
            Write(app3_formula),
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Summary + Outro
    # ------------------------------------------------------------------
    def scene8_summary_outro(self):
        """Summary and next video tease"""
        self.ly.section_divider(8, "Summary")

        self.add_subcaption(
            "The Radon-Nikodym theorem gives us the measure-theoretic "
            "foundation for density functions, likelihood ratios, and much more.",
            duration=6,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text("\u03BD \u226A \u03BC means \u03BD cannot detect \u03BC-null sets", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("RN theorem: \u03BD(A) = \u222B_A (d\u03BD/d\u03BC) d\u03BC when \u03BD \u226A \u03BC", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("RN derivative obeys chain rule, linearity, inverse", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("PDFs, likelihood ratios, KL divergence \u2014 all RN derivatives!", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title, wait_time=0.8)
        self.wait(1.5)

        self.ly.clear()

        play_outro(self, "Product Measures & Fubini's Theorem", "Measure Theory")
