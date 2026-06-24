"""Video 84: Counting Principles
Discrete Mathematics -- Video 6 of 12

Covers: Fundamental counting principle (product rule), permutations P(n,k),
combinations C(n,k), binomial coefficient properties, symmetry,
Pascal's identity, applications (poker hands, lottery, arrangements).

Plan: planning/video-84-counting-principles.md

Render draft:  manim -ql scripts/undergraduate/video-84-counting-principles.py Video84_CountingPrinciples
Render final:  manim -qh scripts/undergraduate/video-84-counting-principles.py Video84_CountingPrinciples
"""

from manim import *
import sys, os
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits, clamp_position


class Video84_CountingPrinciples(Scene):
    """Counting Principles -- product rule, permutations, combinations,
    binomial coefficients, Pascal's triangle."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_product_rule()
        self.scene3_permutations()
        self.scene4_permutation_examples()
        self.scene5_combinations()
        self.scene6_poker_hands()
        self.scene7_binomial_pascal()
        self.scene8_pascal_identity()
        self.scene9_applications()
        self.scene10_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook -- How Many Ways? (1:30)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "In the last video we studied equivalence relations and partitions. "
            "Now we turn to a different question: how many elements are in a set? "
            "How many possible PIN codes exist? "
            "How many different poker hands can you be dealt? "
            "How many ways can you arrange books on a shelf? "
            "These seemingly different questions share a common mathematical structure. "
            "The answer lies in counting principles. "
            "Let's learn how to count systematically.",
            duration=22,
        )
        play_intro(self, "Counting Principles", "Discrete Mathematics")

        title = self.ly.title("How Many Ways?")

        # Bridge from Video 83
        bridge = Text(
            "Equivalence relations partition sets into groups.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(bridge, direction=DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Counting questions
        q1 = Text(
            "How many 4-digit PIN codes exist?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(q1, direction=DOWN, anchor=bridge, buff=0.4)
        self.play(FadeIn(q1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        q2 = Text(
            "How many 5-card poker hands from 52 cards?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(q2, direction=DOWN, anchor=q1, buff=0.4)
        self.play(FadeIn(q2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        q3 = Text(
            "How many ways to arrange 5 books on a shelf?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(q3, direction=DOWN, anchor=q2, buff=0.4)
        self.play(FadeIn(q3, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Fade questions, show concept
        self.play(
            FadeOut(bridge), FadeOut(q1), FadeOut(q2), FadeOut(q3),
            run_time=0.4,
        )

        concept = Text(
            "These share a common structure: counting principles.",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(concept)
        self.play(FadeIn(concept, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Fundamental Counting Principle (1:30)
    # ------------------------------------------------------------------
    def scene2_product_rule(self):
        self.add_subcaption(
            "The fundamental counting principle is the most basic rule. "
            "If task A has m outcomes and task B has n outcomes, "
            "then A followed by B has m times n outcomes. "
            "Think of choosing a shirt and then pants. "
            "With 3 shirts and 4 pants, you have 3 times 4 equals 12 outfits. "
            "This generalizes: for k sequential tasks, "
            "multiply the number of outcomes at each step. "
            "The product rule is the foundation of all combinatorics.",
            duration=24,
        )
        self.ly.section_divider(1, "Fundamental Counting Principle")

        title = self.ly.title("The Product Rule")

        # Statement
        stmt = Text(
            "If task A has m outcomes and B has n outcomes,",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(stmt, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(stmt, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        formula = MathTex(
            r"A \text{ followed by } B \text{ has } m \times n \text{ outcomes}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(formula, direction=DOWN, anchor=stmt, buff=0.4)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Tree diagram visualization
        title2 = self.ly.title("Tree Diagram: 3 Shirts x 4 Pants")

        # Build a simple tree: root -> 3 branches -> each -> 4 branches
        root = Dot(LEFT * 3.5, color=PRIMARY, radius=0.08)
        self.add(root)
        self.wait(0.3)

        level1_positions = [UP * 1.5, ORIGIN, DOWN * 1.5]
        shirts = ["S1", "S2", "S3"]
        level1_dots = []
        for i, pos in enumerate(level1_positions):
            d = Dot(LEFT * 1.5 + pos, color=PRIMARY, radius=0.08)
            l = Line(root.get_center(), d.get_center(), color=PRIMARY, stroke_width=2)
            self.play(Create(l), FadeIn(d), run_time=0.4)
            t = Text(shirts[i], font_size=SMALL_SIZE, color=WHITE, font=MONO)
            t.next_to(d, LEFT, buff=0.15)
            self.play(FadeIn(t), run_time=0.2)
            level1_dots.append(d)
        self.wait(0.5)

        # Second level: 4 branches from each (show only from S1 for clarity)
        level2_labels = ["P1", "P2", "P3", "P4"]
        level2_positions = [UP * 1.8, UP * 0.6, DOWN * 0.6, DOWN * 1.8]
        for i, (pos, label) in enumerate(zip(level2_positions, level2_labels)):
            d = Dot(RIGHT * 0.5 + pos, color=SECONDARY, radius=0.08)
            l = Line(level1_dots[0].get_center(), d.get_center(),
                     color=SECONDARY, stroke_width=1.5)
            self.play(Create(l), FadeIn(d), run_time=0.3)
            t = Text(label, font_size=SMALL_SIZE, color=WHITE, font=MONO)
            t.next_to(d, RIGHT, buff=0.15)
            self.play(FadeIn(t), run_time=0.15)
        self.wait(0.5)

        # Result annotation
        result = Text(
            "3 x 4 = 12 outfits total",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(result, direction=DOWN,
                           anchor=Dot(DOWN * 1.8, color=SECONDARY, radius=0.08),
                           buff=0.6)
        self.play(FadeIn(result, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Generalization
        title3 = self.ly.title("Generalization")

        gen = MathTex(
            r"n_1 \times n_2 \times \cdots \times n_k",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(gen)
        self.play(Write(gen), run_time=NORMAL)
        self.wait(0.8)

        gen_text = Text(
            "For k sequential tasks, multiply the outcomes at each step.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(gen_text, direction=DOWN, anchor=gen, buff=0.5)
        self.play(FadeIn(gen_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Permutations -- When Order Matters (1:30)
    # ------------------------------------------------------------------
    def scene3_permutations(self):
        self.add_subcaption(
            "Now suppose we select k items from n distinct items, "
            "and the order in which we arrange them matters. "
            "This is called a permutation. "
            "Imagine placing items into labeled slots. "
            "For the first slot, there are n choices. "
            "For the second, n minus 1. For the third, n minus 2. "
            "And so on, for k slots. "
            "This gives the formula P of n, k equals n factorial "
            "divided by n minus k factorial. "
            "When k equals n, this simplifies to n factorial.",
            duration=24,
        )
        self.ly.section_divider(2, "Permutations: Order Matters")

        title = self.ly.title("Arranging into Slots")

        # Visual: 4 objects A, B, C, D arranging into 3 slots
        objs = VGroup(
            Square(side_length=0.5, fill_color=PRIMARY, fill_opacity=0.8, stroke_width=0),
            Square(side_length=0.5, fill_color=SECONDARY, fill_opacity=0.8, stroke_width=0),
            Square(side_length=0.5, fill_color=ACCENT, fill_opacity=0.8, stroke_width=0),
            Square(side_length=0.5, fill_color=RED, fill_opacity=0.8, stroke_width=0),
        )
        labels_a = VGroup(
            MathTex(r"A", font_size=LABEL_SIZE, color=WHITE),
            MathTex(r"B", font_size=LABEL_SIZE, color=WHITE),
            MathTex(r"C", font_size=LABEL_SIZE, color=WHITE),
            MathTex(r"D", font_size=LABEL_SIZE, color=WHITE),
        )
        for obj, lab in zip(objs, labels_a):
            lab.move_to(obj)
        objs_with_labels = VGroup(*[
            VGroup(o, l) for o, l in zip(objs, labels_a)
        ])
        objs_with_labels.arrange(RIGHT, buff=0.3)
        objs_with_labels.next_to(title, DOWN, buff=0.6)
        self.play(FadeIn(objs_with_labels), run_time=NORMAL)
        self.wait(1)

        # Slots
        slots = VGroup(*[
            Rectangle(width=0.8, height=0.8, stroke_color=DIM, stroke_width=2,
                       fill_opacity=0)
            for _ in range(3)
        ])
        slots.arrange(RIGHT, buff=0.5)
        slots.move_to(DOWN * 1.2)
        self.play(FadeIn(slots), run_time=0.5)

        # Count choices for each slot
        choices1 = MathTex(r"4 \text{ choices}", font_size=LABEL_SIZE, color=PRIMARY)
        choices1.next_to(slots[0], UP, buff=0.3)
        self.play(Write(choices1), run_time=0.5)
        self.wait(0.5)

        choices2 = MathTex(r"3 \text{ choices}", font_size=LABEL_SIZE, color=PRIMARY)
        choices2.next_to(slots[1], UP, buff=0.3)
        self.play(Write(choices2), run_time=0.5)
        self.wait(0.5)

        choices3 = MathTex(r"2 \text{ choices}", font_size=LABEL_SIZE, color=PRIMARY)
        choices3.next_to(slots[2], UP, buff=0.3)
        self.play(Write(choices3), run_time=0.5)
        self.wait(1)
        self.ly.clear()

        # Formula
        title2 = self.ly.title("Permutation Formula")

        formula_box = MathTex(
            r"P(n, k) = \frac{n!}{(n - k)!}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(formula_box)
        box = SurroundingRectangle(formula_box, color=PRIMARY, buff=0.25,
                                   stroke_width=2, corner_radius=0.1)
        self.play(Write(formula_box), run_time=NORMAL)
        self.play(Create(box), run_time=0.5)
        self.wait(1)

        special = MathTex(
            r"P(n, n) = n!",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(special, direction=DOWN, anchor=formula_box, buff=0.6)
        self.play(Write(special), run_time=NORMAL)
        self.wait(0.8)

        example = Text(
            "Arrange 5 books on a shelf: 5! = 120 ways",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(example, direction=DOWN, anchor=special, buff=0.4)
        self.play(FadeIn(example, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Permutations -- Worked Example (1:00)
    # ------------------------------------------------------------------
    def scene4_permutation_examples(self):
        self.add_subcaption(
            "Let's work through some examples. "
            "How many ways can 8 runners finish on the podium? "
            "That means choosing 3 from 8 where order matters. "
            "P of 8, 3 equals 8 factorial over 5 factorial "
            "equals 8 times 7 times 6 equals 336. "
            "Next, how many 4-letter codes from 26 letters with no repeats? "
            "P of 26, 4 equals 26 times 25 times 24 times 23, "
            "which equals 358 thousand 800. "
            "The permutation formula handles any arrangement problem.",
            duration=24,
        )
        self.ly.section_divider(3, "Permutation Examples")

        # Example 1: Podium
        title = self.ly.title("Podium Arrangements")

        problem1 = Text(
            "8 runners, 3 podium spots: how many arrangements?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(problem1, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(problem1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        steps1 = MathTex(
            r"P(8, 3) = \frac{8!}{5!} = 8 \times 7 \times 6 = 336",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(steps1, direction=DOWN, anchor=problem1, buff=0.5)
        self.play(Write(steps1), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Example 2: Letter codes
        title2 = self.ly.title("Letter Codes")

        problem2 = Text(
            "4-letter codes from 26 letters (no repeats)?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(problem2, direction=DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(problem2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        steps2 = MathTex(
            r"P(26, 4) = 26 \times 25 \times 24 \times 23 = 358{,}800",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(steps2, direction=DOWN, anchor=problem2, buff=0.5)
        self.play(Write(steps2), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Combinations -- When Order Doesn't Matter (1:30)
    # ------------------------------------------------------------------
    def scene5_combinations(self):
        self.add_subcaption(
            "Now the key question: what if order doesn't matter? "
            "Take the set A, B, C. "
            "The permutations ABC, ACB, BAC, BCA, CAB, CBA "
            "all select the same three elements. "
            "They are 6 different orderings of the same combination. "
            "Every k-element combination has k factorial permutations. "
            "So the combination formula divides the permutation by k factorial. "
            "C of n, k equals n factorial over k factorial times n minus k factorial. "
            "Example: choosing 3 friends from 5 for a committee "
            "equals C of 5, 3 which is 10.",
            duration=26,
        )
        self.ly.section_divider(4, "Combinations: Order Doesn't Matter")

        title = self.ly.title("Same Set, Different Orders")

        # Show permutations of {A, B, C}
        perms_text = MathTex(
            r"\text{ABC, ACB, BAC, BCA, CAB, CBA}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(perms_text, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(perms_text), run_time=NORMAL)
        self.wait(1)

        # Collapse into one combination
        collapse = MathTex(
            r"\Longrightarrow \{A, B, C\}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(collapse, direction=DOWN, anchor=perms_text, buff=0.5)
        self.play(Write(collapse), run_time=NORMAL)
        self.wait(0.8)

        note = Text(
            "6 permutations = 1 combination (3! = 6 orderings)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=collapse, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Formula
        title2 = self.ly.title("Combination Formula")

        formula = MathTex(
            r"C(n, k) = \frac{P(n, k)}{k!} = \frac{n!}{k!\,(n - k)!}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.center_in_content(formula)
        box = SurroundingRectangle(formula, color=SECONDARY, buff=0.25,
                                   stroke_width=2, corner_radius=0.1)
        self.play(Write(formula), run_time=NORMAL)
        self.play(Create(box), run_time=0.5)
        self.wait(1)

        example = Text(
            "Choose 3 from 5 for a committee: C(5,3) = 10",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(example, direction=DOWN, anchor=formula, buff=0.6)
        self.play(FadeIn(example, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Combinations -- Poker Hands (1:00)
    # ------------------------------------------------------------------
    def scene6_poker_hands(self):
        self.add_subcaption(
            "The classic application: poker hands. "
            "A standard deck has 52 cards. "
            "How many 5-card hands are possible? "
            "Since a hand is a set of cards, order doesn't matter. "
            "So we use combinations. "
            "C of 52, 5 equals 2 million 598 thousand 960. "
            "Compare this to permutations: P of 52, 5 "
            "would give 311 million 875 thousand 200. "
            "Combinations are much smaller because we divide by 5 factorial equals 120. "
            "When the problem is about selecting, not arranging, use combinations.",
            duration=26,
        )
        self.ly.section_divider(5, "Application: Poker Hands")

        title = self.ly.title("5-Card Poker Hands")

        problem = Text(
            "How many 5-card hands from a 52-card deck?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(problem, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(problem, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Combination computation
        combo = MathTex(
            r"C(52, 5) = \frac{52!}{5!\,47!} = 2{,}598{,}960",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(combo, direction=DOWN, anchor=problem, buff=0.5)
        self.play(Write(combo), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Comparison with permutations
        title2 = self.ly.title("Permutations vs. Combinations")

        perm = MathTex(
            r"P(52, 5) = 311{,}875{,}200",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(perm, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(perm), run_time=NORMAL)
        self.wait(0.8)

        comb = MathTex(
            r"C(52, 5) = 2{,}598{,}960",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(comb, direction=DOWN, anchor=perm, buff=0.4)
        self.play(Write(comb), run_time=NORMAL)
        self.wait(0.8)

        ratio = Text(
            "Difference: factor of 5! = 120",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(ratio, direction=DOWN, anchor=comb, buff=0.4)
        self.play(FadeIn(ratio, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Binomial Coefficients + Pascal's Triangle (1:30)
    # ------------------------------------------------------------------
    def scene7_binomial_pascal(self):
        self.add_subcaption(
            "C of n, k is called the binomial coefficient. "
            "It appears in the binomial theorem, probability, and algebra. "
            "A beautiful property: symmetry. "
            "C of n, k equals C of n, n minus k. "
            "These coefficients form Pascal's triangle. "
            "Row n contains the coefficients C of n, k for k from 0 to n. "
            "Each row begins and ends with 1. "
            "Row 2: 1, 2, 1. Row 3: 1, 3, 3, 1. Row 4: 1, 4, 6, 4, 1. "
            "Watch how the triangle builds up row by row.",
            duration=26,
        )
        self.ly.section_divider(6, "Binomial Coefficients")

        title = self.ly.title("Symmetry Property")

        sym = MathTex(
            r"C(n, k) = C(n, n - k)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(sym)
        box = SurroundingRectangle(sym, color=ACCENT, buff=0.25,
                                   stroke_width=2, corner_radius=0.1)
        self.play(Write(sym), run_time=NORMAL)
        self.play(Create(box), run_time=0.5)
        self.wait(0.8)

        explain = Text(
            "Choosing k from n = choosing n-k to leave behind",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(explain, direction=DOWN, anchor=sym, buff=0.5)
        self.play(FadeIn(explain, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Pascal's Triangle
        title2 = self.ly.title("Pascal's Triangle")

        # Build triangle rows
        rows_data = [
            ["1"],
            ["1", "1"],
            ["1", "2", "1"],
            ["1", "3", "3", "1"],
            ["1", "4", "6", "4", "1"],
        ]

        start_y = 1.8
        row_spacing = 0.7
        all_entries = VGroup()

        for row_idx, row in enumerate(rows_data):
            row_entries = VGroup()
            num_entries = len(row)
            x_spacing = 0.8
            total_width = (num_entries - 1) * x_spacing
            start_x = -total_width / 2

            for col_idx, val in enumerate(row):
                color = ACCENT if (row_idx == 4 and col_idx == 2) else WHITE
                if col_idx == 0 or col_idx == num_entries - 1:
                    color = PRIMARY
                entry = MathTex(
                    val, font_size=LABEL_SIZE, color=color,
                )
                entry.move_to([
                    start_x + col_idx * x_spacing,
                    start_y - row_idx * row_spacing, 0
                ])
                row_entries.add(entry)

            self.play(FadeIn(row_entries), run_time=0.5)
            all_entries.add(row_entries)
            self.wait(0.3)

        self.wait(1)

        # Label
        label = Text(
            "Each entry = C(n, k) for row n, position k",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(label, direction=DOWN,
                           anchor=Dot(DOWN * (start_y - 4 * row_spacing + 0.5),
                                      color=WHITE, radius=0.01),
                           buff=0.5)
        self.play(FadeIn(label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Pascal's Identity (1:00)
    # ------------------------------------------------------------------
    def scene8_pascal_identity(self):
        self.add_subcaption(
            "The most important identity for binomial coefficients "
            "is Pascal's identity. "
            "C of n, k equals C of n minus 1, k minus 1, "
            "plus C of n minus 1, k. "
            "In Pascal's triangle, each entry equals the sum "
            "of the two entries directly above it. "
            "The proof is elegant: an n-element set either "
            "includes element n or it doesn't. "
            "If it does, choose k minus 1 from the remaining n minus 1. "
            "If it doesn't, choose k from the remaining n minus 1. "
            "These two cases cover every possibility.",
            duration=26,
        )
        self.ly.section_divider(7, "Pascal's Identity")

        title = self.ly.title("Pascal's Identity")

        identity = MathTex(
            r"C(n, k) = C(n{-}1, k{-}1) + C(n{-}1, k)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(identity)
        box = SurroundingRectangle(identity, color=ACCENT, buff=0.25,
                                   stroke_width=2, corner_radius=0.1)
        self.play(Write(identity), run_time=NORMAL)
        self.play(Create(box), run_time=0.5)
        self.wait(1)
        self.ly.clear()

        # Visual: triangle snippet
        title2 = self.ly.title("Each Cell = Sum Above")

        # Show row 3 and row 4 snippet
        parent1 = MathTex("1", font_size=LABEL_SIZE, color=PRIMARY)
        parent2 = MathTex("3", font_size=LABEL_SIZE, color=PRIMARY)
        child = MathTex("4", font_size=HEADING_SIZE, color=ACCENT)

        parent1.move_to(LEFT * 0.6 + UP * 0.8)
        parent2.move_to(RIGHT * 0.6 + UP * 0.8)
        child.move_to(ORIGIN)

        self.play(FadeIn(parent1), FadeIn(parent2), run_time=0.5)
        self.wait(0.3)

        # Lines from parents to child
        line1 = Line(parent1.get_center(), child.get_center(),
                     color=PRIMARY, stroke_width=1.5)
        line2 = Line(parent2.get_center(), child.get_center(),
                     color=PRIMARY, stroke_width=1.5)
        self.play(Create(line1), Create(line2), run_time=0.5)

        self.play(FadeIn(child), run_time=0.5)

        plus = MathTex(r"1 + 3 = 4", font_size=BODY_SIZE, color=WHITE)
        plus.next_to(child, DOWN, buff=0.4)
        self.play(Write(plus), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Proof intuition
        title3 = self.ly.title("Why? Two Cases")

        case1 = Text(
            "Includes element n: choose k-1 from n-1",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(case1, direction=DOWN, anchor=title3, buff=0.5)
        self.play(FadeIn(case1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        case2 = Text(
            "Excludes element n: choose k from n-1",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(case2, direction=DOWN, anchor=case1, buff=0.4)
        self.play(FadeIn(case2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        or_text = Text(
            "Two cases, no overlap = complete partition",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(or_text, direction=DOWN, anchor=case2, buff=0.4)
        self.play(FadeIn(or_text, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Applications Summary (1:00)
    # ------------------------------------------------------------------
    def scene9_applications(self):
        self.add_subcaption(
            "Counting principles appear everywhere. "
            "A lottery draws 6 numbers from 49. "
            "The number of possible tickets is C of 49, 6 "
            "equals 13 million 983 thousand 816. "
            "Your chance of winning is about 1 in 14 million. "
            "An n-bit string has 2 to the n possible values. "
            "Each position has 2 choices, and there are n positions. "
            "Binary relations on an n-element set: "
            "2 to the n squared possible relations. "
            "Each of n squared ordered pairs is either in or out. "
            "Next video: what happens when we have more pigeons than holes?",
            duration=28,
        )
        self.ly.section_divider(8, "Applications")

        title = self.ly.title("Counting in the Wild")

        items = [
            Text(
                "Lottery: C(49,6) = 13,983,816 (1 in ~14M)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "n-bit strings: 2^n possibilities",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Relations on n elements: 2^(n^2)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.5)

        # Teaser for next video
        self.ly.clear()

        title2 = self.ly.title("Coming Next")

        teaser = Text(
            "What happens when we have MORE pigeons than holes?",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(teaser)
        self.play(FadeIn(teaser, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Summary + Outro (0:30)
    # ------------------------------------------------------------------
    def scene10_summary(self):
        self.add_subcaption(
            "Let's recap counting principles. "
            "The product rule multiplies outcomes for sequential tasks. "
            "Permutations P of n, k equal n factorial over n minus k factorial, "
            "for arrangements where order matters. "
            "Combinations C of n, k equal n factorial over "
            "k factorial times n minus k factorial, "
            "for selections where order doesn't matter. "
            "The binomial coefficients have elegant structure: "
            "symmetry, Pascal's triangle, and Pascal's identity. "
            "Next up: the Pigeonhole Principle.",
            duration=24,
        )
        title = self.ly.title("Summary")

        items = [
            Text(
                "Product rule: multiply outcomes at each step",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Permutations P(n,k): order matters",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Combinations C(n,k): order doesn't matter",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Binomial coefficients: symmetry + Pascal's triangle",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Pascal's identity: C(n,k) = C(n-1,k-1) + C(n-1,k)",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        play_outro(self, "Pigeonhole Principle", "Discrete Mathematics")
        self.ly.clear()
