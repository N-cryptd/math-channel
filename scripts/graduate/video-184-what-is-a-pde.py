"""
Video 184: What is a PDE? -- Partial Differential Equations Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video184_WhatIsAPDE

Topics: What makes a PDE different from an ODE,
        The general form F(x, u, grad u, ...) = 0,
        Order and linearity classification,
        The three canonical PDEs (heat, wave, Laplace),
        Elliptic/parabolic/hyperbolic classification,
        Why PDEs are fundamentally harder than ODEs.

Prerequisites: Calculus III (multivariable calculus),
               Fourier Analysis (Videos 174-183),
               ODEs (Videos 55-66).

Competitive insights:
- No animated PDE introduction exists on YouTube
- 3B1B covers heat equation intuition (DE2) but not general PDE framework
- commutant has systematic PDE content (234K-342K views) but no animations
- Our approach: physical motivation -> general form -> classification -> canonical examples

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


class Video184_WhatIsAPDE(Scene):
    """What is a PDE? -- Partial Differential Equations."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_ordinary_vs_partial()
        self.scene3_general_form()
        self.scene4_canonical_pdes()
        self.scene5_classification()
        self.scene6_why_hard()
        self.scene7_playlist_preview()
        self.scene8_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook -- The World is Governed by PDEs
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "From the warmth of a morning coffee to the ripples on a "
            "pond, from the shape of a soap bubble to the behavior of "
            "quantum particles. Partial differential equations are the "
            "language that describes all of these phenomena.",
            duration=10,
        )
        play_intro(self, "What is a PDE?", "Partial Differential Equations")

        title = self.ly.title("The Equations That Rule the Universe")

        items = [
            Text("Heat spreading through a metal rod", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Ripples spreading across a pond", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Gravitational fields around planets", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Quantum mechanical wave functions", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: What Makes It "Partial"?
    # ------------------------------------------------------------------ #
    def scene2_ordinary_vs_partial(self):
        self.ly.section_divider("1", "Ordinary vs Partial")
        self.add_subcaption(
            "In an ordinary differential equation, the unknown depends "
            "on a single variable. In a partial differential equation, "
            "the unknown depends on multiple variables, and we take "
            "partial derivatives with respect to each one.",
            duration=8,
        )
        title = self.ly.title("Ordinary vs Partial")

        ode_label = Text("ODE (Ordinary)", font_size=BODY_SIZE, color=DIM, font=SANS)
        self.ly.safe_place(ode_label, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(ode_label, shift=LEFT * 0.15), run_time=NORMAL)

        ode_eq = MathTex(
            r"\frac{dy}{dx} = f(x, y)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(ode_eq, direction=DOWN, anchor=ode_label, buff=0.3)
        self.play(Write(ode_eq), run_time=NORMAL)

        ode_note = Text("One independent variable (x)", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(ode_note, direction=DOWN, anchor=ode_eq, buff=0.3)
        self.play(FadeIn(ode_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Transition: replace ODE with PDE
        self.play(FadeOut(ode_label), FadeOut(ode_eq), FadeOut(ode_note), run_time=0.4)

        pde_label = Text("PDE (Partial)", font_size=BODY_SIZE, color=DIM, font=SANS)
        self.ly.safe_place(pde_label, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(pde_label, shift=LEFT * 0.15), run_time=NORMAL)

        pde_eq = MathTex(
            r"\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(pde_eq, direction=DOWN, anchor=pde_label, buff=0.3)
        self.play(Write(pde_eq), run_time=NORMAL)

        pde_note = Text("Multiple independent variables (x, t)", font_size=LABEL_SIZE, color=PRIMARY, font=SANS)
        self.ly.safe_place(pde_note, direction=DOWN, anchor=pde_eq, buff=0.3)
        self.play(FadeIn(pde_note, shift=LEFT * 0.15), run_time=FAST)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: The General Form
    # ------------------------------------------------------------------ #
    def scene3_general_form(self):
        self.ly.section_divider("2", "General Form of a PDE")

        self.add_subcaption(
            "A partial differential equation relates a function of "
            "several variables to its partial derivatives. The order "
            "is the highest derivative that appears. Whether the unknown "
            "appears linearly or not determines if the equation is "
            "linear or nonlinear.",
            duration=10,
        )
        title = self.ly.title("General Form of a PDE")

        general = MathTex(
            r"F", r"\!\left(",
            r"x_1, \ldots, x_n,",
            r"u,",
            r"\frac{\partial u}{\partial x_1}, \ldots,",
            r"\frac{\partial^2 u}{\partial x_1^2},",
            r"\ldots",
            r"\right) = 0",
            font_size=36, color=WHITE,
        )
        self.ly.formula_box(general)
        self.play(Write(general), run_time=SLOW)
        self.wait(0.5)

        # Order definition
        self.play(FadeOut(general), run_time=0.3)

        order_title = Text("Order", font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD)
        self.ly.safe_place(order_title, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(order_title, shift=LEFT * 0.15), run_time=FAST)

        order_def = Text(
            "Highest partial derivative present",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(order_def, direction=DOWN, anchor=order_title, buff=0.3)
        self.play(FadeIn(order_def, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(order_title), FadeOut(order_def), run_time=0.3)

        # Linearity
        lin_title = Text("Linearity", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD)
        self.ly.safe_place(lin_title, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(lin_title, shift=LEFT * 0.15), run_time=FAST)

        lin_def = Text(
            "Unknown u appears to first power only",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(lin_def, direction=DOWN, anchor=lin_title, buff=0.3)
        self.play(FadeIn(lin_def, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.8)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: The Three Canonical PDEs
    # ------------------------------------------------------------------ #
    def scene4_canonical_pdes(self):
        self.ly.section_divider("1", "The Three Canonical PDEs")

        # --- Heat Equation ---
        self.add_subcaption(
            "The heat equation describes how temperature evolves over "
            "time. The rate of change at any point is proportional to "
            "the curvature at that point. Heat flows from hot regions "
            "to cold regions.",
            duration=8,
        )
        heat_title = self.ly.title("The Heat Equation")

        heat_eq = MathTex(
            r"\frac{\partial u}{\partial t}",
            r"=",
            r"\alpha", r"\nabla^2 u",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.formula_box(heat_eq)
        self.play(Write(heat_eq), run_time=NORMAL)
        self.wait(0.3)

        heat_meaning = Text(
            "Rate of change is proportional to curvature",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(heat_meaning, direction=DOWN, anchor=heat_eq, buff=0.4)
        self.play(FadeIn(heat_meaning, shift=LEFT * 0.15), run_time=NORMAL)

        heat_order = Text(
            "1st order in t, 2nd order in space -- Parabolic",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(heat_order, direction=DOWN, anchor=heat_meaning, buff=0.3)
        self.play(FadeIn(heat_order, shift=LEFT * 0.15), run_time=FAST)

        self.wait(0.8)
        self.ly.clear()

        # --- Wave Equation ---
        self.add_subcaption(
            "The wave equation governs vibrations and oscillations. "
            "The acceleration of any point is proportional to its "
            "curvature. This describes everything from guitar strings "
            "to electromagnetic radiation.",
            duration=8,
        )
        wave_title = self.ly.title("The Wave Equation")

        wave_eq = MathTex(
            r"\frac{\partial^2 u}{\partial t^2}",
            r"=",
            r"c^2", r"\nabla^2 u",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.formula_box(wave_eq)
        self.play(Write(wave_eq), run_time=NORMAL)
        self.wait(0.3)

        wave_meaning = Text(
            "Acceleration is proportional to curvature",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(wave_meaning, direction=DOWN, anchor=wave_eq, buff=0.4)
        self.play(FadeIn(wave_meaning, shift=LEFT * 0.15), run_time=NORMAL)

        wave_order = Text(
            "2nd order in t and space -- Hyperbolic",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(wave_order, direction=DOWN, anchor=wave_meaning, buff=0.3)
        self.play(FadeIn(wave_order, shift=LEFT * 0.15), run_time=FAST)

        self.wait(0.8)
        self.ly.clear()

        # --- Laplace's Equation ---
        self.add_subcaption(
            "Laplace's equation describes equilibrium states. There is "
            "no time evolution. The sum of second derivatives in all "
            "directions equals zero. Solutions are called harmonic "
            "functions and appear in electrostatics and fluid mechanics.",
            duration=9,
        )
        lap_title = self.ly.title("Laplace's Equation")

        lap_eq = MathTex(
            r"\nabla^2 u = 0",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(lap_eq)
        self.play(Write(lap_eq), run_time=NORMAL)
        self.wait(0.3)

        lap_meaning = Text(
            "Equilibrium state -- no time dependence",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(lap_meaning, direction=DOWN, anchor=lap_eq, buff=0.4)
        self.play(FadeIn(lap_meaning, shift=LEFT * 0.15), run_time=NORMAL)

        lap_order = Text(
            "2nd order in space only -- Elliptic",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(lap_order, direction=DOWN, anchor=lap_meaning, buff=0.3)
        self.play(FadeIn(lap_order, shift=LEFT * 0.15), run_time=FAST)

        self.wait(0.8)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Classification
    # ------------------------------------------------------------------ #
    def scene5_classification(self):
        self.ly.section_divider("3", "Classifying Second-Order PDEs")
        self.add_subcaption(
            "We classify second-order linear PDEs into three types "
            "based on their discriminant, similar to classifying conic "
            "sections. Each type has fundamentally different behavior "
            "and requires different solution techniques.",
            duration=9,
        )
        title = self.ly.title("Classifying Second-Order PDEs")

        # Three types in two-column layout
        left_items = [
            Text("Elliptic", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD),
            Text("Parabolic", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD),
            Text("Hyperbolic", font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD),
        ]
        right_items = [
            MathTex(r"\nabla^2 u = 0", font_size=HEADING_SIZE, color=ACCENT),
            MathTex(r"\frac{\partial u}{\partial t} = \alpha \nabla^2 u", font_size=HEADING_SIZE, color=SECONDARY),
            MathTex(r"\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u", font_size=HEADING_SIZE, color=PRIMARY),
        ]

        left_col, right_col = self.ly.two_columns(left_items, right_items, start_from=title)

        self.play(
            *[FadeIn(m, shift=LEFT * 0.15) for m in left_items],
            *[Write(m) for m in right_items],
            run_time=NORMAL,
        )

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Why Are PDEs Hard?
    # ------------------------------------------------------------------ #
    def scene6_why_hard(self):
        self.add_subcaption(
            "Ordinary differential equations have one independent variable "
            "and a rich, well-understood theory. Partial differential "
            "equations exist in infinite dimensions, making them "
            "fundamentally more difficult. There is no single general "
            "solution method.",
            duration=9,
        )
        title = self.ly.title("The Challenge of PDEs")

        items = [
            Text("ODEs: one variable, well-understood theory", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("PDEs: infinite-dimensional problems", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("No single general solution method", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Each equation type needs its own toolkit", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Preview of the Playlist
    # ------------------------------------------------------------------ #
    def scene7_playlist_preview(self):
        self.ly.section_divider("4", "What's Coming Up")
        self.add_subcaption(
            "In this playlist, we will develop the tools to solve "
            "each type of PDE. We will study separation of variables, "
            "the heat equation, the wave equation, Laplace's equation, "
            "and advanced methods including Green's functions and "
            "numerical techniques.",
            duration=9,
        )
        title = self.ly.title("What's Coming Up")

        items = [
            Text("The Heat Equation in depth", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("The Wave Equation and d'Alembert's solution", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Laplace's Equation and boundary values", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Separation of Variables method", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Green's Functions, distributions, and numerics", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary(self):
        self.add_subcaption(
            "PDEs involve functions of multiple variables and their "
            "partial derivatives. The three canonical types are "
            "elliptic, parabolic, and hyperbolic. Each requires "
            "specialized techniques. In the next video, we dive deep "
            "into the heat equation.",
            duration=9,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("PDEs have multiple independent variables", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Three canonical types: elliptic, parabolic, hyperbolic", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Each type needs specialized solution methods", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        play_outro(self, "The Heat Equation", "Partial Differential Equations")
