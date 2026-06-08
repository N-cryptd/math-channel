"""
Video 45: Vector-Valued Functions
Calculus III -- Multivariable Playlist -- Video 5 of 14

Covers: definition of vector-valued functions, limits and continuity,
derivatives (component-by-component), velocity/speed/acceleration,
integrals, arc length, unit tangent vector.

Render draft:  manim -ql scripts/undergraduate/video-45-vector-valued-functions.py Video45_VectorValuedFunctions
Render final:  manim -qh scripts/undergraduate/video-45-vector-valued-functions.py Video45_VectorValuedFunctions
"""

from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video45_VectorValuedFunctions(Scene):
    """Full video: Vector-Valued Functions."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_limits()
        self.scene4_derivatives()
        self.scene5_velocity()
        self.scene6_integrals()
        self.scene7_arc_length()
        self.scene8_summary()

    # ── Scene 1: Hook + Channel Intro ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "What if a function outputs not a number, but a vector? "
            "A vector-valued function maps a real number to a vector. "
            "As the parameter t changes, the tip of that vector traces "
            "out a curve in space. This is how we describe paths.",
            duration=18,
        )
        play_intro(self, "Vector-Valued Functions", "Calculus III — Multivariable")

        bridge = Text(
            "What if a function outputs a vector instead of a number?",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(bridge)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3.0)
        self.ly.clear()

    # ── Scene 2: Definition ─────────────────────────────────────────
    def scene2_definition(self):
        self.add_subcaption(
            "A vector-valued function takes a real number t and returns "
            "a vector. In component form, r of t equals f of t, g of t, "
            "h of t, where each component is an ordinary function. "
            "As t varies, the tip traces a space curve.",
            duration=18,
        )

        self.ly.section_divider(1, "Definition")

        title = self.ly.title("A Function That Outputs a Vector")

        general = MathTex(
            r"\vec{r}(t) = \langle f(t),\, g(t),\, h(t) \rangle",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        note1 = Text(
            "Each component f, g, h is a real-valued function of t",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )

        circle_ex = MathTex(
            r"\vec{r}(t) = \langle \cos t,\, \sin t \rangle"
            r"\;\text{(unit circle)}",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        helix_ex = MathTex(
            r"\vec{r}(t) = \langle \cos t,\, \sin t,\, t \rangle"
            r"\;\text{(helix)}",
            font_size=BODY_SIZE, color=SECONDARY,
        )

        items = [general, note1, circle_ex, helix_ex]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 3: Limits and Continuity ──────────────────────────────
    def scene3_limits(self):
        self.add_subcaption(
            "To find the limit of a vector-valued function, take the "
            "limit of each component separately. The function is continuous "
            "if and only if every component function is continuous. "
            "All the familiar rules carry over from scalar calculus.",
            duration=16,
        )

        self.ly.section_divider(2, "Limits and Continuity")

        title = self.ly.title("Limits: Component by Component")

        limit_eq = MathTex(
            r"\lim_{t \to a} \vec{r}(t) = "
            r"\left\langle "
            r"\lim_{t \to a} f(t),\,"
            r"\lim_{t \to a} g(t),\,"
            r"\lim_{t \to a} h(t)"
            r"\right\rangle",
            font_size=BODY_SIZE, color=ACCENT,
        )

        continuity = Text(
            "Continuous iff each component is continuous",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )

        rules = Text(
            "Sum, product, and chain rules carry over from scalar calculus",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )

        items = [limit_eq, continuity, rules]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 4: Derivatives ────────────────────────────────────────
    def scene4_derivatives(self):
        self.add_subcaption(
            "The derivative of a vector-valued function is found by "
            "differentiating each component. The result r prime of t is "
            "a tangent vector to the curve. It always points in the "
            "direction of motion.",
            duration=18,
        )

        self.ly.section_divider(3, "Derivatives")

        title = self.ly.title("Differentiate Each Component")

        deriv_eq = MathTex(
            r"\vec{r}\,'(t) = \langle f'(t),\, g'(t),\, h'(t) \rangle",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        tangent_note = Text(
            "r'(t) is tangent to the curve at each point",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        direction_note = Text(
            "Points in the direction of motion along the curve",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )

        items = [deriv_eq, tangent_note, direction_note]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 5: Velocity, Speed, Acceleration ─────────────────────
    def scene5_velocity(self):
        self.add_subcaption(
            "If r of t describes the position of a particle, then the "
            "velocity is the first derivative, v equals r prime. The "
            "speed is the magnitude of the velocity vector. The "
            "acceleration is the second derivative, a equals r double "
            "prime. Let us work through an example.",
            duration=22,
        )

        self.ly.section_divider(4, "Velocity and Acceleration")

        title = self.ly.title("Physics Meets Calculus")

        pos = MathTex(
            r"\text{Position:}\quad \vec{r}(t)",
            font_size=BODY_SIZE, color=WHITE,
        )

        vel = MathTex(
            r"\text{Velocity:}\quad \vec{v}(t) = \vec{r}\,'(t)",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        spd = MathTex(
            r"\text{Speed:}\quad |\vec{v}(t)| = |\vec{r}\,'(t)|",
            font_size=BODY_SIZE, color=SECONDARY,
        )

        acc = MathTex(
            r"\text{Acceleration:}\quad \vec{a}(t) = \vec{v}\,'(t) = \vec{r}\,''(t)",
            font_size=BODY_SIZE, color=RED,
        )

        items = [pos, vel, spd, acc]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3.0)
        self.ly.clear()

        # Worked example
        self.add_subcaption(
            "Example: r of t equals t squared, t. Then the velocity "
            "is 2t, 1. The speed is the square root of 4t squared "
            "plus 1. And the acceleration is the constant vector 2, 0.",
            duration=16,
        )

        title2 = self.ly.title("Example: r(t) = (t^2, t)")

        given = MathTex(
            r"\vec{r}(t) = \langle t^2,\, t \rangle",
            font_size=BODY_SIZE, color=WHITE,
        )

        v_calc = MathTex(
            r"\vec{v}(t) = \vec{r}\,'(t) = \langle 2t,\, 1 \rangle",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        a_calc = MathTex(
            r"\vec{a}(t) = \vec{r}\,''(t) = \langle 2,\, 0 \rangle",
            font_size=BODY_SIZE, color=RED,
        )

        items2 = [given, v_calc, a_calc]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 6: Integrals ──────────────────────────────────────────
    def scene6_integrals(self):
        self.add_subcaption(
            "Integration works component by component as well. The "
            "indefinite integral of r of t is the vector of the "
            "integrals of each component, plus a constant vector C. "
            "To recover position from velocity, integrate with the "
            "initial condition.",
            duration=18,
        )

        self.ly.section_divider(5, "Integrals")

        title = self.ly.title("Integrate Each Component")

        int_eq = MathTex(
            r"\int \vec{r}(t)\, dt = "
            r"\left\langle "
            r"\int f(t)\, dt,\;"
            r"\int g(t)\, dt,\;"
            r"\int h(t)\, dt"
            r"\right\rangle + \vec{C}",
            font_size=BODY_SIZE, color=ACCENT,
        )

        recover = MathTex(
            r"\vec{r}(t) = \vec{r}(t_0) + \int_{t_0}^{t} \vec{v}(s)\, ds",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        recover_note = Text(
            "Recover position from velocity using initial condition",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )

        items = [int_eq, recover, recover_note]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 7: Arc Length ──────────────────────────────────────────
    def scene7_arc_length(self):
        self.add_subcaption(
            "The arc length of a space curve is found by integrating "
            "the speed of the particle over the time interval. The "
            "formula is L equals the integral from a to b of the "
            "magnitude of r prime, dt. We also define the unit "
            "tangent vector as r prime divided by its magnitude.",
            duration=20,
        )

        self.ly.section_divider(6, "Arc Length")

        title = self.ly.title("How Long Is the Curve?")

        ds = MathTex(
            r"ds = |\vec{r}\,'(t)|\, dt",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        arc_length = MathTex(
            r"L = \int_{a}^{b} |\vec{r}\,'(t)|\, dt",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        tangent = MathTex(
            r"\vec{T}(t) = \frac{\vec{r}\,'(t)}{|\vec{r}\,'(t)|}",
            font_size=BODY_SIZE, color=SECONDARY,
        )

        tangent_label = Text(
            "Unit tangent vector (always length 1)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )

        items = [ds, arc_length, tangent, tangent_label]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 8: Summary + Outro ──────────────────────────────────────
    def scene8_summary(self):
        self.add_subcaption(
            "To recap: a vector-valued function maps t to a vector "
            "and traces a curve in space. Limits, derivatives, and "
            "integrals are all computed component by component. "
            "The derivative is the velocity, its magnitude is speed, "
            "and arc length equals the integral of speed.",
            duration=22,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text(
                "r(t) = <f(t), g(t), h(t)> traces curves in space",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Limits, derivatives, integrals: component by component",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "r'(t) = velocity (tangent to the curve)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Speed = |r'(t)|,  Acceleration = r''(t)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Arc length L = integral of |r'(t)| dt from a to b",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(takeaways, start_from=title)
        self.wait(4.0)
        self.ly.clear()

        play_outro(self, "Partial Derivatives", "Calculus III — Multivariable")


# ── Compile check ──────────────────────────────────────────────────
if __name__ == "__main__":
    import py_compile
    py_compile.compile(__file__, doraise=True)
    print(f"Compile OK: {__file__}")
