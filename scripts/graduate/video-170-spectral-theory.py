"""
Video 170: Spectral Theory -- Functional Analysis Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video170_SpectralTheory

Topics: Spectrum of a bounded operator,
        Point spectrum, continuous spectrum, residual spectrum,
        Spectral radius formula,
        Spectral mapping theorem,
        Functional calculus preview,
        Spectral theorem for normal operators on Hilbert space,
        Applications.

Prerequisites: Video 166 (Bounded Linear Operators), Video 169 (Compact Operators).

Competitive insights:
- No Manim channel covers spectral theory with animations
- Unique visual: spectrum as colored regions in the complex plane
- Key insight: spectral theory is "eigenvalue theory" for infinite dimensions

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


class Video170_SpectralTheory(Scene):
    """Spectral Theory -- Functional Analysis"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_spectrum_definition()
        self.scene3_spectrum_parts()
        self.scene4_spectral_radius()
        self.scene5_examples()
        self.scene6_functional_calculus()
        self.scene7_normal_operators()
        self.scene8_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Spectral theory is the study of the spectrum of an operator, "
            "which generalizes eigenvalues. In finite dimensions, the "
            "spectrum is just the set of eigenvalues. In infinite dimensions, "
            "it is richer and more complex.",
            duration=9,
        )
        play_intro(self, "Spectral Theory", "Functional Analysis")

        title = self.ly.title("Beyond Eigenvalues")

        items = [
            Text("Eigenvalues: Ax = lambda x, only for finite matrices",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Spectrum: lambda I minus T is not invertible",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Spectral theory is the heart of functional analysis",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Spectrum Definition
    # ------------------------------------------------------------------ #
    def scene2_spectrum_definition(self):
        self.add_subcaption(
            "The spectrum of a bounded operator T is the set of all "
            "complex numbers lambda for which lambda I minus T fails "
            "to be invertible. The complement is the resolvent set.",
            duration=8,
        )

        self.ly.section_divider(2, "The Spectrum")
        title = self.ly.title("Definition of the Spectrum")

        # Spectrum
        spec_label = Text("Spectrum of T:",
                         font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        spec = MathTex(
            r"\sigma(T) = \{\lambda \in \mathbb{C} : \lambda I - T \text{ not invertible}\}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(spec, PRIMARY)
        self.ly.safe_place(spec_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=spec_label, buff=0.2)
        self.play(
            FadeIn(spec_label, shift=LEFT * 0.15),
            Write(spec),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(spec_label), FadeOut(boxed), run_time=FAST)

        # Resolvent
        res_label = Text("Resolvent set:",
                        font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        res = MathTex(
            r"\rho(T) = \mathbb{C} \setminus \sigma(T)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(res_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(res, direction=DOWN, anchor=res_label, buff=0.15)
        self.play(
            FadeIn(res_label, shift=LEFT * 0.15),
            Write(res),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(res_label), FadeOut(res), run_time=FAST)

        # Resolvent operator
        res_op_label = Text("Resolvent operator:",
                          font_size=BODY_SIZE, color=ACCENT, font=SANS)
        res_op = MathTex(
            r"R(\lambda, T) = (\lambda I - T)^{-1}, \quad \lambda \in \rho(T)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(res_op_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(res_op, direction=DOWN, anchor=res_op_label, buff=0.15)
        self.play(
            FadeIn(res_op_label, shift=LEFT * 0.15),
            Write(res_op),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Parts of the Spectrum
    # ------------------------------------------------------------------ #
    def scene3_spectrum_parts(self):
        self.add_subcaption(
            "The spectrum splits into three parts. The point spectrum "
            "consists of eigenvalues. The continuous spectrum consists of "
            "values where lambda I minus T is injective with dense range "
            "but not surjective. The residual spectrum covers the rest.",
            duration=10,
        )

        self.ly.section_divider(3, "Parts of the Spectrum")
        title = self.ly.title("Three Types of Spectral Points")

        # Point spectrum
        pt_label = Text("Point spectrum (eigenvalues):",
                      font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        pt = MathTex(
            r"\sigma_p(T) = \{\lambda : \lambda I - T \text{ not injective}\}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(pt_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(pt, direction=DOWN, anchor=pt_label, buff=0.15)
        self.play(
            FadeIn(pt_label, shift=LEFT * 0.15),
            Write(pt),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(pt_label), FadeOut(pt), run_time=FAST)

        # Continuous spectrum
        ct_label = Text("Continuous spectrum:",
                       font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        ct = Text(
            "injective, dense range, but not surjective",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(ct_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(ct, direction=DOWN, anchor=ct_label, buff=0.15)
        self.play(
            FadeIn(ct_label, shift=LEFT * 0.15),
            FadeIn(ct, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(ct_label), FadeOut(ct), run_time=FAST)

        # Residual spectrum
        rs_label = Text("Residual spectrum:",
                       font_size=BODY_SIZE, color=RED, font=SANS)
        rs = Text(
            "range is not dense",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(rs_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(rs, direction=DOWN, anchor=rs_label, buff=0.15)
        self.play(
            FadeIn(rs_label, shift=LEFT * 0.15),
            FadeIn(rs, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Spectral Radius
    # ------------------------------------------------------------------ #
    def scene4_spectral_radius(self):
        self.add_subcaption(
            "The spectral radius measures the size of the spectrum. "
            "It equals the limit of the n-th root of the operator norm "
            "of T to the n-th power. For any point lambda in the spectrum, "
            "its absolute value is bounded by the spectral radius.",
            duration=10,
        )

        self.ly.section_divider(4, "Spectral Radius")
        title = self.ly.title("Spectral Radius")

        # Definition
        rad_label = Text("Spectral radius:",
                        font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        rad = MathTex(
            r"r(T) = \sup\{|\lambda| : \lambda \in \sigma(T)\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(rad_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(rad, direction=DOWN, anchor=rad_label, buff=0.15)
        self.play(
            FadeIn(rad_label, shift=LEFT * 0.15),
            Write(rad),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(rad_label), FadeOut(rad), run_time=FAST)

        # Gelfand formula
        gelf_label = Text("Gelfand formula:",
                         font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        gelf = MathTex(
            r"r(T) = \lim_{n \to \infty} \|T^n\|^{1/n}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        boxed = self.ly.formula_box(gelf, SECONDARY)
        self.ly.safe_place(gelf_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=gelf_label, buff=0.2)
        self.play(
            FadeIn(gelf_label, shift=LEFT * 0.15),
            Write(gelf),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(gelf_label), FadeOut(boxed), run_time=FAST)

        # Bound
        bound = Text(
            "Always: r(T) is less than or equal to the norm of T",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(bound, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(bound, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Examples
    # ------------------------------------------------------------------ #
    def scene5_examples(self):
        self.add_subcaption(
            "Let us look at examples. On a finite dimensional space, "
            "the spectrum is exactly the eigenvalues. For the shift "
            "operator on l^2, the spectrum is the closed unit disk "
            "but there are no eigenvalues.",
            duration=9,
        )

        self.ly.section_divider(5, "Examples")
        title = self.ly.title("Spectra of Familiar Operators")

        # Finite dim
        fd_label = Text("Finite dimensions:",
                       font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        fd = MathTex(
            r"\sigma(T) = \{\text{eigenvalues of } T\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(fd_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(fd, direction=DOWN, anchor=fd_label, buff=0.15)
        self.play(
            FadeIn(fd_label, shift=LEFT * 0.15),
            Write(fd),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(fd_label), FadeOut(fd), run_time=FAST)

        # Shift operator
        shift_label = Text("Shift operator on l^2:",
                         font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        shift = MathTex(
            r"\sigma(S) = \{\lambda : |\lambda| \leq 1\}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(shift_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(shift, direction=DOWN, anchor=shift_label, buff=0.15)
        self.play(
            FadeIn(shift_label, shift=LEFT * 0.15),
            Write(shift),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(shift_label), FadeOut(shift), run_time=FAST)

        # Key insight
        insight = Text(
            "In infinite dim: spectrum is NOT just eigenvalues!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=title, buff=0.3)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)
        self.play(Indicate(insight), run_time=FAST)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Functional Calculus
    # ------------------------------------------------------------------ #
    def scene6_functional_calculus(self):
        self.add_subcaption(
            "The functional calculus lets us apply functions to operators. "
            "If f is analytic on the spectrum of T, we can define f of T "
            "using the Cauchy integral formula. This generalizes polynomials "
            "of a matrix to analytic functions of an operator.",
            duration=10,
        )

        self.ly.section_divider(6, "Functional Calculus")
        title = self.ly.title("Applying Functions to Operators")

        # Polynomial case
        poly_label = Text("Polynomials of T:",
                        font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        poly = MathTex(
            r"p(T) = a_0 I + a_1 T + \cdots + a_n T^n",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(poly_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(poly, direction=DOWN, anchor=poly_label, buff=0.15)
        self.play(
            FadeIn(poly_label, shift=LEFT * 0.15),
            Write(poly),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(FadeOut(poly_label), FadeOut(poly), run_time=FAST)

        # Analytic functional calculus
        anal_label = Text("Holomorphic functional calculus:",
                        font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        anal = MathTex(
            r"f(T) = \frac{1}{2\pi i} \oint_\Gamma f(\lambda)(\lambda I - T)^{-1}\,d\lambda",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(anal_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(anal, direction=DOWN, anchor=anal_label, buff=0.15)
        self.play(
            FadeIn(anal_label, shift=LEFT * 0.15),
            Write(anal),
            run_time=SLOW,
        )
        self.wait(0.5)
        self.play(FadeOut(anal_label), FadeOut(anal), run_time=FAST)

        # Spectral mapping
        map_label = Text("Spectral mapping theorem:",
                        font_size=BODY_SIZE, color=ACCENT, font=SANS)
        mapping = MathTex(
            r"\sigma(f(T)) = f(\sigma(T))",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(mapping, ACCENT)
        self.ly.safe_place(map_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(boxed, direction=DOWN, anchor=map_label, buff=0.2)
        self.play(
            FadeIn(map_label, shift=LEFT * 0.15),
            Write(mapping),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Normal Operators
    # ------------------------------------------------------------------ #
    def scene7_normal_operators(self):
        self.add_subcaption(
            "For normal operators on Hilbert spaces, the spectral theorem "
            "gives a complete description. A normal operator commutes with "
            "its adjoint, and can be diagonalized by a unitary transformation. "
            "Self adjoint and unitary operators are special cases.",
            duration=10,
        )

        self.ly.section_divider(7, "Normal Operators")
        title = self.ly.title("Spectral Theorem for Normal Operators")

        # Definition
        defn_label = Text("Normal operator:",
                         font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        defn = MathTex(
            r"T^* T = T T^*",
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

        # Spectral theorem
        spec_label = Text("Spectral theorem:",
                        font_size=BODY_SIZE, color=RED, font=SANS)
        spec = MathTex(
            r"T = \int_{\sigma(T)} \lambda \, dE(\lambda)",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(spec_label, direction=DOWN, anchor=title, buff=0.3)
        self.ly.safe_place(spec, direction=DOWN, anchor=spec_label, buff=0.15)
        self.play(
            FadeIn(spec_label, shift=LEFT * 0.15),
            Write(spec),
            run_time=SLOW,
        )
        self.wait(0.5)
        self.play(FadeOut(spec_label), FadeOut(spec), run_time=FAST)

        # Special cases
        cases = [
            Text("Self-adjoint (T* = T): spectrum is real",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Unitary (T* T = I): spectrum on unit circle",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(cases, start_from=title)
        self.wait(0.5)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary
    # ------------------------------------------------------------------ #
    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap. The spectrum generalizes eigenvalues to "
            "infinite dimensions. It splits into point, continuous, and "
            "residual parts. The spectral radius, functional calculus, "
            "and spectral theorem are the pillars of spectral theory.",
            duration=9,
        )

        self.ly.section_divider(8, "Key Takeaways")
        title = self.ly.title("Key Takeaways")

        items = [
            Text("Spectrum: lambda in C where lambda I minus T is not invertible",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Three parts: point (eigenvalues), continuous, residual",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Spectral radius: r(T) = sup of |lambda| for lambda in spectrum",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Functional calculus: apply analytic functions to operators",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Spectral theorem: normal operators are diagonalizable",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        self.ly.clear()
        play_outro(self, "Hahn-Banach Theorem", "Functional Analysis")
