"""
Video 212: Singular Homology — Algebraic Topology
Singular simplices (maps from standard simplex), singular chain complex C_n(X),
singular homology groups H_n(X), comparison with simplicial homology,
and homotopy invariance theorem.

QUALITY RULES:
1. Max 5 visible elements per scene
2. LayoutEngine for ALL positioning
3. Progressive disclosure
4. Raw strings with single backslashes for LaTeX
5. ly.clear() between scenes
6. Narration timing: ~2.5 words/sec minimum duration
7. Each scene needs self.wait(5-8) after animations for narration to breathe
8. ONE subcaption per scene — generous duration
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


class Video212_SingularHomology(Scene):
    """Singular Homology: homology for arbitrary topological spaces."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_singular_simplices()
        self.scene3_singular_chain_complex()
        self.scene4_singular_homology_groups()
        self.scene5_computing_examples()
        self.scene6_comparison_simplicial()
        self.scene7_homotopy_invariance()
        self.scene8_summary()

    # ── Scene 1: Hook ──────────────────────────────────────────────
    def scene1_hook(self):
        """Hook — why we need singular homology beyond simplicial."""
        self.add_subcaption(
            "In the last video, we built simplicial homology by triangulating "
            "a space into simplices and computing chain complexes. This gave us "
            "powerful algebraic invariants that count holes. But there is a "
            "fundamental limitation: simplicial homology only works for "
            "spaces that can be triangulated.",
            duration=14,
        )
        play_intro(self, "Singular Homology", "Algebraic Topology")
        self.wait(8)

        self.add_subcaption(
            "Many important spaces cannot be triangulated, or a triangulation "
            "is hard to find. The torus, the Klein bottle, and infinite-dimensional "
            "spaces like function spaces are examples. We need a version of homology "
            "that works for every topological space, without requiring a "
            "combinatorial decomposition.",
            duration=14,
        )
        title = self.ly.title("Homology Without Triangulation")
        self.wait(2)

        items = [
            Text("Simplicial: requires a triangulation", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Singular: works for ANY topological space", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Key tool: continuous maps from a standard simplex", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)

        self.add_subcaption(
            "The beautiful idea is to replace actual simplices in the space with "
            "maps from the standard simplex into the space. By considering all "
            "such maps, we get homology groups that are invariant under "
            "homotopy equivalence, giving us a truly topological invariant. "
            "Let us begin with the definition of singular simplices.",
            duration=14,
        )
        roadmap = [
            Text("Singular simplices: maps from the standard simplex", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Singular chain complex: infinite-dimensional groups", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Homotopy invariance: the key theorem", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(roadmap)
        self.wait(6)
        self.ly.clear()

    # ── Scene 2: Singular Simplices ──────────────────────────────────
    def scene2_singular_simplices(self):
        """Definition of singular simplices and the standard simplex."""
        self.add_subcaption(
            "The foundation of singular homology is the notion of a singular "
            "simplex. Unlike simplicial homology where simplices are actual "
            "pieces of the space, here a singular simplex is a continuous map "
            "from the standard geometric simplex into the space.",
            duration=14,
        )
        self.ly.section_divider(1, "Singular Simplices")
        self.wait(3)

        title = self.ly.title("The Standard Simplex")
        self.wait(1)

        self.add_subcaption(
            "The standard n-simplex, denoted Delta^n, is the convex hull of "
            "the standard basis vectors e_0, e_1, through e_n in "
            "R^{n+1}. For n equal to 0, it is a single point. For n equal "
            "to 1, it is the line segment from 0 to 1. For n equal to 2, "
            "it is a triangle in R^3.",
            duration=14,
        )
        defn = MathTex(
            r"\Delta^n = \left\{ "
            r"\sum_{i=0}^{n} t_i e_i \;:\; "
            r"t_i \geq 0,\; \sum_{i=0}^{n} t_i = 1 "
            r"\right\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_defn = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.safe_place(boxed_defn, DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(boxed_defn), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "Here the coefficients t_i are called barycentric coordinates. "
            "They tell us how much of each vertex contributes to the point. "
            "The condition that the t_i sum to 1 keeps us inside the simplex.",
            duration=11,
        )
        note = Text(
            "t_i are barycentric coordinates (all non-negative, sum to 1)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=boxed_defn, buff=0.5)
        self.play(FadeIn(note), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "Now we define the key object. A singular n-simplex in a "
            "topological space X is simply a continuous map from the "
            "standard n-simplex into X. The map itself is the simplex. "
            "The image of the map is a possibly curved, possibly degenerate "
            "copy of Delta^n sitting inside X.",
            duration=16,
        )
        title2 = self.ly.title("Definition: Singular Simplex")
        self.wait(1)

        defn2 = MathTex(
            r"\sigma \;:\; \Delta^n \longrightarrow X \quad "
            r"\text{(continuous)}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_defn2 = self.ly.formula_box(defn2, color=ACCENT)
        self.ly.safe_place(boxed_defn2, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(boxed_defn2), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "This is a huge generalization. A singular 1-simplex is any "
            "continuous path in X. A singular 2-simplex is any continuous "
            "map from a triangle into X, which could be a smooth surface, "
            "a crumpled shape, or even a constant map. The space could have "
            "infinitely many singular simplices.",
            duration=15,
        )
        examples = [
            Text("Singular 1-simplex: any continuous path in X", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Singular 2-simplex: any continuous map from a triangle", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Could be smooth, crumpled, or constant", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(examples, start_from=boxed_defn2)
        self.wait(6)
        self.ly.clear()

    # ── Scene 3: Singular Chain Complex ──────────────────────────────
    def scene3_singular_chain_complex(self):
        """Singular chain groups C_n(X), boundary maps, and the chain complex."""
        self.add_subcaption(
            "From singular simplices, we build singular chain groups. The "
            "n-th singular chain group C_n(X) is the free abelian group "
            "generated by all singular n-simplices in X. Because there can "
            "be infinitely many, this group is typically infinite-dimensional.",
            duration=15,
        )
        self.ly.section_divider(2, "Singular Chain Complex")
        self.wait(3)

        title = self.ly.title("Singular Chain Groups")
        self.wait(1)

        defn = MathTex(
            r"C_n(X) = \bigoplus_{\sigma : \Delta^n \to X} \mathbb{Z} "
            r"\cdot \sigma",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_defn = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.safe_place(boxed_defn, DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(boxed_defn), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "An element of C_n(X) is a formal linear combination of singular "
            "n-simplices with integer coefficients. The key difference from "
            "simplicial homology is that the generators are all continuous "
            "maps, not just the simplices of a triangulation. This means "
            "C_n(X) is enormous, but it carries no more information than X.",
            duration=15,
        )
        note = Text(
            "Generators = ALL continuous maps Delta^n -> X",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=boxed_defn, buff=0.5)
        self.play(FadeIn(note), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "The boundary map is defined analogously to the simplicial case. "
            "The boundary of a singular n-simplex sigma is the alternating "
            "sum of its restrictions to the faces of the standard simplex. "
            "For a singular 2-simplex sigma, the boundary is sigma composed "
            "with the first face map, minus sigma composed with the second, "
            "plus sigma composed with the third.",
            duration=18,
        )
        title2 = self.ly.title("The Boundary Map")
        self.wait(1)

        bnd = MathTex(
            r"\partial_n(\sigma) = \sum_{i=0}^{n} (-1)^i \; "
            r"\sigma \circ \delta_i",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_bnd = self.ly.formula_box(bnd, color=PRIMARY)
        self.ly.safe_place(boxed_bnd, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(boxed_bnd), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "Here delta_i is the i-th face map, which embeds the standard "
            "(n-1)-simplex as the i-th face of the standard n-simplex by "
            "omitting vertex i. The composition sigma circle delta_i "
            "restricts sigma to the i-th face, giving a singular "
            "(n-1)-simplex.",
            duration=14,
        )
        face_map = MathTex(
            r"\delta_i : \Delta^{n-1} \hookrightarrow \Delta^n "
            r"\quad \text{(omit vertex } v_i\text{)}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(face_map, DOWN, anchor=boxed_bnd, buff=0.5)
        self.play(FadeIn(face_map), run_time=NORMAL)
        self.wait(6)
        self.ly.clear()

        self.add_subcaption(
            "The boundary maps assemble into the singular chain complex, "
            "a sequence of abelian groups connected by boundary "
            "homomorphisms. As before, the fundamental property holds: "
            "the boundary of a boundary is zero. This follows from the "
            "combinatorial identity that each (n-2)-face of the standard "
            "n-simplex appears twice with opposite signs.",
            duration=17,
        )
        title3 = self.ly.title("The Singular Chain Complex")
        self.wait(1)

        seq = MathTex(
            r"\cdots \xrightarrow{\partial_3} C_2(X) "
            r"\xrightarrow{\partial_2} C_1(X) "
            r"\xrightarrow{\partial_1} C_0(X) "
            r"\xrightarrow{\partial_0} 0",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_seq = self.ly.formula_box(seq, color=PRIMARY)
        self.ly.safe_place(boxed_seq, DOWN, anchor=title3, buff=0.6)
        self.play(FadeIn(boxed_seq), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "The key property is exactly the same as in the simplicial case: "
            "the composition of two consecutive boundary maps is the zero "
            "map. This is a combinatorial fact about the face maps, not "
            "about any particular space.",
            duration=12,
        )
        prop = MathTex(
            r"\partial_n \circ \partial_{n+1} = 0",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_prop = self.ly.formula_box(prop, color=ACCENT)
        self.ly.safe_place(boxed_prop, DOWN, anchor=boxed_seq, buff=0.5)
        self.play(FadeIn(boxed_prop), run_time=NORMAL)
        self.wait(6)
        self.ly.clear()

    # ── Scene 4: Singular Homology Groups ────────────────────────────
    def scene4_singular_homology_groups(self):
        """Definition of H_n(X) = ker(d_n) / im(d_{n+1})."""
        self.add_subcaption(
            "With the chain complex in hand, the definition of singular "
            "homology is formally identical to simplicial homology. The "
            "n-th singular homology group is the quotient of n-cycles by "
            "n-boundaries in the singular chain complex of X.",
            duration=14,
        )
        self.ly.section_divider(3, "Singular Homology Groups")
        self.wait(3)

        title = self.ly.title("Cycles and Boundaries")
        self.wait(1)

        self.add_subcaption(
            "A singular n-cycle is a chain in C_n(X) whose boundary is zero. "
            "These are formal sums of singular simplices that, when their "
            "boundaries are taken with alternating signs, cancel out. "
            "The singular n-cycles form the kernel of the boundary map.",
            duration=14,
        )
        cycles = MathTex(
            r"Z_n(X) = \ker(\partial_n) = \{ c \in C_n(X) : "
            r"\partial_n(c) = 0 \}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_cycles = self.ly.formula_box(cycles, color=PRIMARY)
        self.ly.safe_place(boxed_cycles, DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(boxed_cycles), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "A singular n-boundary is a chain that equals the boundary of "
            "something one dimension higher. These are chains that fill in "
            "a region, even if that region is curved or distorted. "
            "The n-boundaries form the image of the boundary map from "
            "C_{n+1}(X).",
            duration=14,
        )
        title2 = self.ly.title("Boundaries")
        self.wait(1)

        bounds = MathTex(
            r"B_n(X) = \operatorname{im}(\partial_{n+1})",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed_bounds = self.ly.formula_box(bounds, color=SECONDARY)
        self.ly.safe_place(boxed_bounds, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(boxed_bounds), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "Since the boundary of a boundary is zero, every n-boundary is "
            "automatically an n-cycle. The boundaries form a subgroup of "
            "the cycles, exactly as in the simplicial theory.",
            duration=10,
        )
        subset = MathTex(
            r"B_n(X) \subseteq Z_n(X) \subseteq C_n(X)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(subset, DOWN, anchor=boxed_bounds, buff=0.5)
        self.play(FadeIn(subset), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "The n-th singular homology group of X is the quotient of "
            "singular n-cycles by singular n-boundaries. Two cycles are "
            "homologous if their difference is a boundary, meaning one can "
            "be filled in by singular simplices from the other. The homology "
            "group captures the essential n-dimensional holes in X.",
            duration=17,
        )
        title3 = self.ly.title("The Singular Homology Group")
        self.wait(1)

        hom = MathTex(
            r"H_n(X) = Z_n(X) \,/\, B_n(X) = "
            r"\ker(\partial_n) \,/\, "
            r"\operatorname{im}(\partial_{n+1})",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_hom = self.ly.formula_box(hom, color=ACCENT)
        self.ly.safe_place(boxed_hom, DOWN, anchor=title3, buff=0.6)
        self.play(FadeIn(boxed_hom), run_time=NORMAL)
        self.wait(6)

        self.add_subcaption(
            "The reduced homology is a slight variant where we replace C_0 "
            "with the augmentation ideal, making the homology of a "
            "contractible space trivial in all degrees, including degree "
            "zero. We use a tilde notation for the reduced groups.",
            duration=13,
        )
        reduced = MathTex(
            r"\widetilde{H}_0(X) = H_0(X) \,/\, \mathbb{Z}"
            r"\qquad \widetilde{H}_n(X) = H_n(X) \text{ for } n > 0",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(reduced, DOWN, anchor=boxed_hom, buff=0.5)
        self.play(FadeIn(reduced), run_time=NORMAL)
        self.wait(6)
        self.ly.clear()

    # ── Scene 5: Computing Examples ─────────────────────────────────
    def scene5_computing_examples(self):
        """Compute singular homology of a point and of the circle."""
        self.add_subcaption(
            "Let us compute singular homology for two fundamental examples. "
            "These computations illustrate how the definition works in "
            "practice, despite the chain groups being infinite-dimensional.",
            duration=12,
        )
        self.ly.section_divider(4, "Computing Examples")
        self.wait(3)

        # Point example
        self.add_subcaption(
            "First, a single point. Let X be a one-point space. Every "
            "continuous map from the standard simplex into a point is "
            "the constant map. So there is exactly one singular n-simplex "
            "for each n. The chain group C_n of a point is Z for every n.",
            duration=14,
        )
        title = self.ly.title("Singular Homology of a Point")
        self.wait(1)

        point_items = [
            MathTex(r"C_n(\{*\}) = \mathbb{Z}", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"\partial_n = \text{id for } n \text{ even, } 0 \text{ for } n \text{ odd}", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"H_n(\{*\}) = \begin{cases} \mathbb{Z} & n = 0 \\ 0 & n > 0 \end{cases}", font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(point_items, start_from=title)
        self.wait(6)
        self.ly.clear()

        self.add_subcaption(
            "The computation works as follows. Since there is only one "
            "n-simplex for each n, the boundary maps alternate between "
            "the identity and the zero map. For n even, the boundary of "
            "the unique simplex is the unique (n-1)-simplex. For n "
            "odd, the boundary is zero because all faces cancel in "
            "alternating pairs. This gives Z in degree 0 and zero "
            "everywhere else.",
            duration=17,
        )
        title2 = self.ly.title("Why It Works")
        self.wait(1)

        explain = [
            Text("One simplex per dimension: C_n = Z", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Boundary alternates: identity then zero", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Result: H_0 = Z, H_n = 0 for n > 0", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(explain, start_from=title2)
        self.wait(6)
        self.ly.clear()

        # Circle example
        self.add_subcaption(
            "Now the circle. The singular homology of the circle is the "
            "same as its simplicial homology: H_0 is Z and H_1 is Z, "
            "with all higher homology groups trivial. The proof is more "
            "subtle because we cannot enumerate singular simplices.",
            duration=14,
        )
        title3 = self.ly.title("Singular Homology of the Circle")
        self.wait(1)

        circle_result = MathTex(
            r"H_0(S^1) = \mathbb{Z} \qquad "
            r"H_1(S^1) = \mathbb{Z} \qquad "
            r"H_n(S^1) = 0 \text{ for } n \geq 2",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_result = self.ly.formula_box(circle_result, color=PRIMARY)
        self.ly.safe_place(boxed_result, DOWN, anchor=title3, buff=0.6)
        self.play(FadeIn(boxed_result), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "The idea behind the proof is that any singular 1-cycle on the "
            "circle is homologous to some multiple of the identity map going "
            "once around the circle. The degree of the map counts the "
            "winding number. This gives H_1 isomorphic to Z. For higher "
            "dimensions, the circle has no n-dimensional features, so "
            "H_n is trivial.",
            duration=16,
        )
        note = Text(
            "H_1 generator: the identity map S^1 -> S^1",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=boxed_result, buff=0.5)
        self.play(FadeIn(note), run_time=NORMAL)
        self.wait(6)
        self.ly.clear()

    # ── Scene 6: Comparison with Simplicial Homology ──────────────
    def scene6_comparison_simplicial(self):
        """How singular and simplicial homology relate."""
        self.add_subcaption(
            "A natural question arises: if we have both simplicial and "
            "singular homology, how do they compare? The answer is beautiful. "
            "For a triangulable space, the simplicial and singular homology "
            "groups are isomorphic. The singular theory is strictly more "
            "general, but agrees on the spaces where both are defined.",
            duration=16,
        )
        self.ly.section_divider(5, "Singular vs. Simplicial Homology")
        self.wait(3)

        title = self.ly.title("The Comparison")
        self.wait(1)

        self.add_subcaption(
            "There is a natural map from simplicial chains to singular "
            "chains. Each simplex in the triangulation is itself a singular "
            "simplex, since the inclusion of the simplex into the space is "
            "continuous. This extends linearly to a chain map between "
            "the two chain complexes.",
            duration=14,
        )
        map_defn = MathTex(
            r"\text{Inclusion: } C_n^{\text{simp}}(K) "
            r"\hookrightarrow C_n^{\text{sing}}(|K|)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_map = self.ly.formula_box(map_defn, color=PRIMARY)
        self.ly.safe_place(boxed_map, DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(boxed_map), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "The fundamental theorem states that this inclusion induces "
            "isomorphisms on homology. The simplicial homology of a "
            "simplicial complex K is naturally isomorphic to the singular "
            "homology of its geometric realization. This means all our "
            "computations from the last video carry over unchanged.",
            duration=16,
        )
        title2 = self.ly.title("Theorem: Agreement")
        self.wait(1)

        theorem = MathTex(
            r"H_n^{\text{simp}}(K) \cong "
            r"H_n^{\text{sing}}(|K|) "
            r"\quad \text{for all } n",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_theorem = self.ly.formula_box(theorem, color=ACCENT)
        self.ly.safe_place(boxed_theorem, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(boxed_theorem), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "The advantages of singular homology are significant. It applies "
            "to every topological space, not just triangulable ones. "
            "It has cleaner formal properties, such as functoriality and "
            "homotopy invariance, which are harder to prove in the "
            "simplicial setting. And it generalizes naturally to "
            "relative homology and cohomology.",
            duration=15,
        )
        advantages = [
            Text("Works for ALL topological spaces", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Clean functorial properties", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Natural generalization to cohomology", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(advantages, start_from=boxed_theorem)
        self.wait(6)
        self.ly.clear()

    # ── Scene 7: Homotopy Invariance ───────────────────────────────
    def scene7_homotopy_invariance(self):
        """Homotopy invariance theorem: homotopy equivalent spaces have same homology."""
        self.add_subcaption(
            "We now arrive at the most important property of singular "
            "homology: homotopy invariance. This is the theorem that "
            "justifies the entire theory and is the main reason we "
            "prefer singular homology over simplicial homology. It states "
            "that homotopy equivalent spaces have isomorphic homology groups.",
            duration=16,
        )
        self.ly.section_divider(6, "Homotopy Invariance")
        self.wait(3)

        title = self.ly.title("The Induced Map")
        self.wait(1)

        self.add_subcaption(
            "A continuous map f from X to Y induces homomorphisms on "
            "homology groups. The map f sends a singular simplex sigma "
            "in X to the composition f circle sigma, which is a singular "
            "simplex in Y. This extends linearly to chain maps and "
            "descends to homology.",
            duration=16,
        )
        induced = MathTex(
            r"f : X \to Y \quad \Longrightarrow \quad "
            r"f_* : H_n(X) \to H_n(Y)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_induced = self.ly.formula_box(induced, color=PRIMARY)
        self.ly.safe_place(boxed_induced, DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(boxed_induced), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "The induced map has two crucial properties. First, the identity "
            "map induces the identity homomorphism. Second, the composition "
            "of maps induces the composition of homomorphisms. These two "
            "properties make homology a functor from the category of "
            "topological spaces to the category of abelian groups.",
            duration=15,
        )
        functor = [
            Text("Identity induces identity: (id)_* = id", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Composition: (g circle f)_* = g_* circle f_*", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(functor, start_from=boxed_induced)
        self.wait(6)
        self.ly.clear()

        self.add_subcaption(
            "The homotopy invariance theorem states that if two maps "
            "f and g from X to Y are homotopic, then they induce the same "
            "homomorphism on homology. The proof uses a chain homotopy "
            "between the induced chain maps, constructed by interpolating "
            "between f and g using the homotopy parameter.",
            duration=16,
        )
        title2 = self.ly.title("Theorem: Homotopic Maps")
        self.wait(1)

        theorem1 = MathTex(
            r"f \simeq g : X \to Y \quad \Longrightarrow \quad "
            r"f_* = g_* : H_n(X) \to H_n(Y)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_thm1 = self.ly.formula_box(theorem1, color=ACCENT)
        self.ly.safe_place(boxed_thm1, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(boxed_thm1), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "An immediate consequence is that homotopy equivalent spaces "
            "have isomorphic homology groups. If there exist maps f from X "
            "to Y and g from Y to X such that g circle f is homotopic to "
            "the identity on X and f circle g is homotopic to the identity "
            "on Y, then H_n(X) is isomorphic to H_n(Y) for all n.",
            duration=17,
        )
        title3 = self.ly.title("Homotopy Equivalent Spaces")
        self.wait(1)

        theorem2 = MathTex(
            r"X \simeq Y \quad \Longrightarrow \quad "
            r"H_n(X) \cong H_n(Y) \text{ for all } n",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_thm2 = self.ly.formula_box(theorem2, color=ACCENT)
        self.ly.safe_place(boxed_thm2, DOWN, anchor=title3, buff=0.6)
        self.play(FadeIn(boxed_thm2), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "This is incredibly powerful. It means a disk and a point have "
            "the same homology, since the disk is contractible. "
            "The Mobius strip and the circle have the same homology, since "
            "the Mobius strip deformation retracts onto its central circle. "
            "We can often compute homology of complicated spaces by finding "
            "homotopy equivalent simpler ones.",
            duration=16,
        )
        examples = [
            Text("Disk is contractible: same homology as a point", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Mobius strip retracts to circle: same homology", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Strategy: simplify via homotopy equivalence", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(examples, start_from=boxed_thm2)
        self.wait(6)
        self.ly.clear()

    # ── Scene 8: Summary ───────────────────────────────────────────
    def scene8_summary(self):
        """Summary and outro."""
        self.add_subcaption(
            "Let us review the key ideas from this video on singular "
            "homology.",
            duration=5,
        )
        self.ly.section_divider(7, "Summary")
        self.wait(3)

        title = self.ly.title("Key Takeaways")
        self.wait(1)

        self.add_subcaption(
            "Singular homology generalizes simplicial homology by replacing "
            "actual simplices with continuous maps from the standard simplex. "
            "This gives homology groups defined for every topological space. "
            "The chain groups are infinite-dimensional, but the homology "
            "groups capture the essential topological features.",
            duration=16,
        )
        items = [
            Text("Singular n-simplex: continuous map Delta^n -> X", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Singular chain group: free abelian on all such maps", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Boundary defined via face maps of Delta^n", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("H_n(X) = ker(d_n) / im(d_{n+1})", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(6)
        self.ly.clear()

        self.add_subcaption(
            "The singular homology agrees with simplicial homology on "
            "triangulable spaces, so all our previous computations remain "
            "valid. The key advantage is homotopy invariance: homotopy "
            "equivalent spaces have isomorphic homology groups, giving us "
            "a powerful computational tool. Continuous maps induce homomorphisms, "
            "making homology a functor.",
            duration=17,
        )
        title2 = self.ly.title("Why Singular Homology Matters")
        self.wait(1)

        takeaways = [
            Text("Agrees with simplicial homology when both defined", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Homotopy invariance: X = Y implies H_n(X) = H_n(Y)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Functorial: continuous maps induce group homomorphisms", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title2)
        self.wait(6)
        self.ly.clear()

        self.add_subcaption(
            "That concludes our introduction to singular homology. In the "
            "next video, we will explore the Mayer-Vietoris sequence, a "
            "powerful computational tool that uses exact sequences to "
            "compute the homology of a space from the homology of its "
            "subspaces. Thank you for watching!",
            duration=14,
        )
        play_outro(self, "Singular Homology", "Algebraic Topology")
