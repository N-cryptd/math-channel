"""
Video 178: Properties of the Fourier Transform -- Fourier Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video178_PropertiesFourierTransform

Topics: Linearity and scaling, derivative property (multiply by i*omega),
        convolution theorem, duality, Parseval/Plancherel theorem,
        moments and the smoothness-decay connection.

Prerequisites: Video 177 (The Fourier Transform),
               Videos 174-176 (Fourier Series),
               Video 165 (Hilbert Spaces).

Competitive insights:
- MIT OCW 94K views: all properties in whiteboard lecture, no animations
- Steve Brunton 71K views: derivative property with PDE motivation
- Neso Academy 269K views: duality as isolated algebraic trick, slides-only
- Mark Newman 73K views: best visual convolution, but no theorem proof
- Nobody unifies all properties with animation + functional analysis lens
- Our angle: properties as consequences of FT being unitary on L2

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


class Video178_PropertiesFourierTransform(Scene):
    """Properties of the Fourier Transform -- Fourier Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_linearity_scaling()
        self.scene3_derivative_property()
        self.scene4_convolution_theorem()
        self.scene5_duality()
        self.scene6_parseval_plancherel()
        self.scene7_smoothness_decay()
        self.scene8_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook -- The Power of Properties
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "In the last video, we defined the Fourier transform "
            "as the natural limit of Fourier series. We derived "
            "the forward and inverse transforms and computed "
            "the Gaussian and sinc examples.",
            duration=8,
        )
        play_intro(self, "Properties of the Fourier Transform",
                   "Fourier Analysis")

        title = self.ly.title("The Power of Properties")

        self.add_subcaption(
            "But knowing the definition is not enough. The "
            "true power of the Fourier transform lies in its "
            "properties. These properties reveal what the "
            "transform does, not just what it is.",
            duration=7,
        )

        items = [
            Text("Convolution theorem: convolution <-> multiplication",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Derivative property: differentiation <-> multiply by i*omega",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Duality: the FT is almost its own inverse",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Parseval/Plancherel: energy is preserved",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Smoothness <-> Decay: the deepest insight",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "Today we will see that every property reflects a "
            "fundamental truth. Smoothness in one domain means "
            "decay in the other. Let us begin.",
            duration=6,
        )
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Linearity and Scaling
    # ------------------------------------------------------------------ #
    def scene2_linearity_scaling(self):
        self.add_subcaption(
            "The simplest properties follow directly from the "
            "linearity of the integral. The Fourier transform is "
            "a linear operator.",
            duration=6,
        )
        self.ly.section_divider(1, "Linearity, Scaling, and Shifts")
        title = self.ly.title("Linearity, Scaling, and Shifts")

        # Linearity
        self.add_subcaption(
            "Linearity: the transform of a linear combination "
            "is the linear combination of the transforms. "
            "This follows from the linearity of the integral.",
            duration=7,
        )
        linearity = MathTex(
            r"\mathcal{F}\{af + bg\}",
            r"= a\,\hat{f}(\omega) + b\,\hat{g}(\omega)",
            font_size=BODY_SIZE, color=WHITE,
        )
        linearity[0].set_color(PRIMARY)
        linearity_box = self.ly.formula_box(linearity)
        self.play(Write(linearity_box), run_time=SLOW)
        self.wait(3.0)

        # Scaling
        self.add_subcaption(
            "Time scaling: compressing a function in time "
            "stretches its frequency spectrum. If we replace "
            "t with a times t, the frequencies get divided by a.",
            duration=8,
        )
        self.play(FadeOut(linearity_box), run_time=FAST)
        self.wait(0.5)

        scaling = MathTex(
            r"\mathcal{F}\{f(at)\}",
            r"= \frac{1}{|a|}\,\hat{f}\!\left(\frac{\omega}{a}\right)",
            font_size=BODY_SIZE, color=WHITE,
        )
        scaling[0].set_color(PRIMARY)
        scaling[1].set_color(ACCENT)
        scaling_box = self.ly.formula_box(scaling)
        self.play(Write(scaling_box), run_time=SLOW)
        self.wait(3.0)

        # Time shift
        self.add_subcaption(
            "Time shifting: shifting a function in time "
            "multiplies its spectrum by a complex exponential. "
            "This is a phase rotation in the frequency domain.",
            duration=7,
        )
        self.play(FadeOut(scaling_box), run_time=FAST)
        self.wait(0.5)

        shift = MathTex(
            r"\mathcal{F}\{f(t - t_0)\}",
            r"= e^{-i\omega t_0}\,\hat{f}(\omega)",
            font_size=BODY_SIZE, color=WHITE,
        )
        shift[0].set_color(PRIMARY)
        shift[1].set_color(ACCENT)
        shift_box = self.ly.formula_box(shift)
        self.play(Write(shift_box), run_time=SLOW)
        self.wait(3.0)

        # Frequency shift
        self.add_subcaption(
            "Frequency shift, also called modulation: multiplying "
            "by a complex exponential in time shifts the spectrum. "
            "This is the dual of the time shift property.",
            duration=7,
        )
        self.play(FadeOut(shift_box), run_time=FAST)
        self.wait(0.5)

        mod = MathTex(
            r"\mathcal{F}\{f(t)\,e^{i\omega_0 t}\}",
            r"= \hat{f}(\omega - \omega_0)",
            font_size=BODY_SIZE, color=WHITE,
        )
        mod[0].set_color(PRIMARY)
        mod[1].set_color(ACCENT)
        mod_box = self.ly.formula_box(mod)
        self.play(Write(mod_box), run_time=SLOW)
        self.wait(4.0)

        note = Text(
            "These mirror the Fourier series properties from Video 176",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, DOWN, mod_box, buff=0.5)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: The Derivative Property
    # ------------------------------------------------------------------ #
    def scene3_derivative_property(self):
        self.add_subcaption(
            "The most powerful property of the Fourier transform "
            "is what it does to derivatives. Differentiation "
            "becomes simple multiplication.",
            duration=6,
        )
        self.ly.section_divider(2, "The Derivative Property")
        title = self.ly.title("The Derivative Property")

        self.add_subcaption(
            "The Fourier transform of the derivative of f "
            "is i omega times the Fourier transform of f. "
            "The proof uses integration by parts.",
            duration=7,
        )

        deriv = MathTex(
            r"\mathcal{F}\{f'(t)\}",
            r"= i\omega\,\hat{f}(\omega)",
            font_size=BODY_SIZE, color=WHITE,
        )
        deriv[0].set_color(PRIMARY)
        deriv[1].set_color(ACCENT)
        deriv_box = self.ly.formula_box(deriv, color=ACCENT)
        self.play(Write(deriv_box), run_time=SLOW)
        self.wait(3.0)

        # Proof sketch
        self.add_subcaption(
            "Proof sketch. Integrate by parts in the Fourier "
            "transform definition. The boundary terms vanish "
            "for functions that decay at infinity.",
            duration=7,
        )
        self.play(FadeOut(deriv_box), run_time=FAST)
        self.wait(0.5)

        proof = MathTex(
            r"\int f'(t)\,e^{-i\omega t}\,dt",
            r"= \bigl[f(t)\,e^{-i\omega t}\bigr]_{-\infty}^{\infty}",
            r"+ i\omega\!\int f(t)\,e^{-i\omega t}\,dt",
            font_size=BODY_SIZE, color=WHITE,
        )
        proof[0].set_color(PRIMARY)
        proof[2].set_color(ACCENT)
        proof_box = self.ly.formula_box(proof)
        self.play(Write(proof_box), run_time=SLOW)
        self.wait(4.0)

        # Higher derivatives
        self.add_subcaption(
            "Applying this repeatedly, the n-th derivative "
            "transforms to i omega to the n, times the "
            "Fourier transform of f.",
            duration=6,
        )
        self.play(FadeOut(proof_box), run_time=FAST)
        self.wait(0.5)

        higher = MathTex(
            r"\mathcal{F}\{f^{(n)}(t)\}",
            r"= (i\omega)^n\,\hat{f}(\omega)",
            font_size=BODY_SIZE, color=WHITE,
        )
        higher[0].set_color(PRIMARY)
        higher[1].set_color(SECONDARY)
        higher_box = self.ly.formula_box(higher)
        self.play(Write(higher_box), run_time=SLOW)
        self.wait(3.0)

        # ODE application
        self.add_subcaption(
            "This property converts differential equations "
            "into algebraic equations. Consider f prime plus "
            "three f equals g. In the frequency domain, this "
            "becomes i omega plus three, times F, equals G.",
            duration=9,
        )
        self.play(FadeOut(higher_box), run_time=FAST)
        self.wait(0.5)

        ode = MathTex(
            r"f'(t) + 3f(t) = g(t)",
            r"\;\;\longrightarrow\;\;",
            r"(i\omega + 3)\hat{f}(\omega) = \hat{g}(\omega)",
            font_size=BODY_SIZE, color=WHITE,
        )
        ode[0].set_color(PRIMARY)
        ode[2].set_color(ACCENT)
        ode_box = self.ly.formula_box(ode)
        self.play(Write(ode_box), run_time=SLOW)
        self.wait(4.0)

        key = Text(
            "Differentiation becomes multiplication -- ODEs become algebra",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(key, DOWN, ode_box, buff=0.5)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: The Convolution Theorem
    # ------------------------------------------------------------------ #
    def scene4_convolution_theorem(self):
        self.add_subcaption(
            "The convolution theorem is perhaps the most "
            "consequence of the Fourier transform. It converts "
            "the hardest operation, convolution, into the "
            "easiest, multiplication.",
            duration=8,
        )
        self.ly.section_divider(3, "The Convolution Theorem")
        title = self.ly.title("The Convolution Theorem")

        # Convolution definition
        self.add_subcaption(
            "First, the definition. The convolution of f and g "
            "is the integral of f of tau times g of t minus tau, "
            "integrated over tau. Think of it as sliding one "
            "function over the other and measuring overlap.",
            duration=9,
        )

        conv_def = MathTex(
            r"(f * g)(t)",
            r"= \int_{-\infty}^{\infty} f(\tau)\,g(t - \tau)\,d\tau",
            font_size=BODY_SIZE, color=WHITE,
        )
        conv_def[0].set_color(PRIMARY)
        conv_def_box = self.ly.formula_box(conv_def)
        self.play(Write(conv_def_box), run_time=SLOW)
        self.wait(4.0)

        # The theorem
        self.add_subcaption(
            "The convolution theorem states that the Fourier "
            "transform of a convolution is the product of the "
            "individual transforms. Convolution in time becomes "
            "pointwise multiplication in frequency.",
            duration=9,
        )
        self.play(FadeOut(conv_def_box), run_time=FAST)
        self.wait(0.5)

        theorem = MathTex(
            r"\mathcal{F}\{f * g\}",
            r"= \hat{f}(\omega)\,\hat{g}(\omega)",
            font_size=BODY_SIZE, color=WHITE,
        )
        theorem[0].set_color(PRIMARY)
        theorem[1].set_color(ACCENT)
        theorem_box = self.ly.formula_box(theorem, color=ACCENT)
        self.play(Write(theorem_box), run_time=SLOW)
        self.wait(3.0)

        # Dual theorem
        self.add_subcaption(
            "The dual statement: multiplication in the time "
            "domain corresponds to convolution in the frequency "
            "domain. This symmetry is a consequence of duality, "
            "which we will see shortly.",
            duration=8,
        )

        dual = MathTex(
            r"\mathcal{F}\{f \cdot g\}",
            r"= \frac{1}{2\pi}\,(\hat{f} * \hat{g})(\omega)",
            font_size=BODY_SIZE, color=WHITE,
        )
        dual[0].set_color(PRIMARY)
        dual[1].set_color(SECONDARY)
        self.ly.safe_place(dual, DOWN, theorem_box, buff=0.5)
        self.play(Write(dual), run_time=SLOW)
        self.wait(4.0)

        # Key insight
        self.add_subcaption(
            "Why does this matter? Because convolution is "
            "computationally expensive, taking order n squared "
            "operations. But multiplication is order n. The "
            "convolution theorem is the foundation of the "
            "Fast Fourier Transform algorithm.",
            duration=9,
        )

        self.play(FadeOut(theorem_box), FadeOut(dual), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Convolution in time <-> multiplication in frequency",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Multiplication in time <-> convolution in frequency",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Foundation of the FFT algorithm (O(n^2) -> O(n log n))",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Duality
    # ------------------------------------------------------------------ #
    def scene5_duality(self):
        self.add_subcaption(
            "One of the most beautiful properties of the Fourier "
            "transform is duality. The transform is almost its "
            "own inverse.",
            duration=6,
        )
        self.ly.section_divider(4, "Duality")
        title = self.ly.title("Duality: The FT is Its Own (Almost) Inverse")

        self.add_subcaption(
            "The duality property says: if the Fourier "
            "transform of f is capital F, then the Fourier "
            "transform of capital F is two pi times f "
            "evaluated at minus omega.",
            duration=8,
        )

        duality = MathTex(
            r"\hat{f}(\omega) = F(\omega)",
            r"\;\;\Longrightarrow\;\;",
            r"\hat{F}(t) = 2\pi\,f(-t)",
            font_size=BODY_SIZE, color=WHITE,
        )
        duality[0].set_color(PRIMARY)
        duality[2].set_color(ACCENT)
        duality_box = self.ly.formula_box(duality, color=ACCENT)
        self.play(Write(duality_box), run_time=SLOW)
        self.wait(4.0)

        # Proof sketch
        self.add_subcaption(
            "The proof comes from comparing the forward and "
            "inverse Fourier transform formulas. The inverse "
            "transform has a plus sign in the exponential "
            "and a factor of one over two pi. Swapping the "
            "roles of t and omega gives us the duality result.",
            duration=10,
        )
        self.play(FadeOut(duality_box), run_time=FAST)
        self.wait(0.5)

        # Show forward and inverse side by side
        forward = MathTex(
            r"\hat{f}(\omega) = \int f(t)\,e^{-i\omega t}\,dt",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        inverse = MathTex(
            r"f(t) = \frac{1}{2\pi}\!\int \hat{f}(\omega)\,e^{i\omega t}\,d\omega",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        forward_group, inverse_group = self.ly.two_columns(
            [Text("Forward:", font_size=LABEL_SIZE, color=DIM, font=SANS), forward],
            [Text("Inverse:", font_size=LABEL_SIZE, color=DIM, font=SANS), inverse],
            start_from=title,
        )
        self.play(
            FadeIn(forward_group, shift=LEFT * 0.15),
            FadeIn(inverse_group, shift=RIGHT * 0.15),
            run_time=NORMAL,
        )
        self.wait(4.0)

        self.add_subcaption(
            "Notice how similar they are. The only differences "
            "are the sign in the exponential and the factor "
            "of one over two pi. This symmetry between time "
            "and frequency is fundamental.",
            duration=8,
        )
        self.wait(3.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Parseval's Theorem and Plancherel
    # ------------------------------------------------------------------ #
    def scene6_parseval_plancherel(self):
        self.add_subcaption(
            "Parseval's theorem gives us a profound result. "
            "The total energy of a signal, measured in the "
            "time domain, equals its total energy in the "
            "frequency domain.",
            duration=8,
        )
        self.ly.section_divider(5, "Parseval's Theorem")
        title = self.ly.title("Parseval's Theorem and Plancherel")

        self.add_subcaption(
            "Parseval's theorem for the Fourier transform "
            "states: the integral of the absolute value of f "
            "squared equals one over two pi times the integral "
            "of the absolute value of f hat squared.",
            duration=8,
        )

        parseval = MathTex(
            r"\int_{-\infty}^{\infty} |f(t)|^2\,dt",
            r"= \frac{1}{2\pi}\!\int_{-\infty}^{\infty}"
            r"|\hat{f}(\omega)|^2\,d\omega",
            font_size=BODY_SIZE, color=WHITE,
        )
        parseval[0].set_color(PRIMARY)
        parseval[1].set_color(ACCENT)
        parseval_box = self.ly.formula_box(parseval, color=ACCENT)
        self.play(Write(parseval_box), run_time=SLOW)
        self.wait(4.0)

        # Energy interpretation
        self.add_subcaption(
            "In signal processing, the integral of the "
            "absolute value squared is called the energy "
            "of the signal. Parseval says the energy in the "
            "time domain equals the energy in the frequency "
            "domain. Energy is preserved by the Fourier "
            "transform.",
            duration=9,
        )

        self.play(FadeOut(parseval_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Energy in time domain = Energy in frequency domain",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("The Fourier transform preserves the L2 norm",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("This means F is a UNITARY operator on L2(R)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)

        # Connection to Hilbert spaces
        self.add_subcaption(
            "Connecting to Video 165 on Hilbert spaces: a unitary "
            "operator preserves inner products and norms. The "
            "Fourier transform is unitary on L two. This means "
            "the Fourier transform is essentially a rotation "
            "of the function space.",
            duration=9,
        )
        self.wait(2.0)

        self.play(FadeOut(items[0]), FadeOut(items[1]), FadeOut(items[2]),
                  run_time=FAST)
        self.wait(0.5)

        # Plancherel
        plancherel = Text(
            "Plancherel: The FT extends to an isometry on L2(R) -- "
            "even for functions not in L1",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(plancherel, DOWN, title, buff=0.5)
        self.play(FadeIn(plancherel, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Moments and Smoothness -- The Unifying Theme
    # ------------------------------------------------------------------ #
    def scene7_smoothness_decay(self):
        self.add_subcaption(
            "We now come to the deepest insight that connects "
            "all these properties together. There is a "
            "fundamental relationship between the smoothness "
            "of a function and the decay of its Fourier "
            "transform.",
            duration=9,
        )
        self.ly.section_divider(6, "Smoothness and Decay")
        title = self.ly.title("Smoothness <-> Decay: The Unifying Theme")

        # Moments
        self.add_subcaption(
            "First, moments. The n-th moment of f, defined as "
            "the integral of t to the n times f, equals i to "
            "the n times the n-th derivative of f hat at zero. "
            "Moments in time connect to derivatives in "
            "frequency.",
            duration=10,
        )

        moments = MathTex(
            r"\int t^n f(t)\,dt",
            r"= (i)^n\,\hat{f}^{(n)}(0)",
            font_size=BODY_SIZE, color=WHITE,
        )
        moments[0].set_color(PRIMARY)
        moments[1].set_color(ACCENT)
        moments_box = self.ly.formula_box(moments)
        self.play(Write(moments_box), run_time=SLOW)
        self.wait(4.0)

        # The deep insight
        self.add_subcaption(
            "Now the key principle. If a function is n times "
            "differentiable, then its Fourier transform decays "
            "like one over omega to the n. Smoother functions "
            "have faster decaying transforms.",
            duration=8,
        )
        self.play(FadeOut(moments_box), run_time=FAST)
        self.wait(0.5)

        principle = MathTex(
            r"f \in C^n",
            r"\;\;\Longleftrightarrow\;\;",
            r"\hat{f}(\omega) = O\!\left(\frac{1}{|\omega|^n}\right)",
            font_size=BODY_SIZE, color=WHITE,
        )
        principle[0].set_color(PRIMARY)
        principle[2].set_color(ACCENT)
        principle_box = self.ly.formula_box(principle, color=ACCENT)
        self.play(Write(principle_box), run_time=SLOW)
        self.wait(4.0)

        # Examples table
        self.add_subcaption(
            "Let us see this with examples. The Gaussian is "
            "infinitely smooth and its transform decays faster "
            "than any polynomial. The rectangle function has "
            "a jump, so its sinc transform decays slowly, "
            "like one over omega.",
            duration=9,
        )
        self.play(FadeOut(principle_box), run_time=FAST)
        self.wait(0.5)

        # Two-column examples
        left_items = [
            Text("Gaussian:", font_size=LABEL_SIZE, color=PRIMARY, font=SANS),
            Text("Infinitely smooth", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("FT decays super-fast", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        right_items = [
            Text("Rectangle:", font_size=LABEL_SIZE, color=RED, font=SANS),
            Text("Jump discontinuity", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Sinc decays as 1/|w|", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        left_group, right_group = self.ly.two_columns(
            left_items, right_items, start_from=title,
        )
        self.play(
            FadeIn(left_group, shift=LEFT * 0.15),
            FadeIn(right_group, shift=RIGHT * 0.15),
            run_time=NORMAL,
        )
        self.wait(4.0)
        self.ly.clear()

        # Unifying summary
        title2 = self.ly.title("This Explains Everything")
        self.add_subcaption(
            "The derivative property, the convolution theorem, "
            "and Parseval's theorem are all manifestations of "
            "the same truth. Smoothness in one domain means "
            "decay in the other. Differentiation amplifies "
            "high frequencies. Convolution smooths. Energy "
            "measures total spectral content.",
            duration=10,
        )
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Looking Ahead
    # ------------------------------------------------------------------ #
    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap the key properties of the Fourier "
            "transform that we have covered in this video.",
            duration=5,
        )
        title = self.ly.title("Summary: Key Properties")

        items = [
            Text("Linearity, scaling, and shifts",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Derivative: F{f'} = (iw)*F  -- ODEs become algebra",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Convolution: F{f*g} = F*G  -- hard op becomes easy",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Duality: F{F(t)} = 2*pi*f(-t)  -- near self-inverse",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Parseval: ||f||_2 = ||F||_2  -- unitary on L2",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)

        self.add_subcaption(
            "The unifying theme: smoothness in one domain means "
            "decay in the other. Every property reflects this "
            "deep relationship between a function and its "
            "frequency content.",
            duration=8,
        )
        self.wait(2.0)

        self.ly.clear()

        self.add_subcaption(
            "In the next video, we will take a deep dive into "
            "the convolution theorem and explore its "
            "applications in signal processing and partial "
            "differential equations.",
            duration=6,
        )
        play_outro(self, "The Convolution Theorem (Deep Dive)",
                   "Fourier Analysis")
