"""
Video 269: Multiplication -- Numbers & Arithmetic (L1 Foundations, Video 4/14)

Multiplication as repeated addition, built from the successor function.
Equal jumps on the number line, commutativity (rotation proof),
associativity, the area model, and distributivity as the bridge to algebra.
Connects back to Video 268 (Addition and Subtraction) and forward to
Division and Remainders.

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


class Video269_Multiplication(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_repeated_addition()
        self.scene3_number_line()
        self.scene4_commutativity()
        self.scene5_associativity()
        self.scene6_area_model()
        self.scene7_distributivity()
        self.scene8_identity_zero_teaser()
        self.scene9_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: equal groups everywhere, but repeated addition gets tiresome."""
        self.add_subcaption(
            "Welcome back to the playlist. Last time we built addition and "
            "subtraction: combining groups, counting on, and moving along the "
            "number line. Today we meet the operation that makes arithmetic "
            "truly powerful. Picture three bags of apples, each bag holding "
            "five apples. You could write five plus five plus five, and that "
            "works. But imagine two hundred bags. Nobody wants to write two "
            "hundred fives. We need a faster idea. That idea is multiplication.",
            duration=32,
        )
        play_intro(self, "Multiplication", "Numbers & Arithmetic")

        title = self.ly.title("The Next Operation")
        items = [
            Text("Three bags of five apples each",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5 + 5 + 5 works. But 200 bags?",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Time for a faster idea",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(14)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Multiplication as Repeated Addition
    # ------------------------------------------------------------------
    def scene2_repeated_addition(self):
        """Define multiplication via repeated addition and the successor."""
        self.add_subcaption(
            "Multiplication is repeated addition. The expression m times n "
            "means: take the number m and add it to itself n times. Just like "
            "addition, we can define this precisely with the successor "
            "function from Video 267. Start with the empty case: m times zero "
            "is zero, because zero copies of m contain nothing. Then the "
            "step: m times the successor of n equals m times n, plus one more "
            "copy of m. Every successor adds exactly one more copy. "
            "Multiplication is built from addition and successors alone.",
            duration=38,
        )
        self.ly.section_divider(1, "Multiplication as Repeated Addition")
        title = self.ly.title("Multiplication = Repeated Addition")

        formula_general = MathTex(
            r"m \times n = \underbrace{m + m + \cdots + m}_{n \text{ copies}}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(formula_general, DOWN, anchor=title, buff=0.5)
        self.play(Write(formula_general), run_time=SLOW)
        self.wait(FAST)

        formula_zero = MathTex(
            r"m \times 0 = 0",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(formula_zero, DOWN, anchor=formula_general, buff=0.4)
        self.play(Write(formula_zero), run_time=NORMAL)
        self.wait(FAST)

        formula_step = MathTex(
            r"m \times S(n) = (m \times n) + m",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(formula_step, DOWN, anchor=formula_zero, buff=0.4)
        self.play(Write(formula_step), run_time=NORMAL)
        self.wait(22)
        self.ly.clear()

        # Concrete example
        self.add_subcaption(
            "Try it with real numbers. Three times four means four copies of "
            "three. Three plus three is six. Six plus three is nine. Nine "
            "plus three is twelve. Four copies of three give twelve, so "
            "three times four equals twelve. Fast counting of equal groups: "
            "that is all multiplication is.",
            duration=22,
        )
        title2 = self.ly.title("Four Copies of Three")
        steps = [
            MathTex(r"3 \times 4", font_size=HEADING_SIZE, color=WHITE),
            MathTex(r"= 3 + 3 + 3 + 3", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"= 12", font_size=HEADING_SIZE, color=SECONDARY),
        ]
        for i, step in enumerate(steps):
            if i == 0:
                self.ly.safe_place(step, DOWN, anchor=title2, buff=0.5)
            else:
                self.ly.safe_place(step, DOWN, anchor=steps[i - 1], buff=0.3)
            self.play(Write(step), run_time=NORMAL)
            self.wait(FAST)
        self.wait(10)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Number Line -- Equal Jumps
    # ------------------------------------------------------------------
    def scene3_number_line(self):
        """Visualize multiplication as equal jumps from zero."""
        self.add_subcaption(
            "The number line turns multiplication into equal jumps. Addition "
            "could take steps of any size, but multiplication always takes "
            "jumps of the same length. Three times four: start at zero and "
            "make three jumps, each four units long. Zero to four. Four to "
            "eight. Eight to twelve. You land on twelve, exactly as the "
            "repeated addition promised. This picture explains why "
            "multiplication grows so much faster: three jumps cover twelve "
            "units, while three single steps barely leave the start.",
            duration=34,
        )
        self.ly.section_divider(2, "Multiplication on the Number Line")
        title = self.ly.title("Equal Jumps")

        line = NumberLine(
            x_range=[0, 13, 1],
            length=10,
            color=PRIMARY,
            include_numbers=True,
            font_size=LABEL_SIZE,
        )
        self.ly.center_in_content(line)
        line.shift(DOWN * 0.5)
        self.play(Create(line), run_time=SLOW)
        self.wait(FAST)

        start_dot = Dot(line.n2p(0), color=ACCENT, radius=0.1)
        self.play(FadeIn(start_dot), run_time=NORMAL)
        self.wait(FAST)

        jumps = [
            VGroup(
                CurvedArrow(line.n2p(0), line.n2p(4), angle=0.45,
                            color=SECONDARY, stroke_width=3.5),
            ),
            VGroup(
                CurvedArrow(line.n2p(4), line.n2p(8), angle=0.45,
                            color=SECONDARY, stroke_width=3.5),
                MathTex("+4", font_size=BODY_SIZE, color=SECONDARY)
                .next_to(line.n2p(6), UP, buff=1.0),
            ),
            VGroup(
                CurvedArrow(line.n2p(8), line.n2p(12), angle=0.45,
                            color=SECONDARY, stroke_width=3.5),
            ),
        ]
        for jump in jumps:
            self.play(FadeIn(jump, shift=UP * 0.1), run_time=NORMAL)
            self.wait(FAST)

        result_eq = MathTex(
            r"3 \times 4 = 12", font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(result_eq, DOWN, anchor=line, buff=0.6)
        self.play(Write(result_eq), run_time=NORMAL)
        self.wait(12)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Commutativity
    # ------------------------------------------------------------------
    def scene4_commutativity(self):
        """Commutativity: a x b = b x a, with a one-rotation visual proof."""
        self.add_subcaption(
            "Now a property so familiar that nobody questions it. Three times "
            "five is fifteen, and five times three is also fifteen. The order "
            "never matters. This is commutativity. In symbols, a times b "
            "always equals b times a, for every pair of natural numbers. "
            "Addition had this property, and multiplication has it too. But "
            "why? A formula alone is not an explanation. For that, we need a "
            "picture.",
            duration=30,
        )
        self.ly.section_divider(3, "Commutativity")
        title = self.ly.title("Order Does Not Matter")

        formula = MathTex(
            r"a \times b = b \times a", font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(formula, DOWN, anchor=title, buff=0.5)
        self.play(Write(formula), run_time=SLOW)
        self.wait(FAST)

        items = [
            MathTex(r"3 \times 5 = 15 \qquad 5 \times 3 = 15",
                    font_size=BODY_SIZE, color=PRIMARY),
            Text("Same answer, any order",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("True for ALL natural numbers",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=formula)
        self.wait(13)
        self.ly.clear()

        # Visual proof: rotate the rectangle of squares
        self.add_subcaption(
            "Here is the picture. Three rows of five squares: fifteen squares "
            "total. Now rotate the whole block by ninety degrees. The very "
            "same squares now form five rows of three. Nothing was added and "
            "nothing was removed, so the count is still fifteen. One rotation "
            "is a complete proof of commutativity: any rectangle of a rows "
            "and b columns is also b rows and a columns.",
            duration=28,
        )
        title2 = self.ly.title("A One-Rotation Proof")

        unit = 0.34
        grid1 = VGroup(*[
            Square(side_length=unit, stroke_color=BG, stroke_width=2,
                   fill_color=SECONDARY, fill_opacity=0.6)
            for _ in range(15)
        ]).arrange_in_grid(rows=3, cols=5, buff=0.04)
        self.ly.safe_place(grid1, DOWN, anchor=title2, buff=0.5)

        eq1 = MathTex(r"3 \times 5 = 15", font_size=HEADING_SIZE, color=PRIMARY)
        self.ly.safe_place(eq1, DOWN, anchor=grid1, buff=0.5)
        self.play(FadeIn(grid1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(FAST)
        self.play(Write(eq1), run_time=NORMAL)
        self.wait(4)

        grid2 = VGroup(*[
            Square(side_length=unit, stroke_color=BG, stroke_width=2,
                   fill_color=SECONDARY, fill_opacity=0.6)
            for _ in range(15)
        ]).arrange_in_grid(rows=5, cols=3, buff=0.04)
        grid2.move_to(grid1)
        eq2 = MathTex(r"5 \times 3 = 15", font_size=HEADING_SIZE, color=ACCENT)
        eq2.move_to(eq1)
        self.play(
            ReplacementTransform(grid1, grid2),
            ReplacementTransform(eq1, eq2),
            run_time=SLOW,
        )
        self.wait(11)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Associativity
    # ------------------------------------------------------------------
    def scene5_associativity(self):
        """Associativity: (a x b) x c = a x (b x c)."""
        self.add_subcaption(
            "Multiplying three numbers raises a new question: does the "
            "grouping matter? Take two, three, and four. Group the first "
            "pair: two times three is six, and six times four is twenty-four. "
            "Group the second pair instead: three times four is twelve, and "
            "two times twelve is twenty-four. The answers match. This is "
            "associativity, the same property addition had. Because grouping "
            "never matters, we can write a times b times c with no "
            "parentheses at all, and everyone agrees what it means.",
            duration=36,
        )
        self.ly.section_divider(4, "Associativity")
        title = self.ly.title("Grouping Does Not Matter")

        formula = MathTex(
            r"(a \times b) \times c = a \times (b \times c)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(formula, DOWN, anchor=title, buff=0.5)
        self.play(Write(formula), run_time=SLOW)
        self.wait(FAST)

        items = [
            MathTex(r"(2 \times 3) \times 4 = 6 \times 4 = 24",
                    font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"2 \times (3 \times 4) = 2 \times 12 = 24",
                    font_size=BODY_SIZE, color=SECONDARY),
            Text("Same answer: grouping never matters",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=formula)
        self.wait(17)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: The Area Model
    # ------------------------------------------------------------------
    def scene6_area_model(self):
        """The area model: a rectangle of unit squares."""
        self.add_subcaption(
            "Time for the most useful picture in all of arithmetic: the area "
            "model. Build a rectangle five units wide and three units tall, "
            "then fill it with unit squares. Each row contains five squares. "
            "There are three rows. Count them: five, ten, fifteen. The number "
            "of squares is exactly five times three. Width times height gives "
            "the area. This innocent-looking rectangle will carry us through "
            "fractions, decimals, algebra, and far beyond. Whenever "
            "multiplication feels abstract, come back and count squares.",
            duration=36,
        )
        self.ly.section_divider(5, "The Area Model")
        title = self.ly.title("Width Times Height")

        grid = VGroup(*[
            Square(side_length=0.5, stroke_color=BG, stroke_width=2,
                   fill_color=SECONDARY, fill_opacity=0.55)
            for _ in range(15)
        ]).arrange_in_grid(rows=3, cols=5, buff=0.03)
        self.ly.safe_place(grid, DOWN, anchor=title, buff=0.6)

        w_label = MathTex("5", font_size=BODY_SIZE, color=WHITE)
        w_label.next_to(grid, DOWN, buff=0.25)
        h_label = MathTex("3", font_size=BODY_SIZE, color=WHITE)
        h_label.next_to(grid, LEFT, buff=0.25)
        self.play(
            FadeIn(grid, shift=LEFT * 0.15),
            FadeIn(w_label),
            FadeIn(h_label),
            run_time=NORMAL,
        )
        self.wait(FAST)

        eq = MathTex(r"5 \times 3 = 15", font_size=HEADING_SIZE, color=ACCENT)
        self.ly.safe_place(eq, DOWN, anchor=grid, buff=0.7)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(22)
        self.ly.clear()

        # Commutativity, for free
        self.add_subcaption(
            "The area model makes commutativity obvious. A five by three "
            "rectangle tipped on its side becomes three by five. Same "
            "rectangle, same squares, same area. No formula required, just "
            "geometry. Watch for this picture again: it returns when we meet "
            "fractions, decimals, and the distributive law, which is coming "
            "up right now.",
            duration=24,
        )
        title2 = self.ly.title("One Rectangle, Two Views")
        items = [
            MathTex(r"5 \times 3 = 15", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"3 \times 5 = 15", font_size=HEADING_SIZE, color=SECONDARY),
            Text("Same rectangle, tipped on its side",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(13)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Distributivity
    # ------------------------------------------------------------------
    def scene7_distributivity(self):
        """Distributivity via splitting the area rectangle."""
        self.add_subcaption(
            "Distributivity is the deepest property, and the area model "
            "proves it in one glance. Compute three times the sum of two and "
            "four. One route: two plus four is six, and three times six is "
            "eighteen. The other route splits the rectangle into two pieces: "
            "a three by two block and a three by four block. Three times two "
            "is six. Three times four is twelve. Six plus twelve is eighteen. "
            "Both routes land on the same number, because they are just two "
            "ways of counting the same squares.",
            duration=38,
        )
        self.ly.section_divider(6, "Distributivity")
        title = self.ly.title("Splitting the Rectangle")

        unit = 0.5
        part1 = VGroup(*[
            Square(side_length=unit, stroke_color=BG, stroke_width=2,
                   fill_color=PRIMARY, fill_opacity=0.55)
            for _ in range(6)
        ]).arrange_in_grid(rows=3, cols=2, buff=0.0)
        part2 = VGroup(*[
            Square(side_length=unit, stroke_color=BG, stroke_width=2,
                   fill_color=SECONDARY, fill_opacity=0.55)
            for _ in range(12)
        ]).arrange_in_grid(rows=3, cols=4, buff=0.0)
        part2.next_to(part1, RIGHT, buff=0.0)
        rectangle = VGroup(part1, part2)
        self.ly.safe_place(rectangle, DOWN, anchor=title, buff=0.6)

        label_two = MathTex("2", font_size=BODY_SIZE, color=PRIMARY)
        label_two.next_to(part1, DOWN, buff=0.2)
        label_four = MathTex("4", font_size=BODY_SIZE, color=SECONDARY)
        label_four.next_to(part2, DOWN, buff=0.2)
        label_three = MathTex("3", font_size=BODY_SIZE, color=WHITE)
        label_three.next_to(rectangle, LEFT, buff=0.3)
        labels = VGroup(label_two, label_four, label_three)

        eq1 = MathTex(
            r"3 \times (2 + 4) = (3 \times 2) + (3 \times 4)",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(eq1, DOWN, anchor=rectangle, buff=0.7)
        self.play(FadeIn(rectangle, shift=LEFT * 0.15), run_time=NORMAL)
        self.play(FadeIn(labels), run_time=NORMAL)
        self.wait(FAST)
        self.play(Write(eq1), run_time=NORMAL)
        self.wait(FAST)

        eq2 = MathTex(
            r"= 6 + 12 = 18", font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(eq2, DOWN, anchor=eq1, buff=0.3)
        self.play(Write(eq2), run_time=NORMAL)
        self.wait(17)
        self.ly.clear()

        # Bridge to algebra
        self.add_subcaption(
            "In symbols, a times the quantity b plus c equals a times b plus "
            "a times c. This is the bridge from arithmetic into algebra. "
            "Every time you expand an expression like three times the "
            "quantity x plus two, you are splitting an invisible rectangle. "
            "Factoring simply runs the movie backwards.",
            duration=22,
        )
        title2 = self.ly.title("The Bridge to Algebra")
        items = [
            MathTex(r"3 \times (x + 2) = 3x + 6",
                    font_size=HEADING_SIZE, color=PRIMARY),
            Text("Expanding = splitting an invisible rectangle",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Factoring = gluing the pieces back",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(12)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Identity, Zero, and What Comes Next
    # ------------------------------------------------------------------
    def scene8_identity_zero_teaser(self):
        """Multiplicative identity, zero, and the division teaser."""
        self.add_subcaption(
            "Two special cases deserve their own moment. First, one times any "
            "number leaves it exactly unchanged: one is called the "
            "multiplicative identity. Second, zero times any number is always "
            "zero: zero copies of anything contain nothing. Addition had its "
            "own identity, zero. Now multiplication has one too: one. "
            "Together, these structures turn the natural numbers into what "
            "mathematicians call a commutative semiring. Do not worry about "
            "the name yet; just notice how each operation brings its own "
            "rules.",
            duration=34,
        )
        self.ly.section_divider(7, "Identity and Zero")
        title = self.ly.title("Two Special Numbers")

        items = [
            MathTex(r"1 \times n = n", font_size=HEADING_SIZE, color=PRIMARY),
            MathTex(r"n \times 0 = 0", font_size=HEADING_SIZE, color=SECONDARY),
            Text("1 is the multiplicative identity",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("0 annihilates every product",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"(\mathbb{N}, +, \times)",
                    font_size=BODY_SIZE, color=DIM),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(18)
        self.ly.clear()

        # Teaser: division and remainders
        self.add_subcaption(
            "Finally, multiplication begs one more question. Does five fit "
            "into twelve? Write twelve as five plus five plus two. Five fits "
            "in twice, with two left over. Sometimes the leftover is zero, "
            "and sometimes, like here, it is not. Handling these leftovers is "
            "the story of division and remainders, and it is exactly where we "
            "go next.",
            duration=26,
        )
        title2 = self.ly.title("A Question to Sit With")

        split = MathTex(
            r"12 = 5 + 5 + 2", font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(split, DOWN, anchor=title2, buff=0.5)
        self.play(Write(split), run_time=SLOW)
        self.wait(FAST)

        items = [
            Text("Five fits into twelve twice",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Two is left over",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Leftovers: the story of division",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=split)
        self.wait(12)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Summary
    # ------------------------------------------------------------------
    def scene9_summary(self):
        """Key takeaways and outro."""
        self.add_subcaption(
            "Let us recap. Multiplication is repeated addition, defined from "
            "nothing but the successor function. On the number line, it is a "
            "series of equal jumps. It is commutative and associative, one is "
            "its identity, and zero annihilates everything. The area model "
            "turns every product into counting squares, and distributivity "
            "splits rectangles into manageable pieces, the very move that "
            "powers algebra. Next time we tackle division and remainders, and "
            "discover why twelve split into fives is more interesting than it "
            "looks. See you there.",
            duration=38,
        )
        self.ly.section_divider(8, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Multiplication = repeated addition (successor-built)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Number line: equal jumps of the same size",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Commutative and associative",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Area model: width times height, counted in squares",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Distributivity splits rectangles: the seed of algebra",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(14)
        self.ly.clear()
        play_outro(self, next_video="Division and Remainders", next_playlist="Numbers & Arithmetic")
