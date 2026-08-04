"""
Video 155: Lebesgue Measurable Functions -- Measure Theory Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video155_LebesgueMeasurableFunctions

Topics: measurable functions (definition + equivalences),
        examples (continuous, indicator, Dirichlet),
        simple functions and standard form,
        approximation by simple functions theorem,
        properties (algebra, limits),
        Egorov's theorem (statement).

Prerequisites: Videos 151-154 (Measure Theory Intro, Sigma-Algebras,
              Measures, Lebesgue Measure).

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


class Video155_LebesgueMeasurableFunctions(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_formal_definition()
        self.scene3_examples()
        self.scene4_simple_functions()
        self.scene5_approximation_theorem()
        self.scene6_properties()
        self.scene7_egorovs_theorem()
        self.scene8_summary()

    # --- Scene 1: Hook -- "Which Functions Can We Measure?" ~55s ---

    def scene1_hook(self):
        self.add_subcaption(
            "Four videos ago we started building measure theory. "
            "We have measurable sets, sigma-algebras, and the Lebesgue "
            "measure. Now the big question: what functions can we "
            "actually integrate?",
            duration=50,
        )
        play_intro(self, "Lebesgue Measurable Functions", "Measure Theory")

        title = self.ly.title("Which Functions Can We Measure?", color=RED)

        item1 = Text(
            "We have the measure: m(E) gives sizes of sets",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "But we need a measure for FUNCTIONS, not just sets",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "The answer: almost every function you've met is measurable",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=title, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

    # --- Scene 2: Formal Definition ~90s ---

    def scene2_formal_definition(self):
        self.ly.section_divider(1, "Definition: Measurable Function")

        self.add_subcaption(
            "Let X, Sigma be a measurable space. A function f from X "
            "to the real numbers is measurable if the preimage of "
            "every open set is a measurable set. This is the "
            "fundamental definition.",
            duration=40,
        )

        title = self.ly.title("Definition: Measurable Function", color=PRIMARY)

        subtitle = Text(
            "Let (X, \u03a3) be a measurable space. f : X \u2192 \u211d is measurable if:",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(subtitle, DOWN, anchor=title)

        formula = MathTex(
            r"f^{-1}(U) \in \Sigma \quad \text{for every open set } U \subseteq \mathbb{R}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=subtitle)

        self.wait(4)

        # Equivalent characterizations
        self.ly.clear()

        self.add_subcaption(
            "There are several equivalent ways to check measurability. "
            "The most practical: for every real number a, the set "
            "where f exceeds a must be measurable.",
            duration=40,
        )

        title2 = self.ly.title("Equivalent Characterizations", color=SECONDARY)

        item1 = Text(
            "f^{-1}(open U) in Sigma  -- the original definition",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "{ x : f(x) > a } in Sigma for all a in R",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "{ x : f(x) >= a }, { x : f(x) < a } also work",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=title2, reveal_anim=FadeIn,
        )

        self.wait(3)

        # Key insight
        self.ly.clear()

        self.add_subcaption(
            "We check preimages of sets in the codomain, not the "
            "domain. The function doesn't need to be continuous or "
            "even nice. It just needs to send measurable sets back "
            "to measurable sets.",
            duration=35,
        )

        title3 = self.ly.title("Key Insight", color=ACCENT)

        formula2 = MathTex(
            r"\text{measurable sets in } \mathbb{R}"
            r"\xrightarrow{f^{-1}}"
            r"\text{measurable sets in } X",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula2, DOWN, anchor=title3)

        self.wait(3)

        item4 = Text(
            "No continuity required! Much broader than continuous functions",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(item4, DOWN, anchor=formula2)

        self.wait(3)
        self.ly.clear()

    # --- Scene 3: Examples ~80s ---

    def scene3_examples(self):
        self.ly.section_divider(2, "Examples: Measurable Functions")

        self.add_subcaption(
            "Let's look at which functions are measurable. The "
            "results are surprisingly generous. Every continuous "
            "function is measurable, and so are many discontinuous ones.",
            duration=40,
        )

        title = self.ly.title("Examples", color=PRIMARY)

        item1 = Text(
            "Every continuous f : R -> R is measurable",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Indicator function 1_E is measurable iff E is measurable",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "The Dirichlet function is measurable (Q has measure zero!)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=title, reveal_anim=FadeIn,
        )

        self.wait(3)

        self.ly.clear()

        # Dirichlet detail
        self.add_subcaption(
            "The Dirichlet function is the star example. It equals "
            "one on rationals and zero on irrationals. It's nowhere "
            "continuous and not Riemann integrable, but it IS "
            "Lebesgue measurable.",
            duration=40,
        )

        title2 = self.ly.title("The Dirichlet Function", color=RED)

        formula1 = MathTex(
            r"f(x) = \begin{cases} 1 & x \in \mathbb{Q} \\ 0 & x \notin \mathbb{Q} \end{cases}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula1, DOWN, anchor=title2)

        self.wait(3)

        item4 = Text(
            "Nowhere continuous, not Riemann integrable",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        item5 = Text(
            "But {x : f(x) > a} = Q or R or empty -- all measurable!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item4, item5], start_from=formula1, reveal_anim=FadeIn,
        )

        self.wait(3)

        # Monotone functions
        self.ly.clear()

        self.add_subcaption(
            "Monotone functions are another important class. Every "
            "monotone increasing or decreasing function on the real "
            "line is Lebesgue measurable.",
            duration=25,
        )

        title3 = self.ly.title("More Examples", color=SECONDARY)

        item6 = Text(
            "Monotone functions are measurable",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item7 = Text(
            "Borel measurable functions: f^{-1}(Borel set) measurable",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item6, item7], start_from=title3, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

    # --- Scene 4: Simple Functions ~80s ---

    def scene4_simple_functions(self):
        self.ly.section_divider(3, "Simple Functions")

        self.add_subcaption(
            "Simple functions are the building blocks of Lebesgue "
            "integration. They play the same role that step "
            "functions play in Riemann integration.",
            duration=35,
        )

        title = self.ly.title("Definition: Simple Function", color=PRIMARY)

        subtitle = Text(
            "A function s : X -> R is simple if it takes only finitely many values.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(subtitle, DOWN, anchor=title)

        self.wait(3)

        # Standard form
        self.ly.clear()

        self.add_subcaption(
            "Every simple function can be written in standard form "
            "as a finite linear combination of indicator functions "
            "of measurable sets that partition X.",
            duration=35,
        )

        title2 = self.ly.title("Standard Form", color=SECONDARY)

        formula = MathTex(
            r"s(x) = \sum_{i=1}^{n} a_i \, \mathbf{1}_{A_i}(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=title2)

        self.wait(3)

        item1 = Text(
            "Each a_i is a distinct real value that s takes",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item2 = Text(
            "The sets A_i are measurable and partition X",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        item3 = Text(
            "s is measurable iff each A_i is measurable",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=formula, reveal_anim=FadeIn,
        )

        self.wait(3)

        # Analogy
        self.ly.clear()

        self.add_subcaption(
            "Think of simple functions as step functions with "
            "finitely many levels. They are the basic building "
            "blocks, just like rectangles in Riemann integration.",
            duration=30,
        )

        title3 = self.ly.title("The Building Blocks", color=ACCENT)

        item4 = Text(
            "Simple functions : Lebesgue integral :: step functions : Riemann integral",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item5 = Text(
            "Simple functions approximate ANY measurable function",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item4, item5], start_from=title3, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

    # --- Scene 5: Approximation Theorem ~90s ---

    def scene5_approximation_theorem(self):
        self.ly.section_divider(4, "Approximation by Simple Functions")

        self.add_subcaption(
            "One of the most important theorems in measure theory: "
            "every non-negative measurable function can be "
            "approximated from below by an increasing sequence "
            "of simple functions.",
            duration=35,
        )

        title = self.ly.title("Approximation Theorem", color=RED)

        subtitle = Text(
            "For every measurable f >= 0, there exist simple functions:",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(subtitle, DOWN, anchor=title)

        formula = MathTex(
            r"0 \leq s_1 \leq s_2 \leq \cdots \leq f,"
            r"\quad s_n \to f \text{ pointwise}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=subtitle)

        self.wait(4)

        # Construction
        self.ly.clear()

        self.add_subcaption(
            "The construction is beautifully explicit. We divide "
            "the range into finer and finer intervals, and round "
            "the function value down to the nearest grid point.",
            duration=35,
        )

        title2 = self.ly.title("Explicit Construction", color=PRIMARY)

        item1 = Text(
            "Divide [0, n] into 2^{2n} intervals of length 1/2^{2n}",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "s_n(x) = k/2^{2n} when f(x) is in [k/2^{2n}, (k+1)/2^{2n})",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "s_n(x) = n when f(x) >= n (truncation at height n)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=title2, reveal_anim=FadeIn,
        )

        self.wait(3)

        # Visual idea
        self.ly.clear()

        self.add_subcaption(
            "Visually: coarse grid, fine grid, finer grid. At each "
            "step the staircase approximation gets closer to the "
            "true function, always from below.",
            duration=30,
        )

        title3 = self.ly.title("Coarse Grid -> Fine Grid", color=SECONDARY)

        formula2 = MathTex(
            r"s_n(x) = \frac{\lfloor 2^{2n} f(x) \rfloor}{2^{2n}}"
            r"\wedge n",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula2, DOWN, anchor=title3)

        self.wait(3)

        item4 = Text(
            "If you understand simple functions, you understand ALL non-negative measurable functions",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(item4, DOWN, anchor=formula2)

        self.wait(3)
        self.ly.clear()

    # --- Scene 6: Properties of Measurable Functions ~70s ---

    def scene6_properties(self):
        self.ly.section_divider(5, "Properties of Measurable Functions")

        self.add_subcaption(
            "Measurable functions behave wonderfully under algebraic "
            "operations and limits. They form a rich, well-behaved "
            "class of functions.",
            duration=30,
        )

        title = self.ly.title("Algebra of Measurable Functions", color=PRIMARY)

        item1 = Text(
            "f, g measurable => f + g measurable",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "f, g measurable => f * g measurable",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item3 = Text(
            "f measurable => |f| measurable",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=title, reveal_anim=FadeIn,
        )

        self.wait(3)

        # Limit property
        self.ly.clear()

        self.add_subcaption(
            "The most powerful property: measurability is preserved "
            "under pointwise limits. This is NOT true for "
            "continuity, which makes measurable functions far "
            "more robust.",
            duration=35,
        )

        title2 = self.ly.title("Limit Theorem", color=RED)

        formula = MathTex(
            r"f_n \text{ measurable}, \; f_n \to f \text{ pointwise}"
            r"\implies f \text{ measurable}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=title2)

        self.wait(3)

        item4 = Text(
            "max(f, g) and min(f, g) are measurable too",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        item5 = Text(
            "Measurable functions are closed under composition with continuous maps",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        self.ly.progressive_reveal(
            [item4, item5], start_from=formula, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

    # --- Scene 7: Egorov's Theorem ~80s ---

    def scene7_egorovs_theorem(self):
        self.ly.section_divider(6, "Egorov's Theorem")

        self.add_subcaption(
            "We close with a stunning result about sequences of "
            "measurable functions. Egorov's theorem upgrades "
            "pointwise convergence to uniform convergence, "
            "except on a set of arbitrarily small measure.",
            duration=40,
        )

        title = self.ly.title("Egorov's Theorem", color=RED)

        subtitle = Text(
            "Let (X, \u03a3, \u03bc) be a finite measure space.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(subtitle, DOWN, anchor=title)

        formula = MathTex(
            r"f_n \to f \text{ pointwise}"
            r"\implies \forall \varepsilon > 0,"
            r"\; \exists E \in \Sigma :",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=subtitle)

        formula2 = MathTex(
            r"\mu(X \setminus E) < \varepsilon"
            r"\text{ and } f_n \to f \text{ uniformly on } E",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(formula2, DOWN, anchor=formula)

        self.wait(4)

        # Key conditions
        self.ly.clear()

        self.add_subcaption(
            "There are two key hypotheses. The measure space must "
            "have finite total measure, and we need pointwise "
            "convergence. Without finite measure, the theorem "
            "fails.",
            duration=35,
        )

        title2 = self.ly.title("Key Conditions", color=PRIMARY)

        item1 = Text(
            "Finite measure: mu(X) < infinity (essential!)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        item2 = Text(
            "Pointwise convergence (or almost everywhere)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "Conclusion: uniform convergence off a small set",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=title2, reveal_anim=FadeIn,
        )

        self.wait(3)

        # Counterexample
        self.ly.clear()

        self.add_subcaption(
            "Without finite measure, Egorov fails. On the real "
            "line with Lebesgue measure, consider the indicator "
            "of the interval n to n plus 1. It converges to zero "
            "pointwise, but not uniformly on any set of finite "
            "complement.",
            duration=40,
        )

        title3 = self.ly.title("Why Finite Measure Matters", color=RED)

        formula3 = MathTex(
            r"f_n(x) = \mathbf{1}_{[n,\, n+1]}(x)"
            r"\to 0 \text{ pointwise on } \mathbb{R}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula3, DOWN, anchor=title3)

        self.wait(3)

        item4 = Text(
            "But f_n does NOT converge to 0 uniformly on any set of finite complement",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(item4, DOWN, anchor=formula3)

        self.wait(3)

        # Connection to integral
        self.ly.clear()

        self.add_subcaption(
            "Egorov's theorem is a preview of the great convergence "
            "theorems that power the Lebesgue integral: the "
            "dominated convergence theorem and the monotone "
            "convergence theorem.",
            duration=30,
        )

        title4 = self.ly.title("Looking Ahead", color=SECONDARY)

        item5 = Text(
            "Bridge from pointwise to uniform convergence in measure theory",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item6 = Text(
            "Preview: Dominated Convergence and Monotone Convergence theorems",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item5, item6], start_from=title4, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

    # --- Scene 8: Summary & Outro ~45s ---

    def scene8_summary(self):
        self.add_subcaption(
            "Today we defined measurable functions via the preimage "
            "condition, explored examples from continuous to the "
            "Dirichlet function, introduced simple functions as "
            "building blocks, proved the approximation theorem, "
            "studied the algebra of measurable functions, and "
            "stated Egorov's theorem.",
            duration=50,
        )

        title = self.ly.title("Summary", color=ACCENT)

        item1 = Text(
            "Measurable: preimages of open sets are measurable",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Continuous, indicator, and Dirichlet functions are measurable",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "Simple functions: building blocks (finite values, standard form)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        item4 = Text(
            "Approximation theorem: simple functions converge to any measurable f >= 0",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3, item4], start_from=title, reveal_anim=FadeIn,
        )

        self.wait(3)

        self.ly.clear()

        self.add_subcaption(
            "Measurable functions form an algebra closed under "
            "limits. Egorov's theorem upgrades pointwise to "
            "uniform convergence on finite measure spaces. "
            "Next time, we define the Lebesgue integral.",
            duration=35,
        )

        title2 = self.ly.title("Summary (continued)", color=ACCENT)

        item5 = Text(
            "Algebra of measurable functions closed under +, *, |.|, and limits",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item6 = Text(
            "Egorov: pointwise -> uniform on finite measure spaces",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )

        self.ly.progressive_reveal(
            [item5, item6], start_from=title2, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

        play_outro(
            self,
            next_video="The Lebesgue Integral",
            next_playlist="Measure Theory",
        )
