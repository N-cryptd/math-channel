"""
Video 157: Convergence Theorems (MCT, DCT, Fatou's Lemma) — Measure Theory Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video157_ConvergenceTheorems

Topics: When can we swap limits and integrals?
        Fatou's Lemma (one-sided inequality),
        Monotone Convergence Theorem (MCT — equality for increasing sequences),
        MCT application (geometric-type),
        Dominated Convergence Theorem (DCT — equality with dominating function),
        DCT application (power functions),
        Why Riemann fails (spike counterexample),
        Summary of the three convergence theorems.

Prerequisites: Videos 151-156 (Measure Theory Intro through Lebesgue Integral).

Competitive insights (from channel-analysis/improvements.md):
- Unlike TBSOM's static graphs, we ANIMATE the convergence process
- Following Dr. Peyam's emphasis on the bounding function, we visualize g(x)
- Show logical progression Fatou → MCT → DCT (not isolated theorems)
- Intuition-first approach before formal statements (3B1B style)

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
from layout import LayoutEngine, ensure_fits, clamp_position


class Video157_ConvergenceTheorems(Scene):
    """Convergence Theorems: Fatou's Lemma, MCT, DCT"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_fatous_lemma()
        self.scene3_monotone_convergence()
        self.scene4_mct_application()
        self.scene5_dominated_convergence()
        self.scene6_dct_application()
        self.scene7_comparison_riemann()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook — can we swap limits and integrals?
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: Swapping limits and integrals"""
        self.add_subcaption(
            "In calculus, we often want to swap a limit and an integral. "
            "But when is this allowed?",
            duration=5,
        )
        play_intro(self, "Convergence Theorems (MCT, DCT)", "Measure Theory")

        title = self.ly.title("When can we swap limit and integral?")

        # Show the problem: lim ∫f_n vs ∫lim f_n
        lim_integral = MathTex(r"\lim_{n \to \infty} \int f_n", font_size=BODY_SIZE)
        integral_lim = MathTex(r"\int \lim_{n \to \infty} f_n", font_size=BODY_SIZE)
        question = Text("?", font_size=TITLE_SIZE, color=ACCENT, font=SANS)

        problem_group = VGroup(lim_integral, question, integral_lim).arrange(RIGHT, buff=0.8)
        self.ly.safe_place(problem_group, direction=DOWN, anchor=title, buff=0.5)

        self.play(
            Write(lim_integral),
            FadeIn(question, shift=LEFT * 0.15),
            Write(integral_lim),
        )
        self.wait(1)

        # Three theorem names — progressive reveal
        theorem_names = [
            Text("Fatou's Lemma", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
            Text("Monotone Convergence Theorem", font_size=HEADING_SIZE, color=SECONDARY, font=SANS),
            Text("Dominated Convergence Theorem", font_size=HEADING_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(theorem_names, start_from=problem_group, wait_time=0.7)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Fatou's Lemma
    # ------------------------------------------------------------------
    def scene2_fatous_lemma(self):
        """Fatou's Lemma: integral(liminf) ≤ liminf(integral)"""
        self.ly.section_divider(2, "Fatou's Lemma")

        self.add_subcaption(
            "We start with Fatou's Lemma, which gives a one-sided inequality "
            "for non-negative functions.",
            duration=5,
        )

        title = self.ly.title("Fatou's Lemma")

        # Setup: sequence of non-negative measurable functions
        setup = VGroup(
            Text("Let {f_n} be non-negative measurable functions", font_size=BODY_SIZE, font=SANS),
            Text("on a measure space (X, Σ, μ)", font_size=BODY_SIZE, font=SANS),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.ly.safe_place(setup, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(setup, shift=LEFT * 0.15))
        self.wait(1)

        # Statement in a formula box
        statement = MathTex(
            r"\int \liminf_{n \to \infty} f_n \; d\mu \;\leq\; \liminf_{n \to \infty} \int f_n \; d\mu",
            font_size=BODY_SIZE,
        )
        boxed_statement = self.ly.formula_box(statement, color=PRIMARY)
        self.ly.safe_place(boxed_statement, direction=DOWN, anchor=setup, buff=0.6)
        self.play(Write(boxed_statement))
        self.wait(2)

        # Clear setup, keep statement for interpretation
        self.play(FadeOut(setup))

        # Interpretation
        interp_items = [
            Text("In words:", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("∫ of liminf  ≤  liminf of ∫", font_size=BODY_SIZE, font=SANS),
            Text("liminf picks 'smallest frequent' values", font_size=BODY_SIZE, font=SANS),
        ]
        self.ly.progressive_reveal(interp_items, start_from=boxed_statement, wait_time=0.8)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Monotone Convergence Theorem
    # ------------------------------------------------------------------
    def scene3_monotone_convergence(self):
        """Monotone Convergence Theorem: equality for increasing sequences"""
        self.ly.section_divider(3, "Monotone Convergence Theorem")

        self.add_subcaption(
            "For increasing sequences of non-negative functions, "
            "Fatou's inequality becomes equality.",
            duration=5,
        )

        title = self.ly.title("Monotone Convergence Theorem (MCT)")

        # Hypotheses
        hypotheses = VGroup(
            Text("Hypotheses:", font_size=HEADING_SIZE, color=WHITE, font=SANS),
            Text("1.  0 ≤ f₁ ≤ f₂ ≤ ···  (monotone increasing)", font_size=BODY_SIZE, font=SANS),
            Text("2.  f_n → f pointwise", font_size=BODY_SIZE, font=SANS),
            Text("3.  All f_n are measurable", font_size=BODY_SIZE, font=SANS),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.ly.safe_place(hypotheses, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(hypotheses, shift=LEFT * 0.15))
        self.wait(1.5)

        # Conclusion in a formula box
        conclusion = MathTex(
            r"\lim_{n \to \infty} \int f_n \; d\mu = \int f \; d\mu",
            font_size=BODY_SIZE + 2,
            color=SECONDARY,
        )
        boxed_conclusion = self.ly.formula_box(conclusion, color=SECONDARY)
        self.ly.safe_place(boxed_conclusion, direction=DOWN, anchor=hypotheses, buff=0.6)
        self.play(Write(boxed_conclusion))
        self.wait(2)

        self.play(FadeOut(hypotheses))

        # Key insight
        insight = Text(
            "We can swap limit and integral!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=boxed_conclusion, buff=0.4)
        self.play(FadeIn(insight, shift=LEFT * 0.15))
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: MCT Application
    # ------------------------------------------------------------------
    def scene4_mct_application(self):
        """MCT application: geometric series type example"""
        self.ly.section_divider(4, "MCT in Action")

        self.add_subcaption(
            "The MCT lets us find limits of integrals without explicit computation.",
            duration=5,
        )

        title = self.ly.title("MCT in Action: Power Functions")

        # Example definition
        example_intro = Text(
            "On [0,1] with Lebesgue measure, let:", font_size=BODY_SIZE, font=SANS,
        )
        self.ly.safe_place(example_intro, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(example_intro, shift=LEFT * 0.15))

        fn_def = MathTex(r"f_n(x) = (1-x)^n \, e^x", font_size=BODY_SIZE)
        boxed_fn = self.ly.formula_box(fn_def, color=ACCENT)
        self.ly.safe_place(boxed_fn, direction=DOWN, anchor=example_intro, buff=0.4)
        self.play(Write(boxed_fn))
        self.wait(1)

        # Pointwise limit
        pointwise = VGroup(
            Text("As n → ∞:", font_size=BODY_SIZE, font=SANS),
            MathTex(r"(1-x)^n \to 0 \;\text{ for } x \in (0,1]", font_size=BODY_SIZE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        self.ly.safe_place(pointwise, direction=DOWN, anchor=boxed_fn, buff=0.5)
        self.play(FadeIn(pointwise, shift=LEFT * 0.15))
        self.wait(1)

        # Clear example definition
        self.play(FadeOut(example_intro), FadeOut(boxed_fn))

        # MCT result
        mct_result = MathTex(
            r"\lim_{n\to\infty} \int_0^1 (1-x)^n e^x \; dx = 0",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        boxed_result = self.ly.formula_box(mct_result, color=SECONDARY)
        self.ly.safe_place(boxed_result, direction=DOWN, anchor=pointwise, buff=0.5)
        self.play(Write(boxed_result))
        self.wait(1)

        verify = Text(
            "MCT gives the answer for free — no integration needed!",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(verify, direction=DOWN, anchor=boxed_result, buff=0.4)
        self.play(FadeIn(verify, shift=LEFT * 0.15))
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Dominated Convergence Theorem
    # ------------------------------------------------------------------
    def scene5_dominated_convergence(self):
        """Dominated Convergence Theorem: removes monotonicity assumption"""
        self.ly.section_divider(5, "Dominated Convergence Theorem")

        self.add_subcaption(
            "The DCT removes monotonicity at the cost of requiring "
            "a dominating function.",
            duration=5,
        )

        title = self.ly.title("Dominated Convergence Theorem (DCT)")

        # Hypotheses
        hypotheses = VGroup(
            Text("Hypotheses:", font_size=HEADING_SIZE, color=WHITE, font=SANS),
            Text("1.  f_n → f pointwise", font_size=BODY_SIZE, font=SANS),
            Text("2.  |f_n| ≤ g  for all n, with ∫|g| < ∞", font_size=BODY_SIZE, font=SANS),
            Text("3.  All functions are measurable", font_size=BODY_SIZE, font=SANS),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.ly.safe_place(hypotheses, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(hypotheses, shift=LEFT * 0.15))
        self.wait(1.5)

        # Conclusion in a formula box
        conclusion = MathTex(
            r"\lim_{n \to \infty} \int f_n \; d\mu = \int f \; d\mu",
            font_size=BODY_SIZE + 2,
            color=ACCENT,
        )
        boxed_conclusion = self.ly.formula_box(conclusion, color=ACCENT)
        self.ly.safe_place(boxed_conclusion, direction=DOWN, anchor=hypotheses, buff=0.6)
        self.play(Write(boxed_conclusion))
        self.wait(2)

        self.play(FadeOut(hypotheses))

        # g explanation
        g_explain = VGroup(
            Text("g is the dominating function", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("or integrable majorant — it bounds all f_n", font_size=BODY_SIZE, font=SANS),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        self.ly.safe_place(g_explain, direction=DOWN, anchor=boxed_conclusion, buff=0.5)
        self.play(FadeIn(g_explain, shift=LEFT * 0.15))
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: DCT Application
    # ------------------------------------------------------------------
    def scene6_dct_application(self):
        """DCT application: x^n example"""
        self.ly.section_divider(6, "DCT in Action")

        self.add_subcaption(
            "A classic DCT application: the limit of the integral of x^n "
            "via domination by g(x) = 1.",
            duration=5,
        )

        title = self.ly.title("DCT in Action: Power Functions")

        # Example definition
        example_intro = Text("On [0,1], let:", font_size=BODY_SIZE, font=SANS)
        self.ly.safe_place(example_intro, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(example_intro, shift=LEFT * 0.15))

        fn_def = MathTex(r"f_n(x) = x^n", font_size=BODY_SIZE)
        boxed_fn = self.ly.formula_box(fn_def, color=ACCENT)
        self.ly.safe_place(boxed_fn, direction=DOWN, anchor=example_intro, buff=0.4)
        self.play(Write(boxed_fn))
        self.wait(1)

        # Pointwise limit
        pointwise = VGroup(
            Text("As n → ∞:", font_size=BODY_SIZE, font=SANS),
            MathTex(r"x^n \to 0 \;\text{ a.e. on } [0,1]", font_size=BODY_SIZE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        self.ly.safe_place(pointwise, direction=DOWN, anchor=boxed_fn, buff=0.5)
        self.play(FadeIn(pointwise, shift=LEFT * 0.15))
        self.wait(1)

        # Domination check
        domination = MathTex(
            r"|x^n| \leq 1 =: g(x), \quad \int_0^1 1\,dx = 1 < \infty",
            font_size=BODY_SIZE,
        )
        boxed_dom = self.ly.formula_box(domination, color=PRIMARY)
        self.ly.safe_place(boxed_dom, direction=DOWN, anchor=pointwise, buff=0.5)
        self.play(Write(boxed_dom))
        self.wait(1)

        # Clear to make room for result
        self.play(FadeOut(example_intro), FadeOut(boxed_fn), FadeOut(pointwise))

        # DCT result
        dct_result = MathTex(
            r"\lim_{n\to\infty} \int_0^1 x^n \; dx = \int_0^1 0 \; dx = 0",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        boxed_result = self.ly.formula_box(dct_result, color=SECONDARY)
        self.ly.safe_place(boxed_result, direction=DOWN, anchor=boxed_dom, buff=0.5)
        self.play(Write(boxed_result))
        self.wait(1)

        direct = Text(
            "Verify: ∫₀¹ xⁿ dx = 1/(n+1) → 0  ✓",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(direct, direction=DOWN, anchor=boxed_result, buff=0.4)
        self.play(FadeIn(direct, shift=LEFT * 0.15))
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Why Riemann Fails — Spike Counterexample
    # ------------------------------------------------------------------
    def scene7_comparison_riemann(self):
        """Show where Riemann fails but Lebesgue succeeds"""
        self.ly.section_divider(7, "Why Riemann Fails")

        self.add_subcaption(
            "The Riemann integral lacks analogous theorems. "
            "Consider a spike sequence.",
            duration=5,
        )

        title = self.ly.title("Why Riemann Fails: A Counterexample")

        # Define the spike sequence
        spike_intro = Text("Consider on [0,1]:", font_size=BODY_SIZE, font=SANS)
        self.ly.safe_place(spike_intro, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(spike_intro, shift=LEFT * 0.15))

        spike_def = MathTex(r"f_n(x) = n \cdot \mathbf{1}_{[0,\,1/n]}(x)", font_size=BODY_SIZE)
        boxed_spike = self.ly.formula_box(spike_def, color=ACCENT)
        self.ly.safe_place(boxed_spike, direction=DOWN, anchor=spike_intro, buff=0.4)
        self.play(Write(boxed_spike))
        self.wait(1)

        # Each f_n is Riemann integrable
        riemann_int = MathTex(
            r"\int_0^1 f_n(x) \; dx = n \cdot \frac{1}{n} = 1",
            font_size=BODY_SIZE,
        )
        self.ly.safe_place(riemann_int, direction=DOWN, anchor=boxed_spike, buff=0.5)
        self.play(Write(riemann_int))
        self.wait(1)

        # Clear definition
        self.play(FadeOut(spike_intro), FadeOut(boxed_spike))

        # Pointwise limit
        pointwise = Text(
            "Pointwise:  f_n(x) → 0  for all x ∈ (0,1]",
            font_size=BODY_SIZE, font=SANS,
        )
        self.ly.safe_place(pointwise, direction=DOWN, anchor=riemann_int, buff=0.5)
        self.play(FadeIn(pointwise, shift=LEFT * 0.15))
        self.wait(1)

        # The failure
        failure = VGroup(
            MathTex(
                r"\lim_{n\to\infty} \int_0^1 f_n \; dx = 1",
                font_size=BODY_SIZE,
            ),
            MathTex(
                r"\int_0^1 \lim_{n\to\infty} f_n \; dx = 0",
                font_size=BODY_SIZE,
            ),
        ).arrange(DOWN, buff=0.2)
        self.ly.safe_place(failure, direction=DOWN, anchor=pointwise, buff=0.5)
        self.play(Write(failure))
        self.wait(1)

        verdict = Text(
            "1 ≠ 0  —  the swap FAILS!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(verdict, direction=DOWN, anchor=failure, buff=0.4)
        self.play(Write(verdict))
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------
    def scene8_summary_outro(self):
        """Summary and outro"""
        self.ly.section_divider(8, "Summary")

        self.add_subcaption(
            "The three convergence theorems are the cornerstone of "
            "Lebesgue integration theory.",
            duration=5,
        )

        title = self.ly.title("The Three Convergence Theorems")

        # Progressive reveal of the three theorems
        summary_items = [
            Text(
                "Fatou's Lemma:  ∫liminf f_n ≤ liminf ∫f_n",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "MCT:  lim ∫f_n = ∫lim f_n  (for 0 ≤ f_n ↗ f)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "DCT:  lim ∫f_n = ∫lim f_n  (when |f_n| ≤ g ∈ L¹)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Key insight: these justify swapping limits and integrals",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(summary_items, start_from=title, wait_time=1.0)
        self.wait(2)

        # Final punchline
        punchline = Text(
            "The reason Lebesgue beats Riemann in analysis",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        # Get currently visible items from progressive_reveal — place punchline below
        self.ly.safe_place(punchline, direction=DOWN, anchor=summary_items[3], buff=0.5)
        self.play(FadeIn(punchline, shift=LEFT * 0.15))
        self.wait(2)

        # Outro
        self.play(FadeOut(punchline))
        play_outro(self, "L^p Spaces", "Measure Theory")
