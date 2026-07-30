"""
Video 138: Conformal Mappings -- Complex Analysis
TEMPLATE v2 -- Professional quality Manim script

Playlist: Complex Analysis (Video 15 of 15 — FINAL)
Class: Video138_ConformalMappings

Topics: Conformal mappings, angle preservation, derivative condition,
         Möbius transformations, visualizing grid mappings,
         applications to PDEs, playlist finale.

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


class Video138_ConformalMappings(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_what_conformal()
        self.scene3_mobius()
        self.scene4_visualizing()
        self.scene5_applications()
        self.scene6_finale()

    # --- Scene 1: Hook -- "Preserving Angles" ~50s

    def scene1_hook(self):
        self.add_subcaption(
            "We have explored integration, series, residues, and "
            "zeros. One last topic: geometry. A conformal mapping is "
            "a function that preserves angles. Curves that cross at "
            "ninety degrees in the z plane also cross at ninety "
            "degrees in the w plane. The key condition is that the "
            "derivative is nonzero. Conformal mappings are used to "
            "solve partial differential equations by transforming "
            "complicated domains into simple ones. This is the final "
            "video of Complex Analysis.",
            duration=50,
        )
        play_intro(self, "Conformal Mappings", "Complex Analysis")

        # Visual: two perpendicular curves
        plane = Axes(
            x_range=[-2, 2, 1], y_range=[-1.5, 1.5, 1],
            x_length=4, y_length=3,
            axis_config={"include_numbers": False},
            color=PRIMARY,
        )
        self.ly.center_in_content(plane)
        self.play(Create(plane), run_time=FAST)
        self.wait(0.3)

        # Horizontal line
        h_line = Line(
            start=plane.c2p(-1.5, 0.3), end=plane.c2p(1.5, 0.3),
            color=SECONDARY, stroke_width=2,
        )
        self.play(Create(h_line), run_time=NORMAL)

        # Vertical line
        v_line = Line(
            start=plane.c2p(0.5, -1.2), end=plane.c2p(0.5, 1.2),
            color=PRIMARY, stroke_width=2,
        )
        self.play(Create(v_line), run_time=NORMAL)

        # Intersection point
        inter = Dot(point=plane.c2p(0.5, 0.3), color=ACCENT, radius=0.06)
        self.play(FadeIn(inter), run_time=FAST)

        # Angle marker
        angle = Arc(
            radius=0.2, start_angle=0, angle=PI / 2,
            color=ACCENT, stroke_width=2,
        )
        angle.move_to(plane.c2p(0.5, 0.3))
        self.play(Create(angle), run_time=FAST)

        angle_lbl = MathTex(r"90°", font_size=LABEL_SIZE, color=ACCENT)
        angle_lbl.next_to(angle, UR, buff=0.05)
        self.play(Write(angle_lbl), run_time=FAST)
        self.wait(3)

        # Arrow to w-plane
        z_lbl = MathTex(r"z\text{-plane}", font_size=LABEL_SIZE, color=PRIMARY)
        z_lbl.next_to(plane, LEFT, buff=0.3)
        self.play(Write(z_lbl), run_time=FAST)

        arrow_text = Text(
            "Angles preserved!",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(arrow_text, DOWN, anchor=plane, buff=0.3)
        self.play(FadeIn(arrow_text, shift=UP * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: What Makes a Mapping Conformal? ~55s

    def scene2_what_conformal(self):
        self.add_subcaption(
            "When is a mapping conformal? A function f is conformal at "
            "z zero if f prime of z zero is not zero. Here is why. "
            "Near z zero, f of z zero plus h is approximately f of z "
            "zero plus f prime of z zero times h. The factor f prime of "
            "z zero is a complex number, which means it scales by its "
            "magnitude and rotates by its argument. Scaling changes "
            "lengths and rotation changes direction, but angles between "
            "vectors are preserved because both vectors get the same "
            "rotation. When f prime equals zero, this breaks down and "
            "angles can change.",
            duration=55,
        )
        self.ly.section_divider(1, "The Conformality Condition")

        # Theorem
        statement = MathTex(
            r"f'(z_0) \neq 0",
            r"\;\Longrightarrow\;",
            r"f \text{ is conformal at } z_0",
            font_size=HEADING_SIZE,
        )
        for i, col in enumerate([RED, DIM, ACCENT]):
            if i < len(statement):
                statement[i].set_color(col)
        box = self.ly.formula_box(statement, color=ACCENT)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Why
        title = Text(
            "Why it works:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(title)
        self.play(Write(title), run_time=FAST)
        self.wait(1)

        approx = MathTex(
            r"f(z_0 + h) \approx f(z_0) + f'(z_0) \cdot h",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(approx, DOWN, anchor=title, buff=0.4)
        self.play(Write(approx), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        # f'(z0) = re^{iθ}
        polar = MathTex(
            r"f'(z_0) = re^{i\theta}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(polar)
        self.play(Write(polar), run_time=NORMAL)
        self.wait(2)

        interp = [
            Text("r: scales all lengths", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("θ: rotates all directions", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Same rotation for all vectors → angles preserved", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(interp, start_from=polar)
        self.wait(5)

        self.ly.clear()

    # --- Scene 3: Möbius Transformations ~60s

    def scene3_mobius(self):
        self.add_subcaption(
            "The most important conformal mappings are the Möbius "
            "transformations. A Möbius transformation has the form T "
            "of z equals a z plus b over c z plus d, where a d minus "
            "b c is nonzero. These transformations always preserve "
            "angles. They also map circles and lines to circles and "
            "lines, and they are invertible. A beautiful example: T of "
            "z equals z minus i over z plus i maps the upper half "
            "plane to the unit disk. The real line maps to the unit "
            "circle, and i maps to the origin. Möbius transformations "
            "are the conformal automorphisms of the Riemann sphere.",
            duration=60,
        )
        self.ly.section_divider(2, "Möbius Transformations")

        # Definition
        mobius = MathTex(
            r"T(z) = \frac{az + b}{cz + d}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(mobius)
        self.play(Write(mobius), run_time=NORMAL)
        self.wait(2)

        condition = MathTex(
            r"ad - bc \neq 0",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(condition, DOWN, anchor=mobius, buff=0.4)
        self.play(Write(condition), run_time=FAST)
        self.wait(3)

        self.ly.clear()

        # Properties
        props = [
            Text("Preserve angles (conformal)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Map circles/lines to circles/lines", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Invertible: T^{-1} is also Möbius", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        prop_title = self.ly.title("Properties")
        self.ly.progressive_reveal(props, start_from=prop_title)
        self.wait(4)

        self.ly.clear()

        # Example: maps upper half-plane to unit disk
        example = MathTex(
            r"T(z) = \frac{z - i}{z + i}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(example)
        self.play(Write(example), run_time=NORMAL)
        self.wait(2)

        mapping = [
            Text("Upper half-plane → unit disk", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Real line → unit circle", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("z = i → w = 0 (origin)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(mapping, start_from=example)
        self.wait(5)

        self.ly.clear()

    # --- Scene 4: Visualizing a Conformal Map ~55s

    def scene4_visualizing(self):
        self.add_subcaption(
            "Let's visualize w equals z squared. This mapping doubles "
            "angles and squares magnitudes. In the z plane, draw "
            "horizontal and vertical lines. In the w plane, these "
            "become parabolas. The first quadrant maps to the upper "
            "half plane. At z equals zero, the derivative is zero, so "
            "the map is not conformal there. Angles double at the "
            "origin. But everywhere else, angles are preserved. "
            "Conformal everywhere except at critical points where "
            "the derivative vanishes.",
            duration=55,
        )
        self.ly.section_divider(3, "Visualizing w = z^2")

        # The mapping
        mapping = MathTex(
            r"w = z^2",
            font_size=TITLE_SIZE, color=WHITE,
        )
        self.ly.center_in_content(mapping)
        self.play(Write(mapping), run_time=NORMAL)
        self.wait(2)

        # Derivative condition
        deriv = MathTex(
            r"\frac{dw}{dz} = 2z",
            r"\quad \Rightarrow \quad \text{conformal } (z \neq 0)",
            font_size=BODY_SIZE,
        )
        for i, col in enumerate([PRIMARY, ACCENT]):
            if i < len(deriv):
                deriv[i].set_color(col)
        self.ly.safe_place(deriv, DOWN, anchor=mapping, buff=0.5)
        self.play(Write(deriv), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Mapping description
        desc = [
            Text("Horizontal lines → parabolas", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Vertical lines → parabolas", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("First quadrant → upper half-plane", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("At z=0: angles DOUBLE (not conformal!)", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        desc_title = self.ly.title("What happens to the grid:")
        self.ly.progressive_reveal(desc, start_from=desc_title)
        self.wait(5)

        self.ly.clear()

        # Key insight
        insight = Text(
            "Conformal everywhere except critical points",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        box = self.ly.formula_box(insight, color=SECONDARY)
        self.ly.center_in_content(box)
        self.play(Write(box), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 5: Applications ~50s

    def scene5_applications(self):
        self.add_subcaption(
            "Conformal mappings have powerful applications. They are "
            "used to solve partial differential equations by "
            "transforming complicated domains into simple ones. "
            "Map the complicated domain to a disk or half plane, "
            "solve the equation there where it is easy, then map "
            "the solution back. The Riemann Mapping Theorem "
            "guarantees that for any simply connected domain that is "
            "not the whole plane, there exists a conformal map to the "
            "unit disk. This means conformal mappings can always "
            "simplify our problems.",
            duration=50,
        )
        self.ly.section_divider(4, "Applications")

        # Application flow
        title = self.ly.title("The Strategy")
        self.wait(1)

        steps = [
            Text("1. Map complicated domain to simple one", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Solve PDE in simple domain", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Map solution back to original domain", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(steps, start_from=title)
        self.wait(4)

        self.ly.clear()

        # Riemann Mapping Theorem
        rmt_title = Text(
            "Riemann Mapping Theorem:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(rmt_title)
        self.play(Write(rmt_title), run_time=FAST)
        self.wait(1)

        rmt = Text(
            "Every simply-connected domain ≠ C maps",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(rmt, DOWN, anchor=rmt_title, buff=0.4)
        self.play(FadeIn(rmt, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        rmt2 = Text(
            "conformally onto the unit disk",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(rmt2, DOWN, anchor=rmt, buff=0.3)
        self.play(FadeIn(rmt2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 6: Playlist Finale ~50s

    def scene6_finale(self):
        self.add_subcaption(
            "And that completes our Complex Analysis journey. We "
            "started with complex numbers and their beautiful geometry. "
            "We explored complex functions, differentiation, and "
            "integration. Cauchy's theorem showed closed integrals "
            "vanish. The Integral Formula revealed boundary determines "
            "interior. Consequences gave us Liouville and the "
            "Fundamental Theorem of Algebra. Taylor and Laurent "
            "series expanded our toolkit. The Residue Theorem gave us "
            "practical power. And conformal mappings revealed the "
            "geometric beauty of complex functions. From complex "
            "numbers to conformal mappings. Thank you for joining me "
            "on this journey through Complex Analysis.",
            duration=50,
        )
        self.ly.section_divider(5, "Complex Analysis: Complete!")

        title = self.ly.title("The Full Journey")
        self.wait(1)

        points = [
            Text("Complex numbers, functions, limits (V126-128)", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Differentiation and integration (V129-130)", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Cauchy's Theorem + Integral Formula (V131-132)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Consequences: Liouville, FTA (V133)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Taylor, Laurent, Residue Theorem (V134-136)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Zeros/Poles + Conformal Mappings (V137-138)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        self.wait(4)

        self.ly.clear()

        # Final message
        final = Text(
            "From complex numbers to conformal mappings.",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(final)
        self.play(FadeIn(final, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        final2 = Text(
            "Thank you for watching Complex Analysis!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(final2, DOWN, anchor=final, buff=0.4)
        self.play(FadeIn(final2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()
        play_outro(self, "", "Complex Analysis — COMPLETE!")
