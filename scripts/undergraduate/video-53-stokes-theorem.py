"""
Video 53: Stokes' Theorem
Calculus III -- Multivariable Playlist -- Video 13 of 14

Covers: statement of Stokes' Theorem (3D generalization of Green's),
orientation conventions (right-hand rule), proof idea, the "many surfaces
one boundary" insight, worked example, connection to Green's Theorem,
preview of Divergence Theorem.

Render draft:  manim -ql scripts/undergraduate/video-53-stokes-theorem.py Video53_StokesTheorem
Render final:  manim -qh scripts/undergraduate/video-53-stokes-theorem.py Video53_StokesTheorem
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


class Video53_StokesTheorem(Scene):
    """Full video: Stokes' Theorem."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_statement()
        self.scene3_greens_special_case()
        self.scene4_many_surfaces()
        self.scene5_proof_idea()
        self.scene6_worked_example()
        self.scene7_summary()

    # ── Scene 1: Hook ────────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Green's Theorem connects line integrals and double integrals "
            "in the plane. But what if the boundary isn't flat? "
            "What if it wraps around a hemisphere or a cone? "
            "Stokes' Theorem answers this beautifully.",
            duration=24,
        )
        play_intro(self, "Stokes' Theorem",
                   "Calculus III -- Multivariable")

        title = self.ly.title("From Flat Planes to Curved Surfaces")

        question = Text(
            "Green's Theorem works for flat regions in the plane. "
            "What about surfaces that curve through 3D space?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(question)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        answer = Text(
            "Stokes' Theorem extends Green's to any surface in 3D!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(answer, DOWN, anchor=question, buff=0.5)
        self.play(FadeIn(answer, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 2: The Statement ───────────────────────────────────
    def scene2_statement(self):
        self.add_subcaption(
            "Stokes' Theorem states that the line integral of a vector "
            "field around a closed curve equals the surface integral of "
            "the curl over any surface bounded by that curve. "
            "The orientation is given by the right-hand rule.",
            duration=24,
        )
        self.ly.section_divider(1, "The Statement")

        title = self.ly.title("Stokes' Theorem")

        # The theorem formula
        theorem = MathTex(
            r"\oint_C \mathbf{F} \cdot d\mathbf{r}",
            r"=",
            r"\iint_S (\nabla \times \mathbf{F}) \cdot \mathbf{n}\,dS",
            font_size=HEADING_SIZE, color=WHITE,
        )
        theorem[0].set_color(PRIMARY)
        theorem[2].set_color(SECONDARY)
        self.ly.safe_place(theorem, DOWN, anchor=title, buff=0.5)
        ensure_fits(theorem)
        self.play(Write(theorem), run_time=SLOW)
        self.wait(1.5)

        # Remove formula, show definitions
        self.play(FadeOut(theorem), run_time=FAST)

        items = [
            Text(
                "C = closed boundary curve",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "S = any surface with boundary C",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "curl F = \u2207 \u00d7 F",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "n = unit normal (right-hand rule)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

    # ── Scene 3: Green's as Special Case ────────────────────────
    def scene3_greens_special_case(self):
        self.add_subcaption(
            "When the surface S lies flat in the xy-plane, "
            "the unit normal is just k-hat. "
            "The curl dotted with k-hat gives us exactly the "
            "two-dimensional curl from Green's Theorem. "
            "So Stokes' reduces to Green's when the surface is flat.",
            duration=24,
        )
        self.ly.section_divider(2, "Green's = Special Case of Stokes'")

        title = self.ly.title("Flat Surface in the xy-Plane")

        # When S is flat
        setup = Text(
            "If S lies in the xy-plane, then n = k-hat:",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(setup, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(setup, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        curl_k = MathTex(
            r"(\nabla \times \mathbf{F}) \cdot \mathbf{\hat{k}}",
            r"=",
            r"\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}",
            font_size=BODY_SIZE, color=WHITE,
        )
        curl_k[0].set_color(PRIMARY)
        curl_k[2].set_color(ACCENT)
        self.ly.safe_place(curl_k, DOWN, anchor=setup, buff=0.4)
        ensure_fits(curl_k)
        self.play(Write(curl_k), run_time=NORMAL)
        self.wait(1.5)

        # Conclusion
        self.play(FadeOut(setup), FadeOut(curl_k), run_time=FAST)

        conclusion = Text(
            "This is exactly the integrand from Green's Theorem!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(conclusion, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(conclusion, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1)

        note = Text(
            "Green's Theorem = Stokes' Theorem for flat surfaces",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=conclusion, buff=0.3)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 4: Many Surfaces, One Boundary ────────────────────
    def scene4_many_surfaces(self):
        self.add_subcaption(
            "Here is the most profound insight of Stokes' Theorem. "
            "The line integral around C depends only on the boundary, "
            "not on the specific surface you choose. "
            "A disk, a hemisphere, or a cone with the same boundary "
            "all give the same answer.",
            duration=24,
        )
        self.ly.section_divider(3, "Many Surfaces, One Boundary")

        title = self.ly.title("The Surface Doesn't Matter")

        items = [
            Text(
                "Same boundary curve C can bound many surfaces",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Disk, hemisphere, cone, or any surface with boundary C",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "The surface integral of curl F is the same for all of them",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Only the boundary matters \u2192 topological invariance",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        # Key formula
        self.play(FadeOut(self.mobjects[-1]), run_time=FAST)

        invariant = MathTex(
            r"\oint_C \mathbf{F} \cdot d\mathbf{r}",
            r"= \iint_{S_1} (\nabla \times \mathbf{F}) \cdot \mathbf{n}\,dS",
            r"= \iint_{S_2} (\nabla \times \mathbf{F}) \cdot \mathbf{n}\,dS",
            font_size=HEADING_SIZE, color=WHITE,
        )
        invariant[0].set_color(PRIMARY)
        invariant[1].set_color(SECONDARY)
        invariant[2].set_color(RED)
        self.ly.safe_place(invariant, DOWN, anchor=title, buff=3.0)
        ensure_fits(invariant)
        self.play(Write(invariant), run_time=SLOW)
        self.wait(2)
        self.ly.clear()

    # ── Scene 5: Proof Idea ─────────────────────────────────────
    def scene5_proof_idea(self):
        self.add_subcaption(
            "The proof mirrors Green's Theorem. We tile the surface "
            "with tiny patches. On each patch, the circulation equals "
            "the curl dotted with the normal times the patch area. "
            "Interior edges cancel because adjacent patches share "
            "edges in opposite directions. Only the boundary survives.",
            duration=24,
        )
        self.ly.section_divider(4, "Proof Idea")

        title = self.ly.title("Why Stokes' Theorem Works")

        items = [
            Text(
                "1. Tile surface S into tiny patches",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. Circulation on each patch \u2248 (curl F \u00b7 n) \u00d7 area",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "3. Interior edges cancel (opposite directions)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "4. Only boundary edges survive \u2192 line integral on C",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        # Conclusion
        conclusion = Text(
            "Sum over all patches = surface integral of curl = line integral on C",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(conclusion, DOWN, anchor=title, buff=3.0)
        self.play(FadeIn(conclusion, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 6: Worked Example ─────────────────────────────────
    def scene6_worked_example(self):
        self.add_subcaption(
            "Let's verify Stokes' Theorem with a concrete example. "
            "We use the vector field (y squared, minus x squared, z squared) "
            "around the unit circle at z equals zero, with the hemisphere "
            "as our surface. We'll compute both sides and check they match.",
            duration=24,
        )
        self.ly.section_divider(5, "Worked Example")

        title = self.ly.title("Verify Stokes' Theorem")

        # Problem setup
        problem = Text(
            "F = (y\u00b2, -x\u00b2, z\u00b2), C = x\u00b2 + y\u00b2 = 1 at z = 0",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(problem, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(problem, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Step 1: Compute curl
        step1 = Text("Step 1: Compute curl F", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(step1, DOWN, anchor=problem, buff=0.4)
        self.play(FadeIn(step1, shift=LEFT * 0.15), run_time=NORMAL)

        curl_f = MathTex(
            r"\nabla \times \mathbf{F} = \left(0,\, 0,\, -2x - 2y\right)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        curl_f.set_color_by_tex(r"-2x - 2y", ACCENT)
        self.ly.safe_place(curl_f, DOWN, anchor=step1, buff=0.3)
        ensure_fits(curl_f)
        self.play(Write(curl_f), run_time=NORMAL)
        self.wait(1)

        # Step 2: Surface integral
        self.play(FadeOut(step1), FadeOut(curl_f), run_time=FAST)

        step2 = Text("Step 2: Surface integral over hemisphere", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(step2, DOWN, anchor=problem, buff=0.4)
        self.play(FadeIn(step2, shift=LEFT * 0.15), run_time=NORMAL)

        normal_info = Text(
            "Hemisphere normal: n = (x, y, z), curl \u00b7 n = (-2x-2y)z",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(normal_info, DOWN, anchor=step2, buff=0.3)
        self.play(FadeIn(normal_info, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # In polar
        self.play(FadeOut(step2), FadeOut(normal_info), run_time=FAST)

        polar = Text("Switch to polar: the cos\u03b8 and sin\u03b8 terms integrate to zero", font_size=BODY_SIZE, color=DIM, font=SANS)
        self.ly.safe_place(polar, DOWN, anchor=problem, buff=0.4)
        self.play(FadeIn(polar, shift=LEFT * 0.15), run_time=NORMAL)

        result_surface = MathTex(
            r"\iint_S (\nabla \times \mathbf{F}) \cdot \mathbf{n}\,dS = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        result_surface.set_color_by_tex("0", ACCENT)
        self.ly.safe_place(result_surface, DOWN, anchor=polar, buff=0.3)
        self.play(Write(result_surface), run_time=NORMAL)
        self.wait(1)

        # Step 3: Verify with line integral
        self.play(FadeOut(polar), FadeOut(result_surface), run_time=FAST)

        step3 = Text("Direct line integral on C:", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(step3, DOWN, anchor=problem, buff=0.4)
        self.play(FadeIn(step3, shift=LEFT * 0.15), run_time=NORMAL)

        line_integral = MathTex(
            r"\oint_C \mathbf{F} \cdot d\mathbf{r} = 0 \quad \checkmark",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(line_integral, DOWN, anchor=step3, buff=0.3)
        self.play(Write(line_integral), run_time=NORMAL)

        verify = Text(
            "Both sides match! Stokes' Theorem verified.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(verify, DOWN, anchor=line_integral, buff=0.3)
        self.play(FadeIn(verify, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 7: Summary ───────────────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "Stokes' Theorem is the three-dimensional generalization of "
            "Green's Theorem. It says that the circulation of a vector "
            "field around a closed curve equals the surface integral of "
            "the curl over any surface bounded by that curve. "
            "Next up: the Divergence Theorem, the final piece.",
            duration=24,
        )
        self.ly.section_divider(6, "Summary")

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "Stokes': line integral = surface integral of curl",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "\u222e F\u00b7dr = \u222c\u222c (\u2207\u00d7F)\u00b7n dS",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Generalizes Green's Theorem to 3D surfaces",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Only boundary matters, not the specific surface",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

        play_outro(
            self,
            "Divergence Theorem",
            "Calculus III -- Multivariable",
        )
