"""
Video 87: Trees in Discrete Mathematics
Discrete Mathematics -- Video 10 of 12

Covers: Tree definition, visual proof of |E| = |V| - 1, forests, rooted trees,
binary trees, tree traversals (pre/in/post-order), spanning trees, Kruskal's MST,
and applications of trees.

Plan: planning/video-87-trees.md

Render draft:  manim -ql scripts/undergraduate/video-87-trees.py Video87_Trees
Render final:  manim -qh scripts/undergraduate/video-87-trees.py Video87_Trees

v2 Quality Standards (MANDATORY):
  1. setup_background for dot grid + gradient
  2. LayoutEngine v2 for all positioning
  3. progressive_reveal for multi-item scenes (5-item max)
  4. section_divider between major concepts
  5. formula_box for key theorems
  6. Source Sans 3 (SANS) for all body text/titles
  7. play_intro/play_outro branding
  8. ly.clear() between scenes
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


class Video87_Trees(Scene):
    """Trees in Discrete Mathematics: properties, traversals, spanning trees, and MST."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_visual_proof()
        self.scene4_forests_rooted()
        self.scene5_binary_trees()
        self.scene6_traversals_overview()
        self.scene7_preorder()
        self.scene8_inorder_postorder()
        self.scene9_spanning_trees()
        self.scene10_kruskals()
        self.scene11_applications()
        self.scene12_summary_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook -- From Graphs to Trees (1:00)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "In our last video, we explored graphs. "
            "Today we look at a special kind of graph: one with no cycles. "
            "Remove all the cycles from a connected graph, and you get a tree.",
            duration=18,
        )
        play_intro(self, "Trees", "Discrete Mathematics")

        title = self.ly.title("From Graphs to Trees")

        # Build a connected graph with a cycle (pentagon + chord)
        positions = [
            UP * 2 + LEFT * 2,      # 0: A
            UP * 2 + RIGHT * 2,     # 1: B
            DOWN * 1.5 + RIGHT * 2, # 2: C
            DOWN * 1.5 + LEFT * 2,  # 3: D
            DOWN * 0.5,             # 4: E
        ]
        verts = VGroup(*[Dot(p, color=WHITE, radius=0.12) for p in positions])
        labels = VGroup(
            Text("A", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(verts[0], UP),
            Text("B", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(verts[1], UP),
            Text("C", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(verts[2], DOWN),
            Text("D", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(verts[3], DOWN),
            Text("E", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(verts[4], DOWN),
        )
        # Edges: A-B, B-C, C-E, E-D, D-A (cycle) + A-C (chord)
        edge_pairs = [(0,1), (1,2), (2,4), (4,3), (3,0), (0,2)]
        all_edges = VGroup(*[
            Line(verts[i].get_center(), verts[j].get_center(), color=PRIMARY, stroke_width=3)
            for i, j in edge_pairs
        ])

        self.ly.safe_place(verts, direction=DOWN, anchor=title, buff=1)
        self.play(
            LaggedStartMap(FadeIn, verts, scale=0.4, lag_ratio=0.15),
            LaggedStartMap(FadeIn, labels, scale=0.4, lag_ratio=0.15),
            run_time=NORMAL,
        )
        self.play(Create(all_edges), run_time=NORMAL)
        self.wait(1)

        note1 = Text("Remove edges that break cycles...",
                      font_size=BODY_SIZE, color=ACCENT, font=SANS)
        self.ly.safe_place(note1, direction=DOWN, anchor=verts, buff=0.8)
        self.play(FadeIn(note1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Remove chord edge A-C (index 5), then edge C-E (index 2)
        self.play(all_edges[5].animate.set_color(RED), run_time=FAST)
        self.play(FadeOut(all_edges[5]), run_time=FAST)
        self.play(all_edges[2].animate.set_color(RED), run_time=FAST)
        self.play(FadeOut(all_edges[2]), run_time=FAST)
        self.wait(0.5)

        self.play(FadeOut(note1), run_time=FAST)

        tree_label = Text(
            "A Tree: connected, acyclic graph",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(tree_label, direction=DOWN, anchor=verts, buff=0.8)
        self.play(FadeIn(tree_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Tree Definition and Properties (1:30)
    # ------------------------------------------------------------------
    def scene2_definition(self):
        self.add_subcaption(
            "A tree is a connected acyclic graph. Equivalently, a graph where "
            "every pair of vertices has exactly one simple path between them. "
            "The key property: a tree with n vertices has exactly n minus one edges.",
            duration=18,
        )

        self.ly.section_divider(1, "What is a Tree?")
        title = self.ly.title("Tree Definition")

        t_positions = [
            UP * 1.5 + LEFT * 3,  # A
            UP * 1.5 + LEFT * 1,  # B
            UP * 0.5 + LEFT * 2,  # C
            DOWN * 0.5 + LEFT * 1, # D
            UP * 0.5 + LEFT * 4,  # E
        ]
        tree_v = VGroup(*[Dot(p, color=PRIMARY, radius=0.15) for p in t_positions])
        tree_l = VGroup(
            Text("A", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(tree_v[0], UP),
            Text("B", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(tree_v[1], UP),
            Text("C", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(tree_v[2], LEFT),
            Text("D", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(tree_v[3], DOWN),
            Text("E", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(tree_v[4], LEFT),
        )
        tree_e_pairs = [(0,1), (0,4), (1,2), (2,3)]
        tree_edges = VGroup(*[
            Line(tree_v[i].get_center(), tree_v[j].get_center(), color=SECONDARY, stroke_width=4)
            for i, j in tree_e_pairs
        ])

        self.ly.safe_place(tree_v, direction=DOWN, anchor=title, buff=1)
        self.play(
            LaggedStartMap(FadeIn, tree_v, scale=0.4, lag_ratio=0.15),
            LaggedStartMap(FadeIn, tree_l, scale=0.4, lag_ratio=0.15),
            run_time=NORMAL,
        )
        self.play(Create(tree_edges), run_time=NORMAL)
        self.wait(0.5)

        def_items = [
            Text("Connected acyclic graph (no cycles)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Every pair of vertices: exactly one simple path",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5 vertices, 4 edges: |E| = |V| - 1",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(def_items, start_from=title)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Visual Proof -- Edges = Vertices - 1 (1:30)
    # ------------------------------------------------------------------
    def scene3_visual_proof(self):
        self.add_subcaption(
            "Why does a tree with n vertices have exactly n minus one edges? "
            "Start with a single vertex and zero edges. Each time you add a new vertex, "
            "you connect it with exactly one edge. After adding n minus one vertices, "
            "you have n vertices and n minus one edges.",
            duration=18,
        )

        self.ly.section_divider(2, "Why |E| = |V| - 1")
        title = self.ly.title("Visual Proof: Build a Tree")

        step_verts = VGroup(Dot(ORIGIN, color=PRIMARY, radius=0.15))
        step_labels = VGroup(
            Text("v1", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(step_verts[0], UP)
        )
        step_edges = VGroup()

        self.ly.center_in_content(step_verts[0])
        self.play(
            FadeIn(step_verts[0], scale=0.5),
            FadeIn(step_labels[0], scale=0.5),
            run_time=NORMAL,
        )

        counter = Text("|V| = 1, |E| = 0", font_size=BODY_SIZE, color=ACCENT, font=SANS)
        self.ly.safe_place(counter, direction=DOWN, anchor=step_verts[0], buff=1)
        self.play(FadeIn(counter, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        new_positions = [
            UP * 1.5,                # v2
            UP * 1.5 + RIGHT * 2,   # v3
            UP * 0.5 + RIGHT * 1,    # v4
            DOWN * 1 + RIGHT * 0.5,  # v5
            DOWN * 2,                # v6
        ]
        connect_to = [0, 1, 1, 2, 3]

        for idx, (pos, parent) in enumerate(zip(new_positions, connect_to)):
            new_v = Dot(pos, color=PRIMARY, radius=0.15)
            label_dir = UP if pos[1] > 0 else DOWN
            new_label = Text(f"v{idx+2}", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(new_v, label_dir)
            new_edge = Line(step_verts[parent].get_center(), pos, color=SECONDARY, stroke_width=4)

            self.play(FadeOut(counter), run_time=FAST)
            self.play(
                Create(new_edge),
                FadeIn(new_v, scale=0.5),
                FadeIn(new_label, scale=0.5),
                run_time=NORMAL,
            )

            step_verts.add(new_v)
            step_labels.add(new_label)
            step_edges.add(new_edge)

            anchor_for_counter = new_v if pos[1] < 0 else step_verts[0]
            counter = Text(f"|V| = {idx+2}, |E| = {idx+1}", font_size=BODY_SIZE, color=ACCENT, font=SANS)
            self.ly.safe_place(counter, direction=DOWN, anchor=anchor_for_counter, buff=1)
            self.play(FadeIn(counter, shift=LEFT * 0.15), run_time=NORMAL)
            self.wait(0.5)

        self.play(FadeOut(counter), run_time=FAST)
        formula = MathTex(r"|E|", r" = |V| - 1", color=WHITE)
        fbox = self.ly.formula_box(formula, ACCENT)
        self.ly.center_in_content(fbox)
        self.play(Write(fbox), run_time=NORMAL)
        self.wait(1)

        iff = Text("This is if-and-only-if: connected AND acyclic",
                   font_size=BODY_SIZE, color=DIM, font=SANS)
        self.ly.safe_place(iff, direction=DOWN, anchor=fbox, buff=0.5)
        self.play(FadeIn(iff, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Forests and Rooted Trees (1:30)
    # ------------------------------------------------------------------
    def scene4_forests_rooted(self):
        self.add_subcaption(
            "A forest is a disconnected collection of trees. If you pick any vertex "
            "in a tree as the root, it becomes a rooted tree with parent-child relationships. "
            "Leaves have no children, and the height measures the longest root-to-leaf path.",
            duration=18,
        )

        self.ly.section_divider(3, "Rooted Trees and Forests")
        title = self.ly.title("Rooted Trees and Forests")

        f1_v = VGroup(
            Dot(LEFT * 3 + UP * 1, color=PRIMARY, radius=0.12),
            Dot(LEFT * 4 + UP * 0, color=PRIMARY, radius=0.12),
            Dot(LEFT * 2 + UP * 0, color=PRIMARY, radius=0.12),
            Dot(LEFT * 3 + DOWN * 1, color=PRIMARY, radius=0.12),
        )
        f1_l = VGroup(
            Text("C", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(f1_v[0], UP),
            Text("A", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(f1_v[1], LEFT),
            Text("B", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(f1_v[2], RIGHT),
            Text("E", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(f1_v[3], DOWN),
        )
        f1_e = VGroup(
            Line(f1_v[0].get_center(), f1_v[1].get_center(), color=SECONDARY, stroke_width=3),
            Line(f1_v[0].get_center(), f1_v[2].get_center(), color=SECONDARY, stroke_width=3),
            Line(f1_v[0].get_center(), f1_v[3].get_center(), color=SECONDARY, stroke_width=3),
        )

        f2_v = VGroup(
            Dot(RIGHT * 3 + UP * 0.5, color=PRIMARY, radius=0.12),
            Dot(RIGHT * 2 + DOWN * 0.5, color=PRIMARY, radius=0.12),
            Dot(RIGHT * 4 + DOWN * 0.5, color=PRIMARY, radius=0.12),
        )
        f2_l = VGroup(
            Text("R", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(f2_v[0], UP),
            Text("S", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(f2_v[1], LEFT),
            Text("T", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(f2_v[2], RIGHT),
        )
        f2_e = VGroup(
            Line(f2_v[0].get_center(), f2_v[1].get_center(), color=SECONDARY, stroke_width=3),
            Line(f2_v[0].get_center(), f2_v[2].get_center(), color=SECONDARY, stroke_width=3),
        )

        self.ly.safe_place(f1_v, direction=DOWN, anchor=title, buff=1)
        self.play(
            LaggedStartMap(FadeIn, f1_v, scale=0.3, lag_ratio=0.1),
            LaggedStartMap(FadeIn, f1_l, scale=0.3, lag_ratio=0.1),
            LaggedStartMap(FadeIn, f2_v, scale=0.3, lag_ratio=0.1),
            LaggedStartMap(FadeIn, f2_l, scale=0.3, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.play(Create(f1_e), Create(f2_e), run_time=NORMAL)

        forest_label = Text("Forest: two disconnected trees", font_size=BODY_SIZE, color=WHITE, font=SANS)
        self.ly.safe_place(forest_label, direction=DOWN, anchor=f1_v[0], buff=1.5)
        self.play(FadeIn(forest_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.play(FadeOut(forest_label), run_time=FAST)

        root_marker = MathTex(r"\star", font_size=36, color=ACCENT).next_to(f1_v[0], UP, buff=0.15)
        self.play(FadeIn(root_marker), run_time=FAST)

        terms = [
            Text("Parent of A = C (root)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Children of root: A, B, E", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Leaves: A, B, E (no children)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(terms, start_from=title)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Binary Trees (1:30)
    # ------------------------------------------------------------------
    def scene5_binary_trees(self):
        self.add_subcaption(
            "A binary tree is a rooted tree where each node has at most two children: "
            "a left child and a right child. A full binary tree has nodes with zero or two children. "
            "A complete binary tree fills all levels left-to-right.",
            duration=18,
        )

        self.ly.section_divider(4, "Binary Trees")
        title = self.ly.title("Binary Trees")

        full_v = VGroup(
            Dot(LEFT * 4 + UP * 1.5, color=PRIMARY, radius=0.1),
            Dot(LEFT * 5 + UP * 0, color=PRIMARY, radius=0.1),
            Dot(LEFT * 3 + UP * 0, color=PRIMARY, radius=0.1),
            Dot(LEFT * 5.5 + DOWN * 1.5, color=PRIMARY, radius=0.1),
            Dot(LEFT * 4.5 + DOWN * 1.5, color=PRIMARY, radius=0.1),
            Dot(LEFT * 3.5 + DOWN * 1.5, color=PRIMARY, radius=0.1),
            Dot(LEFT * 2.5 + DOWN * 1.5, color=PRIMARY, radius=0.1),
        )
        full_e = VGroup(
            Line(full_v[0].get_center(), full_v[1].get_center(), color=SECONDARY, stroke_width=2.5),
            Line(full_v[0].get_center(), full_v[2].get_center(), color=SECONDARY, stroke_width=2.5),
            Line(full_v[1].get_center(), full_v[3].get_center(), color=SECONDARY, stroke_width=2.5),
            Line(full_v[1].get_center(), full_v[4].get_center(), color=SECONDARY, stroke_width=2.5),
            Line(full_v[2].get_center(), full_v[5].get_center(), color=SECONDARY, stroke_width=2.5),
            Line(full_v[2].get_center(), full_v[6].get_center(), color=SECONDARY, stroke_width=2.5),
        )
        full_label = Text("Full", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(full_v[0], UP, buff=0.3)

        comp_v = VGroup(
            Dot(UP * 1.5, color=PRIMARY, radius=0.1),
            Dot(LEFT * 1 + UP * 0, color=PRIMARY, radius=0.1),
            Dot(RIGHT * 1 + UP * 0, color=PRIMARY, radius=0.1),
            Dot(LEFT * 1.5 + DOWN * 1.5, color=PRIMARY, radius=0.1),
            Dot(LEFT * 0.5 + DOWN * 1.5, color=PRIMARY, radius=0.1),
            Dot(RIGHT * 0.5 + DOWN * 1.5, color=PRIMARY, radius=0.1),
        )
        comp_e = VGroup(
            Line(comp_v[0].get_center(), comp_v[1].get_center(), color=SECONDARY, stroke_width=2.5),
            Line(comp_v[0].get_center(), comp_v[2].get_center(), color=SECONDARY, stroke_width=2.5),
            Line(comp_v[1].get_center(), comp_v[3].get_center(), color=SECONDARY, stroke_width=2.5),
            Line(comp_v[1].get_center(), comp_v[4].get_center(), color=SECONDARY, stroke_width=2.5),
            Line(comp_v[2].get_center(), comp_v[5].get_center(), color=SECONDARY, stroke_width=2.5),
        )
        comp_label = Text("Complete", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(comp_v[0], UP, buff=0.3)

        perf_v = VGroup(
            Dot(RIGHT * 4 + UP * 1.5, color=PRIMARY, radius=0.1),
            Dot(RIGHT * 3 + UP * 0, color=PRIMARY, radius=0.1),
            Dot(RIGHT * 5 + UP * 0, color=PRIMARY, radius=0.1),
            Dot(RIGHT * 3.5 + DOWN * 1.5, color=PRIMARY, radius=0.1),
            Dot(RIGHT * 4.5 + DOWN * 1.5, color=PRIMARY, radius=0.1),
        )
        perf_e = VGroup(
            Line(perf_v[0].get_center(), perf_v[1].get_center(), color=SECONDARY, stroke_width=2.5),
            Line(perf_v[0].get_center(), perf_v[2].get_center(), color=SECONDARY, stroke_width=2.5),
            Line(perf_v[1].get_center(), perf_v[3].get_center(), color=SECONDARY, stroke_width=2.5),
            Line(perf_v[2].get_center(), perf_v[4].get_center(), color=SECONDARY, stroke_width=2.5),
        )
        perf_label = Text("Perfect", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(perf_v[0], UP, buff=0.3)

        self.ly.safe_place(full_v, direction=DOWN, anchor=title, buff=0.8)
        self.play(
            LaggedStartMap(FadeIn, full_v, scale=0.3, lag_ratio=0.1),
            LaggedStartMap(FadeIn, comp_v, scale=0.3, lag_ratio=0.1),
            LaggedStartMap(FadeIn, perf_v, scale=0.3, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.play(Create(full_e), Create(comp_e), Create(perf_e), run_time=NORMAL)
        self.play(
            FadeIn(full_label, shift=LEFT * 0.1),
            FadeIn(comp_label, shift=LEFT * 0.1),
            FadeIn(perf_label, shift=LEFT * 0.1),
            run_time=NORMAL,
        )
        self.wait(1)

        defs = [
            Text("Each node has at most 2 children (left, right)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Full: every node has 0 or 2 children",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Complete: all levels filled, last level left-to-right",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Perfect: all internal nodes have 2 children, same depth",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(defs, start_from=title)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Tree Traversals -- Overview (1:00)
    # ------------------------------------------------------------------
    def scene6_traversals_overview(self):
        self.add_subcaption(
            "How do we visit every node in a tree systematically? "
            "There are three fundamental traversal orders, defined by when we process "
            "the current node relative to its children: pre-order, in-order, and post-order.",
            duration=18,
        )

        self.ly.section_divider(5, "Tree Traversals")
        title = self.ly.title("Exploring Trees: Traversals")

        ref_positions = [
            UP * 2,
            UP * 0.5 + LEFT * 1.5,
            UP * 0.5 + RIGHT * 1.5,
            DOWN * 1 + LEFT * 2.5,
            DOWN * 1 + LEFT * 0.5,
            DOWN * 1 + RIGHT * 0.5,
            DOWN * 1 + RIGHT * 2.5,
        ]
        ref_names = ["F", "B", "G", "A", "D", "C", "I"]
        ref_v = VGroup(*[Dot(p, color=PRIMARY, radius=0.15) for p in ref_positions])
        ref_l = VGroup(*[
            Text(n, font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(
                ref_v[i], UP if ref_positions[i][1] > 0.5 else DOWN)
            for i, n in enumerate(ref_names)
        ])
        ref_pairs = [(0,1), (0,2), (1,3), (1,4), (2,5), (2,6)]
        ref_edges = VGroup(*[
            Line(ref_v[i].get_center(), ref_v[j].get_center(), color=SECONDARY, stroke_width=3)
            for i, j in ref_pairs
        ])

        self.ly.safe_place(ref_v, direction=DOWN, anchor=title, buff=0.8)
        self.play(
            LaggedStartMap(FadeIn, ref_v, scale=0.3, lag_ratio=0.1),
            LaggedStartMap(FadeIn, ref_l, scale=0.3, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.play(Create(ref_edges), run_time=NORMAL)
        self.wait(0.5)

        orders = [
            Text("Pre-order:  Root, Left, Right", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("In-order:   Left, Root, Right", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Post-order: Left, Right, Root", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(orders, start_from=title)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Pre-order Traversal (1:00)
    # ------------------------------------------------------------------
    def scene7_preorder(self):
        self.add_subcaption(
            "Pre-order traversal visits the root first, then the left subtree, then the right subtree. "
            "For our tree: F, then B, A, D, then G, C, I. Pre-order is useful for copying "
            "a tree structure or evaluating expression trees.",
            duration=18,
        )

        self.ly.section_divider(6, "Pre-Order Traversal")
        title = self.ly.title("Pre-Order: Root, Left, Right")

        ref_positions = [
            UP * 1.5,
            UP * 0 + LEFT * 1.5,
            UP * 0 + RIGHT * 1.5,
            DOWN * 1.5 + LEFT * 2.5,
            DOWN * 1.5 + LEFT * 0.5,
            DOWN * 1.5 + RIGHT * 0.5,
            DOWN * 1.5 + RIGHT * 2.5,
        ]
        ref_names = ["F", "B", "G", "A", "D", "C", "I"]
        ref_v = VGroup(*[Dot(p, color=PRIMARY, radius=0.15) for p in ref_positions])
        ref_l = VGroup(*[
            Text(n, font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(
                ref_v[i], UP if ref_positions[i][1] > 0.5 else DOWN)
            for i, n in enumerate(ref_names)
        ])
        ref_pairs = [(0,1), (0,2), (1,3), (1,4), (2,5), (2,6)]
        ref_edges = VGroup(*[
            Line(ref_v[i].get_center(), ref_v[j].get_center(), color=SECONDARY, stroke_width=3)
            for i, j in ref_pairs
        ])

        self.ly.safe_place(ref_v, direction=DOWN, anchor=title, buff=0.8)
        self.play(
            LaggedStartMap(FadeIn, ref_v, scale=0.3, lag_ratio=0.1),
            LaggedStartMap(FadeIn, ref_l, scale=0.3, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.play(Create(ref_edges), run_time=NORMAL)
        self.wait(0.5)

        preorder_order = [0, 1, 3, 4, 2, 5, 6]
        visit_seq = Text("", font_size=BODY_SIZE, color=ACCENT, font=SANS)
        self.ly.safe_place(visit_seq, direction=DOWN, anchor=ref_v[0], buff=1.5)

        for step, idx in enumerate(preorder_order):
            self.play(ref_v[idx].animate.set_color(ACCENT).scale(1.4), run_time=FAST)
            name = ref_names[idx]
            if step == 0:
                seq_text = f"Visit: {name}"
            else:
                seq_text = f"{visit_seq.text}, {name}"
            new_seq = Text(seq_text, font_size=BODY_SIZE, color=ACCENT, font=SANS)
            new_seq.move_to(visit_seq.get_center())
            self.play(FadeOut(visit_seq), FadeIn(new_seq, shift=LEFT * 0.1), run_time=FAST)
            visit_seq = new_seq
            self.wait(0.3)

        self.play(*[v.animate.set_color(PRIMARY).scale(1/1.4) for v in ref_v], run_time=NORMAL)

        app_text = Text("Useful for: copying trees, expression trees (prefix notation)",
                        font_size=BODY_SIZE, color=DIM, font=SANS)
        self.ly.safe_place(app_text, direction=DOWN, anchor=visit_seq, buff=0.4)
        self.play(FadeIn(app_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: In-order and Post-order (1:30)
    # ------------------------------------------------------------------
    def scene8_inorder_postorder(self):
        self.add_subcaption(
            "In-order traversal visits the left subtree, then the root, then the right subtree. "
            "For a binary search tree, this gives sorted output. Post-order visits children first, "
            "then the root, and is used for computing directory sizes or deleting a tree.",
            duration=18,
        )

        title = self.ly.title("In-Order and Post-Order")

        ref_positions = [
            UP * 1.5,
            UP * 0 + LEFT * 1.5,
            UP * 0 + RIGHT * 1.5,
            DOWN * 1.5 + LEFT * 2.5,
            DOWN * 1.5 + LEFT * 0.5,
            DOWN * 1.5 + RIGHT * 0.5,
            DOWN * 1.5 + RIGHT * 2.5,
        ]
        ref_names = ["F", "B", "G", "A", "D", "C", "I"]
        ref_v = VGroup(*[Dot(p, color=PRIMARY, radius=0.15) for p in ref_positions])
        ref_l = VGroup(*[
            Text(n, font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(
                ref_v[i], UP if ref_positions[i][1] > 0.5 else DOWN)
            for i, n in enumerate(ref_names)
        ])
        ref_pairs = [(0,1), (0,2), (1,3), (1,4), (2,5), (2,6)]
        ref_edges = VGroup(*[
            Line(ref_v[i].get_center(), ref_v[j].get_center(), color=SECONDARY, stroke_width=3)
            for i, j in ref_pairs
        ])

        self.ly.safe_place(ref_v, direction=DOWN, anchor=title, buff=0.6)
        self.play(
            LaggedStartMap(FadeIn, ref_v, scale=0.3, lag_ratio=0.1),
            LaggedStartMap(FadeIn, ref_l, scale=0.3, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.play(Create(ref_edges), run_time=NORMAL)
        self.wait(0.3)

        inorder_order = [3, 1, 4, 0, 5, 2, 6]
        in_label = Text("", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        self.ly.safe_place(in_label, direction=DOWN, anchor=ref_v[0], buff=1.5)

        for step, idx in enumerate(inorder_order):
            self.play(ref_v[idx].animate.set_color(PRIMARY).scale(1.4), run_time=FAST)
            name = ref_names[idx]
            if step == 0:
                seq_text = f"In-order: {name}"
            else:
                seq_text = f"{in_label.text}, {name}"
            new_l = Text(seq_text, font_size=BODY_SIZE, color=PRIMARY, font=SANS)
            new_l.move_to(in_label.get_center())
            self.play(FadeOut(in_label), FadeIn(new_l, shift=LEFT * 0.1), run_time=FAST)
            in_label = new_l
            self.wait(0.2)

        self.play(*[v.animate.set_color(PRIMARY).scale(1/1.4) for v in ref_v], run_time=NORMAL)
        self.play(FadeOut(in_label), run_time=FAST)

        postorder_order = [3, 4, 1, 5, 6, 2, 0]
        post_label = Text("", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(post_label, direction=DOWN, anchor=ref_v[0], buff=1.5)

        for step, idx in enumerate(postorder_order):
            self.play(ref_v[idx].animate.set_color(SECONDARY).scale(1.4), run_time=FAST)
            name = ref_names[idx]
            if step == 0:
                seq_text = f"Post-order: {name}"
            else:
                seq_text = f"{post_label.text}, {name}"
            new_l = Text(seq_text, font_size=BODY_SIZE, color=SECONDARY, font=SANS)
            new_l.move_to(post_label.get_center())
            self.play(FadeOut(post_label), FadeIn(new_l, shift=LEFT * 0.1), run_time=FAST)
            post_label = new_l
            self.wait(0.2)

        self.play(*[v.animate.set_color(PRIMARY).scale(1/1.4) for v in ref_v], run_time=NORMAL)
        self.play(FadeOut(post_label), run_time=FAST)

        insights = [
            Text("In-order on BST gives sorted output",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Post-order: directory sizes, tree deletion",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(insights, start_from=title)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Spanning Trees (1:30)
    # ------------------------------------------------------------------
    def scene9_spanning_trees(self):
        self.add_subcaption(
            "A spanning tree of a connected graph includes every vertex but only enough edges "
            "to keep it connected, forming a tree. A graph can have many spanning trees. "
            "What if edges have weights and we want the cheapest one?",
            duration=18,
        )

        self.ly.section_divider(7, "Spanning Trees")
        title = self.ly.title("Spanning Trees")

        g_positions = [
            UP * 1.5 + LEFT * 2,
            UP * 1.5 + RIGHT * 2,
            DOWN * 1 + RIGHT * 2,
            DOWN * 1 + LEFT * 2,
            DOWN * 0.5,
        ]
        g_names = ["A", "B", "C", "D", "E"]
        g_v = VGroup(*[Dot(p, color=WHITE, radius=0.13) for p in g_positions])
        g_l = VGroup(*[
            Text(n, font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(
                g_v[i], UP if g_positions[i][1] > 0 else DOWN)
            for i, n in enumerate(g_names)
        ])
        g_pairs = [(0,1), (1,2), (2,3), (3,0), (0,4), (2,4)]
        g_edges = VGroup(*[
            Line(g_v[i].get_center(), g_v[j].get_center(), color=PRIMARY, stroke_width=3)
            for i, j in g_pairs
        ])

        self.ly.safe_place(g_v, direction=DOWN, anchor=title, buff=1)
        self.play(
            LaggedStartMap(FadeIn, g_v, scale=0.3, lag_ratio=0.1),
            LaggedStartMap(FadeIn, g_l, scale=0.3, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.play(Create(g_edges), run_time=NORMAL)
        self.wait(0.5)

        st1_indices = [0, 1, 3, 4]
        self.play(
            *[g_edges[idx].animate.set_color(SECONDARY).set_stroke(width=5) for idx in st1_indices],
            *[g_edges[idx].animate.set_color(DIM).set_opacity(0.3) for idx in range(len(g_edges)) if idx not in st1_indices],
            run_time=NORMAL,
        )
        st1_text = Text("Spanning Tree 1", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(st1_text, direction=DOWN, anchor=g_v[0], buff=1.5)
        self.play(FadeIn(st1_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.play(FadeOut(st1_text), run_time=FAST)

        self.play(
            *[g_edges[idx].animate.set_color(PRIMARY).set_stroke(width=3).set_opacity(1) for idx in range(len(g_edges))],
            run_time=FAST,
        )

        st2_indices = [0, 1, 2, 3]
        self.play(
            *[g_edges[idx].animate.set_color(SECONDARY).set_stroke(width=5) for idx in st2_indices],
            *[g_edges[idx].animate.set_color(DIM).set_opacity(0.3) for idx in range(len(g_edges)) if idx not in st2_indices],
            run_time=NORMAL,
        )
        st2_text = Text("Spanning Tree 2 (different edges)", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(st2_text, direction=DOWN, anchor=g_v[0], buff=1.5)
        self.play(FadeIn(st2_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.play(FadeOut(st2_text), run_time=FAST)

        self.play(
            *[g_edges[idx].animate.set_color(PRIMARY).set_stroke(width=3).set_opacity(1) for idx in range(len(g_edges))],
            run_time=FAST,
        )

        bridge = Text(
            "What if edges have weights? Find the cheapest spanning tree.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(bridge, direction=DOWN, anchor=g_v[0], buff=1.5)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Kruskal's Algorithm (2:00)
    # ------------------------------------------------------------------
    def scene10_kruskals(self):
        self.add_subcaption(
            "Kruskal's algorithm finds the minimum spanning tree. Sort all edges by weight, "
            "then add the cheapest edge that doesn't create a cycle. Repeat until all vertices "
            "are connected. Let us see it in action.",
            duration=18,
        )

        self.ly.section_divider(8, "Minimum Spanning Tree")
        title = self.ly.title("Kruskal's Algorithm: MST")

        k_positions = [
            LEFT * 3 + UP * 2,
            RIGHT * 3 + UP * 2,
            RIGHT * 3,
            LEFT * 3,
            DOWN * 1 + LEFT * 0.5,
            DOWN * 1 + RIGHT * 0.5,
        ]
        k_names = ["A", "B", "C", "D", "E", "F"]
        k_v = VGroup(*[Dot(p, color=WHITE, radius=0.12) for p in k_positions])
        k_l = VGroup(*[
            Text(n, font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(
                k_v[i], UP if k_positions[i][1] > 0 else DOWN)
            for i, n in enumerate(k_names)
        ])

        k_edges_data = [
            (0, 1, 4),
            (1, 2, 8),
            (2, 3, 7),
            (3, 0, 2),
            (0, 4, 5),
            (1, 5, 1),
            (4, 5, 3),
            (2, 5, 6),
        ]
        k_edges = VGroup()
        k_weights = VGroup()
        for i, j, w in k_edges_data:
            edge = Line(k_v[i].get_center(), k_v[j].get_center(), color=PRIMARY, stroke_width=3)
            mid = (k_v[i].get_center() + k_v[j].get_center()) / 2
            offset = UP * 0.25 if abs(k_v[i].get_center()[1] - k_v[j].get_center()[1]) > 1 else RIGHT * 0.25
            wt = Text(str(w), font_size=LABEL_SIZE, color=ACCENT, font=MONO).move_to(mid + offset)
            k_edges.add(edge)
            k_weights.add(wt)

        self.ly.safe_place(k_v, direction=DOWN, anchor=title, buff=0.8)
        self.play(
            LaggedStartMap(FadeIn, k_v, scale=0.3, lag_ratio=0.1),
            LaggedStartMap(FadeIn, k_l, scale=0.3, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.play(Create(k_edges), run_time=NORMAL)
        self.play(LaggedStartMap(FadeIn, k_weights, scale=0.3, lag_ratio=0.05), run_time=NORMAL)
        self.wait(1)

        sorted_indices = [5, 3, 6, 0, 4, 7, 2, 1]

        parent = list(range(len(k_v)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[px] = py
            return True

        step_label = Text("", font_size=BODY_SIZE, color=WHITE, font=SANS)
        self.ly.safe_place(step_label, direction=DOWN, anchor=k_v[0], buff=2)

        accepted = []

        for sort_step, eidx in enumerate(sorted_indices):
            i, j, w = k_edges_data[eidx]
            can_add = union(i, j)

            e_name = f"{k_names[i]}-{k_names[j]}"
            step_text = f"Step {sort_step+1}: Add {e_name} (w={w})"
            new_label = Text(step_text, font_size=BODY_SIZE, color=WHITE, font=SANS)
            new_label.move_to(step_label.get_center())
            self.play(FadeOut(step_label), FadeIn(new_label, shift=LEFT * 0.1), run_time=FAST)
            step_label = new_label

            if can_add:
                accepted.append(eidx)
                self.play(k_edges[eidx].animate.set_color(SECONDARY).set_stroke(width=5), run_time=NORMAL)
            else:
                self.play(
                    k_edges[eidx].animate.set_color(RED).set_stroke(width=2),
                    k_weights[eidx].animate.set_color(RED),
                    run_time=NORMAL,
                )
            self.wait(0.3)

            if len(accepted) == len(k_v) - 1:
                self.play(FadeOut(step_label), run_time=FAST)
                total_w = sum(k_edges_data[idx][2] for idx in accepted)
                mst_text = Text(
                    f"MST total weight: {total_w}",
                    font_size=BODY_SIZE, color=SECONDARY, font=SANS,
                )
                self.ly.safe_place(mst_text, direction=DOWN, anchor=k_v[0], buff=2)
                self.play(FadeIn(mst_text, shift=LEFT * 0.15), run_time=NORMAL)
                self.wait(2)
                break

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 11: Applications of Trees (1:30)
    # ------------------------------------------------------------------
    def scene11_applications(self):
        self.add_subcaption(
            "Trees appear everywhere in science and technology. File systems use directory trees. "
            "Decision trees classify data with yes-no questions. Phylogenetic trees show "
            "evolutionary relationships. Huffman coding uses trees for optimal data compression.",
            duration=18,
        )

        title = self.ly.title("Where Trees Appear")

        apps = [
            Text("File Systems: directories and files as a rooted tree",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Decision Trees: yes/no questions lead to classifications",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Phylogenetic Trees: evolutionary relationships",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Network Routing: spanning trees connect all nodes minimally",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Huffman Coding: optimal compression via binary trees",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(apps, start_from=title)
        # +10s hold: narration for this scene needs ~17.3s natural TTS; the slot
        # is capped by the next scene's subcaption start (stale-render audit fix).
        self.wait(12)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 12: Summary and Outro (1:00)
    # ------------------------------------------------------------------
    def scene12_summary_outro(self):
        self.add_subcaption(
            "Trees are connected acyclic graphs with exactly n minus one edges. "
            "We explored rooted trees, binary trees, three traversal orders, spanning trees, "
            "and Kruskal's algorithm for the minimum spanning tree. Next up: Graph Coloring.",
            duration=18,
        )

        title = self.ly.title("Trees: Summary")

        points = [
            Text("Tree: connected, acyclic, |E| = |V| - 1",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Rooted tree: parent, child, leaf, height",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Binary tree: at most 2 children per node",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Traversals: pre-order, in-order, post-order",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Spanning tree: all vertices, minimal edges",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("MST via Kruskal's: cheapest edges, no cycles",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        # +2s hold: summary narration needs ~16.6s natural TTS before outro starts.
        self.wait(4)

        formula = MathTex(r"|E| = |V| - 1", color=WHITE)
        fbox = self.ly.formula_box(formula, ACCENT)
        self.ly.safe_place(fbox, direction=DOWN, buff=0.5)
        self.play(Write(fbox), run_time=NORMAL)
        self.wait(1.5)

        next_text = Text(
            "Next: Graph Coloring - assigning colors under constraints",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(next_text, direction=DOWN, anchor=fbox, buff=0.4)
        self.play(FadeIn(next_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        self.ly.clear()

        self.add_subcaption(
            "Thank you for watching! Subscribe for more visual math explanations.",
            duration=8,
        )
        play_outro(self, "Graph Coloring", "Discrete Mathematics")
