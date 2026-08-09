"""
Video 169: Compact Operators -- Functional Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video169_CompactOperators

Topics: Definition of compact operator,
        Equivalent characterizations,
        Examples (finite-rank, integral operators, diagonal on l^2),
        Compact operators as limits of finite-rank operators,
        Spectrum of compact operators,
        Spectral theorem for compact self-adjoint operators,
        Fredholm alternative.

Prerequisites: Video 166 (Bounded Linear Operators), Video 167 (Dual Space),
               Video 168 (Weak Topology).

Competitive insights:
- No Manim channel covers compact operators with animations
- Key visual: bounded set → compact set (geometric transformation)
- Color coding distinguishes operator types clearly

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
from layout import LayoutEngine, ensure_fits


class Video169_CompactOperators(Scene):
    """Compact Operators -- Functional Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_examples()
        self.scene4_approximation()
        self.scene5_spectrum()
        self.scene6_spectral_theorem()
        self.scene7_fredholm()
        self.scene8_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Some operators on infinite dimensional spaces behave "
            "almost like matrices. They send bounded sets to sets "
            "that are essentially finite dimensional. These are "
            "called compact operators.",
            duration=9,
        )
        play_intro(self, "Compact Operators", "Functional Analysis")

        title = self.ly.title("What Makes an Operator Compact?")

        items = [
            Text("In finite dimensions, every bounded operator is compact",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("In infinite dimensions: compact means close to finite rank",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Compact operators have beautiful spectral theory",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Definition
    # ------------------------------------------------------------------ #
    def scene2_definition(self):
        self.add_subcaption(
            "An operator T from X to Y is compact if it maps the "
            "unit ball to a set whose closure is compact. Equivalently, "
            "every bounded sequence has a subsequence whose image converges.",
            duration=8,
        )

        self.ly.section_divider(2, "Definition")
        title = self.ly.title("Compact Operator")

        # Definition 1
        label1 = Text("Definition (topological):",
                     font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        defn1 = MathTex(
            r"T : X \to Y \text{ is compact if } \overline{T(B_1)} \text{ is compact}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(label1, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(defn1, direction=DOWN, anchor=label1, buff=0.15)
        self.play(
            FadeIn(label1, shift=LEFT * 0.15),
            Write(defn1),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(label1), FadeOut(defn1), run_time=FAST)

        # Definition 2 (sequential)
        label2 = Text("Definition (sequential):",
                     font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        defn2 = MathTex(
            r"\forall\, \{x_n\} \text{ bounded: } \{Tx_n\} \text{ has convergent subsequence}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(label2, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(defn2, direction=DOWN, anchor=label2, buff=0.15)
        self.play(
            FadeIn(label2, shift=LEFT * 0.15),
            Write(defn2),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(label2), FadeOut(defn2), run_time=FAST)

        # Key properties
        props = [
            Text("Every finite-rank operator is compact",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Compact operators form a closed subspace of B(X,Y)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(props, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Examples
    # ------------------------------------------------------------------ #
    def scene3_examples(self):
        self.add_subcaption(
            "Let us look at examples. Finite rank operators and integral "
            "operators with square integrable kernels are compact. "
            "The identity operator on an infinite dimensional space is NOT compact.",
            duration=9,
        )

        self.ly.section_divider(3, "Examples")
        title = self.ly.title("Key Examples")

        # Example 1: NOT compact
        not_label = Text("NOT compact:",
                        font_size=BODY_SIZE, color=RED, font=SANS)
        not_ex = Text(
            "Identity on infinite-dimensional space",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(not_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(not_ex, direction=DOWN, anchor=not_label, buff=0.15)
        self.play(
            FadeIn(not_label, shift=LEFT * 0.15),
            FadeIn(not_ex, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(not_label), FadeOut(not_ex), run_time=FAST)

        # Example 2: Diagonal
        diag_label = Text("Compact on l^2:",
                         font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        diag = MathTex(
            r"T(x_1, x_2, \ldots) = (\lambda_1 x_1, \lambda_2 x_2, \ldots), \;\; \lambda_n \to 0",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(diag_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(diag, direction=DOWN, anchor=diag_label, buff=0.15)
        self.play(
            FadeIn(diag_label, shift=LEFT * 0.15),
            Write(diag),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(diag_label), FadeOut(diag), run_time=FAST)

        # Example 3: Integral
        int_label = Text("Integral operator (L^2 kernel):",
                        font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        int_ex = MathTex(
            r"(Tf)(x) = \int_a^b K(x,y)\,f(y)\,dy, \quad K \in L^2([a,b]^2)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(int_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(int_ex, direction=DOWN, anchor=int_label, buff=0.15)
        self.play(
            FadeIn(int_label, shift=LEFT * 0.15),
            Write(int_ex),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(int_label), FadeOut(int_ex), run_time=FAST)

        # Insight
        insight = Text(
            "Compact = close to finite rank in operator norm",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Approximation
    # ------------------------------------------------------------------ #
    def scene4_approximation(self):
        self.add_subcaption(
            "A beautiful result: every compact operator is the limit "
            "of finite rank operators. In Hilbert spaces, the compact "
            "operators are exactly the closure of the finite rank operators.",
            duration=8,
        )

        self.ly.section_divider(4, "Approximation")
        title = self.ly.title("Compact = Limit of Finite Rank")

        # Main result
        label = Text("Approximation theorem:",
                    font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        formula = MathTex(
            r"T \text{ compact } \iff T = \lim_{n \to \infty} T_n \text{ (finite rank)}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(formula, PRIMARY)
        self.ly.safe_place(label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=label, buff=0.2)
        self.play(
            FadeIn(label, shift=LEFT * 0.15),
            Write(formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(label), FadeOut(boxed), run_time=FAST)

        # Hilbert space special case
        hilbert = Text(
            "In Hilbert spaces: compact = closure of finite rank",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(hilbert, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(hilbert, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(hilbert), run_time=FAST)

        # SVD connection
        svd_label = Text("Connection to SVD:",
                        font_size=BODY_SIZE, color=ACCENT, font=SANS)
        svd = MathTex(
            r"T = \sum_{n=1}^{\infty} \sigma_n \, \langle \cdot, y_n \rangle \, x_n, \;\; \sigma_n \to 0",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(svd_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(svd, direction=DOWN, anchor=svd_label, buff=0.15)
        self.play(
            FadeIn(svd_label, shift=LEFT * 0.15),
            Write(svd),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Spectrum
    # ------------------------------------------------------------------ #
    def scene5_spectrum(self):
        self.add_subcaption(
            "The spectrum of a compact operator is remarkably clean. "
            "Every nonzero spectral point is an eigenvalue with finite "
            "multiplicity. The only possible accumulation point is zero.",
            duration=8,
        )

        self.ly.section_divider(5, "Spectrum of Compact Operators")
        title = self.ly.title("Spectral Structure")

        facts = [
            Text("If 0 is not equal to lambda in the spectrum, then lambda is an eigenvalue",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Every nonzero eigenvalue has finite multiplicity",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("At most countably many eigenvalues",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Only accumulation point: zero",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(facts, start_from=title)
        self.wait(0.5)

        # Visual: spectrum picture
        self.play(FadeOut(*self.mobjects), run_time=FAST)

        spec_label = Text("Spectrum (visualized):",
                         font_size=BODY_SIZE, color=WHITE, font=SANS)
        spec = MathTex(
            r"\sigma(T) = \{0\} \cup \{\lambda_1, \lambda_2, \ldots\}, \;\; |\lambda_n| \to 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        boxed = self.ly.formula_box(spec, WHITE)
        self.ly.safe_place(spec_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=spec_label, buff=0.2)
        self.play(
            FadeIn(spec_label, shift=LEFT * 0.15),
            Write(spec),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Spectral Theorem
    # ------------------------------------------------------------------ #
    def scene6_spectral_theorem(self):
        self.add_subcaption(
            "For compact self adjoint operators on a Hilbert space, "
            "there exists an orthonormal basis of eigenvectors. "
            "The operator can be written as a weighted sum of projections.",
            duration=8,
        )

        self.ly.section_divider(6, "Spectral Theorem")
        title = self.ly.title("Compact Self-Adjoint Operators")

        # Statement
        stmt_label = Text("Spectral Theorem:",
                        font_size=BODY_SIZE, color=RED, font=SANS)
        stmt = MathTex(
            r"Tx = \sum_{n=1}^{\infty} \lambda_n \langle x, e_n \rangle \, e_n",
            font_size=HEADING_SIZE, color=RED,
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

        # Properties
        props = [
            Text("{e_n} is an orthonormal basis of eigenvectors",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Eigenvalues are real (self-adjoint) and tend to zero",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(props, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Fredholm Alternative
    # ------------------------------------------------------------------ #
    def scene7_fredholm(self):
        self.add_subcaption(
            "The Fredholm alternative tells us exactly when the equation "
            "Tx minus lambda x equals y has a solution. For a compact "
            "operator and nonzero lambda, either it always has a solution, "
            "or the homogeneous equation has nontrivial solutions.",
            duration=9,
        )

        self.ly.section_divider(7, "Fredholm Alternative")
        title = self.ly.title("Fredholm Alternative")

        # Statement
        stmt_label = Text("For T compact, lambda not equal to zero:",
                         font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        stmt = MathTex(
            r"Tx - \lambda x = y",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(stmt_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(stmt, direction=DOWN, anchor=stmt_label, buff=0.15)
        self.play(
            FadeIn(stmt_label, shift=LEFT * 0.15),
            Write(stmt),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(stmt_label), FadeOut(stmt), run_time=FAST)

        # Two cases
        cases = [
            Text("EITHER: unique solution for every y",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("OR: nonzero solutions to Tx = lambda x exist",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Index of (lambda I - T) is always zero",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(cases, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary
    # ------------------------------------------------------------------ #
    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap. Compact operators are the closest thing "
            "to matrices in infinite dimensions. Their spectrum is "
            "discrete, they can be approximated by finite rank operators, "
            "and the Fredholm alternative governs solvability.",
            duration=8,
        )

        self.ly.section_divider(8, "Key Takeaways")
        title = self.ly.title("Key Takeaways")

        items = [
            Text("Compact: bounded sequences map to sequences with convergent subsequences",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Identity on infinite-dim space is NOT compact",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Compact = limit of finite-rank operators",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Every nonzero spectral point is an eigenvalue, finite multiplicity",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Fredholm alternative: exactly one of two things holds",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()
        play_outro(self, "Spectral Theory", "Functional Analysis")
