"""
Video 88: Planarity and Euler's Formula
Discrete Mathematics -- Video 11 of 12

Covers: Planar graphs, planar embeddings, Euler's formula (V - E + F = 2),
consequences (E <= 3V-6, bipartite bound), Kuratowski's theorem (K5, K3,3),
and applications to graph drawing and map coloring.

Plan: planning/video-88-planarity-euler.md

Render draft:  manim -ql scripts/undergraduate/video-88-planarity-euler.py Video88_PlanarityEuler
Render final:  manim -qh scripts/undergraduate/video-88-planarity-euler.py Video88_PlanarityEuler
"""

from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video88_PlanarityEuler(Scene):
    """Planarity and Euler's Formula: the geometry of drawing graphs flat."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_planar_definition()
        self.scene3_eulers_formula()
        self.scene4_consequences()
        self.scene5_kuratowski()
        self.scene6_applications()
        self.scene7_summary()
        self.scene8_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook — Can You Draw Without Crossing? (45s)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Imagine three houses and three utilities: gas, water, and electricity. "
            "Each house needs to connect to every utility, but no lines can cross. "
            "Is it possible? This is the famous utility graph puzzle.",
            duration=18,
        )
        play_intro(self, "Planarity and Euler's Formula", "Discrete Mathematics")

        title = self.ly.title("The Crossing Puzzle")

        # Draw K3,3 — 3 houses on left, 3 utilities on right
        houses = VGroup(
            Dot(UP * 1.5 + LEFT * 3, color=WHITE, radius=0.15),
            Dot(UP * 0 + LEFT * 3, color=WHITE, radius=0.15),
            Dot(DOWN * 1.5 + LEFT * 3, color=WHITE, radius=0.15),
        )
        utils = VGroup(
            Dot(UP * 1.5 + RIGHT * 3, color=SECONDARY, radius=0.15),
            Dot(UP * 0 + RIGHT * 3, color=SECONDARY, radius=0.15),
            Dot(DOWN * 1.5 + RIGHT * 3, color=SECONDARY, radius=0.15),
        )
        # Labels
        h_labels = VGroup(
            Text("H1", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(houses[0], LEFT, buff=0.15),
            Text("H2", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(houses[1], LEFT, buff=0.15),
            Text("H3", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(houses[2], LEFT, buff=0.15),
        )
        u_labels = VGroup(
            Text("G", font_size=LABEL_SIZE, color=SECONDARY, font=SANS).next_to(utils[0], RIGHT, buff=0.15),
            Text("W", font_size=LABEL_SIZE, color=SECONDARY, font=SANS).next_to(utils[1], RIGHT, buff=0.15),
            Text("E", font_size=LABEL_SIZE, color=SECONDARY, font=SANS).next_to(utils[2], RIGHT, buff=0.15),
        )

        # Edges (all 9 connections — some will cross)
        edges = VGroup(
            Line(houses[0].get_center(), utils[0].get_center(), color=DIM, stroke_width=2),
            Line(houses[0].get_center(), utils[1].get_center(), color=DIM, stroke_width=2),
            Line(houses[0].get_center(), utils[2].get_center(), color=DIM, stroke_width=2),
            Line(houses[1].get_center(), utils[0].get_center(), color=DIM, stroke_width=2),
            Line(houses[1].get_center(), utils[1].get_center(), color=DIM, stroke_width=2),
            Line(houses[1].get_center(), utils[2].get_center(), color=DIM, stroke_width=2),
            Line(houses[2].get_center(), utils[0].get_center(), color=DIM, stroke_width=2),
            Line(houses[2].get_center(), utils[1].get_center(), color=DIM, stroke_width=2),
            Line(houses[2].get_center(), utils[2].get_center(), color=DIM, stroke_width=2),
        )

        graph_group = VGroup(houses, utils, h_labels, u_labels, edges)
        self.ly.center_in_content(graph_group)
        self.play(
            LaggedStartMap(FadeIn, houses, scale=0.5, lag_ratio=0.1),
            LaggedStartMap(FadeIn, utils, scale=0.5, lag_ratio=0.1),
            LaggedStartMap(FadeIn, h_labels, scale=0.5, lag_ratio=0.1),
            LaggedStartMap(FadeIn, u_labels, scale=0.5, lag_ratio=0.1),
            run_time=FAST,
        )
        self.play(Create(edges), run_time=NORMAL)
        self.wait(1)

        # Highlight crossings
        question = Text(
            "Can you redraw this with NO crossings?",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(question, direction=DOWN, anchor=graph_group, buff=0.6)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        key = Text(
            "Hint: the answer reveals a deep property of graphs.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=question, buff=0.4)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Planar Graphs Definition (60s)
    # ------------------------------------------------------------------
    def scene2_planar_definition(self):
        self.add_subcaption(
            "A graph is planar if it can be drawn in the plane so that no edges "
            "cross. The same graph can have many different drawings, but a planar "
            "graph always has at least one drawing with no edge crossings.",
            duration=18,
        )
        self.ly.section_divider(1, "What is a Planar Graph?")

        # Definition
        defn = Text(
            "A graph is PLANAR if it can be drawn with no edge crossings.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.center_in_content(defn)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        # K4 planar example — redraw showing it can be planar
        k4_title = Text("K4: Planar (can redraw without crossings)", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.center_in_content(k4_title)
        self.play(FadeIn(k4_title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # K4 vertices in a diamond/square with diagonals drawn outside
        k4_v = VGroup(
            Dot(UP * 1.5, color=WHITE, radius=0.13),
            Dot(LEFT * 1.5, color=WHITE, radius=0.13),
            Dot(RIGHT * 1.5, color=WHITE, radius=0.13),
            Dot(DOWN * 1.5, color=WHITE, radius=0.13),
        )
        k4_labels = VGroup(
            Text("1", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(k4_v[0], UP, buff=0.1),
            Text("2", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(k4_v[1], LEFT, buff=0.1),
            Text("3", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(k4_v[2], RIGHT, buff=0.1),
            Text("4", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(k4_v[3], DOWN, buff=0.1),
        )
        # Outer cycle (no crossings)
        k4_outer = VGroup(
            Line(k4_v[0].get_center(), k4_v[1].get_center(), color=PRIMARY, stroke_width=3),
            Line(k4_v[0].get_center(), k4_v[2].get_center(), color=PRIMARY, stroke_width=3),
            Line(k4_v[1].get_center(), k4_v[3].get_center(), color=PRIMARY, stroke_width=3),
            Line(k4_v[2].get_center(), k4_v[3].get_center(), color=PRIMARY, stroke_width=3),
        )
        # Diagonals drawn as curved arcs to avoid crossings
        k4_diag1 = ArcBetweenPoints(
            k4_v[1].get_center(), k4_v[2].get_center(),
            color=SECONDARY, stroke_width=3, angle=-TAU / 4,
        )
        k4_diag2 = ArcBetweenPoints(
            k4_v[0].get_center(), k4_v[3].get_center(),
            color=SECONDARY, stroke_width=3, angle=-TAU / 4,
        )
        k4_group = VGroup(k4_v, k4_labels, k4_outer, k4_diag1, k4_diag2)
        self.ly.center_in_content(k4_group)
        self.play(
            Create(k4_outer), LaggedStartMap(FadeIn, k4_v, scale=0.5, lag_ratio=0.1),
            LaggedStartMap(FadeIn, k4_labels, scale=0.5, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.play(Create(k4_diag1), Create(k4_diag2), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # K5 not planar
        k5_title = Text("K5: NOT planar — every drawing has crossings", font_size=BODY_SIZE, color=RED, font=SANS)
        self.ly.center_in_content(k5_title)
        self.play(FadeIn(k5_title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Pentagon with all diagonals (K5)
        k5_positions = [
            UP * 2,
            UP * 0.6 + RIGHT * 1.9,
            DOWN * 1.2 + RIGHT * 1.2,
            DOWN * 1.2 + LEFT * 1.2,
            UP * 0.6 + LEFT * 1.9,
        ]
        k5_v = VGroup(*[Dot(p, color=WHITE, radius=0.13) for p in k5_positions])
        k5_edges = VGroup()
        for i in range(5):
            for j in range(i + 1, 5):
                k5_edges.add(Line(k5_positions[i], k5_positions[j], color=DIM, stroke_width=2))
        k5_graph = VGroup(k5_v, k5_edges)
        self.ly.center_in_content(k5_graph)
        self.play(
            LaggedStartMap(FadeIn, k5_v, scale=0.5, lag_ratio=0.1),
            Create(k5_edges),
            run_time=NORMAL,
        )
        self.wait(1)

        note = Text(
            "Every edge must connect two vertices — crossings are unavoidable!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=k5_graph, buff=0.5)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Euler's Formula (90s)
    # ------------------------------------------------------------------
    def scene3_eulers_formula(self):
        self.add_subcaption(
            "For any connected planar graph, the number of vertices V, edges E, "
            "and faces F satisfy V minus E plus F equals 2. Faces are the regions "
            "created when you draw the graph, including the unbounded outer face.",
            duration=18,
        )
        self.ly.section_divider(2, "Euler's Formula")

        # The formula
        formula = MathTex(r"V - E + F = 2", font_size=HEADING_SIZE, color=ACCENT)
        formula_box = self.ly.formula_box(formula, ACCENT)
        self.ly.center_in_content(formula_box)
        self.play(Write(formula_box), run_time=NORMAL)
        self.wait(1)

        # Explain variables
        vars_text = VGroup(
            Text("V = Vertices (points)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("E = Edges (connections)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("F = Faces (regions, including outer face)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        )
        self.ly.progressive_reveal(vars_text, start_from=formula_box)
        self.wait(1.5)
        self.ly.clear()

        # Example: cube graph (Q3) or simpler triangle-based
        example_title = Text("Example: A Planar Graph", font_size=BODY_SIZE, color=ACCENT, font=SANS)
        self.ly.center_in_content(example_title)
        self.play(FadeIn(example_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # A planar graph: triangle with one extra vertex connected to all three
        p_v = VGroup(
            Dot(UP * 1.5 + LEFT * 1, color=WHITE, radius=0.15),
            Dot(UP * 1.5 + RIGHT * 1, color=WHITE, radius=0.15),
            Dot(DOWN * 0.5, color=WHITE, radius=0.15),
            Dot(DOWN * 1.5, color=WHITE, radius=0.15),
        )
        p_edges = VGroup(
            Line(p_v[0].get_center(), p_v[1].get_center(), color=PRIMARY, stroke_width=3),
            Line(p_v[1].get_center(), p_v[2].get_center(), color=PRIMARY, stroke_width=3),
            Line(p_v[2].get_center(), p_v[0].get_center(), color=PRIMARY, stroke_width=3),
            Line(p_v[3].get_center(), p_v[0].get_center(), color=SECONDARY, stroke_width=3),
            Line(p_v[3].get_center(), p_v[1].get_center(), color=SECONDARY, stroke_width=3),
            Line(p_v[3].get_center(), p_v[2].get_center(), color=SECONDARY, stroke_width=3),
        )
        p_graph = VGroup(p_v, p_edges)
        self.ly.center_in_content(p_graph)
        self.play(
            Create(p_edges), LaggedStartMap(FadeIn, p_v, scale=0.5, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.wait(1)

        # Count: V=4, E=6, F=4
        counts = VGroup(
            MathTex(r"V = 4", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"E = 6", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"F = 4", font_size=BODY_SIZE, color=PRIMARY),
        )
        self.ly.progressive_reveal(counts, start_from=p_graph, spacing=0.3)
        self.wait(1)

        # Verify formula
        check = MathTex(r"4 - 6 + 4 = 2 \;\checkmark", font_size=HEADING_SIZE, color=ACCENT)
        self.ly.safe_place(check, direction=DOWN, anchor=counts[-1] if hasattr(self, '_last_visible') else counts[2], buff=0.4)
        self.play(Write(check), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Intuition: proof sketch via tree growing
        proof_title = Text("Proof idea: grow a spanning tree", font_size=BODY_SIZE, color=ACCENT, font=SANS)
        self.ly.center_in_content(proof_title)
        self.play(FadeIn(proof_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        proof_steps = [
            Text("Start with one vertex: V=1, E=0, F=1 (outer face)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Add edges one at a time (spanning tree): V-E+F stays 2", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Each new edge either adds 1 vertex (+1V,+1E) or 1 face (+1E,+1F)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("In both cases: V - E + F is unchanged!", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(proof_steps, start_from=proof_title)
        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Consequences of Euler's Formula (60s)
    # ------------------------------------------------------------------
    def scene4_consequences(self):
        self.add_subcaption(
            "Euler's formula gives us powerful tools. For simple planar graphs, "
            "each face has at least 3 edges, so we can derive E is at most "
            "3V minus 6. This inequality lets us prove that K5 is not planar.",
            duration=18,
        )
        self.ly.section_divider(3, "Consequences")

        # Bound for simple planar graphs
        bound_title = self.ly.title("Edge Bound for Simple Planar Graphs")

        bound1 = MathTex(r"E \leq 3V - 6", font_size=HEADING_SIZE, color=ACCENT)
        bound1_box = self.ly.formula_box(bound1, ACCENT)
        self.ly.safe_place(bound1_box, direction=DOWN, anchor=bound_title, buff=0.8)
        self.play(Write(bound1_box), run_time=NORMAL)
        self.wait(1)

        # Reasoning
        reasoning = [
            Text("Each face borders at least 3 edges (simple graph, no loops)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Each edge borders at most 2 faces", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("So: 2E >= 3F, plug into Euler's formula", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(reasoning, start_from=bound1_box)
        self.wait(2)
        self.ly.clear()

        # Apply to K5
        k5_proof = self.ly.title("K5 is NOT planar")

        k5_check = VGroup(
            MathTex(r"K_5:\; V=5,\; E=\binom{5}{2}=10", font_size=BODY_SIZE, color=WHITE),
        )
        self.ly.safe_place(k5_check[0], direction=DOWN, anchor=k5_proof, buff=0.8)
        self.play(Write(k5_check[0]), run_time=NORMAL)
        self.wait(0.5)

        k5_contra = MathTex(r"10 \leq 3(5) - 6 = 9 \;\;\text{CONTRADICTION!}", font_size=HEADING_SIZE, color=RED)
        self.ly.safe_place(k5_contra, direction=DOWN, anchor=k5_check[0], buff=0.6)
        self.play(Write(k5_contra), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Apply to K3,3 with bipartite bound
        bip_title = self.ly.title("K3,3 is NOT planar")

        bip_bound = MathTex(r"E \leq 2V - 4 \;\;\text{(bipartite planar)}", font_size=HEADING_SIZE, color=ACCENT)
        bip_box = self.ly.formula_box(bip_bound, ACCENT)
        self.ly.safe_place(bip_box, direction=DOWN, anchor=bip_title, buff=0.8)
        self.play(Write(bip_box), run_time=NORMAL)
        self.wait(1)

        k33_check = VGroup(
            MathTex(r"K_{3,3}:\; V=6,\; E=9", font_size=BODY_SIZE, color=WHITE),
        )
        self.ly.safe_place(k33_check[0], direction=DOWN, anchor=bip_box, buff=0.5)
        self.play(Write(k33_check[0]), run_time=NORMAL)
        self.wait(0.5)

        k33_contra = MathTex(r"9 \leq 2(6) - 4 = 8 \;\;\text{CONTRADICTION!}", font_size=HEADING_SIZE, color=RED)
        self.ly.safe_place(k33_contra, direction=DOWN, anchor=k33_check[0], buff=0.5)
        self.play(Write(k33_contra), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Kuratowski's Theorem (75s)
    # ------------------------------------------------------------------
    def scene5_kuratowski(self):
        self.add_subcaption(
            "Kuratowski's theorem gives a complete characterization: a graph is "
            "planar if and only if it contains no subdivision of K5 or K3,3. "
            "A subdivision replaces edges with paths, inserting extra vertices.",
            duration=18,
        )
        self.ly.section_divider(4, "Kuratowski's Theorem")

        # The theorem
        theorem = VGroup(
            Text("A graph is planar if and only if it contains", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("NO subdivision of K5 or K3,3", font_size=HEADING_SIZE, color=ACCENT, font=SANS),
        )
        theorem_group = VGroup(*theorem).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.ly.center_in_content(theorem_group)
        self.play(LaggedStartMap(FadeIn, theorem, shift=LEFT * 0.15, lag_ratio=0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Subdivision explanation
        sub_title = Text("What is a subdivision?", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        self.ly.center_in_content(sub_title)
        self.play(Write(sub_title), run_time=FAST)
        self.wait(0.5)

        sub_items = [
            Text("Replace an edge with a path (insert vertices)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The graph's topology does not change", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("If the original is non-planar, so is the subdivision", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(sub_items, start_from=sub_title)
        self.wait(1.5)
        self.ly.clear()

        # Show K5 and K3,3 as the forbidden minors
        forbidden_title = Text("The Two Forbidden Subgraphs", font_size=HEADING_SIZE, color=RED, font=SANS)
        self.ly.center_in_content(forbidden_title)
        self.play(Write(forbidden_title), run_time=NORMAL)
        self.wait(0.5)

        # K5 on left
        k5_verts = [
            UP * 1.2 + LEFT * 3.5,
            UP * 0.3 + LEFT * 5,
            DOWN * 0.6 + LEFT * 4.2,
            DOWN * 0.6 + LEFT * 2.8,
            UP * 0.3 + LEFT * 2,
        ]
        k5v = VGroup(*[Dot(p, color=WHITE, radius=0.11) for p in k5_verts])
        k5e = VGroup()
        for i in range(5):
            for j in range(i + 1, 5):
                k5e.add(Line(k5_verts[i], k5_verts[j], color=PRIMARY, stroke_width=2))
        k5_label = Text("K5", font_size=HEADING_SIZE, color=RED, font=SANS).next_to(k5v, DOWN, buff=0.3)
        k5_group = VGroup(k5v, k5e, k5_label)

        # K3,3 on right
        k33_left = [UP * 1.2 + RIGHT * 3.5, UP * 0 + RIGHT * 3.5, DOWN * 1.2 + RIGHT * 3.5]
        k33_right = [UP * 1.2 + RIGHT * 5.5, UP * 0 + RIGHT * 5.5, DOWN * 1.2 + RIGHT * 5.5]
        k33v = VGroup(*[Dot(p, color=WHITE, radius=0.11) for p in k33_left + k33_right])
        k33e = VGroup()
        for l in k33_left:
            for r in k33_right:
                k33e.add(Line(l, r, color=PRIMARY, stroke_width=2))
        k33_label = Text("K3,3", font_size=HEADING_SIZE, color=RED, font=SANS).next_to(k33v, DOWN, buff=0.3)
        k33_group = VGroup(k33v, k33e, k33_label)

        # Position side by side
        combined = VGroup(k5_group, k33_group).arrange(RIGHT, buff=1.5)
        self.ly.center_in_content(combined)
        self.play(
            LaggedStartMap(FadeIn, k5v, scale=0.5, lag_ratio=0.05),
            Create(k5e),
            FadeIn(k5_label),
            LaggedStartMap(FadeIn, k33v, scale=0.5, lag_ratio=0.05),
            Create(k33e),
            FadeIn(k33_label),
            run_time=NORMAL,
        )
        self.wait(1)

        # Check mark
        check_text = Text(
            "Contains K5 or K3,3 subdivision? NOT planar!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(check_text, direction=DOWN, anchor=combined, buff=0.5)
        self.play(FadeIn(check_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Applications (45s)
    # ------------------------------------------------------------------
    def scene6_applications(self):
        self.add_subcaption(
            "Planarity has real applications everywhere. Circuit board designers "
            "need to lay out connections without crossings. The famous four color "
            "theorem says every planar map needs at most four colors to color "
            "countries so no two adjacent countries share a color.",
            duration=18,
        )
        self.ly.section_divider(5, "Applications")

        title = self.ly.title("Where Planarity Matters")

        apps = [
            Text("Circuit boards: route wires without crossings", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Map coloring: four color theorem (max 4 colors)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Graph drawing: algorithms for nice visualizations", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Network design: planar overlays reduce interference", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(apps, start_from=title)
        self.wait(1.5)

        # Four color theorem preview
        fcc = Text(
            "Four Color Theorem: every planar map needs at most 4 colors!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        last_item = apps[-1] if hasattr(self, '_last_visible') else apps[3]
        self.ly.safe_place(fcc, direction=DOWN, anchor=last_item, buff=0.6)
        self.play(FadeIn(fcc, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Summary (45s)
    # ------------------------------------------------------------------
    def scene7_summary(self):
        self.add_subcaption(
            "Let's recap: planar graphs can be drawn without edge crossings. "
            "Euler's formula V minus E plus F equals 2 connects vertices, edges, "
            "and faces. Kuratowski's theorem tells us K5 and K3,3 are the obstacles.",
            duration=16,
        )

        title = self.ly.title("Planarity: Summary")

        points = [
            Text("Planar graph: drawable with no edge crossings", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Euler's formula: V - E + F = 2", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Edge bound: E <= 3V - 6 (simple planar)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("K5 and K3,3 are NOT planar (proved by inequalities)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Kuratowski: planar iff no K5/K3,3 subdivision", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        self.wait(2)

        # Bridge to next video
        next_note = Text(
            "Next: Graph Coloring",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        last_pt = points[-1] if hasattr(self, '_last_visible') else points[4]
        self.ly.safe_place(next_note, direction=DOWN, anchor=last_pt, buff=0.6)
        self.play(FadeIn(next_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Outro
    # ------------------------------------------------------------------
    def scene8_outro(self):
        self.add_subcaption(
            "Thanks for watching! Planarity is one of the most visual topics "
            "in graph theory. If you found this helpful, please like and subscribe.",
            duration=10,
        )
        play_outro(self, "Graph Coloring", "Discrete Mathematics")
