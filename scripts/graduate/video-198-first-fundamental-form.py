"""
Video 198: First Fundamental Form -- Differential Geometry Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video198_FirstFundamentalForm

Topics: First fundamental form (metric), coefficients E, F, G,
        arc length, angles, area element, intrinsic geometry.

Prerequisites: Video 197 (Surfaces in R³), Video 195 (Arc Length & Curvature),
               Linear Algebra (inner products, metric tensors).

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


class Video198_FirstFundamentalForm(Scene):
    """First Fundamental Form -- Differential Geometry Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_coefficients()
        self.scene4_arc_length()
        self.scene5_angles()
        self.scene6_area()
        self.scene7_sphere_example()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook — Measuring on a Surface
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "If you live on the surface of a sphere, "
            "you can measure distances, angles, and "
            "areas, all without leaving the surface. "
            "These measurements are intrinsic. The "
            "first fundamental form encodes them all.",
            duration=9,
        )
        play_intro(self, "First Fundamental Form", "Differential Geometry")

        title = self.ly.title("Measuring on a Surface")

        items = [
            Text(
                "Distances along curves on S",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Angles between curves on S",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Areas of regions on S",
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
        self.ly.section_divider("1", "The Coefficients E, F, G")
        self.add_subcaption(
            "The first fundamental form is a "
            "quadratic form on the tangent plane. "
            "It is defined by the dot products of "
            "the partial derivatives of the "
            "parametrization.",
            duration=7,
        )
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Definition of E, F, G
    # ------------------------------------------------------------------ #
    def scene3_coefficients(self):
        self.add_subcaption(
            "The first fundamental form has three "
            "coefficients. E is the dot product of "
            "sigma u with itself. F is the dot "
            "product of sigma u with sigma v. G "
            "is the dot product of sigma v with "
            "itself.",
            duration=8,
        )
        title = self.ly.title("The Three Coefficients")

        e_def = MathTex(
            r"E = \sigma_u \cdot \sigma_u",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(e_def, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(e_def), run_time=NORMAL)

        f_def = MathTex(
            r"F = \sigma_u \cdot \sigma_v",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(f_def, direction=DOWN, anchor=e_def, buff=0.4)
        self.play(FadeIn(f_def, shift=LEFT * 0.15), run_time=NORMAL)

        g_def = MathTex(
            r"G = \sigma_v \cdot \sigma_v",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(g_def, direction=DOWN, anchor=f_def, buff=0.4)
        self.play(FadeIn(g_def, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Matrix form
        self.add_subcaption(
            "Together, these form a symmetric two "
            "by two matrix. This matrix is the "
            "metric tensor of the surface. It "
            "encodes all intrinsic measurements.",
            duration=7,
        )
        title2 = self.ly.title("Matrix Form")

        matrix = MathTex(
            r"I = \begin{bmatrix} E & F \\ F & G \end{bmatrix}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(matrix, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(matrix), run_time=NORMAL)

        metric = Text(
            "The metric tensor of the surface",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(metric, direction=DOWN, anchor=matrix, buff=0.4)
        self.play(FadeIn(metric, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Arc Length on a Surface
    # ------------------------------------------------------------------ #
    def scene4_arc_length(self):
        self.add_subcaption(
            "To find the length of a curve on the "
            "surface, compose the curve with the "
            "parametrization and use the chain rule. "
            "The result involves E, F, and G.",
            duration=7,
        )
        title = self.ly.title("Arc Length")

        curve = MathTex(
            r"\gamma(t) = \sigma(u(t),\, v(t))",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(curve, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(curve), run_time=NORMAL)

        ds = MathTex(
            r"ds^2 = E\,du^2 + 2F\,du\,dv + G\,dv^2",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ds, direction=DOWN, anchor=curve, buff=0.5)
        self.play(FadeIn(ds, shift=LEFT * 0.15), run_time=NORMAL)

        length = MathTex(
            r"L = \int\sqrt{E\,u'^2 + 2F\,u'\,v' + G\,v'^2}\,dt",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(length, direction=DOWN, anchor=ds, buff=0.4)
        self.play(FadeIn(length, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Line element interpretation
        self.add_subcaption(
            "The expression ds squared is called the "
            "line element. It replaces the flat space "
            "dx squared plus dy squared plus dz "
            "squared with a version adapted to the "
            "curved surface.",
            duration=8,
        )
        title2 = self.ly.title("The Line Element")

        items = [
            Text(
                "Flat space: ds² = dx² + dy² + dz²",
                font_size=BODY_SIZE, color=DIM, font=SANS,
            ),
            Text(
                "On surface: ds² = E du² + 2F du dv + G dv²",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Same idea, adapted to the curved geometry",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title2)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Angles on a Surface
    # ------------------------------------------------------------------ #
    def scene5_angles(self):
        self.add_subcaption(
            "The angle between two curves on the "
            "surface is computed using the first "
            "fundamental form. It is the I-form "
            "of the tangent vectors divided by the "
            "product of their speeds.",
            duration=8,
        )
        title = self.ly.title("Angles Between Curves")

        cos_angle = MathTex(
            r"\cos\theta = \frac{I(\mathbf{v},\,\mathbf{w})}"
            r"{|\mathbf{v}|\,|\mathbf{w}|}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(cos_angle, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(cos_angle), run_time=NORMAL)

        expanded = MathTex(
            r"= \frac{E\,u_1'u_2' + F(u_1'v_2' + v_1'u_2') + G\,v_1'v_2'}"
            r"{\sqrt{E\,u_1'^2 + 2F\,u_1'v_1' + G\,v_1'^2}\;"
            r"\sqrt{E\,u_2'^2 + 2F\,u_2'v_2' + G\,v_2'^2}}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(expanded, direction=DOWN, anchor=cos_angle, buff=0.5)
        self.play(FadeIn(expanded, shift=LEFT * 0.15), run_time=NORMAL)

        note = Text(
            "Generalizes the flat-space cosine formula",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=expanded, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Area on a Surface
    # ------------------------------------------------------------------ #
    def scene6_area(self):
        self.add_subcaption(
            "The area element on the surface is the "
            "magnitude of the cross product of the "
            "partial derivatives. Using the Lagrange "
            "identity, this equals the square root "
            "of E G minus F squared.",
            duration=9,
        )
        title = self.ly.title("Area Element")

        cross = MathTex(
            r"dA = |\sigma_u \times \sigma_v|\,du\,dv",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(cross, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(cross), run_time=NORMAL)

        lagrange = MathTex(
            r"|\sigma_u \times \sigma_v|^2 = EG - F^2",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(lagrange, direction=DOWN, anchor=cross, buff=0.5)
        self.play(FadeIn(lagrange, shift=LEFT * 0.15), run_time=NORMAL)

        da_final = MathTex(
            r"dA = \sqrt{EG - F^2}\;du\,dv",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(da_final, direction=DOWN, anchor=lagrange, buff=0.4)
        self.play(FadeIn(da_final, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Total area formula
        self.add_subcaption(
            "The total area of a region R on the "
            "surface is the double integral of "
            "the area element over the parameter "
            "domain.",
            duration=6,
        )
        title2 = self.ly.title("Surface Area")

        area_int = MathTex(
            r"A = \iint_R \sqrt{EG - F^2}\;du\,dv",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(area_int, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(area_int), run_time=NORMAL)

        note2 = Text(
            "Integrate the area element over the parameter domain",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(note2, direction=DOWN, anchor=area_int, buff=0.4)
        self.play(FadeIn(note2, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Example — Sphere
    # ------------------------------------------------------------------ #
    def scene7_sphere_example(self):
        self.add_subcaption(
            "Let us compute the first fundamental "
            "form for the sphere. Spherical coordinates "
            "have E equals R squared sine squared phi, "
            "F equals zero, and G equals R squared.",
            duration=8,
        )
        title = self.ly.title("Example: Sphere")

        param = MathTex(
            r"\sigma = (R\sin\phi\cos\theta,\;"
            r"R\sin\phi\sin\theta,\;R\cos\phi)",
            font_size=HEADING_SIZE, color=DIM,
        )
        self.ly.safe_place(param, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(param), run_time=FAST)

        efg = MathTex(
            r"E = R^2\sin^2\!\phi, \quad F = 0, \quad G = R^2",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(efg, direction=DOWN, anchor=param, buff=0.4)
        self.play(FadeIn(efg, shift=LEFT * 0.15), run_time=NORMAL)

        f_zero = Text(
            "F = 0: coordinate lines are perpendicular",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(f_zero, direction=DOWN, anchor=efg, buff=0.4)
        self.play(FadeIn(f_zero, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Area computation
        self.add_subcaption(
            "The area element is R squared sine phi "
            "d phi d theta. Integrating over the "
            "full sphere gives four pi R squared, "
            "the familiar formula.",
            duration=8,
        )
        title2 = self.ly.title("Sphere Area")

        da_sphere = MathTex(
            r"dA = R^2\sin\phi\;d\phi\,d\theta",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(da_sphere, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(da_sphere), run_time=NORMAL)

        area_sphere = MathTex(
            r"A = \int_0^{2\pi}\!\!\int_0^{\pi} R^2\sin\phi\;d\phi\,d\theta"
            r" = 4\pi R^2",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(area_sphere, direction=DOWN, anchor=da_sphere, buff=0.5)
        self.play(FadeIn(area_sphere, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary_outro(self):
        self.add_subcaption(
            "The first fundamental form is the "
            "complete tool for intrinsic geometry. "
            "It encodes lengths, angles, and areas "
            "using only measurements on the "
            "surface itself.",
            duration=7,
        )
        title = self.ly.title("Key Results")

        items = [
            Text(
                "1. I = [[E, F], [F, G]] from partial derivatives",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. Arc length: ds² = E du² + 2F du dv + G dv²",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3. Angles: cos θ = I(v, w) / (|v|·|w|)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "4. Area: dA = √(EG − F²) du dv",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "5. Intrinsic: depends only on the surface",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        self.add_subcaption(
            "Next time, we introduce the second "
            "fundamental form, which measures how "
            "the surface curves in space. Thank you "
            "for watching.",
            duration=7,
        )
        play_outro(
            self,
            next_video="Second Fundamental Form",
            next_playlist="Differential Geometry",
        )
