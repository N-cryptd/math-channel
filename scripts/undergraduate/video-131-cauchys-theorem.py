"""
Video 131: Cauchy's Theorem -- Complex Analysis
TEMPLATE v2 -- Professional quality Manim script

Playlist: Complex Analysis (Video 8 of 13)
Class: Video131_CauchysTheorem

Topics: Cauchy's Theorem (Cauchy-Goursat), holomorphic functions, closed contour
         integrals, proof via Green's theorem + Cauchy-Riemann equations,
         simply-connected domains, path independence,
         example f(z)=z^2 around unit circle,
         counterexample f(z)=1/z showing the simply-connected condition matters.

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


class Video131_CauchysTheorem(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_simply_connected()
        self.scene3_theorem_statement()
        self.scene4_green_theorem_intuition()
        self.scene5_cr_proof()
        self.scene6_geometric_picture()
        self.scene7_counterexample()
        self.scene8_summary()

    # --- Scene 1: Hook -- "The Most Surprising Result in Complex Analysis" ~46s
    # Narration ~46s. Elements: contour, integral=0, contrast, intro

    def scene1_hook(self):
        self.add_subcaption(
            "In the last video we computed contour integrals and found that "
            "polynomials integrated around closed paths give zero. What if I "
            "told you this is not just true for polynomials, but for every "
            "single analytic function? This is Cauchy's theorem, the most "
            "important result in all of complex analysis. This is Video 8 "
            "of Complex Analysis.",
            duration=46,
        )
        play_intro(self, "Cauchy's Theorem", "Complex Analysis")

        # Visual: a squiggly closed contour
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=5, y_length=3.5,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.5)

        # Squiggly closed contour
        t_arr = np.linspace(0, 2 * np.pi, 120)
        contour_pts = [
            plane.c2p(
                1.5 * np.cos(t) + 0.3 * np.sin(3 * t),
                1.0 * np.sin(t) + 0.2 * np.cos(2 * t),
            )
            for t in t_arr
        ]
        contour = VMobject()
        contour.set_points_smoothly(contour_pts)
        contour.set_color(SECONDARY)
        contour.set_stroke(width=2.5)

        self.play(Create(contour), run_time=NORMAL)
        self.wait(1)

        gamma_lbl = MathTex(r"\gamma", font_size=LABEL_SIZE, color=SECONDARY)
        gamma_lbl.next_to(contour.get_top(), RIGHT, buff=0.15)
        self.play(Write(gamma_lbl), run_time=FAST)
        self.wait(2)

        self.ly.clear()

        # The claim
        claim = MathTex(
            r"\oint_\gamma z^2 \, dz = 0",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(claim)
        self.play(Write(claim), run_time=NORMAL)
        self.wait(3)

        claim_note = Text(
            "z^2 is entire -- holomorphic everywhere in C",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(claim_note, DOWN, anchor=claim, buff=0.5)
        self.play(FadeIn(claim_note, shift=UP * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Contrast with real case
        contrast = Text(
            "In real calculus, closed-path integrals are rarely zero",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.center_in_content(contrast)
        self.play(FadeIn(contrast, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: Simply-Connected Domains ~55s
    # Narration ~55s. Elements: simply-connected region, shrinking contour,
    #             multiply-connected domain (annulus with hole)

    def scene2_simply_connected(self):
        self.add_subcaption(
            "Before stating the theorem, we need one key concept. A domain "
            "D in the complex plane is simply connected if every closed curve "
            "inside D can be continuously shrunk to a point without leaving D. "
            "Think of a disk or a rectangle. Any loop inside can shrink "
            "down to nothing. But an annulus, a region with a hole, is not "
            "simply connected. A loop encircling the hole cannot shrink "
            "past it. This distinction matters enormously for Cauchy's theorem.",
            duration=55,
        )
        self.ly.section_divider(1, "Simply-Connected Domains")

        # Visual: simply-connected domain with shrinking contour
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=5, y_length=3.5,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.5)

        # Filled domain
        domain = Circle(radius=1.5, color=SECONDARY, fill_opacity=0.12, stroke_width=2)
        domain.move_to(plane.c2p(0, 0))
        self.play(Create(domain), run_time=FAST)
        self.wait(1)

        # Contour inside domain
        t_arr = np.linspace(0, 2 * np.pi, 80)
        c_pts = [
            plane.c2p(0.8 * np.cos(t), 0.5 * np.sin(t))
            for t in t_arr
        ]
        c1 = VMobject()
        c1.set_points_smoothly(c_pts)
        c1.set_color(ACCENT)
        c1.set_stroke(width=2.5)

        self.play(Create(c1), run_time=FAST)
        self.wait(1)

        sc_label = Text(
            "Simply connected: loop shrinks to a point",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(sc_label, DOWN, anchor=plane, buff=0.3)
        self.play(FadeIn(sc_label, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

        # Multiply-connected: annulus with hole
        plane2 = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=5, y_length=3.5,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane2)
        self.play(Create(plane2), run_time=FAST)
        self.wait(0.5)

        outer = Circle(radius=1.8, color=SECONDARY, fill_opacity=0.08, stroke_width=2)
        outer.move_to(plane2.c2p(0, 0))
        self.play(Create(outer), run_time=FAST)
        self.wait(0.5)

        # Hole at origin
        hole = Circle(radius=0.4, color=RED, fill_opacity=0.3, stroke_width=2)
        hole.move_to(plane2.c2p(0, 0))
        self.play(FadeIn(hole), run_time=FAST)
        self.wait(1)

        # Contour encircling the hole
        t_arr2 = np.linspace(0, 2 * np.pi, 80)
        c2_pts = [
            plane2.c2p(1.0 * np.cos(t), 0.7 * np.sin(t))
            for t in t_arr2
        ]
        c2 = VMobject()
        c2.set_points_smoothly(c2_pts)
        c2.set_color(ACCENT)
        c2.set_stroke(width=2.5)

        self.play(Create(c2), run_time=FAST)
        self.wait(1)

        mc_label = Text(
            "Not simply connected: loop cannot cross the hole",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(mc_label, DOWN, anchor=plane2, buff=0.3)
        self.play(FadeIn(mc_label, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 3: The Theorem Statement ~50s
    # Narration ~50s. Elements: theorem box, three conditions

    def scene3_theorem_statement(self):
        self.add_subcaption(
            "Now for the theorem. Cauchy's theorem, also called the "
            "Cauchy-Goursat theorem, states that if f is holomorphic on "
            "and inside a simple closed contour gamma in a simply connected "
            "domain, then the integral of f of z dz around gamma equals zero. "
            "There are three ingredients. First, f must be holomorphic "
            "everywhere inside the contour. Second, the contour must be a "
            "simple closed curve. Third, the domain must be simply connected.",
            duration=55,
        )
        self.ly.section_divider(2, "The Theorem Statement")

        # Theorem in a box
        theorem = MathTex(
            r"f \text{ holomorphic on and inside } \gamma",
            r"\;\Longrightarrow\;",
            r"\oint_\gamma f(z)\,dz = 0",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, DIM, ACCENT]):
            if i < len(theorem):
                theorem[i].set_color(col)
        box = self.ly.formula_box(theorem, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Conditions
        cond_title = Text(
            "Three ingredients:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(cond_title)
        self.play(Write(cond_title), run_time=FAST)
        self.wait(1)

        conditions = [
            Text("1. f holomorphic everywhere on and inside gamma", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. gamma is a simple closed curve", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3. Domain is simply connected", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(conditions, start_from=cond_title)
        self.wait(5)

        self.ly.clear()

    # --- Scene 4: Intuition via Green's Theorem ~65s
    # Narration ~65s. Elements: f=u+iv, dz=dx+idy, expanded form,
    #             Green's theorem recap, connection insight

    def scene4_green_theorem_intuition(self):
        self.add_subcaption(
            "Why should this be true? Write f of z as u plus i v, and "
            "dz as dx plus i dy. Multiplying out, f dz equals u dx minus "
            "v dy, plus i times v dx plus u dy. This is a sum of two real "
            "line integrals. Each one looks exactly like the kind of "
            "integral that appears in Green's theorem. Green's theorem "
            "converts a line integral around a closed curve into a double "
            "integral over the enclosed region. And the Cauchy-Riemann "
            "equations will make both double integrals vanish. Let me show you.",
            duration=70,
        )
        self.ly.section_divider(3, "The Intuition: Green's Theorem")

        # Step 1: f = u + iv
        step1 = MathTex(
            r"f(z) = u(x,y) + i\, v(x,y)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(step1)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(3)

        # Step 2: dz = dx + i dy
        step2 = MathTex(
            r"dz = dx + i\, dy",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step2, DOWN, anchor=step1, buff=0.5)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Step 3: Multiply out
        product = MathTex(
            r"f(z)\,dz",
            r"= (u + iv)(dx + i\,dy)",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([ACCENT, WHITE]):
            if i < len(product):
                product[i].set_color(col)
        self.ly.center_in_content(product)
        self.play(Write(product), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Step 4: Expanded form
        expanded = MathTex(
            r"= (u\,dx - v\,dy) + i\,(v\,dx + u\,dy)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(expanded)
        self.play(Write(expanded), run_time=NORMAL)
        self.wait(3)

        # Green's theorem reminder
        green = MathTex(
            r"\oint_C P\,dx + Q\,dy = \iint_D \!\left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(green, DOWN, anchor=expanded, buff=0.5)
        self.play(Write(green), run_time=NORMAL)
        self.wait(3)

        insight = Text(
            "Two real line integrals -- perfect for Green's theorem!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=green, buff=0.4)
        self.play(FadeIn(insight, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 5: CR Proof Sketch ~65s
    # Narration ~65s. Elements: CR equations, real part cancellation,
    #             imaginary part cancellation, zero result

    def scene5_cr_proof(self):
        self.add_subcaption(
            "Here is the proof sketch. Take the real part of the "
            "integral, u dx minus v dy. By Green's theorem, this equals "
            "the double integral over the region of partial v over partial "
            "x minus partial u over partial y, with a minus sign, times dA. "
            "But the Cauchy-Riemann equations tell us that partial u over "
            "partial y equals negative partial v over partial x. So the "
            "integrand becomes negative v sub x minus negative v sub x, "
            "which is zero. The exact same cancellation happens for the "
            "imaginary part. Both real and imaginary parts vanish, so "
            "the entire integral is zero.",
            duration=70,
        )
        self.ly.section_divider(4, "The C-R Equations Make It Vanish")

        # CR equations reminder
        cr = MathTex(
            r"\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}",
            r",\qquad",
            r"\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}",
            font_size=BODY_SIZE,
        )
        for i, col in enumerate([PRIMARY, DIM, SECONDARY]):
            if i < len(cr):
                cr[i].set_color(col)
        self.ly.center_in_content(cr)
        self.play(Write(cr), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Real part: P = u, Q = -v
        rp_title = Text(
            "Real part: P = u, Q = -v",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.center_in_content(rp_title)
        self.play(FadeIn(rp_title, shift=UP * 0.15), run_time=FAST)
        self.wait(1)

        rp_step = MathTex(
            r"\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}"
            r"= -\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}"
            r"= -\frac{\partial v}{\partial x} + \frac{\partial v}{\partial x} = 0",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(rp_step, DOWN, anchor=rp_title, buff=0.5)
        ensure_fits(rp_step)
        clamp_position(rp_step)
        self.play(Write(rp_step), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Imaginary part: P = v, Q = u
        ip_title = Text(
            "Imaginary part: P = v, Q = u",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.center_in_content(ip_title)
        self.play(FadeIn(ip_title, shift=UP * 0.15), run_time=FAST)
        self.wait(1)

        ip_step = MathTex(
            r"\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}"
            r"= \frac{\partial u}{\partial x} - \frac{\partial v}{\partial y}"
            r"= \frac{\partial u}{\partial x} - \frac{\partial u}{\partial x} = 0",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(ip_step, DOWN, anchor=ip_title, buff=0.5)
        ensure_fits(ip_step)
        clamp_position(ip_step)
        self.play(Write(ip_step), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Result
        result = MathTex(
            r"\oint_\gamma f(z)\,dz = 0 + i\cdot 0 = 0",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        box = self.ly.formula_box(result, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 6: Geometric Picture -- Path Independence ~55s
    # Narration ~55s. Elements: two paths sharing endpoints, closed loop
    #             integral zero, path independence statement

    def scene6_geometric_picture(self):
        self.add_subcaption(
            "Cauchy's theorem has a beautiful geometric consequence. "
            "If f is holomorphic, then the integral between two points "
            "does not depend on the path. Take any two paths gamma one "
            "and gamma two from z one to z two. Together they form a "
            "closed loop. By Cauchy's theorem the integral around this "
            "loop is zero. That means the integral along gamma one equals "
            "the integral along gamma two. The path doesn't matter. "
            "This is path independence, and it means antiderivatives "
            "exist for analytic functions.",
            duration=60,
        )
        self.ly.section_divider(5, "Path Independence")

        # Visual: two paths sharing endpoints on a plane
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=5, y_length=3.5,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.5)

        # Two paths from z1 to z2
        z1_pos = plane.c2p(-1.5, -0.5)
        z2_pos = plane.c2p(1.5, 0.5)

        # Path 1: upper arc
        t_arr = np.linspace(0, 1, 80)
        path1_pts = [
            plane.c2p(
                -1.5 + 3.0 * t,
                -0.5 + 1.0 * np.sin(np.pi * t) + 1.0 * t,
            )
            for t in t_arr
        ]
        path1 = VMobject()
        path1.set_points_smoothly(path1_pts)
        path1.set_color(SECONDARY)
        path1.set_stroke(width=2.5)

        # Path 2: lower arc
        path2_pts = [
            plane.c2p(
                -1.5 + 3.0 * t,
                -0.5 - 0.8 * np.sin(np.pi * t) + 1.0 * t,
            )
            for t in t_arr
        ]
        path2 = VMobject()
        path2.set_points_smoothly(path2_pts)
        path2.set_color(ACCENT)
        path2.set_stroke(width=2.5)

        self.play(Create(path1), run_time=NORMAL)
        self.wait(0.5)
        self.play(Create(path2), run_time=NORMAL)
        self.wait(1)

        # Labels for z1, z2
        z1_lbl = MathTex(r"z_1", font_size=LABEL_SIZE, color=WHITE)
        z1_lbl.next_to(z1_pos, DOWN, buff=0.15)
        z2_lbl = MathTex(r"z_2", font_size=LABEL_SIZE, color=WHITE)
        z2_lbl.next_to(z2_pos, UP, buff=0.15)
        g1_lbl = MathTex(r"\gamma_1", font_size=LABEL_SIZE, color=SECONDARY)
        g1_lbl.next_to(path1.get_top(), LEFT, buff=0.15)
        g2_lbl = MathTex(r"\gamma_2", font_size=LABEL_SIZE, color=ACCENT)
        g2_lbl.next_to(path2.get_bottom(), LEFT, buff=0.15)

        self.play(
            Write(z1_lbl), Write(z2_lbl),
            Write(g1_lbl), Write(g2_lbl),
            run_time=FAST,
        )
        self.wait(3)

        self.ly.clear()

        # Key formula
        key = MathTex(
            r"\int_{\gamma_1} f(z)\,dz = \int_{\gamma_2} f(z)\,dz",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(key)
        self.play(Write(key), run_time=NORMAL)
        self.wait(3)

        note = Text(
            "Path independence: the integral only depends on endpoints",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=key, buff=0.5)
        self.play(FadeIn(note, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 7: Counterexample -- f(z) = 1/z ~60s
    # Narration ~60s. Elements: unit circle contour, computation,
    #             hole visualization, integral = 2*pi*i

    def scene7_counterexample(self):
        self.add_subcaption(
            "But what happens without simply connectedness? Consider "
            "f of z equals one over z. This is holomorphic everywhere "
            "except at z equals zero. The domain C minus zero is not "
            "simply connected because of the hole at the origin. Let's "
            "integrate around the unit circle. Parameterize gamma of t "
            "equals e to the i t. Then dz equals i e to the i t dt. "
            "Substituting, the integrand is one over e to the i t times "
            "i e to the i t dt, which simplifies to i dt. The integral "
            "from zero to two pi of i dt is two pi i. Not zero!",
            duration=65,
        )
        self.ly.section_divider(6, "Counterexample: f(z) = 1/z")

        # Plane with unit circle
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=5, y_length=3.5,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.5)

        # Unit circle
        unit_circle = Circle(radius=1.0, color=SECONDARY, stroke_width=2.5)
        unit_circle.move_to(plane.c2p(0, 0))
        self.play(Create(unit_circle), run_time=NORMAL)
        self.wait(0.5)

        # Hole at origin
        hole = Circle(radius=0.15, color=RED, fill_opacity=0.6, stroke_width=0)
        hole.move_to(plane.c2p(0, 0))
        self.play(FadeIn(hole), run_time=FAST)
        self.wait(1)

        # Labels
        gamma_lbl = MathTex(r"\gamma", font_size=LABEL_SIZE, color=SECONDARY)
        gamma_lbl.next_to(unit_circle.get_right(), UR, buff=0.15)
        hole_lbl = MathTex(r"z=0", font_size=LABEL_SIZE, color=RED)
        hole_lbl.next_to(hole, DOWN, buff=0.15)
        self.play(Write(gamma_lbl), Write(hole_lbl), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # f(z) = 1/z and the computation
        func = MathTex(r"f(z) = \frac{1}{z}", font_size=HEADING_SIZE, color=WHITE)
        self.ly.center_in_content(func)
        self.play(Write(func), run_time=NORMAL)
        self.wait(2)

        param = MathTex(
            r"\gamma(t) = e^{it}, \quad dz = i\,e^{it}\,dt",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(param, DOWN, anchor=func, buff=0.5)
        self.play(Write(param), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # The computation
        comp = MathTex(
            r"\oint_\gamma \frac{1}{z}\,dz",
            r"= \int_0^{2\pi} \frac{1}{e^{it}} \cdot i\,e^{it}\,dt",
            r"= \int_0^{2\pi} i\,dt",
            r"= 2\pi i",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, DIM, PRIMARY, RED]):
            if i < len(comp):
                comp[i].set_color(col)
        self.ly.center_in_content(comp)
        self.play(Write(comp), run_time=NORMAL)
        self.wait(5)

        why = Text(
            "Not zero! The singularity at z=0 breaks simply-connectedness",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(why, DOWN, anchor=comp, buff=0.5)
        self.play(FadeIn(why, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 8: Summary ~45s
    # Narration ~45s. Elements: recap points, key formula, outro

    def scene8_summary(self):
        self.add_subcaption(
            "Let's recap what we covered. Cauchy's theorem says that if f "
            "is holomorphic on and inside a simple closed contour in a "
            "simply connected domain, the contour integral is zero. The "
            "proof comes from Green's theorem and the Cauchy-Riemann "
            "equations. This gives us path independence, meaning "
            "antiderivatives exist. And the simply-connected condition is "
            "essential, as one over z around the unit circle shows. "
            "Next time we will see Cauchy's integral formula, which uses "
            "this theorem as its foundation.",
            duration=55,
        )
        self.ly.section_divider(7, "Summary")

        title = self.ly.title("Key Takeaways")
        self.wait(1)

        points = [
            Text("Holomorphic + simply connected => integral = 0", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Proof: Green's theorem + Cauchy-Riemann equations", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Path independence follows directly", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Simply-connectedness is essential (1/z counterexample)", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        self.wait(3)

        self.ly.clear()

        # Final formula
        final = MathTex(
            r"\oint_\gamma f(z)\,dz = 0",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        box = self.ly.formula_box(final, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()
        play_outro(self, "Cauchy's Integral Formula", "Complex Analysis")