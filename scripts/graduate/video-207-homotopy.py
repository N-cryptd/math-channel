"""
Video 207: Homotopy — Algebraic Topology
The concept of continuous deformation between paths and spaces.

QUALITY RULES:
1. Max 5 visible elements per scene
2. LayoutEngine for ALL positioning
3. Progressive disclosure
4. Raw strings with single backslashes for LaTeX
5. ly.clear() between scenes
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


class Video207_Homotopy(Scene):
    """Homotopy: continuous deformation of paths and spaces."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intuition()
        self.scene3_definition()
        self.scene4_path_homotopy()
        self.scene5_equivalence()
        self.scene6_examples()
        self.scene7_why_matters()

    def scene1_hook(self):
        """Hook — when are two shapes the same?"""
        self.add_subcaption(
            "Welcome to Algebraic Topology! Today we explore homotopy, "
            "the idea of continuous deformation between shapes.",
            duration=6,
        )
        play_intro(self, "Homotopy", "Algebraic Topology")

        self.add_subcaption(
            "A fundamental question: when should we consider two shapes to be essentially the same?",
            duration=5,
        )
        title = self.ly.title("When Are Two Shapes the Same?")
        items = [
            Text("Topology studies the 'shape' of spaces", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Key idea: stretching and bending are allowed", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("But cutting, tearing, and gluing are forbidden", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    def scene2_intuition(self):
        """Intuitive examples of homotopy."""
        self.add_subcaption(
            "Imagine taking a square and continuously stretching it into a circle. "
            "No tearing, no gluing — just smooth deformation.",
            duration=6,
        )
        self.ly.section_divider(1, "Intuition")

        title = self.ly.title("The Idea of Continuous Deformation")

        # Square morphing into circle
        square = Square(side_length=2, color=PRIMARY, stroke_width=3)
        circle = Circle(radius=1.2, color=SECONDARY, stroke_width=3)
        square.move_to(LEFT * 2.5)
        circle.move_to(RIGHT * 2.5)

        self.ly.safe_place(square, LEFT, anchor=title, buff=0.8)
        self.ly.safe_place(circle, RIGHT, anchor=title, buff=0.8)

        self.play(Create(square), run_time=NORMAL)
        self.wait(0.3)
        self.play(Transform(square, circle), run_time=2.5)
        self.wait(0.3)

        self.ly.clear()

        self.add_subcaption(
            "This smooth transformation from one shape to another is called a homotopy. "
            "The Greek word 'homos' means same, and 'topos' means place.",
            duration=6,
        )
        title2 = self.ly.title("This is Homotopy")
        items = [
            Text("Continuous deformation", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("No cutting, no gluing, no tearing", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("From Greek: homos (same) + topos (place)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(0.5)
        self.ly.clear()

    def scene3_definition(self):
        """Formal definition of homotopy."""
        self.add_subcaption(
            "Formally, a homotopy is a continuous map H from X cross the unit interval into Y, "
            "that smoothly transforms one function into another.",
            duration=7,
        )
        self.ly.section_divider(2, "Formal Definition")

        title = self.ly.title("Formal Definition")
        self.wait(0.5)

        # Definition
        defn1 = MathTex(
            r"\text{A homotopy between } f, g : X \to Y",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(defn1, DOWN, anchor=title, buff=0.5)
        self.play(Write(defn1), run_time=NORMAL)

        defn2 = MathTex(
            r"H : X \times [0,1] \to Y",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_defn2 = self.ly.formula_box(defn2, color=PRIMARY)
        self.ly.safe_place(boxed_defn2, DOWN, anchor=defn1, buff=0.4)
        self.play(FadeIn(boxed_defn2), run_time=NORMAL)

        # Constraints
        self.add_subcaption(
            "The homotopy H at time zero gives function f, and at time one gives function g. "
            "For every point x in X, the path H of x, t connects f of x to g of x.",
            duration=6,
        )
        constraints = VGroup(
            MathTex(r"H(x, 0) = f(x)", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"H(x, 1) = g(x)", font_size=BODY_SIZE, color=SECONDARY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        self.ly.safe_place(constraints, DOWN, anchor=defn2, buff=0.5)
        self.play(FadeIn(constraints, shift=LEFT * 0.15), run_time=NORMAL)

        # Visual: parameter t
        self.add_subcaption(
            "Think of t as a time parameter. At each moment, H gives an intermediate "
            "shape between f and g.",
            duration=5,
        )
        t_visual = MathTex(
            r"t = 0 \Rightarrow f, \quad t = 1 \Rightarrow g, \quad t \in [0,1]",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(t_visual, DOWN, anchor=constraints, buff=0.5)
        self.play(Write(t_visual), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

    def scene4_path_homotopy(self):
        """Path homotopy — homotopy between two paths."""
        self.add_subcaption(
            "Now consider a special case. What if f and g are both paths "
            "from point a to point b? A path homotopy keeps the endpoints fixed.",
            duration=7,
        )
        self.ly.section_divider(3, "Path Homotopy")

        title = self.ly.title("Path Homotopy")

        # Two paths visual
        path_a = Dot(color=SECONDARY).move_to(LEFT * 3 + DOWN * 0.5)
        path_b = Dot(color=SECONDARY).move_to(RIGHT * 3 + DOWN * 0.5)
        labels_a = MathTex(r"a", font_size=LABEL_SIZE, color=SECONDARY).next_to(path_a, DOWN, buff=0.15)
        labels_b = MathTex(r"b", font_size=LABEL_SIZE, color=SECONDARY).next_to(path_b, DOWN, buff=0.15)

        path_f = ArcBetweenPoints(
            path_a.get_center(), path_b.get_center(),
            angle=-0.5, color=PRIMARY, stroke_width=3,
        )
        path_g = ArcBetweenPoints(
            path_a.get_center(), path_b.get_center(),
            angle=0.5, color=RED, stroke_width=3,
        )

        labels_f = MathTex(r"\gamma", font_size=LABEL_SIZE, color=PRIMARY).next_to(path_f, UP, buff=0.15)
        labels_g = MathTex(r"\sigma", font_size=LABEL_SIZE, color=RED).next_to(path_g, UP, buff=0.15)

        group = VGroup(path_a, path_b, labels_a, labels_b, path_f, path_g, labels_f, labels_g)
        self.ly.safe_place(group, DOWN, anchor=title, buff=0.6)

        self.play(
            FadeIn(path_a), FadeIn(path_b),
            FadeIn(labels_a), FadeIn(labels_b),
            Create(path_f), Create(path_g),
            FadeIn(labels_f), FadeIn(labels_g),
            run_time=NORMAL,
        )

        # Deformation animation
        self.add_subcaption(
            "Watch as one path smoothly deforms into the other while both endpoints stay fixed.",
            duration=5,
        )
        self.play(
            Transform(path_f, path_g),
            run_time=2.0,
        )
        self.play(FadeOut(path_f), FadeOut(labels_f))

        self.ly.clear()

        # Definition of path homotopy
        self.add_subcaption(
            "A path homotopy H satisfies H of zero, t equals a and H of one, t equals b "
            "for all t in the interval. We write gamma is path homotopic to sigma.",
            duration=7,
        )
        title2 = self.ly.title("Path Homotopy Definition")
        self.wait(0.3)

        ph_defn = MathTex(
            r"H : [0,1] \times [0,1] \to Y",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ph_defn, DOWN, anchor=title2, buff=0.5)
        self.play(Write(ph_defn), run_time=NORMAL)

        ph_constraints = VGroup(
            MathTex(r"H(0, t) = a, \quad H(1, t) = b", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"H(s, 0) = \gamma(s), \quad H(s, 1) = \sigma(s)", font_size=BODY_SIZE, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        self.ly.safe_place(ph_constraints, DOWN, anchor=ph_defn, buff=0.5)
        self.play(FadeIn(ph_constraints, shift=LEFT * 0.15), run_time=NORMAL)

        notation = MathTex(
            r"\gamma \simeq \sigma \quad \text{(path homotopic)}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(notation, DOWN, anchor=ph_constraints, buff=0.5)
        self.play(Write(notation), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

    def scene5_equivalence(self):
        """Homotopy equivalence of spaces."""
        self.add_subcaption(
            "We can extend this idea to whole spaces. Two spaces X and Y are "
            "homotopy equivalent if there exist maps between them that compose "
            "to something homotopic to the identity.",
            duration=8,
        )
        self.ly.section_divider(4, "Homotopy Equivalence")

        title = self.ly.title("Homotopy Equivalence")

        self.add_subcaption(
            "X and Y are homotopy equivalent, written X tilde equals Y, if there exist "
            "continuous maps f from X to Y and g from Y to X, such that g composed with f "
            "is homotopic to the identity on X, and f composed with g is homotopic to the identity on Y.",
            duration=10,
        )
        defn = MathTex(
            r"X \simeq Y \iff \exists\, f : X \to Y,\, g : Y \to X",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(defn, DOWN, anchor=title, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)

        constraints = VGroup(
            MathTex(r"g \circ f \simeq \text{id}_X", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"f \circ g \simeq \text{id}_Y", font_size=BODY_SIZE, color=PRIMARY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        self.ly.safe_place(constraints, DOWN, anchor=defn, buff=0.5)
        self.play(FadeIn(constraints, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.3)
        self.ly.clear()

        # Examples
        self.add_subcaption(
            "Classic examples: a circle is homotopy equivalent to a punctured plane. "
            "The open interval from 0 to 1 is homotopy equivalent to the entire real line. "
            "A solid disk is homotopy equivalent to a single point.",
            duration=8,
        )
        title2 = self.ly.title("Examples")
        items = [
            MathTex(r"S^1 \simeq \mathbb{R}^2 \setminus \{0\}", font_size=BODY_SIZE, color=PRIMARY),
            Text("(punctured plane retracts to a circle)", font_size=LABEL_SIZE, color=DIM, font=SANS),
            MathTex(r"(0, 1) \simeq \mathbb{R}", font_size=BODY_SIZE, color=SECONDARY),
            Text("(open interval retracts to whole line)", font_size=LABEL_SIZE, color=DIM, font=SANS),
            MathTex(r"D^2 \simeq \{*\}", font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(0.5)
        self.ly.clear()

    def scene6_examples(self):
        """Examples and counterexamples."""
        self.add_subcaption(
            "Here's a visual example. A solid disk can be continuously shrunk to a point, "
            "so the disk is homotopy equivalent to a point. We call such a space contractible.",
            duration=8,
        )
        self.ly.section_divider(5, "Examples and Counterexamples")

        title = self.ly.title("Contractible Spaces")

        # Disk shrinking to point
        disk = Circle(radius=1.5, color=PRIMARY, stroke_width=3, fill_opacity=0.15)
        dot = Dot(color=ACCENT, radius=0.08)
        disk.move_to(LEFT * 2.5)
        dot.move_to(RIGHT * 2.5)

        self.ly.safe_place(disk, LEFT, anchor=title, buff=0.8)
        self.ly.safe_place(dot, RIGHT, anchor=title, buff=0.8)

        self.play(Create(disk), run_time=FAST)
        self.play(Transform(disk, dot.copy().move_to(LEFT * 2.5)), run_time=2.0)
        self.wait(0.3)

        contractible = Text(
            "A space that deformation retracts to a point is contractible",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(contractible, DOWN, anchor=title, buff=0.8)
        self.play(FadeIn(contractible, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.ly.clear()

        # Counterexample
        self.add_subcaption(
            "But not all spaces are homotopy equivalent! A circle and a sphere "
            "are fundamentally different. You cannot continuously deform one into the other. "
            "The hole in the circle cannot be removed without tearing.",
            duration=9,
        )
        title2 = self.ly.title("Not All Spaces Are Equivalent")

        s1 = Circle(radius=1.0, color=PRIMARY, stroke_width=3)
        s2 = Circle(radius=1.0, color=SECONDARY, stroke_width=3)
        s2_label = Text("S\u00B2", font_size=LABEL_SIZE, color=SECONDARY, font=MONO)
        s1.move_to(LEFT * 2.5)
        s2.move_to(RIGHT * 2.5)
        s1_label = MathTex(r"S^1", font_size=LABEL_SIZE, color=PRIMARY).next_to(s1, DOWN, buff=0.2)
        s2_label.next_to(s2, DOWN, buff=0.2)

        self.ly.safe_place(s1, LEFT, anchor=title2, buff=0.8)
        self.ly.safe_place(s2, RIGHT, anchor=title2, buff=0.8)

        self.play(Create(s1), Create(s2), run_time=FAST)
        self.play(Write(s1_label), FadeIn(s2_label), run_time=FAST)
        self.wait(0.3)

        # Remove circles before adding formula to respect content budget
        self.play(FadeOut(s1), FadeOut(s2), FadeOut(s1_label), FadeOut(s2_label), run_time=FAST)

        not_equiv = MathTex(
            r"S^1 \not\simeq S^2",
            font_size=HEADING_SIZE, color=RED,
        )
        boxed_ne = self.ly.formula_box(not_equiv, color=RED)
        self.ly.safe_place(boxed_ne, DOWN, anchor=title2, buff=0.8)
        self.play(FadeIn(boxed_ne), run_time=NORMAL)

        reason = Text(
            "Different homotopy groups (more in the next video!)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(reason, DOWN, anchor=boxed_ne, buff=0.5)
        self.play(FadeIn(reason, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

    def scene7_why_matters(self):
        """Summary and motivation for the playlist."""
        self.add_subcaption(
            "Homotopy is the foundational concept of algebraic topology. "
            "It gives us a precise way to say when two spaces have the same shape, "
            "up to continuous deformation.",
            duration=7,
        )
        self.ly.section_divider(6, "Why It Matters")

        title = self.ly.title("Why Homotopy Matters")
        items = [
            Text("Foundation of algebraic topology", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Classifies spaces by shape, not exact geometry", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Leads to homotopy groups, fundamental group", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Connects topology to algebra", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(0.5)
        self.ly.clear()

        # Summary formula box
        self.add_subcaption(
            "To summarize: a homotopy is a continuous deformation H from X cross I to Y. "
            "Two spaces are homotopy equivalent if maps between them compose to the identity, "
            "up to homotopy. This is our first algebraic invariant of topological spaces.",
            duration=9,
        )
        title2 = self.ly.title("Summary")
        summary = self.ly.formula_box(
            MathTex(
                r"H : X \times [0,1] \to Y, \quad "
                r"H(x,0)=f(x), \; H(x,1)=g(x)",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            color=PRIMARY,
        )
        self.ly.safe_place(summary, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(summary), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Outro
        self.add_subcaption(
            "In the next video, we will study the fundamental group, "
            "which captures the loops in a space up to homotopy. "
            "Thank you for watching!",
            duration=6,
        )
        play_outro(self, "The Fundamental Group", "Algebraic Topology")
