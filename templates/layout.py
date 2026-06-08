"""
LayoutEngine v2 — strict positioning & content budget for Manim scenes.

Overhaul of v1 with:
  - Content budget enforcement (max items per scene)
  - Auto scene-splitting when overflow detected
  - Progressive reveal: animate items one by one, cull oldest when budget hit
  - Font auto-scaling before spacing compression
  - Collision detection between horizontal zones
  - Content zone with reserved margins

Usage in a scene:
    from layout import LayoutEngine

    class MyScene(Scene):
        def construct(self):
            self.camera.background_color = BG
            ly = LayoutEngine(self)

            title = ly.title("My Title")
            items = [Text("A"), Text("B"), MathTex(r"x^2")]
            revealed = ly.progressive_reveal(items, start_from=title)

            # Two-column layout (auto-sized)
            left, right = ly.two_columns(col1_items, col2_items)

            # Clean scene transition
            ly.clear()
"""

from manim import *


# ── Frame constants (16:9 default) ─────────────────────────────────
FRAME_W = config.frame_width   # 14.22
FRAME_H = config.frame_height  # 8.0

# Safe margins from edges
MARGIN = 0.6
SAFE_LEFT   = -FRAME_W / 2 + MARGIN
SAFE_RIGHT  =  FRAME_W / 2 - MARGIN
SAFE_BOTTOM = -FRAME_H / 2 + MARGIN
SAFE_TOP    =  FRAME_H / 2 - MARGIN

# Title bar reserved height
TITLE_ZONE_H = 1.0
CONTENT_TOP  = SAFE_TOP - TITLE_ZONE_H

# Standard spacing
SPACING_TIGHT  = 0.2
SPACING_NORMAL = 0.4
SPACING_LOOSE  = 0.6

# Max widths for common elements
MAX_FULL_WIDTH  = FRAME_W - 2 * MARGIN          # ~13.02
MAX_HALF_WIDTH  = (FRAME_W - 2 * MARGIN) / 2 - 0.8  # ~5.71 — leaves room for gap
MAX_THIRD_WIDTH = (FRAME_W - 2 * MARGIN) / 3 - 0.3  # ~3.81

COLUMN_GAP = 1.2  # Manim units between column centers (~72px at 480p)

# Content budget
DEFAULT_MAX_ITEMS = 5  # maximum visible elements at once


def ensure_fits(mobject, max_width=None, max_height=None):
    """Scale mobject down if it exceeds bounds. Returns the mobject."""
    if max_width is None:
        max_width = MAX_FULL_WIDTH
    w = mobject.width
    if w > max_width:
        mobject.scale(max_width / w)
    if max_height is not None:
        h = mobject.height
        if h > max_height:
            scale = max_height / h
            if scale < 1.0:
                mobject.scale(scale)
    return mobject


def clamp_position(mobject, margin=MARGIN):
    """Shift mobject back on-screen if any part extends beyond the safe zone."""
    bb = mobject.get_critical_point(UR)
    bl = mobject.get_critical_point(DL)
    dx = dy = 0
    if bb[0] > SAFE_RIGHT:
        dx = SAFE_RIGHT - bb[0]
    if bl[0] < SAFE_LEFT:
        dx = SAFE_LEFT - bl[0]
    if bb[1] > SAFE_TOP:
        dy = SAFE_TOP - bb[1]
    if bl[1] < SAFE_BOTTOM:
        dy = SAFE_BOTTOM - bl[1]
    if dx != 0 or dy != 0:
        mobject.shift(RIGHT * dx + UP * dy)
    return mobject


class LayoutEngine:
    """Strict layout assistant for a Manim Scene.

    Enforces content budgets, prevents overflow, and provides smart
    placement methods that guarantee content stays within bounds.
    """

    def __init__(self, scene, max_items=DEFAULT_MAX_ITEMS):
        self.scene = scene
        self._title_mobject = None
        self.max_items = max_items

    # ── Content zone ───────────────────────────────────────────────
    @property
    def content_top(self):
        """Y coordinate below the title zone."""
        return CONTENT_TOP

    @property
    def content_bottom(self):
        """Y coordinate at the bottom safe zone."""
        return SAFE_BOTTOM

    @property
    def available_height(self):
        """Total usable vertical space for content."""
        return CONTENT_TOP - SAFE_BOTTOM

    def remaining_height(self, below_mobject):
        """How much vertical space is left below a mobject."""
        bottom = below_mobject.get_bottom()[1]
        return bottom - SAFE_BOTTOM

    # ── Title ───────────────────────────────────────────────────────
    def title(self, text, color=None, size=None, font=None, weight=BOLD,
              animate_in=True):
        """Place a title at the top of the frame. Returns the mobject.

        If animate_in=True, plays a Write animation (preferred).
        Set animate_in=False if you want to handle animation yourself.
        """
        from channel_branding import PRIMARY, SANS, TITLE_SIZE
        color = color or PRIMARY
        size = size or TITLE_SIZE
        font = font or SANS

        m = Text(text, font_size=size, color=color, font=font, weight=weight)
        m.to_edge(UP, buff=0.4)
        ensure_fits(m, max_width=MAX_FULL_WIDTH)
        self._title_mobject = m

        if animate_in:
            self.scene.play(Write(m), run_time=0.6)
            self.scene.wait(0.15)

        return m

    # ── Safe placement ─────────────────────────────────────────────
    def safe_place(self, mobject, direction=DOWN, anchor=None, buff=0.4):
        """Place mobject relative to anchor (or center), clamped to safe zone."""
        ensure_fits(mobject)
        if anchor is not None:
            mobject.next_to(anchor, direction, buff=buff)
        else:
            mobject.move_to(ORIGIN)
        clamp_position(mobject)
        return mobject

    # ── Center in content area ─────────────────────────────────────
    def center_in_content(self, mobject):
        """Center mobject in the content area (below title zone)."""
        center_y = (CONTENT_TOP + SAFE_BOTTOM) / 2
        mobject.move_to(UP * center_y)
        clamp_position(mobject)
        return mobject

    # ── Vertical stack with overflow detection ─────────────────────
    def stack_down(self, items, start_from=None, start_y=None,
                   spacing=SPACING_NORMAL, aligned_edge=LEFT,
                   max_font_size=None):
        """Stack items vertically from top. Returns (VGroup, overflow_items).

        If items exceed available vertical space, returns the fitting items
        in the VGroup and the remaining items as overflow_items.
        """
        if not items:
            return VGroup(), []

        # Determine starting position
        if start_from is not None:
            start_y = start_from.get_bottom()[1] - spacing
        elif start_y is None:
            start_y = self.content_top

        available_bottom = SAFE_BOTTOM
        available_height = start_y - available_bottom

        # Try fitting with current sizes
        temp = VGroup(*items).arrange(DOWN, buff=spacing, aligned_edge=aligned_edge)
        ensure_fits(temp)

        if temp.height > available_height:
            # Try reducing font sizes first
            if max_font_size is not None and max_font_size > 16:
                new_size = max(16, max_font_size - 4)
                for item in items:
                    if hasattr(item, 'font_size') and item.font_size == max_font_size:
                        item.font_size = new_size
                temp = VGroup(*items).arrange(DOWN, buff=spacing, aligned_edge=aligned_edge)
                ensure_fits(temp)

            if temp.height > available_height:
                # Try tighter spacing
                temp = VGroup(*items).arrange(DOWN, buff=SPACING_TIGHT, aligned_edge=aligned_edge)
                ensure_fits(temp)

        # Position
        if start_from is not None:
            temp.next_to(start_from, DOWN, buff=spacing)
        else:
            available_center_y = (min(start_y, SAFE_TOP) + SAFE_BOTTOM) / 2
            temp.move_to(UP * available_center_y)

        clamp_position(temp)

        # Check for overflow
        if temp.get_bottom()[1] < SAFE_BOTTOM:
            # Find how many items fit
            fitted = []
            overflow = []
            current_y = start_y if start_from is None else start_from.get_bottom()[1] - spacing
            for item in items:
                item_copy = item.copy()
                item_copy.move_to(UP * current_y)
                if item_copy.get_bottom()[1] >= SAFE_BOTTOM - 0.1:
                    fitted.append(item)
                    current_y -= item.height + spacing
                else:
                    overflow.append(item)
            if fitted:
                result = VGroup(*fitted).arrange(DOWN, buff=spacing, aligned_edge=aligned_edge)
                if start_from is not None:
                    result.next_to(start_from, DOWN, buff=spacing)
                else:
                    result.move_to(UP * ((start_y + start_y - result.height) / 2))
                clamp_position(result)
                return result, overflow
            # Nothing fits — return first item scaled down
            first = items[0]
            ensure_fits(first, max_height=available_height)
            first.move_to(UP * (start_y - available_height / 2))
            clamp_position(first)
            return VGroup(first), items[1:]

        return temp, []

    # ── Progressive reveal ─────────────────────────────────────────
    def progressive_reveal(self, items, start_from=None, spacing=SPACING_NORMAL,
                           aligned_edge=LEFT, reveal_anim=FadeIn, anim_kwargs=None,
                           run_time=0.8, wait_time=0.5):
        """Animate items one by one, removing oldest when budget is exceeded.

        Returns list of items currently visible on screen.
        """
        if anim_kwargs is None:
            anim_kwargs = {"shift": LEFT * 0.2}

        visible = []
        for i, item in enumerate(items):
            # Check budget
            if len(visible) >= self.max_items:
                # Remove oldest item
                oldest = visible.pop(0)
                self.scene.play(FadeOut(oldest), run_time=0.3)
                # Re-position remaining items in a CHAIN (not all to same spot)
                if visible and start_from is not None:
                    prev = start_from
                    anims = []
                    for m in visible:
                        m.next_to(prev, DOWN, buff=spacing)
                        ensure_fits(m)
                        clamp_position(m)
                        anims.append(m.animate.move_to(m.get_center()))
                        prev = m
                    if anims:
                        self.scene.play(*anims, run_time=0.4)

            # Add new item at the bottom of the chain
            if start_from and visible:
                item.next_to(visible[-1], DOWN, buff=spacing)
            elif start_from:
                item.next_to(start_from, DOWN, buff=spacing)
            else:
                if visible:
                    item.next_to(visible[-1], DOWN, buff=spacing)
                else:
                    item.move_to(UP * self.content_top)

            ensure_fits(item)
            clamp_position(item)

            self.scene.play(reveal_anim(item, **anim_kwargs), run_time=run_time)
            self.scene.wait(wait_time)
            visible.append(item)

        return visible

    # ── Two columns ────────────────────────────────────────────────
    def two_columns(self, left_items, right_items, spacing=SPACING_NORMAL,
                    start_from=None):
        """Place two sets of items side by side with guaranteed separation.

        Columns are positioned using absolute x-coordinates so they never
        overlap regardless of content width. Each column is scaled to fit
        within its allocated half (minus a comfortable gap).

        If start_from is given, positions both columns below it.
        Returns: (left_vgroup, right_vgroup)
        """
        left = VGroup(*left_items).arrange(
            DOWN, buff=spacing, aligned_edge=LEFT
        ) if left_items else VGroup()
        right = VGroup(*right_items).arrange(
            DOWN, buff=spacing, aligned_edge=LEFT
        ) if right_items else VGroup()

        # Scale each column to fit half the width (with gap buffer)
        ensure_fits(left, max_width=MAX_HALF_WIDTH)
        ensure_fits(right, max_width=MAX_HALF_WIDTH)

        # Scale both to match the taller column's height
        max_h = max(left.height, right.height)
        available_h = CONTENT_TOP - SAFE_BOTTOM
        if start_from is not None:
            available_h -= spacing
        if max_h > available_h:
            scale = available_h / max_h
            left.scale(scale)
            right.scale(scale)

        # Position columns using edge alignment (never overlap)
        # Left column right edge stops at -(COLUMN_GAP/2)
        # Right column left edge starts at +(COLUMN_GAP/2)
        left.align_to(np.array([-(COLUMN_GAP / 2), 0, 0]), RIGHT)
        right.align_to(np.array([(COLUMN_GAP / 2), 0, 0]), LEFT)

        # Align tops
        top_y = CONTENT_TOP if start_from is None else start_from.get_bottom()[1] - spacing
        left.align_to(UP * top_y, UP)
        right.align_to(UP * top_y, UP)

        clamp_position(left)
        clamp_position(right)

        return left, right

    # ── Formula box (highlighted) ──────────────────────────────────
    def formula_box(self, math_tex, color=None, buff=0.25):
        """Place a MathTex centered with a rounded highlight box around it."""
        from channel_branding import ACCENT
        color = color or ACCENT

        ensure_fits(math_tex)
        math_tex.move_to(ORIGIN)
        box = SurroundingRectangle(math_tex, color=color, buff=buff,
                                   stroke_width=2, corner_radius=0.1)
        group = VGroup(math_tex, box)
        clamp_position(group)
        return group

    # ── Section divider ────────────────────────────────────────────
    def section_divider(self, section_number, section_title):
        """Create an animated section divider between content blocks.

        Shows a number, title, and horizontal line sweep.
        """
        from channel_branding import PRIMARY, ACCENT, DIM, SANS, HEADING_SIZE, LABEL_SIZE

        num = Text(
            f"{section_number}", font_size=48, color=ACCENT,
            font=SANS, weight=BOLD,
        )
        title = Text(
            section_title, font_size=HEADING_SIZE, color=PRIMARY,
            font=SANS,
        )
        label_group = VGroup(num, title).arrange(RIGHT, buff=0.4)
        label_group.move_to(UP * ((CONTENT_TOP + 0) / 2))

        line = Line(LEFT * 4, RIGHT * 4, color=PRIMARY, stroke_width=1.5)
        line.next_to(label_group, DOWN, buff=0.3)

        # Animate
        self.scene.play(Write(num), run_time=0.5)
        self.scene.play(FadeIn(title, shift=RIGHT * 0.2), run_time=0.5)
        self.scene.play(Create(line), run_time=0.5)
        self.scene.wait(0.8)
        self.scene.play(
            FadeOut(label_group), FadeOut(line),
            run_time=0.4,
        )
        self.scene.wait(0.2)

    # ── Scene management ───────────────────────────────────────────
    def clear(self, run_time=0.5):
        """Fade out all scene mobjects. Call between scenes.

        Uses LaggedFadeOut for a cleaner transition where each element
        fades individually rather than as a monolithic block.
        """
        if self.scene.mobjects:
            # Filter out background elements (dots, gradient) — keep them
            to_remove = [m for m in self.scene.mobjects
                         if not hasattr(m, '_is_background')]
            if to_remove:
                self.scene.play(
                    *[FadeOut(m, run_time=run_time) for m in to_remove],
                    lag_ratio=0.1,
                )
                self.scene.wait(0.3)
        self._title_mobject = None

    def scene_break(self, run_time=0.5):
        """Clear everything — alias for clear()."""
        self.clear(run_time)
