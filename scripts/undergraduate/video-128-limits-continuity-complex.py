"""
Video 128: Limits and Continuity in C — Complex Analysis
TEMPLATE v2 -- Professional quality Manim script

Playlist: Complex Analysis (Video 3 of 13)
Class: Video128_LimitsContinuityComplex

Topics: complex limits, epsilon-delta definition for C, approach paths,
         counter-example (conjugate/z), continuity in C, component-wise
         continuity, continuous functions (polynomials, e^z, rational),
         complex sequences and series convergence.

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


class Video128_LimitsContinuityComplex(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_approach_paths()
        self.scene4_counterexample()
        self.scene5_continuity()
        self.scene6_examples()
        self.scene7_sequences()
        self.scene8_summary()

    # --- Scene 1: Hook --- "What Does 'Close' Mean in the Complex Plane?"
    # Narration ~40s. Elements: real limit, question, complex plane with paths

    def scene1_hook(self):
        self.add_subcaption(
            "In calculus, the limit of f of x as x approaches a equals L means "
            "the function value gets close to L when x is close to a. On the "
            "real line, x can only approach a from two directions: the left "
            "and the right. But in the complex plane, there are infinitely "
            "many directions to approach a point. A path from the real axis, "
            "a path from the imaginary axis, or a spiral path, all converging "
            "to the same point. This makes complex limits both richer and "
            "more subtle. This is Complex Analysis, Video 3.",
            duration=42,
        )
        play_intro(self, "Limits and Continuity in C", "Complex Analysis")

        title = self.ly.title("What Does \"Close\" Mean in C?")
        self.wait(2)

        # Real limit reminder
        real_note = Text(
            "On R: x approaches a from LEFT and RIGHT only",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.progressive_reveal([real_note], start_from=title)
        self.wait(3)

        self.ly.clear()

        # Complex plane with paths
        question = Text(
            "In C: infinitely many approach directions!",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.center_in_content(question)
        self.play(Write(question), run_time=NORMAL)
        self.wait(2)

        # Draw approach paths
        plane = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=5,
            y_length=4,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.safe_place(plane, DOWN, anchor=question, buff=0.5)
        self.play(Create(plane), run_time=FAST)
        self.wait(1)

        # Central point z0
        z0_dot = Dot(plane.c2p(0, 0), color=ACCENT, radius=0.08)
        z0_lbl = MathTex(r"z_0", font_size=LABEL_SIZE, color=ACCENT)
        z0_lbl.next_to(z0_dot, DOWN, buff=0.15)
        self.play(FadeIn(z0_dot), Write(z0_lbl), run_time=FAST)
        self.wait(1)

        # Draw 3 approach paths
        paths = []
        colors = [PRIMARY, SECONDARY, RED]
        angles = [0, np.pi / 2, np.pi / 4]
        for col, angle in zip(colors, angles):
            pts = [
                plane.c2p(2 * np.cos(angle), 2 * np.sin(angle)),
                plane.c2p(0.3 * np.cos(angle), 0.3 * np.sin(angle)),
            ]
            line = Line(pts[0], pts[1], color=col, stroke_width=2.5)
            line.add_tip(tip_length=0.15)
            paths.append(line)
        self.play(*[Create(p) for p in paths], run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: Complex Limits — Definition
    # Narration ~50s. Elements: epsilon-delta formula, delta disk, epsilon disk, mapping

    def scene2_definition(self):
        self.add_subcaption(
            "The formal definition of a complex limit mirrors the epsilon-delta "
            "definition from real analysis. We say the limit of f of z as z "
            "approaches z zero equals L if for every epsilon greater than zero, "
            "there exists a delta greater than zero such that whenever the "
            "distance from z to z zero is less than delta, the distance from "
            "f of z to L is less than epsilon. Visually, we have a delta disk "
            "around z zero in the z-plane, and the function maps this entire "
            "disk inside the epsilon disk around L in the w-plane.",
            duration=48,
        )
        self.ly.section_divider(1, "The Formal Definition")

        # Main epsilon-delta definition
        lim_def = MathTex(
            r"\lim_{z \to z_0} f(z) = L",
            font_size=HEADING_SIZE,
            color=ACCENT,
        )
        self.ly.center_in_content(lim_def)
        self.play(Write(lim_def), run_time=NORMAL)
        self.wait(2)

        # Epsilon-delta statement
        ed_stmt = MathTex(
            r"\forall\, \varepsilon > 0,\; \exists\, \delta > 0 :",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(ed_stmt, DOWN, anchor=lim_def, buff=0.5)
        self.play(Write(ed_stmt), run_time=NORMAL)
        self.wait(2)

        ed_impl = MathTex(
            r"|z - z_0| < \delta \;\Longrightarrow\; |f(z) - L| < \varepsilon",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(ed_impl, DOWN, anchor=ed_stmt, buff=0.4)
        self.play(Write(ed_impl), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Visual: two planes with disks
        self.add_subcaption(
            "Think of it this way: in the z-plane, draw a tiny disk of radius "
            "delta around z zero. In the w-plane, draw a tiny disk of radius "
            "epsilon around L. The function f must map every point in the "
            "delta disk to a point inside the epsilon disk. This is exactly the "
            "same definition as for functions from R squared to R squared, "
            "because C is topologically the same as R squared.",
            duration=30,
        )

        z_title = Text("z-plane", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        w_title = Text("w-plane", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        left_vg, right_vg = self.ly.two_columns([z_title], [w_title])

        z_pl = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-2.5, 2.5, 1],
            x_length=4.5, y_length=3.5,
            axis_config={"include_numbers": False}, color=PRIMARY,
        )
        w_pl = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-2.5, 2.5, 1],
            x_length=4.5, y_length=3.5,
            axis_config={"include_numbers": False}, color=SECONDARY,
        )
        z_pl.move_to(left_vg.get_center() + DOWN * 0.8)
        w_pl.move_to(right_vg.get_center() + DOWN * 0.8)
        clamp_position(z_pl)
        clamp_position(w_pl)

        self.play(Create(z_pl), Create(w_pl), run_time=FAST)
        self.wait(1)

        # Delta disk on z-plane
        delta_disk = Circle(
            radius=0.8, color=ACCENT, stroke_width=2,
        ).move_to(z_pl.c2p(0, 0))
        delta_lbl = MathTex(r"\delta", font_size=SMALL_SIZE, color=ACCENT)
        delta_lbl.next_to(delta_disk, UP, buff=0.1)
        self.play(Create(delta_disk), Write(delta_lbl), run_time=FAST)
        self.wait(1)

        # Epsilon disk on w-plane
        eps_disk = Circle(
            radius=0.8, color=ACCENT, stroke_width=2,
        ).move_to(w_pl.c2p(1.5, 1))
        eps_lbl = MathTex(r"\varepsilon", font_size=SMALL_SIZE, color=ACCENT)
        eps_lbl.next_to(eps_disk, UP, buff=0.1)
        L_dot = Dot(w_pl.c2p(1.5, 1), color=RED, radius=0.07)
        L_lbl = MathTex(r"L", font_size=SMALL_SIZE, color=RED)
        L_lbl.next_to(L_dot, DOWN, buff=0.1)
        self.play(Create(eps_disk), Write(eps_lbl), FadeIn(L_dot), Write(L_lbl), run_time=FAST)
        self.wait(2)

        # z0 label on z-plane
        z0 = Dot(z_pl.c2p(0, 0), color=RED, radius=0.07)
        z0_l = MathTex(r"z_0", font_size=SMALL_SIZE, color=RED)
        z0_l.next_to(z0, DOWN, buff=0.1)
        self.play(FadeIn(z0), Write(z0_l), run_time=FAST)
        self.wait(3)

        self.ly.clear()

    # --- Scene 3: Approach Paths — Why Complex Limits Are Harder
    # Narration ~48s. Elements: plane, 3-4 paths, labels

    def scene3_approach_paths(self):
        self.add_subcaption(
            "In real analysis, to check a limit at x equals a, you only need "
            "to verify two directions: from the left and from the right. If "
            "both one-sided limits agree, the two-sided limit exists. But in "
            "the complex plane, z can approach z zero along infinitely many "
            "paths. A straight line from any angle, a spiral, a parabolic "
            "curve, or any continuous path. For the limit to exist, the "
            "function must approach the same value L along every single path. "
            "If even two paths disagree, the limit does not exist.",
            duration=44,
        )
        self.ly.section_divider(2, "Approach Paths")

        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-2.5, 2.5, 1],
            x_length=5, y_length=4,
            axis_config={"include_numbers": False}, color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(1)

        z0 = Dot(plane.c2p(0, 0), color=ACCENT, radius=0.08)
        z0_lbl = MathTex(r"z_0", font_size=LABEL_SIZE, color=ACCENT)
        z0_lbl.next_to(z0, DOWN, buff=0.15)
        self.play(FadeIn(z0), Write(z0_lbl), run_time=FAST)
        self.wait(1)

        # Multiple approach paths with arrows
        path_data = [
            (r"\text{real axis}", 0, PRIMARY),
            (r"\text{imag axis}", np.pi / 2, SECONDARY),
            (r"\text{diagonal}", np.pi / 4, RED),
            (r"\text{spiral}", None, DIM),
        ]
        for label_text, angle, col in path_data:
            if angle is not None:
                start = plane.c2p(2.2 * np.cos(angle), 2.2 * np.sin(angle))
                end = plane.c2p(0.3 * np.cos(angle), 0.3 * np.sin(angle))
                line = Line(start, end, color=col, stroke_width=2.5)
                line.add_tip(tip_length=0.15)
            else:
                # Spiral path
                pts = []
                for t in np.linspace(0, 3 * np.pi, 60):
                    r = 0.2 + 0.6 * t / (3 * np.pi)
                    pts.append(plane.c2p(r * np.cos(t), r * np.sin(t)))
                line = VMobject(color=col, stroke_width=2)
                line.set_points_smoothly(pts)

            lbl = MathTex(label_text, font_size=SMALL_SIZE, color=col)
            if angle is not None:
                lbl.next_to(line.get_start(), UR if angle < np.pi else UL, buff=0.1)
            else:
                lbl.next_to(line.get_start(), RIGHT, buff=0.1)

            self.play(Create(line), Write(lbl), run_time=FAST)
            self.wait(1.5)

        # Key insight
        insight = MathTex(
            r"\text{ALL paths must agree} \;\Rightarrow\; \lim \text{ exists}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(insight, DOWN, anchor=plane, buff=0.3)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 4: Limit Does Not Exist — Counter-Example
    # Narration ~45s. Elements: function, two paths, different results, Red X

    def scene4_counterexample(self):
        self.add_subcaption(
            "Let's see an example where the limit does not exist. Consider "
            "f of z equals z-bar over z, where z-bar is the complex conjugate. "
            "We examine the limit as z approaches zero. Along the real axis, "
            "z equals x, so z-bar over z equals x over x, which equals 1. "
            "Along the imaginary axis, z equals iy, so z-bar over z equals "
            "negative iy over iy, which equals negative 1. Since different "
            "paths give different values, the limit does not exist.",
            duration=40,
        )
        self.ly.section_divider(3, "When Limits Don't Exist")

        # Function
        func = MathTex(
            r"f(z) = \frac{\overline{z}}{z}", r"\qquad",
            r"\lim_{z \to 0} f(z) \stackrel{?}{=}",
            font_size=HEADING_SIZE,
        )
        func[0].set_color(WHITE)
        func[2].set_color(RED)
        self.ly.center_in_content(func)
        self.play(Write(func), run_time=NORMAL)
        self.wait(2)

        # Two path results
        self.ly.clear()

        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-2.5, 2.5, 1],
            x_length=5, y_length=3.5,
            axis_config={"include_numbers": False}, color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(1)

        # Real axis path
        real_path = Line(
            plane.c2p(2, 0), plane.c2p(0.3, 0),
            color=PRIMARY, stroke_width=2.5,
        )
        real_path.add_tip(tip_length=0.15)
        real_res = MathTex(
            r"z = x:\quad \frac{\overline{x}}{x} = 1",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        real_res.next_to(plane, UP, buff=0.3)
        self.play(Create(real_path), Write(real_res), run_time=FAST)
        self.wait(2)

        # Imaginary axis path
        imag_path = Line(
            plane.c2p(0, 2), plane.c2p(0, 0.3),
            color=SECONDARY, stroke_width=2.5,
        )
        imag_path.add_tip(tip_length=0.15)
        imag_res = MathTex(
            r"z = iy:\quad \frac{-iy}{iy} = -1",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(imag_res, DOWN, anchor=real_res, buff=0.15)
        self.play(Create(imag_path), Write(imag_res), run_time=FAST)
        self.wait(2)

        # Does not exist verdict
        dne = MathTex(
            r"1 \neq -1 \;\Longrightarrow\; \lim_{z \to 0} \frac{\overline{z}}{z}",
            r"\text{ DNE}",
            font_size=HEADING_SIZE,
        )
        dne[0].set_color(RED)
        dne[1].set_color(RED)
        self.ly.safe_place(dne, DOWN, anchor=plane, buff=0.3)
        self.play(Write(dne), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 5: Continuity in C
    # Narration ~45s. Elements: definition, 3 perspectives, visual

    def scene5_continuity(self):
        self.add_subcaption(
            "A complex function f is continuous at z zero if the limit of "
            "f of z as z approaches z zero equals f of z zero. This means "
            "the function value matches what the limit predicts, with no "
            "jump or discontinuity. There are three equivalent ways to think "
            "about this. First, the epsilon-delta definition. Second, the "
            "sequential definition: if z sub n converges to z zero, then "
            "f of z sub n converges to f of z zero. Third, the component "
            "view: f equals u plus i v is continuous if and only if both "
            "u of x comma y and v of x comma y are continuous as real "
            "functions of two variables.",
            duration=46,
        )
        self.ly.section_divider(4, "Continuity in the Complex Plane")

        # Definition
        cont_def = MathTex(
            r"f \text{ continuous at } z_0 \;\Longleftrightarrow\;",
            font_size=BODY_SIZE, color=WHITE,
        )
        cont_eq = MathTex(
            r"\lim_{z \to z_0} f(z) = f(z_0)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(cont_def)
        self.play(Write(cont_def), run_time=NORMAL)
        self.wait(1)
        self.ly.safe_place(cont_eq, DOWN, anchor=cont_def, buff=0.4)
        self.play(Write(cont_eq), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Three perspectives
        perps = [
            Text("1. Epsilon-delta: directly from definition", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Sequential: z_n → z₀ ⟹ f(z_n) → f(z₀)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Component: u, v both continuous", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(perps)
        self.wait(3)

        self.ly.clear()

        # Component-wise insight
        comp = MathTex(
            r"f(z) = u(x,y) + i\,v(x,y)",
            r"\quad\text{continuous} \Longleftrightarrow",
            r"\begin{cases} u(x,y) \text{ cont.} \\ v(x,y) \text{ cont.} \end{cases}",
            font_size=HEADING_SIZE,
        )
        comp[0].set_color(PRIMARY)
        comp[1].set_color(DIM)
        comp[2].set_color(WHITE)
        self.ly.center_in_content(comp)
        self.play(Write(comp), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # --- Scene 6: Examples of Continuous Functions
    # Narration ~45s. Elements: polynomial, punctured plane, continuity domain

    def scene6_examples(self):
        self.add_subcaption(
            "Let's look at which functions are continuous in the complex plane. "
            "Polynomials are continuous everywhere on C. For example, p of z "
            "equals z cubed plus 2z minus 1 is continuous for all z. The "
            "complex exponential e to the z is also continuous everywhere. "
            "Rational functions, like one over z, are continuous everywhere "
            "except at their poles. For one over z, the function is continuous "
            "on the punctured plane, that is, all of C except zero. At the "
            "pole, the function is undefined, so it cannot be continuous there.",
            duration=44,
        )
        self.ly.section_divider(5, "Continuous Functions in C")

        # Polynomials
        items = [
            Text("Polynomials: continuous everywhere on C", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            MathTex(r"p(z) = z^3 + 2z - 1", font_size=BODY_SIZE, color=PRIMARY),
            Text("e^z: continuous everywhere on C", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items)
        self.wait(3)

        self.ly.clear()

        # Rational functions
        rat_title = Text(
            "Rational functions: continuous except at poles",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.progressive_reveal([rat_title])
        self.wait(2)

        self.ly.clear()

        # Punctured plane visual
        punct_title = Text(
            "f(z) = 1/z: punctured plane C \\ {0}",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.center_in_content(punct_title)
        self.play(Write(punct_title), run_time=NORMAL)
        self.wait(2)

        plane = Axes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1],
            x_length=4, y_length=3.5,
            axis_config={"include_numbers": False}, color=PRIMARY,
        )
        self.ly.safe_place(plane, DOWN, anchor=punct_title, buff=0.4)
        self.play(Create(plane), run_time=FAST)
        self.wait(1)

        # Pole marker at origin
        pole_x = MathTex(r"\times", font_size=HEADING_SIZE, color=RED)
        pole_x.move_to(plane.c2p(0, 0))
        pole_txt = Text("pole", font_size=SMALL_SIZE, color=RED, font=MONO)
        pole_txt.next_to(pole_x, DOWN, buff=0.15)
        self.play(Write(pole_x), Write(pole_txt), run_time=FAST)
        self.wait(1)

        # Shaded region (everything except origin)
        cont_lbl = Text(
            "Continuous on C \\ {0}",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        cont_lbl.next_to(plane, RIGHT, buff=0.3)
        self.play(FadeIn(cont_lbl, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 7: Sequences and Series — Complex Version
    # Narration ~40s. Elements: sequence convergence, disk vs interval

    def scene7_sequences(self):
        self.add_subcaption(
            "Complex sequences converge just like real sequences, but in two "
            "dimensions. A sequence z sub n converges to z zero if the "
            "distance from z sub n to z zero approaches zero. This is "
            "exactly the same as convergence in R squared. But here is "
            "where complex analysis gets beautiful. In real analysis, a "
            "power series converges on an interval, like from negative R "
            "to R. In complex analysis, a power series converges on a "
            "disk, centered at some point with radius R. The radius of "
            "convergence is a genuine geometric disk, not just a "
            "one-dimensional interval. This geometric insight is at the "
            "heart of complex analysis.",
            duration=46,
        )
        self.ly.section_divider(6, "Sequences and Convergence in C")

        # Sequence definition
        seq_def = MathTex(
            r"z_n \to z_0 \;\Longleftrightarrow\; |z_n - z_0| \to 0",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(seq_def)
        self.play(Write(seq_def), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Disk vs interval comparison
        r_title = Text("Real: interval", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        c_title = Text("Complex: disk", font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        left_vg, right_vg = self.ly.two_columns([r_title], [c_title])

        # Real number line with interval
        real_line = NumberLine(
            x_range=[-3, 3, 1], length=4.5, color=PRIMARY,
        )
        real_line.move_to(left_vg.get_center() + DOWN * 1.0)
        clamp_position(real_line)
        # Highlighted interval on the number line
        int_start = real_line.n2p(-1.5)
        int_end = real_line.n2p(1.5)
        interval = Line(int_start, int_end, color=ACCENT, stroke_width=6)
        r_min_lbl = MathTex(r"-R", font_size=SMALL_SIZE, color=PRIMARY)
        r_max_lbl = MathTex(r"R", font_size=SMALL_SIZE, color=PRIMARY)
        r_min_lbl.next_to(real_line.n2p(-1.5), DOWN, buff=0.1)
        r_max_lbl.next_to(real_line.n2p(1.5), DOWN, buff=0.1)

        # Complex disk
        c_plane = Axes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1],
            x_length=4, y_length=3,
            axis_config={"include_numbers": False}, color=SECONDARY,
        )
        c_plane.move_to(right_vg.get_center() + DOWN * 1.0)
        clamp_position(c_plane)
        disk = Circle(radius=1.2, color=ACCENT, stroke_width=2).move_to(c_plane.get_center())

        self.play(
            Create(real_line), Create(interval),
            Write(r_min_lbl), Write(r_max_lbl),
            Create(c_plane), Create(disk),
            run_time=NORMAL,
        )
        self.wait(4)

        # Key insight
        insight = MathTex(
            r"\text{Radius of convergence } R: \text{ a DISK in } \mathbb{C}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(insight, DOWN, anchor=c_plane, buff=0.3)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 8: Summary and Road Ahead
    # Narration ~30s. Elements: summary, teaser, outro

    def scene8_summary(self):
        self.add_subcaption(
            "Today we learned about limits and continuity in the complex plane. "
            "The key ideas are: complex limits require convergence along all "
            "paths, not just two. The epsilon-delta definition looks just like "
            "R squared, because C and R squared are topologically the same. "
            "A function is continuous if its limit matches its value. "
            "Polynomials and e to the z are continuous everywhere. Rational "
            "functions are continuous except at poles. In the next video, we "
            "will explore complex differentiation, where the Cauchy-Riemann "
            "equations reveal that being differentiable in C is much "
            "stronger than in R. Thank you for watching!",
            duration=48,
        )

        summary_items = [
            Text("Complex limits need ALL-path agreement", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("C ≅ R²: same epsilon-delta definition", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Continuity = u(x,y), v(x,y) both continuous", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Polynomials, e^z continuous everywhere", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Next: Complex Differentiation & Cauchy-Riemann", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(summary_items)
        self.wait(5)

        self.ly.clear()

        play_outro(self, "Complex Differentiation", "Complex Analysis")
