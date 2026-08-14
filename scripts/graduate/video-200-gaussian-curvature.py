"""
Video 200: Gaussian Curvature -- Differential Geometry Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video200_GaussianCurvature

Topics: Gaussian curvature, Theorema Egregium, isometric invariance,
        constant curvature surfaces, developable surfaces.

Prerequisites: Video 198 (First Fundamental Form), Video 199 (Second
               Fundamental Form), Linear Algebra (determinants).

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


class Video200_GaussianCurvature(Scene):
    """Gaussian Curvature -- Differential Geometry Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_definition_examples()
        self.scene4_theorema_egregium()
        self.scene5_isometric_bending()
        self.scene6_k_from_first_form()
        self.scene7_constant_curvature()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook — The Most Surprising Theorem
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Gauss discovered something astonishing. "
            "The Gaussian curvature of a surface can "
            "be computed using only measurements on "
            "the surface itself. A flat sheet of paper "
            "and a cylinder have the same curvature: "
            "zero. But paper cannot be bent into a "
            "sphere.",
            duration=10,
        )
        play_intro(self, "Gaussian Curvature", "Differential Geometry")

        title = self.ly.title("The Theorema Egregium")

        items = [
            Text(
                "Paper → cylinder: OK (no stretching)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Paper → sphere: IMPOSSIBLE",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Why? Gaussian curvature is intrinsic.",
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
        self.ly.section_divider("1", "Definition and Examples")
        self.add_subcaption(
            "Gaussian curvature is the product of "
            "the two principal curvatures. It can "
            "also be computed from the fundamental "
            "form coefficients.",
            duration=6,
        )
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Definition and Examples
    # ------------------------------------------------------------------ #
    def scene3_definition_examples(self):
        self.add_subcaption(
            "The Gaussian curvature K is the product "
            "of the principal curvatures. In terms "
            "of the fundamental form coefficients, "
            "K equals eg minus f squared, divided "
            "by EG minus F squared.",
            duration=8,
        )
        title = self.ly.title("Definition")

        k_def = MathTex(
            r"K = \kappa_1 \cdot \kappa_2"
            r"= \frac{eg - f^2}{EG - F^2}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(k_def, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(k_def), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Examples
        self.add_subcaption(
            "The plane has K equals zero. The "
            "sphere has K equals one over R squared. "
            "The cylinder has K equals zero because "
            "one principal curvature is zero. The "
            "saddle has K less than zero.",
            duration=9,
        )
        title2 = self.ly.title("Examples")

        items = [
            Text(
                "Plane: K = 0  (flat everywhere)",
                font_size=BODY_SIZE, color=DIM, font=SANS,
            ),
            Text(
                "Sphere (radius R): K = 1/R²",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Cylinder: K = 0  (flat along axis)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Saddle: K < 0  (opposite curvature)",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title2)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: The Theorema Egregium
    # ------------------------------------------------------------------ #
    def scene4_theorema_egregium(self):
        self.ly.section_divider("2", "Theorema Egregium")
        self.ly.clear()

        self.add_subcaption(
            "Gauss's Theorema Egregium states that "
            "the Gaussian curvature is an isometric "
            "invariant. An isometry preserves the "
            "first fundamental form, so K, being "
            "computable from only E, F, and G, is "
            "preserved.",
            duration=9,
        )
        title = self.ly.title("The Remarkable Theorem")

        theorem = MathTex(
            r"K \text{ depends only on } E, F, G "
            r"\text{ and their derivatives}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(theorem, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(theorem), run_time=NORMAL)

        iso = Text(
            "Isometry = distance-preserving map → preserves K",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(iso, direction=DOWN, anchor=theorem, buff=0.4)
        self.play(FadeIn(iso, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Implications
        self.add_subcaption(
            "This means bending without stretching "
            "preserves Gaussian curvature. You can "
            "roll a plane into a cylinder because "
            "both have K equals zero. But you cannot "
            "bend a plane into a sphere because the "
            "sphere has positive curvature.",
            duration=9,
        )
        title2 = self.ly.title("Implications")

        items = [
            Text(
                "Bending = isometry (preserves K)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Plane → cylinder: K = 0 → 0  ✓",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Plane → sphere: K = 0 → 1/R²  ✗",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title2)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Isometric Bending Examples
    # ------------------------------------------------------------------ #
    def scene5_isometric_bending(self):
        self.add_subcaption(
            "A cone, minus its vertex, is locally "
            "isometric to a plane. The cylinder is "
            "globally isometric to the plane minus "
            "a line. These are developable surfaces.",
            duration=8,
        )
        title = self.ly.title("Developable Surfaces")

        items = [
            Text(
                "Cylinder ≅ plane (globally, K = 0)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Cone ≅ plane (locally, K = 0 away from vertex)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Tangent developable: envelope of tangent lines",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "All developable: K = 0 everywhere",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

        # Map projection
        self.add_subcaption(
            "A consequence: you cannot make a flat "
            "map of the Earth without distortion. "
            "The Earth has positive Gaussian curvature, "
            "but a flat map has zero. Any map "
            "projection must distort either areas, "
            "angles, or both.",
            duration=9,
        )
        title2 = self.ly.title("Map Projections")

        earth = Text(
            "Earth: K > 0 (sphere-like)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(earth, direction=DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(earth, shift=LEFT * 0.15), run_time=NORMAL)

        flat_map = Text(
            "Flat map: K = 0 (plane)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(flat_map, direction=DOWN, anchor=earth, buff=0.4)
        self.play(FadeIn(flat_map, shift=LEFT * 0.15), run_time=NORMAL)

        distort = Text(
            "→ Any projection distorts area or angles",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(distort, direction=DOWN, anchor=flat_map, buff=0.4)
        self.play(FadeIn(distort, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: K from the First Fundamental Form
    # ------------------------------------------------------------------ #
    def scene6_k_from_first_form(self):
        self.add_subcaption(
            "The explicit formula for K in terms of "
            "only the first fundamental form is "
            "long. It involves E, F, G and their "
            "first and second partial derivatives. "
            "We state it without full derivation.",
            duration=8,
        )
        title = self.ly.title("Brioschi Formula (Sketch)")

        brioschi = MathTex(
            r"K = \frac{1}{(EG-F^2)^2}\Big[",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(brioschi, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(brioschi), run_time=NORMAL)

        note = Text(
            "... involves E_u, E_v, E_uu, F_u, F_v, F_uv, G_u, G_v, G_vv ...",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=brioschi, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)

        key = Text(
            "Key: K is fully determined by E, F, G alone!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=note, buff=0.4)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # What this means
        self.add_subcaption(
            "This is the computational heart of the "
            "Theorema Egregium. Since K depends on "
            "only the first fundamental form, any "
            "isometry, which preserves the first "
            "form, automatically preserves K.",
            duration=8,
        )
        title2 = self.ly.title("What This Means")

        items = [
            Text(
                "K uses only E, F, G (no σ_uu · N needed)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Isometry preserves E, F, G",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Therefore: isometry preserves K. QED.",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title2)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Surfaces of Constant Curvature
    # ------------------------------------------------------------------ #
    def scene7_constant_curvature(self):
        self.add_subcaption(
            "Surfaces with constant Gaussian curvature "
            "everywhere form a special class. K equals "
            "zero gives developable surfaces. K "
            "positive gives spheres. K negative "
            "gives pseudospheres, which realize "
            "hyperbolic geometry.",
            duration=9,
        )
        title = self.ly.title("Constant Gaussian Curvature")

        items = [
            Text(
                "K = 0: planes, cylinders, cones (developable)",
                font_size=BODY_SIZE, color=DIM, font=SANS,
            ),
            Text(
                "K = 1/R² > 0: sphere (unique!)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "K = -1/R² < 0: pseudosphere (hyperbolic geometry)",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Connection: constant K ↔ non-Euclidean geometry",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary_outro(self):
        self.add_subcaption(
            "Gaussian curvature is the most important "
            "invariant of a surface. It is intrinsic, "
            "computed from the first fundamental form "
            "alone, and it is preserved by isometries. "
            "This is the Theorema Egregium.",
            duration=7,
        )
        title = self.ly.title("Key Results")

        items = [
            Text(
                "1. K = k₁·k₂ = (eg-f²)/(EG-F²)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. Theorema Egregium: K is isometric invariant",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3. K depends only on first fundamental form",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "4. Plane ≅ cylinder (K=0), sphere ≠ plane (K≠0)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "5. Constant K ↔ non-Euclidean geometry",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        self.add_subcaption(
            "Next time, we study geodesics, the "
            "straightest possible curves on a "
            "surface. These are the analogs of "
            "lines in curved geometry. Thank you "
            "for watching.",
            duration=7,
        )
        play_outro(
            self,
            next_video="Geodesics",
            next_playlist="Differential Geometry",
        )
