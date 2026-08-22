r"""
Video 228: Advanced Abstract Algebra Summary

Final video of the playlist. Recaps the journey from group actions
through Galois theory to Abel-Ruffini, cyclotomic fields, and finite fields.

Follows v2 template quality rules.
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


class Video228_AdvancedAlgebraSummary(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_groups()
        self.scene3_fields()
        self.scene4_galois()
        self.scene5_special()
        self.scene6_grand_connection()
        self.scene7_next_steps()

    def scene1_hook(self):
        self.add_subcaption(
            "We have come a long way. Starting from group actions and solvable groups, "
            "building through field extensions and Galois theory, and culminating in "
            "the proof that the general quintic is not solvable by radicals. "
            "This video recaps the entire Advanced Abstract Algebra playlist.",
            duration=14,
        )
        play_intro(self, "Advanced Abstract Algebra Summary", "Advanced Abstract Algebra")

        title = self.ly.title("The Big Picture")

        # Timeline of videos
        timeline_items = [
            Text("217-218: Groups (actions, solvable, nilpotent)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("219-221: Fields (extensions, algebraic, splitting)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("222-225: Galois Theory (groups, FTGT, Abel-Ruffini)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("226-227: Cyclotomic Fields, Finite Fields",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(timeline_items, start_from=title)
        self.ly.clear()

    def scene2_groups(self):
        self.add_subcaption(
            "Videos 217 and 218 covered advanced group theory. Group actions formalize symmetry. "
            "Solvable groups have a terminating derived series. Nilpotent groups are stronger. "
            "The Sylow theorems constrain finite group structure.",
            duration=14,
        )
        title = self.ly.title("Part I: Groups (Videos 217-218)")
        items = [
            Text("Group actions: formalizing symmetry",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Solvable groups: derived series terminates at {e}",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Nilpotent groups: lower central series terminates",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Sylow theorems: structure of finite groups",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene3_fields(self):
        self.add_subcaption(
            "Videos 219 through 221 built field theory. Field extensions measure how much "
            "bigger one field is than another. Algebraic extensions are where every element "
            "satisfies a polynomial. Splitting fields contain all roots of a polynomial.",
            duration=14,
        )
        title = self.ly.title("Part II: Fields (Videos 219-221)")
        items = [
            Text("Field extensions: E/F, degree [E:F]",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Algebraic extensions: minimal polynomials, tower law",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Splitting fields: contain all roots, degree <= n!",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene4_galois(self):
        self.add_subcaption(
            "Videos 222 through 225 are the heart of the playlist. Galois groups capture "
            "symmetries of field extensions. The Fundamental Theorem establishes a perfect "
            "correspondence between subfields and subgroups. The Abel-Ruffini theorem shows "
            "the general quintic is unsolvable because S5 is not solvable.",
            duration=18,
        )
        title = self.ly.title("Part III: Galois Theory (Videos 222-225)")
        items = [
            Text("Galois groups: Aut(E/F), symmetries of extensions",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("FTGT: subfields <-> subgroups (perfect correspondence)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Solvability by radicals <-> solvable Galois group",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Abel-Ruffini: S5 not solvable -> quintic unsolvable",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("A5 is simple: the key lemma",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene5_special(self):
        self.add_subcaption(
            "Videos 226 and 227 explored two beautiful families of fields. "
            "Cyclotomic fields have abelian Galois groups. Finite fields have "
            "cyclic Galois groups generated by the Frobenius automorphism.",
            duration=12,
        )
        title = self.ly.title("Part IV: Special Fields (Videos 226-227)")
        items = [
            Text("Cyclotomic fields: Q(zeta_n), Galois group (Z/nZ)*",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Applications: constructibility, reciprocity, FLT",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Finite fields: GF(p^n), Frobenius generates Galois group",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Applications: coding theory, cryptography",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene6_grand_connection(self):
        self.add_subcaption(
            "The grand connection: solving polynomial equations by radicals is equivalent "
            "to checking whether the Galois group is solvable. Groups control fields "
            "through the FTGT. Field extensions encode polynomial roots. "
            "This triangle is Galois' immortal insight.",
            duration=16,
        )
        title = self.ly.title("The Grand Connection")

        # Triangle of concepts
        groups = Text("GROUPS", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        fields = Text("FIELDS", font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        polys = Text("POLYNOMIALS", font_size=HEADING_SIZE, color=ACCENT, font=SANS)

        # Position in triangle
        groups.move_to(UP * 1.5)
        fields.move_to(DOWN * 1.0 + LEFT * 2.5)
        polys.move_to(DOWN * 1.0 + RIGHT * 2.5)

        tri = VGroup(groups, fields, polys)
        self.ly.center_in_content(tri)

        # Arrows
        arrow_gf = Arrow(fields.get_top(), groups.get_bottom(),
                         buff=0.3, stroke_width=2, color=DIM)
        arrow_gp = Arrow(groups.get_bottom(), polys.get_top(),
                         buff=0.3, stroke_width=2, color=DIM)
        arrow_fp = Arrow(polys.get_left(), fields.get_right(),
                         buff=0.3, stroke_width=2, color=DIM)

        self.play(FadeIn(groups), FadeIn(fields), FadeIn(polys), run_time=FAST)
        self.play(Create(arrow_gf), Create(arrow_gp), Create(arrow_fp), run_time=NORMAL)
        self.wait(6)
        self.ly.clear()

    def scene7_next_steps(self):
        self.add_subcaption(
            "Where to from here? Algebraic number theory applies these tools to study "
            "integers in number fields. Algebraic geometry studies polynomial rings "
            "and geometric objects. Representation theory studies groups through "
            "their actions on vector spaces. Thank you for watching.",
            duration=16,
        )
        title = self.ly.title("What Comes Next")
        items = [
            Text("Algebraic Number Theory: integers in number fields",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Algebraic Geometry: polynomial rings and varieties",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Representation Theory: groups acting on vector spaces",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

        play_outro(self, "", "Advanced Abstract Algebra")
