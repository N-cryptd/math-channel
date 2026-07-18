"""
Video 125: Quotient Rings — Animated Abstract Algebra

This script implements the full lesson on quotient rings (R/I) including:
- Motivation from modular arithmetic
- Construction of quotient rings from ideals
- Well-definedness of operations
- Examples: Z/nZ, finite fields
- First Isomorphism Theorem for rings
- Correspondence theorem
- Comparison with quotient groups

Follows V2 quality rules: max 5 elements, LayoutEngine positioning, progressive disclosure.
TEMPLATE v2: Manim Math Video Script — Professional Quality

Copy this file to start a new video. Follow the quality rules below.

Usage:
  1. Copy: cp template.py scripts/<playlist>/video-XX-topic.py
  2. Edit: Fill in the scenes per the plan
  3. Draft:  manim -ql scripts/<playlist>/video-XX-topic.py VideoXX_TopicName
  4. Final:  manim -qh scripts/<playlist>/video-XX-topic.py VideoXX_TopicName

QUALITY RULES (enforced):
  1. Max 5 visible elements per scene at any time
  2. Use LayoutEngine for ALL positioning — no manual .shift() or .to_edge()
  3. Progressive disclosure: add items one at a time
  4. Use consistent animation vocabulary (see channel_branding.py docstring)
  5. Each add_subcaption() duration ≈ words / 2.5 seconds (12 words ≈ 5s)
  6. Call ly.clear() between scenes
  7. No more than 7 lines of text/formula visible simultaneously
  8. Use ly.progressive_reveal() or ly.stack_down() — never raw VGroup.arrange()
     followed by positioning without layout checks
"""

from manim import *
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background, clear_background,
)
from layout import LayoutEngine, ensure_fits


class VideoXX_TopicName(Scene):
    """Replace with your video class name."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        # ALWAYS call setup_background for the dot grid + gradient
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_introduction()
        # self.scene2_core_concept()
        # self.scene3_example()
        # self.scene4_recap()

    def scene1_introduction(self):
        """Hook + motivation. Max 5 elements visible at once."""
        self.add_subcaption(
            "Your narration here. Aim for ~12 words per 5 seconds.",
            duration=5,
        )
        play_intro(self, "Video Title Here", "Playlist Name")

        # Use LayoutEngine for positioning — NEVER use .shift() or .to_edge()
        title = self.ly.title("Section Title")

        # Progressive reveal: items appear one by one
        items = [
            Text("First point", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Second point", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Third point", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)
        self.ly.clear()
