"""
Video 161: Lebesgue vs Riemann Integration — Measure Theory Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video161_LebesgueVsRiemann

Topics: Recap: Riemann integration (partition-based),
        How Lebesgue integration works (level sets, horizontal slices),
        Key differences between the two approaches,
        Comparison of integrable function spaces,
        Advantages of Lebesgue (convergence theorems, L^p completeness),
        Dirichlet function: Lebesgue integrable but not Riemann integrable,
        Lebesgue's characterization of Riemann integrable functions,
        Practical guidance on when to use which,
        Summary of the entire Measure Theory playlist.

Prerequisites: Videos 151-160 (complete Measure Theory playlist).

Competitive insights: Analysis skipped (youtubei.js search returned minimal data).

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


class Video161_LebesgueVsRiemann(Scene):
    """Lebesgue vs Riemann Integration: Series Finale"""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_riemann_recap()
        self.scene3_lebesgue_approach()
        self.scene4_key_differences()
        self.scene5_dirichlet_example()
        self.scene6_characterization()
        self.scene7_advantages()
        self.scene8_practical_guidance()
        self.scene9_recap_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook — Two Ways to Integrate
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: Vertical slices vs horizontal slices"""
        self.add_subcaption(
            "The Riemann integral partitions the x-axis into vertical slices. "
            "The Lebesgue integral partitions the y-axis into horizontal slices. "
            "Which approach is better, and when?",
            duration=8,
        )
        play_intro(self, "Lebesgue vs Riemann", "Measure Theory")

        title = self.ly.title("Two Ways to Integrate")

        # Visual comparison
        reimann_text = VGroup(
            Text("Riemann:", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Vertical slices (x-axis)", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.05)

        lebesgue_text = VGroup(
            Text("Lebesgue:", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Horizontal slices (y-axis)", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.05)

        columns = self.ly.two_columns(
            [reimann_text], [lebesgue_text], start_from=title,
        )
        self.play(
            FadeIn(reimann_text, shift=LEFT * 0.15),
            FadeIn(lebesgue_text, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1)

        # Motivating question
        question = Text(
            "Are they the same? Is one more powerful?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(question, direction=DOWN, anchor=reimann_text, buff=0.5)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Riemann Integration Recap
    # ------------------------------------------------------------------
    def scene2_riemann_recap(self):
        """Brief recap of Riemann integration"""
        self.ly.section_divider(2, "Riemann Integration")

        self.add_subcaption(
            "In Riemann integration, we partition the domain into intervals, "
            "compute upper and lower sums, and take the limit as the "
            "partition gets finer.",
            duration=7,
        )

        title = self.ly.title("Riemann: Vertical Slices")

        # Upper and lower sums
        formula_upper = MathTex(
            r"U(f, P) = \sum_{i} \sup_{[x_{i-1}, x_i]} f \;\Delta x_i",
            font_size=BODY_SIZE,
            color=PRIMARY,
        )
        formula_lower = MathTex(
            r"L(f, P) = \sum_{i} \inf_{[x_{i-1}, x_i]} f \;\Delta x_i",
            font_size=BODY_SIZE,
            color=SECONDARY,
        )
        formula_eq = MathTex(
            r"\int_a^b f(x)\,dx = \lim_{\|P\|\to 0} U(f,P) = \lim_{\|P\|\to 0} L(f,P)",
            font_size=BODY_SIZE,
            color=WHITE,
        )
        self.ly.safe_place(formula_upper, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(formula_upper), run_time=NORMAL)
        self.wait(0.3)

        self.ly.safe_place(formula_lower, direction=DOWN, anchor=formula_upper, buff=0.15)
        self.play(Write(formula_lower), run_time=NORMAL)
        self.wait(0.3)

        self.ly.safe_place(formula_eq, direction=DOWN, anchor=formula_lower, buff=0.15)
        self.play(Write(formula_eq), run_time=NORMAL)
        self.wait(0.5)

        # Key requirement
        req = Text(
            "Requires: f bounded on [a,b] and partitions converge",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(req, direction=DOWN, anchor=formula_eq, buff=0.3)
        self.play(FadeIn(req, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Lebesgue Integration Approach
    # ------------------------------------------------------------------
    def scene3_lebesgue_approach(self):
        """How Lebesgue integration works differently"""
        self.ly.section_divider(3, "Lebesgue Integration")

        self.add_subcaption(
            "Lebesgue's approach is fundamentally different. "
            "Instead of partitioning the x-axis, we partition the range "
            "of the function and measure how much of the domain "
            "maps to each level.",
            duration=8,
        )

        title = self.ly.title("Lebesgue: Horizontal Slices")

        # Simple function approximation
        step1 = Text("Step 1: Approximate f by simple functions", font_size=BODY_SIZE, color=WHITE, font=SANS)
        simple = MathTex(
            r"s(x) = \sum_{i=1}^{n} c_i \; \mathbf{1}_{A_i}(x)",
            font_size=BODY_SIZE,
            color=PRIMARY,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title, buff=0.4)
        self.ly.safe_place(simple, direction=DOWN, anchor=step1, buff=0.2)
        self.play(
            FadeIn(step1, shift=LEFT * 0.15),
            Write(simple),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Step 2
        self.play(FadeOut(step1))

        step2 = Text("Step 2: Integrate the simple function", font_size=BODY_SIZE, color=WHITE, font=SANS)
        integral_simple = MathTex(
            r"\int s \; d\mu = \sum_{i=1}^{n} c_i \cdot \mu(A_i)",
            font_size=BODY_SIZE,
            color=SECONDARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=simple, buff=0.4)
        self.ly.safe_place(integral_simple, direction=DOWN, anchor=step2, buff=0.2)
        self.play(
            FadeIn(step2, shift=LEFT * 0.15),
            Write(integral_simple),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # Step 3
        self.play(FadeOut(step2))

        step3 = Text("Step 3: Take the supremum", font_size=BODY_SIZE, color=WHITE, font=SANS)
        sup_formula = MathTex(
            r"\int f \; d\mu = \sup \left\{\int s \; d\mu : 0 \leq s \leq f\right\}",
            font_size=BODY_SIZE,
            color=ACCENT,
        )
        boxed = self.ly.formula_box(sup_formula, ACCENT)
        self.ly.safe_place(step3, direction=DOWN, anchor=integral_simple, buff=0.4)
        self.ly.safe_place(boxed, direction=DOWN, anchor=step3, buff=0.2)
        self.play(
            FadeIn(step3, shift=LEFT * 0.15),
            Write(sup_formula),
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Key Differences (Two-Column)
    # ------------------------------------------------------------------
    def scene4_key_differences(self):
        """Side-by-side comparison"""
        self.ly.section_divider(4, "Key Differences")

        self.add_subcaption(
            "Let's compare the two integrals across several important dimensions.",
            duration=4,
        )

        title = self.ly.title("Riemann vs Lebesgue at a Glance")

        # Left column: Riemann features
        r_items = [
            VGroup(
                Text("Slices", font_size=BODY_SIZE, color=WHITE, font=SANS),
                Text("Vertical (x-axis)", font_size=LABEL_SIZE, color=DIM, font=SANS),
            ).arrange(DOWN, buff=0.03),
            VGroup(
                Text("Domain", font_size=BODY_SIZE, color=WHITE, font=SANS),
                Text("Bounded intervals", font_size=LABEL_SIZE, color=DIM, font=SANS),
            ).arrange(DOWN, buff=0.03),
            VGroup(
                Text("Limits", font_size=BODY_SIZE, color=WHITE, font=SANS),
                Text("Hard to swap", font_size=LABEL_SIZE, color=DIM, font=SANS),
            ).arrange(DOWN, buff=0.03),
        ]

        # Right column: Lebesgue features
        l_items = [
            VGroup(
                Text("Slices", font_size=BODY_SIZE, color=WHITE, font=SANS),
                Text("Horizontal (y-axis)", font_size=LABEL_SIZE, color=DIM, font=SANS),
            ).arrange(DOWN, buff=0.03),
            VGroup(
                Text("Domain", font_size=BODY_SIZE, color=WHITE, font=SANS),
                Text("Any measure space", font_size=LABEL_SIZE, color=DIM, font=SANS),
            ).arrange(DOWN, buff=0.03),
            VGroup(
                Text("Limits", font_size=BODY_SIZE, color=WHITE, font=SANS),
                Text("DCT / MCT", font_size=LABEL_SIZE, color=DIM, font=SANS),
            ).arrange(DOWN, buff=0.03),
        ]

        r_group = VGroup(*r_items).arrange(DOWN, buff=0.15)
        l_group = VGroup(*l_items).arrange(DOWN, buff=0.15)

        # Add column headers
        r_header = Text("Riemann", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        l_header = Text("Lebesgue", font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        r_col = VGroup(r_header, r_group).arrange(DOWN, buff=0.2)
        l_col = VGroup(l_header, l_group).arrange(DOWN, buff=0.2)

        ensure_fits(r_col, MAX_HALF_WIDTH, 4.0)
        ensure_fits(l_col, MAX_HALF_WIDTH, 4.0)

        columns = self.ly.two_columns(
            [r_col], [l_col], start_from=title,
        )
        self.play(
            FadeIn(r_header), FadeIn(l_header),
            run_time=FAST,
        )
        self.play(
            *[FadeIn(item, shift=LEFT * 0.15) for item in r_items],
            *[FadeIn(item, shift=LEFT * 0.15) for item in l_items],
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Dirichlet Function Example
    # ------------------------------------------------------------------
    def scene5_dirichlet_example(self):
        """Dirichlet function: Lebesgue integrable but not Riemann integrable"""
        self.ly.section_divider(5, "The Dirichlet Function")

        self.add_subcaption(
            "The Dirichlet function is the classic example of a function "
            "that Lebesgue can integrate but Riemann cannot.",
            duration=5,
        )

        title = self.ly.title("Where Riemann Breaks Down")

        # The function
        func_formula = MathTex(
            r"f(x) = \begin{cases} 1 & x \in \mathbb{Q} \\ 0 & x \notin \mathbb{Q} \end{cases}",
            font_size=HEADING_SIZE,
            color=PRIMARY,
        )
        formula_box = self.ly.formula_box(func_formula, PRIMARY)
        self.ly.safe_place(formula_box, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(func_formula), run_time=NORMAL)
        self.wait(0.5)

        # Riemann fails
        reimann_fails = Text(
            "Riemann: U(f,P) = 1, L(f,P) = 0  =>  NOT integrable",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(reimann_fails, direction=DOWN, anchor=formula_box, buff=0.4)
        self.play(FadeIn(reimann_fails, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Lebesgue succeeds
        lebesgue_works = Text(
            "Lebesgue: Q has measure zero => integral = 0",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(lebesgue_works, direction=DOWN, anchor=reimann_fails, buff=0.3)
        self.play(FadeIn(lebesgue_works, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # The insight
        self.play(FadeOut(reimann_fails))

        insight = Text(
            "Lebesgue ignores sets of measure zero!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=formula_box, buff=0.4)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Lebesgue's Characterization
    # ------------------------------------------------------------------
    def scene6_characterization(self):
        """When is a function Riemann integrable?"""
        self.ly.section_divider(6, "Lebesgue's Characterization")

        self.add_subcaption(
            "Lebesgue proved a beautiful theorem that exactly characterizes "
            "which functions are Riemann integrable, using measure theory!",
            duration=6,
        )

        title = self.ly.title("When is Riemann Good Enough?")

        # The theorem
        theorem = MathTex(
            r"f \text{ is Riemann integrable on } [a,b] \iff "
            r"\{x : f \text{ discontinuous at } x\} "
            r"\text{ has } \lambda\text{-measure } 0",
            font_size=BODY_SIZE,
            color=PRIMARY,
        )
        boxed = self.ly.formula_box(theorem, PRIMARY)
        self.ly.safe_place(boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(theorem), run_time=NORMAL)
        self.wait(0.5)

        # Consequences
        self.play(FadeOut(boxed))

        con1 = Text(
            "Continuous functions on [a,b]: always Riemann integrable",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        con2 = Text(
            "Bounded + countably many discontinuities: Riemann integrable",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        con3 = Text(
            "Riemann integrable => Lebesgue integrable (same value!)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        items = [con1, con2, con3]
        self.ly.progressive_reveal(items, start_from=title, wait_time=0.7)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Advantages of Lebesgue
    # ------------------------------------------------------------------
    def scene7_advantages(self):
        """Why Lebesgue integration is more powerful"""
        self.ly.section_divider(7, "Advantages of Lebesgue")

        self.add_subcaption(
            "Lebesgue integration is strictly more powerful than Riemann. "
            "Here are the key advantages that make it essential.",
            duration=6,
        )

        title = self.ly.title("Why Lebesgue Wins")

        items = [
            Text("L^p spaces are complete (Banach / Hilbert)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Convergence theorems: MCT, DCT, Fatou", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Works on arbitrary measure spaces", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Foundation for probability and expectation", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, wait_time=0.7)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Practical Guidance
    # ------------------------------------------------------------------
    def scene8_practical_guidance(self):
        """When to use Riemann vs Lebesgue"""
        self.ly.section_divider(8, "When to Use Which")

        self.add_subcaption(
            "In practice, you'll use both. Riemann for intuition and "
            "computation, Lebesgue for theory and probability.",
            duration=5,
        )

        title = self.ly.title("Practical Guidance")

        # When to use Riemann
        r_header = Text("Use Riemann:", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        r1 = Text("Basic calculus and physics", font_size=LABEL_SIZE, color=DIM, font=SANS)
        r2 = Text("Computing definite integrals", font_size=LABEL_SIZE, color=DIM, font=SANS)
        r_items = VGroup(r1, r2).arrange(DOWN, buff=0.05)

        # When to use Lebesgue
        l_header = Text("Use Lebesgue:", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        l1 = Text("Probability theory", font_size=LABEL_SIZE, color=DIM, font=SANS)
        l2 = Text("Functional analysis", font_size=LABEL_SIZE, color=DIM, font=SANS)
        l3 = Text("Convergence questions", font_size=LABEL_SIZE, color=DIM, font=SANS)
        l_items = VGroup(l1, l2, l3).arrange(DOWN, buff=0.05)

        r_col = VGroup(r_header, r_items).arrange(DOWN, buff=0.1)
        l_col = VGroup(l_header, l_items).arrange(DOWN, buff=0.1)

        columns = self.ly.two_columns(
            [r_col], [l_col], start_from=title,
        )
        self.play(
            FadeIn(r_header, shift=LEFT * 0.15),
            FadeIn(l_header, shift=LEFT * 0.15),
            run_time=FAST,
        )
        self.play(
            FadeIn(r_items, shift=LEFT * 0.15),
            FadeIn(l_items, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)

        # They agree on nice functions
        self.play(FadeOut(r_col), FadeOut(l_col))

        agree = Text(
            "For continuous functions on [a,b]: both give the same answer!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(agree, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(agree, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Playlist Recap + Series Outro
    # ------------------------------------------------------------------
    def scene9_recap_outro(self):
        """Summary of entire Measure Theory playlist"""
        self.ly.section_divider(9, "Measure Theory Recap")

        self.add_subcaption(
            "That completes our Measure Theory playlist! We built the "
            "Lebesgue integral from scratch, starting with sigma-algebras "
            "and culminating in Fubini's theorem and Lebesgue vs Riemann.",
            duration=8,
        )

        title = self.ly.title("What We Built Together")

        takeaways = [
            Text("Sigma-algebras and measures: the foundation", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Lebesgue integral: more powerful than Riemann", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Convergence theorems: MCT, DCT, Fatou", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("L^p spaces, RN derivative, Fubini complete the toolkit", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title, wait_time=0.8)
        self.wait(1.5)

        self.ly.clear()

        play_outro(self, "Functional Analysis", "Graduate Mathematics")
