"""
Video 202: Gauss-Bonnet Theorem -- Differential Geometry Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video202_GaussBonnet

Topics: Gauss-Bonnet theorem (global and local), Euler characteristic,
        parallel transport, holonomy, geodesic triangles, curvature
        and topology bridge.

Prerequisites: Video 198 (First Fundamental Form), Video 199 (Second
               Fundamental Form), Video 200 (Gaussian Curvature),
               Video 201 (Geodesics).

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


class Video202_GaussBonnet(Scene):
    """Gauss-Bonnet Theorem -- Differential Geometry Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_setup()
        self.scene3_global_theorem()
        self.scene4_examples()
        self.scene5_parallel_transport()
        self.scene6_local_theorem()
        self.scene7_why_euler()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook — The Most Beautiful Theorem
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "The sphere has total curvature four pi. "
            "The torus has total curvature zero. "
            "This number doesn't change no matter how "
            "you bend the surface. Why? Because it's "
            "a topological invariant, fixed by the "
            "Gauss-Bonnet theorem.",
            duration=15,
        )
        play_intro(self, "Gauss-Bonnet Theorem", "Differential Geometry")

        title = self.ly.title("The Bridge Between Geometry and Topology")

        items = [
            Text(
                "Sphere: total curvature = 4\u03C0",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Torus: total curvature = 0",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Curvature \u2194 Euler characteristic",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(3.8)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Setup — What We Need
    # ------------------------------------------------------------------ #
    def scene2_setup(self):
        self.add_subcaption(
            "Before stating Gauss-Bonnet, let's recall "
            "the key ingredients. Gaussian curvature K "
            "measures intrinsic curvature. Geodesic "
            "curvature measures how much a curve "
            "deviates from a geodesic. And the Euler "
            "characteristic counts the topology.",
            duration=17,
        )
        title = self.ly.title("Key Ingredients")

        items = [
            Text(
                "K: Gaussian curvature (Video 200)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "\u03BA_g: geodesic curvature of a curve",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "\u03C7 = V \u2212 E + F: Euler characteristic",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Geodesics: curves with \u03BA_g = 0 (Video 201)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(7.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: The Global Gauss-Bonnet Theorem
    # ------------------------------------------------------------------ #
    def scene3_global_theorem(self):
        self.ly.section_divider("1", "The Global Theorem")
        self.add_subcaption(
            "The global Gauss-Bonnet theorem states "
            "that the integral of Gaussian curvature "
            "over a closed surface equals two pi "
            "times the Euler characteristic. This "
            "means the total curvature is entirely "
            "determined by the surface's topology.",
            duration=16,
        )

        title = self.ly.title("Global Gauss-Bonnet Theorem")

        formula = MathTex(
            r"\iint_S K \, dA = 2\pi \, \chi(S)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(formula, color=PRIMARY)
        self.play(Write(formula_box[0]), run_time=NORMAL)
        self.play(Create(formula_box[1]), run_time=FAST)

        self.wait(0.5)

        items = [
            Text(
                "Left side: total Gaussian curvature",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Right side: surface topology",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Geometry equals topology!",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=formula_box)

        self.wait(8.1)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Examples — Sphere and Torus
    # ------------------------------------------------------------------ #
    def scene4_examples(self):
        self.add_subcaption(
            "Let's verify the theorem. For a sphere "
            "of radius R, Gaussian curvature is "
            "one over R squared everywhere. Integrating "
            "gives four pi. The Euler characteristic "
            "of a sphere is two, so two pi times two "
            "equals four pi. The theorem holds.",
            duration=17,
        )
        title = self.ly.title("Verification: Sphere")

        sphere_formula = MathTex(
            r"K = \frac{1}{R^2}, \quad"
            r"\iint K \, dA = 4\pi",
            font_size=BODY_SIZE, color=WHITE,
        )
        sphere_chi = MathTex(
            r"\chi(S^2) = 2, \quad 2\pi \cdot 2 = 4\pi \;\checkmark",
            font_size=BODY_SIZE, color=SECONDARY,
        )

        self.ly.safe_place(sphere_formula, DOWN, title)
        self.play(Write(sphere_formula), run_time=NORMAL)
        self.wait(0.5)
        self.ly.safe_place(sphere_chi, DOWN, sphere_formula)
        self.play(FadeIn(sphere_chi, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(13.1)

        self.ly.clear()

        self.add_subcaption(
            "For a torus, Gaussian curvature is "
            "positive on the outer part and negative "
            "on the inner part. The total integral "
            "cancels to zero. The Euler characteristic "
            "of a torus is also zero. So zero "
            "equals two pi times zero. It holds.",
            duration=18,
        )
        title2 = self.ly.title("Verification: Torus")

        torus_formula = MathTex(
            r"\iint K \, dA = 0",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        torus_chi = MathTex(
            r"\chi(T^2) = 0, \quad 2\pi \cdot 0 = 0 \;\checkmark",
            font_size=BODY_SIZE, color=SECONDARY,
        )

        self.ly.safe_place(torus_formula, DOWN, title2)
        self.play(Write(torus_formula), run_time=NORMAL)
        self.wait(0.5)
        self.ly.safe_place(torus_chi, DOWN, torus_formula)
        self.play(FadeIn(torus_chi, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(10.2)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Parallel Transport and Holonomy
    # ------------------------------------------------------------------ #
    def scene5_parallel_transport(self):
        self.ly.section_divider("2", "Geometric Intuition")
        self.add_subcaption(
            "The deep reason Gauss-Bonnet works is "
            "parallel transport. Move a tangent "
            "vector around a closed loop on a "
            "surface, keeping it as straight as "
            "possible. When it returns, it's "
            "rotated. This rotation angle is "
            "called holonomy.",
            duration=16,
        )

        title = self.ly.title("Parallel Transport on a Sphere")

        items = [
            Text(
                "Move tangent vector along a closed loop",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Vector returns rotated by holonomy angle",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "On flat surface: no rotation (holonomy = 0)",
                font_size=BODY_SIZE, color=DIM, font=SANS,
            ),
            Text(
                "On sphere: rotation = area \u00D7 curvature",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(9.4)
        self.ly.clear()

        self.add_subcaption(
            "The holonomy angle equals the integral "
            "of Gaussian curvature over the region "
            "enclosed by the loop. This is the "
            "geometric heart of Gauss-Bonnet. "
            "Curvature causes parallel transport "
            "to rotate vectors.",
            duration=15,
        )
        title2 = self.ly.title("The Holonomy Formula")

        holonomy = MathTex(
            r"\theta_{\text{holonomy}} = \iint_R K \, dA",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(holonomy, color=PRIMARY)
        self.play(Write(formula_box[0]), run_time=NORMAL)
        self.play(Create(formula_box[1]), run_time=FAST)

        self.wait(0.5)

        insight = Text(
            "This IS Gauss-Bonnet in geometric form!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, formula_box)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(6.9)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: The Local Gauss-Bonnet Theorem
    # ------------------------------------------------------------------ #
    def scene6_local_theorem(self):
        self.ly.section_divider("3", "The Local Version")
        self.add_subcaption(
            "The local Gauss-Bonnet theorem applies "
            "to a region with a boundary curve. "
            "The geodesic curvature along the "
            "boundary plus the integral of Gaussian "
            "curvature over the interior equals "
            "two pi minus the sum of exterior "
            "angles.",
            duration=16,
        )

        title = self.ly.title("Local Gauss-Bonnet Theorem")

        local_formula = MathTex(
            r"\int_C \kappa_g \, ds"
            r"+ \iint_R K \, dA"
            r"= 2\pi - \sum_i (\pi - \alpha_i)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(local_formula, color=PRIMARY)
        self.play(Write(formula_box[0]), run_time=NORMAL)
        self.play(Create(formula_box[1]), run_time=FAST)

        self.wait(13.0)
        self.ly.clear()

        self.add_subcaption(
            "For a geodesic triangle, the geodesic "
            "curvature is zero on all three sides. "
            "So the formula simplifies. The sum of "
            "interior angles equals pi plus the "
            "integral of curvature. On a sphere, "
            "angles always exceed pi, and the "
            "excess equals the area times K.",
            duration=20,
        )
        title2 = self.ly.title("Geodesic Triangles")

        triangle_formula = MathTex(
            r"\alpha_1 + \alpha_2 + \alpha_3 = \pi + \iint_T K \, dA",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(triangle_formula, DOWN, title2)
        self.play(Write(triangle_formula), run_time=NORMAL)
        self.wait(0.5)

        items = [
            Text(
                "Flat: angles sum to \u03C0 (Euclidean)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Sphere: angles exceed \u03C0 (spherical excess)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Saddle: angles fall short of \u03C0",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=triangle_formula)

        self.wait(10.4)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Why Euler Characteristic?
    # ------------------------------------------------------------------ #
    def scene7_why_euler(self):
        self.ly.section_divider("4", "The Bridge: Geometry Meets Topology")
        self.add_subcaption(
            "Why does the Euler characteristic "
            "appear? Triangulate the surface into "
            "many small geodesic triangles. Apply "
            "the local theorem to each one. Sum "
            "over all triangles. The boundary "
            "terms cancel because interior edges "
            "are shared by adjacent triangles.",
            duration=18,
        )

        title = self.ly.title("Triangulation Argument")

        items = [
            Text(
                "Step 1: Triangulate the surface",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Step 2: Apply local GB to each triangle",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Step 3: Sum all triangles",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Step 4: Boundary terms cancel pairwise",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(11.8)
        self.ly.clear()

        self.add_subcaption(
            "After cancellation, only the curvature "
            "integrals remain. The sum of angle "
            "terms gives two pi times the Euler "
            "characteristic. The result is exactly "
            "the global Gauss-Bonnet theorem. "
            "Geometry on the left, topology on the "
            "right.",
            duration=17,
        )
        title2 = self.ly.title("The Result")

        result = MathTex(
            r"\underbrace{\iint_S K \, dA}_{\text{geometry}}"
            r"= \underbrace{2\pi \, \chi(S)}_{\text{topology}}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula_box = self.ly.formula_box(result, color=ACCENT)
        self.play(Write(formula_box[0]), run_time=NORMAL)
        self.play(Create(formula_box[1]), run_time=FAST)

        self.wait(0.5)

        bridge = Text(
            "The most profound equation in differential geometry",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(bridge, DOWN, formula_box)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(11.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary_outro(self):
        self.add_subcaption(
            "Let's recap. The global Gauss-Bonnet "
            "theorem says total curvature equals "
            "two pi times Euler characteristic. "
            "The local version adds the geodesic "
            "curvature boundary term. And the "
            "geometric version says holonomy "
            "equals the curvature integral. "
            "Three faces of the same truth.",
            duration=20,
        )
        title = self.ly.title("Three Forms of Gauss-Bonnet")

        items = [
            Text(
                "1. Global: \u222BK dA = 2\u03C0\u03C7(S)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "2. Local: \u222B\u03BA_g ds + \u222BK dA = 2\u03C0 \u2212 \u03A3(ext. \u2220)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "3. Geometric: holonomy = \u222BK dA",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(14.4)
        self.ly.clear()

        self.add_subcaption(
            "That's the Gauss-Bonnet theorem. It "
            "reveals that curvature, a geometric "
            "property, is controlled by topology. "
            "Next time, we'll begin our study of "
            "manifolds, generalizing surfaces to "
            "arbitrary dimensions. Thanks for "
            "watching!",
            duration=16,
        )
        self.wait(8.3)
        play_outro(self, "Manifolds Intro", "Differential Geometry")
