"""
Video 133: Consequences of CIF -- Complex Analysis
TEMPLATE v2 -- Professional quality Manim script

Playlist: Complex Analysis (Video 10 of 13)
Class: Video133_ConsequencesOfCIF

Topics: Cauchy's Estimates, Maximum Modulus Principle, Liouville's Theorem,
         Fundamental Theorem of Algebra, chain of implications from CIF.

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


class Video133_ConsequencesOfCIF(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_cauchy_estimates()
        self.scene3_maximum_modulus()
        self.scene4_liouville()
        self.scene5_fta()
        self.scene6_big_picture()

    # --- Scene 1: Hook -- "From One Formula to Three Theorems" ~50s
    # Narration ~50s. Elements: CIF formula, three branching arrows, intro

    def scene1_hook(self):
        self.add_subcaption(
            "In the last video we learned Cauchy's Integral Formula, which "
            "gives the value of an analytic function at any interior point "
            "from its values on the boundary. But this formula is more "
            "than a computation tool. It is an engine that drives three of "
            "the most important results in all of mathematics: the Maximum "
            "Modulus Principle, Liouville's Theorem, and the Fundamental "
            "Theorem of Algebra. This is Video 10 of Complex Analysis.",
            duration=50,
        )
        play_intro(self, "Consequences of CIF", "Complex Analysis")

        # CIF formula in center
        cif = MathTex(
            r"f(z_0) = \frac{1}{2\pi i}",
            r"\oint_\gamma \frac{f(z)}{z - z_0}\,dz",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([DIM, ACCENT]):
            if i < len(cif):
                cif[i].set_color(col)
        self.ly.center_in_content(cif)
        self.play(Write(cif), run_time=NORMAL)
        self.wait(3)

        # Three branches
        branch_labels = [
            Text("Maximum Modulus", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Liouville's Theorem", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Fundamental Thm of Algebra", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]

        arrows = []
        for label in branch_labels:
            arr = Arrow(
                start=cif.get_bottom() + UP * 0.1,
                end=label.get_top() + UP * 0.1,
                color=DIM, stroke_width=1.5, max_tip_length_to_length_ratio=0.2,
            )
            arrows.append(arr)

        # Position branches in a row below
        branch_group = VGroup(*branch_labels)
        branch_group.arrange(DOWN, buff=0.35)
        self.ly.safe_place(branch_group, DOWN, anchor=cif, buff=1.0)

        # Draw arrows from cif to each branch
        for label, arr in zip(branch_labels, arrows):
            arr.put_start_and_end_on(cif.get_bottom(), label.get_top())
            arr.set_color(label.get_color())
        arrow_group = VGroup(*arrows)

        self.play(
            FadeIn(branch_labels[0], shift=LEFT * 0.15),
            Create(arrows[0]),
            run_time=FAST,
        )
        self.wait(1)
        self.play(
            FadeIn(branch_labels[1], shift=LEFT * 0.15),
            Create(arrows[1]),
            run_time=FAST,
        )
        self.wait(1)
        self.play(
            FadeIn(branch_labels[2], shift=LEFT * 0.15),
            Create(arrows[2]),
            run_time=FAST,
        )
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: The Cauchy Estimates ~55s
    # Narration ~55s. Elements: statement, derivation from CIF, bound formula

    def scene2_cauchy_estimates(self):
        self.add_subcaption(
            "The first consequence is the Cauchy Estimates. If f is "
            "analytic on and inside a circle of radius R centered at z "
            "zero, then the n-th derivative at z zero is bounded by M "
            "times n factorial over R to the n, where M is the maximum "
            "of absolute f on the circle. Here is the idea. From the "
            "generalized CIF, f to the n at z zero equals n factorial "
            "over two pi i times the integral. Taking absolute values "
            "and using the ML inequality gives the bound. This bounds "
            "derivatives in terms of the maximum on the boundary.",
            duration=55,
        )
        self.ly.section_divider(1, "The Cauchy Estimates")

        # Statement
        statement = MathTex(
            r"|f^{(n)}(z_0)|",
            r"\leq \frac{M \cdot n!}{R^n}",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, ACCENT]):
            if i < len(statement):
                statement[i].set_color(col)
        box = self.ly.formula_box(statement, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(3)

        # Where
        where_text = MathTex(
            r"M = \max_{|z-z_0|=R} |f(z)|",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(where_text, DOWN, anchor=box, buff=0.4)
        self.play(Write(where_text), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Derivation sketch
        title = Text(
            "From the generalized CIF:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(title)
        self.play(Write(title), run_time=FAST)
        self.wait(1)

        step1 = MathTex(
            r"|f^{(n)}(z_0)|",
            r"= \frac{n!}{2\pi}",
            r"\left|\oint \frac{f(z)}{(z-z_0)^{n+1}}\,dz\right|",
            font_size=BODY_SIZE,
        )
        for i, col in enumerate([WHITE, DIM, WHITE]):
            if i < len(step1):
                step1[i].set_color(col)
        self.ly.safe_place(step1, DOWN, anchor=title, buff=0.4)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        step2 = MathTex(
            r"\leq \frac{n!}{2\pi} \cdot \frac{M}{R^{n+1}} \cdot 2\pi R",
            r"= \frac{M \cdot n!}{R^n}",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([PRIMARY, ACCENT]):
            if i < len(step2):
                step2[i].set_color(col)
        box2 = self.ly.formula_box(step2, color=ACCENT)
        self.ly.center_in_content(box2)
        self.play(Write(box2), run_time=NORMAL)
        self.wait(4)

        insight = Text(
            "Derivatives bounded by boundary maximum!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=box2, buff=0.4)
        self.play(FadeIn(insight, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 3: Maximum Modulus Principle ~55s
    # Narration ~55s. Elements: statement, visual of |f| on disk,
    #             contrast with real functions

    def scene3_maximum_modulus(self):
        self.add_subcaption(
            "The second consequence is the Maximum Modulus Principle. "
            "If f is analytic on a domain and continuous on its closure, "
            "then the absolute value of f achieves its maximum on the "
            "boundary, not in the interior. Here is the idea. If f had "
            "a local maximum of absolute value at an interior point, "
            "the Cauchy estimates would force f to be constant near that "
            "point. So non-constant analytic functions cannot have interior "
            "maxima of their modulus. Contrast this with real functions: "
            "sine has local maxima everywhere. But no non-constant "
            "analytic function can do this.",
            duration=55,
        )
        self.ly.section_divider(2, "Maximum Modulus Principle")

        # Statement
        statement = Text(
            "|f| achieves its maximum on the boundary",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        box = self.ly.formula_box(statement, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Visual: disk with contour highlighted as max
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=4, y_length=3,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.3)

        # Disk
        disk = Circle(radius=1.5, color=SECONDARY, stroke_width=2.5)
        disk.move_to(plane.c2p(0, 0))
        self.play(Create(disk), run_time=NORMAL)
        self.wait(1)

        # Boundary glow
        boundary_ring = Circle(radius=1.5, color=ACCENT, stroke_width=5)
        boundary_ring.move_to(plane.c2p(0, 0))
        self.play(Create(boundary_ring), run_time=FAST)
        self.wait(0.5)

        # Interior point with lower value
        interior = Dot(point=plane.c2p(0, 0), color=DIM, radius=0.06)
        self.play(FadeIn(interior), run_time=FAST)

        max_lbl = Text(
            "max on boundary",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(max_lbl, DOWN, anchor=plane, buff=0.3)
        self.play(FadeIn(max_lbl, shift=UP * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Contrast
        contrast = Text(
            "Real: sin(x) has interior maxima",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.center_in_content(contrast)
        self.play(FadeIn(contrast, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        complex_text = Text(
            "Complex: non-constant analytic => no interior max of |f|",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(complex_text, DOWN, anchor=contrast, buff=0.4)
        self.play(FadeIn(complex_text, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 4: Liouville's Theorem ~60s
    # Narration ~60s. Elements: statement, proof via Cauchy estimates,
    #             R -> infinity argument

    def scene4_liouville(self):
        self.add_subcaption(
            "The third consequence is Liouville's Theorem: every bounded "
            "entire function is constant. The proof is beautifully simple "
            "using the Cauchy estimates. Let f be entire with absolute f "
            "of z less than or equal to M for all z. For any point z zero "
            "and any radius R, the Cauchy estimate gives the absolute "
            "value of f prime at z zero is at most M over R. Since R can "
            "be arbitrarily large, f prime at z zero must be zero. This "
            "holds for every point z zero, so f is constant. The more "
            "room you give an entire function, the more constrained its "
            "derivative becomes. An entire function that does not grow "
            "must be flat.",
            duration=60,
        )
        self.ly.section_divider(3, "Liouville's Theorem")

        # Statement
        statement = MathTex(
            r"f \text{ entire and bounded}",
            r"\;\Longrightarrow\;",
            r"f \text{ is constant}",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, DIM, ACCENT]):
            if i < len(statement):
                statement[i].set_color(col)
        box = self.ly.formula_box(statement, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Proof: Step 1
        title = Text(
            "Proof:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(title)
        self.play(Write(title), run_time=FAST)
        self.wait(1)

        assumption = MathTex(
            r"|f(z)| \leq M \quad \forall z \in \mathbb{C}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(assumption, DOWN, anchor=title, buff=0.4)
        self.play(Write(assumption), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Step 2: Cauchy estimate for f'
        estimate = MathTex(
            r"|f'(z_0)| \leq \frac{M}{R}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(estimate)
        self.play(Write(estimate), run_time=NORMAL)
        self.wait(3)

        # Let R -> infinity
        limit = MathTex(
            r"R \to \infty",
            r"\;\Longrightarrow\;",
            r"|f'(z_0)| \to 0",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([RED, DIM, ACCENT]):
            if i < len(limit):
                limit[i].set_color(col)
        self.ly.safe_place(limit, DOWN, anchor=estimate, buff=0.5)
        self.play(Write(limit), run_time=NORMAL)
        self.wait(3)

        # So f' = 0 everywhere
        conclusion = MathTex(
            r"f'(z_0) = 0 \;\; \forall z_0 \implies f \text{ is constant}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(conclusion, DOWN, anchor=limit, buff=0.5)
        self.play(Write(conclusion), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Visual: expanding circle
        plane = Axes(
            x_range=[-3, 3, 1], y_range=[-2, 2, 1],
            x_length=5, y_length=3.5,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.3)

        z0_dot = Dot(point=plane.c2p(0.3, 0.1), color=ACCENT, radius=0.06)
        self.play(FadeIn(z0_dot), run_time=FAST)

        # Small circle
        circ = Circle(radius=0.5, color=SECONDARY, stroke_width=2)
        circ.move_to(plane.c2p(0.3, 0.1))
        self.play(Create(circ), run_time=FAST)
        self.wait(1)

        # Expand
        circ_large = Circle(radius=2.0, color=SECONDARY, stroke_width=2)
        circ_large.move_to(plane.c2p(0.3, 0.1))
        self.play(Transform(circ, circ_large), run_time=NORMAL)
        self.wait(1)

        bound_text = MathTex(
            r"\frac{M}{R} \to 0",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(bound_text, DOWN, anchor=plane, buff=0.3)
        self.play(Write(bound_text), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 5: The Fundamental Theorem of Algebra ~65s
    # Narration ~65s. Elements: statement, proof by contradiction via
    #             Liouville, key step showing 1/p(z) bounded

    def scene5_fta(self):
        self.add_subcaption(
            "Now for the crown jewel. The Fundamental Theorem of Algebra "
            "states that every non-constant polynomial with complex "
            "coefficients has at least one complex root. Gauss proved "
            "this in his doctoral thesis. We will prove it using "
            "Liouville's theorem. Proof by contradiction. Suppose p of z "
            "has no root. Then one over p of z is entire. For large "
            "absolute z, p of z behaves like its leading term z to the "
            "n, so one over p of z goes to zero. This means one over p of "
            "z is bounded. By Liouville, one over p of z is constant, so p "
            "of z is constant. But p was assumed non-constant. "
            "Contradiction. One of the oldest problems in mathematics, "
            "proved in three lines.",
            duration=65,
        )
        self.ly.section_divider(4, "Fundamental Theorem of Algebra")

        # Statement
        statement = MathTex(
            r"\text{Every } p(z) \in \mathbb{C}[z] \text{ has a root in } \mathbb{C}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        box = self.ly.formula_box(statement, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Proof chain
        title = Text(
            "Proof by contradiction:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(title)
        self.play(Write(title), run_time=FAST)
        self.wait(1)

        steps = [
            Text("Assume p(z) has no root", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Then 1/p(z) is entire", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("p(z) ~ z^n, so 1/p(z) -> 0 as |z| -> inf", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("1/p(z) is bounded", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Liouville => 1/p(z) constant => p(z) constant!", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(steps, start_from=title)
        self.wait(4)

        self.ly.clear()

        # The contradiction
        contradiction = Text(
            "But p(z) is non-constant. Contradiction!",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        box2 = self.ly.formula_box(contradiction, color=RED)
        self.ly.center_in_content(box2)
        self.play(Write(box2), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Key step: why 1/p(z) is bounded
        key_title = Text(
            "Key step: why is 1/p(z) bounded?",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(key_title)
        self.play(Write(key_title), run_time=FAST)
        self.wait(1)

        leading = MathTex(
            r"p(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_0",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(leading, DOWN, anchor=key_title, buff=0.5)
        self.play(Write(leading), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        behavior = MathTex(
            r"\frac{1}{p(z)} \sim \frac{1}{z^n} \to 0",
            r"\quad \text{as } |z| \to \infty",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([ACCENT, DIM]):
            if i < len(behavior):
                behavior[i].set_color(col)
        self.ly.center_in_content(behavior)
        self.play(Write(behavior), run_time=NORMAL)
        self.wait(2)

        bounded = MathTex(
            r"\implies |1/p(z)| \leq M \text{ for some } M",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(bounded, DOWN, anchor=behavior, buff=0.5)
        self.play(Write(bounded), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 6: The Big Picture ~50s
    # Narration ~50s. Elements: chain of implications, each step colored,
    #             teaser for next video, outro

    def scene6_big_picture(self):
        self.add_subcaption(
            "Let's see the big picture. Cauchy's Integral Formula gives "
            "us the Cauchy Estimates, which bound derivatives in terms "
            "of boundary values. The Cauchy Estimates immediately give "
            "us Liouville's Theorem, that bounded entire functions are "
            "constant. And Liouville's Theorem gives us the Fundamental "
            "Theorem of Algebra, that every polynomial has a complex "
            "root. This is the power of complex analysis. A single "
            "formula about integrals leads to one of the oldest problems "
            "in mathematics. Next time we will explore Taylor series in "
            "the complex plane, and discover they converge in perfect "
            "disks, unlike the real case.",
            duration=50,
        )
        self.ly.section_divider(5, "The Big Picture")

        title = self.ly.title("The Chain of Implications")
        self.wait(1)

        # Chain as sequential items
        items = [
            MathTex(r"\text{Cauchy's Integral Formula}", font_size=BODY_SIZE, color=ACCENT),
            MathTex(r"\Downarrow", font_size=BODY_SIZE, color=DIM),
            MathTex(r"\text{Cauchy Estimates}", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"\Downarrow", font_size=BODY_SIZE, color=DIM),
            MathTex(r"\text{Maximum Modulus + Liouville}", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"\Downarrow", font_size=BODY_SIZE, color=DIM),
            MathTex(r"\text{Fundamental Theorem of Algebra}", font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3)

        self.ly.clear()

        # Final takeaway
        takeaway = Text(
            "One integral formula solves one of",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(takeaway)
        self.play(FadeIn(takeaway, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        takeaway2 = Text(
            "the oldest problems in mathematics!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(takeaway2, DOWN, anchor=takeaway, buff=0.3)
        self.play(FadeIn(takeaway2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()
        play_outro(self, "Taylor Series in the Complex Plane", "Complex Analysis")
