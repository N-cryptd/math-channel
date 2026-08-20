"""
Video 222: Galois Theory - Advanced Abstract Algebra
Galois groups, field automorphisms, Aut(E/F), fixed fields,
and the Galois correspondence teaser.

QUALITY RULES:
1. Max 5 visible elements per scene
2. LayoutEngine for ALL positioning
3. Progressive disclosure
4. Raw strings with single backslashes for LaTeX
5. ly.clear() between scenes
6. One subcaption per scene, self.wait(3-5) after content
"""

from manim import *
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'templates'))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video222_GaloisTheory(Scene):
    """Galois Theory: the symmetries of field extensions."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_automorphisms()
        self.scene3_example_sqrt2()
        self.scene4_example_zeta3()
        self.scene5_fixed_fields()
        self.scene6_correspondence()
        self.scene7_summary()

    def scene1_hook(self):
        """Hook - the mystery of field symmetries."""
        self.add_subcaption(
            'In the last few videos we built up the machinery of field extensions '
            'algebraic elements, minimal polynomials, splitting fields. But there is '
            'a question we have not asked yet: what are the symmetries of a field '
            'extension? If we adjoin the square root of 2 to Q, what maps does Q of '
            'square root of 2 have that preserve the field structure? This question '
            'and its stunning answer is Galois theory.',
            duration=30,
        )
        play_intro(self, 'Galois Theory', 'Advanced Abstract Algebra')

        title = self.ly.title('The Symmetries of Field Extensions')
        items = [
            Text('Field extensions: Q < Q(sqrt2) < Q(sqrt2, i)',
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text('Question: what maps preserve the algebraic structure?',
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text('Galois groups encode these symmetries',
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(7)
        self.ly.clear()

    def scene2_automorphisms(self):
        """Field automorphisms - definition."""
        self.add_subcaption(
            'A field automorphism is a bijective map from a field to itself '
            'that preserves addition and multiplication. For a field extension '
            'E over F, we are interested in automorphisms of E that fix every '
            'element of F. These form a group called Aut of E over F, also '
            'written as Gal of E over F.',
            duration=28,
        )
        self.ly.section_divider(1, 'Field Automorphisms')

        title = self.ly.title('Field Automorphisms')

        # Definition: sigma properties
        defn = MathTex(
            r'\sigma : E \to E \text{ bijective, } '
            r'\sigma(a+b) = \sigma(a)+\sigma(b), '
            r'\sigma(ab) = \sigma(a)\sigma(b)',
            font_size=BODY_SIZE, color=PRIMARY,
        )
        boxed_defn = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.safe_place(boxed_defn, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_defn), run_time=NORMAL)
        self.wait(3)

        # Gal(E/F) definition
        self.play(FadeOut(boxed_defn), run_time=FAST)
        gal_def = MathTex(
            r'\text{Gal}(E/F) = \{\sigma \in \text{Aut}(E) : '
            r'\sigma(c) = c \text{ for all } c \in F\}',
            font_size=BODY_SIZE, color=SECONDARY,
        )
        boxed_gal = self.ly.formula_box(gal_def, color=SECONDARY)
        self.ly.safe_place(boxed_gal, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_gal), run_time=NORMAL)
        self.wait(3)

        # Group property
        grp = Text(
            'Gal(E/F) forms a GROUP under composition',
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(grp, DOWN, anchor=boxed_gal, buff=0.4)
        self.play(FadeIn(grp, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene3_example_sqrt2(self):
        """Example: Gal(Q(sqrt2)/Q)."""
        self.add_subcaption(
            'Let us compute our first Galois group. Every element of Q of square '
            'root of 2 can be written as a plus b times square root of 2. An '
            'automorphism sigma fixing Q must send square root of 2 to another root '
            'of x squared minus 2, so either square root of 2 or negative square root '
            'of 2. This gives exactly two automorphisms: the identity and the map '
            'sending square root of 2 to negative square root of 2. So the Galois group '
            'is isomorphic to Z over 2Z.',
            duration=38,
        )
        self.ly.section_divider(2, 'First Example')

        title = self.ly.title('Gal(Q(sqrt2) / Q)')

        # Element form
        elem = MathTex(
            r'\text{Every element: } a + b\sqrt{2}, \text{ where } a, b \in \mathbb{Q}',
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(elem, DOWN, anchor=title, buff=0.5)
        self.play(Write(elem), run_time=NORMAL)
        self.wait(3)

        # Root constraint
        self.play(FadeOut(elem), run_time=FAST)
        constraint = MathTex(
            r'\sigma(\sqrt{2}) \text{ must satisfy } x^2 - 2 = 0',
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(constraint, DOWN, anchor=title, buff=0.5)
        self.play(Write(constraint), run_time=NORMAL)
        self.wait(2)

        roots = MathTex(
            r'\Rightarrow \sigma(\sqrt{2}) = \sqrt{2} \text{ or } \sigma(\sqrt{2}) = -\sqrt{2}',
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(roots, DOWN, anchor=constraint, buff=0.4)
        self.play(Write(roots), run_time=NORMAL)
        self.wait(3)

        # Table of automorphisms
        self.play(FadeOut(constraint), FadeOut(roots), run_time=FAST)
        id_map = MathTex(
            r'\text{id}: a + b\sqrt{2} \mapsto a + b\sqrt{2}',
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(id_map, DOWN, anchor=title, buff=0.5)
        self.play(Write(id_map), run_time=NORMAL)
        self.wait(2)

        sigma_map = MathTex(
            r'\sigma: a + b\sqrt{2} \mapsto a - b\sqrt{2}',
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(sigma_map, DOWN, anchor=id_map, buff=0.4)
        self.play(Write(sigma_map), run_time=NORMAL)
        self.wait(3)

        # Result
        self.play(FadeOut(id_map), FadeOut(sigma_map), run_time=FAST)
        result = MathTex(
            r'\text{Gal}(\mathbb{Q}(\sqrt{2}) / \mathbb{Q}) \cong \mathbb{Z}/2\mathbb{Z}',
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_result = self.ly.formula_box(result, color=ACCENT)
        self.ly.safe_place(boxed_result, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_result), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene4_example_zeta3(self):
        """Example: Gal(Q(zeta_3)/Q)."""
        self.add_subcaption(
            'Now a richer example. Let zeta sub 3 be a primitive cube root of '
            'unity, e to the 2 pi i over 3. The minimal polynomial of zeta sub 3 '
            'over Q is x squared plus x plus 1. An automorphism must send zeta sub '
            '3 to another root, either zeta sub 3 itself or zeta sub 3 squared. This '
            'gives Gal(Q(zeta sub 3) over Q) isomorphic to Z over 2Z as well, same '
            'group but for a different reason.',
            duration=36,
        )
        self.ly.section_divider(3, 'Second Example')

        title = self.ly.title('Gal(Q(zeta_3) / Q)')

        # Define zeta_3
        zeta_def = MathTex(
            r'\zeta_3 = e^{2\pi i / 3}, \text{ so } \zeta_3^2 + \zeta_3 + 1 = 0',
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(zeta_def, DOWN, anchor=title, buff=0.5)
        self.play(Write(zeta_def), run_time=NORMAL)
        self.wait(3)

        # Roots
        self.play(FadeOut(zeta_def), run_time=FAST)
        roots = MathTex(
            r'\text{Roots of } x^2+x+1: \zeta_3 \text{ and } \zeta_3^2',
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(roots, DOWN, anchor=title, buff=0.5)
        self.play(Write(roots), run_time=NORMAL)
        self.wait(3)

        # Automorphisms
        self.play(FadeOut(roots), run_time=FAST)
        auto1 = MathTex(
            r'\text{id}: \zeta_3 \mapsto \zeta_3',
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(auto1, DOWN, anchor=title, buff=0.5)
        self.play(Write(auto1), run_time=NORMAL)
        self.wait(2)

        auto2 = MathTex(
            r'\sigma: \zeta_3 \mapsto \zeta_3^2',
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(auto2, DOWN, anchor=auto1, buff=0.4)
        self.play(Write(auto2), run_time=NORMAL)
        self.wait(3)

        # Result
        self.play(FadeOut(auto1), FadeOut(auto2), run_time=FAST)
        result = MathTex(
            r'\text{Gal}(\mathbb{Q}(\zeta_3) / \mathbb{Q}) \cong \mathbb{Z}/2\mathbb{Z}',
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_result = self.ly.formula_box(result, color=ACCENT)
        self.ly.safe_place(boxed_result, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_result), run_time=NORMAL)
        self.wait(3)

        note = Text(
            'Same group, different reason (different minimal polynomials)',
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=boxed_result, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene5_fixed_fields(self):
        """Fixed fields definition and example."""
        self.add_subcaption(
            'Given a group G of automorphisms of E, the fixed field of G is the set '
            'of all elements of E that every automorphism in G leaves unchanged. For a '
            'subgroup H of the Galois group, the fixed field E to the power H gives us a '
            'field between F and E. This is one half of the Galois correspondence.',
            duration=28,
        )
        self.ly.section_divider(4, 'Fixed Fields')

        title = self.ly.title('Fixed Fields')

        # Definition
        defn = MathTex(
            r'E^H = \{x \in E : \sigma(x) = x \text{ for all } \sigma \in H\}',
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_defn = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.safe_place(boxed_defn, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_defn), run_time=NORMAL)
        self.wait(3)

        # Example computation
        self.play(FadeOut(boxed_defn), run_time=FAST)
        ex_title = Text(
            'Example: What is Q(sqrt2)^{id, sigma}?',
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(ex_title, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(ex_title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        self.play(FadeOut(ex_title), run_time=FAST)
        calc = MathTex(
            r'\sigma(a + b\sqrt{2}) = a - b\sqrt{2} = a + b\sqrt{2}',
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(calc, DOWN, anchor=title, buff=0.5)
        self.play(Write(calc), run_time=NORMAL)
        self.wait(2)

        only_if = Text(
            'This holds iff b = 0, so the fixed field is Q',
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(only_if, DOWN, anchor=calc, buff=0.4)
        self.play(FadeIn(only_if, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene6_correspondence(self):
        """The Galois correspondence - teaser."""
        self.add_subcaption(
            'Here is the remarkable theorem: for a Galois extension E over F, there is '
            'a perfect one to one correspondence between subgroups of the Galois group '
            'and intermediate fields. It reverses inclusion. Subgroups of order 2 '
            'correspond to extensions of degree 2. Normal subgroups correspond to '
            'Galois sub extensions. This is the Fundamental Theorem of Galois Theory, '
            'and we will prove it in the next video.',
            duration=32,
        )
        self.ly.section_divider(5, 'The Galois Correspondence')

        title = self.ly.title('The Fundamental Theorem')

        # Key statement
        stmt = Text(
            'Subgroups of Gal(E/F) correspond to intermediate fields',
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(stmt, DOWN, anchor=title, buff=0.5)
        self.play(Write(stmt), run_time=NORMAL)
        self.wait(3)

        # Properties
        self.play(FadeOut(stmt), run_time=FAST)
        props = [
            Text('Correspondence is inclusion-reversing',
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text('Normal subgroups <-> Galois subextensions',
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text('Order of subgroup = degree of corresponding extension',
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(props, start_from=title)
        self.wait(3)
        self.ly.clear()

        self.ly.section_divider(6, 'Coming Next')
        title2 = self.ly.title('Full Proof Next Video')
        tease = Text(
            'The Fundamental Theorem of Galois Theory: complete proof',
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(tease, DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(tease, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene7_summary(self):
        """Summary and outro."""
        self.add_subcaption(
            'Let us recap. Field automorphisms that fix the base field form the '
            'Galois group. We computed Gal(Q(sqrt2)/Q) and Gal(Q(zeta3)/Q), both '
            'isomorphic to Z over 2Z. Fixed fields give us intermediate fields from '
            'subgroups. And the Galois correspondence, the Fundamental Theorem, links '
            'subgroups and intermediate fields in a perfect, inclusion-reversing pairing. '
            'Thank you for watching!',
            duration=34,
        )
        self.ly.section_divider(7, 'Summary')

        title = self.ly.title('Key Takeaways')
        items = [
            Text('Gal(E/F) = field automorphisms fixing F',
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text('Gal(Q(sqrt2)/Q) = Z/2Z: identity + conjugation',
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text('Fixed field E^H: elements unchanged by all sigma in H',
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text('Galois correspondence: subgroups <-> intermediate fields',
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            'Thank you for watching! Next time: the Fundamental Theorem.',
            duration=6,
        )
        play_outro(self, 'The Galois Correspondence', 'Advanced Abstract Algebra')
