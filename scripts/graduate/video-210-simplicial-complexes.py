"""
Video 210: Simplicial Complexes — Algebraic Topology
Simplices (points, edges, triangles, tetrahedra), simplicial complexes,
abstract vs geometric simplicial complexes, barycentric subdivision.

QUALITY RULES:
1. Max 5 visible elements per scene
2. LayoutEngine for ALL positioning
3. Progressive disclosure
4. Raw strings with single backslashes for LaTeX
5. ly.clear() between scenes
6. Narration timing: ~2.5 words/sec minimum duration
7. Each scene needs self.wait(3-5) after animations for narration to breathe
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


class Video210_SimplicialComplexes(Scene):
    """Simplicial Complexes: combinatorial building blocks of topology."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_simplices()
        self.scene3_geometric_complex()
        self.scene4_examples()
        self.scene5_abstract_complex()
        self.scene6_geometric_realization()
        self.scene7_barycentric_subdivision()
        self.scene8_summary()

    # ── Scene 1: Hook ──────────────────────────────────────────────
    def scene1_hook(self):
        """Hook — shapes built from simple pieces."""
        self.add_subcaption(
            "Welcome back to Algebraic Topology! In our first three videos, "
            "we studied continuous deformations and fundamental groups.",
            duration=8,
        )
        play_intro(self, "Simplicial Complexes", "Algebraic Topology")
        self.wait(3)

        self.add_subcaption(
            "Today we take a different approach. Instead of studying spaces "
            "directly, we build them from the simplest possible pieces: points, "
            "edges, triangles, and their higher-dimensional cousins.",
            duration=9,
        )
        title = self.ly.title("Building Spaces from Simple Pieces")
        self.wait(2)

        self.add_subcaption(
            "These building blocks are called simplices. "
            "When we glue them together following strict rules, "
            "the result is a simplicial complex.",
            duration=7,
        )
        items = [
            Text("Points, edges, triangles, tetrahedra", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Glue them together following strict rules", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("The result: a simplicial complex", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4)
        self.ly.clear()

    # ── Scene 2: Simplices defined ─────────────────────────────────
    def scene2_simplices(self):
        """Definition of simplices by dimension."""
        self.add_subcaption(
            "Let us start with the building blocks themselves. "
            "A simplex is the generalization of a triangle to any dimension.",
            duration=7,
        )
        self.ly.section_divider(1, "Simplices")
        self.wait(3)

        title = self.ly.title("What is a Simplex?")
        self.wait(1)

        self.add_subcaption(
            "A 0-simplex is just a single point. "
            "A 1-simplex is the line segment between two points. "
            "A 2-simplex is a solid triangle with its interior.",
            duration=9,
        )
        low_dim = [
            MathTex(r"\Delta^0 : \text{ vertex (point)}", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"\Delta^1 : \text{ edge (line segment)}", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"\Delta^2 : \text{ triangle (with interior)}", font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(low_dim, start_from=title)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "A 3-simplex is a solid tetrahedron, the convex hull of four points "
            "in general position. We can keep going to any dimension n, "
            "where an n-simplex has n plus 1 vertices.",
            duration=10,
        )
        title2 = self.ly.title("Higher-Dimensional Simplices")
        self.wait(1)

        high_dim = [
            MathTex(r"\Delta^3 : \text{ tetrahedron (4 vertices)}", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"\Delta^n : \text{ convex hull of } n+1 \text{ points}", font_size=BODY_SIZE, color=SECONDARY),
            Text("General position: no point in the span of the others", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(high_dim, start_from=title2)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "Formally, given n plus 1 affinely independent points "
            "v naught through v n in R to the d, "
            "the n-simplex is all convex combinations of those points.",
            duration=9,
        )
        title3 = self.ly.title("Formal Definition")
        self.wait(1)
        defn = MathTex(
            r"\Delta^n = \left\{ \sum_{i=0}^{n} t_i \, v_i "
            r"\;\middle|\; t_i \geq 0, \; \sum t_i = 1 \right\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_defn = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.safe_place(boxed_defn, DOWN, anchor=title3, buff=0.6)
        self.play(FadeIn(boxed_defn), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    # ── Scene 3: Geometric simplicial complexes ───────────────────
    def scene3_geometric_complex(self):
        """Definition and rules of a geometric simplicial complex."""
        self.add_subcaption(
            "A simplicial complex is a collection of simplices glued together "
            "following two specific rules. Let us define them carefully.",
            duration=7,
        )
        self.ly.section_divider(2, "Geometric Simplicial Complexes")
        self.wait(3)

        title = self.ly.title("Definition")
        self.wait(1)

        self.add_subcaption(
            "A geometric simplicial complex K is a finite collection of simplices "
            "in some Euclidean space, satisfying two conditions.",
            duration=7,
        )
        formula = MathTex(
            r"K = \{\sigma_1, \sigma_2, \ldots, \sigma_N\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_formula = self.ly.formula_box(formula, color=PRIMARY)
        self.ly.safe_place(boxed_formula, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_formula), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "The first condition is closure under faces. "
            "Every face of a simplex in K must also be in K. "
            "If a triangle is present, all three of its edges and "
            "all three of its vertices must also be in the complex.",
            duration=10,
        )
        condition1 = MathTex(
            r"\sigma \in K \implies \text{ every face } \tau \subseteq \sigma "
            r"\text{ satisfies } \tau \in K",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(condition1, DOWN, anchor=boxed_formula, buff=0.5)
        self.play(Write(condition1), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "The second condition governs intersections. "
            "The intersection of any two simplices must be "
            "a face of both. They are either disjoint, "
            "touch at a vertex, share an edge, or share a higher-dimensional face.",
            duration=11,
        )
        title2 = self.ly.title("Intersection Condition")
        self.wait(1)

        condition2 = MathTex(
            r"\sigma, \tau \in K \implies \sigma \cap \tau \text{ is a face of both}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(condition2, DOWN, anchor=title2, buff=0.5)
        self.play(Write(condition2), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "These two conditions ensure the complex is well-behaved. "
            "The face condition prevents dangling edges, and the intersection "
            "condition prevents simplices from partially overlapping.",
            duration=9,
        )
        summary = [
            Text("Face closure: no dangling edges", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Clean intersections: no partial overlaps", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(summary, start_from=condition2)
        self.wait(4)
        self.ly.clear()

    # ── Scene 4: Examples ──────────────────────────────────────────
    def scene4_examples(self):
        """Good and bad examples of simplicial complexes."""
        self.add_subcaption(
            "Let us look at examples to build intuition for these rules.",
            duration=4,
        )
        self.ly.section_divider(3, "Examples")
        self.wait(3)

        # Valid examples
        self.add_subcaption(
            "A single triangle with its three edges and three vertices "
            "forms a valid simplicial complex. "
            "Two triangles sharing an edge also works perfectly, "
            "because their intersection is that shared edge, "
            "which is a face of both.",
            duration=11,
        )
        title = self.ly.title("Valid Complexes")
        self.wait(1)

        valid = [
            Text("A triangle with all its edges and vertices", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Two triangles sharing an edge", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Tetrahedron surface: 4 triangles, 6 edges, 4 vertices", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(valid, start_from=title)
        self.wait(5)
        self.ly.clear()

        # Invalid examples
        self.add_subcaption(
            "Not every collection of simplices is a simplicial complex. "
            "Here are things that go wrong.",
            duration=5,
        )
        title2 = self.ly.title("Invalid Examples")
        self.wait(1)

        invalid = [
            Text("Edge without its endpoints: breaks face condition", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Two edges crossing without a shared vertex", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Two triangles overlapping in a pentagon", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(invalid, start_from=title2)
        self.wait(5)
        self.ly.clear()

        # Classic spaces as complexes
        self.add_subcaption(
            "Many familiar spaces can be triangulated, meaning they are "
            "homeomorphic to a simplicial complex. The circle can be built "
            "from three edges forming a hollow triangle. "
            "The sphere uses two triangles sharing edges. "
            "The torus requires many triangles glued carefully.",
            duration=13,
        )
        title3 = self.ly.title("Classic Triangulations")
        self.wait(1)

        spaces = [
            Text("Circle: 3 edges forming a hollow triangle", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Sphere: 2 triangles sharing all edges", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Torus: many triangles glued carefully", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(spaces, start_from=title3)
        self.wait(5)
        self.ly.clear()

    # ── Scene 5: Abstract simplicial complexes ────────────────────
    def scene5_abstract_complex(self):
        """Abstract simplicial complexes: combinatorial abstraction."""
        self.add_subcaption(
            "So far we have worked in Euclidean space with specific coordinates. "
            "But a powerful idea is to strip away the geometry entirely and work "
            "with just the combinatorial data of which vertices form simplices.",
            duration=10,
        )
        self.ly.section_divider(4, "Abstract Simplicial Complexes")
        self.wait(3)

        title = self.ly.title("The Combinatorial Abstraction")
        self.wait(1)

        self.add_subcaption(
            "An abstract simplicial complex on a vertex set V is "
            "a family of finite subsets of V that is closed under "
            "taking subsets. If a set of vertices is a simplex, "
            "then every subset of those vertices is also a simplex.",
            duration=11,
        )
        defn = MathTex(
            r"\Delta \subseteq \mathcal{P}(V), \quad "
            r"\sigma \in \Delta, \; \tau \subseteq \sigma "
            r"\implies \tau \in \Delta",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_defn = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.safe_place(boxed_defn, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_defn), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "For example, let V be the set of vertices 0, 1, 2, 3. "
            "The family containing the edges 0-1, 1-2, 2-3, "
            "the triangle 0-1-2, and all their subsets "
            "forms an abstract simplicial complex.",
            duration=11,
        )
        title2 = self.ly.title("Concrete Example")
        self.wait(1)

        vertex_set = MathTex(
            r"V = \{0, 1, 2, 3\}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(vertex_set, DOWN, anchor=title2, buff=0.5)
        self.play(Write(vertex_set), run_time=NORMAL)
        self.wait(3)

        facets = [
            MathTex(r"\{0,1\}, \{1,2\}, \{2,3\}, \{0,1,2\}", font_size=BODY_SIZE, color=SECONDARY),
            Text("Plus all subsets: vertices and empty set", font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(facets, start_from=vertex_set)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "The advantage of the abstract viewpoint is that we do not "
            "need to choose coordinates in any Euclidean space. "
            "We can study the topology purely from the combinatorial data "
            "of which vertex sets are present.",
            duration=10,
        )
        title3 = self.ly.title("Why Go Abstract?")
        self.wait(1)

        benefits = [
            Text("No coordinates needed", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Purely combinatorial: easy to compute with", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Same abstract complex, many geometric realizations", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(benefits, start_from=title3)
        self.wait(5)
        self.ly.clear()

    # ── Scene 6: Geometric realization ─────────────────────────────
    def scene6_geometric_realization(self):
        """Connecting abstract back to geometric."""
        self.add_subcaption(
            "The bridge between abstract and geometric simplicial "
            "complexes is called the geometric realization. "
            "It gives us a concrete topological space from the abstract data.",
            duration=9,
        )
        self.ly.section_divider(5, "Geometric Realization")
        self.wait(3)

        title = self.ly.title("From Abstract to Geometric")
        self.wait(1)

        self.add_subcaption(
            "Given an abstract simplicial complex on n vertices, "
            "map those vertices to affinely independent points in "
            "R to the n. Then fill in the convex hulls of each simplex. "
            "The resulting space is the geometric realization.",
            duration=11,
        )
        step = MathTex(
            r"|V| = n \implies |\Delta| \subseteq \mathbb{R}^n",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_step = self.ly.formula_box(step, color=PRIMARY)
        self.ly.safe_place(boxed_step, DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(boxed_step), run_time=NORMAL)
        self.wait(5)

        self.add_subcaption(
            "A key theorem guarantees this always works. "
            "Every abstract simplicial complex has a geometric "
            "realization. Moreover, any two realizations of the same "
            "abstract complex are homeomorphic. "
            "This means the topology is determined entirely by the combinatorial data.",
            duration=13,
        )
        theorem = MathTex(
            r"|\Delta| \cong |\Delta'| \quad \text{if } \Delta = \Delta'",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(theorem, DOWN, anchor=boxed_step, buff=0.5)
        self.play(FadeIn(theorem), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "The realization lives in a space whose dimension is at most "
            "the number of vertices minus one. This is why "
            "abstract complexes are so powerful: they let us study "
            "topology without worrying about specific embeddings.",
            duration=10,
        )
        title2 = self.ly.title("Realization Dimension")
        self.wait(1)

        dim = [
            MathTex(r"|\Delta| \subseteq \mathbb{R}^{|V|-1}", font_size=BODY_SIZE, color=PRIMARY),
            Text("Often much lower: an n-simplex fits in R^n", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Topology depends only on the abstract structure", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(dim, start_from=title2)
        self.wait(5)
        self.ly.clear()

    # ── Scene 7: Barycentric subdivision ───────────────────────────
    def scene7_barycentric_subdivision(self):
        """Barycentric subdivision as a refinement operation."""
        self.add_subcaption(
            "One of the most important operations on simplicial "
            "complexes is subdivision: breaking simplices into "
            "smaller pieces while preserving the overall topology. "
            "The most common form is barycentric subdivision.",
            duration=11,
        )
        self.ly.section_divider(6, "Barycentric Subdivision")
        self.wait(3)

        title = self.ly.title("What is Barycentric Subdivision?")
        self.wait(1)

        self.add_subcaption(
            "The barycentric subdivision of a simplex works as follows. "
            "First, compute the barycenter, the average of all vertices. "
            "Then connect this barycenter to all barycenters of its proper faces.",
            duration=10,
        )
        bary = MathTex(
            r"b = \frac{1}{n+1} \sum_{i=0}^{n} v_i",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_bary = self.ly.formula_box(bary, color=PRIMARY)
        self.ly.safe_place(boxed_bary, DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(boxed_bary), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "For a triangle, the barycentric subdivision produces "
            "six smaller triangles. For a tetrahedron, it produces "
            "twenty-four smaller tetrahedra. "
            "The topology does not change, but the mesh gets finer.",
            duration=11,
        )
        title2 = self.ly.title("Subdivision in Action")
        self.wait(1)

        examples = [
            MathTex(r"\text{sd}(\Delta^2) : 6 \text{ sub-triangles}", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"\text{sd}(\Delta^3) : 24 \text{ sub-tetrahedra}", font_size=BODY_SIZE, color=SECONDARY),
            Text("Same topology, finer mesh", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(examples, start_from=title2)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "We can iterate this process. After k iterations, "
            "the mesh becomes arbitrarily fine. This is crucial "
            "for proofs that require a small enough simplex size, "
            "such as the simplicial approximation theorem, "
            "which we will encounter when defining homology.",
            duration=12,
        )
        title3 = self.ly.title("Iterated Subdivision")
        self.wait(1)

        iteration = [
            MathTex(r"\text{sd}^k(\Delta^n) : (n+1)!^k \text{ simplices}", font_size=BODY_SIZE, color=PRIMARY),
            Text("Mesh diameter tends to zero as k grows", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Foundation for simplicial approximation", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(iteration, start_from=title3)
        self.wait(5)
        self.ly.clear()

    # ── Scene 8: Summary ──────────────────────────────────────────
    def scene8_summary(self):
        """Summary and outro."""
        self.add_subcaption(
            "Let us review the key ideas from this video about simplicial complexes.",
            duration=4,
        )
        self.ly.section_divider(7, "Summary")
        self.wait(3)

        title = self.ly.title("Key Takeaways")
        self.wait(1)

        self.add_subcaption(
            "We defined simplices as convex hulls of affinely independent points. "
            "We built simplicial complexes from these simplices using "
            "face closure and clean intersection rules. "
            "We learned about the abstract viewpoint that strips away coordinates.",
            duration=11,
        )
        items = [
            Text("n-simplex: convex hull of n+1 points", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Complex: simplices with face and intersection rules", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Abstract complex: purely combinatorial", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Barycentric subdivision: refining the mesh", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)
        self.ly.clear()

        # Summary formula
        self.add_subcaption(
            "Simplicial complexes give us a bridge between continuous "
            "topology and discrete combinatorics. In the next video, "
            "we will define homology groups, which use these complexes "
            "to detect and classify topological holes in a space.",
            duration=11,
        )
        title2 = self.ly.title("Looking Ahead")
        self.wait(1)

        ahead = self.ly.formula_box(
            MathTex(
                r"\text{Simplicial complex } K "
                r"\;\longrightarrow\; H_n(K) \text{ (homology groups)}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            color=PRIMARY,
        )
        self.ly.safe_place(ahead, DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(ahead), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

        # Outro
        self.add_subcaption(
            "That concludes our introduction to simplicial complexes. "
            "In the next video, we will build homology groups from "
            "these combinatorial structures. Thank you for watching!",
            duration=8,
        )
        play_outro(self, "Simplicial Homology", "Algebraic Topology")
