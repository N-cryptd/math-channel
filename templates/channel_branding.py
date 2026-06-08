"""
Channel branding v2 — professional visual language for The Manifold.

Upgrades over v1:
  - Dot grid background pattern (like 3B1B but our palette)
  - Sans-serif body font (Source Sans 3) + Menlo for code/labels
  - Section divider component
  - Consistent animation vocabulary
  - Radial gradient background (center slightly lighter)
  - Refined color palette with more depth
  - Simplified, more polished intro/outro

Usage in video scripts:
  from channel_branding import ChannelIntro, ChannelOutro
  from channel_branding import BG, PRIMARY, SECONDARY, ACCENT, DIM, WHITE, SANS, MONO
  from channel_branding import TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE
  from channel_branding import FAST, NORMAL, SLOW
  from channel_branding import play_intro, play_outro, setup_background
"""

from manim import *

# ── Channel visual language ──────────────────────────────────────────
BG          = "#1A1832"   # Deeper, more professional dark
BG_LIGHT    = "#222045"   # Slightly lighter center for radial gradient
PRIMARY     = "#5BC0EB"   # Brighter, more saturated blue
SECONDARY   = "#7BC950"   # Fresh green
ACCENT      = "#FFD166"   # Warm yellow-gold (less harsh than pure yellow)
RED         = "#EF476F"   # Coral red (more modern)
DIM         = "#6B6B8D"   # Subtle muted purple-gray
WHITE       = "#FFFFFF"
SANS        = "Source Sans 3"  # Professional sans-serif for body text
MONO        = "Menlo"         # Monospace for code, labels, formulas
DISPLAY     = "Source Sans 3" # Display font for titles

CHANNEL_NAME = "The Manifold"

TITLE_SIZE   = 52
HEADING_SIZE = 38
BODY_SIZE    = 32
LABEL_SIZE   = 26
SMALL_SIZE   = 20

FAST   = 0.6
NORMAL = 1.2
SLOW   = 2.0

# ── Animation vocabulary ─────────────────────────────────────────────
# Use these consistently across all videos:
#   Titles       → Write (builds character by character)
#   Body text    → FadeIn(shift=LEFT*0.15) (slides in from left)
#   Formulas     → Transform from previous or Write
#   Highlights   → Indicate (brief glow pulse)
#   Removals     → FadeOut
#   Transitions  → ly.clear() (0.5s fade)
#   Graphs/axes  → Create (draws the line)
#   Points/dots  → FadeIn (simple appear)
#   Results      → Write with ACCENT color


def setup_background(scene):
    """Set up the professional background with subtle dot grid.

    Call once at the start of construct(). Returns (dots, gradient) for
    optional removal during scene transitions.
    """
    scene.camera.background_color = BG

    # Dot grid pattern — optimized with fewer, evenly spaced dots
    dots = VGroup()
    for x in range(-8, 9, 2):      # every 1.6 units
        for y in range(-5, 6, 2):
            dot = Dot(
                np.array([x * 0.8, y * 0.8, 0]),
                radius=0.018,
                color=BG_LIGHT,
                fill_opacity=0.5,
            )
            dots.add(dot)

    # Radial gradient: center slightly brighter (4 layers instead of 8)
    gradient = VGroup()
    for r in [7, 5, 3, 1]:
        circle = Circle(
            radius=r * 0.9,
            fill_color=BG_LIGHT,
            fill_opacity=0.025,
            stroke_width=0,
        )
        gradient.add(circle)

    scene.add(dots, gradient)
    # Move gradient behind dots so dots aren't occluded
    gradient.z_index = -1
    # Mark as background so ly.clear() preserves them
    dots._is_background = True
    gradient._is_background = True
    return dots, gradient


def clear_background(scene, dots=None, gradient=None):
    """Remove background elements before scene transition."""
    if gradient:
        scene.remove(gradient)
    if dots:
        scene.remove(dots)


# ═══════════════════════════════════════════════════════════════════════
# Animated Intro
# ═══════════════════════════════════════════════════════════════════════

class ChannelIntro(Scene):
    """Animated intro — clean, professional, fast.

    Sequence:
      1. Background fades in with dot grid
      2. M logo writes itself
      3. Channel name fades in
      4. Horizontal line sweeps across
      5. Video title fades in
      6. Playlist tag appears
      7. Everything fades out
    """

    def __init__(self, video_title="", playlist_name="Calculus I", **kwargs):
        super().__init__(**kwargs)
        self._video_title = video_title
        self._playlist_name = playlist_name

    def construct(self):
        self.camera.background_color = BG

        # ── Background ─────────────────────────────────────────
        # Subtle floating math symbols (fewer, more elegant)
        import random
        symbols_text = [
            r"\sum", r"\int", r"\infty", r"\partial",
            r"\nabla", r"\pi", r"\lambda",
        ]
        symbols = VGroup(*[
            MathTex(s, font_size=28, color=PRIMARY, fill_opacity=0.15)
            for s in symbols_text
        ])
        random.seed(42)
        for s in symbols:
            s.move_to(np.array([
                random.uniform(-5, 5),
                random.uniform(-2.5, 2.5), 0
            ]))
            s.rotate(random.uniform(-0.2, 0.2))
        self.add(symbols)
        self.play(
            *[FadeIn(s, scale=0.7) for s in symbols],
            run_time=1.0, lag_ratio=0.1,
        )

        # ── Logo ───────────────────────────────────────────────
        logo = MathTex(r"\mathcal{M}", font_size=88, color=PRIMARY)
        self.play(Write(logo), run_time=0.8)
        self.play(
            Flash(logo, color=PRIMARY, num_lines=8, line_length=0.3, flash_radius=0.5),
            run_time=0.5,
        )
        self.wait(0.2)

        # ── Channel name ───────────────────────────────────────
        name = Text(
            CHANNEL_NAME, font_size=36, color=WHITE,
            font=DISPLAY, weight=BOLD,
        ).next_to(logo, DOWN, buff=0.4)
        self.play(FadeIn(name, shift=UP * 0.15), run_time=0.5)
        self.wait(0.15)

        # ── Line sweep ─────────────────────────────────────────
        line = Line(LEFT * 3, RIGHT * 3, color=PRIMARY, stroke_width=1.5)
        line.next_to(name, DOWN, buff=0.3)
        self.play(Create(line), run_time=0.4)
        self.wait(0.1)

        # ── Video title ────────────────────────────────────────
        title = Text(
            self._video_title or "Video Title", font_size=TITLE_SIZE,
            color=ACCENT, font=DISPLAY, weight=BOLD,
        ).next_to(line, DOWN, buff=0.35)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.6)
        self.wait(0.15)

        # ── Playlist tag ───────────────────────────────────────
        playlist = Text(
            self._playlist_name, font_size=LABEL_SIZE,
            color=DIM, font=MONO,
        ).next_to(title, DOWN, buff=0.2)
        self.play(FadeIn(playlist), run_time=0.3)
        self.wait(0.8)

        # ── Fade out ───────────────────────────────────────────
        everything = VGroup(logo, name, line, title, playlist, symbols)
        self.play(FadeOut(everything), run_time=0.5)
        self.wait(0.2)


# ═══════════════════════════════════════════════════════════════════════
# Animated Outro
# ═══════════════════════════════════════════════════════════════════════

class ChannelOutro(Scene):
    """Animated outro — clean closing.

    Sequence:
      1. "Thank you for watching" writes in
      2. Subscribe with pulse
      3. Logo + channel name
      4. Optional next video card
    """

    def __init__(self, next_video="", next_playlist="", **kwargs):
        super().__init__(**kwargs)
        self._next_video = next_video
        self._next_playlist = next_playlist

    def construct(self):
        self.camera.background_color = BG

        # ── Thank you ──────────────────────────────────────────
        thanks = Text(
            "Thank you for watching", font_size=HEADING_SIZE,
            color=WHITE, font=DISPLAY, weight=BOLD,
        )
        self.play(Write(thanks), run_time=NORMAL)
        self.wait(0.3)

        # ── Subscribe CTA ──────────────────────────────────────
        subscribe = Text(
            "Subscribe", font_size=TITLE_SIZE,
            color=PRIMARY, font=DISPLAY, weight=BOLD,
        ).next_to(thanks, DOWN, buff=0.5)

        subscribe.save_state()
        self.play(Write(subscribe), run_time=NORMAL)
        self.play(subscribe.animate.scale(1.08).set_color(ACCENT), run_time=0.25)
        self.play(subscribe.animate.scale(1 / 1.08).set_color(PRIMARY), run_time=0.25)
        self.wait(0.4)

        # ── Logo + name ────────────────────────────────────────
        logo = MathTex(r"\mathcal{M}", font_size=64, color=PRIMARY)
        logo.next_to(subscribe, DOWN, buff=0.4)
        self.play(Write(logo), run_time=0.5)

        channel = Text(
            CHANNEL_NAME, font_size=BODY_SIZE,
            color=DIM, font=DISPLAY,
        ).next_to(logo, DOWN, buff=0.15)
        self.play(FadeIn(channel), run_time=0.3)
        self.wait(0.4)

        # ── Next video card ───────────────────────────────────
        if self._next_video:
            card = self._make_next_card(self._next_video, self._next_playlist)
            card.shift(RIGHT * 8)
            self.play(card.animate.shift(LEFT * 8), run_time=0.6)
            self.wait(0.2)

            up_next = Text(
                "Up next", font_size=LABEL_SIZE,
                color=DIM, font=MONO,
            ).next_to(card, UP, buff=0.25)
            arrow = MathTex(r"\rightarrow", font_size=LABEL_SIZE, color=PRIMARY).next_to(up_next, RIGHT, buff=0.1)
            self.play(FadeIn(up_next), FadeIn(arrow), run_time=0.3)
            self.wait(1.2)

            everything = VGroup(thanks, subscribe, logo, channel, card, up_next, arrow)
        else:
            everything = VGroup(thanks, subscribe, logo, channel)

        self.play(FadeOut(everything), run_time=0.6)
        self.wait(0.3)

    def _make_next_card(self, title, playlist=""):
        """Create a styled 'next video' preview card."""
        card = VGroup()

        bg_rect = RoundedRectangle(
            corner_radius=0.15,
            fill_color="#12102A",
            fill_opacity=0.9,
            stroke_color=PRIMARY,
            stroke_width=1.2,
            width=5.5, height=1.5,
        )
        card.add(bg_rect)

        if playlist:
            pl = Text(
                playlist, font_size=SMALL_SIZE,
                color=DIM, font=MONO,
            ).next_to(bg_rect.get_top(), DOWN, buff=0.2)
            card.add(pl)

        t = Text(
            title, font_size=HEADING_SIZE,
            color=ACCENT, font=DISPLAY, weight=BOLD,
        )
        if playlist:
            t.next_to(pl, DOWN, buff=0.12)
        else:
            t.next_to(bg_rect.get_top(), DOWN, buff=0.25)
        card.add(t)

        card.move_to(DOWN * 1.3)
        return card


# ═══════════════════════════════════════════════════════════════════════
# Standalone render (for testing)
# ═══════════════════════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════════════════════
# Helper functions — call inside any Scene to play animated intro/outro
# ═══════════════════════════════════════════════════════════════════════

def play_intro(scene, video_title="", playlist_name="Calculus I"):
    """Animated intro played within an existing Scene."""
    import random

    # Floating symbols (fewer, more elegant)
    symbols_text = [
        r"\sum", r"\int", r"\infty", r"\partial",
        r"\nabla", r"\pi", r"\lambda",
    ]
    symbols = VGroup(*[
        MathTex(s, font_size=28, color=PRIMARY, fill_opacity=0.15)
        for s in symbols_text
    ])
    random.seed(42)
    for s in symbols:
        s.move_to(np.array([
            random.uniform(-5, 5),
            random.uniform(-2.5, 2.5), 0
        ]))
        s.rotate(random.uniform(-0.2, 0.2))
    scene.add(symbols)
    scene.play(
        *[FadeIn(s, scale=0.7) for s in symbols],
        run_time=1.0, lag_ratio=0.1,
    )

    # Logo
    logo = MathTex(r"\mathcal{M}", font_size=88, color=PRIMARY)
    scene.play(Write(logo), run_time=0.8)
    scene.play(
        Flash(logo, color=PRIMARY, num_lines=8, line_length=0.3, flash_radius=0.5),
        run_time=0.5,
    )
    scene.wait(0.2)

    # Channel name
    name = Text(
        CHANNEL_NAME, font_size=36, color=WHITE,
        font=DISPLAY, weight=BOLD,
    ).next_to(logo, DOWN, buff=0.4)
    scene.play(FadeIn(name, shift=UP * 0.15), run_time=0.5)
    scene.wait(0.15)

    # Line sweep
    line = Line(LEFT * 3, RIGHT * 3, color=PRIMARY, stroke_width=1.5)
    line.next_to(name, DOWN, buff=0.3)
    scene.play(Create(line), run_time=0.4)
    scene.wait(0.1)

    # Video title
    title = Text(
        video_title, font_size=TITLE_SIZE,
        color=ACCENT, font=DISPLAY, weight=BOLD,
    ).next_to(line, DOWN, buff=0.35)
    scene.play(FadeIn(title, shift=UP * 0.1), run_time=0.6)
    scene.wait(0.15)

    # Playlist tag
    playlist = Text(
        playlist_name, font_size=LABEL_SIZE,
        color=DIM, font=MONO,
    ).next_to(title, DOWN, buff=0.2)
    scene.play(FadeIn(playlist), run_time=0.3)
    scene.wait(0.8)

    # Fade out
    everything = VGroup(logo, name, line, title, playlist, symbols)
    scene.play(FadeOut(everything), run_time=0.5)
    scene.wait(0.2)


def play_outro(scene, next_video="", next_playlist=""):
    """Animated outro played within an existing Scene."""
    # Thank you
    thanks = Text(
        "Thank you for watching", font_size=HEADING_SIZE,
        color=WHITE, font=DISPLAY, weight=BOLD,
    )
    scene.play(Write(thanks), run_time=NORMAL)
    scene.wait(0.3)

    # Subscribe
    subscribe = Text(
        "Subscribe", font_size=TITLE_SIZE,
        color=PRIMARY, font=DISPLAY, weight=BOLD,
    ).next_to(thanks, DOWN, buff=0.5)
    subscribe.save_state()
    scene.play(Write(subscribe), run_time=NORMAL)
    scene.play(subscribe.animate.scale(1.08).set_color(ACCENT), run_time=0.25)
    scene.play(subscribe.animate.scale(1 / 1.08).set_color(PRIMARY), run_time=0.25)
    scene.wait(0.4)

    # Logo + name
    logo = MathTex(r"\mathcal{M}", font_size=64, color=PRIMARY)
    logo.next_to(subscribe, DOWN, buff=0.4)
    scene.play(Write(logo), run_time=0.5)

    channel = Text(
        CHANNEL_NAME, font_size=BODY_SIZE,
        color=DIM, font=DISPLAY,
    ).next_to(logo, DOWN, buff=0.15)
    scene.play(FadeIn(channel), run_time=0.3)
    scene.wait(0.4)

    # Next video card
    if next_video:
        card = VGroup()
        bg_rect = RoundedRectangle(
            corner_radius=0.15,
            fill_color="#12102A", fill_opacity=0.9,
            stroke_color=PRIMARY, stroke_width=1.2,
            width=5.5, height=1.5,
        )
        card.add(bg_rect)
        if next_playlist:
            pl = Text(next_playlist, font_size=SMALL_SIZE, color=DIM, font=MONO)
            pl.next_to(bg_rect.get_top(), DOWN, buff=0.2)
            card.add(pl)
        t = Text(next_video, font_size=HEADING_SIZE, color=ACCENT, font=DISPLAY, weight=BOLD)
        t.next_to(pl if next_playlist else bg_rect.get_top(), DOWN, buff=0.12)
        card.add(t)
        card.move_to(DOWN * 1.3)
        card.shift(RIGHT * 8)

        scene.play(card.animate.shift(LEFT * 8), run_time=0.6)
        scene.wait(0.2)

        up_next = Text("Up next", font_size=LABEL_SIZE, color=DIM, font=MONO)
        up_next.next_to(card, UP, buff=0.25)
        arrow = MathTex(r"\rightarrow", font_size=LABEL_SIZE, color=PRIMARY)
        arrow.next_to(up_next, RIGHT, buff=0.1)
        scene.play(FadeIn(up_next), FadeIn(arrow), run_time=0.3)
        scene.wait(1.2)

        everything = VGroup(thanks, subscribe, logo, channel, card, up_next, arrow)
    else:
        everything = VGroup(thanks, subscribe, logo, channel)

    scene.play(FadeOut(everything), run_time=0.6)
    scene.wait(0.3)
