"""
Video 134: Taylor Series in the Complex Plane -- Complex Analysis
TEMPLATE v2 -- Professional quality Manim script

Playlist: Complex Analysis (Video 11 of 13)
Class: Video134_TaylorSeriesComplex

Topics: Taylor series for analytic functions, convergence in disks,
         radius of convergence = distance to nearest singularity,
         contrast with real Taylor series, coefficient formula from CIF.

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


class Video134_TaylorSeriesComplex(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_formula()
        self.scene3_radius_of_convergence()
        self.scene4_visualizing_convergence()
        self.scene5_real_vs_complex()
        self.scene6_summary()

    # --- Scene 1: Hook -- "Series That Always Converge in Circles" ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "From Cauchy's Integral Formula, we can extract every "
            "derivative of an analytic function. And derivatives give "
            "us power series. In real analysis, Taylor series are "
            "mysterious. Some converge, some do not, and the reasons "
            "are subtle. But in complex analysis, Taylor series always "
            "converge in perfect disks. And the radius is determined "
            "by something beautiful: the distance to the nearest "
            "singularity. This is one of the most striking differences "
            "between real and complex analysis. This is Video 11 of "
            "Complex Analysis.",
            duration=50,
        )
        play_intro(self, "Taylor Series in C", "Complex Analysis")

        # Concentric circles expanding
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=4, y_length=3,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.3)

        # Center point
        center = Dot(point=plane.c2p(0.3, 0), color=ACCENT, radius=0.06)
        self.play(FadeIn(center), run_time=FAST)

        # Expanding circles
        for r, col in [(0.4, SECONDARY), (0.8, SECONDARY), (1.2, PRIMARY), (1.5, RED)]:
            circ = Circle(radius=r, color=col, stroke_width=2)
            circ.move_to(plane.c2p(0.3, 0))
            self.play(Create(circ), run_time=FAST)
            self.wait(0.3)

        # Singularity at edge
        sing = Dot(point=plane.c2p(0.3 + 1.5, 0), color=RED, radius=0.06)
        self.play(FadeIn(sing), run_time=FAST)
        sing_lbl = MathTex(r"z_1", font_size=LABEL_SIZE, color=RED)
        sing_lbl.next_to(sing, RIGHT, buff=0.1)
        self.play(Write(sing_lbl), run_time=FAST)
        self.wait(3)

        caption = Text(
            "Series converges up to the nearest singularity",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(caption, DOWN, anchor=plane, buff=0.3)
        self.play(FadeIn(caption, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: The Taylor Series Formula ~55s

    def scene2_formula(self):
        self.add_subcaption(
            "Every analytic function has a Taylor series expansion. "
            "If f is analytic in a disk centered at a, then f of z "
            "equals the sum from n equals zero to infinity of f to "
            "the n at a divided by n factorial times z minus a to "
            "the n. The coefficients come from Cauchy's Integral "
            "Formula. We already know f to the n at a equals n "
            "factorial over two pi i times the integral of f over "
            "z minus a to the n plus one. So the n-th coefficient is "
            "just one over two pi i times that integral. Every "
            "analytic function equals its Taylor series within the "
            "disk of convergence.",
            duration=55,
        )
        self.ly.section_divider(1, "The Taylor Series Formula")

        # The formula
        series = MathTex(
            r"f(z) = \sum_{n=0}^{\infty}",
            r"\frac{f^{(n)}(a)}{n!}",
            r"(z-a)^n",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, ACCENT, PRIMARY]):
            if i < len(series):
                series[i].set_color(col)
        box = self.ly.formula_box(series, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Coefficient from CIF
        coeff_title = Text(
            "Coefficient from CIF:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(coeff_title)
        self.play(Write(coeff_title), run_time=FAST)
        self.wait(1)

        coeff = MathTex(
            r"c_n = \frac{f^{(n)}(a)}{n!}",
            r"= \frac{1}{2\pi i}",
            r"\oint_\gamma \frac{f(z)}{(z-a)^{n+1}}\,dz",
            font_size=BODY_SIZE,
        )
        for i, col in enumerate([WHITE, DIM, SECONDARY]):
            if i < len(coeff):
                coeff[i].set_color(col)
        self.ly.safe_place(coeff, DOWN, anchor=coeff_title, buff=0.5)
        self.play(Write(coeff), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Key insight
        insight = Text(
            "Every analytic function = its Taylor series",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        box2 = self.ly.formula_box(insight, color=SECONDARY)
        self.ly.center_in_content(box2)
        self.play(Write(box2), run_time=NORMAL)
        self.wait(3)

        inside = Text(
            "(within the disk of convergence)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(inside, DOWN, anchor=box2, buff=0.4)
        self.play(FadeIn(inside, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 3: The Radius of Convergence ~60s

    def scene3_radius_of_convergence(self):
        self.add_subcaption(
            "Here is the key theorem. The Taylor series of f about a "
            "converges for absolute z minus a less than R, where R is "
            "the distance from a to the nearest singularity of f. "
            "The disk of convergence always reaches exactly to the "
            "nearest singularity. For example, one over one minus z "
            "expanded about z equals zero has a singularity at z equals "
            "one, so R equals one. The series is z plus z squared plus "
            "z cubed and so on, which converges for absolute z less "
            "than one. The singularities are the roadblocks. The series "
            "cannot converge past them.",
            duration=60,
        )
        self.ly.section_divider(2, "Radius of Convergence")

        # Statement
        statement = MathTex(
            r"R = \text{dist}(a, \text{nearest singularity of } f)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        box = self.ly.formula_box(statement, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Example 1: 1/(1-z) at z=0
        plane = Axes(
            x_range=[-2, 3, 1], y_range=[-2, 2, 1],
            x_length=5, y_length=3.5,
            axis_config={"include_numbers": True, "font_size": LABEL_SIZE},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.3)

        # Expansion point
        a_pt = Dot(point=plane.c2p(0, 0), color=ACCENT, radius=0.06)
        self.play(FadeIn(a_pt), run_time=FAST)
        a_lbl = MathTex(r"a=0", font_size=LABEL_SIZE, color=ACCENT)
        a_lbl.next_to(a_pt, DOWN, buff=0.15)
        self.play(Write(a_lbl), run_time=FAST)

        # Singularity
        s_pt = Dot(point=plane.c2p(1, 0), color=RED, radius=0.06)
        self.play(FadeIn(s_pt), run_time=FAST)
        s_lbl = MathTex(r"z=1", font_size=LABEL_SIZE, color=RED)
        s_lbl.next_to(s_pt, DOWN, buff=0.15)
        self.play(Write(s_lbl), run_time=FAST)
        self.wait(1)

        # Convergence disk
        disk = Circle(radius=1.0, color=SECONDARY, fill_opacity=0.1, stroke_width=2.5)
        disk.move_to(plane.c2p(0, 0))
        self.play(Create(disk), run_time=NORMAL)
        self.wait(1)

        r_lbl = MathTex(r"R=1", font_size=LABEL_SIZE, color=SECONDARY)
        r_lbl.next_to(disk.get_top(), RIGHT, buff=0.1)
        self.play(Write(r_lbl), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # The series
        series = MathTex(
            r"\frac{1}{1-z} = \sum_{n=0}^{\infty} z^n",
            r"= 1 + z + z^2 + z^3 + \cdots",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, DIM]):
            if i < len(series):
                series[i].set_color(col)
        self.ly.center_in_content(series)
        self.play(Write(series), run_time=NORMAL)
        self.wait(3)

        domain = MathTex(
            r"|z| < 1",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(domain, DOWN, anchor=series, buff=0.4)
        self.play(Write(domain), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 4: Visualizing Convergence ~55s

    def scene4_visualizing_convergence(self):
        self.add_subcaption(
            "Let's visualize what convergence looks like. As we add "
            "more terms to the Taylor series, the partial sums "
            "approximate the function better and better inside the "
            "disk. Outside the disk, the partial sums diverge. At the "
            "boundary, the behavior is more subtle and depends on the "
            "specific function. Inside the disk, the convergence is "
            "uniform on compact sets. This means the Taylor polynomials "
            "converge to the function at the same rate everywhere "
            "inside any smaller disk.",
            duration=55,
        )
        self.ly.section_divider(3, "Visualizing Convergence")

        # Show partial sums
        title = Text(
            "Partial sums of 1/(1-z):",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(title)
        self.play(Write(title), run_time=FAST)
        self.wait(1)

        partials = [
            MathTex(r"T_0 = 1", font_size=HEADING_SIZE, color=DIM),
            MathTex(r"T_1 = 1 + z", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"T_2 = 1 + z + z^2", font_size=HEADING_SIZE, color=SECONDARY),
            MathTex(r"T_n \to \frac{1}{1-z}", font_size=HEADING_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(partials, start_from=title)
        self.wait(4)

        self.ly.clear()

        # Regions
        regions = [
            Text("Inside disk: converges uniformly", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("On boundary: behavior varies", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Outside disk: diverges", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        reg_title = self.ly.title("Convergence Regions")
        self.ly.progressive_reveal(regions, start_from=reg_title)
        self.wait(5)

        self.ly.clear()

    # --- Scene 5: Contrast with Real Analysis ~50s

    def scene5_real_vs_complex(self):
        self.add_subcaption(
            "This is where complex analysis really shines. Consider "
            "the natural log series: one plus x equals x minus x "
            "squared over two plus x cubed over three minus and so "
            "on. In real analysis, this converges only for negative "
            "one less than x less than or equal to one. The reason "
            "is mysterious in real analysis. But in complex analysis, "
            "the same series converges for absolute z less than one, "
            "and the reason is crystal clear: the singularity at "
            "z equals negative one. The complex picture explains what "
            "the real picture cannot.",
            duration=50,
        )
        self.ly.section_divider(4, "Real vs Complex Convergence")

        # The series
        series = MathTex(
            r"\ln(1+z) = z - \frac{z^2}{2} + \frac{z^3}{3} - \cdots",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(series)
        self.play(Write(series), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Two columns: real vs complex
        real_title = Text(
            "Real Analysis:",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        real_detail = MathTex(
            r"-1 < x \leq 1",
            font_size=BODY_SIZE, color=RED,
        )
        real_mystery = Text(
            "Mysterious convergence behavior",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )

        complex_title = Text(
            "Complex Analysis:",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        complex_detail = MathTex(
            r"|z| < 1",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        complex_reason = Text(
            "Singularity at z = -1 explains everything!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        left_items = [real_title, real_detail, real_mystery]
        right_items = [complex_title, complex_detail, complex_reason]

        cols = self.ly.two_columns(left_items, right_items)
        self.wait(5)

        self.ly.clear()

        # Visual: plane with singularity
        plane = Axes(
            x_range=[-2, 2, 1], y_range=[-1.8, 1.8, 1],
            x_length=4, y_length=3,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.3)

        # Singularity at z=-1
        s_pt = Dot(point=plane.c2p(-1, 0), color=RED, radius=0.06)
        self.play(FadeIn(s_pt), run_time=FAST)
        s_lbl = MathTex(r"z=-1", font_size=LABEL_SIZE, color=RED)
        s_lbl.next_to(s_pt, DOWN, buff=0.15)
        self.play(Write(s_lbl), run_time=FAST)

        # Convergence disk centered at z=0, R=1
        disk = Circle(radius=1.0, color=SECONDARY, fill_opacity=0.1, stroke_width=2.5)
        disk.move_to(plane.c2p(0, 0))
        self.play(Create(disk), run_time=NORMAL)
        self.wait(2)

        caption = Text(
            "The singularity determines the radius!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(caption, DOWN, anchor=plane, buff=0.3)
        self.play(FadeIn(caption, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 6: Summary and Preview ~45s

    def scene6_summary(self):
        self.add_subcaption(
            "Let's recap. Every analytic function has a Taylor series "
            "that converges in a disk. The radius equals the distance "
            "to the nearest singularity. Complex Taylor series are "
            "simpler and more beautiful than real ones, because the "
            "radius of convergence always has a clear geometric "
            "explanation. Next time, we will explore what happens when "
            "a function has a singularity inside the region of "
            "interest. This leads to Laurent series, which generalize "
            "Taylor series to include negative powers.",
            duration=45,
        )
        self.ly.section_divider(5, "Summary")

        title = self.ly.title("Key Takeaways")
        self.wait(1)

        points = [
            Text("Analytic f = Taylor series within convergence disk", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Radius = distance to nearest singularity", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Coefficients from CIF: c_n = f^(n)(a)/n!", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Complex convergence is simpler than real", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        self.wait(3)

        self.ly.clear()

        # Final formula
        final = MathTex(
            r"R = \mathrm{dist}(a, \text{nearest singularity})",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        box = self.ly.formula_box(final, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()
        play_outro(self, "Laurent Series", "Complex Analysis")
