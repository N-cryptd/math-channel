"""
Video 190: Green's Functions -- Partial Differential Equations Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video190_GreensFunctions

Topics: Green's function as impulse response,
        Formal definition with Dirac delta,
        Heat kernel as the Green's function for diffusion,
        Convolution representation of general solutions,
        Method of images for boundary conditions,
        Connection to Fourier analysis.

Prerequisites: Video 189 (Sturm-Liouville Theory), Video 185 (Heat Equation),
               Videos 174-179 (Fourier Analysis), Video 170 (Inner Product Spaces).

Competitive insights:
- Mathemaniac (755K views): excellent impulse response motivation via 3B1B-style
  visuals, but only covers ODEs, no PDE-specific content, no method of images
- Faculty of Khan (156K views): rigorous PDE Green's functions, whiteboard-only
- Andrew Dotson (96K views): physics-focused electrostatics intuition, whiteboard
- Prof. Dave (19K views): heat kernel connection, surface-level, no animations
- NO competitor animates PDE Green's functions with all five aspects covered

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


class Video190_GreensFunctions(Scene):
    """Green's Functions -- the golden key to solving PDEs for any source."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_formal_definition()
        self.scene3_heat_kernel()
        self.scene4_convolution()
        self.scene5_method_of_images()
        self.scene6_fourier_connection()
        self.scene7_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook -- The Impulse Response
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Separation of variables solves PDEs on nice domains "
            "with nice boundary conditions. But what if the source "
            "term is complicated, or the geometry is irregular? "
            "Green's functions give you a universal solution "
            "method. The key idea: solve the PDE for a single "
            "point source, then build up the full solution by "
            "superposition. This is the impulse response "
            "approach, and it works for almost any PDE.",
            duration=15,
        )
        play_intro(self, "Green's Functions", "Partial Differential Equations")

        title = self.ly.title("The Impulse Response of a PDE")

        items = [
            Text("Solve the PDE for a single point source", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("The solution = Green's function G(x, xi)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Full solution = convolution with G", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Works for heat, wave, Laplace, and more", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Formal Definition
    # ------------------------------------------------------------------ #
    def scene2_formal_definition(self):
        self.ly.section_divider("1", "Formal Definition")
        self.add_subcaption(
            "For a linear differential operator L, the Green's "
            "function G satisfies L of G equals the Dirac delta "
            "function. The Dirac delta is infinite at the source "
            "point, zero everywhere else, and integrates to one. "
            "Think of it as the idealized point source. The "
            "Green's function tells you: how does the system "
            "respond to a unit kick at a specific location?",
            duration=14,
        )
        title = self.ly.title("Formal Definition")

        # The defining equation
        def_eq = MathTex(
            r"L[G(x, \xi)] = \delta(x - \xi)",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.formula_box(def_eq)
        self.play(Write(def_eq), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(def_eq), run_time=0.3)

        items = [
            MathTex(r"\delta(x - \xi)", r"\text{: infinite at } \xi", r"\text{, zero elsewhere}", font_size=HEADING_SIZE, color=WHITE),
            MathTex(r"\int \delta(x - \xi) \, dx = 1", font_size=HEADING_SIZE, color=PRIMARY),
            Text("G encodes the response to a unit impulse", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Symmetry: G(x, xi) = G(xi, x) for self-adjoint L", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: The Heat Kernel
    # ------------------------------------------------------------------ #
    def scene3_heat_kernel(self):
        self.ly.section_divider("2", "The Heat Kernel")
        self.add_subcaption(
            "For the heat equation, the Green's function is the "
            "heat kernel, a Gaussian that starts as a point and "
            "spreads over time. At time equals zero, it is the "
            "Dirac delta, a perfect point source. As time "
            "increases, the Gaussian broadens and flattens. This "
            "is exactly what diffusion looks like: heat "
            "spreading out from a single hot point. The heat "
            "kernel is also called the fundamental solution.",
            duration=15,
        )
        title = self.ly.title("The Heat Kernel: Gaussian Spreading")

        # The heat kernel formula
        kernel = MathTex(
            r"G(x, t) = \frac{1}{\sqrt{4 \pi \alpha t}} \, "
            r"e^{-x^2 / (4 \alpha t)}",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.formula_box(kernel)
        self.play(Write(kernel), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(kernel), run_time=0.3)

        items = [
            Text("At t = 0: delta function (point source)", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("As t grows: Gaussian broadens and flattens", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Visual: heat spreading from a single hot point", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Also called: fundamental solution, diffusion kernel", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Convolution Representation
    # ------------------------------------------------------------------ #
    def scene4_convolution(self):
        self.ly.section_divider("3", "Convolution Representation")
        self.add_subcaption(
            "Once you have the Green's function, the general "
            "solution is a convolution. You integrate the Green's "
            "function against the source term. Physically, this "
            "means you sum up the contributions from every source "
            "point. For the heat equation, this becomes: the "
            "temperature at any point and time is the integral of "
            "the heat kernel times the initial temperature "
            "distribution. This is why the heat kernel is so "
            "powerful.",
            duration=16,
        )
        title = self.ly.title("The Solution: Convolution")

        # The convolution formula
        conv_eq = MathTex(
            r"u(x, t) = \int_{-\infty}^{\infty} "
            r"G(x - \xi, t) \, f(\xi) \, d\xi",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.formula_box(conv_eq)
        self.play(Write(conv_eq), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(conv_eq), run_time=0.3)

        items = [
            Text("G(x-xi, t): how heat from point xi reaches x", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("f(xi): the initial temperature at point xi", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Integrate: sum contributions from all source points", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Works for ANY initial condition f(x)", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Method of Images
    # ------------------------------------------------------------------ #
    def scene5_method_of_images(self):
        self.ly.section_divider("4", "Method of Images")
        self.add_subcaption(
            "The free-space Green's function ignores boundaries. "
            "But real problems have boundary conditions. The "
            "method of images is a clever trick: place a mirror "
            "image source to enforce the boundary condition. For "
            "the half-line with Dirichlet conditions, subtract "
            "a reflected Green's function. The positive source "
            "and the negative mirror source cancel at the "
            "boundary, giving you exactly zero. This trick works "
            "for heat, wave, and Laplace equations.",
            duration=16,
        )
        title = self.ly.title("Method of Images: Mirror Sources")

        # The Dirichlet Green's function
        img_eq = MathTex(
            r"G_D(x, \xi) = G_{\text{free}}(x, \xi) "
            r"- G_{\text{free}}(x, -\xi)",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.formula_box(img_eq)
        self.play(Write(img_eq), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(img_eq), run_time=0.3)

        items = [
            Text("Free-space G ignores boundaries", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Mirror source: place source at -xi with opposite sign", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Positive + negative cancel at the boundary", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Works for heat, wave, and Laplace equations", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Connection to Fourier Analysis
    # ------------------------------------------------------------------ #
    def scene6_fourier_connection(self):
        self.ly.section_divider("5", "Fourier Transform")
        self.add_subcaption(
            "Fourier analysis gives us the easiest way to find "
            "Green's functions. Take the PDE, apply the Fourier "
            "transform, and solve algebraically. The Green's "
            "function in Fourier space is just one over the "
            "symbol of the operator. Then transform back. This "
            "connects directly to the convolution theorem: "
            "convolution in physical space equals multiplication "
            "in frequency space. The Green's function is the "
            "multiplicative inverse of the operator.",
            duration=16,
        )
        title = self.ly.title("Fourier Transform: The Easy Path")

        # Fourier space Green's function
        ft_eq = MathTex(
            r"\hat{G}(k) = \frac{1}{\hat{L}(k)}",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.formula_box(ft_eq)
        self.play(Write(ft_eq), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(ft_eq), run_time=0.3)

        items = [
            Text("Apply Fourier transform to L[u] = f", font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"\hat{L}(k) \, \hat{u}(k) = \hat{f}(k)", font_size=HEADING_SIZE, color=PRIMARY),
            Text("G-hat = 1 over L-hat: invert in frequency space", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Inverse Fourier transform gives G(x)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene7_summary(self):
        self.add_subcaption(
            "Green's functions are the universal tool for solving "
            "linear PDEs. The Green's function is the impulse "
            "response: it satisfies L of G equals delta. The "
            "general solution is a convolution with G. For the "
            "heat equation, the heat kernel is a spreading "
            "Gaussian. The method of images handles boundaries "
            "with mirror sources. And the Fourier transform "
            "gives the easiest way to compute Green's functions "
            "in frequency space. Next, we study well-posed "
            "problems.",
            duration=17,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("Green's function = impulse response of the PDE", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Solution = convolution with G", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Heat kernel = Gaussian spreading from a point", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Method of images: mirror sources for boundaries", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Fourier: G-hat = 1 / L-hat in frequency space", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        play_outro(self, "Well-Posed Problems", "Partial Differential Equations")
