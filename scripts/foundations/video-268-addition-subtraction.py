"""
Video 268: Addition and Subtraction -- Numbers & Arithmetic (L1 Foundations, Video 3/14)

Addition as counting on, subtraction as the inverse operation, number line
visualization, and the key properties: commutativity and associativity.
Connects back to Video 267 (Natural Numbers).

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


class Video268_AdditionSubtraction(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_addition_as_counting_on()
        self.scene3_number_line_addition()
        self.scene4_commutativity()
        self.scene5_associativity()
        self.scene6_subtraction_as_inverse()
        self.scene7_number_line_subtraction()
        self.scene8_subtraction_limitations()
        self.scene9_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: a simple question about combining groups."""
        self.add_subcaption(
            "Last time we built the natural numbers from nothing: zero, one, "
            "two, three, and upward forever using the successor function. "
            "Now we have numbers. But what can we do with them? Here is the "
            "most natural question. If you have three apples and someone "
            "gives you five more, how many do you have? You know the answer "
            "is eight. But what does that mean mathematically? That is addition.",
            duration=36,
        )
        play_intro(self, "Addition and Subtraction", "Numbers & Arithmetic")

        title = self.ly.title("What Can We Do With Numbers?")
        items = [
            Text("3 apples + 5 more apples = 8 apples",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("You already know this intuitively",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("But what is really happening mathematically?",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(14)  # pacing: seg0 TTS 22.7s needs slot >= 25s (was 8)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Addition as Counting On
    # ------------------------------------------------------------------
    def scene2_addition_as_counting_on(self):
        """Define addition via the successor function."""
        self.add_subcaption(
            "We defined natural numbers using the successor function, so we "
            "should define addition the same way. To add one to any number n, "
            "just take its successor. So n plus one equals S of n. To add two, "
            "take the successor twice: n plus two equals S of S of n. In general, "
            "adding m means applying the successor function m times. This is "
            "called counting on. You start at n and count up m steps.",
            duration=42,
        )
        self.ly.section_divider(1, "Addition as Counting On")
        title = self.ly.title("Repeated Successor")

        formula_1 = MathTex(
            r"n + 1 = S(n)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(formula_1, DOWN, anchor=title, buff=0.5)
        self.play(Write(formula_1), run_time=SLOW)
        self.wait(FAST)

        formula_2 = MathTex(
            r"n + 2 = S(S(n))",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(formula_2, DOWN, anchor=formula_1, buff=0.4)
        self.play(Write(formula_2), run_time=SLOW)
        self.wait(FAST)

        formula_3 = MathTex(
            r"n + m = \underbrace{S(S(\cdots S}_{m \text{ times}}(n)\cdots))",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(formula_3, DOWN, anchor=formula_2, buff=0.4)
        self.play(Write(formula_3), run_time=SLOW)
        self.wait(20)  # pacing: seg1 TTS 27.8s needs slot >= 31s (was 8; flagged 1.7x)
        self.ly.clear()

        # Concrete example
        self.add_subcaption(
            "Let us try a concrete example. Three plus two. Starting from "
            "three, we apply the successor function twice. The successor of three "
            "is four. The successor of four is five. So three plus two equals "
            "five. That is all addition is: repeated counting on.",
            duration=26,
        )
        title2 = self.ly.title("Example: 3 + 2")
        steps = [
            MathTex(r"3 + 2", font_size=HEADING_SIZE, color=WHITE),
            MathTex(r"= S(S(3))", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"= S(4) = 5", font_size=HEADING_SIZE, color=SECONDARY),
        ]
        for i, step in enumerate(steps):
            if i == 0:
                self.ly.safe_place(step, DOWN, anchor=title2, buff=0.5)
            else:
                self.ly.safe_place(step, DOWN, anchor=steps[i - 1], buff=0.3)
            self.play(Write(step), run_time=NORMAL)
            self.wait(FAST)
        self.wait(13)  # pacing: seg2 TTS 17.5s needs slot >= 19.3s (was 10)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Number Line Addition
    # ------------------------------------------------------------------
    def scene3_number_line_addition(self):
        """Visualize addition as rightward jumps on the number line."""
        self.add_subcaption(
            "The number line gives us a beautiful picture of addition. "
            "To add, start at the first number and move right by the second "
            "number. Four plus three means start at four and take three steps "
            "to the right. You land on seven. The plus sign means: move right. "
            "This picture will become even more powerful when we introduce "
            "negative numbers later in this playlist.",
            duration=36,
        )
        self.ly.section_divider(2, "Number Line Addition")
        title = self.ly.title("Addition = Move Right")

        line = NumberLine(
            x_range=[0, 10, 1],
            length=10,
            color=PRIMARY,
            include_numbers=True,
            font_size=LABEL_SIZE,
        )
        self.ly.center_in_content(line)
        line.shift(DOWN * 0.5)
        self.play(Create(line), run_time=SLOW)
        self.wait(FAST)

        start_dot = Dot(line.n2p(4), color=ACCENT, radius=0.1)
        start_label = MathTex("4", font_size=BODY_SIZE, color=ACCENT)
        start_label.next_to(start_dot, UP, buff=0.3)
        self.play(
            FadeIn(start_dot),
            FadeIn(start_label, shift=UP * 0.1),
            run_time=NORMAL,
        )
        self.wait(FAST)

        arrow = Arrow(
            line.n2p(4), line.n2p(7),
            buff=0.15, color=SECONDARY, stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )
        arrow_label = MathTex("+3", font_size=BODY_SIZE, color=SECONDARY)
        arrow_label.next_to(arrow, UP, buff=0.15)
        self.play(
            GrowArrow(arrow),
            FadeIn(arrow_label, shift=UP * 0.1),
            run_time=NORMAL,
        )
        self.wait(FAST)

        end_dot = Dot(line.n2p(7), color=RED, radius=0.1)
        end_label = MathTex("7", font_size=BODY_SIZE, color=RED)
        end_label.next_to(end_dot, UP, buff=0.3)
        result_eq = MathTex(
            r"4 + 3 = 7", font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(result_eq, DOWN, anchor=line, buff=0.6)
        self.play(
            FadeIn(end_dot),
            FadeIn(end_label, shift=UP * 0.1),
            Write(result_eq),
            run_time=NORMAL,
        )
        self.wait(14)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Commutativity
    # ------------------------------------------------------------------
    def scene4_commutativity(self):
        """Commutativity: a + b = b + a with visual proof."""
        self.add_subcaption(
            "Here is a property you have probably never questioned. Three plus "
            "five equals eight, and five plus three also equals eight. The order "
            "does not matter. This is called commutativity. In symbols, a plus "
            "b equals b plus a for all natural numbers a and b. On the number "
            "line, starting at three and moving right five steps lands at eight. "
            "Starting at five and moving right three steps also lands at eight.",
            duration=40,
        )
        self.ly.section_divider(3, "Commutativity")
        title = self.ly.title("Order Does Not Matter")

        formula = MathTex(
            r"a + b = b + a", font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(formula, DOWN, anchor=title, buff=0.5)
        self.play(Write(formula), run_time=SLOW)
        self.wait(FAST)

        items = [
            Text("3 + 5 = 8   and   5 + 3 = 8",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Same destination, different starting points",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Holds for ALL natural numbers",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=formula)
        self.wait(18)  # pacing: seg4 TTS 25.6s needs slot >= 28.2s (was 10)
        self.ly.clear()

        # Visual proof with two rows of dots
        self.add_subcaption(
            "Here is a visual proof using dots. Three dots, then five dots. "
            "That is three plus five. Now flip the order: five dots, then "
            "three dots. Both rows have eight dots total. The total does not "
            "change when you swap the groups. This is commutativity.",
            duration=28,
        )
        title2 = self.ly.title("Visual Proof")

        row1_label = Text("3 + 5:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        row1_dots = VGroup(
            *[Dot(radius=0.1, color=PRIMARY) for _ in range(3)]
            + [Dot(radius=0.1, color=SECONDARY) for _ in range(5)]
        ).arrange(RIGHT, buff=0.25)
        row1 = VGroup(row1_label, row1_dots).arrange(RIGHT, buff=0.3)

        row2_label = Text("5 + 3:", font_size=BODY_SIZE, color=WHITE, font=SANS)
        row2_dots = VGroup(
            *[Dot(radius=0.1, color=SECONDARY) for _ in range(5)]
            + [Dot(radius=0.1, color=PRIMARY) for _ in range(3)]
        ).arrange(RIGHT, buff=0.25)
        row2 = VGroup(row2_label, row2_dots).arrange(RIGHT, buff=0.3)

        both = VGroup(row1, row2).arrange(DOWN, buff=0.6)
        self.ly.safe_place(both, DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(row1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(FAST)
        self.play(FadeIn(row2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        eq = Text(
            "= 8 dots both ways",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(eq, DOWN, anchor=both, buff=0.5)
        self.play(FadeIn(eq, shift=LEFT * 0.1), run_time=NORMAL)
        self.wait(10)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Associativity
    # ------------------------------------------------------------------
    def scene5_associativity(self):
        """Associativity: (a + b) + c = a + (b + c)."""
        self.add_subcaption(
            "When you add three or more numbers, how you group them does not "
            "matter either. Take two plus three plus four. Compute the parentheses "
            "first way: two plus three is five, plus four is nine. Second way: "
            "three plus four is seven, two plus seven is nine. Same answer. This "
            "is called associativity, and it means we never need parentheses "
            "when writing a sum of many numbers.",
            duration=38,
        )
        self.ly.section_divider(4, "Associativity")
        title = self.ly.title("Grouping Does Not Matter")

        formula = MathTex(
            r"(a + b) + c = a + (b + c)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(formula, DOWN, anchor=title, buff=0.5)
        self.play(Write(formula), run_time=SLOW)
        self.wait(FAST)

        items = [
            Text("(2 + 3) + 4 = 5 + 4 = 9",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2 + (3 + 4) = 2 + 7 = 9",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("No parentheses needed for sums of many numbers",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=formula)
        self.wait(18)  # pacing: seg6 TTS 25.4s needs slot >= 28s (was 14)
        self.ly.clear()

        # Identity element
        self.add_subcaption(
            "There is one more property worth noting. Adding zero to any number "
            "leaves it unchanged. Five plus zero equals five. Zero is called the "
            "additive identity. Together with commutativity and associativity, "
            "these three properties define what mathematicians call a commutative "
            "monoid. The natural numbers under addition form one.",
            duration=36,
        )
        title2 = self.ly.title("The Additive Identity")
        items2 = [
            Text("5 + 0 = 5   and   0 + 5 = 5",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Adding zero changes nothing",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("0 is the additive identity",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("(N, +) is a commutative monoid",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(17)  # pacing: seg7 TTS 21.0s needs slot >= 23s (was 14)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Subtraction as Inverse
    # ------------------------------------------------------------------
    def scene6_subtraction_as_inverse(self):
        """Define subtraction as the inverse of addition."""
        self.add_subcaption(
            "Now for subtraction. If addition combines two groups, subtraction "
            "undoes that. Seven minus three asks: what number, when added to "
            "three, gives seven? The answer is four. Subtraction is defined as "
            "the inverse of addition. In symbols, a minus b equals c precisely "
            "when c plus b equals a. Subtraction asks the question that addition "
            "answers.",
            duration=38,
        )
        self.ly.section_divider(5, "Subtraction as Inverse")
        title = self.ly.title("Undoing Addition")

        formula = MathTex(
            r"a - b = c \iff c + b = a",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(formula, DOWN, anchor=title, buff=0.5)
        self.play(Write(formula), run_time=SLOW)
        self.wait(FAST)

        items = [
            Text("7 - 3 = 4  because  4 + 3 = 7",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Subtraction = reverse question of addition",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("If you combined groups, subtraction splits them",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=formula)
        self.wait(17)  # pacing: seg8 TTS 25.0s needs slot >= 27.5s (was 12)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Number Line Subtraction
    # ------------------------------------------------------------------
    def scene7_number_line_subtraction(self):
        """Visualize subtraction as leftward jumps on the number line."""
        self.add_subcaption(
            "On the number line, addition moves right. So subtraction moves left. "
            "Seven minus three means start at seven and move left three steps. "
            "You land on four. This mirrors addition perfectly. Right is plus, "
            "left is minus. Once we add negative numbers, this picture becomes "
            "even cleaner. Subtraction will literally become adding a negative.",
            duration=34,
        )
        self.ly.section_divider(6, "Number Line Subtraction")
        title = self.ly.title("Subtraction = Move Left")

        line = NumberLine(
            x_range=[0, 10, 1],
            length=10,
            color=PRIMARY,
            include_numbers=True,
            font_size=LABEL_SIZE,
        )
        self.ly.center_in_content(line)
        line.shift(DOWN * 0.5)
        self.play(Create(line), run_time=SLOW)
        self.wait(FAST)

        start_dot = Dot(line.n2p(7), color=ACCENT, radius=0.1)
        start_label = MathTex("7", font_size=BODY_SIZE, color=ACCENT)
        start_label.next_to(start_dot, UP, buff=0.3)
        self.play(
            FadeIn(start_dot),
            FadeIn(start_label, shift=UP * 0.1),
            run_time=NORMAL,
        )
        self.wait(FAST)

        arrow = Arrow(
            line.n2p(7), line.n2p(4),
            buff=0.15, color=RED, stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )
        arrow_label = MathTex("-3", font_size=BODY_SIZE, color=RED)
        arrow_label.next_to(arrow, UP, buff=0.15)
        self.play(
            GrowArrow(arrow),
            FadeIn(arrow_label, shift=UP * 0.1),
            run_time=NORMAL,
        )
        self.wait(FAST)

        end_dot = Dot(line.n2p(4), color=SECONDARY, radius=0.1)
        end_label = MathTex("4", font_size=BODY_SIZE, color=SECONDARY)
        end_label.next_to(end_dot, UP, buff=0.3)
        result_eq = MathTex(
            r"7 - 3 = 4", font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(result_eq, DOWN, anchor=line, buff=0.6)
        self.play(
            FadeIn(end_dot),
            FadeIn(end_label, shift=UP * 0.1),
            Write(result_eq),
            run_time=NORMAL,
        )
        self.wait(14)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Subtraction Limitations
    # ------------------------------------------------------------------
    def scene8_subtraction_limitations(self):
        """Subtraction is not always possible in N."""
        self.add_subcaption(
            "But there is a problem. Three minus five. What natural number, "
            "when added to five, gives three? The answer is: there is not one. "
            "Subtraction is not always possible within the natural numbers. "
            "This is a genuine limitation. In the natural numbers, we can only "
            "subtract when the first number is at least as large as the second. "
            "To fix this, we need to expand our number system. That is exactly "
            "what we will do when we introduce the integers and negative numbers.",
            duration=44,
        )
        self.ly.section_divider(7, "A Problem")
        title = self.ly.title("Subtraction Is Not Always Possible")

        problem = MathTex(
            r"3 - 5 = \,?\,", font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(problem, DOWN, anchor=title, buff=0.5)
        self.play(Write(problem), run_time=SLOW)
        self.wait(FAST)

        items = [
            Text("No natural number c satisfies c + 5 = 3",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Subtraction only works when a >= b in N",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("This gap motivates negative numbers -- the integers Z",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=problem)
        self.wait(22)  # pacing: seg10 TTS 29.3s needs slot >= 32.2s (was 16; bullet-merge content unchanged)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Summary
    # ------------------------------------------------------------------
    def scene9_summary(self):
        """Key takeaways and outro."""
        self.add_subcaption(
            "Let us recap. Addition is repeated application of the successor "
            "function, also called counting on. On the number line, addition "
            "moves right and subtraction moves left. Addition is commutative "
            "and associative, and zero is the additive identity. Subtraction is "
            "the inverse of addition, but it is not always possible in the "
            "natural numbers. That limitation leads us to the next topic: "
            "negative numbers and the integers. See you there.",
            duration=42,
        )
        self.ly.section_divider(8, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Addition = repeated successor (counting on)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Number line: + moves right, - moves left",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Commutative: a + b = b + a",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Associative: (a + b) + c = a + (b + c)",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Subtraction inverts addition, but not always in N",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(16)
        self.ly.clear()
        play_outro(self, next_video="Negative Numbers & Integers", next_playlist="Numbers & Arithmetic")
