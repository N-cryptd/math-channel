"""
Video 167: The Dual Space -- Functional Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video167_DualSpace

Topics: Linear functionals on normed spaces,
        The dual space X* and its norm,
        Finite-dimensional examples and dual basis,
        Infinite-dimensional examples (C[a,b], L^p),
        Hahn-Banach theorem preview,
        The double dual X** and reflexivity,
        Connection to Riesz representation.

Prerequisites: Video 162 (Normed Spaces), Video 163 (Banach Spaces),
               Video 165 (Hilbert Spaces), Video 166 (Bounded Linear Operators).

Competitive insights:
- No major Manim channel covers the dual space with animations
- The Math Sorcerer covers on whiteboard only (no visual intuition)
- Unique opportunity: animate the duality between elements and functionals
- Use color coding: elements of X (PRIMARY), functionals (SECONDARY), double dual (ACCENT)
- Geometric intuition: functionals as "measurements" of vectors
- Concrete examples before abstract theory

Quality Rules (mandatory):
1. Max 5 visible elements per scene at any time
2. Use LayoutEngine for ALL positioning -- no manual .shift() or .to_edge()
3. Progressive disclosure: add items one at a time
4. Each add_subcaption() duration = words / 2.5 seconds (12 words = 5s)
5. Call ly.clear() between scenes
6. Use consistent animation vocabulary from channel_branding.py
"""

from manim import *
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background, clear_background,
)
from layout import LayoutEngine, ensure_fits


class Video167_DualSpace(Scene):
    """The Dual Space -- Functional Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_linear_functionals()
        self.scene3_dual_space()
        self.scene4_finite_dim_examples()
        self.scene5_infinite_dim_examples()
        self.scene6_hahn_banach()
        self.scene7_double_dual()
        self.scene8_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Given a vector space, can we build a completely new space from it? "
            "The answer is yes, and the result is called the dual space. "
            "Let us explore why this matters.",
            duration=10,
        )
        play_intro(self, "The Dual Space", "Functional Analysis")

        title = self.ly.title("Why the Dual Space?")

        items = [
            Text("Vectors are objects; functionals are measurements of them",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("The dual space captures ALL possible linear measurements",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Essential for PDEs, optimization, quantum mechanics",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Linear Functionals
    # ------------------------------------------------------------------ #
    def scene2_linear_functionals(self):
        self.add_subcaption(
            "A linear functional is a linear map from a vector space "
            "to its underlying field of scalars. It takes a vector "
            "and returns a number, respecting linearity.",
            duration=8,
        )

        self.ly.section_divider(2, "Linear Functionals")
        title = self.ly.title("What is a Linear Functional?")

        # Definition
        defn_label = Text("Definition:",
                           font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        defn = MathTex(
            r"f : X \to \mathbb{F}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(defn_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(defn, direction=DOWN, anchor=defn_label, buff=0.15)
        self.play(
            FadeIn(defn_label, shift=LEFT * 0.15),
            Write(defn),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Linearity condition
        linearity = MathTex(
            r"f(ax + by) = a\,f(x) + b\,f(y)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(linearity, direction=DOWN, anchor=defn, buff=0.2)
        self.play(Write(linearity), run_time=NORMAL)
        self.wait(0.5)

        # Bounded
        self.play(FadeOut(defn_label), FadeOut(defn), FadeOut(linearity), run_time=FAST)

        bound_label = Text("Bounded means:",
                           font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        bounded = MathTex(
            r"|f(x)| \leq M\,\|x\|",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(bound_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(bounded, direction=DOWN, anchor=bound_label, buff=0.15)
        self.play(
            FadeIn(bound_label, shift=LEFT * 0.15),
            Write(bounded),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(bound_label), FadeOut(bounded), run_time=FAST)

        # Examples
        self.add_subcaption(
            "Three classic examples: the dot product with a fixed vector, "
            "the trace of a matrix, and evaluation of a function at a point.",
            duration=7,
        )

        ex_label = Text("Examples of linear functionals:",
                        font_size=BODY_SIZE, color=ACCENT, font=SANS)
        examples = [
            MathTex(r"f(\vec{x}) = \vec{a} \cdot \vec{x}",
                    font_size=BODY_SIZE, color=WHITE),
            MathTex(r"f(A) = \mathrm{tr}(A)",
                    font_size=BODY_SIZE, color=WHITE),
            MathTex(r"\delta_t(f) = f(t)",
                    font_size=BODY_SIZE, color=WHITE),
        ]
        self.ly.safe_place(ex_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.progressive_reveal(examples, start_from=ex_label, run_time=FAST)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: The Dual Space X*
    # ------------------------------------------------------------------ #
    def scene3_dual_space(self):
        self.add_subcaption(
            "The dual space X star is the collection of all bounded linear "
            "functionals on X. It is itself a normed space, using the "
            "operator norm. Even if X is not complete, X star always is.",
            duration=10,
        )

        self.ly.section_divider(3, "The Dual Space X*")
        title = self.ly.title("The Dual Space")

        # Definition
        defn_label = Text("Dual space:",
                         font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        defn = MathTex(
            r"X^* = B(X,\, \mathbb{F}) = \{ f : X \to \mathbb{F} \mid f \text{ bounded and linear} \}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(defn_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(defn, direction=DOWN, anchor=defn_label, buff=0.15)
        self.play(
            FadeIn(defn_label, shift=LEFT * 0.15),
            Write(defn),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(defn_label), FadeOut(defn), run_time=FAST)

        # Dual norm
        self.add_subcaption(
            "The norm of a functional f is the largest value it takes "
            "on the unit ball. This is exactly the operator norm.",
            duration=6,
        )

        norm_label = Text("Dual norm (operator norm for functionals):",
                         font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        norm = MathTex(
            r"\|f\| = \sup\{|f(x)| : \|x\| \leq 1\}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed = self.ly.formula_box(norm, SECONDARY)
        self.ly.safe_place(norm_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=norm_label, buff=0.2)
        self.play(
            FadeIn(norm_label, shift=LEFT * 0.15),
            Write(norm),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(norm_label), FadeOut(boxed), run_time=FAST)

        # Key theorem
        self.add_subcaption(
            "An important fact: even if the original space X is not complete, "
            "its dual space X star is always a Banach space.",
            duration=6,
        )

        key = Text(
            "X* is ALWAYS a Banach space (even if X is not complete)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(Indicate(key), run_time=FAST)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Finite-Dimensional Examples
    # ------------------------------------------------------------------ #
    def scene4_finite_dim_examples(self):
        self.add_subcaption(
            "In finite dimensions, every linear functional is the dot product "
            "with some fixed vector. This means R n dual is isomorphic to R n. "
            "We also define the dual basis.",
            duration=9,
        )

        self.ly.section_divider(4, "Finite Dimensions")
        title = self.ly.title("R^n is Self-Dual")

        # Main formula
        formula_label = Text("Every linear functional on R^n:",
                            font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        formula = MathTex(
            r"f(\vec{x}) = \vec{a} \cdot \vec{x} = \sum_{i=1}^{n} a_i\, x_i",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(formula_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(formula, direction=DOWN, anchor=formula_label, buff=0.15)
        self.play(
            FadeIn(formula_label, shift=LEFT * 0.15),
            Write(formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(formula_label), FadeOut(formula), run_time=FAST)

        # Isomorphism
        iso_label = Text("Isomorphism:",
                        font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        iso = MathTex(
            r"(\mathbb{R}^n)^* \cong \mathbb{R}^n",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(iso_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(iso, direction=DOWN, anchor=iso_label, buff=0.15)
        self.play(
            FadeIn(iso_label, shift=LEFT * 0.15),
            Write(iso),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(iso_label), FadeOut(iso), run_time=FAST)

        # Dual basis
        self.add_subcaption(
            "The dual basis consists of functionals that pick out individual "
            "coordinates. The i-th dual basis element gives the i-th "
            "component of a vector.",
            duration=7,
        )

        db_label = Text("Dual basis:",
                        font_size=BODY_SIZE, color=ACCENT, font=SANS)
        db = MathTex(
            r"e_i^*(e_j) = \delta_{ij} = \begin{cases} 1 & i = j \\ 0 & i \neq j \end{cases}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(db_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(db, direction=DOWN, anchor=db_label, buff=0.15)
        self.play(
            FadeIn(db_label, shift=LEFT * 0.15),
            Write(db),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(db_label), FadeOut(db), run_time=FAST)

        # Takeaway
        takeaway = Text(
            "In finite dimensions: dim(X*) = dim(X)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(takeaway, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(takeaway, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Infinite-Dimensional Examples
    # ------------------------------------------------------------------ #
    def scene5_infinite_dim_examples(self):
        self.add_subcaption(
            "In infinite dimensions, the dual space can be much richer "
            "and more complex. On continuous functions, evaluation at a "
            "point is a bounded functional. For L p spaces, the dual is L q.",
            duration=9,
        )

        self.ly.section_divider(5, "Infinite Dimensions")
        title = self.ly.title("Infinite-Dimensional Duals")

        # Example 1: C[a,b]
        ex1_label = Text("On C[a,b] (continuous functions):",
                        font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        ex1 = MathTex(
            r"\delta_t(f) = f(t)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ex1_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ex1, direction=DOWN, anchor=ex1_label, buff=0.15)
        self.play(
            FadeIn(ex1_label, shift=LEFT * 0.15),
            Write(ex1),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(ex1_label), FadeOut(ex1), run_time=FAST)

        # Example 2: L^p duality
        ex2_label = Text("L^p duality (Riesz representation):",
                        font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        ex2 = MathTex(
            r"(L^p)^* \cong L^q \quad \text{where} \quad \frac{1}{p} + \frac{1}{q} = 1",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex2_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ex2, direction=DOWN, anchor=ex2_label, buff=0.15)
        self.play(
            FadeIn(ex2_label, shift=LEFT * 0.15),
            Write(ex2),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(ex2_label), FadeOut(ex2), run_time=FAST)

        # Key insight
        self.add_subcaption(
            "Unlike finite dimensions, in infinite dimensions the dual space "
            "is usually NOT isomorphic to the original space. "
            "Not all functionals are easy to write explicitly.",
            duration=7,
        )

        insight_label = Text("Key difference from finite dimensions:",
                            font_size=BODY_SIZE, color=ACCENT, font=SANS)
        insight = Text(
            "X* is generally NOT isomorphic to X",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(insight, direction=DOWN, anchor=insight_label, buff=0.15)
        self.play(
            FadeIn(insight_label, shift=LEFT * 0.15),
            FadeIn(insight, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(Indicate(insight), run_time=FAST)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Hahn-Banach Theorem (Preview)
    # ------------------------------------------------------------------ #
    def scene6_hahn_banach(self):
        self.add_subcaption(
            "The Hahn-Banach theorem says that any bounded linear functional "
            "on a subspace can be extended to the whole space without "
            "increasing its norm. This guarantees the dual space is always rich.",
            duration=9,
        )

        self.ly.section_divider(6, "Hahn-Banach Theorem")
        title = self.ly.title("Hahn-Banach Theorem (Preview)")

        # Statement
        stmt_label = Text("Theorem (Hahn-Banach):",
                         font_size=BODY_SIZE, color=RED, font=SANS)
        stmt = MathTex(
            r"\text{If } f \text{ is bounded on } Y \subseteq X, "
            r"\text{ then } \exists\, \tilde{f} \in X^* : "
            r"\tilde{f}|_Y = f, \; \|\tilde{f}\| = \|f\|",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(stmt_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(stmt, direction=DOWN, anchor=stmt_label, buff=0.15)
        self.play(
            FadeIn(stmt_label, shift=LEFT * 0.15),
            Write(stmt),
            run_time=SLOW,
        )
        self.wait(0.5)
        self.play(FadeOut(stmt_label), FadeOut(stmt), run_time=FAST)

        # Geometric meaning
        self.add_subcaption(
            "Geometrically, this means you can extend any measurement from a "
            "subspace to the full space without distorting it. "
            "The extension preserves the maximum measurement value.",
            duration=8,
        )

        geo_items = [
            Text("Extend functional from subspace to whole space",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Norm is preserved: no distortion during extension",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Guarantees X* is always non-trivial and rich",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(geo_items, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: The Double Dual X**
    # ------------------------------------------------------------------ #
    def scene7_double_dual(self):
        self.add_subcaption(
            "If we take the dual of the dual, we get the double dual X double star. "
            "There is a natural embedding from X into its double dual. "
            "When this embedding is onto, we say X is reflexive.",
            duration=9,
        )

        self.ly.section_divider(7, "The Double Dual X**")
        title = self.ly.title("Double Dual and Reflexivity")

        # Definition
        defn_label = Text("Double dual:",
                        font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        defn = MathTex(
            r"X^{**} = (X^*)^*",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(defn_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(defn, direction=DOWN, anchor=defn_label, buff=0.15)
        self.play(
            FadeIn(defn_label, shift=LEFT * 0.15),
            Write(defn),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(defn_label), FadeOut(defn), run_time=FAST)

        # Natural embedding
        self.add_subcaption(
            "The natural embedding maps each element x of X to an element "
            "of the double dual. This element acts on functionals f by "
            "returning f of x.",
            duration=7,
        )

        embed_label = Text("Natural embedding J: X to X double star:",
                          font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        embed = MathTex(
            r"J(x)(f) = f(x)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed = self.ly.formula_box(embed, SECONDARY)
        self.ly.safe_place(embed_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=embed_label, buff=0.2)
        self.play(
            FadeIn(embed_label, shift=LEFT * 0.15),
            Write(embed),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(embed_label), FadeOut(boxed), run_time=FAST)

        # Reflexivity
        self.add_subcaption(
            "A space is reflexive when the natural embedding J is onto, "
            "meaning every element of the double dual comes from some "
            "element of the original space. All finite dimensional spaces "
            "and all Hilbert spaces are reflexive.",
            duration=9,
        )

        ref_label = Text("Reflexive: J is onto (X = X**):",
                        font_size=BODY_SIZE, color=ACCENT, font=SANS)
        ref_items = [
            Text("All finite-dimensional spaces are reflexive",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("All Hilbert spaces are reflexive (via Riesz)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("L^1 and L^infinity are NOT reflexive",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.safe_place(ref_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.progressive_reveal(ref_items, start_from=ref_label, run_time=FAST)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary
    # ------------------------------------------------------------------ #
    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap what we have learned about the dual space. "
            "The dual space is fundamental in functional analysis, "
            "connecting to weak topologies, reflexivity, and much more.",
            duration=8,
        )

        self.ly.section_divider(8, "Key Takeaways")
        title = self.ly.title("Key Takeaways")

        items = [
            Text("X* = space of all bounded linear functionals on X",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("X* is always a Banach space (even if X is not)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Finite dim: X* isomorphic to X; infinite dim: usually not",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Hahn-Banach guarantees X* is always rich",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Reflexive (X = X**): finite dim and Hilbert spaces",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()
        play_outro(self, "Weak and Weak-* Topology", "Functional Analysis")
