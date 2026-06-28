"""
Video 88: Planarity and Euler's Formula
Discrete Mathematics -- Video 11 of 12

Covers: Planar graphs, planar embeddings, Euler's formula (V - E + F = 2),
consequences (edge bounds), K5 and K3,3 non-planarity, Kuratowski's theorem.

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
    """Planarity and Euler's Formula: when graphs can live in the plane."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_euler_formula()
        self.scene4_applications()
        self.scene5_kuratowski()
        self.scene6_summary()
        self.scene7_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook — Can You Draw Without Crossing? (45s)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Can you draw three houses connected to three utilities without "
            "any pipes crossing? This classic puzzle reveals a deep property "
            "of graphs called planarity.",
            duration=16,
        )
        play_intro(self, "Planarity and Euler's Formula", "Discrete Mathematics")

        title = self.ly.title("Can You Draw Without Crossing?")

        # Draw K3,3 (utility graph) — simple version with crossing visible
        left_verts = VGroup(
            Dot(LEFT * 2 + UP * 1.5, color=PRIMARY, radius=0.13),
            Dot(LEFT * 2, color=PRIMARY, radius=0.13),
            Dot(LEFT * 2 + DOWN * 1.5, color=PRIMARY, radius=0.13),
        )
        right_verts = VGroup(
            Dot(RIGHT * 2 + UP * 1.5, color=SECONDARY, radius=0.13),
            Dot(RIGHT * 2, color=SECONDARY, radius=0.13),
            Dot(RIGHT * 2 + DOWN * 1.5, color=SECONDARY, radius=0.13),
        )

        # Draw all edges — some will cross
        edges = VGroup()
        for lv in left_verts:
            for rv in right_verts:
                edges.add(Line(lv.get_center(), rv.get_center(), color=DIM, stroke_width=2))

        k33 = VGroup(left_verts, right_verts, edges)
        self.ly.center_in_content(k33)
        self.play(
            LaggedStartMap(FadeIn, left_verts, scale=0.5, lag_ratio=0.15),
            LaggedStartMap(FadeIn, right_verts, scale=0.5, lag_ratio=0.15),
            Create(edges),
            run_time=NORMAL,
        )
        self.wait(1)

        # Label the puzzle
        puzzle = Text(
            "The Utility Graph: can we redraw with no crossings?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(puzzle, direction=DOWN, anchor=k33, buff=0.5)
        self.play(FadeIn(puzzle, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        # Real-world motivation
        motivation = Text(
            "Applications: circuit boards, map coloring, network layout",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(motivation, direction=DOWN, anchor=puzzle, buff=0.3)
        self.play(FadeIn(motivation, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Planar Graphs Definition (60s)
    # ------------------------------------------------------------------
    def scene2_definition(self):
        self.add_subcaption(
            "A graph is planar if it can be drawn in the plane with no edge "
            "crossings. Different drawings of the same graph might look "
            "different, but if one can be redrawn without crossings, the "
            "graph itself is planar.",
            duration=18,
        )
        self.ly.section_divider(1, "What Are Planar Graphs?")

        # Definition
        defn = Text(
            "A graph is planar if it can be drawn in the plane with no edge crossings.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.center_in_content(defn)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # K4 is planar — show planar drawing
        k4_title = Text("K4: planar (can be redrawn flat)", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        k4_title.move_to(UP * 1.8)
        self.play(FadeIn(k4_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Planar K4: square + diagonal, with one vertex inside
        k4_a = Dot(LEFT * 1.5 + UP * 1, color=WHITE, radius=0.13)
        k4_b = Dot(RIGHT * 1.5 + UP * 1, color=WHITE, radius=0.13)
        k4_c = Dot(RIGHT * 1.5 + DOWN * 1, color=WHITE, radius=0.13)
        k4_d = Dot(LEFT * 1.5 + DOWN * 1, color=WHITE, radius=0.13)
        k4_verts = VGroup(k4_a, k4_b, k4_c, k4_d)

        k4_edges = VGroup(
            Line(k4_a.get_center(), k4_b.get_center(), color=SECONDARY, stroke_width=3),
            Line(k4_b.get_center(), k4_c.get_center(), color=SECONDARY, stroke_width=3),
            Line(k4_c.get_center(), k4_d.get_center(), color=SECONDARY, stroke_width=3),
            Line(k4_d.get_center(), k4_a.get_center(), color=SECONDARY, stroke_width=3),
            Line(k4_a.get_center(), k4_c.get_center(), color=SECONDARY, stroke_width=3),
            Line(k4_b.get_center(), k4_d.get_center(), color=SECONDARY, stroke_width=3),
        )
        k4_graph = VGroup(k4_verts, k4_edges)
        self.ly.center_in_content(k4_graph)
        self.play(
            Create(k4_edges), LaggedStartMap(FadeIn, k4_verts, scale=0.5, lag_ratio=0.15),
            run_time=NORMAL,
        )
        self.wait(2)
        self.ly.clear()

        # K5 is NOT planar
        k5_title = Text("K5: NOT planar (always has crossings)", font_size=BODY_SIZE, color=RED, font=SANS)
        k5_title.move_to(UP * 1.8)
        self.play(FadeIn(k5_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Pentagon K5
        k5_verts_list = []
        for i in range(5):
            angle = PI / 2 + i * 2 * PI / 5
            k5_verts_list.append(Dot(
                np.array([np.cos(angle) * 1.5, np.sin(angle) * 1.5, 0]),
                color=WHITE, radius=0.13,
            ))
        k5_verts = VGroup(*k5_verts_list)

        k5_edges = VGroup()
        for i in range(5):
            for j in range(i + 1, 5):
                k5_edges.add(Line(
                    k5_verts[i].get_center(), k5_verts[j].get_center(),
                    color=DIM, stroke_width=2,
                ))

        k5_graph = VGroup(k5_verts, k5_edges)
        self.ly.center_in_content(k5_graph)
        self.play(
            Create(k5_edges), LaggedStartMap(FadeIn, k5_verts, scale=0.5, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Euler's Formula (90s)
    # ------------------------------------------------------------------
    def scene3_euler_formula(self):
        self.add_subcaption(
            "For any connected planar graph, the number of vertices minus "
            "edges plus faces always equals 2. This is Euler's formula: "
            "V minus E plus F equals 2. A face is any region enclosed by "
            "edges, including the unbounded outer face.",
            duration=20,
        )
        self.ly.section_divider(2, "Euler's Formula")

        # The formula
        formula = MathTex(r"V - E + F = 2", font_size=HEADING_SIZE, color=ACCENT)
        fbox = self.ly.formula_box(formula, ACCENT)
        self.ly.center_in_content(fbox)
        self.play(Write(fbox), run_time=NORMAL)
        self.wait(1)

        # Variable definitions
        items = [
            Text("V = number of vertices", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("E = number of edges", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("F = number of faces (regions, including outer face)", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=fbox)
        self.wait(2)
        self.ly.clear()

        # Worked example: a simple planar graph
        self.add_subcaption(
            "Let's verify with a simple graph: a square with a diagonal. "
            "We have 4 vertices, 5 edges, and counting the triangular "
            "regions plus the outer region, we get 3 faces.",
            duration=14,
        )
        example_title = Text("Example: square with diagonal", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        self.ly.center_in_content(example_title)
        self.play(FadeIn(example_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Draw the graph
        ea = Dot(LEFT * 1.5 + UP * 0.8, color=WHITE, radius=0.13)
        eb = Dot(RIGHT * 1.5 + UP * 0.8, color=WHITE, radius=0.13)
        ec = Dot(RIGHT * 1.5 + DOWN * 0.8, color=WHITE, radius=0.13)
        ed = Dot(LEFT * 1.5 + DOWN * 0.8, color=WHITE, radius=0.13)
        everts = VGroup(ea, eb, ec, ed)

        eedges = VGroup(
            Line(ea.get_center(), eb.get_center(), color=SECONDARY, stroke_width=3),
            Line(eb.get_center(), ec.get_center(), color=SECONDARY, stroke_width=3),
            Line(ec.get_center(), ed.get_center(), color=SECONDARY, stroke_width=3),
            Line(ed.get_center(), ea.get_center(), color=SECONDARY, stroke_width=3),
            Line(ea.get_center(), ec.get_center(), color=RED, stroke_width=3),
        )
        egraph = VGroup(everts, eedges)
        self.ly.center_in_content(egraph)
        self.play(
            Create(eedges), LaggedStartMap(FadeIn, everts, scale=0.5, lag_ratio=0.15),
            run_time=NORMAL,
        )
        self.wait(1)

        # Count V, E, F
        count = VGroup(
            Text("V = 4", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("E = 5", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("F = 3", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("V - E + F = 4 - 5 + 3 = 2  \u2713", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        )
        self.ly.progressive_reveal(count, start_from=egraph)
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Applications of Euler's Formula (60s)
    # ------------------------------------------------------------------
    def scene4_applications(self):
        self.add_subcaption(
            "Euler's formula lets us prove that planar graphs have limited "
            "edges. For simple planar graphs, E is at most 3V minus 6. "
            "This means K5 with 5 vertices and 10 edges cannot be planar, "
            "since it would need at most 9 edges.",
            duration=20,
        )
        self.ly.section_divider(3, "Consequences")

        # Edge bound for simple planar graphs
        title = self.ly.title("Edge Bound")

        bound = MathTex(r"E \leq 3V - 6", font_size=HEADING_SIZE, color=ACCENT)
        bound_box = self.ly.formula_box(bound, ACCENT)
        self.ly.safe_place(bound_box, direction=DOWN, anchor=title, buff=1)
        self.play(Write(bound_box), run_time=NORMAL)
        self.wait(1)

        note1 = Text(
            "(for simple, connected planar graphs with V >= 3)",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note1, direction=DOWN, anchor=bound_box, buff=0.3)
        self.play(FadeIn(note1), run_time=FAST)
        self.wait(1)
        self.ly.clear()

        # K5 contradiction
        k5_title = self.ly.title("K5 is NOT Planar")
        k5_check = VGroup(
            Text("K5 has V = 5, E = 10", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Bound: E <= 3(5) - 6 = 9", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("But 10 > 9  —  CONTRADICTION!", font_size=BODY_SIZE, color=RED, font=SANS),
        )
        self.ly.progressive_reveal(k5_check, start_from=k5_title)
        self.wait(2)
        self.ly.clear()

        # K3,3 contradiction (bipartite bound)
        k33_title = self.ly.title("K3,3 is NOT Planar")

        self.add_subcaption(
            "For bipartite planar graphs, the edge bound is even tighter: "
            "E is at most 2V minus 4. K3,3 has 6 vertices and 9 edges, "
            "but the bound says at most 8. Contradiction!",
            duration=16,
        )

        bipartite_bound = MathTex(r"E \leq 2V - 4", font_size=HEADING_SIZE, color=ACCENT)
        bip_box = self.ly.formula_box(bipartite_bound, ACCENT)
        self.ly.safe_place(bip_box, direction=DOWN, anchor=k33_title, buff=1)
        self.play(Write(bip_box), run_time=NORMAL)
        self.wait(1)

        note2 = Text(
            "(for bipartite planar graphs with V >= 3)",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note2, direction=DOWN, anchor=bip_box, buff=0.3)
        self.play(FadeIn(note2), run_time=FAST)
        self.wait(0.5)

        k33_check = VGroup(
            Text("K3,3 has V = 6, E = 9", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Bound: E <= 2(6) - 4 = 8", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("But 9 > 8  —  CONTRADICTION!", font_size=BODY_SIZE, color=RED, font=SANS),
        )
        self.ly.progressive_reveal(k33_check, start_from=note2)
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Kuratowski's Theorem (75s)
    # ------------------------------------------------------------------
    def scene5_kuratowski(self):
        self.add_subcaption(
            "Kuratowski's theorem gives a complete characterization: a graph "
            "is planar if and only if it contains no subdivision of K5 or "
            "K3,3. A subdivision is formed by inserting extra vertices along "
            "edges, which doesn't change the essential structure.",
            duration=20,
        )
        self.ly.section_divider(4, "Kuratowski's Theorem")

        title = self.ly.title("Kuratowski's Theorem")

        theorem = Text(
            "A graph is planar iff it contains no subdivision of K5 or K3,3",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        theorem_box = self.ly.formula_box(theorem, ACCENT)
        self.ly.safe_place(theorem_box, direction=DOWN, anchor=title, buff=1)
        self.play(Write(theorem_box), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # Explain subdivision
        self.add_subcaption(
            "A subdivision adds vertices of degree 2 along edges. "
            "Think of it as placing dots on a line. The topology "
            "doesn't change — the graph is still essentially the same.",
            duration=16,
        )

        sub_title = self.ly.title("What is a Subdivision?")

        # Show original edge, then subdivided
        orig_a = Dot(LEFT * 2, color=WHITE, radius=0.13)
        orig_b = Dot(RIGHT * 2, color=WHITE, radius=0.13)
        orig_edge = Line(orig_a.get_center(), orig_b.get_center(), color=PRIMARY, stroke_width=3)
        orig_group = VGroup(orig_a, orig_b, orig_edge)
        self.ly.center_in_content(orig_group)
        self.play(Create(orig_edge), FadeIn(orig_a), FadeIn(orig_b), run_time=FAST)
        self.wait(0.5)

        # Subdivide: add a vertex in the middle
        mid = Dot(ORIGIN, color=ACCENT, radius=0.13)
        sub_edge1 = Line(orig_a.get_center(), ORIGIN, color=PRIMARY, stroke_width=3)
        sub_edge2 = Line(ORIGIN, orig_b.get_center(), color=PRIMARY, stroke_width=3)
        self.play(
            FadeOut(orig_edge),
            FadeIn(mid, scale=0.5),
            Create(sub_edge1), Create(sub_edge2),
            run_time=NORMAL,
        )
        self.wait(1)

        sub_label = Text(
            "Adding a degree-2 vertex preserves the essential structure",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(sub_label, direction=DOWN, anchor=orig_group, buff=0.5)
        self.play(FadeIn(sub_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Summary of the theorem significance
        significance = VGroup(
            Text("K5 and K3,3 are the only obstructions to planarity", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Any non-planar graph contains one of these as a substructure", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("This gives an algorithmic way to test planarity", font_size=BODY_SIZE, color=WHITE, font=SANS),
        )
        self.ly.progressive_reveal(significance)
        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Applications and Summary (45s)
    # ------------------------------------------------------------------
    def scene6_summary(self):
        self.add_subcaption(
            "Planarity has real applications. Circuit board layout requires "
            "planar connections. Map coloring needs planar graphs. "
            "Euler's formula is one of the most beautiful results in "
            "graph theory, connecting vertices, edges, and faces.",
            duration=16,
        )

        title = self.ly.title("Planarity: Summary")

        points = [
            Text("Planar graph: can be drawn with no edge crossings", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Euler's formula: V - E + F = 2", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Simple planar bound: E <= 3V - 6", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("K5 and K3,3 are NOT planar", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Kuratowski: planar iff no K5/K3,3 subdivision", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        self.wait(2)

        # Applications note
        apps = Text(
            "Applications: circuit boards, map coloring, graph drawing algorithms",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(apps, direction=DOWN, anchor=points[-1] if hasattr(self, '_last_visible') else points[4], buff=0.5)
        self.play(FadeIn(apps, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Outro
    # ------------------------------------------------------------------
    def scene7_outro(self):
        self.add_subcaption(
            "Thanks for watching! Planarity and Euler's formula reveal "
            "beautiful structure in graphs. In the next video, we'll explore "
            "graph coloring and the famous four color theorem.",
            duration=14,
        )
        play_outro(self, "Graph Coloring", "Discrete Mathematics")
