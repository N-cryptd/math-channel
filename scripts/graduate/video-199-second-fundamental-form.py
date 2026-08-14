"""
Video 199: Second Fundamental Form -- Differential Geometry Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video199_SecondFundamentalForm

Topics: Shape operator (Weingarten map), second fundamental form (II),
        coefficients L, M, N, principal curvatures, Gaussian and mean curvature.

Prerequisites: Video 198 (First Fundamental Form), Video 197 (Surfaces in R^3),
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
        self.scene3_shape_operator()
        self.scene4_ii_definition()
        self.scene5_computing_lmn()
        self.scene6_principal_curvatures()
        self.scene7_gaussian_mean()
        self.scene8_examples()
        self.scene9_summary_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook -- How Surfaces Bend
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "The first fundamental form told us how to "
            "measure distances, angles, and areas on a "
            "surface. But it said nothing about curvature, "
            "about how the surface bends in space. A flat "
            "sheet of paper and a cylinder wrapped from that "
            "paper have the same first fundamental form, yet "
            "they look completely different.",
            duration=14,
        )
        play_intro(self, "Second Fundamental Form", "Differential Geometry")

        title = self.ly.title("How Surfaces Bend")

        items = [
            Text(
                "Intrinsic (I): distances, angles, areas",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Extrinsic (II): how the surface curves in R\u00b3",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Same I \u2260 same shape (cylinder vs flat sheet)",
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
        self.ly.section_divider("1", "The Shape Operator")
        self.add_subcaption(
            "To measure how a surface bends, we first "
            "need a linear map that captures how the "
            "normal vector changes as we move along the "
            "surface. This map is called the shape "
            "operator.",
            duration=7,
        )
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: The Shape Operator
    # ------------------------------------------------------------------ #
    def scene3_shape_operator(self):
        # Part 1: Gauss map
        self.add_subcaption(
            "The Gauss map sends each point on the surface "
            "to its unit normal vector on the sphere. It is "
            "a map from the surface S to the unit sphere S "
            "two.",
            duration=7,
        )
        title = self.ly.title("The Gauss Map")

        gauss = MathTex(
            r"\mathbf{N} \colon S \to S^2",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(gauss, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(gauss), run_time=NORMAL)

        desc = Text(
            "Maps each point to its unit normal on S\u00b2",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(desc, direction=DOWN, anchor=gauss, buff=0.4)
        self.play(FadeIn(desc, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Part 2: Differential and shape operator
        self.add_subcaption(
            "The differential of the Gauss map, d N, "
            "takes a tangent vector and returns another "
            "tangent vector. This is not obvious, but it "
            "follows from the fact that N is always "
            "perpendicular to the surface. The shape "
            "operator is the negative of d N.",
            duration=10,
        )
        title2 = self.ly.title("The Shape Operator")

        dn = MathTex(
            r"d\mathbf{N}_p \colon T_pS \to T_pS",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(dn, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(dn), run_time=NORMAL)

        shape_def = MathTex(
            r"S_p = -d\mathbf{N}_p",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(shape_def, direction=DOWN, anchor=dn, buff=0.4)
        self.play(FadeIn(shape_def, shift=LEFT * 0.15), run_time=NORMAL)

        interp = Text(
            "S(v): how the normal changes in direction v",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(interp, direction=DOWN, anchor=shape_def, buff=0.4)
        self.play(FadeIn(interp, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Part 3: Self-adjoint property
        self.add_subcaption(
            "A key property: the shape operator is "
            "self-adjoint. This means that its matrix "
            "representation with respect to any orthonormal "
            "basis is symmetric. This guarantees real "
            "eigenvalues, which we will see are the "
            "principal curvatures.",
            duration=9,
        )
        title3 = self.ly.title("Self-Adjoint Property")

        adjoint = MathTex(
            r"\langle S(\mathbf{v}), \mathbf{w} \rangle "
            r"= \langle \mathbf{v}, S(\mathbf{w}) \rangle",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(adjoint, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(adjoint), run_time=NORMAL)

        note = Text(
            "Matrix of S is symmetric \u2192 real eigenvalues",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=adjoint, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Second Fundamental Form Definition
    # ------------------------------------------------------------------ #
    def scene4_ii_definition(self):
        # Part 1: Definition
        self.add_subcaption(
            "The second fundamental form is the bilinear "
            "form associated to the shape operator via the "
            "first fundamental form. It takes two tangent "
            "vectors and returns a scalar.",
            duration=7,
        )
        title = self.ly.title("Second Fundamental Form")

        ii_def = MathTex(
            r"II_p(\mathbf{v}, \mathbf{w}) "
            r"= \langle S(\mathbf{v}), \mathbf{w} \rangle "
            r"= -\langle d\mathbf{N}(\mathbf{v}), \mathbf{w} \rangle",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(ii_def, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(ii_def), run_time=NORMAL)

        desc = Text(
            "Bilinear form on the tangent plane (extrinsic)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(desc, direction=DOWN, anchor=ii_def, buff=0.4)
        self.play(FadeIn(desc, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Part 2: Matrix form
        self.add_subcaption(
            "In coordinates, the second fundamental form "
            "has a symmetric two by two matrix, just like "
            "the first form. The entries are L, M, and N.",
            duration=7,
        )
        title2 = self.ly.title("Matrix Form of II")

        expanded = MathTex(
            r"II_p(\mathbf{v}, \mathbf{w}) = Lac + M(ad + bc) + Nbd",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(expanded, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(expanded), run_time=NORMAL)

        matrix = MathTex(
            r"II = \begin{bmatrix} L & M \\ M & N \end{bmatrix}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(matrix, direction=DOWN, anchor=expanded, buff=0.5)
        self.play(FadeIn(matrix, shift=LEFT * 0.15), run_time=NORMAL)

        contrast = Text(
            "I = [[E, F], [F, G]] (first) vs II = [[L, M], [M, N]] (second)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(contrast, direction=DOWN, anchor=matrix, buff=0.4)
        self.play(FadeIn(contrast, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Computing L, M, N
    # ------------------------------------------------------------------ #
    def scene5_computing_lmn(self):
        self.add_subcaption(
            "The coefficients L, M, and N are computed from "
            "the second derivatives of the parametrization "
            "projected onto the normal direction. While E, "
            "F, and G come from first derivatives, these "
            "come from second derivatives.",
            duration=9,
        )
        title = self.ly.title("The Coefficients L, M, N")

        l_def = MathTex(
            r"L = \sigma_{uu} \cdot \mathbf{N}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(l_def, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(l_def), run_time=NORMAL)

        m_def = MathTex(
            r"M = \sigma_{uv} \cdot \mathbf{N}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(m_def, direction=DOWN, anchor=l_def, buff=0.4)
        self.play(FadeIn(m_def, shift=LEFT * 0.15), run_time=NORMAL)

        n_def = MathTex(
            r"N = \sigma_{vv} \cdot \mathbf{N}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(n_def, direction=DOWN, anchor=m_def, buff=0.4)
        self.play(FadeIn(n_def, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Comparison with E, F, G
        self.add_subcaption(
            "Notice the parallel: E, F, G use first "
            "partial derivatives dotted with each other. "
            "L, M, N use second partial derivatives "
            "dotted with the unit normal. The second "
            "form captures how the surface accelerates "
            "away from its tangent plane.",
            duration=10,
        )
        title2 = self.ly.title("First vs Second Form Coefficients")

        left_items = [
            Text(
                "First form (I):",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            MathTex(
                r"E = \sigma_u \cdot \sigma_u",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            MathTex(
                r"F = \sigma_u \cdot \sigma_v",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            MathTex(
                r"G = \sigma_v \cdot \sigma_v",
                font_size=HEADING_SIZE, color=WHITE,
            ),
        ]
        right_items = [
            Text(
                "Second form (II):",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            MathTex(
                r"L = \sigma_{uu} \cdot \mathbf{N}",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            MathTex(
                r"M = \sigma_{uv} \cdot \mathbf{N}",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            MathTex(
                r"N = \sigma_{vv} \cdot \mathbf{N}",
                font_size=HEADING_SIZE, color=WHITE,
            ),
        ]
        left_col, right_col = self.ly.two_columns(left_items, right_items)
        self.play(
            FadeIn(left_col, shift=LEFT * 0.2),
            FadeIn(right_col, shift=RIGHT * 0.2),
            run_time=NORMAL,
        )

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Principal Curvatures
    # ------------------------------------------------------------------ #
    def scene6_principal_curvatures(self):
        # Part 1: Eigenvalues
        self.add_subcaption(
            "Since the shape operator is symmetric, it "
            "has real eigenvalues. These eigenvalues are "
            "called the principal curvatures, and they "
            "tell us the maximum and minimum bending at "
            "each point.",
            duration=8,
        )
        title = self.ly.title("Principal Curvatures")

        eigen = MathTex(
            r"S(\mathbf{e}_1) = \kappa_1 \mathbf{e}_1, \quad "
            r"S(\mathbf{e}_2) = \kappa_2 \mathbf{e}_2",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(eigen, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(eigen), run_time=NORMAL)

        names = Text(
            "\u03ba\u2081, \u03ba\u2082: eigenvalues of S (principal curvatures)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(names, direction=DOWN, anchor=eigen, buff=0.4)
        self.play(FadeIn(names, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Part 2: Geometric meaning + classification
        self.add_subcaption(
            "Geometrically, the principal curvatures are "
            "the maximum and minimum normal curvatures "
            "over all directions in the tangent plane. "
            "The signs of kappa one and kappa two classify "
            "the surface point as elliptic, hyperbolic, or "
            "parabolic.",
            duration=10,
        )
        title2 = self.ly.title("Classification of Surface Points")

        items = [
            Text(
                "\u03ba\u2081\u00b7\u03ba\u2082 > 0: elliptic (sphere-like, all normals curve same way)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "\u03ba\u2081\u00b7\u03ba\u2082 < 0: hyperbolic (saddle, normals curve opposite ways)",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "\u03ba\u2081\u00b7\u03ba\u2082 = 0: parabolic (cylinder, one direction flat)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title2)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Gaussian and Mean Curvature
    # ------------------------------------------------------------------ #
    def scene7_gaussian_mean(self):
        # Part 1: Gaussian curvature
        self.add_subcaption(
            "Gaussian curvature is the determinant of the "
            "shape operator. It equals the determinant of "
            "the second form matrix divided by the "
            "determinant of the first form matrix. "
            "Geometrically, K equals kappa one times kappa "
            "two.",
            duration=10,
        )
        title = self.ly.title("Gaussian Curvature")

        k_formula = MathTex(
            r"K = \kappa_1 \kappa_2 = \det(S)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(k_formula, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(k_formula), run_time=NORMAL)

        k_ratio = MathTex(
            r"K = \frac{LN - M^2}{EG - F^2}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(k_ratio, direction=DOWN, anchor=k_formula, buff=0.4)
        self.play(FadeIn(k_ratio, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Part 2: Mean curvature
        self.add_subcaption(
            "Mean curvature is half the trace of the shape "
            "operator, or equivalently, the average of the "
            "principal curvatures. In terms of the "
            "coefficients, it is given by this formula.",
            duration=8,
        )
        title2 = self.ly.title("Mean Curvature")

        h_formula = MathTex(
            r"H = \frac{1}{2}\mathrm{tr}(S) "
            r"= \frac{\kappa_1 + \kappa_2}{2}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(h_formula, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(h_formula), run_time=NORMAL)

        h_coeff = MathTex(
            r"H = \frac{EN - 2FM + GL}{2(EG - F^2)}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(h_coeff, direction=DOWN, anchor=h_formula, buff=0.4)
        self.play(FadeIn(h_coeff, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Part 3: Theorema Egregium preview
        self.add_subcaption(
            "Here is one of the most surprising results in "
            "all of mathematics: Gauss's Theorema Egregium. "
            "It states that Gaussian curvature depends only "
            "on the first fundamental form and its "
            "derivatives. Despite being defined via the "
            "second form, K is actually an intrinsic "
            "quantity.",
            duration=12,
        )
        title3 = self.ly.title("Theorema Egregium (Preview)")

        items = [
            Text(
                "K depends only on E, F, G and their derivatives",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Despite using II in its definition, K is intrinsic!",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Full treatment in next video (Gaussian Curvature)",
                font_size=BODY_SIZE, color=DIM, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title3)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Examples -- Sphere and Saddle
    # ------------------------------------------------------------------ #
    def scene8_examples(self):
        # Part 1: Sphere
        self.add_subcaption(
            "Let us compute the second fundamental form "
            "for a sphere of radius R. The unit normal "
            "points outward, so N equals sigma over R. "
            "We find L equals minus R sine squared phi, M "
            "equals zero, and N coefficient equals minus R.",
            duration=10,
        )
        title = self.ly.title("Example: Sphere")

        param = MathTex(
            r"\sigma(\theta,\phi) = (R\sin\phi\cos\theta,\;"
            r"R\sin\phi\sin\theta,\;R\cos\phi)",
            font_size=HEADING_SIZE, color=DIM,
        )
        self.ly.safe_place(param, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(param), run_time=FAST)

        lmn_sphere = MathTex(
            r"L = -R\sin^2\!\phi, \quad M = 0, \quad N = -R",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(lmn_sphere, direction=DOWN, anchor=param, buff=0.4)
        self.play(FadeIn(lmn_sphere, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Sphere K computation
        self.add_subcaption(
            "The Gaussian curvature of the sphere is K "
            "equals one over R squared. The principal "
            "curvatures are both one over R, making every "
            "point an umbilic point, where all normal "
            "curvatures are equal.",
            duration=8,
        )
        title2 = self.ly.title("Sphere Curvature")

        k_sphere = MathTex(
            r"K = \frac{LN - M^2}{EG - F^2} "
            r"= \frac{R^2 \sin^2\!\phi}{R^4 \sin^2\!\phi} "
            r"= \frac{1}{R^2}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(k_sphere, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(k_sphere), run_time=NORMAL)

        kappa_sphere = MathTex(
            r"\kappa_1 = \kappa_2 = \frac{1}{R}"
            r"\quad \text{(umbilic point)}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(kappa_sphere, direction=DOWN, anchor=k_sphere, buff=0.4)
        self.play(FadeIn(kappa_sphere, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Part 2: Saddle
        self.add_subcaption(
            "Now consider the saddle surface sigma of u, v "
            "equals u, v, u v. At the origin, the unit "
            "normal is zero, zero, one. Computing the "
            "second derivatives and dotting with N, we get "
            "L equals zero, M equals one, and N equals zero.",
            duration=10,
        )
        title3 = self.ly.title("Example: Saddle Surface")

        param_saddle = MathTex(
            r"\sigma(u,v) = (u,\; v,\; uv)",
            font_size=HEADING_SIZE, color=DIM,
        )
        self.ly.safe_place(param_saddle, direction=DOWN, anchor=title3, buff=0.4)
        self.play(Write(param_saddle), run_time=FAST)

        lmn_saddle = MathTex(
            r"L = 0, \quad M = 1, \quad N = 0"
            r"\quad \text{(at origin)}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(lmn_saddle, direction=DOWN, anchor=param_saddle, buff=0.4)
        self.play(FadeIn(lmn_saddle, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Saddle K computation
        self.add_subcaption(
            "The Gaussian curvature at the origin is K "
            "equals zero minus one over one minus zero, "
            "which is minus one. Negative curvature! The "
            "principal curvatures are one and minus one. "
            "This is a hyperbolic point.",
            duration=8,
        )
        title4 = self.ly.title("Saddle Curvature")

        k_saddle = MathTex(
            r"K = \frac{0 \cdot 0 - 1^2}{1 - 0} = -1",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(k_saddle, direction=DOWN, anchor=title4, buff=0.5)
        self.play(Write(k_saddle), run_time=NORMAL)

        kappa_saddle = MathTex(
            r"\kappa_1 = 1, \quad \kappa_2 = -1"
            r"\quad \text{(hyperbolic)}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(kappa_saddle, direction=DOWN, anchor=k_saddle, buff=0.4)
        self.play(FadeIn(kappa_saddle, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 9: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene9_summary_outro(self):
        self.add_subcaption(
            "Let us review the key results. The shape "
            "operator measures how the normal changes "
            "along the surface. The second fundamental "
            "form is the associated bilinear form. The "
            "principal curvatures are its eigenvalues, "
            "and Gaussian and mean curvature summarize "
            "the bending at each point.",
            duration=10,
        )
        title = self.ly.title("Key Results")

        items = [
            Text(
                "1. S = -dN: how the normal changes along S",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. II = [[L, M], [M, N]]: second fundamental form",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3. L = \u03c3_uu\u00b7N, M = \u03c3_uv\u00b7N, N = \u03c3_vv\u00b7N",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "4. \u03ba\u2081, \u03ba\u2082: eigenvalues of S (principal curvatures)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "5. K = (LN - M\u00b2)/(EG - F\u00b2), H = tr(S)/2",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "6. II is extrinsic (unlike I which is intrinsic)",
                font_size=BODY_SIZE, color=DIM, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        self.add_subcaption(
            "Next time, we dive deeper into Gaussian "
            "curvature and prove the Theorema Egregium. "
            "Thank you for watching.",
            duration=6,
        )
        play_outro(
            self,
            next_video="Gaussian Curvature",
            next_playlist="Differential Geometry",
        )
