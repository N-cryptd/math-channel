"""
Video 208: The Fundamental Group — Algebraic Topology
pi_1(X, x_0): loops up to homotopy, group structure, pi_1(S^1) = Z,
simply connected spaces, homotopy invariance.

QUALITY RULES:
1. Max 5 visible elements per scene
2. LayoutEngine for ALL positioning
3. Progressive disclosure
4. Raw strings with single backslashes for LaTeX
5. ly.clear() between scenes

NARRATION TIMING (v2 fix):
- Duration set to ceil(words / 2.2) + 1 for natural TTS pace
- self.wait() added after animations to fill caption window
- No overlapping SRT segments — each next caption starts after previous ends
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


class Video208_FundamentalGroup(Scene):
    """The fundamental group: loops, homotopy classes, and algebraic topology."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_group_operation()
        self.scene4_circle_example()
        self.scene5_simply_connected()
        self.scene6_homotopy_invariance()
        self.scene7_summary()

    # ── Scene 1: Hook — Loops That Can't Be Untied ────────────────────
    def scene1_hook(self):
        """Motivating hook: loops around a hole vs loops in a disk."""
        # 30 words → duration=15
        self.add_subcaption(
            "Welcome back to Algebraic Topology! In the last video we studied "
            "homotopy, the idea of continuous deformation. Today we turn that "
            "idea into a powerful algebraic tool: the fundamental group.",
            duration=15,
        )
        play_intro(self, "The Fundamental Group", "Algebraic Topology")
        # play_intro ~6s, remaining ~9s filled by wait
        self.wait(8)

        # 43 words → duration=21
        self.add_subcaption(
            "Imagine a loop of string sitting on a flat table. You can shrink "
            "it down to a point without any trouble. But wrap that string around "
            "a pole, and suddenly it is trapped. The pole creates a hole that "
            "the loop cannot cross.",
            duration=21,
        )
        title = self.ly.title("Loops That Can't Be Untied")

        # Flat disk with loop
        disk = Circle(radius=1.3, color=PRIMARY, stroke_width=3, fill_opacity=0.08)
        loop_disk = Circle(radius=0.6, color=SECONDARY, stroke_width=2.5)
        disk.move_to(LEFT * 2.8)
        loop_disk.move_to(LEFT * 2.8)

        # Circle (S^1) with loop around it
        circle_space = Circle(radius=1.3, color=PRIMARY, stroke_width=3, fill_opacity=0.08)
        hole = Dot(color=RED, radius=0.15)
        loop_hole = Circle(radius=1.0, color=SECONDARY, stroke_width=2.5)
        circle_space.move_to(RIGHT * 2.8)
        hole.move_to(RIGHT * 2.8)
        loop_hole.move_to(RIGHT * 2.8)

        self.ly.safe_place(disk, LEFT, anchor=title, buff=0.7)
        self.ly.safe_place(circle_space, RIGHT, anchor=title, buff=0.7)

        self.play(
            FadeIn(disk), Create(loop_disk),
            FadeIn(circle_space), Create(loop_hole),
            run_time=FAST,
        )

        # Labels
        lbl_disk = Text("Contractible", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)
        lbl_disk.next_to(disk, DOWN, buff=0.15)
        lbl_hole = Text("Non-contractible", font_size=LABEL_SIZE, color=RED, font=SANS)
        lbl_hole.next_to(circle_space, DOWN, buff=0.15)

        self.play(FadeIn(lbl_disk), FadeIn(lbl_hole), run_time=FAST)
        # Animations ~1.2s, fill remaining ~19s
        self.wait(18)

        self.ly.clear()

        # 32 words → duration=16
        self.add_subcaption(
            "The fundamental group captures exactly this distinction. It turns "
            "the topology of holes into algebra. A flat disk has a trivial "
            "fundamental group, while a circle has a non-trivial one: the integers.",
            duration=16,
        )
        title2 = self.ly.title("From Loops to Algebra")
        items = [
            Text("Topology of holes becomes algebra", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Flat disk: trivial fundamental group", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Circle: fundamental group is the integers", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        # progressive_reveal ~2s, fill remaining ~14s
        self.wait(13)
        self.ly.clear()

    # ── Scene 2: Definition — pi_1(X, x_0) ───────────────────────────
    def scene2_definition(self):
        """Formal definition of the fundamental group."""
        # 28 words → duration=14
        self.add_subcaption(
            "To define the fundamental group precisely, we need three ingredients: "
            "a space X, a base point x naught, and the idea of a loop based at x naught.",
            duration=14,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("Loops at a Base Point")

        # Base point + loop visual
        base_dot = Dot(color=ACCENT, radius=0.08)
        base_label = MathTex(r"x_0", font_size=LABEL_SIZE, color=ACCENT)
        base_label.next_to(base_dot, DOWN, buff=0.15)
        loop = Circle(radius=1.2, color=PRIMARY, stroke_width=2.5)
        arrow_tip = CurvedArrow(
            base_dot.get_center(),
            base_dot.get_center() + UP * 0.5 + RIGHT * 0.3,
            angle=-TAU / 4, color=PRIMARY, stroke_width=2.5,
        )

        group = VGroup(base_dot, base_label, loop)
        self.ly.safe_place(group, DOWN, anchor=title, buff=0.5)
        self.ly.center_in_content(group)

        self.play(
            FadeIn(base_dot), FadeIn(base_label),
            Create(loop), run_time=NORMAL,
        )

        loop_defn = MathTex(
            r"\gamma : [0,1] \to X, \quad \gamma(0) = \gamma(1) = x_0",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(loop_defn, DOWN, anchor=group, buff=0.5)
        self.play(Write(loop_defn), run_time=NORMAL)
        # Animations ~2.4s, fill remaining ~11s
        self.wait(10)
        self.ly.clear()

        # 28 words → duration=14
        self.add_subcaption(
            "Two loops gamma and sigma based at x naught are equivalent if there "
            "exists a path homotopy between them that keeps the base point fixed "
            "throughout the deformation.",
            duration=14,
        )
        title2 = self.ly.title("Homotopy Classes of Loops")

        equiv_defn = MathTex(
            r"\gamma, \sigma \text{ loops at } x_0, \quad "
            r"\gamma \simeq \sigma \text{ rel } \{0, 1\}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(equiv_defn, DOWN, anchor=title2, buff=0.5)
        self.play(Write(equiv_defn), run_time=NORMAL)

        # Fix base point constraint
        fix_constraint = MathTex(
            r"H(0, t) = H(1, t) = x_0 \quad \forall\, t \in [0,1]",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(fix_constraint, DOWN, anchor=equiv_defn, buff=0.5)
        self.play(Write(fix_constraint), run_time=NORMAL)
        # Animations ~2.4s, fill remaining ~11s
        self.wait(10)
        self.ly.clear()

        # 31 words → duration=15
        self.add_subcaption(
            "The fundamental group pi one of X at x naught is the set of all "
            "homotopy classes of loops at x naught, equipped with a group "
            "operation we will define next.",
            duration=15,
        )
        title3 = self.ly.title("The Fundamental Group")

        pi_defn = MathTex(
            r"\pi_1(X, x_0) = \{[\gamma] \mid \gamma \text{ is a loop at } x_0\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_pi = self.ly.formula_box(pi_defn, color=PRIMARY)
        self.ly.safe_place(boxed_pi, DOWN, anchor=title3, buff=0.6)
        self.play(FadeIn(boxed_pi), run_time=NORMAL)

        class_text = Text(
            "where [gamma] is the homotopy class of gamma",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(class_text, DOWN, anchor=boxed_pi, buff=0.5)
        self.play(FadeIn(class_text, shift=LEFT * 0.15), run_time=FAST)
        # Animations ~1.8s, fill remaining ~13s
        self.wait(12)
        self.ly.clear()

    # ── Scene 3: Group Operation — Concatenation ──────────────────────
    def scene3_group_operation(self):
        """Loop concatenation gives a group structure."""
        # 22 words → duration=11
        self.add_subcaption(
            "How do we make homotopy classes of loops into a group? "
            "The operation is concatenation: run loop alpha first, then loop beta.",
            duration=11,
        )
        self.ly.section_divider(2, "Group Operation")

        title = self.ly.title("Concatenation of Loops")

        # Two loops visual
        loop_a = Circle(radius=0.8, color=PRIMARY, stroke_width=2.5)
        loop_b = Circle(radius=0.8, color=SECONDARY, stroke_width=2.5)
        loop_a.move_to(LEFT * 2.5)
        loop_b.move_to(RIGHT * 2.5)
        dot_ab = Dot(color=ACCENT, radius=0.06)

        self.ly.safe_place(loop_a, LEFT, anchor=title, buff=0.7)
        self.ly.safe_place(loop_b, RIGHT, anchor=title, buff=0.7)

        self.play(Create(loop_a), Create(loop_b), FadeIn(dot_ab), run_time=FAST)

        label_a = MathTex(r"\alpha", font_size=LABEL_SIZE, color=PRIMARY)
        label_a.next_to(loop_a, DOWN, buff=0.15)
        label_b = MathTex(r"\beta", font_size=LABEL_SIZE, color=SECONDARY)
        label_b.next_to(loop_b, DOWN, buff=0.15)
        self.play(Write(label_a), Write(label_b), run_time=FAST)
        # Animations ~1.2s, fill remaining ~9s
        self.wait(8)

        # Remove loops before showing formula
        self.play(
            FadeOut(loop_a), FadeOut(loop_b),
            FadeOut(label_a), FadeOut(label_b), FadeOut(dot_ab),
            run_time=FAST,
        )

        # Concatenation definition
        concat_defn = MathTex(
            r"(\alpha * \beta)(s) = "
            r"\begin{cases}"
            r"\alpha(2s) & 0 \le s \le 1/2 \\"
            r"\beta(2s - 1) & 1/2 \le s \le 1"
            r"\end{cases}",
            font_size=BODY_SIZE, color=WHITE,
        )
        boxed_concat = self.ly.formula_box(concat_defn, color=PRIMARY)
        self.ly.safe_place(boxed_concat, DOWN, anchor=title, buff=0.7)
        self.play(FadeIn(boxed_concat), run_time=NORMAL)
        # Animations ~1.8s, fill remaining ~7s (within the same caption window if we extend, or just good pause)
        self.wait(6)
        self.ly.clear()

        # 26 words → duration=13
        self.add_subcaption(
            "Concatenation descends to homotopy classes and satisfies all "
            "group axioms. The identity element is the constant loop at x naught, "
            "which never leaves the base point.",
            duration=13,
        )
        title2 = self.ly.title("Group Axioms")

        identity = MathTex(
            r"e = [\text{const}_{x_0}]",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(identity, DOWN, anchor=title2, buff=0.5)
        self.play(Write(identity), run_time=FAST)

        inverse_def = MathTex(
            r"\alpha^{-1}(s) = \alpha(1 - s)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(inverse_def, DOWN, anchor=identity, buff=0.5)
        self.play(Write(inverse_def), run_time=FAST)
        # Animations ~1.2s, fill remaining ~11s
        self.wait(10)

        # 29 words → duration=14
        self.add_subcaption(
            "The inverse of alpha is alpha traversed backwards. "
            "Concatenating alpha with its inverse gives a loop homotopic to "
            "the constant loop, as the two halves cancel each other out.",
            duration=14,
        )
        cancel = MathTex(
            r"[\alpha] * [\alpha^{-1}] = [e]",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(cancel, DOWN, anchor=inverse_def, buff=0.5)
        self.play(Write(cancel), run_time=NORMAL)
        # Animations ~1.2s, fill remaining ~12s
        self.wait(11)

        # Properties list
        self.ly.clear()
        # 25 words → duration=13
        self.add_subcaption(
            "Associativity holds up to homotopy, though the reparametrization "
            "is important. The operation is associative because rescaling the "
            "parameter interval does not change the homotopy class.",
            duration=13,
        )
        title3 = self.ly.title("Key Properties")
        items = [
            Text("Associativity: (alpha * beta) * gamma = alpha * (beta * gamma)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Identity: alpha * e = alpha = e * alpha",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Inverses: alpha * alpha^(-1) = e",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title3)
        # Animations ~2s, fill remaining ~11s
        self.wait(10)
        self.ly.clear()

    # ── Scene 4: Example — pi_1(S^1) = Z ─────────────────────────────
    def scene4_circle_example(self):
        """The fundamental group of the circle is the integers."""
        # 29 words → duration=14
        self.add_subcaption(
            "The canonical example: what is the fundamental group of the circle? "
            "The answer is the integers, where each integer counts how many times "
            "a loop winds around the circle.",
            duration=14,
        )
        self.ly.section_divider(3, "The Circle")

        title = self.ly.title(r"pi_1(S^1) = Z")

        # Circle with winding number visual
        s1_circle = Circle(radius=1.5, color=PRIMARY, stroke_width=3)
        self.ly.safe_place(s1_circle, DOWN, anchor=title, buff=0.6)
        self.ly.center_in_content(s1_circle)

        self.play(Create(s1_circle), run_time=NORMAL)
        # Animations ~1.2s, fill remaining ~12s
        self.wait(11)

        # 27 words → duration=14
        self.add_subcaption(
            "A loop that goes once around the circle counterclockwise has "
            "winding number one. Going around twice gives winding number two, "
            "and going backwards gives negative winding numbers.",
            duration=14,
        )
        w1_label = MathTex(r"n = 1", font_size=LABEL_SIZE, color=SECONDARY)
        w1_label.next_to(s1_circle, RIGHT, buff=0.3)
        self.play(Write(w1_label), run_time=FAST)
        # Animations ~0.6s, fill remaining ~13s
        self.wait(12)
        self.ly.clear()

        # Winding numbers gallery
        # No new subcaption here — same caption window continues or we add a new one
        title2 = self.ly.title("Winding Number")

        # Show n = 0, n = 1, n = -1 as text items
        w0 = VGroup(
            MathTex(r"n = 0", font_size=BODY_SIZE, color=WHITE),
            Text("constant loop", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.15)

        w1 = VGroup(
            MathTex(r"n = 1", font_size=BODY_SIZE, color=SECONDARY),
            Text("once around", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.15)

        w_neg1 = VGroup(
            MathTex(r"n = -1", font_size=BODY_SIZE, color=RED),
            Text("once around backwards", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.15)

        items = [w0, w1, w_neg1]
        self.ly.progressive_reveal(items, start_from=title2)
        # Animations ~2s
        self.wait(10)
        self.ly.clear()

        # 29 words → duration=14
        self.add_subcaption(
            "This is the deep theorem: the fundamental group of the circle "
            "is isomorphic to the integers. Each homotopy class of loops "
            "corresponds to exactly one integer, its winding number.",
            duration=14,
        )
        title3 = self.ly.title("The Fundamental Theorem")

        theorem = MathTex(
            r"\pi_1(S^1) \cong \mathbb{Z}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_thm = self.ly.formula_box(theorem, color=PRIMARY)
        self.ly.safe_place(boxed_thm, DOWN, anchor=title3, buff=0.7)
        self.play(FadeIn(boxed_thm), run_time=NORMAL)

        explanation = Text(
            "Each integer = one homotopy class of loops",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(explanation, DOWN, anchor=boxed_thm, buff=0.5)
        self.play(FadeIn(explanation, shift=LEFT * 0.15), run_time=NORMAL)
        # Animations ~1.8s, fill remaining ~12s
        self.wait(11)
        self.ly.clear()

    # ── Scene 5: Simply Connected Spaces ───────────────────────────────
    def scene5_simply_connected(self):
        """Simply connected: trivial fundamental group."""
        # 26 words → duration=13
        self.add_subcaption(
            "A space is simply connected if every loop can be continuously "
            "shrunk to a point. Equivalently, its fundamental group is trivial, "
            "containing only the identity element.",
            duration=13,
        )
        self.ly.section_divider(4, "Simply Connected Spaces")

        title = self.ly.title("Simply Connected Spaces")

        definition = MathTex(
            r"X \text{ simply connected} \iff \pi_1(X, x_0) = \{e\}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(definition, DOWN, anchor=title, buff=0.5)
        self.play(Write(definition), run_time=NORMAL)
        # Animations ~1.2s, fill remaining ~11s
        self.wait(10)
        self.ly.clear()

        # 33 words → duration=16
        self.add_subcaption(
            "Every point in a simply connected space can be connected to every "
            "other point by a path, and every loop is contractible. "
            "The disk, the sphere, and all convex sets are simply connected.",
            duration=16,
        )
        title2 = self.ly.title("Examples")

        disk_ex = VGroup(
            MathTex(r"\mathbb{R}^n", font_size=BODY_SIZE, color=PRIMARY),
            Text("Euclidean space", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.15)

        sphere_ex = VGroup(
            MathTex(r"S^n \;(n \ge 2)", font_size=BODY_SIZE, color=SECONDARY),
            Text("higher spheres", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.15)

        convex_ex = VGroup(
            Text("Any convex set", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("disks, balls, cubes", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.15)

        items = [disk_ex, sphere_ex, convex_ex]
        self.ly.progressive_reveal(items, start_from=title2)
        # Animations ~2s, fill remaining ~14s
        self.wait(13)
        self.ly.clear()

        # 31 words → duration=15
        self.add_subcaption(
            "In fact, every contractible space is simply connected. A contractible "
            "space can be continuously shrunk to a point, so any loop inside it "
            "can certainly be shrunk to the constant loop.",
            duration=15,
        )
        title3 = self.ly.title("Contractible Implies Simply Connected")

        impl = MathTex(
            r"X \text{ contractible} \implies \pi_1(X, x_0) = \{e\}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(impl, DOWN, anchor=title3, buff=0.5)
        self.play(Write(impl), run_time=NORMAL)
        # Fill remaining 13s of the 15s caption window before next subcaption
        self.wait(13)

        # 31 words → duration=15
        self.add_subcaption(
            "For instance, a solid disk is contractible: we can retract "
            "every point toward the center. Since the disk is contractible, "
            "every loop in the disk is homotopic to the constant loop.",
            duration=15,
        )
        shrink_disk = Circle(radius=1.0, color=SECONDARY, stroke_width=2.5, fill_opacity=0.1)
        self.ly.safe_place(shrink_disk, DOWN, anchor=impl, buff=0.6)
        self.play(Create(shrink_disk), run_time=FAST)

        shrink_dot = Dot(color=ACCENT, radius=0.06)
        self.play(Transform(shrink_disk, shrink_dot), run_time=2.0)
        # Animations ~3.8s, fill remaining ~11s
        self.wait(10)
        self.ly.clear()

    # ── Scene 6: Homotopy Invariance ──────────────────────────────────
    def scene6_homotopy_invariance(self):
        """The fundamental group is a homotopy invariant."""
        # 24 words → duration=12
        self.add_subcaption(
            "One of the most powerful properties of the fundamental group "
            "is homotopy invariance: if two spaces are homotopy equivalent, "
            "they have isomorphic fundamental groups.",
            duration=12,
        )
        self.ly.section_divider(5, "Homotopy Invariance")

        title = self.ly.title("Homotopy Invariance")

        invariant = MathTex(
            r"X \simeq Y \implies \pi_1(X) \cong \pi_1(Y)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_inv = self.ly.formula_box(invariant, color=PRIMARY)
        self.ly.safe_place(boxed_inv, DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(boxed_inv), run_time=NORMAL)
        # Animations ~1.2s, fill remaining ~10s
        self.wait(9)
        self.ly.clear()

        # 32 words → duration=16
        self.add_subcaption(
            "This means the fundamental group is a topological invariant. "
            "If two spaces have different fundamental groups, they cannot be "
            "homotopy equivalent. This gives us a concrete algebraic test "
            "to distinguish topological spaces.",
            duration=16,
        )
        title2 = self.ly.title("Consequences")

        items = [
            Text("Algebraic test: different pi_1 means different spaces",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"\pi_1(S^1) = \mathbb{Z}, \quad \pi_1(S^2) = \{e\}",
                    font_size=BODY_SIZE, color=PRIMARY),
            Text("So S^1 is NOT homotopy equivalent to S^2",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        # Animations ~2s, fill remaining ~14s
        self.wait(13)
        self.ly.clear()

        # 30 words → duration=15
        self.add_subcaption(
            "More examples: the punctured plane has fundamental group Z, "
            "since it is homotopy equivalent to a circle. The torus has "
            "fundamental group Z cross Z, reflecting its two independent holes.",
            duration=15,
        )
        title3 = self.ly.title("Computing pi_1 by Equivalence")

        punctured = VGroup(
            MathTex(r"\pi_1(\mathbb{R}^2 \setminus \{0\}) = \mathbb{Z}",
                    font_size=BODY_SIZE, color=PRIMARY),
            Text("(punctured plane = circle)", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.15)

        torus = VGroup(
            MathTex(r"\pi_1(T^2) = \mathbb{Z} \times \mathbb{Z}",
                    font_size=BODY_SIZE, color=SECONDARY),
            Text("(two independent loops)", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.15)

        items2 = [punctured, torus]
        self.ly.progressive_reveal(items2, start_from=title3)
        # Animations ~2s, fill remaining ~13s
        self.wait(12)
        self.ly.clear()

    # ── Scene 7: Summary + Teaser ──────────────────────────────────────
    def scene7_summary(self):
        """Summary of concepts and teaser for Video 209."""
        # 33 words → duration=16
        self.add_subcaption(
            "Let us summarize what we have learned. The fundamental group "
            "pi_1 of X at x naught is the set of homotopy classes of loops "
            "at x naught, with concatenation as the group operation.",
            duration=16,
        )
        self.ly.section_divider(6, "Summary")

        title = self.ly.title("Key Takeaways")

        items = [
            Text("pi_1(X, x_0): homotopy classes of loops at x naught",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Group operation: concatenation of loops",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("pi_1(S^1) = Z: winding number classifies loops",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Homotopy invariant: distinguishes non-equivalent spaces",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        # Animations ~2.5s, fill remaining ~13s
        self.wait(12)
        self.ly.clear()

        # 27 words → duration=14
        self.add_subcaption(
            "The fundamental group is our first bridge between topology and "
            "algebra. It is a powerful invariant that captures the essence "
            "of the hole structure of a space.",
            duration=14,
        )
        title2 = self.ly.title("The Big Picture")
        summary_box = self.ly.formula_box(
            MathTex(
                r"\pi_1(X, x_0) = "
                r"\{[\gamma] \mid \gamma(0)=\gamma(1)=x_0\}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            color=PRIMARY,
        )
        self.ly.safe_place(summary_box, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(summary_box), run_time=NORMAL)
        # Animations ~1.2s, fill remaining ~12s
        self.wait(11)
        self.ly.clear()

        # 35 words → duration=20 (generous for TTS natural pace)
        self.add_subcaption(
            "In the next video, we will explore the covering space approach "
            "to computing fundamental groups, and see how higher homotopy "
            "groups pi_n capture even more about the structure of a space. "
            "Thank you for watching!",
            duration=20,
        )
        play_outro(self, "Covering Spaces", "Algebraic Topology")
        # Ensure video extends to cover the full 20s caption window
        self.wait(6)
