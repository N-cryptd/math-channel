"""
Video 165: Hilbert Spaces — Functional Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video165_HilbertSpaces

Topics: Definition (complete inner product space),
        Why completeness matters (non-complete example),
        Key examples (l^2, L^2, C^n),
        Orthogonal decomposition theorem,
        Orthonormal bases and Fourier expansion,
        Parseval's identity,
        Riesz Representation Theorem.

Prerequisites: Video 162 (Normed Spaces), Video 163 (Banach Spaces),
               Video 164 (Inner Product Spaces), Video 158 (L^p Spaces).

Competitive insights:
- No major competitor has a dedicated animated Hilbert space video
- Steve Brunton covers applications via whiteboard (not Manim)
- 3B1B touches on it in Fourier series but not as a standalone topic
- Gap in market: first animated exposition of Hilbert spaces

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


class Video165_HilbertSpaces(Scene):
    """Hilbert Spaces: The Perfect Marriage of Geometry and Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_why_completeness()
        self.scene4_examples()
        self.scene5_orthogonal_decomposition()
        self.scene6_fourier_expansion()
        self.scene7_riesz()
        self.scene8_summary_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook — The Perfect Marriage
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: combining inner product geometry with analytic completeness"""
        self.add_subcaption(
            "What do you get when you combine the geometry of inner product "
            "spaces with the analytic power of completeness? The answer is a "
            "Hilbert space, the natural setting for Fourier analysis, quantum "
            "mechanics, and signal processing.",
            duration=12,
        )
        play_intro(self, "Hilbert Spaces", "Functional Analysis")

        title = self.ly.title("The Perfect Marriage")

        items = [
            Text("Inner product spaces give us angles and orthogonality",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("But Cauchy sequences might not converge to anything useful",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Completeness guarantees every Cauchy sequence converges",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("A Hilbert space has BOTH properties",
                 font_size=HEADING_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Definition
    # ------------------------------------------------------------------
    def scene2_definition(self):
        """Formal definition of a Hilbert space"""
        self.ly.section_divider(2, "Definition: Hilbert Space")

        self.add_subcaption(
            "A Hilbert space is a complete inner product space. It combines "
            "the algebraic structure of an inner product with the topological "
            "property of completeness. Equivalently, it is a Banach space "
            "whose norm arises from an inner product.",
            duration=10,
        )

        title = self.ly.title("Hilbert Space: Definition")

        # Main definition
        def_label = Text("Definition",
                         font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        def_text = Text(
            "A Hilbert space is a COMPLETE inner product space",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(def_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(def_text, direction=DOWN, anchor=def_label, buff=0.1)
        self.play(
            Write(def_label),
            FadeIn(def_text, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(def_label), FadeOut(def_text), run_time=FAST)

        # Formal notation
        formal = MathTex(
            r"\mathcal{H} = (H, \langle \cdot, \cdot \rangle)",
            r"\text{ is complete under } \|x\| = \sqrt{\langle x, x \rangle}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(formal, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(formal), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(formal), run_time=FAST)

        # Equivalent characterization
        equiv_label = Text("Equivalent characterization:",
                          font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        equiv_text = Text(
            "A Banach space whose norm comes from an inner product",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(equiv_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(equiv_text, direction=DOWN, anchor=equiv_label, buff=0.1)
        self.play(
            FadeIn(equiv_label, shift=LEFT * 0.15),
            FadeIn(equiv_text, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Why Completeness Matters
    # ------------------------------------------------------------------
    def scene3_why_completeness(self):
        """Non-complete inner product space example"""
        self.ly.section_divider(3, "Why Completeness Matters")

        self.add_subcaption(
            "Consider continuous functions on the unit interval with the L-two "
            "inner product. This is an inner product space, but it is NOT "
            "complete. A Cauchy sequence of continuous functions can converge "
            "to a discontinuous limit that is not in the space. Completing "
            "the space gives L-two, our first true Hilbert space.",
            duration=14,
        )

        title = self.ly.title("A Non-Complete Inner Product Space")

        # Example setup
        ex_label = Text("Example: C[0,1] with L^2 inner product",
                        font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        ex_formula = MathTex(
            r"\langle f, g \rangle = \int_0^1 f(x)\, g(x)\, dx",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ex_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ex_formula, direction=DOWN, anchor=ex_label, buff=0.1)
        self.play(
            FadeIn(ex_label, shift=LEFT * 0.15),
            Write(ex_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(ex_label), FadeOut(ex_formula), run_time=FAST)

        # The problem
        prob = Text(
            "A Cauchy sequence of continuous functions",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        prob2 = Text(
            "can converge to a DISCONTINUOUS function",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(prob, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(prob2, direction=DOWN, anchor=prob, buff=0.1)
        self.play(
            FadeIn(prob, shift=LEFT * 0.15),
            FadeIn(prob2, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(prob), FadeOut(prob2), run_time=FAST)

        # The fix
        fix = Text(
            "Completing C[0,1] gives L^2[0,1] — a Hilbert space",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(fix, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(fix, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(fix), run_time=FAST)

        # Key insight
        insight = MathTex(
            r"\|f_n - f_m\| \to 0",
            r"\implies",
            r"\exists\, f \in L^2 : \|f_n - f\| \to 0",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Examples
    # ------------------------------------------------------------------
    def scene4_examples(self):
        """Three key examples of Hilbert spaces"""
        self.ly.section_divider(4, "Examples of Hilbert Spaces")

        self.add_subcaption(
            "The three most important examples of Hilbert spaces are: "
            "little-l-two, the space of square-summable sequences; "
            "L-two, the space of square-integrable functions; "
            "and C-n, the space of n-dimensional complex vectors. "
            "Every finite-dimensional inner product space is automatically "
            "complete, hence a Hilbert space.",
            duration=12,
        )

        title = self.ly.title("Three Key Hilbert Spaces")

        # Example 1: l^2
        ex1_label = Text("l^2 — square-summable sequences",
                         font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        ex1_formula = MathTex(
            r"\ell^2 = \left\{ (a_n) : \sum_{n=1}^{\infty} |a_n|^2 < \infty \right\}",
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

        # Example 2: L^2
        ex2_label = Text("L^2 — square-integrable functions",
                         font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        ex2_formula = MathTex(
            r"L^2(\Omega) = \left\{ f : \int_\Omega |f|^2 < \infty \right\}",
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

        # Example 3: C^n
        ex3_label = Text("C^n — finite-dimensional (always complete)",
                         font_size=BODY_SIZE, color=ACCENT, font=SANS)
        ex3_note = Text(
            "Every finite-dimensional inner product space is a Hilbert space",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(ex3_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ex3_note, direction=DOWN, anchor=ex3_label, buff=0.1)
        self.play(
            FadeIn(ex3_label, shift=LEFT * 0.15),
            FadeIn(ex3_note, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Orthogonal Decomposition
    # ------------------------------------------------------------------
    def scene5_orthogonal_decomposition(self):
        """Orthogonal decomposition theorem"""
        self.ly.section_divider(5, "Orthogonal Decomposition")

        self.add_subcaption(
            "One of the most powerful results about Hilbert spaces is the "
            "orthogonal decomposition theorem. If M is a closed subspace of "
            "a Hilbert space H, then every vector in H can be uniquely written "
            "as the sum of a vector in M and a vector in its orthogonal "
            "complement. This is the foundation of Fourier series and "
            "least squares approximation.",
            duration=14,
        )

        title = self.ly.title("Orthogonal Decomposition Theorem")

        # Theorem statement
        thm_label = Text("Theorem",
                         font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        thm_text = Text(
            "If M is a closed subspace of H:",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(thm_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(thm_text, direction=DOWN, anchor=thm_label, buff=0.1)
        self.play(
            Write(thm_label),
            FadeIn(thm_text, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(thm_label), FadeOut(thm_text), run_time=FAST)

        # Decomposition formula
        decomp = MathTex(
            r"\mathcal{H} = M \oplus M^\perp",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(decomp, PRIMARY)
        self.ly.safe_place(boxed, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(decomp), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(boxed), run_time=FAST)

        # Unique decomposition
        unique = MathTex(
            r"x = m + n, \quad m \in M,\; n \in M^\perp",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        unique_note = Text(
            "This decomposition is UNIQUE for every x",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(unique, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(unique_note, direction=DOWN, anchor=unique, buff=0.1)
        self.play(
            Write(unique),
            FadeIn(unique_note, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(unique), FadeOut(unique_note), run_time=FAST)

        # Applications
        apps = Text(
            "Foundation of: Fourier series, least squares, PCA",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(apps, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(apps, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Orthonormal Bases and Fourier Expansion
    # ------------------------------------------------------------------
    def scene6_fourier_expansion(self):
        """Orthonormal bases, Fourier expansion, Parseval's identity"""
        self.ly.section_divider(6, "Orthonormal Bases and Fourier Expansion")

        self.add_subcaption(
            "In a separable Hilbert space, there exists a countable "
            "orthonormal basis. Every vector can be expanded as a Fourier "
            "series using this basis. The coefficients are the inner products "
            "with each basis vector. Parseval's identity tells us the norm "
            "squared equals the sum of the squared coefficients.",
            duration=12,
        )

        title = self.ly.title("Fourier Expansion in Hilbert Spaces")

        # Orthonormal basis
        basis_label = Text("Orthonormal basis:",
                          font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        basis_formula = MathTex(
            r"\langle e_i, e_j \rangle = \delta_{ij}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(basis_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(basis_formula, direction=DOWN, anchor=basis_label, buff=0.1)
        self.play(
            FadeIn(basis_label, shift=LEFT * 0.15),
            Write(basis_formula),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(basis_label), FadeOut(basis_formula), run_time=FAST)

        # Fourier expansion
        fourier = MathTex(
            r"x = \sum_{n=1}^{\infty} \langle x, e_n \rangle \, e_n",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed = self.ly.formula_box(fourier, SECONDARY)
        self.ly.safe_place(boxed, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(fourier), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(boxed), run_time=FAST)

        # Parseval's identity
        parseval_label = Text("Parseval's Identity:",
                              font_size=BODY_SIZE, color=ACCENT, font=SANS)
        parseval = MathTex(
            r"\|x\|^2 = \sum_{n=1}^{\infty} |\langle x, e_n \rangle|^2",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(parseval_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(parseval, direction=DOWN, anchor=parseval_label, buff=0.1)
        self.play(
            FadeIn(parseval_label, shift=LEFT * 0.15),
            Write(parseval),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(parseval_label), FadeOut(parseval), run_time=FAST)

        # Classic example
        ex_label = Text("Example in L^2[-π, π]:",
                        font_size=BODY_SIZE, color=WHITE, font=SANS)
        ex_basis = Text(
            "Basis: {1/√2π, cos(nx)/√π, sin(nx)/√π}",
            font_size=LABEL_SIZE, color=DIM, font=MONO,
        )
        self.ly.safe_place(ex_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ex_basis, direction=DOWN, anchor=ex_label, buff=0.1)
        self.play(
            FadeIn(ex_label, shift=LEFT * 0.15),
            FadeIn(ex_basis, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Riesz Representation Theorem
    # ------------------------------------------------------------------
    def scene7_riesz(self):
        """Riesz Representation Theorem"""
        self.ly.section_divider(7, "Riesz Representation Theorem")

        self.add_subcaption(
            "The Riesz Representation Theorem is one of the most beautiful "
            "results in functional analysis. It says that every continuous "
            "linear functional on a Hilbert space is represented by the inner "
            "product with some fixed vector. The dual space is isometrically "
            "isomorphic to the space itself. This is why inner products are "
            "so powerful — they capture all continuous linear functionals.",
            duration=14,
        )

        title = self.ly.title("Riesz Representation Theorem")

        # Statement
        thm_label = Text("Theorem (Riesz, 1907)",
                        font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        self.ly.safe_place(thm_label, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(thm_label), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(thm_label), run_time=FAST)

        # Main formula
        main = MathTex(
            r"\forall\, f \in \mathcal{H}^*, \;\; \exists!\, y \in \mathcal{H}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(main, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(main), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(main), run_time=FAST)

        # Such that
        such = MathTex(
            r"f(x) = \langle x, y \rangle \quad \forall\, x \in \mathcal{H}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed = self.ly.formula_box(such, SECONDARY)
        self.ly.safe_place(boxed, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(such), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(boxed), run_time=FAST)

        # Isometry
        iso = MathTex(
            r"\|f\| = \|y\|",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        iso_note = Text(
            "H and H* are isometrically isomorphic",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(iso, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(iso_note, direction=DOWN, anchor=iso, buff=0.1)
        self.play(
            Write(iso),
            FadeIn(iso_note, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(iso), FadeOut(iso_note), run_time=FAST)

        # Why it matters
        why = Text(
            "This is WHY inner products capture ALL continuous linear maps",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        bridge = Text(
            "Next: Bounded Linear Operators (Video 166)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(why, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(bridge, direction=DOWN, anchor=why, buff=0.1)
        self.play(
            FadeIn(why, shift=LEFT * 0.15),
            FadeIn(bridge, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Summary + Outro
    # ------------------------------------------------------------------
    def scene8_summary_outro(self):
        """Summary and outro"""
        self.ly.section_divider(8, "Summary")

        self.add_subcaption(
            "Let us recap what we have learned about Hilbert spaces. A Hilbert "
            "space is a complete inner product space. Key results include "
            "the orthogonal decomposition theorem, Fourier expansion with "
            "Parseval's identity, and the Riesz representation theorem. "
            "Thank you for watching!",
            duration=10,
        )

        title = self.ly.title("Key Takeaways")

        items = [
            Text("Hilbert space = complete inner product space",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Orthogonal decomposition: H = M ⊕ M⊥",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Fourier expansion + Parseval's identity",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Riesz: every functional is an inner product",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()

        play_outro(self, "Bounded Linear Operators", "Functional Analysis")
