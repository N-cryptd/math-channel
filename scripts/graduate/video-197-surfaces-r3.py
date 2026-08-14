"""
Video 197: Surfaces in R³ -- Differential Geometry Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video197_SurfacesR3

Topics: Regular surfaces, coordinate charts, atlases, tangent plane,
        normal vector, examples (sphere, cylinder, torus, saddle).

Prerequisites: Video 194 (Curves in R^n), Video 195 (Arc Length & Curvature),
               Video 196 (Frenet-Serret Frame), Linear Algebra, Calculus III.

Quality Rules (mandatory):
1. Max 5 visible elements per scene
2. Use LayoutEngine for ALL positioning
3. Progressive disclosure
4. Narration timing ~12 words / 5s
5. Call ly.clear() between scenes
6. MathTex: raw strings with single backslashes
"""

from manim import *
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video197_SurfacesR3(Scene):
    """Surfaces in R³ -- Differential Geometry Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_parametric_surfaces()
        self.scene4_regularity()
        self.scene5_tangent_plane_normal()
        self.scene6_charts_atlases()
        self.scene7_examples_gallery()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook — From Curves to Surfaces
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "For three videos, we studied curves, "
            "one-dimensional objects in space. Now "
            "we make the jump to two dimensions. A "
            "surface is a sheet, a skin, a membrane "
            "in three-dimensional space.",
            duration=10,
        )
        play_intro(self, "Surfaces in R³", "Differential Geometry")

        title = self.ly.title("From Curves to Surfaces")

        items = [
            Text(
                "Curves: 1D objects (one parameter)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Surfaces: 2D objects (two parameters)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "How do we describe them mathematically?",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Intro + Section Divider
    # ------------------------------------------------------------------ #
    def scene2_intro(self):
        self.ly.section_divider("1", "What is a Surface?")
        self.add_subcaption(
            "Today we define surfaces rigorously. "
            "We start from the familiar idea of a "
            "parametrization, just as we did for "
            "curves, but now with two parameters "
            "instead of one.",
            duration=7,
        )
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Parametric Surfaces
    # ------------------------------------------------------------------ #
    def scene3_parametric_surfaces(self):
        # Curve → surface transition
        self.add_subcaption(
            "A curve is a smooth map from R into "
            "R three with one parameter. A surface "
            "is a smooth map from R squared into R "
            "three with two parameters.",
            duration=7,
        )
        title = self.ly.title("Parametric Surfaces")

        curve_def = MathTex(
            r"\gamma(t) : \mathbb{R} \to \mathbb{R}^3",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(curve_def, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(curve_def), run_time=NORMAL)

        surf_def = MathTex(
            r"\sigma(u,v) : U \subset \mathbb{R}^2 \to \mathbb{R}^3",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(surf_def, direction=DOWN, anchor=curve_def, buff=0.4)
        self.play(FadeIn(surf_def, shift=LEFT * 0.15), run_time=NORMAL)

        dim_note = Text(
            "One parameter → curve    |    Two parameters → surface",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(dim_note, direction=DOWN, anchor=surf_def, buff=0.4)
        self.play(FadeIn(dim_note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Component form
        self.add_subcaption(
            "In components, sigma of u and v "
            "equals x of u and v, y of u and v, "
            "z of u and v. The domain U is an "
            "open set in the plane, and the image "
            "is a surface in three-dimensional space.",
            duration=8,
        )
        title2 = self.ly.title("Component Form")

        comp = MathTex(
            r"\sigma(u,v) = \big(x(u,v),\; y(u,v),\; z(u,v)\big)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(comp, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(comp), run_time=NORMAL)

        domain = Text(
            "Domain U: open set in R²  (e.g., rectangle, disk)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(domain, direction=DOWN, anchor=comp, buff=0.4)
        self.play(FadeIn(domain, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Cylinder example
        self.add_subcaption(
            "The cylinder is parameterized by an "
            "angle and a height. Sigma of u and v "
            "equals cosine u, sine u, v.",
            duration=6,
        )
        title3 = self.ly.title("Example: Cylinder")

        cyl = MathTex(
            r"\sigma(u,v) = (\cos u,\;\sin u,\;v)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(cyl, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(cyl), run_time=NORMAL)

        cyl_note = Text(
            "u in [0, 2pi], v in R",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(cyl_note, direction=DOWN, anchor=cyl, buff=0.4)
        self.play(FadeIn(cyl_note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Regularity Condition
    # ------------------------------------------------------------------ #
    def scene4_regularity(self):
        self.add_subcaption(
            "Not every parametrization describes a "
            "valid surface. We need the partial "
            "derivatives sigma u and sigma v to be "
            "linearly independent everywhere. "
            "Their cross product must never vanish.",
            duration=9,
        )
        title = self.ly.title("Regularity Condition")

        partials = MathTex(
            r"\sigma_u = \frac{\partial \sigma}{\partial u}",
            r",\quad",
            r"\sigma_v = \frac{\partial \sigma}{\partial v}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(partials, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(partials), run_time=NORMAL)

        reg_cond = MathTex(
            r"\sigma_u \times \sigma_v \neq \mathbf{0}",
            r"\quad \Longleftrightarrow \quad",
            r"\text{rank}\, D\sigma = 2",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(reg_cond, direction=DOWN, anchor=partials, buff=0.5)
        self.play(Write(reg_cond), run_time=NORMAL)

        geo = Text(
            "Guarantees a well-defined tangent plane at every point",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(geo, direction=DOWN, anchor=reg_cond, buff=0.4)
        self.play(FadeIn(geo, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Jacobian interpretation
        self.add_subcaption(
            "The Jacobian matrix D sigma has two "
            "columns, sigma u and sigma v. Regularity "
            "means these columns are linearly "
            "independent. If they become parallel, "
            "the surface pinches or forms a cusp.",
            duration=9,
        )
        title2 = self.ly.title("Jacobian Interpretation")

        jac = MathTex(
            r"D\sigma = \begin{bmatrix}",
            r"\dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\[6pt]",
            r"\dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} \\[6pt]",
            r"\dfrac{\partial z}{\partial u} & \dfrac{\partial z}{\partial v}",
            r"\end{bmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(jac, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(jac), run_time=NORMAL)

        rank2 = Text(
            "Rank 2: columns are linearly independent",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(rank2, direction=DOWN, anchor=jac, buff=0.4)
        self.play(FadeIn(rank2, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Tangent Plane and Normal Vector
    # ------------------------------------------------------------------ #
    def scene5_tangent_plane_normal(self):
        self.add_subcaption(
            "At a point p on the surface, the "
            "tangent plane is spanned by sigma u "
            "and sigma v. Every curve on the surface "
            "passing through p has its tangent "
            "vector lying in this plane.",
            duration=8,
        )
        title = self.ly.title("Tangent Plane")

        tplane = MathTex(
            r"T_p S = \mathrm{span}\{\sigma_u,\; \sigma_v\}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(tplane, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(tplane), run_time=NORMAL)

        tp_note = Text(
            "All tangent vectors to curves on S through p",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(tp_note, direction=DOWN, anchor=tplane, buff=0.4)
        self.play(FadeIn(tp_note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Normal vector
        self.add_subcaption(
            "The unit normal vector is the cross "
            "product of the partial derivatives, "
            "normalized. It is perpendicular to "
            "every tangent direction and points "
            "away from the surface.",
            duration=8,
        )
        title2 = self.ly.title("Unit Normal Vector")

        normal = MathTex(
            r"\mathbf{n} = \frac{\sigma_u \times \sigma_v}"
            r"{|\sigma_u \times \sigma_v|}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(normal, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(normal), run_time=NORMAL)

        n_note = Text(
            "Perpendicular to tangent plane at every point",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(n_note, direction=DOWN, anchor=normal, buff=0.4)
        self.play(FadeIn(n_note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Charts and Atlases
    # ------------------------------------------------------------------ #
    def scene6_charts_atlases(self):
        self.ly.section_divider("2", "Coordinate Charts")
        self.ly.clear()

        self.add_subcaption(
            "A single parametrization may not cover "
            "the entire surface. Spherical coordinates "
            "break down at the poles. The solution "
            "is to use multiple overlapping "
            "parametrizations called coordinate charts.",
            duration=9,
        )
        title = self.ly.title("The Problem")

        problem = Text(
            "Spherical coordinates: singular at poles",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(problem, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(problem, shift=LEFT * 0.15), run_time=NORMAL)

        sing = MathTex(
            r"\phi = 0 \text{ or } \pi \;\Longrightarrow\; "
            r"|\sigma_\theta \times \sigma_\phi| = 0",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(sing, direction=DOWN, anchor=problem, buff=0.4)
        self.play(Write(sing), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Atlas solution
        self.add_subcaption(
            "An atlas is a collection of charts whose "
            "images cover the surface. Where charts "
            "overlap, the transition from one set "
            "of coordinates to another must be "
            "smooth. This is the definition of a "
            "regular surface.",
            duration=9,
        )
        title2 = self.ly.title("Atlas Solution")

        items = [
            Text(
                "Chart: smooth parametrization of part of S",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Atlas: collection of charts covering all of S",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Transition maps: smooth coordinate changes",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title2)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Examples Gallery
    # ------------------------------------------------------------------ #
    def scene7_examples_gallery(self):
        # Sphere
        self.add_subcaption(
            "The sphere of radius R uses spherical "
            "coordinates. The cross product of partials "
            "has magnitude R squared sine phi, which is "
            "nonzero away from the poles.",
            duration=7,
        )
        title = self.ly.title("Example: Sphere")

        sphere = MathTex(
            r"\sigma(\theta,\phi) = (R\sin\phi\cos\theta,\;"
            r"R\sin\phi\sin\theta,\;R\cos\phi)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(sphere, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(sphere), run_time=NORMAL)

        sphere_reg = MathTex(
            r"|\sigma_\theta \times \sigma_\phi| = R^2 \sin\phi \neq 0",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(sphere_reg, direction=DOWN, anchor=sphere, buff=0.4)
        self.play(FadeIn(sphere_reg, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Torus
        self.add_subcaption(
            "The torus is parameterized by two angles "
            "u and v, with major radius R and minor "
            "radius r. Regularity requires R greater "
            "than r, so the inner tube never touches "
            "itself.",
            duration=8,
        )
        title2 = self.ly.title("Example: Torus")

        torus = MathTex(
            r"\sigma(u,v) = \big((R + r\cos v)\cos u,\;"
            r"(R + r\cos v)\sin u,\; r\sin v\big)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(torus, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(torus), run_time=NORMAL)

        torus_reg = Text(
            "Regular when R > r (tube doesn't self-intersect)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(torus_reg, direction=DOWN, anchor=torus, buff=0.4)
        self.play(FadeIn(torus_reg, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Saddle
        self.add_subcaption(
            "The saddle surface has a particularly "
            "nice property. Its partial derivatives "
            "are never parallel, so a single chart "
            "covers the entire surface. The "
            "cross product magnitude is always "
            "positive.",
            duration=8,
        )
        title3 = self.ly.title("Example: Saddle Surface")

        saddle = MathTex(
            r"\sigma(u,v) = (u,\; v,\; u^2 - v^2)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(saddle, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(saddle), run_time=NORMAL)

        saddle_reg = MathTex(
            r"|\sigma_u \times \sigma_v| = \sqrt{1 + 4u^2 + 4v^2} > 0",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(saddle_reg, direction=DOWN, anchor=saddle, buff=0.4)
        self.play(FadeIn(saddle_reg, shift=LEFT * 0.15), run_time=NORMAL)

        single_chart = Text(
            "Single chart covers entire surface!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(single_chart, direction=DOWN, anchor=saddle_reg, buff=0.4)
        self.play(FadeIn(single_chart, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary_outro(self):
        self.add_subcaption(
            "Today we defined surfaces as the "
            "two-dimensional objects of differential "
            "geometry. A surface is described locally "
            "by smooth parametrizations from R squared "
            "into R three.",
            duration=7,
        )
        title = self.ly.title("Key Results")

        items = [
            Text(
                "1. Surface: sigma(u,v) maps R² to R³",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. Regularity: partials linearly independent",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3. Tangent plane = span{sigma_u, sigma_v}",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "4. Unit normal = (sigma_u x sigma_v) / |...|",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "5. Atlas of charts covers the full surface",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        # Preview + outro
        self.add_subcaption(
            "Next time, we introduce the first "
            "fundamental form, the tool that lets "
            "us measure lengths and angles on "
            "surfaces. Thank you for watching.",
            duration=7,
        )
        play_outro(
            self,
            next_video="First Fundamental Form",
            next_playlist="Differential Geometry",
        )
