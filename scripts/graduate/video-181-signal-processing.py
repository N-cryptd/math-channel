"""
Video 181: Applications in Signal Processing -- Fourier Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video181_SignalProcessing

Topics: Nyquist-Shannon sampling theorem, aliasing, DFT and FFT algorithm,
        windowing, spectral leakage, practical filter design, STFT for
        time-frequency analysis, real-world applications.

Prerequisites: Video 177 (The Fourier Transform),
               Video 178 (FT Properties),
               Video 179 (Convolution Theorem),
               Video 180 (Parseval's Theorem).

Competitive insights:
- Reducible: FFT via polynomial multiplication (2.2M views), no signal processing
- 3B1B: FT intuition only, no discrete/sampling/FFT
- Marshall Bruner: aliasing visual, narrow scope
- Rich Radke: rigorous sampling theorem, zero visuals
- Our unique angle: unified animated signal processing from theory to practice

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


class Video181_SignalProcessing(Scene):
    """Applications in Signal Processing -- Fourier Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_sampling()
        self.scene3_aliasing()
        self.scene4_dft_fft()
        self.scene5_windowing()
        self.scene6_filter_design()
        self.scene7_stft()
        self.scene8_applications()
        self.scene9_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Over seven videos we have built the Fourier transform "
            "from first principles. Now comes the payoff. Every "
            "phone call, every digital image, every song you stream "
            "uses Fourier analysis.",
            duration=8,
        )
        play_intro(self, "Applications: Signal Processing", "Fourier Analysis")

        title = self.ly.title("From Abstract to Applied")

        self.add_subcaption(
            "The Fourier transform is the engine of modern "
            "communication. Let us see how abstract theory "
            "becomes engineering practice.",
            duration=6,
        )
        items = [
            Text("Sample: continuous signals become discrete data",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Transform: FFT converts time to frequency",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Analyze: spectrograms reveal time-frequency structure",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: The Sampling Theorem
    # ------------------------------------------------------------------ #
    def scene2_sampling(self):
        self.add_subcaption(
            "A continuous signal lives on the real line, but "
            "computers work with discrete data. We sample the "
            "signal at uniform time intervals. The key question "
            "is: how fast must we sample to avoid losing information?",
            duration=9,
        )
        title = self.ly.title("The Sampling Theorem")

        nyquist = MathTex(
            r"x[n] = x\!\left(\frac{n}{f_s}\right)",
            font_size=BODY_SIZE, color=WHITE,
        )
        nyquist_box = self.ly.formula_box(nyquist, color=PRIMARY)
        self.play(Write(nyquist_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "The Nyquist-Shannon sampling theorem gives the "
            "answer. If a signal has bandwidth B, meaning its "
            "Fourier transform is zero outside minus B to B, "
            "then sampling at a rate f sub s greater than 2B "
            "allows perfect reconstruction.",
            duration=10,
        )

        self.play(FadeOut(nyquist_box), run_time=FAST)
        self.wait(0.5)

        theorem = MathTex(
            r"f_s > 2B \implies \text{perfect reconstruction}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        theorem_box = self.ly.formula_box(theorem, color=ACCENT)
        self.play(Write(theorem_box), run_time=SLOW)
        self.wait(2.0)

        self.add_subcaption(
            "The critical rate 2B is called the Nyquist rate. "
            "Sampling above this rate preserves all the "
            "information in the signal. This follows from the "
            "Poisson summation formula applied to the Fourier "
            "transform of the sampled signal.",
            duration=8,
        )

        self.play(FadeOut(theorem_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Bandwidth B: FT zero outside [-B, B]",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Nyquist rate: f_s > 2B (sufficient condition)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Aliasing
    # ------------------------------------------------------------------ #
    def scene3_aliasing(self):
        self.add_subcaption(
            "What happens when we violate the sampling theorem? "
            "If we sample too slowly, high frequencies masquerade "
            "as low frequencies. This is called aliasing.",
            duration=7,
        )
        title = self.ly.title("Aliasing")

        self.add_subcaption(
            "A high frequency sine wave sampled below the Nyquist "
            "rate produces the same sample points as a low frequency "
            "sine wave. The two signals are indistinguishable. In "
            "the frequency domain, spectral copies overlap and "
            "destroy the original spectrum.",
            duration=10,
        )

        items = [
            Text("Undersampling: f_s < 2B",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("High frequencies fold back as low frequencies",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Frequency domain: spectral copies overlap",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

        self.add_subcaption(
            "Anti-aliasing is essential in practice. Before "
            "sampling, we pass the signal through a low-pass filter "
            "that removes frequencies above the Nyquist frequency. "
            "This prevents folding and ensures faithful "
            "reconstruction.",
            duration=8,
        )

        title2 = self.ly.title("Anti-Aliasing")
        items2 = [
            Text("Low-pass filter before sampling (analog or digital)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Removes frequencies above f_s / 2",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: The DFT and FFT Algorithm
    # ------------------------------------------------------------------ #
    def scene4_dft_fft(self):
        self.ly.section_divider(1, "The DFT and FFT Algorithm")

        self.add_subcaption(
            "On a computer we work with discrete sequences. The "
            "Discrete Fourier Transform maps N time-domain samples "
            "to N frequency-domain coefficients.",
            duration=7,
        )
        title = self.ly.title("Discrete Fourier Transform")

        dft = MathTex(
            r"X[k] = \sum_{n=0}^{N-1} x[n]\, e^{-i 2\pi k n / N}",
            font_size=BODY_SIZE, color=WHITE,
        )
        dft_box = self.ly.formula_box(dft, color=PRIMARY)
        self.play(Write(dft_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "Computing each of the N outputs requires N multiplications, "
            "giving O(N squared) total. For a one-second audio clip at "
            "44 kilohertz, that is over one billion operations.",
            duration=7,
        )

        self.play(FadeOut(dft_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Direct computation: O(N^2) multiplications",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("1 second of 44kHz audio: N = 44000, over 10^9 ops",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

        self.add_subcaption(
            "The Cooley-Tukey Fast Fourier Transform exploits the "
            "periodicity of complex exponentials. By splitting the "
            "sum into even and odd indexed terms, the N-point DFT "
            "decomposes into two N-over-2 point DFTs. Repeating this "
            "gives O(N log N) complexity.",
            duration=10,
        )

        title2 = self.ly.title("The FFT: O(N log N)")

        self.add_subcaption(
            "For N = 44000, the FFT needs only about 600000 "
            "operations instead of one billion. This thousand-fold "
            "speedup turned Fourier analysis from a mathematical "
            "curiosity into the workhorse of digital signal processing.",
            duration=8,
        )

        items2 = [
            Text("Split into even/odd sums recursively",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Butterfly pattern: combine results efficiently",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("O(N log N) vs O(N^2): 1000x speedup at N=44000",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Windowing and Spectral Leakage
    # ------------------------------------------------------------------ #
    def scene5_windowing(self):
        self.add_subcaption(
            "In practice we can only observe a signal for a "
            "finite duration. This finite observation is equivalent "
            "to multiplying the signal by a window function. The "
            "choice of window has profound consequences.",
            duration=8,
        )
        title = self.ly.title("Windowing and Spectral Leakage")

        self.add_subcaption(
            "A rectangular window of duration T has Fourier transform "
            "equal to a sinc function. By the convolution theorem, "
            "the observed spectrum is the true spectrum convolved "
            "with this sinc. This spreads energy from one frequency "
            "into neighboring bins. That is spectral leakage.",
            duration=10,
        )

        items = [
            Text("Finite observation = multiplication by window",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Frequency domain: convolution with window's FT",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Spectral leakage: energy bleeds into neighboring bins",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

        self.add_subcaption(
            "Better windows reduce spectral leakage at the cost of "
            "wider main lobes. The Hamming and Hann windows taper "
            "the edges smoothly, suppressing side lobes. The "
            "Blackman window offers even stronger suppression. "
            "The trade-off is always between frequency resolution "
            "and leakage suppression.",
            duration=10,
        )

        title2 = self.ly.title("Choosing a Window")
        items2 = [
            Text("Rectangular: sharp main lobe, strong side lobes",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Hamming/Hann: balanced main lobe and side lobes",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Blackman: minimal leakage, wider main lobe",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Practical Filter Design
    # ------------------------------------------------------------------ #
    def scene6_filter_design(self):
        self.add_subcaption(
            "Filtering is the most fundamental signal processing "
            "operation. An ideal low-pass filter multiplies the "
            "spectrum by a rectangle, passing low frequencies and "
            "removing high ones. By the convolution theorem, this "
            "is convolution with a sinc function in the time domain.",
            duration=10,
        )
        title = self.ly.title("Practical Filter Design")

        self.add_subcaption(
            "But the sinc impulse response is infinite and non-causal. "
            "We cannot build an ideal filter. Real filters approximate "
            "it: Butterworth filters have maximally flat passbands, "
            "Chebyshev filters allow ripple for steeper roll-off, and "
            "FIR filters truncate the sinc with a window. Every "
            "practical filter is a compromise.",
            duration=10,
        )

        items = [
            Text("Ideal: brick-wall in frequency = sinc in time (impossible)",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Butterworth: maximally flat passband",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("FIR: truncated sinc with chosen window",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: The Short-Time Fourier Transform
    # ------------------------------------------------------------------ #
    def scene7_stft(self):
        self.ly.section_divider(2, "Time-Frequency Analysis")

        self.add_subcaption(
            "The standard Fourier transform gives the total frequency "
            "content of a signal, but it loses all time information. "
            "A musical note and a chord have the same frequencies, "
            "just arranged differently in time.",
            duration=8,
        )
        title = self.ly.title("The Short-Time Fourier Transform")

        stft = MathTex(
            r"X(t,\omega) = \int x(\tau)\, w(\tau - t)\, "
            r"e^{-i\omega\tau}\, d\tau",
            font_size=BODY_SIZE, color=WHITE,
        )
        stft_box = self.ly.formula_box(stft, color=ACCENT)
        self.play(Write(stft_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "The short-time Fourier transform applies a sliding "
            "window to the signal, computing the Fourier transform "
            "of each windowed segment. The result is a two-dimensional "
            "spectrogram: frequency content as a function of time.",
            duration=8,
        )

        self.play(FadeOut(stft_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Slide a window across the signal",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Compute FT of each windowed segment",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Result: spectrogram (frequency vs. time)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

        self.add_subcaption(
            "The window length sets the resolution trade-off. A narrow "
            "window gives good time resolution but poor frequency "
            "resolution. A wide window gives sharp frequency peaks "
            "but blurs when events occur. This is the uncertainty "
            "principle in action again.",
            duration=9,
        )

        title2 = self.ly.title("The Resolution Trade-off")
        items2 = [
            Text("Narrow window: good time, poor frequency resolution",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Wide window: sharp frequencies, blurred in time",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Cannot have both: Fourier uncertainty principle",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Applications Showcase
    # ------------------------------------------------------------------ #
    def scene8_applications(self):
        self.add_subcaption(
            "Signal processing touches nearly every technology "
            "we use. Let us highlight three major applications "
            "where Fourier analysis is essential.",
            duration=5,
        )
        title = self.ly.title("Applications in the Real World")

        self.add_subcaption(
            "Audio processing uses the FFT for noise removal, "
            "equalization, and compression. The MP3 and AAC "
            "codecs use a modified discrete cosine transform, "
            "a close cousin of the Fourier transform, to "
            "represent audio efficiently.",
            duration=8,
        )
        self.wait(0.5)

        self.add_subcaption(
            "Image processing applies two-dimensional Fourier "
            "transforms for filtering and compression. The JPEG "
            "format uses the discrete cosine transform on image "
            "blocks. Medical imaging relies heavily on frequency "
            "domain techniques.",
            duration=8,
        )
        self.wait(0.5)

        self.add_subcaption(
            "Wireless communications use orthogonal frequency "
            "division multiplexing, which modulates data onto "
            "closely spaced subcarriers using the inverse FFT. "
            "Every 4G, 5G, and WiFi transmission depends on it.",
            duration=8,
        )

        items = [
            Text("Audio: MP3/AAC use DCT (Fourier variant) for compression",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Images: JPEG uses 2D DCT on 8x8 blocks",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Communications: OFDM uses inverse FFT (4G/5G/WiFi)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 9: Summary
    # ------------------------------------------------------------------ #
    def scene9_summary(self):
        self.add_subcaption(
            "Let us review the key ideas from this tour of "
            "signal processing applications.",
            duration=3,
        )
        title = self.ly.title("Key Takeaways")

        self.add_subcaption(
            "First, the Nyquist-Shannon theorem tells us to sample "
            "above twice the bandwidth. Second, aliasing occurs when "
            "we violate this condition. Third, the FFT reduces the "
            "computational cost from O(N squared) to O(N log N). "
            "Fourth, windowing causes spectral leakage. And fifth, "
            "the STFT gives us time-frequency analysis via sliding "
            "windows.",
            duration=16,
        )

        items = [
            Text("1. Sampling theorem: f_s > 2B for perfect reconstruction",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Aliasing: undersampling folds frequencies back",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("3. FFT: O(N log N) made Fourier analysis practical",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("4. Windowing: finite observation causes spectral leakage",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("5. STFT: time-frequency analysis via sliding windows",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)

        self.add_subcaption(
            "In the next video, we apply Fourier analysis to "
            "one of the most important partial differential "
            "equations: the heat equation.",
            duration=5,
        )
        self.ly.clear()

        play_outro(
            self,
            next_video="Applications: Heat Equation",
            next_playlist="Fourier Analysis",
        )
