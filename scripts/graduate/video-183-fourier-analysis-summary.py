"""
Video 183: Fourier Analysis Summary -- Fourier Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video183_FourierAnalysisSummary

Topics: Recap of entire Fourier Analysis playlist (Videos 174-182),
        the Fourier analysis roadmap, connections between series and transform,
        the big picture (Hilbert space, unitarity, energy),
        what comes next (Differential Geometry, PDEs, or Number Theory).

Prerequisites: All 9 previous videos in the Fourier Analysis playlist.

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


class Video183_FourierAnalysisSummary(Scene):
    """Fourier Analysis Summary -- Final video of the playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_series_recap()
        self.scene3_transform_recap()
        self.scene4_deep_dives_recap()
        self.scene5_unifying_theme()
        self.scene6_roadmap()
        self.scene7_what_comes_next()
        self.scene8_farewell()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook — The Journey ~60s
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Over nine videos, we have built Fourier analysis from "
            "scratch. From Hilbert space foundations to real-world "
            "applications in signal processing and the heat equation. "
            "Today we step back and see the big picture.",
            duration=15,
        )
        play_intro(self, "Fourier Analysis Summary", "Fourier Analysis")

        title = self.ly.title("The Journey Through Fourier Analysis", color=ACCENT)

        self.add_subcaption(
            "We began with Fourier series on periodic functions, "
            "moved to the Fourier transform for non-periodic "
            "functions, proved the deep theorems, and applied "
            "everything to real problems.",
            duration=10,
        )
        items = [
            Text("9 videos, from series to applications", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("From Hilbert space foundations to the heat equation",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("A complete graduate-level treatment",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Let us see what connects it all",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            items, start_from=title, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.6,
        )
        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Fourier Series Recap ~100s
    # ------------------------------------------------------------------ #
    def scene2_series_recap(self):
        self.add_subcaption(
            "Videos 174 through 176 covered Fourier series. "
            "We viewed periodic functions as vectors in a "
            "Hilbert space, expanded them in an orthonormal "
            "trigonometric basis, and studied convergence.",
            duration=12,
        )
        self.ly.section_divider("1", "Fourier Series")

        self.ly.title("Videos 174-176: Fourier Series", color=PRIMARY)

        self.add_subcaption(
            "The key idea: every periodic function in L squared "
            "has a Fourier expansion. The coefficients are inner "
            "products with the trigonometric basis functions.",
            duration=8,
        )
        items = [
            Text("Periodic functions as Hilbert space vectors",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Orthonormal trigonometric basis",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Fourier coefficients as inner products",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            items, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.8,
        )
        self.wait(0.5)
        self.ly.clear()

        self.ly.title("Series: Convergence & Properties", color=SECONDARY)

        self.add_subcaption(
            "Dirichlet conditions guarantee pointwise convergence. "
            "Gibbs phenomenon appears at jump discontinuities. "
            "Linearity and symmetry properties simplify computation. "
            "Parseval's identity shows energy is conserved.",
            duration=10,
        )
        items2 = [
            Text("Dirichlet conditions: pointwise convergence",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Gibbs phenomenon at discontinuities",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Even/odd symmetry, linearity, Parseval",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(
            items2, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.8,
        )
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Fourier Transform Recap ~100s
    # ------------------------------------------------------------------ #
    def scene3_transform_recap(self):
        self.add_subcaption(
            "Videos 177 and 178 introduced the Fourier transform. "
            "We let the period go to infinity, converting sums "
            "into integrals. This extends Fourier analysis to "
            "non-periodic functions on the real line.",
            duration=12,
        )
        self.ly.section_divider("2", "Fourier Transform")

        self.ly.title("Videos 177-178: The Transform", color=PRIMARY)

        self.add_subcaption(
            "The forward transform maps a function from the time "
            "domain to the frequency domain. The inverse transform "
            "reconstructs the original. Together they form a "
            "unitary operator on L squared of R.",
            duration=9,
        )
        f_formula = MathTex(
            r"\hat{f}(\omega) = \int_{-\infty}^{\infty} f(t)\, e^{-i\omega t}\, dt",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        ensure_fits(f_formula)
        self.ly.center_in_content(f_formula)
        self.play(Write(f_formula), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

        self.ly.title("Transform: Key Properties", color=SECONDARY)

        self.add_subcaption(
            "The derivative property turns differentiation into "
            "multiplication. The convolution theorem converts "
            "convolution into pointwise multiplication. Plancherel "
            "and Parseval establish energy conservation.",
            duration=9,
        )
        items = [
            Text("Derivative property: multiplication by i*omega",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Convolution theorem: convolution becomes product",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Plancherel: energy conservation in frequency domain",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Duality: F(F(f))(x) = 2*pi*f(-x)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(
            items, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.6,
        )
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Deep Dives Recap ~100s
    # ------------------------------------------------------------------ #
    def scene4_deep_dives_recap(self):
        self.add_subcaption(
            "Videos 179 through 182 explored the deep results and "
            "applications. The convolution theorem, Parseval's "
            "theorem, signal processing, and the heat equation.",
            duration=10,
        )
        self.ly.section_divider("3", "Deep Dives & Applications")

        self.ly.title("Video 179: Convolution Theorem", color=PRIMARY)

        self.add_subcaption(
            "We proved the convolution theorem via Fubini, showing "
            "that convolution in the time domain equals multiplication "
            "in the frequency domain. This is the workhorse of "
            "Fourier analysis.",
            duration=8,
        )
        items = [
            Text("Convolution: flip, slide, integrate",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Proof via Fubini's theorem",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(
            items, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.8,
        )
        self.wait(0.5)
        self.ly.clear()

        self.ly.title("Video 180: Parseval's Theorem", color=SECONDARY)

        self.add_subcaption(
            "Parseval's theorem connects time-domain energy to "
            "frequency-domain energy. The Wiener-Khinchin theorem "
            "links autocorrelation to power spectral density.",
            duration=7,
        )
        items2 = [
            Text("Energy conservation across domains",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Wiener-Khinchin: autocorrelation to power spectrum",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            items2, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.8,
        )
        self.wait(0.5)
        self.ly.clear()

        self.ly.title("Videos 181-182: Applications", color=ACCENT)

        self.add_subcaption(
            "Signal processing brought sampling, aliasing, the "
            "FFT algorithm, and spectral analysis to life. The "
            "heat equation showed how the Fourier transform converts "
            "partial differential equations into algebra.",
            duration=8,
        )
        items3 = [
            Text("Signal processing: sampling, FFT, filtering",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Heat equation: PDEs become algebra via FT",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Heat kernel is a Gaussian: smoothing as low-pass filter",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            items3, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.6,
        )
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: The Unifying Theme — Unitary Operators ~100s
    # ------------------------------------------------------------------ #
    def scene5_unifying_theme(self):
        self.add_subcaption(
            "What connects everything in Fourier analysis? The answer "
            "is unitary operators on Hilbert spaces. Fourier series "
            "and the Fourier transform are both changes of orthonormal "
            "basis, and unitarity explains Parseval, Plancherel, and "
            "the four-fold identity.",
            duration=15,
        )
        self.ly.section_divider("4", "The Unifying Theme")

        self.ly.title("Unitary Operators on Hilbert Spaces", color=ACCENT)

        self.add_subcaption(
            "The Fourier series gives a unitary map on L squared "
            "of minus pi to pi. The Fourier transform gives a "
            "unitary map on L squared of R. In both cases, "
            "unitarity means inner products are preserved.",
            duration=10,
        )
        items = [
            Text("Fourier series: unitary on L^2[-pi, pi]",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Fourier transform: unitary on L^2(R)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Unitarity = preserve inner products",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            items, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(0.5)
        self.ly.clear()

        self.ly.title("Unitarity Explains Everything", color=RED)

        self.add_subcaption(
            "Parseval and Plancherel are just energy conservation "
            "from unitarity. The four-fold identity, Fourier of "
            "Fourier, follows from the duality inherent in the "
            "transform. Convolution becomes multiplication because "
            "unitary operators are algebra homomorphisms on the "
            "algebra of functions.",
            duration=14,
        )
        items2 = [
            Text("Parseval & Plancherel: energy conservation",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("F^4 = I: the four-fold identity",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Convolution theorem: algebra homomorphism",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            items2, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )

        self.add_subcaption(
            "At its core, Fourier analysis is the study of "
            "changes of orthonormal basis in function spaces. "
            "Time and frequency are just two different "
            "coordinates for the same vector.",
            duration=10,
        )
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: The Map of Fourier Analysis ~100s
    # ------------------------------------------------------------------ #
    def scene6_roadmap(self):
        self.add_subcaption(
            "Let us look at the full roadmap of what we have built. "
            "It all starts with Hilbert space foundations from "
            "our Functional Analysis playlist, and branches into "
            "theory and applications.",
            duration=12,
        )
        self.ly.section_divider("5", "The Fourier Analysis Roadmap")

        self.ly.title("Foundation Layer", color=PRIMARY)

        self.add_subcaption(
            "Everything rests on Hilbert spaces, inner products, "
            "and orthonormal bases. These were covered in our "
            "Functional Analysis playlist, Videos 164 through 165.",
            duration=8,
        )
        items = [
            Text("Hilbert spaces & inner products (Videos 164-165)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Bounded operators & dual space (Videos 166-167)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(
            items, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(0.5)
        self.ly.clear()

        self.ly.title("Series & Transform Layer", color=SECONDARY)

        self.add_subcaption(
            "Fourier series handles periodic functions. The "
            "Fourier transform extends this to the real line. "
            "Properties connect the two: convergence, duality, "
            "and the convolution theorem.",
            duration=9,
        )
        items2 = [
            Text("Fourier series: periodic functions (174-176)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Fourier transform: non-periodic functions (177-178)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Convolution & Parseval: deep theorems (179-180)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            items2, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.6,
        )
        self.wait(0.5)
        self.ly.clear()

        self.ly.title("Application Layer", color=ACCENT)

        self.add_subcaption(
            "Signal processing uses sampling, the FFT, and spectral "
            "analysis. The heat equation shows Fourier transforms "
            "solving partial differential equations. Both rely on "
            "the theoretical foundation we built.",
            duration=9,
        )
        items3 = [
            Text("Signal processing: FFT, sampling, filtering (181)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("PDEs: heat equation via Fourier (182)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Quantum mechanics, probability, and more",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            items3, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.6, wait_time=0.6,
        )
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: What Comes Next ~80s
    # ------------------------------------------------------------------ #
    def scene7_what_comes_next(self):
        self.add_subcaption(
            "Fourier analysis is not just a topic. It is a way of "
            "thinking that pervades all of mathematics. Let us "
            "survey where these ideas lead next.",
            duration=10,
        )
        self.ly.section_divider("6", "What Comes Next")

        self.ly.title("Future Frontiers", color=RED)

        self.add_subcaption(
            "Partial differential equations go deeper into the heat, "
            "wave, and Laplace equations using Fourier methods. "
            "Differential geometry extends Fourier analysis to "
            "manifolds and Lie groups.",
            duration=10,
        )
        items = [
            Text("PDEs: heat, wave, Laplace in depth",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Differential geometry: Fourier on manifolds",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(
            items, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(0.5)
        self.ly.clear()

        self.ly.title("More Frontiers", color=ACCENT)

        self.add_subcaption(
            "Number theory uses Dirichlet characters and modular "
            "forms, which are deeply Fourier-analytic. Probability "
            "theory connects through characteristic functions "
            "and the central limit theorem.",
            duration=10,
        )
        items2 = [
            Text("Number theory: Dirichlet characters, modular forms",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Probability: characteristic functions, CLT",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Quantum mechanics: spectral theory, entanglement",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(
            items2, start_from=None, reveal_anim=FadeIn,
            anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8,
        )
        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Farewell and Outro ~60s
    # ------------------------------------------------------------------ #
    def scene8_farewell(self):
        self.add_subcaption(
            "Thank you for completing the Fourier Analysis "
            "playlist. You now have a rigorous, visual "
            "understanding of one of mathematics' most "
            "powerful and beautiful frameworks.",
            duration=10,
        )
        self.ly.section_divider("", "Thank You")

        final = Text(
            "Every time you see oscillation, periodicity, "
            "or frequency, think Fourier.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        ensure_fits(final)
        self.ly.center_in_content(final)
        self.play(Write(final), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

        self.add_subcaption(
            "The Fourier transform is not just a topic. "
            "It is a way of thinking about the world.",
            duration=6,
        )
        tagline = Text(
            "Fourier analysis: the mathematics of frequency.",
            font_size=TITLE_SIZE, color=WHITE, font=SANS, weight=BOLD,
        )
        ensure_fits(tagline)
        self.ly.center_in_content(tagline)
        self.play(Write(tagline), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

        play_outro(self, next_video="Explore More", next_playlist="Next Playlist")
