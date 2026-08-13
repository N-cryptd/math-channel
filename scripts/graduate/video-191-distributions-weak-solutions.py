"""
Video 191: Distributions & Weak Solutions -- Partial Differential Equations Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video191_DistributionsWeakSolutions

Topics: Why classical solutions are not enough,
        The Dirac delta as a distribution,
        Test functions and distributional derivatives,
        Weak form of PDEs and weak solutions,
        Connection to Green's functions and Sobolev spaces.

Prerequisites: Videos 184-190 (PDE intro through Green's Functions),
               Real Analysis (99-110), Functional Analysis (162-173).

Quality Rules (mandatory):
1. Max 5 visible elements per scene
2. Use LayoutEngine for ALL positioning
3. Progressive disclosure
4. Narration timing ~12 words / 5s
5. Call ly.clear() between scenes
6. MathTex: raw strings with single backslashes
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


class Video191_DistributionsWeakSolutions(Scene):
    """Distributions & Weak Solutions -- PDE Playlist."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_why_weak()
        self.scene3_dirac_delta()
        self.scene4_test_functions()
        self.scene5_weak_form()
        self.scene6_weak_solutions()
        self.scene7_connections()
        self.scene8_summary()

    # ------------------------------------------------------------------ #
    # Scene 1: Hook
    # ------------------------------------------------------------------ #
    def scene1_hook(self):
        self.add_subcaption(
            "Some PDE solutions are not smooth enough to satisfy "
            "the equation in the classical sense. Shock waves in "
            "fluids, cracks in solids, and point charges in "
            "electrostatics all require a broader notion of "
            "solution. Welcome to the world of distributions "
            "and weak solutions.",
            duration=9,
        )
        play_intro(self, "Distributions & Weak Solutions", "Partial Differential Equations")

        title = self.ly.title("Beyond Classical Solutions")

        items = [
            Text("Shock waves are not differentiable", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Point charges are not functions", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("We need a broader framework", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 2: Why Classical Solutions Fail
    # ------------------------------------------------------------------ #
    def scene2_why_weak(self):
        self.ly.section_divider("1", "The Problem with Classical Solutions")
        self.add_subcaption(
            "A classical solution must be differentiable enough "
            "for every derivative in the PDE to exist pointwise. "
            "But many physically meaningful solutions have "
            "discontinuities or singularities. We need to "
            "weaken the requirements while keeping the physics.",
            duration=8,
        )
        title = self.ly.title("The Problem with Classical Solutions")

        items = [
            Text("Classical: derivatives exist pointwise", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Shock: velocity has a jump discontinuity", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Point charge: potential is 1/r (singular!)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 3: The Dirac Delta
    # ------------------------------------------------------------------ #
    def scene3_dirac_delta(self):
        self.ly.section_divider("2", "The Dirac Delta")
        self.add_subcaption(
            "The Dirac delta is not a function. It is a distribution "
            "that picks out the value of a test function at a "
            "specific point. We write it as delta of x, and its "
            "defining property is that its integral against any "
            "test function gives the function's value at zero.",
            duration=9,
        )
        title = self.ly.title("The Dirac Delta")

        delta_prop = MathTex(
            r"\int_{-\infty}^{\infty} \delta(x - \xi) \, \phi(x) \, dx = \phi(\xi)",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.formula_box(delta_prop)
        self.play(Write(delta_prop), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(delta_prop), run_time=0.3)

        items = [
            Text("Not a function: a distribution", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Picks out the value at a specific point", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Derivative of the Heaviside step function", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 4: Test Functions
    # ------------------------------------------------------------------ #
    def scene4_test_functions(self):
        self.ly.section_divider("3", "Test Functions")
        self.add_subcaption(
            "Distributions are defined by how they act on test "
            "functions. A test function is infinitely differentiable "
            "and has compact support, meaning it is zero outside "
            "a finite region. The space of test functions is called "
            "D, and distributions live in its dual space D*.",
            duration=9,
        )
        title = self.ly.title("Test Functions")

        items = [
            Text("Infinitely differentiable (C-infinity)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Compact support (zero outside finite region)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Distribution: linear functional on test functions", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 5: The Weak Form
    # ------------------------------------------------------------------ #
    def scene5_weak_form(self):
        self.ly.section_divider("4", "The Weak Form of a PDE")
        self.add_subcaption(
            "The weak form of a PDE moves derivatives from the "
            "solution onto the test function using integration by "
            "parts. This means the solution only needs to be "
            "integrable, not differentiable. The weak form is "
            "the foundation of the finite element method.",
            duration=9,
        )
        title = self.ly.title("The Weak Form of a PDE")

        weak = MathTex(
            r"\int_\Omega \nabla u \cdot \nabla \phi \, dx = \int_\Omega f \, \phi \, dx",
            r"\quad \forall \phi \in D",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.formula_box(weak)
        self.play(Write(weak), run_time=NORMAL)

        weak_note = Text(
            "Derivatives moved from u to test function phi",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(weak_note, direction=DOWN, anchor=weak, buff=0.3)
        self.play(FadeIn(weak_note, shift=LEFT * 0.15), run_time=FAST)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 6: Weak Solutions
    # ------------------------------------------------------------------ #
    def scene6_weak_solutions(self):
        self.ly.section_divider("5", "Weak Solutions")
        self.add_subcaption(
            "A weak solution satisfies the weak form of the PDE "
            "for all test functions. It does not need to be "
            "classically differentiable. The concept of weak "
            "solutions is essential for the modern theory of "
            "PDEs, and it underpins numerical methods like the "
            "finite element method.",
            duration=10,
        )
        title = self.ly.title("What is a Weak Solution?")

        items = [
            Text("Satisfies weak form for all test functions", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Only needs to be integrable, not differentiable", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Foundation of the finite element method (FEM)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Connects to Sobolev spaces and functional analysis", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 7: Connections
    # ------------------------------------------------------------------ #
    def scene7_connections(self):
        self.add_subcaption(
            "Distributions and weak solutions connect back to "
            "many topics we have studied. The Dirac delta appears "
            "in Green's functions. Weak solutions live in Sobolev "
            "spaces, which we encountered in functional analysis. "
            "The Lax-Milgram theorem guarantees existence and "
            "uniqueness of weak solutions.",
            duration=10,
        )
        title = self.ly.title("Connections to Earlier Topics")

        items = [
            Text("Dirac delta: foundation of Green's functions", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Weak solutions: live in Sobolev spaces (Video 173)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Lax-Milgram: existence and uniqueness", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

    # ------------------------------------------------------------------ #
    # Scene 8: Summary and Outro
    # ------------------------------------------------------------------ #
    def scene8_summary(self):
        self.add_subcaption(
            "Classical solutions require differentiability, but "
            "many physical problems need less regular solutions. "
            "Distributions generalize functions. The weak form "
            "moves derivatives to test functions. Weak solutions "
            "only need integrability. Next, numerical methods.",
            duration=9,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("Classical solutions sometimes fail", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Dirac delta: distribution, not function", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Weak form: derivatives on test functions", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Weak solutions: only need integrability", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1.0)
        self.ly.clear()

        play_outro(self, "Numerical Methods for PDEs", "Partial Differential Equations")
