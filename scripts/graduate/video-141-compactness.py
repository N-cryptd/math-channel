"""
Video 141: Compactness -- Topology Playlist
TEMPLATE v2 -- Professional quality Manim script

Playlist: Topology (Video 6 of 12)
Class: Video141_Compactness
"""

from manim import *
import numpy as np
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits, clamp_position


class Video141_Compactness(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_definition()
        self.scene3_noncompact_example()
        self.scene4_properties()
        self.scene5_heine_borel()
        self.scene6_sequential_compactness()
        self.scene7_tychonoff()
        self.scene8_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "What does it mean for a space to be compact? "
            "Imagine a closed disk covered by infinitely many tiny "
            "open patches. Compactness means you can always find "
            "finitely many of those patches that still cover the "
            "entire disk. You never need infinitely many. "
            "This idea, every open cover has a finite subcover, "
            "is one of the most powerful concepts in all of topology.",
            duration=50,
        )
        play_intro(self, "Compactness", "Topology")
        disk = Circle(radius=1.8, color=SECONDARY, fill_opacity=0.15, stroke_width=3)
        self.ly.center_in_content(disk)
        self.play(Create(disk), run_time=NORMAL)
        self.wait(0.5)
        covers = VGroup()
        cover_positions = [
            (-0.8, 0.6), (0.5, 0.9), (0.1, -0.3), (-0.6, -0.7),
            (0.9, 0.2), (-0.2, 0.1), (0.7, -0.8), (-1.0, -0.1),
        ]
        colors = [PRIMARY, SECONDARY, ACCENT, "#E8A0BF", "#C3F73A", "#FF9F1C", "#7B2D8E", "#2EC4B6"]
        for i, (x, y) in enumerate(cover_positions):
            c = Circle(radius=0.55, color=colors[i % len(colors)], fill_opacity=0.12, stroke_width=1.5).move_to(np.array([x, y, 0]))
            covers.add(c)
        self.play(*[FadeIn(c, scale=0.6) for c in covers], run_time=2.0, lag_ratio=0.15)
        self.wait(0.5)
        label = Text("infinitely many open sets", font_size=LABEL_SIZE, color=DIM, font=SANS)
        label.next_to(disk, DOWN, buff=0.5)
        self.play(FadeIn(label, shift=UP * 0.15), run_time=FAST)
        self.wait(1.0)
        self.play(FadeOut(label), run_time=FAST)
        question = Text("Can we cover it with only finitely many?", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD)
        question.next_to(disk, DOWN, buff=0.5)
        self.play(FadeIn(question, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1.0)
        self.play(FadeOut(question), FadeOut(covers), run_time=FAST)
        fin_covers = VGroup(
            Circle(radius=1.3, color=PRIMARY, fill_opacity=0.12, stroke_width=2).move_to(LEFT * 0.5 + UP * 0.3),
            Circle(radius=1.3, color=SECONDARY, fill_opacity=0.12, stroke_width=2).move_to(RIGHT * 0.5 + DOWN * 0.3),
            Circle(radius=0.9, color=ACCENT, fill_opacity=0.12, stroke_width=2).move_to(ORIGIN),
        )
        self.play(*[FadeIn(c, scale=0.7) for c in fin_covers], run_time=1.5, lag_ratio=0.2)
        self.wait(0.5)
        yes_label = Text("Yes! That is compactness.", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD)
        yes_label.next_to(disk, DOWN, buff=0.5)
        self.play(FadeIn(yes_label, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    def scene2_definition(self):
        self.add_subcaption(
            "Let us make this precise. An open cover of a set K is a collection of open sets whose union contains K. A finite subcover is a finite subcollection that still covers K. A set K is compact if every open cover admits a finite subcover. The word every is crucial.",
            duration=60,
        )
        self.ly.section_divider("1", "The Definition")
        self.ly.title("Open Cover", color=PRIMARY)
        oc_def = MathTex(r"\mathcal{U} = \{U_i\}_{i \in I}", r"\text{ with }", r"K \subseteq \bigcup_{i \in I} U_i")
        oc_def[0].set_color(PRIMARY)
        oc_def[2].set_color(ACCENT)
        self.ly.center_in_content(oc_def)
        self.play(Write(oc_def), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()
        self.ly.title("Open Cover", color=PRIMARY)
        k_set = VGroup(Line(LEFT * 2, RIGHT * 2, color=SECONDARY, stroke_width=4), Dot(LEFT * 2, color=SECONDARY), Dot(RIGHT * 2, color=SECONDARY))
        self.ly.center_in_content(k_set)
        k_label = Text("K", font_size=BODY_SIZE, color=SECONDARY, font=MONO)
        k_label.next_to(k_set, DOWN, buff=0.2)
        self.play(Create(k_set), FadeIn(k_label), run_time=NORMAL)
        self.wait(0.5)
        u1 = Circle(radius=0.7, color=PRIMARY, fill_opacity=0.1, stroke_width=2).move_to(LEFT * 0.8)
        u2 = Circle(radius=0.7, color=SECONDARY, fill_opacity=0.1, stroke_width=2).move_to(RIGHT * 0.8)
        u3 = Circle(radius=0.5, color=ACCENT, fill_opacity=0.1, stroke_width=2).move_to(ORIGIN)
        self.play(FadeIn(u1), FadeIn(u2), FadeIn(u3), run_time=NORMAL)
        self.wait(0.5)
        union_label = MathTex(r"K \subseteq U_1 \cup U_2 \cup U_3", font_size=LABEL_SIZE, color=WHITE)
        union_label.next_to(k_label, DOWN, buff=0.3)
        self.play(FadeIn(union_label, shift=UP * 0.15), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()
        self.ly.title("Finite Subcover", color=PRIMARY)
        sub_def = MathTex(r"\text{Choose } U_{i_1}, \ldots, U_{i_n}", r"\text{ such that }", r"K \subseteq \bigcup_{k=1}^{n} U_{i_k}")
        sub_def[0].set_color(PRIMARY)
        sub_def[2].set_color(ACCENT)
        self.ly.center_in_content(sub_def)
        self.play(Write(sub_def), run_time=NORMAL)
        self.wait(1.0)
        self.ly.clear()
        self.ly.title("Compactness", color=ACCENT)
        comp_line1 = Text("K is compact if:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        comp_line2 = MathTex(r"\text{EVERY open cover of } K", r"\text{ has a finite subcover.}")
        comp_line2[0].set_color(PRIMARY)
        comp_line2[1].set_color(ACCENT)
        comp_def = VGroup(comp_line1, comp_line2).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.center_in_content(comp_def)
        self.play(FadeIn(comp_line1, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(comp_line2), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    def scene3_noncompact_example(self):
        self.add_subcaption(
            "To understand compactness, let us see a space that is not compact. Consider the open interval zero one. No finite subcollection of our cover reaches the endpoints.",
            duration=60,
        )
        self.ly.section_divider("2", "A Non-Compact Example")
        self.ly.title("(0, 1) is NOT Compact", color=RED)
        nline = NumberLine(x_range=[-0.5, 1.5, 0.5], length=10, color=DIM, include_numbers=True, font_size=LABEL_SIZE)
        self.ly.center_in_content(nline)
        self.play(Create(nline), run_time=NORMAL)
        self.wait(0.3)
        interval = Line(nline.n2p(0.0), nline.n2p(1.0), color=SECONDARY, stroke_width=8)
        self.play(Create(interval), run_time=FAST)
        self.wait(0.3)
        open_dot_left = Circle(radius=0.08, color=RED, stroke_width=3).move_to(nline.n2p(0.0))
        open_dot_right = Circle(radius=0.08, color=RED, stroke_width=3).move_to(nline.n2p(1.0))
        self.play(FadeIn(open_dot_left), FadeIn(open_dot_right), run_time=FAST)
        self.wait(0.5)
        self.ly.clear()
        self.ly.title("No Finite Subcover!", color=RED)
        problem = VGroup(
            Text("No finite subcollection reaches 0 or 1", font_size=BODY_SIZE, color=RED, font=SANS),
            MathTex(r"\bigcup_{k=1}^{n} U_{i_k} \subsetneq (0,1)", color=RED),
        )
        stacked = VGroup(*problem).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.center_in_content(stacked)
        self.play(FadeIn(problem[0], shift=LEFT * 0.15), Write(problem[1]), run_time=NORMAL)
        self.wait(1.5)
        contrast = Text("But [0, 1] IS compact! (closed + bounded)", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD)
        contrast.next_to(stacked, DOWN, buff=0.5)
        self.play(FadeIn(contrast, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    def scene4_properties(self):
        self.add_subcaption(
            "Compact sets have remarkable properties. In a Hausdorff space, every compact set is closed and bounded. A closed subset of a compact set is compact. The continuous image of compact is compact, giving the Extreme Value Theorem.",
            duration=60,
        )
        self.ly.section_divider("3", "Key Properties")
        self.ly.title("Properties of Compact Sets", color=PRIMARY)
        properties = [
            Text("1. Compact => Closed (Hausdorff spaces)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. Compact => Bounded (metric spaces)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3. Closed subset of compact => compact", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("4. Finite union of compact => compact", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("5. Continuous image => compact (EVT!)", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(properties, start_from=None, reveal_anim=FadeIn, anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=1.0)
        self.wait(1.0)
        self.ly.clear()
        self.ly.title("Extreme Value Theorem", color=ACCENT)
        evt_line1 = Text("If K is compact and f is continuous:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        evt_line2 = MathTex(r"f \text{ attains its } \max \text{ and } \min \text{ on } K", color=ACCENT)
        evt = VGroup(evt_line1, evt_line2).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.center_in_content(evt)
        self.play(FadeIn(evt_line1, shift=LEFT * 0.15), Write(evt_line2), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    def scene5_heine_borel(self):
        self.add_subcaption(
            "The Heine Borel theorem gives us a practical criterion for compactness in R^n. A subset K of R^n is compact if and only if K is closed and bounded.",
            duration=60,
        )
        self.ly.section_divider("4", "Heine-Borel Theorem")
        self.ly.title("Heine-Borel Theorem", color=ACCENT)
        line1 = Text("In R^n:", font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD)
        line2 = MathTex(r"K \text{ is compact}", r"\iff", r"K \text{ is closed and bounded}")
        line2[0].set_color(ACCENT)
        line2[2].set_color(SECONDARY)
        statement = VGroup(line1, line2).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        self.ly.center_in_content(statement)
        self.play(Write(line1), run_time=FAST)
        self.play(Write(line2), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()
        self.ly.title("Examples in R^2", color=PRIMARY)
        closed_disk = Circle(radius=1.5, color=SECONDARY, fill_opacity=0.15, stroke_width=3)
        closed_disk_label = Text("Closed disk: COMPACT", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD)
        closed_disk_label.next_to(closed_disk, DOWN, buff=0.3)
        left_col = VGroup(closed_disk, closed_disk_label)
        left_col.move_to(LEFT * 3.2 + DOWN * 0.3)
        open_disk = Circle(radius=1.5, color=RED, fill_opacity=0.1, stroke_width=2)
        open_label = Text("Open disk: NOT compact", font_size=BODY_SIZE, color=RED, font=SANS)
        open_label.next_to(open_disk, DOWN, buff=0.3)
        right_col = VGroup(open_disk, open_label)
        right_col.move_to(RIGHT * 3.2 + DOWN * 0.3)
        self.play(FadeIn(left_col, shift=LEFT * 0.2), FadeIn(right_col, shift=RIGHT * 0.2), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()
        self.ly.title("More Examples", color=PRIMARY)
        rect = Rectangle(width=3, height=2, color=SECONDARY, fill_opacity=0.15, stroke_width=3)
        rect_label = Text("[a,b] x [c,d]: COMPACT", font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD)
        rect_group = VGroup(rect, rect_label).arrange(DOWN, buff=0.3)
        self.ly.center_in_content(rect_group)
        self.play(FadeIn(rect), FadeIn(rect_label, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1.0)
        warning = Text("Caution: Heine-Borel fails in infinite dimensions!", font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD)
        warning.next_to(rect_group, DOWN, buff=0.5)
        self.play(FadeIn(warning, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    def scene6_sequential_compactness(self):
        self.add_subcaption(
            "There is another way to characterize compactness using sequences. A set K is sequentially compact if every sequence in K has a convergent subsequence with limit in K. In metric spaces, compactness and sequential compactness are equivalent.",
            duration=60,
        )
        self.ly.section_divider("5", "Sequential Compactness")
        self.ly.title("Sequential Compactness", color=PRIMARY)
        d1 = Text("K is sequentially compact if:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        d2 = Text("every sequence in K has a convergent", font_size=BODY_SIZE, color=WHITE, font=SANS)
        d3 = Text("subsequence with limit in K.", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD)
        defn = VGroup(d1, d2, d3).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        self.ly.center_in_content(defn)
        self.play(FadeIn(d1, shift=LEFT * 0.15), FadeIn(d2, shift=LEFT * 0.15), FadeIn(d3, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()
        self.ly.title("Visual: Convergent Subsequence", color=PRIMARY)
        seq_line = NumberLine(x_range=[-0.2, 1.2, 0.5], length=10, color=DIM, include_numbers=True, font_size=LABEL_SIZE)
        self.ly.center_in_content(seq_line)
        closed_int = Line(seq_line.n2p(0.0), seq_line.n2p(1.0), color=SECONDARY, stroke_width=6)
        self.play(Create(seq_line), Create(closed_int), run_time=FAST)
        self.wait(0.3)
        seq_positions = [0.1, 0.95, 0.3, 0.85, 0.5, 0.78, 0.4, 0.72, 0.55, 0.68, 0.6, 0.66, 0.63, 0.65]
        seq_dots = VGroup()
        for pos in seq_positions:
            dot = Dot(seq_line.n2p(pos), radius=0.06, color=DIM)
            seq_dots.add(dot)
        self.play(*[FadeIn(d) for d in seq_dots], run_time=2.0, lag_ratio=0.12)
        self.wait(0.5)
        subseq_indices = [1, 3, 5, 7, 9, 11, 13]
        subseq_dots = VGroup(*[seq_dots[i] for i in subseq_indices])
        self.play(*[d.animate.set_color(ACCENT).set_radius(0.09) for d in subseq_dots], run_time=1.5)
        self.wait(0.5)
        limit_dot = Dot(seq_line.n2p(0.65), radius=0.1, color=RED)
        limit_label = Text("limit = 0.65", font_size=LABEL_SIZE, color=RED, font=MONO)
        limit_label.next_to(limit_dot, UP, buff=0.2)
        self.play(FadeIn(limit_dot), FadeIn(limit_label, shift=DOWN * 0.1), run_time=FAST)
        self.wait(1.5)
        self.ly.clear()
        self.ly.title("In Metric Spaces", color=ACCENT)
        equiv = MathTex(r"\text{Compact}", r"\iff", r"\text{Sequentially Compact}", r"\iff", r"\text{Complete \& Totally Bounded}")
        equiv[0].set_color(PRIMARY)
        equiv[2].set_color(SECONDARY)
        equiv[4].set_color(ACCENT)
        self.ly.center_in_content(equiv)
        self.play(Write(equiv), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    def scene7_tychonoff(self):
        self.add_subcaption(
            "One of the deepest results in topology is Tychonoff's theorem. The product of any collection of compact spaces is compact, with respect to the product topology. This holds even for infinite products and is equivalent to the Axiom of Choice.",
            duration=60,
        )
        self.ly.section_divider("6", "Tychonoff's Theorem")
        self.ly.title("Tychonoff's Theorem", color=ACCENT)
        s1 = Text("The product of any collection", font_size=BODY_SIZE, color=WHITE, font=SANS)
        s2 = Text("of compact spaces is compact.", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD)
        s3 = Text("(with the product topology)", font_size=LABEL_SIZE, color=DIM, font=SANS)
        statement = VGroup(s1, s2, s3).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.ly.center_in_content(statement)
        self.play(FadeIn(s1, shift=LEFT * 0.15), FadeIn(s2, shift=LEFT * 0.15), FadeIn(s3, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()
        self.ly.title("Finite Case", color=PRIMARY)
        x_space = Rectangle(width=2.5, height=1.5, color=PRIMARY, fill_opacity=0.1, stroke_width=2)
        x_label = Text("X (compact)", font_size=LABEL_SIZE, color=PRIMARY, font=SANS)
        x_label.next_to(x_space, UP, buff=0.2)
        cross = MathTex(r"\times", font_size=HEADING_SIZE, color=DIM)
        y_space = Rectangle(width=2.5, height=1.5, color=SECONDARY, fill_opacity=0.1, stroke_width=2)
        y_label = Text("Y (compact)", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)
        y_label.next_to(y_space, UP, buff=0.2)
        arrow = MathTex(r"\Rightarrow", font_size=HEADING_SIZE, color=DIM)
        xy_space = Rectangle(width=2.5, height=2.0, color=ACCENT, fill_opacity=0.15, stroke_width=3)
        xy_label = Text("X x Y (compact!)", font_size=LABEL_SIZE, color=ACCENT, font=SANS, weight=BOLD)
        xy_label.next_to(xy_space, UP, buff=0.2)
        top_row = VGroup(x_label, x_space, cross, y_label, y_space).arrange(RIGHT, buff=0.4)
        arrow_obj = arrow.next_to(top_row, DOWN, buff=0.3)
        bottom_row = VGroup(xy_label, xy_space).arrange(DOWN, buff=0.15)
        bottom_row.next_to(arrow_obj, DOWN, buff=0.3)
        product_vis = VGroup(top_row, arrow_obj, bottom_row)
        self.ly.center_in_content(product_vis)
        self.play(FadeIn(top_row, shift=LEFT * 0.15), run_time=NORMAL)
        self.play(Write(arrow_obj), run_time=FAST)
        self.play(FadeIn(bottom_row, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()
        self.ly.title("Even Infinite Products!", color=ACCENT)
        inf1 = MathTex(r"\prod_{\alpha \in A} K_\alpha", r"\text{ is compact}")
        inf1[0].set_color(ACCENT)
        inf1[1].set_color(SECONDARY)
        inf2 = Text("if each K_alpha is compact", font_size=BODY_SIZE, color=WHITE, font=SANS)
        infinite = VGroup(inf1, inf2).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.center_in_content(infinite)
        self.play(Write(inf1), run_time=NORMAL)
        self.play(FadeIn(inf2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.0)
        aoc = Text("Equivalent to the Axiom of Choice!", font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD)
        aoc.next_to(infinite, DOWN, buff=0.5)
        self.play(FadeIn(aoc, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap. Compactness means every open cover has a finite subcover. In metric spaces this is equivalent to sequential compactness. In R^n, compact means closed and bounded. And Tychonoff's theorem extends compactness to products.",
            duration=40,
        )
        self.ly.section_divider("7", "Summary")
        self.ly.title("Compactness", color=ACCENT)
        summary_items = [
            Text("Every open cover has a finite subcover", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("In metric spaces: <=> sequential compactness", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("In R^n: <=> closed and bounded (Heine-Borel)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Continuous image of compact => compact", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Products of compact => compact (Tychonoff)", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(summary_items, start_from=None, reveal_anim=FadeIn, anim_kwargs={"shift": LEFT * 0.15}, run_time=0.8, wait_time=0.8)
        self.wait(1.0)
        self.ly.clear()
        play_outro(self, next_video="Separation Axioms", next_playlist="Topology")

