"""
Video 164: Inner Product Spaces — Functional Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video164_InnerProductSpaces

Topics: What a norm misses (angles, orthogonality),
        Formal definition (three axioms),
        Inner product induces a norm,
        Examples (R^n dot product, L^2 function space, l^2 sequences),
        Cauchy-Schwarz inequality (visual proof),
        Orthogonality and orthogonal complements,
        Orthogonal projection and best approximation,
        Gram-Schmidt in function spaces (Legendre polynomials).

Prerequisites: Video 162 (Normed Spaces), Video 163 (Banach Spaces),
               Linear Algebra Videos 37-38 (Inner Product, Orthogonality/Gram-Schmidt),
               Measure Theory Video 158 (L^p Spaces).

Competitive insights:
- Steve Brunton: application framing drives 158K views (data science angle)
- No animated Manim video covers inner product spaces at graduate level
- Cauchy-Schwarz visual proof via projection geometry (3B1B style)
- Function inner products are the "graduate leap" beyond LA video 37

Quality Rules (mandatory):
1. Max 5 visible elements per scene at any time
2. Use LayoutEngine for ALL positioning -- no manual .shift() or .to_edge()
3. Progressive disclosure: add items one at a time
4. Each add_subcaption() duration = words / 2.5 seconds (12 words = 5s)
5. Call ly.clear() between scenes
6. Use consistent animation vocabulary from channel_branding.py
7. MathTex: raw strings with single backslashes
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
from layout import LayoutEngine, ensure_fits, clamp_position, MAX_HALF_WIDTH


class Video164_InnerProductSpaces(Scene):
    """Inner Product Spaces: Adding Angles, Orthogonality, and Projection"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_induces_norm()
        self.scene4_examples()
        self.scene5_cauchy_schwarz()
        self.scene6_orthogonality()
        self.scene7_projection()
        self.scene8_gram_schmidt()
        self.scene9_summary_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook — What a Norm Misses
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: norms give length, but not angles or orthogonality"""
        self.add_subcaption(
            "A norm tells you the length of a vector. But what about the "
            "angle between two vectors? When are two functions perpendicular? "
            "Inner product spaces give us angles, orthogonality, and projection.",
            duration=10,
        )
        play_intro(self, "Inner Product Spaces", "Functional Analysis")

        title = self.ly.title("What Does a Norm NOT Give You?")

        items = [
            Text("A norm gives you the LENGTH of a vector",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("But what about the ANGLE between two vectors?",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("What does it mean for two functions to be PERPENDICULAR?",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Inner product: angles, orthogonality, projection",
                 font_size=HEADING_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Formal Definition
    # ------------------------------------------------------------------
    def scene2_definition(self):
        """Three axioms of an inner product"""
        self.ly.section_divider(2, "Definition: Inner Product")

        self.add_subcaption(
            "An inner product is a function that takes two vectors and "
            "returns a scalar. It must satisfy three axioms: conjugate "
            "symmetry, linearity in the first argument, and positive "
            "definiteness.",
            duration=10,
        )

        title = self.ly.title("Inner Product: Three Axioms")

        # Axiom 1: Symmetry
        ax1_label = Text("1. Conjugate Symmetry",
                         font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        ax1_formula = MathTex(
            r"\langle x, y \rangle = \overline{\langle y, x \rangle}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ax1_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ax1_formula, direction=DOWN, anchor=ax1_label, buff=0.1)
        self.play(
            FadeIn(ax1_label, shift=LEFT * 0.15),
            Write(ax1_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(ax1_label), FadeOut(ax1_formula), run_time=FAST)

        # Axiom 2: Linearity
        ax2_label = Text("2. Linearity in First Argument",
                         font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        ax2_formula = MathTex(
            r"\langle \alpha x + \beta y,\, z \rangle "
            r"= \alpha \langle x, z \rangle + \beta \langle y, z \rangle",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ax2_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ax2_formula, direction=DOWN, anchor=ax2_label, buff=0.1)
        self.play(
            FadeIn(ax2_label, shift=LEFT * 0.15),
            Write(ax2_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(ax2_label), FadeOut(ax2_formula), run_time=FAST)

        # Axiom 3: Positive-definiteness
        ax3_label = Text("3. Positive-Definiteness",
                         font_size=BODY_SIZE, color=ACCENT, font=SANS)
        ax3_formula = MathTex(
            r"\langle x, x \rangle \geq 0, \quad "
            r"\langle x, x \rangle = 0 \iff x = 0",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(ax3_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ax3_formula, direction=DOWN, anchor=ax3_label, buff=0.1)
        self.play(
            FadeIn(ax3_label, shift=LEFT * 0.15),
            Write(ax3_formula),
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Inner Product Induces a Norm
    # ------------------------------------------------------------------
    def scene3_induces_norm(self):
        """Bridge between inner product and norm"""
        self.ly.section_divider(3, "Inner Product Induces a Norm")

        self.add_subcaption(
            "Every inner product naturally gives you a norm. Simply take "
            "the square root of the inner product of a vector with itself. "
            "But be careful, not every norm comes from an inner product.",
            duration=8,
        )

        title = self.ly.title("The Bridge: Inner Product to Norm")

        # Key formula
        formula = MathTex(
            r"\|x\| = \sqrt{\langle x, x \rangle}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(formula, PRIMARY)
        self.ly.safe_place(boxed, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(1)
        self.play(FadeOut(boxed), run_time=FAST)

        # Verification
        verify = Text(
            "This satisfies all norm axioms by the inner product axioms",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(verify, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(verify, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(verify), run_time=FAST)

        # Warning
        warning = Text(
            "NOT every norm comes from an inner product!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        warn_detail = Text(
            "Example: L1 and L-infinity norms are NOT inner-product norms",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(warning, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(warn_detail, direction=DOWN, anchor=warning, buff=0.1)
        self.play(
            FadeIn(warning, shift=LEFT * 0.15),
            FadeIn(warn_detail, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Examples
    # ------------------------------------------------------------------
    def scene4_examples(self):
        """Three key examples of inner product spaces"""
        self.ly.section_divider(4, "Examples of Inner Product Spaces")

        self.add_subcaption(
            "The most familiar inner product is the dot product in R^n. "
            "But the real power comes in infinite dimensions: the L-two "
            "function inner product and the little-l-two sequence space.",
            duration=8,
        )

        title = self.ly.title("Three Inner Product Spaces")

        # Example 1: R^n
        ex1_label = Text("R^n — the dot product",
                         font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        ex1_formula = MathTex(
            r"\langle x, y \rangle = \sum_{i=1}^{n} x_i \, y_i",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ex1_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ex1_formula, direction=DOWN, anchor=ex1_label, buff=0.1)
        self.play(
            FadeIn(ex1_label, shift=LEFT * 0.15),
            Write(ex1_formula),
            run_time=NORMAL,
        )
        self.wait(1)
        self.play(FadeOut(ex1_label), FadeOut(ex1_formula), run_time=FAST)

        # Example 2: L^2[a,b]
        ex2_label = Text("L^2[a,b] — function inner product",
                         font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        ex2_formula = MathTex(
            r"\langle f, g \rangle = \int_{a}^{b} f(x)\,g(x)\,dx",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex2_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ex2_formula, direction=DOWN, anchor=ex2_label, buff=0.1)
        self.play(
            FadeIn(ex2_label, shift=LEFT * 0.15),
            Write(ex2_formula),
            run_time=NORMAL,
        )
        self.wait(1)
        self.play(FadeOut(ex2_label), FadeOut(ex2_formula), run_time=FAST)

        # Example 3: l^2
        ex3_label = Text("l^2 — square-summable sequences",
                         font_size=BODY_SIZE, color=ACCENT, font=SANS)
        ex3_formula = MathTex(
            r"\langle a, b \rangle = \sum_{n=1}^{\infty} a_n \, b_n",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(ex3_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ex3_formula, direction=DOWN, anchor=ex3_label, buff=0.1)
        self.play(
            FadeIn(ex3_label, shift=LEFT * 0.15),
            Write(ex3_formula),
            run_time=NORMAL,
        )
        self.wait(1)

        # Key insight
        insight = Text(
            "The sum becomes an integral in infinite dimensions",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=ex3_formula, buff=0.3)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Cauchy-Schwarz Inequality
    # ------------------------------------------------------------------
    def scene5_cauchy_schwarz(self):
        """Statement and visual proof intuition of Cauchy-Schwarz"""
        self.ly.section_divider(5, "Cauchy-Schwarz Inequality")

        self.add_subcaption(
            "The Cauchy-Schwarz inequality is the most important inequality "
            "in inner product spaces. It says the inner product of two "
            "vectors is bounded by the product of their norms. Think of "
            "it geometrically: the projection of one vector onto another "
            "cannot exceed the length of the original vector.",
            duration=12,
        )

        title = self.ly.title("Cauchy-Schwarz Inequality")

        # Statement
        formula = MathTex(
            r"|\langle x, y \rangle| \leq \|x\| \, \|y\|",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(formula, PRIMARY)
        self.ly.safe_place(boxed, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(1)
        self.play(FadeOut(boxed), run_time=FAST)

        # Geometric intuition
        int1 = Text(
            "Geometric intuition: project y onto x",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(int1, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(int1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(int1), run_time=FAST)

        # Projection formula
        proj = MathTex(
            r"\text{proj}_x(y) = \frac{\langle x, y \rangle}{\|x\|^2}\, x",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(proj, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(proj), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(proj), run_time=FAST)

        # Angle formula
        angle = MathTex(
            r"\cos(\theta) = \frac{\langle x, y \rangle}{\|x\|\,\|y\|}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        angle_label = Text(
            "This is why we need an inner product for angles!",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(angle, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(angle_label, direction=DOWN, anchor=angle, buff=0.1)
        self.play(Write(angle), FadeIn(angle_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.play(FadeOut(angle), FadeOut(angle_label), run_time=FAST)

        # Equality case
        eq = Text(
            "Equality iff x and y are linearly dependent",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(eq, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(eq, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Orthogonality and Complements
    # ------------------------------------------------------------------
    def scene6_orthogonality(self):
        """Orthogonality definition, complements, Pythagorean theorem"""
        self.ly.section_divider(6, "Orthogonality")

        self.add_subcaption(
            "Two vectors are orthogonal if their inner product is zero. "
            "The orthogonal complement of a subspace consists of all "
            "vectors perpendicular to every vector in that subspace. "
            "Orthogonality gives us the Pythagorean theorem in any "
            "inner product space.",
            duration=10,
        )

        title = self.ly.title("Orthogonality and Complements")

        # Definition
        def_label = Text("Definition:", font_size=BODY_SIZE, color=DIM, font=SANS)
        def_formula = MathTex(
            r"x \perp y \iff \langle x, y \rangle = 0",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(def_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(def_formula, direction=DOWN, anchor=def_label, buff=0.1)
        self.play(
            FadeIn(def_label, shift=LEFT * 0.15),
            Write(def_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(def_label), FadeOut(def_formula), run_time=FAST)

        # Orthogonal complement
        comp_label = Text("Orthogonal Complement of M:",
                          font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        comp_formula = MathTex(
            r"M^\perp = \{x : \langle x, m \rangle = 0 \;\; \forall\, m \in M\}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(comp_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(comp_formula, direction=DOWN, anchor=comp_label, buff=0.1)
        self.play(
            FadeIn(comp_label, shift=LEFT * 0.15),
            Write(comp_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(comp_label), FadeOut(comp_formula), run_time=FAST)

        # Pythagorean theorem
        pyth = MathTex(
            r"x \perp y \implies \|x + y\|^2 = \|x\|^2 + \|y\|^2",
            font_size=BODY_SIZE, color=ACCENT,
        )
        pyth_note = Text(
            "The Pythagorean theorem holds in ANY inner product space!",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(pyth, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(pyth_note, direction=DOWN, anchor=pyth, buff=0.1)
        self.play(Write(pyth), FadeIn(pyth_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Orthogonal Projection
    # ------------------------------------------------------------------
    def scene7_projection(self):
        """Orthogonal projection and best approximation"""
        self.ly.section_divider(7, "Orthogonal Projection")

        self.add_subcaption(
            "Given an orthonormal basis, we can project any vector onto a "
            "subspace by summing the inner products with each basis vector. "
            "This projection is the best approximation in the sense that "
            "it minimizes the distance to the subspace.",
            duration=10,
        )

        title = self.ly.title("Orthogonal Projection")

        # Projection formula
        formula = MathTex(
            r"\text{proj}_M(x) = \sum_{i} \langle x, e_i \rangle \, e_i",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(formula, PRIMARY)
        self.ly.safe_place(boxed, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(boxed), run_time=FAST)

        # Best approximation
        best = Text(
            "Best Approximation Theorem:",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        best_formula = MathTex(
            r"\|x - \text{proj}_M(x)\| \leq \|x - m\| "
            r"\quad \forall\, m \in M",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(best, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(best_formula, direction=DOWN, anchor=best, buff=0.1)
        self.play(
            FadeIn(best, shift=LEFT * 0.15),
            Write(best_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(best), FadeOut(best_formula), run_time=FAST)

        # Applications teaser
        apps = Text(
            "Applications: Fourier series, PCA, least squares",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(apps, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(apps, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Gram-Schmidt in Function Spaces
    # ------------------------------------------------------------------
    def scene8_gram_schmidt(self):
        """Gram-Schmidt applied to polynomials in L^2[-1,1]"""
        self.ly.section_divider(8, "Gram-Schmidt in Function Spaces")

        self.add_subcaption(
            "The Gram-Schmidt process works in any inner product space. "
            "Applied to the monomials one, x, x-squared in the L-two "
            "inner product on the interval from minus one to one, it "
            "produces the Legendre polynomials, a fundamental family "
            "of orthogonal polynomials.",
            duration=12,
        )

        title = self.ly.title("Legendre Polynomials via Gram-Schmidt")

        # Process description
        desc = Text(
            "Apply Gram-Schmidt to {1, x, x^2, ...} in L^2[-1,1]",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(desc, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(desc, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(desc), run_time=FAST)

        # P_0
        p0_label = Text("P_0(x) = 1",
                        font_size=BODY_SIZE, color=PRIMARY, font=MONO)
        self.ly.safe_place(p0_label, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(p0_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(p0_label), run_time=FAST)

        # P_1
        p1_label = Text("P_1(x) = x",
                        font_size=BODY_SIZE, color=SECONDARY, font=MONO)
        self.ly.safe_place(p1_label, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(p1_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(p1_label), run_time=FAST)

        # P_2
        p2_label = Text("P_2(x) = (3x^2 - 1) / 2",
                        font_size=BODY_SIZE, color=ACCENT, font=MONO)
        self.ly.safe_place(p2_label, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(p2_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(p2_label), run_time=FAST)

        # Key insight
        insight = Text(
            "These polynomials are mutually orthogonal in L^2[-1,1]!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        detail = Text(
            "They form the natural basis for approximating functions on [-1,1]",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(detail, direction=DOWN, anchor=insight, buff=0.1)
        self.play(
            FadeIn(insight, shift=LEFT * 0.15),
            FadeIn(detail, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Summary + Outro
    # ------------------------------------------------------------------
    def scene9_summary_outro(self):
        """Summary and preview of Hilbert Spaces"""
        self.add_subcaption(
            "To recap: inner product spaces give us angles, orthogonality, "
            "and projection on top of what norms provide. The Cauchy-Schwarz "
            "inequality is the foundational result. Not every norm comes "
            "from an inner product. In the next video, we add completeness "
            "to get Hilbert spaces, the crown jewels of functional analysis.",
            duration=12,
        )

        title = self.ly.title("Summary + What's Next")

        items = [
            Text("Inner product: angles, orthogonality, projection",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Cauchy-Schwarz: the foundational inequality",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Not every norm comes from an inner product",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("L^2 function space: the key infinite-dimensional example",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        play_outro(self, "Hilbert Spaces", "Functional Analysis")
