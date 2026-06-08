"""Test render — validates template v2 pipeline (layout, branding, narration)."""

from manim import *
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class TestPipeline(Scene):
    def construct(self):
        self.camera.background_color = BG
        ly = LayoutEngine(self)
        # FIX: Now calls setup_background for dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        # ── Intro ──────────────────────────────────────────────
        self.add_subcaption(
            "Welcome to the test render. This validates our new pipeline.",
            duration=4,
        )
        play_intro(self, "Pipeline Test", "Quality v2")

        # ── Scene 1: Title + progressive reveal ────────────────
        self.add_subcaption(
            "We test progressive reveal with a content budget of five items.",
            duration=5,
        )
        title = ly.title("Progressive Reveal")

        items = [
            Text("First concept appears", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Second follows", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Third is here", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Fourth item", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Fifth fills the budget", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("This triggers removal of the first item", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        ly.progressive_reveal(items, start_from=title)
        self.wait(0.5)
        ly.clear()

        # ── Scene 2: Formula box ───────────────────────────────
        self.add_subcaption(
            "Formula boxes highlight key results with a clean border.",
            duration=4,
        )
        title2 = ly.title("Key Result")
        formula = MathTex(r"E = mc^2", font_size=44, color=WHITE)
        box = ly.formula_box(formula, color=ACCENT)
        ly.safe_place(box, direction=DOWN, anchor=title2, buff=0.6)
        self.play(Write(box), run_time=NORMAL)
        self.wait(1.0)
        ly.clear()

        # ── Scene 3: Two columns ──────────────────────────────
        self.add_subcaption(
            "Two column layouts keep comparisons clean and balanced.",
            duration=5,
        )
        title3 = ly.title("Comparison")
        left_items = [
            Text("Pro: Clean code", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Pro: Easy to read", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        right_items = [
            Text("Con: Slower render", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Con: More complex", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        left, right = ly.two_columns(left_items, right_items, start_from=title3)
        self.play(FadeIn(left), FadeIn(right), run_time=NORMAL)
        self.wait(1.0)
        ly.clear()

        # ── Scene 4: Stack with overflow ──────────────────────
        self.add_subcaption(
            "Vertical stacking detects overflow and handles it gracefully.",
            duration=4,
        )
        title4 = ly.title("Stack Test")
        stack_items = [
            Text(f"Item {i}", font_size=BODY_SIZE, color=WHITE, font=SANS)
            for i in range(1, 10)
        ]
        fitted, overflow = ly.stack_down(stack_items, start_from=title4, spacing=0.3)
        self.play(FadeIn(fitted), run_time=NORMAL)
        if overflow:
            self.add_subcaption(
                f"Notice: {len(overflow)} items were deferred to avoid overflow.",
                duration=4,
            )
        self.wait(1.0)
        ly.clear()

        # ── Outro ─────────────────────────────────────────────
        play_outro(self, "What is a Vector?", "Linear Algebra")
