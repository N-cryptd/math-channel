"""
Video 154: Lebesgue Measure -- Measure Theory Playlist
TEMPLATE v2 -- Professional quality Manim script

Class: Video154_LebesgueMeasure

Topics: Lebesgue outer measure, translation invariance,
        rationals have measure zero, Caratheodory criterion,
        the Lebesgue sigma-algebra, key properties.

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


class Video154_LebesgueMeasure(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_outer_measure_definition()
        self.scene3_translation_invariance()
        self.scene4_rationals_measure_zero()
        self.scene5_caratheodory_criterion()
        self.scene6_key_properties()
        self.scene7_summary()

    # --- Scene 1: Hook -- "Where Riemann Breaks" ~60s ---

    def scene1_hook(self):
        self.add_subcaption(
            "We've spent three videos building the machinery of measure "
            "theory. Sigma-algebras tell us which sets we can measure, "
            "and the measure function assigns sizes. Now we meet the "
            "most important measure of all: the Lebesgue measure on "
            "the real line. But first, why do we need it?",
            duration=55,
        )
        play_intro(self, "Lebesgue Measure", "Measure Theory")

        title = self.ly.title("Where Riemann Breaks", color=RED)

        item1 = Text(
            "The Dirichlet function: f(x) = 1 on Q, 0 on R\\Q",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Riemann upper sums = 1, lower sums = 0",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        item3 = Text(
            "Not Riemann integrable, but Lebesgue can handle it",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=title, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

    # --- Scene 2: Outer Measure Definition ~90s ---

    def scene2_outer_measure_definition(self):
        self.ly.section_divider(1, "Lebesgue Outer Measure")

        self.add_subcaption(
            "The Lebesgue outer measure is defined by covering a set "
            "with countably many open intervals. The outer measure is "
            "the infimum, the greatest lower bound, of the total "
            "lengths of all such covers.",
            duration=40,
        )

        title = self.ly.title("Definition: Outer Measure", color=PRIMARY)

        subtitle = Text(
            "For any subset A of the real numbers:",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(subtitle, DOWN, anchor=title)

        formula = MathTex(
            r"m^*(A) = \inf \left\{ \sum_{n=1}^{\infty} |I_n| "
            r": A \subseteq \bigcup_{n=1}^{\infty} I_n \right\}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=subtitle)

        self.wait(4)

        # Explanation items
        self.add_subcaption(
            "We cover the set A with a countable collection of open "
            "intervals. The outer measure is the smallest possible "
            "total length over all such covers. Think of it as "
            "wrapping A in blankets and finding the tightest wrap.",
            duration=40,
        )

        item1 = Text(
            "Each I_n is an open interval (a_n, b_n)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "|I_n| = b_n - a_n is its length",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "We take the infimum over ALL such covers",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=formula, reveal_anim=FadeIn,
        )

        self.wait(3)

        # Example
        self.ly.clear()

        self.add_subcaption(
            "As a simple example, the unit interval has outer "
            "measure exactly one. It is covered by itself, giving "
            "total length one, and no cover can be shorter.",
            duration=30,
        )

        title2 = self.ly.title("Example: m*([0,1]) = 1", color=SECONDARY)

        formula2 = MathTex(
            r"[0,1] \subseteq (0, 1) \implies m^*([0,1]) \leq 1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula2, DOWN, anchor=title2)

        item4 = Text(
            "Also m*([0,1]) >= 1, so m*([0,1]) = 1",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(item4, DOWN, anchor=formula2)

        self.wait(3)
        self.ly.clear()

    # --- Scene 3: Translation Invariance ~60s ---

    def scene3_translation_invariance(self):
        self.ly.section_divider(2, "Translation Invariance")

        self.add_subcaption(
            "One of the most important properties of Lebesgue outer "
            "measure is translation invariance. Shifting a set by "
            "any real number x does not change its outer measure. "
            "This is what makes Lebesgue measure geometrically natural.",
            duration=40,
        )

        title = self.ly.title("Translation Invariance", color=PRIMARY)

        formula = MathTex(
            r"m^*(A + x) = m^*(A) \quad \text{for all } x \in \mathbb{R}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=title)

        self.wait(3)

        item1 = Text(
            "A + x = { a + x : a in A } is the shifted set",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Proof: shift every interval in a cover by x",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "Total length is unchanged: |(a+x, b+x)| = b - a",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=formula, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

    # --- Scene 4: Rationals Have Measure Zero ~90s ---

    def scene4_rationals_measure_zero(self):
        self.ly.section_divider(3, "A Stunning Result")

        self.add_subcaption(
            "Here is one of the most surprising results in measure "
            "theory. The rational numbers are countable, and despite "
            "being dense in every interval, they have Lebesgue "
            "outer measure zero.",
            duration=45,
        )

        title = self.ly.title("The Rationals Have Measure Zero", color=RED)

        item1 = Text(
            "Q intersect [0,1] is countable: q_1, q_2, q_3, ...",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Cover q_n by an interval of length epsilon / 2^n",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "Total length = epsilon * sum(1/2^n) = epsilon",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=title, reveal_anim=FadeIn,
        )

        self.wait(3)

        self.ly.clear()

        # The proof formula
        self.add_subcaption(
            "The total length of the cover can be made as small as "
            "we like, since the geometric series sums to one. "
            "Since epsilon is arbitrary, the outer measure is zero. "
            "This means almost every point in the unit interval "
            "is irrational, in a precise mathematical sense.",
            duration=45,
        )

        title2 = self.ly.title("Proof", color=PRIMARY)

        formula1 = MathTex(
            r"\sum_{n=1}^{\infty} \frac{\varepsilon}{2^n} "
            r"= \varepsilon \sum_{n=1}^{\infty} \frac{1}{2^n} "
            r"= \varepsilon",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula1, DOWN, anchor=title2)

        self.wait(3)

        result = MathTex(
            r"m^*(\mathbb{Q} \cap [0,1]) = 0",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(result, DOWN, anchor=formula1)

        self.wait(3)

        item4 = Text(
            "The irrationals in [0,1] have full measure 1",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(item4, DOWN, anchor=result)

        self.wait(3)
        self.ly.clear()

    # --- Scene 5: Caratheodory's Criterion ~90s ---

    def scene5_caratheodory_criterion(self):
        self.ly.section_divider(4, "Measurable Sets")

        self.add_subcaption(
            "Recall from the last video that the Caratheodory condition "
            "is what determines which sets are measurable. A set E is "
            "Lebesgue measurable if it splits every test set A "
            "additively with respect to the outer measure.",
            duration=50,
        )

        title = self.ly.title("Caratheodory's Condition", color=PRIMARY)

        formula = MathTex(
            r"m^*(A) = m^*(A \cap E) + m^*(A \setminus E)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=title)

        self.wait(3)

        item1 = Text(
            "Must hold for ALL subsets A of R",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        item2 = Text(
            "E is Lebesgue measurable iff this condition holds",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2], start_from=formula, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

        # The Lebesgue sigma-algebra
        self.add_subcaption(
            "The collection of all Lebesgue measurable sets forms a "
            "sigma-algebra, which we call the Lebesgue sigma-algebra. "
            "It contains all the Borel sets, and much more.",
            duration=40,
        )

        title2 = self.ly.title("The Lebesgue Sigma-Algebra", color=SECONDARY)

        item3 = Text(
            "L = { E subseteq R : E is Lebesgue measurable }",
            font_size=BODY_SIZE, color=WHITE, font=MONO,
        )
        item4 = Text(
            "L is a sigma-algebra on R",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item5 = Text(
            "L contains all open sets and all Borel sets",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        self.ly.progressive_reveal(
            [item3, item4, item5], start_from=title2, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

    # --- Scene 6: Key Properties ~60s ---

    def scene6_key_properties(self):
        self.ly.section_divider(5, "Key Properties")

        self.add_subcaption(
            "Lebesgue measure has several remarkable properties that "
            "make it the natural notion of length on the real line.",
            duration=40,
        )

        title = self.ly.title("Properties of Lebesgue Measure", color=PRIMARY)

        item1 = Text(
            "Contains all Borel sets (open, closed, countable unions)",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Subsets of null sets are measurable (measure zero)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item3 = Text(
            "Translation invariant: m(E + x) = m(E)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3], start_from=title, reveal_anim=FadeIn,
        )

        self.wait(3)

        self.ly.clear()

        # Lebesgue measure agrees with length
        self.add_subcaption(
            "Perhaps the most reassuring property: Lebesgue measure "
            "agrees with our ordinary notion of length. The measure "
            "of a closed interval from a to b is simply b minus a.",
            duration=35,
        )

        title2 = self.ly.title("Agrees With Length", color=SECONDARY)

        formula = MathTex(
            r"m([a, b]) = b - a",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, DOWN, anchor=title2)

        item4 = Text(
            "Lebesgue measure extends ordinary length to ALL measurable sets",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(item4, DOWN, anchor=formula)

        self.wait(3)
        self.ly.clear()

    # --- Scene 7: Summary & Outro ~30s ---

    def scene7_summary(self):
        self.add_subcaption(
            "Today we defined the Lebesgue outer measure using "
            "interval covers, showed that the rationals have "
            "measure zero, and constructed the Lebesgue "
            "sigma-algebra via Caratheodory's criterion. "
            "Next time we'll see how this leads to the "
            "Lebesgue integral, the true successor to Riemann.",
            duration=40,
        )

        title = self.ly.title("Summary", color=ACCENT)

        item1 = Text(
            "Outer measure: inf of total lengths of interval covers",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        item2 = Text(
            "Rationals in [0,1] have measure zero (but are dense!)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        item3 = Text(
            "Lebesgue measurable: Caratheodory's condition",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        item4 = Text(
            "Lebesgue measure extends ordinary length",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )

        self.ly.progressive_reveal(
            [item1, item2, item3, item4], start_from=title, reveal_anim=FadeIn,
        )

        self.wait(3)
        self.ly.clear()

        play_outro(
            self,
            next_video="The Lebesgue Integral",
            next_playlist="Measure Theory",
        )
