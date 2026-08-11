"""
Video 176: Fourier Series Properties -- Fourier Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video176_FourierSeriesProperties

Topics: Linearity of Fourier series,
        Differentiation and integration of series (term by term),
        Even and odd extensions (half-range expansions),
        Parseval's identity as energy conservation.

Prerequisites: Video 174 (Intro to Fourier Series),
               Video 175 (Convergence of Fourier Series),
               Video 165 (Hilbert Spaces).

Competitive insights:
- Engineering Funda 7.8K views on properties (slides, engineering-focused)
- No animated Manim video covers all four properties at graduate level
- Our angle: Hilbert space framework gives unified proofs and geometric intuition
- Signature: side-by-side diff vs integration, even/odd extension visuals,
  Parseval energy bars

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


class Video176_FourierSeriesProperties(Scene):
    """Fourier Series Properties -- Fourier Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_linearity()
        self.scene3_differentiation()
        self.scene4_integration()
        self.scene5_section_divider()
        self.scene6_even_odd_extensions()
        self.scene7_parseval()
        self.scene8_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook -- The Rules of the Game
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "In the last two videos, we built Fourier series from "
            "orthogonal projections and studied when they converge. "
            "Now we ask: what can we do with them?",
            duration=6,
        )
        play_intro(self, "Fourier Series Properties", "Fourier Analysis")

        title = self.ly.title("The Rules of the Game")

        self.add_subcaption(
            "Fourier series obey a small set of powerful algebraic "
            "rules. Once you know them, you can manipulate series "
            "with confidence. We will cover four key properties.",
            duration=6,
        )

        items = [
            Text("Linearity -- series of a sum is the sum of series",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Differentiation & Integration -- term by term",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Even & Odd Extensions -- half-range expansions",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Parseval's Identity -- energy conservation",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Linearity -- The Easiest Property
    # ------------------------------------------------------------------ #
    def scene2_linearity(self):
        self.add_subcaption(
            "The first property is almost obvious. The Fourier "
            "series of a linear combination is the linear "
            "combination of the Fourier series.",
            duration=5,
        )
        title = self.ly.title("Linearity of Fourier Series")

        self.add_subcaption(
            "If f has coefficients a-sub-n and b-sub-n, and g has "
            "coefficients c-sub-n and d-sub-n, then the function "
            "alpha f plus beta g has Fourier coefficients alpha "
            "a-sub-n plus beta c-sub-n, and alpha b-sub-n plus "
            "beta d-sub-n.",
            duration=8,
        )

        linearity = MathTex(
            r"(\alpha f + \beta g)(x)",
            r"= \frac{\alpha a_0 + \beta c_0}{2}",
            r"+ \sum_{n=1}^{\infty}\!\left(",
            r"(\alpha a_n + \beta c_n)\cos(nx)",
            r"+ (\alpha b_n + \beta d_n)\sin(nx)",
            r"\right)",
            font_size=BODY_SIZE, color=WHITE,
        )
        linearity_box = self.ly.formula_box(linearity)
        self.play(Write(linearity_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "Why does this work? The Fourier coefficient formula "
            "involves an integral. And integration is linear. So "
            "the integral of alpha f plus beta g splits into "
            "alpha times the integral of f, plus beta times the "
            "integral of g. That is it.",
            duration=9,
        )

        self.play(FadeOut(linearity_box), run_time=FAST)
        self.wait(0.5)

        proof_step = MathTex(
            r"a_n^{\alpha f + \beta g}",
            r"= \frac{1}{\pi}\!\int_{-\pi}^{\pi}",
            r"(\alpha f + \beta g)\cos(nx)\,dx",
            r"= \alpha\, a_n^f + \beta\, a_n^g",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        proof_box = self.ly.formula_box(proof_step)
        self.play(Write(proof_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "In Hilbert space language, this is linearity of the "
            "inner product. The Fourier coefficients are inner "
            "products with the basis functions, and inner products "
            "are linear in the first argument.",
            duration=7,
        )

        insight = Text(
            "Linearity of integral = linearity of Fourier series",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, proof_box, buff=0.5)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Differentiation of Fourier Series
    # ------------------------------------------------------------------ #
    def scene3_differentiation(self):
        self.add_subcaption(
            "Can we differentiate a Fourier series term by term? "
            "The answer is yes, but only under the right conditions.",
            duration=5,
        )
        title = self.ly.title("Differentiation of Fourier Series")

        self.add_subcaption(
            "If f is continuous and f prime is piecewise smooth, "
            "then we can differentiate the series term by term. "
            "The derivative of cosine n x is minus n sine n x, "
            "and the derivative of sine n x is n cosine n x.",
            duration=8,
        )

        diff_formula = MathTex(
            r"f'(x) = \sum_{n=1}^{\infty}\!\left(",
            r"{-n\, a_n \sin(nx)}",
            r"{+ n\, b_n \cos(nx)}",
            r"\right)",
            font_size=BODY_SIZE, color=WHITE,
        )
        diff_formula[1].set_color(ACCENT)
        diff_formula[2].set_color(ACCENT)
        diff_box = self.ly.formula_box(diff_formula)
        self.play(Write(diff_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "Notice the factor of n. Each coefficient gets "
            "multiplied by its frequency. This means "
            "differentiation amplifies higher frequencies. "
            "In signal processing, differentiation is a "
            "high-pass filter.",
            duration=7,
        )

        self.play(FadeOut(diff_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Cosine terms: a_n cos(nx) -> -n*a_n sin(nx)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Sine terms: b_n sin(nx) -> n*b_n cos(nx)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Factor n amplifies high frequencies",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "But be careful. For the square wave, differentiating "
            "the series gives a divergent result at the jump points. "
            "The differentiated series does not converge there. "
            "Smoothness matters.",
            duration=7,
        )
        warning = Text(
            "WARNING: Fails at discontinuities (e.g., square wave)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.progressive_reveal([warning])
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Integration of Fourier Series
    # ------------------------------------------------------------------ #
    def scene4_integration(self):
        self.add_subcaption(
            "Integration is the opposite of differentiation. "
            "Remarkably, we can always integrate a Fourier series "
            "term by term, even when differentiation fails.",
            duration=6,
        )
        title = self.ly.title("Integration of Fourier Series")

        self.add_subcaption(
            "The integrated series has each term divided by n "
            "instead of multiplied by n. A new linear term "
            "appears from the constant coefficient a-sub-zero.",
            duration=6,
        )

        int_formula = MathTex(
            r"\int f(x)\,dx = \frac{a_0}{2}\,x",
            r"+ \sum_{n=1}^{\infty}\!\left(",
            r"\frac{a_n}{n}\sin(nx)",
            r"- \frac{b_n}{n}\cos(nx)",
            r"\right) + C",
            font_size=BODY_SIZE, color=WHITE,
        )
        int_formula[2].set_color(SECONDARY)
        int_formula[3].set_color(SECONDARY)
        int_box = self.ly.formula_box(int_formula)
        self.play(Write(int_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "Dividing by n means integration attenuates higher "
            "frequencies. It is a low-pass filter. This is why "
            "integration always converges, even when f has "
            "jump discontinuities. The series smooths out.",
            duration=8,
        )

        self.play(FadeOut(int_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Differentiation: multiply by n (high-pass)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Integration: divide by n (low-pass)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Integration ALWAYS converges (smoothing effect)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Section Divider -- From Algebra to Extensions
    # ------------------------------------------------------------------ #
    def scene5_section_divider(self):
        self.ly.section_divider(2, "Extensions & Energy")
        self.add_subcaption(
            "Now that we understand how to manipulate Fourier "
            "series algebraically, let us see how to apply them "
            "to functions that are not naturally periodic.",
            duration=5,
        )
        self.wait(1.0)

    # ------------------------------------------------------------------ #
    # Scene 6: Even and Odd Extensions
    # ------------------------------------------------------------------ #
    def scene6_even_odd_extensions(self):
        self.add_subcaption(
            "Many problems, especially in partial differential "
            "equations, define a function only on a half "
            "interval, say zero to L. To use Fourier series, we "
            "need to extend the function to a full period.",
            duration=7,
        )
        title = self.ly.title("Even & Odd Extensions")

        self.add_subcaption(
            "We have two natural choices. An even extension "
            "mirrors the function symmetrically about zero. This "
            "produces a cosine-only series. An odd extension "
            "mirrors it antisymmetrically, producing a "
            "sine-only series.",
            duration=7,
        )

        items = [
            Text("Even extension: f_even(x) = f(|x|) on [-L, L]",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Only cosine terms survive (all b_n = 0)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Odd extension: f_odd(x) = sign(x) * f(|x|)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Only sine terms survive (all a_n = 0)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)

        self.add_subcaption(
            "The half-range cosine formula: a-sub-n equals "
            "two over L times the integral from zero to L of "
            "f of x, cosine n pi x over L, d x. For the "
            "sine series, replace cosine with sine.",
            duration=7,
        )

        cosine_coeff = MathTex(
            r"a_n = \frac{2}{L}\!\int_{0}^{L} f(x)\cos\!\left(\frac{n\pi x}{L}\right)dx",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        cosine_box = self.ly.formula_box(cosine_coeff)
        self.play(FadeOut(items[0]), FadeOut(items[1]), FadeOut(items[2]), FadeOut(items[3]), run_time=FAST)
        self.play(Write(cosine_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "The choice of extension matters for PDE boundary "
            "conditions. Dirichlet conditions, where the value "
            "is fixed at the boundary, use the sine series "
            "because it equals zero at the endpoints. Neumann "
            "conditions, where the derivative is fixed, use "
            "the cosine series because its derivative vanishes "
            "at the endpoints.",
            duration=10,
        )

        self.play(FadeOut(cosine_box), run_time=FAST)
        self.wait(0.5)

        pde_items = [
            Text("Dirichlet conditions -> sine series (f = 0 at boundary)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Neumann conditions -> cosine series (f' = 0 at boundary)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(pde_items, start_from=title)
        self.wait(3.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Parseval's Identity -- Energy Conservation
    # ------------------------------------------------------------------ #
    def scene7_parseval(self):
        self.add_subcaption(
            "Our final property is perhaps the most profound. "
            "Parseval's identity states that the total energy "
            "of a function equals the sum of energy in each "
            "of its Fourier coefficients.",
            duration=7,
        )
        title = self.ly.title("Parseval's Identity")

        self.add_subcaption(
            "Specifically: one over pi, times the integral from "
            "minus pi to pi of f of x squared, d x, equals "
            "a-sub-zero squared over two, plus the sum from "
            "n equals one to infinity of a-sub-n squared plus "
            "b-sub-n squared.",
            duration=9,
        )

        parseval = MathTex(
            r"\frac{1}{\pi}\!\int_{-\pi}^{\pi} |f(x)|^2\,dx",
            r"= \frac{a_0^2}{2} + \sum_{n=1}^{\infty}(a_n^2 + b_n^2)",
            font_size=BODY_SIZE, color=WHITE,
        )
        parseval[1].set_color(RED)
        parseval_box = self.ly.formula_box(parseval)
        self.play(Write(parseval_box), run_time=SLOW)
        self.wait(4.0)

        self.add_subcaption(
            "This is the Pythagorean theorem for infinite "
            "dimensions. In R-n, the squared norm of a vector "
            "equals the sum of squared components. In L-two, "
            "the squared norm of a function equals the sum "
            "of squared Fourier coefficients. The Fourier "
            "series is an isometry.",
            duration=10,
        )

        self.play(FadeOut(parseval_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Pythagorean theorem in infinite dimensions",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Signal power = sum of power per frequency",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Wave energy = sum of energy per mode",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)

        self.add_subcaption(
            "Parseval's identity tells us that the Fourier "
            "series does not lose or gain energy. It perfectly "
            "preserves the L-two norm. This is why truncating "
            "the series is safe: the discarded terms carry "
            "only a small amount of energy.",
            duration=8,
        )

        key = Text(
            "Fourier series is an isometry of L2",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.progressive_reveal([key])
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary(self):
        self.add_subcaption(
            "Let us review what we have learned about Fourier "
            "series properties.",
            duration=3,
        )
        title = self.ly.title("Summary")

        items = [
            Text("1. Linearity: Fourier coefficients are linear in f",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Differentiation: multiply by n (high-pass filter)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("3. Integration: divide by n (low-pass filter)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("4. Even/odd extensions for half-range problems",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)

        item5 = Text(
            "5. Parseval's identity: energy conservation in L2",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.progressive_reveal([item5])
        self.wait(3.0)

        self.add_subcaption(
            "In the next video, we will leave the world of "
            "periodic functions behind. The Fourier transform "
            "extends everything we have learned to functions "
            "defined on the entire real line. It is the bridge "
            "from periodic analysis to the frequency domain "
            "of all signals.",
            duration=9,
        )

        self.ly.clear()

        play_outro(
            self,
            next_video="The Fourier Transform",
            next_playlist="Fourier Analysis",
        )
