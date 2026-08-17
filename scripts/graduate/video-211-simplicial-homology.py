"""
Video 211: Simplicial Homology — Algebraic Topology
Simplicial chains C_n, boundary maps ∂_n, chain complexes,
homology groups H_n = ker(∂_n) / im(∂_{n+1}),
computing H_0 and H_1 with worked examples.

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


class Video211_SimplicialHomology(Scene):
    """Simplicial Homology: algebraic invariants from chain complexes."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_oriented_simplices_chains()
        self.scene3_boundary_maps()
        self.scene4_chain_complex()
        self.scene5_homology_groups()
        self.scene6_computing_h0()
        self.scene7_computing_h1()
        self.scene8_worked_example()
        self.scene9_summary()

    # ── Scene 1: Hook ──────────────────────────────────────────────
    def scene1_hook(self):
        """Hook — from simplicial complexes to algebraic invariants."""
        self.add_subcaption(
            "Welcome back to Algebraic Topology! In the last video, we built "
            "spaces from simplices: points, edges, triangles, and higher-dimensional "
            "pieces glued together following strict combinatorial rules.",
            duration=12,
        )
        play_intro(self, "Simplicial Homology", "Algebraic Topology")
        self.wait(8)

        self.add_subcaption(
            "Now we ask a fundamental question: given a simplicial complex, "
            "how can we detect and classify its holes? A disk has no holes. "
            "A circle has one 1-dimensional hole. A sphere has a 2-dimensional "
            "void. Homology groups are algebraic objects that count these holes.",
            duration=14,
        )
        title = self.ly.title("Counting Holes Algebraically")
        self.wait(2)

        items = [
            Text("Disk: no holes", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Circle: one 1-dimensional hole", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Sphere: one 2-dimensional void", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)

        self.add_subcaption(
            "The idea is beautiful: we build a chain complex from the simplicial "
            "complex, study its cycles and boundaries, and the quotient reveals "
            "the topological features. By the end of this video, you will "
            "understand the definition of H_n and know how to compute "
            "H_0 and H_1 for concrete examples.",
            duration=13,
        )
        roadmap = [
            Text("Chains: formal sums of simplices", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Boundary maps: edges of a simplex", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Homology: cycles modulo boundaries", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(roadmap)
        self.wait(6)
        self.ly.clear()

    # ── Scene 2: Oriented Simplices and Chains ──────────────────────
    def scene2_oriented_simplices_chains(self):
        """Oriented simplices, formal sums, and chain groups C_n."""
        self.add_subcaption(
            "To do algebra on a simplicial complex, we need to treat simplices "
            "as algebraic objects. The first step is orientation. An edge from "
            "vertex A to vertex B is different from the same edge oriented "
            "from B to A. This distinction is captured by a sign.",
            duration=13,
        )
        self.ly.section_divider(1, "Oriented Simplices and Chains")
        self.wait(3)

        title = self.ly.title("Orientation")
        self.wait(1)

        self.add_subcaption(
            "For a 1-simplex with vertices v0 and v1, the oriented simplex "
            "v0 v1 is the negative of v1 v0. We write this as v0 v1 "
            "equals minus v1 v0. For a 2-simplex with vertices "
            "v0, v1, v2, swapping any two vertices flips the sign.",
            duration=13,
        )
        orient = [
            MathTex(r"[v_0, v_1] = -[v_1, v_0]", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"[v_0, v_1, v_2] = -[v_1, v_0, v_2]", font_size=BODY_SIZE, color=SECONDARY),
            Text("Odd permutations flip the sign", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(orient, start_from=title)
        self.wait(6)
        self.ly.clear()

        self.add_subcaption(
            "Now we form chain groups. The n-th chain group C_n is the free "
            "abelian group generated by the n-simplices of the complex. "
            "An element of C_n is a formal linear combination of n-simplices "
            "with integer coefficients. Think of it as a formal sum where "
            "coefficients can be positive, negative, or zero.",
            duration=15,
        )
        title2 = self.ly.title("Chain Groups")
        self.wait(1)

        defn = MathTex(
            r"C_n(K) = \bigoplus_{\sigma^n \in K} \mathbb{Z} \cdot \sigma^n",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_defn = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.safe_place(boxed_defn, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(boxed_defn), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "For example, if a complex has three edges e1, e2, e3, then "
            "C_1 is the free abelian group on those three generators. "
            "A typical element looks like 2 times e1 minus e2 plus e3. "
            "There is no geometric picture required: this is pure algebra.",
            duration=13,
        )
        example = MathTex(
            r"2e_1 - e_2 + e_3 \;\in\; C_1(K)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(example, DOWN, anchor=boxed_defn, buff=0.5)
        self.play(FadeIn(example), run_time=NORMAL)
        self.wait(6)
        self.ly.clear()

    # ── Scene 3: Boundary Maps ─────────────────────────────────────
    def scene3_boundary_maps(self):
        """Boundary operator ∂_n: from n-chains to (n-1)-chains."""
        self.add_subcaption(
            "The boundary map is the bridge between adjacent chain groups. "
            "It takes an n-simplex and returns the formal sum of its "
            "(n minus 1)-dimensional faces, with signs determined by "
            "orientation. This single idea drives all of homology.",
            duration=13,
        )
        self.ly.section_divider(2, "Boundary Maps")
        self.wait(3)

        title = self.ly.title("The Boundary Operator")
        self.wait(1)

        self.add_subcaption(
            "The boundary of a vertex is zero: a point has no boundary. "
            "The boundary of an oriented edge from v0 to v1 is the "
            "difference v1 minus v0. This captures the idea that the "
            "boundary has a direction: the end minus the start.",
            duration=12,
        )
        bnd0 = MathTex(
            r"\partial_1[v_0, v_1] = [v_1] - [v_0]",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_bnd0 = self.ly.formula_box(bnd0, color=PRIMARY)
        self.ly.safe_place(boxed_bnd0, DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(boxed_bnd0), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "For a triangle with vertices v0, v1, v2, the boundary "
            "is the alternating sum of its three edges. Each edge "
            "appears with a sign that depends on which vertex is omitted.",
            duration=10,
        )
        title2 = self.ly.title("Boundary of a Triangle")
        self.wait(1)

        bnd2 = MathTex(
            r"\partial_2[v_0, v_1, v_2] = "
            r"[v_1, v_2] - [v_0, v_2] + [v_0, v_1]",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_bnd2 = self.ly.formula_box(bnd2, color=PRIMARY)
        self.ly.safe_place(boxed_bnd2, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(boxed_bnd2), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "In general, the boundary of an n-simplex is the alternating sum "
            "over all its faces, where the face omitting vertex v_i gets "
            "a sign of negative one to the power of i. This formula is "
            "the heart of simplicial homology.",
            duration=12,
        )
        title3 = self.ly.title("General Formula")
        self.wait(1)

        general = MathTex(
            r"\partial_n[v_0, \ldots, v_n] = "
            r"\sum_{i=0}^{n} (-1)^i \, [v_0, \ldots, \hat{v}_i, \ldots, v_n]",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_general = self.ly.formula_box(general, color=PRIMARY)
        self.ly.safe_place(boxed_general, DOWN, anchor=title3, buff=0.6)
        self.play(FadeIn(boxed_general), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "The hat notation means the vertex v_i is omitted from the list. "
            "This produces the (n minus 1)-face opposite to v_i.",
            duration=6,
        )
        note = Text(
            "Hat = omit the i-th vertex",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=boxed_general, buff=0.4)
        self.play(FadeIn(note), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    # ── Scene 4: Chain Complex ────────────────────────────────────
    def scene4_chain_complex(self):
        """Chain complex: the sequence with composition ∂∘∂ = 0."""
        self.add_subcaption(
            "The boundary maps connect all chain groups into a single "
            "algebraic structure called a chain complex. It is a sequence "
            "of abelian groups connected by homomorphisms, with one crucial "
            "property: applying the boundary twice always gives zero.",
            duration=14,
        )
        self.ly.section_divider(3, "Chain Complexes")
        self.wait(3)

        title = self.ly.title("The Chain Complex")
        self.wait(1)

        self.add_subcaption(
            "For a simplicial complex K, the chain complex is a sequence of "
            "chain groups connected by boundary maps. Each map goes from "
            "C_n to C_{n-1}. At the ends, the boundary of any vertex is "
            "zero, and there are no simplices above the top dimension.",
            duration=13,
        )
        seq = MathTex(
            r"\cdots \xrightarrow{\partial_3} C_2 "
            r"\xrightarrow{\partial_2} C_1 "
            r"\xrightarrow{\partial_1} C_0 "
            r"\xrightarrow{\partial_0} 0",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_seq = self.ly.formula_box(seq, color=PRIMARY)
        self.ly.safe_place(boxed_seq, DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(boxed_seq), run_time=NORMAL)
        self.wait(6)
        self.ly.clear()

        self.add_subcaption(
            "The fundamental property is that the composition of two "
            "consecutive boundary maps is zero. In symbols, the boundary "
            "of the boundary is always zero. This is a theorem that follows "
            "directly from the alternating sign formula: each face appears "
            "twice with opposite signs and cancels.",
            duration=15,
        )
        title2 = self.ly.title("The Key Property")
        self.wait(1)

        prop = MathTex(
            r"\partial_n \circ \partial_{n+1} = 0",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_prop = self.ly.formula_box(prop, color=ACCENT)
        self.ly.safe_place(boxed_prop, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(boxed_prop), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "This property is sometimes called the boundary of a boundary "
            "is zero. Geometrically, the boundary of a triangle is a "
            "closed loop, and a closed loop has no boundary. The algebra "
            "perfectly mirrors the geometry.",
            duration=10,
        )
        intuition = [
            Text("Boundary of a triangle = closed loop of edges", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("A closed loop has no boundary", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(intuition, start_from=boxed_prop)
        self.wait(6)
        self.ly.clear()

    # ── Scene 5: Homology Groups ────────────────────────────────────
    def scene5_homology_groups(self):
        """Definition of H_n = ker(∂_n) / im(∂_{n+1})."""
        self.add_subcaption(
            "We now arrive at the central definition. The chain complex gives "
            "us two important subgroups in each C_n: the kernel of the "
            "boundary map, consisting of cycles, and the image of the next "
            "boundary map, consisting of boundaries. The homology group is "
            "the quotient of cycles by boundaries.",
            duration=18,
        )
        self.ly.section_divider(4, "Homology Groups")
        self.wait(3)

        title = self.ly.title("Cycles and Boundaries")
        self.wait(1)

        self.add_subcaption(
            "An n-cycle is a chain whose boundary is zero. These are closed "
            "loops when n is 1, closed surfaces when n is 2, and so on. "
            "The group of n-cycles is the kernel of the boundary map.",
            duration=12,
        )
        cycles = MathTex(
            r"Z_n = \ker(\partial_n) = \{ c \in C_n : \partial_n(c) = 0 \}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_cycles = self.ly.formula_box(cycles, color=PRIMARY)
        self.ly.safe_place(boxed_cycles, DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(boxed_cycles), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "An n-boundary is a chain that is the boundary of something in "
            "the next dimension. These are chains that fill in a region. "
            "The group of n-boundaries is the image of the boundary map "
            "from C_{n+1}.",
            duration=13,
        )
        title2 = self.ly.title("Boundaries")
        self.wait(1)

        bounds = MathTex(
            r"B_n = \operatorname{im}(\partial_{n+1})",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed_bounds = self.ly.formula_box(bounds, color=SECONDARY)
        self.ly.safe_place(boxed_bounds, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(boxed_bounds), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "Because the boundary of a boundary is zero, every boundary "
            "is automatically a cycle. The boundaries form a subgroup "
            "of the cycles. This is exactly the condition we need "
            "to form the quotient group.",
            duration=11,
        )
        subset = MathTex(
            r"B_n \subseteq Z_n \subseteq C_n",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(subset, DOWN, anchor=boxed_bounds, buff=0.5)
        self.play(FadeIn(subset), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "The n-th homology group is the quotient of n-cycles by "
            "n-boundaries. Two cycles are homologous if their difference "
            "is a boundary, meaning one can be continuously deformed "
            "into the other across the filled region.",
            duration=13,
        )
        title3 = self.ly.title("The Homology Group")
        self.wait(1)

        hom = MathTex(
            r"H_n(K) = Z_n / B_n = "
            r"\ker(\partial_n) \,/\, \operatorname{im}(\partial_{n+1})",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_hom = self.ly.formula_box(hom, color=ACCENT)
        self.ly.safe_place(boxed_hom, DOWN, anchor=title3, buff=0.6)
        self.play(FadeIn(boxed_hom), run_time=NORMAL)
        self.wait(6)
        self.ly.clear()

    # ── Scene 6: Computing H_0 ────────────────────────────────────
    def scene6_computing_h0(self):
        """H_0 counts the connected components."""
        self.add_subcaption(
            "Let us compute our first homology group. The zeroth homology "
            "group H_0 has a beautiful interpretation: it counts the number "
            "of connected components of the space. Every connected component "
            "contributes one copy of the integers.",
            duration=14,
        )
        self.ly.section_divider(5, "Computing H_0")
        self.wait(3)

        title = self.ly.title("H_0: Connected Components")
        self.wait(1)

        self.add_subcaption(
            "Let us work through this step by step. The zeroth chain group "
            "C_0 is generated by the vertices. The boundary map from C_0 "
            "to zero is the zero map, so every 0-chain is a 0-cycle. "
            "This means Z_0 equals C_0.",
            duration=12,
        )
        step1 = [
            MathTex(r"C_0 = \text{free abelian group on vertices}", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"\partial_0 = 0 \implies Z_0 = C_0", font_size=BODY_SIZE, color=SECONDARY),
        ]
        self.ly.progressive_reveal(step1, start_from=title)
        self.wait(6)
        self.ly.clear()

        self.add_subcaption(
            "The zeroth boundary group B_0 is the image of the first "
            "boundary map. An element of B_0 is a formal sum of vertices "
            "that arises as the boundary of some 1-chain. The key insight "
            "is that two vertices connected by an edge become identified "
            "in the quotient.",
            duration=15,
        )
        title2 = self.ly.title("What is B_0?")
        self.wait(1)

        step2 = MathTex(
            r"B_0 = \operatorname{im}(\partial_1)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_step2 = self.ly.formula_box(step2, color=PRIMARY)
        self.ly.safe_place(boxed_step2, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(boxed_step2), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "The quotient H_0 equals Z_0 over B_0 identifies vertices that "
            "are connected by paths. Each connected component contributes "
            "one copy of the integers. If the complex has k connected "
            "components, then H_0 is the direct sum of k copies of Z.",
            duration=14,
        )
        title3 = self.ly.title("The Result")
        self.wait(1)

        result = MathTex(
            r"H_0(K) \cong \mathbb{Z}^{\beta_0}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_result = self.ly.formula_box(result, color=ACCENT)
        self.ly.safe_place(boxed_result, DOWN, anchor=title3, buff=0.6)
        self.play(FadeIn(boxed_result), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "Here beta_0 is the zeroth Betti number, which equals the number "
            "of connected components. For example, a single connected "
            "complex has H_0 equal to Z, while two disjoint triangles "
            "have H_0 equal to Z squared.",
            duration=13,
        )
        examples = [
            MathTex(r"\beta_0 = \text{number of components}", font_size=BODY_SIZE, color=PRIMARY),
            Text("One complex: H_0 = Z", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Two disjoint pieces: H_0 = Z^2", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(examples, start_from=boxed_result)
        self.wait(6)
        self.ly.clear()

    # ── Scene 7: Computing H_1 ────────────────────────────────────
    def scene7_computing_h1(self):
        """H_1 counts 1-dimensional holes (loops)."""
        self.add_subcaption(
            "The first homology group H_1 captures the one-dimensional holes "
            "in the space. Think of it as the group of independent non-contractible "
            "loops, where two loops are considered the same if together they "
            "bound a region.",
            duration=13,
        )
        self.ly.section_divider(6, "Computing H_1")
        self.wait(3)

        title = self.ly.title("H_1: One-Dimensional Holes")
        self.wait(1)

        self.add_subcaption(
            "To compute H_1, we need the group of 1-cycles and 1-boundaries. "
            "A 1-cycle is a formal sum of edges whose boundary is zero. "
            "Geometrically, this means each vertex is entered and exited "
            "the same number of times, forming a collection of closed loops.",
            duration=14,
        )
        step1 = [
            MathTex(r"Z_1 = \{ c \in C_1 : \partial_1(c) = 0 \}", font_size=BODY_SIZE, color=PRIMARY),
            Text("Edges forming closed loops", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(step1, start_from=title)
        self.wait(6)
        self.ly.clear()

        self.add_subcaption(
            "A 1-boundary is the boundary of some 2-chain. Geometrically, "
            "this is a collection of edges that form the perimeter of one "
            "or more filled triangles. Such a loop is trivial in homology "
            "because it bounds a region.",
            duration=12,
        )
        title2 = self.ly.title("1-Boundaries")
        self.wait(1)

        step2 = [
            MathTex(r"B_1 = \operatorname{im}(\partial_2)", font_size=BODY_SIZE, color=PRIMARY),
            Text("Edges that bound filled triangles", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(step2, start_from=title2)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "The quotient H_1 equals Z_1 over B_1 identifies loops that "
            "differ by a boundary. A loop around a hole cannot be written "
            "as a boundary, so it survives in homology. A loop that bounds "
            "a region is killed, becoming zero in the quotient.",
            duration=13,
        )
        title3 = self.ly.title("The Quotient")
        self.wait(1)

        quotient = MathTex(
            r"H_1(K) = Z_1 / B_1",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_quotient = self.ly.formula_box(quotient, color=ACCENT)
        self.ly.safe_place(boxed_quotient, DOWN, anchor=title3, buff=0.6)
        self.play(FadeIn(boxed_quotient), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "The rank of H_1 is the first Betti number beta_1, which counts "
            "the independent 1-dimensional holes. For a circle triangulated "
            "as three edges, H_1 is Z. For a hollow triangle with three edges, "
            "the single loop generates H_1. For a disk, H_1 is trivial "
            "because every loop bounds a triangle.",
            duration=15,
        )
        results = [
            MathTex(r"\text{rank}(H_1) = \beta_1", font_size=BODY_SIZE, color=PRIMARY),
            Text("Circle (3 edges): H_1 = Z", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Disk: H_1 = 0 (no holes)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(results, start_from=boxed_quotient)
        self.wait(6)
        self.ly.clear()

    # ── Scene 8: Worked Example ────────────────────────────────────
    def scene8_worked_example(self):
        """Full worked computation: the circle and the sphere."""
        self.add_subcaption(
            "Let us put everything together with two classic examples. "
            "We will compute the homology of the circle and the sphere, "
            "triangulated as simplicial complexes. These examples show how "
            "the algebra detects topological features.",
            duration=13,
        )
        self.ly.section_divider(7, "Worked Examples")
        self.wait(3)

        # Circle example
        self.add_subcaption(
            "First, the circle. Triangulate it as three vertices and three "
            "edges forming a hollow triangle. There are no 2-simplices. "
            "Since there are no filled triangles, every 1-cycle is a "
            "boundary of nothing, so B_1 is trivial. This means "
            "H_1 equals Z_1, the group of all 1-cycles.",
            duration=16,
        )
        title = self.ly.title("The Circle S^1")
        self.wait(1)

        circle_items = [
            MathTex(r"C_0 = \mathbb{Z}^3,\; C_1 = \mathbb{Z}^3,\; C_2 = 0", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"B_1 = \operatorname{im}(\partial_2) = 0", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"H_1(S^1) \cong \mathbb{Z}", font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(circle_items, start_from=title)
        self.wait(6)
        self.ly.clear()

        self.add_subcaption(
            "The generator of H_1 for the circle is the loop e1 plus e2 plus "
            "e3, going all the way around. Any integer multiple of this "
            "loop represents winding around the hole that many times.",
            duration=10,
        )
        title2 = self.ly.title("Generator of H_1")
        self.wait(1)

        gen = MathTex(
            r"[e_1 + e_2 + e_3] \;\in\; H_1(S^1)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_gen = self.ly.formula_box(gen, color=PRIMARY)
        self.ly.safe_place(boxed_gen, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(boxed_gen), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        # Sphere example
        self.add_subcaption(
            "Now the sphere. Triangulate it as two triangles sharing "
            "all three edges, forming the boundary of a tetrahedron. "
            "There are four vertices, six edges, and two triangles.",
            duration=10,
        )
        title3 = self.ly.title("The Sphere S^2")
        self.wait(1)

        sphere_items = [
            MathTex(r"C_0 = \mathbb{Z}^4,\; C_1 = \mathbb{Z}^6,\; C_2 = \mathbb{Z}^2", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"H_0(S^2) = \mathbb{Z}", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"H_1(S^2) = 0", font_size=BODY_SIZE, color=ACCENT),
            MathTex(r"H_2(S^2) = \mathbb{Z}", font_size=BODY_SIZE, color=RED),
        ]
        self.ly.progressive_reveal(sphere_items, start_from=title3)
        self.wait(6)
        self.ly.clear()

        self.add_subcaption(
            "The sphere has H_1 trivial because every loop on the sphere "
            "bounds a region: either one of the two triangles or both. "
            "But H_2 is Z because the two triangles together form a closed "
            "2-cycle that is not the boundary of any 3-simplex, since there "
            "are no 3-simplices in the complex.",
            duration=16,
        )
        title4 = self.ly.title("Why H_2 = Z")
        self.wait(1)

        explain = [
            Text("Every loop bounds a triangle: H_1 = 0", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Two triangles form a closed 2-cycle", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("No 3-simplices: cycle is not a boundary", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(explain, start_from=title4)
        self.wait(6)
        self.ly.clear()

    # ── Scene 9: Summary ───────────────────────────────────────────
    def scene9_summary(self):
        """Summary and outro."""
        self.add_subcaption(
            "Let us review the key ideas from this video on simplicial homology.",
            duration=5,
        )
        self.ly.section_divider(8, "Summary")
        self.wait(3)

        title = self.ly.title("Key Takeaways")
        self.wait(1)

        self.add_subcaption(
            "We assigned orientations to simplices and formed chain groups, "
            "free abelian groups generated by the simplices of each dimension. "
            "We defined the boundary map that takes an n-simplex to an alternating "
            "sum of its faces. We built the chain complex and used its key "
            "property that the boundary of a boundary is zero.",
            duration=15,
        )
        items = [
            Text("Chain groups C_n: free abelian on n-simplices", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Boundary map: alternating sum of faces", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Chain complex: ... -> C_2 -> C_1 -> C_0 -> 0", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("H_n = ker(d_n) / im(d_{n+1})", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(6)
        self.ly.clear()

        self.add_subcaption(
            "The homology groups H_n are topological invariants: homeomorphic "
            "spaces have isomorphic homology groups. The Betti numbers beta_n, "
            "which are the ranks of these groups, count the n-dimensional "
            "holes. H_0 counts components, H_1 counts tunnels, "
            "H_2 counts voids, and so on.",
            duration=16,
        )
        title2 = self.ly.title("Betti Numbers")
        self.wait(1)

        betti = [
            Text("beta_0: connected components", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("beta_1: independent tunnels / 1-holes", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("beta_2: independent voids / cavities", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(betti, start_from=title2)
        self.wait(6)
        self.ly.clear()

        self.add_subcaption(
            "That concludes our introduction to simplicial homology. In the "
            "next video, we will explore higher homology groups, the Euler "
            "characteristic, and the relationship between homology and the "
            "fundamental group. Thank you for watching!",
            duration=12,
        )
        play_outro(self, "Simplicial Homology", "Algebraic Topology")
