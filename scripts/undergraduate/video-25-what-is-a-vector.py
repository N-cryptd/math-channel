"""
Video 25: What is a Vector? (Geometric)
Linear Algebra Playlist — Video 1 of 16

Covers: geometric intuition for vectors, components, magnitude,
vector addition (tip-to-tail), and scalar multiplication.

Render draft:  manim -ql scripts/undergraduate/video-25-what-is-a-vector.py Video25_WhatIsAVector
Render final:  manim -qh scripts/undergraduate/video-25-what-is-a-vector.py Video25_WhatIsAVector
Preview still: manim -ql --format=png -s scripts/undergraduate/video-25-what-is-a-vector.py Video25_WhatIsAVector

v2 rewrite: setup_background, SANS font for body, progressive_reveal,
section_divider, formula_box, content budgets, no manual positioning.
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
from layout import LayoutEngine, ensure_fits, clamp_position


# ═══════════════════════════════════════════════════════════════════════
class Video25_WhatIsAVector(Scene):
    """Full video: 7 scenes on geometric vectors. v2 quality standards."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_geometric_view()
        self.scene3_components()
        self.scene3b_basis_vectors()
        self.scene4_magnitude()
        self.scene4b_formula()
        self.scene5_vector_addition()
        self.scene5b_result()
        self.scene6_scalar_multiplication()
        self.scene6b_insight()
        self.scene7_summary()

    # ── Scene 1: Hook + Intro ─────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Welcome to Linear Algebra. Today we answer a fundamental question: "
            "what exactly is a vector?",
            duration=8,
        )
        play_intro(self, "What is a Vector?", "Linear Algebra")

        self.add_subcaption(
            "Vectors show up everywhere: physics uses them for forces and velocity, "
            "computer graphics for positions, and data science for features.",
            duration=12,
        )

        contexts = [
            Text("Physics: Force, Velocity", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Graphics: Position, Color", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Data: Features, Embeddings", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(contexts, start_from=None,
                                   run_time=0.7, wait_time=0.8)
        self.ly.clear()

        # Key takeaway
        self.add_subcaption(
            "At their core, a vector is simply a quantity with both magnitude and direction.",
            duration=6,
        )
        key = Text(
            "Magnitude + Direction",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(key)
        self.play(Write(key), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 2: The Geometric View ───────────────────────────────────
    def scene2_geometric_view(self):
        self.ly.section_divider(1, "The Geometric View")

        self.add_subcaption(
            "Let's start with the most intuitive picture. "
            "On a number line, a vector is just a displacement from zero.",
            duration=10,
        )

        # Number line
        number_line = NumberLine(
            x_range=[-1, 5, 1], length=8,
            color=DIM, include_numbers=True,
        )
        self.ly.center_in_content(number_line)

        self.play(Create(number_line), run_time=NORMAL)
        self.wait(0.5)

        # Vector on number line
        vec_1d = Arrow(
            number_line.n2p(0), number_line.n2p(3),
            buff=0, stroke_width=4, color=ACCENT,
            max_tip_length_to_length_ratio=0.15,
        )
        label_1d = MathTex(r"3", font_size=BODY_SIZE, color=ACCENT)
        label_1d.next_to(vec_1d.get_end(), UP, buff=0.2)

        self.add_subcaption(
            "This arrow represents the number 3. "
            "It tells us: start at zero and move 3 units to the right.",
            duration=8,
        )
        self.play(GrowArrow(vec_1d), run_time=NORMAL)
        self.play(Write(label_1d), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    def scene2b_2d(self):
        """2D vector view (split from scene2 for budget compliance)."""
        # This is now handled inline in scene2 via the transition below
        pass

    def scene2c_2d_view(self):
        self.add_subcaption(
            "But in two dimensions, things get much more interesting. "
            "A vector is an arrow in the plane.",
            duration=10,
        )

        plane = NumberPlane(
            x_range=[-1, 5, 1], y_range=[-1, 5, 1],
            x_length=7, y_length=5,
            background_line_style={
                "stroke_color": "#3A3870",
                "stroke_width": 1,
            },
            axis_config={"color": DIM},
        )
        self.ly.center_in_content(plane)

        vec_2d = Arrow(
            plane.c2p(0, 0), plane.c2p(2, 3),
            buff=0, stroke_width=5, color=ACCENT,
            max_tip_length_to_length_ratio=0.12,
        )
        vec_label = MathTex(r"\vec{v}", font_size=HEADING_SIZE, color=ACCENT)
        vec_label.next_to(vec_2d.get_end(), UR, buff=0.15)

        self.play(Create(plane), run_time=NORMAL)
        self.play(GrowArrow(vec_2d), run_time=NORMAL)
        self.play(Write(vec_label), run_time=FAST)
        self.wait(1.0)

        # Concept — progressive reveal
        concept_items = [
            Text("A vector has magnitude (length)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("and direction (angle)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(concept_items, start_from=vec_2d,
                                   reveal_anim=FadeIn, run_time=0.7, wait_time=1.0)
        self.wait(1.5)
        self.ly.clear()

    # ── Scene 3: Components ───────────────────────────────────────────
    def scene3_components(self):
        self.ly.section_divider(2, "Components")

        self.add_subcaption(
            "To work with vectors mathematically, we describe them using components. "
            "Every vector can be broken down into an x-part and a y-part.",
            duration=15,
        )

        plane = NumberPlane(
            x_range=[-1, 5, 1], y_range=[-1, 5, 1],
            x_length=7, y_length=5,
            background_line_style={
                "stroke_color": "#3A3870",
                "stroke_width": 1,
            },
            axis_config={"color": DIM},
        )
        self.ly.center_in_content(plane)

        vec = Arrow(
            plane.c2p(0, 0), plane.c2p(2, 3),
            buff=0, stroke_width=5, color=ACCENT,
            max_tip_length_to_length_ratio=0.12,
        )

        self.play(Create(plane), GrowArrow(vec), run_time=NORMAL)

        # X-component
        x_comp = DashedLine(
            plane.c2p(0, 0), plane.c2p(2, 0),
            color=PRIMARY, stroke_width=3,
        )
        x_label = MathTex(r"2", font_size=LABEL_SIZE, color=PRIMARY)
        x_label.next_to(x_comp, DOWN, buff=0.15)

        self.add_subcaption(
            "The x-component is 2, the horizontal distance.",
            duration=6,
        )
        self.play(Create(x_comp), Write(x_label), run_time=NORMAL)
        self.wait(0.5)

        # Y-component
        y_comp = DashedLine(
            plane.c2p(2, 0), plane.c2p(2, 3),
            color=SECONDARY, stroke_width=3,
        )
        y_label = MathTex(r"3", font_size=LABEL_SIZE, color=SECONDARY)
        y_label.next_to(y_comp, RIGHT, buff=0.15)

        self.add_subcaption(
            "The y-component is 3, the vertical distance.",
            duration=6,
        )
        self.play(Create(y_comp), Write(y_label), run_time=NORMAL)
        self.wait(1.5)

        # Vector notation — remove old items first to stay in budget
        self.play(FadeOut(x_comp), FadeOut(x_label), FadeOut(y_comp), FadeOut(y_label),
                  run_time=0.3)

        vec_eq = MathTex(
            r"\vec{v} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_group = self.ly.formula_box(vec_eq, color=ACCENT)
        self.ly.center_in_content(formula_group)

        self.add_subcaption(
            "We write the vector as a column: v equals the column 2, 3.",
            duration=8,
        )
        self.play(Write(formula_group), run_time=SLOW)
        self.wait(2.0)
        self.ly.clear()

    def scene3b_basis_vectors(self):
        """Basis vectors as separate sub-scene for budget compliance."""
        self.add_subcaption(
            "Equivalently, v equals 2 times i-hat plus 3 times j-hat. "
            "I-hat is the unit vector along x. J-hat is the unit vector along y.",
            duration=14,
        )

        plane = NumberPlane(
            x_range=[-1, 4, 1], y_range=[-1, 4, 1],
            x_length=7, y_length=5,
            background_line_style={
                "stroke_color": "#3A3870",
                "stroke_width": 1,
            },
            axis_config={"color": DIM},
        )
        self.ly.center_in_content(plane)

        # Basis vectors
        i_hat = Arrow(
            plane.c2p(0, 0), plane.c2p(1, 0),
            buff=0, stroke_width=4, color=PRIMARY,
            max_tip_length_to_length_ratio=0.2,
        )
        i_label = MathTex(r"\hat{\imath}", font_size=LABEL_SIZE, color=PRIMARY)
        i_label.next_to(i_hat.get_end(), DOWN, buff=0.15)

        j_hat = Arrow(
            plane.c2p(0, 0), plane.c2p(0, 1),
            buff=0, stroke_width=4, color=SECONDARY,
            max_tip_length_to_length_ratio=0.2,
        )
        j_label = MathTex(r"\hat{\jmath}", font_size=LABEL_SIZE, color=SECONDARY)
        j_label.next_to(j_hat.get_end(), LEFT, buff=0.15)

        # Full vector
        vec = Arrow(
            plane.c2p(0, 0), plane.c2p(2, 3),
            buff=0, stroke_width=5, color=ACCENT,
            max_tip_length_to_length_ratio=0.12,
        )

        self.play(Create(plane), run_time=FAST)
        self.play(GrowArrow(i_hat), Write(i_label), run_time=NORMAL)
        self.play(GrowArrow(j_hat), Write(j_label), run_time=NORMAL)
        self.play(GrowArrow(vec), run_time=NORMAL)
        self.wait(1.5)

        # Equation
        eq = MathTex(
            r"\vec{v} = 2\hat{\imath} + 3\hat{\jmath}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_group = self.ly.formula_box(eq, color=ACCENT)
        formula_group.move_to(DOWN * 3)
        clamp_position(formula_group)

        self.play(Write(formula_group), run_time=SLOW)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 4: Magnitude ────────────────────────────────────────────
    def scene4_magnitude(self):
        self.ly.section_divider(3, "Magnitude")

        self.add_subcaption(
            "How long is a vector? The magnitude, or length, "
            "comes straight from the Pythagorean theorem.",
            duration=12,
        )

        plane = NumberPlane(
            x_range=[-1, 6, 1], y_range=[-1, 6, 1],
            x_length=6, y_length=5,
            background_line_style={
                "stroke_color": "#3A3870",
                "stroke_width": 1,
            },
            axis_config={"color": DIM},
        )
        self.ly.center_in_content(plane)

        # 3-4-5 vector
        vec = Arrow(
            plane.c2p(0, 0), plane.c2p(3, 4),
            buff=0, stroke_width=5, color=ACCENT,
            max_tip_length_to_length_ratio=0.12,
        )
        x_side = DashedLine(
            plane.c2p(0, 0), plane.c2p(3, 0),
            color=PRIMARY, stroke_width=3,
        )
        y_side = DashedLine(
            plane.c2p(3, 0), plane.c2p(3, 4),
            color=SECONDARY, stroke_width=3,
        )
        right_angle = RightAngle(
            x_side, y_side, length=0.3,
            color=DIM, stroke_width=2,
        )

        x_lbl = MathTex(r"3", font_size=BODY_SIZE, color=PRIMARY)
        x_lbl.next_to(x_side, DOWN, buff=0.15)
        y_lbl = MathTex(r"4", font_size=BODY_SIZE, color=SECONDARY)
        y_lbl.next_to(y_side, RIGHT, buff=0.15)

        self.play(Create(plane), run_time=FAST)
        self.play(GrowArrow(vec), run_time=NORMAL)
        self.play(
            Create(x_side), Create(y_side),
            Write(x_lbl), Write(y_lbl),
            Create(right_angle),
            run_time=NORMAL,
        )
        self.wait(1.5)
        self.ly.clear()

    def scene4b_formula(self):
        """Formula presentation in separate sub-scene."""
        self.add_subcaption(
            "The magnitude of v is the square root of x squared plus y squared. "
            "For our 3-4-5 triangle, that gives us exactly 5.",
            duration=12,
        )

        # Specific calculation
        specific = MathTex(
            r"|\vec{v}| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5",
            font_size=BODY_SIZE, color=WHITE,
        )
        specific_group = self.ly.formula_box(specific, color=PRIMARY)
        self.ly.center_in_content(specific_group)
        specific_group.shift(UP * 0.5)

        self.play(Write(specific_group), run_time=SLOW)
        self.wait(2.0)

        # General formula
        gen = MathTex(
            r"|\vec{v}| = \sqrt{x^2 + y^2}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        gen_group = self.ly.formula_box(gen, color=ACCENT)
        gen_group.move_to(DOWN * 1.2)
        clamp_position(gen_group)

        self.play(Write(gen_group), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 5: Vector Addition (Tip to Tail) ────────────────────────
    def scene5_vector_addition(self):
        self.ly.section_divider(4, "Vector Addition")

        self.add_subcaption(
            "How do we add two vectors? "
            "The rule is simple: tip to tail.",
            duration=8,
        )

        plane = NumberPlane(
            x_range=[-1, 6, 1], y_range=[-1, 6, 1],
            x_length=7, y_length=5,
            background_line_style={
                "stroke_color": "#3A3870",
                "stroke_width": 1,
            },
            axis_config={"color": DIM},
        )
        self.ly.center_in_content(plane)

        a_vec = Arrow(
            plane.c2p(0, 0), plane.c2p(2, 1),
            buff=0, stroke_width=4, color=PRIMARY,
            max_tip_length_to_length_ratio=0.15,
        )
        a_label = MathTex(r"\vec{a} = (2, 1)", font_size=LABEL_SIZE, color=PRIMARY)
        a_label.next_to(a_vec.get_end(), UR, buff=0.15)

        b_vec_orig = Arrow(
            plane.c2p(0, 0), plane.c2p(1, 3),
            buff=0, stroke_width=4, color=SECONDARY,
            max_tip_length_to_length_ratio=0.15,
        )
        b_label_orig = MathTex(r"\vec{b} = (1, 3)", font_size=LABEL_SIZE, color=SECONDARY)
        b_label_orig.next_to(b_vec_orig.get_end(), RIGHT, buff=0.15)

        self.play(Create(plane), GrowArrow(a_vec), Write(a_label), run_time=NORMAL)
        self.wait(0.5)
        self.play(GrowArrow(b_vec_orig), Write(b_label_orig), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()

    def scene5b_result(self):
        """Tip-to-tail animation + result in separate sub-scene."""
        self.add_subcaption(
            "Now we move vector b so its tail sits at the tip of vector a. "
            "Think of it like walking: first walk along a, then walk along b. "
            "Component-wise, we just add the x's and add the y's.",
            duration=16,
        )

        plane = NumberPlane(
            x_range=[-1, 6, 1], y_range=[-1, 6, 1],
            x_length=7, y_length=5,
            background_line_style={
                "stroke_color": "#3A3870",
                "stroke_width": 1,
            },
            axis_config={"color": DIM},
        )
        self.ly.center_in_content(plane)

        a_vec = Arrow(
            plane.c2p(0, 0), plane.c2p(2, 1),
            buff=0, stroke_width=4, color=PRIMARY,
            max_tip_length_to_length_ratio=0.15,
        )
        a_label = MathTex(r"\vec{a}", font_size=LABEL_SIZE, color=PRIMARY)
        a_label.next_to(a_vec.get_end(), UR, buff=0.15)

        b_vec_moved = Arrow(
            plane.c2p(2, 1), plane.c2p(3, 4),
            buff=0, stroke_width=4, color=SECONDARY,
            max_tip_length_to_length_ratio=0.15,
        )
        b_label_moved = MathTex(r"\vec{b}", font_size=LABEL_SIZE, color=SECONDARY)
        b_label_moved.next_to(b_vec_moved.get_end(), UR, buff=0.1)

        result_vec = Arrow(
            plane.c2p(0, 0), plane.c2p(3, 4),
            buff=0, stroke_width=5, color=ACCENT,
            max_tip_length_to_length_ratio=0.12,
        )
        result_label = MathTex(
            r"\vec{a} + \vec{b} = (3, 4)",
            font_size=LABEL_SIZE, color=ACCENT,
        )
        result_label.next_to(result_vec.get_end(), UR, buff=0.15)

        self.play(Create(plane), GrowArrow(a_vec), Write(a_label), run_time=FAST)
        self.play(GrowArrow(b_vec_moved), Write(b_label_moved), run_time=NORMAL)
        self.play(GrowArrow(result_vec), run_time=NORMAL)
        self.play(Write(result_label), run_time=NORMAL)
        self.wait(1.0)

        # Component formula
        self.play(FadeOut(a_vec), FadeOut(a_label), FadeOut(b_vec_moved),
                  FadeOut(b_label_moved), FadeOut(result_label), run_time=0.3)

        formula = MathTex(
            r"(2, 1) + (1, 3) = (2+1, \, 1+3) = (3, 4)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_group = self.ly.formula_box(formula, color=ACCENT)
        self.ly.center_in_content(formula_group)

        self.play(Write(formula_group), run_time=SLOW)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 6: Scalar Multiplication ────────────────────────────────
    def scene6_scalar_multiplication(self):
        self.ly.section_divider(5, "Scalar Multiplication")

        self.add_subcaption(
            "What happens when we multiply a vector by a plain number, "
            "called a scalar? It stretches or flips the vector.",
            duration=10,
        )

        plane = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-4, 4, 1],
            x_length=8, y_length=5,
            background_line_style={
                "stroke_color": "#3A3870",
                "stroke_width": 1,
            },
            axis_config={"color": DIM},
        )
        self.ly.center_in_content(plane)

        orig_vec = Arrow(
            plane.c2p(0, 0), plane.c2p(2, 1),
            buff=0, stroke_width=4, color=ACCENT,
            max_tip_length_to_length_ratio=0.15,
        )
        orig_label = MathTex(r"\vec{v} = (2, 1)", font_size=LABEL_SIZE, color=ACCENT)
        orig_label.next_to(orig_vec.get_end(), UR, buff=0.15)

        self.play(Create(plane), GrowArrow(orig_vec), Write(orig_label), run_time=NORMAL)
        self.wait(0.5)

        # Scale by 2
        vec_2 = Arrow(
            plane.c2p(0, 0), plane.c2p(4, 2),
            buff=0, stroke_width=4, color=WHITE,
            max_tip_length_to_length_ratio=0.12,
        )
        label_2 = MathTex(r"2\vec{v} = (4, 2)", font_size=LABEL_SIZE, color=WHITE)
        label_2.next_to(vec_2.get_end(), UR, buff=0.1)

        self.add_subcaption(
            "Multiply by 2: the vector stretches to twice its length, "
            "same direction. Each component gets doubled.",
            duration=8,
        )
        self.play(GrowArrow(vec_2), Write(label_2), run_time=NORMAL)
        self.wait(1.0)

        # Scale by -1
        vec_neg = Arrow(
            plane.c2p(0, 0), plane.c2p(-2, -1),
            buff=0, stroke_width=4, color=RED,
            max_tip_length_to_length_ratio=0.15,
        )
        label_neg = MathTex(
            r"-\vec{v} = (-2, -1)", font_size=LABEL_SIZE, color=RED,
        )
        label_neg.next_to(vec_neg.get_end(), DL, buff=0.1)

        self.add_subcaption(
            "Multiply by negative 1: the vector flips to point the opposite way. "
            "Same length, opposite direction.",
            duration=8,
        )
        self.play(GrowArrow(vec_neg), Write(label_neg), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    def scene6b_insight(self):
        """Key insight as separate sub-scene."""
        self.add_subcaption(
            "All scalar multiples of a vector lie on the same line through the origin. "
            "This is a crucial insight that we will build on throughout linear algebra.",
            duration=12,
        )

        insight_items = [
            Text("Scalar multiplication changes magnitude", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("and possibly direction", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("but stays on the SAME LINE", font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD),
            Text("through the origin", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(insight_items, run_time=0.7, wait_time=1.0)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Summary + Outro ──────────────────────────────────────
    def scene7_summary(self):
        self.ly.section_divider("", "Key Takeaways")

        self.add_subcaption(
            "Let's recap what we've learned about vectors.",
            duration=5,
        )

        bullets = [
            Text("1. A vector has magnitude and direction", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. Components: v = (x, y)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("3. |v| = sqrt(x^2 + y^2)", font_size=BODY_SIZE, color=WHITE, font=MONO),
            Text("4. Addition: tip-to-tail, component-wise", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5. Scalar mult: stretches / flips, same line", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(bullets, run_time=0.7, wait_time=0.6)
        self.wait(1.0)

        self.ly.clear()

        # Teaser for next video
        self.add_subcaption(
            "But what if we combine scalars and vectors freely? "
            "What set of points can we reach? That is the span, "
            "and it is the topic of our next video.",
            duration=10,
        )

        teaser = Text(
            "Next: What happens when we combine scalars and vectors freely?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(teaser)
        self.play(FadeIn(teaser, shift=UP * 0.3), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear(run_time=0.3)

        # Outro
        play_outro(self, "Linear Combinations and Span", "Linear Algebra")
