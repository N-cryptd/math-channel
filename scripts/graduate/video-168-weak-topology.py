"""
Video 168: Weak and Weak-* Topology -- Functional Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video168_WeakTopology

Topics: Motivation for weaker topologies,
        Review of norm topology and convergence,
        Weak convergence on X,
        Weak-* convergence on X*,
        Banach-Alaoglu theorem,
        Comparison of topologies,
        Applications (PDEs, optimization),
        Connection to reflexivity.

Prerequisites: Video 162 (Normed Spaces), Video 167 (The Dual Space).

Competitive insights:
- No Manim channel covers weak topologies with animations
- This is typically lecture-only content at the graduate level
- Unique opportunity: animated comparison of strong/weak/weak-* convergence
- Visual: nested topology circles showing fewer open sets = more compactness
- Color coding makes the topology hierarchy immediately clear

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


class Video168_WeakTopology(Scene):
    """Weak and Weak-* Topology -- Functional Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_norm_topology_review()
        self.scene3_weak_convergence()
        self.scene4_weak_star_convergence()
        self.scene5_banach_alaoglu()
        self.scene6_comparison()
        self.scene7_applications()
        self.scene8_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "In infinite dimensions, the closed unit ball is not compact "
            "in the norm topology. This is a serious problem for proving "
            "existence results. The solution: weaken the topology.",
            duration=9,
        )
        play_intro(self, "Weak and Weak-* Topology", "Functional Analysis")

        title = self.ly.title("Why Weaker Topologies?")

        items = [
            Text("Closed unit ball is NOT compact in infinite dimensions",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Compactness is essential for existence proofs",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Weakening the topology recovers compactness",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Norm Topology Review
    # ------------------------------------------------------------------ #
    def scene2_norm_topology_review(self):
        self.add_subcaption(
            "Recall that in the norm topology, a sequence converges "
            "when the norm of the difference goes to zero. This is "
            "the strongest form of convergence we consider.",
            duration=7,
        )

        self.ly.section_divider(2, "Norm Topology")
        title = self.ly.title("Norm (Strong) Convergence")

        # Definition
        label = Text("Norm convergence (strongest):",
                    font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        formula = MathTex(
            r"x_n \to x \iff \|x_n - x\| \to 0",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(formula, PRIMARY)
        self.ly.safe_place(label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=label, buff=0.2)
        self.play(
            FadeIn(label, shift=LEFT * 0.15),
            Write(formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(label), FadeOut(boxed), run_time=FAST)

        # Problem
        self.add_subcaption(
            "The problem: in infinite dimensions, the closed unit ball "
            "has no convergent subsequences. We cannot use compactness "
            "arguments with the norm topology.",
            duration=6,
        )

        prob_label = Text("Problem in infinite dimensions:",
                         font_size=BODY_SIZE, color=RED, font=SANS)
        prob = MathTex(
            r"B_1 = \{x \in X : \|x\| \leq 1\}",
            font_size=BODY_SIZE, color=RED,
        )
        not_compact = Text(
            "is NOT compact (no convergent subsequences)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(prob_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(prob, direction=DOWN, anchor=prob_label, buff=0.15)
        self.ly.safe_place(not_compact, direction=DOWN, anchor=prob, buff=0.15)
        self.play(
            FadeIn(prob_label, shift=LEFT * 0.15),
            Write(prob),
            FadeIn(not_compact, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(Indicate(not_compact), run_time=FAST)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Weak Convergence
    # ------------------------------------------------------------------ #
    def scene3_weak_convergence(self):
        self.add_subcaption(
            "Weak convergence requires that every bounded linear functional "
            "agrees the sequence converges. This is a weaker condition "
            "than norm convergence, meaning fewer sequences converge weakly.",
            duration=9,
        )

        self.ly.section_divider(3, "Weak Convergence")
        title = self.ly.title("Weak Convergence on X")

        # Definition
        label = Text("Weak convergence:",
                    font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        formula = MathTex(
            r"x_n \rightharpoonup x \iff f(x_n) \to f(x) \;\; \forall\, f \in X^*",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed = self.ly.formula_box(formula, SECONDARY)
        self.ly.safe_place(label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=label, buff=0.2)
        self.play(
            FadeIn(label, shift=LEFT * 0.15),
            Write(formula),
            run_time=SLOW,
        )
        self.wait(0.5)
        self.play(FadeOut(label), FadeOut(boxed), run_time=FAST)

        # Key facts
        self.add_subcaption(
            "Norm convergence implies weak convergence, but not vice versa. "
            "In reflexive spaces, the closed unit ball is weakly compact, "
            "which is the key tool for many existence proofs.",
            duration=8,
        )

        facts = [
            Text("Strong convergence implies weak convergence",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Converse is FALSE in infinite dimensions",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Unit ball is weakly compact if X is reflexive",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(facts, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Weak-* Convergence
    # ------------------------------------------------------------------ #
    def scene4_weak_star_convergence(self):
        self.add_subcaption(
            "The weak star topology lives on the dual space X star. "
            "A sequence of functionals converges weak star when they "
            "agree on convergence for every element of the original space X.",
            duration=8,
        )

        self.ly.section_divider(4, "Weak-* Convergence")
        title = self.ly.title("Weak-* Convergence on X*")

        # Definition
        label = Text("Weak-* convergence:",
                    font_size=BODY_SIZE, color=ACCENT, font=SANS)
        formula = MathTex(
            r"f_n \overset{*}{\rightharpoonup} f \iff f_n(x) \to f(x) \;\; \forall\, x \in X",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(formula, ACCENT)
        self.ly.safe_place(label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=label, buff=0.2)
        self.play(
            FadeIn(label, shift=LEFT * 0.15),
            Write(formula),
            run_time=SLOW,
        )
        self.wait(0.5)
        self.play(FadeOut(label), FadeOut(boxed), run_time=FAST)

        # Compare weak vs weak-*
        self.add_subcaption(
            "Weak star convergence is even weaker than weak convergence "
            "on X star. The key advantage: the closed unit ball of X star "
            "is always compact in the weak star topology.",
            duration=7,
        )

        compare = [
            Text("Weak-* is weaker than weak convergence on X*",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Fewer sequences converge (stronger requirement to prove)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("But the unit ball of X* is weak-* compact!",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(compare, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Banach-Alaoglu Theorem
    # ------------------------------------------------------------------ #
    def scene5_banach_alaoglu(self):
        self.add_subcaption(
            "The Banach-Alaoglu theorem is one of the most important "
            "results in functional analysis. It states that the closed "
            "unit ball of the dual space is always weak star compact.",
            duration=8,
        )

        self.ly.section_divider(5, "Banach-Alaoglu")
        title = self.ly.title("Banach-Alaoglu Theorem")

        # Statement
        stmt_label = Text("Theorem (Banach-Alaoglu):",
                         font_size=BODY_SIZE, color=RED, font=SANS)
        stmt = MathTex(
            r"B_1^* = \{f \in X^* : \|f\| \leq 1\}",
            font_size=BODY_SIZE, color=RED,
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

        # Compactness statement
        compact = Text(
            "is weak-* compact (ALWAYS, no completeness needed)",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(compact, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(compact, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(Indicate(compact), run_time=FAST)
        self.wait(0.5)
        self.play(FadeOut(compact), run_time=FAST)

        # Corollary
        self.add_subcaption(
            "As a corollary, in reflexive spaces the closed unit ball "
            "of the original space X is weakly compact. This connects "
            "back to the reflexivity we discussed in the dual space video.",
            duration=7,
        )

        cor_label = Text("Corollary (reflexive spaces):",
                        font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        cor = Text(
            "If X is reflexive, then B_1(X) is weakly compact",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(cor_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(cor, direction=DOWN, anchor=cor_label, buff=0.15)
        self.play(
            FadeIn(cor_label, shift=LEFT * 0.15),
            FadeIn(cor, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Comparison Diagram
    # ------------------------------------------------------------------ #
    def scene6_comparison(self):
        self.add_subcaption(
            "Let us compare the three topologies. The norm topology "
            "is the strongest, with the most open sets. The weak "
            "topology has fewer open sets, and the weak star topology "
            "has even fewer. Fewer open sets means more compactness.",
            duration=10,
        )

        self.ly.section_divider(6, "Topology Comparison")
        title = self.ly.title("Hierarchy of Topologies")

        # Three levels
        strong = Text("Norm topology (strongest)",
                     font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        weak = Text("Weak topology",
                   font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        weak_star = Text("Weak-* topology (weakest)",
                        font_size=HEADING_SIZE, color=ACCENT, font=SANS)

        # Stack them
        self.ly.safe_place(strong, direction=DOWN, anchor=title, buff=0.4)
        self.ly.safe_place(weak, direction=DOWN, anchor=strong, buff=0.4)
        self.ly.safe_place(weak_star, direction=DOWN, anchor=weak, buff=0.4)

        self.play(
            FadeIn(strong, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(
            FadeIn(weak, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(
            FadeIn(weak_star, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(strong), FadeOut(weak), FadeOut(weak_star), run_time=FAST)

        # Trade-off
        tradeoff = [
            Text("Weaker topology = fewer open sets",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("More sets are compact (good for existence!)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("But harder to work with analytically",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(tradeoff, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Applications
    # ------------------------------------------------------------------ #
    def scene7_applications(self):
        self.add_subcaption(
            "Weak and weak star topologies are essential tools in "
            "modern analysis. They are used to prove existence of "
            "solutions to PDEs, find minimizers of functionals, "
            "and construct many objects in functional analysis.",
            duration=9,
        )

        self.ly.section_divider(7, "Applications")
        title = self.ly.title("Why This Matters")

        apps = [
            Text("PDE existence: weak compactness finds solutions",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Optimization: continuous functions on compact sets",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Calculus of variations: energy minimizers",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Spectral theory: weak convergence of eigenfunctions",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(apps, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary
    # ------------------------------------------------------------------ #
    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap what we have learned. The norm topology is "
            "strong but lacks compactness in infinite dimensions. "
            "Weak and weak star topologies trade analytical convenience "
            "for compactness, enabling powerful existence results.",
            duration=9,
        )

        self.ly.section_divider(8, "Key Takeaways")
        title = self.ly.title("Key Takeaways")

        items = [
            Text("Norm convergence: strongest, but no compactness in infinite dim",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Weak convergence: f(x_n) to f(x) for all f in X star",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Weak-* convergence: f_n(x) to f(x) for all x in X",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Banach-Alaoglu: unit ball of X* is weak-* compact",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Trade-off: weaker topology means more compactness",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()
        play_outro(self, "Compact Operators", "Functional Analysis")
