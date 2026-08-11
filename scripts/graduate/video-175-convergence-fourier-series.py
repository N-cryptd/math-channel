"""
Video 175: Convergence of Fourier Series -- Fourier Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video175_ConvergenceFourierSeries

Topics: Pointwise convergence, uniform convergence, L2 convergence,
        Dirichlet kernel derivation, Dirichlet conditions theorem,
        convergence at discontinuities (midpoint rule),
        Gibbs phenomenon deep-dive with sine integral,
        convergence hierarchy.

Prerequisites: Video 174 (Introduction to Fourier Series),
               Video 165 (Hilbert Spaces), Video 164 (Inner Product Spaces).

Competitive insights:
- No animated Manim video covers Fourier convergence theory at graduate level
- Dr. Peyam, Michael Penn: whiteboard theorem-proof style, no visuals
- TBSOM: animated but superficial, doesn't prove Dirichlet conditions
- Our unique angle: convergence as different topologies on L2, with visual hierarchy
- Gibbs phenomenon deep-dive with Dirichlet kernel analysis

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
from layout import LayoutEngine, ensure_fits


class Video175_ConvergenceFourierSeries(Scene):
    """Convergence of Fourier Series -- Fourier Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_dirichlet_kernel()
        self.scene3_dirichlet_conditions()
        self.scene4_convergence_at_jumps()
        self.scene5_uniform_convergence()
        self.scene6_l2_convergence()
        self.scene7_gibbs_phenomenon()
        self.scene8_hierarchy()
        self.scene9_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook -- When Does Approximation Become Reality?
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "In the last video, we built partial sums S-sub-N of x and "
            "watched them approach f of x. But a critical question "
            "remains. Does S-sub-N actually converge to f?",
            duration=6,
        )
        play_intro(self, "Convergence of Fourier Series", "Fourier Analysis")

        title = self.ly.title("When Does Approximation Become Reality?")

        self.add_subcaption(
            "We need to be precise about what convergence means "
            "for functions. There are three distinct levels.",
            duration=5,
        )
        items = [
            Text("Pointwise: S_N(x) -> f(x) at each x",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Uniform: convergence everywhere at the same rate",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("L2: convergence in the mean-square sense",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "The answer depends on which kind of convergence you "
            "demand, and on the properties of f. Some functions "
            "converge in all three senses. Others only in one or two.",
            duration=6,
        )
        item4 = Text(
            "The answer depends on f and the type of convergence",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.progressive_reveal([item4])
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: The Dirichlet Kernel
    # ------------------------------------------------------------------ #
    def scene2_dirichlet_kernel(self):
        self.add_subcaption(
            "To understand convergence, we need the Dirichlet kernel. "
            "The N-th partial sum of the Fourier series can be written "
            "as an integral involving this kernel.",
            duration=6,
        )
        title = self.ly.title("The Dirichlet Kernel")

        self.add_subcaption(
            "Starting from the partial sum and substituting the "
            "Fourier coefficient formulas, we can rewrite S-sub-N "
            "of x as an integral of f of t times the Dirichlet "
            "kernel D-sub-N of x minus t.",
            duration=8,
        )

        # Partial sum as integral with Dirichlet kernel
        s_integral = MathTex(
            r"S_N(x)",
            r"= \frac{1}{\pi}\int_{-\pi}^{\pi}",
            r"f(t)\,D_N(x-t)\,dt",
            font_size=BODY_SIZE, color=WHITE,
        )
        s_box = self.ly.formula_box(s_integral, color=PRIMARY)
        self.play(Write(s_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "The Dirichlet kernel has two equivalent forms. "
            "First, as a finite sum of cosines: D-sub-N of u "
            "equals one-half plus the sum from k equals one to "
            "N of cosine k u.",
            duration=8,
        )

        self.play(FadeOut(s_box), run_time=FAST)
        self.wait(0.5)

        # Dirichlet kernel -- sum form
        d_sum = MathTex(
            r"D_N(u)",
            r"= \frac{1}{2}",
            r"+ \sum_{k=1}^{N}\cos(ku)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        d_sum_box = self.ly.formula_box(d_sum, color=PRIMARY)
        self.play(Write(d_sum_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "This sum telescopes into a beautiful closed form "
            "using trigonometric identities. The Dirichlet kernel "
            "equals sine of N plus one-half times u, divided by "
            "two sine of u over two.",
            duration=8,
        )

        self.play(FadeOut(d_sum_box), run_time=FAST)
        self.wait(0.5)

        # Dirichlet kernel -- closed form
        d_closed = MathTex(
            r"D_N(u)",
            r"= \frac{\sin\!\left((N+\frac{1}{2})u\right)}{2\sin(u/2)}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        d_closed_box = self.ly.formula_box(d_closed, color=ACCENT)
        self.play(Write(d_closed_box), run_time=SLOW)
        self.wait(2.5)

        key = Text(
            "S_N(x) = convolution of f with D_N",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(key, DOWN, d_closed_box, buff=0.5)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Dirichlet Conditions
    # ------------------------------------------------------------------ #
    def scene3_dirichlet_conditions(self):
        self.ly.section_divider(1, "Dirichlet's Convergence Theorem")

        self.add_subcaption(
            "When does the Fourier series actually converge "
            "pointwise? Dirichlet proved that three mild "
            "conditions on f are sufficient.",
            duration=5,
        )
        title = self.ly.title("Dirichlet Conditions")

        self.add_subcaption(
            "First, f must be piecewise continuous, meaning it has "
            "only finitely many jump discontinuities in each "
            "period. Second, f must be piecewise monotonic, with "
            "finitely many local maxima and minima per period. "
            "Third, f must be periodic with period two pi.",
            duration=10,
        )

        items = [
            Text("1. Piecewise continuous (finitely many jumps)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Piecewise monotonic (finitely many extrema)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Periodic with period 2pi",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "If f satisfies all three Dirichlet conditions, then "
            "at every point x where f is continuous, the Fourier "
            "series converges to f of x. At each jump "
            "discontinuity, it converges to the midpoint of "
            "the left and right limits.",
            duration=10,
        )

        # Theorem statement
        theorem = MathTex(
            r"\lim_{N\to\infty} S_N(x)",
            r"= \frac{f(x^+) + f(x^-)}{2}",
            font_size=BODY_SIZE, color=WHITE,
        )
        theorem_box = self.ly.formula_box(theorem, color=PRIMARY)
        self.play(FadeOut(items[0]), FadeOut(items[1]), FadeOut(items[2]), run_time=FAST)
        self.play(FadeIn(theorem_box, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.5)

        note = Text(
            "Sufficient conditions — not necessary, but cover most applications",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, DOWN, theorem_box, buff=0.5)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Convergence at Discontinuities -- The Midpoint Rule
    # ------------------------------------------------------------------ #
    def scene4_convergence_at_jumps(self):
        self.add_subcaption(
            "The midpoint rule is one of the most surprising "
            "facts about Fourier series. At a jump discontinuity, "
            "the series does not converge to the function value.",
            duration=6,
        )
        title = self.ly.title("Convergence at Jump Discontinuities")

        self.add_subcaption(
            "Instead, it converges to the average of the left "
            "limit f of x minus and the right limit f of x "
            "plus. If the function jumps from zero to one, "
            "the Fourier series converges to one-half at the jump.",
            duration=8,
        )

        items = [
            Text("At a jump: S_N(x_0) -> [f(x_0+) + f(x_0-)] / 2",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("The series does NOT converge to f(x_0) itself",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "Why does this happen? The Fourier series cannot "
            "distinguish between a function and one that is "
            "changed at a single point, because changing f at "
            "a single point does not change any of the Fourier "
            "coefficients. In L-two, single points have zero "
            "measure.",
            duration=9,
        )
        item3 = Text(
            "Changing f at one point changes no Fourier coefficient",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        item4 = Text(
            "L2 convergence is blind to point values",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.progressive_reveal([item3, item4])
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Uniform Convergence -- Stronger, Rarer
    # ------------------------------------------------------------------ #
    def scene5_uniform_convergence(self):
        self.ly.section_divider(2, "Uniform Convergence")

        self.add_subcaption(
            "Uniform convergence is much stronger than pointwise "
            "convergence. It demands that the worst-case error "
            "between S-sub-N and f goes to zero, everywhere "
            "simultaneously.",
            duration=7,
        )
        title = self.ly.title("Uniform Convergence")

        self.add_subcaption(
            "Formally, the supremum over all x of the absolute "
            "value of S-sub-N of x minus f of x tends to zero "
            "as N goes to infinity. This means every point "
            "converges at the same rate.",
            duration=8,
        )

        sup_formula = MathTex(
            r"\lim_{N\to\infty}",
            r"\sup_{x}",
            r"|S_N(x) - f(x)| = 0",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        sup_box = self.ly.formula_box(sup_formula, color=PRIMARY)
        self.play(Write(sup_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "The theorem says: the Fourier series converges "
            "uniformly to f if and only if f is continuous "
            "and f prime is piecewise continuous. This is "
            "much stronger than the Dirichlet conditions.",
            duration=7,
        )

        self.play(FadeOut(sup_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Requires: f continuous AND f' piecewise continuous",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Square wave: pointwise YES, uniform NO",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "The square wave is the canonical counterexample. "
            "It satisfies Dirichlet conditions, so it converges "
            "pointwise. But it has jump discontinuities, so "
            "uniform convergence fails. The Gibbs overshoot "
            "prevents the supremum error from going to zero.",
            duration=9,
        )
        item3 = Text(
            "Gibbs overshoot prevents sup-norm from vanishing",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.progressive_reveal([item3])
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: L2 Convergence -- The Universal Guarantee
    # ------------------------------------------------------------------ #
    def scene6_l2_convergence(self):
        self.ly.section_divider(3, "L2 Convergence")

        self.add_subcaption(
            "L2 convergence is the weakest of the three types, "
            "but it has a remarkable property: it always works.",
            duration=5,
        )
        title = self.ly.title("L2 Convergence: Always Works")

        self.add_subcaption(
            "Recall from our study of Hilbert spaces that L-two "
            "convergence means the norm of S-sub-N minus f "
            "goes to zero, where the norm is the integral of "
            "the square of the difference.",
            duration=7,
        )

        l2_def = MathTex(
            r"\lim_{N\to\infty}",
            r"\|S_N - f\|_2 = 0",
            font_size=BODY_SIZE, color=ACCENT,
        )
        l2_box = self.ly.formula_box(l2_def, color=ACCENT)
        self.play(Write(l2_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "The theorem is powerful: for every function f in "
            "L-two of minus pi to pi, the Fourier partial sums "
            "converge to f in the L-two norm. No smoothness "
            "required. Just square integrability.",
            duration=8,
        )

        self.play(FadeOut(l2_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("For ALL f in L2, the Fourier series converges in L2",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("No smoothness conditions needed",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "Parseval's identity makes this precise. The energy "
            "in the function equals the energy in the coefficients. "
            "The sum of the squares of all Fourier coefficients "
            "converges to the L-two norm squared of f.",
            duration=9,
        )

        parseval = MathTex(
            r"\|f\|_2^2",
            r"= \frac{a_0^2}{2}",
            r"+ \sum_{n=1}^{\infty}(a_n^2 + b_n^2)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        parseval_box = self.ly.formula_box(parseval, color=ACCENT)
        self.play(FadeOut(items[0]), FadeOut(items[1]), run_time=FAST)
        self.play(FadeIn(parseval_box, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.5)

        energy = Text(
            "Energy in f = energy in its Fourier coefficients",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(energy, DOWN, parseval_box, buff=0.5)
        self.play(FadeIn(energy, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Gibbs Phenomenon -- Deep Dive
    # ------------------------------------------------------------------ #
    def scene7_gibbs_phenomenon(self):
        self.ly.section_divider(4, "The Gibbs Phenomenon")

        self.add_subcaption(
            "We saw in the last video that partial sums overshoot "
            "near jump discontinuities. Now let us understand "
            "WHY this happens, and compute the exact overshoot.",
            duration=7,
        )
        title = self.ly.title("Why Does the Overshoot Happen?")

        self.add_subcaption(
            "The Dirichlet kernel D-sub-N of u has a large "
            "central lobe and oscillating side lobes. Near a "
            "jump discontinuity, the integral of f times "
            "D-sub-N picks up a contribution from the first "
            "side lobe that does not vanish as N grows.",
            duration=9,
        )

        items = [
            Text("D_N has a main lobe + oscillating side lobes",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Near jumps, first side lobe contributes overshoot",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("This contribution approaches a fixed limit",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "The Gibbs constant is given by the sine integral "
            "evaluated at pi. The overshoot equals approximately "
            "zero point zero eight nine five times the jump "
            "height. On each side of the jump, the partial "
            "sums overshoot by about nine percent.",
            duration=9,
        )

        gibbs = MathTex(
            r"\text{Gibbs overshoot}",
            r"\approx \frac{1}{\pi}\!\int_{0}^{\pi}",
            r"\frac{\sin t}{t}\,dt - \frac{1}{2}",
            r"\approx 0.0895",
            font_size=BODY_SIZE, color=RED,
        )
        gibbs_box = self.ly.formula_box(gibbs, color=RED)
        self.play(FadeOut(items[0]), FadeOut(items[1]), FadeOut(items[2]), run_time=FAST)
        self.play(Write(gibbs_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "The crucial fact is that as N goes to infinity, the "
            "overshoot height stays constant, but its width "
            "shrinks to zero. This is why pointwise convergence "
            "still holds away from the jump point, but "
            "uniform convergence fails.",
            duration=9,
        )
        self.play(FadeOut(gibbs_box), run_time=FAST)
        self.wait(0.5)

        items2 = [
            Text("Overshoot HEIGHT stays constant as N -> infinity",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Overshoot WIDTH shrinks to zero",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Convergence Hierarchy -- Putting It All Together
    # ------------------------------------------------------------------ #
    def scene8_hierarchy(self):
        self.add_subcaption(
            "We have seen three levels of convergence for "
            "Fourier series. Let us organize them into a "
            "clear hierarchy from strongest to weakest.",
            duration=6,
        )
        title = self.ly.title("Convergence Hierarchy")

        self.add_subcaption(
            "Uniform convergence is the strongest. It requires "
            "continuity and a piecewise smooth derivative. "
            "Pointwise convergence is in the middle. It needs "
            "the Dirichlet conditions. L-two convergence is "
            "the weakest but most universal. It works for all "
            "square-integrable functions.",
            duration=10,
        )

        items = [
            Text("Uniform: f continuous + f' piecewise continuous",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Pointwise: Dirichlet conditions (most functions)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("L2: ALL functions in L2 (universal guarantee)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "The practical message is simple. Choose the right "
            "type of convergence for your application. "
            "Engineers use L-two convergence for energy "
            "calculations. PDE theory relies on uniform "
            "convergence for error bounds. Signal processing "
            "uses pointwise convergence to reconstruct "
            "the original signal.",
            duration=10,
        )
        item4 = Text(
            "Choose the right convergence for your application",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.progressive_reveal([item4])
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 9: Summary and Preview
    # ------------------------------------------------------------------ #
    def scene9_summary(self):
        self.add_subcaption(
            "Let us review the key ideas from this video.",
            duration=3,
        )
        title = self.ly.title("Key Takeaways")

        self.add_subcaption(
            "First, Fourier partial sums are convolutions with "
            "the Dirichlet kernel. Second, Dirichlet conditions "
            "guarantee pointwise convergence, with the series "
            "converging to the midpoint at jumps. Third, uniform "
            "convergence requires smoothness and fails at "
            "discontinuities. Fourth, L-two convergence is "
            "universal for all square integrable functions. "
            "And fifth, the Gibbs phenomenon is a fundamental, "
            "quantifiable limitation of Fourier approximation "
            "at jump discontinuities.",
            duration=18,
        )

        items = [
            Text("1. S_N(x) = convolution of f with D_N",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Dirichlet conditions => pointwise convergence",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Uniform convergence requires smoothness",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. L2 convergence: universal for all f in L2",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5. Gibbs phenomenon: ~9% overshoot at jumps",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)

        self.add_subcaption(
            "In the next video, we will extend Fourier analysis "
            "beyond periodic functions. The Fourier transform "
            "lets us decompose any function, not just periodic "
            "ones, into frequency components. This is one of "
            "the most powerful tools in all of mathematics.",
            duration=10,
        )
        self.ly.clear()

        play_outro(
            self,
            next_video="The Fourier Transform",
            next_playlist="Fourier Analysis",
        )
