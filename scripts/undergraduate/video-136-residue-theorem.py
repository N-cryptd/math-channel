"""
Video 136: The Residue Theorem -- Complex Analysis
TEMPLATE v2 -- Professional quality Manim script

Playlist: Complex Analysis (Video 13 of 13 — FINALE)
Class: Video136_ResidueTheorem

Topics: Residue Theorem statement, computing residues at poles,
         evaluating contour integrals, application to real integrals,
         playlist recap and finale.

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


class Video136_ResidueTheorem(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_theorem_statement()
        self.scene3_computing_residues()
        self.scene4_contour_example()
        self.scene5_real_integral()
        self.scene6_finale()

    # --- Scene 1: Hook -- "The Most Practical Theorem" ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "We have built an incredible machinery. Cauchy's Integral "
            "Formula, Laurent series, and residues. The Residue Theorem "
            "brings it all together into the most practical tool in "
            "complex analysis. Here is the idea. If a function has "
            "singularities inside a contour, the contour integral equals "
            "two pi i times the sum of the residues at those "
            "singularities. That is it. No parameterization, no "
            "messy trig integrals. Just find the residues inside and "
            "sum them up. This is Video 13, the finale of Complex Analysis.",
            duration=50,
        )
        play_intro(self, "The Residue Theorem", "Complex Analysis")

        # Visual: contour with singularities
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
        contour = Circle(radius=1.8, color=SECONDARY, stroke_width=2.5)
        contour.move_to(plane.c2p(0, 0))
        self.play(Create(contour), run_time=NORMAL)
        self.wait(0.5)

        # Three singularities
        positions = [(0.5, 0.5), (-0.7, -0.3), (0.2, -0.8)]
        labels = [r"a_1", r"a_2", r"a_3"]
        for (px, py), lbl in zip(positions, labels):
            dot = Dot(point=plane.c2p(px, py), color=RED, radius=0.06)
            self.play(FadeIn(dot), run_time=FAST)
            text = MathTex(lbl, font_size=LABEL_SIZE, color=RED)
            text.next_to(dot, UR, buff=0.1)
            self.play(Write(text), run_time=FAST)
            self.wait(0.5)
        self.wait(2)

        # Result formula
        result = MathTex(
            r"\oint_\gamma f(z)\,dz = 2\pi i \sum_k \text{Res}(f, a_k)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(result, DOWN, anchor=plane, buff=0.3)
        self.play(Write(result), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: The Theorem Statement ~55s

    def scene2_theorem_statement(self):
        self.add_subcaption(
            "Here is the precise statement. If f is analytic on and "
            "inside a simple closed contour gamma, except for finitely "
            "many isolated singularities inside gamma, then the "
            "integral of f of z dz around gamma equals two pi i times "
            "the sum of the residues at those singularities. We only "
            "need to know the residues at the singularities inside "
            "the contour. Everything else cancels out. We don't need "
            "to parameterize anything. Just find the singularities "
            "inside, compute their residues, sum them up, and multiply "
            "by two pi i.",
            duration=55,
        )
        self.ly.section_divider(1, "The Theorem Statement")

        # Theorem box
        theorem = MathTex(
            r"\oint_\gamma f(z)\,dz",
            r"= 2\pi i",
            r"\sum_{k=1}^{n} \text{Res}(f, a_k)",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, ACCENT, RED]):
            if i < len(theorem):
                theorem[i].set_color(col)
        box = self.ly.formula_box(theorem, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

        # Key point
        title = self.ly.title("Key Insight")
        self.wait(1)

        points = [
            Text("Find singularities inside the contour", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Compute residue at each one", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Sum and multiply by 2πi", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        self.wait(5)

        self.ly.clear()

    # --- Scene 3: Computing Residues at Poles ~60s

    def scene3_computing_residues(self):
        self.add_subcaption(
            "To use the theorem, we need to compute residues. For a "
            "simple pole at a, the residue is the limit as z approaches "
            "a of z minus a times f of z. For a pole of order k, the "
            "formula involves derivatives. The residue equals one over "
            "k minus one factorial times the limit as z approaches a "
            "of the k minus one derivative of z minus a to the k times "
            "f of z. Let's practice. Consider f of z equals e to the z "
            "over z minus one times z minus two. The singularities are "
            "at z equals one and z equals two, both simple poles.",
            duration=60,
        )
        self.ly.section_divider(2, "Computing Residues")

        # Simple pole formula
        simple = MathTex(
            r"\text{Simple pole: } \text{Res}(f, a) = \lim_{z \to a} (z-a)\,f(z)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.center_in_content(simple)
        self.play(Write(simple), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Higher order pole formula
        higher = MathTex(
            r"\text{Pole of order } k:",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(higher)
        self.play(Write(higher), run_time=FAST)
        self.wait(1)

        formula = MathTex(
            r"\text{Res}(f, a) = \frac{1}{(k-1)!}",
            r"\lim_{z \to a} \frac{d^{k-1}}{dz^{k-1}}\!",
            r"\left[(z-a)^k f(z)\right]",
            font_size=BODY_SIZE,
        )
        for i, col in enumerate([DIM, WHITE, SECONDARY]):
            if i < len(formula):
                formula[i].set_color(col)
        self.ly.safe_place(formula, DOWN, anchor=higher, buff=0.4)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Practice example
        example = MathTex(
            r"f(z) = \frac{e^z}{(z-1)(z-2)}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(example)
        self.play(Write(example), run_time=NORMAL)
        self.wait(2)

        singularities = Text(
            "Singularities: z=1 and z=2 (simple poles)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(singularities, DOWN, anchor=example, buff=0.4)
        self.play(FadeIn(singularities, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 4: Example — Evaluating a Contour Integral ~55s

    def scene4_contour_example(self):
        self.add_subcaption(
            "Let's use the residue theorem. Evaluate the integral of "
            "e to the z over z minus one times z minus two dz, where "
            "gamma is the circle absolute z equals three. Both z equals "
            "one and z equals two are inside this circle. The residue "
            "at z equals one is e to the one over one minus two, which "
            "equals negative e. The residue at z equals two is e squared "
            "over two minus one, which equals e squared. By the "
            "Residue Theorem, the integral equals two pi i times "
            "negative e plus e squared, which is two pi i times e "
            "squared minus e. No parameterization, no messy trig "
            "integrals, just algebra!",
            duration=55,
        )
        self.ly.section_divider(3, "Example: Contour Integral")

        # The integral
        integral = MathTex(
            r"\oint_\gamma \frac{e^z}{(z-1)(z-2)}\,dz",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(integral)
        self.play(Write(integral), run_time=NORMAL)
        self.wait(2)

        gamma_info = MathTex(
            r"\gamma:\; |z| = 3",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(gamma_info, DOWN, anchor=integral, buff=0.4)
        self.play(Write(gamma_info), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Residues
        res1 = MathTex(
            r"\text{Res}(f, 1) = \frac{e^1}{1-2} = -e",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.center_in_content(res1)
        self.play(Write(res1), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        res2 = MathTex(
            r"\text{Res}(f, 2) = \frac{e^2}{2-1} = e^2",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.center_in_content(res2)
        self.play(Write(res2), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        # Final answer
        answer = MathTex(
            r"= 2\pi i \cdot (-e + e^2)",
            r"= 2\pi i (e^2 - e)",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([DIM, ACCENT]):
            if i < len(answer):
                answer[i].set_color(col)
        box = self.ly.formula_box(answer, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        insight = Text(
            "Just algebra — no parameterization!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=box, buff=0.4)
        self.play(FadeIn(insight, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 5: Application to Real Integrals ~60s

    def scene5_real_integral(self):
        self.add_subcaption(
            "Here is the payoff of the entire complex analysis playlist. "
            "We can evaluate real integrals using the Residue Theorem. "
            "Consider the integral from negative infinity to infinity "
            "of one over x squared plus one dx. In calculus, this "
            "requires the arctangent substitution and gives pi. Using "
            "complex analysis, consider the function one over z squared "
            "plus one integrated around a semicircle in the upper half "
            "plane. The singularities are at z equals i and z equals "
            "negative i. Only z equals i is inside our contour. The "
            "residue there is one over two i. By the Residue Theorem, "
            "the integral equals two pi i times one over two i, which "
            "equals pi. The same result, obtained by finding one residue!",
            duration=60,
        )
        self.ly.section_divider(4, "Evaluating Real Integrals")

        # The real integral
        real_int = MathTex(
            r"\int_{-\infty}^{\infty} \frac{1}{x^2 + 1}\,dx",
            r"= \pi",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, ACCENT]):
            if i < len(real_int):
                real_int[i].set_color(col)
        self.ly.center_in_content(real_int)
        self.play(Write(real_int), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Complex setup
        title = Text(
            "Complex method:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(title)
        self.play(Write(title), run_time=FAST)
        self.wait(1)

        f_z = MathTex(
            r"f(z) = \frac{1}{z^2 + 1}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(f_z, DOWN, anchor=title, buff=0.4)
        self.play(Write(f_z), run_time=NORMAL)
        self.wait(2)

        # Semicircle note
        semicircle = Text(
            "Integrate over semicircle in upper half-plane",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(semicircle, DOWN, anchor=f_z, buff=0.3)
        self.play(FadeIn(semicircle, shift=LEFT * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Singularities
        sings = MathTex(
            r"z^2 + 1 = 0 \implies z = i,\; z = -i",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.center_in_content(sings)
        self.play(Write(sings), run_time=NORMAL)
        self.wait(2)

        inside = Text(
            "Only z = i is inside the contour",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(inside, DOWN, anchor=sings, buff=0.4)
        self.play(FadeIn(inside, shift=LEFT * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Residue at i
        res = MathTex(
            r"\text{Res}\!\left(\frac{1}{z^2+1},\, i\right)",
            r"= \frac{1}{2i}",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, RED]):
            if i < len(res):
                res[i].set_color(col)
        self.ly.center_in_content(res)
        self.play(Write(res), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Answer
        answer = MathTex(
            r"= 2\pi i \cdot \frac{1}{2i}",
            r"= \pi",
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
            "Real integral solved by finding one residue!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=box, buff=0.4)
        self.play(FadeIn(insight, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 6: Playlist Recap and Finale ~50s

    def scene6_finale(self):
        self.add_subcaption(
            "This brings our Complex Analysis journey to a close. We "
            "started with complex numbers and their geometry. Then "
            "complex functions, differentiation, and integration. "
            "Cauchy's theorem showed that closed integrals vanish. "
            "Cauchy's Integral Formula gave us boundary determines "
            "interior. The consequences gave us Liouville's theorem "
            "and the Fundamental Theorem of Algebra. Taylor and "
            "Laurent series expanded our toolkit. And finally, the "
            "Residue Theorem gave us the practical payoff. From "
            "complex numbers to evaluating impossible integrals. Thank "
            "you for watching Complex Analysis.",
            duration=50,
        )
        self.ly.section_divider(5, "Complex Analysis: The Journey")

        title = self.ly.title("Playlist Recap")
        self.wait(1)

        points = [
            Text("Complex numbers, functions, limits (V126-128)", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Differentiation and integration (V129-130)", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Cauchy's Theorem + Integral Formula (V131-132)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Consequences: Liouville, FTA (V133)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Taylor, Laurent, Residue Theorem (V134-136)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        self.wait(4)

        self.ly.clear()

        # Final message
        final = Text(
            "From complex numbers to evaluating",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(final)
        self.play(FadeIn(final, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        final2 = Text(
            "impossible integrals.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(final2, DOWN, anchor=final, buff=0.3)
        self.play(FadeIn(final2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Final formula
        final_formula = MathTex(
            r"\oint_\gamma f(z)\,dz = 2\pi i \sum \text{Res}(f, a_k)",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        box = self.ly.formula_box(final_formula, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()
        play_outro(self, "Thank You for Watching!", "Complex Analysis — Complete!")
