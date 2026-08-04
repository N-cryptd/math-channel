"""
Video 156: The Lebesgue Integral -- Measure Theory Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video156_LebesgueIntegral

Topics: Riemann integral's limitation with Dirichlet function,
        integration of simple functions,
        definition of the Lebesgue integral via approximation,
        general functions (positive/negative parts),
        Lebesgue vs Riemann comparison,
        key properties (linearity, monotonicity, Markov),
        preview of convergence theorems (MCT, DCT).

Prerequisites: Videos 151-155 (Measure Theory Intro through Measurable Functions).

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
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits, clamp_position


class Video156_LebesgueIntegral(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_simple_function_integral()
        self.scene3_definition()
        self.scene4_general_functions()
        self.scene5_lebesgue_vs_riemann()
        self.scene6_properties()
        self.scene7_preview_convergence()
        self.scene8_summary()

    # --- Scene 1: Hook -- Riemann's Fatal Flaw ~60s ---

    def scene1_hook(self):
        self.add_subcaption(
            "In Video 107 we studied the Riemann integral. It works "
            "beautifully for continuous functions. But it has a fatal "
            "flaw: it cannot integrate the Dirichlet function.",
            duration=50,
        )
        play_intro(self, "The Lebesgue Integral", "Measure Theory")

        title = self.ly.title("Riemann's Fatal Flaw", color=RED)

        item1 = Text(
            "Riemann integral: partitions the DOMAIN (vertical slices)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Dirichlet function: 1 on Q, 0 on R\\Q (nowhere continuous)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "Upper Riemann sum = 1, lower sum = 0 -- integral does not exist",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=title, reveal_anim=FadeIn,
        )

        self.wait(4)

        # The solution
        self.ly.clear()

        self.add_subcaption(
            "The rationals have measure zero, so intuitively the "
            "integral should be zero. The Lebesgue integral achieves "
            "this by slicing horizontally through the range instead "
            "of vertically through the domain.",
            duration=40,
        )

        title2 = self.ly.title("The Lebesgue Solution", color=SECONDARY)

        item4 = Text(
            "Q has Lebesgue measure zero -- rationals are negligible",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item5 = Text(
            "Lebesgue integral: partitions the RANGE (horizontal slices)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        self.ly.progressive_reveal(
            [item4, item5], start_from=title2, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

    # --- Scene 2: Simple Function Integration ~90s ---

    def scene2_simple_function_integral(self):
        self.ly.section_divider(1, "Integration of Simple Functions")

        self.add_subcaption(
            "We defined simple functions in Video 155. A simple function "
            "takes finitely many values. To integrate one, we just sum "
            "each value times the measure of its preimage set.",
            duration=40,
        )

        title = self.ly.title("Simple Function Integral", color=PRIMARY)

        subtitle = Text(
            "Let s(x) = sum of a_i times 1_A_i(x), where a_i >= 0",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(subtitle, DOWN, anchor=title)

        formula = MathTex(
            r"\int s \, d\mu = \sum_{i=1}^{n} a_i \, \mu(A_i)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=subtitle)

        self.wait(4)
        self.ly.clear()

        # Intuition
        self.add_subcaption(
            "Think of each horizontal bar at height a_i having width "
            "proportional to the measure of A_i. The integral is the "
            "total area of all these horizontal bars.",
            duration=35,
        )

        title2 = self.ly.title("Visual Intuition", color=SECONDARY)

        item1 = Text(
            "Each level a_i forms a horizontal bar",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Bar area = height (a_i) times width (mu of A_i)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "Total integral = sum of all bar areas",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=title2, reveal_anim=FadeIn,
        )

        self.wait(4)
        self.ly.clear()

        # Key properties
        self.add_subcaption(
            "The simple function integral satisfies linearity and "
            "monotonicity, just like the Riemann integral. These "
            "properties will extend to the full Lebesgue integral.",
            duration=35,
        )

        title3 = self.ly.title("Properties of Simple Integrals", color=SECONDARY)

        item4 = Text(
            "Linearity: integral(s + t) = integral(s) + integral(t)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item5 = Text(
            "Monotonicity: s <= t implies integral(s) <= integral(t)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item4, item5], start_from=title3, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

    # --- Scene 3: Definition of the Lebesgue Integral ~90s ---

    def scene3_definition(self):
        self.ly.section_divider(2, "The Lebesgue Integral (f >= 0)")

        self.add_subcaption(
            "For a general non-negative measurable function f, we use "
            "the approximation theorem from Video 155. A sequence of "
            "simple functions s_n converges upward to f, and we "
            "define the integral as the limit of their integrals.",
            duration=45,
        )

        title = self.ly.title("Definition: Integral of f >= 0", color=RED)

        subtitle = Text(
            "By the approximation theorem, 0 <= s_1 <= s_2 <= ... <= f",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(subtitle, DOWN, anchor=title)

        formula = MathTex(
            r"\int f \, d\mu = \sup_n \int s_n \, d\mu = \lim_{n \to \infty} \int s_n \, d\mu",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=subtitle)

        self.wait(4)
        self.ly.clear()

        # Key facts
        self.add_subcaption(
            "This limit always exists because the integrals of the "
            "simple functions form an increasing sequence. The value "
            "may be finite or infinity.",
            duration=30,
        )

        title2 = self.ly.title("Why This Works", color=SECONDARY)

        item1 = Text(
            "integral(s_n) is an increasing sequence of non-negative numbers",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Every increasing sequence in the extended reals has a limit",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "Result is well-defined (independent of the approximating sequence)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=title2, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

        # Equivalent definition
        self.add_subcaption(
            "Equivalently, the integral is the supremum over ALL "
            "simple functions that lie below f. This captures the "
            "idea of the largest area we can approximate from below.",
            duration=30,
        )

        title3 = self.ly.title("Equivalent Formulation", color=SECONDARY)

        formula2 = MathTex(
            r"\int f \, d\mu = \sup \left\{ \int s \, d\mu : 0 \leq s \leq f, \, s \text{ simple} \right\}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula2, DOWN, anchor=title3)

        self.wait(3)
        self.ly.clear()

    # --- Scene 4: General Functions (Signed) ~80s ---

    def scene4_general_functions(self):
        self.ly.section_divider(3, "General Functions: Positive & Negative Parts")

        self.add_subcaption(
            "What about functions that take both positive and negative "
            "values? We decompose f into its positive part f plus and "
            "negative part f minus.",
            duration=30,
        )

        title = self.ly.title("Decomposition", color=PRIMARY)

        subtitle = Text(
            "For any measurable f: X -> R, define:",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(subtitle, DOWN, anchor=title)

        formula = MathTex(
            r"f^+(x) = \max(f(x), 0), \quad f^-(x) = \max(-f(x), 0)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=subtitle)

        self.wait(4)
        self.ly.clear()

        self.add_subcaption(
            "Then f equals f plus minus f minus, and the absolute "
            "value of f equals f plus plus f minus. Both parts are "
            "non-negative measurable functions, so their Lebesgue "
            "integrals are already defined.",
            duration=35,
        )

        title2 = self.ly.title("Key Identities", color=SECONDARY)

        item1 = Text(
            "f = f^+ - f^-, and |f| = f^+ + f^-",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Both f^+ and f^- are non-negative measurable functions",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2], start_from=title2, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

        # Definition
        self.add_subcaption(
            "The Lebesgue integral of f is the difference of the "
            "integrals of its positive and negative parts. We say f "
            "is Lebesgue integrable when both are finite.",
            duration=30,
        )

        title3 = self.ly.title("Integral of General Functions", color=RED)

        formula2 = MathTex(
            r"\int f \, d\mu = \int f^+ \, d\mu - \int f^- \, d\mu",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula2, DOWN, anchor=title3)

        self.wait(3)
        self.ly.clear()

        self.add_subcaption(
            "We write L^1 of X, mu for the space of all integrable "
            "functions. A function f is integrable when the integral "
            "of its absolute value is finite.",
            duration=25,
        )

        title4 = self.ly.title("The Space L^1", color=SECONDARY)

        formula3 = MathTex(
            r"L^1(X, \mu) = \left\{ f : \int |f| \, d\mu < \infty \right\}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula3, DOWN, anchor=title4)

        self.wait(3)
        self.ly.clear()

    # --- Scene 5: Lebesgue vs Riemann -- The Star Example ~80s ---

    def scene5_lebesgue_vs_riemann(self):
        self.ly.section_divider(4, "Lebesgue vs Riemann: The Dirichlet Function")

        self.add_subcaption(
            "The Dirichlet function is the star example that separates "
            "Lebesgue from Riemann. Recall D of x equals 1 when x is "
            "rational and 0 when x is irrational, on the interval 0 to 1.",
            duration=35,
        )

        title = self.ly.title("The Dirichlet Function", color=RED)

        formula = MathTex(
            r"D(x) = \begin{cases} 1 & x \in \mathbb{Q} \\ 0 & x \in \mathbb{R} \setminus \mathbb{Q} \end{cases}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=title)

        self.wait(3)
        self.ly.clear()

        # Riemann fails
        self.add_subcaption(
            "Under Riemann integration, the upper sum is always 1 and "
            "the lower sum is always 0. The Riemann integral does not "
            "exist for the Dirichlet function.",
            duration=25,
        )

        title2 = self.ly.title("Riemann Fails", color=RED)

        item1 = Text(
            "Upper Riemann sum = 1 (every interval contains a rational)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Lower Riemann sum = 0 (every interval contains an irrational)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2], start_from=title2, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

        # Lebesgue succeeds
        self.add_subcaption(
            "Under Lebesgue integration, the Dirichlet function is "
            "itself a simple function. The rationals have measure "
            "zero, so the integral equals 1 times 0 plus 0 times 1, "
            "which equals 0. Exactly as our intuition demands.",
            duration=40,
        )

        title3 = self.ly.title("Lebesgue Succeeds", color=SECONDARY)

        formula2 = MathTex(
            r"\int_{[0,1]} D \, dm = 1 \cdot m(\mathbb{Q}) + 0 \cdot m([0,1] \setminus \mathbb{Q}) = 0",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula2, DOWN, anchor=title3)

        self.wait(4)
        self.ly.clear()

        # Key comparison
        self.add_subcaption(
            "The fundamental difference: Riemann partitions the domain "
            "into vertical slices, while Lebesgue partitions the range "
            "into horizontal slices. When a function oscillates wildly "
            "between rationals and irrationals, vertical slicing fails "
            "but horizontal slicing works perfectly.",
            duration=45,
        )

        title4 = self.ly.title("Vertical vs Horizontal Slicing", color=ACCENT)

        item3 = Text(
            "Riemann: partition the domain x-axis (vertical slices)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item4 = Text(
            "Lebesgue: partition the range y-axis (horizontal slices)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item3, item4], start_from=title4, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

    # --- Scene 6: Key Properties ~80s ---

    def scene6_properties(self):
        self.ly.section_divider(5, "Properties of the Lebesgue Integral")

        self.add_subcaption(
            "The Lebesgue integral inherits powerful properties from "
            "the simple function integral. Here are the most important ones.",
            duration=25,
        )

        title = self.ly.title("Fundamental Properties", color=PRIMARY)

        item1 = Text(
            "Linearity: integral of (af + bg) = a*integral(f) + b*integral(g)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Monotonicity: f <= g implies integral(f) <= integral(g)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "integral(f) = 0 does NOT imply f = 0 everywhere",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=title, reveal_anim=FadeIn,
        )

        self.wait(4)
        self.ly.clear()

        # Counterexample for property 3
        self.add_subcaption(
            "For example, the indicator function of the rationals has "
            "Lebesgue integral zero, even though it is not identically "
            "zero. It just differs from zero only on a null set. "
            "This is a feature, not a bug.",
            duration=35,
        )

        title2 = self.ly.title("Null Sets and Integrals", color=SECONDARY)

        item4 = Text(
            "1_Q on [0,1]: integral = 0, but f is not zero everywhere",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item5 = Text(
            "The integral ignores differences on null sets (feature!)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        self.ly.progressive_reveal(
            [item4, item5], start_from=title2, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

        # Markov's inequality
        self.add_subcaption(
            "Markov's inequality connects the size of the integral to "
            "the measure of the set where a function is large. If the "
            "integral is small, the function cannot be large on a big set.",
            duration=35,
        )

        title3 = self.ly.title("Markov's Inequality", color=RED)

        formula = MathTex(
            r"\mu(\{x : |f(x)| \geq c\}) \leq \frac{1}{c} \int |f| \, d\mu",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=title3)

        self.wait(3)
        self.ly.clear()

        self.add_subcaption(
            "Intuition: if the total area under |f| is small, then "
            "the set where |f| exceeds any threshold c must be small. "
            "A function with a finite integral cannot be very large on "
            "a very big set.",
            duration=35,
        )

        title4 = self.ly.title("Intuition", color=SECONDARY)

        item6 = Text(
            "Small integral => f cannot be large on a big set",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item7 = Text(
            "Bound tightens as c increases (more demanding threshold)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item6, item7], start_from=title4, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

    # --- Scene 7: Preview — Convergence Theorems ~60s ---

    def scene7_preview_convergence(self):
        self.ly.section_divider(6, "Preview: The Convergence Theorems")

        self.add_subcaption(
            "The real power of the Lebesgue integral reveals itself "
            "when we study limits and integrals together. The convergence "
            "theorems are the crown jewels of measure theory.",
            duration=30,
        )

        title = self.ly.title("Why Lebesgue Integral is Powerful", color=ACCENT)

        self.wait(2)
        self.ly.clear()

        # MCT
        self.add_subcaption(
            "The Monotone Convergence Theorem: if we have a sequence "
            "of non-negative functions that increases pointwise to f, "
            "then the integral of f_n converges to the integral of f. "
            "We can always swap limit and integral for monotone sequences.",
            duration=40,
        )

        title2 = self.ly.title("Monotone Convergence Theorem", color=PRIMARY)

        cond = Text(
            "0 <= f_1 <= f_2 <= ... and f_n -> f pointwise",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(cond, DOWN, anchor=title2)

        formula = MathTex(
            r"\lim_{n \to \infty} \int f_n \, d\mu = \int \left( \lim_{n \to \infty} f_n \right) d\mu = \int f \, d\mu",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=cond)

        self.wait(4)
        self.ly.clear()

        # DCT
        self.add_subcaption(
            "The Dominated Convergence Theorem: if f_n converges "
            "pointwise to f, and all f_n are bounded in absolute "
            "value by some integrable function g, then the integrals "
            "also converge.",
            duration=40,
        )

        title3 = self.ly.title("Dominated Convergence Theorem", color=PRIMARY)

        cond2 = Text(
            "f_n -> f pointwise, and |f_n| <= g where g is integrable",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(cond2, DOWN, anchor=title3)

        formula2 = MathTex(
            r"\lim_{n \to \infty} \int f_n \, d\mu = \int f \, d\mu",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula2, DOWN, anchor=cond2)

        self.wait(4)
        self.ly.clear()

        # Significance
        self.add_subcaption(
            "These theorems fail for the Riemann integral. Even uniform "
            "convergence does not guarantee interchange of limit and "
            "Riemann integral in general. This is why the Lebesgue "
            "integral is the standard tool in modern analysis.",
            duration=35,
        )

        title4 = self.ly.title("Why This Matters", color=RED)

        item1 = Text(
            "MCT and DCT let us swap limits and integrals freely",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Riemann integration does not have analogous theorems",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2], start_from=title4, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

    # --- Scene 8: Summary & Outro ~50s ---

    def scene8_summary(self):
        self.add_subcaption(
            "Today we built the Lebesgue integral from the ground up. "
            "We started with simple functions, extended to non-negative "
            "measurable functions via the approximation theorem, and "
            "then to general functions using positive and negative parts.",
            duration=40,
        )

        title = self.ly.title("Summary", color=ACCENT)

        item1 = Text(
            "Simple integral: sum of a_i times mu(A_i)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Lebesgue integral (f >= 0): sup of simple integrals below f",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "General case: integral of f^+ minus integral of f^-",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        item4 = Text(
            "Dirichlet function: Lebesgue gives 0, Riemann fails",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3, item4], start_from=title, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

        self.add_subcaption(
            "Key properties include linearity, monotonicity, and Markov's "
            "inequality. Looking ahead, the convergence theorems MCT "
            "and DCT are the true power of the Lebesgue integral.",
            duration=35,
        )

        title2 = self.ly.title("Summary (continued)", color=ACCENT)

        item5 = Text(
            "Properties: linearity, monotonicity, Markov's inequality",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item6 = Text(
            "Preview: MCT and DCT -- swapping limits and integrals",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item5, item6], start_from=title2, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

        play_outro(
            self,
            next_video="Convergence Theorems (MCT, DCT)",
            next_playlist="Measure Theory",
        )
