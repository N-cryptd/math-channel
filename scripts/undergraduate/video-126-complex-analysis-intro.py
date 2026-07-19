"""
Video 126: Complex Numbers Revisited — Introduction to Complex Analysis
TEMPLATE v2 -- Professional quality Manim script

Playlist: Complex Analysis (Video 1 of 13)
Class: Video126_ComplexAnalysisIntro

Topics: complex number review from analysis perspective, the complex plane (Argand
         diagram), complex arithmetic as geometry, modulus and argument, polar
         form, Euler's formula, Euler's identity, De Moivre's theorem.

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


class Video126_ComplexAnalysisIntro(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_complex_plane()
        self.scene4_arithmetic()
        self.scene5_modulus_argument()
        self.scene6_euler()
        self.scene7_polar_operations()
        self.scene8_summary()

    # --- Scene 1: Hook --- "What Lies Beyond the Real Line?"
    # Narration ~38s. Elements: title, number line, question, i symbol

    def scene1_hook(self):
        self.add_subcaption(
            "Throughout our Real Analysis series, we worked entirely within the "
            "real numbers. But there is a fundamental equation that has no real "
            "solution. What number squared equals negative one? The answer takes "
            "us beyond the real line and into a rich new world. "
            "Today we revisit complex numbers from an analytical perspective, "
            "building the foundation for Complex Analysis. "
            "This is Complex Analysis, Video 1.",
            duration=38,
        )
        play_intro(self, "Complex Numbers Revisited", "Complex Analysis")

        title = self.ly.title("What Lies Beyond the Real Line?")
        self.wait(2)

        # Real number line visual
        line = NumberLine(
            x_range=[-4, 4, 1],
            length=7,
            color=PRIMARY,
            include_numbers=True,
            font_size=LABEL_SIZE,
        )
        self.ly.center_in_content(line)
        self.add(line)

        question = Text(
            "x\u00b2 = \u22121  \u2014  no real solution!",
            font_size=BODY_SIZE,
            color=RED,
            font=SANS,
        )
        self.ly.safe_place(question, DOWN, anchor=line, buff=0.8)
        self.play(Write(question), run_time=NORMAL)
        self.wait(3)

        i_label = MathTex(r"i", color=ACCENT, font_size=HEADING_SIZE)
        i_label.next_to(question, RIGHT, buff=0.8)
        self.play(Write(i_label), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # --- Scene 2: Complex Numbers — Definition and Notation
    # Narration ~42s. Elements: definition, Re/Im labels, examples

    def scene2_definition(self):
        self.add_subcaption(
            "A complex number is written as z equals a plus b i, "
            "where a and b are real numbers and i is the imaginary unit "
            "with the property i squared equals negative one. "
            "We call a the real part of z, written Re of z, "
            "and b the imaginary part, written Im of z. "
            "For example, three plus two i has real part three and imaginary part two. "
            "The number five is also complex, with imaginary part zero. "
            "Every real number is also a complex number.",
            duration=42,
        )
        self.ly.section_divider(1, "Complex Numbers")

        formula = MathTex(
            r"z = a + bi", r"\quad", r"i^2 = -1",
            font_size=HEADING_SIZE,
            color=WHITE,
        )
        formula[0].set_color(ACCENT)
        formula[2].set_color(RED)
        self.ly.center_in_content(formula)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(2)

        parts = [
            Text("a = Re(z)  \u2014  the real part", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("b = Im(z)  \u2014  the imaginary part", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(parts, start_from=formula)
        self.wait(3)

        examples = [
            MathTex(r"z_1 = 3 + 2i", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"z_2 = -1 + 4i", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"z_3 = 5 \;\;(\text{Im}(z_3) = 0)", font_size=BODY_SIZE, color=DIM),
        ]
        self.ly.progressive_reveal(examples, start_from=formula)
        self.wait(4)

        self.ly.clear()

    # --- Scene 3: The Complex Plane (Argand Diagram)
    # Narration ~48s. Elements: axes, plotted points, labels

    def scene3_complex_plane(self):
        self.add_subcaption(
            "We can visualize complex numbers as points in a plane. "
            "The horizontal axis represents the real part, and the "
            "vertical axis represents the imaginary part. "
            "This is called the Argand diagram, or the complex plane. "
            "Every complex number corresponds to exactly one point. "
            "Notice how each complex number is also a vector from the origin. "
            "This geometric viewpoint connects complex numbers to linear algebra.",
            duration=48,
        )
        self.ly.section_divider(2, "The Complex Plane")

        # Build Argand diagram
        plane = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            axis_config={"include_numbers": True, "font_size": LABEL_SIZE},
            x_length=7,
            y_length=5,
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=SLOW)
        self.wait(2)

        re_label = Text("Re", font_size=LABEL_SIZE, color=PRIMARY, font=MONO)
        im_label = Text("Im", font_size=LABEL_SIZE, color=SECONDARY, font=MONO)
        re_label.next_to(plane.x_axis.get_right(), RIGHT, buff=0.2)
        im_label.next_to(plane.y_axis.get_top(), UP, buff=0.2)
        self.play(FadeIn(re_label), FadeIn(im_label), run_time=FAST)
        self.wait(2)

        # Plot points
        dots_labels = [
            (3, 2, r"3+2i", ACCENT),
            (-1, 3, r"-1+3i", SECONDARY),
            (-3, -1, r"-3-i", RED),
        ]
        plotted = []
        for (cx, cy, label_str, col) in dots_labels:
            dot = Dot(plane.c2p(cx, cy), color=col, radius=0.08)
            label = MathTex(label_str, font_size=SMALL_SIZE, color=col)
            label.next_to(dot, UR, buff=0.15)
            self.play(FadeIn(dot), Write(label), run_time=FAST)
            plotted.extend([dot, label])
            self.wait(2)

        # Show vector for first point
        arrow_start = plane.c2p(0, 0)
        arrow_end = plane.c2p(3, 2)
        vec_arrow = Arrow(arrow_start, arrow_end, color=ACCENT, buff=0.05, stroke_width=3)
        self.play(Create(vec_arrow), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

    # --- Scene 4: Complex Arithmetic — Geometric View
    # Narration ~44s. Elements: vectors, result vectors, formulas

    def scene4_arithmetic(self):
        self.add_subcaption(
            "Complex arithmetic has beautiful geometric interpretations. "
            "Adding two complex numbers follows the parallelogram law, "
            "just like vector addition in linear algebra. "
            "Multiplying by i rotates a number by ninety degrees. "
            "In general, multiplying two complex numbers rotates and scales. "
            "For example, two times i equals two i, which is two i. "
            "And i times i equals negative one, a one-eighty degree rotation.",
            duration=44,
        )
        self.ly.section_divider(3, "Arithmetic as Geometry")

        mini_plane = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=4,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(mini_plane)
        self.play(Create(mini_plane), run_time=FAST)
        self.wait(1)

        # Addition: z1 + z2
        z1 = MathTex(r"z_1 = 1 + 2i", font_size=BODY_SIZE, color=PRIMARY)
        z2 = MathTex(r"z_2 = 2 + i", font_size=BODY_SIZE, color=SECONDARY)
        zsum = MathTex(r"z_1 + z_2 = 3 + 3i", font_size=BODY_SIZE, color=ACCENT)

        z1_dot = Dot(mini_plane.c2p(1, 2), color=PRIMARY, radius=0.08)
        z2_dot = Dot(mini_plane.c2p(2, 1), color=SECONDARY, radius=0.08)
        zs_dot = Dot(mini_plane.c2p(3, 3), color=ACCENT, radius=0.08)

        z1_vec = Arrow(mini_plane.c2p(0, 0), mini_plane.c2p(1, 2), color=PRIMARY, buff=0.05, stroke_width=2.5)
        z2_vec = Arrow(mini_plane.c2p(0, 0), mini_plane.c2p(2, 1), color=SECONDARY, buff=0.05, stroke_width=2.5)

        self.play(Write(z1), run_time=FAST)
        self.play(Create(z1_vec), FadeIn(z1_dot), run_time=NORMAL)
        self.wait(2)

        self.play(ReplacementTransform(z1, z2), run_time=FAST)
        self.play(Create(z2_vec), FadeIn(z2_dot), run_time=NORMAL)
        self.wait(2)

        # Show sum
        self.play(Write(zsum), run_time=FAST)
        self.play(Create(Arrow(mini_plane.c2p(0, 0), mini_plane.c2p(3, 3), color=ACCENT, buff=0.05, stroke_width=3)), FadeIn(zs_dot), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Multiplication by i
        self.add_subcaption(
            "Now let us see multiplication. Multiplying a complex number by i "
            "rotates it ninety degrees counter-clockwise. "
            "Starting at one, multiplying by i gives i. "
            "Multiplying by i again gives negative one. "
            "And multiplying by i a third time gives negative i. "
            "Four times brings us back to one. "
            "Multiplication in the complex plane is rotation and scaling.",
            duration=30,
        )

        title2 = self.ly.title("Multiplication by i = 90\u00b0 Rotation")

        rot_plane = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=4.5,
            y_length=4.5,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(rot_plane)
        self.play(Create(rot_plane), run_time=FAST)

        # Unit circle
        circ = Circle(radius=1.5, color=DIM, stroke_width=1)
        circ.move_to(rot_plane.c2p(0, 0))
        self.play(Create(circ), run_time=FAST)
        self.wait(1)

        rot_points = [
            (1, 0, "1", PRIMARY),
            (0, 1, "i", SECONDARY),
            (-1, 0, r"-1", ACCENT),
            (0, -1, r"-i", RED),
        ]
        rot_dots = []
        rot_labels = []
        for (rx, ry, lbl, col) in rot_points:
            d = Dot(rot_plane.c2p(rx, ry), color=col, radius=0.08)
            l = MathTex(lbl, font_size=LABEL_SIZE, color=col)
            l.next_to(d, UR if rx >= 0 and ry >= 0 else (UL if ry > 0 else DR if rx > 0 else DL), buff=0.15)
            self.play(FadeIn(d), Write(l), run_time=FAST)
            rot_dots.append(d)
            rot_labels.append(l)
            self.wait(2)

        # Show rotation arrows
        for i_idx in range(len(rot_points) - 1):
            x1, y1 = rot_points[i_idx][0], rot_points[i_idx][1]
            x2, y2 = rot_points[i_idx + 1][0], rot_points[i_idx + 1][1]
            arc = ArcBetweenPoints(
                rot_plane.c2p(x1, y1), rot_plane.c2p(x2, y2),
                angle=-TAU / 4,
                color=ACCENT,
                stroke_width=2,
            )
            self.play(Create(arc), run_time=FAST)
            self.wait(1)

        self.wait(2)
        self.ly.clear()

    # --- Scene 5: Modulus and Argument — Polar Form
    # Narration ~40s. Elements: triangle, labels, formulas

    def scene5_modulus_argument(self):
        self.add_subcaption(
            "Every complex number can be described by its distance from the origin "
            "and its angle with the real axis. The distance is called the modulus, "
            "written as the absolute value of z, and equals the square root of "
            "a squared plus b squared. The angle is called the argument, "
            "written arg of z. Together they give the polar form: "
            "z equals r times cosine theta plus i sine theta. "
            "This form makes multiplication and exponentiation much simpler.",
            duration=40,
        )
        self.ly.section_divider(4, "Modulus and Argument")

        # Show z = a + bi in plane with right triangle
        polar_plane = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 4, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(polar_plane)
        self.play(Create(polar_plane), run_time=FAST)

        # Point at (3, 2)
        p = polar_plane.c2p(3, 2)
        o = polar_plane.c2p(0, 0)
        px = polar_plane.c2p(3, 0)

        dot_z = Dot(p, color=ACCENT, radius=0.08)
        vec_z = Arrow(o, p, color=ACCENT, buff=0.05, stroke_width=2.5)
        h_line = DashedLine(o, px, color=PRIMARY, stroke_width=1.5)
        v_line = DashedLine(px, p, color=SECONDARY, stroke_width=1.5)

        # Labels
        a_label = MathTex(r"a", font_size=LABEL_SIZE, color=PRIMARY)
        a_label.move_to((np.array(o) + np.array(px)) / 2 + np.array([0, -0.3, 0]))
        b_label = MathTex(r"b", font_size=LABEL_SIZE, color=SECONDARY)
        b_label.move_to((np.array(px) + np.array(p)) / 2 + np.array([0.35, 0, 0]))
        z_label = MathTex(r"z", font_size=BODY_SIZE, color=ACCENT)
        z_label.next_to(p, UR, buff=0.15)

        self.play(Create(vec_z), FadeIn(dot_z), run_time=NORMAL)
        self.play(Write(z_label), run_time=FAST)
        self.wait(1)

        self.play(Create(h_line), Write(a_label), run_time=FAST)
        self.play(Create(v_line), Write(b_label), run_time=FAST)
        self.wait(2)

        # Angle arc
        angle_arc = Arc(radius=0.8, start_angle=0, angle=np.arctan2(2, 3), color=ACCENT, stroke_width=2)
        angle_arc.move_to(o)
        theta_label = MathTex(r"\theta", font_size=LABEL_SIZE, color=ACCENT)
        theta_label.next_to(angle_arc, RIGHT, buff=0.1)
        self.play(Create(angle_arc), Write(theta_label), run_time=FAST)
        self.wait(2)

        # Formulas
        mod_formula = MathTex(
            r"|z| = r = \sqrt{a^2 + b^2}",
            font_size=HEADING_SIZE,
            color=ACCENT,
        )
        arg_formula = MathTex(
            r"\arg(z) = \theta = \arctan\!\left(\frac{b}{a}\right)",
            font_size=HEADING_SIZE,
            color=SECONDARY,
        )
        polar_formula = MathTex(
            r"z = r(\cos\theta + i\sin\theta)",
            font_size=HEADING_SIZE,
            color=WHITE,
        )

        formulas = [mod_formula, arg_formula, polar_formula]
        self.ly.progressive_reveal(formulas, start_from=None)
        self.wait(4)

        self.ly.clear()

    # --- Scene 6: Euler's Formula — The Crown Jewel
    # Narration ~50s. Elements: unit circle, formula, Euler's identity

    def scene6_euler(self):
        self.add_subcaption(
            "One of the most remarkable results in all of mathematics "
            "is Euler's formula. It states that e to the power of i theta "
            "equals cosine theta plus i sine theta. "
            "This single formula connects the exponential function, "
            "trigonometry, and complex numbers into one elegant identity. "
            "When theta equals pi, we get the famous Euler's identity: "
            "e to the i pi plus one equals zero. "
            "This relates the five most important constants in mathematics: "
            "e, i, pi, one, and zero. "
            "On the complex plane, e to the i theta traces the unit circle "
            "as theta goes from zero to two pi.",
            duration=50,
        )
        self.ly.section_divider(5, "Euler's Formula")

        # Unit circle setup
        euler_plane = Axes(
            x_range=[-1.8, 1.8, 0.5],
            y_range=[-1.8, 1.8, 0.5],
            x_length=5.5,
            y_length=5.5,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(euler_plane)
        self.play(Create(euler_plane), run_time=FAST)

        uc = Circle(radius=1.8, color=DIM, stroke_width=1.5)
        uc.move_to(euler_plane.c2p(0, 0))
        self.play(Create(uc), run_time=FAST)
        self.wait(1)

        # Euler's formula
        euler_formula = MathTex(
            r"e^{i\theta} = \cos\theta + i\sin\theta",
            font_size=HEADING_SIZE,
            color=ACCENT,
        )
        euler_formula.to_edge(UP, buff=0.4)
        self.play(Write(euler_formula), run_time=NORMAL)
        self.wait(3)

        # Animate tracing the unit circle
        tracing_dot = Dot(euler_plane.c2p(1.8, 0), color=RED, radius=0.06)
        self.add(tracing_dot)

        theta_tracker = ValueTracker(0)
        tracing_line = always_redraw(
            lambda: Line(
                euler_plane.c2p(0, 0),
                euler_plane.c2p(
                    1.8 * np.cos(theta_tracker.get_value()),
                    1.8 * np.sin(theta_tracker.get_value()),
                ),
                color=SECONDARY,
                stroke_width=2,
            )
        )
        self.add(tracing_line)

        self.play(
            theta_tracker.animate.set_value(TAU),
            run_time=6,
            rate_func=linear,
        )
        self.wait(2)

        # Euler's identity
        self.ly.clear()
        self.add_subcaption(
            "Setting theta to pi, the point lands at negative one on the real axis. "
            "This gives us Euler's identity: e to the i pi plus one equals zero. "
            "Five fundamental constants united in a single equation.",
            duration=18,
        )

        identity = MathTex(
            r"e^{i\pi} + 1 = 0",
            font_size=TITLE_SIZE,
            color=RED,
        )
        self.ly.center_in_content(identity)
        self.play(Write(identity), run_time=SLOW)
        self.wait(4)

        # Color-code each constant
        self.play(FadeOut(identity), run_time=FAST)
        identity_parts = MathTex(
            r"e", r"^{\,i\pi}", r" + 1", r" = 0",
            font_size=TITLE_SIZE,
        )
        identity_parts[0].set_color(PRIMARY)
        identity_parts[1].set_color(ACCENT)
        identity_parts[2].set_color(SECONDARY)
        identity_parts[3].set_color(WHITE)
        self.ly.center_in_content(identity_parts)
        self.play(Write(identity_parts), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # --- Scene 7: Operations in Polar Form
    # Narration ~38s. Elements: multiplication visual, De Moivre formula

    def scene7_polar_operations(self):
        self.add_subcaption(
            "The polar form makes certain operations elegant. "
            "To multiply two complex numbers, multiply their moduli "
            "and add their arguments. To divide, divide the moduli "
            "and subtract the arguments. "
            "De Moivre's theorem generalizes this to powers: "
            "cosine theta plus i sine theta, raised to the n-th power, "
            "equals cosine n theta plus i sine n theta. "
            "This is incredibly powerful for finding roots of complex numbers.",
            duration=38,
        )
        self.ly.section_divider(6, "Polar Operations")

        # Multiplication rule
        mult_title = Text(
            "Multiplication in Polar Form",
            font_size=HEADING_SIZE,
            color=PRIMARY,
            font=SANS,
        )
        mult_rule = MathTex(
            r"z_1 z_2 = r_1 r_2 \;\cdot\;"
            r"(\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2))",
            font_size=BODY_SIZE,
            color=WHITE,
        )
        mult_note1 = Text(
            "Moduli: multiply",
            font_size=BODY_SIZE,
            color=PRIMARY,
            font=SANS,
        )
        mult_note2 = Text(
            "Arguments: add",
            font_size=BODY_SIZE,
            color=SECONDARY,
            font=SANS,
        )

        self.play(Write(mult_title), run_time=FAST)
        self.ly.progressive_reveal(
            [mult_rule, mult_note1, mult_note2],
            start_from=mult_title,
        )
        self.wait(4)

        self.ly.clear()

        # Division rule
        div_title = Text(
            "Division in Polar Form",
            font_size=HEADING_SIZE,
            color=PRIMARY,
            font=SANS,
        )
        div_rule = MathTex(
            r"\frac{z_1}{z_2} = \frac{r_1}{r_2} \;\cdot\;"
            r"(\cos(\theta_1 - \theta_2) + i\sin(\theta_1 - \theta_2))",
            font_size=BODY_SIZE,
            color=WHITE,
        )
        self.play(Write(div_title), run_time=FAST)
        self.play(Write(div_rule), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # De Moivre's theorem
        dm_title = self.ly.title("De Moivre's Theorem")
        dm_formula = MathTex(
            r"(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)",
            font_size=HEADING_SIZE,
            color=ACCENT,
        )
        self.ly.center_in_content(dm_formula)
        self.play(Write(dm_formula), run_time=NORMAL)
        self.wait(4)

        dm_example = MathTex(
            r"(1+i)^{10} = (\sqrt{2})^{10}(\cos\tfrac{5\pi}{4}\cdot 10"
            r" + i\sin\tfrac{5\pi}{4}\cdot 10)",
            font_size=BODY_SIZE,
            color=WHITE,
        )
        dm_result = MathTex(
            r"= 32(\cos\tfrac{5\pi}{2} + i\sin\tfrac{5\pi}{2}) = 32i",
            font_size=BODY_SIZE,
            color=SECONDARY,
        )
        self.ly.progressive_reveal(
            [dm_example, dm_result],
            start_from=dm_formula,
        )
        self.wait(4)

        self.ly.clear()

    # --- Scene 8: Summary and Road Ahead
    # Narration ~35s. Elements: summary list, teaser, outro

    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap what we covered today. Complex numbers extend the real "
            "line into the complex plane, where each number is a point. "
            "Polar form describes numbers by modulus and argument. "
            "Euler's formula unites exponentials, trigonometry, and complex numbers. "
            "Next time, we will explore complex functions and discover what it "
            "means for a function to be differentiable in the complex sense. "
            "Complex differentiability is far more restrictive, and far more "
            "beautiful, than real differentiability. Thank you for watching.",
            duration=35,
        )
        self.ly.section_divider(7, "Summary")

        items = [
            Text("Complex plane: z = a + bi as points in 2D", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Polar form: z = r(cos\u03b8 + i sin\u03b8)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Euler's formula: e^(i\u03b8) = cos\u03b8 + i sin\u03b8", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Euler's identity: e^(i\u03c0) + 1 = 0", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=None)
        self.wait(4)

        teaser = Text(
            "Next: Complex Functions \u2014 What makes them special?",
            font_size=BODY_SIZE,
            color=DIM,
            font=SANS,
        )
        self.ly.safe_place(teaser, DOWN, anchor=items[-1], buff=0.6)
        self.play(FadeIn(teaser, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()
        play_outro(self, "Complex Functions", "Complex Analysis")
