"""
Video 41: Vectors in 3D Space
Calculus III -- Multivariable Playlist -- Video 1 of 14

Covers: extending vectors from 2D to 3D, components with unit vectors i/j/k,
magnitude formula, direction and unit vectors, and vector operations in 3D.

Render draft:  manim -ql scripts/undergraduate/video-41-vectors-3d.py Video41_Vectors3D
Render final:  manim -qh scripts/undergraduate/video-41-vectors-3d.py Video41_Vectors3D
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


class Video41_Vectors3D(Scene):
    """Full video: Vectors in 3D Space."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_from_2d_to_3d()
        self.scene3_components()
        self.scene4_magnitude()
        self.scene5_direction()
        self.scene6_operations()
        self.scene7_summary()

    # ── Scene 1: Hook + Channel Intro ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "In Linear Algebra we studied vectors in R-n. "
            "Now we visualize them in three-dimensional space.",
            duration=10,
        )
        play_intro(self, "Vectors in 3D Space", "Calculus III — Multivariable")

        bridge = Text(
            "From Linear Algebra to 3D Geometry",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(bridge)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 2: From 2D to 3D ─────────────────────────────────────
    def scene2_from_2d_to_3d(self):
        self.add_subcaption(
            "You already know vectors in the plane. "
            "Now we add a third axis, the z-axis, pointing up. "
            "A point in 3D is located by an ordered triple x, y, z. "
            "A vector also has three components written in angle brackets.",
            duration=20,
        )

        self.ly.section_divider(1, "The Third Dimension")

        title = self.ly.title("From 2D to 3D")

        axes_desc = Text(
            "Three perpendicular axes: x, y, and z",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        point_desc = MathTex(
            r"P = (x,\, y,\, z)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        vec_desc = MathTex(
            r"\vec{v} = \langle v_1,\, v_2,\, v_3 \rangle",
            font_size=HEADING_SIZE, color=PRIMARY,
        )

        items = [axes_desc, point_desc, vec_desc]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 3: 3D Vector Components ───────────────────────────────
    def scene3_components(self):
        self.add_subcaption(
            "Every 3D vector decomposes along the axes "
            "using unit vectors i, j, and k. "
            "A vector v equals v-one times i plus v-two times j "
            "plus v-three times k.",
            duration=20,
        )

        self.ly.section_divider(2, "Vector Components in 3D")

        title = self.ly.title("Unit Vectors i, j, k")

        unit_vecs = VGroup(
            MathTex(r"\hat{i} = \langle 1,0,0 \rangle", font_size=BODY_SIZE).set_color(RED),
            MathTex(r"\hat{j} = \langle 0,1,0 \rangle", font_size=BODY_SIZE).set_color(SECONDARY),
            MathTex(r"\hat{k} = \langle 0,0,1 \rangle", font_size=BODY_SIZE).set_color(PRIMARY),
        ).arrange(RIGHT, buff=0.6)

        decomposition = MathTex(
            r"\vec{v} = v_1 \hat{i} + v_2 \hat{j} + v_3 \hat{k}",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        example = MathTex(
            r"\vec{v} = 3\hat{i} + 4\hat{j} + 5\hat{k} "
            r"= \langle 3, 4, 5 \rangle",
            font_size=BODY_SIZE, color=WHITE,
        )

        items = [unit_vecs, decomposition, example]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 4: Magnitude in 3D ────────────────────────────────────
    def scene4_magnitude(self):
        self.add_subcaption(
            "The length of a 3D vector extends the Pythagorean theorem. "
            "Square each component, sum them, and take the square root. "
            "For the vector three, four, five, "
            "the length is five times the square root of two.",
            duration=20,
        )

        self.ly.section_divider(3, "Magnitude")

        title = self.ly.title("Magnitude in 3D")

        mag_formula = MathTex(
            r"|\vec{v}| = \sqrt{v_1^2 + v_2^2 + v_3^2}",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        calc = MathTex(
            r"|\langle 3,4,5 \rangle| = \sqrt{9 + 16 + 25} "
            r"= \sqrt{50} = 5\sqrt{2}",
            font_size=BODY_SIZE, color=WHITE,
        )

        insight = Text(
            "Magnitude = distance from origin to tip",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        items = [mag_formula, calc, insight]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 5: Direction and Unit Vectors ─────────────────────────
    def scene5_direction(self):
        self.add_subcaption(
            "To specify direction without magnitude, we normalize. "
            "Divide the vector by its length to get a unit vector. "
            "Unit vectors are essential for projections and coordinate frames.",
            duration=20,
        )

        self.ly.section_divider(4, "Direction in Space")

        title = self.ly.title("Unit Vectors and Direction")

        unit_formula = MathTex(
            r"\hat{u} = \frac{\vec{v}}{|\vec{v}|}",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        example = MathTex(
            r"\hat{u} = \frac{\langle 3,4,5 \rangle}{5\sqrt{2}}",
            font_size=BODY_SIZE, color=WHITE,
        )

        use_case = Text(
            "Unit vectors encode pure direction (length = 1)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        items = [unit_formula, example, use_case]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 6: Vector Operations in 3D ───────────────────────────
    def scene6_operations(self):
        self.add_subcaption(
            "Vector addition and scalar multiplication work "
            "component-wise in 3D, just like in 2D. "
            "The parallelogram law and tip-to-tail addition still apply.",
            duration=20,
        )

        self.ly.section_divider(5, "Operations in 3D")

        title = self.ly.title("Addition and Scalar Multiplication")

        add_formula = MathTex(
            r"\langle 3,4,5 \rangle + \langle 1,2,3 \rangle "
            r"= \langle 4,6,8 \rangle",
            font_size=BODY_SIZE, color=WHITE,
        )

        scale_formula = MathTex(
            r"2 \cdot \langle 3,4,5 \rangle = \langle 6,8,10 \rangle",
            font_size=BODY_SIZE, color=WHITE,
        )

        geometric = Text(
            "Parallelogram law and tip-to-tail still apply",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        items = [add_formula, scale_formula, geometric]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Summary + Outro ───────────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "Today we covered 3D vectors with three components, "
            "the magnitude formula, unit vectors for direction, "
            "and component-wise operations. "
            "Next time: the Dot Product in 3D.",
            duration=15,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text(
                "3D vector: v = <v1, v2, v3> = v1*i + v2*j + v3*k",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Magnitude: |v| = sqrt(v1^2 + v2^2 + v3^2)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Unit vector: u = v / |v| (pure direction, length 1)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Operations: addition and scalar mult are component-wise",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Up next: the Dot Product in 3D",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(takeaways, start_from=title)
        self.wait(2.0)
        self.ly.clear()

        play_outro(self, "Dot Product", "Calculus III — Multivariable")


# ── Compile check ──────────────────────────────────────────────────
if __name__ == "__main__":
    import py_compile
    py_compile.compile(__file__, doraise=True)
    print(f"Compile OK: {__file__}")
