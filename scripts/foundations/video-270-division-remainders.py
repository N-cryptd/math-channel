"""
Video 270: Division and Remainders -- Numbers & Arithmetic (L1 Foundations, Video 5/14)

Division as fair sharing and repeated subtraction, division as the
inverse of multiplication, the division algorithm a = q*b + r with
0 <= r < b, remainder cycles, and why division by zero is undefined.
Connects back to Video 269 (Multiplication) and forward to
Video 271 (Negative Numbers).

Follows v2 template quality rules.
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


class Video270_DivisionRemainders(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_fair_sharing()
        self.scene3_repeated_subtraction()
        self.scene4_inverse_of_multiplication()
        self.scene5_uneven_sharing()
        self.scene6_division_algorithm()
        self.scene7_remainder_cycles()
        self.scene8_dividing_by_zero()
        self.scene9_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook - undoing multiplication
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: division answers 'how many in each group'."""
        self.add_subcaption(
            "Last time we learned multiplication: repeated addition, "
            "areas, and the great laws. Today we ask the reverse "
            "question. If twelve apples are shared equally among "
            "three bags, how many apples go in each bag? "
            "Multiplication built the total from the group size. "
            "Division recovers the group size from the total. It is "
            "multiplication run backwards. And as we will see, "
            "sometimes running it backwards leaves something "
            "left over.",
            duration=38,
        )
        play_intro(self, "Division and Remainders", "Numbers & Arithmetic")

        title = self.ly.title("Multiplication in Reverse")
        items = [
            MathTex(r"3 \times 4 = 12", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"12 \div 3 = \, ?", font_size=BODY_SIZE, color=ACCENT),
            Text("Division undoes multiplication",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(12)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Division as Fair Sharing
    # ------------------------------------------------------------------
    def scene2_fair_sharing(self):
        """Deal 12 dots into 3 rows, one at a time."""
        self.add_subcaption(
            "The most natural way to picture division is fair "
            "sharing. Take twelve dots and deal them out to three "
            "people, one at a time, like dealing cards. First round: "
            "each person gets one dot. Second round: two dots each. "
            "Third round: three. Fourth round: four. The dots are "
            "exhausted, and everyone holds exactly four. So twelve "
            "divided by three equals four. Fair sharing is division.",
            duration=40,
        )
        self.ly.section_divider(1, "Fair Sharing")
        title = self.ly.title("Deal 12 Dots to 3 People")

        # 3 rows x 4 columns dealt left to right
        rows, cols = 3, 4
        dots = VGroup(*[
            Dot(
                RIGHT * (c * 1.0 - (cols - 1) * 0.5)
                + DOWN * (r * 0.8 - (rows - 1) * 0.4),
                radius=0.11,
                color=[PRIMARY, SECONDARY, ACCENT][r],
            )
            for r in range(rows)
            for c in range(cols)
        ])
        dots_group = VGroup(dots)
        self.ly.center_in_content(dots_group)
        # deal order: round-by-round, one dot per person (column-major)
        deal_order = [dots[r * cols + c] for c in range(cols) for r in range(rows)]

        person_labels = VGroup(*[
            Text(name, font_size=LABEL_SIZE, color=DIM, font=SANS)
            .next_to(VGroup(*[dots[r * cols + c] for c in range(cols)]), LEFT, buff=0.5)
            for r, name in enumerate(["A", "B", "C"])
        ])

        formula = MathTex(
            r"12 \div 3 = 4",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, direction=DOWN, anchor=dots_group, buff=0.7)

        self.play(Write(title), run_time=NORMAL)
        self.play(FadeIn(person_labels), run_time=FAST)
        for d in deal_order:
            self.play(FadeIn(d, scale=0.5), run_time=0.18)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(30)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Repeated Subtraction
    # ------------------------------------------------------------------
    def scene3_repeated_subtraction(self):
        """12 - 3 - 3 - 3 - 3 = 0; count the steps."""
        self.add_subcaption(
            "There is a second picture: repeated subtraction. Start "
            "with twelve and keep taking away three. Twelve minus "
            "three is nine. Nine minus three is six. Six minus three "
            "is three. Three minus three is zero. We subtracted three "
            "exactly four times before hitting zero, so the answer is "
            "four. Multiplication is repeated addition; division is "
            "repeated subtraction. Two sides of the same coin.",
            duration=40,
        )
        self.ly.section_divider(2, "Repeated Subtraction")
        title = self.ly.title("Keep Taking Away 3")
        chain = MathTex(
            r"12 \to 9 \to 6 \to 3 \to 0",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(chain)
        count = MathTex(
            r"\text{We subtracted } 3 \text{ four times} \;\Rightarrow\; 12 \div 3 = 4",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(count, direction=DOWN, anchor=chain, buff=0.8)
        self.play(Write(title), run_time=NORMAL)
        self.play(Write(chain), run_time=SLOW)
        self.wait(8)
        self.play(Write(count), run_time=NORMAL)
        self.wait(22)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Division as the Inverse of Multiplication
    # ------------------------------------------------------------------
    def scene4_inverse_of_multiplication(self):
        """If b x q = a then a / b = q."""
        self.add_subcaption(
            "Here is the algebraic view. Multiplication and division "
            "are inverse operations, just like addition and "
            "subtraction. If three times four is twelve, then twelve "
            "divided by three must be four, and twelve divided by "
            "four must be three. Every multiplication fact gives you "
            "two division facts for free. This is why memorizing "
            "times tables makes division automatic.",
            duration=32,
        )
        self.ly.section_divider(3, "Inverse Operations")
        title = self.ly.title("Two Facts for the Price of One")
        pairs = [
            MathTex(r"3 \times 4 = 12", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"12 \div 3 = 4", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"12 \div 4 = 3", font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(pairs, start_from=title)
        self.wait(20)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Uneven Sharing - The Remainder Appears
    # ------------------------------------------------------------------
    def scene5_uneven_sharing(self):
        """13 dots to 3 people: 4 each, 1 left over."""
        self.add_subcaption(
            "Now for the surprise. Take thirteen dots and deal them "
            "to three people. One, two, three, three rounds: everyone "
            "has four. That accounts for twelve dots, but we started "
            "with thirteen. One dot is left over, and no whole dot "
            "can be shared without breaking it. We write thirteen "
            "divided by three equals four, remainder one. The leftover "
            "is called the remainder, and it is the star of today's "
            "show.",
            duration=42,
        )
        self.ly.section_divider(4, "The Remainder")
        title = self.ly.title("13 Dots to 3 People")

        rows, cols = 3, 4
        dots = VGroup(*[
            Dot(
                RIGHT * (c * 1.0 - (cols - 1) * 0.5) + LEFT * 0.8
                + DOWN * (r * 0.8 - (rows - 1) * 0.4),
                radius=0.11,
                color=[PRIMARY, SECONDARY, ACCENT][r],
            )
            for r in range(rows)
            for c in range(cols)
        ])
        leftover = Dot(RIGHT * 3.2, radius=0.14, color=RED)
        dots_group = VGroup(dots, leftover)
        self.ly.center_in_content(dots_group)

        left_label = MathTex(r"4 \text{ each}", font_size=LABEL_SIZE, color=WHITE)
        left_label.move_to(LEFT * 0.8 + DOWN * 2.0)
        rem_label = MathTex(r"1 \text{ left over}", font_size=LABEL_SIZE, color=RED)
        rem_label.next_to(leftover, UP, buff=0.3)

        formula = MathTex(
            r"13 \div 3 = 4 \text{ R } 1",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(formula, direction=DOWN, anchor=left_label, buff=0.5)

        self.play(Write(title), run_time=NORMAL)
        self.play(FadeIn(dots, lag_ratio=0.03), run_time=NORMAL)
        self.play(Write(left_label), run_time=FAST)
        self.play(FadeIn(leftover, scale=2.0), run_time=NORMAL)
        self.play(Write(rem_label), run_time=FAST)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(28)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: The Division Algorithm
    # ------------------------------------------------------------------
    def scene6_division_algorithm(self):
        """a = q*b + r with 0 <= r < b."""
        self.add_subcaption(
            "Every division of whole numbers fits one universal "
            "pattern, called the division algorithm. Divide a by b: "
            "the answer is a quotient q and a remainder r, with "
            "a equals q times b plus r. In words: the total is some "
            "number of full groups, plus a leftover that is too "
            "small to form another group. That last condition is "
            "crucial: the remainder must be strictly less than b. "
            "If the leftover were b or more, we could peel off "
            "another full group. Check our example: thirteen equals "
            "three times four plus one. Perfect.",
            duration=48,
        )
        self.ly.section_divider(5, "The Division Algorithm")
        title = self.ly.title("One Pattern for Every Division")
        formula = MathTex(
            r"a = q \times b + r, \qquad 0 \le r < b",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(formula)
        check = MathTex(
            r"13 = 3 \times 4 + 1",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(check, direction=DOWN, anchor=formula, buff=0.7)
        self.play(Write(title), run_time=NORMAL)
        self.play(Write(formula), run_time=SLOW)
        self.wait(10)
        self.play(Write(check), run_time=NORMAL)
        self.wait(28)
        self.ly.clear()

        # Why r < b
        self.add_subcaption(
            "Why must the remainder be smaller than the divisor? "
            "Suppose you divided thirteen by three and answered "
            "quotient three, remainder four. But four is bigger than "
            "three, so those four leftovers contain another full "
            "group of three. Your division simply was not finished. "
            "Quotient four, remainder one is the unique answer with "
            "a remainder smaller than three.",
            duration=30,
        )
        title2 = self.ly.title("Why r < b ?")
        items = [
            Text("Leftover 4 contains another group of 3",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Not finished yet: keep dividing",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("Remainder must always be < divisor",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(18)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Remainder Cycles
    # ------------------------------------------------------------------
    def scene7_remainder_cycles(self):
        """Counting by 3s: remainders cycle 0,1,2 - foreshadow mod arithmetic."""
        self.add_subcaption(
            "Remainders hide a beautiful secret. Watch the remainder "
            "when you divide the counting numbers by three. One "
            "leaves remainder one. Two leaves two. Three leaves "
            "zero. Four leaves one again. Five leaves two. Six "
            "leaves zero. The remainders cycle: one, two, zero, "
            "one, two, zero, forever. Dividing by seven gives a "
            "cycle of length seven. This cycling idea becomes "
            "modular arithmetic, the mathematics of clocks and "
            "codes, which we will meet later in this playlist.",
            duration=44,
        )
        self.ly.section_divider(6, "Remainder Cycles")
        title = self.ly.title("Dividing by 3: a Cycle")
        table = VGroup(
            MathTex(
                r"n:", r"\ 1", r"\ \ 2", r"\ \ 3", r"\ \ 4", r"\ \ 5", r"\ \ 6", r"\ \ 7", r"\ \ 8",
                font_size=BODY_SIZE, color=WHITE,
            ),
            MathTex(
                r"n \bmod 3:", r"\ 1", r"\ \ 2", r"\ \ 0", r"\ \ 1", r"\ \ 2", r"\ \ 0", r"\ \ 1", r"\ \ 2",
                font_size=BODY_SIZE, color=ACCENT,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        self.ly.center_in_content(table)
        self.play(Write(title), run_time=NORMAL)
        self.play(Write(table), run_time=SLOW)
        self.wait(12)
        self.ly.clear()

        # Cycle highlight
        cycle = MathTex(
            r"1 \to 2 \to 0 \to 1 \to 2 \to 0 \to \cdots",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(cycle)
        note = Text(
            "Remainders repeat forever - the seed of modular arithmetic",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=cycle, buff=0.8)
        self.play(Write(cycle), run_time=SLOW)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(20)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Dividing by Zero
    # ------------------------------------------------------------------
    def scene8_dividing_by_zero(self):
        """Why a / 0 is undefined."""
        self.add_subcaption(
            "One famous question remains: why can't we divide by "
            "zero? Twelve divided by three asks: three groups of "
            "how many make twelve? But twelve divided by zero asks: "
            "zero groups of how many make twelve? Zero groups of "
            "anything is zero groups of nothing: total zero. No "
            "number can work. The question has no answer, so we "
            "declare twelve divided by zero undefined. Division by "
            "zero is not a mistake you get punished for; it is a "
            "question mathematics refuses to answer.",
            duration=44,
        )
        self.ly.section_divider(7, "The Forbidden Division")
        title = self.ly.title("Why Not Divide by Zero?")
        items = [
            MathTex(r"12 \div 3 = q \iff 3 \times q = 12", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"12 \div 0 = q \iff 0 \times q = 12", font_size=BODY_SIZE, color=RED),
            Text("0 x anything = 0. Never 12. No answer exists.",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            MathTex(r"12 \div 0 \ \text{is undefined}",
                    font_size=BODY_SIZE, color=WHITE),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(30)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Summary
    # ------------------------------------------------------------------
    def scene9_summary(self):
        """Recap division and remainders."""
        self.add_subcaption(
            "Let us recap. Division is fair sharing and repeated "
            "subtraction, the inverse of multiplication. Every "
            "division of whole numbers gives a quotient and a "
            "remainder, obeying a equals q times b plus r with "
            "remainder strictly less than b. Remainders cycle with "
            "beautiful regularity, planting the seed of modular "
            "arithmetic. And division by zero is undefined because "
            "no number can answer it. But sharing gets stranger "
            "still: what if we owe someone apples? To handle debts, "
            "we need numbers smaller than zero. That is negative "
            "numbers, next time. See you then.",
            duration=50,
        )
        self.ly.section_divider(8, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Division = fair sharing = repeated subtraction",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Inverse of multiplication: 3x4=12 gives 12/3=4",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("a = q x b + r with 0 <= r < b",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Remainders cycle - the seed of modular arithmetic",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Division by zero is undefined",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(21)
        self.ly.clear()
        play_outro(self, next_video="Negative Numbers", next_playlist="Numbers & Arithmetic")
