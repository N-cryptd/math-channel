"""
Video 186: The Wave Equation -- Partial Differential Equations Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video186_WaveEquation

Topics: Derivation from Newton's second law (vibrating string),
        d'Alembert's solution on the real line,
        Separation of variables on [0, L],
        Standing waves and the harmonic series,
        Comparison with heat equation (oscillation vs decay).

Prerequisites: Video 184 (What is a PDE?), Video 185 (Heat Equation),
               Calculus III, Fourier Series (174-176).

Competitive insights:
- 3B1B covers wave equation visually in DE series
- commutant: wave equation separation (342K views, blackboard)
- Our approach: animated derivation + d'Alembert + standing waves

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


class Video186_WaveEquation(Scene):
    """The Wave Equation -- PDE Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_derivation()
        self.scene3_interpretation()
        self.scene4_initial_conditions()
        self.scene5_dalembert()
        self.scene6_separation()
        self.scene7_standing_waves()
        self.scene8_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "When you pluck a guitar string, ripples travel along "
            "the surface of a pond, or light crosses the universe, "
            "the same mathematical equation governs them all. The "
            "wave equation is the universal language of oscillation.",
            duration=8,
        )
        play_intro(self, "The Wave Equation", "Partial Differential Equations")

        title = self.ly.title("The Mathematics of Vibration")

        items = [
            Text("Guitar strings and drum heads", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Sound waves in air", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Electromagnetic radiation", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Derivation
    # ------------------------------------------------------------------ #
    def scene2_derivation(self):
        self.add_subcaption(
            "Consider a taut string under tension. A small segment "
            "of the string feels forces from both sides. The net "
            "vertical force depends on the curvature. By Newton's "
            "second law, mass times acceleration equals net force. "
            "This gives us the wave equation.",
            duration=9,
        )
        title = self.ly.title("Deriving the Wave Equation")

        step1 = Text(
            "Net force on a small segment:",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(step1, shift=LEFT * 0.15), run_time=NORMAL)

        force = MathTex(
            r"F_{\text{net}} = T \frac{\partial^2 u}{\partial x^2} \, \Delta x",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(force, direction=DOWN, anchor=step1, buff=0.3)
        self.play(Write(force), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(step1), FadeOut(force), run_time=0.3)

        step2 = Text(
            "Newton's second law (mass times acceleration):",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(step2, shift=LEFT * 0.15), run_time=NORMAL)

        result = MathTex(
            r"\frac{\partial^2 u}{\partial t^2}",
            r"=",
            r"c^2", r"\frac{\partial^2 u}{\partial x^2}",
            r"\quad c = \sqrt{T/\rho}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=step2, buff=0.4)
        self.play(Write(result), run_time=SLOW)

        c_note = Text(
            "c is the wave speed (tension / density)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(c_note, direction=DOWN, anchor=result, buff=0.25)
        self.play(FadeIn(c_note, shift=LEFT * 0.15), run_time=FAST)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Physical Interpretation
    # ------------------------------------------------------------------ #
    def scene3_interpretation(self):
        self.add_subcaption(
            "Unlike the heat equation, the wave equation is second "
            "order in time. This means oscillations, not exponential "
            "decay. The acceleration at any point is proportional to "
            "the curvature. Curved regions accelerate, while flat "
            "regions coast.",
            duration=8,
        )
        title = self.ly.title("What Does It Mean?")

        items = [
            Text("Second order in time -> oscillations, not decay", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Acceleration proportional to curvature", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Wave speed c depends on tension and density", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Contrast: heat equation decays, wave equation oscillates", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Initial Conditions
    # ------------------------------------------------------------------ #
    def scene4_initial_conditions(self):
        self.add_subcaption(
            "Because the wave equation is second order in time, we "
            "need two initial conditions: the initial shape of the "
            "string, and the initial velocity at each point. This is "
            "unlike the heat equation, which only needs one.",
            duration=8,
        )
        title = self.ly.title("Two Initial Conditions")

        ic1 = MathTex(
            r"u(x, 0) = f(x)",
            r"\quad \text{(initial displacement)}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ic1, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(ic1), run_time=NORMAL)

        ic2 = MathTex(
            r"\frac{\partial u}{\partial t}(x, 0) = g(x)",
            r"\quad \text{(initial velocity)}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ic2, direction=DOWN, anchor=ic1, buff=0.3)
        self.play(Write(ic2), run_time=NORMAL)

        note = Text(
            "Two conditions needed (2nd order in time)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=ic2, buff=0.25)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: d'Alembert's Solution
    # ------------------------------------------------------------------ #
    def scene5_dalembert(self):
        self.ly.section_divider("2", "d'Alembert's Solution")

        self.add_subcaption(
            "On the infinite real line with no boundaries, we can "
            "find the general solution by factoring the differential "
            "operator. The solution is a sum of a right-moving wave "
            "and a left-moving wave, each traveling at speed c.",
            duration=8,
        )
        title = self.ly.title("Traveling Wave Solution")

        dalembert = MathTex(
            r"u(x, t) = F(x - ct) + G(x + ct)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(dalembert)
        self.play(Write(dalembert), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(dalembert), run_time=0.3)

        items = [
            Text("F(x - ct): right-moving wave at speed c", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("G(x + ct): left-moving wave at speed c", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Superposition: waves pass through each other", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Separation of Variables
    # ------------------------------------------------------------------ #
    def scene6_separation(self):
        self.add_subcaption(
            "On a finite interval, we use separation of variables. "
            "The spatial problem is identical to the heat equation, "
            "giving the same sine eigenfunctions. But the temporal "
            "equation is second order, producing oscillations "
            "instead of exponential decay.",
            duration=9,
        )
        title = self.ly.title("Separation of Variables on [0, L]")

        ansatz = MathTex(
            r"u(x, t) = X(x) \, T(t)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ansatz, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(ansatz), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(ansatz), run_time=0.3)

        temporal = Text(
            "Temporal equation (oscillation!):",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(temporal, direction=DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(temporal, shift=LEFT * 0.15), run_time=FAST)

        t_eq = MathTex(
            r"T_n'' + c^2 \lambda_n T_n = 0",
            r"\quad \lambda_n = (n\pi/L)^2",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(t_eq, direction=DOWN, anchor=temporal, buff=0.3)
        self.play(Write(t_eq), run_time=NORMAL)

        t_sol = MathTex(
            r"T_n(t) = A_n \cos\!\left(\frac{n\pi c t}{L}\right)"
            r"+ B_n \sin\!\left(\frac{n\pi c t}{L}\right)",
            font_size=28, color=ACCENT,
        )
        self.ly.safe_place(t_sol, direction=DOWN, anchor=t_eq, buff=0.3)
        self.play(Write(t_sol), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Standing Waves
    # ------------------------------------------------------------------ #
    def scene7_standing_waves(self):
        self.add_subcaption(
            "The complete solution is a superposition of standing "
            "waves. Each mode oscillates at a specific frequency "
            "determined by the mode number n. These frequencies form "
            "the harmonic series, which is why musical instruments "
            "produce overtones at integer multiples.",
            duration=10,
        )
        title = self.ly.title("Standing Waves and Harmonics")

        full = MathTex(
            r"u(x,t) = \sum_{n=1}^{\infty} \sin\!\left(\frac{n\pi x}{L}\right)"
            r"\!\left[ A_n \cos\!\left(\frac{n\pi ct}{L}\right)"
            r"+ B_n \sin\!\left(\frac{n\pi ct}{L}\right) \right]",
            font_size=26, color=PRIMARY,
        )
        self.ly.safe_place(full, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(full), run_time=SLOW)
        self.wait(0.5)

        self.play(FadeOut(full), run_time=0.3)

        items = [
            Text("Each mode: a standing wave at a fixed frequency", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Frequencies: f_n = nc / (2L)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("The harmonic series explains musical overtones", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary(self):
        self.add_subcaption(
            "The wave equation governs oscillations and vibrations. "
            "It is second order in time, requiring two initial "
            "conditions. On the real line, d'Alembert gives "
            "traveling waves. On a finite interval, separation of "
            "variables yields standing waves at discrete harmonic "
            "frequencies. Next, we study Laplace's equation.",
            duration=10,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("Wave equation: 2nd order in time -> oscillations", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("d'Alembert: superposition of traveling waves", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Separation: standing waves at harmonic frequencies", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Contrast with heat: oscillation vs exponential decay", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        play_outro(self, "Laplace's Equation", "Partial Differential Equations")
