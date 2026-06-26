"Video 86: Graph Theory Basics
Discrete Mathematics -- Video 8 of 12

Covers: Graph definition, vertices and edges, degree, paths and cycles, connectedness, trees, and basic graph algorithms (BFS/DFS).

Plan: planning/video-86-graph-theory-basics.md

Render draft:  manim -ql scripts/undergraduate/video-86-graph-theory-basics.py Video86_GraphTheoryBasics
Render final:  manim -qh scripts/undergraduate/video-86-graph-theory-basics.py Video86_GraphTheoryBasics
"

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


class Video86_GraphTheoryBasics(Scene):
    """Graph Theory Basics: definitions, visualizations, and introductory algorithms."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definitions()
        self.scene3_visual_examples()
        self.scene4_degree_handshaking()
        self.scene5_paths_cycles()
        self.scene6_connected_trees()
        self.scene7_bfs_dfs()
        self.scene8_real_world()
        self.scene9_summary()
        self.scene10_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook -- The Seven Bridges of Königsberg (2:00)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "In 1736, Leonhard Euler faced a puzzle: could you walk through the city of Königsberg, crossing each of its seven bridges exactly once? This question birthed an entire field of mathematics.",
            duration=18,
        )
        play_intro(self, "Graph Theory Basics", "Discrete Mathematics")

        title = self.ly.title("The Bridges of Königsberg")

        # Show the city layout with rivers and bridges
        river = Line(LEFT * 4, RIGHT * 4, color=BLUE_D, stroke_width=8)
        island1 = Dot(UP * 1 + LEFT * 2, color=WHITE, radius=0.15)
        island2 = Dot(UP * 1 + RIGHT * 2, color=WHITE, radius=0.15)
        left_bank = Dot(DOWN * 1 + LEFT * 3, color=WHITE, radius=0.15)
        right_bank = Dot(DOWN * 1 + RIGHT * 3, color=WHITE, radius=0.15)

        # Seven bridges
        bridges = VGroup(
            Line(left_bank.get_top(), island1.get_bottom(), color=BROWN, stroke_width=4),
            Line(left_bank.get_top(), island1.get_bottom() + RIGHT * 0.5, color=BROWN, stroke_width=4),
            Line(left_bank.get_top(), island2.get_bottom(), color=BROWN, stroke_width=4),
            Line(island1.get_top(), right_bank.get_bottom(), color=BROWN, stroke_width=4),
            Line(island2.get_top(), right_bank.get_bottom(), color=BROWN, stroke_width=4),
            Line(island1.get_right(), island2.get_left(), color=BROWN, stroke_width=4),
            Line(island1.get_left() + UP * 0.3, island2.get_right() + DOWN * 0.3, color=BROWN, stroke_width=4),
        )

        self.ly.safe_place(river, direction=DOWN)
        self.ly.safe_place(island1, direction=UP, anchor=river, buff=0.5)
        self.ly.safe_place(island2, direction=UP, anchor=river, buff=0.5)
        self.ly.safe_place(left_bank, direction=DOWN, anchor=river, buff=0.5)
        self.ly.safe_place(right_bank, direction=DOWN, anchor=river, buff=0.5)

        self.play(
            Create(river),
            FadeIn(VGroup(island1, island2, left_bank, right_bank), scale=0.5),
            Create(bridges),
            run_time=NORMAL,
        )
        self.wait(2)

        question = Text(
            "Can you cross each bridge exactly once?", font_size=HEADING_SIZE, color=YELLOW
        )
        self.ly.safe_place(question, direction=DOWN, anchor=bridges, buff=0.8)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        euler_note = Text(
            "Euler proved it's impossible... and invented graph theory to do it.",
            font_size=BODY_SIZE,
            color=WHITE,
        )
        self.ly.safe_place(euler_note, direction=DOWN, anchor=question, buff=0.6)
        self.play(FadeIn(euler_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Basic Definitions (2:00)
    # ------------------------------------------------------------------
    def scene2_definitions(self):
        self.add_subcaption(
            "A graph is simply a collection of points, called vertices, connected by lines called edges. That's it—no jargon, just dots and lines.",
            duration=16,
        )

        title = self.ly.title("What is a Graph?")
        self.play(FadeIn(title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Simple graph: 4 vertices, 4 edges
        vertices = VGroup(
            Dot(UP * 2 + LEFT * 2, color=WHITE, radius=0.15),
            Dot(UP * 2 + RIGHT * 2, color=WHITE, radius=0.15),
            Dot(DOWN * 2 + LEFT * 2, color=WHITE, radius=0.15),
            Dot(DOWN * 2 + RIGHT * 2, color=WHITE, radius=0.15),
        )
        labels = VGroup(
            Text("A", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[0], LEFT),
            Text("B", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[1], RIGHT),
            Text("C", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[2], LEFT),
            Text("D", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[3], RIGHT),
        )
        edges = VGroup(
            Line(vertices[0].get_center(), vertices[1].get_center(), color=PRIMARY, stroke_width=4),
            Line(vertices[1].get_center(), vertices[3].get_center(), color=PRIMARY, stroke_width=4),
            Line(vertices[3].get_center(), vertices[2].get_center(), color=PRIMARY, stroke_width=4),
            Line(vertices[2].get_center(), vertices[0].get_center(), color=PRIMARY, stroke_width=4),
        )

        self.ly.safe_place(vertices, direction=DOWN, anchor=title, buff=1)
        self.play(
            LaggedStartMap(FadeIn, vertices, scale=0.5, lag_ratio=0.2),
            LaggedStartMap(FadeIn, labels, scale=0.5, lag_ratio=0.2),
            run_time=NORMAL,
        )
        self.play(Create(edges), run_time=NORMAL)
        self.wait(1)

        definition = VGroup(
            Text("Vertex (node):", font_size=BODY_SIZE, color=YELLOW),
            Text("A point in the graph", font_size=BODY_SIZE, color=WHITE),
            Text("Edge (link):", font_size=BODY_SIZE, color=YELLOW),
            Text("A connection between two vertices", font_size=BODY_SIZE, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        definition[0::2].set_color(YELLOW)  # Labels
        definition[1::2].set_color(WHITE)  # Definitions

        self.ly.safe_place(definition, direction=DOWN, anchor=vertices, buff=0.8)
        self.play(
            LaggedStartMap(FadeIn, definition, shift=LEFT * 0.15, lag_ratio=0.3),
            run_time=NORMAL,
        )
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Visual Examples (2:00)
    # ------------------------------------------------------------------
    def scene3_visual_examples(self):
        self.add_subcaption(
            "Let's look at some examples. This graph has 4 vertices and 4 edges forming a cycle. This one has 3 vertices all connected to each other—a complete graph.",
            duration=18,
        )

        title = self.ly.title("Graph Examples")
        self.play(FadeIn(title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Example 1: Cycle
        cycle_title = Text("Cycle C₄", font_size=LABEL_SIZE, color=GREEN)
        cycle_vertices = VGroup(
            Dot(LEFT * 3 + UP * 1, color=WHITE, radius=0.12),
            Dot(LEFT * 1 + UP * 1, color=WHITE, radius=0.12),
            Dot(LEFT * 1 + DOWN * 1, color=WHITE, radius=0.12),
            Dot(LEFT * 3 + DOWN * 1, color=WHITE, radius=0.12),
        )
        cycle_edges = VGroup(
            Line(cycle_vertices[0].get_center(), cycle_vertices[1].get_center(), color=BLUE, stroke_width=3),
            Line(cycle_vertices[1].get_center(), cycle_vertices[2].get_center(), color=BLUE, stroke_width=3),
            Line(cycle_vertices[2].get_center(), cycle_vertices[3].get_center(), color=BLUE, stroke_width=3),
            Line(cycle_vertices[3].get_center(), cycle_vertices[0].get_center(), color=BLUE, stroke_width=3),
        )
        cycle_label = VGroup(cycle_title, cycle_vertices, cycle_edges).arrange(DOWN, buff=0.3)

        # Example 2: Complete graph
        complete_title = Text("Complete K₃", font_size=LABEL_SIZE, color=GREEN)
        complete_vertices = VGroup(
            Dot(RIGHT * 2 + UP * 1, color=WHITE, radius=0.12),
            Dot(RIGHT * 3 + UP * 0.5, color=WHITE, radius=0.12),
            Dot(RIGHT * 2.5 + DOWN * 0.5, color=WHITE, radius=0.12),
        )
        complete_edges = VGroup(
            Line(complete_vertices[0].get_center(), complete_vertices[1].get_center(), color=GREEN, stroke_width=3),
            Line(complete_vertices[1].get_center(), complete_vertices[2].get_center(), color=GREEN, stroke_width=3),
            Line(complete_vertices[2].get_center(), complete_vertices[0].get_center(), color=GREEN, stroke_width=3),
        )
        complete_label = VGroup(complete_title, complete_vertices, complete_edges).arrange(DOWN, buff=0.3)

        examples = VGroup(cycle_label, complete_label).arrange(RIGHT, buff=2)
        self.ly.safe_place(examples, direction=DOWN, anchor=title, buff=0.8)

        self.play(
            LaggedStartMap(FadeIn, cycle_vertices, scale=0.4, lag_ratio=0.2),
            LaggedStartMap(FadeIn, complete_vertices, scale=0.4, lag_ratio=0.2),
            run_time=NORMAL,
        )
        self.play(
            Create(cycle_edges),
            Create(complete_edges),
            run_time=NORMAL,
        )
        self.play(
            FadeIn(cycle_title, shift=LEFT * 0.1),
            FadeIn(complete_title, shift=LEFT * 0.1),
            run_time=NORMAL,
        )
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Degree and Handshaking Lemma (2:00)
    # ------------------------------------------------------------------
    def scene4_degree_handshaking(self):
        self.add_subcaption(
            "The degree of a vertex is how many edges touch it. Here, vertex A has degree 3. Notice something: if we add up all the degrees, we get twice the number of edges. Why?",
            duration=18,
        )

        title = self.ly.title("Vertex Degree")
        self.play(FadeIn(title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Graph for degree demonstration
        vertices = VGroup(
            Dot(LEFT * 3, color=WHITE, radius=0.15),  # A
            Dot(LEFT * 1, color=WHITE, radius=0.15),  # B
            Dot(RIGHT * 1, color=WHITE, radius=0.15), # C
            Dot(RIGHT * 3, color=WHITE, radius=0.15), # D
        )
        labels = VGroup(
            Text("A", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[0], LEFT),
            Text("B", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[1], LEFT),
            Text("C", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[2], RIGHT),
            Text("D", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[3], RIGHT),
        )
        edges = VGroup(
            Line(vertices[0].get_center(), vertices[1].get_center(), color=PRIMARY, stroke_width=4),  # A-B
            Line(vertices[0].get_center(), vertices[2].get_center(), color=PRIMARY, stroke_width=4),  # A-C
            Line(vertices[0].get_center(), vertices[3].get_center(), color=PRIMARY, stroke_width=4),  # A-D
            Line(vertices[1].get_center(), vertices[2].get_center(), color=PRIMARY, stroke_width=4),  # B-C
            Line(vertices[2].get_center(), vertices[3].get_center(), color=PRIMARY, stroke_width=4),  # C-D
        )

        self.ly.safe_place(vertices, direction=DOWN, anchor=title, buff=1)
        self.play(
            LaggedStartMap(FadeIn, vertices, scale=0.5, lag_ratio=0.2),
            LaggedStartMap(FadeIn, labels, scale=0.5, lag_ratio=0.2),
            run_time=NORMAL,
        )
        self.play(Create(edges), run_time=NORMAL)
        self.wait(0.5)

        # Highlight vertex A and its edges
        self.play(
            vertices[0].animate.set_color(YELLOW).scale(1.3),
            edges[0].animate.set_color(YELLOW).scale(1.2),
            edges[1].animate.set_color(YELLOW).scale(1.2),
            edges[2].animate.set_color(YELLOW).scale(1.2),
            run_time=NORMAL,
        )
        deg_label = Text("deg(A) = 3", font_size=BODY_SIZE, color=YELLOW)
        self.ly.safe_place(deg_label, direction=DOWN, anchor=vertices[0], buff=0.5)
        self.play(FadeIn(deg_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.play(
            vertices[0].animate.set_color(WHITE).scale(1/1.3),
            edges[0].animate.set_color(PRIMARY).scale(1/1.2),
            edges[1].animate.set_color(PRIMARY).scale(1/1.2),
            edges[2].animate.set_color(PRIMARY).scale(1/1.2),
            FadeOut(deg_label),
            run_time=NORMAL,
        )

        # Show degree calculation
        degree_label = Text("Degree = number of incident edges", font_size=BODY_SIZE, color=WHITE)
        self.ly.safe_place(degree_label, direction=DOWN, anchor=title, buff=1.8)
        self.play(FadeIn(degree_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Sum of degrees = 2 * |E|
        deg_sum = VGroup(
            Text("deg(A) + deg(B) + deg(C) + deg(D) = ", font_size=BODY_SIZE, color=WHITE),
            Text("3 + 2 + 2 + 3 = 10", font_size=BODY_SIZE, color=YELLOW),
            Text("2 × |E| = 2 × 5 = 10", font_size=BODY_SIZE, color=YELLOW),
        ).arrange(RIGHT, buff=0.3)
        self.ly.safe_place(deg_sum, direction=DOWN, anchor=degree_label, buff=0.5)

        self.play(FadeIn(deg_sum[0], shift=LEFT * 0.15), run_time=NORMAL)
        self.play(FadeIn(deg_sum[1], shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeIn(deg_sum[2], shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        # Handshaking lemma
        hlemma = Text(
            "Handshaking Lemma: Σ deg(v) = 2|E|\n(Each edge contributes 2 to the degree sum)",
            font_size=BODY_SIZE,
            color=GREEN,
        )
        self.ly.safe_place(hlemma, direction=DOWN, anchor=deg_sum, buff=0.6)
        self.play(FadeIn(hlemma, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Paths and Cycles (2:00)
    # ------------------------------------------------------------------
    def scene5_paths_cycles(self):
        self.add_subcaption(
            "A path is a sequence of vertices where each consecutive pair is connected by an edge. If the path starts and ends at the same vertex, it's a cycle.",
            duration=18,
        )

        title = self.ly.title("Paths and Cycles")
        self.play(FadeIn(title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Create a graph
        vertices = VGroup(
            Dot(LEFT * 3 + UP * 1, color=WHITE, radius=0.12),
            Dot(LEFT * 1 + UP * 1, color=WHITE, radius=0.12),
            Dot(RIGHT * 1 + UP * 1, color=WHITE, radius=0.12),
            Dot(LEFT * 2 + DOWN * 1, color=WHITE, radius=0.12),
            Dot(RIGHT * 2 + DOWN * 1, color=WHITE, radius=0.12),
        )
        labels = VGroup(
            Text("A", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[0], UP),
            Text("B", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[1], UP),
            Text("C", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[2], UP),
            Text("D", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[3], DOWN),
            Text("E", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[4], DOWN),
        )
        edges = VGroup(
            Line(vertices[0].get_center(), vertices[1].get_center(), color=BLUE, stroke_width=3),  # A-B
            Line(vertices[1].get_center(), vertices[2].get_center(), color=BLUE, stroke_width=3),  # B-C
            Line(vertices[2].get_center(), vertices[4].get_center(), color=BLUE, stroke_width=3),  # C-E
            Line(vertices[4].get_center(), vertices[3].get_center(), color=BLUE, stroke_width=3),  # E-D
            Line(vertices[3].get_center(), vertices[0].get_center(), color=BLUE, stroke_width=3),  # D-A
            Line(vertices[0].get_center(), vertices[3].get_center(), color=GREY, stroke_width=2),  # A-D (diagonal)
        )

        self.ly.safe_place(vertices, direction=DOWN, anchor=title, buff=1)
        self.play(
            LaggedStartMap(FadeIn, vertices, scale=0.4, lag_ratio=0.2),
            LaggedStartMap(FadeIn, labels, scale=0.4, lag_ratio=0.2),
            run_time=NORMAL,
        )
        self.play(Create(edges), run_time=NORMAL)
        self.wait(0.5)

        # Highlight a path: A -> B -> C -> E
        path_vertices = VGroup(vertices[0], vertices[1], vertices[2], vertices[4])
        path_edges = VGroup(edges[0], edges[1], edges[2])
        self.play(
            path_vertices.animate.set_color(YELLOW).scale(1.3),
            path_edges.animate.set_color(YELLOW).scale(1.2),
            run_time=NORMAL,
        )
        path_label = Text("Path: A→B→C→E", font_size=BODY_SIZE, color=YELLOW)
        self.ly.safe_place(path_label, direction=DOWN, anchor=title, buff=2.2)
        self.play(FadeIn(path_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.play(
            path_vertices.animate.set_color(WHITE).scale(1/1.3),
            path_edges.animate.set_color(BLUE).scale(1/1.2),
            FadeOut(path_label),
            run_time=NORMAL,
        )

        # Highlight a cycle: A -> B -> C -> E -> D -> A
        cycle_vertices = VGroup(vertices[0], vertices[1], vertices[2], vertices[4], vertices[3])
        cycle_edges = VGroup(edges[0], edges[1], edges[2], edges[3], edges[4])
        self.play(
            cycle_vertices.animate.set_color(GREEN).scale(1.3),
            cycle_edges.animate.set_color(GREEN).scale(1.2),
            run_time=NORMAL,
        )
        cycle_label = Text("Cycle: A→B→C→E→D→A", font_size=BODY_SIZE, color=GREEN)
        self.ly.safe_place(cycle_label, direction=DOWN, anchor=title, buff=2.2)
        self.play(FadeIn(cycle_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.play(
            cycle_vertices.animate.set_color(WHITE).scale(1/1.3),
            cycle_edges.animate.set_color(BLUE).scale(1/1.2),
            FadeOut(cycle_label),
            run_time=NORMAL,
        )

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Connectedness and Trees (2:00)
    # ------------------------------------------------------------------
    def scene6_connected_trees(self):
        self.add_subcaption(
            "A graph is connected if there's a path between every pair of vertices. A tree is a connected graph with no cycles—minimally connected.",
            duration=18,
        )

        title = self.ly.title("Connected Graphs and Trees")
        self.play(FadeIn(title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Connected graph (with cycle)
        conn_title = Text("Connected (has cycle)", font_size=LABEL_SIZE, color=BLUE)
        conn_vertices = VGroup(
            Dot(LEFT * 3 + UP * 1, color=WHITE, radius=0.12),
            Dot(LEFT * 1 + UP * 1, color=WHITE, radius=0.12),
            Dot(RIGHT * 1 + UP * 1, color=WHITE, radius=0.12),
            Dot(LEFT * 2 + DOWN * 1, color=WHITE, radius=0.12),
        )
        conn_edges = VGroup(
            Line(conn_vertices[0].get_center(), conn_vertices[1].get_center(), color=BLUE, stroke_width=3),
            Line(conn_vertices[1].get_center(), conn_vertices[2].get_center(), color=BLUE, stroke_width=3),
            Line(conn_vertices[2].get_center(), conn_vertices[3].get_center(), color=BLUE, stroke_width=3),
            Line(conn_vertices[3].get_center(), conn_vertices[0].get_center(), color=BLUE, stroke_width=3),  # Creates cycle
            Line(conn_vertices[0].get_center(), conn_vertices[2].get_center(), color=BLUE, stroke_width=3),  # Extra edge
        )
        conn_group = VGroup(conn_title, conn_vertices, conn_edges).arrange(DOWN, buff=0.3)

        # Tree (connected, no cycles)
        tree_title = Text("Tree (connected, no cycles)", font_size=LABEL_SIZE, color=GREEN)
        tree_vertices = VGroup(
            Dot(RIGHT * 3 + UP * 1.5, color=WHITE, radius=0.12),
            Dot(RIGHT * 2 + UP * 0.5, color=WHITE, radius=0.12),
            Dot(RIGHT * 4 + UP * 0.5, color=WHITE, radius=0.12),
            Dot(RIGHT * 1 + DOWN * 0.5, color=WHITE, radius=0.12),
            Dot(RIGHT * 3 + DOWN * 0.5, color=WHITE, radius=0.12),
            Dot(RIGHT * 5 + DOWN * 0.5, color=WHITE, radius=0.12),
        )
        tree_edges = VGroup(
            Line(tree_vertices[0].get_center(), tree_vertices[1].get_center(), color=GREEN, stroke_width=3),
            Line(tree_vertices[0].get_center(), tree_vertices[2].get_center(), color=GREEN, stroke_width=3),
            Line(tree_vertices[1].get_center(), tree_vertices[3].get_center(), color=GREEN, stroke_width=3),
            Line(tree_vertices[2].get_center(), tree_vertices[4].get_center(), color=GREEN, stroke_width=3),
            Line(tree_vertices[2].get_center(), tree_vertices[5].get_center(), color=GREEN, stroke_width=3),
        )
        tree_group = VGroup(tree_title, tree_vertices, tree_edges).arrange(DOWN, buff=0.3)

        groups = VGroup(conn_group, tree_group).arrange(RIGHT, buff=1.5)
        self.ly.safe_place(groups, direction=DOWN, anchor=title, buff=0.8)

        # Show connected graph
        self.play(
            LaggedStartMap(FadeIn, conn_vertices, scale=0.4, lag_ratio=0.2),
            LaggedStartMap(FadeIn, conn_edges, lag_ratio=0.2),
            run_time=NORMAL,
        )
        self.play(FadeIn(conn_title, shift=LEFT * 0.1), run_time=NORMAL)
        self.wait(0.5)

        # Show tree
        self.play(
            LaggedStartMap(FadeIn, tree_vertices, scale=0.4, lag_ratio=0.2),
            LaggedStartMap(FadeIn, tree_edges, lag_ratio=0.2),
            run_time=NORMAL,
        )
        self.play(FadeIn(tree_title, shift=LEFT * 0.1), run_time=NORMAL)
        self.wait(1)

        # Property: For a tree, |E| = |V| - 1
        tree_prop = VGroup(
            Text("For any tree:", font_size=BODY_SIZE, color=YELLOW),
            Text("|E| = |V| - 1", font_size=BODY_SIZE, color=WHITE),
            Text("(6 vertices → 5 edges)", font_size=BODY_SIZE, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        self.ly.safe_place(tree_prop, direction=DOWN, anchor=tree_group, buff=0.6)
        self.play(
            LaggedStartMap(FadeIn, tree_prop, shift=LEFT * 0.15, lag_ratio=0.2),
            run_time=NORMAL,
        )
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: BFS and DFS (2:00)
    # ------------------------------------------------------------------
    def scene7_bfs_dfs(self):
        self.add_subcaption(
            "Breadth-first search explores level by level. Depth-first goes as deep as possible before backtracking. Both are fundamental for exploring graphs.",
            duration=18,
        )

        title = self.ly.title("Graph Traversal: BFS vs DFS")
        self.play(FadeIn(title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Create a binary tree-like graph for traversal
        vertices = VGroup(
            Dot(LEFT * 4 + UP * 2, color=WHITE, radius=0.12),  # A (0)
            Dot(LEFT * 2 + UP * 2, color=WHITE, radius=0.12),  # B (1)
            Dot(LEFT * 0 + UP * 2, color=WHITE, radius=0.12),  # C (2)
            Dot(LEFT * 4 + UP * 0, color=WHITE, radius=0.12),  # D (3)
            Dot(LEFT * 2 + UP * 0, color=WHITE, radius=0.12),  # E (4)
            Dot(LEFT * 0 + UP * 0, color=WHITE, radius=0.12),   # F (5)
            Dot(LEFT * 4 + DOWN * 2, color=WHITE, radius=0.12), # G (6)
            Dot(LEFT * 2 + DOWN * 2, color=WHITE, radius=0.12), # H (7)
            Dot(LEFT * 0 + DOWN * 2, color=WHITE, radius=0.12), # I (8)
        )
        labels = VGroup(
            Text("A", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[0], UP),
            Text("B", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[1], UP),
            Text("C", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[2], UP),
            Text("D", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[3], DOWN),
            Text("E", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[4], DOWN),
            Text("F", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[5], DOWN),
            Text("G", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[6], DOWN),
            Text("H", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[7], DOWN),
            Text("I", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[8], DOWN),
        )
        edges = VGroup(
            Line(vertices[0].get_center(), vertices[1].get_center(), color=BLUE, stroke_width=3),  # A-B
            Line(vertices[0].get_center(), vertices[2].get_center(), color=BLUE, stroke_width=3),  # A-C
            Line(vertices[1].get_center(), vertices[3].get_center(), color=BLUE, stroke_width=3),  # B-D
            Line(vertices[1].get_center(), vertices[4].get_center(), color=BLUE, stroke_width=3),  # B-E
            Line(vertices[2].get_center(), vertices[5].get_center(), color=BLUE, stroke_width=3),  # C-F
            Line(vertices[3].get_center(), vertices[6].get_center(), color=BLUE, stroke_width=3),  # D-G
            Line(vertices[3].get_center(), vertices[7].get_center(), color=BLUE, stroke_width=3),  # D-H
            Line(vertices[4].get_center(), vertices[7].get_center(), color=BLUE, stroke_width=3),  # E-H
            Line(vertices[5].get_center(), vertices[8].get_center(), color=BLUE, stroke_width=3),  # F-I
        )

        self.ly.safe_place(vertices, direction=DOWN, anchor=title, buff=1)
        self.play(
            LaggedStartMap(FadeIn, vertices, scale=0.3, lag_ratio=0.1),
            LaggedStartMap(FadeIn, labels, scale=0.3, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.play(Create(edges), run_time=NORMAL)
        self.wait(0.5)

        # BFS demonstration
        bfs_title = Text("BFS: Visit A, then B,C, then D,E,F, then G,H,I", font_size=BODY_SIZE, color=GREEN)
        self.ly.safe_place(bfs_title, direction=DOWN, anchor=title, buff=2.2)
        self.play(FadeIn(bfs_title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Animate BFS levels
        level1 = VGroup(vertices[0])  # A
        level2 = VGroup(vertices[1], vertices[2])  # B, C
        level3 = VGroup(vertices[3], vertices[4], vertices[5])  # D, E, F
        level4 = VGroup(vertices[6], vertices[7], vertices[8])  # G, H, I

        self.play(
            lagged_start=lag_ratio=0.1,
            run_time=NORMAL,
            *[
                v.animate.set_color(YELLOW).scale(1.3)
                for v in level1
            ]
        )
        self.wait(0.5)
        self.play(
            *[v.animate.set_color(WHITE).scale(1/1.3) for v in level1],
            *[v.animate.set_color(YELLOW).scale(1.3) for v in level2],
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(
            *[v.animate.set_color(WHITE).scale(1/1.3) for v in level2],
            *[v.animate.set_color(YELLOW).scale(1.3) for v in level3],
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(
            *[v.animate.set_color(WHITE).scale(1/1.3) for v in level3],
            *[v.animate.set_color(YELLOW).scale(1.3) for v in level4],
            run_time=NORMAL,
        )
        self.wait(1)
        self.play(
            *[v.animate.set_color(WHITE).scale(1/1.3) for v in level4],
            run_time=NORMAL,
        )
        self.play(FadeOut(bfs_title), run_time=NORMAL)

        # DFS demonstration
        dfs_title = Text("DFS: Go deep A→B→D→G, backtrack, then B→E→H, etc.", font_size=BODY_SIZE, color=YELLOW)
        self.ly.safe_place(dfs_title, direction=DOWN, anchor=title, buff=2.2)
        self.play(FadeIn(dfs_title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Simple DFS-like path (not full algorithm, just illustration)
        dfs_path = VGroup(
            vertices[0], vertices[1], vertices[3], vertices[6],  # A-B-D-G
            vertices[4], vertices[7],  # B-E-H
            vertices[5], vertices[8],  # C-F-I
        )
        dfs_edges = VGroup(
            edges[0], edges[3], edges[6],  # A-B, B-D, D-G
            edges[4], edges[7],  # B-E, E-H
            edges[1], edges[5],  # A-C, C-F
            edges[8],  # F-I
        )

        self.play(
            LaggedStart(
                lambda m: m.animate.set_color(RED).scale(1.3),
                dfs_path,
                lag_ratio=0.2,
            ),
            LaggedStart(
                lambda m: m.animate.set_color(RED).scale(1.2),
                dfs_edges,
                lag_ratio=0.2,
            ),
            run_time=NORMAL,
        )
        self.wait(1.5)
        self.play(
            LaggedStart(
                lambda m: m.animate.set_color(WHITE).scale(1/1.3),
                dfs_path,
                lag_ratio=0.2,
            ),
            LaggedStart(
                lambda m: m.animate.set_color(BLUE).scale(1/1.2),
                dfs_edges,
                lag_ratio=0.2,
            ),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(dfs_title), run_time=NORMAL)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Real World Applications (2:00)
    # ------------------------------------------------------------------
    def scene8_real_world(self):
        self.add_subcaption(
            "Graphs aren't just abstract math—they're everywhere: social networks, transportation systems, molecular structures, and computer networks all use graph theory.",
            duration=18,
        )

        title = self.ly.title("Graphs in the Real World")
        self.play(FadeIn(title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Social network
        social_title = Text("Social Network", font_size=LABEL_SIZE, color=RED)
        social_people = VGroup(
            Dot(LEFT * 4 + UP * 1, color=WHITE, radius=0.1),
            Dot(LEFT * 2 + UP * 1, color=WHITE, radius=0.1),
            Dot(LEFT * 0 + UP * 1, color=WHITE, radius=0.1),
            Dot(LEFT * 2 + DOWN * 1, color=WHITE, radius=0.1),
            Dot(LEFT * 4 + DOWN * 1, color=WHITE, radius=0.1),
        )

        social_friends = VGroup(
            Line(social_people[0].get_center(), social_people[1].get_center(), color=RED, stroke_width=2),
            Line(social_people[0].get_center(), social_people[2].get_center(), color=RED, stroke_width=2),
            Line(social_people[1].get_center(), social_people[3].get_center(), color=RED, stroke_width=2),
            Line(social_people[2].get_center(), social_people[4].get_center(), color=RED, stroke_width=2),
            Line(social_people[3].get_center(), social_people[4].get_center(), color=RED, stroke_width=2),
        )
        social_group = VGroup(social_title, social_people, social_friends).arrange(DOWN, buff=0.2)
<tool_call>
<function=terminal>
<parameter=command>
cat >> ~/math-channel/scripts/undergraduate/video-86-graph-theory-basics.py << 'EOF'

        social_friends = VGroup(
            Line(social_people[0].get_center(), social_people[1].get_center(), color=RED, stroke_width=2),
            Line(social_people[0].get_center(), social_people[2].get_center(), color=RED, stroke_width=2),
            Line(social_people[1].get_center(), social_people[3].get_center(), color=RED, stroke_width=2),
            Line(social_people[2].get_center(), social_people[4].get_center(), color=RED, stroke_width=2),
            Line(social_people[3].get_center(), social_people[4].get_center(), color=RED, stroke_width=2),
        )
        social_group = VGroup(social_title, social_people, social_friends).arrange(DOWN, buff=0.2)

        # Transportation network
        transport_title = Text("Transportation Network", font_size=LABEL_SIZE, color=BLUE)
        transport_stops = VGroup(
            Dot(LEFT * 2, color=WHITE, radius=0.08),
            Dot(ORIGIN, color=WHITE, radius=0.08),
            Dot(RIGHT * 2, color=WHITE, radius=0.08),
            Dot(UP * 1.5, color=WHITE, radius=0.08),
            Dot(DOWN * 1.5, color=WHITE, radius=0.08),
        )
        transport_routes = VGroup(
            Line(transport_stops[0].get_center(), transport_stops[1].get_center(), color=BLUE, stroke_width=2),
            Line(transport_stops[1].get_center(), transport_stops[2].get_center(), color=BLUE, stroke_width=2),
            Line(transport_stops[1].get_center(), transport_stops[3].get_center(), color=BLUE, stroke_width=2),
            Line(transport_stops[1].get_center(), transport_stops[4].get_center(), color=BLUE, stroke_width=2),
            Line(transport_stops[0].get_center(), transport_stops[3].get_center(), color=BLUE, stroke_width=1, stroke_opacity=0.5),
            Line(transport_stops[2].get_center(), transport_stops[4].get_center(), color=BLUE, stroke_width=1, stroke_opacity=0.5),
        )
        transport_group = VGroup(transport_title, transport_stops, transport_routes).arrange(DOWN, buff=0.2)

        # Internet/network
        tech_title = Text("Internet / Computer Network", font_size=LABEL_SIZE, color=GREEN)
        tech_devices = VGroup(
            Dot(LEFT * 3 + UP * 1, color=WHITE, radius=0.1),
            Dot(LEFT * 1 + UP * 1, color=WHITE, radius=0.1),
            Dot(RIGHT * 1 + UP * 1, color=WHITE, radius=0.1),
            Dot(RIGHT * 3 + UP * 1, color=WHITE, radius=0.1),
            Dot(LEFT * 2 + DOWN * 1, color=WHITE, radius=0.1),
            Dot(RIGHT * 2 + DOWN * 1, color=WHITE, radius=0.1),
        )
        tech_connections = VGroup(
            Line(tech_devices[0].get_center(), tech_devices[1].get_center(), color=GREEN, stroke_width=2),
            Line(tech_devices[0].get_center(), tech_devices[2].get_center(), color=GREEN, stroke_width=2),
            Line(tech_devices[1].get_center(), tech_devices[3].get_center(), color=GREEN, stroke_width=2),
            Line(tech_devices[2].get_center(), tech_devices[3].get_center(), color=GREEN, stroke_width=2),
            Line(tech_devices[1].get_center(), tech_devices[4].get_center(), color=GREEN, stroke_width=2),
            Line(tech_devices[2].get_center(), tech_devices[5].get_center(), color=GREEN, stroke_width=2),
            Line(tech_devices[4].get_center(), tech_devices[5].get_center(), color=GREEN, stroke_width=2),
        )
        tech_group = VGroup(tech_title, tech_devices, tech_connections).arrange(DOWN, buff=0.2)

        # Molecular structure
        bio_title = Text("Molecular Structure", font_size=LABEL_SIZE, color=YELLOW)
        bio_atoms = VGroup(
            Dot(LEFT * 2, color=RED, radius=0.12),  # Carbon
            Dot(LEFT * 1, color=WHITE, radius=0.08), # H
            Dot(LEFT * 3, color=WHITE, radius=0.08), # H
            Dot(RIGHT * 1, color=WHITE, radius=0.08), # H
            Dot(RIGHT * 3, color=WHITE, radius=0.08), # H
        )
        bio_bonds = VGroup(
            Line(bio_atoms[0].get_center(), bio_atoms[1].get_center(), color=YELLOW, stroke_width=3),
            Line(bio_atoms[0].get_center(), bio_atoms[2].get_center(), color=YELLOW, stroke_width=3),
            Line(bio_atoms[0].get_center(), bio_atoms[3].get_center(), color=YELLOW, stroke_width=3),
            Line(bio_atoms[0].get_center(), bio_atoms[4].get_center(), color=YELLOW, stroke_width=3),
        )
        bio_group = VGroup(bio_title, bio_atoms, bio_bonds).arrange(DOWN, buff=0.2)

        examples = VGroup(social_group, transport_group, tech_group, bio_group).arrange_in_grid(
            rows=2, cols=2, buff=0.8
        )
        self.ly.safe_place(examples, direction=DOWN, anchor=title, buff=0.8)

        # Animate each example
        for group in [social_group, transport_group, tech_group, bio_group]:
            self.play(
                FadeIn(group[0], shift=LEFT * 0.1),  # title
                run_time=NORMAL / 2,
            )
            self.wait(0.2)
            self.play(
                FadeIn(group[1], scale=0.5),  # nodes/dots
                run_time=NORMAL / 2,
            )
            self.wait(0.2)
            self.play(
                Create(group[2]),  # connections/lines
                run_time=NORMAL / 2,
            )
            self.wait(0.3)

        self.wait(1)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Summary (1:30)
    # ------------------------------------------------------------------
    def scene9_summary(self):
        self.add_subcaption(
            "Let's recap: graphs model relationships with vertices and edges. Key concepts: degree, paths, cycles, connectedness, trees, and traversal algorithms like BFS and DFS.",
            duration=16,
        )

        title = self.ly.title("Graph Theory Basics: Summary")
        self.play(FadeIn(title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Key points in a vertical list
        points = VGroup(
            Text("• Vertices (nodes) and edges (links)", font_size=BODY_SIZE, color=WHITE),
            Text("• Degree: edges touching a vertex", font_size=BODY_SIZE, color=WHITE),
            Text("• Paths and cycles: walks through the graph", font_size=BODY_SIZE, color=WHITE),
            Text("• Connected: path between every vertex pair", font_size=BODY_SIZE, color=WHITE),
            Text("• Tree: connected + no cycles → |E| = |V|-1", font_size=BODY_SIZE, color=WHITE),
            Text("• BFS/DFS: fundamental graph traversal algorithms", font_size=BODY_SIZE, color=WHITE),
            Text("• Real-world: social, transportation, molecular networks", font_size=BODY_SIZE, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        self.ly.safe_place(points, direction=DOWN, anchor=title, buff=0.8)

        self.play(
            LaggedStartMap(FadeIn, points, shift=LEFT * 0.15, lag_ratio=0.2),
            run_time=NORMAL,
        )
        self.wait(2)

        # Bridge to next video
        next_preview = Text(
            "Next: Trees - special graphs with unique properties and applications",
            font_size=BODY_SIZE,
            color=YELLOW,
        )
        self.ly.safe_place(next_preview, direction=DOWN, anchor=points, buff=0.8)
        self.play(FadeIn(next_preview, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Outro
    # ------------------------------------------------------------------
    def scene10_outro(self):
        self.add_subcaption(
            "Thanks for watching! If you enjoyed seeing graph theory come alive, please like and subscribe for more visual math.",
            duration=10,
        )
        play_outro(self, "Trees and Forest Structures", "Discrete Mathematics")
```

This means that when I did my patch, it didn't remove all the corrupted text - it left the terminal command text that was after the corrupted section.

I need to remove that corrupted terminal command text and everything from there until the correct content resumes. Looking at the output, after that terminal command text, I should see the social_friends definition.

Let me check what comes after that terminal command text<tool_call>
<function=terminal>
<parameter=command>
head -n 690 /root/math-channel/scripts/undergraduate/video-86-graph-theory-basics.py | tail -n 20
