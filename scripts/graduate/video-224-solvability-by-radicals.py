r"""
Video 224: Solvability by Radicals — Advanced Abstract Algebra
Radical extensions, the theorem connecting solvable Galois groups to
solvability by radicals, the quartic example, teaser for quintic insolvability.

QUALITY RULES:
1. Max 5 visible elements per scene
2. LayoutEngine for ALL positioning
3. Progressive disclosure
4. Raw strings with single backslashes for LaTeX
5. ly.clear() between scenes
6. One subcaption per scene, self.wait(3-5) after content

Builds on: Video 218 (solvable groups), Video 222 (Galois groups),
Video 223 (FTGT).
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


class Video224_SolvabilityByRadicals(Scene):
    """Solvability by Radicals: when can a polynomial be solved with roots?"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_radical_extensions()
        self.scene3_solvable_by_radicals()
        self.scene4_big_theorem()
        self.scene5_why_radical_implies_solvable()
        self.scene6_quartic_example()
        self.scene7_quintic_teaser()
        self.scene8_summary()

    def scene1_hook(self):
        """Hook — the 300-year-old question."""
        self.add_subcaption(
            'For over 300 years, mathematicians sought a general formula to '
            'solve polynomial equations by radicals. Quadratics have the '
            'quadratic formula. Cubics have Cardano\'s formula. Quartics '
            'have Ferrari\'s formula. But quintics? No general formula '
            'exists. Today we connect this to Galois theory. The question '
            '"which equations are solvable by radicals?" becomes "which '
            'Galois groups are solvable?" And we already know the answer '
            'from Video 218.',
            duration=55,
        )
        play_intro(self, 'Solvability by Radicals', 'Advanced Abstract Algebra')

        title = self.ly.title('The 300-Year-Old Question')
        items = [
            Text('Quadratic, cubic, quartic formulas all use radicals',
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text('Is there a general radical formula for degree 5+?',
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text('Galois\' insight: reformulate in terms of Galois groups',
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text('Answer: exactly when the Galois group is solvable',
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(22)
        self.ly.clear()

    def scene2_radical_extensions(self):
        """Radical Extensions — definition and tower visualization."""
        self.add_subcaption(
            'What does it mean to solve a polynomial by radicals? It means '
            'the roots live in a field you can build by successively '
            'adjoining roots. Formally, a radical extension of F is an '
            'extension E over F where there exists a tower of fields F '
            'equals K sub zero, contained in K sub one, contained in K '
            'sub two, all the way up to K sub n equals E, where each step '
            'K sub i over K sub i minus one is obtained by adjoining an '
            'element alpha sub i such that alpha sub i to the power of m '
            'sub i lies in K sub i minus one. In other words, each step '
            'adds a radical.',
            duration=70,
        )
        self.ly.section_divider(1, 'Radical Extensions')

        title = self.ly.title('Radical Extensions')

        # The tower
        tower = MathTex(
            r'F = K_0 \\< K_1 \\< K_2 \\< \cdots \\< K_n = E',
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(tower, DOWN, anchor=title, buff=0.5)
        self.play(Write(tower), run_time=NORMAL)
        self.wait(10)

        # Each step condition
        step = MathTex(
            r'K_i = K_{i-1}(\alpha_i), \quad \alpha_i^{m_i} \in K_{i-1}',
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step, DOWN, anchor=tower, buff=0.5)
        self.play(Write(step), run_time=NORMAL)
        self.wait(10)

        # Concrete example
        example = Text(
            'Example: Q(sqrt2, sqrt3) = Q(sqrt2)(sqrt3) is radical over Q',
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(example, DOWN, anchor=step, buff=0.4)
        self.play(FadeIn(example, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(12)
        self.ly.clear()

    def scene3_solvable_by_radicals(self):
        """When is a polynomial solvable by radicals?"""
        self.add_subcaption(
            'A polynomial f over F is solvable by radicals if its '
            'splitting field is contained in a radical extension of F. '
            'That is the definition. Let us check it on two examples. '
            'x squared minus 2 over Q has splitting field Q of square root '
            'of 2, which is itself a radical extension, so it is solvable '
            'by radicals. For x cubed minus 2 over Q, the splitting field '
            'is Q of cube root of 2, omega, where omega is a primitive '
            'cube root of unity. This is a radical extension: first '
            'adjoin omega, then adjoin cube root of 2. So x cubed minus '
            '2 is also solvable by radicals.',
            duration=55,
        )
        self.ly.section_divider(2, 'Solvable by Radicals')

        title = self.ly.title('When Is a Polynomial Solvable by Radicals?')

        # Definition
        defn = MathTex(
            r'f \text{ solvable by radicals } \iff '
            r'\text{Split}(f) \subseteq E, \text{ E/F radical}',
            font_size=BODY_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed), run_time=NORMAL)
        self.wait(10)

        # Example 1
        self.play(FadeOut(boxed), run_time=FAST)
        ex1 = MathTex(
            r'x^2 - 2: \quad \text{Split} = \mathbb{Q}(\sqrt{2}) \text{ is radical } '
            r'\checkmark',
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex1, DOWN, anchor=title, buff=0.5)
        self.play(Write(ex1), run_time=NORMAL)
        self.wait(8)

        # Example 2
        self.play(FadeOut(ex1), run_time=FAST)
        ex2 = MathTex(
            r'x^3 - 2: \quad \text{Split} = \mathbb{Q}(\sqrt[3]{2}, \omega) '
            r'\text{ is radical } \checkmark',
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(ex2, DOWN, anchor=title, buff=0.5)
        self.play(Write(ex2), run_time=NORMAL)
        self.wait(10)
        self.ly.clear()

    def scene4_big_theorem(self):
        """The central theorem: solvable Galois group iff solvable by radicals."""
        self.add_subcaption(
            'Now the central theorem. A polynomial f with coefficients in '
            'a field F of characteristic zero is solvable by radicals if '
            'and only if the Galois group of its splitting field over F is '
            'a solvable group. This is the theorem that justifies the '
            'entire Galois theory program. The "only if" direction says: '
            'if you can solve by radicals, the Galois group must be '
            'solvable. The "if" direction says: if the Galois group is '
            'solvable, you can solve by radicals. This direction is '
            'harder to prove because you need to reverse-engineer the '
            'radical tower from the solvable group.',
            duration=75,
        )
        self.ly.section_divider(3, 'The Central Theorem')

        title = self.ly.title('Solvability by Radicals Theorem')

        # The big theorem box
        theorem = MathTex(
            r'f \text{ solvable by radicals } \iff '
            r'\text{Gal}(\text{Split}(f)/F) \text{ is solvable}',
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(theorem, color=ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed), run_time=SLOW)
        self.wait(14)

        # Three key parts
        parts = [
            Text('Only if: radical extension -> solvable Galois group (easier)',
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text('If: solvable Galois group -> radical extension (harder)',
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text('Characteristic zero required (avoids inseparable complications)',
                 font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(parts, start_from=boxed)
        self.wait(14)
        self.ly.clear()

    def scene5_why_radical_implies_solvable(self):
        """From radical extensions to solvable groups — the visual climax."""
        self.add_subcaption(
            'Let us see why the "only if" direction works. Suppose E over F '
            'is a radical extension, so we have a tower F equals K zero, '
            'K one, up to K n equals E, where each step adjoins alpha i '
            'with alpha i to the m i in K i minus one. When we pass to '
            'the splitting field and take Galois groups, the Fundamental '
            'Theorem gives us a reverse tower of groups: Gal of E over E '
            'is trivial, contained in Gal of E over K n minus one, '
            'contained in, all the way up to Gal of E over F. Each '
            'quotient is a cyclic group, because adjoining an m-th root '
            'in characteristic zero gives a cyclic Galois group. And a '
            'group with a tower of cyclic quotients is exactly a solvable '
            'group. This is the content of Video 218.',
            duration=80,
        )
        self.ly.section_divider(4, 'Why Radical Implies Solvable')

        title = self.ly.title('From Radical Extensions to Solvable Groups')

        # Field tower on the left
        left_head = Text('Field Tower', font_size=LABEL_SIZE,
                         color=PRIMARY, font=SANS)
        f_nodes = [
            MathTex(r'F = K_0', font_size=LABEL_SIZE, color=PRIMARY),
            MathTex(r'K_1', font_size=LABEL_SIZE, color=PRIMARY),
            MathTex(r'K_2', font_size=LABEL_SIZE, color=PRIMARY),
            MathTex(r'\cdots', font_size=LABEL_SIZE, color=PRIMARY),
            MathTex(r'K_n = E', font_size=LABEL_SIZE, color=PRIMARY),
        ]
        field_col = VGroup(*f_nodes).arrange(DOWN, buff=0.65)
        field_group = VGroup(left_head, field_col).arrange(DOWN, buff=0.3)

        # Group tower on the right (inclusion-reversed)
        right_head = Text('Galois Group Tower', font_size=LABEL_SIZE,
                          color=SECONDARY, font=SANS)
        g_nodes = [
            MathTex(r'G = \text{Gal}(E/F)', font_size=LABEL_SIZE, color=SECONDARY),
            MathTex(r'G_1 = \text{Gal}(E/K_1)', font_size=LABEL_SIZE, color=SECONDARY),
            MathTex(r'G_2 = \text{Gal}(E/K_2)', font_size=LABEL_SIZE, color=SECONDARY),
            MathTex(r'\cdots', font_size=LABEL_SIZE, color=SECONDARY),
            MathTex(r'\{e\}', font_size=LABEL_SIZE, color=SECONDARY),
        ]
        group_col = VGroup(*g_nodes).arrange(DOWN, buff=0.65)
        group_group = VGroup(right_head, group_col).arrange(DOWN, buff=0.3)

        # Place side by side
        diagram = VGroup(field_group, group_group).arrange(RIGHT, buff=2.5)
        ensure_fits(diagram, max_width=13.0, max_height=5.5)
        self.ly.center_in_content(diagram)

        # Animate field tower
        self.play(FadeIn(left_head), run_time=FAST)
        self.play(Write(field_col), run_time=NORMAL)
        self.wait(4)

        # Field tower edges
        f_edges = VGroup()
        for i in range(len(f_nodes) - 1):
            if i != 3 and (i + 1) != 3:
                f_edges.add(Line(
                    f_nodes[i].get_bottom(), f_nodes[i + 1].get_top(),
                    stroke_width=2, color=DIM,
                ))
        self.play(Create(f_edges), run_time=FAST)
        self.wait(3)

        # Animate group tower
        self.play(FadeIn(right_head), run_time=FAST)
        self.play(Write(group_col), run_time=NORMAL)
        self.wait(4)

        # Group tower edges
        g_edges = VGroup()
        for i in range(len(g_nodes) - 1):
            if i != 3 and (i + 1) != 3:
                g_edges.add(Line(
                    g_nodes[i].get_bottom(), g_nodes[i + 1].get_top(),
                    stroke_width=2, color=DIM,
                ))
        self.play(Create(g_edges), run_time=FAST)
        self.wait(3)

        # FTGT arrow connecting them
        ftgt_label = Text('FTGT', font_size=LABEL_SIZE, color=ACCENT, font=SANS)
        ftgt_label.move_to((field_group.get_right() + group_group.get_left()) / 2)
        arrow_l = Arrow(
            field_group.get_right() + RIGHT * 0.1,
            ftgt_label.get_left() + LEFT * 0.05,
            buff=0.05, stroke_width=3, color=ACCENT,
            max_tip_length_to_length_ratio=0.35,
        )
        arrow_r = Arrow(
            ftgt_label.get_right() + RIGHT * 0.05,
            group_group.get_left() + LEFT * 0.1,
            buff=0.05, stroke_width=3, color=ACCENT,
            max_tip_length_to_length_ratio=0.35,
        )
        self.play(GrowArrow(arrow_l), FadeIn(ftgt_label), run_time=NORMAL)
        self.play(GrowArrow(arrow_r), run_time=FAST)
        self.wait(6)

        # Cyclic quotient labels
        cyclic = MathTex(
            r'G_{i-1} / G_i \text{ is cyclic}',
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(cyclic, DOWN, anchor=diagram, buff=0.3)
        self.play(Write(cyclic), run_time=NORMAL)
        self.wait(4)

        # Key connection
        key = Text(
            'Tower with cyclic quotients = solvable group (Video 218)',
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(key, DOWN, anchor=cyclic, buff=0.4)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(6)
        self.wait(7)
        self.ly.clear()

    def scene6_quartic_example(self):
        """The quartic x^4 - 2 as a solvable-by-radicals example."""
        self.add_subcaption(
            'Let us see a concrete example. Consider x to the fourth '
            'minus 2. The roots are plus or minus the fourth root of 2, '
            'and plus or minus i times the fourth root of 2. The '
            'splitting field over Q has degree 8, namely Q of fourth '
            'root of 2, i. The Galois group is the dihedral group D 4 '
            'of order 8. From Video 218, D 4 is solvable: its derived '
            'series is D 4, then V 4, then trivial. Since D 4 is '
            'solvable, x to the fourth minus 2 is solvable by radicals.',
            duration=85,
        )
        self.ly.section_divider(5, 'Example: x^4 - 2')

        title = self.ly.title('A Quartic Solvable by Radicals')

        # The polynomial
        poly = MathTex(
            r'f(x) = x^4 - 2',
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(poly, DOWN, anchor=title, buff=0.5)
        self.play(Write(poly), run_time=NORMAL)
        self.wait(4)

        # Roots
        roots = MathTex(
            r'\text{Roots: } \pm \sqrt[4]{2},\ \pm i\sqrt[4]{2}',
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(roots, DOWN, anchor=poly, buff=0.4)
        self.play(Write(roots), run_time=NORMAL)
        self.wait(6)

        # Splitting field and Galois group
        self.play(FadeOut(poly), FadeOut(roots), run_time=FAST)
        info = MathTex(
            r'\text{Split} = \mathbb{Q}(\sqrt[4]{2}, i), \quad '
            r'[\text{Split} : \mathbb{Q}] = 8, \quad '
            r'\text{Gal} \cong D_4',
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(info, DOWN, anchor=title, buff=0.5)
        self.play(Write(info), run_time=NORMAL)
        self.wait(10)

        # Derived series of D_4
        self.play(FadeOut(info), run_time=FAST)
        series = MathTex(
            r'D_4 \triangleright V_4 \triangleright \{e\}',
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed = self.ly.formula_box(series, color=SECONDARY)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed), run_time=NORMAL)
        self.wait(6)

        # Quotients
        quotients = MathTex(
            r'D_4 / V_4 \cong \mathbb{Z}/2\mathbb{Z}, \quad '
            r'V_4 / \{e\} \cong V_4 \text{ (abelian)}',
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(quotients, DOWN, anchor=boxed, buff=0.4)
        self.play(Write(quotients), run_time=NORMAL)
        self.wait(8)

        # Conclusion
        conclusion = Text(
            'D_4 is solvable => x^4 - 2 is solvable by radicals!',
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(conclusion, DOWN, anchor=quotients, buff=0.4)
        self.play(FadeIn(conclusion, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(8)
        self.ly.clear()

    def scene7_quintic_teaser(self):
        """Teaser: the quintic and Abel-Ruffini."""
        self.add_subcaption(
            'Now the moment you have been waiting for. The symmetric group '
            'S 5, which is the Galois group of the general quintic '
            'polynomial, is not solvable. We saw in Video 218 that the '
            'derived series of S 5 is S 5, then A 5, then A 5 again. '
            'It never reaches the trivial group. So the general quintic '
            'is not solvable by radicals. This is the Abel-Ruffini '
            'theorem. But this is just the beginning of the story. The '
            'proof that S 5 is not solvable is beautiful, and there are '
            'specific quintics with smaller Galois groups that are '
            'solvable. We will explore all of this in the next video.',
            duration=65,
        )
        self.ly.section_divider(6, 'The Quintic')

        title = self.ly.title('The Quintic: A Teaser')

        # S_5 derived series FAILING
        series = MathTex(
            r'S_5 \triangleright A_5 = A_5 = A_5 = \cdots',
            font_size=HEADING_SIZE, color=RED,
        )
        boxed = self.ly.formula_box(series, color=RED)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed), run_time=NORMAL)
        self.wait(10)

        # Key fact
        fact = Text(
            'A_5 is simple: A_5\' = A_5, series never reaches {e}',
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(fact, DOWN, anchor=boxed, buff=0.4)
        self.play(FadeIn(fact, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(8)

        # Consequence
        consequence = Text(
            'S_5 is NOT solvable => general quintic NOT solvable by radicals',
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(consequence, DOWN, anchor=fact, buff=0.4)
        self.play(FadeIn(consequence, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(8)

        # Teaser for next video
        teaser = Text(
            'Next: the full Abel-Ruffini proof + which quintics ARE solvable',
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(teaser, DOWN, anchor=consequence, buff=0.4)
        self.play(FadeIn(teaser, shift=LEFT * 0.15), run_time=FAST)
        self.wait(7)
        self.ly.clear()

    def scene8_summary(self):
        """Summary and outro."""
        self.add_subcaption(
            'Let us recap. A radical extension is built by successively '
            'adjoining roots. A polynomial is solvable by radicals if its '
            'splitting field lives inside a radical extension. The '
            'central theorem: solvable by radicals if and only if the '
            'Galois group is solvable. The proof uses the FTGT to '
            'convert a radical tower into a group tower with cyclic '
            'quotients, which is exactly a solvable group. And the '
            'quintic fails because S 5 is not solvable. This is '
            'Galois\' immortal achievement.',
            duration=50,
        )
        self.ly.section_divider(7, 'Summary')

        title = self.ly.title('Key Takeaways')
        items = [
            Text('Radical extension: built by successively adjoining n-th roots',
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text('f solvable by radicals iff Split(f) is in a radical extension',
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            MathTex(
                r'f \text{ solvable by radicals } \iff '
                r'\text{Gal}(\text{Split}(f)/F) \text{ is solvable}',
                font_size=BODY_SIZE, color=ACCENT,
            ),
            Text('Proof: radical tower -> group tower with cyclic quotients (FTGT)',
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text('The quintic: S_5 not solvable -> general quintic not solvable',
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(16)
        self.wait(17)
        self.ly.clear()

        self.add_subcaption(
            'Thank you for watching! Next time: the insolvability of the quintic.',
            duration=6,
        )
        play_outro(self, 'Insolvability of the Quintic', 'Advanced Abstract Algebra')
