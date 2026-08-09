"""
Video 166: Bounded Linear Operators -- Functional Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video166_BoundedLinearOperators

Topics: Definition of bounded linear operator,
        Operator norm and geometric meaning,
        Bounded = Continuous theorem,
        Examples (identity, multiplication, differentiation),
        Space of bounded operators B(X,Y),
        Adjoint operators on Hilbert spaces,
        Spectral radius and preview of spectral theory.

Prerequisites: Video 163 (Banach Spaces), Video 165 (Hilbert Spaces).

Competitive insights:
- No competitor provides animated intuition for "bounded"
- TBSOM covers topic across 3+ separate videos; we unify in one
- MIT OCW has 84-min lecture; we use 8 focused scenes
- Differentiation as unbounded example is a key visual no competitor animates
- Adjoint connects back to Riesz theorem from Video 165

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


class Video166_BoundedLinearOperators(Scene):
    """Bounded Linear Operators: The Gentle Transformers"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_operator_norm()
        self.scene4_bounded_continuous()
        self.scene5_examples()
        self.scene6_space_bxy()
        self.scene7_adjoint()
        self.scene8_spectral_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook -- The Gentle Transformers
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: linear maps that behave well"""
        self.add_subcaption(
            "In functional analysis, we study linear maps between normed "
            "spaces. But not all linear maps are created equal. Some send "
            "bounded sets to bounded sets, while others can blow things up "
            "to infinity. Today we study bounded linear operators, the "
            "well-behaved maps that are the backbone of functional analysis.",
            duration=12,
        )
        play_intro(self, "Bounded Linear Operators", "Functional Analysis")

        title = self.ly.title("The Gentle Transformers")

        items = [
            Text("Linear maps can stretch, rotate, and project vectors",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("But some maps send bounded sets to UNBOUNDED sets",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Bounded operators: bounded input always gives bounded output",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("These are the operators we can actually work with",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Definition
    # ------------------------------------------------------------------
    def scene2_definition(self):
        """Formal definition of bounded linear operator"""
        self.ly.section_divider(2, "Definition: Bounded Linear Operator")

        self.add_subcaption(
            "A linear operator T from a normed space X to a normed space Y "
            "is called bounded if there exists a constant M such that the "
            "norm of T of x is at most M times the norm of x, for all x. "
            "Equivalently, T maps the unit ball to a bounded set.",
            duration=12,
        )

        title = self.ly.title("Definition: Bounded Operator")

        # Setup
        def_label = Text("Definition",
                         font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        def_formula = MathTex(
            r"T : X \to Y",
            r"\text{ is bounded if }",
            r"\exists\, M \geq 0 : \|Tx\| \leq M\|x\|",
            r"\;\; \forall\, x \in X",
            font_size=BODY_SIZE,
        )
        def_formula[0].set_color(WHITE)
        def_formula[2].set_color(ACCENT)
        def_formula[3].set_color(DIM)
        self.ly.safe_place(def_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(def_formula, direction=DOWN, anchor=def_label, buff=0.2)
        self.play(
            Write(def_label),
            Write(def_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(def_label), FadeOut(def_formula), run_time=FAST)

        # Geometric intuition
        intu_label = Text("Geometric meaning:",
                          font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        intu = Text(
            "T maps the unit ball to a BOUNDED set in Y",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(intu_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(intu, direction=DOWN, anchor=intu_label, buff=0.1)
        self.play(
            FadeIn(intu_label, shift=LEFT * 0.15),
            FadeIn(intu, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(intu_label), FadeOut(intu), run_time=FAST)

        # The operator norm
        norm_label = Text("The operator norm:",
                          font_size=BODY_SIZE, color=ACCENT, font=SANS)
        norm_formula = MathTex(
            r"\|T\| = \sup \left\{ \frac{\|Tx\|}{\|x\|} : x \neq 0 \right\}",
            r"= \sup \{ \|Tx\| : \|x\| \leq 1 \}",
            font_size=HEADING_SIZE,
        )
        norm_formula[0].set_color(ACCENT)
        norm_formula[1].set_color(DIM)
        boxed = self.ly.formula_box(norm_formula, ACCENT)
        self.ly.safe_place(norm_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=norm_label, buff=0.2)
        self.play(
            FadeIn(norm_label, shift=LEFT * 0.15),
            Write(norm_formula),
            run_time=NORMAL,
        )
        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Operator Norm
    # ------------------------------------------------------------------
    def scene3_operator_norm(self):
        """Operator norm: geometric meaning and properties"""
        self.ly.section_divider(3, "The Operator Norm")

        self.add_subcaption(
            "The operator norm measures the maximum stretching factor of a "
            "linear map. It is the largest factor by which T can magnify any "
            "unit vector. The operator norm satisfies all three norm axioms: "
            "it is positive definite, homogeneous, and satisfies the "
            "triangle inequality.",
            duration=12,
        )

        title = self.ly.title("The Operator Norm")

        # Intuition: maximum stretching factor
        stretch = Text(
            "Maximum stretching factor of T",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(stretch, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(stretch, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(stretch), run_time=FAST)

        # Three axioms
        ax_label = Text("The operator norm satisfies:",
                        font_size=BODY_SIZE, color=WHITE, font=SANS)
        ax1 = MathTex(
            r"\|T\| \geq 0,",
            r"\quad \|T\| = 0 \iff T = 0",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        ax2 = MathTex(
            r"\|\alpha T\| = |\alpha| \, \|T\|",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        ax3 = MathTex(
            r"\|T + S\| \leq \|T\| + \|S\|",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(ax_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ax1, direction=DOWN, anchor=ax_label, buff=0.1)
        self.play(
            FadeIn(ax_label, shift=LEFT * 0.15),
            Write(ax1),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(ax1), run_time=FAST)
        self.ly.safe_place(ax2, direction=DOWN, anchor=ax_label, buff=0.1)
        self.play(Write(ax2), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(ax2), run_time=FAST)
        self.ly.safe_place(ax3, direction=DOWN, anchor=ax_label, buff=0.1)
        self.play(Write(ax3), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(ax_label), FadeOut(ax3), run_time=FAST)

        # Key insight
        insight = Text(
            "The operator norm is itself a NORM",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Bounded = Continuous
    # ------------------------------------------------------------------
    def scene4_bounded_continuous(self):
        """Bounded iff Continuous theorem"""
        self.ly.section_divider(4, "Bounded = Continuous")

        self.add_subcaption(
            "One of the most important facts about bounded operators is that "
            "they are exactly the continuous linear operators. Bounded implies "
            "Lipschitz continuous, which implies continuous. And continuous at "
            "the origin implies bounded. This equivalence is the reason we "
            "study bounded operators instead of continuous ones directly.",
            duration=12,
        )

        title = self.ly.title("The Key Equivalence")

        # Theorem statement
        thm_label = Text("Theorem",
                         font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        thm = MathTex(
            r"T \text{ is bounded}",
            r"\iff",
            r"T \text{ is continuous}",
            font_size=HEADING_SIZE,
        )
        thm[0].set_color(PRIMARY)
        thm[1].set_color(ACCENT)
        thm[2].set_color(SECONDARY)
        boxed = self.ly.formula_box(thm, PRIMARY)
        self.ly.safe_place(thm_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=thm_label, buff=0.2)
        self.play(Write(thm_label), run_time=NORMAL)
        self.play(Write(thm), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(thm_label), FadeOut(boxed), run_time=FAST)

        # Proof sketch: bounded -> continuous
        sk_label = Text("Proof idea (bounded implies continuous):",
                        font_size=BODY_SIZE, color=WHITE, font=SANS)
        sk1 = MathTex(
            r"\|Tx - Ty\| = \|T(x - y)\| \leq \|T\|\,\|x - y\|",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(sk_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(sk1, direction=DOWN, anchor=sk_label, buff=0.2)
        self.play(
            FadeIn(sk_label, shift=LEFT * 0.15),
            Write(sk1),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(sk_label), FadeOut(sk1), run_time=FAST)

        # Lipschitz interpretation
        lips = Text(
            "This means T is LIPSCHITZ with constant ||T||",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(lips, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(lips, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(lips), run_time=FAST)

        # Why it matters
        why = Text(
            "In infinite dimensions, linear does NOT imply continuous",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(why, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(why, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Key Examples
    # ------------------------------------------------------------------
    def scene5_examples(self):
        """Three key examples: identity, multiplication, differentiation"""
        self.ly.section_divider(5, "Examples: Bounded vs. Unbounded")

        self.add_subcaption(
            "Let us look at three examples. The identity operator has norm one. "
            "The multiplication operator on continuous functions is bounded with "
            "norm one. But the differentiation operator is unbounded, even on "
            "continuous functions. This is a key difference from finite "
            "dimensions, where every linear map is automatically bounded.",
            duration=14,
        )

        title = self.ly.title("Three Examples")

        # Example 1: Identity
        ex1_label = Text("Example 1: Identity operator",
                         font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        ex1_formula = MathTex(
            r"Id : X \to X, \quad \|Id\| = 1",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ex1_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ex1_formula, direction=DOWN, anchor=ex1_label, buff=0.1)
        self.play(
            FadeIn(ex1_label, shift=LEFT * 0.15),
            Write(ex1_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(ex1_label), FadeOut(ex1_formula), run_time=FAST)

        # Example 2: Multiplication operator
        ex2_label = Text("Example 2: Multiplication on C[0,1]",
                         font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        ex2_formula = MathTex(
            r"(Mf)(x) = x \cdot f(x), \quad \|M\| = 1",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex2_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ex2_formula, direction=DOWN, anchor=ex2_label, buff=0.1)
        self.play(
            FadeIn(ex2_label, shift=LEFT * 0.15),
            Write(ex2_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(ex2_label), FadeOut(ex2_formula), run_time=FAST)

        # Example 3: Differentiation -- NOT BOUNDED
        ex3_label = Text("Example 3: Differentiation on C[0,1]",
                         font_size=BODY_SIZE, color=RED, font=SANS)
        ex3_status = Text(
            "NOT BOUNDED!",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(ex3_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ex3_status, direction=DOWN, anchor=ex3_label, buff=0.1)
        self.play(
            FadeIn(ex3_label, shift=LEFT * 0.15),
            FadeIn(ex3_status, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(ex3_label), FadeOut(ex3_status), run_time=FAST)

        # Why differentiation fails
        counter = Text(
            "Take f_n(x) = sin(n*x): ||f_n|| = 1 but ||f'_n|| = n",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        counter2 = MathTex(
            r"\left\| \frac{d}{dx} \right\| = \sup_n n = \infty",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(counter, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(counter2, direction=DOWN, anchor=counter, buff=0.2)
        self.play(
            FadeIn(counter, shift=LEFT * 0.15),
            Write(counter2),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(counter), FadeOut(counter2), run_time=FAST)

        # Key insight
        insight = Text(
            "In infinite dimensions, linear does NOT imply bounded",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: B(X,Y) as a Banach Space
    # ------------------------------------------------------------------
    def scene6_space_bxy(self):
        """The space of bounded operators B(X,Y)"""
        self.ly.section_divider(6, "The Space B(X,Y)")

        self.add_subcaption(
            "The set of all bounded linear operators from X to Y forms a "
            "vector space that we call B of X, Y. When Y is a Banach space, "
            "B of X, Y is itself a Banach space. Composition of operators "
            "corresponds to multiplication, and the operator norm satisfies "
            "submultiplicativity.",
            duration=12,
        )

        title = self.ly.title("B(X,Y): Operators as a Space")

        # Definition
        def_label = Text("B(X,Y) = {bounded linear operators T : X to Y}",
                        font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        self.ly.safe_place(def_label, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(def_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(def_label), run_time=FAST)

        # Banach space result
        banach_label = Text("Theorem:",
                           font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        banach = Text(
            "If Y is complete, then B(X,Y) is a Banach space",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(banach_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(banach, direction=DOWN, anchor=banach_label, buff=0.1)
        self.play(
            Write(banach_label),
            FadeIn(banach, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(banach_label), FadeOut(banach), run_time=FAST)

        # Composition
        comp_label = Text("Composition of operators:",
                          font_size=BODY_SIZE, color=WHITE, font=SANS)
        comp_formula = MathTex(
            r"T \in B(X,Y), \; S \in B(Y,Z) \implies ST \in B(X,Z)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(comp_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(comp_formula, direction=DOWN, anchor=comp_label, buff=0.2)
        self.play(
            FadeIn(comp_label, shift=LEFT * 0.15),
            Write(comp_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(comp_label), FadeOut(comp_formula), run_time=FAST)

        # Submultiplicativity
        sub_label = Text("Submultiplicativity:",
                         font_size=BODY_SIZE, color=WHITE, font=SANS)
        sub_formula = MathTex(
            r"\|ST\| \leq \|S\| \, \|T\|",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(sub_formula, ACCENT)
        self.ly.safe_place(sub_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=sub_label, buff=0.2)
        self.play(
            FadeIn(sub_label, shift=LEFT * 0.15),
            Write(sub_formula),
            run_time=NORMAL,
        )
        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Adjoint Operators
    # ------------------------------------------------------------------
    def scene7_adjoint(self):
        """Adjoint operators on Hilbert spaces"""
        self.ly.section_divider(7, "Adjoint Operators")

        self.add_subcaption(
            "On Hilbert spaces, the Riesz Representation Theorem from our "
            "last video lets us define the adjoint of a bounded operator. "
            "For each bounded T, there is a unique T-star such that the "
            "inner product of T x with y equals the inner product of x "
            "with T-star y. The adjoint is a mirror image of T.",
            duration=12,
        )

        title = self.ly.title("The Adjoint Operator")

        # Connection to Riesz
        riesz_ref = Text(
            "Uses the Riesz Representation Theorem (Video 165)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(riesz_ref, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(riesz_ref, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(riesz_ref), run_time=FAST)

        # Definition
        def_label = Text("Definition: T* is the unique operator with",
                         font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        def_formula = MathTex(
            r"\langle Tx,\, y \rangle = \langle x,\, T^*y \rangle",
            r"\quad \forall\, x, y \in \mathcal{H}",
            font_size=HEADING_SIZE,
        )
        def_formula[0].set_color(PRIMARY)
        def_formula[1].set_color(DIM)
        boxed = self.ly.formula_box(def_formula, PRIMARY)
        self.ly.safe_place(def_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=def_label, buff=0.2)
        self.play(
            FadeIn(def_label, shift=LEFT * 0.15),
            Write(def_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(def_label), FadeOut(boxed), run_time=FAST)

        # Key properties
        prop_label = Text("Key properties:",
                          font_size=BODY_SIZE, color=WHITE, font=SANS)
        prop1 = MathTex(
            r"\|T^*\| = \|T\|",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(prop_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(prop1, direction=DOWN, anchor=prop_label, buff=0.1)
        self.play(
            FadeIn(prop_label, shift=LEFT * 0.15),
            Write(prop1),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(prop1), run_time=FAST)

        prop2 = MathTex(
            r"(T^*)^* = T",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(prop2, direction=DOWN, anchor=prop_label, buff=0.1)
        self.play(Write(prop2), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(prop2), run_time=FAST)

        prop3 = MathTex(
            r"(ST)^* = T^* S^*",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(prop3, direction=DOWN, anchor=prop_label, buff=0.1)
        self.play(Write(prop3), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(prop_label), FadeOut(prop3), run_time=FAST)

        # Mirror metaphor
        mirror = Text(
            "Think of T* as the mirror image of T across the inner product",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(mirror, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(mirror, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Spectral Radius and Summary
    # ------------------------------------------------------------------
    def scene8_spectral_summary(self):
        """Spectral radius preview and summary"""
        self.ly.section_divider(8, "Spectral Radius and Summary")

        self.add_subcaption(
            "The spectral radius measures the size of an operator's spectrum. "
            "It satisfies a remarkable formula involving the limit of the "
            "n-th root of the norm of T to the n. This connects to "
            "eigenvalues and will lead us to the spectral theorem. Let us "
            "recap what we have learned.",
            duration=12,
        )

        title = self.ly.title("Spectral Radius")

        # Spectrum and spectral radius
        spec_label = Text("Spectrum:",
                         font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        spec = MathTex(
            r"\sigma(T) = \{\lambda \in \mathbb{C} : \lambda I - T \text{ not invertible}\}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(spec_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(spec, direction=DOWN, anchor=spec_label, buff=0.1)
        self.play(
            FadeIn(spec_label, shift=LEFT * 0.15),
            Write(spec),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(spec_label), FadeOut(spec), run_time=FAST)

        # Spectral radius
        rad_label = Text("Spectral radius:",
                         font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        rad = MathTex(
            r"r(T) = \sup \{ |\lambda| : \lambda \in \sigma(T) \}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(rad_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(rad, direction=DOWN, anchor=rad_label, buff=0.2)
        self.play(
            FadeIn(rad_label, shift=LEFT * 0.15),
            Write(rad),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(rad_label), FadeOut(rad), run_time=FAST)

        # Spectral radius formula
        formula_label = Text("Spectral radius formula:",
                              font_size=BODY_SIZE, color=WHITE, font=SANS)
        formula = MathTex(
            r"r(T) = \lim_{n \to \infty} \|T^n\|^{1/n}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(formula, ACCENT)
        self.ly.safe_place(formula_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=formula_label, buff=0.2)
        self.play(
            FadeIn(formula_label, shift=LEFT * 0.15),
            Write(formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(formula_label), FadeOut(boxed), run_time=FAST)

        # Teaser
        teaser = Text(
            "This leads to the Spectral Theorem (future videos)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(teaser, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(teaser, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(teaser), run_time=FAST)

        # Summary
        self.ly.clear()
        self.ly.section_divider(8, "Key Takeaways")

        title2 = self.ly.title("Key Takeaways")

        items = [
            Text("Bounded operator: ||Tx|| <= M||x|| for some constant M",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Operator norm = maximum stretching factor",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Bounded = Continuous (only in infinite dim this matters)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("B(X,Y) is a Banach space; differentiation is NOT bounded",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Adjoint T*: mirror of T via inner product",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(1)

        self.ly.clear()

        play_outro(self, "Compact Operators", "Functional Analysis")
