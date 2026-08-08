"""
Video 162: Normed Spaces -- Functional Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video162_NormedSpaces

Topics: Opening hook (measuring the size of vectors and functions),
        The hierarchy of spaces (vector -> inner product -> normed -> metric -> topological),
        Formal definition of a norm (three axioms),
        Geometric intuition: unit balls in R^2 for L1, L2, L-infinity norms,
        How unit balls morph as p varies,
        Examples of normed spaces (R^n, l^p, l^inf, C[a,b]),
        Every norm induces a metric,
        Properties of norms (reverse triangle inequality, scaling),
        Finite vs infinite dimensional norm equivalence,
        Convergence in normed spaces,
        Teaser: Banach spaces (next video),
        Summary + what's next.

Prerequisites: Videos 151-161 (Measure Theory), Videos 25-40 (Linear Algebra),
              Video 145 (Metric Spaces).

Competitive analysis: channel-analysis/improvements.md [2026-08-07] Normed Spaces.
Key insights: Unit ball morphing (Dr. Will Wood), concrete-to-abstract (3B1B),
application-driven hooks.

Quality Rules (mandatory):
1. Max 5 visible elements per scene at any time
2. Use LayoutEngine for ALL positioning -- no manual .shift() or .to_edge()
3. Progressive disclosure: add items one at a time
4. Each add_subcaption() duration = words / 2.5 seconds (12 words = 5s)
5. Call ly.clear() between scenes
6. Use consistent animation vocabulary from channel_branding.py
7. MathTex: raw strings with single backslashes
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
from layout import LayoutEngine, ensure_fits, clamp_position, MAX_HALF_WIDTH


class Video162_NormedSpaces(Scene):
    """Normed Spaces: First video in the Functional Analysis playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_ladder_of_spaces()
        self.scene3_formal_definition()
        self.scene4_unit_balls_r2()
        self.scene5_unit_ball_morphing()
        self.scene6_examples()
        self.scene7_norm_induces_metric()
        self.scene8_properties()
        self.scene9_finite_vs_infinite()
        self.scene10_convergence()
        self.scene11_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook -- Measuring Size
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: How do we measure the size of a function?"""
        self.add_subcaption(
            "The length of a vector is easy. But what is the 'length' of "
            "a function? Norms give us a rigorous way to measure size "
            "in any vector space.",
            duration=8,
        )
        play_intro(self, "Normed Spaces", "Functional Analysis")

        title = self.ly.title("How Do We Measure Size?")

        vector_label = Text(
            "Length of a vector: easy!", font_size=BODY_SIZE,
            color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(vector_label, anchor=title, direction=DOWN)

        vector_formula = MathTex(
            r"\|(3, 4)\| = \sqrt{3^2 + 4^2} = 5",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(vector_formula, anchor=vector_label, direction=DOWN)

        self.play(
            FadeIn(vector_label, shift=LEFT * 0.15),
            FadeIn(vector_formula, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1)

        self.play(FadeOut(vector_label), FadeOut(vector_formula), run_time=0.4)

        func_label = Text(
            "But what is the 'size' of a function?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(func_label, anchor=title, direction=DOWN)

        func_formula = MathTex(
            r"f(x) = e^{-x^2}", font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(func_formula, anchor=func_label, direction=DOWN)

        self.play(
            FadeIn(func_label, shift=LEFT * 0.15),
            FadeIn(func_formula, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1.5)

        answer = Text(
            "Norms give us a rigorous answer.",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(answer, anchor=func_formula, direction=DOWN)
        self.play(FadeIn(answer, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: The Ladder of Spaces
    # ------------------------------------------------------------------
    def scene2_ladder_of_spaces(self):
        """The hierarchy: vector -> inner product -> normed -> metric -> topological"""
        self.add_subcaption(
            "Each mathematical structure adds a new tool. A vector space "
            "gives addition and scaling. An inner product gives angles. "
            "A norm gives size and distance. We are here: normed spaces.",
            duration=10,
        )
        title = self.ly.title("The Ladder of Spaces")

        boxes = []
        labels_data = [
            ("Topological Space", DIM),
            ("Metric Space", DIM),
            ("Normed Space", PRIMARY),
            ("Inner Product Space", SECONDARY),
            ("Vector Space", WHITE),
        ]

        for label_text, color in labels_data:
            box = RoundedRectangle(
                corner_radius=0.1, stroke_width=2,
                stroke_color=color, fill_opacity=0.15,
                fill_color=color, width=5.0, height=0.7,
            )
            label = Text(label_text, font_size=LABEL_SIZE, color=color, font=SANS)
            group = VGroup(box, label)
            boxes.append(group)

        chain = VGroup(*boxes).arrange(DOWN, buff=0.25)
        self.ly.center_in_content(chain)

        for box in boxes:
            self.play(FadeIn(box, shift=UP * 0.15), run_time=FAST)
            self.wait(0.3)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Formal Definition of a Norm
    # ------------------------------------------------------------------
    def scene3_formal_definition(self):
        """Formal definition: three axioms of a norm."""
        self.add_subcaption(
            "A norm is a function that assigns a non-negative length to "
            "every vector. It satisfies three axioms: positive "
            "definiteness, absolute homogeneity, and the triangle inequality.",
            duration=12,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("Definition of a Norm")

        definition = MathTex(
            r"\|\cdot\| : V \to [0, \infty)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(definition, anchor=title, direction=DOWN)
        self.play(Write(definition), run_time=NORMAL)
        self.wait(0.5)

        axioms = [
            (r"\|x\| \geq 0,\;\; \|x\| = 0 \iff x = 0",
             PRIMARY, "Positive Definiteness"),
            (r"\|\alpha x\| = |\alpha|\,\|x\|",
             SECONDARY, "Absolute Homogeneity"),
            (r"\|x + y\| \leq \|x\| + \|y\|",
             ACCENT, "Triangle Inequality"),
        ]

        for formula_tex, color, name in axioms:
            axiom_formula = MathTex(
                formula_tex, font_size=LABEL_SIZE, color=WHITE,
            )
            axiom_label = Text(
                f"({name})", font_size=SMALL_SIZE, color=color, font=MONO,
            )
            axiom_group = VGroup(axiom_formula, axiom_label).arrange(
                DOWN, buff=0.05, aligned_edge=LEFT,
            )
            ensure_fits(axiom_group)
            self.ly.safe_place(axiom_group, anchor=title, direction=DOWN, buff=0.6)
            self.play(FadeIn(axiom_group, shift=LEFT * 0.15), run_time=NORMAL)
            self.wait(1)
            self.play(FadeOut(axiom_group), run_time=0.4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Unit Balls in R^2
    # ------------------------------------------------------------------
    def scene4_unit_balls_r2(self):
        """Unit balls in R^2: L1 (diamond), L2 (circle), L-infinity (square)."""
        self.add_subcaption(
            "The unit ball of a norm is the set of all vectors with norm "
            "equal to one. In two dimensions, each norm produces a "
            "different shape. The L1 norm gives a diamond, L2 gives "
            "a circle, and L-infinity gives a square.",
            duration=14,
        )
        self.ly.section_divider(2, "Unit Balls")

        title = self.ly.title("Unit Balls in R^2")

        subtitle = Text(
            "The set of vectors with norm = 1",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(subtitle, anchor=title, direction=DOWN)
        self.play(FadeIn(subtitle, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # L1: diamond
        l1_diamond = self._unit_ball_l1()
        l1_label = MathTex(
            r"\|x\|_1 = 1", font_size=LABEL_SIZE, color=PRIMARY,
        )
        l1_group = VGroup(l1_diamond, l1_label).arrange(DOWN, buff=0.2)

        # L2: circle
        l2_circle = Circle(radius=1.2, color=SECONDARY, stroke_width=2.5)
        l2_label = MathTex(
            r"\|x\|_2 = 1", font_size=LABEL_SIZE, color=SECONDARY,
        )
        l2_group = VGroup(l2_circle, l2_label).arrange(DOWN, buff=0.2)

        # L-infinity: square
        l_inf_square = Square(
            side_length=2.4, color=ACCENT, stroke_width=2.5,
        )
        l_inf_label = MathTex(
            r"\|x\|_\infty = 1", font_size=LABEL_SIZE, color=ACCENT,
        )
        l_inf_group = VGroup(l_inf_square, l_inf_label).arrange(DOWN, buff=0.2)

        # Arrange three balls horizontally below subtitle
        three_balls = VGroup(l1_group, l2_group, l_inf_group).arrange(
            RIGHT, buff=1.0,
        )
        three_balls.next_to(subtitle, DOWN, buff=0.5)
        ensure_fits(three_balls)
        clamp_position(three_balls)

        # Animate each ball
        self.play(Create(l1_diamond), FadeIn(l1_label), run_time=NORMAL)
        self.wait(0.5)
        self.play(Create(l2_circle), FadeIn(l2_label), run_time=NORMAL)
        self.wait(0.5)
        self.play(Create(l_inf_square), FadeIn(l_inf_label), run_time=NORMAL)
        self.wait(1)

        # Key insight
        self.play(FadeOut(subtitle), run_time=0.3)
        insight = Text(
            "Choosing a norm = choosing a geometry",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, anchor=three_balls, direction=DOWN)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    def _unit_ball_l1(self):
        """Create a diamond shape representing the L1 unit ball."""
        diamond = VMobject()
        diamond.set_points_as_corners([
            np.array([1.2, 0, 0]),
            np.array([0, 1.2, 0]),
            np.array([-1.2, 0, 0]),
            np.array([0, -1.2, 0]),
            np.array([1.2, 0, 0]),
        ])
        diamond.set_color(PRIMARY)
        diamond.set_stroke(width=2.5)
        return diamond

    # ------------------------------------------------------------------
    # Scene 5: Unit Ball Morphing
    # ------------------------------------------------------------------
    def scene5_unit_ball_morphing(self):
        """The Lp unit ball shape as p varies from 1 to infinity."""
        self.add_subcaption(
            "For the general Lp norm, the unit ball smoothly changes "
            "shape as p increases. At p equals one we get a diamond, "
            "at p equals two a circle, and as p approaches infinity "
            "the ball fills out into a square.",
            duration=12,
        )
        title = self.ly.title("Unit Balls as p Varies")

        # Show the general formula
        formula = MathTex(
            r"\|x\|_p = \left(\sum_{i=1}^{n} |x_i|^p\right)^{1/p}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, anchor=title, direction=DOWN, buff=0.3)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(0.5)

        # Create several unit balls for different p values
        p_values = [1, 1.5, 2, 4, 10, 100]
        balls = []
        labels_list = []

        for p in p_values:
            ball = self._lp_ball(p, radius=1.2)
            balls.append(ball)
            if p >= 100:
                p_str = r"\infty"
            else:
                p_str = str(p)
            lbl = MathTex(
                rf"p = {p_str}", font_size=LABEL_SIZE,
                color=WHITE, font=MONO,
            )
            labels_list.append(lbl)

        # Show p=1 on the left
        start_ball = balls[0].copy()
        start_label = labels_list[0].copy()
        start_group = VGroup(start_ball, start_label).arrange(DOWN, buff=0.15)
        start_group.next_to(formula, DOWN, buff=0.5)
        ensure_fits(start_group)
        clamp_position(start_group)

        self.play(Create(start_ball), FadeIn(start_label), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(formula), run_time=0.3)

        # Morph through intermediate p values
        for i in range(1, len(p_values)):
            self.play(
                Transform(start_ball, balls[i]),
                Transform(start_label, labels_list[i]),
                run_time=1.0,
            )
            self.wait(0.3)

        self.wait(1)
        self.ly.clear()

    def _lp_ball(self, p, radius=1.2, num_points=200):
        """Create an Lp unit ball VMobject for given p value."""
        points = []
        for i in range(num_points):
            theta = 2 * PI * i / num_points
            x = radius * np.sign(np.cos(theta)) * abs(np.cos(theta)) ** (2.0 / p)
            y = radius * np.sign(np.sin(theta)) * abs(np.sin(theta)) ** (2.0 / p)
            points.append(np.array([x, y, 0]))
        points.append(points[0])  # close the curve
        ball = VMobject(color=PRIMARY)
        ball.set_points_smoothly(points)
        ball.set_stroke(width=2.5)
        return ball

    # ------------------------------------------------------------------
    # Scene 6: Examples of Normed Spaces
    # ------------------------------------------------------------------
    def scene6_examples(self):
        """Examples: R^n, l^p, l^infinity, C[a,b]."""
        self.add_subcaption(
            "Many familiar spaces carry a natural norm. Euclidean space "
            "with the standard norm, spaces of sequences with the Lp "
            "norm, bounded sequences, and continuous functions on an "
            "interval with the supremum norm.",
            duration=13,
        )
        self.ly.section_divider(3, "Examples")

        title = self.ly.title("Examples of Normed Spaces")

        examples = [
            (
                r"\mathbb{R}^n:\;\; \|x\|_2 = \sqrt{\sum x_i^2}",
                "Euclidean space",
                SECONDARY,
            ),
            (
                r"\ell^p:\;\; \|x\|_p = \left(\sum |x_n|^p\right)^{1/p}",
                "Sequences with finite p-norm",
                PRIMARY,
            ),
            (
                r"\ell^\infty:\;\; \|x\|_\infty = \sup_n |x_n|",
                "Bounded sequences",
                ACCENT,
            ),
            (
                r"C[a,b]:\;\; \|f\| = \sup_{x \in [a,b]} |f(x)|",
                "Continuous functions on [a,b]",
                RED,
            ),
        ]

        for formula_tex, desc, color in examples:
            formula = MathTex(formula_tex, font_size=LABEL_SIZE, color=color)
            desc_text = Text(
                f"  {desc}", font_size=SMALL_SIZE, color=DIM, font=SANS,
            )
            group = VGroup(formula, desc_text).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
            ensure_fits(group, max_width=MAX_HALF_WIDTH * 1.5)
            self.ly.safe_place(group, anchor=title, direction=DOWN, buff=0.5)
            self.play(FadeIn(group, shift=LEFT * 0.15), run_time=NORMAL)
            self.wait(1.2)
            self.play(FadeOut(group), run_time=0.4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Norm Induces a Metric
    # ------------------------------------------------------------------
    def scene7_norm_induces_metric(self):
        """Every norm induces a metric: d(x,y) = ||x - y||."""
        self.add_subcaption(
            "Every normed space is automatically a metric space. The "
            "distance between two points is simply the norm of their "
            "difference. This connects normed spaces to everything we "
            "learned about metric spaces.",
            duration=11,
        )
        self.ly.section_divider(4, "Norm to Metric")

        title = self.ly.title("Every Norm Induces a Metric")

        # The main formula in a box
        formula = MathTex(
            r"d(x, y) = \|x - y\|",
            font_size=HEADING_SIZE, color=WHITE,
        )
        boxed = self.ly.formula_box(formula, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(boxed), run_time=NORMAL)
        self.wait(1)

        # Three verification items
        checks = [
            (r"d(x,y) \geq 0,\;\; d(x,y) = 0 \iff x = y",
             "Positive definiteness"),
            (r"d(x,y) = d(y,x)",
             "Symmetry"),
            (r"d(x,z) \leq d(x,y) + d(y,z)",
             "Triangle inequality"),
        ]

        prev_check = None
        for formula_tex, desc in checks:
            if prev_check is not None:
                self.play(FadeOut(prev_check), run_time=0.3)

            check_formula = MathTex(
                formula_tex, font_size=LABEL_SIZE, color=WHITE,
            )
            check_desc = Text(
                desc, font_size=SMALL_SIZE, color=DIM, font=SANS,
            )
            check_group = VGroup(check_formula, check_desc).arrange(
                DOWN, buff=0.05, aligned_edge=LEFT,
            )
            ensure_fits(check_group)
            self.ly.safe_place(check_group, anchor=boxed, direction=DOWN, buff=0.4)
            self.play(FadeIn(check_group, shift=LEFT * 0.15), run_time=NORMAL)
            self.wait(1)
            prev_check = check_group

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Properties and Consequences
    # ------------------------------------------------------------------
    def scene8_properties(self):
        """Properties: reverse triangle inequality, scaling consequences."""
        self.add_subcaption(
            "From the three axioms, important consequences follow. The "
            "reverse triangle inequality bounds the difference of norms. "
            "Homogeneity means scaling a vector scales its length. "
            "These rules let us do calculus in abstract spaces.",
            duration=12,
        )
        title = self.ly.title("Properties and Consequences")

        # Reverse triangle inequality
        rti = MathTex(
            r"\big|\|x\| - \|y\|\big| \leq \|x - y\|",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        rti_label = Text(
            "Reverse Triangle Inequality",
            font_size=LABEL_SIZE, color=PRIMARY, font=SANS,
        )
        rti_group = VGroup(rti, rti_label).arrange(DOWN, buff=0.1)
        self.ly.safe_place(rti_group, anchor=title, direction=DOWN)
        self.play(Write(rti), FadeIn(rti_label), run_time=NORMAL)
        self.wait(1.5)

        self.play(FadeOut(rti_group), run_time=0.4)

        # Scaling
        scale_text = MathTex(
            r"\|\alpha x\| = |\alpha| \cdot \|x\|",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        scale_label = Text(
            "Scaling: stretching vectors",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        scale_group = VGroup(scale_text, scale_label).arrange(DOWN, buff=0.1)
        self.ly.safe_place(scale_group, anchor=title, direction=DOWN)
        self.play(Write(scale_text), FadeIn(scale_label), run_time=NORMAL)
        self.wait(1.5)

        self.play(FadeOut(scale_group), run_time=0.4)

        # Key insight
        insight = Text(
            "These are the 'rules of measurement'",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, anchor=title, direction=DOWN, buff=0.8)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Finite vs Infinite Dimensions
    # ------------------------------------------------------------------
    def scene9_finite_vs_infinite(self):
        """Norm equivalence on R^n, but not in infinite dimensions."""
        self.add_subcaption(
            "In finite dimensions, all norms are equivalent: they "
            "produce the same notion of convergence. But in infinite "
            "dimensions, different norms can disagree. A sequence "
            "can converge in one norm but not another.",
            duration=13,
        )
        self.ly.section_divider(5, "Finite vs Infinite Dimensions")

        title = self.ly.title("Are All Norms Equivalent?")

        # Finite dimensions
        finite_title = Text(
            "Finite dimensions (R^n):",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        finite_formula = MathTex(
            r"c\,\|x\|_a \leq \|x\|_b \leq C\,\|x\|_a",
            font_size=HEADING_SIZE, color=WHITE,
        )
        finite_desc = Text(
            "All norms agree on convergence!",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        finite_group = VGroup(finite_title, finite_formula, finite_desc).arrange(
            DOWN, buff=0.15, aligned_edge=LEFT,
        )
        self.ly.safe_place(finite_group, anchor=title, direction=DOWN)
        self.play(FadeIn(finite_group, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.play(FadeOut(finite_group), run_time=0.4)

        # Infinite dimensions
        inf_title = Text(
            "Infinite dimensions: NOT equivalent!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        inf_desc = Text(
            "l^1 vs l^2 convergence can disagree",
            font_size=LABEL_SIZE, color=RED, font=SANS,
        )
        inf_group = VGroup(inf_title, inf_desc).arrange(DOWN, buff=0.15)
        self.ly.safe_place(inf_group, anchor=title, direction=DOWN)
        self.play(FadeIn(inf_group, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        # Insight
        insight = Text(
            "Geometry depends on your choice of norm",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, anchor=inf_group, direction=DOWN, buff=0.5)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Convergence in Normed Spaces
    # ------------------------------------------------------------------
    def scene10_convergence(self):
        """Convergence: ||x_n - x|| -> 0. Teaser for Banach spaces."""
        self.add_subcaption(
            "A sequence converges in a normed space if the distance "
            "between terms shrinks to zero. But some Cauchy sequences "
            "don't converge, just like rationals can approach "
            "irrationals. When every Cauchy sequence converges, "
            "we have a Banach space. That's our next video.",
            duration=14,
        )
        title = self.ly.title("Convergence in Normed Spaces")

        # Convergence formula
        conv_formula = MathTex(
            r"x_n \to x \;\iff\; \|x_n - x\| \to 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        boxed_conv = self.ly.formula_box(conv_formula, color=PRIMARY)
        self.ly.safe_place(boxed_conv, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(boxed_conv), run_time=NORMAL)
        self.wait(1)

        # Cauchy but not convergent
        cauchy = Text(
            "But some Cauchy sequences don't converge...",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(cauchy, anchor=boxed_conv, direction=DOWN, buff=0.5)
        self.play(FadeIn(cauchy, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.play(FadeOut(cauchy), run_time=0.4)

        # Teaser
        teaser = Text(
            "When every Cauchy sequence converges:",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        teaser_result = Text(
            "That's a BANACH SPACE",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        teaser_group = VGroup(teaser, teaser_result).arrange(DOWN, buff=0.2)
        self.ly.safe_place(teaser_group, anchor=boxed_conv, direction=DOWN, buff=0.5)
        self.play(
            FadeIn(teaser, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.play(Write(teaser_result), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 11: Summary + Outro
    # ------------------------------------------------------------------
    def scene11_summary(self):
        """Summary of key points + what's next."""
        self.add_subcaption(
            "To recap: a norm measures size in a vector space. The three "
            "axioms give us the rules of measurement. Unit balls reveal "
            "the geometry. Every norm induces a metric. And when a "
            "normed space is also complete, it becomes a Banach space. "
            "That's what we'll explore next.",
            duration=14,
        )

        title = self.ly.title("Summary")

        bullets = [
            ("A norm measures 'size' in a vector space", PRIMARY),
            ("Three axioms: definiteness, homogeneity, triangle inequality", SECONDARY),
            ("Unit balls reveal the geometry of a norm", ACCENT),
            ("Every norm induces a metric", WHITE),
        ]

        prev = None
        for text, color in bullets:
            if prev is not None:
                self.play(FadeOut(prev), run_time=0.3)

            bullet = Text(
                text, font_size=BODY_SIZE, color=color, font=SANS,
            )
            self.ly.safe_place(bullet, anchor=title, direction=DOWN, buff=0.5)
            self.play(FadeIn(bullet, shift=LEFT * 0.15), run_time=NORMAL)
            self.wait(0.8)
            prev = bullet

        self.wait(1)
        self.ly.clear()

        # Outro
        play_outro(
            self,
            next_video="Banach Spaces",
            next_playlist="Functional Analysis",
        )
