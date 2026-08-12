"""
Video 193: PDE Summary -- Partial Differential Equations Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video193_PDESummary

Topics: Recap of the entire PDE playlist (Videos 184-192),
        The three canonical PDEs and their relationships,
        Solution methods and when to use them,
        Advanced topics and further study,
        Connection to other playlists.

Prerequisites: All Videos 184-192.

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


class Video193_PDESummary(Scene):
    """PDE Summary -- PDE Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_three_canonical()
        self.scene3_solution_methods()
        self.scene4_connections()
        self.scene5_what_next()
        self.scene6_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "In this final video of the PDE playlist, we bring "
            "everything together. From the heat equation to Green's "
            "functions, from separation of variables to numerical "
            "methods, we have built a complete toolkit for "
            "understanding and solving partial differential equations.",
            duration=9,
        )
        play_intro(self, "PDE Summary", "Partial Differential Equations")

        title = self.ly.title("The Complete PDE Toolkit")

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: The Three Canonical PDEs
    # ------------------------------------------------------------------ #
    def scene2_three_canonical(self):
        self.add_subcaption(
            "The three canonical PDEs are the foundation. The heat "
            "equation is parabolic, describing diffusion and decay. "
            "The wave equation is hyperbolic, describing oscillations "
            "and wave propagation. Laplace's equation is elliptic, "
            "describing equilibrium states.",
            duration=8,
        )
        title = self.ly.title("The Big Three")

        heat = MathTex(
            r"\frac{\partial u}{\partial t} = \alpha \nabla^2 u",
            r"\quad \text{(parabolic)}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(heat, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(heat), run_time=NORMAL)

        wave = MathTex(
            r"\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u",
            r"\quad \text{(hyperbolic)}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(wave, direction=DOWN, anchor=heat, buff=0.3)
        self.play(Write(wave), run_time=NORMAL)

        lap = MathTex(
            r"\nabla^2 u = 0",
            r"\quad \text{(elliptic)}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(lap, direction=DOWN, anchor=wave, buff=0.3)
        self.play(Write(lap), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Solution Methods
    # ------------------------------------------------------------------ #
    def scene3_solution_methods(self):
        self.add_subcaption(
            "We learned four major solution approaches. Separation "
            "of variables works for linear PDEs on simple domains. "
            "Green's functions handle inhomogeneous problems. "
            "Sturm-Liouville theory unifies the eigenvalue problems. "
            "Numerical methods handle everything else.",
            duration=9,
        )
        title = self.ly.title("Solution Methods")

        items = [
            Text("Separation of variables: linear, simple domains", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Green's functions: impulse response method", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Sturm-Liouville: unifying eigenvalue theory", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Numerical methods: general-purpose computation", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Connections to Other Playlists
    # ------------------------------------------------------------------ #
    def scene4_connections(self):
        self.add_subcaption(
            "PDEs connect to many topics in our curriculum. The "
            "Fourier transform solves PDEs on the real line. "
            "Functional analysis provides the rigorous framework "
            "for existence and uniqueness. Complex analysis connects "
            "to harmonic functions. And the theory of distributions "
            "provides the language for weak solutions.",
            duration=10,
        )
        title = self.ly.title("Connections Across Mathematics")

        items = [
            Text("Fourier Analysis: transform method on R", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Functional Analysis: rigorous PDE theory", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Complex Analysis: harmonic functions, conformal maps", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Distributions: language for weak solutions", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: What Comes Next?
    # ------------------------------------------------------------------ #
    def scene5_what_next(self):
        self.add_subcaption(
            "PDEs are an enormous field. Topics for further study "
            "include nonlinear PDEs like the Navier-Stokes equations, "
            "variational methods, spectral theory, scattering "
            "theory, and geometric PDEs on manifolds. The study of "
            "PDEs connects to physics, engineering, finance, and "
            "biology.",
            duration=10,
        )
        title = self.ly.title("Further Study")

        items = [
            Text("Nonlinear PDEs: Navier-Stokes, KdV, Schrodinger", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Variational methods and calculus of variations", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Geometric PDEs on manifolds", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Applications: physics, engineering, biology", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Outro
    # ------------------------------------------------------------------ #
    def scene6_outro(self):
        self.add_subcaption(
            "Thank you for joining us on this journey through "
            "partial differential equations. You now have the "
            "foundations to understand and solve the equations "
            "that describe the physical world. Keep exploring!",
            duration=7,
        )
        play_outro(self)
