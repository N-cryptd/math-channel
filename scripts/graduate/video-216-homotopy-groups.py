"""
Video 216: Introduction to Homotopy Groups — Algebraic Topology
Higher homotopy groups pi_n, pi_n(S^1)=0 for n>=2, pi_n(S^n)=Z,
fibration and long exact sequence, relation to homology via Hurewicz.
Playlist finale.

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


class Video216_HomotopyGroups(Scene):
    """Introduction to Homotopy Groups: from loops to higher dimensions."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_abelian()
        self.scene4_circle_trivial()
        self.scene5_sphere_groups()
        self.scene6_fibration()
        self.scene7_hurewicz()
        self.scene8_summary()

    # ───────────────────────────────────────────────────────────────
    # Scene 1: Hook
    # ───────────────────────────────────────────────────────────────
    def scene1_hook(self):
        """Hook — from loops to spheres."""
        self.add_subcaption(
            "Welcome to the finale of our Algebraic Topology series! "
            "We have studied the fundamental group, covering spaces, "
            "homology, cohomology, and the degree of a map. "
            "Today we ascend to higher homotopy groups, "
            "the natural generalization of loops to higher dimensions.",
            duration=22,
        )
        play_intro(self, "Introduction to Homotopy Groups", "Algebraic Topology")

        title = self.ly.title("From Loops to Higher Dimensions")
        items = [
            Text("Fundamental group: loops in X", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Higher homotopy: spheres in X", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("New tools: fibrations, Hurewicz theorem", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(8)
        self.ly.clear()

    # ───────────────────────────────────────────────────────────────
    # Scene 2: Definition of pi_n
    # ───────────────────────────────────────────────────────────────
    def scene2_definition(self):
        """Formal definition of higher homotopy groups."""
        self.add_subcaption(
            "Recall that the fundamental group pi one of X at a basepoint "
            "x zero is the set of homotopy classes of loops based at x zero. "
            "To generalize, replace the circle S one with the n-sphere S n. "
            "Define pi n of X as the set of homotopy classes of maps "
            "from S n to X that send a chosen basepoint to x zero. "
            "Equivalently, use the n-cube I to the n with its boundary "
            "mapped to x zero.",
            duration=28,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("The n-th Homotopy Group")

        defn = MathTex(
            r"\pi_n(X, x_0) = [S^n, X]_{x_0}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(defn, DOWN, anchor=title, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(3)

        equiv = Text(
            "Equivalently: homotopy classes of maps",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(equiv, DOWN, anchor=defn, buff=0.4)
        self.play(FadeIn(equiv, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        cube_def = MathTex(
            r"f : (I^n, \partial I^n) \to (X, x_0)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(cube_def, DOWN, anchor=equiv, buff=0.4)
        self.play(Write(cube_def), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    # ───────────────────────────────────────────────────────────────
    # Scene 3: Group structure and abelian for n >= 2
    # ───────────────────────────────────────────────────────────────
    def scene3_abelian(self):
        """Group structure and key property: abelian for n >= 2."""
        self.add_subcaption(
            "The group operation on pi n is defined by concatenation "
            "of spheres: pinch the equator of S n to get two hemispheres, "
            "apply one map to each hemisphere, and rescale. "
            "For n equals one this recovers concatenation of loops, "
            "which may not be commutative. "
            "But for n greater than or equal to two, the group pi n "
            "is always abelian. This is because we can swap the two "
            "hemispheres through the extra dimensions.",
            duration=28,
        )
        self.ly.section_divider(2, "Group Structure")

        title = self.ly.title("Higher Homotopy Groups Are Abelian")

        items = [
            Text("Operation: concatenate along equator of S^n", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("pi_1(X) can be non-abelian", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("pi_n(X) is abelian for all n >= 2", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3)

        reason = Text(
            "Extra room in I^n for n >= 2 lets us swap hemispheres",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(reason, DOWN, anchor=items[-1], buff=0.5)
        self.play(FadeIn(reason, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    # ───────────────────────────────────────────────────────────────
    # Scene 4: pi_n(S^1) = 0 for n >= 2
    # ───────────────────────────────────────────────────────────────
    def scene4_circle_trivial(self):
        """The circle has no higher homotopy."""
        self.add_subcaption(
            "A remarkable fact: the circle S one has trivial higher "
            "homotopy groups. For all n greater than or equal to two, "
            "pi n of S one is the trivial group. "
            "The intuition is that any map from a higher-dimensional "
            "sphere into the circle can be contracted to a point. "
            "The circle is one-dimensional, so higher-dimensional "
            "spheres always miss enough structure to create holes.",
            duration=26,
        )
        self.ly.section_divider(3, "The Circle")

        title = self.ly.title("Higher Homotopy of S^1")

        formula = MathTex(
            r"\pi_n(S^1) = 0 \quad \text{for all } n \geq 2",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(formula, color=PRIMARY)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed), run_time=NORMAL)
        self.wait(3)

        intuition = Text(
            "Higher spheres cannot detect the 1-dimensional hole",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(intuition, DOWN, anchor=boxed, buff=0.5)
        self.play(FadeIn(intuition, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    # ───────────────────────────────────────────────────────────────
    # Scene 5: pi_n(S^n) = Z
    # ───────────────────────────────────────────────────────────────
    def scene5_sphere_groups(self):
        """Homotopy groups of spheres: the central mystery."""
        self.add_subcaption(
            "For the n-sphere, the n-th homotopy group is the integers. "
            "This generalizes the winding number: a map from S n to S n "
            "wraps the target sphere some integer number of times. "
            "But computing pi m of S n when m differs from n "
            "is extraordinarily difficult. "
            "These are the stable homotopy groups of spheres, "
            "one of the deepest open problems in mathematics. "
            "For example, pi 3 of S 2 equals Z, discovered by Hopf.",
            duration=28,
        )
        self.ly.section_divider(4, "Spheres")

        title = self.ly.title("Homotopy Groups of Spheres")

        main_result = MathTex(
            r"\pi_n(S^n) \cong \mathbb{Z}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_main = self.ly.formula_box(main_result, color=PRIMARY)
        self.ly.safe_place(boxed_main, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_main), run_time=NORMAL)
        self.wait(3)

        hopf = MathTex(
            r"\pi_3(S^2) \cong \mathbb{Z} \quad \text{(Hopf fibration)}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(hopf, DOWN, anchor=boxed_main, buff=0.5)
        self.play(Write(hopf), run_time=NORMAL)
        self.wait(2)

        mystery = Text(
            "pi_m(S^n) for m != n: still largely unknown!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(mystery, DOWN, anchor=hopf, buff=0.5)
        self.play(FadeIn(mystery, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    # ───────────────────────────────────────────────────────────────
    # Scene 6: Fibrations and the long exact sequence
    # ───────────────────────────────────────────────────────────────
    def scene6_fibration(self):
        """Fibrations give a long exact sequence in homotopy."""
        self.add_subcaption(
            "A fibration is a map p from E to B with a nice local "
            "structure. The key example is the Hopf fibration, "
            "which maps S 3 to S 2 with fiber S 1. "
            "Every fibration gives rise to a long exact sequence "
            "in homotopy. This sequence connects the homotopy groups "
            "of the total space E, the base space B, and the fiber F. "
            "The connecting maps relate pi n of the fiber "
            "to pi n minus one of the base space.",
            duration=28,
        )
        self.ly.section_divider(5, "Fibrations")

        title = self.ly.title("The Long Exact Sequence of a Fibration")

        sequence = MathTex(
            r"\cdots \to \pi_n(F) \to \pi_n(E) \to \pi_n(B)"
            r"\to \pi_{n-1}(F) \to \cdots",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        boxed_seq = self.ly.formula_box(sequence, color=PRIMARY)
        self.ly.safe_place(boxed_seq, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_seq), run_time=NORMAL)
        self.wait(3)

        hopf_label = Text(
            "Hopf fibration: S^1 -> S^3 -> S^2",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(hopf_label, DOWN, anchor=boxed_seq, buff=0.5)
        self.play(FadeIn(hopf_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        use = Text(
            "Computes pi_3(S^2) from pi_3(S^3) = Z",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(use, DOWN, anchor=hopf_label, buff=0.5)
        self.play(FadeIn(use, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    # ───────────────────────────────────────────────────────────────
    # Scene 7: Hurewicz theorem — relation to homology
    # ───────────────────────────────────────────────────────────────
    def scene7_hurewicz(self):
        """Hurewicz theorem connects homotopy and homology."""
        self.add_subcaption(
            "How do homotopy groups relate to homology groups? "
            "The Hurewicz theorem provides the bridge. "
            "If X is path-connected and pi k of X is trivial "
            "for all k less than n, then the first nontrivial "
            "homotopy group pi n of X is isomorphic to "
            "the first nontrivial homology group H n of X. "
            "The Hurewicz homomorphism maps a homotopy class "
            "of spheres to a homology class, and under these "
            "conditions, it is an isomorphism.",
            duration=28,
        )
        self.ly.section_divider(6, "Hurewicz Theorem")

        title = self.ly.title("Connecting Homotopy and Homology")

        condition = Text(
            "If pi_k(X) = 0 for all 1 <= k < n:",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(condition, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(condition, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        result = MathTex(
            r"h : \pi_n(X) \xrightarrow{\cong} H_n(X)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_result = self.ly.formula_box(result, color=PRIMARY)
        self.ly.safe_place(boxed_result, DOWN, anchor=condition, buff=0.5)
        self.play(FadeIn(boxed_result), run_time=NORMAL)
        self.wait(3)

        note = Text(
            "Homotopy and homology agree at the first nontrivial level",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=boxed_result, buff=0.5)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    # ───────────────────────────────────────────────────────────────
    # Scene 8: Summary and Outro
    # ───────────────────────────────────────────────────────────────
    def scene8_summary(self):
        """Summary and playlist finale."""
        self.add_subcaption(
            "That concludes our introduction to homotopy groups and our "
            "Algebraic Topology series. We defined the n-th homotopy "
            "group as maps from spheres into a space, saw that higher "
            "groups are abelian, computed homotopy of the circle, "
            "studied the deep mystery of homotopy groups of spheres, "
            "and connected homotopy to homology via the Hurewicz theorem "
            "and fibrations via the long exact sequence. "
            "This series has taken us from the fundamental group "
            "through homology, cohomology, degree, and homotopy. "
            "Thank you for watching!",
            duration=32,
        )
        self.ly.section_divider(7, "Summary")

        title = self.ly.title("Key Takeaways")
        items = [
            Text("pi_n(X): homotopy classes of maps S^n to X", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Abelian for n >= 2", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("pi_n(S^1) = 0, pi_n(S^n) = Z", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Fibrations -> long exact sequence", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "This concludes the Algebraic Topology series. "
            "Thank you for watching!",
            duration=8,
        )
        play_outro(self)
