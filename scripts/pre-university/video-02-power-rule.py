"""
Video 02: The Power Rule
Calculus I — computing derivatives without limits.

v2 rewrite: LayoutEngine v2, progressive_reveal, Source Sans 3, dot grid background,
section dividers, content budgets, proper narration timing.

Render draft:  manim -ql scripts/pre-university/video-02-power-rule.py Video02_PowerRule
Render final:  manim -qh scripts/pre-university/video-02-power-rule.py Video02_PowerRule

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


class Video02_PowerRule(Scene):
    """Full video: 7 scenes — power rule, proof, extensions, linearity."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_recap()
        self.scene2_pattern()
        self.scene3_power_rule()
        self.scene4_proof()
        self.scene5_beyond_integers()
        self.scene6_linearity()
        self.scene7_recap()

    # ── Scene 1: Recap + Motivation ────────────────────────────────
    def scene1_recap(self):
        self.add_subcaption(
            "Last time we used the limit definition to find the derivative of x squared."
            " It took six steps. What about x to the fifth?",
            duration=9,
        )
        play_intro(self, "The Power Rule", "Calculus I")

        # Recap last result
        recall_title = self.ly.title("Last time:", color=DIM)

        recall = MathTex(
            r"f(x) = x^2 \implies f'(x) = 2x",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(recall, direction=DOWN, anchor=recall_title, buff=0.5)
        self.play(Write(recall), run_time=NORMAL)
        self.wait(0.5)

        # Flash the limit steps briefly — then fade
        self.add_subcaption(
            "The limit steps were tedious. We need a faster way.",
            duration=6,
        )
        steps = VGroup(
            MathTex(r"= \lim_{h \to 0} \frac{(x+h)^2 - x^2}{h}", font_size=LABEL_SIZE, color=DIM),
            MathTex(r"= \lim_{h \to 0} (2x + h)", font_size=LABEL_SIZE, color=DIM),
            MathTex(r"= 2x", font_size=LABEL_SIZE, color=ACCENT),
        )
        self.ly.stack_down(steps, start_from=recall, spacing=0.25)
        self.play(FadeIn(steps, shift=LEFT * 0.15), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(steps), run_time=0.3)

        # Motivate
        question = Text(
            "But what about x^5?  x^100?",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(question, direction=DOWN, anchor=recall, buff=0.8)
        self.play(Write(question), run_time=NORMAL)
        self.wait(1.0)

        hint = Text(
            "There must be a pattern...",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(hint, direction=DOWN, anchor=question, buff=0.5)
        self.play(FadeIn(hint, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 2: Hunting for the Pattern ───────────────────────────
    def scene2_pattern(self):
        self.add_subcaption(
            "The derivative of x to the n is n times x to the n minus one. Let's verify this.",
            duration=9,
        )

        self.ly.section_divider(1, "Finding the Pattern")

        # Three computation cases — progressive reveal (left column)
        cases = [
            MathTex(r"f(x) = x \;\to\; f'(x) = 1 = 1 \cdot x^0", font_size=LABEL_SIZE, color=PRIMARY),
            MathTex(r"f(x) = x^2 \;\to\; f'(x) = 2x = 2 \cdot x^1", font_size=LABEL_SIZE, color=PRIMARY),
            MathTex(r"f(x) = x^3 \;\to\; f'(x) = 3x^2", font_size=LABEL_SIZE, color=PRIMARY),
        ]

        visible_cases = self.ly.progressive_reveal(
            cases, spacing=0.4,
            anim_kwargs={"shift": LEFT * 0.15},
        )

        # Show x^3 derivation briefly
        self.add_subcaption(
            "For x cubed, the binomial expansion gives us three x squared after the limit.",
            duration=7,
        )
        x3_detail = MathTex(
            r"= \lim_{h \to 0} \frac{3x^2h + 3xh^2 + h^3}{h} = 3x^2",
            font_size=LABEL_SIZE, color=DIM,
        )
        self.ly.safe_place(x3_detail, direction=DOWN, anchor=cases[-1], buff=0.3)
        self.play(FadeIn(x3_detail, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.8)
        self.play(FadeOut(x3_detail), run_time=FAST)

        # Results column on the right
        self.add_subcaption(
            "Look at the pattern: the exponent comes down as a multiplier.",
            duration=6,
        )
        results = [
            MathTex(r"x^1 \;\to\; 1 \cdot x^0", font_size=LABEL_SIZE, color=SECONDARY),
            MathTex(r"x^2 \;\to\; 2 \cdot x^1", font_size=LABEL_SIZE, color=SECONDARY),
            MathTex(r"x^3 \;\to\; 3 \cdot x^2", font_size=LABEL_SIZE, color=SECONDARY),
        ]
        for r in results:
            r.shift(RIGHT * 3.5)
        self.ly.stack_down(results, spacing=0.3)
        for r in results:
            self.play(FadeIn(r, shift=RIGHT * 0.15), run_time=FAST)
            self.wait(0.3)

        # Pattern highlight
        pattern = MathTex(
            r"x^n \;\to\; n \cdot x^{n-1}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        fb = self.ly.formula_box(pattern, color=ACCENT)
        self.ly.safe_place(fb, direction=DOWN, anchor=None)
        self.play(Write(pattern), run_time=SLOW)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 3: The Power Rule Statement (AHA) ───────────────────
    def scene3_power_rule(self):
        self.add_subcaption(
            "The Power Rule: the derivative of x to the n equals n times x to the n minus one.",
            duration=8,
        )

        self.ly.section_divider(2, "The Power Rule")

        # THE formula — big and centered in a formula box
        formula = MathTex(
            r"\frac{d}{dx}\left[x^n\right] = n \cdot x^{n-1}",
            font_size=48, color=ACCENT,
        )
        fb = self.ly.formula_box(formula, color=ACCENT)
        self.ly.center_in_content(fb)
        self.play(Write(formula), run_time=SLOW)
        self.wait(1.0)

        # Explanation
        self.add_subcaption(
            "The power comes down as a multiplier, and the exponent decreases by one.",
            duration=7,
        )
        demo_label = Text(
            "The power comes down, the exponent decreases by 1",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(demo_label, direction=DOWN, anchor=fb, buff=0.8)
        self.play(FadeIn(demo_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Quick examples — progressive reveal (budget: 5 items)
        examples = [
            MathTex(r"x^4 \;\to\; 4x^3", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"x^7 \;\to\; 7x^6", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"x^{10} \;\to\; 10x^9", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"x^{100} \;\to\; 100x^{99}", font_size=BODY_SIZE, color=PRIMARY),
        ]
        self.ly.progressive_reveal(
            examples, start_from=demo_label,
            anim_kwargs={"shift": RIGHT * 0.15},
        )

        self.add_subcaption(
            "No limits needed. Instant differentiation.",
            duration=5,
        )
        punchline = Text(
            "No limits needed. Instant.", font_size=HEADING_SIZE,
            color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(punchline, direction=DOWN, anchor=None)
        self.play(Write(punchline), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 4: Proof via Binomial Theorem ───────────────────────
    def scene4_proof(self):
        self.add_subcaption(
            "Using the binomial theorem: when we expand (x plus h) to the n,"
            " only the first two terms survive the limit.",
            duration=10,
        )

        self.ly.section_divider(3, "Proof (Positive Integers)")

        # Step 1: Limit definition — formula box
        s1 = MathTex(
            r"f'(x) = \lim_{h \to 0} \frac{(x+h)^n - x^n}{h}",
            font_size=BODY_SIZE, color=WHITE,
        )
        fb1 = self.ly.formula_box(s1, color=PRIMARY)
        self.play(Write(s1), run_time=NORMAL)
        self.wait(0.5)

        # Step 2: Binomial expansion
        binom = MathTex(
            r"(x+h)^n = x^n + nx^{n-1}h + \tfrac{n(n-1)}{2}x^{n-2}h^2 + \cdots + h^n",
            font_size=LABEL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(binom, direction=DOWN, anchor=fb1, buff=0.5)
        self.play(Write(binom), run_time=SLOW)
        self.wait(0.8)

        # Step 3: Substitute and cancel x^n
        self.add_subcaption(
            "The x to the n terms cancel. Factor out h and it cancels too.",
            duration=7,
        )
        s3 = MathTex(
            r"\frac{x^n + nx^{n-1}h + \cdots + h^n - x^n}{h}"
            r"= \frac{nx^{n-1}h + \cdots}{h}",
            font_size=LABEL_SIZE, color=WHITE,
        )
        self.ly.safe_place(s3, direction=DOWN, anchor=binom, buff=0.4)
        cancel_note = Text(
            "x^n cancels!", font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        cancel_note.next_to(s3, RIGHT, buff=0.3)
        self.play(Write(s3), run_time=NORMAL)
        self.play(Write(cancel_note), run_time=FAST)
        self.wait(0.5)

        # Step 4: Every remaining term has h → vanishes
        self.add_subcaption(
            "Every remaining term has an h factor, so they all vanish when h goes to zero.",
            duration=7,
        )
        vanish = Text(
            "Every remaining term has an h factor → they all vanish!",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(vanish, direction=DOWN, anchor=s3, buff=0.5)
        self.play(Write(vanish), run_time=NORMAL)
        self.wait(0.5)

        # Final result
        result = MathTex(
            r"f'(x) = nx^{n-1} \;\;\checkmark",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        fb_result = self.ly.formula_box(result, color=ACCENT)
        self.ly.safe_place(fb_result, direction=DOWN, anchor=vanish, buff=0.5)
        self.play(Write(result), run_time=SLOW)
        self.wait(2.0)

        self.ly.clear()

    # ── Scene 5: Beyond Integers ──────────────────────────────────
    def scene5_beyond_integers(self):
        self.add_subcaption(
            "The power rule works for negative and fractional powers too — any real number n.",
            duration=8,
        )

        self.ly.section_divider(4, "Beyond Integers")

        # Negative power example — left side
        neg_title = Text(
            "Negative powers:", font_size=HEADING_SIZE,
            color=SECONDARY, font=SANS,
        )
        neg_steps = [
            MathTex(r"\frac{1}{x} = x^{-1}", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"\frac{d}{dx}[x^{-1}] = -1 \cdot x^{-2}", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"= -\frac{1}{x^2}", font_size=BODY_SIZE, color=ACCENT),
        ]

        self.ly.safe_place(neg_title, direction=UP + LEFT, anchor=None)
        self.play(Write(neg_title), run_time=FAST)
        self.ly.progressive_reveal(
            neg_steps, start_from=neg_title,
            spacing=0.3,
            anim_kwargs={"shift": LEFT * 0.15},
        )

        # Graph for 1/x — right side
        neg_axes = Axes(
            x_range=[-2, 2, 1], y_range=[-3, 3, 1],
            x_length=3.5, y_length=3,
            axis_config={"color": DIM, "include_numbers": False},
        )
        neg_axes.shift(RIGHT * 3.2 + DOWN * 0.3)
        neg_curve = neg_axes.plot(
            lambda x: 1 / x, x_range=[0.4, 2], color=PRIMARY, stroke_width=2,
        )
        neg_curve2 = neg_axes.plot(
            lambda x: 1 / x, x_range=[-2, -0.4], color=PRIMARY, stroke_width=2,
        )
        self.play(Create(neg_axes), run_time=FAST)
        self.play(Create(neg_curve), Create(neg_curve2), run_time=NORMAL)
        self.wait(1.0)

        # Transition: clear graph, show fractional powers
        self.play(
            FadeOut(neg_axes), FadeOut(neg_curve), FadeOut(neg_curve2),
            FadeOut(neg_title),
            run_time=0.5,
        )

        self.add_subcaption(
            "Fractional powers follow the same rule. The derivative of root x is one over two root x.",
            duration=8,
        )

        frac_title = Text(
            "Fractional powers:", font_size=HEADING_SIZE,
            color=SECONDARY, font=SANS,
        )
        frac_steps = [
            MathTex(r"\sqrt{x} = x^{1/2}", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"\frac{d}{dx}[x^{1/2}] = \tfrac{1}{2} \cdot x^{-1/2}", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"= \frac{1}{2\sqrt{x}}", font_size=BODY_SIZE, color=ACCENT),
        ]

        self.ly.safe_place(frac_title, direction=UP + LEFT, anchor=None)
        self.play(Write(frac_title), run_time=FAST)
        self.ly.progressive_reveal(
            frac_steps, start_from=frac_title,
            spacing=0.3,
            anim_kwargs={"shift": LEFT * 0.15},
        )

        # Graph for sqrt(x)
        frac_axes = Axes(
            x_range=[0, 4, 1], y_range=[0, 2.5, 0.5],
            x_length=3.5, y_length=3,
            axis_config={"color": DIM, "include_numbers": False},
        )
        frac_axes.shift(RIGHT * 3.2 + DOWN * 0.3)
        frac_curve = frac_axes.plot(
            lambda x: np.sqrt(x), x_range=[0, 4], color=PRIMARY, stroke_width=2,
        )
        self.play(Create(frac_axes), run_time=FAST)
        self.play(Create(frac_curve), run_time=NORMAL)
        self.wait(1.0)

        # General statement
        general = Text(
            "Works for any real power n.", font_size=HEADING_SIZE,
            color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(general, direction=DOWN, anchor=None)
        self.play(Write(general), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 6: Linearity ─────────────────────────────────────────
    def scene6_linearity(self):
        self.add_subcaption(
            "The derivative is linear: you can differentiate term by term.",
            duration=6,
        )

        self.ly.section_divider(5, "Combining with Linearity")

        # Linearity rules — formula boxes
        rules = VGroup(
            MathTex(r"\frac{d}{dx}[c \cdot f(x)] = c \cdot f'(x)", font_size=LABEL_SIZE, color=PRIMARY),
            MathTex(r"\frac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x)", font_size=LABEL_SIZE, color=PRIMARY),
        )
        self.ly.stack_down(rules, spacing=0.4)
        rules.shift(LEFT * 3.0 + UP * 0.5)

        self.play(Write(rules[0]), run_time=NORMAL)
        self.play(Write(rules[1]), run_time=NORMAL)
        self.wait(1.0)

        # Example polynomial — right side
        self.add_subcaption(
            "Polynomials become easy: apply the power rule term by term.",
            duration=6,
        )
        ex_label = Text(
            "Example:", font_size=HEADING_SIZE,
            color=WHITE, font=SANS, weight=BOLD,
        )
        original = MathTex(
            r"f(x) = 3x^4 - 5x^2 + 7x - 2",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        step1 = MathTex(
            r"= 3 \cdot 4x^3 - 5 \cdot 2x + 7 \cdot 1 - 0",
            font_size=LABEL_SIZE, color=WHITE,
        )
        step2 = MathTex(
            r"= 12x^3 - 10x + 7",
            font_size=BODY_SIZE, color=ACCENT,
        )

        ex_group = VGroup(ex_label, original, step1, step2)
        self.ly.stack_down(ex_group, spacing=0.35)
        ex_group.shift(RIGHT * 2.5)

        self.play(Write(ex_label), run_time=FAST)
        self.play(Write(original), run_time=NORMAL)
        self.wait(0.5)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.5)

        note = Text(
            "Term by term. Mechanical.", font_size=LABEL_SIZE,
            color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=step2, buff=0.5)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ── Scene 7: Recap + Preview ───────────────────────────────────
    def scene7_recap(self):
        self.add_subcaption(
            "The power rule is your first shortcut."
            " But not everything is a simple power — next: product and quotient rules.",
            duration=9,
        )

        title = self.ly.title("What We Learned")

        bullets = [
            Text(
                "The Power Rule: d/dx[x^n] = nx^{n-1}",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Proved for positive integers (binomial theorem)",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Works for all real powers",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Combine with linearity for polynomials",
                font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
            ),
        ]
        self.ly.progressive_reveal(
            bullets, start_from=title,
            anim_kwargs={"shift": LEFT * 0.15},
        )

        self.wait(1.0)
        play_outro(self, "Product & Quotient Rules", "Calculus I")
