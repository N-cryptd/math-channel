"""
Video 174: Introduction to Fourier Series -- Fourier Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video174_FourierSeriesIntro

Topics: Periodic functions as infinite-dimensional vectors,
        Trigonometric basis in L2,
        Fourier coefficients as inner products,
        Building partial sums with animated convergence,
        Square wave example with computation,
        Gibbs phenomenon with visual,
        Applications and connection to Functional Analysis.

Prerequisites: Video 165 (Hilbert Spaces), Video 164 (Inner Product Spaces),
               Video 166 (Bounded Linear Operators).

Competitive insights:
- 3B1B's Fourier Transform (12.3M views) uses winding machine -- we use Hilbert space projection
- No channel provides a full Fourier Analysis playlist with Manim animations
- Our unique angle: connect to completed Functional Analysis content
- Visual approach: geometric projection, partial sum convergence, Gibbs phenomenon

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


class Video174_FourierSeriesIntro(Scene):
    """Introduction to Fourier Series -- Fourier Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_motivation()
        self.scene3_trig_basis()
        self.scene4_coefficients()
        self.scene5_series_formula()
        self.scene6_square_wave_setup()
        self.scene7_square_wave_result()
        self.scene8_gibbs()
        self.scene9_applications()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook -- The Universal Language of Waves
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Every sound you hear, every image you see, every signal that "
            "travels through space. At its heart, it is just waves.",
            duration=5,
        )
        play_intro(self, "Introduction to Fourier Series", "Fourier Analysis")

        title = self.ly.title("The Language of Waves")

        self.add_subcaption(
            "And there is a remarkable fact. Any periodic wave, no matter "
            "how complex, can be built from simple sine and cosine waves.",
            duration=5,
        )
        items = [
            Text("Any periodic function",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("= sum of sines and cosines",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "This is Fourier series. It connects everything we learned "
            "about Hilbert spaces to the real world of signals and waves.",
            duration=5,
        )
        item3 = Text(
            "Connects Hilbert spaces to real-world signals",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.progressive_reveal([item3])
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Motivation -- Why Decompose Functions?
    # ------------------------------------------------------------------ #
    def scene2_motivation(self):
        self.add_subcaption(
            "Why would we want to break a function into pieces?",
            duration=3,
        )
        title = self.ly.title("Why Decompose Functions?")

        self.add_subcaption(
            "In linear algebra, we decompose vectors into components "
            "along basis vectors. A vector in R-two splits into x "
            "and y components. Each component tells us how much of "
            "that basis direction the vector has.",
            duration=6,
        )
        items = [
            Text("In R2: v = v_x e_x + v_y e_y",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Each coefficient: how much of that basis direction?",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "A function is an infinite-dimensional vector. The "
            "same idea applies. We decompose a function into "
            "components along basis functions. Fourier series "
            "chooses sines and cosines as the basis.",
            duration=6,
        )
        item3 = Text(
            "Functions are infinite-dimensional vectors",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        item4 = Text(
            "Decompose into sine and cosine components",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.progressive_reveal([item3, item4])
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: The Trigonometric Basis
    # ------------------------------------------------------------------ #
    def scene3_trig_basis(self):
        self.add_subcaption(
            "In L-two of zero to two pi, the set of all functions "
            "sine n x and cosine n x, for n equals zero, one, "
            "two, and so on, forms an orthonormal basis. This means "
            "every square-integrable function can be written as "
            "a unique combination of these trig functions.",
            duration=8,
        )
        title = self.ly.title("The Trigonometric Basis")

        items = [
            Text("In L2[0, 2pi], the functions {1, cos(nx), sin(nx)}",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("form a complete orthonormal basis",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "The inner product in L-two is the integral of f "
            "times g. Two functions are orthogonal when this "
            "integral equals zero. The sine and cosine functions "
            "are pairwise orthogonal, which makes computing "
            "Fourier coefficients remarkably clean.",
            duration=8,
        )

        # Show inner product formula
        inner_prod = MathTex(
            r"\langle f, g \rangle = \int_{0}^{2\pi} f(x)\,g(x)\,dx",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        inner_box = self.ly.formula_box(inner_prod)
        self.play(FadeOut(items[0]), FadeOut(items[1]), run_time=FAST)
        self.play(FadeIn(inner_box, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)

        ortho = Text(
            "sin(nx) and cos(mx) are orthogonal for all n, m",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(ortho, DOWN, inner_box, buff=0.5)
        self.play(FadeIn(ortho, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Fourier Coefficients as Projections
    # ------------------------------------------------------------------ #
    def scene4_coefficients(self):
        self.add_subcaption(
            "The Fourier coefficients tell us how much of each sine "
            "and cosine frequency is present in our function.",
            duration=4,
        )
        title = self.ly.title("Fourier Coefficients")

        self.add_subcaption(
            "For a function f with period two pi, the n-th cosine "
            "coefficient a-sub-n equals one over pi, times the "
            "integral from zero to two pi of f of x, cosine n x, "
            "d x. This is exactly the projection of f onto the "
            "cosine n x basis function.",
            duration=8,
        )

        a_n = MathTex(
            r"a_n = \frac{1}{\pi}\int_{0}^{2\pi} f(x)\cos(nx)\,dx",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        a_n_box = self.ly.formula_box(a_n)
        self.play(Write(a_n_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "Similarly, the n-th sine coefficient b-sub-n equals "
            "one over pi, times the integral from zero to two pi "
            "of f of x, sine n x, d x. And the constant term a-sub-"
            "zero over two is the average value of the function.",
            duration=8,
        )

        self.play(FadeOut(a_n_box), run_time=FAST)
        self.wait(0.5)

        b_n = MathTex(
            r"b_n = \frac{1}{\pi}\int_{0}^{2\pi} f(x)\sin(nx)\,dx",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        b_n_box = self.ly.formula_box(b_n)
        self.play(Write(b_n_box), run_time=SLOW)
        self.wait(2.5)

        a0 = Text(
            "a_0 / 2 = average value of f(x)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(a0, DOWN, b_n_box, buff=0.5)
        self.play(FadeIn(a0, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: The Fourier Series Formula
    # ------------------------------------------------------------------ #
    def scene5_series_formula(self):
        self.add_subcaption(
            "The Fourier series of f is the sum over all n, from "
            "one to infinity, of a-sub-n cosine n x plus b-sub-n "
            "sine n x, plus the constant term a-sub-zero over two.",
            duration=6,
        )
        title = self.ly.title("The Fourier Series")

        series = MathTex(
            r"f(x) = \frac{a_0}{2}",
            r"+ \sum_{n=1}^{\infty}",
            r"\left(a_n \cos(nx) + b_n \sin(nx)\right)",
            font_size=BODY_SIZE, color=WHITE,
        )
        series_box = self.ly.formula_box(series)
        self.play(Write(series_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "As we include more terms in the partial sum, the "
            "approximation gets closer and closer to the original "
            "function. With just the first harmonic, we capture "
            "the overall shape. With five terms, the details "
            "emerge. With twenty terms, the approximation is "
            "nearly indistinguishable from the original.",
            duration=10,
        )

        self.play(FadeOut(series_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("S_1(x): fundamental frequency only",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("S_5(x): first five harmonics combined",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("S_20(x): very close to the original",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Example -- Square Wave Setup
    # ------------------------------------------------------------------ #
    def scene6_square_wave_setup(self):
        self.ly.section_divider(1, "Example: Square Wave")

        self.add_subcaption(
            "Let us compute the Fourier series of a square wave. "
            "This function equals one on the interval zero to pi, "
            "and minus one on pi to two pi.",
            duration=5,
        )
        title = self.ly.title("Square Wave Definition")

        items = [
            Text("f(x) = 1 for x in [0, pi]",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("f(x) = -1 for x in [pi, 2pi]",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Period: 2pi",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "Because the square wave is an odd function, meaning "
            "f of minus x equals minus f of x, all cosine "
            "coefficients a-sub-n are zero. We only need the "
            "sine coefficients.",
            duration=6,
        )
        item4 = Text(
            "Odd function => all a_n = 0",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.progressive_reveal([item4])
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Square Wave Result
    # ------------------------------------------------------------------ #
    def scene7_square_wave_result(self):
        self.add_subcaption(
            "Computing the sine coefficients, we find that "
            "b-sub-n equals four over pi n when n is odd, and "
            "zero when n is even. So the Fourier series of the "
            "square wave contains only odd harmonics.",
            duration=7,
        )
        title = self.ly.title("Square Wave Fourier Series")

        b_formula = MathTex(
            r"b_n = \frac{4}{\pi n}\quad\text{for odd } n",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        b_box = self.ly.formula_box(b_formula)
        self.play(Write(b_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "So the series is four over pi, times sine x plus "
            "sine three x over three, plus sine five x over "
            "five, and so on. Each term is smaller than the last, "
            "and the sum converges to the square wave.",
            duration=7,
        )

        self.play(FadeOut(b_box), run_time=FAST)
        self.wait(0.5)

        result = MathTex(
            r"f(x) = \frac{4}{\pi}\!\left(",
            r"\sin x + \frac{\sin 3x}{3}",
            r"+ \frac{\sin 5x}{5} + \cdots\right)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        result_box = self.ly.formula_box(result)
        self.play(Write(result_box), run_time=SLOW)
        self.wait(4.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: The Gibbs Phenomenon
    # ------------------------------------------------------------------ #
    def scene8_gibbs(self):
        self.ly.section_divider(2, "The Gibbs Phenomenon")

        self.add_subcaption(
            "Now look closely at the partial sums near the jump "
            "discontinuities of the square wave. Something strange "
            "happens. The approximation overshoots.",
            duration=5,
        )
        title = self.ly.title("Overshoot at Discontinuities")

        items = [
            Text("Near jumps, partial sums overshoot the target",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Overshoot is approximately 9% of the jump height",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "The surprising fact is that this overshoot never "
            "goes away, no matter how many terms we add. Even as "
            "N goes to infinity, the overshoot persists at the "
            "same height. This is the Gibbs phenomenon. It is "
            "a fundamental limitation of Fourier approximation "
            "at jump discontinuities.",
            duration=9,
        )
        item3 = Text(
            "Overshoot persists even as N approaches infinity",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item4 = Text(
            "Pointwise convergence fails at discontinuities",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.progressive_reveal([item3, item4])
        self.wait(2.0)

        self.add_subcaption(
            "The Gibbs overshoot equals approximately zero point "
            "zero eight nine, times the jump height. More "
            "precisely, it is related to the sine integral "
            "evaluated at pi.",
            duration=6,
        )

        gibbs = MathTex(
            r"\text{Gibbs overshoot} \approx 0.08949 \times (\text{jump height})",
            font_size=BODY_SIZE, color=RED,
        )
        gibbs_box = self.ly.formula_box(gibbs)
        self.play(FadeOut(items[0]), FadeOut(items[1]), FadeOut(item3), FadeOut(item4), run_time=FAST)
        self.play(Write(gibbs_box), run_time=SLOW)
        self.wait(3.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 9: Applications and Outro
    # ------------------------------------------------------------------ #
    def scene9_applications(self):
        self.add_subcaption(
            "Fourier series is not just theory. It powers some of "
            "the most important technologies we use every day.",
            duration=4,
        )
        title = self.ly.title("Why Fourier Series Matters")

        items = [
            Text("Audio compression: MP3, AAC, OGG",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Image processing: JPEG, edge detection",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Physics: heat equation, wave equation, quantum mechanics",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Engineering: signal transmission, filtering, radar",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)

        self.add_subcaption(
            "In the next video, we will study convergence of "
            "Fourier series. When does the series actually equal "
            "the function? What conditions on f guarantee this? "
            "These questions lead us to some of the most beautiful "
            "theorems in analysis. For now, remember this: every "
            "periodic function has a voice, and Fourier series "
            "lets us hear each frequency separately.",
            duration=12,
        )
        self.ly.clear()

        play_outro(
            self,
            next_video="Convergence of Fourier Series",
            next_playlist="Fourier Analysis",
        )
