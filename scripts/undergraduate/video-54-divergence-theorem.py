"""
Video 54: Divergence Theorem
Calculus III -- Multivariable Playlist -- Video 14 of 14 (FINAL)

Covers: statement of the Divergence Theorem (Gauss's Theorem),
physical intuition (sources and sinks), connection to Green's Theorem
flux form, the FTC unification framework, proof idea (volume decomposition),
worked example (F = (x,y,z) through unit sphere), applications
(Gauss's law, fluid dynamics), and grand finale summary.

Render draft:  manim -ql scripts/undergraduate/video-54-divergence-theorem.py Video54_DivergenceTheorem
Render final:  manim -qh scripts/undergraduate/video-54-divergence-theorem.py Video54_DivergenceTheorem
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


class Video54_DivergenceTheorem(Scene):
    """Full video: Divergence Theorem — the grand finale of Calculus III."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_sources_sinks()
        self.scene3_statement()
        self.scene4_greens_special_case()
        self.scene5_ftc_unification()
        self.scene6_proof_idea()
        self.scene7_worked_example()
        self.scene8_applications_summary()

    # ── Scene 1: Hook — The Final Theorem ───────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "We've journeyed from tangent lines to surface integrals. "
            "Green's Theorem connected curves to areas. Stokes' Theorem "
            "connected curves to surfaces. Now, one final theorem connects "
            "surfaces to volumes. This is the grand finale of vector calculus.",
            duration=24,
        )
        play_intro(self, "Divergence Theorem",
                   "Calculus III -- Multivariable")

        title = self.ly.title("The Final Theorem")

        # Theorem progression
        progression_items = [
            Text(
                "Fundamental Theorem of Calculus",
                font_size=BODY_SIZE, color=DIM, font=SANS,
            ),
            Text(
                "Green's Theorem: curves \u2194 regions",
                font_size=BODY_SIZE, color=DIM, font=SANS,
            ),
            Text(
                "Stokes' Theorem: curves \u2194 surfaces",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Divergence Theorem: surfaces \u2194 volumes",
                font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
            ),
        ]
        self.ly.progressive_reveal(progression_items, start_from=title)
        self.wait(2)

        # Grand finale note
        self.ly.clear()
        finale = Text(
            "The capstone of multivariable calculus.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(finale)
        self.play(FadeIn(finale, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 2: Physical Intuition — Sources and Sinks ────────────
    def scene2_sources_sinks(self):
        self.add_subcaption(
            "Imagine a vector field representing fluid flow. "
            "The divergence at a point measures whether fluid is being "
            "created there, like a source, or destroyed there, like a sink. "
            "A positive divergence means fluid flows outward. "
            "A negative divergence means fluid flows inward. "
            "The total flux through a closed surface equals the total "
            "net creation of fluid inside.",
            duration=24,
        )
        self.ly.section_divider(1, "Sources and Sinks")

        title = self.ly.title("The Physical Picture")

        items = [
            Text(
                "Think of F as fluid velocity",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "div F > 0: source (fluid created, flows out)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "div F < 0: sink (fluid destroyed, flows in)",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Total outward flux = net creation inside",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        # Key formula
        self.ly.clear()
        title2 = self.ly.title("Flux = Source - Sink")

        insight = MathTex(
            r"\text{Flux through } \partial V",
            r"=",
            r"\iiint_V (\text{div}\, \mathbf{F})\, dV",
            font_size=HEADING_SIZE, color=WHITE,
        )
        insight[0].set_color(PRIMARY)
        insight[2].set_color(SECONDARY)
        self.ly.safe_place(insight, DOWN, anchor=title2, buff=0.5)
        ensure_fits(insight)
        self.play(Write(insight), run_time=SLOW)
        self.wait(2)

        note = Text(
            "Everything leaving the volume must have been created inside",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=insight, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 3: The Statement ─────────────────────────────────────
    def scene3_statement(self):
        self.add_subcaption(
            "The Divergence Theorem states that the outward flux of a "
            "vector field through a closed surface equals the triple "
            "integral of the divergence over the enclosed volume. "
            "The surface must be closed, meaning it completely encloses "
            "the volume with no gaps, and the normal always points outward.",
            duration=24,
        )
        self.ly.section_divider(2, "The Statement")

        title = self.ly.title("Divergence Theorem (Gauss's Theorem)")

        # The theorem formula
        theorem = MathTex(
            r"\oint \!\!\!\!\!\oint_S \mathbf{F} \cdot \mathbf{n}\,dS",
            r"=",
            r"\iiint_V (\nabla \cdot \mathbf{F})\,dV",
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
                "S = closed surface (boundary of V)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "V = volume enclosed by S",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "n = outward unit normal (always points OUT)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "div F = \u2207 \u00b7 F = \u2202P/\u2202x + \u2202Q/\u2202y + \u2202R/\u2202z",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        # Important note about outward normal
        self.ly.clear()
        title2 = self.ly.title("Key: Outward Normal")

        warn = Text(
            "The normal n must always point OUTWARD from the volume.",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(warn)
        self.play(FadeIn(warn, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1)

        note = Text(
            "This is different from Stokes', where the normal direction "
            "depends on the curve orientation via the right-hand rule.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=warn, buff=0.5)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 4: Green's Theorem as 2D Special Case ────────────────
    def scene4_greens_special_case(self):
        self.add_subcaption(
            "The flux form of Green's Theorem relates the flux through "
            "a closed curve to the double integral of divergence over the "
            "enclosed region. This is actually the two-dimensional version "
            "of the Divergence Theorem. When the volume flattens into a "
            "region and the surface becomes its boundary curve, the "
            "Divergence Theorem reduces exactly to the flux form of Green's.",
            duration=24,
        )
        self.ly.section_divider(3, "Green's as 2D Special Case")

        title = self.ly.title("From 2D to 3D")

        # 2D version
        label_2d = Text(
            "Flux form of Green's Theorem (2D):",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(label_2d, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(label_2d, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        green_flux = MathTex(
            r"\oint_C \mathbf{F} \cdot \mathbf{n}\,ds",
            r"=",
            r"\iint_D (\nabla \cdot \mathbf{F})\,dA",
            font_size=HEADING_SIZE, color=WHITE,
        )
        green_flux[0].set_color(PRIMARY)
        green_flux[2].set_color(ACCENT)
        self.ly.safe_place(green_flux, DOWN, anchor=label_2d, buff=0.4)
        ensure_fits(green_flux)
        self.play(Write(green_flux), run_time=NORMAL)
        self.wait(1.5)

        self.play(FadeOut(label_2d), FadeOut(green_flux), run_time=FAST)

        # 3D version
        label_3d = Text(
            "Divergence Theorem (3D):",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(label_3d, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(label_3d, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        div_theorem = MathTex(
            r"\oint \!\!\!\!\!\oint_S \mathbf{F} \cdot \mathbf{n}\,dS",
            r"=",
            r"\iiint_V (\nabla \cdot \mathbf{F})\,dV",
            font_size=HEADING_SIZE, color=WHITE,
        )
        div_theorem[0].set_color(PRIMARY)
        div_theorem[2].set_color(ACCENT)
        self.ly.safe_place(div_theorem, DOWN, anchor=label_3d, buff=0.4)
        ensure_fits(div_theorem)
        self.play(Write(div_theorem), run_time=NORMAL)
        self.wait(1.5)

        self.play(FadeOut(label_3d), FadeOut(div_theorem), run_time=FAST)

        # Connection
        connection = Text(
            "When the volume flattens to a region and the surface "
            "becomes its boundary curve, the Divergence Theorem "
            "reduces to Green's flux form.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.center_in_content(connection)
        self.play(FadeIn(connection, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        arrow_note = Text(
            "Green's \u2192 Divergence: curve flux \u2192 surface flux",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(arrow_note, DOWN, anchor=connection, buff=0.4)
        self.play(FadeIn(arrow_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 5: FTC Unification ────────────────────────────────────
    def scene5_ftc_unification(self):
        self.add_subcaption(
            "All four great theorems of vector calculus share one deep "
            "structure. The integral of a derivative over an interior equals "
            "something evaluated on the boundary. The Fundamental Theorem "
            "of Calculus, Green's Theorem, Stokes' Theorem, and the "
            "Divergence Theorem are all manifestations of the same idea "
            "in different dimensions.",
            duration=24,
        )
        self.ly.section_divider(4, "The Grand Unification")

        title = self.ly.title("One Idea, Four Theorems")

        # Show all four theorems side by side
        left_items = [
            Text("1D: FTC", font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD),
            MathTex(
                r"\int_a^b f'(x)\,dx = f(b) - f(a)",
                font_size=BODY_SIZE, color=WHITE,
            ),
            Text("", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2D: Green's", font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD),
            MathTex(
                r"\oint_C \mathbf{F} \cdot d\mathbf{r}",
                r"= \iint_D (\nabla \times \mathbf{F})_z\,dA",
                font_size=BODY_SIZE, color=WHITE,
            ),
        ]

        right_items = [
            Text("2D: Stokes'", font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD),
            MathTex(
                r"\oint_C \mathbf{F} \cdot d\mathbf{r}",
                r"= \iint_S (\nabla \times \mathbf{F}) \cdot \mathbf{n}\,dS",
                font_size=BODY_SIZE, color=WHITE,
            ),
            Text("", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3D: Divergence", font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD),
            MathTex(
                r"\oint \!\!\!\!\!\oint_S \mathbf{F} \cdot \mathbf{n}\,dS",
                r"= \iiint_V (\nabla \cdot \mathbf{F})\,dV",
                font_size=BODY_SIZE, color=WHITE,
            ),
        ]

        left_group, right_group = self.ly.two_columns(left_items, right_items, start_from=title)
        self.play(
            *[FadeIn(m, shift=LEFT * 0.15) for m in left_group],
            *[FadeIn(m, shift=RIGHT * 0.15) for m in right_group],
            run_time=SLOW,
        )
        self.wait(2)
        self.ly.clear()

        # Unifying message
        title2 = self.ly.title("The Pattern")

        pattern = Text(
            "Integral of derivative over interior = boundary evaluation",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(pattern)
        self.play(FadeIn(pattern, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1)

        items = [
            Text(
                "FTC: d/dx over interval = values at endpoints",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Green's: curl over region = circulation on boundary",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Stokes': curl over surface = circulation on boundary",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Divergence: div over volume = flux through boundary",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=pattern)
        self.wait(2)
        self.ly.clear()

    # ── Scene 6: Proof Idea ─────────────────────────────────────────
    def scene6_proof_idea(self):
        self.add_subcaption(
            "The proof idea mirrors Green's and Stokes'. We decompose the "
            "volume into tiny boxes. For each box, the flux through its "
            "faces equals the divergence times the box volume. When we "
            "sum over all boxes, the flux through interior faces cancels "
            "because adjacent boxes share faces in opposite orientations. "
            "Only the flux through the outer surface survives.",
            duration=24,
        )
        self.ly.section_divider(5, "Proof Idea")

        title = self.ly.title("Why It Works: Volume Decomposition")

        items = [
            Text(
                "1. Chop volume V into tiny boxes",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. Flux through each box \u2248 (div F) \u00d7 (box volume)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "3. Interior face fluxes cancel (adjacent boxes, opposite normals)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "4. Only outer surface flux survives",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        # Conclusion
        self.ly.clear()
        title2 = self.ly.title("Sum \u2192 Integral")

        conclusion1 = MathTex(
            r"\sum_{\text{boxes}} (\text{div}\, \mathbf{F}) \Delta V",
            r"\;\longrightarrow\;",
            r"\iiint_V (\nabla \cdot \mathbf{F})\,dV",
            font_size=HEADING_SIZE, color=WHITE,
        )
        conclusion1[0].set_color(DIM)
        conclusion1[2].set_color(PRIMARY)
        self.ly.safe_place(conclusion1, DOWN, anchor=title2, buff=0.5)
        ensure_fits(conclusion1)
        self.play(Write(conclusion1), run_time=SLOW)
        self.wait(1)

        conclusion2 = Text(
            "Internal fluxes cancel \u2192 only surface flux remains",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(conclusion2, DOWN, anchor=conclusion1, buff=0.4)
        self.play(FadeIn(conclusion2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 7: Worked Example ────────────────────────────────────
    def scene7_worked_example(self):
        self.add_subcaption(
            "Let's verify the Divergence Theorem with F equals x, y, z "
            "through the unit sphere. First we compute the divergence, "
            "which is three. Then we evaluate the triple integral of "
            "three over the unit ball, which gives four pi. For the "
            "direct surface integral, the normal to the sphere is x, y, z, "
            "so F dot n equals x squared plus y squared plus z squared, "
            "which equals one on the sphere. The surface integral is the "
            "surface area, which is also four pi. Both methods match!",
            duration=24,
        )
        self.ly.section_divider(6, "Worked Example")

        title = self.ly.title("Verify the Divergence Theorem")

        # Problem setup
        problem = Text(
            "F = (x, y, z),  S: x\u00b2 + y\u00b2 + z\u00b2 = 1  (unit sphere)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(problem, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(problem, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Method 1: Divergence Theorem
        method1_label = Text(
            "Method 1: Divergence Theorem",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(method1_label, DOWN, anchor=problem, buff=0.4)
        self.play(FadeIn(method1_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        div_f = MathTex(
            r"\nabla \cdot \mathbf{F} = \frac{\partial x}{\partial x}"
            r" + \frac{\partial y}{\partial y} + \frac{\partial z}{\partial z}"
            r" = 3",
            font_size=HEADING_SIZE, color=WHITE,
        )
        div_f.set_color_by_tex("= 3", ACCENT)
        self.ly.safe_place(div_f, DOWN, anchor=method1_label, buff=0.3)
        ensure_fits(div_f)
        self.play(Write(div_f), run_time=NORMAL)
        self.wait(1)

        triple_int = MathTex(
            r"\iiint_V 3\,dV = 3 \cdot \frac{4\pi}{3} = 4\pi",
            font_size=HEADING_SIZE, color=WHITE,
        )
        triple_int.set_color_by_tex("4\\pi", ACCENT)
        self.ly.safe_place(triple_int, DOWN, anchor=div_f, buff=0.3)
        ensure_fits(triple_int)
        self.play(Write(triple_int), run_time=NORMAL)
        self.wait(1)

        # Transition to Method 2
        self.play(
            FadeOut(method1_label), FadeOut(div_f), FadeOut(triple_int),
            run_time=FAST,
        )

        # Method 2: Direct surface integral
        method2_label = Text(
            "Method 2: Direct Surface Integral",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(method2_label, DOWN, anchor=problem, buff=0.4)
        self.play(FadeIn(method2_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        normal_info = Text(
            "Sphere normal: n = (x, y, z),  so F \u00b7 n = x\u00b2 + y\u00b2 + z\u00b2 = 1",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(normal_info, DOWN, anchor=method2_label, buff=0.3)
        self.play(FadeIn(normal_info, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        surface_int = MathTex(
            r"\oint \!\!\!\!\!\oint_S 1\,dS = \text{Surface Area} = 4\pi",
            font_size=HEADING_SIZE, color=WHITE,
        )
        surface_int.set_color_by_tex("4\\pi", ACCENT)
        self.ly.safe_place(surface_int, DOWN, anchor=normal_info, buff=0.3)
        ensure_fits(surface_int)
        self.play(Write(surface_int), run_time=NORMAL)
        self.wait(1)

        # Verification
        self.play(FadeOut(method2_label), FadeOut(normal_info), FadeOut(surface_int), run_time=FAST)

        verify = MathTex(
            r"4\pi = 4\pi \quad \checkmark",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(verify)
        self.play(Write(verify), run_time=SLOW)
        self.wait(1)

        verify_text = Text(
            "Both methods give the same answer. Divergence Theorem verified!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(verify_text, DOWN, anchor=verify, buff=0.4)
        self.play(FadeIn(verify_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 8: Applications and Grand Finale Summary ────────────
    def scene8_applications_summary(self):
        self.add_subcaption(
            "And so we reach the end of Calculus Three. From tangent "
            "lines and derivatives, through integrals in multiple "
            "dimensions, vector fields, line integrals, surface integrals, "
            "and the four great theorems of vector calculus. "
            "Green's Theorem, Stokes' Theorem, and the Divergence Theorem "
            "all generalize the Fundamental Theorem of Calculus to higher "
            "dimensions. Thank you for joining this mathematical journey.",
            duration=24,
        )
        self.ly.section_divider(8, "The Grand Finale")

        title = self.ly.title("Calculus III Complete")

        items = [
            Text(
                "Green's: line integral = curl integral over region",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Stokes': line integral = curl integral over surface",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Divergence: surface flux = div integral over volume",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "All unify: interior derivative = boundary evaluation",
                font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

        # Final message
        title2 = self.ly.title("From Tangent Lines to the Divergence Theorem")

        journey = Text(
            "The complete multivariable calculus journey.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(journey)
        self.play(FadeIn(journey, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1)

        thank_you = Text(
            "Thank you for watching.",
            font_size=TITLE_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(thank_you, DOWN, anchor=journey, buff=0.6)
        self.play(Write(thank_you), run_time=SLOW)
        self.wait(2)
        self.ly.clear()

        # Outro — no next video since this is the final one
        play_outro(
            self,
            next_video="",
            next_playlist="",
        )
