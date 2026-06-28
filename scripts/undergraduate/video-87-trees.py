"""
Video 87: Trees
Discrete Mathematics -- Video 10 of 12

Covers: Tree definition, properties, rooted trees, binary trees,
tree traversals, spanning trees, and minimum spanning trees.

Plan: planning/video-87-trees.md

Render draft:  manim -ql scripts/undergraduate/video-87-trees.py Video87_Trees
Render final:  manim -qh scripts/undergraduate/video-87-trees.py Video87_Trees
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
    """Trees: the simplest connected acyclic structures in graph theory."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_properties()
        self.scene4_rooted_trees()
        self.scene5_binary_trees()
        self.scene6_traversals()
        self.scene7_spanning_trees()
        self.scene8_summary()
        self.scene9_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook — Why Trees Matter (45s)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Trees are everywhere: family trees organize genealogy, file systems structure your computer, "
            "decision trees guide choices, and network routing relies on tree structures. "
            "They are the simplest connected graphs without cycles.",
            duration=18,
        )
        play_intro(self, "Trees", "Discrete Mathematics")

        title = self.ly.title("Trees Are Everywhere")

        items = [
            Text("Family trees — organize genealogy", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("File systems — folders and subfolders", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Decision trees — guide algorithmic choices", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Network routing — efficient data paths", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(0.5)

        key = Text(
            "Key insight: trees balance connectivity and efficiency.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=items[-1] if hasattr(self, '_last_visible') else items[3], buff=0.6)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Definition and Properties (90s)
    # ------------------------------------------------------------------
    def scene2_definition(self):
        self.add_subcaption(
            "A tree is a connected graph with no cycles. That simple definition "
            "has powerful consequences. A tree with n vertices always has exactly "
            "n minus 1 edges, and every edge is a bridge.",
            duration=18,
        )
        self.ly.section_divider(1, "What is a Tree?")

        # Draw a sample tree
        v1 = Dot(UP * 1.5, color=WHITE, radius=0.13)
        v2 = Dot(UP * 1.5 + LEFT * 1.5, color=WHITE, radius=0.13)
        v3 = Dot(UP * 1.5 + RIGHT * 1.5, color=WHITE, radius=0.13)
        v4 = Dot(UP * 0 + LEFT * 0.8, color=WHITE, radius=0.13)
        v5 = Dot(UP * 0 + RIGHT * 0.8, color=WHITE, radius=0.13)
        v6 = Dot(DOWN * 1.2, color=WHITE, radius=0.13)
        tree_verts = VGroup(v1, v2, v3, v4, v5, v6)

        tree_edges = VGroup(
            Line(v1.get_center(), v2.get_center(), color=PRIMARY, stroke_width=3),
            Line(v1.get_center(), v3.get_center(), color=PRIMARY, stroke_width=3),
            Line(v2.get_center(), v4.get_center(), color=PRIMARY, stroke_width=3),
            Line(v2.get_center(), v5.get_center(), color=PRIMARY, stroke_width=3),
            Line(v4.get_center(), v6.get_center(), color=PRIMARY, stroke_width=3),
        )
        tree_graph = VGroup(tree_verts, tree_edges)
        self.ly.center_in_content(tree_graph)
        self.play(Create(tree_edges), LaggedStartMap(FadeIn, tree_verts, scale=0.5, lag_ratio=0.15), run_time=NORMAL)
        self.wait(1)

        # Definition
        defn = VGroup(
            Text("A tree is a connected, acyclic graph.", font_size=HEADING_SIZE, color=ACCENT, font=SANS),
        )
        self.ly.safe_place(defn, direction=DOWN, anchor=tree_graph, buff=0.8)
        self.play(FadeIn(defn[0], shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        # Remove tree, show equivalent characterizations
        self.play(FadeOut(tree_graph), run_time=FAST)

        equivs = [
            Text("Connected + acyclic", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Connected + |E| = |V| - 1", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Acyclic + |E| = |V| - 1", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Any two vertices share exactly one path", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Connected + every edge is a bridge", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        equiv_title = Text("Equivalent definitions:", font_size=BODY_SIZE, color=ACCENT, font=SANS)
        self.ly.safe_place(equiv_title, direction=UP, anchor=defn[0])
        self.ly.safe_place(equiv_title, direction=UP)
        # Place equiv_title at center content area
        equiv_title.move_to(UP * 1.5)
        self.play(FadeOut(defn[0]), run_time=FAST)
        self.ly.safe_place(equiv_title, direction=UP)
        self.play(FadeIn(equiv_title, shift=LEFT * 0.15), run_time=NORMAL)

        self.ly.progressive_reveal(equivs, start_from=equiv_title)
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Properties of Trees (60s)
    # ------------------------------------------------------------------
    def scene3_properties(self):
        self.add_subcaption(
            "Trees have elegant properties. With n vertices, there are exactly "
            "n minus 1 edges. Removing any single edge disconnects the tree, "
            "and adding any edge creates a cycle. Every pair of vertices is "
            "connected by a unique path.",
            duration=18,
        )

        title = self.ly.title("Properties of Trees")

        # Formula box
        formula = MathTex(r"|E| = |V| - 1", font_size=HEADING_SIZE, color=ACCENT)
        formula_box = self.ly.formula_box(formula, ACCENT)
        self.ly.safe_place(formula_box, direction=DOWN, anchor=title, buff=1)
        self.play(Write(formula_box), run_time=NORMAL)
        self.wait(1)

        props = [
            Text("Every edge is a bridge (removal disconnects)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Adding any edge creates a cycle", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Unique path between every pair of vertices", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Tree with n vertices has exactly n-1 edges", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(props, start_from=formula_box)
        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Rooted Trees and Terminology (75s)
    # ------------------------------------------------------------------
    def scene4_rooted_trees(self):
        self.add_subcaption(
            "When we pick one vertex as the root, a tree gains direction and hierarchy. "
            "The root sits at the top. Vertices directly below are children, and the "
            "one above is the parent. Vertices with no children are leaves.",
            duration=18,
        )
        self.ly.section_divider(2, "Rooted Trees")

        # Draw a rooted tree
        root = Dot(UP * 2, color=ACCENT, radius=0.15)
        c1 = Dot(UP * 0.5 + LEFT * 1.5, color=WHITE, radius=0.13)
        c2 = Dot(UP * 0.5 + RIGHT * 1.5, color=WHITE, radius=0.13)
        gc1 = Dot(DOWN * 0.8 + LEFT * 2.2, color=WHITE, radius=0.13)
        gc2 = Dot(DOWN * 0.8 + LEFT * 0.8, color=WHITE, radius=0.13)
        gc3 = Dot(DOWN * 0.8 + RIGHT * 0.8, color=WHITE, radius=0.13)
        leaf = Dot(DOWN * 0.8 + RIGHT * 2.2, color=SECONDARY, radius=0.13)

        rverts = VGroup(root, c1, c2, gc1, gc2, gc3, leaf)
        redges = VGroup(
            Line(root.get_center(), c1.get_center(), color=PRIMARY, stroke_width=3),
            Line(root.get_center(), c2.get_center(), color=PRIMARY, stroke_width=3),
            Line(c1.get_center(), gc1.get_center(), color=PRIMARY, stroke_width=3),
            Line(c1.get_center(), gc2.get_center(), color=PRIMARY, stroke_width=3),
            Line(c2.get_center(), gc3.get_center(), color=PRIMARY, stroke_width=3),
            Line(c2.get_center(), leaf.get_center(), color=PRIMARY, stroke_width=3),
        )
        rtree = VGroup(rverts, redges)
        self.ly.center_in_content(rtree)
        self.play(Create(redges), LaggedStartMap(FadeIn, rverts, scale=0.5, lag_ratio=0.15), run_time=NORMAL)
        self.wait(1)

        # Label root
        root_label = Text("Root", font_size=LABEL_SIZE, color=ACCENT, font=SANS).next_to(root, UP, buff=0.2)
        self.play(FadeIn(root_label), run_time=FAST)
        self.wait(0.5)

        # Label internal vs leaves
        leaf_label = Text("Leaves", font_size=LABEL_SIZE, color=SECONDARY, font=SANS).next_to(leaf, RIGHT, buff=0.2)
        self.play(FadeIn(leaf_label), run_time=FAST)
        self.wait(0.5)

        # Terminology list
        terms = [
            Text("Root: top of the tree", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Parent/Child: one level above/below", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Leaves: vertices with no children", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Height: longest root-to-leaf path", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]

        # Remove tree, show terms
        self.play(FadeOut(rtree), FadeOut(root_label), FadeOut(leaf_label), run_time=FAST)
        self.ly.progressive_reveal(terms)
        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Binary Trees (60s)
    # ------------------------------------------------------------------
    def scene5_binary_trees(self):
        self.add_subcaption(
            "A binary tree is a rooted tree where each node has at most two children: "
            "a left child and a right child. Full binary trees have exactly two children "
            "for every internal node, and complete binary trees fill all levels left to right.",
            duration=18,
        )
        self.ly.section_divider(3, "Binary Trees")

        # Draw a binary tree
        b_root = Dot(UP * 2, color=WHITE, radius=0.13)
        b_l = Dot(UP * 0.7 + LEFT * 1.2, color=WHITE, radius=0.13)
        b_r = Dot(UP * 0.7 + RIGHT * 1.2, color=WHITE, radius=0.13)
        b_ll = Dot(DOWN * 0.5 + LEFT * 2, color=WHITE, radius=0.13)
        b_lr = Dot(DOWN * 0.5 + LEFT * 0.4, color=WHITE, radius=0.13)
        b_rl = Dot(DOWN * 0.5 + RIGHT * 0.4, color=WHITE, radius=0.13)
        b_rr = Dot(DOWN * 0.5 + RIGHT * 2, color=SECONDARY, radius=0.13)

        bverts = VGroup(b_root, b_l, b_r, b_ll, b_lr, b_rl, b_rr)
        bedges = VGroup(
            Line(b_root.get_center(), b_l.get_center(), color=PRIMARY, stroke_width=3),
            Line(b_root.get_center(), b_r.get_center(), color=PRIMARY, stroke_width=3),
            Line(b_l.get_center(), b_ll.get_center(), color=PRIMARY, stroke_width=3),
            Line(b_l.get_center(), b_lr.get_center(), color=PRIMARY, stroke_width=3),
            Line(b_r.get_center(), b_rl.get_center(), color=PRIMARY, stroke_width=3),
            Line(b_r.get_center(), b_rr.get_center(), color=PRIMARY, stroke_width=3),
        )
        btree = VGroup(bverts, bedges)
        self.ly.center_in_content(btree)
        self.play(Create(bedges), LaggedStartMap(FadeIn, bverts, scale=0.5, lag_ratio=0.1), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(btree), run_time=FAST)

        # Key formula
        formula = MathTex(r"\text{Max nodes at level } k = 2^k", font_size=HEADING_SIZE, color=ACCENT)
        fbox = self.ly.formula_box(formula, ACCENT)
        self.ly.center_in_content(fbox)
        self.play(Write(fbox), run_time=NORMAL)
        self.wait(1)

        items = [
            Text("Binary tree: each node has at most 2 children", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Full binary tree: every internal node has 2 children", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Complete binary tree: all levels filled left to right", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=fbox)
        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Tree Traversals (90s)
    # ------------------------------------------------------------------
    def scene6_traversals(self):
        self.add_subcaption(
            "How do we visit every node in a binary tree systematically? "
            "Three standard traversals: pre-order visits root first, "
            "in-order visits left subtree then root then right subtree, "
            "and post-order visits children before the root.",
            duration=18,
        )
        self.ly.section_divider(4, "Tree Traversals")

        # Build a small binary tree with values
        t_root = Dot(UP * 2, color=ACCENT, radius=0.13)
        t_l = Dot(UP * 0.7 + LEFT * 1.2, color=WHITE, radius=0.13)
        t_r = Dot(UP * 0.7 + RIGHT * 1.2, color=WHITE, radius=0.13)
        t_ll = Dot(DOWN * 0.5 + LEFT * 2, color=WHITE, radius=0.13)
        t_lr = Dot(DOWN * 0.5 + LEFT * 0.4, color=WHITE, radius=0.13)

        labels = VGroup(
            Text("A", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(t_root, UP, buff=0.15),
            Text("B", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(t_l, LEFT, buff=0.15),
            Text("C", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(t_r, RIGHT, buff=0.15),
            Text("D", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(t_ll, LEFT, buff=0.15),
            Text("E", font_size=LABEL_SIZE, color=WHITE, font=SANS).next_to(t_lr, RIGHT, buff=0.15),
        )

        tverts = VGroup(t_root, t_l, t_r, t_ll, t_lr)
        tedges = VGroup(
            Line(t_root.get_center(), t_l.get_center(), color=PRIMARY, stroke_width=3),
            Line(t_root.get_center(), t_r.get_center(), color=PRIMARY, stroke_width=3),
            Line(t_l.get_center(), t_ll.get_center(), color=PRIMARY, stroke_width=3),
            Line(t_l.get_center(), t_lr.get_center(), color=PRIMARY, stroke_width=3),
        )

        ttree = VGroup(tverts, tedges, labels)
        self.ly.center_in_content(ttree)
        self.play(Create(tedges), LaggedStartMap(FadeIn, tverts, scale=0.5, lag_ratio=0.1), LaggedStartMap(FadeIn, labels, scale=0.5, lag_ratio=0.1), run_time=NORMAL)
        self.wait(1)

        # Pre-order
        pre_title = Text("Pre-order: Root → Left → Right", font_size=BODY_SIZE, color=ACCENT, font=SANS)
        self.ly.safe_place(pre_title, direction=DOWN, anchor=ttree, buff=0.6)
        self.play(FadeIn(pre_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        pre_order = Text("Visit order: A, B, D, E, C", font_size=BODY_SIZE, color=WHITE, font=SANS)
        self.ly.safe_place(pre_order, direction=DOWN, anchor=pre_title, buff=0.3)
        self.play(FadeIn(pre_order, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        # Transition to in-order
        self.play(FadeOut(pre_title), FadeOut(pre_order), run_time=FAST)

        in_title = Text("In-order: Left → Root → Right", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(in_title, direction=DOWN, anchor=ttree, buff=0.6)
        self.play(FadeIn(in_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        in_order = Text("Visit order: D, B, E, A, C", font_size=BODY_SIZE, color=WHITE, font=SANS)
        self.ly.safe_place(in_order, direction=DOWN, anchor=in_title, buff=0.3)
        self.play(FadeIn(in_order, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        # Transition to post-order
        self.play(FadeOut(in_title), FadeOut(in_order), run_time=FAST)

        post_title = Text("Post-order: Left → Right → Root", font_size=BODY_SIZE, color=RED, font=SANS)
        self.ly.safe_place(post_title, direction=DOWN, anchor=ttree, buff=0.6)
        self.play(FadeIn(post_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        post_order = Text("Visit order: D, E, B, C, A", font_size=BODY_SIZE, color=WHITE, font=SANS)
        self.ly.safe_place(post_order, direction=DOWN, anchor=post_title, buff=0.3)
        self.play(FadeIn(post_order, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Spanning Trees (75s)
    # ------------------------------------------------------------------
    def scene7_spanning_trees(self):
        self.add_subcaption(
            "A spanning tree of a connected graph is a subgraph that includes all vertices "
            "and forms a tree. Every connected graph has at least one spanning tree. "
            "When edges have weights, we seek a minimum spanning tree with the smallest total weight.",
            duration=18,
        )
        self.ly.section_divider(5, "Spanning Trees")

        # Draw a connected graph
        g1 = Dot(UP * 1.5 + LEFT * 1.5, color=WHITE, radius=0.13)
        g2 = Dot(UP * 1.5 + RIGHT * 1.5, color=WHITE, radius=0.13)
        g3 = Dot(DOWN * 0.5 + LEFT * 2, color=WHITE, radius=0.13)
        g4 = Dot(DOWN * 0.5, color=WHITE, radius=0.13)
        g5 = Dot(DOWN * 0.5 + RIGHT * 2, color=WHITE, radius=0.13)

        gverts = VGroup(g1, g2, g3, g4, g5)
        # Complete graph edges (some to remove later)
        g_all_edges = VGroup(
            Line(g1.get_center(), g2.get_center(), color=DIM, stroke_width=2),
            Line(g1.get_center(), g3.get_center(), color=DIM, stroke_width=2),
            Line(g1.get_center(), g4.get_center(), color=DIM, stroke_width=2),
            Line(g2.get_center(), g4.get_center(), color=DIM, stroke_width=2),
            Line(g2.get_center(), g5.get_center(), color=DIM, stroke_width=2),
            Line(g3.get_center(), g4.get_center(), color=DIM, stroke_width=2),
            Line(g4.get_center(), g5.get_center(), color=DIM, stroke_width=2),
            Line(g3.get_center(), g5.get_center(), color=DIM, stroke_width=2),
        )

        graph_group = VGroup(gverts, g_all_edges)
        self.ly.center_in_content(graph_group)
        self.play(LaggedStartMap(FadeIn, gverts, scale=0.5, lag_ratio=0.1), Create(g_all_edges), run_time=NORMAL)
        self.wait(1)

        # Show spanning tree edges highlighted
        st_edges = VGroup(
            Line(g1.get_center(), g3.get_center(), color=SECONDARY, stroke_width=4),
            Line(g1.get_center(), g2.get_center(), color=SECONDARY, stroke_width=4),
            Line(g3.get_center(), g4.get_center(), color=SECONDARY, stroke_width=4),
            Line(g4.get_center(), g5.get_center(), color=SECONDARY, stroke_width=4),
        )

        self.play(
            *[Transform(g_all_edges[i], st_edges[i]) for i in range(len(g_all_edges))],
            run_time=SLOW,
        )
        self.wait(1)

        # Definition
        defn = Text(
            "Spanning tree: includes ALL vertices, forms a TREE",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(defn, direction=DOWN, anchor=graph_group, buff=0.6)
        self.play(FadeIn(defn, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        # MST note
        self.play(FadeOut(graph_group), FadeOut(defn), run_time=FAST)

        mst_items = [
            Text("Minimum Spanning Tree (MST):", font_size=HEADING_SIZE, color=ACCENT, font=SANS),
            Text("Edges have weights (costs)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Find spanning tree with minimum total weight", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Kruskal: add cheapest edges, skip cycles", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Prim: grow tree from a vertex, add cheapest", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(mst_items)
        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Summary (45s)
    # ------------------------------------------------------------------
    def scene8_summary(self):
        self.add_subcaption(
            "Let's recap: trees are connected acyclic graphs with powerful properties. "
            "A tree with n vertices has exactly n minus 1 edges, every edge is a bridge, "
            "and there's a unique path between any two vertices.",
            duration=14,
        )

        title = self.ly.title("Trees: Summary")

        points = [
            Text("Tree = connected + acyclic graph", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("With n vertices: exactly n-1 edges", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Every edge is a bridge", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Unique path between any two vertices", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Binary trees: at most 2 children per node", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Spanning trees: minimum weight subgraphs", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        self.wait(2)

        # Bridge to next video
        next_note = Text(
            "Next: Planarity and Euler's Formula",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(next_note, direction=DOWN, anchor=points[-1] if hasattr(self, '_last_visible') else points[5], buff=0.6)
        self.play(FadeIn(next_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Outro
    # ------------------------------------------------------------------
    def scene9_outro(self):
        self.add_subcaption(
            "Thanks for watching! Trees are a fundamental structure in both mathematics "
            "and computer science. If you found this helpful, please like and subscribe.",
            duration=10,
        )
        play_outro(self, "Planarity and Euler's Formula", "Discrete Mathematics")
