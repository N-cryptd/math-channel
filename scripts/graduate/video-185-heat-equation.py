"""
Video 185: The Heat Equation -- Partial Differential Equations Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video185_HeatEquation

Topics: Derivation from Fourier's law of heat conduction,
        Initial and boundary conditions (Dirichlet, Neumann),
        Separation of variables method,
        Eigenvalue problem X'' + lambda X = 0,
        Fourier sine series solution,
        Exponential decay of modes and smoothing.

Prerequisites: Video 184 (What is a PDE?), Calculus III,
               Fourier Series (Videos 174-176).
Note: Video 182 covered heat equation via Fourier transform on R.
      This video covers the classical series approach on [0, L].

Competitive insights:
- 3B1B DE2 covers intuition beautifully (3.2M views)
- commutant covers derivation on blackboard (234K views)
- Faculty of Khan covers separation of variables rigorously (whiteboard)
- Our approach: animated derivation + separation of variables with visual modes

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


class Video185_HeatEquation(Scene):
    """The Heat Equation -- PDE Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_derivation()
        self.scene3_interpretation()
        self.scene4_boundary_conditions()
        self.scene5_separation_setup()
        self.scene6_spatial_problem()
        self.scene7_temporal_problem()
        self.scene8_complete_solution()
        self.scene9_example()
        self.scene10_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Why does a hot cup of coffee gradually cool down? "
            "The answer lies in the heat equation, one of the "
            "most fundamental partial differential equations in "
            "all of physics and engineering.",
            duration=8,
        )
        play_intro(self, "The Heat Equation", "Partial Differential Equations")

        title = self.ly.title("The Equation of Heat")

        items = [
            Text("Hot objects cool; cold objects warm", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Heat flows from high to low temperature", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("The rate depends on the temperature gradient", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Derivation from Physical Reasoning
    # ------------------------------------------------------------------ #
    def scene2_derivation(self):
        self.ly.section_divider("1", "Deriving the Heat Equation")
        self.add_subcaption(
            "We derive the heat equation from two physical principles. "
            "First, Fourier's law: heat flux is proportional to the "
            "negative temperature gradient. Second, conservation of "
            "energy: the rate of change equals flux in minus flux out.",
            duration=10,
        )
        title = self.ly.title("Deriving the Heat Equation")

        # Fourier's Law
        step1 = Text(
            "Step 1: Fourier's Law of Heat Conduction",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(step1, shift=LEFT * 0.15), run_time=NORMAL)

        flux_eq = MathTex(
            r"q = -k \frac{\partial u}{\partial x}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(flux_eq, direction=DOWN, anchor=step1, buff=0.3)
        self.play(Write(flux_eq), run_time=NORMAL)

        flux_note = Text(
            "Heat flux q is proportional to negative gradient",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(flux_note, direction=DOWN, anchor=flux_eq, buff=0.25)
        self.play(FadeIn(flux_note, shift=LEFT * 0.15), run_time=FAST)

        self.wait(0.5)
        self.play(FadeOut(step1), FadeOut(flux_eq), FadeOut(flux_note), run_time=0.4)

        # Conservation of energy
        step2 = Text(
            "Step 2: Conservation of Energy",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(step2, shift=LEFT * 0.15), run_time=NORMAL)

        balance = MathTex(
            r"\frac{\partial u}{\partial t}",
            r"=",
            r"\alpha \frac{\partial^2 u}{\partial x^2}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(balance, direction=DOWN, anchor=step2, buff=0.4)
        self.play(Write(balance), run_time=NORMAL)

        result_note = Text(
            "Rate of change = thermal diffusivity times curvature",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(result_note, direction=DOWN, anchor=balance, buff=0.25)
        self.play(FadeIn(result_note, shift=LEFT * 0.15), run_time=FAST)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Physical Interpretation
    # ------------------------------------------------------------------ #
    def scene3_interpretation(self):
        self.add_subcaption(
            "The heat equation tells us that temperature changes fastest "
            "where the curvature is greatest. At a peak in temperature, "
            "the second derivative is negative, so the temperature "
            "decreases. At a trough, it increases. This drives "
            "everything toward equilibrium.",
            duration=9,
        )
        title = self.ly.title("What Does It Mean?")

        items = [
            Text("Heat flows away from temperature peaks", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Rate of change is proportional to curvature", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Higher curvature means faster change", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Everything smooths toward equilibrium", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Initial and Boundary Conditions
    # ------------------------------------------------------------------ #
    def scene4_boundary_conditions(self):
        self.ly.section_divider("2", "Initial and Boundary Conditions")
        self.add_subcaption(
            "To solve a PDE we need conditions. The initial condition "
            "specifies the temperature at time zero. Boundary conditions "
            "specify what happens at the endpoints. Dirichlet fixes the "
            "temperature, and Neumann fixes the heat flux at the boundary.",
            duration=9,
        )
        title = self.ly.title("Initial and Boundary Conditions")

        ic = MathTex(
            r"u(x, 0) = f(x)", r"\quad \text{(initial condition)}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(ic, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(ic), run_time=NORMAL)

        self.wait(0.5)
        self.play(FadeOut(ic), run_time=0.3)

        bc_title = Text("Boundary Conditions", font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD)
        self.ly.safe_place(bc_title, direction=DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(bc_title, shift=LEFT * 0.15), run_time=FAST)

        dirichlet = MathTex(
            r"u(0,t) = u(L,t) = 0",
            r"\quad \text{(Dirichlet: fixed temp)}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(dirichlet, direction=DOWN, anchor=bc_title, buff=0.3)
        self.play(Write(dirichlet), run_time=NORMAL)

        neumann = MathTex(
            r"\frac{\partial u}{\partial x}(0,t) = 0",
            r"\quad \text{(Neumann: insulated)}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(neumann, direction=DOWN, anchor=dirichlet, buff=0.3)
        self.play(Write(neumann), run_time=NORMAL)

        focus = Text(
            "We focus on Dirichlet with zero endpoints",
            font_size=LABEL_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(focus, direction=DOWN, anchor=neumann, buff=0.3)
        self.play(FadeIn(focus, shift=LEFT * 0.15), run_time=FAST)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Separation of Variables — Setup
    # ------------------------------------------------------------------ #
    def scene5_separation_setup(self):
        self.ly.section_divider("2", "Separation of Variables")

        self.add_subcaption(
            "The key idea is to assume the solution is a product of "
            "a function of x and a function of t. When we substitute "
            "this into the heat equation, we can separate the variables "
            "and solve two ordinary differential equations independently.",
            duration=9,
        )
        title = self.ly.title("Assume a Product Solution")

        # Show the ansatz
        ansatz = MathTex(
            r"u(x, t) = X(x) \, T(t)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.formula_box(ansatz)
        self.play(Write(ansatz), run_time=NORMAL)
        self.wait(0.3)

        # Substitution
        sub = MathTex(
            r"\frac{X T'}{X T} = \alpha \frac{X'' T}{X T}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(sub, direction=DOWN, anchor=ansatz, buff=0.4)
        self.play(Write(sub), run_time=NORMAL)
        self.wait(0.5)

        # Simplified
        self.play(FadeOut(sub), run_time=0.3)

        separated = MathTex(
            r"\frac{T'}{T}",
            r"=",
            r"\alpha \frac{X''}{X}",
            r"=",
            r"-\lambda",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(separated, direction=DOWN, anchor=ansatz, buff=0.4)
        self.play(Write(separated), run_time=NORMAL)

        note = Text(
            "Each side must equal a constant (negative for BCs)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=separated, buff=0.3)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: The Spatial Problem — Eigenvalues
    # ------------------------------------------------------------------ #
    def scene6_spatial_problem(self):
        self.ly.section_divider("3", "The Spatial Eigenvalue Problem")
        self.add_subcaption(
            "The spatial equation is a second-order ODE with boundary "
            "conditions. Only specific values of lambda, called "
            "eigenvalues, allow solutions that satisfy both boundary "
            "conditions. These are sine functions that vanish at "
            "both endpoints.",
            duration=9,
        )
        title = self.ly.title("The Spatial Eigenvalue Problem")

        spatial = MathTex(
            r"X'' + \lambda X = 0",
            r"\quad",
            r"X(0) = X(L) = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(spatial, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(spatial), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(spatial), run_time=0.3)

        eigenvalues = Text("Eigenvalues and eigenfunctions:", font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD)
        self.ly.safe_place(eigenvalues, direction=DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(eigenvalues, shift=LEFT * 0.15), run_time=FAST)

        lambda_eq = MathTex(
            r"\lambda_n = \left(\frac{n\pi}{L}\right)^2",
            r"\quad n = 1, 2, 3, \ldots",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(lambda_eq, direction=DOWN, anchor=eigenvalues, buff=0.3)
        self.play(Write(lambda_eq), run_time=NORMAL)

        x_n = MathTex(
            r"X_n(x) = \sin\!\left(\frac{n\pi x}{L}\right)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(x_n, direction=DOWN, anchor=lambda_eq, buff=0.3)
        self.play(Write(x_n), run_time=NORMAL)

        connection = Text(
            "A Fourier sine series on [0, L]",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(connection, direction=DOWN, anchor=x_n, buff=0.25)
        self.play(FadeIn(connection, shift=LEFT * 0.15), run_time=FAST)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: The Temporal Problem
    # ------------------------------------------------------------------ #
    def scene7_temporal_problem(self):
        self.add_subcaption(
            "The temporal equation is a simple first-order ODE. Its "
            "solution is an exponential decay. Critically, higher "
            "modes decay much faster than lower ones. Mode number n "
            "squared appears in the exponent, so the fundamental "
            "mode persists the longest.",
            duration=10,
        )
        title = self.ly.title("The Temporal Equation")

        temporal = MathTex(
            r"T' + \alpha \lambda_n T = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(temporal, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(temporal), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(temporal), run_time=0.3)

        solution = MathTex(
            r"T_n(t) = e^{-\alpha (n\pi/L)^2 \, t}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.formula_box(solution)
        self.play(Write(solution), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(solution), run_time=0.3)

        items = [
            Text("Each mode decays exponentially", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Higher n means faster decay (n squared!)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Fundamental mode (n=1) lasts longest", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Complete Solution
    # ------------------------------------------------------------------ #
    def scene8_complete_solution(self):
        self.ly.section_divider("4", "The Complete Solution")
        self.add_subcaption(
            "The complete solution is a superposition of all modes. "
            "The initial condition determines the Fourier sine "
            "coefficients. As time goes to infinity, all modes decay "
            "and the temperature approaches zero everywhere, which "
            "is the equilibrium for our fixed-zero boundaries.",
            duration=10,
        )
        title = self.ly.title("The Complete Solution")

        full = MathTex(
            r"u(x,t) = \sum_{n=1}^{\infty} b_n \sin\!\left(\frac{n\pi x}{L}\right)"
            r" e^{-\alpha (n\pi/L)^2 t}",
            font_size=32, color=SECONDARY,
        )
        self.ly.formula_box(full)
        self.play(Write(full), run_time=SLOW)
        self.wait(0.5)

        self.play(FadeOut(full), run_time=0.3)

        coeffs = MathTex(
            r"b_n = \frac{2}{L} \int_0^L f(x) \sin\!\left(\frac{n\pi x}{L}\right) dx",
            font_size=30, color=WHITE,
        )
        self.ly.safe_place(coeffs, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(coeffs), run_time=NORMAL)

        coeffs_label = Text(
            "Fourier sine coefficients from initial condition",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(coeffs_label, direction=DOWN, anchor=coeffs, buff=0.25)
        self.play(FadeIn(coeffs_label, shift=LEFT * 0.15), run_time=FAST)

        self.wait(0.5)
        self.play(FadeOut(coeffs), FadeOut(coeffs_label), run_time=0.3)

        limit = Text(
            "As t approaches infinity, u approaches zero",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(limit, direction=DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(limit, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 9: Visual Example
    # ------------------------------------------------------------------ #
    def scene9_example(self):
        self.add_subcaption(
            "Consider a metal rod with a triangular temperature spike "
            "in the middle. The Fourier coefficients capture this shape. "
            "Over time, each mode decays independently. Higher modes "
            "vanish first, leaving a smoother profile. Eventually "
            "the rod reaches uniform cold temperature.",
            duration=10,
        )
        title = self.ly.title("Example: Triangular Temperature Spike")

        initial = MathTex(
            r"f(x) = \begin{cases} 2x/L & 0 \le x \le L/2 \\ 2(L-x)/L & L/2 < x \le L \end{cases}",
            font_size=28, color=WHITE,
        )
        self.ly.safe_place(initial, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(initial), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(initial), run_time=0.3)

        items = [
            Text("Fourier sine series captures the triangular shape", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Higher modes add detail to the shape", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Over time, high modes vanish first", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Profile smooths toward equilibrium", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 10: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene10_summary(self):
        self.add_subcaption(
            "The heat equation describes how temperature evolves. "
            "Separation of variables splits the PDE into two ODEs. "
            "Boundary conditions create a discrete spectrum of "
            "eigenvalues. Higher Fourier modes decay exponentially "
            "faster, producing a smoothing effect. In the next "
            "video, we study the wave equation.",
            duration=10,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("Heat equation from conservation + Fourier's law", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Separation of variables: u = X(x)T(t)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Boundary conditions yield discrete eigenvalues", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Higher modes decay faster, producing smoothing", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        play_outro(self, "The Wave Equation", "Partial Differential Equations")
