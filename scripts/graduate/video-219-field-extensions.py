"""
Video 219: Field Extensions — Advanced Abstract Algebra
Field extension definition, degree, algebraic vs transcendental,
minimal polynomial, tower law.

QUALITY RULES:
1. Max 5 visible elements per scene
2. LayoutEngine for ALL positioning
3. Progressive disclosure
4. Raw strings with single backslashes for LaTeX
5. ly.clear() between scenes
6. One subcaption per scene, self.wait(5-8) after content

Competitive analysis: Socratica (definition-first, Manim), Math Sorcerer
(whiteboard, proof-heavy), Michael Penn (whiteboard, fast-paced).
Our approach: intuition-first with visual inclusion diagrams, color-coded
algebraic vs transcendental, animated tower law proof.
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


class Video219_FieldExtensions(Scene):
    """Field Extensions: the gateway to Galois theory."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_degree()
        self.scene4_algebraic_vs_transcendental()
        self.scene5_minimal_polynomial()
        self.scene6_tower_law()
        self.scene7_examples()
        self.scene8_summary()

    def scene1_hook(self):
        """Hook — fields inside fields."""
        self.add_subcaption(
            "The rational numbers live inside the reals, and the reals live "
            "inside the complex numbers. Each inclusion is an example of a "
            "field extension, the fundamental object that opens the door to "
            "Galois theory. Today we define field extensions precisely, "
            "classify their elements as algebraic or transcendental, "
            "introduce the degree and minimal polynomial, and prove the "
            "tower law that governs how degrees compose.",
            duration=24,
        )
        play_intro(self, "Field Extensions", "Advanced Abstract Algebra")

        title = self.ly.title("Fields Inside Fields")
        items = [
            Text("Q (rationals) inside R (reals) inside C (complex)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Field extensions capture how fields grow",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Foundation for Galois theory",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(7)
        self.ly.clear()

    def scene2_definition(self):
        """Formal definition of a field extension."""
        self.add_subcaption(
            "A field extension is a pair of fields where one contains "
            "the other. Formally, if K is a field and E is a larger field "
            "containing K, we call E over K a field extension and write "
            "E over K or E colon K. The smaller field K is called the "
            "base field, and E is called the extension field. Every field "
            "extension is a vector space over the base field.",
            duration=24,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("Field Extension")

        # Visual: nested circles representing K inside E
        circle_k = Circle(radius=1.0, color=SECONDARY, stroke_width=2)
        circle_e = Circle(radius=2.0, color=PRIMARY, stroke_width=2)
        label_k = Text("K", font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        label_e = Text("E", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        label_k.move_to(circle_k.get_center())
        label_e.move_to(ORIGIN + UP * 1.6 + LEFT * 1.3)
        circles = VGroup(circle_e, circle_k, label_e, label_k)

        self.ly.safe_place(circles, DOWN, anchor=title, buff=0.5)
        self.play(Create(circle_e), run_time=NORMAL)
        self.play(Create(circle_k), run_time=NORMAL)
        self.play(Write(label_e), Write(label_k), run_time=FAST)
        self.wait(2)

        # Formal definition using K subseteq E
        defn = MathTex(
            r"K \subseteq E",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(defn, DOWN, anchor=circles, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(2)

        notation = Text(
            "E/K means E is an extension of K",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(notation, DOWN, anchor=defn, buff=0.5)
        self.play(FadeIn(notation, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene3_degree(self):
        """Degree of a field extension as a vector space dimension."""
        self.add_subcaption(
            "Since a field extension E over K is a vector space over K, "
            "we can ask about its dimension. The degree of the extension, "
            "written with square brackets E colon K, is the dimension of E "
            "as a vector space over K. If this dimension is finite, we call "
            "E a finite extension of K. For example, the complex numbers "
            "are a degree two extension of the reals, with basis one and i. "
            "The reals over the rationals have infinite degree.",
            duration=26,
        )
        self.ly.section_divider(2, "Degree of an Extension")

        title = self.ly.title("The Degree")

        # Definition
        formula = MathTex(
            r"[E : K] = \dim_K(E)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_formula = self.ly.formula_box(formula, color=PRIMARY)
        self.ly.safe_place(boxed_formula, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_formula), run_time=NORMAL)
        self.wait(3)

        # Examples
        examples = [
            MathTex(r"[\mathbb{C} : \mathbb{R}] = 2", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"[\mathbb{R} : \mathbb{Q}] = \infty", font_size=BODY_SIZE, color=RED),
        ]
        self.ly.progressive_reveal(examples, start_from=boxed_formula)
        self.wait(3)

        # Basis for C/R
        basis = MathTex(
            r"\text{Basis of } \mathbb{C}/\mathbb{R}{: } \{1,\, i\}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(basis, DOWN, anchor=examples[-1], buff=0.4)
        self.play(FadeIn(basis, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene4_algebraic_vs_transcendental(self):
        """Algebraic and transcendental elements."""
        self.add_subcaption(
            "Given a field extension E over K, an element alpha in E is "
            "called algebraic over K if it satisfies some nonzero polynomial "
            "with coefficients in K. Otherwise, alpha is called transcendental "
            "over K. The classic example: the square root of 2 is algebraic "
            "over the rationals because it satisfies x squared minus 2 equals "
            "zero. But pi and e are transcendental over Q, a deep result of "
            "Lindemann and Hermite.",
            duration=26,
        )
        self.ly.section_divider(3, "Algebraic vs Transcendental")

        title = self.ly.title("Two Kinds of Elements")

        # Algebraic
        alg_label = Text("Algebraic over K:", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(alg_label, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(alg_label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        alg_def = MathTex(
            r"\exists\, f \in K[x],\; f \neq 0 \;\colon\; f(\alpha) = 0",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(alg_def, DOWN, anchor=alg_label, buff=0.4)
        self.play(Write(alg_def), run_time=NORMAL)
        self.wait(3)

        # Transcendental
        trans_label = Text("Transcendental over K:", font_size=BODY_SIZE, color=RED, font=SANS)
        trans_def = Text(
            "No nonzero polynomial in K[x] vanishes at alpha",
            font_size=LABEL_SIZE, color=RED, font=SANS,
        )
        trans_group = VGroup(trans_label, trans_def).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeOut(alg_label), FadeOut(alg_def), run_time=FAST)
        self.ly.safe_place(trans_group, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(trans_group), run_time=NORMAL)
        self.wait(3)

        # Concrete examples
        self.play(FadeOut(trans_group), run_time=FAST)
        ex_title = Text("Examples over Q:", font_size=HEADING_SIZE, color=WHITE, font=SANS)
        self.ly.safe_place(ex_title, DOWN, anchor=title, buff=0.5)
        self.play(Write(ex_title), run_time=FAST)

        ex_items = [
            Text("sqrt(2) is algebraic: x^2 - 2 = 0",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("pi and e are transcendental (Lindemann, Hermite)",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(ex_items, start_from=ex_title)
        self.wait(5)
        self.ly.clear()

    def scene5_minimal_polynomial(self):
        """Minimal polynomial: the unique monic irreducible."""
        self.add_subcaption(
            "When alpha is algebraic over K, there are many polynomials "
            "in K of x that vanish at alpha. Among all such polynomials, "
            "there is a unique monic polynomial of smallest degree called "
            "the minimal polynomial of alpha over K. This polynomial is "
            "always irreducible over K. Furthermore, a polynomial in K of x "
            "vanishes at alpha if and only if the minimal polynomial divides "
            "it. The degree of the minimal polynomial equals the degree of "
            "the extension K of alpha over K.",
            duration=28,
        )
        self.ly.section_divider(4, "Minimal Polynomial")

        title = self.ly.title("The Minimal Polynomial")

        defn = MathTex(
            r"m_{\alpha,K}(x) = \text{monic poly of smallest degree with } m(\alpha) = 0",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_def = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.safe_place(boxed_def, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_def), run_time=NORMAL)
        self.wait(3)

        # Key properties
        props = [
            Text("Unique and irreducible over K",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("f(alpha) = 0 iff m_alpha divides f(x)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(props, start_from=boxed_def)
        self.wait(4)

        # Key equality
        self.play(FadeOut(props[0]), run_time=FAST)
        degree_eq = MathTex(
            r"[K(\alpha) : K] = \deg(m_{\alpha,K})",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_eq = self.ly.formula_box(degree_eq, color=PRIMARY)
        self.ly.safe_place(boxed_eq, DOWN, anchor=boxed_def, buff=0.5)
        self.play(
            FadeOut(props[1]),
            FadeIn(boxed_eq),
            run_time=NORMAL,
        )
        self.wait(5)
        self.ly.clear()

    def scene6_tower_law(self):
        """Tower law: degrees multiply in a tower of extensions."""
        self.add_subcaption(
            "Suppose we have a tower of field extensions: F inside K "
            "inside E. The tower law states that the degree of E over F "
            "equals the degree of E over K times the degree of K over F. "
            "The proof is beautiful: a basis for E over K has degree of E "
            "over K elements, and each of those multiplies with a basis of K "
            "over F. This gives a basis for E over F of size equal to the "
            "product. This multiplication of degrees is essential for "
            "computing extension degrees in practice.",
            duration=28,
        )
        self.ly.section_divider(5, "Tower Law")

        title = self.ly.title("The Tower Law")

        # Tower diagram: F -> K -> E
        f_circle = Circle(radius=0.5, color=DIM, stroke_width=2)
        k_circle = Circle(radius=1.2, color=SECONDARY, stroke_width=2)
        e_circle = Circle(radius=1.9, color=PRIMARY, stroke_width=2)
        f_label = Text("F", font_size=LABEL_SIZE, color=DIM, font=SANS).move_to(ORIGIN)
        k_label = Text("K", font_size=LABEL_SIZE, color=SECONDARY, font=SANS).move_to(UP * 0.35 + LEFT * 0.8)
        e_label = Text("E", font_size=LABEL_SIZE, color=PRIMARY, font=SANS).move_to(UP * 0.7 + LEFT * 1.35)
        tower = VGroup(e_circle, k_circle, f_circle, e_label, k_label, f_label)

        self.ly.safe_place(tower, DOWN, anchor=title, buff=0.5)
        self.play(
            Create(f_circle), Create(k_circle), Create(e_circle),
            Write(f_label), Write(k_label), Write(e_label),
            run_time=NORMAL,
        )
        self.wait(2)

        # Tower law formula
        tower_law = MathTex(
            r"[E : F] = [E : K] \cdot [K : F]",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_law = self.ly.formula_box(tower_law, color=PRIMARY)
        self.ly.safe_place(boxed_law, DOWN, anchor=tower, buff=0.5)
        self.play(FadeIn(boxed_law), run_time=NORMAL)
        self.wait(4)

        # Example computation
        self.play(FadeOut(tower), run_time=FAST)
        ex = Text(
            "Example: [Q(sqrt(2), i) : Q] = [Q(sqrt(2), i) : Q(sqrt(2))] x 2 = 4",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(ex, DOWN, anchor=boxed_law, buff=0.4)
        self.play(FadeIn(ex, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene7_examples(self):
        """Worked examples: Q(sqrt(2)), Q(sqrt(2), sqrt(3)), Q(i)."""
        self.add_subcaption(
            "Let us work through concrete examples. First, Q of sqrt 2 "
            "is a degree 2 extension of Q because the minimal polynomial "
            "of sqrt 2 over Q is x squared minus 2. Next, Q of sqrt 2 "
            "comma sqrt 3 has degree 4 over Q. By the tower law, going "
            "through Q of sqrt 2, the first step has degree 2 and "
            "sqrt 3 satisfies x squared minus 3 over Q of sqrt 2, giving "
            "another degree 2, for a total of 4.",
            duration=28,
        )
        self.ly.section_divider(6, "Worked Examples")

        title = self.ly.title("Computing Degrees")

        # Example 1
        ex1_title = Text("Q(sqrt(2)) / Q:", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        self.ly.safe_place(ex1_title, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(ex1_title, shift=LEFT * 0.15), run_time=FAST)

        ex1_poly = MathTex(
            r"m_{\sqrt{2},\mathbb{Q}}(x) = x^2 - 2, \quad [\mathbb{Q}(\sqrt{2}) : \mathbb{Q}] = 2",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex1_poly, DOWN, anchor=ex1_title, buff=0.4)
        self.play(Write(ex1_poly), run_time=NORMAL)
        self.wait(4)

        # Example 2
        self.play(FadeOut(ex1_title), FadeOut(ex1_poly), run_time=FAST)
        ex2_title = Text("Q(sqrt(2), sqrt(3)) / Q:", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        self.ly.safe_place(ex2_title, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(ex2_title, shift=LEFT * 0.15), run_time=FAST)

        ex2_step = MathTex(
            r"[\mathbb{Q}(\sqrt{2},\sqrt{3}) : \mathbb{Q}] "
            r"= [\mathbb{Q}(\sqrt{2},\sqrt{3}) : \mathbb{Q}(\sqrt{2})] "
            r"\cdot [\mathbb{Q}(\sqrt{2}) : \mathbb{Q}]",
            font_size=LABEL_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex2_step, DOWN, anchor=ex2_title, buff=0.4)
        self.play(Write(ex2_step), run_time=NORMAL)
        self.wait(3)

        ex2_result = MathTex(
            r"= 2 \cdot 2 = 4",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(ex2_result, DOWN, anchor=ex2_step, buff=0.4)
        self.play(Write(ex2_result), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene8_summary(self):
        """Summary and outro."""
        self.add_subcaption(
            "Field extensions are the fundamental objects that bridge "
            "field theory and Galois theory. A field extension E over K "
            "is simply a pair of fields where K sits inside E. The degree "
            "of an extension is the dimension of E as a vector space over "
            "K. Elements are classified as algebraic or transcendental, and "
            "algebraic elements have a unique minimal polynomial whose degree "
            "equals the extension degree. The tower law tells us that degrees "
            "multiply in chains of extensions. In the next video we will "
            "dive deeper into algebraic extensions. Thank you for watching!",
            duration=30,
        )
        self.ly.section_divider(7, "Summary")

        title = self.ly.title("Key Takeaways")
        items = [
            Text("E/K: K is a subfield of E",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("[E:K] = dim_K(E) — the degree of the extension",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Algebraic: satisfies a polynomial; transcendental: does not",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3)

        # Additional takeaway (replace oldest to stay in budget)
        extra = Text(
            "Tower law: [E:F] = [E:K] x [K:F] for F <= K <= E",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.progressive_reveal([extra], start_from=items[-1])
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "Thank you for watching! In the next video we will study "
            "algebraic extensions in more depth.",
            duration=10,
        )
        play_outro(self, "Algebraic Extensions", "Advanced Abstract Algebra")
