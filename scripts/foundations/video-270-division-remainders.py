"""
Video 270: Division and Remainders -- Numbers & Arithmetic (L1 Foundations, Video 5/14)

Division as repeated subtraction: the quotient counts full groups, the
remainder is the leftover. The division algorithm a = q*b + r with
0 <= r < b and uniqueness of (q, r), long division (735 / 6) as chunked
subtraction, divisibility (r = 0), and remainder cycles as the seed of
modular arithmetic. Connects back to Video 269 (Multiplication) and
forward to Video 271 (Negative Numbers & Integers).

Follows v2 template quality rules.
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


class Video270_DivisionRemainders(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_repeated_subtraction()
        self.scene3_number_line()
        self.scene4_quotient_remainder()
        self.scene5_division_algorithm()
        self.scene6_worked_examples()
        self.scene7_why_remainder_smaller()
        self.scene8_long_division()
        self.scene9_remainder_zero()
        self.scene10_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook - what if it doesn't split evenly?
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: 17 cookies, 5 friends -- leftovers matter."""
        self.add_subcaption(
            "Last time we built multiplication as repeated addition. "
            "Today we ask the reverse question: instead of combining "
            "equal groups, can we split things into equal groups? "
            "Imagine seventeen cookies and five hungry friends. "
            "Everyone should get a fair share. But seventeen doesn't "
            "split into five equal whole-number groups. Everyone gets "
            "three cookies, and two are left sitting on the plate. "
            "What do we do with the leftovers? That leftover is called "
            "the remainder, and it turns out to be one of the most "
            "important ideas in all of mathematics.",
            duration=38,
        )
        play_intro(self, "Division and Remainders", "Numbers & Arithmetic")

        title = self.ly.title("What If It Doesn't Split Evenly?")
        items = [
            Text("17 cookies, 5 friends: how many each?",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Everyone gets 3, but 2 cookies are left over",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("The leftovers matter as much as the share",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        # pacing fix t_ca7fa7ff: caption 1 slot 19.3s vs 33.4s TTS -> +21s
        self.wait(29)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Division as Repeated Subtraction
    # ------------------------------------------------------------------
    def scene2_repeated_subtraction(self):
        """17 - 5 - 5 - 5 = 2, then count full groups of dots."""
        self.add_subcaption(
            "Multiplication was repeated addition, so you can probably "
            "guess what division is: repeated subtraction. Take "
            "seventeen and keep subtracting five. Seventeen minus five "
            "is twelve. Twelve minus five is seven. Seven minus five "
            "is two. Now we're stuck, because two is smaller than five "
            "and we can't subtract another full group. We subtracted "
            "three times, so the answer is three groups of five, with "
            "two left over. In symbols, seventeen equals three times "
            "five plus two.",
            duration=36,
        )
        self.ly.section_divider(1, "Division as Repeated Subtraction")
        title = self.ly.title("Keep Subtracting")

        chain = VGroup(
            MathTex(r"17 - 5 = 12", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"12 - 5 = 7", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"7 - 5 = 2", font_size=HEADING_SIZE, color=PRIMARY),
        ).arrange(DOWN, buff=0.3)
        self.ly.center_in_content(chain)
        for step in chain:
            self.play(Write(step), run_time=NORMAL)
            self.wait(2.5)
        self.play(FadeOut(chain), run_time=FAST)

        result = self.ly.formula_box(
            MathTex(r"17 = 3 \cdot 5 + 2", font_size=HEADING_SIZE, color=ACCENT)
        )
        self.ly.safe_place(result, direction=DOWN, anchor=title, buff=0.9)
        self.play(Write(result), run_time=SLOW)
        self.wait(9)
        self.ly.clear()

        # Block 2: counting full groups (22s)
        self.add_subcaption(
            "Here is the same answer as a picture: three complete "
            "groups of five dots, plus two extras. The quotient three "
            "simply counts the complete groups. The remainder two "
            "counts what could not fill another group. Quotient is "
            "full groups; remainder is leftovers. Keep those two jobs "
            "separate and division always makes sense.",
            duration=22,
        )
        title2 = self.ly.title("Counting Full Groups")
        dot_rows = VGroup()
        for _ in range(3):
            row = VGroup(*[
                Dot(radius=0.09, color=SECONDARY) for _ in range(5)
            ]).arrange(RIGHT, buff=0.18)
            dot_rows.add(row)
        dot_rows.add(VGroup(
            Dot(radius=0.09, color=ACCENT),
            Dot(radius=0.09, color=ACCENT),
        ).arrange(RIGHT, buff=0.18))
        dot_rows.arrange(DOWN, buff=0.3)
        self.ly.safe_place(dot_rows, direction=DOWN, anchor=title2, buff=1.0)
        dot_formula = MathTex(
            r"3 \cdot 5 + 2 = 17", font_size=HEADING_SIZE, color=ACCENT,
        ).next_to(dot_rows, RIGHT, buff=0.8)
        clamp_position(dot_formula)
        self.play(FadeIn(dot_rows, lag_ratio=0.15), run_time=SLOW)
        self.play(Write(dot_formula), run_time=NORMAL)
        # pacing fix t_ca7fa7ff: caption 3 slot 12.4s vs 20.4s TTS -> +11s
        self.wait(19)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Division on the Number Line
    # ------------------------------------------------------------------
    def scene3_number_line(self):
        """Jump left by 5 until you can't: 17 -> 12 -> 7 -> 2."""
        self.add_subcaption(
            "Here is the same idea on the number line. Start at "
            "seventeen and jump left by five, again and again. One "
            "jump lands on twelve. A second lands on seven. A third "
            "lands on two. A fourth jump would need five more steps, "
            "but only two remain, so it would fall off the line. The "
            "number of jumps is the quotient; the spot where you get "
            "stuck is the remainder.",
            duration=32,
        )
        self.ly.section_divider(2, "Division on the Number Line")
        title = self.ly.title("Jump Until You Can't")

        numberline = NumberLine(
            x_range=[0, 18, 1],
            length=11.4,
            include_numbers=True,
            font_size=24,
            color=PRIMARY,
        )
        self.ly.center_in_content(numberline)
        numberline.shift(DOWN * 0.5)

        start_dot = Dot(numberline.number_to_point(17), radius=0.09, color=ACCENT)
        start_lab = MathTex("17", font_size=LABEL_SIZE, color=ACCENT)
        start_lab.next_to(start_dot, UR, buff=0.12)
        self.play(FadeIn(numberline), run_time=NORMAL)
        self.play(FadeIn(start_dot, scale=2.0), Write(start_lab), run_time=FAST)
        self.wait(3)

        jumps = []
        for frm, to, height in [(17, 12, 0.4), (12, 7, 0.75), (7, 2, 1.1)]:
            p0 = numberline.number_to_point(frm) + UP * height
            p1 = numberline.number_to_point(to) + UP * height
            arrow = Arrow(p0, p1, color=SECONDARY, stroke_width=3,
                          buff=0, tip_length=0.18)
            lab = MathTex("-5", font_size=LABEL_SIZE, color=SECONDARY)
            lab.next_to(arrow, UP, buff=0.1)
            jumps.append(VGroup(arrow, lab))
        for jump in jumps:
            self.play(GrowArrow(jump[0]), FadeIn(jump[1]), run_time=NORMAL)
            self.wait(2.5)

        end_dot = Dot(numberline.number_to_point(2), radius=0.09, color=SECONDARY)
        end_lab = MathTex("2", font_size=LABEL_SIZE, color=SECONDARY)
        end_lab.next_to(end_dot, UP, buff=0.15)
        result = MathTex(r"17 = 3 \cdot 5 + 2",
                         font_size=HEADING_SIZE, color=WHITE)
        self.ly.safe_place(result, direction=DOWN, anchor=numberline, buff=0.55)
        self.play(FadeIn(end_dot, scale=2.0), Write(end_lab), run_time=FAST)
        self.play(Write(result), run_time=NORMAL)
        self.wait(6)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Quotient and Remainder -- naming the pieces
    # ------------------------------------------------------------------
    def scene4_quotient_remainder(self):
        """Name dividend, divisor, quotient, remainder; then notations."""
        self.add_subcaption(
            "These numbers all have names. Seventeen is the dividend, "
            "the amount being divided. Five is the divisor, the size "
            "of each group. Three is the quotient, the number of "
            "complete groups. Two is the remainder, the amount left "
            "over. A quick check: three times five plus two gives "
            "back seventeen. Different books write this differently: "
            "school notation says seventeen divided by five is three "
            "remainder two, and programmers write seventeen slash "
            "slash five for the quotient and seventeen percent five "
            "for the remainder.",
            duration=36,
        )
        self.ly.section_divider(3, "Quotient and Remainder")
        title = self.ly.title("Naming the Pieces")

        eq = MathTex("17", "=", "3", r"\cdot", "5", "+", "2",
                     font_size=HEADING_SIZE)
        eq[0].set_color(WHITE)
        eq[2].set_color(PRIMARY)
        eq[4].set_color(SECONDARY)
        eq[6].set_color(ACCENT)
        self.ly.safe_place(eq, direction=DOWN, anchor=title, buff=1.1)

        dividend = Text("dividend", font_size=SMALL_SIZE, color=WHITE, font=SANS)
        dividend.next_to(eq[0], UP, buff=0.28)
        divisor = Text("divisor", font_size=SMALL_SIZE, color=SECONDARY, font=SANS)
        divisor.next_to(eq[4], UP, buff=0.28)
        quotient = Text("quotient", font_size=SMALL_SIZE, color=PRIMARY, font=SANS)
        quotient.next_to(eq[2], DOWN, buff=0.32)
        remainder = Text("remainder", font_size=SMALL_SIZE, color=ACCENT, font=SANS)
        remainder.next_to(eq[6], DOWN, buff=0.85)
        for m in (dividend, divisor, quotient, remainder):
            clamp_position(m)

        self.play(Write(eq), run_time=NORMAL)
        self.play(
            FadeIn(dividend, shift=DOWN * 0.15),
            FadeIn(divisor, shift=DOWN * 0.15),
            run_time=NORMAL,
        )
        self.play(
            FadeIn(quotient, shift=UP * 0.15),
            FadeIn(remainder, shift=UP * 0.15),
            run_time=NORMAL,
        )
        self.wait(4)
        self.play(
            FadeOut(eq), FadeOut(dividend), FadeOut(divisor),
            FadeOut(quotient), FadeOut(remainder),
            run_time=FAST,
        )

        notations = [
            MathTex(r"17 \div 5 = 3 \text{ R } 2",
                    font_size=BODY_SIZE, color=WHITE),
            Text("17 // 5 = 3", font_size=BODY_SIZE, color=PRIMARY, font=MONO),
            Text("17 % 5 = 2", font_size=BODY_SIZE, color=ACCENT, font=MONO),
        ]
        stack, overflow = self.ly.stack_down(notations, start_from=title, spacing=0.55)
        for item in stack:
            self.play(Write(item), run_time=NORMAL)
            self.wait(2.5)
        # pacing fix t_ca7fa7ff: caption 5 slot 26.4s vs 34.2s TTS -> +2.7s
        self.wait(5.7)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: The Division Algorithm
    # ------------------------------------------------------------------
    def scene5_division_algorithm(self):
        """a = qb + r, 0 <= r < b, and (q, r) is unique."""
        self.add_subcaption(
            "We can now state one of the foundational theorems of "
            "arithmetic: the division algorithm. For every natural "
            "number a and every positive divisor b, there exist "
            "unique whole numbers q and r satisfying a equals q times "
            "b plus r, with r between zero and b minus one. The "
            "quotient q counts how many complete groups of size b fit "
            "inside a. The remainder r is whatever cannot fill "
            "another group. And the word unique is doing real work "
            "here: exactly one pair q, r exists. Division never has "
            "two different answers.",
            duration=40,
        )
        self.ly.section_divider(4, "The Division Algorithm")
        title = self.ly.title("One Theorem, One Answer")

        g = self.ly.formula_box(
            MathTex(r"a = qb + r,\qquad 0 \le r < b",
                    font_size=HEADING_SIZE, color=WHITE)
        )
        self.ly.safe_place(g, direction=DOWN, anchor=title, buff=0.9)
        self.play(Write(g), run_time=SLOW)
        self.wait(3)

        bullets = [
            Text("q counts the full groups of size b inside a",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("r is the leftover: 0 <= r < b",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("q and r are unique \u2014 exactly one pair works",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(bullets, start_from=g)
        # pacing fix t_ca7fa7ff: caption 6 slot 21.0s vs 34.8s TTS -> +19s
        self.wait(27)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Worked Examples
    # ------------------------------------------------------------------
    def scene6_worked_examples(self):
        """Read off q and r for 29/7, 100/7, 53/6; then q as a search."""
        self.add_subcaption(
            "Let's practice. Twenty-nine divided by seven: four sevens "
            "is twenty-eight, so the quotient is four and the remainder "
            "is one. One hundred divided by seven: fourteen sevens is "
            "ninety-eight, so fourteen groups fit, leaving two. "
            "Fifty-three divided by six: eight sixes is forty-eight, "
            "leaving five. In each case the same job: find the largest "
            "multiple of the divisor that still fits, and whatever is "
            "left is the remainder.",
            duration=30,
        )
        self.ly.section_divider(5, "Worked Examples")
        title = self.ly.title("Reading Off q and r")
        examples = [
            MathTex(r"29 = 4 \cdot 7 + 1", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"100 = 14 \cdot 7 + 2", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"53 = 8 \cdot 6 + 5", font_size=BODY_SIZE, color=WHITE),
        ]
        self.ly.progressive_reveal(examples, start_from=title)
        # pacing fix t_ca7fa7ff: caption 7 slot 14.0s vs 29.3s TTS -> +26.5s
        self.wait(32.5)
        self.ly.clear()

        # Block 2: finding q is a search (18s)
        self.add_subcaption(
            "Finding the quotient is a small search. Multiply the "
            "divisor up: seven, fourteen, twenty-one, twenty-eight. "
            "Twenty-eight fits inside twenty-nine, but thirty-five "
            "overshoots. So four is the quotient. Your multiplication "
            "tables are a search index for division.",
            duration=18,
        )
        title2 = self.ly.title("Finding q Is a Search")
        search = self.ly.formula_box(
            MathTex(r"7 \cdot 4 = 28 \le 29 < 7 \cdot 5 = 35",
                    font_size=HEADING_SIZE, color=ACCENT)
        )
        self.ly.safe_place(search, direction=DOWN, anchor=title2, buff=1.2)
        self.play(Write(search), run_time=SLOW)
        # pacing fix t_ca7fa7ff: caption 8 slot 11.2s vs 18.0s TTS -> +9s
        self.wait(17)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Why the Remainder Is Smaller
    # ------------------------------------------------------------------
    def scene7_why_remainder_smaller(self):
        """Bar picture: qb plus r; if r >= b another group still fits."""
        self.add_subcaption(
            "Why must the remainder be strictly smaller than the "
            "divisor? Suppose someone claims that twenty-nine divided "
            "by seven gives three, remainder eight. Eight is larger "
            "than seven, which means one more complete group still "
            "fits inside the leftover. Regrouping, three sevens plus "
            "an eight becomes four sevens plus a one. Every time a "
            "leftover reaches the size of the divisor, we promote it "
            "to a full group and increase the quotient by one. "
            "Requiring r less than b is exactly what makes the "
            "quotient as large as possible, and what pins down the "
            "unique answer.",
            duration=40,
        )
        self.ly.section_divider(6, "Why the Remainder Is Smaller")
        title = self.ly.title("One More Group Must Not Fit")

        def labeled_bar(width, color, label):
            rect = Rectangle(width=width, height=0.9, stroke_color=color,
                             fill_color=color, fill_opacity=0.35)
            lab = MathTex(label, font_size=BODY_SIZE, color=color)
            lab.move_to(rect)
            return VGroup(rect, lab)

        b_bars = VGroup(*[
            labeled_bar(2.4, SECONDARY, "b") for _ in range(3)
        ])
        r_bar = labeled_bar(0.9, ACCENT, "r")
        bars = VGroup(*b_bars, r_bar).arrange(RIGHT, buff=0.08)
        self.ly.safe_place(bars, direction=DOWN, anchor=title, buff=1.3)

        brace_qb = Brace(VGroup(*b_bars), UP, color=SECONDARY)
        qb_label = MathTex(r"qb", font_size=BODY_SIZE, color=SECONDARY)
        qb_label.next_to(brace_qb, UP, buff=0.12)
        brace_r = Brace(r_bar, DOWN, color=ACCENT)
        r_label = MathTex(r"r < b", font_size=BODY_SIZE, color=ACCENT)
        r_label.next_to(brace_r, DOWN, buff=0.12)

        self.play(FadeIn(bars, lag_ratio=0.15), run_time=SLOW)
        self.play(
            GrowFromCenter(brace_qb), Write(qb_label),
            GrowFromCenter(brace_r), Write(r_label),
            run_time=NORMAL,
        )
        self.wait(3)

        bullets = [
            MathTex(r"29 = 3 \cdot 7 + 8", font_size=BODY_SIZE, color=RED),
            Text("8 >= 7, so one more full group still fits",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"29 = 4 \cdot 7 + 1", font_size=BODY_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(bullets, start_from=VGroup(brace_r, r_label))
        # pacing fix t_ca7fa7ff: caption 9 slot 20.2s vs 35.3s TTS -> +22.5s
        self.wait(28.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Long Division (735 / 6)
    # ------------------------------------------------------------------
    def scene8_long_division(self):
        """Staged long-division tableau: 735 = 6 * 122 + 3."""
        self.add_subcaption(
            "For bigger numbers, subtracting one group at a time is "
            "painfully slow. Long division speeds this up by "
            "subtracting in large chunks, working one digit at a time "
            "from the left. Take seven hundred thirty-five divided by "
            "six. Look at the leading digit first. Six goes into seven "
            "one time. Write a one in the quotient on top. Multiply "
            "one times six, which is six, write it under the seven, "
            "and subtract: seven minus six leaves one.",
            duration=34,
        )
        self.ly.section_divider(7, "Long Division")
        title = self.ly.title("Long Division, Step by Step")

        digits = MathTex("7", "3", "5", font_size=40)
        digits.arrange(RIGHT, buff=0.55)
        digits.move_to(RIGHT * 1.2 + UP * 1.3)
        divisor = MathTex("6", font_size=40).next_to(digits, LEFT, buff=0.55)

        ytop = digits.get_top()[1] + 0.25
        vx = digits.get_left()[0] - 0.3
        vline = Line((vx, ytop, 0), (vx, -1.9, 0), color=WHITE, stroke_width=2)
        hbar = Line((vx, ytop, 0),
                    (digits.get_right()[0] + 0.3, ytop, 0),
                    color=WHITE, stroke_width=2)
        tableau = VGroup(digits, divisor, vline, hbar)
        self.play(FadeIn(tableau, lag_ratio=0.1), run_time=NORMAL)
        self.wait(3.5)

        xc7 = digits[0].get_center()[0]
        xc3 = digits[1].get_center()[0]
        xc5 = digits[2].get_center()[0]
        qy = digits.get_top()[1] + 0.7

        # Step 1: 6 into 7 goes 1 time; 1*6 = 6; 7 - 6 = 1
        q1 = MathTex("1", font_size=40, color=WHITE).move_to((xc7, qy, 0))
        p1 = MathTex("6", font_size=40, color=PRIMARY).move_to((xc7, 0.55, 0))
        m1 = MathTex("-", font_size=40, color=PRIMARY).next_to(p1, LEFT, buff=0.12)
        r1 = MathTex("1", font_size=40, color=WHITE).move_to((xc7, 0.0, 0))
        self.play(Write(q1), run_time=FAST)
        self.play(Write(p1), FadeIn(m1), run_time=FAST)
        self.play(Write(r1), run_time=FAST)
        self.wait(3)

        # Bring down the 3
        bd3 = MathTex("3", font_size=40, color=WHITE).move_to((xc3, 0.0, 0))
        self.play(TransformFromCopy(digits[1], bd3), run_time=NORMAL)
        # pacing fix t_ca7fa7ff: caption 10 slot 20.8s vs 28.8s TTS -> +6.5s
        self.wait(9)

        # Step 2: 6 into 13 goes 2 times; 2*6 = 12; 13 - 12 = 1
        q2 = MathTex("2", font_size=40, color=WHITE).move_to((xc3, qy, 0))
        p2 = MathTex("12", font_size=40, color=PRIMARY).move_to(
            ((xc7 + xc3) / 2, -0.55, 0))
        m2 = MathTex("-", font_size=40, color=PRIMARY).next_to(p2, LEFT, buff=0.12)
        r2 = MathTex("1", font_size=40, color=WHITE).move_to((xc3, -1.1, 0))
        self.play(Write(q2), run_time=FAST)
        self.play(Write(p2), FadeIn(m2), run_time=FAST)
        self.play(Write(r2), run_time=FAST)
        self.wait(2.5)

        # Block 2: bring down 5, step 3, remainder, check (40s)
        self.add_subcaption(
            "Now bring down the three, making thirteen. Six goes into "
            "thirteen two times. Write a two on top. Two sixes are "
            "twelve; subtract thirteen minus twelve, leaving one. "
            "Bring down the five, making fifteen. Six goes into fifteen "
            "two times. Two sixes are twelve; subtract and three "
            "remains. No more digits to bring down, so three is the "
            "remainder. In symbols, seven hundred thirty-five equals "
            "six times one hundred twenty-two plus three. Check: six "
            "times one twenty-two is seven hundred thirty-two, and "
            "three more makes seven hundred thirty-five.",
            duration=40,
        )

        # Bring down the 5
        bd5 = MathTex("5", font_size=40, color=WHITE).move_to((xc5, -1.1, 0))
        self.play(TransformFromCopy(digits[2], bd5), run_time=NORMAL)
        self.wait(2.5)

        # Step 3: 6 into 15 goes 2 times; 2*6 = 12
        q3 = MathTex("2", font_size=40, color=WHITE).move_to((xc5, qy, 0))
        p3 = MathTex("12", font_size=40, color=PRIMARY).move_to(
            ((xc3 + xc5) / 2, -1.65, 0))
        m3 = MathTex("-", font_size=40, color=PRIMARY).next_to(p3, LEFT, buff=0.12)
        self.play(Write(q3), run_time=FAST)
        self.play(Write(p3), FadeIn(m3), run_time=FAST)
        self.wait(3)

        # Remainder 3, highlighted
        r3 = MathTex("3", font_size=40, color=ACCENT).move_to((xc5, -2.2, 0))
        r3_box = SurroundingRectangle(r3, color=ACCENT, buff=0.12)
        self.play(Write(r3), Create(r3_box), run_time=NORMAL)
        self.wait(3)

        # Check line
        final = MathTex(r"735 = 6 \cdot 122 + 3",
                        font_size=HEADING_SIZE, color=ACCENT)
        final.move_to((0, -3.05, 0))
        clamp_position(final)
        self.play(Write(final), run_time=NORMAL)
        # pacing fix t_ca7fa7ff: caption 11 slot 17.8s vs 37.7s TTS -> +35s
        self.wait(39)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: When the Remainder Is Zero
    # ------------------------------------------------------------------
    def scene9_remainder_zero(self):
        """Divisibility, even/odd, clocks; then remainder cycles."""
        self.add_subcaption(
            "Sometimes the remainder is zero. Twenty cookies among "
            "five friends: everyone gets exactly four and the plate is "
            "empty. We say five divides twenty evenly, written with a "
            "small vertical bar. This one idea sorts every whole "
            "number into bins. Divided by two with remainder zero "
            "means even. Remainder one means odd. And a clock is a "
            "remainder machine: fourteen o'clock is two in the "
            "afternoon, because fourteen divided by twelve leaves "
            "remainder two.",
            duration=34,
        )
        self.ly.section_divider(8, "When the Remainder Is Zero")
        title = self.ly.title("Divisible")

        eq = MathTex(r"20 = 5 \cdot 4 + 0", font_size=HEADING_SIZE, color=WHITE)
        self.ly.safe_place(eq, direction=DOWN, anchor=title, buff=0.9)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(3)

        div_symbol = MathTex(r"4 \mid 20", font_size=HEADING_SIZE, color=ACCENT)
        div_symbol.move_to(eq)
        divides_lab = Text("b divides a", font_size=SMALL_SIZE, color=DIM, font=SANS)
        divides_lab.next_to(div_symbol, DOWN, buff=0.3)
        self.play(
            Transform(eq, div_symbol),
            FadeIn(divides_lab, shift=UP * 0.15),
            run_time=NORMAL,
        )
        self.wait(3)

        bullets = [
            Text("Even numbers: remainder 0 on division by 2",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Odd numbers: remainder 1 on division by 2",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Clocks are remainder machines: 14 o'clock = 2 pm (mod 12)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(bullets, start_from=VGroup(eq, divides_lab))
        # pacing fix t_ca7fa7ff: caption 12 slot 22.4s vs 30.1s TTS -> +4.5s
        self.wait(10.5)
        self.ly.clear()

        # Block 2: remainders repeat (20s)
        self.add_subcaption(
            "Remainders also fall into cycles. Divide zero through "
            "eight by three and the remainders read zero, one, two, "
            "zero, one, two, over and over. Everything beyond just "
            "repeats the pattern. These cycles are the seed of "
            "modular arithmetic, an entire branch of mathematics "
            "built on nothing but remainders.",
            duration=20,
        )
        title2 = self.ly.title("Remainders Repeat")
        cycle = MathTex(r"0,\ 1,\ 2,\ 0,\ 1,\ 2,\ 0,\ 1,\ 2",
                        font_size=HEADING_SIZE, color=PRIMARY)
        self.ly.center_in_content(cycle)
        note = Text("remainders of 0..8 divided by 3",
                    font_size=BODY_SIZE, color=DIM, font=SANS)
        self.ly.safe_place(note, direction=DOWN, anchor=cycle, buff=0.7)
        self.play(Write(cycle), run_time=SLOW)
        self.play(FadeIn(note, shift=UP * 0.15), run_time=NORMAL)
        # pacing fix t_ca7fa7ff: caption 13 slot 10.4s vs 22.5s TTS -> +21.5s
        self.wait(27.5)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Summary
    # ------------------------------------------------------------------
    def scene10_summary(self):
        """Recap: quotient, remainder, algorithm, long division, divisibility."""
        self.add_subcaption(
            "Let's pull everything together. Division is repeated "
            "subtraction: the quotient counts how many complete groups "
            "of the divisor fit, and the remainder is what cannot fill "
            "another group. The division algorithm guarantees the "
            "decomposition a equals q times b plus r, with r at least "
            "zero and strictly less than b, and it guarantees this "
            "pair is unique. Long division organizes the same idea "
            "into fast chunks for big numbers. When the remainder hits "
            "zero, the divisor divides evenly, and that idea will "
            "power our videos on primes and greatest common divisors. "
            "Next time we cross below zero into the negative numbers. "
            "See you there.",
            duration=46,
        )
        self.ly.section_divider(9, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Division is repeated subtraction \u2014 q counts full groups",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Division algorithm: a = qb + r with 0 <= r < b",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("q and r are unique \u2014 exactly one decomposition",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Long division: repeated subtraction in big chunks",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("r = 0 means b divides a exactly",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        # pacing fix t_ca7fa7ff: caption 14 slot capped by video end -> +1s
        self.wait(15)
        self.ly.clear()
        play_outro(self, next_video="Negative Numbers & Integers",
                   next_playlist="Numbers & Arithmetic")
