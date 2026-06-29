"""
Video 89: Graph Coloring
Discrete Mathematics -- Video 12 of 12 (Final Video)

Covers: Proper vertex coloring, chromatic number, greedy coloring algorithm,
Four Color Theorem, applications (scheduling, register allocation, map coloring),
bipartite graphs and 2-colorability, chromatic number bounds.

Plan: planning/video-89-graph-coloring.md

Render draft:  manim -ql scripts/undergraduate/video-89-graph-coloring.py Video89_GraphColoring
Render final:  manim -qh scripts/undergraduate/video-89-graph-coloring.py Video89_GraphColoring
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


# Color palette for graph coloring demonstration
COLOR_1 = RED           # "red"
COLOR_2 = PRIMARY       # "blue"
COLOR_3 = SECONDARY     # "green"
COLOR_4 = ACCENT         # "yellow"


class Video89_GraphColoring(Scene):
    """Graph Coloring: assigning colors to vertices so neighbors never match."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_applications()
        self.scene3_definition()
        self.scene4_bipartite()
        self.scene5_greedy()
        self.scene6_four_color()
        self.scene7_bounds()
        self.scene8_summary()
        self.scene9_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook -- Can You Color a Map? (50s)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Can you color this map with only four colors so that no two "
            "adjacent regions share the same color? This simple-sounding "
            "puzzle took over a century to solve, and the answer changed "
            "mathematics forever.",
            duration=18,
        )
        play_intro(self, "Graph Coloring", "Discrete Mathematics")

        title = self.ly.title("Can You Color This Map?")

        # Build a simple 5-region "map" using polygons
        regions = VGroup(
            Polygon(
                [-2.5, 1.5, 0], [-0.5, 1.5, 0], [-0.5, 0.3, 0], [-2.5, 0.3, 0],
                color=DIM, stroke_width=3, fill_opacity=0.15,
            ),
            Polygon(
                [-0.5, 1.5, 0], [2.5, 1.5, 0], [2.5, 0.3, 0], [-0.5, 0.3, 0],
                color=DIM, stroke_width=3, fill_opacity=0.15,
            ),
            Polygon(
                [-2.5, 0.3, 0], [2.5, 0.3, 0], [1.5, -0.8, 0], [-1.5, -0.8, 0],
                color=DIM, stroke_width=3, fill_opacity=0.15,
            ),
            Polygon(
                [-1.5, -0.8, 0], [0.2, -0.8, 0], [0.2, -2.0, 0], [-1.5, -2.0, 0],
                color=DIM, stroke_width=3, fill_opacity=0.15,
            ),
            Polygon(
                [0.2, -0.8, 0], [1.5, -0.8, 0], [1.5, -2.0, 0], [0.2, -2.0, 0],
                color=DIM, stroke_width=3, fill_opacity=0.15,
            ),
        )
        self.ly.center_in_content(regions)
        self.play(LaggedStartMap(FadeIn, regions, lag_ratio=0.15), run_time=NORMAL)
        self.wait(1)

        # Label the regions
        labels = VGroup(
            Text("A", font_size=LABEL_SIZE, color=WHITE, font=SANS).move_to([-1.5, 0.9, 0]),
            Text("B", font_size=LABEL_SIZE, color=WHITE, font=SANS).move_to([1.0, 0.9, 0]),
            Text("C", font_size=LABEL_SIZE, color=WHITE, font=SANS).move_to([0, -0.25, 0]),
            Text("D", font_size=LABEL_SIZE, color=WHITE, font=SANS).move_to([-0.65, -1.4, 0]),
            Text("E", font_size=LABEL_SIZE, color=WHITE, font=SANS).move_to([0.85, -1.4, 0]),
        )
        self.play(LaggedStartMap(FadeIn, labels, lag_ratio=0.1), run_time=FAST)
        self.wait(0.5)

        # Question
        question = Text(
            "Color with 4 colors: no adjacent regions share a color",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(question, direction=DOWN, anchor=regions, buff=0.4)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        # Color it properly as answer
        colors_list = [COLOR_1, COLOR_2, COLOR_3, COLOR_1, COLOR_2]
        self.play(
            *[r.animate.set_fill(c, opacity=0.7) for r, c in zip(regions, colors_list)],
            run_time=NORMAL,
        )
        self.wait(1)

        teaser = Text(
            "What is the MINIMUM number of colors needed for ANY map?",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(teaser, direction=DOWN, anchor=question, buff=0.3)
        self.play(FadeIn(teaser, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Applications -- Why Do We Care? (70s)
    # ------------------------------------------------------------------
    def scene2_applications(self):
        self.add_subcaption(
            "Graph coloring appears everywhere. Exam scheduling: if two "
            "courses share students, they cannot be at the same time. Register "
            "allocation: if two variables are used simultaneously, they need "
            "different CPU registers. Map coloring: adjacent regions need "
            "different colors.",
            duration=22,
        )
        self.ly.section_divider(1, "Why Does Coloring Matter?")

        # Exam scheduling
        sched_title = self.ly.title("Exam Scheduling")
        sched_desc = Text(
            "Courses = vertices,  Conflicts = edges,  Time slots = colors",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(sched_desc, direction=DOWN, anchor=sched_title, buff=1)

        # Small scheduling graph
        v1 = Dot([-1.5, -0.5, 0], color=COLOR_1, radius=0.15)
        v2 = Dot([0, -0.5, 0], color=COLOR_2, radius=0.15)
        v3 = Dot([1.5, -0.5, 0], color=COLOR_1, radius=0.15)
        v4 = Dot([-0.75, -1.5, 0], color=COLOR_3, radius=0.15)
        v5 = Dot([0.75, -1.5, 0], color=COLOR_3, radius=0.15)
        sched_verts = VGroup(v1, v2, v3, v4, v5)
        sched_edges = VGroup(
            Line(v1.get_center(), v2.get_center(), color=DIM, stroke_width=2),
            Line(v2.get_center(), v3.get_center(), color=DIM, stroke_width=2),
            Line(v1.get_center(), v4.get_center(), color=DIM, stroke_width=2),
            Line(v2.get_center(), v4.get_center(), color=DIM, stroke_width=2),
            Line(v2.get_center(), v5.get_center(), color=DIM, stroke_width=2),
            Line(v3.get_center(), v5.get_center(), color=DIM, stroke_width=2),
        )
        sched_graph = VGroup(sched_edges, sched_verts)
        self.ly.center_in_content(sched_graph)
        self.play(
            FadeIn(sched_title),
            FadeIn(sched_desc, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.play(
            Create(sched_edges),
            LaggedStartMap(FadeIn, sched_verts, scale=0.5, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.wait(2)
        self.ly.clear()

        # Register allocation
        reg_title = self.ly.title("Register Allocation")
        reg_desc = Text(
            "Variables = vertices,  Simultaneous use = edges,  Registers = colors",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(reg_desc, direction=DOWN, anchor=reg_title, buff=1)
        self.play(
            FadeIn(reg_title),
            FadeIn(reg_desc, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(2)
        self.ly.clear()

        # Map coloring application
        map_title = self.ly.title("Map Coloring")
        map_desc = Text(
            "Regions = vertices,  Shared borders = edges,  Paint colors = colors",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(map_desc, direction=DOWN, anchor=map_title, buff=1)
        self.play(
            FadeIn(map_title),
            FadeIn(map_desc, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(2)

        # Unifying message
        unify = Text(
            "All these problems share the same mathematical structure!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.center_in_content(unify)
        self.play(Write(unify), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Proper Vertex Coloring Definition (75s)
    # ------------------------------------------------------------------
    def scene3_definition(self):
        self.add_subcaption(
            "A proper vertex coloring assigns a color to each vertex of a "
            "graph so that no two adjacent vertices share the same color. "
            "The chromatic number, written chi of G, is the minimum number "
            "of colors needed for a proper coloring of graph G.",
            duration=20,
        )
        self.ly.section_divider(2, "Proper Vertex Coloring")

        # Definition
        defn = Text(
            "A proper coloring: no two adjacent vertices share the same color.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.center_in_content(defn)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Chromatic number formula
        chi_title = self.ly.title("Chromatic Number")
        chi_formula = MathTex(
            r"\chi(G)", "=", r"\text{minimum colors}",
            font_size=HEADING_SIZE,
        )
        chi_formula.set_color_by_tex(r"\chi(G)", ACCENT)
        chi_formula.set_color_by_tex(r"\text{minimum colors}", WHITE)
        chi_box = self.ly.formula_box(chi_formula, ACCENT)
        self.ly.safe_place(chi_box, direction=DOWN, anchor=chi_title, buff=1)
        self.play(Write(chi_box), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Examples: K3 and C4
        self.add_subcaption(
            "Examples: the complete graph K3 needs 3 colors since every "
            "vertex is adjacent to every other. An even cycle needs only 2 "
            "colors, alternating around the ring.",
            duration=14,
        )

        ex_title = self.ly.title("Examples")

        # K3: triangle needs 3 colors
        k3_label = MathTex(r"\chi(K_3) = 3", font_size=BODY_SIZE, color=PRIMARY)
        k3_label.move_to(LEFT * 3.5)
        k3_a = Dot(LEFT * 3.5 + UP * 0.5, color=COLOR_1, radius=0.12)
        k3_b = Dot(LEFT * 3.5 + RIGHT * 0.8 + DOWN * 0.5, color=COLOR_2, radius=0.12)
        k3_c = Dot(LEFT * 3.5 + LEFT * 0.8 + DOWN * 0.5, color=COLOR_3, radius=0.12)
        k3_edges = VGroup(
            Line(k3_a.get_center(), k3_b.get_center(), color=DIM, stroke_width=2),
            Line(k3_b.get_center(), k3_c.get_center(), color=DIM, stroke_width=2),
            Line(k3_c.get_center(), k3_a.get_center(), color=DIM, stroke_width=2),
        )
        k3_graph = VGroup(k3_label, k3_edges, VGroup(k3_a, k3_b, k3_c))
        k3_graph.move_to(LEFT * 3.5 + DOWN * 1.2)

        # C4: even cycle needs 2 colors
        c4_label = MathTex(r"\chi(C_4) = 2", font_size=BODY_SIZE, color=PRIMARY)
        c4_label.move_to(RIGHT * 3.5)
        c4_positions = [
            RIGHT * 3.5 + UP * 0.8,
            RIGHT * 3.5 + RIGHT * 0.8 + DOWN * 0.3,
            RIGHT * 3.5 + DOWN * 0.8,
            RIGHT * 3.5 + LEFT * 0.8 + DOWN * 0.3,
        ]
        c4_colors_list = [COLOR_1, COLOR_2, COLOR_1, COLOR_2]
        c4_dots = [Dot(p, color=c, radius=0.12) for p, c in zip(c4_positions, c4_colors_list)]
        c4_edge_list = VGroup(
            Line(c4_dots[0].get_center(), c4_dots[1].get_center(), color=DIM, stroke_width=2),
            Line(c4_dots[1].get_center(), c4_dots[2].get_center(), color=DIM, stroke_width=2),
            Line(c4_dots[2].get_center(), c4_dots[3].get_center(), color=DIM, stroke_width=2),
            Line(c4_dots[3].get_center(), c4_dots[0].get_center(), color=DIM, stroke_width=2),
        )
        c4_graph = VGroup(c4_label, c4_edge_list, VGroup(*c4_dots))
        c4_graph.move_to(RIGHT * 3.5 + DOWN * 1.2)

        self.play(FadeIn(ex_title), run_time=FAST)
        self.play(
            FadeIn(k3_graph, shift=LEFT * 0.15),
            FadeIn(c4_graph, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(2)
        self.ly.clear()

        # Improper coloring example
        self.add_subcaption(
            "Here is an improper coloring. These two adjacent vertices "
            "both have the same color, which violates the rule.",
            duration=12,
        )
        imp_title = Text(
            "Improper Coloring", font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.center_in_content(imp_title)
        self.play(FadeIn(imp_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        imp_a = Dot(LEFT * 1.5, color=COLOR_1, radius=0.18)
        imp_b = Dot(RIGHT * 1.5, color=COLOR_1, radius=0.18)
        imp_edge = Line(imp_a.get_center(), imp_b.get_center(), color=DIM, stroke_width=3)
        imp_x = Text("CONFLICT!", font_size=BODY_SIZE, color=RED, font=SANS)
        imp_x.move_to(UP * 1.0)
        self.ly.center_in_content(VGroup(imp_edge, VGroup(imp_a, imp_b)))
        self.play(
            Create(imp_edge), FadeIn(imp_a), FadeIn(imp_b),
            run_time=FAST,
        )
        self.play(FadeIn(imp_x), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Bipartite Graphs and 2-Colorability (60s)
    # ------------------------------------------------------------------
    def scene4_bipartite(self):
        self.add_subcaption(
            "A graph is bipartite if and only if its chromatic number is 2. "
            "If you can split the vertices into two groups with all edges "
            "crossing between groups, you need exactly 2 colors.",
            duration=16,
        )
        self.ly.section_divider(3, "Bipartite and 2-Colorable")

        # Theorem
        title = self.ly.title("Bipartite Equivalence")
        theorem = Text(
            "A graph is bipartite if and only if its chromatic number is 2",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        thm_box = self.ly.formula_box(theorem, ACCENT)
        self.ly.safe_place(thm_box, direction=DOWN, anchor=title, buff=1)
        self.play(Write(thm_box), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Show bipartite graph with 2 colors
        bp_title = Text(
            "Bipartite graph: 2 colors suffice",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        bp_title.move_to(UP * 2.0)

        bp_left = VGroup(
            Dot(LEFT * 2 + UP * 0.5, color=COLOR_2, radius=0.15),
            Dot(LEFT * 2, color=COLOR_2, radius=0.15),
            Dot(LEFT * 2 + DOWN * 0.5, color=COLOR_2, radius=0.15),
        )
        bp_right = VGroup(
            Dot(RIGHT * 2 + UP * 1.0, color=COLOR_3, radius=0.15),
            Dot(RIGHT * 2, color=COLOR_3, radius=0.15),
            Dot(RIGHT * 2 + DOWN * 1.0, color=COLOR_3, radius=0.15),
        )
        bp_edges = VGroup()
        for lv in bp_left:
            for rv in bp_right:
                bp_edges.add(Line(lv.get_center(), rv.get_center(), color=DIM, stroke_width=2))

        bp_graph = VGroup(bp_edges, bp_left, bp_right)
        self.ly.center_in_content(bp_graph)
        self.play(
            FadeIn(bp_title, shift=LEFT * 0.15),
            Create(bp_edges),
            LaggedStartMap(FadeIn, bp_left, scale=0.5, lag_ratio=0.1),
            LaggedStartMap(FadeIn, bp_right, scale=0.5, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.wait(2)
        self.ly.clear()

        # Odd cycle needs 3 colors
        odd_title = Text(
            "Odd cycle (C5): needs 3 colors",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        odd_title.move_to(UP * 2.0)

        odd_dots = []
        odd_col_list = [COLOR_1, COLOR_2, COLOR_1, COLOR_2, COLOR_3]
        for i in range(5):
            angle = PI / 2 + i * 2 * PI / 5
            pos = np.array([np.cos(angle) * 1.3, np.sin(angle) * 1.3, 0])
            odd_dots.append(Dot(pos, color=odd_col_list[i], radius=0.15))
        odd_verts = VGroup(*odd_dots)
        odd_edges = VGroup()
        for i in range(5):
            j = (i + 1) % 5
            odd_edges.add(Line(
                odd_dots[i].get_center(), odd_dots[j].get_center(),
                color=DIM, stroke_width=2,
            ))
        odd_graph = VGroup(odd_edges, odd_verts)
        self.ly.center_in_content(odd_graph)
        self.play(
            FadeIn(odd_title, shift=LEFT * 0.15),
            Create(odd_edges),
            LaggedStartMap(FadeIn, odd_verts, scale=0.5, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Greedy Coloring Algorithm (90s)
    # ------------------------------------------------------------------
    def scene5_greedy(self):
        self.add_subcaption(
            "The greedy coloring algorithm iterates through vertices in some "
            "order and assigns each vertex the smallest available color not "
            "used by its neighbors. It is fast, but the result depends on "
            "the ordering you choose.",
            duration=17,
        )
        self.ly.section_divider(4, "Greedy Coloring Algorithm")

        # Algorithm description
        algo_title = self.ly.title("Greedy Coloring")
        steps = [
            Text(
                "1. Pick an ordering of the vertices",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. Assign each vertex the smallest available color",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "3. A color is available if no neighbor uses it",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(steps, start_from=algo_title)
        self.wait(2)
        self.ly.clear()

        # Step-by-step greedy on a small graph
        self.add_subcaption(
            "Let us walk through an example. We have five vertices "
            "connected as shown. Processing them left to right, we "
            "assign colors one at a time.",
            duration=14,
        )
        step_title = self.ly.title("Step-by-Step Example")

        g_verts = VGroup(
            Dot(LEFT * 2.5, color=WHITE, radius=0.15),
            Dot(LEFT * 0.8, color=WHITE, radius=0.15),
            Dot(UP * 0.5 + RIGHT * 0.5, color=WHITE, radius=0.15),
            Dot(DOWN * 1.2 + RIGHT * 0.5, color=WHITE, radius=0.15),
            Dot(RIGHT * 2.5 + DOWN * 0.3, color=WHITE, radius=0.15),
        )
        g_edges = VGroup(
            Line(g_verts[0].get_center(), g_verts[1].get_center(), color=DIM, stroke_width=2),
            Line(g_verts[1].get_center(), g_verts[2].get_center(), color=DIM, stroke_width=2),
            Line(g_verts[1].get_center(), g_verts[3].get_center(), color=DIM, stroke_width=2),
            Line(g_verts[2].get_center(), g_verts[3].get_center(), color=DIM, stroke_width=2),
            Line(g_verts[3].get_center(), g_verts[4].get_center(), color=DIM, stroke_width=2),
        )
        g_graph = VGroup(g_edges, g_verts)
        self.ly.center_in_content(g_graph)
        self.play(
            FadeIn(step_title),
            Create(g_edges),
            LaggedStartMap(FadeIn, g_verts, scale=0.5, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Color vertices one by one
        self.play(g_verts[0].animate.set_color(COLOR_1), run_time=FAST)
        self.wait(0.3)
        self.play(g_verts[1].animate.set_color(COLOR_2), run_time=FAST)
        self.wait(0.3)
        self.play(g_verts[2].animate.set_color(COLOR_1), run_time=FAST)
        self.wait(0.3)
        self.play(g_verts[3].animate.set_color(COLOR_3), run_time=FAST)
        self.wait(0.3)
        self.play(g_verts[4].animate.set_color(COLOR_1), run_time=FAST)
        self.wait(1)

        count_label = Text(
            "Used 3 colors (red, blue, green)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(count_label, direction=DOWN, anchor=g_graph, buff=0.4)
        self.play(FadeIn(count_label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

        # ORDER DEPENDENCE demo
        self.add_subcaption(
            "Here is the key insight: the greedy result depends on vertex "
            "order. The same graph with a different processing order may "
            "use more colors. Greedy is not always optimal.",
            duration=16,
        )
        order_title = self.ly.title("Order Matters!")

        g2_verts = VGroup(
            Dot(LEFT * 2.5, color=WHITE, radius=0.15),
            Dot(LEFT * 0.8, color=WHITE, radius=0.15),
            Dot(UP * 0.5 + RIGHT * 0.5, color=WHITE, radius=0.15),
            Dot(DOWN * 1.2 + RIGHT * 0.5, color=WHITE, radius=0.15),
            Dot(RIGHT * 2.5 + DOWN * 0.3, color=WHITE, radius=0.15),
        )
        g2_edges = VGroup(
            Line(g2_verts[0].get_center(), g2_verts[1].get_center(), color=DIM, stroke_width=2),
            Line(g2_verts[1].get_center(), g2_verts[2].get_center(), color=DIM, stroke_width=2),
            Line(g2_verts[1].get_center(), g2_verts[3].get_center(), color=DIM, stroke_width=2),
            Line(g2_verts[2].get_center(), g2_verts[3].get_center(), color=DIM, stroke_width=2),
            Line(g2_verts[3].get_center(), g2_verts[4].get_center(), color=DIM, stroke_width=2),
        )
        g2_graph = VGroup(g2_edges, g2_verts)
        self.ly.center_in_content(g2_graph)
        self.play(
            FadeIn(order_title),
            Create(g2_edges),
            LaggedStartMap(FadeIn, g2_verts, scale=0.5, lag_ratio=0.1),
            run_time=NORMAL,
        )
        self.wait(0.3)

        # Color in different order: hub vertex (1) first
        order_seq = [1, 0, 2, 3, 4]
        order_col = [COLOR_1, COLOR_2, COLOR_2, COLOR_3, COLOR_1]
        for idx, color in zip(order_seq, order_col):
            self.play(g2_verts[idx].animate.set_color(color), run_time=FAST)
            self.wait(0.3)
        self.wait(0.5)

        order_label = Text(
            "Same graph, different order: 3 colors",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(order_label, direction=DOWN, anchor=g2_graph, buff=0.4)
        self.play(FadeIn(order_label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        takeaway = Text(
            "Greedy is fast but NOT always optimal!",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        ensure_fits(takeaway)
        self.ly.center_in_content(takeaway)
        self.play(
            FadeOut(order_label),
            Write(takeaway),
            run_time=NORMAL,
        )
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: The Four Color Theorem (90s)
    # ------------------------------------------------------------------
    def scene6_four_color(self):
        self.add_subcaption(
            "The Four Color Theorem states that every planar graph can be "
            "properly colored using at most four colors. This was first "
            "conjectured in 1852. Kempe published a proof in 1879 that "
            "was believed correct for eleven years until Heawood found a flaw.",
            duration=22,
        )
        self.ly.section_divider(5, "The Four Color Theorem")

        # The theorem
        title = self.ly.title("Four Color Theorem")
        theorem_text = Text(
            "Every planar graph can be colored with at most 4 colors.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        thm_box = self.ly.formula_box(theorem_text, ACCENT)
        self.ly.safe_place(thm_box, direction=DOWN, anchor=title, buff=1)
        self.play(Write(thm_box), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Timeline
        self.add_subcaption(
            "The road to proof was long. Kempe's proof seemed correct "
            "but had a subtle flaw found by Heawood in 1890. It was not "
            "until 1976 that Appel and Haken proved the theorem using a "
            "computer to check hundreds of cases.",
            duration=20,
        )

        timeline_title = self.ly.title("The Road to Proof")
        timeline = VGroup(
            Text("1852: Guthrie conjectures the theorem", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("1879: Kempe publishes a 'proof'", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("1890: Heawood finds the flaw", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("1976: Appel and Haken prove it by computer", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("2005: Robertson et al. simplify the proof", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        )
        self.ly.progressive_reveal(timeline, start_from=timeline_title)
        self.wait(2)
        self.ly.clear()

        # Philosophical question
        self.add_subcaption(
            "This raised a profound question: is a proof valid if no human "
            "can verify every step? The computer checked over a thousand "
            "reducible configurations.",
            duration=14,
        )
        phil_title = self.ly.title("A Philosophical Question")
        phil = Text(
            "If a computer checks the proof, is it really a proof?",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        ensure_fits(phil)
        self.ly.center_in_content(phil)
        self.play(FadeIn(phil, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        context = Text(
            "The proof required checking 1,936 reducible configurations.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(context, direction=DOWN, anchor=phil, buff=0.5)
        self.play(FadeIn(context), run_time=FAST)
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Chromatic Number Bounds (60s)
    # ------------------------------------------------------------------
    def scene7_bounds(self):
        self.add_subcaption(
            "We can bound the chromatic number without knowing it exactly. "
            "The clique number gives a lower bound. The maximum degree "
            "gives an upper bound. Brook's theorem tightens this further "
            "for most connected graphs.",
            duration=18,
        )
        self.ly.section_divider(6, "Bounding the Chromatic Number")

        # Lower bound
        title = self.ly.title("Bounds on the Chromatic Number")

        lower = MathTex(
            r"\chi(G)", r"\geq", r"\omega(G)",
            font_size=HEADING_SIZE,
        )
        lower.set_color_by_tex(r"\chi(G)", ACCENT)
        lower.set_color_by_tex(r"\omega(G)", SECONDARY)
        lower_desc = Text(
            "clique number = size of largest complete subgraph",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        lower_group = VGroup(lower, lower_desc).arrange(DOWN, buff=0.2)
        self.ly.safe_place(lower_group, direction=DOWN, anchor=title, buff=0.8)
        self.play(Write(lower), run_time=NORMAL)
        self.play(FadeIn(lower_desc), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

        # Upper bound
        ub_title = self.ly.title("Upper Bound")
        upper = MathTex(
            r"\chi(G)", r"\leq", r"\Delta(G) + 1",
            font_size=HEADING_SIZE,
        )
        upper.set_color_by_tex(r"\chi(G)", ACCENT)
        upper.set_color_by_tex(r"\Delta(G)", PRIMARY)
        upper_desc = Text(
            "maximum degree = largest number of neighbors",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        upper_group = VGroup(upper, upper_desc).arrange(DOWN, buff=0.2)
        self.ly.safe_place(upper_group, direction=DOWN, anchor=ub_title, buff=0.8)
        self.play(Write(upper), run_time=NORMAL)
        self.play(FadeIn(upper_desc), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()

        # Brook's theorem
        brook_title = self.ly.title("Brook's Theorem")
        brook = Text(
            "For most connected graphs: chi(G) <= Delta(G)",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        brook_except = Text(
            "Exceptions: complete graphs and odd cycles",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        brook_group = VGroup(brook, brook_except).arrange(DOWN, buff=0.2)
        self.ly.safe_place(brook_group, direction=DOWN, anchor=brook_title, buff=0.8)
        self.play(FadeIn(brook, shift=LEFT * 0.15), run_time=NORMAL)
        self.play(FadeIn(brook_except), run_time=FAST)
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Summary (50s)
    # ------------------------------------------------------------------
    def scene8_summary(self):
        self.add_subcaption(
            "Let us review. Proper vertex coloring assigns colors so no "
            "adjacent vertices match. The chromatic number is the minimum "
            "colors needed. The greedy algorithm is fast but order-dependent. "
            "Every planar graph needs at most four colors.",
            duration=18,
        )
        self.ly.section_divider(7, "Summary")

        title = self.ly.title("Graph Coloring: Key Takeaways")

        points = [
            Text(
                "Proper coloring: no adjacent vertices share a color",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Chromatic number: minimum colors needed",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Bipartite graphs: exactly 2-colorable",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Greedy algorithm: fast but order-dependent",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Four Color Theorem: 4 colors suffice for any planar graph",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        self.wait(2)

        apps = Text(
            "Applications: exam scheduling, register allocation, map coloring",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(apps, direction=DOWN, anchor=points[-1], buff=0.5)
        self.play(FadeIn(apps, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Outro
    # ------------------------------------------------------------------
    def scene9_outro(self):
        self.add_subcaption(
            "That concludes our Discrete Mathematics playlist! From logic "
            "and sets to graph coloring, we have covered the foundational "
            "topics of discrete math. Thank you for watching this entire "
            "journey. Stay curious and keep exploring mathematics.",
            duration=18,
        )
        play_outro(self, "Discrete Mathematics Complete", "Discrete Mathematics")
