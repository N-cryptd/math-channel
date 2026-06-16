"""Video 70: Random Variables
Probability & Statistics -- Video 4 of 12

Covers: random variable definition (X: Omega -> R), discrete vs continuous,
PMF, CDF, PDF introduction, comparison of discrete and continuous types.

Competitive analysis: 3B1B probability series, Khan Academy, StatQuest, Dr. Trefor Bazett, jbstatistics
Plan: planning/video-70-random-variables.md

Render draft:  manim -ql scripts/undergraduate/video-70-random-variables.py Video70_RandomVariables
Render final:  manim -qh scripts/undergraduate/video-70-random-variables.py Video70_RandomVariables
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


class Video70_RandomVariables(Scene):
    """Full video: Random Variables — turning events into numbers."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_quiz_hook()
        self.scene2_definition()
        self.scene3_discrete_rv()
        self.scene4_pmf()
        self.scene5_cdf()
        self.scene6_continuous_intro()
        self.scene7_comparison()
        self.scene8_summary()

    # -- Scene 1: Hook -- The Quiz Score --
    def scene1_quiz_hook(self):
        self.add_subcaption(
            "Imagine you take a ten question quiz, each worth ten "
            "points, and you guess every answer randomly with four "
            "choices each. What can you say about your score?",
            duration=18,
        )
        play_intro(self, "Random Variables", "Probability & Statistics")

        title = self.ly.title("The Quiz Score Puzzle")

        # Quiz boxes as a 5x2 grid
        boxes = VGroup(*[
            RoundedRectangle(
                corner_radius=0.08, width=0.6, height=0.5,
                fill_color=PRIMARY, fill_opacity=0.15,
                stroke_color=PRIMARY, stroke_width=1.5,
            )
            for _ in range(10)
        ])
        boxes.arrange_in_grid(rows=2, cols=5, buff=0.15)
        self.ly.safe_place(boxes, DOWN, anchor=title, buff=0.5)

        self.play(Create(boxes), run_time=NORMAL)
        self.wait(0.5)

        self.add_subcaption(
            "Your score is not fixed. It depends on how many you "
            "guess correctly. It could be anything from zero to one "
            "hundred. This is a random variable.",
            duration=18,
        )

        # Show score as a random variable
        score_text = MathTex(
            r"\text{Score}", r"=", r"10 \times", r"\text{(\# correct)}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        score_text[0].set_color(ACCENT)
        score_text[3].set_color(ACCENT)
        score_text.next_to(boxes, DOWN, buff=0.4)
        ensure_fits(score_text)
        self.play(Write(score_text), run_time=NORMAL)
        self.wait(1)

        box = self.ly.formula_box(score_text, color=ACCENT)
        self.play(Create(box), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # -- Scene 2: What is a Random Variable? --
    def scene2_definition(self):
        self.add_subcaption(
            "A random variable is a function X that assigns a real "
            "number to every outcome in the sample space. It maps "
            "outcomes to numbers.",
            duration=16,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("Random Variable")

        # Formal definition
        def_tex = MathTex(
            r"X", r":", r"\Omega", r"\to", r"\mathbb{R}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        def_tex[0].set_color(ACCENT)
        def_tex[2].set_color(PRIMARY)
        def_tex[4].set_color(SECONDARY)
        self.ly.center_in_content(def_tex)
        self.play(Write(def_tex), run_time=SLOW)
        self.wait(0.5)

        box = self.ly.formula_box(def_tex, color=ACCENT)
        self.play(Create(box), run_time=FAST)
        self.wait(1)

        self.play(FadeOut(box), FadeOut(def_tex), run_time=FAST)

        # Mapping diagram: Omega outcomes -> number line
        self.add_subcaption(
            "Think of it as arrows from each outcome down to a "
            "number. For a coin flip, heads maps to one and tails "
            "maps to zero. This is called an indicator variable.",
            duration=24,
        )

        title2 = self.ly.title("Example: Coin Flip Indicator")

        # Sample space outcomes
        omega_label = MathTex(
            r"\Omega", font_size=LABEL_SIZE, color=DIM,
        )
        outcomes = VGroup(
            Text("H", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("T", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        )
        outcomes.arrange(RIGHT, buff=1.2)

        outcomes_group = VGroup(omega_label, outcomes)
        outcomes_group.arrange(DOWN, buff=0.3)
        self.ly.safe_place(outcomes_group, UP, anchor=title2, buff=0.5)
        self.play(FadeIn(outcomes_group), run_time=NORMAL)
        self.wait(0.3)

        # Number line
        r_label = MathTex(
            r"\mathbb{R}", font_size=LABEL_SIZE, color=DIM,
        )
        num_line = NumberLine(
            x_range=[-0.5, 1.5, 1], length=3.0,
            color=SECONDARY, stroke_width=2,
            include_numbers=True, font_size=LABEL_SIZE,
        )
        num_vals = VGroup(r_label, num_line)
        num_vals.arrange(DOWN, buff=0.3)
        self.ly.safe_place(num_vals, DOWN, anchor=outcomes_group, buff=1.5)
        self.play(Create(num_line), FadeIn(r_label), run_time=NORMAL)
        self.wait(0.3)

        # Arrows from outcomes to values
        arrow_h = CurvedArrow(
            outcomes[0].get_bottom(), num_line.n2p(1),
            color=ACCENT, stroke_width=2, tip_length=0.15,
        )
        arrow_t = CurvedArrow(
            outcomes[1].get_bottom(), num_line.n2p(0),
            color=ACCENT, stroke_width=2, tip_length=0.15,
        )

        self.play(
            Create(arrow_h), Create(arrow_t),
            run_time=NORMAL,
        )
        self.wait(1)

        # Labels for the mapping
        label_x = Text(
            "X(H) = 1,  X(T) = 0",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(label_x, DOWN, anchor=num_vals, buff=0.4)
        self.play(FadeIn(label_x, shift=UP * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # -- Scene 3: Discrete Random Variables --
    def scene3_discrete_rv(self):
        self.add_subcaption(
            "A random variable is discrete if it takes values in a "
            "countable set. You can list all possible values, and "
            "between any two there is a gap.",
            duration=16,
        )
        self.ly.section_divider(2, "Discrete Random Variables")

        title = self.ly.title("Discrete")

        def_text = Text(
            "X is discrete if X takes values in a countable set.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(def_text, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(def_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(def_text), run_time=FAST)

        # Example: Sum of two dice
        self.add_subcaption(
            "Example: roll two dice and let X be the sum. The "
            "possible values are two through twelve. Each value is "
            "a whole number, and you can count them all.",
            duration=18,
        )

        title2 = self.ly.title("Example: Sum of Two Dice")

        sum_eq = MathTex(
            r"X", r"=", r"d_1", r"+", r"d_2",
            r", \quad X \in \{2, 3, \ldots, 12\}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        sum_eq[0].set_color(ACCENT)
        sum_eq[2].set_color(PRIMARY)
        sum_eq[4].set_color(PRIMARY)
        sum_eq[5].set_color(ACCENT)
        self.ly.safe_place(sum_eq, DOWN, anchor=title2, buff=0.5)
        self.play(Write(sum_eq), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(sum_eq), run_time=FAST)

        # Number of heads in 3 flips
        self.add_subcaption(
            "Another example: flip three coins, let X be the number "
            "of heads. X can be zero, one, two, or three. Four "
            "countable values. That is discrete.",
            duration=18,
        )

        title3 = self.ly.title("Example: 3 Coin Flips")

        heads_eq = MathTex(
            r"X", r"=", r"\#\{\text{heads in 3 flips}\}",
            r", \quad X \in \{0, 1, 2, 3\}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        heads_eq[0].set_color(ACCENT)
        heads_eq[2].set_color(PRIMARY)
        heads_eq[3].set_color(ACCENT)
        self.ly.safe_place(heads_eq, DOWN, anchor=title3, buff=0.5)
        self.play(Write(heads_eq), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # -- Scene 4: Probability Mass Function --
    def scene4_pmf(self):
        self.add_subcaption(
            "The Probability Mass Function tells us the probability "
            "that X takes each specific value. It completely "
            "describes a discrete random variable.",
            duration=16,
        )
        self.ly.section_divider(3, "PMF")

        title = self.ly.title("Probability Mass Function")

        pmf_def = MathTex(
            r"p_X(x)", r"=", r"P(X = x)",
            font_size=TITLE_SIZE, color=WHITE,
        )
        pmf_def[0].set_color(ACCENT)
        pmf_def[2].set_color(ACCENT)
        self.ly.center_in_content(pmf_def)
        self.play(Write(pmf_def), run_time=SLOW)
        self.wait(0.5)

        box = self.ly.formula_box(pmf_def, color=ACCENT)
        self.play(Create(box), run_time=FAST)
        self.wait(1)

        self.play(FadeOut(box), FadeOut(pmf_def), run_time=FAST)

        # Properties
        self.add_subcaption(
            "The PMF has two key properties. First, every probability "
            "is non-negative. Second, all probabilities sum to "
            "exactly one. This is like saying something must happen.",
            duration=20,
        )

        props = [
            Text(
                "1.  p_X(x) >= 0  for all x",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "2.  sum of p_X(x) over all x = 1",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        title2 = self.ly.title("PMF Properties")
        self.ly.progressive_reveal(props, start_from=title2)
        self.wait(1)

        self.ly.clear()

        # PMF of 3 coin flips
        self.add_subcaption(
            "Let us compute the PMF for the number of heads in "
            "three fair coin flips. There are eight equally likely "
            "outcomes. X equals zero has one outcome, X equals one "
            "has three, X equals two has three, X equals three has one.",
            duration=30,
        )

        title3 = self.ly.title("PMF: Number of Heads in 3 Flips")

        # Show probabilities
        pmf_items = [
            Text("P(X=0) = 1/8", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("P(X=1) = 3/8", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("P(X=2) = 3/8", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("P(X=3) = 1/8", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(pmf_items, start_from=title3)
        self.wait(1.5)

        self.ly.clear()

    # -- Scene 5: Cumulative Distribution Function --
    def scene5_cdf(self):
        self.add_subcaption(
            "The Cumulative Distribution Function gives the "
            "probability that X is at most x. It accumulates "
            "probability as x increases.",
            duration=16,
        )
        self.ly.section_divider(4, "CDF")

        title = self.ly.title("Cumulative Distribution Function")

        cdf_def = MathTex(
            r"F_X(x)", r"=", r"P(X \leq x)",
            font_size=TITLE_SIZE, color=WHITE,
        )
        cdf_def[0].set_color(ACCENT)
        cdf_def[2].set_color(ACCENT)
        self.ly.center_in_content(cdf_def)
        self.play(Write(cdf_def), run_time=SLOW)
        self.wait(0.5)

        box = self.ly.formula_box(cdf_def, color=ACCENT)
        self.play(Create(box), run_time=FAST)
        self.wait(1)

        self.play(FadeOut(box), FadeOut(cdf_def), run_time=FAST)

        # CDF values for 3 coin flips
        self.add_subcaption(
            "For our coin flip example, the CDF is a staircase. "
            "At zero, the probability is one eighth. At one, it "
            "jumps to four eighths, or one half. At two, seven "
            "eighths. And at three, we reach one.",
            duration=24,
        )

        title2 = self.ly.title("CDF: Number of Heads in 3 Flips")

        cdf_vals = [
            Text("F(0) = P(X<=0) = 1/8", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("F(1) = P(X<=1) = 4/8", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("F(2) = P(X<=2) = 7/8", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("F(3) = P(X<=3) = 8/8 = 1", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(cdf_vals, start_from=title2)
        self.wait(1.5)

        self.ly.clear()

        # Properties
        self.add_subcaption(
            "Key properties of any CDF: it always lies between "
            "zero and one, it never decreases, and it starts at "
            "zero on the left and ends at one on the right.",
            duration=16,
        )

        title3 = self.ly.title("CDF Properties")

        cdf_props = [
            Text("0 <= F_X(x) <= 1  for all x", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("F_X is non-decreasing", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("F_X(-inf) = 0,  F_X(+inf) = 1", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(cdf_props, start_from=title3)
        self.wait(1.5)

        self.ly.clear()

    # -- Scene 6: Continuous Random Variables --
    def scene6_continuous_intro(self):
        self.add_subcaption(
            "Not all random variables are discrete. What if X is "
            "the time until the next bus arrives? X could be "
            "three point five minutes, three point five one, three "
            "point five one seven, and so on. Uncountably many "
            "values.",
            duration=24,
        )
        self.ly.section_divider(5, "Continuous Random Variables")

        title = self.ly.title("Continuous")

        def_text = Text(
            "X is continuous if X takes values in an interval.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(def_text, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(def_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(def_text), run_time=FAST)

        # Key difference
        self.add_subcaption(
            "The key difference: for a continuous random variable, "
            "the probability of hitting any exact value is zero. "
            "Instead, we ask about intervals.",
            duration=18,
        )

        title2 = self.ly.title("Key Difference")

        key_eq = MathTex(
            r"P(X = x)", r"=", r"0", r"\quad (\text{for continuous } X)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        key_eq[0].set_color(RED)
        key_eq[2].set_color(RED)
        key_eq[3].set_color(DIM)
        self.ly.center_in_content(key_eq)
        self.play(Write(key_eq), run_time=SLOW)
        self.wait(1)

        self.play(FadeOut(key_eq), run_time=FAST)

        # PDF definition
        self.add_subcaption(
            "Instead of a probability mass function, we use a "
            "Probability Density Function. The probability of "
            "falling in an interval is the area under the curve.",
            duration=18,
        )

        title3 = self.ly.title("PDF")

        pdf_def = MathTex(
            r"P(a \leq X \leq b)", r"=",
            r"\int_a^b", r"f_X(x)", r"\,dx",
            font_size=TITLE_SIZE, color=WHITE,
        )
        pdf_def[0].set_color(ACCENT)
        pdf_def[3].set_color(ACCENT)
        self.ly.center_in_content(pdf_def)
        self.play(Write(pdf_def), run_time=SLOW)
        self.wait(0.5)

        box = self.ly.formula_box(pdf_def, color=ACCENT)
        self.play(Create(box), run_time=FAST)
        self.wait(1)

        self.play(FadeOut(box), FadeOut(pdf_def), run_time=FAST)

        # PDF property
        prop_text = Text(
            "Total area under f_X(x) = 1  (always)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.center_in_content(prop_text)
        self.play(FadeIn(prop_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # -- Scene 7: Discrete vs Continuous Comparison --
    def scene7_comparison(self):
        self.add_subcaption(
            "Let us compare discrete and continuous random "
            "variables side by side. The ideas are parallel, but "
            "the math looks different.",
            duration=16,
        )
        self.ly.section_divider(6, "Comparison")

        title = self.ly.title("Discrete vs Continuous")

        disc_items = [
            Text("Values: countable", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("PMF: bar chart", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("P(X=x) > 0", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Sum of PMF = 1", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        cont_items = [
            Text("Values: uncountable", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("PDF: smooth curve", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("P(X=x) = 0", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Integral of PDF = 1", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]

        disc_header = Text(
            "Discrete", font_size=HEADING_SIZE, color=PRIMARY,
            font=SANS, weight=BOLD,
        )
        cont_header = Text(
            "Continuous", font_size=HEADING_SIZE, color=SECONDARY,
            font=SANS, weight=BOLD,
        )

        self.ly.two_columns(disc_items, cont_items, start_from=title)
        self.wait(2)

        self.ly.clear()

    # -- Scene 8: Summary and Outro --
    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap what we learned today. A random variable "
            "assigns a number to each outcome. Discrete random "
            "variables use a PMF, continuous ones use a PDF. The "
            "CDF works for both.",
            duration=24,
        )

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "Random variable X:  Omega -> R",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Discrete RVs: countable values, PMF",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "PMF:  p_X(x) = P(X=x),  sums to 1",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "CDF:  F_X(x) = P(X<=x),  non-decreasing",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Continuous:  PDF replaces PMF, integrals replace sums",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        self.ly.clear()

        self.add_subcaption(
            "Next time, we will cover expectation and variance, "
            "which measure the center and spread of a random "
            "variable. These are the most important summary "
            "statistics in all of probability.",
            duration=24,
        )

        play_outro(
            self,
            next_video="Expectation and Variance",
            next_playlist="Probability & Statistics",
        )
