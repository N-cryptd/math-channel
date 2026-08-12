"""
Video 192: Numerical Methods for PDEs -- Partial Differential Equations Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video192_NumericalMethodsPDEs

Topics: Why numerical methods are needed,
        Finite difference method (FDM),
        Discretization of derivatives,
        Stability: CFL condition,
        Convergence and error analysis,
        Finite element method (FEM) overview.

Prerequisites: Videos 184-191 (all PDE theory),
               Calculus III (Taylor series for finite differences).

Quality Rules (mandatory):
1. Max 5 visible elements per scene
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


class Video192_NumericalMethodsPDEs(Scene):
    """Numerical Methods for PDEs -- PDE Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_why_numerical()
        self.scene3_finite_differences()
        self.scene4_discretizing_the_heat_eq()
        self.scene5_stability()
        self.scene6_fem_overview()
        self.scene7_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Most PDEs cannot be solved exactly. Complex geometries, "
            "nonlinear equations, and real-world problems demand "
            "numerical methods. The computer becomes our laboratory, "
            "approximating solutions on a discrete grid. This video "
            "introduces the two most important numerical methods "
            "for PDEs.",
            duration=10,
        )
        play_intro(self, "Numerical Methods for PDEs", "Partial Differential Equations")

        title = self.ly.title("When Analytic Solutions Fail")

        items = [
            Text("Complex geometries: no exact solution", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Nonlinear equations: superposition fails", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Real-world problems need computers", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Why Numerical Methods
    # ------------------------------------------------------------------ #
    def scene2_why_numerical(self):
        self.add_subcaption(
            "Analytical methods like separation of variables only "
            "work for very special cases. Real engineering problems "
            "involve irregular domains, variable coefficients, and "
            "nonlinear terms. Numerical methods discretize the PDE "
            "into a system of algebraic equations that computers "
            "can solve efficiently.",
            duration=9,
        )
        title = self.ly.title("The Need for Computation")

        items = [
            Text("Separation of variables: only rectangles", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Green's functions: only simple geometries", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Numerical methods: any geometry, any PDE", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Trade exactness for generality", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Finite Differences
    # ------------------------------------------------------------------ #
    def scene3_finite_differences(self):
        self.add_subcaption(
            "The finite difference method replaces derivatives with "
            "difference quotients on a grid. The first derivative "
            "becomes a central difference, and the second derivative "
            "becomes a second-order central difference. These "
            "approximations come from Taylor's theorem.",
            duration=9,
        )
        title = self.ly.title("Finite Difference Approximations")

        fd1 = MathTex(
            r"u'(x) \approx \frac{u(x+h) - u(x-h)}{2h}",
            r"\quad \text{(central difference)}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(fd1, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(fd1), run_time=NORMAL)

        fd2 = MathTex(
            r"u''(x) \approx \frac{u(x+h) - 2u(x) + u(x-h)}{h^2}",
            r"\quad \text{(2nd order)}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(fd2, direction=DOWN, anchor=fd1, buff=0.3)
        self.play(Write(fd2), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Discretizing the Heat Equation
    # ------------------------------------------------------------------ #
    def scene4_discretizing_the_heat_eq(self):
        self.add_subcaption(
            "To solve the heat equation numerically, we replace "
            "each derivative with its finite difference "
            "approximation on a grid. This turns the PDE into a "
            "system of linear equations. At each time step, we "
            "update the temperature at every grid point.",
            duration=9,
        )
        title = self.ly.title("Discretizing the Heat Equation")

        discrete = MathTex(
            r"\frac{u_j^{n+1} - u_j^n}{\Delta t} = \alpha \frac{u_{j+1}^n - 2u_j^n + u_{j-1}^n}{(\Delta x)^2}",
            font_size=28, color=WHITE,
        )
        self.ly.safe_place(discrete, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(discrete), run_time=NORMAL)

        note = Text(
            "PDE becomes algebraic equations on a grid",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=discrete, buff=0.25)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Stability and CFL
    # ------------------------------------------------------------------ #
    def scene5_stability(self):
        self.add_subcaption(
            "Not all discretizations are stable. If the time step "
            "is too large relative to the space step, errors grow "
            "exponentially and the solution blows up. The Courant-"
            "Friedrichs-Lewy condition provides a stability bound: "
            "the ratio of time step to space step must be small "
            "enough for information to propagate correctly.",
            duration=10,
        )
        title = self.ly.title("Stability: The CFL Condition")

        cfl = MathTex(
            r"\frac{\alpha \Delta t}{(\Delta x)^2} \leq \frac{1}{2}",
            r"\quad \text{(CFL condition for heat equation)}",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(cfl, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(cfl), run_time=NORMAL)

        self.play(FadeOut(cfl), run_time=0.3)

        items = [
            Text("Too large time step: solution explodes", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("CFL: information must not skip grid points", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Smaller grid = more accurate but slower", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Finite Element Method Overview
    # ------------------------------------------------------------------ #
    def scene6_fem_overview(self):
        self.add_subcaption(
            "The finite element method takes a different approach. "
            "It starts from the weak form of the PDE and expands "
            "the solution in piecewise polynomial basis functions. "
            "FEM handles complex geometries naturally and is the "
            "dominant method in engineering simulation.",
            duration=9,
        )
        title = self.ly.title("Finite Element Method")

        items = [
            Text("Start from weak form of the PDE", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Expand in piecewise polynomial basis", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Handles complex geometries naturally", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Dominant method in engineering simulation", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene7_summary(self):
        self.add_subcaption(
            "Numerical methods solve PDEs that resist analytical "
            "techniques. Finite differences replace derivatives "
            "with difference quotients on a grid. The CFL "
            "condition ensures stability. The finite element "
            "method uses the weak form and handles complex "
            "geometries. In the final video, we summarize the "
            "entire PDE playlist.",
            duration=10,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("Finite differences: grid-based approximation", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("CFL condition: stability bound on time step", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("FEM: weak form + piecewise polynomials", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        play_outro(self, "PDE Summary", "Partial Differential Equations")
