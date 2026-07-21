"""
Video 129: Complex Differentiation — Complex Analysis
TEMPLATE v2 -- Professional quality Manim script

Playlist: Complex Analysis (Video 4 of 13)
Class: Video129_ComplexDifferentiation

Topics: complex derivative definition, why complex differentiability is stronger
         than real, Cauchy-Riemann equations derivation, holomorphic functions,
         example z^2 (holomorphic), counter-example z-bar (nowhere differentiable),
         entire functions.

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


class Video129_ComplexDifferentiation(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_why_stronger()
        self.scene4_derive_cr()
        self.scene5_cr_statement()
        self.scene6_example_z2()
        self.scene7_counterexample_zbar()
        self.scene8_holomorphic()
        self.scene9_summary()

    # --- Scene 1: Hook --- "Same Formula, Different World"
    # Narration ~45s. Elements: real derivative, complex derivative, real line vs C plane

    def scene1_hook(self):
        self.add_subcaption(
            "In calculus, the derivative of f at x is defined as the limit "
            "as h approaches zero of f of x plus h minus f of x, all "
            "over h. Here h is a real number, so it can only approach zero "
            "from the left or from the right. What happens if we replace x "
            "with z, where z is a complex number? We get f prime of z equals "
            "the limit as h approaches zero of f of z plus h minus f of z "
            "over h. The formula looks identical, but h is now complex. "
            "It can approach zero from any direction in the plane. This is "
            "Complex Analysis, Video 4.",
            duration=46,
        )
        play_intro(self, "Complex Differentiation", "Complex Analysis")

        # Real derivative reminder
        real_deriv = MathTex(
            r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(real_deriv)
        self.play(Write(real_deriv), run_time=NORMAL)
        self.wait(2)

        real_note = Text(
            "h is real: approaches from LEFT or RIGHT",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(real_note, DOWN, anchor=real_deriv, buff=0.5)
        self.play(FadeIn(real_note, shift=UP * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Complex version
        comp_deriv = MathTex(
            r"f'(z) = \lim_{h \to 0} \frac{f(z+h) - f(z)}{h}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.center_in_content(comp_deriv)
        self.play(Write(comp_deriv), run_time=NORMAL)
        self.wait(2)

        comp_note = Text(
            "h is complex: approaches from ANY direction!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(comp_note, DOWN, anchor=comp_deriv, buff=0.5)
        self.play(FadeIn(comp_note, shift=UP * 0.15), run_time=FAST)
        self.wait(2)

        # Visual: real line vs complex plane side by side
        self.ly.clear()

        r_title = Text("Real", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        c_title = Text("Complex", font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        left_vg, right_vg = self.ly.two_columns([r_title], [c_title])

        # Real number line with two arrows
        r_line = NumberLine(
            x_range=[-2, 2, 1], length=4.5, color=PRIMARY,
        )
        r_line.move_to(left_vg.get_center() + DOWN * 1.0)
        clamp_position(r_line)
        r_left = Arrow(
            r_line.n2p(-1.8), r_line.n2p(-0.3),
            color=PRIMARY, stroke_width=2.5, buff=0, tip_length=0.15,
        )
        r_right = Arrow(
            r_line.n2p(1.8), r_line.n2p(0.3),
            color=PRIMARY, stroke_width=2.5, buff=0, tip_length=0.15,
        )
        r_label = Text("2 directions", font_size=SMALL_SIZE, color=PRIMARY, font=SANS)
        r_label.next_to(r_line, DOWN, buff=0.2)

        # Complex plane with many arrows
        c_plane = Axes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1],
            x_length=4, y_length=3,
            axis_config={"include_numbers": False}, color=SECONDARY,
        )
        c_plane.move_to(right_vg.get_center() + DOWN * 1.0)
        clamp_position(c_plane)

        # Multiple approach arrows
        arrows = []
        for angle in [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi,
                       5 * np.pi / 4, 3 * np.pi / 2, 7 * np.pi / 4]:
            start = c_plane.c2p(1.8 * np.cos(angle), 1.8 * np.sin(angle))
            end = c_plane.c2p(0.4 * np.cos(angle), 0.4 * np.sin(angle))
            arr = Arrow(start, end, color=SECONDARY, stroke_width=1.5, buff=0, tip_length=0.1)
            arrows.append(arr)
        c_label = Text("Infinitely many!", font_size=SMALL_SIZE, color=SECONDARY, font=SANS)
        c_label.next_to(c_plane, DOWN, buff=0.2)

        self.play(
            Create(r_line), Create(r_left), Create(r_right), FadeIn(r_label),
            Create(c_plane), *[Create(a) for a in arrows], FadeIn(c_label),
            run_time=NORMAL,
        )
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: Complex Derivative — Definition
    # Narration ~50s. Elements: definition formula, shrinking h vectors, convergence

    def scene2_definition(self):
        self.add_subcaption(
            "The formal definition of the complex derivative mirrors the "
            "real case. We say f is differentiable at z zero if the limit "
            "as h approaches zero of f of z zero plus h minus f of z zero, "
            "all over h, exists and is the same regardless of how h "
            "approaches zero. Here h is a complex number. The key point is "
            "that this single limit must agree for every path h takes to "
            "zero. If the limit along the real axis disagrees with the "
            "limit along the imaginary axis, the derivative does not "
            "exist. This is why complex differentiability is so restrictive.",
            duration=50,
        )
        self.ly.section_divider(1, "The Complex Derivative")

        # Formal definition
        deriv_def = MathTex(
            r"f'(z_0) = \lim_{h \to 0} \frac{f(z_0 + h) - f(z_0)}{h},",
            r"\quad h \in \mathbb{C}",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([ACCENT, DIM]):
            if i < len(deriv_def):
                deriv_def[i].set_color(col)
        self.ly.center_in_content(deriv_def)
        self.play(Write(deriv_def), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Visual: h shrinking from different angles
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-2.5, 2.5, 1],
            x_length=5, y_length=4,
            axis_config={"include_numbers": False}, color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(1)

        # z0 point
        z0 = Dot(plane.c2p(0, 0), color=ACCENT, radius=0.08)
        z0_lbl = MathTex(r"z_0", font_size=LABEL_SIZE, color=ACCENT)
        z0_lbl.next_to(z0, DOWN, buff=0.15)
        self.play(FadeIn(z0), Write(z0_lbl), run_time=FAST)
        self.wait(1)

        # Show h vectors shrinking from 3 directions
        for col, angle in [(PRIMARY, 0), (SECONDARY, np.pi / 2), (RED, np.pi / 4)]:
            # First show large h
            h_start = plane.c2p(2 * np.cos(angle), 2 * np.sin(angle))
            h_end = plane.c2p(0, 0)
            h_arrow = Arrow(h_start, h_end, color=col, stroke_width=2, buff=0, tip_length=0.12)
            h_lbl = MathTex(r"h", font_size=SMALL_SIZE, color=col)
            h_lbl.next_to(h_start, UR if angle < np.pi else UL, buff=0.1)
            self.play(Create(h_arrow), Write(h_lbl), run_time=FAST)
            self.wait(1)

            # Then shrink it
            h_mid = plane.c2p(0.8 * np.cos(angle), 0.8 * np.sin(angle))
            h_arrow2 = Arrow(h_mid, h_end, color=col, stroke_width=2, buff=0, tip_length=0.12)
            self.play(Transform(h_arrow, h_arrow2), run_time=FAST)
            self.wait(1)

            h_small = plane.c2p(0.2 * np.cos(angle), 0.2 * np.sin(angle))
            h_arrow3 = Arrow(h_small, h_end, color=col, stroke_width=2, buff=0, tip_length=0.1)
            self.play(Transform(h_arrow, h_arrow3), run_time=FAST)
            self.wait(1)

        # Convergence label
        converge = Text(
            "All paths must give the SAME value",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(converge, DOWN, anchor=plane, buff=0.3)
        self.play(FadeIn(converge, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 3: Why Complex Differentiability Is STRONGER
    # Narration ~48s. Elements: 2 checks vs infinite checks, comparison

    def scene3_why_stronger(self):
        self.add_subcaption(
            "In real analysis, a function is differentiable at x if the "
            "left-hand limit and the right-hand limit of the difference "
            "quotient both exist and agree. That is just two conditions. "
            "In complex analysis, the difference quotient must converge "
            "to the same value along every possible path in the complex "
            "plane. Straight lines from any angle, curves, spirals, zigzag "
            "paths. There are infinitely many conditions to satisfy. This is "
            "why complex differentiable functions are incredibly well "
            "behaved. In fact, if a function is complex differentiable, "
            "it is automatically infinitely differentiable. You cannot "
            "say that in real analysis.",
            duration=52,
        )
        self.ly.section_divider(2, "Why Complex Differentiability is Stronger")

        # Real case
        real_title = Text("Real Differentiability", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        self.ly.center_in_content(real_title)
        self.play(Write(real_title), run_time=NORMAL)
        self.wait(2)

        real_cond = MathTex(
            r"\lim_{h \to 0^+} \frac{f(x+h)-f(x)}{h} = "
            r"\lim_{h \to 0^-} \frac{f(x+h)-f(x)}{h}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(real_cond, DOWN, anchor=real_title, buff=0.5)
        self.play(Write(real_cond), run_time=NORMAL)
        self.wait(2)

        real_count = Text(
            "= 2 conditions (left and right)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(real_count, DOWN, anchor=real_cond, buff=0.4)
        self.play(FadeIn(real_count, shift=UP * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Complex case
        comp_title = Text("Complex Differentiability", font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        self.ly.center_in_content(comp_title)
        self.play(Write(comp_title), run_time=NORMAL)
        self.wait(2)

        comp_cond = MathTex(
            r"\lim_{h \to 0} \frac{f(z_0+h)-f(z_0)}{h}",
            r"\;\text{ must agree for ALL } h \in \mathbb{C}",
            font_size=BODY_SIZE,
        )
        for i, col in enumerate([WHITE, DIM]):
            if i < len(comp_cond):
                comp_cond[i].set_color(col)
        self.ly.safe_place(comp_cond, DOWN, anchor=comp_title, buff=0.5)
        self.play(Write(comp_cond), run_time=NORMAL)
        self.wait(2)

        comp_count = Text(
            "= Infinitely many conditions!",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(comp_count, DOWN, anchor=comp_cond, buff=0.4)
        self.play(FadeIn(comp_count, shift=UP * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Miracle consequence
        miracle = MathTex(
            r"\text{Complex differentiable} \;\Longrightarrow\; "
            r"\text{infinitely differentiable}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(miracle)
        self.play(Write(miracle), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 4: Deriving the Cauchy-Riemann Equations
    # Narration ~60s. Elements: f=u+iv, two approaches, C-R equations

    def scene4_derive_cr(self):
        self.add_subcaption(
            "To derive the Cauchy-Riemann equations, we write f of z "
            "as u of x comma y plus i times v of x comma y, where z "
            "equals x plus iy. Then we compute the derivative using two "
            "different approaches. First, let h approach zero along "
            "the real axis. So h equals delta x is real. The difference "
            "quotient becomes the partial derivative of u with respect "
            "to x plus i times the partial derivative of v with respect "
            "to x. Second, let h approach zero along the imaginary axis. "
            "So h equals i times delta y. After dividing by i, the "
            "quotient becomes the partial derivative of v with respect to "
            "y minus i times the partial derivative of u with respect to y.",
            duration=56,
        )
        self.ly.section_divider(3, "Deriving the Cauchy-Riemann Equations")

        # Decomposition
        decomp = MathTex(
            r"f(z) = f(x + iy) = u(x,y) + i\,v(x,y)",
            font_size=HEADING_SIZE,
        )
        decomp.set_color(WHITE)
        self.ly.center_in_content(decomp)
        self.play(Write(decomp), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Approach 1: Real axis
        app1_title = Text(
            "Approach 1: h along real axis (h = Dx)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.center_in_content(app1_title)
        self.play(Write(app1_title), run_time=FAST)
        self.wait(1)

        app1 = MathTex(
            r"f'(z) = \frac{\partial u}{\partial x} + i\,\frac{\partial v}{\partial x}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(app1, DOWN, anchor=app1_title, buff=0.5)
        self.play(Write(app1), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Approach 2: Imaginary axis
        self.add_subcaption(
            "Since both approaches give the same derivative, we equate "
            "the real parts and the imaginary parts. This yields the "
            "Cauchy-Riemann equations.",
            duration=15,
        )
        app2_title = Text(
            "Approach 2: h along imaginary axis (h = iDy)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.center_in_content(app2_title)
        self.play(Write(app2_title), run_time=FAST)
        self.wait(1)

        app2 = MathTex(
            r"f'(z) = \frac{\partial v}{\partial y}"
            r" - i\,\frac{\partial u}{\partial y}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(app2, DOWN, anchor=app2_title, buff=0.5)
        self.play(Write(app2), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Equate
        eq_label = Text(
            "Both must be equal!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.center_in_content(eq_label)
        self.play(Write(eq_label), run_time=NORMAL)
        self.wait(2)

        # C-R equations
        cr = MathTex(
            r"\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}",
            r"\qquad",
            r"\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([ACCENT, DIM, ACCENT]):
            if i < len(cr):
                cr[i].set_color(col)
        self.ly.safe_place(cr, DOWN, anchor=eq_label, buff=0.5)
        self.play(Write(cr), run_time=NORMAL)
        self.wait(3)

        cr_name = Text(
            "The Cauchy-Riemann Equations",
            font_size=TITLE_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(cr_name, DOWN, anchor=cr, buff=0.4)
        self.play(FadeIn(cr_name, shift=UP * 0.15), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 5: C-R Statement and Meaning
    # Narration ~45s. Elements: theorem box, Jacobian, geometric interpretation

    def scene5_cr_statement(self):
        self.add_subcaption(
            "The Cauchy-Riemann equations are a necessary condition for "
            "complex differentiability. If f equals u plus iv is "
            "differentiable at z zero, then the C-R equations must hold "
            "at that point. The converse is also true: if u and v have "
            "continuous partial derivatives satisfying the C-R equations "
            "at z zero, then f is differentiable there. Geometrically, the "
            "C-R equations force the Jacobian matrix of f to be a "
            "similarity transformation, meaning f preserves angles. "
            "This is called conformality.",
            duration=46,
        )
        self.ly.section_divider(4, "Meaning of the C-R Equations")

        # Theorem statement
        theorem = MathTex(
            r"f = u + iv \;\text{ differentiable at } z_0"
            r" \;\Longrightarrow\;",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.center_in_content(theorem)
        self.play(Write(theorem), run_time=NORMAL)
        self.wait(1)

        cr_eq = MathTex(
            r"\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y},",
            r"\qquad",
            r"\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}",
            font_size=HEADING_SIZE,
        )
        # Use safe coloring — check submobject count first
        for i, col in enumerate([ACCENT, DIM, ACCENT]):
            if i < len(cr_eq):
                cr_eq[i].set_color(col)
        self.ly.safe_place(cr_eq, DOWN, anchor=theorem, buff=0.4)
        self.play(Write(cr_eq), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Geometric interpretation — Jacobian
        geom_title = Text(
            "Geometric meaning: Jacobian = rotation + scaling",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(geom_title)
        self.play(Write(geom_title), run_time=NORMAL)
        self.wait(2)

        jacobian = MathTex(
            r"J_f = \begin{pmatrix}"
            r"\partial u/\partial x & -\partial u/\partial y \\"
            r"\partial u/\partial y & \partial u/\partial x"
            r"\end{pmatrix}"
            r" = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(jacobian, DOWN, anchor=geom_title, buff=0.5)
        self.play(Write(jacobian), run_time=NORMAL)
        self.wait(3)

        conformal = Text(
            "= Similarity transform (preserves angles!)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(conformal, DOWN, anchor=jacobian, buff=0.4)
        self.play(FadeIn(conformal, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 6: Example — f(z) = z^2 (Holomorphic)
    # Narration ~50s. Elements: z^2 decomposition, partials, checkmarks

    def scene6_example_z2(self):
        self.add_subcaption(
            "Let's verify the Cauchy-Riemann equations for f of z "
            "equals z squared. Expanding, z squared equals x squared "
            "minus y squared plus i times 2xy. So u of x comma y "
            "equals x squared minus y squared, and v of x comma y "
            "equals 2xy. Now check the C-R equations. Partial u "
            "partial x equals 2x, partial v partial y equals 2x. "
            "They match. Partial u partial y equals negative 2y, "
            "partial v partial x equals 2y, so negative 2y equals "
            "negative 2y. They match too. The C-R equations hold "
            "everywhere, so z squared is holomorphic on all of C.",
            duration=52,
        )
        self.ly.section_divider(5, "Example: f(z) = z^2")

        # Expansion
        expand = MathTex(
            r"f(z) = z^2 = (x^2 - y^2) + i\,(2xy)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(expand)
        self.play(Write(expand), run_time=NORMAL)
        self.wait(3)

        # u and v
        uv = MathTex(
            r"u = x^2 - y^2,",
            r"\qquad",
            r"v = 2xy",
            font_size=BODY_SIZE,
        )
        for i, col in enumerate([PRIMARY, DIM, SECONDARY]):
            if i < len(uv):
                uv[i].set_color(col)
        self.ly.safe_place(uv, DOWN, anchor=expand, buff=0.5)
        self.play(Write(uv), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # C-R Check 1
        check1 = MathTex(
            r"\frac{\partial u}{\partial x} = 2x",
            r"\qquad",
            r"\frac{\partial v}{\partial y} = 2x",
            r"\quad \checkmark",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([PRIMARY, DIM, SECONDARY, ACCENT]):
            if i < len(check1):
                check1[i].set_color(col)
        self.ly.center_in_content(check1)
        self.play(Write(check1), run_time=NORMAL)
        self.wait(3)

        # C-R Check 2
        check2 = MathTex(
            r"\frac{\partial u}{\partial y} = -2y",
            r"\qquad",
            r"-\frac{\partial v}{\partial x} = -2y",
            r"\quad \checkmark",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([PRIMARY, DIM, SECONDARY, ACCENT]):
            if i < len(check2):
                check2[i].set_color(col)
        self.ly.safe_place(check2, DOWN, anchor=check1, buff=0.5)
        self.play(Write(check2), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Conclusion
        result = Text(
            "C-R hold everywhere: f(z) = z^2 is ENTIRE",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.center_in_content(result)
        self.play(Write(result), run_time=NORMAL)
        self.wait(2)

        formula = MathTex(
            r"f'(z) = 2z \quad \text{(same formula as real!)}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=result, buff=0.5)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 7: Counter-Example — f(z) = z-bar (NOT Differentiable)
    # Narration ~50s. Elements: z-bar decomposition, C-R check with X

    def scene7_counterexample_zbar(self):
        self.add_subcaption(
            "Now for the classic counter-example. In Video 128, we saw "
            "that f of z equals z-bar over z has no limit at zero. What "
            "about just f of z equals z-bar, the complex conjugate? "
            "Write z-bar as x minus iy. So u equals x and v equals "
            "negative y. Check the first C-R equation: partial u "
            "partial x equals 1, but partial v partial y equals "
            "negative 1. One does not equal negative one. The C-R "
            "equations fail! Even though z-bar is continuous everywhere, "
            "it is differentiable nowhere. In real analysis, the absolute "
            "value of x is continuous but not differentiable at one "
            "point. In complex analysis, z-bar is continuous everywhere "
            "but differentiable nowhere. That is how strong the "
            "requirement is.",
            duration=54,
        )
        self.ly.section_divider(6, "Counter-Example: f(z) = z-bar")

        # Function
        func = MathTex(
            r"f(z) = \overline{z} = x - iy",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(func)
        self.play(Write(func), run_time=NORMAL)
        self.wait(2)

        uv = MathTex(
            r"u = x,",
            r"\qquad",
            r"v = -y",
            font_size=BODY_SIZE,
        )
        for i, col in enumerate([PRIMARY, DIM, SECONDARY]):
            if i < len(uv):
                uv[i].set_color(col)
        self.ly.safe_place(uv, DOWN, anchor=func, buff=0.5)
        self.play(Write(uv), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # C-R Check — FAIL
        fail1 = MathTex(
            r"\frac{\partial u}{\partial x} = 1",
            r"\qquad",
            r"\frac{\partial v}{\partial y} = -1",
            r"\quad 1 \neq -1 \;\times",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([PRIMARY, DIM, SECONDARY, RED]):
            if i < len(fail1):
                fail1[i].set_color(col)
        self.ly.center_in_content(fail1)
        self.play(Write(fail1), run_time=NORMAL)
        self.wait(3)

        verdict = Text(
            "C-R FAIL: z-bar is differentiable NOWHERE",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(verdict, DOWN, anchor=fail1, buff=0.5)
        self.play(Write(verdict), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Comparison to real analysis
        comp_note = MathTex(
            r"\text{Real: } |x| \text{ cont. everywhere, not diff. at } 0",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(comp_note)
        self.play(Write(comp_note), run_time=NORMAL)
        self.wait(2)

        comp_note2 = MathTex(
            r"\text{Complex: } \overline{z} \text{ cont. everywhere, diff. } \textbf{NOWHERE}",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(comp_note2, DOWN, anchor=comp_note, buff=0.4)
        self.play(Write(comp_note2), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 8: Holomorphic and Entire Functions
    # Narration ~42s. Elements: definitions, examples, key property

    def scene8_holomorphic(self):
        self.add_subcaption(
            "A function is called holomorphic on an open set capital Omega "
            "if it is complex differentiable at every point of capital "
            "Omega. If a function is holomorphic on all of the complex "
            "plane, we call it entire. Examples of entire functions include "
            "all polynomials, the complex exponential e to the z, sine of "
            "z, and cosine of z. One of the most remarkable facts in all "
            "of mathematics is that if f is holomorphic on an open set, "
            "then f is infinitely differentiable there, f is analytic "
            "meaning it equals its Taylor series, and f satisfies Cauchy's "
            "integral formula. These three properties are automatic "
            "consequences of complex differentiability.",
            duration=48,
        )
        self.ly.section_divider(7, "Holomorphic and Entire Functions")

        # Definitions
        hol_def = Text(
            "Holomorphic: differentiable at every point of an open set",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.center_in_content(hol_def)
        self.play(Write(hol_def), run_time=NORMAL)
        self.wait(2)

        ent_def = Text(
            "Entire: holomorphic on ALL of C",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(ent_def, DOWN, anchor=hol_def, buff=0.4)
        self.play(FadeIn(ent_def, shift=UP * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Examples
        ex_title = Text("Examples of entire functions:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        self.ly.center_in_content(ex_title)
        self.play(Write(ex_title), run_time=FAST)
        self.wait(1)

        examples = [
            MathTex(r"p(z) = a_n z^n + \cdots + a_1 z + a_0", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"e^z, \;\sin(z), \;\cos(z)", font_size=BODY_SIZE, color=SECONDARY),
        ]
        self.ly.progressive_reveal(examples, start_from=ex_title)
        self.wait(3)

        self.ly.clear()

        # Miracle of complex analysis
        miracle_title = Text(
            "The Miracle of Complex Analysis:",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.center_in_content(miracle_title)
        self.play(Write(miracle_title), run_time=NORMAL)
        self.wait(2)

        properties = [
            MathTex(
                r"\text{Holomorphic} \;\Longrightarrow\; \text{infinitely differentiable}",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"\text{Holomorphic} \;\Longrightarrow\; \text{analytic (Taylor series)}",
                font_size=BODY_SIZE, color=SECONDARY,
            ),
            MathTex(
                r"\text{Holomorphic} \;\Longrightarrow\; \text{Cauchy's integral formula}",
                font_size=BODY_SIZE, color=ACCENT,
            ),
        ]
        self.ly.progressive_reveal(properties, start_from=miracle_title)
        self.wait(5)

        self.ly.clear()

    # --- Scene 9: Summary and Road Ahead
    # Narration ~35s. Elements: summary, teaser, outro

    def scene9_summary(self):
        self.add_subcaption(
            "Today we learned about complex differentiation. The key "
            "ideas are: the complex derivative has the same formula as "
            "the real derivative, but h approaches zero from all "
            "directions, making it vastly more restrictive. The "
            "Cauchy-Riemann equations are the necessary and sufficient "
            "condition for differentiability. Polynomials and e to the z "
            "are holomorphic everywhere, while z-bar is differentiable "
            "nowhere. In the next video, we will explore complex "
            "integration and Cauchy's theorem. Thank you for watching!",
            duration=44,
        )

        summary_items = [
            Text("Complex derivative = same formula, much stronger", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("C-R equations: du/dx = dv/dy, du/dy = -dv/dx", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Polynomials, e^z, sin(z), cos(z) are entire", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("z-bar: continuous everywhere, differentiable nowhere", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Next: Complex Integration & Cauchy's Theorem", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(summary_items)
        self.wait(5)

        self.ly.clear()

        play_outro(self, "Complex Integration", "Complex Analysis")
