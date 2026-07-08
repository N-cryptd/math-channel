"""
Video 110: Series of Functions
TEMPLATE v2 -- Professional quality Manim script

Playlist: Real Analysis I (Video 12 of 12) -- FINAL VIDEO
Class: Video110_SeriesOfFunctions

QUALITY RULES (enforced):
  1. Max 5 visible elements per scene at any time
  2. Use LayoutEngine for ALL positioning -- no manual .shift() or .to_edge()
  3. Progressive disclosure: add items one at a time
  4. Use consistent animation vocabulary (Write, FadeIn, Create, etc.)
  5. Each add_subcaption() duration ~ words / 2.5 seconds
  6. Call ly.clear() between scenes
  7. Raw strings for MathTex with single backslashes
  8. No font= parameter on MathTex (only on Text)
"""

from manim import *
import numpy as np
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits, clamp_position


class Video110_SeriesOfFunctions(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_series_convergence()
        self.scene3_m_test()
        self.scene4_term_by_term_integration()
        self.scene5_term_by_term_differentiation()
        self.scene6_power_series()
        self.scene7_big_picture()
        self.scene8_summary()

    # --- Scene 1: Hook ---
    def scene1_hook(self):
        self.add_subcaption(
            "When can you swap a sum and an integral? "
            "When can you differentiate term by term? "
            "The answer: when the series converges uniformly. "
            "Today we go from sequences of functions to series "
            "of functions, and unlock the operations that make "
            "power series so powerful. "
            "This is the final video of Real Analysis One.",
            duration=20,
        )
        play_intro(self, "Series of Functions", "Real Analysis I")

        title = self.ly.title("The Key Question")

        question = Text(
            "When can you swap the sum and the integral?",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(question, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(question), run_time=SLOW)
        self.wait(0.5)

        # Animated: partial sums building up
        axes = Axes(
            x_range=[-0.3, 1.5, 0.5], y_range=[-0.3, 2.5, 1],
            x_length=4.5, y_length=2.0,
            axis_config={"include_numbers": False, "font_size": 14, "stroke_width": 1.5},
        )
        self.ly.safe_place(axes, direction=DOWN, anchor=question, buff=0.3)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        # Show partial sums of geometric series: S_N(x) = 1 + x + x^2 + ... + x^N
        colors = [DIM, PRIMARY, SECONDARY, ACCENT]
        for idx, N in enumerate([0, 1, 3, 10]):
            S_val = lambda x, nn=N: sum([x**k for k in range(nn + 1)])
            graph = axes.plot(S_val, x_range=[0, 0.95], color=colors[idx],
                             stroke_width=2.5 if idx == 3 else 1.5)
            self.play(Create(graph), run_time=FAST)
            self.wait(0.2)

        self.wait(0.5)
        self.ly.clear()

    # --- Scene 2: Convergence of Series of Functions ---
    def scene2_series_convergence(self):
        self.add_subcaption(
            "A series of functions is simply an infinite sum "
            "of functions. "
            "We define the partial sums: S sub N of x equals "
            "the sum from n equals 1 to N of f sub n of x. "
            "The series converges pointwise at x if the "
            "sequence of partial sums converges at x. "
            "The series converges uniformly if the partial "
            "sums converge uniformly. "
            "Everything from the previous video applies, "
            "just replace f sub n with S sub N.",
            duration=28,
        )
        self.ly.section_divider("1", "Convergence of Series of Functions")
        self.ly.clear()

        title = self.ly.title("Series of Functions")

        # Notation
        notation = MathTex(
            r"\sum_{n=1}^{\infty} f_n(x) = f_1(x) + f_2(x) + \cdots",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(notation, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(notation), run_time=SLOW)
        self.wait(0.3)

        # Partial sums definition
        partial = MathTex(
            r"S_N(x) = \sum_{n=1}^{N} f_n(x)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(partial, direction=DOWN, anchor=notation, buff=0.4)
        self.play(Write(partial), run_time=NORMAL)
        self.wait(0.3)

        # Pointwise convergence
        pw = MathTex(
            r"\sum f_n \to f \text{ pointwise} \iff S_N \to f \text{ pointwise}",
            font_size=SMALL_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(pw, direction=DOWN, anchor=partial, buff=0.3)
        self.play(Write(pw), run_time=NORMAL)
        self.wait(0.3)

        # Uniform convergence
        unif = MathTex(
            r"\sum f_n \to f \text{ uniformly} \iff S_N \to f \text{ uniformly}",
            font_size=SMALL_SIZE, color=ACCENT,
        )
        self.ly.safe_place(unif, direction=DOWN, anchor=pw, buff=0.3)
        self.play(Write(unif), run_time=NORMAL)
        self.wait(0.5)

        insight = Text(
            "Replace f_n with S_N and everything from Video 109 applies!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=unif, buff=0.3)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 3: Weierstrass M-Test ---
    def scene3_m_test(self):
        self.add_subcaption(
            "The Weierstrass M-test is the most important tool "
            "for proving uniform convergence of series. "
            "If for each n, the absolute value of f sub n of x "
            "is at most M sub n for all x in the domain, and "
            "the sum of M sub n converges, then the series of "
            "f sub n converges uniformly. "
            "The idea: find constants that bound each term "
            "from above, independent of x. "
            "If the bounding series converges, so does the "
            "original. "
            "Example: sum of x to the n over n factorial. "
            "Bound by one over n factorial, which converges.",
            duration=30,
        )
        self.ly.section_divider("2", "The Weierstrass M-Test")
        self.ly.clear()

        title = self.ly.title("The Weierstrass M-Test")

        # Theorem statement
        stmt = MathTex(
            r"|f_n(x)| \leq M_n\ \forall x \in E,\quad \sum M_n < \infty "
            r"\implies \sum f_n \text{ converges uniformly on } E",
            font_size=SMALL_SIZE, color=WHITE,
        )
        self.ly.safe_place(stmt, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(stmt), run_time=SLOW)
        self.wait(0.5)

        insight = Text(
            "Find constants M_n that bound |f_n(x)| independently of x",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=stmt, buff=0.4)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(1.0)

        # Remove insight, add example
        self.play(FadeOut(insight), run_time=FAST)

        example_title = Text(
            "Example: $\\sum x^n / n!$ on $[0,1]$",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(example_title, direction=DOWN, anchor=stmt, buff=0.4)
        self.play(Write(example_title), run_time=NORMAL)
        self.wait(0.3)

        example = MathTex(
            r"\left|\frac{x^n}{n!}\right| \leq \frac{1}{n!} = M_n,\quad \sum \frac{1}{n!} = e < \infty",
            font_size=SMALL_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(example, direction=DOWN, anchor=example_title, buff=0.3)
        self.play(Write(example), run_time=NORMAL)
        self.wait(0.3)

        result = Text(
            "M-test => uniform convergence on [0,1]",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=example, buff=0.3)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 4: Term-by-Term Integration ---
    def scene4_term_by_term_integration(self):
        self.add_subcaption(
            "Now the payoff. "
            "If the series converges uniformly on a closed "
            "interval a b, then you can integrate term by "
            "term. "
            "The integral of the sum equals the sum of the "
            "integrals. "
            "Proof: the difference between the integral of "
            "S sub N and the integral of f is bounded by "
            "b minus a times the supremum of S sub N minus "
            "f, which goes to zero by uniform convergence. "
            "Uniform convergence lets you pull the integral "
            "inside the sum.",
            duration=28,
        )
        self.ly.section_divider("3", "Term-by-Term Integration")
        self.ly.clear()

        title = self.ly.title("Term-by-Term Integration")

        # Theorem
        stmt = MathTex(
            r"\sum f_n \to f \text{ uniformly on } [a,b] "
            r"\implies \int_a^b \sum f_n = \sum \int_a^b f_n",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(stmt, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(stmt), run_time=SLOW)
        self.wait(0.5)

        # Proof
        proof = MathTex(
            r"\left|\int S_N - \int f\right| "
            r"\leq \int |S_N - f| "
            r"\leq (b-a)\, \sup |S_N - f| \to 0",
            font_size=SMALL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(proof, direction=DOWN, anchor=stmt, buff=0.4)
        self.play(Write(proof), run_time=NORMAL)
        self.wait(0.5)

        result = Text(
            "Uniform convergence => swap sum and integral!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=proof, buff=0.4)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 5: Term-by-Term Differentiation ---
    def scene5_term_by_term_differentiation(self):
        self.add_subcaption(
            "Differentiation is trickier. "
            "You need more than uniform convergence of the "
            "original series. "
            "Theorem: if the series converges pointwise, each "
            "f sub n is continuously differentiable, and the "
            "series of derivatives converges uniformly, then "
            "the derivative of the sum equals the sum of the "
            "derivatives. "
            "Why the extra condition? "
            "Because differentiation amplifies small errors. "
            "The derivative of x to the n is n times x to "
            "the n minus one, which grows with n. "
            "Integration smooths errors out, but "
            "differentiation magnifies them.",
            duration=32,
        )
        self.ly.section_divider("4", "Term-by-Term Differentiation")
        self.ly.clear()

        title = self.ly.title("Term-by-Term Differentiation")

        # Theorem
        stmt = MathTex(
            r"\sum f_n' \to g \text{ uniformly} "
            r"\implies \left(\sum f_n\right)' = \sum f_n' = g",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(stmt, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(stmt), run_time=SLOW)
        self.wait(0.3)

        # Conditions
        cond1 = Text(
            "Need: pointwise convergence of sum f_n",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(cond1, direction=DOWN, anchor=stmt, buff=0.3)
        self.play(Write(cond1), run_time=NORMAL)
        self.wait(0.2)

        cond2 = Text(
            "Need: UNIFORM convergence of sum f_n'",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(cond2, direction=DOWN, anchor=cond1, buff=0.2)
        self.play(Write(cond2), run_time=NORMAL)
        self.wait(0.3)

        # Why
        why = MathTex(
            r"\frac{d}{dx}\, x^n = n\, x^{n-1}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(why, direction=DOWN, anchor=cond2, buff=0.3)
        self.play(Write(why), run_time=NORMAL)
        self.wait(0.3)

        insight = Text(
            "Differentiation magnifies errors; integration smooths them!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=why, buff=0.3)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 6: Power Series ---
    def scene6_power_series(self):
        self.add_subcaption(
            "Now everything comes together with power series. "
            "A power series centered at c is: sum of a sub n "
            "times x minus c to the n. "
            "It has a radius of convergence R from the ratio "
            "test. "
            "Key result: a power series converges uniformly "
            "on any compact subset inside the open interval "
            "of convergence. "
            "Proof idea: use the M-test with M sub n equals "
            "a sub n times r to the n for any r less than R. "
            "This means: inside the radius, you can "
            "differentiate and integrate term by term, "
            "infinitely many times!",
            duration=32,
        )
        self.ly.section_divider("5", "Power Series")
        self.ly.clear()

        title = self.ly.title("Power Series: The Grand Finale")

        # Definition
        defn = MathTex(
            r"\sum_{n=0}^{\infty} a_n\, (x - c)^n",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(defn, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(defn), run_time=SLOW)
        self.wait(0.3)

        # Radius
        radius = MathTex(
            r"\text{Radius of convergence: } R = \frac{1}{\limsup |a_n|^{1/n}}",
            font_size=SMALL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(radius, direction=DOWN, anchor=defn, buff=0.4)
        self.play(Write(radius), run_time=NORMAL)
        self.wait(0.3)

        # Key result
        key = MathTex(
            r"\sum a_n x^n \text{ converges uniformly on } [-r, r] \text{ for any } r < R",
            font_size=SMALL_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=radius, buff=0.3)
        self.play(Write(key), run_time=NORMAL)
        self.wait(0.3)

        # M-test argument
        mtest = MathTex(
            r"|a_n x^n| \leq |a_n|\, r^n = M_n, \quad \sum M_n < \infty \text{ for } r < R",
            font_size=SMALL_SIZE, color=ACCENT,
        )
        self.ly.safe_place(mtest, direction=DOWN, anchor=key, buff=0.3)
        self.play(Write(mtest), run_time=NORMAL)
        self.wait(0.3)

        # Consequence
        result = Text(
            "Power series are infinitely differentiable inside (-R, R)!",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=mtest, buff=0.3)
        self.play(Write(result), run_time=SLOW)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 7: The Big Picture ---
    def scene7_big_picture(self):
        self.add_subcaption(
            "Let's see how everything connects. "
            "The Weierstrass M-test gives us uniform "
            "convergence. "
            "Uniform convergence of the series lets us swap "
            "sum and integral. "
            "Uniform convergence of the derivative series "
            "lets us swap sum and derivative. "
            "For power series, the M-test guarantees uniform "
            "convergence on compact subsets inside the "
            "radius. "
            "This unlocks term by term differentiation and "
            "integration, proving power series are infinitely "
            "differentiable. "
            "Uniform convergence is the key that unlocks "
            "all the operations.",
            duration=30,
        )
        title = self.ly.title("The Big Picture")

        items = [
            Text("M-test => uniform convergence",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Uniform convergence => swap sum and integral",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Uniform convergence of derivatives => swap sum and derivative",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Power series: uniform on compact subsets of (-R, R)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("=> Power series are C-infinity inside their radius!",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 8: Summary + Outro ---
    def scene8_summary(self):
        self.add_subcaption(
            "Key takeaways. "
            "One: a series of functions converges when its "
            "partial sums converge. "
            "Two: the Weierstrass M-test proves uniform "
            "convergence by comparison with a convergent "
            "numerical series. "
            "Three: uniform convergence lets you integrate "
            "term by term. "
            "Four: uniform convergence of the derivatives "
            "lets you differentiate term by term. "
            "Five: power series converge uniformly on "
            "compact subsets, so they are infinitely "
            "differentiable inside their radius of "
            "convergence. "
            "This completes Real Analysis One. "
            "Twelve videos covering the foundations of "
            "rigorous calculus. Thank you for watching!",
            duration=38,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("1. Series converge via partial sums S_N",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Weierstrass M-test: |f_n| <= M_n, sum M_n < inf",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Uniform => integrate term by term",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Uniform of derivatives => differentiate term by term",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5. Power series are C-infinity inside (-R, R)",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.0)

        # Celebration note
        self.ly.clear()
        celebration = Text(
            "Real Analysis I Complete!",
            font_size=TITLE_SIZE, color=ACCENT, font=SANS,
            weight=BOLD,
        )
        self.ly.center_in_content(celebration)
        self.play(Write(celebration), run_time=SLOW)
        self.wait(1.0)

        sub = Text(
            "12 videos. From the completeness of the reals to power series.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(sub, direction=DOWN, anchor=celebration, buff=0.5)
        self.play(Write(sub), run_time=NORMAL)
        self.wait(1.0)

        next_up = Text(
            "Next: Abstract Algebra I or Complex Analysis",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(next_up, direction=DOWN, anchor=sub, buff=0.3)
        self.play(Write(next_up), run_time=NORMAL)
        self.wait(1.0)

        play_outro(self, "Real Analysis I Complete!", "Real Analysis I")
