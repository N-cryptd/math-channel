"""
Video 52: Green's Theorem
Calculus III -- Multivariable Playlist -- Video 12 of 14

Covers: statement of Green's Theorem (circulation and flux forms),
proof idea, worked examples, applications (area from line integral).

Render draft:  manim -ql scripts/undergraduate/video-52-greens-theorem.py Video52_GreensTheorem
Render final:  manim -qh scripts/undergraduate/video-52-greens-theorem.py Video52_GreensTheorem
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


class Video52_GreensTheorem(Scene):
    """Full video: Green's Theorem."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_circulation_form()
        self.scene3_flux_form()
        self.scene4_proof_idea()
        self.scene5_worked_example()
        self.scene6_applications()
        self.scene7_summary()

    # ── Scene 1: Hook ────────────────────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "There's a beautiful connection between integrating along "
            "a closed curve and integrating over the region it "
            "encloses. Green's Theorem reveals this bridge.",
            duration=15,
        )
        play_intro(self, "Green's Theorem",
                   "Calculus III -- Multivariable")

        title = self.ly.title("Line Integral ↔ Double Integral")

        question = Text(
            "Can a line integral around a closed curve be "
            "replaced by a double integral over the interior?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(question)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        answer = Text(
            "Yes! That's Green's Theorem.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(answer, DOWN, anchor=question, buff=0.5)
        self.play(FadeIn(answer, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 2: The Circulation Form ─────────────────────────────
    def scene2_circulation_form(self):
        self.add_subcaption(
            "Green's Theorem says: the circulation of a vector field "
            "around the positively oriented boundary of a region equals "
            "the double integral of the curl over that region.",
            duration=18,
        )
        self.ly.section_divider(1, "The Circulation Form")

        title = self.ly.title("Green's Theorem (Circulation)")

        # Setup
        setup = Text(
            "Let F = (P, Q), C = boundary of D (counterclockwise)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(setup, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(setup, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # The theorem
        theorem = MathTex(
            r"\oint_C \mathbf{F} \cdot d\mathbf{r}",
            r"=",
            r"\iint_D \left(\frac{\partial Q}{\partial x}",
            r"-",
            r"\frac{\partial P}{\partial y}\right) dA",
            font_size=HEADING_SIZE, color=WHITE,
        )
        theorem[0].set_color(PRIMARY)
        theorem[2].set_color(SECONDARY)
        theorem[4].set_color(RED)
        self.ly.safe_place(theorem, DOWN, anchor=setup, buff=0.5)
        ensure_fits(theorem)
        self.play(Write(theorem), run_time=SLOW)
        self.wait(1.5)

        # Key point
        self.play(FadeOut(setup), FadeOut(theorem), run_time=FAST)

        insight = Text(
            "Left side: work done circulating around C",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        insight2 = Text(
            "Right side: total curl inside region D",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(insight2, DOWN, anchor=insight, buff=0.3)
        self.play(FadeIn(insight2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 3: The Flux Form ───────────────────────────────────
    def scene3_flux_form(self):
        self.add_subcaption(
            "There is also a flux version of Green's Theorem. It relates "
            "the flux of a vector field across the boundary to the "
            "total divergence inside the region.",
            duration=18,
        )
        self.ly.section_divider(2, "The Flux Form")

        title = self.ly.title("Green's Theorem (Flux)")

        theorem = MathTex(
            r"\oint_C \mathbf{F} \cdot \mathbf{n}\,ds",
            r"=",
            r"\iint_D \left(\frac{\partial P}{\partial x}",
            r"+",
            r"\frac{\partial Q}{\partial y}\right) dA",
            font_size=HEADING_SIZE, color=WHITE,
        )
        theorem[0].set_color(PRIMARY)
        theorem[2].set_color(SECONDARY)
        theorem[4].set_color(ACCENT)
        self.ly.safe_place(theorem, DOWN, anchor=title, buff=0.5)
        ensure_fits(theorem)
        self.play(Write(theorem), run_time=SLOW)
        self.wait(1.5)

        # Div notation
        self.play(FadeOut(theorem), run_time=FAST)

        div_form = MathTex(
            r"\oint_C \mathbf{F} \cdot \mathbf{n}\,ds",
            r"=",
            r"\iint_D (\nabla \cdot \mathbf{F})\,dA",
            font_size=HEADING_SIZE, color=WHITE,
        )
        div_form[0].set_color(PRIMARY)
        div_form[2].set_color(ACCENT)
        self.ly.safe_place(div_form, DOWN, anchor=title, buff=0.5)
        self.play(Write(div_form), run_time=SLOW)

        note = Text(
            "Flux across boundary = total divergence inside",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=div_form, buff=0.3)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)
        self.ly.clear()

    # ── Scene 4: Proof Idea ──────────────────────────────────────
    def scene4_proof_idea(self):
        self.add_subcaption(
            "The proof idea is elegant. Divide the region into tiny "
            "rectangles. On each rectangle, the circulation equals "
            "the curl times the area. Interior edges cancel out because "
            "adjacent rectangles share edges in opposite directions.",
            duration=24,
        )
        self.ly.section_divider(3, "Proof Idea")

        title = self.ly.title("Why Green's Theorem Works")

        items = [
            Text(
                "1. Tile region D with small rectangles",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "2. Circulation on each rectangle \u2248 curl \u00d7 area",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "3. Interior edges cancel (traversed twice, opposite ways)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "4. Only boundary edges survive \u2192 line integral",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        # Conclusion
        conclusion = Text(
            "Sum of (curl \u00d7 area) = ∫∫ curl dA = ∮ F \u00b7 dr",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(conclusion, DOWN, anchor=title, buff=3.0)
        self.play(FadeIn(conclusion, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 5: Worked Example ──────────────────────────────────
    def scene5_worked_example(self):
        self.add_subcaption(
            "Let's verify Green's Theorem with a concrete example. "
            "Use the vector field (y squared, x squared) around the "
            "unit square from zero to one. We'll compute both sides "
            "and confirm they match.",
            duration=24,
        )
        self.ly.section_divider(4, "Worked Example")

        title = self.ly.title("Verify Green's Theorem")

        # Problem
        problem = Text(
            "F(x,y) = (y\u00b2, x\u00b2), C = boundary of [0,1]\u00d7[0,1]",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(problem, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(problem, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Right side: curl
        curl_label = Text("Right side (double integral):", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(curl_label, DOWN, anchor=problem, buff=0.4)
        self.play(FadeIn(curl_label, shift=LEFT * 0.15), run_time=NORMAL)

        curl = MathTex(
            r"\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}",
            r"= 2x - 2y",
            font_size=HEADING_SIZE, color=WHITE,
        )
        curl[1].set_color(ACCENT)
        self.ly.safe_place(curl, DOWN, anchor=curl_label, buff=0.3)
        self.play(Write(curl), run_time=NORMAL)
        self.wait(1)

        # Integral result
        self.play(FadeOut(curl_label), FadeOut(curl), run_time=FAST)

        result = MathTex(
            r"\iint_D (2x - 2y)\,dA = 0",
            r"\quad \text{(by symmetry)}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        result[0].set_color(SECONDARY)
        result[1].set_color(DIM)
        self.ly.safe_place(result, DOWN, anchor=problem, buff=0.4)
        ensure_fits(result)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1)

        # Left side confirmation
        self.play(FadeOut(result), run_time=FAST)

        confirm = Text(
            "Direct line integral also gives 0 ✓",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(confirm, DOWN, anchor=problem, buff=0.4)
        self.play(FadeIn(confirm, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 6: Applications ───────────────────────────────────
    def scene6_applications(self):
        self.add_subcaption(
            "Green's Theorem has a surprising application: computing "
            "the area of a region using only a line integral around "
            "its boundary. This is the principle behind mechanical "
            "planimeters used in engineering.",
            duration=24,
        )
        self.ly.section_divider(5, "Applications")

        title = self.ly.title("Area From a Line Integral")

        area_label = Text(
            "Set F = (-y/2, x/2), then the curl equals 1:",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(area_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(area_label, shift=LEFT * 0.15), run_time=NORMAL)

        curl_check = MathTex(
            r"\frac{\partial}{\partial x}\!\left(\frac{x}{2}\right)",
            r"- \frac{\partial}{\partial y}\!\left(-\frac{y}{2}\right)",
            r"= \frac{1}{2} + \frac{1}{2} = 1",
            font_size=BODY_SIZE, color=WHITE,
        )
        curl_check[2].set_color(ACCENT)
        self.ly.safe_place(curl_check, DOWN, anchor=area_label, buff=0.3)
        ensure_fits(curl_check)
        self.play(Write(curl_check), run_time=NORMAL)
        self.wait(1)

        # Area formula
        self.play(FadeOut(area_label), FadeOut(curl_check), run_time=FAST)

        area_formula = MathTex(
            r"\text{Area}(D) = \frac{1}{2}\oint_C x\,dy - y\,dx",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(area_formula, DOWN, anchor=title, buff=0.5)
        self.play(Write(area_formula), run_time=SLOW)
        self.wait(1.5)

        planimeter = Text(
            "This is how mechanical planimeters measure area!",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(planimeter, DOWN, anchor=area_formula, buff=0.3)
        self.play(FadeIn(planimeter, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 7: Summary ────────────────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "Green's Theorem connects line integrals and double integrals "
            "over a region and its boundary. The circulation form uses "
            "the curl, and the flux form uses the divergence. "
            "Applications include simplifying line integrals and "
            "computing areas.",
            duration=24,
        )
        self.ly.section_divider(6, "Summary")

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "Green's Theorem: boundary line integral = interior double integral",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Circulation form: \u222e F\u00b7dr = \u222c\u222c (curl F) dA",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Flux form: \u222e F\u00b7n ds = \u222c\u222c (div F) dA",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Area formula: A = (1/2) \u222e (x dy - y dx)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

        play_outro(
            self,
            "Stokes' Theorem",
            "Calculus III -- Multivariable",
        )
