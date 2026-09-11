"""
Video 274: Exponents -- Numbers & Arithmetic (L1 Foundations, Video 9/14)

Pattern-first spine (competitive analysis, improvements.md Sep 2026):
repeated-multiplication build-up -> the tower (base/exponent vocabulary)
-> squared/cubed geometry nicknames -> THE LADDER (successive division,
Khan's proven intuition modernized with animation) -> the zero rung
(2^0 = 1 forced by the pattern) -> negative exponents as fractions ->
the laws as CONSEQUENCES of counting copies (multiply=add, divide=subtract,
power-of-power=multiply) -> powers of ten payoff: the place value chart
from Video 273 IS the powers of ten in a row -> summary + Roots teaser.

Differentiation: laws are SEEN as chain-counting, never presented as named
rules to memorize (anti-TOCT); the division ladder is fully animated
(nobody else does this); series continuity with Video 273's place-value
columns (uniquely ours).

Follows v2 template quality rules (5-item budget, LayoutEngine only,
progressive disclosure, SANS/MONO discipline, raw-string LaTeX).
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


class Video274_Exponents(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_tower()
        self.scene3_square_cube()
        self.scene4_ladder()
        self.scene5_zero()
        self.scene6_negative()
        self.scene7_multiply()
        self.scene8_divide()
        self.scene9_power_of_power()
        self.scene10_powers_of_ten()
        self.scene11_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook - numbers that grow by jumping
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: doubling is fast, but writing it is torture -> shorthand."""
        self.add_subcaption(
            "Here is a number that grows by jumping. Start with two, and "
            "multiply by two, over and over. Two times two is four. Four "
            "times two is eight. Eight times two is sixteen. Keep going: "
            "thirty-two, sixty-four, one hundred twenty-eight. Each jump "
            "doubles where we were. Doubling is sneaky. After just ten "
            "jumps, two has become one thousand twenty-four. After twenty "
            "jumps, over a million. But writing this is a pain. Two times "
            "two times two, and so on: twenty multiplications is a "
            "paragraph, and one hundred of them is a wall of symbols. "
            "Mathematicians are lazy in the best way: when something "
            "repeats, they invent a shorthand. Today we build that "
            "shorthand, watch it climb down a ladder to zero and below, "
            "and discover that the place value chart from last time was "
            "secretly made of these jumps all along.",
            duration=54.8,
        )
        play_intro(self, "Exponents", "Numbers & Arithmetic")

        title = self.ly.title("Numbers That Jump")

        chain = MathTex(
            r"2 \to 4 \to 8 \to 16 \to 32 \to 64 \to 128",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(chain)
        self.play(Write(chain), run_time=SLOW)
        self.wait(3)

        long_chain = MathTex(
            r"2 \times 2 \times 2 \times 2 \times \cdots",
            font_size=HEADING_SIZE, color=DIM,
        )
        self.ly.safe_place(long_chain, direction=DOWN, anchor=chain, buff=0.7)
        self.play(Write(long_chain), run_time=NORMAL)
        self.wait(2)

        question = Text(
            "how do you write a hundred twos, without the pain?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(question, direction=DOWN, anchor=long_chain, buff=0.6)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(39.3)  # pacing: extends caption slot to natural + 2.0
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: The tower - base and exponent
    # ------------------------------------------------------------------
    def scene2_tower(self):
        """Expanded form squeezed into a tower; name the two jobs."""
        self.add_subcaption(
            "Here is the shorthand. Two times two times two times two "
            "times two: the same factor, five times. We squeeze it into a "
            "tower: a two, with a small five in the corner. The big number "
            "is called the base: it is the thing being multiplied. The "
            "small raised number is called the exponent: it counts the "
            "copies. Two to the fifth power means five copies of two, "
            "multiplied together. Reading is easy once you see the two "
            "jobs: the base tells you what number, and the exponent tells "
            "you how many times. Six to the third power is six copies of "
            "six. Ten to the fourth power is ten copies of ten. And you "
            "can always unfold the tower to check your work: write the "
            "copies out and multiply left to right. Two to the fifth "
            "unfolds to thirty-two. The tower is not a new operation. It "
            "is counting in disguise.",
            duration=52.2,
        )
        self.ly.section_divider(1, "The Shorthand")
        title = self.ly.title("The Tower of Copies")

        expanded = MathTex(
            r"2 \times 2 \times 2 \times 2 \times 2",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(expanded, direction=DOWN, anchor=title, buff=0.8)
        self.play(Write(expanded), run_time=NORMAL)
        self.wait(2)

        tower = MathTex(r"2^{5}", font_size=72, color=ACCENT)
        self.ly.center_in_content(tower)
        self.play(Write(tower), run_time=SLOW)
        self.wait(2)

        exp_label = Text(
            "exponent: counts the copies",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(exp_label, direction=UP, anchor=tower, buff=0.4)
        base_label = Text(
            "base: the number being multiplied",
            font_size=LABEL_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(base_label, direction=DOWN, anchor=tower, buff=0.4)
        self.play(
            FadeIn(exp_label, shift=LEFT * 0.15),
            FadeIn(base_label, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(3)

        check = MathTex(
            r"2^{5} = 32", font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(check, direction=DOWN, anchor=base_label, buff=0.5)
        self.play(FadeOut(expanded), run_time=FAST)
        self.play(Write(check), run_time=NORMAL)
        self.wait(35.5)  # pacing: extends caption slot (render-1 bump +0.78)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Squared, cubed, and the first power
    # ------------------------------------------------------------------
    def scene3_square_cube(self):
        """Geometry nicknames: squares are areas, cubes are volumes."""
        self.add_subcaption(
            "Some exponents have nicknames that come from geometry. Three "
            "to the second power is called squared, because a square with "
            "side three holds three rows of three: nine little cells. "
            "Three squared is nine: the exponent is a side length, and the "
            "answer is an area. Two to the third power is called cubed, "
            "because a cube with side two holds two by two by two: eight "
            "little blocks. Two cubed is eight: the answer is a volume. "
            "One more easy case before the interesting part: an exponent "
            "of one. Three to the first power is just one copy of three: "
            "three. Nothing deep is happening. The exponent counts the "
            "copies, and one copy is the number itself. So far our ladder "
            "only climbs up. Next we point it down, and that is where "
            "exponents get strange, in the best possible way.",
            duration=52.5,
        )
        self.ly.section_divider(2, "Squares and Cubes")
        title = self.ly.title("Nicknames from Geometry")

        cells = VGroup(*[
            Square(side_length=0.52, stroke_color=PRIMARY, stroke_width=2,
                   fill_color=ACCENT, fill_opacity=0.35)
            for _ in range(9)
        ]).arrange_in_grid(rows=3, cols=3, buff=0.06)
        self.ly.center_in_content(cells)
        self.play(FadeIn(cells, lag_ratio=0.15), run_time=NORMAL)
        self.wait(2)

        sq_label = MathTex(
            r"3^{2} = 9 \quad \text{three squared: an area}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(sq_label, direction=DOWN, anchor=cells, buff=0.5)
        self.play(Write(sq_label), run_time=NORMAL)
        self.wait(2)

        cube_tex = MathTex(
            r"2^{3} = 2 \cdot 2 \cdot 2 = 8 \quad \text{two cubed: a volume}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(cube_tex, direction=DOWN, anchor=sq_label, buff=0.5)
        self.play(Write(cube_tex), run_time=NORMAL)
        self.wait(2)

        self.play(FadeOut(cells), FadeOut(sq_label), run_time=FAST)

        one_tex = MathTex(
            r"3^{1} = 3 \quad \text{one copy: the number itself}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(one_tex)
        self.play(Write(one_tex), run_time=NORMAL)
        self.wait(37.6)  # pacing: extends caption slot (render-1 bump +0.81)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: The ladder - divide by the base at every step
    # ------------------------------------------------------------------
    def scene4_ladder(self):
        """2^5 -> 2^1: every step down divides by the base. The pattern."""
        self.add_subcaption(
            "Watch this ladder. Start at two to the fifth: thirty-two. "
            "Step down to two to the fourth. What happened to the value? "
            "Thirty-two became sixteen: it was divided by two. Step down "
            "again: two to the third is eight, divided by two once more. "
            "Again: two to the second is four. Again: two to the first is "
            "two. Every single step down this ladder divides by the base. "
            "And this is not a trick we chose. It is what the tower means: "
            "two to the fourth has one fewer copy of two than two to the "
            "fifth, so its value is two times smaller. The exponent counts "
            "copies, so losing a copy divides. Pause and sit with this "
            "ladder, because it is about to answer two famous questions "
            "for us. The pattern is in charge now. Where the numbers go "
            "next is the ladder's decision, not ours.",
            duration=51.7,
        )
        self.ly.section_divider(3, "The Ladder")
        title = self.ly.title("Step Down, Divide by Two")

        ladder = VGroup(*[
            MathTex(tex, font_size=BODY_SIZE, color=WHITE)
            for tex in (
                r"2^{5} = 32", r"2^{4} = 16", r"2^{3} = 8",
                r"2^{2} = 4", r"2^{1} = 2",
            )
        ]).arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        for row, d in zip(ladder, (r"\div 2",) * 4 + (r"",)):
            if d:
                mark = MathTex(d, font_size=LABEL_SIZE, color=RED)
                mark.next_to(row, RIGHT, buff=0.8)
                row.add(mark)
        self.ly.center_in_content(ladder)
        self.play(FadeIn(ladder, lag_ratio=0.3), run_time=SLOW)
        self.wait(2)

        self.play(
            Indicate(ladder[0], color=ACCENT), run_time=NORMAL,
        )
        self.wait(2)

        box = SurroundingRectangle(
            ladder[0], color=ACCENT, buff=0.14, corner_radius=0.08,
            stroke_width=2,
        )
        self.play(Create(box), run_time=NORMAL)
        self.wait(39.8)  # pacing: extends caption slot (render-1 bump +0.39)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: The zero rung
    # ------------------------------------------------------------------
    def scene5_zero(self):
        """The ladder forces 2^0 = 1; any nonzero base to the zero is 1."""
        self.add_subcaption(
            "So keep stepping. Two to the first is two. Divide by two one "
            "more time, and the ladder insists the next value is one. And "
            "which rung is that? Two to the zero. One. Not zero: one. Two "
            "to the zero power is one. That looks bizarre if you expect "
            "zero powers to mean nothing, but the ladder says otherwise: "
            "it is exactly one divide-by-two past two to the first. The "
            "pattern does not care that zero feels special. And it is not "
            "just two. Five to the zero: start at five, divide by five, "
            "and you land on one. One hundred to the zero: one. Any "
            "nonzero number, raised to the zero power, is one. "
            "Mathematicians did not vote on this. The pattern of dividing "
            "by the base, followed faithfully, forces the answer. Zero is "
            "not nothing. It is one step below one.",
            duration=53.1,
        )
        self.ly.section_divider(4, "The Zero Rung")
        title = self.ly.title("One Step Below One")

        rungs = VGroup(
            MathTex(r"2^{1} = 2", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"2^{0} = 1", font_size=HEADING_SIZE, color=ACCENT),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        self.ly.center_in_content(rungs)
        self.play(FadeIn(rungs, lag_ratio=0.5), run_time=NORMAL)
        self.wait(2)

        box = SurroundingRectangle(
            rungs[1], color=ACCENT, buff=0.14, corner_radius=0.08,
            stroke_width=2,
        )
        self.play(Create(box), run_time=NORMAL)
        self.wait(2)

        cousins = MathTex(
            r"5^{0} = 1 \qquad 100^{0} = 1 \qquad 1000^{0} = 1",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(cousins, direction=DOWN, anchor=rungs, buff=0.7)
        self.play(Write(cousins), run_time=NORMAL)
        self.wait(2)

        rule = self.ly.formula_box(
            MathTex(r"a^{0} = 1 \quad (a \neq 0)",
                    font_size=HEADING_SIZE, color=ACCENT)
        )
        self.ly.safe_place(rule, direction=DOWN, anchor=cousins, buff=0.6)
        self.play(Write(rule[0]), run_time=NORMAL)
        self.play(Create(rule[1]), run_time=FAST)
        self.wait(38.2)  # pacing: extends caption slot (render-1 bump +0.79)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Below zero - negative exponents are fractions
    # ------------------------------------------------------------------
    def scene6_negative(self):
        """The ladder keeps dividing: 2^-n = 1/2^n; 10^-1 = 0.1 tie-in."""
        self.add_subcaption(
            "Why stop at zero? The ladder keeps dividing. Two to the zero "
            "is one. Divide by two, and two to the minus one must be one "
            "half. Divide again: two to the minus two is one quarter. "
            "Again: one eighth. Negative exponents do not make negative "
            "numbers. They make fractions: one over the positive power. "
            "Two to the minus three is one over two cubed: one over eight. "
            "The minus sign is a direction on the ladder, down into the "
            "fractions, not a flip into the negatives. And here is the "
            "payoff from last time. Ten to the minus one is one tenth: "
            "zero point one. Ten to the minus two is one hundredth: zero "
            "point zero one. The tenths and hundredths columns in every "
            "decimal you have ever written? Those places are negative "
            "exponents of ten, sitting quietly to the right of the decimal "
            "point.",
            duration=53.0,
        )
        self.ly.section_divider(5, "Below Zero")
        title = self.ly.title("Down into the Fractions")

        rungs = VGroup(
            MathTex(r"2^{0} = 1", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"2^{-1} = \tfrac{1}{2}", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"2^{-2} = \tfrac{1}{4}", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"2^{-3} = \tfrac{1}{8}", font_size=BODY_SIZE, color=ACCENT),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.ly.center_in_content(rungs)
        self.play(FadeIn(rungs, lag_ratio=0.3), run_time=SLOW)
        self.wait(2)

        rule = self.ly.formula_box(
            MathTex(r"a^{-b} = \tfrac{1}{a^{\,b}}",
                    font_size=HEADING_SIZE, color=ACCENT)
        )
        self.ly.safe_place(rule, direction=DOWN, anchor=rungs, buff=0.55)
        self.play(Write(rule[0]), run_time=NORMAL)
        self.play(Create(rule[1]), run_time=FAST)
        self.wait(2)

        tie = MathTex(
            r"10^{-1} = 0.1 \qquad 10^{-2} = 0.01",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(tie, direction=DOWN, anchor=rule, buff=0.55)
        self.play(Write(tie), run_time=NORMAL)
        self.wait(40.5)  # pacing: extends caption slot (render-1 bump +0.84)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Multiplying powers - chains merge, exponents add
    # ------------------------------------------------------------------
    def scene7_multiply(self):
        """2^3 x 2^2: unfold, glue the chains, count -> add exponents."""
        self.add_subcaption(
            "Now, the rules everyone memorizes. Except we are going to see "
            "them instead. Take two to the third, times two to the second. "
            "Unfold both towers. The first is three copies of two. The "
            "second is two copies. Multiply them, and you get five copies "
            "of two in one long chain. Five copies is two to the fifth. So "
            "the exponents added: three plus two is five. That is the "
            "whole secret. Multiplying powers of the same base glues "
            "their chains together, and gluing chains adds their lengths. "
            "Four to the second times four to the third: two plus three "
            "copies, four to the fifth. You never have to trust the rule: "
            "unfold, count, refold. One warning: the base must match. Two "
            "to the third times three to the second mixes different "
            "factors, the chains do not merge, and the shortcut does not "
            "apply. Same base: add the exponents.",
            duration=58.1,
        )
        self.ly.section_divider(6, "Chains That Merge")
        title = self.ly.title("Multiplying Powers")

        t1 = MathTex(r"2^{3} \times 2^{2}", font_size=HEADING_SIZE, color=WHITE)
        self.ly.center_in_content(t1)
        self.play(Write(t1), run_time=NORMAL)
        self.wait(2)

        t2 = MathTex(
            r"(2 \cdot 2 \cdot 2) \times (2 \cdot 2)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        t2.move_to(t1)
        self.play(ReplacementTransform(t1, t2), run_time=NORMAL)
        self.wait(2)

        t3 = MathTex(
            r"(2 \cdot 2 \cdot 2) \times (2 \cdot 2) = 2^{5}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        t3.move_to(t2)
        self.play(ReplacementTransform(t2, t3), run_time=NORMAL)
        self.wait(2)

        rule = self.ly.formula_box(
            MathTex(r"a^{m} \cdot a^{n} = a^{m+n}",
                    font_size=HEADING_SIZE, color=ACCENT)
        )
        self.ly.safe_place(rule, direction=DOWN, anchor=t3, buff=0.6)
        self.play(Write(rule[0]), run_time=NORMAL)
        self.play(Create(rule[1]), run_time=FAST)
        self.wait(2)

        caution = Text(
            "same base only: the chains must hold the same number",
            font_size=LABEL_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(caution, direction=DOWN, anchor=rule, buff=0.5)
        self.play(FadeIn(caution, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(39.9)  # pacing: extends caption slot (render-1 bump +1.33)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Dividing powers - cancel pairs, subtract
    # ------------------------------------------------------------------
    def scene8_divide(self):
        """2^5 / 2^2: cancel pairs -> subtract exponents; the ladder again."""
        self.add_subcaption(
            "Division runs the film backward. Two to the fifth, divided "
            "by two to the second. Write it as a fraction: five copies of "
            "two on top, two copies underneath. Cancel the pairs: two "
            "strike out below, and two strike out on top. Three copies "
            "survive: two to the third. The exponents subtracted: five "
            "minus two. You have already met this rule in disguise. The "
            "ladder from earlier divides at every single step, and every "
            "step lowers the exponent by one: that is this rule, taken "
            "one divide at a time. Dividing by the base climbs down one "
            "rung. Dividing by a power of the base jumps down several "
            "rungs at once. Same base on top and bottom: subtract the "
            "exponents. And once again, we did not memorize anything. We "
            "unfolded, crossed out matching pairs, and counted what "
            "survived.",
            duration=53.6,
        )
        self.ly.section_divider(7, "Chains That Cancel")
        title = self.ly.title("Dividing Powers")

        frac = MathTex(r"\dfrac{2^{5}}{2^{2}}",
                       font_size=HEADING_SIZE, color=WHITE)
        self.ly.center_in_content(frac)
        self.play(Write(frac), run_time=NORMAL)
        self.wait(2)

        solved = MathTex(
            r"\dfrac{2^{5}}{2^{2}} = 2^{5-2} = 2^{3}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        solved.move_to(frac)
        self.play(ReplacementTransform(frac, solved), run_time=NORMAL)
        self.wait(2)

        rule = self.ly.formula_box(
            MathTex(r"\dfrac{a^{m}}{a^{n}} = a^{m-n}",
                    font_size=HEADING_SIZE, color=ACCENT)
        )
        self.ly.safe_place(rule, direction=DOWN, anchor=solved, buff=0.65)
        self.play(Write(rule[0]), run_time=NORMAL)
        self.play(Create(rule[1]), run_time=FAST)
        self.wait(2)

        tie = Text(
            "the ladder, jumping several rungs at once",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(tie, direction=DOWN, anchor=rule, buff=0.5)
        self.play(FadeIn(tie, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(38.6)  # pacing: extends caption slot (render-1 bump +1.04)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Power of a power - repackage the chains
    # ------------------------------------------------------------------
    def scene9_power_of_power(self):
        """(2^3)^2: chains of three, two rows of them -> multiply."""
        self.add_subcaption(
            "One more move: a tower on a tower. Take two to the third, "
            "and square the whole thing: two to the third, times itself. "
            "Unfold: three copies of two, then three copies again. Six "
            "copies in total: two to the sixth. The exponents multiplied: "
            "three times two. Think of it as repackaging. The outer "
            "exponent says how many chains to lay side by side, and the "
            "inner exponent says how long each chain is. Chains of three, "
            "laid down two times: six. So a power of a power multiplies "
            "the exponents. Five to the second, cubed: two times three is "
            "six, five to the sixth. Careful not to mix this up with the "
            "last rule: multiplying two powers adds the exponents, but "
            "repeating one power multiplies them. If you ever forget "
            "which is which, unfold one small example and count. The "
            "copies never lie.",
            duration=56.6,
        )
        self.ly.section_divider(8, "A Tower on a Tower")
        title = self.ly.title("Power of a Power")

        p1 = MathTex(r"\left(2^{3}\right)^{2}",
                     font_size=HEADING_SIZE, color=WHITE)
        self.ly.center_in_content(p1)
        self.play(Write(p1), run_time=NORMAL)
        self.wait(2)

        p2 = MathTex(
            r"(2 \cdot 2 \cdot 2) \times (2 \cdot 2 \cdot 2)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        p2.move_to(p1)
        self.play(ReplacementTransform(p1, p2), run_time=NORMAL)
        self.wait(2)

        p3 = MathTex(
            r"\left(2^{3}\right)^{2} = 2^{3 \times 2} = 2^{6}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        p3.move_to(p2)
        self.play(ReplacementTransform(p2, p3), run_time=NORMAL)
        self.wait(2)

        rule = self.ly.formula_box(
            MathTex(r"\left(a^{m}\right)^{n} = a^{m \cdot n}",
                    font_size=HEADING_SIZE, color=ACCENT)
        )
        self.ly.safe_place(rule, direction=DOWN, anchor=p3, buff=0.6)
        self.play(Write(rule[0]), run_time=NORMAL)
        self.play(Create(rule[1]), run_time=FAST)
        self.wait(2)

        compare = Text(
            "two powers: add - one power twice: multiply",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(compare, direction=DOWN, anchor=rule, buff=0.5)
        self.play(FadeIn(compare, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(38.5)  # pacing: extends caption slot (render-1 bump +1.42)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: The powers of ten - place value was exponents all along
    # ------------------------------------------------------------------
    def scene10_powers_of_ten(self):
        """The 273 payoff: the place value chart = powers of ten in a row."""
        self.add_subcaption(
            "Time to collect the reward promised at the start. The powers "
            "of ten. Ten to the first is ten. Ten to the second is one "
            "hundred. Ten to the third is one thousand. Ten to the zero: "
            "by the ladder, one. Ten to the minus one: one tenth. Ten to "
            "the minus two: one hundredth. Now look at a number you know: "
            "three thousand six hundred forty-five point two. Its columns "
            "are one thousand, one hundred, ten, and one: ten to the "
            "three, ten to the two, ten to the one, ten to the zero. And "
            "past the point: one tenth and two tenths, ten to the minus "
            "one. The entire place value chart, the one we marched across "
            "last time, is just the powers of ten standing in a row. "
            "Every number you will ever write is a sum of "
            "ten-to-the-something columns. Exponents were underneath your "
            "arithmetic the whole time.",
            duration=54.3,
        )
        self.ly.section_divider(9, "The Powers of Ten")
        title = self.ly.title("You Already Knew This")

        up_row = MathTex(
            r"10^{3} = 1000 \quad 10^{2} = 100 \quad 10^{1} = 10 \quad 10^{0} = 1",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(up_row, direction=DOWN, anchor=title, buff=0.9)
        self.play(Write(up_row), run_time=NORMAL)
        self.wait(2)

        down_row = MathTex(
            r"10^{-1} = 0.1 \qquad 10^{-2} = 0.01",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(down_row, direction=DOWN, anchor=up_row, buff=0.55)
        self.play(Write(down_row), run_time=NORMAL)
        self.wait(2)

        number = MathTex(
            r"3645.2 = 3{\cdot}10^{3} + 6{\cdot}10^{2} + 4{\cdot}10^{1}"
            r" + 5{\cdot}10^{0} + 2{\cdot}10^{-1}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        ensure_fits(number)
        self.ly.safe_place(number, direction=DOWN, anchor=down_row, buff=0.7)
        self.play(Write(number), run_time=SLOW)
        self.wait(42.4)  # pacing: extends caption slot (render-1 bump +1.12)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 11: Summary + outro
    # ------------------------------------------------------------------
    def scene11_summary(self):
        """Recap the pattern; tease Roots and Radicals."""
        self.add_subcaption(
            "Let us recap. An exponent is a counter: the base tells you "
            "the number, and the exponent tells you how many copies "
            "multiply together. Climb the ladder by multiplying by the "
            "base, and climb down by dividing. Followed faithfully, the "
            "pattern forces the famous facts: anything to the first is "
            "itself, anything nonzero to the zero is one, and negative "
            "exponents are fractions, one over the positive power. The "
            "three rules are bookkeeping on chains of copies: multiplying "
            "powers with the same base adds the exponents, dividing "
            "subtracts them, and a power of a power multiplies them. "
            "Squared means area, cubed means volume, and the columns of "
            "place value are the powers of ten, from thousands down to "
            "tenths. Next time: the ladder in reverse. If two to the "
            "third makes eight, what number times itself makes nine? What "
            "undoes a square? That is roots and radicals. See you then.",
            duration=58.9,
        )
        self.ly.section_divider(10, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("An exponent counts copies: 2^5 = 32",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The ladder: multiply climbs, divide descends",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("a^1 = a,  a^0 = 1,  a^-b = 1/a^b",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Same base: x adds, / subtracts, (a^m)^n multiplies",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Place value = the powers of ten, up and down",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(41.6)  # pacing: last caption slot (incl. outro) >= natural + 2.0
        self.ly.clear()
        play_outro(self, next_video="Roots and Radicals",
                   next_playlist="Numbers & Arithmetic")
