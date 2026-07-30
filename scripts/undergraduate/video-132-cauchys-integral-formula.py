"""
Video 132: Cauchy's Integral Formula -- Complex Analysis
TEMPLATE v2 -- Professional quality Manim script

Playlist: Complex Analysis (Video 9 of 13)
Class: Video132_CauchysIntegralFormula

Topics: Cauchy's Integral Formula, contour integrals with singularities,
         the 1/(z-z0) kernel, proof via contour deformation,
         evaluating integrals using CIF, generalized CIF for derivatives,
         analytic once implies analytic infinitely many times.

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


class Video132_CauchysIntegralFormula(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_theorem_statement()
        self.scene3_key_ingredient()
        self.scene4_geometric_proof()
        self.scene5_example1()
        self.scene6_generalized_cif()
        self.scene7_example2()
        self.scene8_summary()

    # --- Scene 1: Hook -- "Values from the Boundary" ~50s
    # Narration ~50s. Elements: contour with interior point, integral reads value, intro

    def scene1_hook(self):
        self.add_subcaption(
            "In the last video we learned Cauchy's theorem: the integral of "
            "an analytic function around a closed contour is zero. But what "
            "if the function has a singularity inside the contour? Then the "
            "integral is no longer zero, and it encodes something beautiful. "
            "Cauchy's Integral Formula says the value of an analytic "
            "function at any interior point is completely determined by "
            "its values on the boundary. This is Video 9 of Complex Analysis.",
            duration=50,
        )
        play_intro(self, "Cauchy's Integral Formula", "Complex Analysis")

        # Complex plane with a contour and an interior point
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=5, y_length=3.5,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.5)

        # Closed contour (ellipse)
        contour = Ellipse(
            width=4.0, height=2.8, color=SECONDARY, stroke_width=2.5,
        )
        contour.move_to(plane.c2p(0, 0))
        self.play(Create(contour), run_time=NORMAL)
        self.wait(0.5)

        # Interior point
        z0_dot = Dot(point=plane.c2p(0.5, 0.3), color=ACCENT, radius=0.06)
        self.play(FadeIn(z0_dot), run_time=FAST)
        self.wait(0.5)

        z0_lbl = MathTex(r"z_0", font_size=LABEL_SIZE, color=ACCENT)
        z0_lbl.next_to(z0_dot, UR, buff=0.1)
        self.play(Write(z0_lbl), run_time=FAST)

        # Gamma label
        gamma_lbl = MathTex(r"\gamma", font_size=LABEL_SIZE, color=SECONDARY)
        gamma_lbl.next_to(contour.get_top(), RIGHT, buff=0.15)
        self.play(Write(gamma_lbl), run_time=FAST)
        self.wait(3)

        # Arrow from boundary to interior point (metaphorical)
        arrow = Arrow(
            start=plane.c2p(2.0, 0.5),
            end=plane.c2p(0.5, 0.3),
            color=ACCENT, stroke_width=2, max_tip_length_to_length_ratio=0.15,
        )
        self.play(Create(arrow), run_time=NORMAL)
        self.wait(2)

        readout = Text(
            "Boundary values determine interior values!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(readout, DOWN, anchor=plane, buff=0.3)
        self.play(FadeIn(readout, shift=UP * 0.15), run_time=FAST)
        self.wait(6)

        self.ly.clear()

    # --- Scene 2: The Theorem Statement ~55s
    # Narration ~55s. Elements: theorem box, three key conditions

    def scene2_theorem_statement(self):
        self.add_subcaption(
            "Here is the theorem. If f is analytic on and inside a simple "
            "closed contour gamma, and z zero is a point inside gamma, then "
            "f of z zero equals one over two pi i times the integral around "
            "gamma of f of z over z minus z zero dz. The left side is just "
            "a function value. The right side is an integral over the "
            "boundary. This is remarkable: boundary data determines "
            "interior values completely. For analytic functions, knowing "
            "the values on a circle tells you everything inside.",
            duration=55,
        )
        self.ly.section_divider(1, "The Theorem Statement")

        # Theorem in a formula box
        theorem = MathTex(
            r"f(z_0) = \frac{1}{2\pi i}",
            r"\oint_\gamma \frac{f(z)}{z - z_0}\,dz",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([ACCENT, WHITE]):
            if i < len(theorem):
                theorem[i].set_color(col)
        box = self.ly.formula_box(theorem, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Three key conditions
        cond_title = Text(
            "Three key conditions:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(cond_title)
        self.play(Write(cond_title), run_time=FAST)
        self.wait(1)

        conditions = [
            Text("1. f is analytic on and inside gamma", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. gamma is a simple closed contour", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3. z_0 is a point inside gamma", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(conditions, start_from=cond_title)
        self.wait(4)

        self.ly.clear()

    # --- Scene 3: The Key Ingredient -- 1/(z - z0) ~60s
    # Narration ~60s. Elements: recall of 1/z integral, small circle around z0,
    #             computation showing 2*pi*i, independence of radius

    def scene3_key_ingredient(self):
        self.add_subcaption(
            "Before proving the formula, let's recall a key fact from the "
            "last video. The integral of one over z minus z zero around "
            "any contour enclosing z zero equals two pi i. Let's verify "
            "this with a small circle of radius r centered at z zero. "
            "Parameterize as z zero plus r e to the i t. Then dz equals "
            "i r e to the i t dt. The integral simplifies to the integral "
            "from zero to two pi of i dt, which is two pi i. Notice the "
            "answer does not depend on r. Any circle around z zero gives "
            "the same result. This is the kernel of Cauchy's formula.",
            duration=60,
        )
        self.ly.section_divider(2, "The Key Ingredient: 1/(z - z_0)")

        # Small circle around z0
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=4, y_length=3,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.3)

        # Point z0
        z0_dot = Dot(point=plane.c2p(0.3, 0), color=ACCENT, radius=0.06)
        self.play(FadeIn(z0_dot), run_time=FAST)
        z0_lbl = MathTex(r"z_0", font_size=LABEL_SIZE, color=ACCENT)
        z0_lbl.next_to(z0_dot, DOWN, buff=0.15)
        self.play(Write(z0_lbl), run_time=FAST)
        self.wait(1)

        # Circle of radius r1
        circ1 = Circle(radius=0.8, color=SECONDARY, stroke_width=2.5)
        circ1.move_to(plane.c2p(0.3, 0))
        self.play(Create(circ1), run_time=NORMAL)
        r1_lbl = MathTex(r"r_1", font_size=LABEL_SIZE, color=SECONDARY)
        r1_lbl.next_to(circ1.get_right(), RIGHT, buff=0.1)
        self.play(Write(r1_lbl), run_time=FAST)
        self.wait(2)

        # Show it gives 2*pi*i
        result1 = MathTex(
            r"\oint_{|z-z_0|=r_1} \frac{1}{z-z_0}\,dz = 2\pi i",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(result1, DOWN, anchor=plane, buff=0.3)
        self.play(Write(result1), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Larger circle — same result
        plane2 = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=4, y_length=3,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane2)
        self.play(Create(plane2), run_time=FAST)
        self.wait(0.3)

        z0_dot2 = Dot(point=plane2.c2p(0.3, 0), color=ACCENT, radius=0.06)
        self.play(FadeIn(z0_dot2), run_time=FAST)

        circ2 = Circle(radius=1.5, color=PRIMARY, stroke_width=2.5)
        circ2.move_to(plane2.c2p(0.3, 0))
        self.play(Create(circ2), run_time=NORMAL)
        r2_lbl = MathTex(r"r_2", font_size=LABEL_SIZE, color=PRIMARY)
        r2_lbl.next_to(circ2.get_right(), RIGHT, buff=0.1)
        self.play(Write(r2_lbl), run_time=FAST)
        self.wait(1)

        # Same result
        result2 = MathTex(
            r"\oint_{|z-z_0|=r_2} \frac{1}{z-z_0}\,dz = 2\pi i",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(result2, DOWN, anchor=plane2, buff=0.3)
        self.play(Write(result2), run_time=NORMAL)
        self.wait(2)

        # Key insight
        insight = Text(
            "The answer is the same for any circle!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=result2, buff=0.3)
        self.play(FadeIn(insight, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

        # The parameterization computation
        param = MathTex(
            r"z = z_0 + r\,e^{it}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(param)
        self.play(Write(param), run_time=NORMAL)
        self.wait(2)

        step2 = MathTex(
            r"dz = i\,r\,e^{it}\,dt",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step2, DOWN, anchor=param, buff=0.5)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        computation = MathTex(
            r"\oint \frac{1}{r\,e^{it}} \cdot i\,r\,e^{it}\,dt",
            r"= \int_0^{2\pi} i\,dt",
            r"= 2\pi i",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([DIM, WHITE, ACCENT]):
            if i < len(computation):
                computation[i].set_color(col)
        self.ly.center_in_content(computation)
        self.play(Write(computation), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # --- Scene 4: The Geometric Proof via Deformation ~65s
    # Narration ~65s. Elements: decomposition trick, first integral = f(z0),
    #             contour deformation, second integral vanishes

    def scene4_geometric_proof(self):
        self.add_subcaption(
            "Now for the proof. The key trick is to decompose the "
            "integrand. Write f of z over z minus z zero as f of z zero "
            "over z minus z zero, plus f of z minus f of z zero over "
            "z minus z zero. The first integral gives f of z zero times "
            "one over two pi i times the integral of one over z minus z "
            "zero, which we know equals two pi i. So the first part gives "
            "f of z zero exactly. For the second integral, we deform the "
            "contour to a tiny circle of radius epsilon around z zero. "
            "Since f is analytic, the numerator is of order epsilon, "
            "and the whole integral vanishes as epsilon goes to zero.",
            duration=65,
        )
        self.ly.section_divider(3, "The Proof: Contour Deformation")

        # Step 1: The decomposition
        decomp_title = Text(
            "Key decomposition:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(decomp_title)
        self.play(Write(decomp_title), run_time=FAST)
        self.wait(1)

        decomp = MathTex(
            r"\frac{f(z)}{z - z_0}",
            r"= \frac{f(z_0)}{z - z_0}",
            r"+ \frac{f(z) - f(z_0)}{z - z_0}",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, SECONDARY, RED]):
            if i < len(decomp):
                decomp[i].set_color(col)
        self.ly.safe_place(decomp, DOWN, anchor=decomp_title, buff=0.5)
        self.play(Write(decomp), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

        # Part 1: the f(z0) part
        part1_title = Text(
            "Part 1:",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(part1_title)
        self.play(Write(part1_title), run_time=FAST)
        self.wait(1)

        part1 = MathTex(
            r"\frac{1}{2\pi i}",
            r"\oint_\gamma \frac{f(z_0)}{z-z_0}\,dz",
            r"= f(z_0)",
            r"\cdot \frac{1}{2\pi i} \cdot 2\pi i = f(z_0)",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([DIM, SECONDARY, ACCENT, WHITE]):
            if i < len(part1):
                part1[i].set_color(col)
        self.ly.safe_place(part1, DOWN, anchor=part1_title, buff=0.4)
        self.play(Write(part1), run_time=NORMAL)
        self.wait(4)

        check1 = MathTex(r"\checkmark", font_size=HEADING_SIZE, color=SECONDARY)
        self.ly.safe_place(check1, DOWN, anchor=part1, buff=0.4)
        self.play(Write(check1), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Part 2: the vanishing part
        part2_title = Text(
            "Part 2:",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(part2_title)
        self.play(Write(part2_title), run_time=FAST)
        self.wait(1)

        # Visual: large contour
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=4, y_length=3,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.3)

        # Large contour
        t_arr = np.linspace(0, 2 * np.pi, 120)
        contour_pts = [
            plane.c2p(
                1.5 * np.cos(t) + 0.2 * np.sin(3 * t),
                1.0 * np.sin(t) + 0.15 * np.cos(2 * t),
            )
            for t in t_arr
        ]
        contour = VMobject()
        contour.set_points_smoothly(contour_pts)
        contour.set_color(SECONDARY)
        contour.set_stroke(width=2.5)
        self.play(Create(contour), run_time=NORMAL)
        self.wait(0.5)

        z0_dot = Dot(point=plane.c2p(0.3, 0.1), color=ACCENT, radius=0.06)
        self.play(FadeIn(z0_dot), run_time=FAST)
        self.wait(2)

        # Shrink contour to tiny circle around z0
        tiny = Circle(radius=0.3, color=RED, stroke_width=2)
        tiny.move_to(plane.c2p(0.3, 0.1))
        self.play(
            Transform(contour, tiny),
            run_time=NORMAL,
        )
        self.wait(1)

        # Bound explanation
        bound = MathTex(
            r"\left|\frac{f(z) - f(z_0)}{z - z_0}\right| \leq M",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(bound, DOWN, anchor=plane, buff=0.3)
        self.play(Write(bound), run_time=NORMAL)
        self.wait(2)

        vanish = MathTex(
            r"\text{Integral} \leq M \cdot 2\pi\varepsilon \to 0",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(vanish, DOWN, anchor=bound, buff=0.3)
        self.play(Write(vanish), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

        # Conclusion
        conclude = MathTex(
            r"\frac{1}{2\pi i}",
            r"\oint_\gamma \frac{f(z)}{z - z_0}\,dz",
            r"= f(z_0)",
            font_size=TITLE_SIZE,
        )
        for i, col in enumerate([DIM, WHITE, ACCENT]):
            if i < len(conclude):
                conclude[i].set_color(col)
        box = self.ly.formula_box(conclude, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # --- Scene 5: Computing with CIF -- Example 1 ~60s
    # Narration ~60s. Elements: integral of z^2/(z-1), identify f and z0,
    #             result via CIF, comparison with parameterization

    def scene5_example1(self):
        self.add_subcaption(
            "Let's put the formula to work. Evaluate the integral of z "
            "squared over z minus one dz, where gamma is the circle "
            "absolute z equals two. First identify f of z equals z squared "
            "and z zero equals one, which is inside the circle. By Cauchy's "
            "Integral Formula, the integral equals two pi i times f of one, "
            "which is two pi i times one, giving two pi i. Notice how easy "
            "this is. No parameterization needed, no messy trigonometric "
            "integrals. In the last video we computed similar integrals by "
            "parameterization. Cauchy's formula gives us the answer instantly.",
            duration=60,
        )
        self.ly.section_divider(4, "Example 1: CIF in Action")

        # The integral
        integral = MathTex(
            r"\oint_\gamma \frac{z^2}{z - 1}\,dz",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(integral)
        self.play(Write(integral), run_time=NORMAL)
        self.wait(2)

        gamma_info = MathTex(
            r"\gamma:\; |z| = 2",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(gamma_info, DOWN, anchor=integral, buff=0.4)
        self.play(Write(gamma_info), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Visual: circle with z0=1 inside
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=4, y_length=3,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.3)

        circle = Circle(radius=1.5, color=SECONDARY, stroke_width=2.5)
        circle.move_to(plane.c2p(0, 0))
        self.play(Create(circle), run_time=NORMAL)
        self.wait(0.5)

        z0 = Dot(point=plane.c2p(0.75, 0), color=ACCENT, radius=0.06)
        self.play(FadeIn(z0), run_time=FAST)
        z0_lbl = MathTex(r"z_0=1", font_size=LABEL_SIZE, color=ACCENT)
        z0_lbl.next_to(z0, DOWN, buff=0.15)
        self.play(Write(z0_lbl), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Apply CIF
        identify = MathTex(
            r"f(z) = z^2",
            r",\quad z_0 = 1",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([SECONDARY, ACCENT]):
            if i < len(identify):
                identify[i].set_color(col)
        self.ly.center_in_content(identify)
        self.play(Write(identify), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Computation
        steps = MathTex(
            r"\oint_\gamma \frac{z^2}{z-1}\,dz",
            r"= 2\pi i \cdot f(1)",
            r"= 2\pi i \cdot 1",
            r"= 2\pi i",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, DIM, PRIMARY, ACCENT]):
            if i < len(steps):
                steps[i].set_color(col)
        box = self.ly.formula_box(steps, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        insight = Text(
            "No parameterization needed!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=box, buff=0.4)
        self.play(FadeIn(insight, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 6: Higher Derivatives -- The General Formula ~60s
    # Narration ~60s. Elements: generalized formula, cascade of derivatives,
    #             once analytic => infinitely differentiable

    def scene6_generalized_cif(self):
        self.add_subcaption(
            "Cauchy's Integral Formula doesn't just give the function "
            "value. It gives all derivatives too. The generalized formula "
            "says f to the n-th derivative at z zero equals n factorial "
            "over two pi i times the integral of f of z over z minus z "
            "zero to the power n plus one. To get this, just differentiate "
            "the basic formula with respect to z zero. The derivative "
            "passes under the integral sign. This is extraordinary. If a "
            "function is analytic once, it is automatically analytic "
            "infinitely many times. In real analysis, being differentiable "
            "once does not imply twice. But in complex analysis, once "
            "means forever.",
            duration=60,
        )
        self.ly.section_divider(5, "The Generalized Formula")

        # The generalized CIF
        gen_formula = MathTex(
            r"f^{(n)}(z_0)",
            r"= \frac{n!}{2\pi i}",
            r"\oint_\gamma \frac{f(z)}{(z - z_0)^{n+1}}\,dz",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([ACCENT, DIM, WHITE]):
            if i < len(gen_formula):
                gen_formula[i].set_color(col)
        box = self.ly.formula_box(gen_formula, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

        # Cascade visualization
        cascade_title = Text(
            "From boundary to all derivatives:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(cascade_title)
        self.play(Write(cascade_title), run_time=FAST)
        self.wait(1)

        derivs = [
            MathTex(r"f(z_0)", font_size=HEADING_SIZE, color=SECONDARY),
            MathTex(r"f'(z_0)", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"f''(z_0)", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"f'''(z_0)", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"\cdots", font_size=HEADING_SIZE, color=DIM),
        ]
        self.ly.progressive_reveal(derivs, start_from=cascade_title)
        self.wait(3)

        self.ly.clear()

        # Key insight: once = infinitely many
        insight_title = Text(
            "The deepest consequence:",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(insight_title)
        self.play(Write(insight_title), run_time=FAST)
        self.wait(1)

        real_text = Text(
            "Real analysis: differentiable once",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(real_text, DOWN, anchor=insight_title, buff=0.5)
        self.play(FadeIn(real_text, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        real_detail = Text(
            "does NOT imply twice!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(real_detail, DOWN, anchor=real_text, buff=0.3)
        self.play(FadeIn(real_detail, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        complex_text = Text(
            "Complex analysis: analytic once",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(complex_text, DOWN, anchor=real_detail, buff=0.4)
        self.play(FadeIn(complex_text, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        complex_detail = Text(
            "implies infinitely differentiable!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(complex_detail, DOWN, anchor=complex_text, buff=0.3)
        self.play(FadeIn(complex_detail, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 7: Computing Derivatives -- Example 2 ~50s
    # Narration ~50s. Elements: integral of e^z/(z-1)^3, identify n=2 case,
    #             extract second derivative of e^z

    def scene7_example2(self):
        self.add_subcaption(
            "Let's use the generalized formula. Evaluate the integral of "
            "e to the z over z minus one cubed dz, where gamma is "
            "absolute z equals two. This is the n equals two case, so f of "
            "z equals e to the z and z zero equals one. By the generalized "
            "Cauchy Integral Formula, the integral equals two pi i times f "
            "double prime at one divided by two factorial. The second "
            "derivative of e to the z is e to the z, so f double prime at "
            "one equals e. The answer is pi i e. We extracted the second "
            "derivative of e to the z at z equals one, just from a boundary "
            "integral.",
            duration=50,
        )
        self.ly.section_divider(6, "Example 2: Extracting Derivatives")

        # The integral
        integral = MathTex(
            r"\oint_\gamma \frac{e^z}{(z-1)^3}\,dz",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(integral)
        self.play(Write(integral), run_time=NORMAL)
        self.wait(2)

        gamma_info = MathTex(
            r"\gamma:\; |z| = 2, \quad n = 2",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(gamma_info, DOWN, anchor=integral, buff=0.4)
        self.play(Write(gamma_info), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Identify f and z0
        identify = MathTex(
            r"f(z) = e^z",
            r",\quad z_0 = 1",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([SECONDARY, ACCENT]):
            if i < len(identify):
                identify[i].set_color(col)
        self.ly.center_in_content(identify)
        self.play(Write(identify), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Apply generalized CIF
        gen_apply = MathTex(
            r"\oint \frac{e^z}{(z-1)^3}\,dz",
            r"= \frac{2\pi i \cdot f''(1)}{2!}",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, PRIMARY]):
            if i < len(gen_apply):
                gen_apply[i].set_color(col)
        self.ly.center_in_content(gen_apply)
        self.play(Write(gen_apply), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Compute f''(1)
        deriv = MathTex(
            r"f''(z) = e^z",
            r"\implies f''(1) = e",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([SECONDARY, ACCENT]):
            if i < len(deriv):
                deriv[i].set_color(col)
        self.ly.center_in_content(deriv)
        self.play(Write(deriv), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Final answer
        answer = MathTex(
            r"= \frac{2\pi i \cdot e}{2}",
            r"= \pi i \, e",
            font_size=TITLE_SIZE,
        )
        for i, col in enumerate([DIM, ACCENT]):
            if i < len(answer):
                answer[i].set_color(col)
        box = self.ly.formula_box(answer, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        insight = Text(
            "Extracted f''(1) from a boundary integral!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=box, buff=0.4)
        self.play(FadeIn(insight, shift=UP * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # --- Scene 8: Summary and Preview ~45s
    # Narration ~45s. Elements: recap points, key formula, outro

    def scene8_summary(self):
        self.add_subcaption(
            "Let's recap. Cauchy's Integral Formula says f of z zero "
            "equals one over two pi i times the integral of f of z over "
            "z minus z zero dz. The proof uses the decomposition and "
            "contour deformation. The generalized formula gives all "
            "derivatives from boundary data. And most remarkably, if a "
            "function is analytic once, it is analytic infinitely many "
            "times. Next time we will use this formula to prove powerful "
            "consequences including the Maximum Modulus Principle, "
            "Liouville's theorem, and the Fundamental Theorem of Algebra.",
            duration=50,
        )
        self.ly.section_divider(7, "Summary")

        title = self.ly.title("Key Takeaways")
        self.wait(1)

        points = [
            Text("CIF: f(z_0) from boundary integral of f(z)/(z-z_0)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Proof: decomposition + contour deformation", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Generalized CIF gives all derivatives", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Analytic once => infinitely differentiable", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        self.wait(3)

        self.ly.clear()

        # Final formula
        final = MathTex(
            r"f(z_0) = \frac{1}{2\pi i}",
            r"\oint_\gamma \frac{f(z)}{z - z_0}\,dz",
            font_size=TITLE_SIZE,
        )
        for i, col in enumerate([DIM, ACCENT]):
            if i < len(final):
                final[i].set_color(col)
        box = self.ly.formula_box(final, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()
        play_outro(self, "Maximum Modulus Principle", "Complex Analysis")
