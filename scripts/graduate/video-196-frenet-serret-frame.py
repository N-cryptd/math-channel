"""
Video 196: Frenet-Serret Frame -- Differential Geometry Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video196_FrenetSerretFrame

Topics: TNB frame (tangent, normal, binormal), osculating plane,
        Frenet-Serret formulas, torsion, fundamental theorem of space curves.

Prerequisites: Video 194 (Curves in R^n), Video 195 (Arc Length & Curvature),
               Linear Algebra (cross products, orthonormal bases).

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


class Video196_FrenetSerretFrame(Scene):
    """Frenet-Serret Frame -- Differential Geometry Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_tangent_normal()
        self.scene4_binormal_tnb()
        self.scene5_frenet_serret_formulas()
        self.scene6_torsion_geometric()
        self.scene7_helix_example()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook — Bending vs Twisting
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Imagine driving along a winding mountain road. "
            "The road curves left and right. That is "
            "bending. But it also banks into the "
            "hillside. That is twisting. In differential "
            "geometry, curvature measures bending and "
            "torsion measures twisting.",
            duration=10,
        )
        play_intro(self, "Frenet-Serret Frame", "Differential Geometry")

        title = self.ly.title("Bending vs Twisting")

        items = [
            Text(
                "Planar curve: pure bending",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Space curve: bending + twisting",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "What makes them different?",
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
        self.ly.section_divider("1", "The TNB Frame")
        self.add_subcaption(
            "Today we build the Frenet-Serret frame, the "
            "natural moving coordinate system attached "
            "to every point of a space curve. Three "
            "orthonormal vectors: tangent, normal, and "
            "binormal.",
            duration=7,
        )
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Tangent and Normal Vectors
    # ------------------------------------------------------------------ #
    def scene3_tangent_normal(self):
        self.add_subcaption(
            "From the arc-length parametrization, the "
            "unit tangent vector is T of s equals alpha "
            "prime of s. Since the speed is one, this "
            "is already a unit vector.",
            duration=7,
        )
        title = self.ly.title("Unit Tangent Vector")

        t_def = MathTex(
            r"\mathbf{T}(s) = \alpha'(s)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(t_def, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(t_def), run_time=NORMAL)

        unit_note = Text(
            "|T| = 1  (unit vector by arc-length param.)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(unit_note, direction=DOWN, anchor=t_def, buff=0.4)
        self.play(FadeIn(unit_note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # T' is perpendicular to T
        self.add_subcaption(
            "Since T has length one, differentiating T "
            "dot T equals one gives two T prime equals "
            "zero. So T prime is perpendicular to T. "
            "It points toward the center of curvature.",
            duration=8,
        )
        title2 = self.ly.title("T prime is Perpendicular")

        t_perp = MathTex(
            r"\mathbf{T} \cdot \mathbf{T} = 1 "
            r"\;\Longrightarrow\; 2\,\mathbf{T}' \cdot \mathbf{T} = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(t_perp, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(t_perp), run_time=NORMAL)

        note = Text(
            "T'(s) is perpendicular to T(s)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=t_perp, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Principal normal
        self.add_subcaption(
            "The principal normal vector N is the unit "
            "vector in the direction of T prime. Since "
            "T prime has magnitude kappa, we write N "
            "equals T prime over kappa. The osculating "
            "plane is the plane spanned by T and N.",
            duration=9,
        )
        title3 = self.ly.title("Principal Normal Vector")

        n_def = MathTex(
            r"\mathbf{N}(s) = \frac{\mathbf{T}'(s)}"
            r"{|\mathbf{T}'(s)|} = \frac{\mathbf{T}'(s)}"
            r"{\kappa(s)}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(n_def, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(n_def), run_time=NORMAL)

        osc = Text(
            "Osculating plane = span{T, N}",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(osc, direction=DOWN, anchor=n_def, buff=0.4)
        self.play(FadeIn(osc, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Binormal Vector and TNB Frame
    # ------------------------------------------------------------------ #
    def scene4_binormal_tnb(self):
        self.add_subcaption(
            "The binormal vector is the cross product "
            "T cross N. Together with T and N, it forms "
            "a right-handed orthonormal basis for R "
            "three at every point. This is the TNB "
            "frame, a moving coordinate system.",
            duration=9,
        )
        title = self.ly.title("The Binormal Vector")

        b_def = MathTex(
            r"\mathbf{B}(s) = \mathbf{T}(s) \times \mathbf{N}(s)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(b_def, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(b_def), run_time=NORMAL)

        ortho = Text(
            "{T, N, B} forms an orthonormal basis",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(ortho, direction=DOWN, anchor=b_def, buff=0.4)
        self.play(FadeIn(ortho, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Three planes
        self.add_subcaption(
            "The three pairs of frame vectors define "
            "three planes. The osculating plane spans "
            "T and N. The normal plane spans N and B. "
            "The rectifying plane spans T and B. The "
            "key question: how does this frame change "
            "along the curve?",
            duration=9,
        )
        title2 = self.ly.title("Three Planes")

        items = [
            Text(
                "Osculating plane: span{T, N}",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Normal plane: span{N, B}",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Rectifying plane: span{T, B}",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title2)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Frenet-Serret Formulas
    # ------------------------------------------------------------------ #
    def scene5_frenet_serret_formulas(self):
        self.ly.section_divider("2", "The Frenet-Serret Formulas")
        self.ly.clear()

        # T' formula
        self.add_subcaption(
            "The first formula is by definition. T "
            "prime equals kappa times N. The tangent "
            "vector changes in the direction of the "
            "normal, at a rate given by the curvature.",
            duration=7,
        )
        title = self.ly.title("Formula 1: Tangent")

        f1 = MathTex(
            r"\mathbf{T}'(s) = \kappa(s)\,\mathbf{N}(s)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(f1, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(f1), run_time=NORMAL)

        note1 = Text(
            "By definition of N (immediate)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(note1, direction=DOWN, anchor=f1, buff=0.4)
        self.play(FadeIn(note1, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # B' formula
        self.add_subcaption(
            "For the binormal, since B equals T cross "
            "N, differentiate using the product rule. "
            "T prime is parallel to N, so the first "
            "cross product vanishes. B prime must be "
            "perpendicular to both B and T, so B prime "
            "is parallel to N. Define torsion tau so "
            "that B prime equals negative tau times N.",
            duration=11,
        )
        title2 = self.ly.title("Formula 2: Binormal")

        f2 = MathTex(
            r"\mathbf{B}'(s) = -\tau(s)\,\mathbf{N}(s)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(f2, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(f2), run_time=NORMAL)

        note2 = Text(
            "tau(s) = torsion (twisting rate)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note2, direction=DOWN, anchor=f2, buff=0.4)
        self.play(FadeIn(note2, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # N' formula
        self.add_subcaption(
            "Since N equals B cross T, differentiating "
            "and substituting gives N prime equals "
            "negative kappa T plus tau B. Now we have "
            "all three Frenet-Serret formulas. They "
            "encode the entire geometry using just "
            "curvature and torsion.",
            duration=9,
        )
        title3 = self.ly.title("Formula 3: Normal")

        f3 = MathTex(
            r"\mathbf{N}'(s) = -\kappa(s)\,\mathbf{T}(s)"
            r" + \tau(s)\,\mathbf{B}(s)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(f3, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(f3), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # All three together
        self.add_subcaption(
            "Together, the three Frenet-Serret formulas "
            "describe exactly how the moving frame "
            "changes along the curve. Two scalar "
            "functions, curvature and torsion, encode "
            "the complete geometry.",
            duration=7,
        )
        title4 = self.ly.title("The Frenet-Serret System")

        all_formulas = MathTex(
            r"\mathbf{T}' &= \kappa\,\mathbf{N} \\"
            r"\mathbf{N}' &= -\kappa\,\mathbf{T} + \tau\,\mathbf{B} \\"
            r"\mathbf{B}' &= -\tau\,\mathbf{N}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(all_formulas, direction=DOWN, anchor=title4, buff=0.5)
        self.play(Write(all_formulas), run_time=SLOW)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Torsion — Geometric Meaning
    # ------------------------------------------------------------------ #
    def scene6_torsion_geometric(self):
        self.add_subcaption(
            "Curvature measures how much the curve "
            "bends, how fast T rotates within the "
            "osculating plane. Torsion measures how "
            "much the curve twists, how fast the "
            "osculating plane itself rotates.",
            duration=8,
        )
        title = self.ly.title("Curvature vs Torsion")

        items = [
            Text(
                "kappa = bending (T rotates in osc. plane)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "tau = twisting (osculating plane rotates)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Curvature: how much you TURN",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Torsion: how much you TWIST",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

        # tau = 0 planar
        self.add_subcaption(
            "If torsion is zero everywhere, the "
            "osculating plane never changes and the "
            "curve is planar. A circle has curvature "
            "but zero torsion. A helix has both. "
            "The sign of torsion gives the handedness.",
            duration=8,
        )
        title2 = self.ly.title("Interpretation")

        items2 = [
            Text(
                "tau = 0 everywhere: curve is planar",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Circle: kappa > 0, tau = 0",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Helix: kappa > 0, tau > 0",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Helix Example
    # ------------------------------------------------------------------ #
    def scene7_helix_example(self):
        self.add_subcaption(
            "Let us compute the Frenet frame for the "
            "standard helix. We already know the "
            "curvature is one half from the previous "
            "video. Now we find the torsion.",
            duration=7,
        )
        title = self.ly.title("Helix: Frenet Frame")

        helix_eq = MathTex(
            r"\gamma(t) = (\cos t,\,\sin t,\, t), "
            r"\quad |\gamma'| = \sqrt{2}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(helix_eq, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(helix_eq), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # TNB computation summary
        self.add_subcaption(
            "The tangent T points along the helix. The "
            "normal N points inward toward the axis. "
            "The binormal B completes the right-handed "
            "frame. Curvature kappa equals one half.",
            duration=7,
        )
        title2 = self.ly.title("TNB for the Helix")

        t_vec = MathTex(
            r"\mathbf{T} = \frac{1}{\sqrt{2}}"
            r"(-\sin\theta,\, \cos\theta,\, 1)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(t_vec, direction=DOWN, anchor=title2, buff=0.4)
        self.play(Write(t_vec), run_time=NORMAL)

        n_vec = MathTex(
            r"\mathbf{N} = (-\cos\theta,\, -\sin\theta,\, 0)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(n_vec, direction=DOWN, anchor=t_vec, buff=0.3)
        self.play(Write(n_vec), run_time=NORMAL)

        kappa_h = MathTex(
            r"\kappa = \frac{1}{2}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(kappa_h, direction=DOWN, anchor=n_vec, buff=0.3)
        self.play(Write(kappa_h), run_time=NORMAL)

        self.wait(0.5)
        self.ly.clear()

        # Torsion result
        self.add_subcaption(
            "Differentiating the binormal vector B, "
            "we find the torsion is also one half. "
            "The helix has equal curvature and "
            "torsion. This is a remarkable property "
            "unique to the circular helix.",
            duration=8,
        )
        title3 = self.ly.title("Torsion of the Helix")

        b_prime = MathTex(
            r"\mathbf{B}' = -\frac{1}{2}\,\mathbf{N}"
            r"\quad \Longrightarrow \quad \tau = \frac{1}{2}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(b_prime, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(b_prime), run_time=NORMAL)

        key = Text(
            "Helix: kappa = tau = 1/2  (equal!)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=b_prime, buff=0.4)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary, Fundamental Theorem, and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary_outro(self):
        self.add_subcaption(
            "Today we built the Frenet-Serret frame, "
            "the complete moving coordinate system for "
            "space curves. Three orthonormal vectors "
            "governed by curvature and torsion. The "
            "fundamental theorem says these two "
            "functions uniquely determine the curve.",
            duration=10,
        )
        title = self.ly.title("Summary")

        items = [
            Text(
                "1. T, N, B: moving orthonormal frame",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "2. Frenet-Serret formulas",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "3. kappa = how fast curve BENDS",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "4. tau = how fast curve TWISTS",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "5. Helix: kappa = tau = 1/2",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()

        # Fundamental theorem
        self.add_subcaption(
            "The fundamental theorem of space curves: "
            "a curve is uniquely determined, up to "
            "rigid motion, by its curvature and "
            "torsion. Two curves with the same kappa "
            "and tau are the same curve.",
            duration=7,
        )
        title2 = self.ly.title("Fundamental Theorem")

        theorem = Text(
            "Curvature + Torsion uniquely determine",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(theorem, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(theorem), run_time=NORMAL)

        theorem2 = Text(
            "the curve (up to rigid motion)",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(theorem2, direction=DOWN, anchor=theorem, buff=0.3)
        self.play(FadeIn(theorem2, shift=LEFT * 0.15), run_time=NORMAL)

        self.wait(1.5)
        self.ly.clear()

        play_outro(self, "Surfaces in R^3", "Differential Geometry")
