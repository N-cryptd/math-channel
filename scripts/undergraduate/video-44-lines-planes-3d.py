"""
Video 44: Lines and Planes in 3D
Calculus III -- Multivariable Playlist -- Video 4 of 14

Covers: lines in 3D (parametric, vector, symmetric forms), planes in 3D
(point-normal form, standard form), distance from point to plane,
and worked examples (line through two points, plane through three points).

Render draft:  manim -ql scripts/undergraduate/video-44-lines-planes-3d.py Video44_LinesAndPlanes3D
Render final:  manim -qh scripts/undergraduate/video-44-lines-planes-3d.py Video44_LinesAndPlanes3D
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


class Video44_LinesAndPlanes3D(Scene):
    """Full video: Lines and Planes in 3D."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_direction_vector()
        self.scene3_three_forms()
        self.scene4_line_example()
        self.scene5_point_normal_form()
        self.scene6_standard_and_distance()
        self.scene7_plane_example()
        self.scene8_summary()

    # ── Scene 1: Hook + Channel Intro ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "A line in 3D is not described by y equals m x plus b. "
            "We need more information, either a point and a direction, "
            "or two points. And a plane? That is defined by a point "
            "and a normal vector. Let us see how these equations work.",
            duration=15,
        )
        play_intro(self, "Lines and Planes in 3D", "Calculus III — Multivariable")

        bridge = Text(
            "How do we describe straight lines and flat surfaces in 3D space?",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(bridge)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3.0)
        self.ly.clear()

    # ── Scene 2: Lines — The Direction Vector ──────────────────────
    def scene2_direction_vector(self):
        self.add_subcaption(
            "Every line in 3D has a direction vector that tells us which "
            "way it points. Given a point on the line and a direction "
            "vector d, we can write the line in three equivalent forms: "
            "parametric, vector, and symmetric.",
            duration=16,
        )

        self.ly.section_divider(1, "Lines in 3D")

        title = self.ly.title("A Line Needs: Point + Direction")

        parametric = MathTex(
            r"x = x_0 + at, \quad y = y_0 + bt, \quad z = z_0 + ct",
            font_size=BODY_SIZE, color=ACCENT,
        )

        d_text = MathTex(
            r"\vec{d} = \langle a,\, b,\, c \rangle",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        d_label = Text(
            "Direction vector (parallel to the line)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )

        items = [parametric, VGroup(d_text, d_label).arrange(DOWN, buff=0.1)]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 3: Three Forms of a Line ─────────────────────────────
    def scene3_three_forms(self):
        self.add_subcaption(
            "The parametric form writes each coordinate as a function of "
            "the parameter t. The vector form combines them: r equals r0 "
            "plus t times d. The symmetric form eliminates t by setting "
            "each fraction equal to t. Each form is useful in different "
            "situations.",
            duration=20,
        )

        self.ly.section_divider(2, "Three Equivalent Forms")

        title = self.ly.title("Vector Form and Symmetric Form")

        vector_form = MathTex(
            r"\vec{r} = \vec{r}_0 + t\,\vec{d}",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        vector_expanded = MathTex(
            r"\langle x, y, z \rangle = \langle x_0, y_0, z_0 \rangle "
            r"+ t \langle a, b, c \rangle",
            font_size=BODY_SIZE, color=WHITE,
        )

        symmetric = MathTex(
            r"\frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        sym_note = Text(
            "If a, b, or c = 0, use the parametric form instead",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )

        items = [vector_form, vector_expanded, symmetric, sym_note]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 4: Worked Example — Line Through Two Points ──────────
    def scene4_line_example(self):
        self.add_subcaption(
            "Find the line through the points (1, 2, 3) and (4, 5, 6). "
            "The direction vector is the difference: (3, 3, 3). "
            "So the parametric form is x equals 1 plus 3t, "
            "y equals 2 plus 3t, z equals 3 plus 3t.",
            duration=16,
        )

        self.ly.section_divider(3, "Worked Example: Line")

        title = self.ly.title("Line Through Two Points")

        points = MathTex(
            r"P_0 = (1, 2, 3), \quad P_1 = (4, 5, 6)",
            font_size=BODY_SIZE, color=WHITE,
        )

        direction = MathTex(
            r"\vec{d} = P_1 - P_0 = \langle 3, 3, 3 \rangle",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        result = MathTex(
            r"x = 1 + 3t, \quad y = 2 + 3t, \quad z = 3 + 3t",
            font_size=BODY_SIZE, color=SECONDARY,
        )

        items = [points, direction, result]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 5: Planes — Point-Normal Form ────────────────────────
    def scene5_point_normal_form(self):
        self.add_subcaption(
            "A plane in 3D is determined by a point on it and a normal "
            "vector perpendicular to it. The equation comes from the dot "
            "product: n dot the vector r minus r0 equals zero. "
            "If the normal is (a, b, c) and the point is (x0, y0, z0), "
            "we get a times x minus x0 plus b times y minus y0 "
            "plus c times z minus z0 equals zero.",
            duration=24,
        )

        self.ly.section_divider(4, "Planes in 3D")

        title = self.ly.title("A Plane Needs: Point + Normal Vector")

        dot_derivation = MathTex(
            r"\vec{n} \cdot (\vec{r} - \vec{r}_0) = 0",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        point_normal = MathTex(
            r"a(x - x_0) + b(y - y_0) + c(z - z_0) = 0",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        normal_def = MathTex(
            r"\vec{n} = \langle a, b, c \rangle",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        normal_label = Text(
            "Normal vector (perpendicular to the plane)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )

        items = [
            dot_derivation, point_normal,
            VGroup(normal_def, normal_label).arrange(DOWN, buff=0.1),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 6: Standard Form and Distance ─────────────────────────
    def scene6_standard_and_distance(self):
        self.add_subcaption(
            "Expanding the point-normal form gives the standard equation "
            "of a plane: ax plus by plus cz equals d, where d equals "
            "ax0 plus by0 plus cz0. To find the distance from a point "
            "to a plane, plug it into the formula.",
            duration=16,
        )

        self.ly.section_divider(5, "Standard Form and Distance")

        title = self.ly.title("Standard Form of a Plane")

        standard = MathTex(
            r"ax + by + cz = d",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        d_def = MathTex(
            r"d = ax_0 + by_0 + cz_0",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        distance = MathTex(
            r"\text{dist} = \frac{|ax_1 + by_1 + cz_1 - d|}"
            r"{\sqrt{a^2 + b^2 + c^2}}",
            font_size=BODY_SIZE, color=SECONDARY,
        )

        dist_label = Text(
            "Distance from point (x1, y1, z1) to the plane",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )

        items = [standard, d_def, distance, dist_label]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 7: Worked Example — Plane Through Three Points ───────
    def scene7_plane_example(self):
        self.add_subcaption(
            "Find the plane through (1, 0, 0), (0, 1, 0), and (0, 0, 1). "
            "Two direction vectors in the plane are v1 and v2. "
            "Their cross product gives the normal: n equals (1, 1, 1). "
            "The plane equation is x plus y plus z equals 1.",
            duration=16,
        )

        self.ly.section_divider(6, "Worked Example: Plane")

        title = self.ly.title("Plane Through Three Points")

        pts = MathTex(
            r"P_0(1,0,0),\; P_1(0,1,0),\; P_2(0,0,1)",
            font_size=BODY_SIZE, color=WHITE,
        )

        cross_calc = MathTex(
            r"\vec{v}_1 \times \vec{v}_2 "
            r"= \langle -1,1,0 \rangle \times \langle -1,0,1 \rangle "
            r"= \langle 1, 1, 1 \rangle",
            font_size=BODY_SIZE, color=PRIMARY,
        )

        result = MathTex(
            r"x + y + z = 1",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        items = [pts, cross_calc, result]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 8: Summary + Outro ────────────────────────────────────
    def scene8_summary(self):
        self.add_subcaption(
            "To recap: lines in 3D need a point and direction, with "
            "three equivalent equation forms. Planes need a point and a "
            "normal vector. The dot product is the key tool for finding "
            "plane equations, and the cross product lets us compute "
            "normals from points on the plane. Next up, vector-valued "
            "functions that trace out curves in 3D space.",
            duration=25,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text(
                "Line = point + direction vector d = (a, b, c)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Three forms: parametric, vector (r = r0 + td), symmetric",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Plane = point + normal vector n = (a, b, c)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Standard form: ax + by + cz = d (from dot product)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Use cross product to find normals from points on the plane",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(takeaways, start_from=title)
        self.wait(4.0)
        self.ly.clear()

        play_outro(self, "Vector-Valued Functions", "Calculus III — Multivariable")


# ── Compile check ──────────────────────────────────────────────────
if __name__ == "__main__":
    import py_compile
    py_compile.compile(__file__, doraise=True)
    print(f"Compile OK: {__file__}")
