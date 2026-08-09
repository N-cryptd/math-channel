"""
Video 171: Hahn-Banach Theorem -- Functional Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video171_HahnBanachTheorem

Topics: Hahn-Banach theorem (analytic and geometric forms),
        Extension of linear functionals,
        Separation of convex sets,
        Applications: existence of supporting functionals,
        Duality and reflexivity consequences,
        Uniform boundedness preview.

Prerequisites: Video 162 (Normed Spaces), Video 167 (Dual Space),
               Video 168 (Weak Topology).

Competitive insights:
- No Manim channel covers the Hahn-Banach theorem with animations
- Key visual: functional on subspace → extension to whole space (geometric)
- Unique: animated convex set separation

Quality Rules (mandatory):
1. Max 5 visible elements per scene at any time
2. Use LayoutEngine for ALL positioning -- no manual .shift() or .to_edge()
3. Progressive disclosure: add items one at a time
4. Each add_subcaption() duration = words / 2.5 seconds (12 words = 5s)
5. Call ly.clear() between scenes
6. Use consistent animation vocabulary from channel_branding.py
7. MathTex: raw strings with single backslashes
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


class Video171_HahnBanachTheorem(Scene):
    """Hahn-Banach Theorem -- Functional Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_analytic_form()
        self.scene3_proof_idea()
        self.scene4_geometric_form()
        self.scene5_applications()
        self.scene6_consequences()
        self.scene7_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "The Hahn-Banach theorem is one of the big three theorems "
            "of functional analysis. It guarantees that we can always "
            "extend a bounded linear functional from a subspace to the "
            "whole space without increasing its norm.",
            duration=9,
        )
        play_intro(self, "Hahn-Banach Theorem", "Functional Analysis")

        title = self.ly.title("The Big Three: Hahn-Banach")

        items = [
            Text("Extend linear functionals preserving the norm",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Separate convex sets with hyperplanes",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Guarantees the dual space is always rich",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Analytic Form
    # ------------------------------------------------------------------ #
    def scene2_analytic_form(self):
        self.add_subcaption(
            "The analytic form says that if p is a sublinear functional "
            "on a real vector space, and f is a linear functional on a "
            "subspace dominated by p, then f extends to the whole space "
            "still dominated by p.",
            duration=9,
        )

        self.ly.section_divider(2, "Analytic Form")
        title = self.ly.title("Hahn-Banach (Analytic)")

        # Setup
        setup_label = Text("Let Y be a subspace of X:",
                          font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        setup = MathTex(
            r"f : Y \to \mathbb{R} \text{ linear}, \quad |f(y)| \leq p(y) \;\; \forall\, y \in Y",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(setup_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(setup, direction=DOWN, anchor=setup_label, buff=0.15)
        self.play(
            FadeIn(setup_label, shift=LEFT * 0.15),
            Write(setup),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(setup_label), FadeOut(setup), run_time=FAST)

        # Conclusion
        conc_label = Text("Then there exists an extension:",
                        font_size=BODY_SIZE, color=RED, font=SANS)
        conc = MathTex(
            r"\tilde{f} : X \to \mathbb{R}, \quad \tilde{f}|_Y = f, \quad |\tilde{f}(x)| \leq p(x)",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(conc_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(conc, direction=DOWN, anchor=conc_label, buff=0.15)
        self.play(
            FadeIn(conc_label, shift=LEFT * 0.15),
            Write(conc),
            run_time=SLOW,
        )
        self.wait(0.5)
        self.play(FadeOut(conc_label), FadeOut(conc), run_time=FAST)

        # Normed space version
        norm_label = Text("Normed space version:",
                        font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        norm = MathTex(
            r"\|\tilde{f}\| = \|f\|",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed = self.ly.formula_box(norm, SECONDARY)
        self.ly.safe_place(norm_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=norm_label, buff=0.2)
        self.play(
            FadeIn(norm_label, shift=LEFT * 0.15),
            Write(norm),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Proof Idea
    # ------------------------------------------------------------------ #
    def scene3_proof_idea(self):
        self.add_subcaption(
            "The proof uses Zorn's lemma. We consider all partial "
            "extensions of f that respect the bound, and show that "
            "every chain has an upper bound. By Zorn's lemma, a maximal "
            "element exists and must be defined on all of X.",
            duration=10,
        )

        self.ly.section_divider(3, "Proof Idea")
        title = self.ly.title("Proof via Zorn's Lemma")

        steps = [
            Text("Consider all extensions of f that respect the norm bound",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Partially order by: g is less than or equal to h if h extends g",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Every chain has an upper bound (take the union)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Zorn's lemma gives a maximal element",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Maximality forces the extension to be defined on all of X",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(steps, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Geometric Form
    # ------------------------------------------------------------------ #
    def scene4_geometric_form(self):
        self.add_subcaption(
            "The geometric form of the Hahn-Banach theorem says that "
            "two disjoint convex sets in a vector space can be separated "
            "by a closed hyperplane. This is a powerful tool in optimization.",
            duration=8,
        )

        self.ly.section_divider(4, "Geometric Form")
        title = self.ly.title("Separation of Convex Sets")

        stmt_label = Text("Hahn-Banach (geometric):",
                        font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        stmt = Text(
            "Two disjoint convex sets can be separated by a hyperplane",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(stmt_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(stmt, direction=DOWN, anchor=stmt_label, buff=0.15)
        self.play(
            FadeIn(stmt_label, shift=LEFT * 0.15),
            FadeIn(stmt, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(stmt_label), FadeOut(stmt), run_time=FAST)

        # Math statement
        math_label = Text("Formally: exists f in X* and alpha in R such that:",
                         font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        math_stmt = MathTex(
            r"f(x) \leq \alpha \leq f(y) \quad \forall\, x \in A,\, y \in B",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(math_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(math_stmt, direction=DOWN, anchor=math_label, buff=0.15)
        self.play(
            FadeIn(math_label, shift=LEFT * 0.15),
            Write(math_stmt),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(math_label), FadeOut(math_stmt), run_time=FAST)

        # Strict separation
        strict = Text(
            "If A is compact and B is closed: strict separation possible",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(strict, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(strict, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Applications
    # ------------------------------------------------------------------ #
    def scene5_applications(self):
        self.add_subcaption(
            "The Hahn-Banach theorem has many important applications. "
            "It guarantees the existence of supporting functionals, "
            "shows the dual space separates points, and is used in "
            "optimization and the theory of convex sets.",
            duration=9,
        )

        self.ly.section_divider(5, "Applications")
        title = self.ly.title("What Hahn-Banach Gives Us")

        apps = [
            Text("For every nonzero x, exists f with f(x) equal to norm of x",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("X* separates points of X (if x is not 0, some f has f(x) not 0)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Used to prove the Open Mapping and Closed Graph theorems",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Foundation of convex optimization duality theory",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(apps, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Consequences
    # ------------------------------------------------------------------ #
    def scene6_consequences(self):
        self.add_subcaption(
            "Important consequences for duality and reflexivity. "
            "The natural embedding of X into its double dual is always "
            "isometric. A space is reflexive precisely when this "
            "embedding is surjective.",
            duration=8,
        )

        self.ly.section_divider(6, "Consequences for Duality")
        title = self.ly.title("Duality Implications")

        cons = [
            Text("Natural map J: X to X** is always isometric",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("X is reflexive iff J(X) equals X**",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Hahn-Banach implies X** is always non-trivial",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Connected to Uniform Boundedness Principle (next video)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(cons, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Summary
    # ------------------------------------------------------------------ #
    def scene7_summary(self):
        self.add_subcaption(
            "Let us recap. The Hahn-Banach theorem is fundamental. "
            "It extends linear functionals, separates convex sets, "
            "and guarantees the dual space is rich. Together with "
            "the Open Mapping and Closed Graph theorems, it forms "
            "the foundation of functional analysis.",
            duration=10,
        )

        self.ly.section_divider(7, "Key Takeaways")
        title = self.ly.title("Key Takeaways")

        items = [
            Text("Hahn-Banach: extend functionals preserving the norm",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Geometric form: separate disjoint convex sets",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Proof uses Zorn's lemma (non-constructive)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Dual space X* always separates points of X",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()
        play_outro(self, "Open Mapping Theorem", "Functional Analysis")
