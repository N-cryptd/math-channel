"""
Video 135: Laurent Series -- Complex Analysis
TEMPLATE v2 -- Professional quality Manim script

Playlist: Complex Analysis (Video 12 of 13)
Class: Video135_LaurentSeries

Topics: Laurent series for functions with singularities, annulus of convergence,
         analytic part vs principal part, classification of singularities
         (removable, pole, essential), residues as c_{-1}.

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


class Video135_LaurentSeries(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_formula()
        self.scene3_annulus()
        self.scene4_classification()
        self.scene5_residue()
        self.scene6_summary()

    # --- Scene 1: Hook -- "What About Singularities?" ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "In the last video we saw that Taylor series converge in "
            "disks, stopping at the nearest singularity. But what if "
            "we want to represent a function near a singularity itself? "
            "Taylor series fail here because they only have positive "
            "powers. Laurent series generalize Taylor series by "
            "including negative powers, and they converge in annuli, "
            "not disks. An annulus is a region between two concentric "
            "circles, like a ring. This is Video 12 of Complex Analysis.",
            duration=50,
        )
        play_intro(self, "Laurent Series", "Complex Analysis")

        # Visual: annulus
        plane = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-1.8, 1.8, 1],
            x_length=4, y_length=3,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.3)

        # Outer circle
        outer = Circle(radius=1.8, color=SECONDARY, stroke_width=2.5)
        outer.move_to(plane.c2p(0, 0))
        self.play(Create(outer), run_time=NORMAL)

        # Inner circle (hole)
        inner = Circle(radius=0.5, color=RED, stroke_width=2.5)
        inner.move_to(plane.c2p(0, 0))
        self.play(Create(inner), run_time=NORMAL)

        # Singularity at center
        sing = Dot(point=plane.c2p(0, 0), color=RED, radius=0.06)
        self.play(FadeIn(sing), run_time=FAST)
        s_lbl = MathTex(r"a", font_size=LABEL_SIZE, color=RED)
        s_lbl.next_to(sing, DOWN, buff=0.15)
        self.play(Write(s_lbl), run_time=FAST)
        self.wait(2)

        r_lbl = MathTex(r"r", font_size=LABEL_SIZE, color=RED)
        r_lbl.next_to(inner.get_top(), RIGHT, buff=0.1)
        R_lbl = MathTex(r"R", font_size=LABEL_SIZE, color=SECONDARY)
        R_lbl.next_to(outer.get_top(), RIGHT, buff=0.1)
        self.play(Write(r_lbl), Write(R_lbl), run_time=FAST)
        self.wait(3)

        caption = Text(
            "Converges in the annulus r < |z-a| < R",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(caption, DOWN, anchor=plane, buff=0.3)
        self.play(FadeIn(caption, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: The Laurent Series Formula ~55s

    def scene2_formula(self):
        self.add_subcaption(
            "If f is analytic in the annulus r less than absolute z "
            "minus a less than R, then f of z equals the sum from "
            "n equals negative infinity to infinity of c sub n times "
            "z minus a to the n. We can split this into two parts. "
            "The sum from n equals zero to infinity gives the analytic "
            "part with positive powers, converging for absolute z "
            "minus a less than R. The sum from n equals one to infinity "
            "gives the principal part with negative powers, converging "
            "for absolute z minus a greater than r. Together they "
            "converge in the annulus.",
            duration=55,
        )
        self.ly.section_divider(1, "The Laurent Series Formula")

        # Full formula
        series = MathTex(
            r"f(z) = \sum_{n=-\infty}^{\infty} c_n (z-a)^n",
            font_size=HEADING_SIZE, color=WHITE,
        )
        box = self.ly.formula_box(series, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Split into two parts
        split_title = Text(
            "Split into two parts:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(split_title)
        self.play(Write(split_title), run_time=FAST)
        self.wait(1)

        analytic = MathTex(
            r"\underbrace{\sum_{n=0}^{\infty} c_n (z-a)^n}_{\text{analytic part}}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(analytic, DOWN, anchor=split_title, buff=0.5)
        self.play(Write(analytic), run_time=NORMAL)
        self.wait(2)

        principal = MathTex(
            r"+ \underbrace{\sum_{n=1}^{\infty} c_{-n} (z-a)^{-n}}_{\text{principal part}}",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(principal, DOWN, anchor=analytic, buff=0.4)
        self.play(Write(principal), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Coefficient formula
        coeff_title = Text(
            "Same CIF formula for ALL n (including negative!):",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.center_in_content(coeff_title)
        self.play(FadeIn(coeff_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        coeff = MathTex(
            r"c_n = \frac{1}{2\pi i}",
            r"\oint_\gamma \frac{f(z)}{(z-a)^{n+1}}\,dz",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([DIM, ACCENT]):
            if i < len(coeff):
                coeff[i].set_color(col)
        self.ly.safe_place(coeff, DOWN, anchor=coeff_title, buff=0.4)
        self.play(Write(coeff), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 3: The Annulus of Convergence ~55s

    def scene3_annulus(self):
        self.add_subcaption(
            "The Laurent series converges in an annulus. The inner "
            "boundary is determined by the singularity at the center, "
            "and the outer boundary by the next nearest singularity. "
            "For example, one over z times z minus one expanded about "
            "z equals one has singularities at z equals zero and z "
            "equals one. The annulus of convergence for this Laurent "
            "series is zero less than absolute z less than one. "
            "The singularities are the roadblocks, just like for "
            "Taylor series, but now we have one on each side.",
            duration=55,
        )
        self.ly.section_divider(2, "Annulus of Convergence")

        # Visual example
        plane = Axes(
            x_range=[-0.5, 1.5, 0.5], y_range=[-1.2, 1.2, 0.5],
            x_length=4, y_length=3,
            axis_config={"include_numbers": True, "font_size": LABEL_SIZE},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.3)

        # Singularity at z=0
        s1 = Dot(point=plane.c2p(0, 0), color=RED, radius=0.06)
        self.play(FadeIn(s1), run_time=FAST)
        s1_lbl = MathTex(r"z=0", font_size=LABEL_SIZE, color=RED)
        s1_lbl.next_to(s1, DOWN, buff=0.15)
        self.play(Write(s1_lbl), run_time=FAST)

        # Singularity at z=1
        s2 = Dot(point=plane.c2p(1, 0), color=RED, radius=0.06)
        self.play(FadeIn(s2), run_time=FAST)
        s2_lbl = MathTex(r"z=1", font_size=LABEL_SIZE, color=RED)
        s2_lbl.next_to(s2, DOWN, buff=0.15)
        self.play(Write(s2_lbl), run_time=FAST)
        self.wait(1)

        # Outer boundary
        outer_circ = Circle(radius=1.0, color=SECONDARY, stroke_width=2.5)
        outer_circ.move_to(plane.c2p(0, 0))
        self.play(Create(outer_circ), run_time=NORMAL)
        self.wait(2)

        # Annulus label
        ann_lbl = MathTex(
            r"0 < |z| < 1",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(ann_lbl, DOWN, anchor=plane, buff=0.3)
        self.play(Write(ann_lbl), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # The function and series
        func = MathTex(
            r"f(z) = \frac{1}{z(z-1)}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(func)
        self.play(Write(func), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

    # --- Scene 4: Classification of Singularities ~60s

    def scene4_classification(self):
        self.add_subcaption(
            "The principal part of the Laurent series tells us "
            "exactly what kind of singularity we have. There are three "
            "types. First, removable singularities. The principal "
            "part is empty, no negative powers at all. For example, "
            "sine of z over z at z equals zero. Just fill in the "
            "hole. Second, poles. The principal part has finitely "
            "many terms. For example, one over z cubed has a pole of "
            "order three. Third, essential singularities. The "
            "principal part has infinitely many terms. For example, "
            "e to the one over z at z equals zero. The principal "
            "part IS the singularity. It tells you exactly what "
            "kind you have.",
            duration=60,
        )
        self.ly.section_divider(3, "Classification of Singularities")

        # Title
        title = Text(
            "Three types of singularity:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(title)
        self.play(Write(title), run_time=FAST)
        self.wait(1)

        # Type 1: Removable
        t1 = MathTex(
            r"\text{Removable: } \text{no principal part}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(t1, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(t1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        e1 = MathTex(
            r"\frac{\sin z}{z} = 1 - \frac{z^2}{6} + \cdots",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(e1, DOWN, anchor=t1, buff=0.3)
        self.play(Write(e1), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Type 2: Pole
        t2_title = Text(
            "Pole: finitely many negative powers",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.center_in_content(t2_title)
        self.play(Write(t2_title), run_time=FAST)
        self.wait(1)

        e2 = MathTex(
            r"\frac{1}{z^3}: \quad c_{-3} = 1, \text{ others } = 0",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(e2, DOWN, anchor=t2_title, buff=0.4)
        self.play(Write(e2), run_time=FAST)
        self.wait(1)

        order = MathTex(
            r"\text{Pole of order 3}",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(order, DOWN, anchor=e2, buff=0.3)
        self.play(Write(order), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Type 3: Essential
        t3_title = Text(
            "Essential: infinitely many negative powers",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.center_in_content(t3_title)
        self.play(Write(t3_title), run_time=FAST)
        self.wait(1)

        e3 = MathTex(
            r"e^{1/z} = 1 + \frac{1}{z} + \frac{1}{2!z^2} + \cdots",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(e3, DOWN, anchor=t3_title, buff=0.4)
        self.play(Write(e3), run_time=FAST)
        self.wait(3)

        wild = Text(
            "Wild behavior near z=0!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(wild, DOWN, anchor=e3, buff=0.3)
        self.play(FadeIn(wild, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 5: The Residue ~50s

    def scene5_residue(self):
        self.add_subcaption(
            "The residue of f at a is c sub negative one, the "
            "coefficient of one over z minus a in the Laurent "
            "series. Why does this single coefficient matter so much? "
            "Because it is the only term that contributes a nonzero "
            "integral around a. For all n except negative one, the "
            "integral of z minus a to the n around a closed contour "
            "is zero. But for n equals negative one, the integral "
            "equals two pi i. So the residue gives the value of the "
            "contour integral around the singularity. Next time we "
            "will use residues to evaluate real integrals, one of the "
            "most powerful applications of complex analysis.",
            duration=50,
        )
        self.ly.section_divider(4, "The Residue")

        # Definition
        residue_def = MathTex(
            r"\text{Res}(f, a) = c_{-1}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        box = self.ly.formula_box(residue_def, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Why it matters
        why_title = Text(
            "Why c_{-1} matters:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(why_title)
        self.play(Write(why_title), run_time=FAST)
        self.wait(1)

        integral_check = MathTex(
            r"\oint_\gamma (z-a)^n\,dz",
            r"= 0",
            r"\;\; \forall n \neq -1",
            font_size=BODY_SIZE,
        )
        for i, col in enumerate([WHITE, SECONDARY, DIM]):
            if i < len(integral_check):
                integral_check[i].set_color(col)
        self.ly.safe_place(integral_check, DOWN, anchor=why_title, buff=0.5)
        self.play(Write(integral_check), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # But for n=-1
        except_term = MathTex(
            r"\oint_\gamma \frac{1}{z-a}\,dz",
            r"= 2\pi i",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([WHITE, ACCENT]):
            if i < len(except_term):
                except_term[i].set_color(col)
        box2 = self.ly.formula_box(except_term, color=ACCENT)
        self.ly.center_in_content(box2)
        self.play(Write(box2), run_time=NORMAL)
        self.wait(3)

        # So
        so_text = MathTex(
            r"\oint_\gamma f(z)\,dz = 2\pi i \cdot \text{Res}(f, a)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(so_text, DOWN, anchor=box2, buff=0.4)
        self.play(Write(so_text), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 6: Summary and Preview ~45s

    def scene6_summary(self):
        self.add_subcaption(
            "Let's recap. Laurent series generalize Taylor series by "
            "including negative powers. They converge in annuli "
            "between singularities. The principal part classifies "
            "singularities as removable, poles, or essential. And the "
            "residue, the coefficient of one over z minus a, gives "
            "the value of contour integrals. This is the foundation "
            "for residue theory, which we will explore next time.",
            duration=45,
        )
        self.ly.section_divider(5, "Summary")

        title = self.ly.title("Key Takeaways")
        self.wait(1)

        points = [
            Text("Laurent series = analytic part + principal part", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Converge in annuli between singularities", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Classification: removable / pole / essential", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Residue = c_{-1} (key for integration)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        self.wait(3)

        self.ly.clear()

        # Final formula
        final = MathTex(
            r"\oint_\gamma f(z)\,dz = 2\pi i \cdot \text{Res}(f, a)",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        box = self.ly.formula_box(final, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()
        play_outro(self, "The Residue Theorem", "Complex Analysis")
