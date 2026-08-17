"""
Video 215: Cohomology — Algebraic Topology
Cochain groups, coboundary maps, cohomology groups H^n,
cup product, Poincare duality statement.

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


class Video215_Cohomology(Scene):
    """Cohomology: the dual theory of homology."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_cochain_groups()
        self.scene3_coboundary()
        self.scene4_cohomology_groups()
        self.scene5_functoriality()
        self.scene6_cup_product()
        self.scene7_poincare_duality()
        self.scene8_summary()

    def scene1_hook(self):
        """Hook — turning homology inside out."""
        self.add_subcaption(
            "We have spent many videos building homology groups, which "
            "capture the cycles and boundaries of a space. Today we meet "
            "cohomology, the elegant dual theory obtained by reversing all "
            "the arrows. Cohomology carries a natural ring structure called "
            "the cup product, and it satisfies the profound Poincare duality "
            "theorem for manifolds.",
            duration=24,
        )
        play_intro(self, "Cohomology", "Algebraic Topology")

        title = self.ly.title("Homology, Reversed")
        items = [
            Text("Homology: chains, boundaries, cycles", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Cohomology: cochains, coboundaries, cocycles", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Cup product gives a ring structure", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(7)
        self.ly.clear()

    def scene2_cochain_groups(self):
        """Cochain groups as dual of chain groups."""
        self.add_subcaption(
            "The key idea is hom-dualization. Given an abelian group G, "
            "its dual Hom of G into Z is the group of homomorphisms "
            "from G to the integers. For each chain group C_n of X, we "
            "define the cochain group C^n of X as Hom of C_n into our "
            "coefficient ring, which we usually take to be the integers. "
            "A cochain assigns an integer to each n-chain.",
            duration=24,
        )
        self.ly.section_divider(1, "Cochain Groups")

        title = self.ly.title("From Chains to Cochains")

        defn = MathTex(
            r"C^n(X) = \operatorname{Hom}(C_n(X), \mathbb{Z})",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(defn, DOWN, anchor=title, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(3)

        interpretation = Text(
            "A cochain assigns an integer to each n-chain",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(interpretation, DOWN, anchor=defn, buff=0.5)
        self.play(FadeIn(interpretation, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene3_coboundary(self):
        """Coboundary maps: dualizing the boundary operator."""
        self.add_subcaption(
            "The boundary map takes C_n to C_{n-1}. To dualize this, "
            "we apply the Hom functor to get a map from C^{n-1} to C^n. "
            "This is the coboundary map delta. It goes in the opposite "
            "direction from the boundary map, which is why cohomology "
            "chains run upward. We write the coboundary operator as "
            "delta acting on a cochain phi to produce a cochain in the "
            "next degree, defined by composing phi with the boundary of "
            "each chain.",
            duration=26,
        )
        self.ly.section_divider(2, "Coboundary Maps")

        title = self.ly.title("Reversing the Arrows")

        boundary = MathTex(
            r"\partial_n : C_n \to C_{n-1}",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(boundary, DOWN, anchor=title, buff=0.5)
        self.play(Write(boundary), run_time=FAST)
        self.wait(2)

        coboundary = MathTex(
            r"\delta^n : C^n \to C^{n+1}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_cb = self.ly.formula_box(coboundary, color=PRIMARY)
        self.ly.safe_place(boxed_cb, DOWN, anchor=boundary, buff=0.5)
        self.play(FadeIn(boxed_cb), run_time=NORMAL)
        self.wait(3)

        eval_formula = MathTex(
            r"(\delta\varphi)(\sigma) = \varphi(\partial\sigma)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(eval_formula, DOWN, anchor=boxed_cb, buff=0.5)
        self.play(Write(eval_formula), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene4_cohomology_groups(self):
        """Cohomology groups H^n: kernel mod image of delta."""
        self.add_subcaption(
            "Just as homology is kernel of boundary mod image of boundary, "
            "cohomology is kernel of delta mod image of delta. "
            "The kernel of delta are the cocycles, cochains whose "
            "coboundary vanishes. The image of delta are the coboundaries. "
            "The n-th cohomology group is the quotient of cocycles "
            "by coboundaries. For a good space like a circle, "
            "the cohomology in degree zero is Z and in degree one is Z, "
            "mirroring homology.",
            duration=26,
        )
        self.ly.section_divider(3, "Cohomology Groups")

        title = self.ly.title("The Definition")

        formula = MathTex(
            r"H^n(X) = \frac{\ker \delta^n}{\operatorname{im} \delta^{n-1}}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_formula = self.ly.formula_box(formula, color=PRIMARY)
        self.ly.safe_place(boxed_formula, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_formula), run_time=NORMAL)
        self.wait(3)

        names = [
            Text("Cocycles: ker(delta) = cochains with vanishing coboundary",
                 font_size=LABEL_SIZE, color=SECONDARY, font=SANS),
            Text("Coboundaries: im(delta) = cochains coming from below",
                 font_size=LABEL_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(names, start_from=boxed_formula)
        self.wait(5)
        self.ly.clear()

    def scene5_functoriality(self):
        """Universal coefficient theorem and functoriality."""
        self.add_subcaption(
            "The universal coefficient theorem relates cohomology to homology. "
            "It says that for any space X, the n-th cohomology with integer "
            "coefficients is isomorphic to Hom of H_n with Z plus Ext of "
            "H_{n-1} with Z. In many cases, especially when homology is free "
            "abelian, the Ext term vanishes and cohomology is simply the "
            "dual of homology. But cohomology can carry strictly more "
            "information, revealing torsion that homology alone cannot see.",
            duration=26,
        )
        self.ly.section_divider(4, "Universal Coefficient Theorem")

        title = self.ly.title("Cohomology from Homology")

        uct = MathTex(
            r"H^n(X;\mathbb{Z}) \cong "
            r"\operatorname{Hom}(H_n(X),\mathbb{Z}) "
            r"\oplus \operatorname{Ext}(H_{n-1}(X),\mathbb{Z})",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_uct = self.ly.formula_box(uct, color=PRIMARY)
        self.ly.safe_place(boxed_uct, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_uct), run_time=NORMAL)
        self.wait(3)

        implication = Text(
            "When H_{n-1} is free, Ext vanishes and H^n is the dual of H_n",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(implication, DOWN, anchor=boxed_uct, buff=0.5)
        self.play(FadeIn(implication, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene6_cup_product(self):
        """Cup product: the ring structure on cohomology."""
        self.add_subcaption(
            "One of the great advantages of cohomology over homology is the "
            "cup product. Given cochains phi in degree p and psi in degree q, "
            "their cup product phi wedge psi is a cochain in degree p plus q. "
            "This descends to a product on cohomology, making the direct sum "
            "of all cohomology groups into a graded ring. For the circle, "
            "the cup product is trivial because H^1 wedged with H^1 would "
            "land in H^2 which is zero. But on the torus, H^1 is Z squared "
            "and the cup product of the two generators lives in H^2 "
            "which is Z, giving a rich ring structure.",
            duration=28,
        )
        self.ly.section_divider(5, "Cup Product")

        title = self.ly.title("The Ring Structure")

        formula = MathTex(
            r"\smile : H^p(X) \times H^q(X) \to H^{p+q}(X)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_cup = self.ly.formula_box(formula, color=PRIMARY)
        self.ly.safe_place(boxed_cup, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_cup), run_time=NORMAL)
        self.wait(3)

        ring = MathTex(
            r"H^*(X) = \bigoplus_{n=0}^{\infty} H^n(X)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ring, DOWN, anchor=boxed_cup, buff=0.5)
        self.play(Write(ring), run_time=NORMAL)
        self.wait(3)

        remark = Text(
            "Cohomology is a graded ring; homology is only a graded group",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(remark, DOWN, anchor=ring, buff=0.5)
        self.play(FadeIn(remark, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(6)
        self.ly.clear()

    def scene7_poincare_duality(self):
        """Poincare duality statement for oriented manifolds."""
        self.add_subcaption(
            "For a compact oriented n-dimensional manifold M, Poincare duality "
            "states that the k-th cohomology is isomorphic to the n minus k-th "
            "homology. This creates a perfect pairing between cohomology in "
            "complementary degrees. The cup product pairing H^k of M with "
            "H^{n-k} of M mapping to H^n of M isomorphic to Z is "
            "non-degenerate. Poincare duality is a deep connection between "
            "the topology of a manifold and its algebraic invariants, "
            "linking local geometry to global structure.",
            duration=26,
        )
        self.ly.section_divider(6, "Poincare Duality")

        title = self.ly.title("The Duality Theorem")

        duality = MathTex(
            r"H^k(M) \cong H_{n-k}(M)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        condition = Text(
            "for a compact oriented n-manifold M",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        duality_group = VGroup(duality, condition).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        boxed_dual = self.ly.formula_box(duality, color=PRIMARY)
        self.ly.safe_place(boxed_dual, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_dual), run_time=NORMAL)
        self.wait(3)

        pairing = Text(
            "Cup product pairs complementary degrees non-degenerately",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(pairing, DOWN, anchor=boxed_dual, buff=0.5)
        self.play(FadeIn(pairing, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene8_summary(self):
        """Summary and outro."""
        self.add_subcaption(
            "Cohomology is the dual theory of homology, obtained by applying "
            "the Hom functor to chain groups and reversing the boundary maps. "
            "The resulting cohomology groups carry a natural ring structure "
            "via the cup product, making them algebraically richer than "
            "homology. Poincare duality for compact oriented manifolds "
            "reveals a deep symmetry linking cohomology in complementary "
            "degrees. Together, homology and cohomology form the twin "
            "pillars of algebraic topology. Thank you for watching!",
            duration=28,
        )
        self.ly.section_divider(7, "Summary")

        title = self.ly.title("Key Takeaways")
        items = [
            Text("Cochains: Hom(C_n, Z) — arrows reversed",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("H^n = cocycles / coboundaries",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Cup product makes H* into a graded ring",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "Thank you for watching! In the next video we will study "
            "homotopy groups in more depth.",
            duration=10,
        )
        play_outro(self, "Homotopy Groups", "Algebraic Topology")
