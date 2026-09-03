"""
Video 271: Negative Numbers -- Numbers & Arithmetic (L1 Foundations, Video 6/14)

Why numbers below zero are needed (debts, temperatures), the number
line extended left of zero, the integers, ordering and absolute value,
signed addition as walking the line, subtraction as adding the
opposite, sign rules for multiplication, and a full proof that minus
times minus is plus via the distributive law. Connects back to
Video 270 (Division and Remainders) and forward to Video 272 (Fractions).

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


class Video271_NegativeNumbers(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_why_below_zero()
        self.scene3_extending_the_line()
        self.scene4_ordering()
        self.scene5_signed_addition()
        self.scene6_subtraction()
        self.scene7_multiplying_signs()
        self.scene8_minus_times_minus()
        self.scene9_in_the_wild()
        self.scene10_summary()

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _make_line(self, xmin, xmax, length):
        """Styled number line consistent across scenes."""
        return NumberLine(
            x_range=[xmin, xmax, 1],
            length=length,
            color=PRIMARY,
            include_numbers=True,
            font_size=LABEL_SIZE,
        )

    def _walk_arrow(self, line, a, b, color, below=True):
        """Arrow showing a walk from a to b, offset off the line."""
        offset = DOWN * 0.45 if below else UP * 0.45
        return Arrow(
            line.n2p(a) + offset, line.n2p(b) + offset,
            buff=0.12, color=color, stroke_width=3.5,
            max_tip_length_to_length_ratio=0.18,
        )

    # ------------------------------------------------------------------
    # Scene 1: Hook - less than nothing
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: counting numbers cannot answer 5 - 8."""
        self.add_subcaption(
            "Last time, division left us owing apples. If you must "
            "repay eight apples but only have five, then five take "
            "away eight has no answer among the counting numbers. "
            "Unless numbers can dip below zero. Winter mornings do "
            "it daily: the thermometer reads five degrees, then "
            "falls eight more. Debts do it too: five dollars in "
            "your pocket, eight dollars owed. Mathematics needs a "
            "name for less than nothing. Today we extend the number "
            "line to the left, meet the integers, and discover that "
            "arithmetic keeps working, with a few beautiful "
            "surprises along the way.",
            duration=42,
        )
        play_intro(self, "Negative Numbers", "Numbers & Arithmetic")

        title = self.ly.title("Less Than Nothing?")
        items = [
            MathTex(r"5 - 8 = \, ?", font_size=BODY_SIZE, color=ACCENT),
            Text("Five dollars in your pocket, eight dollars owed",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("The thermometer falls eight degrees below zero",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(8)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Why we need numbers below zero
    # ------------------------------------------------------------------
    def scene2_why_below_zero(self):
        """Two everyday pictures: temperature and debt."""
        self.add_subcaption(
            "Why do we need numbers below zero? Two everyday "
            "pictures force the issue. First, temperature. Zero "
            "degrees is not the coldest it can get: on a bitter "
            "morning the mercury sits three notches below zero, "
            "and below needs a symbol, so we write minus three. "
            "Second, money. You hold five dollars but owe a friend "
            "eight. Your net worth is five take away eight: three "
            "dollars below zero, written minus three. In both "
            "pictures the minus sign means the same thing: a "
            "distance below a natural starting point. Owning and "
            "owing, warm and cold, above and below: opposites, "
            "measured from zero.",
            duration=48,
        )
        self.ly.section_divider(1, "Why Below Zero?")
        title = self.ly.title("Two Everyday Pictures")

        left_items = [
            Text("Temperature", font_size=BODY_SIZE, color=PRIMARY,
                 font=SANS, weight=BOLD),
            MathTex(r"5^\circ \text{ above zero}", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"-3^\circ \text{ below zero}", font_size=BODY_SIZE, color=RED),
        ]
        right_items = [
            Text("Money", font_size=BODY_SIZE, color=SECONDARY,
                 font=SANS, weight=BOLD),
            MathTex(r"5 \text{ dollars earned}", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"-8 \text{ dollars owed}", font_size=BODY_SIZE, color=RED),
        ]
        left, right = self.ly.two_columns(left_items, right_items, start_from=title)
        self.play(FadeIn(left, lag_ratio=0.2), run_time=NORMAL)
        self.play(FadeIn(right, lag_ratio=0.2), run_time=NORMAL)
        self.wait(9)

        key = Text("A minus sign marks distance below the starting point",
                   font_size=BODY_SIZE, color=ACCENT, font=SANS)
        self.ly.safe_place(key, direction=DOWN, anchor=left, buff=0.5)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(9)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: The number line, extended left
    # ------------------------------------------------------------------
    def scene3_extending_the_line(self):
        """Mirror the counting numbers to the left of zero."""
        self.add_subcaption(
            "Here is the number line we know so far: zero, one, "
            "two, three, four, five, marching forever to the "
            "right. To extend it, stand at zero and reflect: the "
            "same spacings, the same rhythm, but to the left. One "
            "step left of zero is minus one. Two steps is minus "
            "two. Every counting number gets a mirror twin, "
            "exactly as far from zero but on the other side. The "
            "counting numbers, their mirror twins, and zero in "
            "the middle are called the integers. The line no "
            "longer begins anywhere: it stretches equally in both "
            "directions, and zero is no longer the edge of the "
            "world, just the center of the map.",
            duration=52,
        )
        self.ly.section_divider(2, "Extending the Line")
        title = self.ly.title("Every Number Gets a Mirror Twin")

        full = self._make_line(-5, 5, 11)
        self.ly.center_in_content(full)
        half = self._make_line(0, 5, 5.5)
        half.shift(full.n2p(0) - half.n2p(0))

        self.play(Create(half), run_time=SLOW)
        self.wait(4)

        zone_r = Text("counting numbers", font_size=LABEL_SIZE,
                      color=DIM, font=SANS)
        zone_r.move_to(half.n2p(2.5) + UP * 0.75)
        self.play(FadeIn(zone_r, shift=UP * 0.15), run_time=FAST)
        self.wait(3)

        self.play(Create(full), FadeOut(half), run_time=SLOW)
        zone_l = Text("their mirror twins", font_size=LABEL_SIZE,
                      color=DIM, font=SANS)
        zone_l.move_to(full.n2p(-2.5) + UP * 0.75)
        self.play(FadeIn(zone_l, shift=UP * 0.15), run_time=FAST)

        integers = MathTex(
            r"\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(integers, direction=DOWN, anchor=full, buff=0.8)
        self.play(Write(integers), run_time=NORMAL)
        self.wait(12)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Ordering and absolute value
    # ------------------------------------------------------------------
    def scene4_ordering(self):
        """Left means smaller; absolute value means distance."""
        self.add_subcaption(
            "Which is bigger, minus two or minus five? Careful: "
            "intuition says five. But on the line, ordering means "
            "position, not the size of the numeral. Numbers grow "
            "to the right and shrink to the left. Minus five sits "
            "further left than minus two, so minus five is the "
            "smaller number. If temperatures, minus five degrees "
            "is colder than minus two degrees: smaller, and in "
            "winter, more dangerous. To talk about how far a "
            "number sits from zero, without caring which side, we "
            "use absolute value, written with two vertical bars. "
            "The absolute value of minus five is five, because "
            "minus five sits five steps from zero. Absolute value "
            "measures distance, and distance is never negative.",
            duration=52,
        )
        self.ly.section_divider(3, "Ordering")
        title = self.ly.title("Left Means Smaller")

        line = self._make_line(-6, 6, 10)
        self.ly.center_in_content(line)
        self.play(Create(line), run_time=SLOW)

        d_shallow = Dot(line.n2p(-2), color=SECONDARY, radius=0.1)
        lbl_shallow = MathTex(r"-2", font_size=BODY_SIZE, color=SECONDARY)
        lbl_shallow.next_to(d_shallow, UP, buff=0.25)
        d_deep = Dot(line.n2p(-5), color=RED, radius=0.1)
        lbl_deep = MathTex(r"-5", font_size=BODY_SIZE, color=RED)
        lbl_deep.next_to(d_deep, UP, buff=0.25)
        self.play(
            FadeIn(d_shallow), FadeIn(lbl_shallow, shift=UP * 0.1),
            FadeIn(d_deep), FadeIn(lbl_deep, shift=UP * 0.1),
            run_time=NORMAL,
        )

        ineq = MathTex(r"-5 < -2", font_size=HEADING_SIZE, color=ACCENT)
        self.ly.safe_place(ineq, direction=DOWN, anchor=line, buff=0.7)
        self.play(Write(ineq), run_time=NORMAL)
        self.wait(10)

        compare_group = VGroup(d_shallow, lbl_shallow, d_deep, lbl_deep, ineq)
        self.play(FadeOut(compare_group), run_time=FAST)

        # Absolute value: brace above the line (number labels own the space below)
        brace = Brace(
            Line(line.n2p(-5), line.n2p(0)),
            UP, color=DIM, buff=0.15,
        )
        brace_lbl = MathTex(r"5 \text{ steps}", font_size=LABEL_SIZE, color=DIM)
        brace_lbl.next_to(brace, UP, buff=0.15)
        abs_val = MathTex(r"|-5| = 5", font_size=HEADING_SIZE, color=WHITE)
        abs_val.next_to(line, DOWN, buff=1.1)
        self.play(GrowFromCenter(brace), run_time=NORMAL)
        self.play(Write(brace_lbl), run_time=FAST)
        self.play(Write(abs_val), run_time=NORMAL)
        self.wait(12)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Signed addition as walking the line
    # ------------------------------------------------------------------
    def scene5_signed_addition(self):
        """Addition = walking; positive right, negative left."""
        self.add_subcaption(
            "Now arithmetic. Addition is walking on the line: "
            "positive numbers walk right, negative numbers walk "
            "left. Watch three plus minus five. Start at three, "
            "then walk five steps left: you land on minus two. "
            "The signs disagree, so we subtract the magnitudes, "
            "five minus three, and keep the sign of the bigger "
            "walk: minus. Now both walkers head left: minus two "
            "plus minus six. Start at minus two, walk six more "
            "steps left, and land on minus eight. Same signs: add "
            "the magnitudes and keep the sign. So the complete "
            "rule: same signs, add and keep the common sign. "
            "Different signs, subtract the smaller magnitude from "
            "the larger and keep the sign of the larger. The "
            "number line turns every signed addition into a "
            "simple walk.",
            duration=58,
        )
        self.ly.section_divider(4, "Adding Signed Numbers")
        title = self.ly.title("Addition = Walking the Line")

        line = self._make_line(-8, 8, 12)
        self.ly.center_in_content(line)
        self.play(Create(line), run_time=SLOW)

        # Beat A: 3 + (-5)
        dot_a = Dot(line.n2p(3), color=ACCENT, radius=0.1)
        arrow_a = self._walk_arrow(line, 3, -2, RED)
        eq_a = MathTex(r"3 + (-5) = -2", font_size=HEADING_SIZE, color=ACCENT)
        eq_a.next_to(line, DOWN, buff=1.1)
        self.play(FadeIn(dot_a, scale=0.5), run_time=FAST)
        self.play(GrowArrow(arrow_a), run_time=NORMAL)
        self.play(Write(eq_a), run_time=NORMAL)
        self.wait(10)

        beat_a = VGroup(dot_a, arrow_a, eq_a)
        self.play(FadeOut(beat_a), run_time=FAST)

        # Beat B: (-2) + (-6)
        dot_b = Dot(line.n2p(-2), color=ACCENT, radius=0.1)
        arrow_b = self._walk_arrow(line, -2, -8, RED)
        eq_b = MathTex(r"(-2) + (-6) = -8", font_size=HEADING_SIZE, color=ACCENT)
        eq_b.next_to(line, DOWN, buff=1.1)
        self.play(FadeIn(dot_b, scale=0.5), run_time=FAST)
        self.play(GrowArrow(arrow_b), run_time=NORMAL)
        self.play(Write(eq_b), run_time=NORMAL)
        self.wait(8)

        self.play(FadeOut(VGroup(dot_b, arrow_b, eq_b)), run_time=FAST)

        # Rules
        rules = [
            Text("Same signs: add the magnitudes, keep the sign",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Different signs: subtract, keep the sign of the larger",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(rules, start_from=line, spacing=0.5)
        self.wait(8)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Subtraction = adding the opposite
    # ------------------------------------------------------------------
    def scene6_subtraction(self):
        """Subtracting b = adding -b; double reversal for -(-x)."""
        self.add_subcaption(
            "Subtraction hides a shortcut. Three take away five "
            "is a walk: start at three, move five steps left, "
            "land on minus two. But walking five steps left is "
            "exactly what the number minus five does. Subtracting "
            "five and adding minus five land on the same spot: "
            "they are the same move. So every subtraction can be "
            "rewritten as adding the opposite: three minus five "
            "equals three plus minus five. The rule never fails, "
            "even twice in a row. What is five minus minus two? "
            "Subtracting minus two means adding plus two, so five "
            "plus two is seven. Subtracting a negative is a "
            "double reversal: a leftward number, walked "
            "rightward. Two wrongs, beautifully, make a right.",
            duration=52,
        )
        self.ly.section_divider(5, "Subtraction")
        title = self.ly.title("Subtracting = Adding the Opposite")

        identity = MathTex(
            r"a - b = a + (-b)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(identity, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(identity), run_time=NORMAL)
        self.wait(6)
        self.play(FadeOut(identity), run_time=FAST)

        line = self._make_line(-7, 7, 11)
        self.ly.center_in_content(line)
        self.play(Create(line), run_time=SLOW)

        # Beat A: 3 - 5
        dot_a = Dot(line.n2p(3), color=ACCENT, radius=0.1)
        arrow_a = self._walk_arrow(line, 3, -2, RED)
        eq_a = MathTex(r"3 - 5 = 3 + (-5) = -2",
                       font_size=BODY_SIZE, color=WHITE)
        eq_a.next_to(arrow_a, DOWN, buff=0.35)
        self.play(FadeIn(dot_a, scale=0.5), run_time=FAST)
        self.play(GrowArrow(arrow_a), run_time=NORMAL)
        self.play(Write(eq_a), run_time=NORMAL)
        self.wait(8)
        self.play(FadeOut(VGroup(dot_a, arrow_a, eq_a)), run_time=FAST)

        # Beat B: 5 - (-2)
        dot_b = Dot(line.n2p(5), color=ACCENT, radius=0.1)
        arrow_b = self._walk_arrow(line, 5, 7, SECONDARY)
        eq_b = MathTex(r"5 - (-2) = 5 + 2 = 7",
                       font_size=BODY_SIZE, color=ACCENT)
        eq_b.next_to(arrow_b, DOWN, buff=0.35)
        self.play(FadeIn(dot_b, scale=0.5), run_time=FAST)
        self.play(GrowArrow(arrow_b), run_time=NORMAL)
        self.play(Write(eq_b), run_time=NORMAL)
        self.wait(9)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Multiplying signed numbers
    # ------------------------------------------------------------------
    def scene7_multiplying_signs(self):
        """3 x (-2) as repeated jumps; countdown pattern reveals (-1)(-2)=+2."""
        self.add_subcaption(
            "Multiplication was repeated addition, so let us "
            "repeat. Three times minus two means three groups of "
            "minus two: starting from zero, jump left two, again, "
            "and again. We land on minus six. Negative times "
            "positive gives negative: the sign of the group wins. "
            "Now a pattern that unlocks everything. Watch the "
            "products as the first factor counts down: three "
            "times minus two is minus six. Two times minus two is "
            "minus four. One times minus two is minus two. Zero "
            "times minus two is zero. Each product grows by "
            "exactly two, marching steadily up the line. So what "
            "must come next? Minus one times minus two has to be "
            "plus two.",
            duration=52,
        )
        self.ly.section_divider(6, "Multiplying Signs")
        title = self.ly.title("Three Groups of Minus Two")

        line = self._make_line(-7, 7, 12)
        self.ly.center_in_content(line)
        self.play(Create(line), run_time=SLOW)

        jumps = VGroup(
            self._walk_arrow(line, 0, -2, RED),
            self._walk_arrow(line, -2, -4, RED),
            self._walk_arrow(line, -4, -6, RED),
        )
        eq = MathTex(r"3 \times (-2) = -6",
                     font_size=HEADING_SIZE, color=ACCENT)
        eq.next_to(jumps, DOWN, buff=0.3)
        dot_end = Dot(line.n2p(-6), color=RED, radius=0.11)

        self.play(GrowArrow(jumps[0]), run_time=NORMAL)
        self.play(GrowArrow(jumps[1]), run_time=NORMAL)
        self.play(GrowArrow(jumps[2]), FadeIn(dot_end, scale=0.5),
                  run_time=NORMAL)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(8)
        self.ly.clear()

        # Countdown pattern
        title2 = self.ly.title("Count Down the Products")
        rows = [
            MathTex(r"3 \times (-2) = -6", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"2 \times (-2) = -4", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"1 \times (-2) = -2", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"0 \times (-2) = \ 0", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"(-1) \times (-2) = +2", font_size=HEADING_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(rows, start_from=title2, spacing=0.35)
        self.wait(12)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Why minus times minus is plus
    # ------------------------------------------------------------------
    def scene8_minus_times_minus(self):
        """The distributive-law proof in four lines."""
        self.add_subcaption(
            "The pattern suggests it, but mathematics demands a "
            "proof, and the distributive law delivers it in four "
            "lines. We know that minus one times any number flips "
            "that number's sign. Now compute minus one times the "
            "quantity minus one plus one. The parentheses sum to "
            "zero, so the whole product is zero. But we can also "
            "distribute: minus one times minus one, plus minus "
            "one times one. The second term is minus one, so "
            "minus one times minus one, plus minus one, equals "
            "zero. Something plus minus one equals zero only if "
            "that something is plus one. Therefore minus one "
            "times minus one equals plus one: proved, not "
            "guessed. Every sign combination now obeys one table: "
            "plus times plus is plus, plus times minus and minus "
            "times plus are minus, and minus times minus is "
            "plus.",
            duration=60,
        )
        self.ly.section_divider(7, "Minus Times Minus")
        title = self.ly.title("Proof from the Distributive Law")

        given = MathTex(
            r"(-1) \times x = -x \quad \text{for any } x",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(given, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(given), run_time=NORMAL)
        self.wait(6)

        steps = [
            MathTex(r"(-1) \times \bigl((-1) + 1\bigr) = 0",
                    font_size=BODY_SIZE, color=WHITE),
            MathTex(r"(-1)(-1) + (-1)(1) = 0", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"(-1)(-1) + (-1) = 0", font_size=BODY_SIZE, color=WHITE),
            MathTex(r"\therefore \ (-1) \times (-1) = +1",
                    font_size=HEADING_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(steps, start_from=given, spacing=0.35)
        self.wait(14)
        self.ly.clear()

        fb = self.ly.formula_box(
            MathTex(r"(-) \times (-) = +", font_size=HEADING_SIZE, color=ACCENT)
        )
        self.play(Write(fb[0]), run_time=NORMAL)
        self.play(Create(fb[1]), run_time=FAST)
        note = Text("Positive when signs match, negative when they differ",
                    font_size=BODY_SIZE, color=DIM, font=SANS)
        self.ly.safe_place(note, direction=DOWN, anchor=fb, buff=0.45)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(8)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Negative numbers in the wild
    # ------------------------------------------------------------------
    def scene9_in_the_wild(self):
        """Temperature and debt worked examples."""
        self.add_subcaption(
            "Let us use it in the wild. Temperature: dawn sits at "
            "minus seven degrees, and the afternoon warms by "
            "twelve. Minus seven plus twelve: different signs, "
            "subtract the magnitudes, twelve minus seven, keep "
            "the sign of the larger: plus. Five degrees by "
            "lunchtime. Money: your balance is minus twenty "
            "dollars, and you deposit thirty-five. Minus twenty "
            "plus thirty-five: subtract, keep the positive: "
            "fifteen dollars, out of debt. Same mechanics every "
            "time: walk, or add the opposite. Elevators below "
            "ground, golf under par, years before year one: "
            "civilization writes below as a minus sign, and the "
            "arithmetic you now own handles all of it.",
            duration=52,
        )
        self.ly.section_divider(8, "In the Wild")
        title = self.ly.title("Two Quick Calculations")
        rows = [
            Text("Dawn: -7 degrees, afternoon warms by 12",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            MathTex(r"-7 + 12 = +5", font_size=HEADING_SIZE, color=ACCENT),
            Text("Balance: -20 dollars, deposit 35 dollars",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            MathTex(r"-20 + 35 = +15", font_size=HEADING_SIZE, color=ACCENT),
            Text("Below ground, under par, before year one: all negatives",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(rows, start_from=title, spacing=0.35)
        self.wait(10)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Summary
    # ------------------------------------------------------------------
    def scene10_summary(self):
        """Recap negatives; tease fractions."""
        self.add_subcaption(
            "Let us recap. The number line extends left of zero: "
            "every counting number has a mirror twin, and "
            "together they form the integers. Ordering follows "
            "position: further left is smaller, so minus five is "
            "less than minus two, and absolute value measures "
            "pure distance from zero. Addition is walking: same "
            "signs add, different signs subtract, keeping the "
            "sign of the larger. Subtraction is adding the "
            "opposite, so minus a negative is a plus. And "
            "multiplication completes the picture: the product is "
            "positive when the signs match and negative when they "
            "differ, with minus times minus is plus proved by the "
            "distributive law. Next time, living between the "
            "integers: the fractions, numbers that measure parts, "
            "ratios, and everything in between. See you then.",
            duration=55,
        )
        self.ly.section_divider(9, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("The line extends left of zero: meet the integers",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Left is smaller: -5 < -2;  |x| = distance from zero",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Addition is walking: same signs add, different signs subtract",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Subtraction = adding the opposite",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Minus times minus is plus (proved!) -- and signs matching = positive",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(16)
        self.ly.clear()
        play_outro(self, next_video="Fractions", next_playlist="Numbers & Arithmetic")
