"""
Video 187: Laplace's Equation -- Partial Differential Equations Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video187_LaplacesEquation

Topics: Laplace's equation as the equilibrium PDE,
        Harmonic functions and their properties,
        Mean value property,
        Maximum principle,
        The Dirichlet problem on rectangles and disks.

Prerequisites: Video 184 (What is a PDE?), Videos 185-186 (heat + wave),
               Calculus III (divergence, gradient).

Competitive insights:
- No animated coverage of Laplace's equation on YouTube
- Our approach: harmonic functions, mean value property, maximum principle

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


class Video187_LaplacesEquation(Scene):
    """Laplace's Equation -- PDE Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_harmonic_functions()
        self.scene4_mean_value()
        self.scene5_maximum_principle()
        self.scene6_dirichlet_problem()
        self.scene7_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Some problems have no time evolution. A metal plate at "
            "steady-state temperature. The electric potential around "
            "a charged conductor. The pressure in a fluid at rest. "
            "All of these are governed by Laplace's equation, the "
            "PDE of perfect balance.",
            duration=9,
        )
        play_intro(self, "Laplace's Equation", "Partial Differential Equations")

        title = self.ly.title("The Equation of Equilibrium")

        items = [
            Text("Steady-state temperature distribution", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Electrostatic potential around charges", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Fluid pressure at rest", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Definition
    # ------------------------------------------------------------------ #
    def scene2_definition(self):
        self.add_subcaption(
            "Laplace's equation states that the Laplacian of the "
            "unknown function equals zero. It has no time derivative, "
            "meaning it describes equilibrium. It is the steady "
            "state that the heat equation approaches as time goes "
            "to infinity.",
            duration=8,
        )
        title = self.ly.title("Laplace's Equation")

        lap = MathTex(
            r"\nabla^2 u = 0",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(lap)
        self.play(Write(lap), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(lap), run_time=0.3)

        items = [
            Text("No time dependence -- pure equilibrium", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Elliptic PDE (2nd order in space only)", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Steady state of the heat equation", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Harmonic Functions
    # ------------------------------------------------------------------ #
    def scene3_harmonic_functions(self):
        self.add_subcaption(
            "Solutions to Laplace's equation are called harmonic "
            "functions. They have remarkable smoothness: every "
            "harmonic function is infinitely differentiable. Any "
            "linear combination of harmonic functions is also "
            "harmonic.",
            duration=8,
        )
        title = self.ly.title("Harmonic Functions")

        defn = Text(
            "Solutions to Laplace's equation are harmonic",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(defn, direction=DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(defn, shift=LEFT * 0.15), run_time=NORMAL)

        examples = MathTex(
            r"x^2 - y^2, \quad xy, \quad \ln r, \quad \frac{1}{r}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(examples, direction=DOWN, anchor=defn, buff=0.4)
        self.play(Write(examples), run_time=NORMAL)

        self.wait(0.5)
        self.play(FadeOut(defn), FadeOut(examples), run_time=0.3)

        items = [
            Text("Infinitely differentiable (C-infinity)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Linear combinations are also harmonic", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Real and imaginary parts of analytic functions", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Mean Value Property
    # ------------------------------------------------------------------ #
    def scene4_mean_value(self):
        self.add_subcaption(
            "The mean value property says that the value of a "
            "harmonic function at any point equals the average of "
            "its values on any circle centered at that point. This "
            "means harmonic functions have no hot spots or cold "
            "spots in the interior.",
            duration=9,
        )
        title = self.ly.title("The Mean Value Property")

        mvp = MathTex(
            r"u(x_0) = \frac{1}{2\pi}",
            r"\int_0^{2\pi} u(x_0 + r\cos\theta)\, d\theta",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(mvp)
        self.play(Write(mvp), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(mvp), run_time=0.3)

        items = [
            Text("Value at a point = average on any circle", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Unique to harmonic functions", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("No interior hot spots or cold spots", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Maximum Principle
    # ------------------------------------------------------------------ #
    def scene5_maximum_principle(self):
        self.add_subcaption(
            "The maximum principle is a powerful consequence of "
            "the mean value property. A non-constant harmonic "
            "function cannot have an interior maximum or minimum. "
            "The extremes must occur on the boundary of the domain. "
            "This is crucial for the theory of elliptic PDEs.",
            duration=10,
        )
        title = self.ly.title("The Maximum Principle")

        items = [
            Text("No interior maximum or minimum", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Extremes must be on the boundary", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Implies uniqueness of the Dirichlet problem", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Physical: equilibrium has no interior peaks", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: The Dirichlet Problem
    # ------------------------------------------------------------------ #
    def scene6_dirichlet_problem(self):
        self.add_subcaption(
            "The fundamental problem for Laplace's equation is "
            "the Dirichlet problem: given values on the boundary, "
            "find the harmonic function inside. By the maximum "
            "principle, this solution is unique. On a rectangle, "
            "we solve it using separation of variables and Fourier "
            "series.",
            duration=10,
        )
        title = self.ly.title("The Dirichlet Problem")

        problem = MathTex(
            r"\nabla^2 u = 0",
            r"\quad \text{in } \Omega",
            r"\qquad u = g",
            r"\quad \text{on } \partial\Omega",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(problem), run_time=0.3)

        items = [
            Text("Boundary values determine everything inside", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Solution exists and is unique (max principle)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("On a rectangle: separation of variables + Fourier", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("On a disk: Fourier in polar coordinates", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene7_summary(self):
        self.add_subcaption(
            "Laplace's equation describes equilibrium states. "
            "Its solutions are harmonic functions, which are "
            "infinitely smooth. The mean value property says each "
            "point's value is the average of its neighbors. The "
            "maximum principle guarantees uniqueness. Next, we "
            "study the general method of separation of variables.",
            duration=10,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("Laplace's equation: equilibrium, no time", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Harmonic functions: infinitely smooth", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Mean value property and maximum principle", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Dirichlet problem: boundary determines all", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        play_outro(self, "Separation of Variables", "Partial Differential Equations")
