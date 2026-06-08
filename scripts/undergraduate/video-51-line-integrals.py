"""
Video 51: Line Integrals
Calculus III -- Multivariable Playlist -- Video 11 of 14

Covers: scalar line integrals (mass of a wire), vector line integrals
(work by a force field), Fundamental Theorem for Line Integrals,
conservative fields, path independence, potential functions.

Render draft:  manim -ql scripts/undergraduate/video-51-line-integrals.py Video51_LineIntegrals
Render final:  manim -qh scripts/undergraduate/video-51-line-integrals.py Video51_LineIntegrals
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


class Video51_LineIntegrals(Scene):
    """Full video: Line Integrals."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_scalar_line_integral()
        self.scene3_vector_line_integral()
        self.scene4_conservative_fields()
        self.scene5_path_independence()
        self.scene6_worked_example()
        self.scene7_summary()

    # ── Scene 1: Hook — Integrating Along a Curve ───────────────
    def scene1_hook(self):
        self.add_subcaption(
            "We've integrated over intervals, regions, and solids. "
            "Now imagine integrating along a curved path. What's the "
            "total mass of a thin wire whose density varies?",
            duration=18,
        )
        play_intro(self, "Line Integrals",
                   "Calculus III -- Multivariable")

        title = self.ly.title("Integrating Along a Curve")

        question = Text(
            "What is the mass of a wire whose density "
            "varies from point to point?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.center_in_content(question)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        answer = Text(
            "Answer: the line integral of the density function",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(answer, DOWN, anchor=question, buff=0.5)
        self.play(FadeIn(answer, shift=UP * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 2: Scalar Line Integral — Mass of a Wire ──────────
    def scene2_scalar_line_integral(self):
        self.add_subcaption(
            "The scalar line integral adds up a function's values along "
            "a curve. We parameterize the curve, and the arc length "
            "element ds becomes the speed times dt.",
            duration=18,
        )
        self.ly.section_divider(1, "Scalar Line Integral")

        title = self.ly.title("Mass of a Wire")

        # Setup
        setup_label = Text(
            "Curve C parameterized by r(t), density f(x, y):",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(setup_label, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(setup_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        formula = MathTex(
            r"\int_C f(x,y)\,ds",
            r"=",
            r"\int_a^b f(r(t))\,|r'(t)|\,dt",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula[0].set_color(PRIMARY)
        formula[2].set_color(ACCENT)
        self.ly.safe_place(formula, DOWN, anchor=setup_label, buff=0.4)
        self.play(Write(formula), run_time=SLOW)
        self.wait(1.5)

        # Key insight
        self.play(FadeOut(setup_label), FadeOut(formula), run_time=FAST)

        insight = Text(
            "ds = |r'(t)| dt converts curve length to parameter",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.center_in_content(insight)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)

        # Special case: arc length
        special = Text(
            "When f = 1: integral gives the arc length of C",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(special, DOWN, anchor=insight, buff=0.4)
        self.play(FadeIn(special, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)
        self.ly.clear()

    # ── Scene 3: Vector Line Integral — Work ─────────────────────
    def scene3_vector_line_integral(self):
        self.add_subcaption(
            "The vector line integral computes work done by a force "
            "field along a path. We take the dot product of the force "
            "with the tangent vector at each point.",
            duration=18,
        )
        self.ly.section_divider(2, "Vector Line Integral")

        title = self.ly.title("Work Done by a Force Field")

        # Physical motivation
        motivation = Text(
            "Force field F pushes a particle along curve C.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(motivation, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(motivation, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(motivation), run_time=FAST)

        formula = MathTex(
            r"W",
            r"=",
            r"\int_C \mathbf{F} \cdot d\mathbf{r}",
            r"=",
            r"\int_a^b \mathbf{F}(r(t)) \cdot r'(t)\,dt",
            font_size=HEADING_SIZE, color=WHITE,
        )
        formula[0].set_color(ACCENT)
        formula[2].set_color(PRIMARY)
        formula[4].set_color(SECONDARY)
        self.ly.safe_place(formula, DOWN, anchor=title, buff=0.5)
        ensure_fits(formula)
        self.play(Write(formula), run_time=SLOW)
        self.wait(1.5)

        # Sign note
        self.play(FadeOut(formula), run_time=FAST)

        note = Text(
            "Positive work: force has component along motion",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.center_in_content(note)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 4: Conservative Fields ────────────────────────────
    def scene4_conservative_fields(self):
        self.add_subcaption(
            "Some vector fields are conservative, meaning they're the "
            "gradient of some scalar potential function. For these fields, "
            "the line integral depends only on the endpoints, not the path.",
            duration=18,
        )
        self.ly.section_divider(3, "Conservative Fields")

        title = self.ly.title("The Fundamental Theorem")

        # Definition
        definition = Text(
            "F is conservative if F = \u2207f for some scalar f",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(definition, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(definition, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # The theorem
        theorem_label = Text(
            "Fundamental Theorem for Line Integrals:",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(theorem_label, DOWN, anchor=definition, buff=0.4)
        self.play(FadeIn(theorem_label, shift=LEFT * 0.15), run_time=NORMAL)

        theorem = MathTex(
            r"\int_C \nabla f \cdot d\mathbf{r}",
            r"=",
            r"f(B)",
            r"-",
            r"f(A)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        theorem[2].set_color(ACCENT)
        theorem[4].set_color(RED)
        self.ly.safe_place(theorem, DOWN, anchor=theorem_label, buff=0.3)
        self.play(Write(theorem), run_time=SLOW)
        self.wait(1.5)

        # Implication
        self.play(
            FadeOut(definition), FadeOut(theorem_label), FadeOut(theorem),
            run_time=FAST,
        )

        implication = Text(
            "The integral only depends on endpoints A and B!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(implication)
        self.play(FadeIn(implication, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 5: Path Independence ───────────────────────────────
    def scene5_path_independence(self):
        self.add_subcaption(
            "When a field is conservative, the line integral has the same "
            "value along any path between two points. This is called "
            "path independence. There are several equivalent conditions.",
            duration=20,
        )
        self.ly.section_divider(4, "Path Independence")

        title = self.ly.title("Equivalent Conditions")

        items = [
            Text(
                "Path independent: integral depends only on endpoints",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Conservative: F = \u2207f for some potential function f",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Curl-free: \u2207 \u00d7 F = 0 (in simply connected domains)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Exact: F dx + G dy = df for some f",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        # Direction arrows between equivalent conditions
        equiv = Text(
            "All four conditions are equivalent!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(equiv, DOWN, anchor=title, buff=3.0)
        self.play(FadeIn(equiv, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

    # ── Scene 6: Worked Example ─────────────────────────────────
    def scene6_worked_example(self):
        self.add_subcaption(
            "Let's find the line integral of the vector field (2xy, "
            "x squared plus y squared) from the origin to (1,1). We "
            "first check if the field is conservative by verifying its "
            "curl is zero, then find the potential function.",
            duration=24,
        )
        self.ly.section_divider(5, "Worked Example")

        title = self.ly.title("Evaluating a Line Integral")

        # Problem
        problem = Text(
            "F(x,y) = (2xy, x\u00b2+y\u00b2), from (0,0) to (1,1)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(problem, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(problem, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Step 1: Check curl
        step1 = MathTex(
            r"\frac{\partial}{\partial y}(2xy) = 2x, \quad "
            r"\frac{\partial}{\partial x}(x^2+y^2) = 2x",
            font_size=BODY_SIZE, color=WHITE,
        )
        step1.set_color(PRIMARY)
        self.ly.safe_place(step1, DOWN, anchor=problem, buff=0.3)
        ensure_fits(step1)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(1)

        curl_note = Text(
            "Curl = 0, so F is conservative!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(curl_note, DOWN, anchor=step1, buff=0.3)
        self.play(FadeIn(curl_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        # Step 2: Find potential
        self.play(FadeOut(step1), FadeOut(curl_note), run_time=FAST)

        potential = MathTex(
            r"f(x,y) = x^2 y + \tfrac{y^3}{3}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(potential, DOWN, anchor=problem, buff=0.3)
        self.play(Write(potential), run_time=NORMAL)
        self.wait(1)

        # Step 3: Apply FT
        self.play(FadeOut(potential), run_time=FAST)

        result = MathTex(
            r"\int_C \mathbf{F} \cdot d\mathbf{r}",
            r"= f(1,1) - f(0,0)",
            r"= \tfrac{4}{3}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        result[2].set_color(ACCENT)
        self.ly.safe_place(result, DOWN, anchor=problem, buff=0.3)
        self.play(Write(result), run_time=SLOW)
        self.wait(2.5)
        self.ly.clear()

    # ── Scene 7: Summary ───────────────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "Line integrals let us integrate along curves. Scalar line "
            "integrals compute quantities like mass and arc length. "
            "Vector line integrals compute work. For conservative "
            "fields, the integral depends only on the endpoints, and "
            "we can use a potential function to evaluate it instantly.",
            duration=24,
        )
        self.ly.section_divider(6, "Summary")

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "Scalar line integral: mass, arc length of a curve",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Vector line integral: work done by a force field",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Conservative F = \u2207f: path-independent integrals",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "FT for Line Integrals: \u222b \u2207f \u00b7 dr = f(B) - f(A)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)
        self.ly.clear()

        play_outro(
            self,
            "Green's Theorem",
            "Calculus III -- Multivariable",
        )
