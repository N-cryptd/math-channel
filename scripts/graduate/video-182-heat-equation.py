"""
Video 182: Applications — Heat Equation -- Fourier Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video182_HeatEquation

Topics: Heat equation on R, Fourier transform solution method,
        heat kernel (fundamental solution), Gaussian spreading,
        general solution via convolution with heat kernel,
        smoothing and regularization, Fourier method for PDEs.

Prerequisites: Videos 177-180 (Fourier Transform through Parseval).

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


class Video182_HeatEquation(Scene):
    """Applications: Heat Equation -- Fourier Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_heat_equation()
        self.scene3_heat_kernel()
        self.scene4_convolution()
        self.scene5_smoothing()
        self.scene6_pde_method()
        self.scene7_connections()
        self.scene8_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Partial differential equations describe the "
            "physical world, from heat flow to quantum "
            "mechanics. The Fourier transform gives us a "
            "powerful method for solving them. Where "
            "calculus fails, algebra succeeds.",
            duration=7,
        )
        play_intro(self, "Applications: Heat Equation", "Fourier Analysis")

        title = self.ly.title("PDEs Become Algebra")

        self.add_subcaption(
            "The key idea is simple. Take the Fourier transform "
            "of the PDE. Spatial derivatives become multiplication "
            "by i omega. The PDE becomes an ODE, which is much "
            "easier to solve.",
            duration=6,
        )
        items = [
            Text("Fourier transform: PDEs -> ODEs",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("The heat equation is our first example",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Derivatives become algebraic operations!",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: The Heat Equation in Fourier Space
    # ------------------------------------------------------------------ #
    def scene2_heat_equation(self):
        self.add_subcaption(
            "The heat equation on the real line is u sub t "
            "equals alpha u sub x x, where u of x and t is "
            "the temperature at position x and time t, and "
            "alpha is the thermal diffusivity constant.",
            duration=7,
        )
        title = self.ly.title("The Heat Equation")

        heat = MathTex(
            r"\frac{\partial u}{\partial t}",
            r"= \alpha\,\frac{\partial^2 u}{\partial x^2}",
            font_size=BODY_SIZE, color=WHITE,
        )
        heat_box = self.ly.formula_box(heat, color=PRIMARY)
        self.play(Write(heat_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "Transform both sides with respect to x. Using "
            "the derivative property, u sub x x becomes "
            "negative omega squared times u hat. The PDE "
            "becomes an ODE: u hat sub t equals negative "
            "alpha omega squared u hat. This solves to "
            "u hat of omega t equals u hat of omega zero "
            "times e to the negative alpha omega squared t.",
            duration=11,
        )

        self.play(FadeOut(heat_box), run_time=FAST)
        self.wait(0.5)

        ode = MathTex(
            r"\hat{u}_t = -\alpha\omega^2\hat{u}",
            r"\;\Rightarrow\;",
            r"\hat{u}(\omega,t) = \hat{u}(\omega,0)\,e^{-\alpha\omega^2 t}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        ode_box = self.ly.formula_box(ode, color=SECONDARY)
        self.play(Write(ode_box), run_time=SLOW)
        self.wait(3.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: The Heat Kernel
    # ------------------------------------------------------------------ #
    def scene3_heat_kernel(self):
        self.ly.section_divider(1, "The Heat Kernel")

        self.add_subcaption(
            "For the special case of a point-source initial "
            "condition, u of x zero equals the Dirac delta, "
            "the solution is called the heat kernel or "
            "fundamental solution.",
            duration=6,
        )
        title = self.ly.title("Fundamental Solution")

        self.add_subcaption(
            "The transform of delta is one over root two pi. "
            "So u hat equals one over root two pi times e "
            "to the negative alpha omega squared t. The "
            "inverse transform gives a Gaussian: one over "
            "root four pi alpha t times e to the negative "
            "x squared over four alpha t.",
            duration=10,
        )

        kernel = MathTex(
            r"G(x,t)",
            r"= \frac{1}{\sqrt{4\pi\alpha t}}\,",
            r"e^{-x^2/(4\alpha t)}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        kernel_box = self.ly.formula_box(kernel, color=PRIMARY)
        self.play(Write(kernel_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "The heat kernel is a Gaussian that spreads over "
            "time. As t approaches zero, it becomes a sharp "
            "peak at the origin. As t grows, it flattens "
            "and spreads. Heat diffuses as a Gaussian!",
            duration=7,
        )

        self.play(FadeOut(kernel_box), run_time=FAST)
        self.wait(0.5)

        items = [
            Text("Heat kernel = spreading Gaussian",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("As t->0: sharp peak (delta). As t->inf: flat (zero).",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: General Solution via Convolution
    # ------------------------------------------------------------------ #
    def scene4_convolution(self):
        self.add_subcaption(
            "For a general initial condition f of x, the "
            "solution is the convolution of f with the heat "
            "kernel. This is because the heat equation is "
            "linear and translation invariant.",
            duration=7,
        )
        title = self.ly.title("Solution by Convolution")

        sol = MathTex(
            r"u(x,t)",
            r"= (G(\cdot,t) * f)(x)",
            r"= \int_{-\infty}^{\infty} G(x-y,t)\,f(y)\,dy",
            font_size=BODY_SIZE, color=WHITE,
        )
        sol_box = self.ly.formula_box(sol, color=SECONDARY)
        self.play(Write(sol_box), run_time=SLOW)
        self.wait(3.0)

        self.add_subcaption(
            "This is convolution in action. The initial "
            "condition gets smoothed by the heat kernel "
            "at each instant. The convolution theorem from "
            "Video 179 explains why the Fourier method "
            "produces this convolution automatically.",
            duration=7,
        )

        self.play(FadeOut(sol_box), run_time=FAST)
        self.wait(0.5)

        note = Text(
            "G is the Green's function for the heat equation",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.progressive_reveal([note])
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Smoothing and Regularization
    # ------------------------------------------------------------------ #
    def scene5_smoothing(self):
        self.add_subcaption(
            "The heat equation smooths functions. In Fourier "
            "space, each frequency component decays as "
            "e to the negative alpha omega squared t. Higher "
            "frequencies decay exponentially faster.",
            duration=7,
        )
        title = self.ly.title("Smoothing Effect")

        self.add_subcaption(
            "This means discontinuities are instantly smoothed "
            "out. Sharp edges become gentle curves. The "
            "Laplacian acts as a low-pass filter, just as "
            "we saw in signal processing. This is why the "
            "heat equation is used in image denoising.",
            duration=8,
        )
        items = [
            Text("High frequencies decay as e^{-alpha*omega^2*t}",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Discontinuities instantly smoothed",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Laplacian = low-pass filter (image denoising!)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Fourier Method for PDEs
    # ------------------------------------------------------------------ #
    def scene6_pde_method(self):
        self.ly.section_divider(2, "The Fourier Method for PDEs")

        self.add_subcaption(
            "The method we used for the heat equation works "
            "for any linear PDE with constant coefficients. "
            "Transform, solve the ODE, and inverse transform.",
            duration=6,
        )
        title = self.ly.title("General Fourier PDE Method")

        items = [
            Text("Step 1: Fourier transform the PDE in space",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Step 2: Solve resulting ODE for u-hat(omega, t)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Step 3: Inverse transform to get u(x, t)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "This works for the heat equation, wave equation, "
            "Laplace equation, and the Schrodinger equation. "
            "The limitation is that it requires constant "
            "coefficients and either the real line or a "
            "periodic domain.",
            duration=7,
        )
        note = Text(
            "Works for heat, wave, Laplace, Schrodinger equations",
            font_size=BODY_SIZE, color=WHITE, font=SANS)
        self.ly.progressive_reveal([note])
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Connections to Previous Topics
    # ------------------------------------------------------------------ #
    def scene7_connections(self):
        self.add_subcaption(
            "The heat equation brings together every concept "
            "from this Fourier Analysis playlist. The heat "
            "kernel is a Gaussian, connecting to our "
            "eigenfunction discussion. The solution is "
            "convolution, connecting to the convolution "
            "theorem. The smoothing connects to "
            "differentiation as a filter.",
            duration=9,
        )
        title = self.ly.title("Everything Connects")

        items = [
            Text("Heat kernel = Gaussian (Video 177: eigenfunction)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Solution = convolution (Video 179: convolution theorem)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Smoothing = integration/low-pass (Video 176)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Energy decay = Parseval (Video 180)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Preview
    # ------------------------------------------------------------------ #
    def scene8_summary(self):
        self.add_subcaption(
            "Let us review the key ideas about the heat "
            "equation and the Fourier method.",
            duration=3,
        )
        title = self.ly.title("Key Takeaways")

        self.add_subcaption(
            "First, the Fourier transform converts the heat "
            "equation PDE into a simple ODE. Second, the "
            "heat kernel is a Gaussian that spreads over "
            "time. Third, the general solution is convolution "
            "with the heat kernel. Fourth, the equation "
            "smooths by exponentially decaying high "
            "frequencies. And fifth, the Fourier method "
            "works for many linear PDEs.",
            duration=14,
        )

        items = [
            Text("1. PDE -> ODE: u-hat_t = -alpha*omega^2*u-hat",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Heat kernel: Gaussian spreading over time",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. General solution: convolution with heat kernel",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Smoothing: high freq decay exponentially",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5. General method: transform, solve ODE, invert",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)

        self.add_subcaption(
            "In the final video of this playlist, we will "
            "summarize all of Fourier analysis and look ahead "
            "to future topics.",
            duration=5,
        )
        self.ly.clear()

        play_outro(
            self,
            next_video="Fourier Analysis Summary",
            next_playlist="Fourier Analysis",
        )
