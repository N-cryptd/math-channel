"""
Video 43: Cross Product in 3D
Calculus III -- Multivariable Playlist -- Video 3 of 14

Covers: algebraic definition (determinant form), component formula,
geometric meaning (right-hand rule, area of parallelogram), properties
(anti-commutative, distributive), and a worked example (torque).

Render draft:  manim -ql scripts/undergraduate/video-43-cross-product.py Video43_CrossProduct
Render final:  manim -qh scripts/undergraduate/video-43-cross-product.py Video43_CrossProduct
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


class Video43_CrossProduct(Scene):
    """Full video: Cross Product in 3D."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_determinant_form()
        self.scene3_component_formula()
        self.scene4_geometric_meaning()
        self.scene5_properties()
        self.scene6_torque_example()
        self.scene7_summary()

    # ── Scene 1: Hook + Channel Intro ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "The dot product measures how much two vectors agree. "
            "But what if we want a vector that is perpendicular to both? "
            "That is the cross product, and it is everywhere in physics.",
            duration=13,
        )
        play_intro(self, "Cross Product in 3D", "Calculus III — Multivariable")

        bridge = Text(
            "How do we find a vector perpendicular to two given vectors?",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(bridge)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3.0)
        self.ly.clear()

    # ── Scene 2: Algebraic Definition — Determinant Form ────────────
    def scene2_determinant_form(self):
        self.add_subcaption(
            "The cross product takes two vectors and produces a new vector "
            "perpendicular to both. We compute it as the determinant of a three "
            "by three matrix with the unit vectors i, j, k in the first row, "
            "the components of a in the second, and the components of b in the third.",
            duration=24,
        )

        self.ly.section_divider(1, "The Determinant Definition")

        title = self.ly.title("Algebraic Definition")

        det_formula = MathTex(
            r"\vec{a} \times \vec{b} = \det",
            r"\begin{pmatrix} \hat{i} & \hat{j} & \hat{k} \\ "
            r"a_1 & a_2 & a_3 \\ "
            r"b_1 & b_2 & b_3 \end{pmatrix}",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        note = Text(
            "Result is a VECTOR (perpendicular to both inputs)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        contrast = Text(
            "Recall: dot product gives a scalar",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )

        items = [det_formula, note, contrast]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 3: Component Formula ──────────────────────────────────
    def scene3_component_formula(self):
        self.add_subcaption(
            "Expanding the determinant gives us the component formula. "
            "The x-component is a2*b3 minus a3*b2. "
            "The y-component is a3*b1 minus a1*b3. "
            "And the z-component is a1*b2 minus a2*b1.",
            duration=20,
        )

        self.ly.section_divider(2, "Component Formula")

        title = self.ly.title("Expanding the Determinant")

        components = MathTex(
            r"\vec{a} \times \vec{b} = \langle",
            r"a_2 b_3 - a_3 b_2,",
            r"a_3 b_1 - a_1 b_3,",
            r"a_1 b_2 - a_2 b_1",
            r"\rangle",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        example = MathTex(
            r"\langle 1,0,0 \rangle \times \langle 0,1,0 \rangle "
            r"= \langle 0,0,1 \rangle",
            font_size=BODY_SIZE, color=SECONDARY,
        )

        example_note = Text(
            "i-hat cross j-hat equals k-hat (unit vectors)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )

        items = [components, example, example_note]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 4: Geometric Meaning ─────────────────────────────────
    def scene4_geometric_meaning(self):
        self.add_subcaption(
            "The cross product vector points in a direction given by the "
            "right-hand rule. Point your index finger along a, curl your "
            "fingers toward b, and your thumb points in the direction of "
            "a cross b. The magnitude equals the area of the parallelogram "
            "spanned by the two vectors.",
            duration=28,
        )

        self.ly.section_divider(3, "Geometric Meaning")

        title = self.ly.title("Right-Hand Rule and Magnitude")

        mag_formula = MathTex(
            r"|\vec{a} \times \vec{b}| = |\vec{a}|\,|\vec{b}| \sin\theta",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        theta_note = MathTex(
            r"\theta = \text{angle between } \vec{a} \text{ and } \vec{b}",
            font_size=BODY_SIZE, color=DIM,
        )

        rhr = Text(
            "Direction: right-hand rule (thumb points along result)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        area = Text(
            "Magnitude = area of the parallelogram spanned by a and b",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        items = [mag_formula, theta_note, rhr, area]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 5: Properties ────────────────────────────────────────
    def scene5_properties(self):
        self.add_subcaption(
            "The cross product is anti-commutative: a cross b equals "
            "negative b cross a. It distributes over addition. "
            "The cross product of a vector with itself is the zero vector. "
            "And two parallel vectors have a zero cross product since "
            "sine of zero equals zero.",
            duration=26,
        )

        self.ly.section_divider(4, "Key Properties")

        title = self.ly.title("Properties")

        p1 = MathTex(
            r"\vec{a} \times \vec{b} = -\vec{b} \times \vec{a}",
            font_size=BODY_SIZE, color=WHITE,
        )
        p1_label = Text("Anti-commutative", font_size=LABEL_SIZE, color=DIM, font=SANS)

        p2 = MathTex(
            r"\vec{a} \times (\vec{b} + \vec{c}) "
            r"= \vec{a} \times \vec{b} + \vec{a} \times \vec{c}",
            font_size=BODY_SIZE, color=WHITE,
        )
        p2_label = Text("Distributive over addition", font_size=LABEL_SIZE, color=DIM, font=SANS)

        p3 = MathTex(
            r"\vec{a} \times \vec{a} = \vec{0}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        p3_label = Text("Self-cross = zero vector", font_size=LABEL_SIZE, color=DIM, font=SANS)

        p4 = MathTex(
            r"\vec{a} \parallel \vec{b} "
            r"\implies \vec{a} \times \vec{b} = \vec{0}",
            font_size=BODY_SIZE, color=RED,
        )
        p4_label = Text("Parallel vectors: sin(0) = 0", font_size=LABEL_SIZE, color=DIM, font=SANS)

        items = [
            VGroup(p1, p1_label).arrange(DOWN, buff=0.1),
            VGroup(p2, p2_label).arrange(DOWN, buff=0.1),
            VGroup(p3, p3_label).arrange(DOWN, buff=0.1),
            VGroup(p4, p4_label).arrange(DOWN, buff=0.1),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 6: Worked Example — Torque ───────────────────────────
    def scene6_torque_example(self):
        self.add_subcaption(
            "A classic application is torque in physics. "
            "If a force of two, three, zero acts at position one, zero, zero "
            "from the pivot, the torque equals r cross F. "
            "Computing: r cross F gives zero, zero, negative three. "
            "The magnitude of torque is three Newton-meters.",
            duration=22,
        )

        self.ly.section_divider(5, "Worked Example")

        title = self.ly.title("Torque = r cross F")

        setup_line = Text(
            "Torque measures the rotational effect of a force",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        torque_formula = MathTex(
            r"\vec{\tau} = \vec{r} \times \vec{F}",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        ex1 = MathTex(
            r"\vec{r} = \langle 1, 0, 0 \rangle, \quad "
            r"\vec{F} = \langle 0, 2, 3 \rangle",
            font_size=BODY_SIZE, color=WHITE,
        )

        result = MathTex(
            r"\vec{\tau} = \langle 0, -3, 2 \rangle, \quad "
            r"|\vec{\tau}| = \sqrt{13} \text{ N}\cdot\text{m}",
            font_size=BODY_SIZE, color=SECONDARY,
        )

        items = [setup_line, torque_formula, ex1, result]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4.0)
        self.ly.clear()

    # ── Scene 7: Summary + Outro ────────────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "To summarize: the cross product takes two vectors and returns "
            "a perpendicular vector. Its magnitude is the area of the "
            "parallelogram, and its direction follows the right-hand rule. "
            "Unlike the dot product, it is anti-commutative. "
            "In physics, it gives us torque and angular momentum. "
            "Next time, we will use cross products to define lines and planes.",
            duration=28,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text(
                "Cross product: a x b = determinant of [i,j,k; a; b]",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Result is a VECTOR perpendicular to both inputs",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "|a x b| = |a||b| sin(theta) = area of parallelogram",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Direction: right-hand rule; Anti-commutative: a x b = -b x a",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Physics applications: torque, angular momentum, magnetic force",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]

        self.ly.progressive_reveal(takeaways, start_from=title)
        self.wait(4.0)
        self.ly.clear()

        play_outro(self, "Lines and Planes in 3D", "Calculus III — Multivariable")


# ── Compile check ──────────────────────────────────────────────────
if __name__ == "__main__":
    import py_compile
    py_compile.compile(__file__, doraise=True)
    print(f"Compile OK: {__file__}")
