"""
Video 127: Complex Functions — Introduction to Complex Analysis
TEMPLATE v2 -- Professional quality Manim script

Playlist: Complex Analysis (Video 2 of 13)
Class: Video127_ComplexFunctions

Topics: complex functions f: C->C, polynomials in C, rational functions,
         exponential function e^z, trigonometric functions sin(z), cos(z)
         as complex functions, visualizing complex functions
         (domain coloring, grid transformation).

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


class Video127_ComplexFunctions(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_polynomials()
        self.scene4_rational()
        self.scene5_exponential()
        self.scene6_trigonometric()
        self.scene7_visualization()
        self.scene8_summary()

    # --- Scene 1: Hook --- "From Real to Complex"
    # Narration ~40s. Elements: real graph, question text, complex plane, arrow

    def scene1_hook(self):
        self.add_subcaption(
            "In the last video, we revisited complex numbers. Now we ask: "
            "what happens when we build functions with complex numbers? "
            "A real function like f of x equals x squared takes a real "
            "input and gives a real output. But a complex function takes "
            "a complex input and gives a complex output. "
            "This is a mapping from a two-dimensional plane to another "
            "two-dimensional plane. Visualizing this is the challenge "
            "and the beauty of complex analysis. "
            "This is Complex Analysis, Video 2.",
            duration=40,
        )
        play_intro(self, "Complex Functions", "Complex Analysis")

        title = self.ly.title("From Real to Complex")
        self.wait(2)

        # Real function graph
        real_plane = Axes(
            x_range=[-2, 2, 1],
            y_range=[-1, 4, 1],
            x_length=4,
            y_length=3,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        real_label = Text("f(x) = x\u00b2", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        self.ly.center_in_content(real_plane)
        self.ly.safe_place(real_label, UP, anchor=real_plane, buff=0.4)
        self.play(Create(real_plane), run_time=FAST)
        self.wait(1)

        # Parabola curve
        curve_points = [real_plane.c2p(x, x**2) for x in np.linspace(-1.8, 1.8, 50)]
        parabola = VMobject(color=ACCENT, stroke_width=3)
        parabola.set_points_smoothly(curve_points)
        self.play(Create(parabola), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        # Question
        self.add_subcaption(
            "For a real function, the input is one-dimensional and the output "
            "is one-dimensional. But for a complex function, both input and "
            "output are two-dimensional. We need four dimensions to graph it! "
            "So how do we visualize complex functions?",
            duration=18,
        )
        question = Text(
            "What happens when the input is complex?",
            font_size=HEADING_SIZE,
            color=RED,
            font=SANS,
        )
        self.ly.center_in_content(question)
        self.play(Write(question), run_time=NORMAL)
        self.wait(3)

        # Transition to complex plane
        self.ly.clear()
        zplane = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=5,
            y_length=4,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(zplane)
        self.play(Create(zplane), run_time=FAST)
        self.wait(1)

        z_label = MathTex(r"z", font_size=BODY_SIZE, color=ACCENT)
        z_label.move_to(zplane.c2p(1, 1))
        self.play(Write(z_label), run_time=FAST)
        self.wait(1)

        w_label = MathTex(r"w = f(z)", font_size=BODY_SIZE, color=SECONDARY)
        self.ly.safe_place(w_label, UP, anchor=zplane, buff=0.4)
        self.play(Write(w_label), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # --- Scene 2: Complex Functions — Definition and Notation
    # Narration ~42s. Elements: definition, u+iv decomposition, z-plane, w-plane

    def scene2_definition(self):
        self.add_subcaption(
            "A complex function maps complex numbers to complex numbers. "
            "We write f from C to C, meaning the domain and codomain are "
            "both the complex numbers. If z equals x plus i y, then "
            "we can decompose f of z into its real and imaginary parts: "
            "f of z equals u of x comma y plus i v of x comma y. "
            "Here u and v are real-valued functions of two real variables. "
            "Every complex function is really two real functions in disguise. "
            "We call the input plane the z-plane and the output plane "
            "the w-plane.",
            duration=42,
        )
        self.ly.section_divider(1, "Complex Functions Defined")

        # Main definition
        func_def = MathTex(
            r"f \colon \mathbb{C} \to \mathbb{C}",
            font_size=HEADING_SIZE,
            color=ACCENT,
        )
        self.ly.center_in_content(func_def)
        self.play(Write(func_def), run_time=NORMAL)
        self.wait(2)

        # Decomposition
        decompose = MathTex(
            r"z = x + iy", r"\quad", r"f(z) = u(x,y) + i\,v(x,y)",
            font_size=HEADING_SIZE,
            color=WHITE,
        )
        decompose[0].set_color(PRIMARY)
        decompose[2].set_color(WHITE)
        self.ly.safe_place(decompose, DOWN, anchor=func_def, buff=0.6)
        self.play(Write(decompose), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # z-plane to w-plane visual
        self.add_subcaption(
            "We visualize this as two separate planes. A point z in the "
            "z-plane maps to a point w in the w-plane under the function f. "
            "This is like having two copies of the complex plane, with "
            "a rule connecting every point in one to a point in the other.",
            duration=18,
        )

        z_title = Text("z-plane (input)", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        w_title = Text("w-plane (output)", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        left_items = [z_title]
        right_items = [w_title]

        left_vg, right_vg = self.ly.two_columns(left_items, right_items)

        z_plane_small = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=4,
            y_length=3.5,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        w_plane_small = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=4,
            y_length=3.5,
            axis_config={"include_numbers": False},
            color=SECONDARY,
        )

        z_plane_small.move_to(left_vg.get_center() + DOWN * 0.8)
        w_plane_small.move_to(right_vg.get_center() + DOWN * 0.8)
        clamp_position(z_plane_small)
        clamp_position(w_plane_small)

        self.play(Create(z_plane_small), Create(w_plane_small), run_time=NORMAL)
        self.wait(2)

        # Point on z-plane
        z_dot = Dot(z_plane_small.c2p(1, 1), color=ACCENT, radius=0.08)
        z_lbl = MathTex(r"z", font_size=LABEL_SIZE, color=ACCENT)
        z_lbl.next_to(z_dot, UR, buff=0.1)
        self.play(FadeIn(z_dot), Write(z_lbl), run_time=FAST)
        self.wait(1)

        # Arrow between planes
        arrow_map = Arrow(
            z_plane_small.get_right(),
            w_plane_small.get_left(),
            color=ACCENT,
            buff=0.15,
            stroke_width=2.5,
        )
        f_arrow_label = MathTex(r"f", font_size=BODY_SIZE, color=ACCENT)
        f_arrow_label.next_to(arrow_map, UP, buff=0.15)
        self.play(Create(arrow_map), Write(f_arrow_label), run_time=NORMAL)
        self.wait(1)

        # Mapped point on w-plane
        w_dot = Dot(w_plane_small.c2p(0, 2), color=ACCENT, radius=0.08)
        w_lbl = MathTex(r"w", font_size=LABEL_SIZE, color=ACCENT)
        w_lbl.next_to(w_dot, UR, buff=0.1)
        self.play(FadeIn(w_dot), Write(w_lbl), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # --- Scene 3: Polynomials in C
    # Narration ~48s. Elements: polynomial definition, z^2 mapping, FTA statement

    def scene3_polynomials(self):
        self.add_subcaption(
            "The simplest complex functions are polynomials. A polynomial "
            "in z has the form p of z equals a_n z to the n plus dot dot "
            "dot plus a_1 z plus a_0, where each coefficient a_k is a "
            "complex number. A classic example is p of z equals z squared "
            "plus one. On the reals, this polynomial has no root. "
            "But in the complex plane, it has roots at z equals i and "
            "z equals negative i. This illustrates the Fundamental "
            "Theorem of Algebra: every non-constant polynomial with "
            "complex coefficients has at least one complex root.",
            duration=48,
        )
        self.ly.section_divider(2, "Polynomials in C")

        # Polynomial definition
        poly_def = MathTex(
            r"p(z) = a_n z^n + \cdots + a_1 z + a_0",
            font_size=HEADING_SIZE,
            color=WHITE,
        )
        poly_def[0].set_color(ACCENT)
        self.ly.center_in_content(poly_def)
        self.play(Write(poly_def), run_time=NORMAL)
        self.wait(3)

        # Example
        example = MathTex(
            r"p(z) = z^2 + 1", r"\qquad",
            r"z = \pm\,i",
            font_size=HEADING_SIZE,
        )
        example[0].set_color(PRIMARY)
        example[2].set_color(RED)
        self.ly.safe_place(example, DOWN, anchor=poly_def, buff=0.6)
        self.play(Write(example), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # z^2 mapping visualization
        self.add_subcaption(
            "Geometrically, squaring a complex number doubles its argument "
            "and squares its modulus. If z has modulus r and argument theta, "
            "then z squared has modulus r squared and argument two theta. "
            "This means the angle doubles and the distance from the origin "
            "squares. Every non-constant polynomial has a root. "
            "This is guaranteed by the Fundamental Theorem of Algebra.",
            duration=30,
        )

        zsq_title = Text(
            "The squaring map: z \u2192 z\u00b2",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(zsq_title, UP, buff=0.6)

        zsq_plane = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=4,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(zsq_plane)
        self.play(Create(zsq_plane), run_time=FAST)
        self.wait(1)

        # Show a few points and their images
        points_data = [
            (1, 0, r"1", r"1", PRIMARY),
            (0, 1, r"i", r"-1", SECONDARY),
            (2, 0, r"2", r"4", ACCENT),
            (1, 1, r"1{+}i", r"2i", RED),
        ]
        for (px, py, in_label, _, col) in points_data:
            d = Dot(zsq_plane.c2p(px, py), color=col, radius=0.07)
            l = MathTex(in_label, font_size=SMALL_SIZE, color=col)
            l.next_to(d, UR, buff=0.1)
            self.play(FadeIn(d), Write(l), run_time=FAST)
            self.wait(1)

        # FTA box
        fta = MathTex(
            r"\text{FTA: every } p(z) \neq \text{const has a root in } \mathbb{C}",
            font_size=BODY_SIZE,
            color=ACCENT,
        )
        self.ly.safe_place(fta, DOWN, anchor=zsq_plane, buff=0.3)
        self.play(Write(fta), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # --- Scene 4: Rational Functions
    # Narration ~38s. Elements: definition, 1/z mapping, pole/zero labels

    def scene4_rational(self):
        self.add_subcaption(
            "A rational function is the ratio of two polynomials: "
            "R of z equals P of z over Q of z. The zeros of Q are "
            "called poles. At a pole, the function blows up to infinity. "
            "The simplest non-trivial rational function is R of z equals "
            "one over z. This maps every point to its reciprocal. "
            "Points close to the origin get sent far away, and points "
            "far from the origin get sent close. The origin is a pole.",
            duration=38,
        )
        self.ly.section_divider(3, "Rational Functions")

        # Definition
        rat_def = MathTex(
            r"R(z) = \frac{P(z)}{Q(z)}",
            font_size=HEADING_SIZE,
            color=WHITE,
        )
        self.ly.center_in_content(rat_def)
        self.play(Write(rat_def), run_time=NORMAL)
        self.wait(2)

        # Zero and pole labels
        zero_label = Text(
            "Zeros: where P(z) = 0",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        pole_label = Text(
            "Poles: where Q(z) = 0  (\u221e)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.progressive_reveal(
            [zero_label, pole_label], start_from=rat_def,
        )
        self.wait(3)

        self.ly.clear()

        # 1/z example
        self.add_subcaption(
            "Consider R of z equals one over z. The origin is a pole, "
            "since Q of zero equals zero. Points near zero are mapped "
            "far away, and points far from the origin are mapped near zero. "
            "Geometrically, one over z inverts the modulus and negates "
            "the argument. If z has argument theta, then one over z "
            "has argument negative theta.",
            duration=28,
        )

        inv_example = MathTex(
            r"R(z) = \frac{1}{z}", r"\qquad",
            r"z = re^{i\theta} \;\mapsto\; \frac{1}{r}e^{-i\theta}",
            font_size=HEADING_SIZE,
        )
        inv_example[0].set_color(ACCENT)
        inv_example[2].set_color(WHITE)
        self.ly.center_in_content(inv_example)
        self.play(Write(inv_example), run_time=NORMAL)
        self.wait(3)

        # Show inversion on plane
        inv_plane = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=4,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.safe_place(inv_plane, DOWN, anchor=inv_example, buff=0.5)
        self.play(Create(inv_plane), run_time=FAST)
        self.wait(1)

        # Pole marker at origin
        pole_x = MathTex(r"\times", font_size=HEADING_SIZE, color=RED)
        pole_x.move_to(inv_plane.c2p(0, 0))
        pole_txt = Text("pole", font_size=SMALL_SIZE, color=RED, font=MONO)
        pole_txt.next_to(pole_x, DOWN, buff=0.15)
        self.play(Write(pole_x), Write(pole_txt), run_time=FAST)
        self.wait(2)

        # Example: z=2 maps to 1/2
        z_before = Dot(inv_plane.c2p(2, 0), color=PRIMARY, radius=0.07)
        z_before_lbl = MathTex(r"2", font_size=SMALL_SIZE, color=PRIMARY)
        z_before_lbl.next_to(z_before, UP, buff=0.1)
        self.play(FadeIn(z_before), Write(z_before_lbl), run_time=FAST)
        self.wait(2)

        z_after = Dot(inv_plane.c2p(0.5, 0), color=SECONDARY, radius=0.07)
        z_after_lbl = MathTex(r"\frac{1}{2}", font_size=SMALL_SIZE, color=SECONDARY)
        z_after_lbl.next_to(z_after, UP, buff=0.1)
        self.play(FadeIn(z_after), Write(z_after_lbl), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # --- Scene 5: The Complex Exponential e^z
    # Narration ~58s. Elements: power series, decomposition, winding, periodicity

    def scene5_exponential(self):
        self.add_subcaption(
            "The complex exponential is one of the most important functions "
            "in all of mathematics. We define it using the same power series "
            "as the real exponential: e to the z equals the sum from n "
            "equals zero to infinity of z to the n over n factorial. "
            "This series converges for every complex number z. "
            "Using Euler's formula from the last video, we can decompose "
            "the exponential into real and imaginary parts.",
            duration=34,
        )
        self.ly.section_divider(4, "The Complex Exponential")

        # Power series definition
        series_def = MathTex(
            r"e^z = \sum_{n=0}^{\infty} \frac{z^n}{n!}",
            font_size=HEADING_SIZE,
            color=ACCENT,
        )
        self.ly.center_in_content(series_def)
        self.play(Write(series_def), run_time=NORMAL)
        self.wait(3)

        # Key decomposition
        self.ly.clear()

        self.add_subcaption(
            "Writing z as x plus i y and using Euler's formula, "
            "we get e to the x plus i y equals e to the x times "
            "e to the i y. This becomes e to the x times "
            "cosine y plus i sine y. So the real part is e to the "
            "x cosine y, and the imaginary part is e to the x sine y.",
            duration=28,
        )

        decompose_exp = MathTex(
            r"e^{x+iy} = e^x(\cos y + i\sin y)",
            font_size=HEADING_SIZE,
            color=WHITE,
        )
        decompose_exp[0].set_color(ACCENT)
        self.ly.center_in_content(decompose_exp)
        self.play(Write(decompose_exp), run_time=NORMAL)
        self.wait(3)

        re_part = MathTex(
            r"\text{Re}(e^z) = e^x \cos y",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        im_part = MathTex(
            r"\text{Im}(e^z) = e^x \sin y",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.progressive_reveal([re_part, im_part], start_from=decompose_exp)
        self.wait(3)

        self.ly.clear()

        # Winding animation — e^(iy) traces unit circle
        self.add_subcaption(
            "The imaginary part of the exponent controls the angle. "
            "As y increases, e to the i y traces the unit circle. "
            "The real part of the exponent controls the radius. "
            "So e to the z wraps the imaginary axis into circles "
            "while scaling by the real part. This gives us "
            "a beautiful winding behavior.",
            duration=26,
        )

        wind_plane = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=5,
            y_length=4,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(wind_plane)
        self.play(Create(wind_plane), run_time=FAST)

        # Unit circle
        uc = Circle(radius=1.5, color=DIM, stroke_width=1.5)
        uc.move_to(wind_plane.c2p(0, 0))
        self.play(Create(uc), run_time=FAST)
        self.wait(1)

        # Tracing dot around unit circle
        theta_tracker = ValueTracker(0)
        tracing_dot = always_redraw(
            lambda: Dot(
                wind_plane.c2p(
                    1.5 * np.cos(theta_tracker.get_value()),
                    1.5 * np.sin(theta_tracker.get_value()),
                ),
                color=RED, radius=0.06,
            )
        )
        tracing_line = always_redraw(
            lambda: Line(
                wind_plane.c2p(0, 0),
                wind_plane.c2p(
                    1.5 * np.cos(theta_tracker.get_value()),
                    1.5 * np.sin(theta_tracker.get_value()),
                ),
                color=SECONDARY, stroke_width=2,
            )
        )
        self.add(tracing_dot, tracing_line)
        self.play(
            theta_tracker.animate.set_value(TAU),
            run_time=5,
            rate_func=linear,
        )
        self.wait(2)

        self.ly.clear()

        # Periodicity
        self.add_subcaption(
            "A remarkable property: e to the z plus two pi i equals "
            "e to the z. The exponential is periodic in the imaginary "
            "direction with period two pi. This is very different "
            "from the real exponential, which is one-to-one. "
            "Each horizontal strip of height two pi maps to the "
            "entire complex plane minus the origin.",
            duration=26,
        )

        periodic = MathTex(
            r"e^{z + 2\pi i} = e^z",
            font_size=HEADING_SIZE,
            color=RED,
        )
        self.ly.center_in_content(periodic)
        self.play(Write(periodic), run_time=NORMAL)
        self.wait(4)

        period_note = Text(
            "Periodic in the imaginary direction (period 2\u03c0)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(period_note, DOWN, anchor=periodic, buff=0.5)
        self.play(FadeIn(period_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

    # --- Scene 6: Trigonometric Functions in C
    # Narration ~46s. Elements: Euler definitions, sin/cos identities, unboundedness

    def scene6_trigonometric(self):
        self.add_subcaption(
            "We can define sine and cosine for complex arguments using "
            "Euler's formula. Cosine of z equals e to the i z plus "
            "e to the negative i z, all divided by two. Sine of z "
            "equals e to the i z minus e to the negative i z, "
            "divided by two i. These satisfy all the familiar identities "
            "from real trigonometry: sine squared plus cosine squared "
            "equals one, the angle addition formulas, and the double "
            "angle formulas.",
            duration=36,
        )
        self.ly.section_divider(5, "Trigonometric Functions in C")

        # Definitions
        cos_def = MathTex(
            r"\cos z = \frac{e^{iz} + e^{-iz}}{2}",
            font_size=HEADING_SIZE,
            color=PRIMARY,
        )
        sin_def = MathTex(
            r"\sin z = \frac{e^{iz} - e^{-iz}}{2i}",
            font_size=HEADING_SIZE,
            color=SECONDARY,
        )
        self.ly.center_in_content(cos_def)
        self.play(Write(cos_def), run_time=NORMAL)
        self.wait(2)

        self.play(FadeOut(cos_def), run_time=FAST)
        self.ly.center_in_content(sin_def)
        self.play(Write(sin_def), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Key identity + unboundedness
        self.add_subcaption(
            "The identity sine squared of z plus cosine squared of z "
            "equals one still holds for all complex z. But here is the "
            "surprise: on the real line, sine and cosine are bounded "
            "between negative one and one. On the complex plane, they "
            "are unbounded! For example, cosine of i y equals the "
            "hyperbolic cosine of y, which grows exponentially. "
            "This is a profound difference between real and complex "
            "trigonometry.",
            duration=34,
        )

        identity = MathTex(
            r"\sin^2 z + \cos^2 z = 1 \quad \text{for all } z \in \mathbb{C}",
            font_size=HEADING_SIZE,
            color=ACCENT,
        )
        self.ly.center_in_content(identity)
        self.play(Write(identity), run_time=NORMAL)
        self.wait(3)

        # Unbounded example
        self.ly.clear()

        unbounded_title = Text(
            "But |sin z| and |cos z| are UNBOUNDED on C!",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(unbounded_title, UP, buff=0.6)

        cosh_example = MathTex(
            r"\cos(iy) = \cosh y = \frac{e^y + e^{-y}}{2}",
            font_size=HEADING_SIZE,
            color=WHITE,
        )
        cosh_example[0].set_color(ACCENT)
        self.ly.center_in_content(cosh_example)
        self.play(Write(cosh_example), run_time=NORMAL)
        self.wait(3)

        grows = Text(
            "\u2192 grows exponentially as y \u2192 \u221e",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(grows, DOWN, anchor=cosh_example, buff=0.5)
        self.play(FadeIn(grows, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # --- Scene 7: Visualizing Complex Functions
    # Narration ~50s. Elements: domain coloring concept, grid transform, Re/Im surfaces

    def scene7_visualization(self):
        self.add_subcaption(
            "The central challenge of complex analysis visualization is "
            "that f maps a two-dimensional input to a two-dimensional "
            "output, which is four dimensions total. We cannot graph "
            "this directly. But there are three powerful techniques. "
            "First: domain coloring, where we color each point in the "
            "z-plane by the argument and modulus of its image. "
            "Second: grid transformation, where we show how a regular "
            "grid warps under the function. "
            "Third: we plot the real and imaginary parts separately "
            "as three-dimensional surfaces.",
            duration=42,
        )
        self.ly.section_divider(6, "Visualizing f: C \u2192 C")

        # Method labels
        m1 = Text(
            "1. Domain Coloring",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        m2 = Text(
            "2. Grid Transformation",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        m3 = Text(
            "3. Re/Im as 3D Surfaces",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.progressive_reveal([m1, m2, m3], start_from=None)
        self.wait(4)

        self.ly.clear()

        # Domain coloring concept
        self.add_subcaption(
            "In domain coloring, each point z gets colored based on "
            "the value f of z. The hue represents the argument, "
            "so the angle of the output. The brightness represents "
            "the modulus, so the distance from the origin. "
            "Near zeros, the image darkens to black. Near poles, "
            "it brightens to white. This creates a visual fingerprint "
            "for each function.",
            duration=26,
        )

        dc_title = Text(
            "Domain Coloring",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(dc_title, UP, buff=0.6)

        # Simple illustration: a grid of colored dots showing hue concept
        hue_grid = VGroup()
        for row in range(-3, 4):
            for col in range(-5, 6):
                angle = np.arctan2(row, col)
                # Map angle to hue-like color
                r_val = max(0, min(1, 0.5 + 0.5 * np.cos(angle)))
                g_val = max(0, min(1, 0.5 + 0.5 * np.cos(angle + 2 * np.pi / 3)))
                b_val = max(0, min(1, 0.5 + 0.5 * np.cos(angle + 4 * np.pi / 3)))
                color = rgb_to_color((r_val * 0.8, g_val * 0.8, b_val * 0.8))
                dot = Dot(
                    np.array([col * 0.45, -row * 0.45, 0]),
                    radius=0.18,
                    color=color,
                    fill_opacity=0.7,
                )
                hue_grid.add(dot)

        hue_grid.move_to(DOWN * 0.3)
        clamp_position(hue_grid)
        self.play(FadeIn(hue_grid), run_time=NORMAL)
        self.wait(3)

        legend_items = [
            Text("Hue = arg(f(z))", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Brightness = |f(z)|", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(legend_items, start_from=dc_title)
        self.wait(3)

        self.ly.clear()

        # Grid transformation concept
        self.add_subcaption(
            "Another powerful technique is the grid transformation. "
            "We draw a regular grid in the z-plane and see how "
            "the function f warps and distorts it. Straight lines "
            "may curve, and angles are preserved locally. "
            "This is the property of conformal mapping. "
            "For example, f of z equals z squared wraps the plane "
            "around itself twice.",
            duration=28,
        )

        gt_title = Text(
            "Grid Transformation: z \u2192 z\u00b2",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(gt_title, UP, buff=0.6)

        # Regular grid (z-plane)
        gt_plane = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=4.5,
            y_length=3.5,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(gt_plane)
        self.play(Create(gt_plane), run_time=FAST)
        self.wait(1)

        # Draw some grid lines that we'll "transform"
        h_lines = VGroup()
        for y_val in [-1, 0, 1]:
            h_line = Line(
                gt_plane.c2p(-2, y_val), gt_plane.c2p(2, y_val),
                color=DIM, stroke_width=1,
            )
            h_lines.add(h_line)
        v_lines = VGroup()
        for x_val in [-1, 0, 1]:
            v_line = Line(
                gt_plane.c2p(x_val, -2), gt_plane.c2p(x_val, 2),
                color=DIM, stroke_width=1,
            )
            v_lines.add(v_line)

        grid = VGroup(h_lines, v_lines)
        self.play(Create(grid), run_time=FAST)
        self.wait(2)

        # Show label about conformal mapping
        conformal = Text(
            "Conformal maps preserve angles locally",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(conformal, DOWN, anchor=gt_plane, buff=0.3)
        self.play(FadeIn(conformal, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Teaser: conformal mapping
        self.add_subcaption(
            "Conformal mapping is one of the most beautiful topics "
            "in complex analysis. We will explore it in depth later "
            "in this series. For now, the key takeaway is that "
            "complex functions can be visualized through domain "
            "coloring, grid transformations, and three-dimensional "
            "surface plots of their real and imaginary parts.",
            duration=18,
        )

        teaser_text = Text(
            "Conformal mapping preserves angles \u2014 more to come!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.center_in_content(teaser_text)
        self.play(Write(teaser_text), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # --- Scene 8: Summary and Road Ahead
    # Narration ~32s. Elements: summary list, teaser, outro

    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap what we covered today. A complex function "
            "maps the complex plane to itself, decomposing into "
            "real and imaginary parts. Polynomials in the complex "
            "plane always have roots, guaranteed by the Fundamental "
            "Theorem of Algebra. The complex exponential e to the z "
            "is periodic in the imaginary direction. "
            "Sine and cosine are unbounded on the complex plane. "
            "And domain coloring and grid transformations are "
            "powerful tools for visualization. "
            "Next time, we will study limits and continuity in the "
            "complex setting. Thank you for watching.",
            duration=40,
        )
        self.ly.section_divider(7, "Summary")

        items = [
            Text("f(z) = u + iv  \u2014 two real functions in disguise", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Polynomials always have roots (FTA)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("e^z is periodic: e^(z+2\u03c0i) = e^z", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("sin(z), cos(z) are UNBOUNDED on C", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=None)
        self.wait(4)

        teaser = Text(
            "Next: Limits and Continuity in C",
            font_size=BODY_SIZE,
            color=DIM,
            font=SANS,
        )
        self.ly.safe_place(teaser, DOWN, anchor=items[-1], buff=0.6)
        self.play(FadeIn(teaser, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()
        play_outro(self, "Limits and Continuity in C", "Complex Analysis")
