"""
Video 209: Covering Spaces — Algebraic Topology
Covering maps, the exponential map, path lifting, and the connection to fundamental groups.

QUALITY RULES:
1. Max 5 visible elements per scene
2. LayoutEngine for ALL positioning
3. Progressive disclosure
4. Raw strings with single backslashes for LaTeX
5. ly.clear() between scenes
6. Narration timing: ~2.5 words/sec minimum duration
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


class Video209_CoveringSpaces(Scene):
    """Covering Spaces: maps that locally look like projections."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_exponential_map()
        self.scene4_examples()
        self.scene5_path_lifting()
        self.scene6_fundamental_group()
        self.scene7_summary()

    def scene1_hook(self):
        """Hook — imagine unwinding a loop."""
        self.add_subcaption(
            "Welcome back to Algebraic Topology! In the last video, "
            "we studied the fundamental group, which captures loops up to homotopy.",
            duration=8,
        )
        play_intro(self, "Covering Spaces", "Algebraic Topology")

        self.add_subcaption(
            "Today we ask a powerful question: can we lift paths "
            "from one space up to another, simpler space?",
            duration=7,
        )
        title = self.ly.title("The Lifting Problem")
        items = [
            Text("A loop on the circle...", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("unwinds to a straight line in R", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Covering spaces make this precise", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    def scene2_definition(self):
        """Formal definition of a covering space."""
        self.add_subcaption(
            "A covering map is a continuous surjection from one space "
            "to another, where every small region lifts to exact copies.",
            duration=8,
        )
        self.ly.section_divider(1, "Definition of Covering Space")

        title = self.ly.title("Covering Map")

        self.add_subcaption(
            "A map p from X-tilde to X is a covering map if every point "
            "x in X has an open neighborhood U, whose preimage is a disjoint "
            "union of open sets, each mapped homeomorphically onto U.",
            duration=10,
        )
        defn_map = MathTex(
            r"p : \widetilde{X} \to X",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_map = self.ly.formula_box(defn_map, color=PRIMARY)
        self.ly.safe_place(boxed_map, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_map), run_time=NORMAL)

        self.wait(0.5)

        self.add_subcaption(
            "Each component of the preimage is called a sheet. "
            "The set of all points mapping to x is called the fiber over x.",
            duration=8,
        )
        terms = [
            Text("Every x in X has neighborhood U", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("p-inverse of U = disjoint copies of U", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Fiber: p-inverse of x", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(terms, start_from=boxed_map)

        self.wait(0.5)
        self.ly.clear()

    def scene3_exponential_map(self):
        """The canonical example: R covers S^1."""
        self.add_subcaption(
            "The most important covering map is the exponential map "
            "from the real line onto the circle.",
            duration=7,
        )
        self.ly.section_divider(2, "The Exponential Map")

        title = self.ly.title("R Covers S^1")

        self.add_subcaption(
            "The map sends a real number t to the point on the unit circle "
            "at angle two pi t. Each interval of length one wraps once "
            "around the circle.",
            duration=9,
        )
        formula = MathTex(
            r"p(t) = e^{2\pi i\, t}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_formula = self.ly.formula_box(formula, color=PRIMARY)
        self.ly.safe_place(boxed_formula, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_formula), run_time=NORMAL)

        self.wait(0.3)

        self.add_subcaption(
            "The fiber of the point one is all integers. "
            "This means the real line wraps around the circle infinitely many times.",
            duration=8,
        )
        fiber = MathTex(
            r"p^{-1}(1) = \mathbb{Z}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(fiber, DOWN, anchor=boxed_formula, buff=0.5)
        self.play(FadeIn(fiber), run_time=NORMAL)

        # Visual: dots on line above circle
        self.add_subcaption(
            "Think of the real line as an infinite helix projecting down onto the circle. "
            "Each integer projects to the same point.",
            duration=7,
        )
        self.wait(0.5)
        self.ly.clear()

    def scene4_examples(self):
        """More examples of covering spaces."""
        self.add_subcaption(
            "Let us see several more examples of covering spaces.",
            duration=4,
        )
        self.ly.section_divider(3, "More Examples")

        self.add_subcaption(
            "The double cover sends each point on the circle to its square. "
            "Going around once in the cover means going around twice below.",
            duration=8,
        )
        title = self.ly.title("Covering Examples")
        examples = [
            MathTex(r"S^1 \xrightarrow{z \mapsto z^2} S^1", font_size=BODY_SIZE, color=PRIMARY),
            Text("Double cover: each point has 2 preimages", font_size=BODY_SIZE, color=DIM, font=SANS),
            MathTex(r"\mathbb{R}^2 \setminus \{0\} \to \mathbb{R}P^1", font_size=BODY_SIZE, color=SECONDARY),
            Text("Universal cover unwinds all loops", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(examples, start_from=title)
        self.wait(0.5)
        self.ly.clear()

        self.add_subcaption(
            "The figure-eight space has a universal cover that looks like an infinite tree. "
            "Every loop lifts to a unique path in this tree.",
            duration=8,
        )
        title2 = self.ly.title("Universal Cover")
        items2 = [
            Text("Figure-eight: S^1 wedge S^1", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Universal cover: infinite Cayley tree", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Every space has a simply connected cover", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(0.5)
        self.ly.clear()

    def scene5_path_lifting(self):
        """The path lifting property."""
        self.add_subcaption(
            "One of the most powerful properties of covering spaces "
            "is the ability to lift paths.",
            duration=6,
        )
        self.ly.section_divider(4, "Path Lifting")

        title = self.ly.title("The Path Lifting Property")

        self.add_subcaption(
            "Given a path gamma in the base space X starting at x naught, "
            "and a point x-tilde in the fiber over x naught, "
            "there exists a unique lifted path gamma-tilde in the cover.",
            duration=10,
        )
        statement = MathTex(
            r"\gamma(0) = x_0, \; \tilde{x} \in p^{-1}(x_0)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(statement, DOWN, anchor=title, buff=0.5)
        self.play(Write(statement), run_time=NORMAL)

        self.add_subcaption(
            "The lift satisfies p composed with gamma-tilde equals gamma, "
            "and gamma-tilde of zero equals x-tilde. "
            "This lift is unique.",
            duration=9,
        )
        lift = MathTex(
            r"p \circ \tilde{\gamma} = \gamma, \quad \tilde{\gamma}(0) = \tilde{x}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(lift, DOWN, anchor=statement, buff=0.5)
        self.play(FadeIn(lift), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Homotopy lifting
        self.add_subcaption(
            "Even better, entire homotopies can be lifted. "
            "If two paths are homotopic in the base, "
            "their lifts are homotopic in the cover.",
            duration=9,
        )
        title2 = self.ly.title("Homotopy Lifting")
        hlift = MathTex(
            r"\gamma \simeq \sigma \implies \tilde{\gamma} \simeq \tilde{\sigma}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed_hlift = self.ly.formula_box(hlift, color=SECONDARY)
        self.ly.safe_place(boxed_hlift, DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(boxed_hlift), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

    def scene6_fundamental_group(self):
        """Connection between covering spaces and the fundamental group."""
        self.add_subcaption(
            "Covering spaces give us a powerful tool for computing "
            "fundamental groups. Let us see how.",
            duration=7,
        )
        self.ly.section_divider(5, "Computing Fundamental Groups")

        title = self.ly.title("The Fundamental Group of S^1")

        self.add_subcaption(
            "The covering map from R to S^1 lets us compute "
            "the fundamental group of the circle. Every loop on the circle "
            "lifts to a path in R, and the endpoint tells us the winding number.",
            duration=10,
        )
        theorem = MathTex(
            r"\pi_1(S^1) \cong \mathbb{Z}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_thm = self.ly.formula_box(theorem, color=PRIMARY)
        self.ly.safe_place(boxed_thm, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_thm), run_time=NORMAL)

        self.add_subcaption(
            "The integer counts how many times the loop winds around the circle. "
            "This is the same result we stated in the last video, "
            "but now we see why: it comes directly from the covering space structure.",
            duration=10,
        )
        self.wait(0.5)
        self.ly.clear()

        # Monodromy
        self.add_subcaption(
            "More generally, the fundamental group acts on the fiber "
            "by permuting the preimage points. This is called the monodromy action.",
            duration=8,
        )
        title2 = self.ly.title("Monodromy Action")
        action = MathTex(
            r"\pi_1(X, x_0) \curvearrowright p^{-1}(x_0)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(action, DOWN, anchor=title2, buff=0.5)
        self.play(Write(action), run_time=NORMAL)

        self.add_subcaption(
            "Different covering spaces correspond to different subgroups "
            "of the fundamental group. The universal cover corresponds "
            "to the trivial subgroup.",
            duration=8,
        )
        subgroups = [
            Text("Universal cover: trivial subgroup", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Other covers: other subgroups", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Galois correspondence of covers", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(subgroups, start_from=action)
        self.wait(0.5)
        self.ly.clear()

    def scene7_summary(self):
        """Summary and outro."""
        self.add_subcaption(
            "Let us summarize what we have learned about covering spaces.",
            duration=4,
        )
        self.ly.section_divider(6, "Summary")

        title = self.ly.title("Key Takeaways")
        items = [
            Text("Covering map: local homeomorphism with discrete fibers", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Canonical example: R covers S^1", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Path and homotopy lifting properties", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Covering spaces compute fundamental groups", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(0.5)
        self.ly.clear()

        # Summary formula
        self.add_subcaption(
            "The covering space framework is one of the most beautiful "
            "in all of topology. It connects local geometry to global algebra, "
            "and gives us concrete computational tools.",
            duration=8,
        )
        title2 = self.ly.title("Summary Formula")
        summary = self.ly.formula_box(
            MathTex(
                r"p : \widetilde{X} \to X, \quad "
                r"\pi_1(X) \cong \text{deck transformations}",
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
            "In the next video, we will study simplicial complexes, "
            "which give us a combinatorial way to build and analyze "
            "topological spaces. Thank you for watching!",
            duration=8,
        )
        play_outro(self, "Simplicial Complexes", "Algebraic Topology")
