"""Video 67: Probability Spaces
Probability & Statistics -- Video 1 of 12

Covers: sample spaces (Omega), events as subsets, Kolmogorov axioms,
complement rule, worked dice example.

Competitive analysis: channel-analysis/improvements.md "2026-06-14 -- Probability Spaces"
Plan: planning/video-67-probability-spaces.md

Render draft:  manim -ql scripts/undergraduate/video-67-probability-spaces.py Video67_ProbabilitySpaces
Render final:  manim -qh scripts/undergraduate/video-67-probability-spaces.py Video67_ProbabilitySpaces
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


class Video67_ProbabilitySpaces(Scene):
    """Full video: Probability Spaces -- foundations of probability theory."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_sample_spaces()
        self.scene3_events()
        self.scene4_probability_function()
        self.scene5_kolmogorov_axioms()
        self.scene6_consequences()
        self.scene7_worked_example()
        self.scene8_summary()

    # -- Scene 1: Hook -- The Coin Puzzle --
    def scene1_hook(self):
        self.add_subcaption(
            "Flip a fair coin ten times. What is the probability "
            "of getting at least one head? Most people try to count "
            "the favorable outcomes. But there is a much easier way.",
            duration=18,
        )
        play_intro(self, "Probability Spaces",
                   "Probability & Statistics")

        title = self.ly.title("The Coin Puzzle")
        self.wait(2)

        self.add_subcaption(
            "There are two to the power of ten, or 1024 possible "
            "outcomes. Counting the ones with at least one head "
            "is tedious. But what if we count the opposite instead?",
            duration=16,
        )

        question = MathTex(
            r"P(\text{at least one } H \text{ in 10 flips}) = \; ?",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(question, DOWN, anchor=title, buff=0.5)
        self.play(Write(question), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "It is easier to find the probability of NO heads. "
            "There is exactly one outcome with all tails. "
            "So we subtract from one.",
            duration=16,
        )

        insight = Text(
            "Count the complement instead!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, DOWN, anchor=question, buff=0.3)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        result = MathTex(
            r"1 - P(\text{all } T) = 1 - \left(\frac{1}{2}\right)^{10} "
            r"\approx 0.999",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(result, DOWN, anchor=insight, buff=0.3)
        self.play(Write(result), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "Almost certain! To understand why this complement "
            "trick works, we need a proper framework. That "
            "framework is a probability space.",
            duration=14,
        )

        bridge = Text(
            "To see why this works, we need a framework.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(bridge, DOWN, anchor=result, buff=0.3)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=FAST)
        self.wait(3)

        self.ly.clear()

    # -- Scene 2: Sample Spaces --
    def scene2_sample_spaces(self):
        self.ly.section_divider(1, "Sample Spaces")

        self.add_subcaption(
            "Every probability question starts with a sample space. "
            "The sample space Omega is the set of all possible "
            "outcomes of an experiment.",
            duration=16,
        )

        title = self.ly.title("Sample Space: Omega")

        definition = MathTex(
            r"\Omega = \text{ set of all outcomes}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(definition, DOWN, anchor=title, buff=0.5)
        self.play(Write(definition), run_time=NORMAL)
        self.wait(4)

        self.add_subcaption(
            "For a coin flip, the sample space has two outcomes. "
            "For a die roll, it has six. The sample space depends "
            "on how we define the experiment.",
            duration=14,
        )

        # Two examples side by side
        coin_label = Text(
            "Coin:", font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        coin_omega = MathTex(
            r"\Omega = \{H, T\}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        coin_group = VGroup(coin_label, coin_omega).arrange(RIGHT, buff=0.3)

        die_label = Text(
            "Die:", font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        die_omega = MathTex(
            r"\Omega = \{1, 2, 3, 4, 5, 6\}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        die_group = VGroup(die_label, die_omega).arrange(RIGHT, buff=0.3)

        examples = VGroup(coin_group, die_group).arrange(DOWN, buff=0.4)
        self.ly.safe_place(examples, DOWN, anchor=definition, buff=0.4)

        self.play(
            FadeIn(coin_group, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(2)
        self.play(
            FadeIn(die_group, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(4)

        self.add_subcaption(
            "Notice the sample space is not unique. If we flip "
            "two coins, we might write Omega as ordered pairs, "
            "or we might just count the number of heads.",
            duration=16,
        )

        note = Text(
            "The sample space depends on how we frame the question",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=examples, buff=0.3)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # -- Scene 3: Events --
    def scene3_events(self):
        self.ly.section_divider(2, "Events")

        self.add_subcaption(
            "An event is any subset of the sample space. It is a "
            "collection of outcomes that we want to assign a "
            "probability to.",
            duration=16,
        )

        title = self.ly.title("Events: Subsets of Omega")

        definition = MathTex(
            r"A \subseteq \Omega",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(definition, DOWN, anchor=title, buff=0.5)
        self.play(Write(definition), run_time=NORMAL)
        self.wait(3)

        # Visual: Omega rectangle with event A shaded
        omega_rect = RoundedRectangle(
            corner_radius=0.1, width=3.5, height=2.5,
            stroke_color=PRIMARY, stroke_width=2, fill_opacity=0,
        )
        omega_label = MathTex(
            r"\Omega", font_size=HEADING_SIZE, color=PRIMARY,
        ).next_to(omega_rect, LEFT, buff=0.15)

        # Event A as a circle inside Omega
        event_a = Circle(
            radius=0.8, fill_color=SECONDARY, fill_opacity=0.4,
            stroke_color=SECONDARY, stroke_width=2,
        ).move_to(omega_rect.get_center() + RIGHT * 0.2 + UP * 0.15)
        a_label = MathTex(
            r"A", font_size=HEADING_SIZE, color=SECONDARY,
        ).move_to(event_a.get_center())

        venn_group = VGroup(omega_label, omega_rect, event_a, a_label)
        self.ly.center_in_content(venn_group)

        self.add_subcaption(
            "We draw Omega as a rectangle and shade the event A "
            "inside it. Any collection of outcomes can be an event.",
            duration=12,
        )

        self.play(
            Create(omega_rect),
            FadeIn(omega_label),
            run_time=NORMAL,
        )
        self.play(
            Create(event_a),
            FadeIn(a_label),
            run_time=NORMAL,
        )
        self.wait(4)

        self.ly.clear()

        # Special events sub-scene
        self.add_subcaption(
            "Two special events. Omega itself is the certain "
            "event, with probability one. The empty set is the "
            "impossible event, with probability zero.",
            duration=16,
        )

        title2 = self.ly.title("Special Events")

        items = [
            Text(
                "Omega = certain event: P(Omega) = 1",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "empty set = impossible event: P(empty) = 0",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Complement: A^c = Omega \\ A",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title2)
        self.wait(5)

        self.add_subcaption(
            "The complement of an event is everything in Omega "
            "that is not in A. This is exactly what we used "
            "in the coin puzzle.",
            duration=14,
        )

        self.ly.clear()

    # -- Scene 4: The Probability Function --
    def scene4_probability_function(self):
        self.ly.section_divider(3, "The Probability Function")

        self.add_subcaption(
            "A probability function P assigns a number between "
            "zero and one to every event. One means certain, "
            "zero means impossible.",
            duration=16,
        )

        title = self.ly.title("The Probability Function P")

        # The triple (Omega, F, P)
        triple = MathTex(
            r"(\Omega, \, \mathcal{F}, \, P)",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        triple_box = self.ly.formula_box(triple, color=ACCENT)
        self.ly.safe_place(triple_box, DOWN, anchor=title, buff=0.4)

        self.play(Write(triple_box), run_time=SLOW)
        self.wait(3)

        self.add_subcaption(
            "Omega is the sample space, script F is the collection "
            "of events, and P is the function that assigns "
            "probabilities to events.",
            duration=14,
        )

        items = [
            Text(
                "Omega = sample space (outcomes)",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "script F = collection of events (subsets)",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "P = probability function: events to [0, 1]",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=triple_box)
        self.wait(5)

        self.ly.clear()

        # Equally-likely outcomes
        self.add_subcaption(
            "When all outcomes are equally likely, probability "
            "reduces to simple counting. P of A equals the "
            "number of outcomes in A divided by the total.",
            duration=14,
        )

        title2 = self.ly.title("Equally-Likely Outcomes")

        eq_likely = MathTex(
            r"P(A) = \frac{|A|}{|\Omega|}",
            font_size=TITLE_SIZE, color=WHITE,
        )
        eq_box = self.ly.formula_box(eq_likely, color=PRIMARY)
        self.ly.safe_place(eq_box, DOWN, anchor=title2, buff=0.5)

        self.play(Write(eq_box), run_time=SLOW)
        self.wait(3)

        self.add_subcaption(
            "For a fair die, the probability of rolling an even "
            "number is three divided by six, or one half. This "
            "connects probability directly to counting.",
            duration=14,
        )

        die_example = MathTex(
            r"P(\text{even}) = \frac{|\{2,4,6\}|}{|\{1,2,3,4,5,6\}|} = \frac{3}{6} = \frac{1}{2}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(die_example, DOWN, anchor=eq_box, buff=0.4)
        self.play(Write(die_example), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # -- Scene 5: Kolmogorov Axioms --
    def scene5_kolmogorov_axioms(self):
        self.ly.section_divider(4, "Kolmogorov Axioms")

        self.add_subcaption(
            "In 1933, Andrey Kolmogorov established three axioms "
            "that define probability. Every rule of probability "
            "follows from these three simple statements.",
            duration=16,
        )

        title = self.ly.title("The Three Axioms of Probability")

        # Axiom 1
        self.add_subcaption(
            "Axiom one: probability is always non-negative. "
            "You can never have a negative probability.",
            duration=12,
        )

        ax1 = MathTex(
            r"\text{Axiom 1: } P(A) \geq 0 \quad \forall\, A \in \mathcal{F}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        ax1_box = self.ly.formula_box(ax1, color=ACCENT)
        self.ly.safe_place(ax1_box, DOWN, anchor=title, buff=0.4)
        self.play(Write(ax1_box), run_time=SLOW)
        self.wait(4)

        self.ly.clear()

        # Axiom 2
        self.add_subcaption(
            "Axiom two: the probability of the entire sample "
            "space is one. Something must happen.",
            duration=12,
        )

        title2 = self.ly.title("The Three Axioms")

        ax2 = MathTex(
            r"\text{Axiom 2: } P(\Omega) = 1",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        ax2_box = self.ly.formula_box(ax2, color=ACCENT)
        self.ly.safe_place(ax2_box, DOWN, anchor=title2, buff=0.4)
        self.play(Write(ax2_box), run_time=SLOW)
        self.wait(4)

        self.ly.clear()

        # Axiom 3
        self.add_subcaption(
            "Axiom three: if two events are disjoint, the "
            "probability of their union is the sum of their "
            "probabilities.",
            duration=14,
        )

        title3 = self.ly.title("The Three Axioms")

        ax3 = MathTex(
            r"\text{Axiom 3: } A \cap B = \emptyset \implies "
            r"P(A \cup B) = P(A) + P(B)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        ax3_box = self.ly.formula_box(ax3, color=ACCENT)
        self.ly.safe_place(ax3_box, DOWN, anchor=title3, buff=0.4)
        self.play(Write(ax3_box), run_time=SLOW)
        self.wait(3)

        self.add_subcaption(
            "Visually, if two regions do not overlap, their "
            "combined area is just the sum of their individual "
            "areas. This is the additivity of probability.",
            duration=14,
        )

        # Visual: two non-overlapping circles inside Omega
        omega_rect = RoundedRectangle(
            corner_radius=0.1, width=3.0, height=1.8,
            stroke_color=PRIMARY, stroke_width=2, fill_opacity=0,
        )
        omega_lbl = MathTex(
            r"\Omega", font_size=LABEL_SIZE, color=PRIMARY,
        ).next_to(omega_rect, LEFT, buff=0.1)

        event_a = Circle(
            radius=0.5, fill_color=SECONDARY, fill_opacity=0.4,
            stroke_color=SECONDARY, stroke_width=1.5,
        ).move_to(omega_rect.get_center() + LEFT * 0.6)
        a_lbl = MathTex(
            r"A", font_size=BODY_SIZE, color=SECONDARY,
        ).move_to(event_a.get_center())

        event_b = Circle(
            radius=0.5, fill_color=PRIMARY, fill_opacity=0.4,
            stroke_color=PRIMARY, stroke_width=1.5,
        ).move_to(omega_rect.get_center() + RIGHT * 0.6)
        b_lbl = MathTex(
            r"B", font_size=BODY_SIZE, color=PRIMARY,
        ).move_to(event_b.get_center())

        venn = VGroup(omega_lbl, omega_rect, event_a, a_lbl, event_b, b_lbl)
        self.ly.safe_place(venn, DOWN, anchor=ax3_box, buff=0.3)

        self.play(
            Create(omega_rect), FadeIn(omega_lbl),
            Create(event_a), FadeIn(a_lbl),
            run_time=NORMAL,
        )
        self.play(
            Create(event_b), FadeIn(b_lbl),
            run_time=NORMAL,
        )
        self.wait(3)

        self.ly.clear()

        # All three axioms summary
        self.add_subcaption(
            "These three rules are the entire foundation of "
            "probability theory. From these axioms alone, "
            "we can derive every other probability law.",
            duration=14,
        )

        title4 = self.ly.title("The Foundation")

        foundation = Text(
            "Three axioms define all of probability theory",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
            weight=BOLD,
        )
        self.ly.center_in_content(foundation)
        self.play(Write(foundation), run_time=SLOW)
        self.wait(5)

        self.ly.clear()

    # -- Scene 6: Consequences --
    def scene6_consequences(self):
        self.ly.section_divider(5, "Consequences from the Axioms")

        self.add_subcaption(
            "From just three axioms, we can prove powerful "
            "results. Let us start with a simple one: "
            "the probability of the empty set is zero.",
            duration=16,
        )

        title = self.ly.title("Consequences of the Axioms")

        # Consequence 1: P(empty) = 0
        self.add_subcaption(
            "Proof. Let A be any event. Since A union empty "
            "equals A, by Axiom three we have P of A equals "
            "P of A plus P of empty. Subtract P of A from "
            "both sides to get P of empty equals zero.",
            duration=18,
        )

        c1_title = Text(
            "1. P(empty set) = 0",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            weight=BOLD,
        )
        self.ly.safe_place(c1_title, DOWN, anchor=title, buff=0.4)

        c1_proof = MathTex(
            r"A \cup \emptyset = A \implies "
            r"P(A) = P(A) + P(\emptyset) \implies "
            r"P(\emptyset) = 0",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(c1_proof, DOWN, anchor=c1_title, buff=0.3)
        self.play(
            FadeIn(c1_title, shift=LEFT * 0.15),
            run_time=FAST,
        )
        self.play(Write(c1_proof), run_time=SLOW)
        self.wait(5)

        self.ly.clear()

        # Consequence 2: Complement rule
        self.add_subcaption(
            "Now the big one: the complement rule. An event "
            "and its complement are disjoint and together "
            "cover Omega. So their probabilities sum to one.",
            duration=18,
        )

        title2 = self.ly.title("The Complement Rule")

        c2_title = Text(
            "2. P(A^c) = 1 - P(A)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
            weight=BOLD,
        )
        self.ly.safe_place(c2_title, DOWN, anchor=title2, buff=0.4)

        c2_proof = MathTex(
            r"A \cup A^c = \Omega, \quad A \cap A^c = \emptyset",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(c2_proof, DOWN, anchor=c2_title, buff=0.3)
        self.play(
            FadeIn(c2_title, shift=LEFT * 0.15),
            run_time=FAST,
        )
        self.play(Write(c2_proof), run_time=NORMAL)
        self.wait(3)

        c2_result = MathTex(
            r"\implies P(A) + P(A^c) = P(\Omega) = 1",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(c2_result, DOWN, anchor=c2_proof, buff=0.3)
        self.play(Write(c2_result), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Connect back to hook
        self.add_subcaption(
            "This is exactly what we used in the coin puzzle! "
            "The probability of at least one head equals one "
            "minus the probability of all tails.",
            duration=14,
        )

        title3 = self.ly.title("Back to the Coin Puzzle")

        coin_puzzle = MathTex(
            r"P(\text{at least one } H) = 1 - P(\text{all } T) "
            r"= 1 - \left(\frac{1}{2}\right)^{10}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.center_in_content(coin_puzzle)
        self.play(Write(coin_puzzle), run_time=SLOW)
        self.wait(5)

        self.ly.clear()

    # -- Scene 7: Worked Example -- Rolling Dice --
    def scene7_worked_example(self):
        self.ly.section_divider(6, "Worked Example")

        self.add_subcaption(
            "Let us put it all together. Roll two six-sided "
            "dice. What is the probability that the sum "
            "of the two dice is seven?",
            duration=16,
        )

        title = self.ly.title("Two Dice: Sum of 7")

        self.add_subcaption(
            "First, define the sample space. Each die can "
            "land on one through six, so there are 36 equally "
            "likely outcomes. We can show them as a grid.",
            duration=16,
        )

        # 6x6 grid
        grid_cells = []
        winning_cells = []
        winning_pairs = [
            (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1),
        ]
        for i in range(1, 7):
            row = []
            for j in range(1, 7):
                is_winner = (i, j) in winning_pairs
                cell = RoundedRectangle(
                    corner_radius=0.05, width=0.45, height=0.45,
                    stroke_color=DIM if not is_winner else SECONDARY,
                    stroke_width=1,
                    fill_color=SECONDARY if is_winner else BG,
                    fill_opacity=0.5 if is_winner else 0.3,
                )
                cell_text = MathTex(
                    str(i + j),
                    font_size=SMALL_SIZE,
                    color=WHITE if not is_winner else WHITE,
                ).move_to(cell.get_center())
                cell_group = VGroup(cell, cell_text)
                row.append(cell_group)
                if is_winner:
                    winning_cells.append(cell_group)
            grid_cells.append(row)

        grid = VGroup()
        for r_idx, row in enumerate(grid_cells):
            for c_idx, cell in enumerate(row):
                cell.move_to(
                    np.array([
                        (c_idx - 2.5) * 0.55,
                        -(r_idx - 2.5) * 0.55,
                        0,
                    ])
                )
                grid.add(cell)

        # Labels
        x_label = Text(
            "Die 1", font_size=SMALL_SIZE, color=DIM, font=MONO,
        )
        x_label.next_to(grid, RIGHT, buff=0.2).shift(UP * 0.5)
        y_label = Text(
            "Die 2", font_size=SMALL_SIZE, color=DIM, font=MONO,
        )
        y_label.next_to(grid, UP, buff=0.2).shift(RIGHT * 0.5)

        grid_group = VGroup(grid, x_label, y_label)
        self.ly.center_in_content(grid_group)

        self.play(Create(grid), run_time=SLOW)
        self.play(
            FadeIn(x_label), FadeIn(y_label),
            run_time=FAST,
        )
        self.wait(3)

        # Highlight winning cells
        self.add_subcaption(
            "The event is sum equals seven. There are six "
            "winning outcomes highlighted in green: "
            "one and six, two and five, three and four, "
            "and so on. The probability is six over 36.",
            duration=18,
        )

        for cell in winning_cells:
            cell[0].set_stroke_color(SECONDARY)
            cell[0].set_fill_color(SECONDARY)
            cell[0].set_fill_opacity(0.6)

        self.play(
            *[cell.animate for cell in winning_cells],
            run_time=NORMAL,
        )
        self.wait(4)

        self.ly.clear()

        # Result
        self.add_subcaption(
            "So the probability of rolling a sum of seven "
            "is six out of 36, which simplifies to one sixth. "
            "And by the complement rule, the probability of "
            "NOT getting a sum of seven is five sixths.",
            duration=18,
        )

        title2 = self.ly.title("Result")

        p_sum7 = MathTex(
            r"P(\text{sum} = 7) = \frac{6}{36} = \frac{1}{6}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(p_sum7, DOWN, anchor=title2, buff=0.5)
        self.play(Write(p_sum7), run_time=SLOW)
        self.wait(3)

        p_comp = MathTex(
            r"P(\text{sum} \neq 7) = 1 - \frac{1}{6} = \frac{5}{6}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(p_comp, DOWN, anchor=p_sum7, buff=0.3)
        self.play(Write(p_comp), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # -- Scene 8: Summary --
    def scene8_summary(self):
        self.add_subcaption(
            "Probability spaces give us a rigorous framework "
            "for reasoning about uncertainty. Let us review "
            "what we learned.",
            duration=14,
        )

        play_outro(self, "Conditional Probability", "Probability & Statistics")

        title = self.ly.title("Key Takeaways")

        items = [
            Text(
                "Sample space Omega = all possible outcomes",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Events = subsets of Omega",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "P maps events to [0, 1]",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
            Text(
                "Three axioms: non-negativity, normalization, additivity",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "Everything else follows from the axioms",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)

        self.ly.clear()
