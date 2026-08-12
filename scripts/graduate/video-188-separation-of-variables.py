"""
Video 188: Separation of Variables -- Partial Differential Equations Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video188_SeparationOfVariables

Topics: Separation of variables as a unified framework,
        The separation ansatz and reduction to ODEs,
        Eigenvalue problems from boundary conditions,
        Fourier series expansion of initial conditions,
        Superposition principle and general solutions,
        Comparison across heat, wave, and Laplace equations,
        When separation works and when it fails.

Prerequisites: Video 184 (What is a PDE?), Videos 185-187 (heat, wave, Laplace),
               Fourier Series (Videos 174-176), Linear Algebra.

Competitive insights:
- No competitor covers separation as a unified framework with animations
- 3B1B DE3 touches the concept but doesn't complete derivation
- Faculty of Khan and commutant cover specific equations but not the general method
- Our approach: unify all three classical PDEs under one framework

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


class Video188_SeparationOfVariables(Scene):
    """Separation of Variables -- unified framework for PDEs."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_general_idea()
        self.scene3_eigenvalue_problem()
        self.scene4_fourier_expansion()
        self.scene5_superposition()
        self.scene6_comparison()
        self.scene7_when_it_works()
        self.scene8_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "In the last three videos, we solved the heat equation, "
            "the wave equation, and Laplace's equation. Each time, "
            "we used the same trick: assume the solution is a "
            "product of single-variable functions. Today, we step "
            "back and understand this method as one unified "
            "framework.",
            duration=11,
        )
        play_intro(self, "Separation of Variables", "Partial Differential Equations")

        title = self.ly.title("One Method to Solve Them All")

        items = [
            Text("Heat equation: exponential decay", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Wave equation: oscillation", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Laplace's equation: no time", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: The General Idea
    # ------------------------------------------------------------------ #
    def scene2_general_idea(self):
        self.add_subcaption(
            "The core idea is breathtakingly simple. Assume the "
            "solution is a product of functions, each depending "
            "on only one variable. Substitute this into the PDE "
            "and divide by the product. If the variables truly "
            "separate, each side must equal a constant. This "
            "reduces a partial differential equation to a system "
            "of ordinary differential equations.",
            duration=13,
        )
        title = self.ly.title("The Separation Ansatz")

        ansatz = MathTex(
            r"u(x, t) = X(x) \cdot T(t)",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.safe_place(ansatz, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(ansatz), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(ansatz), run_time=0.3)

        items = [
            Text("Substitute into PDE", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Divide by the product X*T", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Each side must equal a constant", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("PDE becomes a system of ODEs", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: The Eigenvalue Problem
    # ------------------------------------------------------------------ #
    def scene3_eigenvalue_problem(self):
        self.add_subcaption(
            "After separating variables, the spatial equation "
            "comes with boundary conditions. Not every value "
            "of the separation constant satisfies these "
            "conditions. Only special discrete values, called "
            "eigenvalues, work. Each eigenvalue produces an "
            "eigenfunction, a basis function for building "
            "solutions.",
            duration=12,
        )
        title = self.ly.title("The Eigenvalue Problem")

        spatial = MathTex(
            r"X'' + \lambda X = 0",
            r", \quad X(0) = X(L) = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(spatial, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(spatial), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(spatial), run_time=0.3)

        items = [
            Text("Boundary conditions restrict the constant", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Only discrete eigenvalues work", font_size=BODY_SIZE, color=RED, font=SANS),
            MathTex(r"\lambda_n = \left(\frac{n\pi}{L}\right)^2", font_size=HEADING_SIZE, color=ACCENT),
            Text("Each eigenvalue gives an eigenfunction", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Fourier Series Expansion
    # ------------------------------------------------------------------ #
    def scene4_fourier_expansion(self):
        self.add_subcaption(
            "The initial condition tells us how the solution "
            "starts. To match it, we decompose the initial "
            "data into eigenfunction components. This is a "
            "projection: the Fourier coefficients are the inner "
            "products of the initial data with each basis "
            "function. Higher modes capture finer details.",
            duration=12,
        )
        title = self.ly.title("Expanding in Eigenfunctions")

        coeff = MathTex(
            r"b_n = \frac{2}{L}",
            r"\int_0^L f(x) \sin\!\left(\frac{n\pi x}{L}\right) dx",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(coeff, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(coeff), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(coeff), run_time=0.3)

        items = [
            Text("Inner product: projection onto basis", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Initial condition determines all coefficients", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Higher modes = higher frequency detail", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: The Superposition Principle
    # ------------------------------------------------------------------ #
    def scene5_superposition(self):
        self.add_subcaption(
            "Linearity is the key property that makes all of "
            "this work. If u sub 1 and u sub 2 are solutions, "
            "then any linear combination is also a solution. "
            "Each eigenfunction paired with its temporal "
            "behavior is one mode. The general solution is the "
            "infinite sum of all modes. This lets us match any "
            "initial condition.",
            duration=13,
        )
        title = self.ly.title("Linearity and Superposition")

        items = [
            Text("PDEs are linear operators", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("If u_1 and u_2 solve it, so does a*u_1 + b*u_2", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Each mode: eigenfunction times temporal part", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("General solution = sum of all modes", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Heat vs Wave vs Laplace
    # ------------------------------------------------------------------ #
    def scene6_comparison(self):
        self.add_subcaption(
            "Here is the beautiful insight. All three classical "
            "PDEs share the same spatial eigenvalue problem. "
            "The eigenvalues are always n pi over L squared. "
            "What changes is only the temporal equation: "
            "exponential decay for heat, oscillation for waves, "
            "and no time at all for Laplace. One spatial "
            "structure, three physical behaviors.",
            duration=13,
        )
        title = self.ly.title("Three Equations, One Structure")

        spatial = MathTex(
            r"\text{Spatial: } X'' + \lambda X = 0",
            r"\quad \Rightarrow \quad",
            r"\lambda_n = \left(\frac{n\pi}{L}\right)^2",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(spatial, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(spatial), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(spatial), run_time=0.3)

        items = [
            Text("Heat:  T' + alpha*lambda*T = 0  (decay)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Wave:  T'' + c^2*lambda*T = 0   (oscillation)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Laplace: no time equation", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Spatial structure is universal", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: When Does Separation Work?
    # ------------------------------------------------------------------ #
    def scene7_when_it_works(self):
        self.add_subcaption(
            "Separation of variables is powerful but not "
            "universal. It works for linear, homogeneous "
            "equations on domains where the coordinates match "
            "the geometry: rectangles with Cartesian, disks "
            "with polar, spheres with spherical coordinates. "
            "It fails for nonlinear equations or irregular "
            "boundaries. The Sturm-Liouville theory "
            "generalizes this to a broad class of problems.",
            duration=14,
        )
        title = self.ly.title("When Can We Separate?")

        items = [
            Text("Linear, homogeneous PDEs", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Coordinates must match geometry", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Fails: nonlinear PDEs, irregular domains", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Sturm-Liouville theory generalizes this", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary(self):
        self.add_subcaption(
            "Separation of variables is the workhorse method "
            "for solving PDEs analytically. The product ansatz "
            "reduces a PDE to ODEs. Boundary conditions create "
            "eigenvalue problems. Fourier series expand initial "
            "conditions. Superposition builds the general "
            "solution from individual modes. Next, we study "
            "Sturm-Liouville theory, which generalizes all of "
            "this to a powerful abstract framework.",
            duration=13,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("Product ansatz: PDE becomes ODEs", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Boundary conditions create eigenvalue problems", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Fourier series expand initial conditions", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Superposition builds general solutions", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        play_outro(self, "Sturm-Liouville Theory", "Partial Differential Equations")
