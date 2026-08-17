"""
Video 213: Mayer-Vietoris Sequence — Algebraic Topology
Exact sequences, the Mayer-Vietoris long exact sequence,
computing homology of spaces by decomposition.

QUALITY RULES:
1. Max 5 visible elements per scene
2. LayoutEngine for ALL positioning
3. Progressive disclosure
4. Raw strings with single backslashes for LaTeX
5. ly.clear() between scenes

NARRATION TIMING:
- One subcaption per scene (prevents SRT overlap cascade)
- Duration = total scene time (animations + waits)
- self.wait(5-8) after content to let TTS play naturally
"""

from manim import *
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video213_MayerVietoris(Scene):
    """Mayer-Vietoris: computing homology from pieces."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_exact_sequences()
        self.scene3_the_sequence()
        self.scene4_sphere_example()
        self.scene5_torus_example()
        self.scene6_summary()

    def scene1_hook(self):
        """Hook — decomposing spaces to compute homology."""
        self.add_subcaption(
            "Welcome back to Algebraic Topology! So far we have defined "
            "homology groups but computing them directly is hard. "
            "Today we learn the Mayer-Vietoris sequence, which decomposes "
            "a space into two overlapping pieces and computes the homology "
            "of the whole from the homology of the parts.",
            duration=22,
        )
        play_intro(self, "Mayer-Vietoris Sequence", "Algebraic Topology")

        title = self.ly.title("Homology by Decomposition")
        items = [
            Text("Decompose X = A cup B", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Compute H_n(A), H_n(B), H_n(A cap B)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Recover H_n(X) from the sequence", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(8)
        self.ly.clear()

    def scene2_exact_sequences(self):
        """Recap of exact sequences."""
        self.add_subcaption(
            "We need the concept of an exact sequence. "
            "A sequence of abelian groups and homomorphisms is exact "
            "if the image of each map equals the kernel of the next. "
            "A short exact sequence is a five-term exact sequence "
            "with zeros at both ends. "
            "The key fact is that for a short exact sequence, "
            "the middle group is determined by the outer two.",
            duration=26,
        )
        self.ly.section_divider(1, "Exact Sequences")

        title = self.ly.title("What is an Exact Sequence?")

        exact = MathTex(
            r"\cdots \to A \xrightarrow{f} B \xrightarrow{g} C \to \cdots",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(exact, DOWN, anchor=title, buff=0.5)
        self.play(Write(exact), run_time=NORMAL)
        self.wait(3)

        condition = MathTex(
            r"\operatorname{im}(f) = \ker(g)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        boxed_cond = self.ly.formula_box(condition, color=SECONDARY)
        self.ly.safe_place(boxed_cond, DOWN, anchor=exact, buff=0.5)
        self.play(FadeIn(boxed_cond), run_time=NORMAL)
        self.wait(3)

        short = MathTex(
            r"0 \to A \to B \to C \to 0 \implies B \cong A \oplus C",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(short, DOWN, anchor=boxed_cond, buff=0.5)
        self.play(Write(short), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene3_the_sequence(self):
        """The Mayer-Vietoris long exact sequence."""
        self.add_subcaption(
            "The Mayer-Vietoris sequence is a long exact sequence "
            "that relates the homology of X to the homology of A, B, "
            "and their intersection. "
            "For each dimension n, there is a connecting homomorphism "
            "from H_n of the intersection to H_(n-1) of the union. "
            "The sequence is exact at every term, meaning the image "
            "of each map equals the kernel of the next.",
            duration=26,
        )
        self.ly.section_divider(2, "The Mayer-Vietoris Sequence")

        title = self.ly.title("The Long Exact Sequence")

        mv_seq = MathTex(
            r"\cdots \to H_n(A \cap B) \to H_n(A) \oplus H_n(B)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(mv_seq, DOWN, anchor=title, buff=0.4)
        self.play(Write(mv_seq), run_time=NORMAL)
        self.wait(2)

        mv_seq2 = MathTex(
            r"\to H_n(X) \xrightarrow{\partial} H_{n-1}(A \cap B) \to \cdots",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(mv_seq2, DOWN, anchor=mv_seq, buff=0.4)
        self.play(Write(mv_seq2), run_time=NORMAL)
        self.wait(3)

        note = Text(
            "Exact at every group: im(f) = ker(g)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=mv_seq2, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene4_sphere_example(self):
        """Computing H_n(S^2) using Mayer-Vietoris."""
        self.add_subcaption(
            "Let us compute the homology of the two-sphere using Mayer-Vietoris. "
            "Decompose S^2 as the union of the upper hemisphere U "
            "and the lower hemisphere D, each homeomorphic to a disk. "
            "Their intersection is a circle, the equator. "
            "Both disks are contractible, so their homology is trivial "
            "except in dimension zero. "
            "The sequence then forces H_2(S^2) to be Z, "
            "which detects the void inside the sphere.",
            duration=30,
        )
        self.ly.section_divider(3, "Example: The Sphere S^2")

        title = self.ly.title("Decomposing S^2")

        decomposition = VGroup(
            Text("S^2 = U cup D", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("U, D: contractible (like disks)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("U cap D: circle S^1", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        )
        self.ly.progressive_reveal(decomposition, start_from=title)
        self.wait(4)
        self.ly.clear()

        self.add_subcaption(
            "Since U and D are contractible, their homology vanishes "
            "above dimension zero. Plugging into the Mayer-Vietoris sequence, "
            "we find that H_2(S^2) is isomorphic to Z, "
            "confirming that the sphere has a two-dimensional void.",
            duration=18,
        )
        title2 = self.ly.title("Result")

        result = MathTex(
            r"H_0(S^2) = \mathbb{Z}, \quad H_1(S^2) = 0, \quad H_2(S^2) = \mathbb{Z}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_result = self.ly.formula_box(result, color=PRIMARY)
        self.ly.safe_place(boxed_result, DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(boxed_result), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene5_torus_example(self):
        """Computing H_n(T^2) using Mayer-Vietoris."""
        self.add_subcaption(
            "For the torus, decompose it as the union of two cylinders. "
            "Each cylinder deformation retracts to a circle, "
            "and their intersection is two disjoint circles. "
            "The Mayer-Vietoris sequence then gives us "
            "H_1 of the torus is Z cross Z, reflecting the two "
            "independent loops around the torus.",
            duration=22,
        )
        self.ly.section_divider(4, "Example: The Torus T^2")

        title = self.ly.title("Homology of the Torus")

        result = VGroup(
            MathTex(r"H_0(T^2) = \mathbb{Z}", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"H_1(T^2) = \mathbb{Z} \times \mathbb{Z}", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"H_2(T^2) = \mathbb{Z}", font_size=BODY_SIZE, color=ACCENT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        self.ly.safe_place(result, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(result, shift=LEFT * 0.15), run_time=NORMAL)

        note = Text(
            "H_1 = Z x Z: one generator per independent loop",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=result, buff=0.5)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene6_summary(self):
        """Summary and outro."""
        self.add_subcaption(
            "The Mayer-Vietoris sequence is the homology analog of the "
            "Seifert-van Kampen theorem for fundamental groups. "
            "It lets us compute homology by decomposing a space "
            "into pieces whose homology we already know. "
            "This is one of the most powerful computational tools "
            "in algebraic topology. "
            "In the next video, we will study the degree of a map, "
            "which generalizes winding numbers to higher dimensions.",
            duration=28,
        )
        self.ly.section_divider(5, "Summary")

        title = self.ly.title("Key Takeaways")
        items = [
            Text("Decompose X = A cup B with known homology", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Long exact sequence connects all groups", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Compute H_n(X) from the sequence", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Analogous to Seifert-van Kampen for pi_1", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "In the next video, we will study the degree of a continuous map, "
            "which generalizes winding numbers to higher dimensions. "
            "Thank you for watching!",
            duration=12,
        )
        play_outro(self, "Degree of a Map", "Algebraic Topology")
