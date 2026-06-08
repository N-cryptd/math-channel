"""
Video 37: Inner Product Spaces
Linear Algebra Playlist -- Video 13 of 16

Covers: dot product review, inner product definition and axioms,
Cauchy-Schwarz inequality, angle between vectors, orthogonality.

Render draft:  manim -ql scripts/undergraduate/video-37-inner-product.py Video37_InnerProduct
Render final:  manim -qh scripts/undergraduate/video-37-inner-product.py Video37_InnerProduct
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


class Video37_InnerProduct(Scene):
    """Full video: inner product spaces."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_dot_product_review()
        self.scene3_inner_product_axioms()
        self.scene4_cauchy_schwarz()
        self.scene5_angle_between()
        self.scene6_orthogonality()
        self.scene7_summary()

    # ── Scene 1: Hook + Channel Intro ──────────────────────────────
    def scene1_hook(self):
        self.add_subcaption(
            "So far we have used the dot product "
            "without examining it carefully. "
            "Today we generalize it to inner products.",
            duration=7,
        )
        play_intro(self, "Inner Product Spaces", "Linear Algebra")

        recap = Text(
            "A deeper look at measuring vectors",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.center_in_content(recap)
        self.play(FadeIn(recap, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # ── Scene 2: Dot Product Review ────────────────────────────────
    def scene2_dot_product_review(self):
        self.ly.section_divider(1, "The Dot Product")
        self.wait(0.3)

        self.add_subcaption(
            "The dot product measures how much two vectors point "
            "in the same direction. "
            "It equals the sum of products of components.",
            duration=7,
        )

        title = self.ly.title("Dot Product in R^n")

        formula = MathTex(
            r"\mathbf{u} \cdot \mathbf{v}"
            r"= u_1 v_1 + u_2 v_2 + \cdots + u_n v_n",
            font_size=HEADING_SIZE, color=WHITE,
        )
        geometric = MathTex(
            r"= \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta",
            font_size=HEADING_SIZE, color=PRIMARY,
        )

        items = [formula, geometric]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.6)
        self.ly.center_in_content(fitted)
        self.play(Write(formula), run_time=NORMAL)
        self.play(Write(geometric), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 3: Inner Product Axioms ──────────────────────────────
    def scene3_inner_product_axioms(self):
        self.ly.section_divider(2, "Inner Product Axioms")
        self.wait(0.3)

        self.add_subcaption(
            "An inner product generalizes the dot product. "
            "It must satisfy four axioms.",
            duration=5,
        )

        title = self.ly.title("Definition: Inner Product")

        axiom1 = MathTex(
            r"\langle \mathbf{u}, \mathbf{v} \rangle"
            r"= \langle \mathbf{v}, \mathbf{u} \rangle",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        label1 = Text("Symmetry", font_size=LABEL_SIZE, color=DIM, font=MONO)

        axiom2 = MathTex(
            r"\langle \mathbf{u} + \mathbf{w}, \mathbf{v} \rangle"
            r"= \langle \mathbf{u}, \mathbf{v} \rangle"
            r"+ \langle \mathbf{w}, \mathbf{v} \rangle",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        label2 = Text("Linearity (first argument)", font_size=LABEL_SIZE, color=DIM, font=MONO)

        axiom3 = MathTex(
            r"\langle c\mathbf{u}, \mathbf{v} \rangle"
            r"= c\langle \mathbf{u}, \mathbf{v} \rangle",
            font_size=BODY_SIZE, color=ACCENT,
        )
        label3 = Text("Homogeneity", font_size=LABEL_SIZE, color=DIM, font=MONO)

        axiom4 = MathTex(
            r"\langle \mathbf{u}, \mathbf{u} \rangle \geq 0, "
            r"= 0 \text{ iff } \mathbf{u} = \mathbf{0}",
            font_size=BODY_SIZE, color=WHITE,
        )
        label4 = Text("Positive definiteness", font_size=LABEL_SIZE, color=DIM, font=MONO)

        # Progressive reveal with labels paired
        pair1 = VGroup(axiom1, label1).arrange(RIGHT, buff=0.4)
        pair2 = VGroup(axiom2, label2).arrange(RIGHT, buff=0.4)
        pair3 = VGroup(axiom3, label3).arrange(RIGHT, buff=0.4)
        pair4 = VGroup(axiom4, label4).arrange(RIGHT, buff=0.4)

        items = [pair1, pair2, pair3, pair4]
        fitted, overflow = self.ly.stack_down(items, start_from=title, spacing=0.35)
        self.ly.center_in_content(fitted)
        for item in items:
            self.play(FadeIn(item, shift=LEFT * 0.15), run_time=FAST)
            self.wait(0.5)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 4: Cauchy-Schwarz Inequality ─────────────────────────
    def scene4_cauchy_schwarz(self):
        self.ly.section_divider(3, "Cauchy-Schwarz Inequality")
        self.wait(0.3)

        self.add_subcaption(
            "The most important inequality in linear algebra. "
            "The absolute value of the inner product "
            "is at most the product of the norms.",
            duration=7,
        )

        title = self.ly.title("Cauchy-Schwarz Inequality")

        formula = MathTex(
            r"|\langle \mathbf{u}, \mathbf{v} \rangle|"
            r"\leq \|\mathbf{u}\| \|\mathbf{v}\|",
            font_size=HEADING_SIZE, color=WHITE,
        )

        self.add_subcaption(
            "Equality holds when u and v are parallel. "
            "This inequality underpins the angle formula.",
            duration=6,
        )

        note1 = Text(
            "Equality iff u and v are parallel",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        note2 = Text(
            "Foundation for the angle formula",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )

        items = [formula, note1, note2]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.5)
        self.ly.center_in_content(fitted)
        self.play(Write(formula), run_time=NORMAL)
        self.play(FadeIn(note1, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(note2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 5: Angle Between Vectors ─────────────────────────────
    def scene5_angle_between(self):
        self.add_subcaption(
            "The Cauchy-Schwarz inequality guarantees that "
            "cosine theta stays between minus 1 and 1.",
            duration=6,
        )

        title = self.ly.title("Angle Between Vectors")

        formula = MathTex(
            r"\cos\theta = "
            r"\frac{\langle \mathbf{u}, \mathbf{v} \rangle}"
            r"{\|\mathbf{u}\| \|\mathbf{v}\|}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )

        self.add_subcaption(
            "This generalizes the dot product angle formula "
            "to any inner product space.",
            duration=5,
        )

        example = MathTex(
            r"\text{Example: } \mathbf{u}=(1,0), \mathbf{v}=(1,1) "
            r"\Rightarrow \cos\theta = \frac{1}{\sqrt{2}}"
r"\Rightarrow \theta = 45^\circ",
            font_size=BODY_SIZE, color=WHITE,
        )

        items = [formula, example]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.6)
        self.ly.center_in_content(fitted)
        ensure_fits(fitted, max_width=6.5)
        self.play(Write(formula), run_time=NORMAL)
        self.play(Write(example), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 6: Orthogonality ─────────────────────────────────────
    def scene6_orthogonality(self):
        self.ly.section_divider(4, "Orthogonality")
        self.wait(0.3)

        self.add_subcaption(
            "Two vectors are orthogonal if their inner product is zero. "
            "This is the generalization of perpendicularity.",
            duration=7,
        )

        title = self.ly.title("Orthogonal Vectors")

        defn = MathTex(
            r"\mathbf{u} \perp \mathbf{v} "
            r"\iff \langle \mathbf{u}, \mathbf{v} \rangle = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )

        self.add_subcaption(
            "Orthogonal vectors are the building blocks "
            "of the best coordinate systems. "
            "Pythagoras generalizes to inner product spaces.",
            duration=7,
        )

        pyth = MathTex(
            r"\mathbf{u} \perp \mathbf{v} \Rightarrow "
            r"\|\mathbf{u} + \mathbf{v}\|^2 = "
            r"\|\mathbf{u}\|^2 + \|\mathbf{v}\|^2",
            font_size=BODY_SIZE, color=SECONDARY,
        )

        items = [defn, pyth]
        fitted, _ = self.ly.stack_down(items, start_from=title, spacing=0.6)
        self.ly.center_in_content(fitted)
        self.play(Write(defn), run_time=NORMAL)
        self.play(Write(pyth), run_time=NORMAL)
        self.wait(2.0)
        self.ly.clear()

    # ── Scene 7: Summary + Outro ───────────────────────────────────
    def scene7_summary(self):
        self.add_subcaption(
            "Inner products measure vectors in any space. "
            "Cauchy-Schwarz bounds them. "
            "Orthogonality generalizes perpendicularity.",
            duration=7,
        )

        title = self.ly.title("Summary")

        bullet1 = Text(
            "Inner product: symmetric, linear, positive definite",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        bullet2 = Text(
            "Cauchy-Schwarz: |<u,v>| <= ||u|| ||v||",
            font_size=BODY_SIZE, color=ACCENT, font=MONO,
        )
        bullet3 = Text(
            "Orthogonal iff inner product equals zero",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        items = [bullet1, bullet2, bullet3]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.0)

        self.add_subcaption(
            "Next time we explore orthogonality in depth "
            "and learn the Gram-Schmidt process. "
            "Thanks for watching!",
            duration=5,
        )
        play_outro(self, "Orthogonality & Gram-Schmidt", "Linear Algebra")
        self.ly.clear()
