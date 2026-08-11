"""
Video 180: Parseval's Theorem -- Fourier Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video180_ParsevalsTheorem

Topics: Plancherel theorem, generalized Parseval identity,
        cross-correlation and autocorrelation, Wiener-Khinchin theorem,
        bandwidth-duration products, quantum mechanics application.

Prerequisites: Video 178 (Properties of Fourier Transform),
               Video 179 (Convolution Theorem).

Competitive insights:
- Steve Brunton covers Parseval briefly in Fourier lecture
- Dr. Peyam: whiteboard proof only
- Our unique angle: connect to autocorrelation, Wiener-Khinchin,
  and quantum mechanics for broad applications

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


class Video180_ParsevalsTheorem(Scene):
    """Parseval's Theorem -- Fourier Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_plancherel()
        self.scene3_generalized()
        self.scene4_correlation()
        self.scene5_wiener()
        self.scene6_bandwidth()
        self.scene7_quantum()
        self.scene8_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Energy conservation is the deepest theme in "
            "Fourier analysis. Parseval's theorem gives us "
            "a precise mathematical statement: the total "
            "energy of a function is the same whether we "
            "compute it in the time domain or the frequency "
            "domain.",
            duration=8,
        )
        play_intro(self, "Parseval's Theorem", "Fourier Analysis")

        title = self.ly.title("Energy in Two Domains")

        self.add_subcaption(
            "This is not just a theorem. It is the foundation "
            "of signal analysis, quantum mechanics, and "
            "communication theory. Let us explore its "
            "many faces.",
            duration=6,
        )
        items = [
            Text("Plancherel theorem: L2 norm preserved",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Generalized Parseval: inner product preserved",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Applications: correlation, quantum, signal processing",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Plancherel Theorem
    # ------------------------------------------------------------------ #
    def scene2_plancherel(self):
        self.add_subcaption(
            "The Plancherel theorem is the simplest form "
            "of energy conservation. It states that the "
            "L-two norm of f equals the L-two norm of "
            "its Fourier transform.",
            duration=6,
        )
        title = self.ly.title("Plancherel Theorem")

        plancherel = MathTex(
            r"\int_{-\infty}^{\infty}",
            r"|f(x)|^2\,dx",
            r"= \int_{-\infty}^{\infty}",
            r"|\hat{f}(\omega)|^2\,d\omega",
            font_size=BODY_SIZE, color=WHITE,
        )
        plancherel_box = self.ly.formula_box(plancherel, color=PRIMARY)
        self.play(Write(plancherel_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "The left side is the total energy in the time "
            "domain. The right side is the total energy in "
            "the frequency domain. They are exactly equal. "
            "This follows directly from the unitarity of "
            "the Fourier transform operator.",
            duration=8,
        )

        self.play(FadeOut(plancherel_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Time domain energy = frequency domain energy",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Follows from unitarity of the Fourier transform",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Generalized Parseval Identity
    # ------------------------------------------------------------------ #
    def scene3_generalized(self):
        self.ly.section_divider(1, "Generalized Parseval Identity")

        self.add_subcaption(
            "The generalized Parseval identity extends "
            "Plancherel from one function to two. The "
            "inner product of f and g in the time domain "
            "equals the inner product of their transforms "
            "in the frequency domain.",
            duration=8,
        )
        title = self.ly.title("Inner Product Preservation")

        parseval = MathTex(
            r"\int f(x)\,\overline{g(x)}\,dx",
            r"= \int \hat{f}(\omega)\,\overline{\hat{g}(\omega)}\,d\omega",
            font_size=BODY_SIZE, color=WHITE,
        )
        parseval_box = self.ly.formula_box(parseval, color=SECONDARY)
        self.play(Write(parseval_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "Setting g equal to f recovers the Plancherel "
            "theorem. This is a fundamental property of any "
            "unitary operator. In linear algebra terms, the "
            "Fourier transform is a change of orthonormal "
            "basis that preserves all geometric structure.",
            duration=9,
        )

        self.play(FadeOut(parseval_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Unitary operators preserve inner products",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("g = f recovers Plancherel theorem",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Analogy: rotation preserves dot products in R^n",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Cross-Correlation and Autocorrelation
    # ------------------------------------------------------------------ #
    def scene4_correlation(self):
        self.add_subcaption(
            "Correlation measures how similar two functions "
            "are at different time shifts. The cross-correlation "
            "of f and g is defined as the integral of f "
            "conjugate of t times g of t plus x dt.",
            duration=7,
        )
        title = self.ly.title("Cross-Correlation")

        cross = MathTex(
            r"(f \star g)(x)",
            r"= \int \overline{f(t)}\,g(t+x)\,dt",
            font_size=BODY_SIZE, color=WHITE,
        )
        cross_box = self.ly.formula_box(cross, color=PRIMARY)
        self.play(Write(cross_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "The Fourier transform of the cross-correlation "
            "is root 2 pi times F hat conjugate times G hat. "
            "For autocorrelation, when g equals f, this "
            "becomes root 2 pi times the magnitude of F hat "
            "squared. The autocorrelation theorem is a "
            "powerful tool in signal analysis.",
            duration=10,
        )

        self.play(FadeOut(cross_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Cross-corr transform: sqrt(2pi) * F-hat-conj * G-hat",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Autocorrelation: f star f -> sqrt(2pi) * |F-hat|^2",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Measures self-similarity at different time lags",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Wiener-Khinchin Theorem
    # ------------------------------------------------------------------ #
    def scene5_wiener(self):
        self.ly.section_divider(2, "Wiener-Khinchin Theorem")

        self.add_subcaption(
            "For a wide-sense stationary random process, the "
            "Wiener-Khinchin theorem states that the power "
            "spectral density is the Fourier transform of "
            "the autocorrelation function.",
            duration=7,
        )
        title = self.ly.title("Wiener-Khinchin Theorem")

        self.add_subcaption(
            "If R of tau is the autocorrelation function, "
            "then the power spectral density S of omega "
            "equals the Fourier transform of R. This connects "
            "time-domain statistics to frequency-domain "
            "energy distribution. It is the mathematical "
            "foundation of spectral analysis.",
            duration=9,
        )

        items = [
            Text("S(omega) = F[R(tau)] (power spectral density)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("R(tau) = F^{-1}[S(omega)] (autocorrelation)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Foundation of spectral analysis in engineering",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Bandwidth and Duration
    # ------------------------------------------------------------------ #
    def scene6_bandwidth(self):
        self.add_subcaption(
            "Parseval's theorem connects bandwidth and "
            "duration through energy. The essential bandwidth "
            "is the range of frequencies containing most of "
            "the signal's energy. We can quantify this using "
            "RMS bandwidth and RMS duration.",
            duration=8,
        )
        title = self.ly.title("Bandwidth-Duration Product")

        unc = MathTex(
            r"\sigma_t \cdot \sigma_\omega \geq \frac{1}{2}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        unc_box = self.ly.formula_box(unc, color=ACCENT)
        self.play(Write(unc_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "This is the uncertainty principle again. The "
            "product of RMS duration and RMS bandwidth is "
            "at least one half. The Gaussian achieves "
            "equality. This limits data compression and "
            "underlies Shannon's channel capacity theorem.",
            duration=8,
        )

        self.play(FadeOut(unc_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Gaussian: achieves minimum bandwidth-duration product",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Foundation of Shannon-Nyquist theory",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Quantum Mechanics Application
    # ------------------------------------------------------------------ #
    def scene7_quantum(self):
        self.add_subcaption(
            "In quantum mechanics, the position wave function "
            "psi of x and the momentum wave function psi hat "
            "of p are Fourier transform pairs. Parseval's "
            "theorem guarantees that the total probability "
            "is one in both representations.",
            duration=9,
        )
        title = self.ly.title("Quantum Mechanics")

        self.add_subcaption(
            "The probability density in position is the "
            "magnitude squared of psi. The probability density "
            "in momentum is the magnitude squared of psi hat. "
            "Parseval guarantees that integrating either one "
            "over the entire real line gives exactly one. "
            "The Heisenberg uncertainty principle follows "
            "directly from the Fourier uncertainty principle.",
            duration=10,
        )

        items = [
            Text("|psi(x)|^2: position probability density",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("|psi-hat(p)|^2: momentum probability density",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Parseval: both integrate to 1 (probability conserved)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Preview
    # ------------------------------------------------------------------ #
    def scene8_summary(self):
        self.add_subcaption(
            "Let us review what we learned about Parseval's "
            "theorem and its applications.",
            duration=3,
        )
        title = self.ly.title("Key Takeaways")

        self.add_subcaption(
            "First, Plancherel says the L-two norm is preserved "
            "by the Fourier transform. Second, the generalized "
            "Parseval identity preserves inner products. Third, "
            "the autocorrelation theorem connects self-similarity "
            "to energy spectrum. Fourth, the Wiener-Khinchin "
            "theorem links statistics to spectral density. "
            "And fifth, in quantum mechanics, probability is "
            "conserved between position and momentum.",
            duration=16,
        )

        items = [
            Text("1. Plancherel: ||f||_2 = ||F-hat||_2",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Parseval: inner product preserved",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Autocorrelation: f*f <-> sqrt(2pi)|F-hat|^2",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Wiener-Khinchin: power spectrum = F[autocorrelation]",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5. Quantum: probability conserved between domains",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)

        self.add_subcaption(
            "In the next video, we explore applications of "
            "Fourier analysis in signal processing, including "
            "filtering, sampling, and the FFT.",
            duration=5,
        )
        self.ly.clear()

        play_outro(
            self,
            next_video="Applications: Signal Processing",
            next_playlist="Fourier Analysis",
        )
