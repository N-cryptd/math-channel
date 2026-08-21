"""
Video 223: Fundamental Theorem of Galois Theory - Advanced Abstract Algebra
Galois extensions, the FTGT statement, subgroup-field correspondence,
lattice visualization, degree formula, normal subgroups, proof sketch.

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


class Video223_FundamentalTheoremGalois(Scene):
    """The Fundamental Theorem of Galois Theory: subgroups <-> intermediate fields."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_galois_extensions()
        self.scene3_running_example()
        self.scene4_ftgt_statement()
        self.scene5_lattice_visual()
        self.scene6_degree_formula_normal()
        self.scene7_proof_sketch()
        self.scene8_summary()

    def scene1_hook(self):
        """Hook - the perfect correspondence."""
        self.add_subcaption(
            'Last time we defined Galois groups and fixed fields, and I promised '
            'you the big theorem. Here it is: for a Galois extension, the '
            'subgroups of the Galois group are in perfect one-to-one '
            'correspondence with the intermediate fields. Not just a bijection. '
            'The correspondence preserves structure, reverses inclusion, and '
            'tells you when subextensions are Galois. This is the Fundamental '
            'Theorem of Galois Theory.',
            duration=30,
        )
        play_intro(self, 'Fundamental Theorem of Galois Theory', 'Advanced Abstract Algebra')

        title = self.ly.title('The Perfect Correspondence')
        items = [
            Text('Subgroups of Gal(E/F) correspond to intermediate fields',
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text('The correspondence is inclusion-reversing, structure-preserving',
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(7)
        self.ly.clear()

    def scene2_galois_extensions(self):
        """Galois Extensions - definition and equivalent conditions."""
        self.add_subcaption(
            'Before stating the theorem, we need the definition of a Galois '
            'extension. A finite extension E over F is Galois if it satisfies '
            'any of three equivalent conditions: the fixed field of the Galois '
            'group is exactly F; the number of automorphisms equals the degree '
            'of the extension; or E is the splitting field of a separable '
            'polynomial over F. The key idea: a Galois extension has enough '
            'automorphisms.',
            duration=34,
        )
        self.ly.section_divider(1, 'Galois Extensions')

        title = self.ly.title('Galois Extensions')

        # Main definition
        defn = MathTex(
            r'E/F \text{ is Galois} \iff \text{Fix}(\text{Gal}(E/F)) = F',
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_defn = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.safe_place(boxed_defn, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_defn), run_time=NORMAL)
        self.wait(4)

        # Equivalent condition 1
        self.play(FadeOut(boxed_defn), run_time=FAST)
        eq1 = MathTex(
            r'\text{Also: } |\text{Gal}(E/F)| = [E : F]',
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed_eq1 = self.ly.formula_box(eq1, color=SECONDARY)
        self.ly.safe_place(boxed_eq1, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_eq1), run_time=NORMAL)
        self.wait(3)

        # Equivalent condition 2
        self.play(FadeOut(boxed_eq1), run_time=FAST)
        eq2 = Text(
            'Or: E is the splitting field of a separable polynomial over F',
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(eq2, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(eq2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        # Key insight
        note = Text(
            'Key idea: a Galois extension has ENOUGH automorphisms',
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=eq2, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene3_running_example(self):
        """Running example: Q(sqrt2, sqrt3)/Q and its Galois group."""
        self.add_subcaption(
            'Let us set up our running example. Consider Q adjoin the square '
            'roots of 2 and 3, over Q. This is a degree 4 extension with basis '
            '1, root 2, root 3, root 6. The automorphisms are determined by '
            'where they send root 2 and root 3. Each root can go to plus or '
            'minus itself, giving four maps: the identity, sigma sending root 2 '
            'to minus root 2, tau sending root 3 to minus root 3, and sigma tau '
            'flipping both. The Galois group is the Klein four group V4.',
            duration=48,
        )
        self.ly.section_divider(2, 'Running Example')

        title = self.ly.title('Gal(Q(sqrt2, sqrt3) / Q)')

        # The extension and its degree
        ext = MathTex(
            r'E = \mathbb{Q}(\sqrt{2}, \sqrt{3}), \quad [E : \mathbb{Q}] = 4',
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ext, DOWN, anchor=title, buff=0.5)
        self.play(Write(ext), run_time=NORMAL)
        self.wait(3)

        # Basis
        self.play(FadeOut(ext), run_time=FAST)
        basis = MathTex(
            r'\text{Basis: } 1,\ \sqrt{2},\ \sqrt{3},\ \sqrt{6}',
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(basis, DOWN, anchor=title, buff=0.5)
        self.play(Write(basis), run_time=NORMAL)
        self.wait(3)

        # Four automorphisms, shown two at a time
        self.play(FadeOut(basis), run_time=FAST)
        auto_title = Text(
            'Four automorphisms (choice of signs on the two roots):',
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(auto_title, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(auto_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(2)

        id_auto = MathTex(
            r'\text{id}: \sqrt{2} \mapsto \sqrt{2},\ \sqrt{3} \mapsto \sqrt{3}',
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(id_auto, DOWN, anchor=auto_title, buff=0.3)
        self.play(Write(id_auto), run_time=FAST)
        self.wait(2)

        sigma_auto = MathTex(
            r'\sigma: \sqrt{2} \mapsto -\sqrt{2},\ \sqrt{3} \mapsto \sqrt{3}',
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(sigma_auto, DOWN, anchor=id_auto, buff=0.25)
        self.play(Write(sigma_auto), run_time=FAST)
        self.wait(2)

        self.play(FadeOut(id_auto), run_time=FAST)

        tau_auto = MathTex(
            r'\tau: \sqrt{2} \mapsto \sqrt{2},\ \sqrt{3} \mapsto -\sqrt{3}',
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(tau_auto, DOWN, anchor=auto_title, buff=0.3)
        self.play(Write(tau_auto), run_time=FAST)
        self.wait(2)

        self.play(FadeOut(sigma_auto), run_time=FAST)

        st_auto = MathTex(
            r'\sigma\tau: \sqrt{2} \mapsto -\sqrt{2},\ \sqrt{3} \mapsto -\sqrt{3}',
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(st_auto, DOWN, anchor=tau_auto, buff=0.25)
        self.play(Write(st_auto), run_time=FAST)
        self.wait(3)

        # Result
        self.play(
            FadeOut(auto_title), FadeOut(tau_auto), FadeOut(st_auto),
            run_time=FAST,
        )
        result = MathTex(
            r'\text{Gal}(E/\mathbb{Q}) \cong V_4 \text{ (Klein four)}',
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_result = self.ly.formula_box(result, color=ACCENT)
        self.ly.safe_place(boxed_result, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_result), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene4_ftgt_statement(self):
        """The Fundamental Theorem - formal statement."""
        self.add_subcaption(
            'Here is the Fundamental Theorem. Let E over F be a finite Galois '
            'extension with Galois group G. Then there is a bijection between '
            'the subgroups H of G and the intermediate fields K between F and E. '
            'The maps are: H maps to the fixed field of H, and K maps to Gal of '
            'E over K. The bijection reverses inclusion. The degree of K over F '
            'equals the index of the corresponding subgroup. And normal '
            'subgroups correspond exactly to Galois subextensions.',
            duration=40,
        )
        self.ly.section_divider(3, 'The Fundamental Theorem')

        title = self.ly.title('The Fundamental Theorem of Galois Theory')

        # Bijection statement
        stmt = MathTex(
            r'\{\text{subgroups } H \subseteq G\}'
            r'\ \longleftrightarrow\ '
            r'\{\text{intermediate fields } K\}',
            font_size=BODY_SIZE, color=PRIMARY,
        )
        boxed_stmt = self.ly.formula_box(stmt, color=PRIMARY)
        self.ly.safe_place(boxed_stmt, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_stmt), run_time=NORMAL)
        self.wait(4)

        # The two maps
        self.play(FadeOut(boxed_stmt), run_time=FAST)
        maps = MathTex(
            r'H \longmapsto E^H \text{ (fixed field)},'
            r'\quad K \longmapsto \text{Gal}(E/K)',
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(maps, DOWN, anchor=title, buff=0.5)
        self.play(Write(maps), run_time=NORMAL)
        self.wait(4)

        # Properties
        self.play(FadeOut(maps), run_time=FAST)
        props = [
            MathTex(
                r'H_1 \subseteq H_2 \implies E^{H_2} \subseteq E^{H_1}'
                r'\ \text{(inclusion-reversing)}',
                font_size=BODY_SIZE, color=SECONDARY,
            ),
            MathTex(
                r'[K : F] = [G : H] \text{ (degree formula)}',
                font_size=BODY_SIZE, color=ACCENT,
            ),
            MathTex(
                r'H \trianglelefteq G \iff K/F \text{ is Galois}',
                font_size=BODY_SIZE, color=RED,
            ),
        ]
        self.ly.progressive_reveal(props, start_from=title)
        self.wait(5)
        self.ly.clear()

    def scene5_lattice_visual(self):
        """The lattice - visual climax of the video."""
        self.add_subcaption(
            'The best way to see the correspondence is with a lattice. On the '
            'left, the subgroups of V4, ordered by inclusion, with V4 at the '
            'bottom and the trivial subgroup at the top. On the right, the '
            'intermediate fields. Watch how the correspondence connects them. '
            'The trivial subgroup fixes everything, so it corresponds to the '
            'full field E at the top. V4 itself fixes only Q, so it sits at the '
            'bottom. Each subgroup of order 2 corresponds to a quadratic '
            'intermediate field. And every arrow goes both ways. This is a '
            'genuine bijection.',
            duration=48,
        )
        self.ly.section_divider(4, 'The Lattice')

        title = self.ly.title('Subgroup-Field Lattice')

        # Column headers
        left_head = Text('Subgroups of V4', font_size=LABEL_SIZE,
                         color=PRIMARY, font=SANS)
        right_head = Text('Intermediate fields', font_size=LABEL_SIZE,
                          color=SECONDARY, font=SANS)

        # Left lattice nodes (bottom to top: V4, order-2 subgroups, {e})
        n_e = MathTex(r'\{e\}', font_size=LABEL_SIZE, color=PRIMARY)
        n_tau = MathTex(r'\langle\tau\rangle', font_size=LABEL_SIZE, color=PRIMARY)
        n_sig = MathTex(r'\langle\sigma\rangle', font_size=LABEL_SIZE, color=PRIMARY)
        n_st = MathTex(r'\langle\sigma\tau\rangle', font_size=LABEL_SIZE, color=PRIMARY)
        n_v4 = MathTex(r'V_4', font_size=LABEL_SIZE, color=PRIMARY)

        # Right lattice nodes (bottom to top: Q, quadratics, E)
        f_q = MathTex(r'\mathbb{Q}', font_size=LABEL_SIZE, color=SECONDARY)
        f_q2 = MathTex(r'\mathbb{Q}(\sqrt{2})', font_size=LABEL_SIZE, color=SECONDARY)
        f_q3 = MathTex(r'\mathbb{Q}(\sqrt{3})', font_size=LABEL_SIZE, color=SECONDARY)
        f_q6 = MathTex(r'\mathbb{Q}(\sqrt{6})', font_size=LABEL_SIZE, color=SECONDARY)
        f_e = MathTex(r'E', font_size=LABEL_SIZE, color=SECONDARY)

        # Pair rows so matching pairs sit at the same height:
        # <tau> <-> Q(sqrt2), <sigma> <-> Q(sqrt3), <sigmatau> <-> Q(sqrt6)
        left_mid = VGroup(n_tau, n_sig, n_st).arrange(RIGHT, buff=1.1)
        right_mid = VGroup(f_q2, f_q3, f_q6).arrange(RIGHT, buff=1.1)
        left_col = VGroup(n_e, left_mid, n_v4).arrange(DOWN, buff=1.1)
        right_col = VGroup(f_e, right_mid, f_q).arrange(DOWN, buff=1.1)

        lattice = VGroup(left_col, right_col).arrange(RIGHT, buff=2.2)
        heads = VGroup(left_head, right_head).arrange(RIGHT, buff=2.2)
        heads.align_to(lattice, UP)
        heads.shift(DOWN * 0.7)
        diagram = VGroup(heads, lattice).arrange(DOWN, buff=0.4)
        ensure_fits(diagram, max_width=13.5, max_height=5.6)
        self.ly.center_in_content(diagram)
        self.play(FadeIn(heads), run_time=FAST)
        self.play(Write(left_col), run_time=NORMAL)
        self.play(Write(right_col), run_time=NORMAL)
        self.wait(2)

        # Lattice edges (inclusion lines within each column)
        edges = VGroup()
        for sub in (n_tau, n_sig, n_st):
            edges.add(Line(n_v4.get_top(), sub.get_bottom(),
                           stroke_width=2, color=DIM))
        for sub in (n_tau, n_sig, n_st):
            edges.add(Line(sub.get_top(), n_e.get_bottom(),
                           stroke_width=2, color=DIM))
        for fld in (f_q2, f_q3, f_q6):
            edges.add(Line(f_q.get_top(), fld.get_bottom(),
                           stroke_width=2, color=DIM))
        for fld in (f_q2, f_q3, f_q6):
            edges.add(Line(fld.get_top(), f_e.get_bottom(),
                           stroke_width=2, color=DIM))
        self.play(Create(edges), run_time=NORMAL)
        self.wait(2)

        # Correspondence arrows (pairs at equal height)
        pairs = [
            (n_v4, f_q),
            (n_tau, f_q2),
            (n_sig, f_q3),
            (n_st, f_q6),
            (n_e, f_e),
        ]
        arrow_list = []
        for left_node, right_node in pairs:
            start = left_node.get_right() + RIGHT * 0.1
            end = right_node.get_left() + LEFT * 0.1
            arrow_list.append(
                Arrow(start, end, buff=0.05, stroke_width=3,
                      color=ACCENT, max_tip_length_to_length_ratio=0.35))
        self.play(GrowArrow(arrow_list[0]), run_time=FAST)
        self.wait(1)
        self.play(GrowArrow(arrow_list[1]), GrowArrow(arrow_list[2]),
                  GrowArrow(arrow_list[3]), run_time=NORMAL)
        self.wait(1)
        self.play(GrowArrow(arrow_list[4]), run_time=FAST)
        self.wait(2)

        # Emphasize a pair: <tau> fixes sqrt2, so it pairs with Q(sqrt2)
        highlight = Text(
            '<tau> fixes sqrt2 exactly -> pairs with Q(sqrt2)',
            font_size=LABEL_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(highlight, DOWN, anchor=diagram, buff=0.2)
        self.play(
            FadeIn(highlight, shift=LEFT * 0.15),
            Indicate(n_tau, color=ACCENT),
            Indicate(f_q2, color=ACCENT),
            run_time=NORMAL,
        )
        self.wait(4)
        self.ly.clear()

    def scene6_degree_formula_normal(self):
        """Degree formula and normal subgroups."""
        self.add_subcaption(
            'Two crucial properties. First, the degree formula: the degree of '
            'the intermediate field K over F equals the index of the '
            'corresponding subgroup H in G. In our example, Q of root 2 has '
            'degree 2 over Q, and the subgroup generated by tau has index 2 in '
            'V4. Check it on the lattice. Second, normal subgroups correspond '
            'to Galois subextensions: H is normal in G if and only if the fixed '
            'field of H is Galois over F. Since V4 is abelian, every subgroup '
            'is normal, so every intermediate field is Galois over Q.',
            duration=44,
        )
        self.ly.section_divider(5, 'Key Properties')

        title = self.ly.title('Degree Formula and Normal Subgroups')

        # Degree formula
        formula = MathTex(
            r'[E^H : F] = [G : H]',
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_formula = self.ly.formula_box(formula, color=ACCENT)
        self.ly.safe_place(boxed_formula, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_formula), run_time=NORMAL)
        self.wait(4)

        # Worked example
        example = MathTex(
            r'[\mathbb{Q}(\sqrt{2}) : \mathbb{Q}] = 2 = [V_4 : \langle\tau\rangle]',
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(example, DOWN, anchor=boxed_formula, buff=0.4)
        self.play(Write(example), run_time=NORMAL)
        self.wait(4)

        # Normal subgroups
        self.play(FadeOut(boxed_formula), FadeOut(example), run_time=FAST)
        normal_stmt = MathTex(
            r'H \trianglelefteq G \iff E^H / F \text{ is Galois}',
            font_size=HEADING_SIZE, color=RED,
        )
        boxed_normal = self.ly.formula_box(normal_stmt, color=RED)
        self.ly.safe_place(boxed_normal, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_normal), run_time=NORMAL)
        self.wait(4)

        note = Text(
            'V4 is abelian: all subgroups normal, all subextensions Galois',
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=boxed_normal, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene7_proof_sketch(self):
        """Proof sketch - three key ideas."""
        self.add_subcaption(
            'Why does this work? The proof has three key ideas. First, for any '
            'intermediate field K, the order of Gal of E over K is at most the '
            'degree of E over K, because each automorphism is determined by '
            'where it sends the generators, and each generator has only '
            'finitely many possible images. Second, for a Galois extension, '
            'equality holds: enough automorphisms exist. Third, combining '
            'equality with the tower law gives the bijection and the degree '
            'formula. The inclusion-reversing property is intuitive: a larger '
            'subgroup fixes fewer elements, hence a smaller field.',
            duration=46,
        )
        self.ly.section_divider(6, 'Proof Sketch')

        title = self.ly.title('Why It Works')

        steps = [
            MathTex(
                r'|\text{Gal}(E/K)| \leq [E : K]',
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            MathTex(
                r'\text{Galois: } |\text{Gal}(E/K)| = [E : K]'
                r'\ \text{(enough automorphisms)}',
                font_size=BODY_SIZE, color=SECONDARY,
            ),
            MathTex(
                r'\text{Tower law} \implies \text{bijection} + [K:F] = [G:H]',
                font_size=BODY_SIZE, color=ACCENT,
            ),
        ]
        self.ly.progressive_reveal(steps, start_from=title)
        self.wait(4)

        # Key insight
        insight = Text(
            'Larger subgroup -> fixes fewer elements -> smaller field',
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=steps[-1], buff=0.4)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene8_summary(self):
        """Summary and outro."""
        self.add_subcaption(
            'Let us recap. A Galois extension has enough automorphisms: its '
            'fixed field is exactly the base field. The Fundamental Theorem '
            'gives a perfect bijection between subgroups of the Galois group '
            'and intermediate fields. The correspondence reverses inclusion, '
            'tracks degrees through the index formula, and pairs normal '
            'subgroups with Galois subextensions. Keep the lattice picture in '
            'mind: it encodes the entire correspondence. Next time, we use the '
            'Fundamental Theorem to attack solvability by radicals.',
            duration=40,
        )
        self.ly.section_divider(7, 'Summary')

        title = self.ly.title('Key Takeaways')
        items = [
            MathTex(
                r'E/F \text{ Galois} \iff \text{Fix}(\text{Gal}(E/F)) = F',
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            MathTex(
                r'\text{FTGT: subgroups } H \longleftrightarrow \text{fields } K',
                font_size=BODY_SIZE, color=SECONDARY,
            ),
            MathTex(
                r'[E^H : F] = [G : H], \quad H \trianglelefteq G \iff E^H/F \text{ Galois}',
                font_size=BODY_SIZE, color=ACCENT,
            ),
            Text('The lattice diagram encodes the whole correspondence',
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            'Thank you for watching! Next time: solvability by radicals.',
            duration=6,
        )
        play_outro(self, 'Solvability by Radicals', 'Advanced Abstract Algebra')
