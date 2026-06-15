"""Video 68: Conditional Probability
Probability & Statistics -- Video 2 of 12

Covers: conditional probability definition, P(A|B) = P(A cap B) / P(B),
medical test puzzle, dice worked example, contingency table approach,
key properties (P(A|B) != P(B|A)), law of total probability teaser.

Competitive analysis: channel-analysis/improvements.md "2026-06-15 -- Conditional Probability"
Plan: planning/video-68-conditional-probability.md

Render draft:  manim -ql scripts/undergraduate/video-68-conditional-probability.py Video68_ConditionalProbability
Render final:  manim -qh scripts/undergraduate/video-68-conditional-probability.py Video68_ConditionalProbability
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


class Video68_ConditionalProbability(Scene):
    """Full video: Conditional Probability -- how evidence changes probability."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_medical_test_hook()
        self.scene2_coin_bag_example()
        self.scene3_formal_definition()
        self.scene4_dice_example()
        self.scene5_contingency_table()
        self.scene6_key_properties()
        self.scene7_summary()

    # -- Scene 1: Hook -- The Medical Test Puzzle --
    def scene1_medical_test_hook(self):
        self.add_subcaption(
            "A test for a rare disease is ninety nine percent accurate. "
            "You take the test and get a positive result. "
            "Most people would say the probability is ninety nine percent. "
            "But the real answer is much lower.",
            duration=20,
        )
        play_intro(self, "Conditional Probability",
                   "Probability & Statistics")

        title = self.ly.title("The Medical Test Puzzle")

        self.add_subcaption(
            "A disease affects one in a thousand people. "
            "The test is correct ninety nine percent of the time. "
            "If you test positive, what is the probability "
            "you actually have the disease?",
            duration=18,
        )

        q1 = Text(
            "Disease prevalence: 1 in 1,000",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(q1, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(q1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        q2 = Text(
            "Test accuracy: 99%",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(q2, DOWN, anchor=q1, buff=0.25)
        self.play(FadeIn(q2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.add_subcaption(
            "Surprisingly, even with a positive test, "
            "your chance of having the disease is only about nine percent. "
            "Why? Because the disease is so rare that false positives "
            "outnumber true positives by far. This is conditional probability.",
            duration=18,
        )

        q3 = Text(
            "Given positive test: P(disease) = ?",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(q3, DOWN, anchor=q2, buff=0.3)
        self.play(FadeIn(q3, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        answer = MathTex(
            r"= \frac{0.00099}{0.01089} \approx 9\%",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(answer, DOWN, anchor=q3, buff=0.25)
        self.play(Write(answer), run_time=SLOW)
        self.wait(4)

        self.add_subcaption(
            "This kind of question, probability of one event "
            "given that another has occurred, is called "
            "conditional probability. Let us see how it works.",
            duration=14,
        )

        bridge = Text(
            "This is conditional probability: P(A given B).",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(bridge, DOWN, anchor=answer, buff=0.25)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

    # -- Scene 2: Motivating Example -- Two Bags of Coins --
    def scene2_coin_bag_example(self):
        self.ly.section_divider(1, "A Motivating Example")

        self.add_subcaption(
            "Imagine two bags of coins. Bag A contains three gold coins "
            "and one silver coin. Bag B contains one gold coin "
            "and three silver coins. You pick a bag at random.",
            duration=16,
        )

        title = self.ly.title("Two Bags of Coins")

        # Draw two rectangles representing the bags
        bag_a_rect = Rectangle(
            width=2.2, height=2.5, stroke_color=PRIMARY,
            fill_color=PRIMARY, fill_opacity=0.15,
        )
        bag_a_label = Text("Bag A", font_size=LABEL_SIZE, color=PRIMARY, font=MONO)
        bag_a_label.next_to(bag_a_rect, UP, buff=0.15)
        bag_a_group = VGroup(bag_a_rect, bag_a_label)

        bag_b_rect = Rectangle(
            width=2.2, height=2.5, stroke_color=SECONDARY,
            fill_color=SECONDARY, fill_opacity=0.15,
        )
        bag_b_label = Text("Bag B", font_size=LABEL_SIZE, color=SECONDARY, font=MONO)
        bag_b_label.next_to(bag_b_rect, UP, buff=0.15)
        bag_b_group = VGroup(bag_b_rect, bag_b_label)

        left_col, right_col = self.ly.two_columns(
            [bag_a_group], [bag_b_group],
            start_from=title,
        )
        self.play(Create(bag_a_rect), FadeIn(bag_a_label),
                  Create(bag_b_rect), FadeIn(bag_b_label),
                  run_time=NORMAL)
        self.wait(2)

        # Add coin labels inside
        self.add_subcaption(
            "Bag A has three gold and one silver. "
            "Bag B has one gold and three silver. "
            "You reach into the randomly chosen bag "
            "and pull out a gold coin.",
            duration=16,
        )

        coins_a = Text(
            "3 gold, 1 silver",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        coins_a.move_to(bag_a_rect.get_center())
        coins_b = Text(
            "1 gold, 3 silver",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        coins_b.move_to(bag_b_rect.get_center())

        self.play(FadeIn(coins_a, shift=LEFT * 0.1), run_time=FAST)
        self.play(FadeIn(coins_b, shift=LEFT * 0.1), run_time=FAST)
        self.wait(2)

        self.add_subcaption(
            "You drew a gold coin. What is the probability "
            "that you chose Bag A? This is exactly a conditional "
            "probability question. Probability of Bag A, "
            "given gold.",
            duration=14,
        )

        question = MathTex(
            r"P(\text{Bag } A \mid \text{gold}) = \; ?",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(question, DOWN, anchor=title, buff=5.0)
        self.play(Write(question), run_time=SLOW)
        self.wait(4)

        self.add_subcaption(
            "Intuitively, Bag A has more gold coins, "
            "so it should be more likely. But how do we "
            "compute this precisely? That is the formula.",
            duration=14,
        )

        hint = Text(
            "Bag A has 75% gold. Bag B has 25% gold.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(hint, DOWN, anchor=question, buff=0.25)
        self.play(FadeIn(hint, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

    # -- Scene 3: Formal Definition --
    def scene3_formal_definition(self):
        self.ly.section_divider(2, "The Definition")

        self.add_subcaption(
            "The conditional probability of A given B "
            "is defined as the probability of the intersection "
            "of A and B, divided by the probability of B. "
            "It tells us what fraction of B is also in A.",
            duration=16,
        )

        title = self.ly.title("Conditional Probability")

        formula = MathTex(
            r"P(A \mid B) = \frac{P(A \cap B)}{P(B)}",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.safe_place(formula, DOWN, anchor=title, buff=0.6)
        self.play(Write(formula), run_time=SLOW)
        self.wait(4)

        self.add_subcaption(
            "Here is the intuition using an area model. "
            "Think of the sample space Omega as a unit square. "
            "Events A and B are regions inside it. "
            "P of A given B is the fraction of B that overlaps A.",
            duration=16,
        )

        # Venn diagram
        venn_omega = Circle(radius=2.2, stroke_color=DIM, fill_opacity=0)
        venn_omega_label = Text(
            "Omega", font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        venn_omega_label.next_to(venn_omega, RIGHT, buff=0.1)

        venn_a = Circle(
            radius=0.9, stroke_color=PRIMARY, stroke_width=2,
            fill_color=PRIMARY, fill_opacity=0.3,
        ).shift(LEFT * 0.5)
        venn_b = Circle(
            radius=0.9, stroke_color=SECONDARY, stroke_width=2,
            fill_color=SECONDARY, fill_opacity=0.3,
        ).shift(RIGHT * 0.5)

        venn_a_label = Text("A", font_size=LABEL_SIZE, color=PRIMARY, font=MONO)
        venn_a_label.move_to(venn_a.get_center() + UP * 0.5 + LEFT * 0.15)
        venn_b_label = Text("B", font_size=LABEL_SIZE, color=SECONDARY, font=MONO)
        venn_b_label.move_to(venn_b.get_center() + UP * 0.5 + RIGHT * 0.15)

        # Intersection highlight
        intersection = Intersection(
            venn_a.copy(), venn_b.copy(),
            color=ACCENT, fill_opacity=0.5, stroke_width=0,
        )

        # Clear formula, show Venn below
        self.play(FadeOut(formula), run_time=FAST)

        # Remove title to make room
        title_copy = self.mobjects[0] if self.mobjects else None

        venn_group = VGroup(venn_omega, venn_omega_label,
                             venn_a, venn_b,
                             venn_a_label, venn_b_label)
        self.ly.center_in_content(venn_group)
        venn_group.shift(UP * 0.3)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m not in [venn_group]],
            run_time=FAST,
        )
        self.add(venn_group)
        self.play(Create(venn_omega), FadeIn(venn_omega_label),
                  run_time=FAST)
        self.play(Create(venn_a), Create(venn_b), run_time=NORMAL)
        self.play(FadeIn(venn_a_label), FadeIn(venn_b_label), run_time=FAST)
        self.wait(2)

        self.add_subcaption(
            "The intersection, where A and B overlap, "
            "is P of A intersect B. The full circle B "
            "represents P of B. So P of A given B is "
            "the overlap divided by the full area of B.",
            duration=16,
        )

        self.play(FadeIn(intersection), run_time=NORMAL)
        self.wait(4)

        # Show the formula again below Venn
        formula2 = MathTex(
            r"P(A \mid B) = \frac{P(A \cap B)}{P(B)}"
            r"= \frac{\text{overlap}}{\text{area of } B}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        formula2.to_edge(DOWN, buff=0.8)
        self.play(Write(formula2), run_time=SLOW)
        self.wait(4)

        self.add_subcaption(
            "In other words, conditional probability rescales "
            "everything relative to the new information B. "
            "We throw away everything outside of B and renormalize.",
            duration=14,
        )

        insight = Text(
            "Rescale: zoom into region B, measure what fraction is A.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        insight.next_to(formula2, UP, buff=0.2)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

    # -- Scene 4: Worked Example -- Dice --
    def scene4_dice_example(self):
        self.ly.section_divider(3, "Worked Example: Dice")

        self.add_subcaption(
            "Let us work through a concrete example. "
            "Roll a fair six sided die. Let A be the event "
            "that the result is even, and B be the event "
            "that the result is at least four.",
            duration=16,
        )

        title = self.ly.title("Dice Example")

        # Define the events
        def_a = Text(
            "A = {even number} = {2, 4, 6}",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(def_a, DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(def_a, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        def_b = Text(
            "B = {at least 4} = {4, 5, 6}",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(def_b, DOWN, anchor=def_a, buff=0.25)
        self.play(FadeIn(def_b, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.add_subcaption(
            "We want P of A given B. What is the probability "
            "of rolling an even number, given that the result "
            "is at least four?",
            duration=12,
        )

        question = MathTex(
            r"P(A \mid B) = \; ?",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(question, DOWN, anchor=def_b, buff=0.3)
        self.play(Write(question), run_time=NORMAL)
        self.wait(3)

        # Remove question to make room for steps
        self.remove(question)

        self.add_subcaption(
            "Step one: find P of B. The outcomes in B are "
            "four, five, six. That is three out of six, "
            "so P of B equals one half.",
            duration=14,
        )

        step1 = MathTex(
            r"P(B) = \frac{|\{4, 5, 6\}|}{6} = \frac{3}{6} = \frac{1}{2}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step1, DOWN, anchor=def_b, buff=0.3)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(3)

        self.add_subcaption(
            "Step two: find the intersection. A intersect B "
            "are the outcomes that are both even and at least four. "
            "That is four and six. So P of A intersect B "
            "equals two sixths, or one third.",
            duration=18,
        )

        step2 = MathTex(
            r"A \cap B = \{4, 6\} \implies P(A \cap B) = \frac{2}{6} = \frac{1}{3}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step2, DOWN, anchor=step1, buff=0.3)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(3)

        self.add_subcaption(
            "Step three: divide. P of A given B equals "
            "P of A intersect B divided by P of B. "
            "That is one third divided by one half, "
            "which equals two thirds.",
            duration=16,
        )

        step3 = MathTex(
            r"P(A \mid B) = \frac{1/3}{1/2} = \frac{2}{3}",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.safe_place(step3, DOWN, anchor=step2, buff=0.3)
        self.play(Write(step3), run_time=SLOW)
        self.wait(4)

        self.add_subcaption(
            "Let us verify this by counting. Given that we "
            "know the roll is four, five, or six, "
            "the even results are four and six. "
            "So two out of three, which confirms two thirds.",
            duration=16,
        )

        verify = Text(
            "Verify: B = {4,5,6}, evens in B = {4,6}, so 2/3. Confirmed!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(verify, DOWN, anchor=step3, buff=0.25)
        self.play(FadeIn(verify, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # -- Scene 5: Contingency Table Example --
    def scene5_contingency_table(self):
        self.ly.section_divider(4, "Contingency Table Approach")

        self.add_subcaption(
            "Conditional probability also arises naturally "
            "with survey data. Consider one hundred students "
            "surveyed about whether they like math and physics.",
            duration=16,
        )

        title = self.ly.title("Student Survey Example")

        # Build the table using strings (Table creates its own mobjects)
        header_style = {"font_size": LABEL_SIZE, "color": DIM, "font": MONO}
        cell_style = {"font_size": BODY_SIZE, "color": WHITE, "font": MONO}
        hl_style = {"font_size": BODY_SIZE, "color": ACCENT, "font": MONO}

        table_data = [
            ["", "Likes Math", "No Math", "Total"],
            ["Likes Physics", "30", "10", "40"],
            ["No Physics", "30", "30", "60"],
            ["Total", "60", "40", "100"],
        ]

        table = Table(
            table_data,
            element_to_mobject=lambda x: Text(
                str(x), **cell_style,
            ),
            include_outer_lines=True,
            line_config={"stroke_color": DIM, "stroke_width": 1},
        )
        table.scale(0.7)

        self.ly.safe_place(table, DOWN, anchor=title, buff=0.4)

        self.add_subcaption(
            "Thirty students like both subjects. "
            "Thirty like math only. Ten like physics only. "
            "Thirty like neither.",
            duration=12,
        )
        self.play(Create(table), run_time=SLOW)
        self.wait(4)

        self.add_subcaption(
            "Question: given that a student likes math, "
            "what is the probability they also like physics? "
            "We look at the math column. "
            "There are sixty math lovers total. "
            "Thirty of them also like physics.",
            duration=18,
        )

        question = MathTex(
            r"P(\text{Physics} \mid \text{Math}) = \frac{30}{60} = \frac{1}{2}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(question, DOWN, anchor=table, buff=0.4)
        self.play(Write(question), run_time=SLOW)
        self.wait(4)

        self.add_subcaption(
            "For comparison, among students who do not like math, "
            "only ten out of forty like physics, which is one quarter. "
            "So liking math makes you twice as likely to like physics.",
            duration=16,
        )

        compare = MathTex(
            r"P(\text{Physics} \mid \neg\text{Math}) = \frac{10}{40} = \frac{1}{4}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(compare, DOWN, anchor=question, buff=0.25)
        self.play(Write(compare), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # -- Scene 6: Key Properties --
    def scene6_key_properties(self):
        self.ly.section_divider(5, "Key Properties")

        title = self.ly.title("Important Properties")

        # Property 1: P(A|B) != P(B|A)
        self.add_subcaption(
            "The most common mistake is confusing P of A given B "
            "with P of B given A. They are generally not equal. "
            "For example, the probability of rain given clouds "
            "is very different from the probability of clouds given rain.",
            duration=18,
        )

        prop1 = MathTex(
            r"P(A \mid B) \neq P(B \mid A)",
            font_size=TITLE_SIZE, color=RED,
        )
        self.ly.safe_place(prop1, DOWN, anchor=title, buff=0.5)
        self.play(Write(prop1), run_time=SLOW)
        self.wait(2)

        example1 = Text(
            "Example: P(rain | clouds) >> P(clouds | rain)",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(example1, DOWN, anchor=prop1, buff=0.25)
        self.play(FadeIn(example1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        self.remove(prop1)
        self.remove(example1)

        # Property 2: Complement
        self.add_subcaption(
            "Property two: the conditional probability of the complement. "
            "P of not A given B equals one minus P of A given B. "
            "This mirrors the ordinary complement rule.",
            duration=16,
        )

        prop2 = MathTex(
            r"P(A^c \mid B) = 1 - P(A \mid B)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(prop2, DOWN, anchor=title, buff=0.5)
        self.play(Write(prop2), run_time=NORMAL)
        self.wait(4)

        self.remove(prop2)

        # Property 3: Law of total probability teaser
        self.add_subcaption(
            "Property three: the law of total probability. "
            "If B1 and B2 partition the sample space, "
            "then P of A equals the sum of P of A given B1 "
            "times P of B1, plus P of A given B2 times P of B2. "
            "We will see this again with Bayes theorem.",
            duration=20,
        )

        prop3 = MathTex(
            r"P(A) = P(A \mid B_1)\,P(B_1) + P(A \mid B_2)\,P(B_2)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(prop3, DOWN, anchor=title, buff=0.5)
        self.play(Write(prop3), run_time=SLOW)
        self.wait(4)

        teaser = Text(
            "This is the key to Bayes' theorem — coming next!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(teaser, DOWN, anchor=prop3, buff=0.25)
        self.play(FadeIn(teaser, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

    # -- Scene 7: Summary --
    def scene7_summary(self):
        self.add_subcaption(
            "Conditional probability is one of the most powerful "
            "ideas in probability and statistics. Let us review "
            "what we covered today.",
            duration=12,
        )

        play_outro(self, "Independence and Bayes' Theorem",
                   "Probability & Statistics")

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "P(A|B) = P(A cap B) / P(B) — the core formula",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Measures: what fraction of B is also in A?",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "P(A|B) and P(B|A) are NOT the same!",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Area / Venn models build geometric intuition",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Law of total probability links to Bayes' theorem",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)

        self.ly.clear()
