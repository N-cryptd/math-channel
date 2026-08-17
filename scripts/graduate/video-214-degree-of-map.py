"""
Video 214: Degree of a Map — Algebraic Topology
Degree of maps S^n to S^n, winding number, homotopy invariance,
Hopf degree theorem, applications.

QUALITY RULES:
1. Max 5 visible elements per scene
2. LayoutEngine for ALL positioning
3. Progressive disclosure
4. Raw strings with single backslashes for LaTeX
5. ly.clear() between scenes
6. One subcaption per scene, self.wait(5-8) after content
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


class Video214_DegreeOfAMap(Scene):
    """Degree of a Map: generalizing winding numbers."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_winding_number()
        self.scene4_homotopy_invariance()
        self.scene5_computing_degree()
        self.scene6_applications()
        self.scene7_summary()

    def scene1_hook(self):
        """Hook — how many times does a map wrap?"""
        self.add_subcaption(
            "Welcome back to Algebraic Topology! We have computed homology "
            "groups using the Mayer-Vietoris sequence. Today we study "
            "the degree of a continuous map, which generalizes the winding "
            "number from the circle to higher-dimensional spheres.",
            duration=20,
        )
        play_intro(self, "Degree of a Map", "Algebraic Topology")

        title = self.ly.title("How Many Times Does It Wrap?")
        items = [
            Text("Winding number: loops on S^1", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Degree: maps S^n to S^n", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Homotopy invariant and computable", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(8)
        self.ly.clear()

    def scene2_definition(self):
        """Formal definition of degree."""
        self.add_subcaption(
            "Let f be a continuous map from S^n to S^n. "
            "The induced map on the n-th homology group is a homomorphism "
            "from Z to Z. Since every homomorphism from Z to Z "
            "is multiplication by some integer, we call this integer "
            "the degree of f.",
            duration=22,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("Degree of a Map")

        defn = MathTex(
            r"f_* : H_n(S^n) \to H_n(S^n)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(defn, DOWN, anchor=title, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(3)

        degree = MathTex(
            r"f_*(1) = d \cdot 1 \implies \deg(f) = d \in \mathbb{Z}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed_degree = self.ly.formula_box(degree, color=SECONDARY)
        self.ly.safe_place(boxed_degree, DOWN, anchor=defn, buff=0.5)
        self.play(FadeIn(boxed_degree), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene3_winding_number(self):
        """Degree for n=1: the winding number."""
        self.add_subcaption(
            "For the circle, the degree is exactly the winding number "
            "we studied earlier. A map that wraps the circle k times "
            "counterclockwise has degree k. "
            "The identity map has degree one. "
            "The constant map has degree zero. "
            "The reflection map z maps to z-bar has degree minus one.",
            duration=24,
        )
        self.ly.section_divider(2, "Winding Number")

        title = self.ly.title("Degree on S^1 = Winding Number")

        examples = [
            MathTex(r"\deg(\text{id}_{S^1}) = 1", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"\deg(z \mapsto z^k) = k", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"\deg(z \mapsto \bar{z}) = -1", font_size=BODY_SIZE, color=RED),
        ]
        self.ly.progressive_reveal(examples, start_from=title)
        self.wait(5)
        self.ly.clear()

    def scene4_homotopy_invariance(self):
        """Homotopy invariance of the degree."""
        self.add_subcaption(
            "The degree is a homotopy invariant. If two maps are homotopic, "
            "they have the same degree. "
            "This is because homotopic maps induce the same homomorphism "
            "on homology. "
            "The converse is also true for spheres: two maps from S^n "
            "to S^n are homotopic if and only if they have the same degree. "
            "This is the Hopf degree theorem.",
            duration=26,
        )
        self.ly.section_divider(3, "Homotopy Invariance")

        title = self.ly.title("The Hopf Degree Theorem")

        theorem = MathTex(
            r"f \simeq g \iff \deg(f) = \deg(g) \quad \text{for } f, g : S^n \to S^n",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        boxed_thm = self.ly.formula_box(theorem, color=PRIMARY)
        self.ly.safe_place(boxed_thm, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_thm), run_time=NORMAL)
        self.wait(3)

        consequence = Text(
            "The degree classifies maps S^n to S^n up to homotopy",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(consequence, DOWN, anchor=boxed_thm, buff=0.5)
        self.play(FadeIn(consequence, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene5_computing_degree(self):
        """Computing the degree."""
        self.add_subcaption(
            "There are several ways to compute the degree. "
            "The differential counts preimage points with signs. "
            "A regular value y has preimages x_1 through x_k, "
            "each with a local degree of plus or minus one "
            "depending on whether f preserves or reverses orientation. "
            "The degree is the sum of these local degrees.",
            duration=24,
        )
        self.ly.section_divider(4, "Computing Degree")

        title = self.ly.title("The Differential Formula")

        formula = MathTex(
            r"\deg(f) = \sum_{x \in f^{-1}(y)} \operatorname{sign}(\det Df_x)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        boxed_formula = self.ly.formula_box(formula, color=PRIMARY)
        self.ly.safe_place(boxed_formula, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_formula), run_time=NORMAL)
        self.wait(3)

        interpretation = Text(
            "Count preimages with orientation sign",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(interpretation, DOWN, anchor=boxed_formula, buff=0.5)
        self.play(FadeIn(interpretation, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene6_applications(self):
        """Applications of the degree."""
        self.add_subcaption(
            "The degree has many applications. It proves the fundamental "
            "theorem of algebra: every polynomial has a root. "
            "It shows that a map from S^n to S^n with degree different "
            "from zero and minus one cannot have a fixed-point-free homotopy. "
            "It also gives the Brouwer fixed-point theorem: "
            "every continuous map from a disk to itself has a fixed point.",
            duration=26,
        )
        self.ly.section_divider(5, "Applications")

        title = self.ly.title("What Degree Gives Us")

        items = [
            Text("Fundamental Theorem of Algebra", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Brouwer Fixed Point Theorem", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Hairy Ball Theorem (for even spheres)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)
        self.ly.clear()

    def scene7_summary(self):
        """Summary and outro."""
        self.add_subcaption(
            "The degree of a map generalizes the winding number "
            "to maps between n-spheres. It is a homotopy invariant, "
            "computable via the differential formula, and has powerful "
            "applications across topology and analysis. "
            "In the next video, we will study cohomology, "
            "the dual theory of homology with a rich algebraic structure. "
            "Thank you for watching!",
            duration=26,
        )
        self.ly.section_divider(6, "Summary")

        title = self.ly.title("Key Takeaways")
        items = [
            Text("Degree: f_* on H_n(S^n) = Z", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Generalizes winding number to S^n", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Hopf theorem: degree classifies maps up to homotopy", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "In the next video, we will study cohomology, "
            "the dual theory of homology. Thank you for watching!",
            duration=10,
        )
        play_outro(self, "Cohomology", "Algebraic Topology")
