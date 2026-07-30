"""
Video 137: Zeros and Poles -- Complex Analysis
TEMPLATE v2 -- Professional quality Manim script

Playlist: Complex Analysis (Video 14 of 13 — extended)
Class: Video137_ZerosAndPoles

Topics: Zeros of analytic functions, zeros and poles duality,
         Argument Principle, Rouché's theorem, counting zeros.

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


class Video137_ZerosAndPoles(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_zeros()
        self.scene3_argument_principle()
        self.scene4_rouche()
        self.scene5_application()
        self.scene6_summary()

    # --- Scene 1: Hook -- "Counting Zeros by Integrating" ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "We know how to evaluate integrals using residues. But "
            "integrals can also count things. The Argument Principle "
            "lets us count the number of zeros and poles inside a "
            "contour, just by evaluating one integral. This connects "
            "integration to the fundamental structure of analytic "
            "functions. We will also meet Rouché's theorem, which "
            "lets us count zeros by comparing functions. This is "
            "Video 14 of Complex Analysis.",
            duration=50,
        )
        play_intro(self, "Zeros and Poles", "Complex Analysis")

        # Visual: contour with zeros and poles
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=4, y_length=3,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.3)

        # Contour
        contour = Circle(radius=1.6, color=SECONDARY, stroke_width=2.5)
        contour.move_to(plane.c2p(0, 0))
        self.play(Create(contour), run_time=NORMAL)

        # Zeros (green dots)
        for px, py in [(0.5, 0.4), (-0.6, 0.7), (0.2, -0.5)]:
            dot = Dot(point=plane.c2p(px, py), color=SECONDARY, radius=0.06)
            self.play(FadeIn(dot), run_time=FAST)

        # Pole (red X)
        pole = MathTex(r"\times", font_size=LABEL_SIZE, color=RED)
        pole.move_to(plane.c2p(-0.4, -0.5))
        self.play(Write(pole), run_time=FAST)
        self.wait(2)

        # Counting formula
        count = MathTex(
            r"N - P = \frac{1}{2\pi i}",
            r"\oint_\gamma \frac{f'(z)}{f(z)}\,dz",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(count, DOWN, anchor=plane, buff=0.3)
        self.play(Write(count), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: Zeros of Analytic Functions ~50s

    def scene2_zeros(self):
        self.add_subcaption(
            "First, let's understand zeros. If f is analytic and f of "
            "a equals zero, we say a is a zero of f. If the first "
            "non-zero derivative at a is the m-th derivative, then a is "
            "a zero of order m. Near a zero of order m, f behaves like "
            "z minus a to the m. A crucial fact: zeros of a non-zero "
            "analytic function are isolated. They cannot accumulate "
            "in a finite region. This is because if zeros did "
            "accumulate, f would have to be identically zero by the "
            "identity theorem.",
            duration=50,
        )
        self.ly.section_divider(1, "Zeros of Analytic Functions")

        # Zero of order m
        zero_def = MathTex(
            r"f(z) = (z - a)^m \cdot g(z)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.center_in_content(zero_def)
        self.play(Write(zero_def), run_time=NORMAL)
        self.wait(2)

        where = MathTex(
            r"g(a) \neq 0,\; g \text{ analytic}",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(where, DOWN, anchor=zero_def, buff=0.4)
        self.play(Write(where), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Key fact
        title = self.ly.title("Key Fact")
        self.wait(1)

        fact = Text(
            "Zeros of a non-zero analytic function are isolated",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        box = self.ly.formula_box(fact, color=ACCENT)
        self.ly.safe_place(box, DOWN, anchor=title, buff=0.5)
        self.play(Write(box), run_time=NORMAL)
        self.wait(2)

        reason = Text(
            "Zeros cannot accumulate in a finite region",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(reason, DOWN, anchor=box, buff=0.4)
        self.play(FadeIn(reason, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 3: The Argument Principle ~60s

    def scene3_argument_principle(self):
        self.add_subcaption(
            "The Argument Principle is the main theorem. If f is "
            "meromorphic inside and on a contour gamma, with N zeros "
            "and P poles counting multiplicity, then one over two pi i "
            "times the integral of f prime over f dz equals N minus P. "
            "The key insight is that f prime over f has simple poles "
            "at zeros with residue equal to the order of the zero, and "
            "at poles with residue equal to negative the order of the "
            "pole. So the integral sums up the residues, giving N minus "
            "P. Geometrically, this integral counts how many times "
            "f of gamma winds around the origin.",
            duration=60,
        )
        self.ly.section_divider(2, "The Argument Principle")

        # Statement
        statement = MathTex(
            r"\frac{1}{2\pi i}",
            r"\oint_\gamma \frac{f'(z)}{f(z)}\,dz",
            r"= N - P",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([DIM, WHITE, ACCENT]):
            if i < len(statement):
                statement[i].set_color(col)
        box = self.ly.formula_box(statement, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Why it works
        title = Text(
            "Why it works:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(title)
        self.play(Write(title), run_time=FAST)
        self.wait(1)

        insights = [
            Text("f'/f has poles at zeros: residue = order", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("f'/f has poles at poles: residue = -order", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Sum of residues = N - P", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(insights, start_from=title)
        self.wait(4)

        self.ly.clear()

        # Geometric meaning
        geo_title = Text(
            "Geometric meaning:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(geo_title)
        self.play(Write(geo_title), run_time=FAST)
        self.wait(1)

        geo = Text(
            "f(gamma) winds around the origin N - P times",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(geo, DOWN, anchor=geo_title, buff=0.5)
        self.play(FadeIn(geo, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 4: Rouché's Theorem ~55s

    def scene4_rouche(self):
        self.add_subcaption(
            "Rouché's theorem lets us count zeros by comparing "
            "functions. If f and g are analytic inside and on gamma, "
            "and the absolute value of f minus g is strictly less "
            "than the absolute value of f plus g on gamma, then f "
            "and g have the same number of zeros inside gamma. "
            "Intuitively, on the boundary, f and g are never too "
            "far apart, so their winding numbers must match. "
            "Let's see an example. Consider p of z equals z to the "
            "fifth minus five z plus one. How many zeros in absolute "
            "z less than one?",
            duration=55,
        )
        self.ly.section_divider(3, "Rouché's Theorem")

        # Statement
        statement = Text(
            "|f - g| < |f| on gamma => same number of zeros",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        box = self.ly.formula_box(statement, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Example
        example = MathTex(
            r"p(z) = z^5 - 5z + 1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(example)
        self.play(Write(example), run_time=NORMAL)
        self.wait(2)

        question = Text(
            "How many zeros in |z| < 1?",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(question, DOWN, anchor=example, buff=0.4)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Solution
        sol_title = Text(
            "Take f(z) = -5z (1 zero at z=0)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.center_in_content(sol_title)
        self.play(FadeIn(sol_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        # On |z| = 1
        on_boundary = MathTex(
            r"|z| = 1: \quad |p(z) - f(z)| = |z^5 + 1| \leq 2",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(on_boundary, DOWN, anchor=sol_title, buff=0.4)
        self.play(Write(on_boundary), run_time=NORMAL)
        self.wait(2)

        compare = MathTex(
            r"< 5 = |f(z)| \quad \checkmark",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(compare, DOWN, anchor=on_boundary, buff=0.3)
        self.play(Write(compare), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        # Conclusion
        conclusion = Text(
            "p(z) has exactly 1 zero in |z| < 1",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        box2 = self.ly.formula_box(conclusion, color=ACCENT)
        self.ly.center_in_content(box2)
        self.play(Write(box2), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 5: Application — Counting Zeros ~50s

    def scene5_application(self):
        self.add_subcaption(
            "Let's verify with the Argument Principle. How many "
            "zeros does z to the fourth minus three z squared plus "
            "two have in absolute z less than two? We can factor "
            "this as z squared minus one times z squared minus two, "
            "giving zeros at plus or minus one and plus or minus "
            "root two. All four are inside absolute z less than "
            "two. By the Argument Principle, one over two pi i times "
            "the integral of f prime over f around the circle "
            "equals four, confirming four zeros.",
            duration=50,
        )
        self.ly.section_divider(4, "Example: Counting Zeros")

        # The function
        func = MathTex(
            r"f(z) = z^4 - 3z^2 + 2",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(func)
        self.play(Write(func), run_time=NORMAL)
        self.wait(2)

        # Factor
        factor = MathTex(
            r"= (z^2 - 1)(z^2 - 2)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(factor, DOWN, anchor=func, buff=0.4)
        self.play(Write(factor), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        # Zeros
        zeros_title = Text(
            "Zeros: z = ±1, ±√2",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.center_in_content(zeros_title)
        self.play(Write(zeros_title), run_time=FAST)
        self.wait(2)

        # Visual: circle with zeros
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=4, y_length=3,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.3)

        circ = Circle(radius=1.6, color=SECONDARY, stroke_width=2.5)
        circ.move_to(plane.c2p(0, 0))
        self.play(Create(circ), run_time=NORMAL)

        # Zeros
        for val, lbl in [(1.0, "1"), (-1.0, "-1"), (1.414, r"\sqrt{2}"), (-1.414, r"-\!\sqrt{2}")]:
            frac = min(val / 2.5, 1.0) * 1.6
            dot = Dot(point=plane.c2p(val, 0), color=SECONDARY, radius=0.06)
            self.play(FadeIn(dot), run_time=FAST)
        self.wait(2)

        count = Text(
            "All 4 zeros inside |z| < 2",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(count, DOWN, anchor=plane, buff=0.3)
        self.play(FadeIn(count, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 6: Summary and Preview ~45s

    def scene6_summary(self):
        self.add_subcaption(
            "Let's recap. Zeros of analytic functions are always "
            "isolated. The Argument Principle says one over two pi i "
            "times the integral of f prime over f equals N minus P, "
            "counting zeros and poles. Rouché's theorem lets us "
            "count zeros by comparing functions. The deep message: "
            "integration connects to the topology of analytic "
            "functions. Next time, we will explore conformal "
            "mappings, transformations that preserve angles and "
            "shapes in the complex plane.",
            duration=45,
        )
        self.ly.section_divider(5, "Summary")

        title = self.ly.title("Key Takeaways")
        self.wait(1)

        points = [
            Text("Zeros of analytic f are isolated", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Argument Principle: integral counts N - P", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Rouché: compare functions to count zeros", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Integration reveals topological structure", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        self.wait(3)

        self.ly.clear()

        # Final formula
        final = MathTex(
            r"\frac{1}{2\pi i}",
            r"\oint_\gamma \frac{f'}{f}\,dz",
            r"= N - P",
            font_size=TITLE_SIZE,
        )
        for i, col in enumerate([DIM, WHITE, ACCENT]):
            if i < len(final):
                final[i].set_color(col)
        box = self.ly.formula_box(final, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()
        play_outro(self, "Conformal Mappings", "Complex Analysis")
