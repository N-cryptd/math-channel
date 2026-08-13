"""
Video 189: Sturm-Liouville Theory -- Partial Differential Equations Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video189_SturmLiouville

Topics: Sturm-Liouville form and its role in PDEs,
        Every separation problem as a Sturm-Liouville problem,
        Self-adjoint operators and their properties,
        Real eigenvalues and orthogonal eigenfunctions,
        Completeness and eigenfunction expansions,
        Why Sturm-Liouville theory is the backbone of analytical PDE solutions.

Prerequisites: Video 188 (Separation of Variables), Videos 185-187 (heat, wave, Laplace),
               Linear Algebra (eigenvalues, orthogonality),
               Functional Analysis (inner product spaces).

Competitive insights:
- Faculty of Khan (194K views): rigorous SL proof but whiteboard-only, no physical motivation
- NO competitor animates Sturm-Liouville theory -- world first
- Our approach: physical motivation first, then general form, key properties, PDE payoff

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


class Video189_SturmLiouville(Scene):
    """Sturm-Liouville Theory -- the backbone of analytical PDE solutions."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_sl_form()
        self.scene3_all_sl_problems()
        self.scene4_self_adjoint()
        self.scene5_key_properties()
        self.scene6_completeness()
        self.scene7_pde_payoff()
        self.scene8_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "In every PDE we have solved, separation of variables "
            "produced an eigenvalue problem. Different equations, "
            "different boundary conditions, but the same pattern: "
            "eigenvalues and eigenfunctions. Today we learn why this "
            "always works. Sturm-Liouville theory is the "
            "mathematical backbone behind every analytical PDE "
            "solution.",
            duration=12,
        )
        play_intro(self, "Sturm-Liouville Theory", "Partial Differential Equations")

        title = self.ly.title("The Universal Eigenvalue Problem")

        items = [
            Text("Heat equation: Fourier sines and cosines", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Wave equation: same eigenfunctions, new dynamics", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Disk problems: Bessel functions", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("One theory explains all of them", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: The Sturm-Liouville Form
    # ------------------------------------------------------------------ #
    def scene2_sl_form(self):
        self.ly.section_divider("1", "The Sturm-Liouville Form")
        self.add_subcaption(
            "The Sturm-Liouville form is a second-order "
            "differential equation written in a specific way. "
            "Negative the derivative of p times y prime, plus "
            "q times y, equals lambda times w times y. "
            "Here p, q, and w are functions of x. The function "
            "p is positive, and w is the weight function. "
            "The eigenvalue is lambda.",
            duration=13,
        )
        title = self.ly.title("The Sturm-Liouville Form")

        # Show the SL equation
        sl_eq = MathTex(
            r"-[p(x) \, y']' + q(x) \, y = \lambda \, w(x) \, y",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.formula_box(sl_eq)
        self.play(Write(sl_eq), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(sl_eq), run_time=0.3)

        items = [
            MathTex(r"p(x) > 0", r"\text{: coefficient function}", font_size=HEADING_SIZE, color=WHITE),
            MathTex(r"q(x)", r"\text{: potential function}", font_size=HEADING_SIZE, color=WHITE),
            MathTex(r"w(x) > 0", r"\text{: weight function}", font_size=HEADING_SIZE, color=WHITE),
            Text("Boundary conditions complete the problem", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: Every Separation Problem Is Sturm-Liouville
    # ------------------------------------------------------------------ #
    def scene3_all_sl_problems(self):
        self.ly.section_divider("2", "Every Separation Gives Sturm-Liouville")
        self.add_subcaption(
            "The power of Sturm-Liouville theory is that every "
            "eigenvalue problem from separation of variables fits "
            "this form. The simple case: p equals 1, q equals 0, "
            "w equals 1 gives us the Fourier eigenfunctions. "
            "Bessel's equation uses p equals x and w equals x. "
            "Legendre's equation uses p equals 1 minus x squared. "
            "Fourier, Bessel, Legendre, Chebyshev: all are "
            "Sturm-Liouville eigenfunction problems.",
            duration=14,
        )
        title = self.ly.title("Every Separation Gives Sturm-Liouville")

        items = [
            Text("Fourier:  p=1, q=0, w=1", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Bessel:   p=x, q=0, w=x", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Legendre: p=1-x^2, q=0, w=1", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("ALL special functions are SL eigenfunctions", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Self-Adjoint Operators
    # ------------------------------------------------------------------ #
    def scene4_self_adjoint(self):
        self.ly.section_divider("3", "Self-Adjointness")
        self.add_subcaption(
            "Define the Sturm-Liouville operator L acting on "
            "y as negative the derivative of p times y prime, "
            "plus q times y. Self-adjointness means the "
            "operator equals its own adjoint. In matrix terms, "
            "a symmetric matrix has real eigenvalues and "
            "orthogonal eigenvectors. The same holds for "
            "self-adjoint differential operators. This "
            "property is the foundation for everything that "
            "follows.",
            duration=14,
        )
        title = self.ly.title("Why Self-Adjointness Matters")

        # Show the operator
        op = MathTex(
            r"\mathcal{L}[y] = -[p(x) \, y']' + q(x) \, y",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.formula_box(op)
        self.play(Write(op), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(op), run_time=0.3)

        items = [
            Text("Self-adjoint: L equals its own adjoint", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Boundary conditions enforce this", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Analogue: symmetric matrix in linear algebra", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Symmetric = real eigenvalues, orthogonal eigenvectors", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: Real Eigenvalues and Orthogonal Eigenfunctions
    # ------------------------------------------------------------------ #
    def scene5_key_properties(self):
        self.ly.section_divider("4", "Key Properties")
        self.add_subcaption(
            "Self-adjointness gives three key properties. "
            "First, all eigenvalues are real. Second, "
            "eigenfunctions corresponding to different "
            "eigenvalues are orthogonal with respect to the "
            "weight function w. Third, eigenvalues are "
            "discrete, bounded below, and grow to infinity. "
            "Together these properties mean the eigenfunctions "
            "form a complete orthogonal basis.",
            duration=13,
        )
        title = self.ly.title("The Key Properties")

        items = [
            Text("1. All eigenvalues are real", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Eigenfunctions are orthogonal (weighted)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            MathTex(
                r"\int_a^b w(x) \, y_n(x) \, y_m(x) \, dx = 0",
                font_size=HEADING_SIZE, color=ACCENT,
            ),
            Text("3. Eigenvalues: discrete, bounded below, grow to infinity", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Completeness and Eigenfunction Expansions
    # ------------------------------------------------------------------ #
    def scene6_completeness(self):
        self.ly.section_divider("5", "Completeness")
        self.add_subcaption(
            "Completeness means that any reasonable function "
            "on the interval can be expanded in eigenfunctions. "
            "The coefficients are inner products with the "
            "weight function. This generalizes Fourier series: "
            "the sine and cosine functions are just the "
            "eigenfunctions of the simplest Sturm-Liouville "
            "problem. Bessel series and Legendre series are "
            "also eigenfunction expansions, each with their "
            "own weight function.",
            duration=14,
        )
        title = self.ly.title("Completeness: Every Function Expands")

        # Show the expansion formula
        expansion = MathTex(
            r"f(x) = \sum_{n=1}^{\infty} c_n \, y_n(x)",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.formula_box(expansion)
        self.play(Write(expansion), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(expansion), run_time=0.3)

        items = [
            Text("Fourier series: eigenfunctions of simplest SL problem", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Bessel series: eigenfunctions on a disk", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Legendre series: eigenfunctions on a sphere", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("All unified by Sturm-Liouville completeness", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Why This Matters for PDEs
    # ------------------------------------------------------------------ #
    def scene7_pde_payoff(self):
        self.add_subcaption(
            "Here is the payoff. When you separate variables "
            "in any linear PDE, you get a Sturm-Liouville "
            "problem. The theory guarantees real eigenvalues, "
            "orthogonal eigenfunctions, and completeness. So "
            "any initial condition can be expanded in "
            "eigenfunctions. Fourier series solve the heat "
            "equation on a rod. Bessel series solve the heat "
            "equation on a disk. Same theory, different "
            "geometry.",
            duration=14,
        )
        title = self.ly.title("The Payoff: Solving PDEs in Full Generality")

        items = [
            Text("Separation of variables produces a SL problem", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Theory guarantees: real eigenvalues, orthogonal basis", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Completeness: ANY initial condition expands", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Fourier = rod, Bessel = disk, Legendre = sphere", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary(self):
        self.add_subcaption(
            "Sturm-Liouville theory is the deep reason why "
            "separation of variables works for PDEs. The "
            "Sturm-Liouville form unifies all eigenvalue "
            "problems that arise from separation. "
            "Self-adjointness gives real eigenvalues and "
            "orthogonal eigenfunctions. Completeness means "
            "we can expand any initial condition. Fourier, "
            "Bessel, Legendre: they are all the same theory "
            "in different clothing. Next, we study Green's "
            "functions.",
            duration=14,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("SL form unifies all PDE eigenvalue problems", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Self-adjointness: real eigenvalues, orthogonal basis", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Completeness: any initial condition expands", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Fourier, Bessel, Legendre: same theory, different geometry", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        play_outro(self, "Green's Functions", "Partial Differential Equations")
