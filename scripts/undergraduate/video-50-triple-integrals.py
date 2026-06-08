"""
Video 50: Triple Integrals
Calculus III -- Multivariable Playlist -- Video 10 of 14

Covers: extending double integrals to 3D, iterated triple integrals,
Fubini extension, changing order in 3D, applications (mass,
center of mass, moments of inertia).

Render draft:  manim -ql scripts/undergraduate/video-50-triple-integrals.py Video50_TripleIntegrals
Render final:  manim -qh scripts/undergraduate/video-50-triple-integrals.py Video50_TripleIntegrals
"""

from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video50_TripleIntegrals(Scene):
    """Full video: Triple Integrals."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_iterated()
        self.scene4_worked_example()
        self.scene5_changing_order()
        self.scene6_applications_mass()
        self.scene7_moments()
        self.scene8_summary()

    # ── Scene 1: Hook — From 2D to 3D ───────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "We've mastered double integrals over flat regions in the "
            "plane. Now we extend integration into three dimensions. "
            "What if a solid has varying density throughout its volume?",
            duration=18,
        )
        play_intro(self, "Triple Integrals",
                   "Calculus III -- Multivariable")

        title = self.ly.title("From Flat Regions to Solid Objects")

        # 2D reminder
        reminder = Text(
            "Double integral: integrate f over a region in the xy-plane",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(reminder, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(reminder, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # 3D extension
        extension = Text(
            "Triple integral: integrate f over a solid in 3D space",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(extension, DOWN, anchor=reminder, buff=0.5)
        self.play(FadeIn(extension, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Motivation
        motivation = Text(
            "Real-world question: What is the mass of a solid "
            "whose density varies from point to point?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(motivation, DOWN, anchor=extension, buff=0.4)
        ensure_fits(motivation)
        self.play(FadeIn(motivation, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 2: The Triple Integral Definition ──────────────────
    def scene2_definition(self):
        self.add_subcaption(
            "Just like before, we partition the region into small boxes, "
            "evaluate the function at sample points, sum up, and take "
            "the limit as the boxes shrink to zero volume.",
            duration=18,
        )
        self.ly.section_divider(1, "The Triple Integral")

        title = self.ly.title("Definition of the Triple Integral")

        # Steps
        step1 = Text(
            "1. Partition the 3D region E into small boxes of volume \u0394V",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(step1, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(step1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        step2 = Text(
            "2. At each sample point, evaluate f(x*, y*, z*)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(step2, DOWN, anchor=step1, buff=0.3)
        self.play(FadeIn(step2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        step3 = Text(
            "3. Sum f \u00b7 \u0394V over all boxes, then take the limit",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(step3, DOWN, anchor=step2, buff=0.3)
        self.play(FadeIn(step3, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Formula
        self.play(FadeOut(step1), FadeOut(step2), FadeOut(step3), run_time=FAST)

        formula = MathTex(
            r"\iiint_E f(x,y,z)\,dV",
            r"=",
            r"\lim \sum_{i,j,k}",
            r"f(x_i^*, y_j^*, z_k^*)",
            r"\Delta V",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula[3].set_color(ACCENT)
        formula[4].set_color(SECONDARY)
        self.ly.safe_place(formula, DOWN, anchor=title, buff=0.5)
        self.play(Write(formula), run_time=SLOW)
        self.wait(2.5)
        self.ly.clear()

    # ── Scene 3: Iterated Triple Integrals ────────────────────────
    def scene3_iterated(self):
        self.add_subcaption(
            "Fubini's theorem extends to three dimensions. We evaluate "
            "the triple integral as three nested single integrals. The "
            "innermost integral is evaluated first, working outward.",
            duration=18,
        )
        self.ly.section_divider(2, "Iterated Triple Integrals")

        title = self.ly.title("Evaluating Triple Integrals")

        # General form
        label = Text(
            "For a region E with appropriate bounds:",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        formula = MathTex(
            r"\iiint_E f\,dV",
            r"=",
            r"\int_a^b \int_{g_1(x)}^{g_2(x)} \int_{h_1(x,y)}^{h_2(x,y)}",
            r"f(x,y,z)\,dz\,dy\,dx",
            font_size=BODY_SIZE, color=WHITE,
        )
        formula[2].set_color(PRIMARY)
        formula[3].set_color(ACCENT)
        self.ly.safe_place(formula, DOWN, anchor=label, buff=0.4)
        ensure_fits(formula)
        self.play(Write(formula), run_time=SLOW)
        self.wait(1.5)

        # Key note
        self.play(FadeOut(label), FadeOut(formula), run_time=FAST)

        note1 = Text(
            "Innermost bounds can depend on BOTH outer variables",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(note1, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(note1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        note2 = Text(
            "6 possible orders: dzdydx, dydzdx, dxdzdy, ...",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note2, DOWN, anchor=note1, buff=0.3)
        self.play(FadeIn(note2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 4: Worked Example — Volume of a Tetrahedron ───────
    def scene4_worked_example(self):
        self.add_subcaption(
            "Let's compute the volume of the tetrahedron in the first "
            "octant bounded by the coordinate planes and the plane "
            "x plus y plus z equals one. This is a classic example.",
            duration=18,
        )
        self.ly.section_divider(3, "Worked Example")

        title = self.ly.title("Volume of a Tetrahedron")

        # Region description
        problem = Text(
            "Region: x \u2265 0, y \u2265 0, z \u2265 0, x + y + z \u2264 1",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(problem, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(problem, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Setup
        setup = MathTex(
            r"V = \int_0^1 \int_0^{1-x} \int_0^{1-x-y} dz\,dy\,dx",
            font_size=HEADING_SIZE, color=WHITE,
        )
        setup.set_color(PRIMARY)
        self.ly.safe_place(setup, DOWN, anchor=problem, buff=0.4)
        self.play(Write(setup), run_time=NORMAL)
        self.wait(1)

        # Inner integral
        self.play(FadeOut(setup), run_time=FAST)

        inner = MathTex(
            r"\int_0^{1-x-y} dz = 1 - x - y",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(inner, DOWN, anchor=problem, buff=0.4)
        self.play(Write(inner), run_time=NORMAL)
        self.wait(1)

        # Middle integral
        self.play(FadeOut(inner), run_time=FAST)

        middle = MathTex(
            r"\int_0^{1-x} (1-x-y)\,dy = (1-x)^2 - \tfrac{1}{2}(1-x)^2",
            r"= \tfrac{1}{2}(1-x)^2",
            font_size=BODY_SIZE, color=WHITE,
        )
        middle[1].set_color(SECONDARY)
        self.ly.safe_place(middle, DOWN, anchor=problem, buff=0.4)
        ensure_fits(middle)
        self.play(Write(middle), run_time=SLOW)
        self.wait(1)

        # Outer integral
        self.play(FadeOut(middle), run_time=FAST)

        outer = MathTex(
            r"\int_0^1 \tfrac{1}{2}(1-x)^2\,dx",
            r"= \tfrac{1}{2}\left[-\tfrac{1}{3}(1-x)^3\right]_0^1",
            r"= \tfrac{1}{2} \cdot \tfrac{1}{3}",
            r"= \tfrac{1}{6}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        outer[3].set_color(ACCENT)
        self.ly.safe_place(outer, DOWN, anchor=problem, buff=0.4)
        ensure_fits(outer)
        self.play(Write(outer), run_time=SLOW)
        self.wait(2.5)
        self.ly.clear()

    # ── Scene 5: Changing Order in 3D ────────────────────────────
    def scene5_changing_order(self):
        self.add_subcaption(
            "Just like with double integrals, changing the order of "
            "integration in three dimensions can simplify the computation. "
            "There are six possible orders to choose from.",
            duration=18,
        )
        self.ly.section_divider(4, "Changing the Order")

        title = self.ly.title("Six Orders of Integration")

        # The six orders
        orders = [
            Text("dz dy dx", font_size=BODY_SIZE, color=PRIMARY, font=MONO),
            Text("dz dx dy", font_size=BODY_SIZE, color=PRIMARY, font=MONO),
            Text("dy dz dx", font_size=BODY_SIZE, color=SECONDARY, font=MONO),
            Text("dy dx dz", font_size=BODY_SIZE, color=SECONDARY, font=MONO),
        ]
        self.ly.progressive_reveal(orders, start_from=title)
        self.wait(1)

        # Remaining two
        orders2 = [
            Text("dx dz dy", font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("dx dy dz", font_size=BODY_SIZE, color=ACCENT, font=MONO),
        ]
        # These should replace the first two as they appear
        remaining = Text(
            "... and dx dz dy, dx dy dz",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(remaining, DOWN, anchor=title, buff=3.0)
        self.play(FadeIn(remaining, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Key insight
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if not hasattr(mob, '_is_background')],
            run_time=FAST,
        )

        tip = Text(
            "Choose the order that gives the simplest bounds!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(tip)
        self.play(FadeIn(tip, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 6: Applications — Mass and Center of Mass ──────────
    def scene6_applications_mass(self):
        self.add_subcaption(
            "Triple integrals have powerful applications in physics and "
            "engineering. If density varies throughout a solid, the mass "
            "is the triple integral of the density function.",
            duration=18,
        )
        self.ly.section_divider(5, "Applications: Mass and Center of Mass")

        title = self.ly.title("Mass of a Solid with Variable Density")

        # Mass formula
        mass_label = Text(
            "If \u03b4(x,y,z) is the density at each point:",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(mass_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(mass_label, shift=LEFT * 0.15), run_time=NORMAL)

        mass_formula = MathTex(
            r"M",
            r"=",
            r"\iiint_E \delta(x,y,z)\,dV",
            font_size=HEADING_SIZE, color=WHITE,
        )
        mass_formula[0].set_color(ACCENT)
        mass_formula[2].set_color(PRIMARY)
        self.ly.safe_place(mass_formula, DOWN, anchor=mass_label, buff=0.3)
        self.play(Write(mass_formula), run_time=NORMAL)
        self.wait(1.5)

        # Center of mass
        self.play(FadeOut(mass_label), FadeOut(mass_formula), run_time=FAST)

        com_label = Text(
            "Center of mass coordinates:",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(com_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(com_label, shift=LEFT * 0.15), run_time=NORMAL)

        com = MathTex(
            r"\bar{x} = \frac{1}{M}\iiint_E x\,\delta\,dV",
            r"\qquad",
            r"\bar{y} = \frac{1}{M}\iiint_E y\,\delta\,dV",
            r"\qquad",
            r"\bar{z} = \frac{1}{M}\iiint_E z\,\delta\,dV",
            font_size=BODY_SIZE, color=WHITE,
        )
        com[0].set_color(PRIMARY)
        com[2].set_color(SECONDARY)
        com[4].set_color(ACCENT)
        self.ly.safe_place(com, DOWN, anchor=com_label, buff=0.3)
        ensure_fits(com)
        self.play(Write(com), run_time=SLOW)
        self.wait(2)
        self.ly.clear()

    # ── Scene 7: Moments of Inertia ─────────────────────────────
    def scene7_moments(self):
        self.add_subcaption(
            "The moment of inertia measures resistance to rotational "
            "acceleration. For a solid body, it depends on the distance "
            "from each point to the axis of rotation.",
            duration=18,
        )
        self.ly.section_divider(6, "Moments of Inertia")

        title = self.ly.title("Moments of Inertia")

        # About each axis
        ix_label = Text("About the x-axis:", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        self.ly.safe_place(ix_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(ix_label, shift=LEFT * 0.15), run_time=NORMAL)

        ix = MathTex(
            r"I_x = \iiint_E (y^2 + z^2)\,\delta\,dV",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(ix, DOWN, anchor=ix_label, buff=0.3)
        self.play(Write(ix), run_time=NORMAL)
        self.wait(1.5)

        # About y-axis
        self.play(FadeOut(ix_label), FadeOut(ix), run_time=FAST)

        iy_label = Text("About the y-axis:", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(iy_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(iy_label, shift=LEFT * 0.15), run_time=NORMAL)

        iy = MathTex(
            r"I_y = \iiint_E (x^2 + z^2)\,\delta\,dV",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(iy, DOWN, anchor=iy_label, buff=0.3)
        self.play(Write(iy), run_time=NORMAL)
        self.wait(1.5)

        # About z-axis
        self.play(FadeOut(iy_label), FadeOut(iy), run_time=FAST)

        iz_label = Text("About the z-axis:", font_size=BODY_SIZE, color=ACCENT, font=SANS)
        self.ly.safe_place(iz_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(iz_label, shift=LEFT * 0.15), run_time=NORMAL)

        iz = MathTex(
            r"I_z = \iiint_E (x^2 + y^2)\,\delta\,dV",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(iz, DOWN, anchor=iz_label, buff=0.3)
        self.play(Write(iz), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 8: Summary and Recap ──────────────────────────────
    def scene8_summary(self):
        self.add_subcaption(
            "To recap: triple integrals extend double integrals into "
            "three dimensions. We evaluate them as three nested single "
            "integrals, and there are six possible orders. Key applications "
            "include volume, mass, center of mass, and moments of inertia.",
            duration=24,
        )
        self.ly.section_divider(7, "Summary")

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "Triple integral extends integration to solid objects in 3D",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Evaluate as three nested single integrals (Fubini extends)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "6 possible orders \u2014 choose the simplest bounds",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Applications: volume, mass, center of mass, inertia",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

        play_outro(
            self,
            "Line Integrals",
            "Calculus III -- Multivariable",
        )
