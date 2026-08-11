"""
Video 179: The Convolution Theorem — Fourier Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video179_ConvolutionTheorem

Topics: Convolution definition with visual (slide-and-multiply),
        Convolution Theorem statement,
        Proof sketch via Fubini swap,
        Properties (commutative, associative, Dirac delta identity),
        Applications (signal filtering, probability/CLT, Green's functions/ODEs),
        Polynomial multiplication as discrete convolution.

Prerequisites: Video 177 (Fourier Transform), Video 178 (FT Properties),
               Video 165 (Hilbert Spaces), Video 176 (Fourier Series Properties).

Competitive insights:
- No graduate-level visual convolution theorem video exists (gap between 3B1B and lectures)
- Our playlist context is a structural advantage no standalone competitor has
- Green's functions + convolution: essentially zero visual competition on YouTube
- Adopt: slide-and-integrate visual (BriTheMathGuy), motivation-first (3B1B),
         proof via Fubini swap, discrete-to-continuous ramp
- Avoid: definition-first approach, too much algebra without visuals,
         ignoring discrete case, standalone treatment without context

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


class Video179_ConvolutionTheorem(Scene):
    """The Convolution Theorem: Turning Complex Integrals into Simple Multiplication"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_convolution_defined()
        self.scene3_theorem_statement()
        self.scene4_proof_sketch()
        self.scene5_properties()
        self.scene6_app_filtering()
        self.scene7_app_probability()
        self.scene8_app_greens_functions()
        self.scene9_polynomial_connection()
        self.scene10_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook -- From Multiplication to Convolution
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: the theorem statement as teaser + motivation"""
        self.add_subcaption(
            "The Fourier Transform has many properties. But one stands above "
            "all others. It turns the complex operation of convolution into "
            "simple multiplication. This is the Convolution Theorem, and it "
            "connects signal processing, probability, and differential equations.",
            duration=15,
        )
        play_intro(self, "The Convolution Theorem", "Fourier Analysis")

        title = self.ly.title("The Most Powerful Property")

        # Teaser formula -- the main theorem
        theorem = MathTex(
            r"\mathcal{F}\{f * g\}(\omega) = \mathcal{F}\{f\}(\omega) \cdot \mathcal{F}\{g\}(\omega)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(theorem)
        self.play(Write(theorem), run_time=NORMAL)
        self.wait(1)

        # Motivating question
        q1 = Text(
            "Convolution: a complex integral combining two functions",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        q2 = Text(
            "Multiplication: the simplest operation possible",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        q3 = Text(
            "The Fourier Transform bridges them!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        items = [q1, q2, q3]
        self.ly.progressive_reveal(items, start_from=theorem)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Convolution Defined -- The Slide and Multiply
    # ------------------------------------------------------------------
    def scene2_convolution_defined(self):
        """Definition: discrete first, then continuous, with slide-and-multiply intuition"""
        self.ly.section_divider(2, "Convolution Defined: Slide and Multiply")

        self.add_subcaption(
            "Convolution combines two functions by flipping one, sliding it "
            "across the other, multiplying at each position, and adding up. "
            "Let's see this first with discrete sequences, then continuous functions.",
            duration=13,
        )

        title = self.ly.title("The Slide-and-Multiply Idea")

        # Discrete definition first
        disc_label = Text("Discrete convolution:",
                          font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        disc_formula = MathTex(
            r"(f * g)[n] = \sum_{k=-\infty}^{\infty} f[k] \cdot g[n - k]",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(disc_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(disc_formula, direction=DOWN, anchor=disc_label, buff=0.15)
        self.play(
            FadeIn(disc_label, shift=LEFT * 0.15),
            Write(disc_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Intuition text
        intuition = Text(
            "Flip one, slide it across, multiply, and sum",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(intuition, direction=DOWN, anchor=disc_formula, buff=0.25)
        self.play(FadeIn(intuition, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        # Transition to continuous
        self.play(
            FadeOut(disc_label), FadeOut(disc_formula),
            FadeOut(intuition),
            run_time=FAST,
        )

        # Continuous definition
        cont_label = Text("Continuous convolution:",
                           font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        cont_formula = MathTex(
            r"(f * g)(t) = \int_{-\infty}^{\infty} f(\tau) \, g(t - \tau) \, d\tau",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(cont_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(cont_formula, direction=DOWN, anchor=cont_label, buff=0.15)
        self.play(
            FadeIn(cont_label, shift=LEFT * 0.15),
            Write(cont_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Key insight about the minus sign
        insight = Text(
            "The minus sign means: FLIP g before sliding",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=cont_formula, buff=0.25)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: The Convolution Theorem -- Statement
    # ------------------------------------------------------------------
    def scene3_theorem_statement(self):
        """Formal statement of the convolution theorem"""
        self.ly.section_divider(3, "The Convolution Theorem")

        self.add_subcaption(
            "The Convolution Theorem states that the Fourier transform of a "
            "convolution equals the product of the Fourier transforms. And "
            "conversely, the Fourier transform of a product equals the "
            "convolution of the Fourier transforms, up to a scaling factor.",
            duration=14,
        )

        title = self.ly.title("The Convolution Theorem")

        # Forward theorem
        fwd_label = Text("Forward:",
                         font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        fwd = MathTex(
            r"\mathcal{F}\{f * g\}(\omega) = \mathcal{F}\{f\}(\omega) \cdot \mathcal{F}\{g\}(\omega)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(fwd_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(fwd, direction=DOWN, anchor=fwd_label, buff=0.15)
        self.play(
            FadeIn(fwd_label, shift=LEFT * 0.15),
            Write(fwd),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Inverse theorem
        inv_label = Text("Inverse:",
                          font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        inv = MathTex(
            r"\mathcal{F}\{f \cdot g\}(\omega) = \frac{1}{2\pi}\,(\mathcal{F}\{f\} * \mathcal{F}\{g\})(\omega)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(inv_label, direction=DOWN, anchor=fwd, buff=0.3)
        self.ly.safe_place(inv, direction=DOWN, anchor=inv_label, buff=0.15)
        self.play(
            FadeIn(inv_label, shift=LEFT * 0.15),
            Write(inv),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Insight
        insight = Text(
            "Convolution in time domain = Multiplication in frequency domain",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=inv, buff=0.3)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Proof Sketch -- The Fubini Swap
    # ------------------------------------------------------------------
    def scene4_proof_sketch(self):
        """Proof of the convolution theorem via Fubini's theorem"""
        self.ly.section_divider(4, "Proof: The Fubini Swap")

        self.add_subcaption(
            "The proof is remarkably elegant. We substitute the definition "
            "of convolution into the Fourier transform, then swap the order "
            "of integration using Fubini's theorem. A change of variables "
            "splits the double integral into two independent Fourier transforms.",
            duration=15,
        )

        title = self.ly.title("Proof: Fubini's Theorem")

        # Step 1: Substitute convolution definition into FT
        step1_label = Text("Start with the Fourier transform of (f*g):",
                            font_size=LABEL_SIZE, color=DIM, font=SANS)
        step1 = MathTex(
            r"\mathcal{F}\{(f*g)\}(\omega) = \int_{-\infty}^{\infty}"
            r"\!\left[\int_{-\infty}^{\infty} f(\tau)\,g(t-\tau)\,d\tau\right]"
            r"e^{-i\omega t}\,dt",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step1_label, direction=DOWN, anchor=title, buff=0.25)
        self.ly.safe_place(step1, direction=DOWN, anchor=step1_label, buff=0.1)
        self.play(
            FadeIn(step1_label, shift=LEFT * 0.15),
            Write(step1),
            run_time=NORMAL,
        )
        self.wait(1)
        self.play(FadeOut(step1_label), FadeOut(step1), run_time=FAST)

        # Step 2: Fubini swap
        step2_label = Text("Swap the integrals (Fubini's theorem):",
                           font_size=LABEL_SIZE, color=DIM, font=SANS)
        step2 = MathTex(
            r"= \int_{-\infty}^{\infty} f(\tau)"
            r"\!\left[\int_{-\infty}^{\infty} g(t-\tau)\,e^{-i\omega t}\,dt\right]"
            r"d\tau",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step2_label, direction=DOWN, anchor=title, buff=0.25)
        self.ly.safe_place(step2, direction=DOWN, anchor=step2_label, buff=0.1)
        self.play(
            FadeIn(step2_label, shift=LEFT * 0.15),
            Write(step2),
            run_time=NORMAL,
        )
        self.wait(1)
        self.play(FadeOut(step2_label), FadeOut(step2), run_time=FAST)

        # Step 3: Change variable
        step3_label = Text("Substitute u = t - tau in the inner integral:",
                           font_size=LABEL_SIZE, color=DIM, font=SANS)
        step3 = MathTex(
            r"= \int_{-\infty}^{\infty} f(\tau)\,e^{-i\omega\tau}"
            r"\!\left[\int_{-\infty}^{\infty} g(u)\,e^{-i\omega u}\,du\right]"
            r"d\tau",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(step3_label, direction=DOWN, anchor=title, buff=0.25)
        self.ly.safe_place(step3, direction=DOWN, anchor=step3_label, buff=0.1)
        self.play(
            FadeIn(step3_label, shift=LEFT * 0.15),
            Write(step3),
            run_time=NORMAL,
        )
        self.wait(1)
        self.play(FadeOut(step3_label), FadeOut(step3), run_time=FAST)

        # Step 4: Recognize
        step4_label = Text("Recognize both integrals:",
                           font_size=LABEL_SIZE, color=DIM, font=SANS)
        step4 = MathTex(
            r"= \underbrace{\mathcal{F}\{f\}(\omega)}_{\text{outer integral}}"
            r"\;\cdot\;"
            r"\underbrace{\mathcal{F}\{g\}(\omega)}_{\text{inner integral}}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(step4_label, direction=DOWN, anchor=title, buff=0.25)
        self.ly.safe_place(step4, direction=DOWN, anchor=step4_label, buff=0.15)
        self.play(
            FadeIn(step4_label, shift=LEFT * 0.15),
            Write(step4),
            run_time=NORMAL,
        )
        self.wait(1)

        # QED insight
        qed = Text(
            "The entire proof is just swapping integrals and a change of variables!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(qed, direction=DOWN, anchor=step4, buff=0.3)
        self.play(FadeIn(qed, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Properties of Convolution -- The Algebra
    # ------------------------------------------------------------------
    def scene5_properties(self):
        """Commutative, associative, identity (Dirac delta)"""
        self.ly.section_divider(5, "Algebraic Properties")

        self.add_subcaption(
            "Convolution has beautiful algebraic structure. It is commutative "
            "and associative, forming an algebra of functions. Its identity "
            "element is the Dirac delta, the natural analog of the number one "
            "for multiplication. The Fourier transform of the delta is one, "
            "confirming the convolution theorem.",
            duration=16,
        )

        title = self.ly.title("Convolution as Algebra")

        # Property 1: Commutativity
        prop1_label = Text("Commutativity:  f * g = g * f",
                           font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        prop1_detail = Text(
            "Proof: substitute u = t - tau, limits flip",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(prop1_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(prop1_detail, direction=DOWN, anchor=prop1_label, buff=0.05)
        self.play(
            FadeIn(prop1_label, shift=LEFT * 0.15),
            FadeIn(prop1_detail, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1)
        self.play(FadeOut(prop1_label), FadeOut(prop1_detail), run_time=FAST)

        # Property 2: Associativity
        prop2_label = Text("Associativity:  (f * g) * h = f * (g * h)",
                           font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        prop2_detail = Text(
            "Proof: triple integral + Fubini reordering",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(prop2_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(prop2_detail, direction=DOWN, anchor=prop2_label, buff=0.05)
        self.play(
            FadeIn(prop2_label, shift=LEFT * 0.15),
            FadeIn(prop2_detail, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1)
        self.play(FadeOut(prop2_label), FadeOut(prop2_detail), run_time=FAST)

        # Property 3: Identity (Dirac delta)
        prop3_label = Text("Identity:  f * delta = f",
                           font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD)
        prop3_formula = MathTex(
            r"\int_{-\infty}^{\infty} f(\tau)\,\delta(t - \tau)\,d\tau = f(t)",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(prop3_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(prop3_formula, direction=DOWN, anchor=prop3_label, buff=0.15)
        self.play(
            FadeIn(prop3_label, shift=LEFT * 0.15),
            Write(prop3_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Verification via convolution theorem
        verify = Text(
            "Verify: F{f * delta} = F{f} . F{delta} = F{f} . 1 = F{f}",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(verify, direction=DOWN, anchor=prop3_formula, buff=0.25)
        self.play(FadeIn(verify, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Application 1 -- Signal Filtering
    # ------------------------------------------------------------------
    def scene6_app_filtering(self):
        """Signal filtering as convolution in time = multiplication in frequency"""
        self.ly.section_divider(6, "Application: Signal Filtering")

        self.add_subcaption(
            "In signal processing, removing noise from a signal means "
            "convolution in the time domain. But the convolution theorem "
            "lets us work in the frequency domain instead, where filtering "
            "becomes simple multiplication by a transfer function.",
            duration=14,
        )

        title = self.ly.title("Filtering: Convolution in Practice")

        # Problem setup
        setup = Text(
            "Signal s(t) + noise n(t) = noisy signal",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(setup, direction=DOWN, anchor=title, buff=0.35)
        self.play(FadeIn(setup, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(setup), run_time=FAST)

        # Time domain approach
        td_label = Text("Time domain: convolve with filter h(t)",
                         font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        td_formula = MathTex(
            r"(s + n) * h = s * h + n * h",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(td_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(td_formula, direction=DOWN, anchor=td_label, buff=0.15)
        self.play(
            FadeIn(td_label, shift=LEFT * 0.15),
            Write(td_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(td_label), FadeOut(td_formula), run_time=FAST)

        # Frequency domain approach
        fd_label = Text("Frequency domain: multiply by H(omega)",
                         font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        fd_formula = MathTex(
            r"\mathcal{F}\{(s{+}n) * h\} = [\mathcal{F}\{s\} + \mathcal{F}\{n\}] \cdot H(\omega)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(fd_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(fd_formula, direction=DOWN, anchor=fd_label, buff=0.15)
        self.play(
            FadeIn(fd_label, shift=LEFT * 0.15),
            Write(fd_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Key insight
        insight = Text(
            "Choose H to keep signal frequencies, kill noise frequencies",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=fd_formula, buff=0.25)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Application 2 -- Probability Distributions
    # ------------------------------------------------------------------
    def scene7_app_probability(self):
        """PDF of sum of independent random variables = convolution of PDFs"""
        self.ly.section_divider(7, "Application: Probability Distributions")

        self.add_subcaption(
            "If X and Y are independent random variables, the probability "
            "density function of their sum Z equals X plus Y is the convolution "
            "of their individual densities. This is why repeated convolution "
            "drives distributions toward a Gaussian, the heart of the Central "
            "Limit Theorem.",
            duration=16,
        )

        title = self.ly.title("Sum of Random Variables = Convolution")

        # Setup
        setup_label = Text("X, Y independent with PDFs f_X, f_Y",
                            font_size=BODY_SIZE, color=WHITE, font=SANS)
        setup_q = Text("What is the PDF of Z = X + Y?",
                        font_size=HEADING_SIZE, color=ACCENT, font=SANS)
        self.ly.safe_place(setup_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(setup_q, direction=DOWN, anchor=setup_label, buff=0.15)
        self.play(
            FadeIn(setup_label, shift=LEFT * 0.15),
            FadeIn(setup_q, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(setup_label), FadeOut(setup_q), run_time=FAST)

        # The theorem
        prob_theorem = MathTex(
            r"f_Z(z) = (f_X * f_Y)(z) = \int_{-\infty}^{\infty} f_X(x)\,f_Y(z - x)\,dx",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(prob_theorem, direction=DOWN, anchor=title, buff=0.35)
        self.play(Write(prob_theorem), run_time=NORMAL)
        self.wait(0.5)

        # Example: uniform + uniform = triangle
        ex_label = Text("Example: uniform + uniform = triangular",
                         font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(ex_label, direction=DOWN, anchor=prob_theorem, buff=0.25)
        self.play(FadeIn(ex_label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)
        self.play(FadeOut(ex_label), run_time=FAST)

        # CLT connection
        clt = Text(
            "Repeated convolution converges to Gaussian = Central Limit Theorem!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(clt, direction=DOWN, anchor=prob_theorem, buff=0.25)
        self.play(FadeIn(clt, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Application 3 -- Green's Functions and ODEs
    # ------------------------------------------------------------------
    def scene8_app_greens_functions(self):
        """Green's function as the DNA of a differential operator"""
        self.ly.section_divider(8, "Application: Green's Functions")

        self.add_subcaption(
            "For a linear differential equation with constant coefficients, "
            "the Green's function is the response to a delta function input. "
            "Once you know the Green's function, the solution for any forcing "
            "term is simply the convolution of the Green's function with the "
            "forcing. This is the DNA of the differential operator.",
            duration=16,
        )

        title = self.ly.title("Green's Functions: The DNA of ODEs")

        # ODE setup
        ode_label = Text("Solve the linear ODE:",
                         font_size=BODY_SIZE, color=WHITE, font=SANS)
        ode_formula = MathTex(
            r"L[y] = f(t)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ode_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ode_formula, direction=DOWN, anchor=ode_label, buff=0.15)
        self.play(
            FadeIn(ode_label, shift=LEFT * 0.15),
            Write(ode_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(ode_label), FadeOut(ode_formula), run_time=FAST)

        # Green's function definition
        gf_label = Text("Green's function G(t) satisfies L[G] = delta(t)",
                         font_size=BODY_SIZE, color=RED, font=SANS)
        self.ly.safe_place(gf_label, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(gf_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(gf_label), run_time=FAST)

        # The key formula
        key_formula = MathTex(
            r"y(t) = (G * f)(t) = \int_{-\infty}^{\infty} G(t - \tau)\,f(\tau)\,d\tau",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(key_formula, direction=DOWN, anchor=title, buff=0.35)
        self.play(Write(key_formula), run_time=NORMAL)
        self.wait(0.5)

        # Why it works
        why = Text(
            "Solve ONE problem (impulse response) to solve ALL problems",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(why, direction=DOWN, anchor=key_formula, buff=0.25)
        self.play(FadeIn(why, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Polynomial Multiplication -- The Discrete Connection
    # ------------------------------------------------------------------
    def scene9_polynomial_connection(self):
        """Polynomial multiplication = coefficient convolution, connection to FFT"""
        self.ly.section_divider(9, "Polynomial Multiplication = Convolution")

        self.add_subcaption(
            "The coefficients of a product of polynomials are the convolution "
            "of the coefficient sequences. This means we can multiply polynomials "
            "in quadratic time using naive methods, or in order n log n time by "
            "using the convolution theorem plus the Fast Fourier Transform.",
            duration=15,
        )

        title = self.ly.title("Polynomials and Convolution")

        # The connection
        coeff_formula = MathTex(
            r"c_k = \sum_{j=0}^{k} a_j \cdot b_{k-j}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        label1 = Text(
            "Product coefficients = discrete convolution of coefficient sequences",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(coeff_formula, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(label1, direction=DOWN, anchor=coeff_formula, buff=0.15)
        self.play(
            Write(coeff_formula),
            FadeIn(label1, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(label1), run_time=FAST)

        # FFT algorithm
        algo_steps = [
            Text("1. Pad coefficient sequences to length 2n",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("2. Compute DFT of both: O(n log n) each",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Multiply frequency coefficients: O(n)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("4. Inverse DFT: O(n log n)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(algo_steps, start_from=coeff_formula)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Summary and Preview
    # ------------------------------------------------------------------
    def scene10_summary(self):
        """Summary of key takeaways and preview of next video"""
        self.add_subcaption(
            "We have seen that convolution is far more than just an integral "
            "formula. It is the operation that the Fourier Transform converts "
            "into multiplication, and this single fact powers signal filtering, "
            "probability theory, differential equations, and even polynomial "
            "multiplication.",
            duration=15,
        )

        title = self.ly.title("Summary")

        takeaways = [
            Text("1. Convolution: flip, slide, multiply, integrate",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Convolution Theorem: F{f*g} = F{f} . F{g}",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("3. Proof: Fubini swap + change of variables",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("4. Algebra: commutative, associative, delta = identity",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("5. Applications: filtering, probability, Green's functions",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title)

        self.wait(1)
        self.ly.clear()

        # Preview
        self.add_subcaption(
            "Next time: the Discrete Fourier Transform, bridging the "
            "continuous theory to the digital algorithms that power modern "
            "signal processing.",
            duration=7,
        )
        play_outro(self, "The Convolution Theorem", "Fourier Analysis")
