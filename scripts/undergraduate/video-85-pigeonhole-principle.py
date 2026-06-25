"""Video 85: Pigeonhole Principle
Discrete Mathematics -- Video 7 of 12

Covers: Statement of the Pigeonhole Principle, simple examples (birthdays,
socks drawer, months), proof via contradiction, generalized PHP (ceil(n/k)),
applications (recurring decimals, party handshakes/friends, Erdos-Szekeres
theorem on monotone subsequences).

Plan: planning/video-85-pigeonhole-principle.md

Render draft:  manim -ql scripts/undergraduate/video-85-pigeonhole-principle.py Video85_PigeonholePrinciple
Render final:  manim -qh scripts/undergraduate/video-85-pigeonhole-principle.py Video85_PigeonholePrinciple
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


class Video85_PigeonholePrinciple(Scene):
    """Pigeonhole Principle -- statement, examples, proof, generalized form,
    applications in number theory, graph theory, and combinatorics."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_statement()
        self.scene3_simple_examples()
        self.scene4_proof()
        self.scene5_generalized()
        self.scene6_recurring_decimals()
        self.scene7_party_friends()
        self.scene8_subsequences()
        self.scene9_power_summary()
        self.scene10_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook -- The Hairy Twins (1:30)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "In the last video we learned how to count. "
            "Now we meet a principle so simple it seems trivial, "
            "yet so powerful it forces impossible-seeming conclusions. "
            "Here is a claim: in this room right now, "
            "there are two people with the same number of hairs on their heads. "
            "This sounds absurd. "
            "But the pigeonhole principle makes it absolutely certain. "
            "Let's see why.",
            duration=22,
        )
        play_intro(self, "Pigeonhole Principle", "Discrete Mathematics")

        title = self.ly.title("An Impossible Claim")

        claim = Text(
            "\"Two people in this room have the\nsame number of hairs on their heads.\"",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(claim, direction=DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(claim, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        # Visual: crowd of stick figures
        self.ly.clear()
        title2 = self.ly.title("The Numbers Don't Lie")

        fact1 = Text(
            "Human head: at most ~100,000 hairs",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(fact1, direction=DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(fact1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        fact2 = Text(
            "Earth population: 8 billion people",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(fact2, direction=DOWN, anchor=fact1, buff=0.4)
        self.play(FadeIn(fact2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        fact3 = Text(
            "8,000,000,000 >> 100,000  =  same hair count is FORCED",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(fact3, direction=DOWN, anchor=fact2, buff=0.5)
        self.play(FadeIn(fact3, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Statement of the PHP (1:00)
    # ------------------------------------------------------------------
    def scene2_statement(self):
        self.add_subcaption(
            "The pigeonhole principle says: "
            "if you put n plus 1 pigeons into n pigeonholes, "
            "then at least one hole contains at least two pigeons. "
            "Formally, if the size of set A is greater than the size of set B, "
            "then any function from A to B is not injective. "
            "That means two different elements must map to the same target. "
            "This is deceptively simple. Its applications are deep.",
            duration=22,
        )
        self.ly.section_divider(1, "The Pigeonhole Principle")

        # Animated pigeons into holes
        title = self.ly.title("n+1 Pigeons, n Holes")

        # Create holes (rectangles)
        holes = VGroup(*[
            RoundedRectangle(
                corner_radius=0.1, width=1.2, height=0.9,
                stroke_color=SECONDARY, stroke_width=2, fill_opacity=0,
            )
            for _ in range(4)
        ])
        holes.arrange(RIGHT, buff=0.4)
        holes.move_to(DOWN * 1.0)
        self.play(FadeIn(holes), run_time=NORMAL)

        # Hole labels
        hole_labels = VGroup(*[
            Text(f"H{i+1}", font_size=SMALL_SIZE, color=SECONDARY, font=MONO)
            for i in range(4)
        ])
        for lbl, hole in zip(hole_labels, holes):
            lbl.next_to(hole, UP, buff=0.2)
        self.play(FadeIn(hole_labels), run_time=0.5)

        # Pigeons flying in (5 pigeons into 4 holes)
        pigeons = VGroup(*[
            Circle(radius=0.25, fill_color=PRIMARY, fill_opacity=0.8,
                   stroke_width=0)
            for _ in range(5)
        ])
        pigeon_labels = VGroup(*[
            Text(f"P{i+1}", font_size=SMALL_SIZE, color=WHITE, font=MONO)
            for i in range(5)
        ])
        for pl, pg in zip(pigeon_labels, pigeons):
            pl.move_to(pg)

        # Animate pigeons flying in from above
        start_positions = [
            LEFT * 5 + UP * 2 + RIGHT * i * 1.2
            for i in range(5)
        ]
        for i, (pg, pl, sp) in enumerate(zip(pigeons, pigeon_labels, start_positions)):
            pg.move_to(sp)
            pl.move_to(sp)
            # Place in hole i % 4, last pigeon goes to hole 0
            target_hole = holes[i % 4]
            self.play(
                pg.animate.move_to(target_hole.get_center()),
                pl.animate.move_to(target_hole.get_center()),
                run_time=0.5,
            )
        self.wait(0.5)

        # Highlight the collision (hole 0 has 2 pigeons)
        collision = SurroundingRectangle(
            holes[0], color=RED, stroke_width=3, corner_radius=0.15,
        )
        self.play(Create(collision), run_time=0.5)
        self.wait(1)
        self.ly.clear()

        # Formal statement
        title2 = self.ly.title("Formal Statement")

        informal = Text(
            "n+1 pigeons in n holes → at least one hole has ≥ 2 pigeons",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(informal, direction=DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(informal, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        formal = MathTex(
            r"|A| > |B| \implies \text{ no injection } f: A \to B",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(formal, direction=DOWN, anchor=informal, buff=0.5)
        self.play(Write(formal), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Simple Examples (1:30)
    # ------------------------------------------------------------------
    def scene3_simple_examples(self):
        self.add_subcaption(
            "Let's start with easy examples. "
            "In a group of 367 people, at least two share a birthday. "
            "There are at most 366 possible birthdays, including leap year. "
            "With 367 people, the pigeonhole principle forces a collision. "
            "Socks: you have 6 black socks and 6 blue socks in a drawer. "
            "Pull out 3 socks. With only 2 colors, "
            "the third sock must match one of the first two. "
            "In any group of 13 people, at least two were born in the same month. "
            "Twelve months, thirteen people. Collision forced.",
            duration=28,
        )
        self.ly.section_divider(2, "Simple Examples")

        # Example 1: Birthdays
        title = self.ly.title("Birthdays")

        bday = Text(
            "367 people, at most 366 birthdays",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(bday, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(bday, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        result1 = MathTex(
            r"367 > 366 \implies \text{ shared birthday guaranteed}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(result1, direction=DOWN, anchor=bday, buff=0.5)
        self.play(Write(result1), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Example 2: Socks
        title2 = self.ly.title("Socks in a Drawer")

        sock_prob = Text(
            "Drawer: 6 black + 6 blue. How many pulls for a pair?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(sock_prob, direction=DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(sock_prob, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        sock_ans = MathTex(
            r"2 \text{ colors} \implies 3 \text{ pulls guarantee a match}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(sock_ans, direction=DOWN, anchor=sock_prob, buff=0.5)
        self.play(Write(sock_ans), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Example 3: Months
        title3 = self.ly.title("Same Birth Month")

        month = Text(
            "13 people, 12 months",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(month, direction=DOWN, anchor=title3, buff=0.5)
        self.play(FadeIn(month, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        month_result = MathTex(
            r"13 > 12 \implies \text{ same month guaranteed}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(month_result, direction=DOWN, anchor=month, buff=0.5)
        self.play(Write(month_result), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Proof via Contradiction (1:00)
    # ------------------------------------------------------------------
    def scene4_proof(self):
        self.add_subcaption(
            "Why does the pigeonhole principle work? "
            "Proof by contradiction. "
            "Suppose every hole has at most one pigeon. "
            "Then the total number of pigeons is at most "
            "the number of holes. "
            "But we started with n plus 1 pigeons in n holes. "
            "This is a contradiction. "
            "The only way to avoid two pigeons in one hole is impossible. "
            "Therefore, at least one hole must contain at least two pigeons.",
            duration=24,
        )
        self.ly.section_divider(3, "Proof by Contradiction")

        title = self.ly.title("Assume the Opposite")

        assume = Text(
            "Suppose every hole has at most 1 pigeon.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(assume, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(assume, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        derive = MathTex(
            r"\text{Total pigeons } \leq \text{ number of holes}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(derive, direction=DOWN, anchor=assume, buff=0.5)
        self.play(Write(derive), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # The contradiction
        title2 = self.ly.title("Contradiction!")

        contradiction = MathTex(
            r"n + 1 \text{ pigeons } \not\leq n \text{ holes}",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.center_in_content(contradiction)
        box = SurroundingRectangle(contradiction, color=RED, buff=0.25,
                                   stroke_width=2, corner_radius=0.1)
        self.play(Write(contradiction), run_time=NORMAL)
        self.play(Create(box), run_time=0.5)
        self.wait(0.8)

        conclude = Text(
            "The assumption is false. Some hole has ≥ 2 pigeons.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(conclude, direction=DOWN, anchor=box, buff=0.5)
        self.play(FadeIn(conclude, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Generalized Pigeonhole Principle (1:30)
    # ------------------------------------------------------------------
    def scene5_generalized(self):
        self.add_subcaption(
            "The pigeonhole principle generalizes. "
            "If you put n pigeons into k holes, "
            "then at least one hole has at least the ceiling of n over k pigeons. "
            "This is stronger than the basic version. "
            "It tells you not just that a collision exists, "
            "but how many items must pile up. "
            "Example: 17 socks in 3 colors. "
            "Ceiling of 17 over 3 equals 6. "
            "So at least 6 socks must be the same color.",
            duration=24,
        )
        self.ly.section_divider(4, "Generalized PHP")

        title = self.ly.title("The Generalized Principle")

        formula = MathTex(
            r"n \text{ pigeons, } k \text{ holes } \implies "
            r"\text{ some hole has } \geq \lceil n/k \rceil \text{ pigeons}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(formula)
        box = SurroundingRectangle(formula, color=PRIMARY, buff=0.25,
                                   stroke_width=2, corner_radius=0.1)
        self.play(Write(formula), run_time=NORMAL)
        self.play(Create(box), run_time=0.5)
        self.wait(1)
        self.ly.clear()

        # Visual: distribute evenly
        title2 = self.ly.title("Even Distribution Falls Short")

        explain = Text(
            "If every hole had fewer than ⌈n/k⌉ pigeons,",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(explain, direction=DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(explain, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        impossible = MathTex(
            r"\text{total} \leq k \cdot \lceil n/k \rceil - 1 < n \quad \Rightarrow \!\!\Leftarrow",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(impossible, direction=DOWN, anchor=explain, buff=0.5)
        self.play(Write(impossible), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Worked example
        title3 = self.ly.title("Example: Socks")

        sock_ex = Text(
            "17 socks, 3 colors. How many of one color?",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(sock_ex, direction=DOWN, anchor=title3, buff=0.5)
        self.play(FadeIn(sock_ex, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        sock_ans = MathTex(
            r"\lceil 17 / 3 \rceil = \lceil 5.67 \rceil = 6",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(sock_ans, direction=DOWN, anchor=sock_ex, buff=0.5)
        self.play(Write(sock_ans), run_time=NORMAL)
        self.wait(1)

        sock_conclude = Text(
            "At least 6 socks must be the same color!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(sock_conclude, direction=DOWN, anchor=sock_ans, buff=0.4)
        self.play(FadeIn(sock_conclude, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Application -- Recurring Decimals (1:30)
    # ------------------------------------------------------------------
    def scene6_recurring_decimals(self):
        self.add_subcaption(
            "Why does one seventh have a recurring decimal? "
            "When you compute 1 over 7 by long division, "
            "the remainder at each step is between 1 and 6. "
            "There are only 6 possible non-zero remainders. "
            "After 7 steps, the pigeonhole principle guarantees "
            "that some remainder repeats. "
            "When a remainder repeats, the decimal starts cycling. "
            "This is why every rational number has a recurring "
            "or terminating decimal expansion.",
            duration=26,
        )
        self.ly.section_divider(5, "Application: Recurring Decimals")

        title = self.ly.title("Why Does 1/7 Repeat?")

        setup = Text(
            "Long division of 1/7: remainders cycle through 1..6",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(setup, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(setup, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Show the long division result
        division = MathTex(
            r"\frac{1}{7} = 0.\overline{142857}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(division, direction=DOWN, anchor=setup, buff=0.5)
        self.play(Write(division), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # PHP argument
        title2 = self.ly.title("The Pigeonhole Argument")

        arg1 = Text(
            "At each step, the remainder is in {1, 2, 3, 4, 5, 6}",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(arg1, direction=DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(arg1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        arg2 = Text(
            "Only 6 possible remainders, but 7 division steps",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(arg2, direction=DOWN, anchor=arg1, buff=0.4)
        self.play(FadeIn(arg2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        arg3 = MathTex(
            r"7 > 6 \implies \text{ a remainder repeats } \implies \text{ cycle!}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(arg3, direction=DOWN, anchor=arg2, buff=0.5)
        self.play(Write(arg3), run_time=NORMAL)
        self.wait(1)

        general = Text(
            "Every rational number has a recurring or terminating decimal.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(general, direction=DOWN, anchor=arg3, buff=0.5)
        self.play(FadeIn(general, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Application -- Party Handshakes / Friends (1:00)
    # ------------------------------------------------------------------
    def scene7_party_friends(self):
        self.add_subcaption(
            "Here is a classic application in graph theory. "
            "At any party with n people, where n is at least 2, "
            "there are always at least two people with the same "
            "number of friends at the party. "
            "The possible friend counts are 0 through n minus 1. "
            "But if someone has 0 friends, nobody has n minus 1. "
            "And if someone has n minus 1 friends, nobody has 0. "
            "So there are at most n minus 1 distinct friend counts "
            "for n people. "
            "By the pigeonhole principle, two people share the same count.",
            duration=28,
        )
        self.ly.section_divider(6, "Application: Party Friends")

        title = self.ly.title("Same Number of Friends")

        statement = Text(
            "At a party of n ≥ 2 people, at least two have\nthe same number of friends present.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(statement, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(statement, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Argument
        title2 = self.ly.title("The Argument")

        counts = Text(
            "Possible friend counts: 0, 1, 2, ..., n-1 (n values)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(counts, direction=DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(counts, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        key_insight = Text(
            "0 friends ⇔ nobody knows everyone",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(key_insight, direction=DOWN, anchor=counts, buff=0.4)
        self.play(FadeIn(key_insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        key_insight2 = Text(
            "n-1 friends ⇔ everybody is known (no 0-friend person)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(key_insight2, direction=DOWN, anchor=key_insight, buff=0.4)
        self.play(FadeIn(key_insight2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # Conclusion
        title3 = self.ly.title("Pigeonhole Forces a Match")

        conclusion = MathTex(
            r"\text{At most } n{-}1 \text{ distinct counts for } n \text{ people}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(conclusion, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(conclusion), run_time=NORMAL)
        self.wait(0.8)

        final = Text(
            "Two people must have the same friend count!",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(final, direction=DOWN, anchor=conclusion, buff=0.5)
        self.play(FadeIn(final, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Application -- Sequences and Subsequences (1:00)
    # ------------------------------------------------------------------
    def scene8_subsequences(self):
        self.add_subcaption(
            "Our final application is the Erdos-Szekeres theorem. "
            "Any sequence of n squared plus 1 distinct real numbers "
            "contains either an increasing subsequence of length n plus 1 "
            "or a decreasing subsequence of length n plus 1. "
            "For each position in the sequence, define a pair. "
            "The first number is the length of the longest increasing "
            "subsequence ending at that position. "
            "The second is the length of the longest decreasing one. "
            "Both range from 1 to n. "
            "So there are at most n squared possible pairs. "
            "With n squared plus 1 positions, the pigeonhole principle "
            "forces two positions to share the same pair. "
            "But distinct numbers can't share the same longest subsequence lengths. "
            "This contradiction proves the theorem.",
            duration=32,
        )
        self.ly.section_divider(7, "Application: Erdos-Szekeres Theorem")

        title = self.ly.title("Monotone Subsequences")

        theorem = Text(
            "Any sequence of n²+1 distinct reals contains\n"
            "an increasing or decreasing subsequence of length n+1",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(theorem, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(theorem, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)
        self.ly.clear()

        # Pigeon labeling
        title2 = self.ly.title("Label Each Position")

        label1 = Text(
            "Position i → (inc_i, dec_i) where:",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(label1, direction=DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(label1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        label2 = Text(
            "inc_i = longest increasing subsequence ending at i",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(label2, direction=DOWN, anchor=label1, buff=0.3)
        self.play(FadeIn(label2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        label3 = Text(
            "dec_i = longest decreasing subsequence ending at i",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(label3, direction=DOWN, anchor=label2, buff=0.3)
        self.play(FadeIn(label3, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # PHP argument
        title3 = self.ly.title("Pigeonhole Argument")

        step1 = MathTex(
            r"1 \leq \text{inc}_i \leq n, \quad 1 \leq \text{dec}_i \leq n",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.8)

        step2 = MathTex(
            r"\text{At most } n^2 \text{ distinct pairs}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.4)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.8)

        step3 = MathTex(
            r"n^2 + 1 > n^2 \implies \text{ two positions share a pair}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(step3, direction=DOWN, anchor=step2, buff=0.4)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(1)

        finish = Text(
            "But distinct numbers can't share the same pair!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(finish, direction=DOWN, anchor=step3, buff=0.4)
        self.play(FadeIn(finish, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Summary of Power (0:30)
    # ------------------------------------------------------------------
    def scene9_power_summary(self):
        self.add_subcaption(
            "What does the pigeonhole principle give us? "
            "Certainty from quantity alone. "
            "The generalized form: n items in k holes means "
            "at least ceiling of n over k per hole. "
            "Applications across number theory, graph theory, and sequences. "
            "Next up: graph theory, where connections matter "
            "and the pigeonhole principle returns.",
            duration=20,
        )
        self.ly.section_divider(8, "The Power of PHP")

        title = self.ly.title("What PHP Gives Us")

        items = [
            Text(
                "Certainty from quantity alone",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Generalized: n items in k holes → ≥ ⌈n/k⌉ per hole",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Applications: number theory, graph theory, combinatorics",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1.5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Summary + Outro (0:30)
    # ------------------------------------------------------------------
    def scene10_outro(self):
        self.add_subcaption(
            "Let's recap the pigeonhole principle. "
            "The basic principle: n plus 1 pigeons in n holes forces a collision. "
            "The generalized form: n items in k holes forces "
            "at least ceiling of n over k in one hole. "
            "Proof by contradiction: assume uniformity, derive impossibility. "
            "Applications span recurring decimals, party friend counts, "
            "and the Erdos-Szekeres theorem on monotone subsequences. "
            "Next up: Graph Theory Basics.",
            duration=24,
        )
        title = self.ly.title("Summary")

        items = [
            Text(
                "PHP: n+1 in n holes → collision forced",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Generalized: ≥ ⌈n/k⌉ per hole guaranteed",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Proof: contradiction — can't avoid two in one hole",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Apps: birthdays, recurring decimals, friends, subsequences",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        play_outro(self, "Graph Theory Basics", "Discrete Mathematics")
        self.ly.clear()
