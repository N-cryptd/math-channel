"""
Video 177: The Fourier Transform -- Fourier Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video177_FourierTransform

Topics: Derivation from Fourier series (periodic -> non-periodic),
        Forward and inverse Fourier transform definitions,
        Gaussian example (self-reciprocal),
        Rectangle function -> Sinc function,
        Basic properties (linearity, time shift, frequency shift, scaling),
        Time-frequency duality.

Prerequisites: Video 174 (Intro to Fourier Series),
               Video 175 (Convergence of Fourier Series),
               Video 176 (Fourier Series Properties),
               Video 165 (Hilbert Spaces).

Competitive insights:
- 3B1B 12.3M views: winding machine, no rigor, no definition, no examples
- BriTheMathGuy ~500K views: slides, formula-memorization approach
- Nobody derives FT from Fourier series with animation
- Our angle: natural limit T->infinity, rigorous conditions,
  animated Gaussian and rectangle/sinc examples, Hilbert space perspective

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


class Video177_FourierTransform(Scene):
    """The Fourier Transform -- Fourier Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_derivation()
        self.scene3_definition()
        self.scene4_section_divider()
        self.scene5_gaussian()
        self.scene6_rectangle_sinc()
        self.scene7_properties()
        self.scene8_duality()
        self.scene9_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook -- From Periodic to Everywhere
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "In the last three videos, we built a complete theory "
            "of Fourier series for periodic functions. We showed "
            "that any periodic function decomposes into sines and "
            "cosines via orthogonal projection in L two.",
            duration=8,
        )
        play_intro(self, "The Fourier Transform", "Fourier Analysis")

        title = self.ly.title("From Periodic to Everywhere")

        self.add_subcaption(
            "But what if your function is not periodic? What if it "
            "lives on the entire real line, stretching from minus "
            "infinity to infinity? Can we still decompose it "
            "into frequency components?",
            duration=7,
        )

        items = [
            Text("Fourier series: periodic functions on [-L, L]",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("What about non-periodic functions on (-inf, inf)?",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("The Fourier Transform: discrete -> continuous",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "The answer is yes. The Fourier transform is the "
            "natural extension of Fourier series. We get it by "
            "letting the period go to infinity. Let us see how.",
            duration=7,
        )
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: From Fourier Series to Fourier Transform -- The Limit
    # ------------------------------------------------------------------ #
    def scene2_derivation(self):
        self.add_subcaption(
            "We start with the complex Fourier series on the "
            "interval minus L to L. The function f has Fourier "
            "coefficients c sub n, and the series reconstructs "
            "f as a sum of complex exponentials.",
            duration=8,
        )
        title = self.ly.title("The Limit: Fourier Series -> Transform")

        series = MathTex(
            r"c_n = \frac{1}{2L}\!\int_{-L}^{L} f(t)\,e^{-i n\pi t/L}\,dt",
            font_size=BODY_SIZE, color=WHITE,
        )
        series_box = self.ly.formula_box(series)
        self.play(Write(series_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "Now define omega sub n equals n pi over L. This is "
            "the discrete frequency of the n-th harmonic. The "
            "spacing between consecutive frequencies is delta "
            "omega equals pi over L.",
            duration=7,
        )

        self.play(FadeOut(series_box), run_time=FAST)
        self.wait(0.5)

        omega_def = MathTex(
            r"\omega_n = \frac{n\pi}{L},",
            r"\;\;\Delta\omega = \frac{\pi}{L}",
            font_size=BODY_SIZE, color=WHITE,
        )
        omega_def[0].set_color(PRIMARY)
        omega_def[1].set_color(ACCENT)
        omega_box = self.ly.formula_box(omega_def)
        self.play(Write(omega_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "We can rewrite the Fourier series reconstruction "
            "using omega sub n. Each coefficient c sub n gets "
            "multiplied by delta omega and the exponential. "
            "This looks like a Riemann sum.",
            duration=8,
        )

        self.play(FadeOut(omega_box), run_time=FAST)
        self.wait(0.5)

        rewrite = MathTex(
            r"f(x) = \sum_{n}",
            r"\left[\frac{1}{2\pi}",
            r"\int_{-L}^{L} f(t)\,e^{-i\omega_n t}\,dt\right]",
            r"\Delta\omega\; e^{i\omega_n x}",
            font_size=BODY_SIZE, color=WHITE,
        )
        rewrite[0].set_color(PRIMARY)
        rewrite[3].set_color(ACCENT)
        rewrite_box = self.ly.formula_box(rewrite)
        self.play(Write(rewrite_box), run_time=SLOW)
        self.wait(4.0)

        self.add_subcaption(
            "Now let L go to infinity. The frequency spacing delta "
            "omega goes to zero, so the sum becomes an integral "
            "over omega. The discrete frequencies become a "
            "continuum. The Fourier transform emerges.",
            duration=8,
        )

        self.play(FadeOut(rewrite_box), run_time=FAST)
        self.wait(0.5)

        forward = MathTex(
            r"\hat{f}(\omega) = \int_{-\infty}^{\infty} f(t)\,e^{-i\omega t}\,dt",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        forward_box = self.ly.formula_box(forward, color=PRIMARY)
        self.play(Write(forward_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "This is the forward Fourier transform. It takes a "
            "function of time and produces a function of "
            "frequency. The inverse transform reconstructs the "
            "original function from its frequency content.",
            duration=7,
        )

        self.play(FadeOut(forward_box), run_time=FAST)
        self.wait(0.5)

        inverse = MathTex(
            r"f(x) = \frac{1}{2\pi}\!\int_{-\infty}^{\infty}"
            r"\hat{f}(\omega)\,e^{i\omega x}\,d\omega",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        inverse_box = self.ly.formula_box(inverse, color=SECONDARY)
        self.play(Write(inverse_box), run_time=SLOW)
        self.wait(3.0)

        key = Text(
            "Fourier transform = limit of Fourier series as L -> infinity",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(key, DOWN, inverse_box, buff=0.5)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: The Definition -- Forward and Inverse
    # ------------------------------------------------------------------ #
    def scene3_definition(self):
        self.add_subcaption(
            "Let us state the Fourier transform pair formally "
            "and discuss the conditions under which it is "
            "well-defined.",
            duration=5,
        )
        title = self.ly.title("The Fourier Transform: Definition")

        self.add_subcaption(
            "The forward Fourier transform takes f as input and "
            "produces f-hat of omega. The integral runs over "
            "the entire real line, and the exponential extracts "
            "the frequency omega component from f.",
            duration=7,
        )

        forward = MathTex(
            r"\hat{f}(\omega)",
            r"= \mathcal{F}\{f\}(\omega)",
            r"= \int_{-\infty}^{\infty} f(t)\,e^{-i\omega t}\,dt",
            font_size=BODY_SIZE, color=WHITE,
        )
        forward[0].set_color(PRIMARY)
        forward[1].set_color(DIM)
        forward_box = self.ly.formula_box(forward)
        self.play(Write(forward_box), run_time=SLOW)
        self.wait(4.0)

        self.add_subcaption(
            "The inverse Fourier transform reconstructs f from "
            "its frequency content. Note the one over two pi "
            "factor and the sign change in the exponential.",
            duration=7,
        )

        self.play(FadeOut(forward_box), run_time=FAST)
        self.wait(0.5)

        inverse = MathTex(
            r"f(x)",
            r"= \frac{1}{2\pi}\!\int_{-\infty}^{\infty}"
            r"\hat{f}(\omega)\,e^{i\omega x}\,d\omega",
            font_size=BODY_SIZE, color=WHITE,
        )
        inverse[0].set_color(SECONDARY)
        inverse_box = self.ly.formula_box(inverse)
        self.play(Write(inverse_box), run_time=SLOW)
        self.wait(4.0)

        self.add_subcaption(
            "For the integral to converge, we need f to be in "
            "L one, meaning absolutely integrable. For the "
            "inversion formula to hold pointwise, we also need "
            "f-hat to be in L one and f to be continuous.",
            duration=8,
        )

        self.play(FadeOut(inverse_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("f in L1(R): forward transform integral converges",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("f-hat in L1 + f continuous: inversion holds",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("L2(R): extend by density (Plancherel theorem)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Section Divider -- From Theory to Examples
    # ------------------------------------------------------------------ #
    def scene4_section_divider(self):
        self.ly.section_divider(2, "Examples & Properties")
        self.add_subcaption(
            "Now that we have the definition, let us see what "
            "the Fourier transform actually does to specific "
            "functions.",
            duration=5,
        )
        self.wait(1.0)

    # ------------------------------------------------------------------ #
    # Scene 5: Example 1 -- The Gaussian
    # ------------------------------------------------------------------ #
    def scene5_gaussian(self):
        self.add_subcaption(
            "The most important example by far is the Gaussian. "
            "We will see that the Fourier transform of a "
            "Gaussian is another Gaussian. It is self-reciprocal.",
            duration=7,
        )
        title = self.ly.title("Example 1: The Gaussian")

        self.add_subcaption(
            "Start with f of x equals e to the minus a x squared, "
            "where a is positive. This is a bell curve centered "
            "at zero with width controlled by a.",
            duration=6,
        )

        gaussian = MathTex(
            r"f(x) = e^{-ax^2},",
            r"\;\;a > 0",
            font_size=BODY_SIZE, color=WHITE,
        )
        gaussian[0].set_color(PRIMARY)
        gaussian_box = self.ly.formula_box(gaussian)
        self.play(Write(gaussian_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "Computing the transform by completing the square "
            "in the exponent gives a remarkable result.",
            duration=5,
        )

        self.play(FadeOut(gaussian_box), run_time=FAST)
        self.wait(0.5)

        result = MathTex(
            r"\hat{f}(\omega) = \sqrt{\frac{\pi}{a}}\;e^{-\omega^2/(4a)}",
            font_size=BODY_SIZE, color=WHITE,
        )
        result_box = self.ly.formula_box(result, color=SECONDARY)
        self.play(Write(result_box), run_time=SLOW)
        self.wait(4.0)

        self.add_subcaption(
            "The Fourier transform of a Gaussian is a Gaussian. "
            "This is extraordinary. A wider Gaussian in time "
            "produces a narrower one in frequency, and vice "
            "versa. When a equals one half, the transform "
            "equals the original function exactly.",
            duration=9,
        )

        self.play(FadeOut(result_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Gaussian -> Gaussian (self-reciprocal)",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Wider in time <-> narrower in frequency",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Heisenberg uncertainty: cannot be narrow in both",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Example 2 -- The Rectangle Function and Sinc
    # ------------------------------------------------------------------ #
    def scene6_rectangle_sinc(self):
        self.add_subcaption(
            "Our second example is the rectangle function, "
            "which equals one on a finite interval and zero "
            "outside. Its Fourier transform is the sinc "
            "function.",
            duration=7,
        )
        title = self.ly.title("Example 2: Rectangle -> Sinc")

        self.add_subcaption(
            "The rectangle function is one for x between minus "
            "one half and one half, and zero otherwise. "
            "Computing its transform is a straightforward "
            "integral of the exponential.",
            duration=7,
        )

        rect = MathTex(
            r"f(x) = \text{rect}(x) = "
            r"\begin{cases} 1 & |x| < 1/2 \\ 0 & |x| > 1/2 \end{cases}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        rect_box = self.ly.formula_box(rect)
        self.play(Write(rect_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "The integral of e to the minus i omega x from "
            "minus one half to one half gives the sinc "
            "function. The sinc oscillates with lobes that "
            "decay like one over omega.",
            duration=7,
        )

        self.play(FadeOut(rect_box), run_time=FAST)
        self.wait(0.5)

        sinc_result = MathTex(
            r"\hat{f}(\omega) = \frac{\sin(\omega/2)}{\omega/2}"
            r"= \text{sinc}\!\left(\frac{\omega}{2\pi}\right)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        sinc_box = self.ly.formula_box(sinc_result)
        self.play(Write(sinc_box), run_time=SLOW)
        self.wait(4.0)

        self.add_subcaption(
            "A sharp-edged function produces infinite "
            "oscillation. This is the continuous analogue of "
            "the Gibbs phenomenon. In signal processing, "
            "windowing a signal multiplies by a rectangle, "
            "which convolves the spectrum with a sinc.",
            duration=8,
        )

        self.play(FadeOut(sinc_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Sharp edge (rectangle) -> infinite oscillation (sinc)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Continuous analogue of the Gibbs phenomenon",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Basic Properties
    # ------------------------------------------------------------------ #
    def scene7_properties(self):
        self.add_subcaption(
            "The Fourier transform satisfies a powerful set "
            "of algebraic properties. These are the tools "
            "that make the transform practical.",
            duration=6,
        )
        title = self.ly.title("Basic Properties of the Transform")

        # Property 1: Linearity
        self.add_subcaption(
            "Linearity: the transform of a sum is the sum of "
            "the transforms. This follows directly from "
            "linearity of the integral.",
            duration=5,
        )

        linearity = MathTex(
            r"\mathcal{F}\{\alpha f + \beta g\}",
            r"= \alpha\,\hat{f} + \beta\,\hat{g}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        linearity_box = self.ly.formula_box(linearity, color=PRIMARY)
        self.play(Write(linearity_box), run_time=SLOW)
        self.wait(3.0)
        self.play(FadeOut(linearity_box), run_time=FAST)
        self.wait(0.5)

        # Property 2: Time shift
        self.add_subcaption(
            "Time shift: delaying a function by t sub zero "
            "multiplies its transform by a phase factor. "
            "The magnitude of the spectrum is unchanged.",
            duration=6,
        )

        tshift = MathTex(
            r"\mathcal{F}\{f(t - t_0)\}",
            r"= e^{-i\omega t_0}\,\hat{f}(\omega)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        tshift_box = self.ly.formula_box(tshift, color=SECONDARY)
        self.play(Write(tshift_box), run_time=SLOW)
        self.wait(3.0)
        self.play(FadeOut(tshift_box), run_time=FAST)
        self.wait(0.5)

        # Property 3: Frequency shift
        self.add_subcaption(
            "Frequency shift, also called modulation: "
            "multiplying f by e to the i omega zero t shifts "
            "the spectrum by omega zero. This is the "
            "mathematical basis of AM radio.",
            duration=7,
        )

        fshift = MathTex(
            r"\mathcal{F}\{f(t)\,e^{i\omega_0 t}\}",
            r"= \hat{f}(\omega - \omega_0)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        fshift_box = self.ly.formula_box(fshift, color=ACCENT)
        self.play(Write(fshift_box), run_time=SLOW)
        self.wait(3.0)
        self.play(FadeOut(fshift_box), run_time=FAST)
        self.wait(0.5)

        # Property 4: Scaling
        self.add_subcaption(
            "Scaling: compressing a function in time by "
            "factor a stretches its spectrum by one over "
            "a. The Gaussian self-reciprocity was a special "
            "case of this duality.",
            duration=7,
        )

        scaling = MathTex(
            r"\mathcal{F}\{f(at)\}",
            r"= \frac{1}{|a|}\,\hat{f}\!\left(\frac{\omega}{a}\right)",
            font_size=BODY_SIZE, color=RED,
        )
        scaling_box = self.ly.formula_box(scaling, color=RED)
        self.play(Write(scaling_box), run_time=SLOW)
        self.wait(3.0)
        self.play(FadeOut(scaling_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("1. Linearity: transform of sum = sum of transforms",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Time shift: delay -> phase factor (magnitude preserved)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Modulation: multiply by exponential -> shift spectrum",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Scaling: compress time <-> stretch frequency",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Duality -- The Deep Symmetry
    # ------------------------------------------------------------------ #
    def scene8_duality(self):
        self.add_subcaption(
            "The most beautiful property of the Fourier "
            "transform is duality. The forward and inverse "
            "transforms are essentially the same operation.",
            duration=6,
        )
        title = self.ly.title("Duality: Time and Frequency are Symmetric")

        self.add_subcaption(
            "If the Fourier transform of f is F, then the "
            "Fourier transform of F, evaluated at negative x "
            "and divided by two pi, gives back f. The forward "
            "and inverse transforms mirror each other.",
            duration=8,
        )

        duality = MathTex(
            r"\text{If } \hat{f} = \mathcal{F}\{f\},",
            r"\;\;\text{then } \mathcal{F}\{\hat{f}\}(x)",
            r"= 2\pi\,f(-x)",
            font_size=BODY_SIZE, color=WHITE,
        )
        duality[0].set_color(PRIMARY)
        duality[1].set_color(SECONDARY)
        duality[2].set_color(RED)
        duality_box = self.ly.formula_box(duality)
        self.play(Write(duality_box), run_time=SLOW)
        self.wait(4.0)

        self.add_subcaption(
            "There is no privileged domain. Time and frequency "
            "play symmetric roles. This is why the Gaussian "
            "is self-reciprocal: it is fixed by this "
            "symmetry. This is also the mathematical root "
            "of the Heisenberg uncertainty principle.",
            duration=9,
        )

        self.play(FadeOut(duality_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Forward and inverse are essentially the same",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Time and frequency are symmetric -- no privileged domain",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Gaussian self-reciprocity follows from this symmetry",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 9: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene9_summary(self):
        self.add_subcaption(
            "Let us review what we have learned about the "
            "Fourier transform.",
            duration=3,
        )
        title = self.ly.title("Summary")

        items = [
            Text("1. Fourier transform = limit of series as L -> inf",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Forward: F(omega) = integral f(t) e^{-i*omega*t} dt",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Gaussian -> Gaussian; Rectangle -> Sinc",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Properties: linearity, shifting, scaling, duality",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)

        self.add_subcaption(
            "In the next video, we will explore the convolution "
            "theorem, the most powerful property of the Fourier "
            "transform. It connects multiplication in one domain "
            "to convolution in the other, and it is the "
            "foundation of modern signal processing.",
            duration=9,
        )

        self.ly.clear()

        play_outro(
            self,
            next_video="The Convolution Theorem",
            next_playlist="Fourier Analysis",
        )
