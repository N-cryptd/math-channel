"""
Video 201: Geodesics -- Differential Geometry Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video201_Geodesics

Topics: Geodesics, geodesic equation, Christoffel symbols, parallel
        transport of tangent, great circles, cylinder geodesics,
        variational characterization, exponential map.

Prerequisites: Video 198 (First Fundamental Form), Video 199 (Second
               Fundamental Form), Video 200 (Gaussian Curvature).

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


class Video201_Geodesics(Scene):
    """Geodesics -- Differential Geometry Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_definition()
        self.scene4_variational()
        self.scene5_geodesic_equation()
        self.scene6_sphere_example()
        self.scene7_cylinder_example()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook — What's the Shortest Path on a Sphere?
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "If you fly from New York to Tokyo, "
            "why don't airlines fly in a straight line? "
            "On a flat map, a straight line looks "
            "short. But on a sphere, the true "
            "shortest path curves.",
            duration=10,
        )
        play_intro(self, "Geodesics", "Differential Geometry")

        title = self.ly.title("The Shortest Path Problem")

        items = [
            Text(
                "Flat map: straight line looks shortest",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Sphere: great circle is the true shortest",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Geodesics = straight lines on curved surfaces",
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
        self.ly.section_divider("1", "Geodesics as Straightest Curves")
        self.add_subcaption(
            "A geodesic is the straightest possible "
            "curve on a surface. Its acceleration has "
            "no component tangent to the surface. The "
            "tangent vector is parallel-transported.",
            duration=7,
        )
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Definition — Zero Geodesic Curvature
    # ------------------------------------------------------------------ #
    def scene3_definition(self):
        self.add_subcaption(
            "The geodesic curvature measures how "
            "much a curve bends within the surface, "
            "not perpendicular to it. A geodesic has "
            "zero geodesic curvature. Its tangent "
            "vector is parallel-transported.",
            duration=9,
        )
        title = self.ly.title("Definition: Geodesic")

        kappa_eq = MathTex(
            r"\kappa_g = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(kappa_eq, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(kappa_eq), run_time=NORMAL)

        meaning = Text(
            "Geodesic curvature = 0  (straightest possible curve)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(meaning, direction=DOWN, anchor=kappa_eq, buff=0.4)
        self.play(FadeIn(meaning, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Tangent vector condition
        self.add_subcaption(
            "The acceleration of a geodesic is "
            "either zero or points purely in the "
            "normal direction. There is no "
            "acceleration within the surface.",
            duration=8,
        )
        title2 = self.ly.title("Acceleration Condition")

        accel_eq = MathTex(
            r"\frac{d^2 \mathbf{r}}{ds^2} \parallel \mathbf{N}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(accel_eq, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(accel_eq), run_time=NORMAL)

        items = [
            Text(
                "d²r/ds² has no tangential component",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Tangent vector T is parallel-transported",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=accel_eq)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Variational Characterization
    # ------------------------------------------------------------------ #
    def scene4_variational(self):
        self.add_subcaption(
            "Geodesics are also locally shortest "
            "paths. We find them by minimizing the "
            "arc length using calculus of variations. "
            "The resulting Euler-Lagrange equations "
            "give us the geodesic equations.",
            duration=9,
        )
        title = self.ly.title("Shortest Path Principle")

        # Arc length functional
        arc_len = MathTex(
            r"L[\gamma] = \int \sqrt{E\, u'^2 + 2F\, u'v' + G\, v'^2}\; ds",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(arc_len, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(arc_len), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Energy functional trick
        self.add_subcaption(
            "Instead of minimizing arc length "
            "directly, we minimize the energy "
            "functional. This avoids the square "
            "root and gives cleaner equations.",
            duration=7,
        )
        title2 = self.ly.title("Energy Functional Trick")

        energy = MathTex(
            r"\mathcal{E}[\gamma] = \frac{1}{2} \int g_{ij}"
            r"\frac{du^i}{ds} \frac{du^j}{ds}\; ds",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(energy, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(energy), run_time=NORMAL)

        result = Text(
            "Euler-Lagrange → geodesic equation",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=energy, buff=0.4)
        self.play(FadeIn(result, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: The Geodesic Equation
    # ------------------------------------------------------------------ #
    def scene5_geodesic_equation(self):
        self.ly.section_divider("2", "The Geodesic Equation")
        self.ly.clear()

        self.add_subcaption(
            "The geodesic equation involves the "
            "second derivatives of the coordinates "
            "plus a correction from the Christoffel "
            "symbols. The Christoffel symbols are "
            "computed from the first fundamental "
            "form alone, making them intrinsic.",
            duration=9,
        )
        title = self.ly.title("Geodesic Equation")

        geo_eq = MathTex(
            r"\frac{d^2 u^k}{ds^2}"
            r" + \Gamma^k_{ij}"
            r"\frac{du^i}{ds}\frac{du^j}{ds} = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(geo_eq, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(geo_eq), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Christoffel symbols definition
        self.add_subcaption(
            "The Christoffel symbols of the second "
            "kind encode how the coordinate basis "
            "changes from point to point. They "
            "depend only on the metric and its "
            "partial derivatives.",
            duration=8,
        )
        title2 = self.ly.title("Christoffel Symbols")

        gamma_def = MathTex(
            r"\Gamma^k_{ij} = "
            r"\frac{1}{2}\, g^{kl}"
            r"\!\left("
            r"\frac{\partial g_{li}}{\partial u^j}"
            r"+ \frac{\partial g_{lj}}{\partial u^i}"
            r"- \frac{\partial g_{ij}}{\partial u^l}"
            r"\right)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(gamma_def, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(gamma_def), run_time=NORMAL)

        key_note = Text(
            "Computed from g_{ij} = first fundamental form (intrinsic!)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(key_note, direction=DOWN, anchor=gamma_def, buff=0.4)
        self.play(FadeIn(key_note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Example — Sphere (Great Circles)
    # ------------------------------------------------------------------ #
    def scene6_sphere_example(self):
        self.ly.section_divider("3", "Example: Sphere")
        self.ly.clear()

        self.add_subcaption(
            "On a sphere, the first fundamental "
            "form has E equals R squared, F "
            "equals zero, and G equals R "
            "squared sine squared theta. The "
            "Christoffel symbols follow.",
            duration=9,
        )
        title = self.ly.title("Sphere: Metric")

        param = MathTex(
            r"\mathbf{x}(u,v) = "
            r"(R\sin u\cos v,\;"
            r"R\sin u\sin v,\;"
            r"R\cos u)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(param, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(param), run_time=NORMAL)

        metric_items = [
            MathTex(
                r"E = R^2, \quad F = 0, \quad G = R^2 \sin^2 u",
                font_size=HEADING_SIZE, color=PRIMARY,
            ),
        ]
        self.ly.progressive_reveal(metric_items, start_from=param)

        self.wait(0.5)
        self.ly.clear()

        # Christoffel symbols for sphere
        self.add_subcaption(
            "The non-zero Christoffel symbols for "
            "the sphere are Gamma one twenty-two "
            "equals minus sine theta cosine theta, "
            "and Gamma two one-two equals cotangent "
            "theta.",
            duration=8,
        )
        title2 = self.ly.title("Christoffel Symbols")

        gamma_items = [
            MathTex(
                r"\Gamma^1_{22} = -\sin u\, \cos u",
                font_size=HEADING_SIZE, color=WHITE,
            ),
            MathTex(
                r"\Gamma^2_{12} = \Gamma^2_{21} = \cot u",
                font_size=HEADING_SIZE, color=WHITE,
            ),
        ]
        self.ly.progressive_reveal(gamma_items, start_from=title2)

        self.wait(0.5)
        self.ly.clear()

        # Great circles result
        self.add_subcaption(
            "Solving the geodesic equations shows "
            "that geodesics on a sphere are great "
            "circles. These include the equator, "
            "all meridians, and rotated great "
            "circles through any two points.",
            duration=8,
        )
        title3 = self.ly.title("Result: Great Circles")

        items = [
            Text(
                "Geodesics = great circles",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Equator, meridians: obvious geodesics",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "All other geodesics: rotated great circles",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title3)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Example — Cylinder and Classification
    # ------------------------------------------------------------------ #
    def scene7_cylinder_example(self):
        self.ly.section_divider("4", "Example: Cylinder")
        self.ly.clear()

        self.add_subcaption(
            "The cylinder has a remarkably simple "
            "metric: E equals R squared, F equals "
            "zero, G equals one. Since the metric "
            "coefficients are constant, all "
            "Christoffel symbols vanish.",
            duration=9,
        )
        title = self.ly.title("Cylinder: Metric")

        metric_cyl = MathTex(
            r"E = R^2, \quad F = 0, \quad G = 1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(metric_cyl, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(metric_cyl), run_time=NORMAL)

        vanish = Text(
            "All Christoffel symbols = 0",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(vanish, direction=DOWN, anchor=metric_cyl, buff=0.4)
        self.play(FadeIn(vanish, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Geodesic equations simplify
        self.add_subcaption(
            "With all Christoffel symbols zero, the "
            "geodesic equations become u double "
            "prime equals zero and v double prime "
            "equals zero. So geodesics are straight "
            "lines in coordinate space, which are "
            "helices on the cylinder.",
            duration=9,
        )
        title2 = self.ly.title("Geodesic Equations")

        simple_eq = MathTex(
            r"u'' = 0, \quad v'' = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(simple_eq, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(simple_eq), run_time=NORMAL)

        items = [
            Text(
                "u = as + b,  v = cs + d  (linear in arc length)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "On cylinder: helices, straight lines, circles",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=simple_eq)

        self.wait(0.5)
        self.ly.clear()

        # Classification by curvature
        self.add_subcaption(
            "The behavior of geodesics depends "
            "on the sign of Gaussian curvature. "
            "On positively curved surfaces they "
            "converge. On flat surfaces they "
            "stay parallel. On negatively curved "
            "surfaces they diverge.",
            duration=9,
        )
        title3 = self.ly.title("Geodesics by Curvature")

        items = [
            Text(
                "K > 0 (sphere): geodesics converge",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "K = 0 (cylinder): geodesics are parallel",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "K < 0 (hyperbolic): geodesics diverge",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title3)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary, Exponential Map, and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary_outro(self):
        self.add_subcaption(
            "To summarize: geodesics are curves "
            "with zero geodesic curvature, locally "
            "shortest paths, and solutions to the "
            "geodesic equation with Christoffel "
            "symbols from the metric tensor.",
            duration=8,
        )
        title = self.ly.title("Key Results")

        items = [
            Text(
                "1. κ_g = 0  (parallel-transported tangent)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. Locally shortest paths (variational)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3. Geodesic eq: u''^k + Γ^k_{ij} u'^i u'^j = 0",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "4. Sphere: great circles | Cylinder: helices",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "5. Curvature sign controls convergence/divergence",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        # Exponential map preview
        self.add_subcaption(
            "For every point on the surface and "
            "every tangent vector at that point, "
            "there is a unique geodesic. This "
            "defines the exponential map, which "
            "is central to Riemannian geometry.",
            duration=7,
        )
        title2 = self.ly.title("The Exponential Map")

        items2 = [
            Text(
                "exp_p(v): T_pS → S sends tangent to geodesic point",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Geodesically complete surface: exp_p defined everywhere",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Hopf-Rinow: any two points joined by a geodesic",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)

        self.wait(1.0)
        self.ly.clear()

        self.add_subcaption(
            "Next time we study parallel transport, "
            "the mechanism behind geodesics. Thank "
            "you for watching.",
            duration=5,
        )
        play_outro(
            self,
            next_video="Parallel Transport",
            next_playlist="Differential Geometry",
        )
