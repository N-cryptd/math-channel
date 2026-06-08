"""
Video 04: The Chain Rule
Calculus I — derivatives of composite functions.

v2 rewrite: LayoutEngine v2, progressive_reveal, content budgets, Source Sans 3,
dot grid background, section dividers, formula_box, proper narration timing.

Render draft:  manim -ql scripts/pre-university/video-04-chain-rule.py Video04_ChainRule
Render final:  manim -qh scripts/pre-university/video-04-chain-rule.py Video04_ChainRule

QUALITY RULES (enforced):
  1. Max 5 visible elements per scene at any time
  2. Use LayoutEngine for ALL text/formula positioning — no raw .shift() or .to_edge() for content
  3. Progressive disclosure: add items one at a time
  4. Consistent animation vocabulary (Write for titles, FadeIn for body)
  5. Narration: ~12 words per 5 seconds
  6. ly.clear() between scenes
  7. setup_background() for dot grid in construct()
  8. SANS for body/titles, MONO only for code/labels
"""

from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video04_ChainRule(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_pipeline_metaphor()
        self.scene3_chain_rule_statement()
        self.scene4_example_sin_x2()
        self.scene5_example_e3x()
        self.scene6_example_polynomial()
        self.scene7_combined_rules()
        self.scene8_implicit_preview()
        self.scene9_recap()

    # ── Scene 1: Hook — "It's NOT cos(x²)" ──────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "What is the derivative of sin x squared? "
            "It is not cos x squared. We need a new tool: the chain rule.",
            duration=10,
        )
        play_intro(self, "The Chain Rule", "Calculus I")

        # Central question
        question = MathTex(
            r"\text{What is } \frac{d}{dx}\big[\sin(x^2)\big] ?",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(question)
        self.play(Write(question), run_time=NORMAL)
        self.wait(0.5)

        # Common wrong guess
        wrong = MathTex(
            r"\text{Maybe } \cos(x^2)?",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(wrong, direction=DOWN, anchor=question)
        self.play(Write(wrong), run_time=FAST)
        self.wait(0.5)

        # Cross it out
        wrong_cross = Cross(stroke_color=RED, stroke_width=6).replace(wrong)
        self.play(Create(wrong_cross), run_time=FAST)
        self.wait(0.5)

        # Explanation
        expl = Text(
            "sin(x²) is a composition — one function inside another.",
            font_size=LABEL_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(expl, direction=DOWN, anchor=wrong, buff=0.6)
        self.play(Write(expl), run_time=NORMAL)

        punchline = Text(
            "We need the Chain Rule.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(punchline, direction=DOWN, anchor=expl, buff=0.5)
        self.play(Write(punchline), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 2: Pipeline Metaphor ────────────────────────────────────
    def scene2_pipeline_metaphor(self):
        self.ly.section_divider(1, "The Composition Pipeline")

        self.add_subcaption(
            "Think of the chain rule as a machine with two stages. "
            "The output of the inner function feeds into the outer function. "
            "Each stage has a rate, and the total rate multiplies them.",
            duration=15,
        )

        title = self.ly.title("Composition = Pipeline")

        # Inner function description
        inner_desc = Text(
            "Inner function: g(x) transforms x",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(inner_desc, direction=DOWN, anchor=title)
        self.play(FadeIn(inner_desc, shift=LEFT * 0.15), run_time=NORMAL)

        # Outer function description
        outer_desc = Text(
            "Outer function: f takes that result",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(outer_desc, direction=DOWN, anchor=inner_desc)
        self.play(FadeIn(outer_desc, shift=LEFT * 0.15), run_time=NORMAL)

        # Key insight
        insight = Text(
            "Each stage has a rate of change — multiply them!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=outer_desc)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 3: The Chain Rule Statement (AHA) ──────────────────────
    def scene3_chain_rule_statement(self):
        self.ly.section_divider(2, "The Chain Rule")

        self.add_subcaption(
            "The Chain Rule: the derivative of f of g of x equals "
            "f-prime of g of x times g-prime of x.",
            duration=10,
        )

        # THE formula — centered with formula box
        formula_tex = MathTex(
            r"h'(x) = f'\big(g(x)\big) \cdot g'(x)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        formula_boxed = self.ly.formula_box(formula_tex)
        self.ly.center_in_content(formula_boxed)
        self.play(Write(formula_boxed), run_time=SLOW)
        self.wait(2.0)

        # Annotation below
        annotation = Text(
            "Multiply the rates along the chain!",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(annotation, direction=DOWN, anchor=formula_boxed, buff=0.8)
        self.play(FadeIn(annotation, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 4: Example 1 — sin(x²) ───────────────────────────────
    def scene4_example_sin_x2(self):
        self.ly.section_divider(3, "Example 1: sin(x²)")

        self.add_subcaption(
            "Let us find the derivative of sin x squared. "
            "The inner function is x squared, the outer function is sin of u.",
            duration=10,
        )

        title = self.ly.title("sin(x²)")

        # Problem statement
        problem = MathTex(
            r"\frac{d}{dx}\big[\sin(x^2)\big]",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, direction=DOWN, anchor=title)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        # Step 1: Identify inner/outer
        inner = Text(
            "inner: g(x) = x²",
            font_size=LABEL_SIZE, color=SECONDARY, font=MONO,
        )
        self.ly.safe_place(inner, direction=DOWN, anchor=problem)
        self.play(FadeIn(inner, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        outer = Text(
            "outer: f(u) = sin(u)",
            font_size=LABEL_SIZE, color=PRIMARY, font=MONO,
        )
        self.ly.safe_place(outer, direction=DOWN, anchor=inner)
        self.play(FadeIn(outer, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Apply chain rule
        self.add_subcaption(
            "Applying the chain rule: cos of x squared times 2x.",
            duration=5,
        )
        result = MathTex(
            r"= \cos(x^2) \cdot 2x",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=outer, buff=0.5)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 5: Example 2 — e^(3x) ─────────────────────────────────
    def scene5_example_e3x(self):
        self.ly.section_divider(4, "Example 2: e^(3x)")

        self.add_subcaption(
            "Now the derivative of e to the 3x. "
            "The inner function is 3x, and the outer function is e to the u.",
            duration=10,
        )

        title = self.ly.title("e^(3x)")

        # Problem
        problem = MathTex(
            r"\frac{d}{dx}\big[e^{3x}\big]",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, direction=DOWN, anchor=title)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        # Identify inner/outer
        id_text = Text(
            "inner: 3x,  outer: e^u",
            font_size=LABEL_SIZE, color=SECONDARY, font=MONO,
        )
        self.ly.safe_place(id_text, direction=DOWN, anchor=problem)
        self.play(FadeIn(id_text, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Apply chain rule step by step
        self.add_subcaption(
            "Derivative of e to u is e to u. Multiply by derivative of 3x which is 3.",
            duration=7,
        )
        step1 = MathTex(
            r"= e^{3x} \cdot 3",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=id_text)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)

        # Simplified
        step2 = MathTex(
            r"= 3e^{3x}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 6: Example 3 — (2x+1)^5 ───────────────────────────────
    def scene6_example_polynomial(self):
        self.ly.section_divider(5, "Example 3: (2x+1)^5")

        self.add_subcaption(
            "Finally, the derivative of 2x plus 1 to the fifth power. "
            "Inner: 2x plus 1. Outer: u to the fifth.",
            duration=10,
        )

        title = self.ly.title("(2x+1)^5")

        # Problem
        problem = MathTex(
            r"\frac{d}{dx}\big[(2x+1)^5\big]",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, direction=DOWN, anchor=title)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        # Identify
        id_text = Text(
            "inner: 2x+1,  outer: u^5",
            font_size=LABEL_SIZE, color=SECONDARY, font=MONO,
        )
        self.ly.safe_place(id_text, direction=DOWN, anchor=problem)
        self.play(FadeIn(id_text, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Apply chain rule
        self.add_subcaption(
            "Bring down 5, keep the base, then multiply by derivative of 2x plus 1 which is 2.",
            duration=8,
        )
        step1 = MathTex(
            r"= 5(2x+1)^4 \cdot 2",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=id_text)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)

        # Simplified
        step2 = MathTex(
            r"= 10(2x+1)^4",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 7: Combined — Product Rule + Chain Rule ────────────────
    def scene7_combined_rules(self):
        self.ly.section_divider(6, "Combining Rules")

        self.add_subcaption(
            "Now combine the chain rule with the product rule: "
            "the derivative of x times sin x squared.",
            duration=10,
        )

        title = self.ly.title("Product Rule + Chain Rule")

        # Problem statement
        problem = MathTex(
            r"\frac{d}{dx}\big[x \cdot \sin(x^2)\big]",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(problem, direction=DOWN, anchor=title)
        self.play(Write(problem), run_time=NORMAL)
        self.wait(0.5)

        # Step 1: Apply product rule
        self.add_subcaption(
            "Using the product rule: first times derivative of second, "
            "plus second times derivative of first.",
            duration=7,
        )
        ident = Text(
            "f(x) = x,  g(x) = sin(x²)",
            font_size=LABEL_SIZE, color=SECONDARY, font=MONO,
        )
        self.ly.safe_place(ident, direction=DOWN, anchor=problem)
        self.play(FadeIn(ident, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        step1 = MathTex(
            r"= (1)\sin(x^2) + x \cdot \frac{d}{dx}\big[\sin(x^2)\big]",
            font_size=LABEL_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=ident)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)

        # Step 2: Chain rule on second term
        self.add_subcaption(
            "Now apply the chain rule to the second term: cos of x squared times 2x.",
            duration=7,
        )
        step2 = MathTex(
            r"= \sin(x^2) + x \cdot \cos(x^2) \cdot 2x",
            font_size=LABEL_SIZE, color=WHITE,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.5)

        # Step 3: Simplify
        step3 = MathTex(
            r"= \sin(x^2) + 2x^2 \cos(x^2)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(step3, direction=DOWN, anchor=step2)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 8: Implicit Differentiation Preview ──────────────────
    def scene8_implicit_preview(self):
        self.ly.section_divider(7, "Coming Next: Implicit Differentiation")

        self.add_subcaption(
            "The chain rule lets us differentiate equations like "
            "x squared plus y squared equals 25. This is called implicit differentiation.",
            duration=10,
        )

        # Circle equation
        equation = MathTex(
            r"x^2 + y^2 = 25",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(equation)
        self.play(Write(equation), run_time=NORMAL)
        self.wait(0.5)

        # Circle graph — graph elements get manual positioning
        axes = Axes(
            x_range=[-6, 6, 1], y_range=[-6, 6, 1],
            x_length=6, y_length=6,
            axis_config={"color": DIM, "include_numbers": False},
        ).shift(DOWN * 0.8)

        circle_graph = Circle(
            radius=2.5, color=PRIMARY, stroke_width=3,
        ).move_to(axes.get_center())

        self.play(Create(axes), run_time=FAST)
        self.play(Create(circle_graph), run_time=NORMAL)
        self.wait(0.5)

        # Annotation
        annotation = Text(
            "We will use the chain rule to find dy/dx...",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(annotation, direction=DOWN, anchor=axes, buff=0.5)
        self.play(FadeIn(annotation, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 9: Recap + Outro ──────────────────────────────────────
    def scene9_recap(self):
        self.add_subcaption(
            "The chain rule lets us differentiate any composition of functions. "
            "Next up: implicit differentiation and related rates.",
            duration=10,
        )

        title = self.ly.title("The Chain Rule — Summary")

        bullets = [
            Text("h'(x) = f'(g(x)) · g'(x)", font_size=BODY_SIZE, color=ACCENT, font=MONO),
            Text("Composition = outer rate × inner rate", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Works with Product Rule, Quotient Rule, etc.", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(bullets, start_from=title)
        self.wait(1.0)

        self.ly.clear()

        # Outro
        self.add_subcaption(
            "Thank you for watching. See you next time.",
            duration=5,
        )
        play_outro(self, "Implicit & Related Rates", "Calculus I")
