"""
Video 109: Pointwise vs Uniform Convergence
TEMPLATE v2 -- Professional quality Manim script

Playlist: Real Analysis I (Video 11 of 12)
Class: Video109_PointwiseUniformConvergence

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


class Video109_PointwiseUniformConvergence(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_pointwise()
        self.scene3_uniform()
        self.scene4_xn_example()
        self.scene5_uniform_continuous()
        self.scene6_interchange()
        self.scene7_dini()
        self.scene8_comparison()
        self.scene9_summary()

    # --- Scene 1: Hook ---
    def scene1_hook(self):
        self.add_subcaption(
            "A sequence of functions can converge to a limit "
            "function. But HOW it converges matters deeply. "
            "Pointwise convergence and uniform convergence "
            "look similar but have profoundly different "
            "consequences. "
            "Today we define both, see why the difference "
            "matters, and discover that uniform convergence "
            "preserves continuity and lets us interchange "
            "limits with integrals.",
            duration=20,
        )
        play_intro(self, "Pointwise vs Uniform Convergence", "Real Analysis I")

        title = self.ly.title("Two Kinds of Convergence")

        # Show two sequences of functions converging
        axes = Axes(
            x_range=[-0.3, 3.5, 1], y_range=[-0.3, 2.5, 1],
            x_length=5.5, y_length=2.5,
            axis_config={"include_numbers": False, "font_size": 16, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        # Nice convergence: f_n(x) = 1/(1+nx) → 0 pointwise (for x>0)
        for n in [1, 3, 8, 20]:
            graph = axes.plot(
                lambda x, nn=n: 1.0 / (1 + nn * x), x_range=[0.05, 3], color=SECONDARY,
            )
            self.play(Create(graph), run_time=FAST)
            self.wait(0.2)

        note = Text(
            "The curves approach a limit. But how?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=axes, buff=0.1)
        self.play(Write(note), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 2: Pointwise Convergence ---
    def scene2_pointwise(self):
        self.add_subcaption(
            "Pointwise convergence. "
            "A sequence f sub n converges pointwise to f "
            "if for each fixed x, the sequence of numbers "
            "f sub n of x converges to f of x. "
            "Formally: for every x and every epsilon, "
            "there exists N such that for all n at least N, "
            "the absolute value of f sub n of x minus f of x "
            "is less than epsilon. "
            "The key point: N can depend on x. "
            "Different x values may need different N.",
            duration=25,
        )
        self.ly.section_divider("1", "Pointwise Convergence")
        self.ly.clear()

        title = self.ly.title("Pointwise Convergence")

        defn = MathTex(
            r"f_n \to f \text{ pointwise} \iff \forall x: f_n(x) \to f(x)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(defn, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(defn), run_time=SLOW)
        self.wait(0.5)

        formal = MathTex(
            r"\forall x\, \forall \varepsilon > 0\, \exists\, N: n \geq N \implies |f_n(x) - f(x)| < \varepsilon",
            font_size=SMALL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(formal, direction=DOWN, anchor=defn, buff=0.3)
        self.play(Write(formal), run_time=NORMAL)
        self.wait(0.5)

        note = Text(
            "N may depend on x!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=formal, buff=0.3)
        self.play(Write(note), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 3: Uniform Convergence ---
    def scene3_uniform(self):
        self.add_subcaption(
            "Uniform convergence is stronger. "
            "The sequence f sub n converges uniformly to f "
            "if the supremum of the absolute difference "
            "goes to zero. "
            "Equivalently: for every epsilon, there exists "
            "N such that for all n at least N and for ALL "
            "x simultaneously, the difference is less than "
            "epsilon. "
            "The key: N does NOT depend on x. "
            "One N works for the entire domain.",
            duration=25,
        )
        self.ly.section_divider("2", "Uniform Convergence")
        self.ly.clear()

        title = self.ly.title("Uniform Convergence")

        defn = MathTex(
            r"f_n \to f \text{ uniformly} \iff \sup_{x} |f_n(x) - f(x)| \to 0",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(defn, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(defn), run_time=SLOW)
        self.wait(0.5)

        formal = MathTex(
            r"\forall \varepsilon > 0\, \exists\, N: n \geq N \implies |f_n(x) - f(x)| < \varepsilon\ \forall x",
            font_size=SMALL_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(formal, direction=DOWN, anchor=defn, buff=0.3)
        self.play(Write(formal), run_time=NORMAL)
        self.wait(0.5)

        note = Text(
            "N works for ALL x simultaneously!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=formal, buff=0.3)
        self.play(Write(note), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 4: The Key Example: x^n ---
    def scene4_xn_example(self):
        self.add_subcaption(
            "The classic example: f sub n of x equals x to "
            "the n, on the interval zero to one. "
            "For each fixed x less than one, x to the n goes "
            "to zero. "
            "But at x equals one, x to the n equals one "
            "always. "
            "So the pointwise limit is zero for x less than "
            "one, and one at x equals one. "
            "This limit function has a jump! It is not "
            "continuous, even though each f sub n is "
            "continuous. "
            "Moreover, the supremum of the difference is "
            "always close to one near x equals one. "
            "So the convergence is NOT uniform.",
            duration=30,
        )
        self.ly.section_divider("3", "The Key Example: xⁿ")
        self.ly.clear()

        title = self.ly.title(r"$f_n(x) = x^n$ on $[0,1]$")

        axes = Axes(
            x_range=[-0.1, 1.3, 0.5], y_range=[-0.1, 1.3, 0.5],
            x_length=5.0, y_length=2.5,
            axis_config={"include_numbers": True, "font_size": 16, "stroke_width": 1.5},
        )
        self.ly.center_in_content(axes)
        clamp_position(axes)
        self.play(Create(axes), run_time=NORMAL)

        # Show several x^n curves
        colors = [DIM, PRIMARY, SECONDARY, ACCENT]
        for idx, n in enumerate([1, 2, 5, 15]):
            graph = axes.plot(
                lambda x, nn=n: x ** nn, x_range=[0, 1], color=colors[idx],
            )
            n_label = MathTex(f"x^{{{n}}}", font_size=SMALL_SIZE, color=colors[idx])
            n_label.next_to(graph, RIGHT, buff=0.1)
            self.play(Create(graph), run_time=FAST)

        self.wait(0.5)

        # Show limit function: 0 on [0,1), 1 at x=1
        limit_label = MathTex(
            r"f(x) = \begin{cases} 0 & 0 \leq x < 1 \\ 1 & x = 1 \end{cases}",
            font_size=SMALL_SIZE, color=RED,
        )
        self.ly.safe_place(limit_label, direction=DOWN, anchor=axes, buff=0.1)
        self.play(Write(limit_label), run_time=NORMAL)
        self.wait(0.5)

        # Mark the jump
        jump_dot = Dot(axes.c2p(1, 1), color=RED, radius=0.08)
        self.play(FadeIn(jump_dot), run_time=FAST)

        conclusion = Text(
            "Limit is discontinuous! NOT uniform convergence",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(conclusion, direction=DOWN, anchor=limit_label, buff=0.1)
        self.play(Write(conclusion), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 5: Uniform Limit of Continuous is Continuous ---
    def scene5_uniform_continuous(self):
        self.add_subcaption(
            "Why does uniform convergence matter? "
            "Theorem: if each f sub n is continuous and the "
            "sequence converges uniformly to f, then f is "
            "continuous. "
            "The proof uses the classic epsilon over three "
            "argument. "
            "Continuity of f sub n gives epsilon over three. "
            "Uniform convergence gives epsilon over three. "
            "The triangle inequality combines them to show "
            "f is continuous with tolerance epsilon. "
            "Uniform convergence preserves continuity.",
            duration=28,
        )
        self.ly.section_divider("4", "Uniform Limit of Continuous is Continuous")
        self.ly.clear()

        title = self.ly.title("Theorem: Uniform Preserves Continuity")

        statement = MathTex(
            r"f_n \in C[a,b],\ f_n \to f \text{ uniformly} \implies f \in C[a,b]",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(statement, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(statement), run_time=NORMAL)
        self.wait(0.5)

        step1 = MathTex(
            r"|f(x) - f(y)| \leq |f(x) - f_n(x)| + |f_n(x) - f_n(y)| + |f_n(y) - f(y)|",
            font_size=SMALL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=statement, buff=0.3)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.3)

        step2 = MathTex(
            r"< \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.2)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.3)

        result = Text(
            "The ε/3 argument: uniform + continuous => continuous",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=step2, buff=0.3)
        self.play(Write(result), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 6: Interchange of Limit and Integral ---
    def scene6_interchange(self):
        self.add_subcaption(
            "Another crucial property. "
            "If f sub n converges uniformly to f on a b, "
            "then the limit of the integrals equals the "
            "integral of the limit. "
            "In symbols: the limit as n goes to infinity "
            "of the integral from a to b of f sub n, equals "
            "the integral from a to b of f. "
            "Proof: the absolute value of the difference of "
            "integrals is at most the integral of the "
            "absolute difference, which is at most b minus "
            "a times the supremum, which goes to zero. "
            "Uniform convergence lets you pull the limit "
            "inside the integral.",
            duration=30,
        )
        self.ly.section_divider("5", "Interchange of Limit and Integral")
        self.ly.clear()

        title = self.ly.title("Interchange: Limit and Integral")

        statement = MathTex(
            r"f_n \to f \text{ uniformly on } [a,b] \implies \lim_{n\to\infty} \int_a^b f_n = \int_a^b f",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(statement, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(statement), run_time=NORMAL)
        self.wait(0.5)

        proof = MathTex(
            r"\left|\int_a^b f_n - \int_a^b f\right| \leq \int_a^b |f_n - f| \leq (b-a) \sup|f_n - f|",
            font_size=SMALL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(proof, direction=DOWN, anchor=statement, buff=0.3)
        self.play(Write(proof), run_time=NORMAL)
        self.wait(0.3)

        result = MathTex(
            r"\to 0 \text{ as } n \to \infty",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=proof, buff=0.2)
        self.play(Write(result), run_time=NORMAL)
        self.wait(0.5)

        insight = Text(
            "Uniform convergence => limit goes inside the integral!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=result, buff=0.3)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 7: Dini's Theorem ---
    def scene7_dini(self):
        self.add_subcaption(
            "Bonus theorem: Dini's Theorem. "
            "If f sub n are continuous, converge pointwise "
            "to a continuous f, the sequence is monotone "
            "(either always increasing or always decreasing), "
            "and the domain is compact, then the convergence "
            "is actually uniform. "
            "Dini's theorem upgrades pointwise to uniform "
            "under the right conditions. "
            "Compactness is essential!",
            duration=22,
        )
        self.ly.section_divider("6", "Dini's Theorem")
        self.ly.clear()

        title = self.ly.title("Dini's Theorem")

        hyp = MathTex(
            r"f_n \in C[a,b],\ f_n \to f \text{ pointwise},\ f \in C[a,b]",
            font_size=SMALL_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(hyp, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(hyp), run_time=NORMAL)
        self.wait(0.3)

        mono = MathTex(
            r"f_n \text{ monotone (} f_n \leq f_{n+1} \text{ or } f_n \geq f_{n+1}\text{)}",
            font_size=SMALL_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(mono, direction=DOWN, anchor=hyp, buff=0.2)
        self.play(Write(mono), run_time=NORMAL)
        self.wait(0.3)

        concl = MathTex(
            r"\implies f_n \to f \text{ uniformly}",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(concl, direction=DOWN, anchor=mono, buff=0.3)
        self.play(Write(concl), run_time=SLOW)
        self.wait(0.5)

        insight = Text(
            "Monotone + continuous + compact => uniform!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=concl, buff=0.3)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 8: Visual Comparison ---
    def scene8_comparison(self):
        self.add_subcaption(
            "Let's compare the two types side by side. "
            "Pointwise: for each x, you might need a "
            "different N. The curves can converge at "
            "different rates at different points. "
            "Uniform: one N works for all x. The curves "
            "converge at the same rate everywhere, trapped "
            "within an epsilon tube around the limit.",
            duration=20,
        )
        title = self.ly.title("Pointwise vs Uniform")

        items = [
            Text("Pointwise: N depends on x", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Uniform: one N for ALL x", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Pointwise may lose continuity", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Uniform preserves continuity", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Uniform allows interchange with ∫", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.5)
        self.ly.clear()

    # --- Scene 9: Summary + Outro ---
    def scene9_summary(self):
        self.add_subcaption(
            "Key takeaways. "
            "One: pointwise convergence fixes x first, then "
            "takes n to infinity. N may depend on x. "
            "Two: uniform convergence requires one N for "
            "all x. "
            "Three: x to the n on zero to one is pointwise "
            "but not uniform. "
            "Four: uniform limit of continuous functions is "
            "continuous. "
            "Five: uniform convergence allows interchange of "
            "limit and integral. "
            "Six: Dini's theorem upgrades pointwise to "
            "uniform with monotonicity and compactness. "
            "Next time: Series of Functions.",
            duration=32,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("1. Pointwise: N depends on x",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Uniform: one N for all x",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. xⁿ on [0,1]: pointwise but NOT uniform",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Uniform limit of continuous is continuous",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5. Uniform => limit inside integral",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("6. Dini: monotone + compact => uniform",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        play_outro(self, "Series of Functions", "Real Analysis I")
