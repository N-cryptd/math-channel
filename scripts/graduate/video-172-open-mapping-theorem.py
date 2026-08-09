"""
Video 172: Open Mapping Theorem -- Functional Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video172_OpenMappingTheorem

Topics: Open Mapping Theorem statement and proof idea,
        Closed Graph Theorem,
        Uniform Boundedness Principle (Banach-Steinhaus),
        The "Big Three" theorems of functional analysis,
        Applications: inverse mapping, equivalence of norms,
        Baire Category theorem as foundation.

Prerequisites: Video 163 (Banach Spaces), Video 171 (Hahn-Banach).

Competitive insights:
- No Manim channel covers the Big Three with animations
- Unique visual: showing open maps preserve openness, graph visualization

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


class Video172_OpenMappingTheorem(Scene):
    """Open Mapping Theorem -- Functional Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_open_mapping()
        self.scene3_inverse_mapping()
        self.scene4_closed_graph()
        self.scene5_uniform_boundedness()
        self.scene6_applications()
        self.scene7_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "The Open Mapping Theorem, Closed Graph Theorem, and "
            "Uniform Boundedness Principle are the three pillars of "
            "Banach space theory. Together they show that bounded "
            "linear operators between Banach spaces are remarkably "
            "well-behaved.",
            duration=10,
        )
        play_intro(self, "Open Mapping Theorem", "Functional Analysis")

        title = self.ly.title("The Big Three Theorems")

        items = [
            Text("Open Mapping: surjective bounded maps are open",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Closed Graph: check graph closure to verify boundedness",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Uniform Boundedness: pointwise bounded implies uniformly bounded",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Open Mapping Theorem
    # ------------------------------------------------------------------ #
    def scene2_open_mapping(self):
        self.add_subcaption(
            "The Open Mapping Theorem states that a bounded surjective "
            "linear operator between Banach spaces maps open sets to "
            "open sets. This is remarkable because not every continuous "
            "map has this property.",
            duration=9,
        )

        self.ly.section_divider(2, "Open Mapping Theorem")
        title = self.ly.title("Open Mapping Theorem")

        stmt_label = Text("Theorem:",
                         font_size=BODY_SIZE, color=RED, font=SANS)
        stmt = Text(
            "If T: X to Y is bounded, surjective, and X, Y are Banach, then T is an open map",
            font_size=HEADING_SIZE, color=RED, font=SANS,
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

        # Key consequence
        key = Text(
            "Key: T(B_X) contains an open ball around 0 in Y",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(Indicate(key), run_time=FAST)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Inverse Mapping
    # ------------------------------------------------------------------ #
    def scene3_inverse_mapping(self):
        self.add_subcaption(
            "The Inverse Mapping Theorem follows directly from the "
            "Open Mapping Theorem. If T is bounded, bijective, and both "
            "spaces are Banach, then the inverse T inverse is also bounded.",
            duration=8,
        )

        self.ly.section_divider(3, "Inverse Mapping Theorem")
        title = self.ly.title("Consequence: Inverse Mapping")

        stmt_label = Text("Theorem:",
                         font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        stmt = MathTex(
            r"T \in B(X,Y) \text{ bijective, } X,Y \text{ Banach } \implies T^{-1} \in B(Y,X)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(stmt_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(stmt, direction=DOWN, anchor=stmt_label, buff=0.15)
        self.play(
            FadeIn(stmt_label, shift=LEFT * 0.15),
            Write(stmt),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(stmt_label), FadeOut(stmt), run_time=FAST)

        # Equivalence of norms
        eq_label = Text("Application: equivalence of norms on Banach spaces",
                        font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        eq = MathTex(
            r"\|x\|_1 \leq C\,\|x\|_2 \leq C'\,\|x\|_1",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(eq_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(eq, direction=DOWN, anchor=eq_label, buff=0.15)
        self.play(
            FadeIn(eq_label, shift=LEFT * 0.15),
            Write(eq),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Closed Graph Theorem
    # ------------------------------------------------------------------ #
    def scene4_closed_graph(self):
        self.add_subcaption(
            "The Closed Graph Theorem gives an easy way to verify "
            "an operator is bounded: just check that its graph is closed "
            "in the product space. This is often much easier than "
            "directly verifying the norm bound.",
            duration=9,
        )

        self.ly.section_divider(4, "Closed Graph Theorem")
        title = self.ly.title("Closed Graph Theorem")

        # Graph definition
        graph_label = Text("Graph of T:",
                          font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        graph = MathTex(
            r"\Gamma(T) = \{(x, Tx) : x \in X\} \subseteq X \times Y",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(graph_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(graph, direction=DOWN, anchor=graph_label, buff=0.15)
        self.play(
            FadeIn(graph_label, shift=LEFT * 0.15),
            Write(graph),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(graph_label), FadeOut(graph), run_time=FAST)

        # Theorem
        stmt_label = Text("Theorem:",
                         font_size=BODY_SIZE, color=RED, font=SANS)
        stmt = Text(
            "T: X to Y is bounded iff its graph is closed (X, Y Banach)",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(stmt_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(stmt, direction=DOWN, anchor=stmt_label, buff=0.15)
        self.play(
            FadeIn(stmt_label, shift=LEFT * 0.15),
            FadeIn(stmt, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(Indicate(stmt), run_time=FAST)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Uniform Boundedness
    # ------------------------------------------------------------------ #
    def scene5_uniform_boundedness(self):
        self.add_subcaption(
            "The Uniform Boundedness Principle, also called the "
            "Banach-Steinhaus theorem, says that if a family of "
            "bounded operators is pointwise bounded, then it is "
            "uniformly bounded in operator norm.",
            duration=9,
        )

        self.ly.section_divider(5, "Uniform Boundedness")
        title = self.ly.title("Banach-Steinhaus Theorem")

        stmt_label = Text("Theorem (Uniform Boundedness):",
                         font_size=BODY_SIZE, color=RED, font=SANS)
        stmt = Text(
            "If sup over T in F of norm of Tx is finite for each x, then sup over T in F of norm of T is finite",
            font_size=BODY_SIZE, color=RED, font=SANS,
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

        # Consequence
        cons = Text(
            "Pointwise bounded family of operators is uniformly bounded",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(cons, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(cons, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(cons), run_time=FAST)

        # Baire Category
        baire = Text(
            "All three theorems rely on the Baire Category Theorem",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(baire, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(baire, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Applications
    # ------------------------------------------------------------------ #
    def scene6_applications(self):
        self.add_subcaption(
            "These three theorems have deep applications. The Open "
            "Mapping theorem gives the inverse mapping theorem and "
            "equivalence of norms. The Closed Graph theorem is used "
            "in PDE theory. Uniform boundedness proves convergence "
            "of Fourier series.",
            duration=10,
        )

        self.ly.section_divider(6, "Applications")
        title = self.ly.title("Why These Matter")

        apps = [
            Text("PDE theory: verify solution operators are bounded",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Spectral theory: analytic properties of resolvent",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Fourier analysis: convergence theorems",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Quantum mechanics: unbounded vs bounded operators",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(apps, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Summary
    # ------------------------------------------------------------------ #
    def scene7_summary(self):
        self.add_subcaption(
            "Let us recap. The Open Mapping, Closed Graph, and Uniform "
            "Boundedness theorems are the three fundamental results of "
            "Banach space theory. They all rely on the Baire Category "
            "Theorem and show that bounded operators between Banach "
            "spaces are extremely well behaved.",
            duration=10,
        )

        self.ly.section_divider(7, "Key Takeaways")
        title = self.ly.title("Key Takeaways")

        items = [
            Text("Open Mapping: surjective bounded operators are open",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Inverse Mapping: bijective bounded implies bounded inverse",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Closed Graph: T bounded iff graph is closed",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Uniform Boundedness: pointwise bounded implies uniformly bounded",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("All three depend on Baire Category Theorem",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()
        play_outro(self, "Applications to PDEs", "Functional Analysis")
