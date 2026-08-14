"""
Video 199: Second Fundamental Form -- Differential Geometry Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video199_SecondFundamentalForm

Topics: Gauss map, shape operator, second fundamental form (e, f, g),
        principal curvatures, mean curvature, Gaussian curvature.

Prerequisites: Video 197 (Surfaces in R³), Video 198 (First Fundamental Form),
               Video 196 (Frenet-Serret Frame), Linear Algebra (eigenvalues).

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


class Video199_SecondFundamentalForm(Scene):
    """Second Fundamental Form -- Differential Geometry Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_gauss_map_shape_op()
        self.scene4_coefficients()
        self.scene5_principal_curvatures()
        self.scene6_mean_gaussian()
        self.scene7_examples()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook — Intrinsic vs Extrinsic
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "The first fundamental form tells you how "
            "to measure distances and angles on the "
            "surface. But it says nothing about how "
            "the surface sits in space. The second "
            "fundamental form captures this missing "
            "extrinsic information.",
            duration=9,
        )
        play_intro(self, "Second Fundamental Form", "Differential Geometry")

        title = self.ly.title("Intrinsic vs Extrinsic")

        items = [
            Text(
                "I (first form): lengths, angles, areas",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "II (second form): how surface bends in space",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Together: complete local geometry of S",
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
        self.ly.section_divider("1", "The Gauss Map")
        self.add_subcaption(
            "We begin with the Gauss map, which "
            "sends each point on the surface to its "
            "unit normal vector on the unit sphere. "
            "The derivative of this map is the "
            "shape operator.",
            duration=7,
        )
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Gauss Map and Shape Operator
    # ------------------------------------------------------------------ #
    def scene3_gauss_map_shape_op(self):
        self.add_subcaption(
            "The Gauss map N sends a point on the "
            "surface to the corresponding point on "
            "the unit sphere. The shape operator S "
            "is the negative derivative of N. It "
            "maps tangent vectors to tangent vectors.",
            duration=8,
        )
        title = self.ly.title("Gauss Map")

        gauss = MathTex(
            r"\mathbf{N} : S \to S^2",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(gauss, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(gauss), run_time=NORMAL)

        desc = Text(
            "Each point p maps to its unit normal N(p) on S²",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(desc, direction=DOWN, anchor=gauss, buff=0.4)
        self.play(FadeIn(desc, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Shape operator
        self.add_subcaption(
            "The shape operator S at a point p is "
            "the negative differential of the Gauss "
            "map. It takes a tangent vector v and "
            "returns another tangent vector. S is "
            "self-adjoint with respect to the first "
            "fundamental form.",
            duration=9,
        )
        title2 = self.ly.title("Shape Operator")

        shape = MathTex(
            r"S_p(\mathbf{v}) = -d\mathbf{N}_p(\mathbf{v})",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(shape, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(shape), run_time=NORMAL)

        self_adj = Text(
            "S is self-adjoint: I(S(v), w) = I(v, S(w))",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(self_adj, direction=DOWN, anchor=shape, buff=0.4)
        self.play(FadeIn(self_adj, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Second Fundamental Form Coefficients
    # ------------------------------------------------------------------ #
    def scene4_coefficients(self):
        self.add_subcaption(
            "The second fundamental form is a "
            "quadratic form defined by the shape "
            "operator. Its coefficients e, f, and "
            "g are the normal components of the "
            "second partial derivatives of sigma.",
            duration=8,
        )
        title = self.ly.title("Coefficients e, f, g")

        defs = MathTex(
            r"e = \sigma_{uu} \cdot \mathbf{N},\quad"
            r"f = \sigma_{uv} \cdot \mathbf{N},\quad"
            r"g = \sigma_{vv} \cdot \mathbf{N}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(defs, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(defs), run_time=NORMAL)

        matrix = MathTex(
            r"\mathrm{II} = \begin{bmatrix} e & f \\ f & g \end{bmatrix}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(matrix, direction=DOWN, anchor=defs, buff=0.5)
        self.play(FadeIn(matrix, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Alternative formula
        self.add_subcaption(
            "An equivalent definition: the second "
            "fundamental form of two tangent vectors "
            "equals the negative dot product of the "
            "differential of N with the second vector.",
            duration=7,
        )
        title2 = self.ly.title("Alternative Definition")

        alt = MathTex(
            r"\mathrm{II}(\mathbf{v},\mathbf{w})"
            r"= I(S(\mathbf{v}),\mathbf{w})"
            r"= -\langle d\mathbf{N}(\mathbf{v}),\,\mathbf{w}\rangle",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(alt, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(alt), run_time=NORMAL)

        note = Text(
            "Measures how the normal changes along the surface",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=alt, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Principal Curvatures
    # ------------------------------------------------------------------ #
    def scene5_principal_curvatures(self):
        self.add_subcaption(
            "The shape operator is self-adjoint, so "
            "by the spectral theorem it has real "
            "eigenvalues. These eigenvalues k one "
            "and k two are the principal curvatures. "
            "Their eigenvectors are the principal "
            "directions.",
            duration=9,
        )
        title = self.ly.title("Principal Curvatures")

        eigen = MathTex(
            r"S(\mathbf{e}_1) = \kappa_1 \mathbf{e}_1, \quad"
            r"S(\mathbf{e}_2) = \kappa_2 \mathbf{e}_2",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(eigen, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(eigen), run_time=NORMAL)

        geo = Text(
            "k₁, k₂ = max and min normal curvatures",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(geo, direction=DOWN, anchor=eigen, buff=0.4)
        self.play(FadeIn(geo, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Euler's formula
        self.add_subcaption(
            "The normal curvature in any direction "
            "is a weighted average of the principal "
            "curvatures. This is Euler's formula.",
            duration=6,
        )
        title2 = self.ly.title("Euler's Formula")

        euler = MathTex(
            r"\kappa_n(\theta) = \kappa_1 \cos^2\theta + \kappa_2 \sin^2\theta",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(euler, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(euler), run_time=NORMAL)

        kn = MathTex(
            r"\kappa_n = \frac{\mathrm{II}(\mathbf{v},\mathbf{v})}"
            r"{I(\mathbf{v},\mathbf{v})}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(kn, direction=DOWN, anchor=euler, buff=0.4)
        self.play(FadeIn(kn, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Mean and Gaussian Curvature
    # ------------------------------------------------------------------ #
    def scene6_mean_gaussian(self):
        self.add_subcaption(
            "The mean curvature H is the average of "
            "the principal curvatures. The Gaussian "
            "curvature K is their product. Both are "
            "computed from the fundamental form "
            "coefficients.",
            duration=8,
        )
        title = self.ly.title("Mean Curvature H")

        h_def = MathTex(
            r"H = \frac{\kappa_1 + \kappa_2}{2}"
            r"= \frac{eG - 2fF + gE}{2(EG - F^2)}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(h_def, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(h_def), run_time=NORMAL)

        h_note = Text(
            "H = 0: minimal surface (soap films)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(h_note, direction=DOWN, anchor=h_def, buff=0.4)
        self.play(FadeIn(h_note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Gaussian curvature
        self.add_subcaption(
            "The Gaussian curvature K is the product "
            "of the principal curvatures. It "
            "determines the local shape: positive "
            "means bowl-like, negative means "
            "saddle-like, zero means flat in one "
            "direction.",
            duration=9,
        )
        title2 = self.ly.title("Gaussian Curvature K")

        k_def = MathTex(
            r"K = \kappa_1 \cdot \kappa_2"
            r"= \frac{eg - f^2}{EG - F^2}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(k_def, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(k_def), run_time=NORMAL)

        items = [
            Text(
                "K > 0: bowl-shaped (sphere)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "K < 0: saddle-shaped",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "K = 0: flat in one direction (cylinder)",
                font_size=BODY_SIZE, color=DIM, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=k_def)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Examples — Sphere and Cylinder
    # ------------------------------------------------------------------ #
    def scene7_examples(self):
        self.add_subcaption(
            "For the sphere of radius R with outward "
            "normal, both principal curvatures equal "
            "one over R. So H equals one over R and K "
            "equals one over R squared.",
            duration=8,
        )
        title = self.ly.title("Example: Sphere")

        sphere_k = MathTex(
            r"\kappa_1 = \kappa_2 = \frac{1}{R}, \quad"
            r"H = \frac{1}{R}, \quad"
            r"K = \frac{1}{R^2}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(sphere_k, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(sphere_k), run_time=NORMAL)

        sphere_note = Text(
            "Every direction curves equally: K > 0 everywhere",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(sphere_note, direction=DOWN, anchor=sphere_k, buff=0.4)
        self.play(FadeIn(sphere_note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Cylinder
        self.add_subcaption(
            "For the cylinder, one principal curvature "
            "is one over R from the circular cross "
            "section, and the other is zero along "
            "the axis. So K equals zero.",
            duration=8,
        )
        title2 = self.ly.title("Example: Cylinder")

        cyl_k = MathTex(
            r"\kappa_1 = \frac{1}{R}, \quad \kappa_2 = 0, \quad"
            r"H = \frac{1}{2R}, \quad K = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(cyl_k, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(cyl_k), run_time=NORMAL)

        cyl_note = Text(
            "Flat along the axis: K = 0 (developable surface)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(cyl_note, direction=DOWN, anchor=cyl_k, buff=0.4)
        self.play(FadeIn(cyl_note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary_outro(self):
        self.add_subcaption(
            "The second fundamental form completes "
            "the local description of a surface. "
            "Together with the first fundamental form, "
            "it determines how the surface sits in "
            "space.",
            duration=7,
        )
        title = self.ly.title("Key Results")

        items = [
            Text(
                "1. Shape operator S = −dN (self-adjoint)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. II = [[e, f], [f, g]] from 2nd partials",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3. Principal curvatures: eigenvalues of S",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "4. H = (k₁+k₂)/2, K = k₁·k₂",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "5. Extrinsic: measures bending in space",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        self.add_subcaption(
            "Next time, we dive deep into Gaussian "
            "curvature and the Theorema Egregium, "
            "one of the most surprising results in "
            "all of mathematics. Thank you for "
            "watching.",
            duration=7,
        )
        play_outro(
            self,
            next_video="Gaussian Curvature",
            next_playlist="Differential Geometry",
        )
