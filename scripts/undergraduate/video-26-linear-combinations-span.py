"""
Video 26: Linear Combinations and Span
Linear Algebra Playlist — Video 2 of 16

Covers: linear combinations, span of vectors, linear dependence vs independence,
three-case taxonomy (point, line, plane), 3D preview.

Render draft:  manim -ql scripts/undergraduate/video-26-linear-combinations-span.py Video26_LinearCombinationsSpan
Render final:  manim -qh scripts/undergraduate/video-26-linear-combinations-span.py Video26_LinearCombinationsSpan

v2 rewrite: setup_background, SANS font, progressive_reveal, section_divider,
formula_box, split crowded scenes, content budgets, LayoutEngine v2.
"""

from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits, clamp_position


def make_grid_plane(x_range=(-4, 5, 1), y_range=(-3, 4, 1),
                    x_length=8, y_length=6, shift_vec=ORIGIN):
    """Create a styled NumberPlane consistent with channel branding."""
    plane = NumberPlane(
        x_range=x_range, y_range=y_range,
        x_length=x_length, y_length=y_length,
        background_line_style={
            "stroke_color": "#3A3870",
            "stroke_width": 1,
        },
        axis_config={"color": DIM},
    ).shift(shift_vec)
    return plane


# ═══════════════════════════════════════════════════════════════════════
class Video26_LinearCombinationsSpan(Scene):
    """Full video: 7+ scenes on linear combinations and span. v2 quality."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene2b_example()
        self.scene3_definition_span()
        self.scene3b_span_plane()
        self.scene4_span_line()
        self.scene4b_conclusion()
        self.scene5_three_cases()
        self.scene5b_bridge()
        self.scene6_3d_preview()
        self.scene6b_labels()
        self.scene7_summary()

    # ── Scene 1: Hook + Intro ─────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Welcome back to Linear Algebra. Last time we learned about vectors. "
            "We learned how to add them and scale them. But what if we do both at once?",
            duration=12,
        )
        play_intro(self, "Linear Combinations and Span", "Linear Algebra")

        self.add_subcaption(
            "That is the key question: given a set of vectors, "
            "what set of points can we reach by adding scaled copies of them?",
            duration=10,
        )

        recap_items = [
            Text("Last time: Addition (tip to tail)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Last time: Scaling (stretch or flip)", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(recap_items, run_time=0.7, wait_time=0.8)

        self.ly.clear()

        question = Text(
            "This time: Combine BOTH — What can we reach?",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(question)
        self.play(Write(question), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 2: What is a Linear Combination? ────────────────────────
    def scene2_definition(self):
        self.ly.section_divider(1, "Linear Combinations")

        self.add_subcaption(
            "A linear combination is when you scale each vector by some number "
            "and then add the results. For two vectors a and b, "
            "a linear combination looks like c one times a plus c two times b.",
            duration=15,
        )

        plane = make_grid_plane(shift_vec=LEFT * 2.5)

        a_vec = Arrow(
            plane.c2p(0, 0), plane.c2p(2, 1),
            buff=0, stroke_width=4, color=PRIMARY,
            max_tip_length_to_length_ratio=0.15,
        )
        a_label = MathTex(r"\vec{a}", font_size=HEADING_SIZE, color=PRIMARY)
        a_label.next_to(a_vec.get_end(), UR, buff=0.1)

        b_vec = Arrow(
            plane.c2p(0, 0), plane.c2p(-1, 2),
            buff=0, stroke_width=4, color=SECONDARY,
            max_tip_length_to_length_ratio=0.15,
        )
        b_label = MathTex(r"\vec{b}", font_size=HEADING_SIZE, color=SECONDARY)
        b_label.next_to(b_vec.get_end(), UL, buff=0.1)

        self.play(Create(plane), run_time=FAST)
        self.play(GrowArrow(a_vec), Write(a_label), run_time=NORMAL)
        self.play(GrowArrow(b_vec), Write(b_label), run_time=NORMAL)
        self.wait(1.0)

        # Formula on the right
        formula = MathTex(
            r"c_1 \vec{a} + c_2 \vec{b}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_group = self.ly.formula_box(formula, color=ACCENT)
        formula_group.move_to(RIGHT * 3.5 + UP * 1.0)
        clamp_position(formula_group)

        self.play(Write(formula_group), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

    def scene2b_example(self):
        """Concrete example in separate sub-scene for budget."""
        self.add_subcaption(
            "Let's try a concrete example: 2 times a plus 1 times b. "
            "First we scale a by 2, then add b. The result is a new vector. "
            "Try different scalars: negative 1 times a plus 2 times b gives "
            "a completely different point.",
            duration=18,
        )

        plane = make_grid_plane(shift_vec=LEFT * 2.5)

        a_vec = Arrow(
            plane.c2p(0, 0), plane.c2p(2, 1),
            buff=0, stroke_width=4, color=PRIMARY,
            max_tip_length_to_length_ratio=0.15,
        )

        # 2a + b = (3, 4)
        result_vec = Arrow(
            plane.c2p(0, 0), plane.c2p(3, 4),
            buff=0, stroke_width=5, color=ACCENT,
            max_tip_length_to_length_ratio=0.12,
        )
        result_label = MathTex(
            r"2\vec{a} + \vec{b} = (3,4)", font_size=LABEL_SIZE, color=ACCENT,
        )
        result_label.next_to(result_vec.get_end(), UR, buff=0.1)

        self.play(Create(plane), GrowArrow(a_vec), run_time=FAST)
        self.play(GrowArrow(result_vec), Write(result_label), run_time=NORMAL)
        self.wait(1.0)

        # Second example
        result2_vec = Arrow(
            plane.c2p(0, 0), plane.c2p(-4, 3),
            buff=0, stroke_width=4, color=RED,
            max_tip_length_to_length_ratio=0.12,
        )
        result2_label = MathTex(
            r"-\vec{a} + 2\vec{b} = (-4,3)", font_size=LABEL_SIZE, color=RED,
        )
        result2_label.next_to(result2_vec.get_end(), UL, buff=0.1)

        self.play(GrowArrow(result2_vec), Write(result2_label), run_time=NORMAL)
        self.wait(1.5)

        # Column computation on right
        self.play(FadeOut(result_label), FadeOut(result2_label), run_time=0.3)
        calc = MathTex(
            r"2\begin{pmatrix}2\\1\end{pmatrix}"
            r"+\begin{pmatrix}-1\\2\end{pmatrix}"
            r"=\begin{pmatrix}3\\4\end{pmatrix}",
            font_size=LABEL_SIZE, color=WHITE,
        )
        calc_group = self.ly.formula_box(calc, color=PRIMARY)
        calc_group.move_to(RIGHT * 3.0 + UP * 0.5)
        clamp_position(calc_group)

        self.play(Write(calc_group), run_time=SLOW)
        self.wait(2.0)

        # Key question
        q_text = Text(
            "What if we try ALL possible scalars?",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        q_text.move_to(DOWN * 2.5)
        self.play(Write(q_text), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 3: The Span — Definition ─────────────────────────────────
    def scene3_definition_span(self):
        self.ly.section_divider(2, "The Span")

        self.add_subcaption(
            "The span of a set of vectors is the collection of ALL possible "
            "linear combinations. Every point you can reach by choosing some "
            "scalars is in the span.",
            duration=12,
        )

        title = self.ly.title("Definition: Span", color=PRIMARY)

        definition = MathTex(
            r"\text{span}(\vec{a}, \vec{b}) = "
            r"\{c_1 \vec{a} + c_2 \vec{b} \mid c_1, c_2 \in \mathbb{R}\}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(definition, direction=DOWN, anchor=title)
        self.play(Write(definition), run_time=SLOW)
        self.wait(2.0)
        self.ly.clear()

    def scene3b_span_plane(self):
        """Visual span animation — independent vectors span the plane."""
        self.add_subcaption(
            "Let's see this in action. Vector a and vector b are not parallel. "
            "Watch what happens as we vary the scalars through many values. "
            "When two vectors are not parallel, their span covers the entire plane.",
            duration=16,
        )

        plane = make_grid_plane(shift_vec=ORIGIN)

        a_vec = Arrow(
            plane.c2p(0, 0), plane.c2p(2, 1),
            buff=0, stroke_width=4, color=PRIMARY,
            max_tip_length_to_length_ratio=0.15,
        )
        b_vec = Arrow(
            plane.c2p(0, 0), plane.c2p(-1, 2),
            buff=0, stroke_width=4, color=SECONDARY,
            max_tip_length_to_length_ratio=0.15,
        )
        a_lbl = MathTex(r"\vec{a}", font_size=LABEL_SIZE, color=PRIMARY)
        a_lbl.next_to(a_vec.get_end(), UR, buff=0.1)
        b_lbl = MathTex(r"\vec{b}", font_size=LABEL_SIZE, color=SECONDARY)
        b_lbl.next_to(b_vec.get_end(), UL, buff=0.1)

        self.play(Create(plane), run_time=FAST)
        self.play(
            GrowArrow(a_vec), Write(a_lbl),
            GrowArrow(b_vec), Write(b_lbl),
            run_time=NORMAL,
        )

        # Generate span dots
        span_dots = VGroup()
        c1_vals = np.linspace(-3, 3, 13)
        c2_vals = np.linspace(-3, 3, 13)
        for c1 in c1_vals:
            for c2 in c2_vals:
                ex = c1 * 2 + c2 * (-1)
                ey = c1 * 1 + c2 * 2
                if abs(ex) < 6.5 and abs(ey) < 5:
                    pt = plane.c2p(ex, ey)
                    dot = Dot(pt, radius=0.035, color=ACCENT, fill_opacity=0.4)
                    span_dots.add(dot)

        self.play(
            LaggedStart(*[FadeIn(d, scale=0.5) for d in span_dots], lag_ratio=0.005),
            run_time=4.0,
        )
        self.wait(0.5)

        self.bring_to_front(a_vec, a_lbl, b_vec, b_lbl)

        # Reveal
        reveal = Text(
            "span(a, b) = the entire plane!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(reveal, direction=DOWN, anchor=plane, buff=0.3)

        self.play(Write(reveal), run_time=NORMAL)
        self.wait(2.5)
        self.ly.clear()

    # ── Scene 4: When Span is Just a Line ──────────────────────────────
    def scene4_span_line(self):
        self.ly.section_divider(3, "Dependent Vectors")

        self.add_subcaption(
            "But what if our two vectors point in the same direction? "
            "For example, a equals the vector 1, 2, and b equals 2, 4. "
            "Notice that b is exactly 2 times a. "
            "Vector b is just a scalar multiple of a. These vectors are "
            "linearly DEPENDENT. One is redundant.",
            duration=18,
        )

        plane = make_grid_plane(shift_vec=LEFT * 2.5)

        a_vec = Arrow(
            plane.c2p(0, 0), plane.c2p(1, 2),
            buff=0, stroke_width=4, color=PRIMARY,
            max_tip_length_to_length_ratio=0.18,
        )
        b_vec = Arrow(
            plane.c2p(0, 0), plane.c2p(2, 4),
            buff=0, stroke_width=4, color=SECONDARY,
            max_tip_length_to_length_ratio=0.12,
        )
        a_lbl = MathTex(r"\vec{a}=(1,2)", font_size=LABEL_SIZE, color=PRIMARY)
        a_lbl.next_to(a_vec, LEFT, buff=0.15)
        b_lbl = MathTex(r"\vec{b}=(2,4)", font_size=LABEL_SIZE, color=SECONDARY)
        b_lbl.next_to(b_vec.get_end(), RIGHT, buff=0.15)

        self.play(Create(plane), run_time=FAST)
        self.play(GrowArrow(a_vec), Write(a_lbl), run_time=NORMAL)
        self.play(GrowArrow(b_vec), Write(b_lbl), run_time=NORMAL)
        self.wait(0.5)

        # b = 2a relation
        relation = MathTex(
            r"\vec{b} = 2\vec{a}", font_size=HEADING_SIZE, color=RED,
        )
        relation.move_to(RIGHT * 3.5 + UP * 1.0)
        clamp_position(relation)
        self.play(Write(relation), run_time=NORMAL)
        self.wait(1.0)

        # Show span dots — all on the same line
        span_dots = VGroup()
        for c1 in np.linspace(-4, 4, 25):
            for c2 in np.linspace(-2, 2, 9):
                ex = c1 * 1 + c2 * 2
                ey = c1 * 2 + c2 * 4
                pt = plane.c2p(ex, ey)
                dot = Dot(pt, radius=0.04, color=RED, fill_opacity=0.5)
                span_dots.add(dot)

        self.play(
            LaggedStart(*[FadeIn(d, scale=0.5) for d in span_dots], lag_ratio=0.008),
            run_time=3.0,
        )
        self.wait(0.5)

        # Line through origin
        line_through = DashedLine(
            plane.c2p(-3, -6), plane.c2p(3, 6),
            color=RED, stroke_width=2,
        )
        self.add(line_through)
        self.bring_to_front(a_vec, a_lbl, b_vec, b_lbl)
        self.wait(1.5)
        self.ly.clear()

    def scene4b_conclusion(self):
        """Span conclusion for dependent vectors."""
        self.add_subcaption(
            "No matter what scalars we choose, the result always lands "
            "on the same line. The span collapses from a plane to a line. "
            "We say the vectors are linearly dependent.",
            duration=12,
        )

        reveal = Text(
            "span(a, b) = just a line!",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(reveal)
        self.play(Write(reveal), run_time=NORMAL)
        self.wait(2.5)
        self.ly.clear()

    # ── Scene 5: Three-Case Taxonomy ───────────────────────────────────
    def scene5_three_cases(self):
        self.ly.section_divider(4, "Three Cases of Span")

        self.add_subcaption(
            "Let's organize what we have found. The span can take exactly "
            "three forms, depending on the vectors we start with.",
            duration=10,
        )

        cases = [
            Text("1. span({0}) = {0}  — just the origin", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("2. span({v}) = a line  — all scalar multiples", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("3. span({a, b}) = the entire plane", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD),
            Text("   (if a and b are independent)", font_size=LABEL_SIZE, color=DIM, font=SANS),
            Text("3b. span({a, b}) = just a line", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("   (if a and b are dependent)", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(cases, run_time=0.6, wait_time=0.8)
        self.wait(2.0)
        self.ly.clear()

    def scene5b_bridge(self):
        """Bridge to Video 25 scalar multiplication concept."""
        self.add_subcaption(
            "This connects back to scalar multiplication: "
            "all multiples of one vector stay on the same line through the origin. "
            "Adding a second independent vector breaks us free into the plane.",
            duration=12,
        )

        bridge_items = [
            Text("From Video 25:", font_size=LABEL_SIZE, color=DIM, font=SANS),
            Text("Scalar multiples stay on one line", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("A second independent vector", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("breaks us into the plane", font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(bridge_items, run_time=0.7, wait_time=0.8)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 6: 3D Preview ──────────────────────────────────────────────
    def scene6_3d_preview(self):
        self.ly.section_divider(5, "Extending to 3D")

        self.add_subcaption(
            "Everything extends to 3D and beyond. "
            "In three dimensions, two independent vectors span a flat plane. "
            "Adding a third independent vector lets you reach all of 3D space.",
            duration=14,
        )

        # Stylized 3D axes
        origin = np.array([0, -0.5, 0])
        x_end = origin + np.array([3, -1.5, 0])
        y_end = origin + np.array([-1, -2, 0])
        z_end = origin + np.array([0.5, 3, 0])

        x_axis = Line(origin, x_end, color=PRIMARY, stroke_width=2)
        y_axis = Line(origin, y_end, color=SECONDARY, stroke_width=2)
        z_axis = Line(origin, z_end, color=ACCENT, stroke_width=2)

        x_lbl = Text("x", font_size=LABEL_SIZE, color=PRIMARY, font=MONO)
        x_lbl.next_to(x_end, RIGHT, buff=0.1)
        y_lbl = Text("y", font_size=LABEL_SIZE, color=SECONDARY, font=MONO)
        y_lbl.next_to(y_end, DOWN, buff=0.1)
        z_lbl = Text("z", font_size=LABEL_SIZE, color=ACCENT, font=MONO)
        z_lbl.next_to(z_end, UP, buff=0.1)

        self.play(
            Create(x_axis), Create(y_axis), Create(z_axis),
            Write(x_lbl), Write(y_lbl), Write(z_lbl),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Vectors
        v1_end = origin + np.array([2, -1, 0])
        v2_end = origin + np.array([-0.5, -1.5, 0])
        v3_end = origin + np.array([0.3, 2.5, 0])

        vec1 = Arrow(origin, v1_end, buff=0, stroke_width=4, color=PRIMARY,
                     max_tip_length_to_length_ratio=0.15)
        vec2 = Arrow(origin, v2_end, buff=0, stroke_width=4, color=SECONDARY,
                     max_tip_length_to_length_ratio=0.15)
        vec3 = Arrow(origin, v3_end, buff=0, stroke_width=4, color=ACCENT,
                     max_tip_length_to_length_ratio=0.15)

        self.play(Create(vec1), Create(vec2), run_time=NORMAL)
        self.wait(0.5)

        # Plane patch
        plane_poly = Polygon(
            origin, v1_end, v1_end + (v2_end - origin), v2_end,
            fill_color=PRIMARY, fill_opacity=0.2,
            stroke_color=PRIMARY, stroke_width=1,
        )

        self.add_subcaption(
            "Two vectors span a plane, a flat sheet in 3D space.",
            duration=8,
        )
        self.play(Create(plane_poly), run_time=SLOW)
        self.wait(1.0)

        self.add_subcaption(
            "Adding a third vector not on this plane "
            "lets us reach every point in 3D space.",
            duration=8,
        )
        self.play(Create(vec3), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    def scene6b_labels(self):
        """3D span labels and teaser — separate for budget."""
        items = [
            Text("span(v1, v2) = a plane", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("span(v1, v2, v3) = all of R3", font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD),
            Text("This pattern holds in any dimension.", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The answer: matrices.", font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(items, run_time=0.7, wait_time=1.0)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Summary + Outro ───────────────────────────────────────
    def scene7_summary(self):
        self.ly.section_divider("", "Key Takeaways")

        self.add_subcaption(
            "A linear combination scales and adds vectors. "
            "The span is the set of all possible linear combinations. "
            "It can be a point, a line, or a plane.",
            duration=12,
        )

        bullets = [
            Text("1. Linear combination: c1*v1 + c2*v2 + ...", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. Span = ALL possible linear combinations", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("3. Span: a point, a line, or a plane", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("4. Dependent vectors collapse the span", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("5. Independent vectors maximize the span", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(bullets, run_time=0.6, wait_time=0.5)
        self.wait(1.0)
        self.ly.clear()

        # Teaser
        self.add_subcaption(
            "Next time, we will see how matrices provide a systematic way "
            "to describe linear combinations and transformations.",
            duration=8,
        )

        teaser = Text(
            "Next: How do matrices encode these operations?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(teaser)
        self.play(FadeIn(teaser, shift=UP * 0.3), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear(run_time=0.3)

        # Outro
        play_outro(self, "Matrices as Transformations", "Linear Algebra")
