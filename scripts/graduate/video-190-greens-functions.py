"""
Video 190: Green's Functions -- Partial Differential Equations Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video190_GreensFunctions

Topics: Green's function as impulse response,
        The heat kernel as a Green's function,
        Method of images for simple geometries,
        Convolution representation of PDE solutions,
        Physical intuition: response to a point source.

Prerequisites: Videos 184-189 (PDE intro through Sturm-Liouville),
               Fourier Analysis (177-179), Convolution (179).

Quality Rules (mandatory):
1. Max 5 visible elements per scene at any time
2. Use LayoutEngine for ALL positioning
3. Progressive disclosure
4. Narration timing ~12 words / 5s
5. Call ly.clear() between scenes
6. MathTex: raw strings with single backslashes
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
    """Green's Functions -- PDE Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_impulse_response()
        self.scene3_heat_kernel()
        self.scene4_convolution()
        self.scene5_method_of_images()
        self.scene6_properties()
        self.scene7_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "If you know how a system responds to a single impulse, "
            "you can predict its response to any input. This is the "
            "power of Green's functions. They are the building blocks "
            "for solving PDEs with arbitrary source terms, providing "
            "elegant and general solutions.",
            duration=9,
        )
        play_intro(self, "Green's Functions", "Partial Differential Equations")

        title = self.ly.title("The Impulse Response of a PDE")

        items = [
            Text("Know the response to a single impulse", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Superpose to get the response to any source", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Powerful tool for inhomogeneous PDEs", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: What is a Green's Function?
    # ------------------------------------------------------------------ #
    def scene2_impulse_response(self):
        self.add_subcaption(
            "A Green's function G(x, xi) is the solution to the PDE "
            "when the source is a point mass, or Dirac delta, at "
            "position xi. It tells us how the system at point x "
            "responds to a unit impulse at xi. For an inhomogeneous "
            "PDE, the full solution is a convolution of the Green's "
            "function with the source.",
            duration=10,
        )
        title = self.ly.title("Green's Function = Impulse Response")

        equation = MathTex(
            r"\mathcal{L} G(x, \xi) = \delta(x - \xi)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(equation)
        self.play(Write(equation), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(equation), run_time=0.3)

        items = [
            Text("G(x, xi): response at x to impulse at xi", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("delta(x - xi): Dirac delta (point source)", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Full solution: convolution with source term", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: The Heat Kernel
    # ------------------------------------------------------------------ #
    def scene3_heat_kernel(self):
        self.add_subcaption(
            "For the heat equation, the Green's function is the heat "
            "kernel. It is a Gaussian that spreads out over time, "
            "starting from a point source. The width of the Gaussian "
            "grows with the square root of time, and the height "
            "decreases to conserve total heat.",
            duration=9,
        )
        title = self.ly.title("The Heat Kernel")

        kernel = MathTex(
            r"G(x, t; \xi) = \frac{1}{\sqrt{4\pi\alpha t}}",
            r"e^{-\frac{(x-\xi)^2}{4\alpha t}}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.center_in_content(kernel)
        self.play(Write(kernel), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(kernel), run_time=0.3)

        items = [
            Text("Gaussian spreading from point source", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Width grows as sqrt(t), height decreases", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Total heat (integral) is conserved (= 1)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Convolution Solution
    # ------------------------------------------------------------------ #
    def scene4_convolution(self):
        self.add_subcaption(
            "Once we have the Green's function, the solution to "
            "any inhomogeneous PDE is given by convolution. We "
            "integrate the Green's function against the source "
            "term over all space. This is the same convolution "
            "theorem from Fourier analysis.",
            duration=9,
        )
        title = self.ly.title("Convolution Representation")

        conv = MathTex(
            r"u(x, t) = \int_{-\infty}^{\infty} G(x - \xi, t) f(\xi) \, d\xi",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(conv)
        self.play(Write(conv), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(conv), run_time=0.3)

        items = [
            Text("Integrate Green's function against source", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Works for any initial condition f(x)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Same idea: superposition of impulse responses", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Method of Images
    # ------------------------------------------------------------------ #
    def scene5_method_of_images(self):
        self.add_subcaption(
            "For simple geometries like a half-line or a quarter "
            "plane, the method of images constructs Green's "
            "functions using mirror images. We add fictitious "
            "sources to enforce boundary conditions. For a "
            "Dirichlet boundary at x equals zero, we subtract "
            "the image source.",
            duration=10,
        )
        title = self.ly.title("Method of Images")

        half_line = MathTex(
            r"G_{\text{half}}(x, t; \xi) = G_{\text{free}}(x - \xi, t) - G_{\text{free}}(x + \xi, t)",
            font_size=28, color=ACCENT,
        )
        self.ly.safe_place(half_line, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(half_line), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(half_line), run_time=0.3)

        items = [
            Text("Place a mirror source at the image point", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Sign chosen to match boundary condition", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Works for half-line, quarter-plane, spheres", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Key Properties
    # ------------------------------------------------------------------ #
    def scene6_properties(self):
        self.add_subcaption(
            "Green's functions have key properties that make them "
            "invaluable. They satisfy reciprocity: the response "
            "at x to an impulse at xi equals the response at xi "
            "to an impulse at x. They encode all the information "
            "about the PDE and its boundary conditions.",
            duration=9,
        )
        title = self.ly.title("Properties of Green's Functions")

        items = [
            Text("Reciprocity: G(x, xi) = G(xi, x)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Encodes PDE + boundary conditions", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Universal building block for solutions", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene7_summary(self):
        self.add_subcaption(
            "Green's functions are the impulse responses of PDEs. "
            "The heat kernel is a Gaussian that spreads over time. "
            "Solutions are obtained by convolution. The method of "
            "images handles simple boundary conditions. Green's "
            "functions encode everything about a PDE. Next, we "
            "study distributions and weak solutions.",
            duration=10,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("Green's function: response to point source", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Heat kernel: spreading Gaussian", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Solutions by convolution with source", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Method of images for boundaries", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        play_outro(self, "Distributions & Weak Solutions", "Partial Differential Equations")
