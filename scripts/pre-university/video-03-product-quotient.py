"""
Video 03: Product and Quotient Rules
Calculus I — derivatives of products and quotients.

v2 rewrite: LayoutEngine v2, progressive_reveal, Source Sans 3, dot grid background,
section dividers, content budgets, proper narration timing.

Render draft:  manim -ql scripts/pre-university/video-03-product-quotient.py Video03_ProductQuotient
Render final:  manim -qh scripts/pre-university/video-03-product-quotient.py Video03_ProductQuotient

QUALITY RULES (enforced):
  1. Max 5 visible elements per scene at any time
  2. Use LayoutEngine for ALL text/formula positioning
  3. Progressive disclosure: add items one at a time
  4. Consistent animation vocabulary (Write for titles, FadeIn for body)
  5. Narration: ~12 words per 5 seconds
  6. ly.clear() between scenes
  7. setup_background() for dot grid
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


class Video03_ProductQuotient(Scene):
    """Full video: 7 scenes — product rule, visual proof, examples, quotient rule."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_area_model()
        self.scene3_product_rule()
        self.scene4_examples()
        self.scene5_quotient_rule()
        self.scene6_quotient_example()
        self.scene7_recap()

    # ── Scene 1: Hook — Why can't we just multiply derivatives? ─────
    def scene1_hook(self):
        self.add_subcaption(
            "Can we differentiate a product by just multiplying the derivatives?"
            " Let's test with x times x.",
            duration=8,
        )
        play_intro(self, "Product & Quotient Rules", "Calculus I")

        # The question
        question = self.ly.title("What about f(x) · g(x)?")

        # Naive guess — left
        naive_title = Text(
            "Naive guess:", font_size=HEADING_SIZE, color=DIM, font=SANS,
        )
        naive_formula = MathTex(
            r"(f \cdot g)' \stackrel{?}{=} f' \cdot g'",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.stack_down([naive_title, naive_formula], spacing=0.3)
        naive_title.shift(LEFT * 3.0 + UP * 0.3)
        naive_formula.align_to(naive_title, LEFT)
        self.play(FadeIn(naive_title, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(naive_formula), run_time=FAST)
        self.wait(0.5)

        # Counterexample — right
        counter_label = Text(
            "Counterexample:", font_size=HEADING_SIZE,
            color=ACCENT, font=SANS, weight=BOLD,
        )
        counter_label.shift(RIGHT * 2.5 + UP * 0.3)
        self.play(Write(counter_label), run_time=FAST)

        self.add_subcaption(
            "If f and g are both x, then f times g is x squared."
            " The real derivative is 2x, but the naive guess gives 1.",
            duration=8,
        )

        defs = [
            MathTex(r"f(x) = x,\; g(x) = x", font_size=LABEL_SIZE, color=PRIMARY),
            MathTex(r"f \cdot g = x^2", font_size=LABEL_SIZE, color=PRIMARY),
            MathTex(r"(fg)' = 2x", font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.stack_down(defs, start_from=counter_label, spacing=0.25)
        defs[0].align_to(counter_label, LEFT)
        for d in defs:
            self.play(FadeIn(d, shift=LEFT * 0.15), run_time=FAST)
            self.wait(0.3)

        # Show the contradiction
        naive_result = MathTex(
            r"f' \cdot g' = 1 \cdot 1 = 1",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(naive_result, direction=DOWN, anchor=defs[-1], buff=0.4)
        naive_result.align_to(counter_label, LEFT)
        self.play(Write(naive_result), run_time=NORMAL)

        cross = Cross(naive_result, color=RED)
        self.play(Create(cross), run_time=FAST)

        mismatch = Text(
            "1 ≠ 2x → Product rule needed!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(mismatch, direction=DOWN, anchor=None)
        self.play(Write(mismatch), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 2: Visual proof with area model ──────────────────────
    def scene2_area_model(self):
        self.add_subcaption(
            "Think of the product as the area of a rectangle."
            " When both sides grow, the new area reveals the product rule.",
            duration=8,
        )

        self.ly.section_divider(1, "Visual Proof — Area Model")

        # Initial rectangle
        orig_rect = Rectangle(
            width=3, height=2, stroke_width=2, color=PRIMARY,
            fill_color=PRIMARY, fill_opacity=0.15,
        )
        self.ly.center_in_content(orig_rect)
        a_label = MathTex(r"a = f(x)", font_size=LABEL_SIZE, color=PRIMARY)
        a_label.next_to(orig_rect, LEFT, buff=0.2)
        b_label = MathTex(r"b = g(x)", font_size=LABEL_SIZE, color=PRIMARY)
        b_label.next_to(orig_rect, DOWN, buff=0.2)

        self.play(Create(orig_rect), run_time=NORMAL)
        self.play(Write(a_label), Write(b_label), run_time=FAST)
        self.wait(0.5)

        # Expanded rectangle
        self.add_subcaption(
            "When the sides change by small amounts h and k,"
            " we get four regions in the new area.",
            duration=8,
        )
        new_rect = Rectangle(
            width=4.2, height=3.2, stroke_width=2, color=SECONDARY,
            fill_color=SECONDARY, fill_opacity=0.08,
        ).move_to(orig_rect.get_center() + RIGHT * 0.6 + UP * 0.6)

        h_label = MathTex(r"h", font_size=LABEL_SIZE, color=ACCENT)
        h_label.move_to(orig_rect.get_right() + RIGHT * 0.6)
        k_label = MathTex(r"k", font_size=LABEL_SIZE, color=ACCENT)
        k_label.move_to(orig_rect.get_bottom() + DOWN * 0.6)

        self.play(GrowFromEdge(new_rect, UP), Write(h_label), Write(k_label), run_time=NORMAL)
        self.wait(0.5)

        # Break into regions — show one at a time (content budget)
        # Region 2: a*k (top)
        r2 = Rectangle(
            width=3, height=1.2, stroke_width=1.5, color=ACCENT,
            fill_color=ACCENT, fill_opacity=0.2,
        ).next_to(orig_rect, UP, buff=0, aligned_edge=LEFT)
        r2_label = MathTex(r"a \cdot k", font_size=LABEL_SIZE, color=ACCENT)
        r2_label.move_to(r2.get_center())

        # Region 3: h*b (right)
        r3 = Rectangle(
            width=1.2, height=2, stroke_width=1.5, color=SECONDARY,
            fill_color=SECONDARY, fill_opacity=0.2,
        ).next_to(orig_rect, RIGHT, buff=0, aligned_edge=DOWN)
        r3_label = MathTex(r"h \cdot b", font_size=LABEL_SIZE, color=SECONDARY)
        r3_label.move_to(r3.get_center())

        self.play(FadeIn(r2), Write(r2_label), run_time=NORMAL)
        self.play(FadeIn(r3), Write(r3_label), run_time=NORMAL)

        # The expansion formula
        expansion = MathTex(
            r"(a+h)(b+k) = ab + a\!k + h\!b + h\!k",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(expansion, direction=DOWN, anchor=None)
        self.play(Write(expansion), run_time=NORMAL)
        self.wait(0.5)

        # Derivative connection
        self.add_subcaption(
            "The h times k term vanishes in the limit. What remains is the product rule.",
            duration=7,
        )

        # Fade region details, show the key insight
        self.play(
            FadeOut(r2), FadeOut(r2_label), FadeOut(r3), FadeOut(r3_label),
            FadeOut(new_rect), FadeOut(h_label), FadeOut(k_label),
            FadeOut(a_label), FadeOut(b_label), FadeOut(orig_rect),
            FadeOut(expansion),
            run_time=0.5,
        )

        result_formula = MathTex(
            r"\frac{d}{dx}[f\,g] = f'\,g + f\,g'",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        fb = self.ly.formula_box(result_formula, color=ACCENT)
        note = Text(
            "The hk term vanishes in the limit!",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=fb, buff=0.4)
        self.play(Write(result_formula), run_time=SLOW)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 3: The Product Rule Statement ─────────────────────────
    def scene3_product_rule(self):
        self.add_subcaption(
            "The product rule: the derivative of f times g is f-prime g plus f g-prime."
            " It's like taking turns differentiating.",
            duration=9,
        )

        self.ly.section_divider(2, "The Product Rule")

        # THE formula — big and centered
        formula = MathTex(
            r"\frac{d}{dx}\bigl[f(x)\,g(x)\bigr] = f'(x)\,g(x) + f(x)\,g'(x)",
            font_size=42, color=ACCENT,
        )
        fb = self.ly.formula_box(formula, color=ACCENT)
        self.ly.center_in_content(fb)
        self.play(Write(formula), run_time=SLOW)
        self.wait(1.0)

        # Color-coded breakdown — progressive
        breakdown_items = [
            MathTex(r"(f\,g)'", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"= \underbrace{f'\,g}_{\text{deriv first}} + \underbrace{f\,g'}_{\text{deriv second}}",
                    font_size=BODY_SIZE, color=PRIMARY),
        ]
        self.ly.stack_down(breakdown_items, start_from=fb, spacing=0.5)
        for item in breakdown_items:
            self.play(FadeIn(item, shift=LEFT * 0.15), run_time=NORMAL)
            self.wait(0.5)

        # Mnemonic
        mnemonic = Text(
            "\"Derivative of first × second, plus first × derivative of second\"",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(mnemonic, direction=DOWN, anchor=breakdown_items[-1], buff=0.5)
        self.play(FadeIn(mnemonic, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 4: Product rule worked examples ──────────────────────
    def scene4_examples(self):
        self.add_subcaption(
            "Example one: x squared times e to the x. We apply the product rule step by step.",
            duration=8,
        )

        self.ly.section_divider(3, "Worked Examples")

        # ── Example 1: x^2 * e^x ──
        ex1_label = Text(
            "Example 1:", font_size=HEADING_SIZE,
            color=ACCENT, font=SANS, weight=BOLD,
        )
        ex1_fn = MathTex(
            r"y = x^2 e^x", font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.stack_down([ex1_label, ex1_fn], spacing=0.3)
        ex1_label.shift(LEFT * 2.5)

        self.play(FadeIn(ex1_label, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(ex1_fn), run_time=NORMAL)
        self.wait(0.5)

        # Identify f and g
        fg_id = MathTex(
            r"f = x^2,\; g = e^x",
            font_size=LABEL_SIZE, color=SECONDARY,
        )
        fg_deriv = MathTex(
            r"f' = 2x,\; g' = e^x",
            font_size=LABEL_SIZE, color=SECONDARY,
        )
        self.ly.stack_down([fg_id, fg_deriv], start_from=ex1_fn, spacing=0.2)
        fg_id.align_to(ex1_label, LEFT)

        self.play(FadeIn(fg_id, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(fg_deriv, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Apply product rule
        ex1_step = MathTex(
            r"y' = (2x)(e^x) + (x^2)(e^x)", font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex1_step, direction=DOWN, anchor=fg_deriv, buff=0.4)
        ex1_step.align_to(ex1_label, LEFT)
        self.play(Write(ex1_step), run_time=NORMAL)
        self.wait(0.5)

        ex1_result = MathTex(
            r"y' = (2x + x^2)\,e^x", font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(ex1_result, direction=DOWN, anchor=ex1_step, buff=0.3)
        ex1_result.align_to(ex1_label, LEFT)
        self.play(Write(ex1_result), run_time=NORMAL)
        self.wait(1.0)

        # Transition to Example 2
        self.play(
            FadeOut(ex1_label), FadeOut(ex1_fn), FadeOut(fg_id),
            FadeOut(fg_deriv), FadeOut(ex1_step), FadeOut(ex1_result),
            run_time=0.5,
        )

        self.add_subcaption(
            "Example two: x cubed times sine x. Same process, different functions.",
            duration=7,
        )

        # ── Example 2: x^3 * sin(x) ──
        ex2_label = Text(
            "Example 2:", font_size=HEADING_SIZE,
            color=ACCENT, font=SANS, weight=BOLD,
        )
        ex2_fn = MathTex(
            r"y = x^3 \sin x", font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.stack_down([ex2_label, ex2_fn], spacing=0.3)
        ex2_label.shift(LEFT * 2.5)

        self.play(FadeIn(ex2_label, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(ex2_fn), run_time=NORMAL)
        self.wait(0.3)

        ex2_fg = MathTex(
            r"f = x^3,\; g = \sin x", font_size=LABEL_SIZE, color=SECONDARY,
        )
        ex2_fgd = MathTex(
            r"f' = 3x^2,\; g' = \cos x", font_size=LABEL_SIZE, color=SECONDARY,
        )
        self.ly.stack_down([ex2_fg, ex2_fgd], start_from=ex2_fn, spacing=0.2)
        ex2_fg.align_to(ex2_label, LEFT)

        self.play(FadeIn(ex2_fg, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(ex2_fgd, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        ex2_step = MathTex(
            r"y' = (3x^2)(\sin x) + (x^3)(\cos x)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex2_step, direction=DOWN, anchor=ex2_fgd, buff=0.4)
        ex2_step.align_to(ex2_label, LEFT)
        self.play(Write(ex2_step), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 5: The Quotient Rule ─────────────────────────────────
    def scene5_quotient_rule(self):
        self.add_subcaption(
            "The quotient rule: low d-high minus high d-low over low squared."
            " The order matters in the numerator.",
            duration=9,
        )

        self.ly.section_divider(4, "The Quotient Rule")

        # Connection to product rule
        hint = MathTex(
            r"\frac{f}{g} = f \cdot g^{-1}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(hint, direction=UP, anchor=None)
        note = Text(
            "Derived from the product rule", font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        note.next_to(hint, DOWN, buff=0.2)
        self.play(Write(hint), run_time=NORMAL)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # THE quotient rule formula — big and centered
        formula = MathTex(
            r"\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right]"
            r" = \frac{f'(x)\,g(x) - f(x)\,g'(x)}{[g(x)]^2}",
            font_size=38, color=ACCENT,
        )
        fb = self.ly.formula_box(formula, color=ACCENT)
        self.ly.center_in_content(fb)
        self.play(Write(formula), run_time=SLOW)
        self.wait(1.0)

        # Color-coded breakdown
        self.add_subcaption(
            "The numerator is order-sensitive: f-prime g minus f g-prime. The denominator is g squared.",
            duration=8,
        )
        num = MathTex(
            r"\text{Numerator: } f'g - fg' \quad \text{(order matters!)}",
            font_size=LABEL_SIZE, color=ACCENT,
        )
        den = MathTex(
            r"\text{Denominator: } g^2",
            font_size=LABEL_SIZE, color=PRIMARY,
        )
        self.ly.stack_down([num, den], start_from=fb, spacing=0.4)
        self.play(FadeIn(num, shift=LEFT * 0.15), run_time=NORMAL)
        self.play(FadeIn(den, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Mnemonic
        mnemonic = Text(
            "\"Low d-high minus high d-low, over low squared\"",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(mnemonic, direction=DOWN, anchor=den, buff=0.5)
        self.play(Write(mnemonic), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 6: Quotient rule worked example ──────────────────────
    def scene6_quotient_example(self):
        self.add_subcaption(
            "Example: sine x divided by x. Apply the quotient rule.",
            duration=6,
        )

        title = self.ly.title("Quotient Rule Example")

        # Function
        fn = MathTex(
            r"y = \frac{\sin x}{x}", font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(fn, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(fn), run_time=NORMAL)
        self.wait(0.5)

        # Identify f and g
        ids = [
            MathTex(r"\text{high} = f = \sin x", font_size=LABEL_SIZE, color=ACCENT),
            MathTex(r"\text{low}  = g = x", font_size=LABEL_SIZE, color=PRIMARY),
        ]
        self.ly.stack_down(ids, start_from=fn, spacing=0.2)
        ids[0].shift(RIGHT * 3.0)
        ids[1].align_to(ids[0], LEFT)
        for item in ids:
            self.play(FadeIn(item, shift=LEFT * 0.15), run_time=FAST)
            self.wait(0.2)

        # Derivatives
        derivs = [
            MathTex(r"f' = \cos x", font_size=LABEL_SIZE, color=ACCENT),
            MathTex(r"g' = 1", font_size=LABEL_SIZE, color=PRIMARY),
        ]
        self.ly.stack_down(derivs, start_from=ids[-1], spacing=0.2)
        derivs[0].align_to(ids[0], LEFT)
        derivs[1].align_to(ids[0], LEFT)
        for item in derivs:
            self.play(FadeIn(item, shift=LEFT * 0.15), run_time=FAST)
            self.wait(0.2)

        # Apply quotient rule
        self.add_subcaption(
            "Low d-high minus high d-low over low squared.",
            duration=5,
        )
        step1 = MathTex(
            r"y' = \frac{(\cos x)(x) - (\sin x)(1)}{x^2}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=derivs[-1], buff=0.5)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)

        step2 = MathTex(
            r"y' = \frac{x\cos x - \sin x}{x^2}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        fb = self.ly.formula_box(step2, color=ACCENT)
        self.ly.safe_place(fb, direction=DOWN, anchor=step1, buff=0.4)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 7: Recap + Outro ─────────────────────────────────────
    def scene7_recap(self):
        self.add_subcaption(
            "Summary: product and quotient rules let us differentiate combinations of functions."
            " Next up: the chain rule for composing functions.",
            duration=9,
        )

        title = self.ly.title("What We Learned")

        bullets = [
            VGroup(
                Text("Product Rule:", font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD),
                MathTex(r"(fg)' = f'g + fg'", font_size=BODY_SIZE, color=ACCENT),
            ),
            VGroup(
                Text("Quotient Rule:", font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD),
                MathTex(
                    r"\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}",
                    font_size=BODY_SIZE, color=ACCENT,
                ),
            ),
            Text(
                "Key insight: products expand, quotients are order-sensitive",
                font_size=LABEL_SIZE, color=WHITE, font=SANS,
            ),
        ]
        for b in bullets:
            b.arrange(DOWN, buff=0.1, aligned_edge=LEFT)

        self.ly.progressive_reveal(
            bullets, start_from=title,
            spacing=0.5,
            anim_kwargs={"shift": LEFT * 0.15},
        )

        self.wait(1.0)
        play_outro(self, "The Chain Rule", "Calculus I")
