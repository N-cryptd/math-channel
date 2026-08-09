"""
Video 173: Applications to PDEs -- Functional Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video173_ApplicationsToPDEs

Topics: Weak solutions to PDEs,
        Sobolev spaces motivation,
        Lax-Milgram theorem,
        Elliptic boundary value problems,
        Weak convergence and compactness in PDEs,
        Gelfand triple (V ⊂ H ⊂ V*),
        Connection to the Functional Analysis playlist.

Prerequisites: Video 163 (Banach Spaces), Video 167 (Dual Space),
               Video 168 (Weak Topology), Video 171 (Hahn-Banach),
               Video 172 (Open Mapping).

Competitive insights:
- No Manim channel connects functional analysis to PDEs with animations
- Unique: showing how abstract theorems become concrete tools
- This video ties the entire playlist together

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


class Video173_ApplicationsToPDEs(Scene):
    """Applications to PDEs -- Functional Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_weak_solutions()
        self.scene3_sobolev()
        self.scene4_lax_milgram()
        self.scene5_gelfand_triple()
        self.scene6_concrete_example()
        self.scene7_playlist_recap()
        self.scene8_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Why does functional analysis matter? Because it gives us "
            "the tools to solve partial differential equations. In this "
            "final video, we see how every theorem we learned connects "
            "to real problems in physics and engineering.",
            duration=9,
        )
        play_intro(self, "Applications to PDEs", "Functional Analysis")

        title = self.ly.title("Functional Analysis in Action")

        items = [
            Text("PDEs are the language of physics and engineering",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Classical solutions often do not exist",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Weak solutions + functional analysis save the day",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Weak Solutions
    # ------------------------------------------------------------------ #
    def scene2_weak_solutions(self):
        self.add_subcaption(
            "A weak solution to a PDE satisfies the equation only after "
            "integrating against a test function. This requires less "
            "regularity than a classical solution. The Hahn-Banach theorem "
            "guarantees enough test functions exist.",
            duration=9,
        )

        self.ly.section_divider(2, "Weak Solutions")
        title = self.ly.title("Why Weak Solutions?")

        # Classical problem
        prob_label = Text("Classical PDE: find u such that Lu = f",
                         font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        prob = Text(
            "Requires u to be twice differentiable (too restrictive!)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(prob_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(prob, direction=DOWN, anchor=prob_label, buff=0.15)
        self.play(
            FadeIn(prob_label, shift=LEFT * 0.15),
            FadeIn(prob, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(prob_label), FadeOut(prob), run_time=FAST)

        # Weak formulation
        weak_label = Text("Weak form: integrate against test function v",
                         font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        weak = MathTex(
            r"\int_\Omega (\nabla u \cdot \nabla v + u\,v)\,dx = \int_\Omega f\,v\,dx",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(weak_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(weak, direction=DOWN, anchor=weak_label, buff=0.15)
        self.play(
            FadeIn(weak_label, shift=LEFT * 0.15),
            Write(weak),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(weak_label), FadeOut(weak), run_time=FAST)

        # Key point
        key = Text(
            "u only needs one derivative (less regularity needed)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Sobolev Spaces
    # ------------------------------------------------------------------ #
    def scene3_sobolev(self):
        self.add_subcaption(
            "Sobolev spaces are the natural home for weak solutions. "
            "They are Banach spaces that include functions and their "
            "weak derivatives. The H1 space has functions with one "
            "square integrable weak derivative.",
            duration=9,
        )

        self.ly.section_divider(3, "Sobolev Spaces")
        title = self.ly.title("Sobolev Spaces")

        defn_label = Text("Sobolev space H^1 (Omega):",
                        font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        defn = MathTex(
            r"H^1(\Omega) = \{u \in L^2(\Omega) : \nabla u \in L^2(\Omega)\}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(defn_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(defn, direction=DOWN, anchor=defn_label, buff=0.15)
        self.play(
            FadeIn(defn_label, shift=LEFT * 0.15),
            Write(defn),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(defn_label), FadeOut(defn), run_time=FAST)

        # Norm
        norm_label = Text("With norm:",
                         font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        norm = MathTex(
            r"\|u\|_{H^1}^2 = \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2",
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
        self.play(FadeOut(norm_label), FadeOut(boxed), run_time=FAST)

        # Key property
        prop = Text(
            "H^1 is a Hilbert space (Banach + inner product)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(prop, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(prop, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Lax-Milgram
    # ------------------------------------------------------------------ #
    def scene4_lax_milgram(self):
        self.add_subcaption(
            "The Lax-Milgram theorem is the workhorse for proving "
            "existence of weak solutions. It applies the Riesz "
            "representation theorem to a bilinear form. If the form "
            "is bounded and coercive, a unique solution exists.",
            duration=10,
        )

        self.ly.section_divider(4, "Lax-Milgram Theorem")
        title = self.ly.title("Lax-Milgram Theorem")

        # Setup
        setup_label = Text("Let a: V times V to R be a bilinear form:",
                          font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        setup = Text(
            "Bounded: |a(u,v)| is less than or equal to M times norm u times norm v",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(setup_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(setup, direction=DOWN, anchor=setup_label, buff=0.15)
        self.play(
            FadeIn(setup_label, shift=LEFT * 0.15),
            FadeIn(setup, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(setup_label), FadeOut(setup), run_time=FAST)

        # Coercive
        coerc_label = Text("Coercive (V-elliptic):",
                          font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        coerc = Text(
            "a(v,v) is greater than or equal to alpha times norm v squared",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(coerc_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(coerc, direction=DOWN, anchor=coerc_label, buff=0.15)
        self.play(
            FadeIn(coerc_label, shift=LEFT * 0.15),
            FadeIn(coerc, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(coerc_label), FadeOut(coerc), run_time=FAST)

        # Conclusion
        conc_label = Text("Then: for every f in V*, exists unique u in V:",
                        font_size=BODY_SIZE, color=RED, font=SANS)
        conc = MathTex(
            r"a(u, v) = f(v) \quad \forall\, v \in V",
            font_size=HEADING_SIZE, color=RED,
        )
        boxed = self.ly.formula_box(conc, RED)
        self.ly.safe_place(conc_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=conc_label, buff=0.2)
        self.play(
            FadeIn(conc_label, shift=LEFT * 0.15),
            Write(conc),
            run_time=SLOW,
        )
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Gelfand Triple
    # ------------------------------------------------------------------ #
    def scene5_gelfand_triple(self):
        self.add_subcaption(
            "The Gelfand triple captures the relationship between a "
            "Sobolev space, an L^2 space, and its dual. We have V "
            "densely embedded in H, which is identified with its dual, "
            "giving V is a subset of H is a subset of V star.",
            duration=9,
        )

        self.ly.section_divider(5, "Gelfand Triple")
        title = self.ly.title("The Gelfand Triple")

        triple_label = Text("Gelfand triple (or evolution triple):",
                          font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        triple = MathTex(
            r"V \hookrightarrow H \cong H^* \hookrightarrow V^*",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(triple, PRIMARY)
        self.ly.safe_place(triple_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=triple_label, buff=0.2)
        self.play(
            FadeIn(triple_label, shift=LEFT * 0.15),
            Write(triple),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(triple_label), FadeOut(boxed), run_time=FAST)

        # Example
        ex_label = Text("Example: H^1_0(Omega) is in L^2(Omega) is in H^(-1)(Omega)",
                       font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(ex_label, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(ex_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(ex_label), run_time=FAST)

        # Why it matters
        why = Text(
            "PDE solutions live in V; data lives in V*; energy in H",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(why, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(why, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Concrete Example
    # ------------------------------------------------------------------ #
    def scene6_concrete_example(self):
        self.add_subcaption(
            "Consider the Poisson equation: negative Laplacian of u "
            "equals f on Omega, with u equal to zero on the boundary. "
            "The weak formulation and Lax-Milgram give existence "
            "and uniqueness of the solution in H^1_0.",
            duration=10,
        )

        self.ly.section_divider(6, "Example: Poisson Equation")
        title = self.ly.title("Poisson Equation")

        # PDE
        pde_label = Text("Classical form:",
                        font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        pde = MathTex(
            r"- \Delta u = f \text{ on } \Omega, \quad u = 0 \text{ on } \partial\Omega",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(pde_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(pde, direction=DOWN, anchor=pde_label, buff=0.15)
        self.play(
            FadeIn(pde_label, shift=LEFT * 0.15),
            Write(pde),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(pde_label), FadeOut(pde), run_time=FAST)

        # Weak form
        weak_label = Text("Weak form (find u in H^1_0):",
                        font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        weak = MathTex(
            r"\int_\Omega \nabla u \cdot \nabla v\,dx = \int_\Omega f\,v\,dx \quad \forall\, v \in H^1_0",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(weak_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(weak, direction=DOWN, anchor=weak_label, buff=0.15)
        self.play(
            FadeIn(weak_label, shift=LEFT * 0.15),
            Write(weak),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(weak_label), FadeOut(weak), run_time=FAST)

        # Lax-Milgram applies
        apply = Text(
            "Bilinear form is bounded and coercive: unique solution exists!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(apply, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(apply, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(Indicate(apply), run_time=FAST)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Playlist Recap
    # ------------------------------------------------------------------ #
    def scene7_playlist_recap(self):
        self.add_subcaption(
            "Let us trace how the entire Functional Analysis playlist "
            "connects to PDEs. Normed and Banach spaces give the setting. "
            "Hilbert spaces give inner product structure. Bounded operators "
            "model differential operators. Dual spaces provide test functions. "
            "Weak topology gives compactness for existence proofs.",
            duration=12,
        )

        self.ly.section_divider(7, "The Full Picture")
        title = self.ly.title("How It All Connects")

        connections = [
            Text("Banach/Hilbert spaces: the setting for PDE analysis",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Bounded operators: differential operators as linear maps",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Dual spaces: test functions and distribution theory",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Weak topology: compactness for existence proofs",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Hahn-Banach + Lax-Milgram: existence and uniqueness",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(connections, start_from=title)
        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary
    # ------------------------------------------------------------------ #
    def scene8_summary(self):
        self.add_subcaption(
            "In this final video, we saw how functional analysis provides "
            "the foundation for modern PDE theory. Weak solutions, Sobolev "
            "spaces, and the Lax-Milgram theorem are direct applications "
            "of the abstract theory we built throughout this playlist.",
            duration=9,
        )

        self.ly.section_divider(8, "Key Takeaways")
        title = self.ly.title("Key Takeaways")

        items = [
            Text("Weak solutions require less regularity than classical ones",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Sobolev spaces are the natural home for weak solutions",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Lax-Milgram guarantees existence and uniqueness",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Gelfand triple: V, H, V* organize the duality",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Functional analysis is the language of modern PDE theory",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()
        play_outro(self, "End of Functional Analysis", "Functional Analysis")
