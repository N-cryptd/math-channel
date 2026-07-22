"""
Video 130: Complex Integration (Contour Integrals) — Complex Analysis
TEMPLATE v2 -- Professional quality Manim script

Playlist: Complex Analysis (Video 7 of 13)
Class: Video130_ComplexIntegration

Topics: contour integrals, parameterization of curves, integral of f(z) dz,
         examples with polynomials (f(z)=z along line, f(z)=z^2 along semicircle),
         closed contours, preview of Cauchy's theorem.

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


class Video130_ComplexIntegration(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_parameterization()
        self.scene3_definition()
        self.scene4_computing_dz()
        self.scene5_example_line()
        self.scene6_example_semicircle()
        self.scene7_closed_contours()
        self.scene8_summary()

    # --- Scene 1: Hook --- "From the Real Line to the Complex Plane"
    # Narration ~46s. Elements: real line integral, complex plane curve, transition

    def scene1_hook(self):
        self.add_subcaption(
            "In multivariable calculus, you learned about line integrals: "
            "integrating a function along a curve in the plane. The integral "
            "of f of x comma y along a curve C is written as integral_C f ds, "
            "where ds is the arc length element. Now imagine that f is a "
            "complex-valued function and the curve lives in the complex plane. "
            "This gives us the contour integral, the central object in all of "
            "complex analysis. In Video 129 we studied complex derivatives. "
            "Now we study complex integrals. This is Video 7 of Complex Analysis.",
            duration=48,
        )
        play_intro(self, "Complex Integration", "Complex Analysis")

        # Real line integral reminder
        real_int = MathTex(
            r"\int_C f(x,y) \, ds",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(real_int)
        self.play(Write(real_int), run_time=NORMAL)
        self.wait(2)

        real_note = Text(
            "Real line integral: integrate along a curve in R^2",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(real_note, DOWN, anchor=real_int, buff=0.5)
        self.play(FadeIn(real_note, shift=UP * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Complex version
        comp_int = MathTex(
            r"\int_\gamma f(z) \, dz",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.center_in_content(comp_int)
        self.play(Write(comp_int), run_time=NORMAL)
        self.wait(2)

        comp_note = Text(
            "Contour integral: integrate along a curve in C",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(comp_note, DOWN, anchor=comp_int, buff=0.5)
        self.play(FadeIn(comp_note, shift=UP * 0.15), run_time=FAST)
        self.wait(3)

        # Visual: complex plane with a curve
        self.ly.clear()

        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-2, 2, 1],
            x_length=5, y_length=3.5,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(1)

        # Draw a sample contour
        t_vals = np.linspace(0, 2 * np.pi, 100)
        contour_points = [
            plane.c2p(np.cos(t) * 1.5 + 0.3, np.sin(t) * 0.8)
            for t in t_vals
        ]
        contour = VMobject()
        contour.set_points_smoothly(contour_points)
        contour.set_color(SECONDARY)
        contour.set_stroke(width=2.5)

        self.play(Create(contour), run_time=NORMAL)
        self.wait(1)

        gamma_lbl = MathTex(r"\gamma", font_size=LABEL_SIZE, color=SECONDARY)
        gamma_lbl.next_to(contour.get_top(), RIGHT, buff=0.15)
        self.play(Write(gamma_lbl), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: Contours and Parameterization
    # Narration ~52s. Elements: contour curve, gamma(t)=x(t)+iy(t), tangent vector

    def scene2_parameterization(self):
        self.add_subcaption(
            "A contour or path gamma is a piecewise smooth curve in the complex "
            "plane. We describe it with a parameterization: gamma of t equals "
            "x of t plus i times y of t, where t ranges from a to b. Here x of "
            "t and y of t are real-valued functions. The derivative gamma "
            "prime of t equals x prime of t plus i times y prime of t gives "
            "the tangent vector at each point along the curve. The tangent "
            "vector shows both the direction and speed of traversal.",
            duration=50,
        )
        self.ly.section_divider(1, "Contours and Parameterization")

        # Definition
        param_def = MathTex(
            r"\gamma(t) = x(t) + i\,y(t),",
            r"\quad a \le t \le b",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, DIM]):
            if i < len(param_def):
                param_def[i].set_color(col)
        self.ly.center_in_content(param_def)
        self.play(Write(param_def), run_time=NORMAL)
        self.wait(3)

        # Visual: trace a semicircle
        self.ly.clear()

        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.5, 1.5, 1],
            x_length=5, y_length=3,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.5)

        # Upper semicircle from 1 to -1
        t_arr = np.linspace(0, np.pi, 80)
        semi_points = [
            plane.c2p(np.cos(t), np.sin(t))
            for t in t_arr
        ]
        semi = VMobject()
        semi.set_points_smoothly(semi_points)
        semi.set_color(SECONDARY)
        semi.set_stroke(width=2.5)

        self.play(Create(semi), run_time=NORMAL)
        self.wait(1)

        # Label endpoints
        z_a = Dot(plane.c2p(1, 0), color=ACCENT, radius=0.06)
        z_a_lbl = MathTex(r"\gamma(a)=1", font_size=SMALL_SIZE, color=ACCENT)
        z_a_lbl.next_to(z_a, DR, buff=0.1)
        z_b = Dot(plane.c2p(-1, 0), color=ACCENT, radius=0.06)
        z_b_lbl = MathTex(r"\gamma(b)=-1", font_size=SMALL_SIZE, color=ACCENT)
        z_b_lbl.next_to(z_b, DL, buff=0.1)

        self.play(
            FadeIn(z_a), Write(z_a_lbl),
            FadeIn(z_b), Write(z_b_lbl),
            run_time=FAST,
        )
        self.wait(3)

        self.ly.clear()

        # Tangent vector
        deriv_def = MathTex(
            r"\gamma'(t) = x'(t) + i\,y'(t)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(deriv_def)
        self.play(Write(deriv_def), run_time=NORMAL)
        self.wait(2)

        tangent_note = Text(
            "Tangent vector: direction + speed of traversal",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(tangent_note, DOWN, anchor=deriv_def, buff=0.5)
        self.play(FadeIn(tangent_note, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 3: The Contour Integral Definition
    # Narration ~55s. Elements: definition box, u/v decomposition

    def scene3_definition(self):
        self.add_subcaption(
            "The contour integral of f along gamma is defined as follows. "
            "We substitute z equals gamma of t and dz equals gamma prime of "
            "t dt into the integral, giving us the integral from a to b of "
            "f of gamma of t times gamma prime of t, dt. If we write f of z "
            "as u of x comma y plus i times v of x comma y, the integral "
            "splits into two real integrals: the integral of u dx minus v dy, "
            "plus i times the integral of v dx plus u dy. This is why complex "
            "integrals contain twice as much information as real ones.",
            duration=56,
        )
        self.ly.section_divider(2, "The Contour Integral")

        # Main definition in a box
        main_def = MathTex(
            r"\int_\gamma f(z)\,dz"
            r" = \int_a^b f\bigl(\gamma(t)\bigr)\,\gamma'(t)\,dt",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        box = self.ly.formula_box(main_def, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # u+iv decomposition
        decomp_title = Text(
            "If f(z) = u(x,y) + i v(x,y):",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(decomp_title)
        self.play(Write(decomp_title), run_time=FAST)
        self.wait(1)

        decomp = MathTex(
            r"\int_\gamma f(z)\,dz =",
            r"\int_C (u\,dx - v\,dy)",
            r"\;+\; i",
            r"\int_C (v\,dx + u\,dy)",
            font_size=BODY_SIZE,
        )
        for i, col in enumerate([DIM, PRIMARY, WHITE, SECONDARY]):
            if i < len(decomp):
                decomp[i].set_color(col)
        self.ly.safe_place(decomp, DOWN, anchor=decomp_title, buff=0.5)
        self.play(Write(decomp), run_time=NORMAL)
        self.wait(3)

        two_note = Text(
            "Two real integrals in one complex integral!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(two_note, DOWN, anchor=decomp, buff=0.4)
        self.play(FadeIn(two_note, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 4: Computing dz Along a Contour
    # Narration ~45s. Elements: dz formula, three-step algorithm

    def scene4_computing_dz(self):
        self.add_subcaption(
            "In practice, evaluating a contour integral follows three steps. "
            "Step one: parameterize the contour gamma as gamma of t. Step two: "
            "substitute z equals gamma of t and dz equals gamma prime of t dt. "
            "Step three: evaluate the resulting ordinary integral from t equals "
            "a to t equals b. The key substitution is dz equals gamma prime of "
            "t dt, which converts the complex integral into a standard "
            "calculus integral.",
            duration=46,
        )
        self.ly.section_divider(3, "How to Compute a Contour Integral")

        # dz formula
        dz_formula = MathTex(
            r"dz = \gamma'(t)\,dt = \bigl(x'(t) + i\,y'(t)\bigr)\,dt",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(dz_formula)
        self.play(Write(dz_formula), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Three-step algorithm
        steps = [
            Text("1. Parameterize: z = gamma(t)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Substitute: dz = gamma'(t) dt", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Integrate from t=a to t=b", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(steps)
        self.wait(5)

        self.ly.clear()

    # --- Scene 5: Example 1 — f(z) = z along straight line from 0 to 1+i
    # Narration ~58s. Elements: line segment, parameterization, computation

    def scene5_example_line(self):
        self.add_subcaption(
            "Let's compute the contour integral of f of z equals z along the "
            "straight line from z equals zero to z equals one plus i. We "
            "parameterize the line as gamma of t equals t times one plus i, "
            "where t goes from zero to one. Then gamma prime of t equals one "
            "plus i, and f of gamma of t equals t times one plus i. The "
            "integrand becomes t times one plus i, times one plus i, dt, "
            "which simplifies to 2i t dt. Integrating from zero to one gives "
            "2i times t squared over 2, evaluated from zero to one, which "
            "equals i. Notice: the answer depends on the path! A different "
            "curve from zero to one plus i would give a different result.",
            duration=60,
        )
        self.ly.section_divider(4, "Example: f(z) = z along a Line")

        # Visual: the line segment
        plane = Axes(
            x_range=[-0.5, 1.8, 1], y_range=[-0.5, 1.8, 1],
            x_length=4.5, y_length=3.5,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.5)

        line_seg = Line(
            plane.c2p(0, 0), plane.c2p(1, 1),
            color=SECONDARY, stroke_width=2.5,
        )
        z0 = Dot(plane.c2p(0, 0), color=ACCENT, radius=0.06)
        z1 = Dot(plane.c2p(1, 1), color=ACCENT, radius=0.06)
        z0_lbl = MathTex(r"0", font_size=SMALL_SIZE, color=ACCENT)
        z0_lbl.next_to(z0, DL, buff=0.1)
        z1_lbl = MathTex(r"1+i", font_size=SMALL_SIZE, color=ACCENT)
        z1_lbl.next_to(z1, UR, buff=0.1)

        self.play(
            Create(line_seg), FadeIn(z0), FadeIn(z1),
            Write(z0_lbl), Write(z1_lbl),
            run_time=FAST,
        )
        self.wait(3)

        self.ly.clear()

        # Parameterization
        param = MathTex(
            r"\gamma(t) = t(1+i),",
            r"\quad 0 \le t \le 1",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, DIM]):
            if i < len(param):
                param[i].set_color(col)
        self.ly.center_in_content(param)
        self.play(Write(param), run_time=NORMAL)
        self.wait(2)

        deriv = MathTex(
            r"\gamma'(t) = 1 + i",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(deriv, DOWN, anchor=param, buff=0.5)
        self.play(Write(deriv), run_time=FAST)
        self.wait(2)

        self.ly.clear()

        # Computation
        step1 = MathTex(
            r"f\bigl(\gamma(t)\bigr) \cdot \gamma'(t)"
            r" = t(1+i)(1+i) = 2it",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(step1)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(3)

        step2 = MathTex(
            r"\int_0^1 2it\,dt = 2i\left[\frac{t^2}{2}\right]_0^1 = i",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(step2, DOWN, anchor=step1, buff=0.5)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(3)

        path_note = Text(
            "Path-dependent! Different curve = different answer",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(path_note, DOWN, anchor=step2, buff=0.4)
        self.play(FadeIn(path_note, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 6: Example 2 — f(z) = z^2 along upper unit semicircle
    # Narration ~62s. Elements: semicircle, computation steps, final answer

    def scene6_example_semicircle(self):
        self.add_subcaption(
            "Now let's integrate f of z equals z squared along the upper unit "
            "semicircle from z equals one to z equals negative one. We "
            "parameterize using gamma of t equals e to the i t, where t goes "
            "from zero to pi. The derivative is gamma prime of t equals i e to "
            "the i t. Substituting, f of gamma of t is e to the 2i t, and "
            "gamma prime of t is i e to the i t. Their product is i e to the "
            "3i t. The integral becomes i times the integral from zero to pi "
            "of e to the 3i t dt. Evaluating, we get i times e to the 3i t "
            "over 3i, from zero to pi, which equals one third times e to the "
            "3i pi minus one. Since e to the 3i pi equals negative one, the "
            "answer is one third times negative one minus one, which is "
            "negative two thirds.",
            duration=65,
        )
        self.ly.section_divider(5, "Example: f(z) = z^2 along a Semicircle")

        # Visual: semicircle
        plane = Axes(
            x_range=[-1.5, 1.5, 1], y_range=[-0.5, 1.5, 1],
            x_length=4.5, y_length=3,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.5)

        # Semicircle
        t_arr = np.linspace(0, np.pi, 80)
        semi_pts = [
            plane.c2p(np.cos(t), np.sin(t))
            for t in t_arr
        ]
        semi = VMobject()
        semi.set_points_smoothly(semi_pts)
        semi.set_color(SECONDARY)
        semi.set_stroke(width=2.5)

        z_a = Dot(plane.c2p(1, 0), color=ACCENT, radius=0.06)
        z_a_lbl = MathTex(r"1", font_size=SMALL_SIZE, color=ACCENT)
        z_a_lbl.next_to(z_a, DR, buff=0.1)
        z_b = Dot(plane.c2p(-1, 0), color=ACCENT, radius=0.06)
        z_b_lbl = MathTex(r"-1", font_size=SMALL_SIZE, color=ACCENT)
        z_b_lbl.next_to(z_b, DL, buff=0.1)

        self.play(
            Create(semi), FadeIn(z_a), FadeIn(z_b),
            Write(z_a_lbl), Write(z_b_lbl),
            run_time=FAST,
        )
        self.wait(3)

        self.ly.clear()

        # Parameterization
        param = MathTex(
            r"\gamma(t) = e^{it},",
            r"\quad 0 \le t \le \pi",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, DIM]):
            if i < len(param):
                param[i].set_color(col)
        self.ly.center_in_content(param)
        self.play(Write(param), run_time=NORMAL)
        self.wait(2)

        deriv = MathTex(
            r"\gamma'(t) = i\,e^{it}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(deriv, DOWN, anchor=param, buff=0.5)
        self.play(Write(deriv), run_time=FAST)
        self.wait(2)

        self.ly.clear()

        # Computation step 1
        step1 = MathTex(
            r"f\bigl(\gamma(t)\bigr)\,\gamma'(t)"
            r" = e^{2it} \cdot i\,e^{it} = i\,e^{3it}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(step1)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Computation step 2
        step2 = MathTex(
            r"\int_0^\pi i\,e^{3it}\,dt"
            r" = i\left[\frac{e^{3it}}{3i}\right]_0^\pi",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(step2)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Final answer
        final = MathTex(
            r"= \frac{1}{3}\bigl(e^{3i\pi} - 1\bigr)"
            r" = \frac{1}{3}(-1 - 1) = -\frac{2}{3}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(final)
        self.play(Write(final), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 7: Closed Contours and Preview of Cauchy
    # Narration ~50s. Elements: closed contour, integral=0, holomorphic property

    def scene7_closed_contours(self):
        self.add_subcaption(
            "A contour is called closed if the start and end points coincide, "
            "that is, gamma of a equals gamma of b. We write closed contour "
            "integrals with a small circle on the integral sign. Here is a "
            "remarkable fact. If f is holomorphic everywhere on and inside "
            "the closed contour, the integral equals zero. For example, the "
            "function f of z equals z is entire, so its integral over any "
            "closed contour is zero. This is a consequence of Cauchy's "
            "theorem, the central theorem of complex analysis, which we will "
            "study in the next videos.",
            duration=52,
        )
        self.ly.section_divider(6, "Closed Contours")

        # Closed contour visual
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-2, 2, 1],
            x_length=5, y_length=3.5,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.5)

        # Closed ellipse-like curve
        t_arr = np.linspace(0, 2 * np.pi, 100)
        closed_pts = [
            plane.c2p(1.5 * np.cos(t) + 0.2, 0.9 * np.sin(t))
            for t in t_arr
        ]
        closed_curve = VMobject()
        closed_curve.set_points_smoothly(closed_pts)
        closed_curve.set_color(SECONDARY)
        closed_curve.set_stroke(width=2.5)

        self.play(Create(closed_curve), run_time=NORMAL)
        self.wait(1)

        gamma_lbl = MathTex(r"\gamma", font_size=LABEL_SIZE, color=SECONDARY)
        gamma_lbl.next_to(closed_curve.get_top(), RIGHT, buff=0.15)
        self.play(Write(gamma_lbl), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Closed integral notation
        closed_int = MathTex(
            r"\oint_\gamma f(z)\,dz",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(closed_int)
        self.play(Write(closed_int), run_time=NORMAL)
        self.wait(2)

        closed_note = Text(
            "gamma(a) = gamma(b): the contour closes on itself",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(closed_note, DOWN, anchor=closed_int, buff=0.5)
        self.play(FadeIn(closed_note, shift=UP * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Key fact
        key_fact = MathTex(
            r"f \text{ holomorphic on and inside } \gamma",
            r"\;\Longrightarrow\;",
            r"\oint_\gamma f(z)\,dz = 0",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, DIM, ACCENT]):
            if i < len(key_fact):
                key_fact[i].set_color(col)
        self.ly.center_in_content(key_fact)
        self.play(Write(key_fact), run_time=NORMAL)
        self.wait(3)

        # Example
        example = MathTex(
            r"\oint_\gamma z\,dz = 0",
            r"\quad \text{(z is entire)}",
            font_size=BODY_SIZE,
        )
        for i, col in enumerate([ACCENT, DIM]):
            if i < len(example):
                example[i].set_color(col)
        self.ly.safe_place(example, DOWN, anchor=key_fact, buff=0.5)
        self.play(Write(example), run_time=NORMAL)
        self.wait(3)

        # Cauchy teaser
        teaser = Text(
            "This is Cauchy's Theorem — coming up next!",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(teaser, DOWN, anchor=example, buff=0.4)
        self.play(FadeIn(teaser, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 8: Summary and Road Ahead
    # Narration ~38s. Elements: summary, teaser, outro

    def scene8_summary(self):
        self.add_subcaption(
            "Today we learned about complex integration. The key ideas are: "
            "contour integrals generalize real line integrals to the complex "
            "plane. Parameterization converts them into ordinary calculus "
            "integrals using dz equals gamma prime of t dt. The value of the "
            "integral depends on both the function and the path chosen. And "
            "for holomorphic functions, the integral around any closed "
            "contour is zero. In the next video, we will prove Cauchy's "
            "theorem. Thank you for watching!",
            duration=40,
        )

        summary_items = [
            Text("Contour integral: generalizes line integrals to C", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Parameterize gamma(t), substitute z and dz", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Integral depends on the path chosen", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Holomorphic f: closed contour integral = 0", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Next: Cauchy's Theorem", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(summary_items)
        self.wait(5)

        self.ly.clear()

        play_outro(self, "Cauchy's Theorem", "Complex Analysis")
