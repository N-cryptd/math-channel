"""
Video 42: Dot Product in 3D
Calculus III -- Multivariable Playlist -- Video 2 of 14

Covers: algebraic definition of dot product, geometric meaning (cosine formula),
projection interpretation, properties, orthogonality test, and worked examples
(work done by a force).

Render draft:  manim -ql scripts/undergraduate/video-42-dot-product.py Video42_DotProduct
Render final:  manim -qh scripts/undergraduate/video-42-dot-product.py Video42_DotProduct
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


class Video42_DotProduct(Scene):
    """Full video: Dot Product in 3D."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_algebraic_definition()
        self.scene3_geometric_meaning()
        self.scene4_projection()
        self.scene5_properties()
        self.scene6_worked_example()
        self.scene7_summary()

    # ── Scene 1: Hook + Channel Intro ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Now that we have 3D vectors, how do we measure "
            "how much two vectors point in the same direction? "
            "The answer is the dot product.",
            duration=12,
        )
        play_intro(self, "Dot Product in 3D", "Calculus III — Multivariable")

        bridge = Text(
            "How much do two vectors agree in direction?",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(bridge)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3.0)
        self.ly.clear()

    # ── Scene 2: The Algebraic Definition ──────────────────────────
    def scene2_algebraic_definition(self):
        self.add_subcaption(
            "The dot product takes two vectors and returns a scalar number. "
            "You multiply corresponding components and add them all up. "
            "For vectors a and b, the dot product a dot b equals "
            "a1 times b1 plus a2 times b2 plus a3 times b3.",
            duration=22,
        )

        self.ly.section_divider(1, "The Dot Product Formula")

        title = self.ly.title("Algebraic Definition")

        defn = MathTex(
            r"\vec{a} \cdot \vec{b} "
            r"= a_1 b_1 + a_2 b_2 + a_3 b_3",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        note = Text(
            "Result is a SCALAR (a number, not a vector)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        example = MathTex(
            r"\langle 1,2,3 \rangle \cdot \langle 4,5,6 \rangle "
            r"= 4 + 10 + 18 = 32",
            font_size=BODY_SIZE, color=WHITE,
        )

        items = [defn, note, example]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 3: Geometric Meaning ─────────────────────────────────
    def scene3_geometric_meaning(self):
        self.add_subcaption(
            "Geometrically, the dot product equals the product of "
            "the magnitudes times the cosine of the angle between the vectors. "
            "This connects the algebraic formula to the geometry of space. "
            "When the angle is zero, vectors align and the dot product is maximally positive. "
            "When the angle is ninety degrees, they are perpendicular and the dot product equals zero.",
            duration=28,
        )

        self.ly.section_divider(2, "Geometric Meaning")

        title = self.ly.title("The Cosine Formula")

        geo_formula = MathTex(
            r"\vec{a} \cdot \vec{b} "
            r"= |\vec{a}|\, |\vec{b}| \cos\theta",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        theta_label = MathTex(
            r"\theta = \text{angle between } \vec{a} \text{ and } \vec{b}",
            font_size=BODY_SIZE, color=DIM,
        )

        cases = VGroup(
            MathTex(r"\theta = 0", font_size=BODY_SIZE).set_color(SECONDARY),
            Text("same direction", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ).arrange(RIGHT, buff=0.4)

        cases2 = VGroup(
            MathTex(r"\theta = 90^\circ", font_size=BODY_SIZE).set_color(SECONDARY),
            Text("perpendicular: dot product = 0", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ).arrange(RIGHT, buff=0.4)

        items = [geo_formula, theta_label, cases, cases2]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 4: Projection Interpretation ──────────────────────────
    def scene4_projection(self):
        self.add_subcaption(
            "The dot product tells us how much of one vector projects onto another. "
            "The scalar projection of b onto a is the dot product divided by the length of a. "
            "The vector projection also includes the direction of a. "
            "Think of it as the shadow that one vector casts onto the other. "
            "In physics, this idea is crucial because only force along displacement does work.",
            duration=30,
        )

        self.ly.section_divider(3, "Projection")

        title = self.ly.title("Projection onto a Vector")

        scalar_proj = MathTex(
            r"\text{comp}_{\vec{a}}(\vec{b}) "
            r"= \frac{\vec{a} \cdot \vec{b}}{|\vec{a}|}",
            font_size=BODY_SIZE, color=ACCENT,
        )

        vec_proj = MathTex(
            r"\text{proj}_{\vec{a}}(\vec{b}) "
            r"= \frac{\vec{a} \cdot \vec{b}}{|\vec{a}|^2}\, \vec{a}",
            font_size=BODY_SIZE, color=ACCENT,
        )

        shadow = Text(
            "Think of it as the shadow of one vector onto another",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        application = Text(
            "Physics: only the force component along displacement does work",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        items = [scalar_proj, vec_proj, shadow, application]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 5: Properties of the Dot Product ─────────────────────
    def scene5_properties(self):
        self.add_subcaption(
            "The dot product has several important algebraic properties. "
            "It is commutative, meaning a dot b equals b dot a. "
            "It distributes over vector addition. "
            "And the dot product of a vector with itself gives the magnitude squared. "
            "Crucially, if the dot product of two nonzero vectors is zero, "
            "they must be perpendicular to each other.",
            duration=30,
        )

        self.ly.section_divider(4, "Key Properties")

        title = self.ly.title("Properties")

        p1 = MathTex(
            r"\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}",
            font_size=BODY_SIZE, color=WHITE,
        )
        p1_label = Text(
            "Commutative", font_size=LABEL_SIZE, color=DIM, font=SANS,
        )

        p2 = MathTex(
            r"\vec{a} \cdot (\vec{b} + \vec{c}) "
            r"= \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c}",
            font_size=BODY_SIZE, color=WHITE,
        )
        p2_label = Text(
            "Distributive", font_size=LABEL_SIZE, color=DIM, font=SANS,
        )

        p3 = MathTex(
            r"\vec{a} \cdot \vec{a} = |\vec{a}|^2",
            font_size=BODY_SIZE, color=ACCENT,
        )
        p3_label = Text(
            "Self-dot = magnitude squared", font_size=LABEL_SIZE, color=DIM, font=SANS,
        )

        p4 = MathTex(
            r"\vec{a} \cdot \vec{b} = 0 "
            r"\iff \vec{a} \perp \vec{b}",
            font_size=BODY_SIZE, color=RED,
        )
        p4_label = Text(
            "Orthogonality test", font_size=LABEL_SIZE, color=DIM, font=SANS,
        )

        # Pair formula + label for each property
        items = [
            VGroup(p1, p1_label).arrange(DOWN, buff=0.1),
            VGroup(p2, p2_label).arrange(DOWN, buff=0.1),
            VGroup(p3, p3_label).arrange(DOWN, buff=0.1),
            VGroup(p4, p4_label).arrange(DOWN, buff=0.1),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 6: Worked Example (Work = Force · Displacement) ──────
    def scene6_worked_example(self):
        self.add_subcaption(
            "A classic application of the dot product is computing work in physics. "
            "Work equals force dot displacement. "
            "If we push with force three comma four comma zero "
            "along a displacement of ten comma zero comma zero, "
            "the work is three times ten plus four times zero plus zero times zero, "
            "which equals thirty Joules. Only the x-component of force contributes.",
            duration=28,
        )

        self.ly.section_divider(5, "Worked Example")

        title = self.ly.title("Work = Force dot Displacement")

        setup_line = Text(
            "Work = Force times Displacement in the direction of motion",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        work_formula = MathTex(
            r"W = \vec{F} \cdot \vec{d}",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        ex1 = MathTex(
            r"\vec{F} = \langle 3, 4, 0 \rangle, \quad "
            r"\vec{d} = \langle 10, 0, 0 \rangle",
            font_size=BODY_SIZE, color=WHITE,
        )

        result = MathTex(
            r"W = 3(10) + 4(0) + 0(0) = 30 \text{ J}",
            font_size=BODY_SIZE, color=SECONDARY,
        )

        insight = Text(
            "Only the x-component of force contributes to work",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        items = [setup_line, work_formula, ex1, result, insight]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 7: Summary + Outro ───────────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "To summarize: the dot product combines two vectors into a scalar. "
            "Algebraically, you sum the products of corresponding components. "
            "Geometrically, it equals the product of magnitudes times cosine theta. "
            "It gives us projections, tests for orthogonality, and computes physical work. "
            "Next time, we will explore the Cross Product.",
            duration=25,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text(
                "Dot product: a . b = a1*b1 + a2*b2 + a3*b3",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Geometric: a . b = |a| |b| cos(theta)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Measures how much two vectors agree in direction",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Projection: shadow of one vector onto another",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Orthogonality: a . b = 0 means perpendicular",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(takeaways, start_from=title)
        self.wait(4.0)
        self.ly.clear()

        play_outro(self, "Cross Product", "Calculus III — Multivariable")


# ── Compile check ──────────────────────────────────────────────────
if __name__ == "__main__":
    import py_compile
    py_compile.compile(__file__, doraise=True)
    print(f"Compile OK: {__file__}")
