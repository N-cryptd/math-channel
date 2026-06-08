"""
Video 38: Orthogonality and Gram-Schmidt
Linear Algebra Playlist -- Video 14 of 16

Covers: orthogonal sets, orthonormal bases, projection onto a line,
Gram-Schmidt process, QR decomposition preview.

Render draft:  manim -ql scripts/undergraduate/video-38-orthogonality-gram-schmidt.py Video38_OrthogonalityGramSchmidt
Render final:  manim -qh scripts/undergraduate/video-38-orthogonality-gram-schmidt.py Video38_OrthogonalityGramSchmidt
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


class Video38_OrthogonalityGramSchmidt(Scene):
    """Full video: orthogonality, Gram-Schmidt, QR decomposition."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_orthogonal_sets()
        self.scene3_orthonormal_bases()
        self.scene4_projection()
        self.scene5_gram_schmidt()
        self.scene6_qr_decomposition()
        self.scene7_summary()

    # ── Scene 1: Hook + Channel Intro ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "Orthogonal vectors are the cleanest building blocks. "
            "Today we learn how to build an orthogonal basis "
            "from any basis.",
            duration=7,
        )
        play_intro(self, "Orthogonality & Gram-Schmidt", "Linear Algebra")

        recap = Text(
            "Gram-Schmidt: turning any basis into an orthogonal one",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(recap)
        self.play(FadeIn(recap, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ── Scene 2: Orthogonal Sets ───────────────────────────────────
    def scene2_orthogonal_sets(self):
        self.ly.section_divider(1, "Orthogonal Sets")
        self.wait(0.3)

        self.add_subcaption(
            "A set of vectors is orthogonal "
            "if every pair has inner product zero.",
            duration=5,
        )

        title = self.ly.title("Orthogonal Sets")

        defn = MathTex(
            r"\{ \mathbf{v}_1, \dots, \mathbf{v}_k \} \text{ orthogonal}"
            r"\iff \langle \mathbf{v}_i, \mathbf{v}_j \rangle = 0"
            r"\text{ for } i \neq j",
            font_size=BODY_SIZE, color=WHITE,
        )

        self.add_subcaption(
            "Orthogonal sets are automatically linearly independent. "
            "This makes them ideal as bases.",
            duration=6,
        )

        note = Text(
            "Orthogonal set => linearly independent",
            font_size=BODY_SIZE, color=SECONDARY, font=MONO,
        )

        items = [defn, note]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.6)
        self.ly.center_in_content(fitted)
        self.play(Write(defn), run_time=NORMAL)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 3: Orthonormal Bases ─────────────────────────────────
    def scene3_orthonormal_bases(self):
        self.ly.section_divider(2, "Orthonormal Bases")
        self.wait(0.3)

        self.add_subcaption(
            "An orthonormal basis is even better. "
            "Each vector has unit length and is orthogonal to all others.",
            duration=6,
        )

        title = self.ly.title("Orthonormal Bases")

        defn = MathTex(
            r"\|\mathbf{q}_i\| = 1 \text{ and } "
            r"\langle \mathbf{q}_i, \mathbf{q}_j \rangle = 0"
            r" \text{ for } i \neq j",
            font_size=BODY_SIZE, color=WHITE,
        )

        self.add_subcaption(
            "With an orthonormal basis, "
            "coordinates are just inner products. "
            "No system of equations needed.",
            duration=6,
        )

        coord = MathTex(
            r"\mathbf{x} = \sum_{i} \langle \mathbf{x}, \mathbf{q}_i \rangle \mathbf{q}_i",
            font_size=HEADING_SIZE, color=PRIMARY,
        )

        items = [defn, coord]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.6)
        self.ly.center_in_content(fitted)
        self.play(Write(defn), run_time=NORMAL)
        self.play(Write(coord), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 4: Projection ────────────────────────────────────────
    def scene4_projection(self):
        self.add_subcaption(
            "To build orthogonal bases, we first need projection. "
            "Projecting v onto u gives the component of v along u.",
            duration=7,
        )

        title = self.ly.title("Orthogonal Projection")

        formula = MathTex(
            r"\text{proj}_{\mathbf{u}} \mathbf{v} = "
            r"\frac{\langle \mathbf{v}, \mathbf{u} \rangle}"
            r"{\langle \mathbf{u}, \mathbf{u} \rangle} \mathbf{u}",
            font_size=HEADING_SIZE, color=WHITE,
        )

        self.add_subcaption(
            "The residual is orthogonal to u. "
            "This property is the key to Gram-Schmidt.",
            duration=5,
        )

        residual = MathTex(
            r"\mathbf{v} - \text{proj}_{\mathbf{u}} \mathbf{v}"
            r"\perp \mathbf{u}",
            font_size=HEADING_SIZE, color=ACCENT,
        )

        items = [formula, residual]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.6)
        self.ly.center_in_content(fitted)
        self.play(Write(formula), run_time=NORMAL)
        self.play(Write(residual), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 5: Gram-Schmidt Process ──────────────────────────────
    def scene5_gram_schmidt(self):
        self.ly.section_divider(3, "Gram-Schmidt Process")
        self.wait(0.3)

        self.add_subcaption(
            "Gram-Schmidt turns any basis "
            "into an orthogonal basis, one vector at a time.",
            duration=5,
        )

        title = self.ly.title("The Gram-Schmidt Algorithm")

        self.add_subcaption(
            "Step 1: keep the first vector as is. "
            "Step 2: subtract its projection from the second vector.",
            duration=6,
        )

        step1 = MathTex(
            r"\mathbf{u}_1 = \mathbf{v}_1",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        step2 = MathTex(
            r"\mathbf{u}_2 = \mathbf{v}_2"
            r"- \text{proj}_{\mathbf{u}_1} \mathbf{v}_2",
            font_size=HEADING_SIZE, color=SECONDARY,
        )

        self.add_subcaption(
            "Step 3: subtract projections onto "
            "both previous vectors. Continue for all vectors.",
            duration=6,
        )

        step3 = MathTex(
            r"\mathbf{u}_3 = \mathbf{v}_3"
            r"- \text{proj}_{\mathbf{u}_1} \mathbf{v}_3"
            r"- \text{proj}_{\mathbf{u}_2} \mathbf{v}_3",
            font_size=BODY_SIZE, color=ACCENT,
        )

        steps = VGroup(step1, step2, step3).arrange(DOWN, buff=0.5)
        ensure_fits(steps, max_height=4.5)
        self.ly.center_in_content(steps)
        self.play(Write(step1), run_time=FAST)
        self.play(Write(step2), run_time=NORMAL)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 6: QR Decomposition ──────────────────────────────────
    def scene6_qr_decomposition(self):
        self.ly.section_divider(4, "QR Decomposition")
        self.wait(0.3)

        self.add_subcaption(
            "Gram-Schmidt naturally produces "
            "the QR decomposition of a matrix.",
            duration=5,
        )

        title = self.ly.title("QR Decomposition")

        formula = MathTex(
            r"A = QR",
            font_size=TITLE_SIZE, color=WHITE,
        )

        self.add_subcaption(
            "Q has orthonormal columns. "
            "R is upper triangular. "
            "This is the backbone of numerical linear algebra.",
            duration=7,
        )

        desc1 = Text(
            "Q = orthonormal columns from Gram-Schmidt",
            font_size=BODY_SIZE, color=PRIMARY, font=MONO,
        )
        desc2 = Text(
            "R = upper triangular (the coefficients)",
            font_size=BODY_SIZE, color=SECONDARY, font=MONO,
        )
        note = Text(
            "Used in least squares, eigenvalue algorithms, and more",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )

        items = [formula, desc1, desc2, note]
        fitted, overflow = self.ly.stack_down(items, start_from=title, spacing=0.4)
        self.ly.center_in_content(fitted)
        self.play(Write(formula), run_time=NORMAL)
        self.play(FadeIn(desc1, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(desc2, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Summary + Outro ───────────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "Gram-Schmidt builds orthogonal bases from any basis. "
            "QR decomposition is its matrix form.",
            duration=5,
        )

        title = self.ly.title("Summary")

        bullet1 = Text(
            "Orthogonal sets are automatically independent",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        bullet2 = Text(
            "Gram-Schmidt: subtract projections one by one",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        bullet3 = Text(
            "A = QR: Q orthonormal, R upper triangular",
            font_size=BODY_SIZE, color=ACCENT, font=MONO,
        )

        items = [bullet1, bullet2, bullet3]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "Next time we study linear transformations in the abstract. "
            "Thanks for watching!",
            duration=4,
        )
        play_outro(self, "Linear Transformations", "Linear Algebra")
        self.ly.clear()
