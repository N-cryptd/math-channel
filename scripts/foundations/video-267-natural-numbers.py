"""
Video 267: The Natural Numbers -- Numbers & Arithmetic (L1 Foundations, Video 2/14)

Peano axioms intuition, successor function, counting, ordering,
and why natural numbers are the foundation of all mathematics.
Connects back to Video 266 (What is Mathematics?).

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


class Video267_NaturalNumbers(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_what_are_naturals()
        self.scene3_counting_intuition()
        self.scene4_successor_function()
        self.scene5_peano_axioms_list()
        self.scene6_peano_no_cycles()
        self.scene7_ordering()
        self.scene8_induction_example()
        self.scene9_foundation()
        self.scene10_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook - connect from Video 266
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: counting as the most basic mathematical act."""
        self.add_subcaption(
            "In the last video we saw that mathematics is built on abstraction. "
            "Three apples, three cars, three ideas -- the number three is the "
            "same in every case. But where do these numbers come from in the "
            "first place? They come from the simplest act imaginable: counting. "
            "A child points at objects one by one and says the words. One, two, "
            "three. But behind that simple act hides one of the deepest ideas in "
            "all of mathematics.",
            duration=29,
        )
        play_intro(self, "The Natural Numbers", "Numbers & Arithmetic")

        title = self.ly.title("Where Do Numbers Come From?")
        items = [
            Text("3 apples, 3 cars, 3 ideas  -->  the number 3",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Counting is the most basic mathematical act",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("But what IS a number, really?",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(18)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: What Are Natural Numbers?
    # ------------------------------------------------------------------
    def scene2_what_are_naturals(self):
        """Define the natural numbers and note the two conventions."""
        self.add_subcaption(
            "The natural numbers are the numbers you use for counting. "
            "We write them as N, the set containing zero, one, two, three, "
            "four, and so on forever. Notice the three dots at the end. That "
            "means the pattern continues without bound. The natural numbers "
            "are infinite. There is no largest natural number. No matter how "
            "big a number you name, you can always add one to get a bigger one.",
            duration=26,
        )
        self.ly.section_divider(1, "What Are Natural Numbers?")
        title = self.ly.title("The Counting Numbers")

        nat_set_tex = MathTex(
            r"\mathbb{N} = \{0,\; 1,\; 2,\; 3,\; 4,\; \ldots\}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        nat_box = self.ly.formula_box(nat_set_tex, color=PRIMARY)
        self.ly.safe_place(nat_box, DOWN, anchor=title, buff=0.5)
        self.play(Write(nat_box), run_time=SLOW)
        self.wait(FAST)

        items = [
            Text("The numbers you use for counting",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Infinite: no largest element",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=nat_box)
        self.wait(17)
        self.ly.clear()

        # Two conventions
        self.add_subcaption(
            "There are actually two conventions for the natural numbers. "
            "Some authors define N as starting from zero. Others start from "
            "one. In this series we include zero, for two reasons. First, it "
            "makes the algebraic structure cleaner. Second, it matches how "
            "computers represent numbers. Either convention works fine. "
            "Just be aware that different textbooks may differ.",
            duration=24,
        )
        title2 = self.ly.title("Two Conventions")

        conv_a = MathTex(
            r"\mathbb{N} = \{0, 1, 2, 3, \ldots\}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        conv_a_label = Text(
            "  Convention A (includes 0) -- our choice",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        conv_a_group = VGroup(conv_a, conv_a_label).arrange(RIGHT, buff=0.15)
        self.ly.safe_place(conv_a_group, DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(conv_a_group, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(FAST)

        conv_b = MathTex(
            r"\mathbb{N} = \{1, 2, 3, 4, \ldots\}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        conv_b_label = Text(
            "  Convention B (starts at 1)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        conv_b_group = VGroup(conv_b, conv_b_label).arrange(RIGHT, buff=0.15)
        self.ly.safe_place(conv_b_group, DOWN, anchor=conv_a_group, buff=0.4)
        self.play(FadeIn(conv_b_group, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(20)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Counting Intuition
    # ------------------------------------------------------------------
    def scene3_counting_intuition(self):
        """Visual counting with one-to-one correspondence."""
        self.add_subcaption(
            "Let us think about what counting really means. When you count "
            "a pile of stones, you point at each stone and say the next "
            "number. One, two, three, four, five. This process is called "
            "one-to-one correspondence. Each stone gets exactly one number, "
            "and each number is used at most once. When you run out of "
            "stones, the last number you said is the count. This simple idea "
            "is the foundation of all arithmetic.",
            duration=28,
        )
        self.ly.section_divider(2, "Counting")
        title = self.ly.title("One-to-One Correspondence")

        # Dots representing stones
        stones = VGroup(*[
            Dot(LEFT * 4 + RIGHT * i * 1.2 + DOWN * 0.5, radius=0.12, color=ACCENT)
            for i in range(5)
        ])
        self.ly.safe_place(stones, DOWN, anchor=title, buff=1.6)

        stone_label = Text(
            "Stones", font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        stone_label.next_to(stones, DOWN, buff=0.35)
        self.play(
            FadeIn(stone_label, shift=LEFT * 0.1),
            *[FadeIn(s) for s in stones],
            run_time=NORMAL, lag_ratio=0.1,
        )
        self.wait(FAST)

        # Numbers appearing one by one
        num_labels = VGroup()
        for i in range(5):
            n = MathTex(str(i + 1), font_size=BODY_SIZE, color=PRIMARY)
            n.next_to(stones[i], UP, buff=0.5)
            num_labels.add(n)

        for i in range(5):
            self.play(Write(num_labels[i]), run_time=FAST)
            self.wait(FAST)

        # Arrows connecting
        arrows = VGroup()
        for i in range(5):
            arr = Arrow(
                num_labels[i].get_bottom(),
                stones[i].get_top(),
                buff=0.05, color=SECONDARY, stroke_width=1.5,
                max_tip_length_to_length_ratio=0.2,
            )
            arrows.add(arr)
        self.play(*[FadeIn(a) for a in arrows], run_time=NORMAL)
        self.wait(15)
        self.ly.clear()

        # Key insight
        self.add_subcaption(
            "This is actually a deep idea. Two collections have the same "
            "number of objects precisely when you can pair them up one to one "
            "with nothing left over. This is how we know that five fingers "
            "and five apples have something in common, even though fingers "
            "and apples are completely different things. The number five is "
            "that common property.",
            duration=21,
        )
        title2 = self.ly.title("The Counting Principle")
        items = [
            Text("Each object gets exactly one number",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Each number is used at most once",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("The last number you say IS the count",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("This works for ANY collection of objects",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(15)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: The Successor Function
    # ------------------------------------------------------------------
    def scene4_successor_function(self):
        """Build numbers from nothing using the successor function."""
        self.add_subcaption(
            "How do we actually construct the natural numbers from scratch? "
            "We start with zero. Zero is our starting point, given to us "
            "by definition. Then we define a single operation: the successor "
            "function. The successor of a number n, written S of n, is the "
            "number that comes immediately after n. The successor of zero "
            "is what we call one. The successor of one is two. And so on. "
            "That is all we need. By repeatedly applying the successor "
            "function to zero, we generate every natural number.",
            duration=35,
        )
        self.ly.section_divider(3, "The Successor Function")
        title = self.ly.title("Building Numbers from Nothing")

        # Successor chain visual
        chain = VGroup()
        nums = ["0", "S(0)", "S(S(0))", "S(S(S(0)))"]
        labels = ["=1", "=2", "=3"]
        colors = [WHITE, PRIMARY, SECONDARY, ACCENT]
        for i in range(4):
            num_tex = MathTex(nums[i], font_size=LABEL_SIZE, color=colors[i])
            if i > 0:
                eq_label = MathTex(
                    labels[i - 1], font_size=LABEL_SIZE, color=DIM,
                )
                pair = VGroup(num_tex, eq_label).arrange(RIGHT, buff=0.1)
            else:
                pair = num_tex
            chain.add(pair)
        chain.arrange(RIGHT, buff=0.5)
        self.ly.safe_place(chain, DOWN, anchor=title, buff=1.2)

        # Arrows between items
        arrows = VGroup()
        for i in range(3):
            arrow = MathTex(r"\rightarrow", font_size=LABEL_SIZE, color=PRIMARY)
            arrow.move_to((chain[i].get_right() + chain[i + 1].get_left()) / 2)
            arrows.add(arrow)

        self.play(Write(chain[0]), run_time=NORMAL)
        for i in range(3):
            self.play(
                FadeIn(arrows[i]),
                FadeIn(chain[i + 1], shift=RIGHT * 0.15),
                run_time=NORMAL,
            )
            self.wait(FAST)
        self.wait(24)
        self.ly.clear()

        # Key ideas
        self.add_subcaption(
            "Think of it like a chain of dominoes. Zero is the first domino. "
            "The successor function is the rule that says: for every domino, "
            "there is exactly one domino after it. One is the successor of zero. "
            "Two is the successor of the successor of zero. Three is the successor "
            "of the successor of the successor of zero. And this never stops.",
            duration=23,
        )
        title2 = self.ly.title("A Never-Ending Chain")
        items = [
            Text("0 is the starting point (given by definition)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("S(n) = the number immediately after n",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("1 = S(0),  2 = S(S(0)),  3 = S(S(S(0))),  ...",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("The chain never ends -- no largest number",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(17)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Peano's Five Axioms
    # ------------------------------------------------------------------
    def scene5_peano_axioms_list(self):
        """Present Peano's five axioms."""
        self.add_subcaption(
            "In eighteen eighty nine, the Italian mathematician Giuseppe Peano "
            "wrote down a precise set of rules that completely define the "
            "natural numbers. Just five simple statements, and from them "
            "alone, all of arithmetic follows. These are called the Peano "
            "axioms. Let us go through them. Axiom one: zero is a natural "
            "number. Axiom two: every natural number has a successor that is "
            "also a natural number. Axiom three: zero is not the successor "
            "of any number.",
            duration=33,
        )
        self.ly.section_divider(4, "Peano's Axioms")
        title = self.ly.title("Five Rules Define Everything")

        items_a = [
            Text("P1:  0 is a natural number",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("P2:  Every n in N has successor S(n) in N",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("P3:  0 is not the successor of any number",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items_a, start_from=title)
        self.wait(25)
        self.ly.clear()

        # Axioms 4 and 5
        self.add_subcaption(
            "Axiom four: different numbers have different successors. "
            "In symbols, if S of a equals S of b, then a must equal b. "
            "This means the successor function never collapses two different "
            "numbers into the same next number. Axiom five is the induction "
            "principle: if zero has a property, and if having the property "
            "at any number implies having it at the successor, then every "
            "natural number has that property.",
            duration=28,
        )
        title2 = self.ly.title("Axioms 4 and 5")
        items_b = [
            Text("P4:  If S(a) = S(b) then a = b",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("    (the successor function is injective)",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("P5:  Induction principle",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("    If P(0) and P(n) -> P(S(n)), then P holds for all n",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        visible_b = self.ly.progressive_reveal(items_b, start_from=title2)
        self.wait(10)

        # Highlight P5 formally -- fade the bullet list first so the
        # formula box has the content area to itself (no overlap)
        self.play(*[FadeOut(m) for m in visible_b], run_time=0.5)
        p5_tex = MathTex(
            r"P(0) \wedge \; \forall n\,[P(n) \Rightarrow P(S(n))] \; \Rightarrow \; \forall n\, P(n)",
            font_size=BODY_SIZE, color=RED,
        )
        p5_box = self.ly.formula_box(p5_tex, color=RED)
        self.ly.safe_place(p5_box, DOWN, anchor=title2, buff=0.8)
        self.play(FadeIn(p5_box, shift=UP * 0.15), run_time=NORMAL)
        self.wait(10)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Peano - No Cycles, No Branching
    # ------------------------------------------------------------------
    def scene6_peano_no_cycles(self):
        """Visualize what axioms 3 and 4 guarantee."""
        self.add_subcaption(
            "Axioms three and four together guarantee something important. "
            "The natural numbers form a single, straight, infinite chain. "
            "There are no loops because of axiom three: nothing leads back "
            "to zero. There is no branching because of axiom four: two "
            "different numbers cannot lead to the same successor. And there "
            "are no dead ends because of axiom two: every number has a "
            "successor. The structure is forced. It has to look exactly "
            "like this: zero, one, two, three, and so on forever.",
            duration=34,
        )
        self.ly.section_divider(5, "No Cycles, No Branching")
        title = self.ly.title("The Structure Is Forced")
        items = [
            Text("P3 (0 has no predecessor)  -->  no loops",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("P4 (injective)  -->  no branching or merging",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("P2 (every n has S(n))  -->  no dead ends",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Result: a single infinite straight chain",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(25)
        self.ly.clear()

        # Induction as dominoes
        self.add_subcaption(
            "Axiom five, the induction axiom, is the most powerful. "
            "It says: suppose zero has some property. And suppose that "
            "whenever a number has this property, its successor also has it. "
            "Then axiom five guarantees that every natural number has this "
            "property. Think of a line of dominoes standing on end. If the "
            "first one falls, and each domino knocks over the next, then "
            "they all fall. That is exactly what mathematical induction is.",
            duration=30,
        )
        title2 = self.ly.title("Induction: The Domino Principle")
        items2 = [
            Text("If 0 has property P",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("And: P(n) implies P(S(n)) for all n",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Then: EVERY natural number has property P",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Like dominoes: knock the first, rest follow",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(24)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Ordering
    # ------------------------------------------------------------------
    def scene7_ordering(self):
        """Define ordering on natural numbers."""
        self.add_subcaption(
            "The successor function also gives us the concept of order. "
            "We say a is less than b if you can reach b from a by applying "
            "the successor some number of times. For example, one is less "
            "than three because S of S of one equals three. This definition "
            "gives us a total order on the natural numbers. Any two numbers "
            "can be compared: either they are equal, or one is less than "
            "the other.",
            duration=26,
        )
        self.ly.section_divider(6, "Ordering")
        title = self.ly.title("Less Than, Greater Than")

        # Number line visual
        line = Line(LEFT * 5, RIGHT * 5, color=PRIMARY, stroke_width=2)
        self.ly.safe_place(line, DOWN, anchor=title, buff=1.6)
        self.play(Create(line), run_time=NORMAL)
        self.wait(FAST)

        # Place dots and labels for 0-5
        dots_vg = VGroup()
        num_labels = VGroup()
        for i in range(6):
            pos = line.get_left() + RIGHT * (i * 2)
            dot = Dot(pos, radius=0.06, color=ACCENT)
            label = MathTex(str(i), font_size=BODY_SIZE, color=WHITE)
            label.next_to(dot, DOWN, buff=0.25)
            dots_vg.add(dot)
            num_labels.add(label)
        self.play(
            *[FadeIn(d) for d in dots_vg],
            *[FadeIn(l) for l in num_labels],
            run_time=NORMAL, lag_ratio=0.15,
        )
        self.wait(FAST)

        # Highlight 1 < 3
        red_dots = VGroup()
        for i in (1, 3):
            pos = line.get_left() + RIGHT * (i * 2)
            red_dots.add(Dot(pos, radius=0.08, color=RED))
        lt_label = Text(
            "1 < 3", font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        lt_label.next_to(line, UP, buff=0.4)
        self.play(
            *[FadeIn(d) for d in red_dots],
            FadeIn(lt_label, shift=UP * 0.15),
            run_time=NORMAL,
        )
        self.wait(17)
        self.ly.clear()

        # Well-ordering
        self.add_subcaption(
            "The natural numbers have a special property called well-ordering. "
            "Every non-empty set of natural numbers has a smallest element. "
            "This sounds completely obvious, but it is actually a deep property "
            "that fails for other number systems. The integers, for example, "
            "include negative numbers that go on forever in both directions, "
            "so there is no smallest integer. Well-ordering is what makes "
            "many proofs about natural numbers work.",
            duration=28,
        )
        title2 = self.ly.title("Well-Ordering Principle")
        items = [
            Text("Every non-empty set of natural numbers",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("has a smallest element",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Fails for integers: {..., -2, -1, 0, 1, ...}",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Well-ordering is essential for many proofs",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(22)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Induction Example
    # ------------------------------------------------------------------
    def scene8_induction_example(self):
        """Show a simple induction proof."""
        self.add_subcaption(
            "Let us see induction in action with a famous formula. "
            "Claim: the sum of the first n natural numbers equals n times "
            "n plus one, all over two. We prove this by induction on n. "
            "Base case: when n equals zero, the sum is just zero, and the "
            "formula gives zero times one over two, which is zero. The base "
            "case checks out.",
            duration=26,
        )
        self.ly.section_divider(7, "Induction in Action")
        title = self.ly.title("Sum of First n Natural Numbers")

        # The claim
        claim = MathTex(
            r"0 + 1 + 2 + \cdots + n = \frac{n(n+1)}{2}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(claim, DOWN, anchor=title, buff=0.5)
        self.play(Write(claim), run_time=SLOW)
        self.wait(FAST)

        # Base case
        base_title = Text(
            "Base case (n = 0):", font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(base_title, DOWN, anchor=claim, buff=0.5)
        self.play(FadeIn(base_title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(FAST)

        base_check = MathTex(
            r"0 = \frac{0 \times 1}{2} = 0 \quad \text{\checkmark}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(base_check, DOWN, anchor=base_title, buff=0.3)
        self.play(Write(base_check), run_time=NORMAL)
        self.wait(16)
        self.ly.clear()

        # Inductive step
        self.add_subcaption(
            "For the inductive step, we assume the formula holds for some "
            "number n. Then the sum up to n plus one equals the sum up to n, "
            "plus n plus one. By our assumption, the sum up to n is n times "
            "n plus one over two. Adding n plus one and simplifying gives us "
            "n plus one times n plus two, all over two. This is exactly the "
            "formula with n replaced by n plus one. The inductive step is "
            "complete. By axiom five, the formula holds for all n.",
            duration=34,
        )
        title2 = self.ly.title("Inductive Step")
        items = [
            Text("Assume: sum to n = n(n+1)/2",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Sum to (n+1) = sum to n + (n+1)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("= n(n+1)/2 + (n+1)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("= (n+1)(n+2) / 2  -- formula holds for n+1",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(28)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Foundation of Mathematics
    # ------------------------------------------------------------------
    def scene9_foundation(self):
        """Show how N is the foundation for all number systems."""
        self.add_subcaption(
            "The natural numbers are the foundation of all mathematics. "
            "From the naturals we build the integers by adding negative numbers. "
            "From integers we build the rational numbers as fractions. "
            "From rationals we fill in the gaps to get the real numbers. "
            "And from reals we add the imaginary unit i to get the complex "
            "numbers. Every theorem in every branch of mathematics, from "
            "calculus to topology to number theory, ultimately rests on the "
            "natural numbers. That is why we start here.",
            duration=32,
        )
        self.ly.section_divider(8, "The Foundation")
        title = self.ly.title("Everything Builds on N")

        # Tower of number systems
        systems = [
            (r"\mathbb{N}", "Natural Numbers", PRIMARY),
            (r"\mathbb{Z}", "Integers  (+ negatives)", SECONDARY),
            (r"\mathbb{Q}", "Rationals  (fractions)", ACCENT),
            (r"\mathbb{R}", "Reals  (fill the gaps)", RED),
            (r"\mathbb{C}", "Complex  (+ imaginary unit i)", WHITE),
        ]
        boxes = []
        for i, (sym, desc, color) in enumerate(systems):
            box = RoundedRectangle(
                corner_radius=0.12,
                fill_color=color,
                fill_opacity=0.12,
                stroke_color=color,
                stroke_width=2,
                width=5.5,
                height=0.55,
            )
            sym_tex = MathTex(sym, font_size=BODY_SIZE, color=color)
            desc_text = Text(desc, font_size=LABEL_SIZE, color=DIM, font=SANS)
            label = VGroup(sym_tex, desc_text).arrange(RIGHT, buff=0.4)
            group = VGroup(box, label)
            boxes.append(group)

        tower = VGroup(*boxes).arrange(DOWN, buff=0.25)
        self.ly.safe_place(tower, DOWN, anchor=title, buff=0.5)

        for box_group in boxes:
            self.play(FadeIn(box_group, shift=UP * 0.1), run_time=NORMAL)
            self.wait(FAST)

        self.wait(19)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Summary
    # ------------------------------------------------------------------
    def scene10_summary(self):
        """Key takeaways and outro."""
        self.add_subcaption(
            "Let us recap. The natural numbers are the counting numbers, "
            "starting from zero and going on forever. They can be built "
            "from nothing using just the successor function. Peano's five "
            "axioms give a complete and rigorous foundation. The well-ordering "
            "principle is a powerful property unique to the naturals. "
            "Mathematical induction follows directly from the structure of "
            "the successor chain. And the natural numbers are the bedrock on "
            "which all other number systems and all of mathematics are built. "
            "In the next video, we learn how to add and subtract. See you then.",
            duration=36,
        )
        self.ly.section_divider(9, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("N = {0, 1, 2, 3, ...}  -- the counting numbers",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Built from 0 using the successor function S(n)",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Peano's 5 axioms give a complete foundation",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Well-ordered: every subset has a smallest element",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("All of mathematics rests on the natural numbers",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(18)
        self.ly.clear()
        play_outro(self, next_video="Addition and Subtraction", next_playlist="Numbers & Arithmetic")
