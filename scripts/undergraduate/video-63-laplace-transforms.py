"""
Video 63: Laplace Transforms
Ordinary Differential Equations -- Video 10 of N

Covers: motivation (calculus to algebra), definition, examples (exponential,
constants, polynomials), key properties (linearity, derivative transform),
solving an ODE with Laplace, Heaviside step function, summary.

Competitive analysis: channel-analysis/improvements.md "2026-06-13 — Laplace Transforms"
Plan: planning/video-63-laplace-transforms.md

Render draft:  manim -ql scripts/undergraduate/video-63-laplace-transforms.py Video63_LaplaceTransforms
Render final:  manim -qh scripts/undergraduate/video-63-laplace-transforms.py Video63_LaplaceTransforms
"""

from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video63_LaplaceTransforms(Scene):
    """Full video: Introduction to Laplace Transforms for ODEs."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_example_exponential()
        self.scene4_example_constants()
        self.scene5_properties()
        self.scene6_solve_ode()
        self.scene7_heaviside()
        self.scene8_summary()

    # -- Scene 1: Hook -- When Algebra Beats Calculus --
    def scene1_hook(self):
        self.add_subcaption(
            "We have solved many differential equations using techniques "
            "like separation of variables, integrating factors, and "
            "variation of parameters. But there is a powerful tool that "
            "turns calculus into pure algebra.",
            duration=22,
        )
        play_intro(self, "Laplace Transforms",
                   "Ordinary Differential Equations")

        title = self.ly.title("From Calculus to Algebra")
        self.wait(4)

        self.add_subcaption(
            "Consider a second-order differential equation with a forcing "
            "function. Direct methods require finding a particular solution "
            "and a homogeneous solution, then matching initial conditions.",
            duration=18,
        )

        ode_hard = MathTex(
            r"y'' + 3y' + 2y = f(t)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.play(FadeIn(ode_hard, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(ode_hard, DOWN, anchor=title)
        self.wait(3)

        self.add_subcaption(
            "With the Laplace transform, derivatives become "
            "multiplication by s, and the differential equation becomes "
            "a simple algebraic equation that we can solve for Y of s.",
            duration=18,
        )

        ode_easy = MathTex(
            r"(s^2 + 3s + 2)\,Y = F(s)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.play(Transform(ode_hard, ode_easy), run_time=NORMAL)
        self.wait(3)

        self.add_subcaption(
            "In this video, we will learn the definition of the Laplace "
            "transform, compute several examples, discover the key "
            "properties, and use it to solve a differential equation.",
            duration=18,
        )

        question = Text(
            "What if we could solve ODEs with algebra?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(question, DOWN, anchor=ode_hard)
        self.wait(4)

        self.ly.clear()

    # -- Scene 2: The Definition --
    def scene2_definition(self):
        self.add_subcaption(
            "The Laplace transform takes a function of t and produces "
            "a new function of s. We define it as the integral from zero "
            "to infinity of e to the negative s t times f of t dt.",
            duration=18,
        )

        title = self.ly.title("The Laplace Transform")

        definition = MathTex(
            r"\mathcal{L}\{f(t)\}",
            r"=",
            r"\int_0^{\infty}",
            r"e^{-st}",
            r"f(t)",
            r"\, dt",
            r"=",
            r"F(s)",
            font_size=HEADING_SIZE,
            color=WHITE,
        )
        self.play(Write(definition), run_time=SLOW)
        self.ly.safe_place(definition, DOWN, anchor=title)
        self.wait(4)

        self.add_subcaption(
            "Think of it as a mapping from the time domain to the "
            "s domain. The original function f of t lives in the time "
            "domain, and the transformed function F of s lives in the "
            "frequency domain.",
            duration=16,
        )

        orig_label = Text(
            "f(t): time domain",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.play(FadeIn(orig_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(orig_label, DOWN, anchor=definition)
        self.wait(3)

        self.add_subcaption(
            "The exponential kernel e to the negative s t is the bridge "
            "between the two domains. It weights the function at each "
            "time point and sums them up.",
            duration=14,
        )

        trans_label = Text(
            "F(s): frequency domain",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.play(FadeIn(trans_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(trans_label, DOWN, anchor=orig_label)
        self.wait(3)

        self.add_subcaption(
            "The Laplace transform exists when this improper integral "
            "converges. For most functions we encounter, it converges "
            "for sufficiently large values of s.",
            duration=14,
        )

        self.wait(3)
        self.ly.clear()

    # -- Scene 3: Example — Exponential --
    def scene3_example_exponential(self):
        self.add_subcaption(
            "Let us start with the simplest non-trivial example. "
            "We want to find the Laplace transform of e to the a t.",
            duration=14,
        )

        title = self.ly.title("Example: f(t) = e^{at}")

        step1 = MathTex(
            r"\mathcal{L}\{e^{at}\}",
            r"=",
            r"\int_0^{\infty}",
            r"e^{-(s-a)t}",
            r"\, dt",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.play(Write(step1), run_time=NORMAL)
        self.ly.safe_place(step1, DOWN, anchor=title)
        self.wait(3)

        self.add_subcaption(
            "Evaluating this integral, we get e to the negative s "
            "minus a times t, divided by negative s minus a, evaluated "
            "from zero to infinity.",
            duration=16,
        )

        step2 = MathTex(
            r"=",
            r"\left[",
            r"\frac{e^{-(s-a)t}}{-(s-a)}",
            r"\right]_0^{\infty}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.play(Transform(step1, step2), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "At infinity, the exponential decays to zero when s is "
            "greater than a. At zero, we get one over s minus a.",
            duration=12,
        )

        self.wait(3)

        self.add_subcaption(
            "The final result is one over s minus a, valid when s is "
            "greater than a, which is the region of convergence.",
            duration=12,
        )

        result = MathTex(
            r"=",
            r"\frac{1}{s - a}",
            r", \quad s > a",
            font_size=HEADING_SIZE,
        )
        result[0].set_color(WHITE)
        result[1].set_color(ACCENT)
        result[2].set_color(DIM)
        self.play(Transform(step1, result), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # -- Scene 4: Constants and Powers --
    def scene4_example_constants(self):
        self.add_subcaption(
            "Now let us compute some simpler cases. The Laplace transform "
            "of the constant function 1 is the integral from zero to "
            "infinity of e to the negative s t dt, which equals 1 over s.",
            duration=18,
        )

        title = self.ly.title("Constants and Powers")

        const_result = MathTex(
            r"\mathcal{L}\{1\}",
            r"=",
            r"\frac{1}{s}",
            r", \quad s > 0",
            font_size=HEADING_SIZE,
        )
        const_result[2].set_color(ACCENT)
        self.play(Write(const_result), run_time=NORMAL)
        self.ly.safe_place(const_result, DOWN, anchor=title)
        self.wait(4)

        self.add_subcaption(
            "For f of t equals t, we apply integration by parts or "
            "the derivative property. The result is 1 over s squared. "
            "This pattern continues for higher powers of t.",
            duration=16,
        )

        t_result = MathTex(
            r"\mathcal{L}\{t\}",
            r"=",
            r"\frac{1}{s^2}",
            r", \quad s > 0",
            font_size=HEADING_SIZE,
        )
        t_result[2].set_color(ACCENT)
        self.play(Transform(const_result, t_result), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "In general, the Laplace transform of t to the n is n "
            "factorial divided by s to the n plus 1. This connects "
            "to the Gamma function, where n factorial equals Gamma "
            "of n plus 1.",
            duration=16,
        )

        pattern = MathTex(
            r"\mathcal{L}\{t^n\}",
            r"=",
            r"\frac{n!}{s^{n+1}}",
            font_size=HEADING_SIZE,
        )
        pattern[2].set_color(ACCENT)
        self.play(Transform(const_result, pattern), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # -- Scene 5: Key Properties --
    def scene5_properties(self):
        self.ly.section_divider(5, "Key Properties")

        self.add_subcaption(
            "The Laplace transform is linear, just like the integral. "
            "The transform of a linear combination is the same linear "
            "combination of the transforms.",
            duration=16,
        )

        title = self.ly.title("Linearity")

        linearity = MathTex(
            r"\mathcal{L}\{a\,f + b\,g\}",
            r"=",
            r"a\,F(s)",
            r"+",
            r"b\,G(s)",
            font_size=HEADING_SIZE,
        )
        linearity[2].set_color(SECONDARY)
        linearity[4].set_color(SECONDARY)
        self.play(Write(linearity), run_time=NORMAL)
        self.ly.safe_place(linearity, DOWN, anchor=title)
        self.wait(5)
        self.ly.clear()

        # The magic property
        self.add_subcaption(
            "The key property that makes Laplace transforms useful for "
            "ODEs is the derivative property. The transform of the "
            "derivative f prime equals s times F of s minus f of zero.",
            duration=18,
        )

        title2 = self.ly.title("The Derivative Property")

        deriv1 = MathTex(
            r"\mathcal{L}\{f'(t)\}",
            r"=",
            r"s\,F(s)",
            r"-",
            r"f(0)",
            font_size=HEADING_SIZE,
        )
        deriv1[2].set_color(SECONDARY)
        deriv1[4].set_color(ACCENT)
        self.play(Write(deriv1), run_time=NORMAL)
        self.ly.safe_place(deriv1, DOWN, anchor=title2)
        self.wait(4)

        self.add_subcaption(
            "For the second derivative, we apply the property twice. "
            "The transform of f double prime equals s squared F of s "
            "minus s f of zero minus f prime of zero.",
            duration=18,
        )

        deriv2 = MathTex(
            r"\mathcal{L}\{f''(t)\}",
            r"=",
            r"s^2 F(s)",
            r"-",
            r"s\,f(0)",
            r"-",
            r"f'(0)",
            font_size=HEADING_SIZE,
        )
        deriv2[2].set_color(SECONDARY)
        deriv2[4].set_color(ACCENT)
        deriv2[6].set_color(ACCENT)
        self.play(Transform(deriv1, deriv2), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "This is the magic: derivatives become multiplication by s, "
            "and initial conditions are automatically included. "
            "A differential equation becomes a polynomial equation.",
            duration=16,
        )

        magic = Text(
            "Derivatives become multiplication by s!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.play(FadeIn(magic, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(magic, DOWN, anchor=deriv1)
        self.wait(5)

        self.ly.clear()

    # -- Scene 6: Solving an ODE --
    def scene6_solve_ode(self):
        self.add_subcaption(
            "Now let us use the Laplace transform to solve a differential "
            "equation. Consider y prime plus 3 y equals 6, with y of "
            "zero equals 2.",
            duration=16,
        )

        title = self.ly.title("Solving an ODE")

        ode = MathTex(
            r"y' + 3y = 6",
            r", \quad y(0) = 2",
            font_size=HEADING_SIZE,
        )
        ode[0].set_color(WHITE)
        ode[1].set_color(ACCENT)
        self.play(Write(ode), run_time=NORMAL)
        self.ly.safe_place(ode, DOWN, anchor=title)
        self.wait(4)

        # Step 1: Transform both sides
        self.add_subcaption(
            "Step one: transform both sides. Using the derivative "
            "property, y prime becomes s Y minus y of zero. The "
            "constant 6 becomes 6 over s.",
            duration=16,
        )

        step1_label = Text(
            "Step 1: Transform both sides",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.play(FadeIn(step1_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(step1_label, DOWN, anchor=ode)
        self.wait(2)

        transformed = MathTex(
            r"sY(s) - 2 + 3Y(s) = \frac{6}{s}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.play(Write(transformed), run_time=NORMAL)
        self.ly.safe_place(transformed, DOWN, anchor=step1_label)
        self.wait(5)

        self.play(FadeOut(step1_label), run_time=FAST)

        # Step 2: Solve algebraically
        self.add_subcaption(
            "Step two: collect terms. Factor out Y of s to get "
            "s plus 3 times Y of s equals 6 over s plus 2.",
            duration=14,
        )

        step2_label = Text(
            "Step 2: Solve for Y(s)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.play(Transform(step1_label, step2_label), run_time=FAST)
        self.ly.safe_place(step2_label, DOWN, anchor=ode)
        self.wait(2)

        solved = MathTex(
            r"Y(s) = \frac{2s + 6}{s(s+3)}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.play(Transform(transformed, solved), run_time=NORMAL)
        self.wait(5)

        self.play(FadeOut(step2_label), run_time=FAST)

        # Step 3: Partial fractions
        self.add_subcaption(
            "Step three: partial fractions. The numerator 2 s plus 6 "
            "factors as 2 times s plus 3, which cancels with the "
            "denominator. So Y of s simplifies to 2 over s.",
            duration=18,
        )

        step3_label = Text(
            "Step 3: Partial fractions",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.play(Transform(step2_label, step3_label), run_time=FAST)
        self.ly.safe_place(step3_label, DOWN, anchor=ode)
        self.wait(2)

        simplified = MathTex(
            r"Y(s) = \frac{2(s+3)}{s(s+3)} = \frac{2}{s}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.play(Transform(solved, simplified), run_time=NORMAL)
        self.wait(5)

        self.play(FadeOut(step3_label), run_time=FAST)

        # Step 4: Invert
        self.add_subcaption(
            "Step four: invert. The inverse Laplace transform of "
            "2 over s is simply the constant function 2. So our "
            "solution is y of t equals 2.",
            duration=16,
        )

        step4_label = Text(
            "Step 4: Invert",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.play(Transform(step3_label, step4_label), run_time=FAST)
        self.ly.safe_place(step4_label, DOWN, anchor=ode)
        self.wait(2)

        solution = MathTex(
            r"y(t) = 2",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.play(Transform(simplified, solution), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "Checking: y prime is zero, so y prime plus 3 y equals "
            "zero plus 6 equals 6. And y of zero equals 2. Both "
            "conditions are satisfied!",
            duration=14,
        )

        verify = Text(
            "Verify: 0 + 3(2) = 6 = RHS, and y(0) = 2",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.play(FadeIn(verify, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(verify, DOWN, anchor=solution)
        self.wait(5)

        self.ly.clear()

    # -- Scene 7: Heaviside Step Function --
    def scene7_heaviside(self):
        self.add_subcaption(
            "In the real world, systems often experience sudden changes. "
            "A switch turns on, a force is applied, or a voltage jumps. "
            "The Heaviside step function models these jumps.",
            duration=16,
        )

        title = self.ly.title("Piecewise Functions")

        self.add_subcaption(
            "The Heaviside step function H of t minus a equals zero "
            "when t is less than a, and equals one when t is greater "
            "than or equal to a.",
            duration=14,
        )

        heaviside = MathTex(
            r"H(t-a) =",
            r"\begin{cases}"
            r"0 & t < a \\"
            r"1 & t \geq a"
            r"\end{cases}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.play(Write(heaviside), run_time=NORMAL)
        self.ly.safe_place(heaviside, DOWN, anchor=title)
        self.wait(5)

        self.add_subcaption(
            "The key Laplace transform property for the step function "
            "is the time-shift property. The transform of the shifted "
            "function H of t minus a times f of t minus a equals "
            "e to the negative a s times F of s.",
            duration=20,
        )

        shift_prop = MathTex(
            r"\mathcal{L}\{H(t-a)\,f(t-a)\}",
            r"=",
            r"e^{-as}\,F(s)",
            font_size=HEADING_SIZE,
        )
        shift_prop[2].set_color(ACCENT)
        self.play(Transform(heaviside, shift_prop), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "This exponential factor e to the negative a s is what makes "
            "Laplace transforms so powerful for piecewise and discontinuous "
            "forcing functions.",
            duration=14,
        )

        insight = Text(
            "Laplace handles piecewise inputs naturally!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(insight, DOWN, anchor=shift_prop)
        self.wait(5)

        self.ly.clear()

    # -- Scene 8: Summary --
    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap what we have learned about Laplace transforms. "
            "They convert functions from the time domain to the frequency "
            "domain, turning calculus into algebra.",
            duration=14,
        )

        title = self.ly.title("What We Learned")

        points = [
            Text(
                "1. Laplace transform maps t-domain to s-domain",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(points, start_from=title)
        self.wait(3)

        self.add_subcaption(
            "Derivatives become multiplication by s, which means "
            "differential equations become algebraic equations.",
            duration=10,
        )

        points2 = [
            Text(
                "2. Derivatives become multiplication by s",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(points2, start_from=title)
        self.wait(3)

        self.add_subcaption(
            "ODEs become algebraic equations in s. We solve them "
            "using standard algebra, then invert the transform.",
            duration=12,
        )

        points3 = [
            Text(
                "3. ODEs become algebraic equations in s",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(points3, start_from=title)
        self.wait(3)

        self.add_subcaption(
            "Inversion is done through partial fractions and table "
            "lookup. The Heaviside step function extends this to "
            "piecewise inputs.",
            duration=12,
        )

        points4 = [
            Text(
                "4. Invert via partial fractions + table lookup",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(points4, start_from=title)
        self.wait(4)

        self.add_subcaption(
            "Laplace transforms are especially powerful for equations "
            "with discontinuous forcing, initial value problems, and "
            "systems of differential equations.",
            duration=14,
        )

        self.ly.clear()

        self.add_subcaption(
            "Thank you for watching! In the next video, we will apply "
            "Laplace transforms to systems of differential equations.",
            duration=10,
        )

        play_outro(self, "Systems of ODEs",
                   "Ordinary Differential Equations")
