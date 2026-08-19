"""
Video 220: Algebraic Extensions — Advanced Abstract Algebra
Deep dive into algebraic extensions: finite implies algebraic,
simple extensions, finitely generated algebraic extensions, sum/product
closure, algebraic numbers, and algebraic closure.

QUALITY RULES:
1. Max 5 visible elements per scene
2. LayoutEngine for ALL positioning
3. Progressive disclosure
4. Raw strings with single backslashes for LaTeX
5. ly.clear() between scenes
6. One subcaption per scene, self.wait(3-5) after content

Competitive analysis: Positioned as the "missing foundation" for
popular Galois theory videos (Mathemaniac 549K, Aleph 0 314K).
Builds on Video 219 (Field Extensions).
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


class Video220_AlgebraicExtensions(Scene):
    """Algebraic Extensions: finite, simple, and algebraic closures."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_finite_implies_algebraic()
        self.scene4_simple_extensions()
        self.scene5_finitely_generated()
        self.scene6_sum_product()
        self.scene7_algebraic_numbers()
        self.scene8_algebraic_closure()
        self.scene9_closure_examples()
        self.scene10_summary()

    def scene1_hook(self):
        """Hook — from field extensions to algebraic extensions."""
        self.add_subcaption(
            "In the last video we saw that some elements of a field extension "
            "satisfy polynomials over the base field and some do not. What "
            "happens when every single element is algebraic? That is an "
            "algebraic extension, the most important type in all of Galois theory.",
            duration=22,
        )
        play_intro(self, "Algebraic Extensions", "Advanced Abstract Algebra")

        title = self.ly.title("When Every Element is Algebraic")
        items = [
            Text("Last time: some elements algebraic, some transcendental",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Now: what if ALL elements are algebraic?",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("These algebraic extensions power Galois theory",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)
        self.ly.clear()

    def scene2_definition(self):
        """Formal definition of algebraic extension."""
        self.add_subcaption(
            "A field extension E over F is called algebraic if every "
            "element alpha of E is algebraic over F. The first key result "
            "is that every finite extension is automatically algebraic. "
            "This is a one-way implication: algebraic does not always "
            "mean finite.",
            duration=22,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("Algebraic Extension")

        defn = MathTex(
            r"E/F \text{ is algebraic } \iff \forall\, \alpha \in E,\; "
            r"\alpha \text{ is algebraic over } F",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        boxed_def = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.safe_place(boxed_def, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_def), run_time=NORMAL)
        self.wait(3)

        # Key implication
        imp = MathTex(
            r"\text{Finite} \implies \text{Algebraic}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(imp, DOWN, anchor=boxed_def, buff=0.5)
        self.play(Write(imp), run_time=NORMAL)
        self.wait(4)

        # But not conversely
        note = Text(
            "But algebraic does not imply finite!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=imp, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene3_finite_implies_algebraic(self):
        """Proof that finite extension implies algebraic."""
        self.add_subcaption(
            "Why is every finite extension algebraic? Let E over F have "
            "degree n. Take any element alpha in E. The n plus one elements "
            "one, alpha, alpha squared, up to alpha to the n must be linearly "
            "dependent, since the dimension is only n. This dependency gives "
            "a polynomial that alpha satisfies, proving alpha is algebraic.",
            duration=28,
        )
        self.ly.section_divider(2, "Finite Implies Algebraic")

        title = self.ly.title("Proof: Finite => Algebraic")

        # Setup
        setup = MathTex(
            r"[E : F] = n, \quad \alpha \in E",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(setup, DOWN, anchor=title, buff=0.5)
        self.play(Write(setup), run_time=NORMAL)
        self.wait(2)

        # The key linear dependency
        dep = MathTex(
            r"\{1,\, \alpha,\, \alpha^2,\, \ldots,\, \alpha^n\} "
            r"\text{ are } n{+}1 \text{ elements in an } n\text{-dim space}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(dep, DOWN, anchor=setup, buff=0.5)
        self.play(Write(dep), run_time=NORMAL)
        self.wait(3)

        # The consequence
        self.play(FadeOut(setup), FadeOut(dep), run_time=FAST)
        result = MathTex(
            r"\Rightarrow \exists\, c_0, \ldots, c_n \in F \text{ (not all zero) with } "
            r"c_0 + c_1\alpha + \cdots + c_n\alpha^n = 0",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(result, DOWN, anchor=title, buff=0.5)
        self.play(Write(result), run_time=NORMAL)
        self.wait(4)

        conclusion = Text(
            "So alpha satisfies a polynomial over F: algebraic!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(conclusion, DOWN, anchor=result, buff=0.4)
        self.play(FadeIn(conclusion, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene4_simple_extensions(self):
        """Simple extensions: K(alpha)/K."""
        self.add_subcaption(
            "The simplest type of field extension is obtained by adjoining "
            "a single element alpha to K, written K of alpha. If alpha is "
            "algebraic with minimal polynomial of degree d, then K of alpha "
            "is a degree d extension with basis one, alpha, up to alpha to "
            "the d minus one. If alpha is transcendental, K of alpha is "
            "isomorphic to the field of rational functions in one variable.",
            duration=28,
        )
        self.ly.section_divider(3, "Simple Extensions")

        title = self.ly.title("Adjoining One Element")

        formula = MathTex(
            r"K(\alpha) = \text{smallest field containing } K \cup \{\alpha\}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(formula, DOWN, anchor=title, buff=0.5)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(3)

        # Algebraic case
        alg_case = MathTex(
            r"\alpha \text{ algebraic: } [K(\alpha) : K] = \deg(m_{\alpha,K})",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(alg_case, DOWN, anchor=formula, buff=0.5)
        self.play(Write(alg_case), run_time=NORMAL)
        self.wait(3)

        # Basis
        basis = MathTex(
            r"\text{Basis: } \{1,\, \alpha,\, \alpha^2,\, \ldots,\, "
            r"\alpha^{d-1}\} \text{ where } d = \deg(m_\alpha)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(basis, DOWN, anchor=alg_case, buff=0.4)
        self.play(Write(basis), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene5_finitely_generated(self):
        """Finitely generated algebraic extensions are finite."""
        self.add_subcaption(
            "A powerful result: if we adjoin finitely many algebraic "
            "elements to a field, the resulting extension is finite. The proof "
            "uses the tower law iteratively. Starting from K, adjoin alpha "
            "one: finite by the simple extension result. Then adjoin alpha "
            "two: still finite by the tower law. Continue until all elements "
            "are adjoined.",
            duration=28,
        )
        self.ly.section_divider(4, "Finitely Generated Algebraic")

        title = self.ly.title("Algebraic + Finitely Generated = Finite")

        # Statement
        stmt = Text(
            "If alpha_1, ..., alpha_n are algebraic over K,",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(stmt, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(stmt, shift=LEFT * 0.15), run_time=FAST)

        stmt2 = Text(
            "then K(alpha_1, ..., alpha_n) / K is finite.",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(stmt2, DOWN, anchor=stmt, buff=0.3)
        self.play(FadeIn(stmt2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(3)

        # Tower visualization
        self.play(FadeOut(stmt), FadeOut(stmt2), run_time=FAST)
        tower = MathTex(
            r"K \subseteq K(\alpha_1) \subseteq K(\alpha_1, \alpha_2) "
            r"\subseteq \cdots \subseteq K(\alpha_1, \ldots, \alpha_n)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(tower, DOWN, anchor=title, buff=0.5)
        self.play(Write(tower), run_time=NORMAL)
        self.wait(3)

        # Tower law
        result = MathTex(
            r"[K(\alpha_1, \ldots, \alpha_n) : K] "
            r"= \prod_{i=1}^{n} [K(\alpha_1, \ldots, \alpha_i) : "
            r"K(\alpha_1, \ldots, \alpha_{i-1})]",
            font_size=LABEL_SIZE, color=ACCENT,
        )
        self.ly.safe_place(result, DOWN, anchor=tower, buff=0.5)
        self.play(Write(result), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene6_sum_product(self):
        """Sum and product of algebraic elements are algebraic."""
        self.add_subcaption(
            "If alpha and beta are algebraic over K, then their sum, "
            "product, and inverse if nonzero are also algebraic over K. "
            "The proof is elegant: the extension K of alpha and beta is "
            "finite over K by our previous result, and alpha plus beta, "
            "alpha times beta, and alpha inverse all live inside it. "
            "Since finite implies algebraic, we are done.",
            duration=28,
        )
        self.ly.section_divider(5, "Closure Properties")

        title = self.ly.title("Algebraic Elements Form a Field")

        # The key result
        items = [
            Text("If alpha, beta algebraic over K, then:",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("alpha + beta is algebraic over K",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("alpha * beta is algebraic over K",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3)

        # Proof idea
        proof = Text(
            "Proof: K(alpha, beta)/K is finite, and all three elements live in it",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(proof, DOWN, anchor=items[-1], buff=0.4)
        self.play(FadeIn(proof, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene7_algebraic_numbers(self):
        """The field of algebraic numbers Q-bar."""
        self.add_subcaption(
            "The algebraic numbers, denoted Q-bar, are all complex "
            "numbers that are algebraic over the rationals. This set forms "
            "a field by our closure result. Remarkably, Q-bar is countable, "
            "even though almost all real numbers are transcendental! The "
            "rationals are a tiny countable subset of Q-bar.",
            duration=24,
        )
        self.ly.section_divider(6, "Algebraic Numbers")

        title = self.ly.title("The Field of Algebraic Numbers")

        # Definition
        defn = MathTex(
            r"\overline{\mathbb{Q}} = \{\alpha \in \mathbb{C} : "
            r"\alpha \text{ is algebraic over } \mathbb{Q}\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed_def = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.safe_place(boxed_def, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_def), run_time=NORMAL)
        self.wait(3)

        # Properties
        props = [
            Text("Q-bar is a field (sum/product closure)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Q-bar is countable (amazing!)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(props, start_from=boxed_def)
        self.wait(4)

        # Remarkable fact
        fact = Text(
            "Almost all real numbers are transcendental",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(fact, DOWN, anchor=props[-1], buff=0.4)
        self.play(FadeIn(fact, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene8_algebraic_closure(self):
        """Algebraically closed fields and algebraic closure."""
        self.add_subcaption(
            "A field K is algebraically closed if every non-constant "
            "polynomial in K of x has at least one root in K. Equivalently, "
            "every polynomial factors completely into linear factors. "
            "The algebraic closure of a field F is the smallest "
            "algebraically closed field containing F.",
            duration=22,
        )
        self.ly.section_divider(7, "Algebraic Closure")

        title = self.ly.title("Algebraically Closed Fields")

        # Definition
        defn = MathTex(
            r"K \text{ is algebraically closed } \iff "
            r"\forall\, f \in K[x],\; \deg f \geq 1 "
            r"\implies \exists\, \alpha \in K : f(\alpha) = 0",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        boxed_def = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.safe_place(boxed_def, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed_def), run_time=NORMAL)
        self.wait(3)

        # Equivalent: only linear irreducibles
        equiv = Text(
            "Equivalently: the only irreducible polynomials are linear",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(equiv, DOWN, anchor=boxed_def, buff=0.4)
        self.play(FadeIn(equiv, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        # Algebraic closure definition
        closure_def = MathTex(
            r"\overline{F} = \text{algebraic closure of } F "
            r"\text{ (smallest alg. closed field } \supseteq F\text{)}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(closure_def, DOWN, anchor=equiv, buff=0.4)
        self.play(FadeIn(closure_def, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene9_closure_examples(self):
        """Examples: C is closed, R is not, Q-bar is closure of Q."""
        self.add_subcaption(
            "Let us look at examples. The complex numbers C are "
            "algebraically closed by the Fundamental Theorem of Algebra. "
            "The reals R are not, since x squared plus one has no real "
            "root. The algebraic closure of Q is Q-bar, which is a "
            "proper subfield of C. These distinctions matter deeply "
            "in Galois theory.",
            duration=26,
        )
        self.ly.section_divider(8, "Examples")

        title = self.ly.title("Which Fields Are Closed?")

        items = [
            Text("C is algebraically closed (Fund. Thm of Algebra)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("R is NOT (x^2 + 1 has no real root)",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Q-bar = algebraic closure of Q",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)
        self.ly.clear()

    def scene10_summary(self):
        """Summary and outro."""
        self.add_subcaption(
            "Let us summarize. Every finite extension is algebraic, and "
            "finitely generated algebraic extensions are finite. Algebraic "
            "elements are closed under addition and multiplication. "
            "The algebraic numbers form a countable field, and every "
            "field has an algebraic closure. Next time we will build "
            "splitting fields, the stage where Galois groups act.",
            duration=28,
        )
        self.ly.section_divider(9, "Summary")

        title = self.ly.title("Key Takeaways")
        items = [
            Text("Finite extension => algebraic extension",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Finitely generated + algebraic = finite",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Algebraic elements are closed under +, *, inverse",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(3)

        extra = Text(
            "Q-bar is countable; every field has an algebraic closure",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.progressive_reveal([extra], start_from=items[-1])
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "Thank you for watching! Next time we study splitting fields.",
            duration=8,
        )
        play_outro(self, "Splitting Fields", "Advanced Abstract Algebra")
