"""Video 113: Permutation Groups
TEMPLATE v2 -- Professional quality Manim script

Playlist: Abstract Algebra I (Video 3 of 12)
Class: Video113_PermutationGroups
"""

from manim import *
import numpy as np
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


class Video113_PermutationGroups(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_two_line_notation()
        self.scene4_cycle_notation()
        self.scene5_composition()
        self.scene6_transpositions()
        self.scene7_parity()
        self.scene8_alternating_summary()

    # --- Scene 1: Hook ---

    def scene1_hook(self):
        self.add_subcaption(
            "Imagine four objects in a row. "
            "A red one, a blue one, a green one, and a yellow one. "
            "Now shuffle them. "
            "Red goes to the second position, blue to the fourth, "
            "green stays where it is, yellow moves to the first. "
            "How many ways can you rearrange four objects? "
            "The answer is four factorial, which is twenty four. "
            "But these rearrangements are not just a set of twenty four things. "
            "They have structure. "
            "You can compose two shuffles to get a third. "
            "Every shuffle has an inverse shuffle that undoes it. "
            "These rearrangements form a group. "
            "Today we study permutation groups, "
            "one of the most important families of groups in all of mathematics.",
            duration=25,
        )
        play_intro(self, "Permutation Groups", "Abstract Algebra I")

        title = self.ly.title("The Shuffling Problem")

        # Four colored dots in a row
        dot_colors = [RED, PRIMARY, SECONDARY, ACCENT]
        dot_labels = ["R", "B", "G", "Y"]
        positions = [LEFT * 3 + DOWN * 1.2, LEFT * 1 + DOWN * 1.2,
                     RIGHT * 1 + DOWN * 1.2, RIGHT * 3 + DOWN * 1.2]

        dots = VGroup()
        labels = VGroup()
        for i, (col, lbl, pos) in enumerate(zip(dot_colors, dot_labels, positions)):
            d = Dot(pos, color=col, radius=0.22)
            t = Text(lbl, font_size=LABEL_SIZE, color=WHITE, font=MONO)
            t.move_to(pos)
            dots.add(d)
            labels.add(t)

        self.play(*[Create(d) for d in dots], run_time=NORMAL)
        self.play(*[Write(t) for t in labels], run_time=FAST)
        self.wait(0.3)

        # Animate a shuffle: move dots to new positions
        # New arrangement: Y, R, G, B (positions 0,1,2,3)
        new_order = [3, 0, 2, 1]
        anims = []
        for i, idx in enumerate(new_order):
            anims.append(dots[idx].animate.move_to(positions[i]))
            anims.append(labels[idx].animate.move_to(positions[i]))
        self.play(*anims, run_time=SLOW)
        self.wait(0.3)

        question = Text(
            "How many ways to rearrange 4 objects?",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(question, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(question), run_time=NORMAL)
        self.wait(0.2)

        answer = MathTex(
            r"|S_4| = 4! = 24",
            color=ACCENT, font_size=36,
        )
        self.ly.safe_place(answer, anchor=question, direction=DOWN, buff=0.4)
        self.play(Write(answer), run_time=NORMAL)
        self.wait(0.3)

        bridge = Text(
            "These rearrangements form a group!",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(bridge, anchor=answer, direction=DOWN, buff=0.4)
        self.play(FadeIn(bridge, scale=1.05), run_time=NORMAL)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 2: Definition of S_n ---

    def scene2_definition(self):
        self.add_subcaption(
            "The symmetric group on n elements, written S sub n, "
            "is the set of all bijections from the set 1 through n to itself. "
            "The operation is function composition. "
            "Since the composition of two bijections is a bijection, "
            "the set is closed. "
            "Function composition is always associative. "
            "The identity function is the identity element. "
            "And every bijection has an inverse bijection. "
            "So S sub n is indeed a group. "
            "The order of S sub n is n factorial. "
            "For example, S 3 has six elements, "
            "and S 4 has twenty four. "
            "S 3 is small enough that we can write down all six elements explicitly.",
            duration=25,
        )

        title = self.ly.title("The Symmetric Group S_n")

        defn = Text(
            "S_n = {bijections {1, 2, ..., n} -> {1, 2, ..., n}}",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(defn, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(0.2)

        op = Text(
            "Operation: function composition",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(op, anchor=defn, direction=DOWN, buff=0.35)
        self.play(FadeIn(op, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.2)

        order = MathTex(
            r"|S_n| = n!",
            color=ACCENT, font_size=36,
        )
        self.ly.safe_place(order, anchor=op, direction=DOWN, buff=0.4)
        self.play(Write(order), run_time=NORMAL)
        self.wait(0.2)

        # Group axioms check
        axioms = [
            MathTex(r"\checkmark\;\text{Closure}", color=SECONDARY, font_size=26),
            MathTex(r"\checkmark\;\text{Associativity}", color=SECONDARY, font_size=26),
            MathTex(r"\checkmark\;\text{Identity: } e(i) = i", color=SECONDARY, font_size=26),
            MathTex(r"\checkmark\;\text{Inverses exist}", color=SECONDARY, font_size=26),
        ]

        axioms_vg = VGroup(*axioms).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        self.ly.safe_place(axioms_vg, anchor=order, direction=DOWN, buff=0.4)
        for ax in axioms:
            self.play(Write(ax), run_time=FAST)
            self.wait(0.15)
        self.wait(0.3)

        self.ly.clear()

        # S_3 elements
        title2 = self.ly.title("S_3: The Six Permutations")

        s3_elements = VGroup(
            MathTex(r"e = \begin{pmatrix} 1 & 2 & 3 \\ 1 & 2 & 3 \end{pmatrix}",
                    color=WHITE, font_size=24),
            MathTex(r"\sigma_1 = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 3 \end{pmatrix}",
                    color=PRIMARY, font_size=24),
            MathTex(r"\sigma_2 = \begin{pmatrix} 1 & 2 & 3 \\ 3 & 2 & 1 \end{pmatrix}",
                    color=PRIMARY, font_size=24),
            MathTex(r"\sigma_3 = \begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 2 \end{pmatrix}",
                    color=SECONDARY, font_size=24),
            MathTex(r"\sigma_4 = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix}",
                    color=SECONDARY, font_size=24),
            MathTex(r"\sigma_5 = \begin{pmatrix} 1 & 2 & 3 \\ 3 & 1 & 2 \end{pmatrix}",
                    color=SECONDARY, font_size=24),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)

        self.ly.safe_place(s3_elements, anchor=title2, direction=DOWN, buff=0.4)
        self.play(Write(s3_elements), run_time=NORMAL)
        self.wait(0.3)

        note = Text(
            "|S_3| = 3! = 6 elements",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, anchor=s3_elements, direction=DOWN, buff=0.35)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 3: Two-Line Notation ---

    def scene3_two_line_notation(self):
        self.add_subcaption(
            "We need a way to write down permutations clearly. "
            "Two-line notation does exactly this. "
            "Write the numbers one through n on the top row. "
            "Write where each number goes on the bottom row. "
            "For example, sigma sends one to two, two to four, "
            "three to one, and four to three. "
            "The identity permutation has the same numbers on both rows. "
            "Two-line notation is clear but a bit bulky. "
            "In the next scene we will see a more compact notation "
            "called cycle notation, which is what mathematicians actually use. "
            "Two-line notation is the bridge that helps us understand "
            "how to read permutations before we switch to the compact form.",
            duration=25,
        )

        title = self.ly.title("Two-Line Notation")

        defn = Text(
            "Write elements on top, their images below:",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(defn, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(0.2)

        # Show a permutation in two-line notation
        perm = MathTex(
            r"\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 4 & 1 & 3 \end{pmatrix}",
            color=ACCENT, font_size=34,
        )
        self.ly.safe_place(perm, anchor=defn, direction=DOWN, buff=0.5)
        self.play(Write(perm), run_time=NORMAL)
        self.wait(0.2)

        reading = Text(
            "Read: 1 -> 2,  2 -> 4,  3 -> 1,  4 -> 3",
            font_size=BODY_SIZE, color=PRIMARY, font=MONO,
        )
        self.ly.safe_place(reading, anchor=perm, direction=DOWN, buff=0.35)
        self.play(FadeIn(reading, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        # Identity
        self.ly.clear()

        title2 = self.ly.title("Identity in Two-Line Notation")

        identity = MathTex(
            r"e = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 1 & 2 & 3 & 4 \end{pmatrix}",
            color=SECONDARY, font_size=34,
        )
        self.ly.safe_place(identity, anchor=title2, direction=DOWN, buff=0.5)
        self.play(Write(identity), run_time=NORMAL)
        self.wait(0.2)

        note = Text(
            "Every element maps to itself.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(note, anchor=identity, direction=DOWN, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        bridge = Text(
            "Next: a more compact notation...",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(bridge, anchor=note, direction=DOWN, buff=0.35)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 4: Cycle Notation ---

    def scene4_cycle_notation(self):
        self.add_subcaption(
            "Cycle notation is the standard way to write permutations. "
            "Instead of two rows, we track the movement of each element. "
            "Take our permutation sigma. "
            "One goes to two, two goes to four, four goes back to one. "
            "That forms a cycle: one, two, four. "
            "And three maps to itself, a trivial cycle. "
            "We write this as one, two, four in parentheses, "
            "and omit the one-cycle of three. "
            "Disjoint cycles commute, so their order does not matter. "
            "For example, one, two times three, four "
            "equals three, four times one, two. "
            "A permutation that is a single cycle covering all n elements "
            "is called an n-cycle. "
            "The identity is often written as just e.",
            duration=28,
        )

        title = self.ly.title("Cycle Notation")

        defn = Text(
            "Track where each element goes, forming cycles:",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(defn, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(0.2)

        # Show the permutation diagram with colored dots and arrows
        dot_positions = {
            1: LEFT * 3,
            2: LEFT * 1,
            3: RIGHT * 1,
            4: RIGHT * 3,
        }
        dot_colors_map = {1: RED, 2: PRIMARY, 3: SECONDARY, 4: ACCENT}

        dots = VGroup()
        dot_lbls = VGroup()
        for i in range(1, 5):
            d = Dot(dot_positions[i], color=dot_colors_map[i], radius=0.18)
            l = Text(str(i), font_size=LABEL_SIZE, color=WHITE, font=MONO)
            l.move_to(dot_positions[i])
            dots.add(d)
            labels.add(l) if i == 1 else None
        dot_lbls = VGroup()
        for i in range(1, 5):
            l = Text(str(i), font_size=LABEL_SIZE, color=WHITE, font=MONO)
            l.move_to(dot_positions[i])
            dot_lbls.add(l)

        self.ly.center_in_content(dots)
        self.play(*[Create(d) for d in dots], run_time=FAST)
        self.play(*[Write(l) for l in dot_lbls], run_time=FAST)
        self.wait(0.2)

        # Arrows: 1->2, 2->4, 4->1 (cycle), 3->3 (self-loop)
        arrows = VGroup()
        # 1 -> 2
        arr1 = Arrow(dot_positions[1] + RIGHT * 0.25, dot_positions[2] + LEFT * 0.25,
                     color=PRIMARY, stroke_width=2, buff=0.05, max_tip_length_to_length_ratio=0.15)
        # 2 -> 4
        arr2 = CurvedArrow(dot_positions[2] + RIGHT * 0.25, dot_positions[4] + LEFT * 0.25,
                            color=SECONDARY, stroke_width=2, angle=-TAU / 8)
        # 4 -> 1
        arr3 = CurvedArrow(dot_positions[4] + UP * 0.3, dot_positions[1] + UP * 0.3,
                            color=ACCENT, stroke_width=2, angle=-TAU / 6)
        arrows.add(arr1, arr2, arr3)

        self.play(Create(arr1), run_time=FAST)
        self.play(Create(arr2), run_time=FAST)
        self.play(Create(arr3), run_time=FAST)
        self.wait(0.3)

        # Show cycle notation
        cycle = MathTex(
            r"\sigma = (1\; 2\; 4)(3)",
            color=ACCENT, font_size=34,
        )
        self.ly.safe_place(cycle, anchor=dots, direction=DOWN, buff=0.5)
        self.play(Write(cycle), run_time=NORMAL)
        self.wait(0.2)

        explanation = Text(
            "1 -> 2 -> 4 -> 1,  and 3 stays fixed",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(explanation, anchor=cycle, direction=DOWN, buff=0.35)
        self.play(FadeIn(explanation, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        self.ly.clear()

        # Disjoint cycles
        title2 = self.ly.title("Disjoint Cycles")

        dc1 = MathTex(
            r"\sigma = (1\; 2)(3\; 4)",
            color=PRIMARY, font_size=34,
        )
        self.ly.safe_place(dc1, anchor=title2, direction=DOWN, buff=0.5)
        self.play(Write(dc1), run_time=NORMAL)
        self.wait(0.2)

        dc2 = Text(
            "Elements in different cycles don't interact.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(dc2, anchor=dc1, direction=DOWN, buff=0.35)
        self.play(FadeIn(dc2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.2)

        commute = MathTex(
            r"(1\; 2)(3\; 4) = (3\; 4)(1\; 2)",
            color=SECONDARY, font_size=30,
        )
        self.ly.safe_place(commute, anchor=dc2, direction=DOWN, buff=0.4)
        self.play(Write(commute), run_time=NORMAL)
        self.wait(0.2)

        # Convention
        convention = Text(
            "Convention: omit 1-cycles, identity = e",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(convention, anchor=commute, direction=DOWN, buff=0.35)
        self.play(FadeIn(convention, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 5: Composition of Permutations ---

    def scene5_composition(self):
        self.add_subcaption(
            "Composing permutations means applying one, then the other. "
            "The key point: we use function composition convention, "
            "which means right to left. "
            "Take sigma composed with tau, where sigma is the cycle one, two, three "
            "and tau is the transposition one, three. "
            "To compose, we first apply tau, then sigma. "
            "Start with element one. "
            "Tau sends one to three. Then sigma sends three to one. "
            "So one maps to one in the composition. "
            "Start with two. "
            "Tau fixes two. Then sigma sends two to three. "
            "So two maps to three. "
            "Start with three. "
            "Tau sends three to one. Then sigma sends one to two. "
            "So three maps to two. "
            "The result is the transposition two, three. "
            "Important: permutations are generally not commutative. "
            "The order matters.",
            duration=32,
        )

        title = self.ly.title("Composition of Permutations")

        defn = Text(
            "sigma . tau means: apply tau FIRST, then sigma",
            font_size=HEADING_SIZE, color=WHITE, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(defn, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(0.2)

        right_left = Text(
            "Right-to-left convention (function composition)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(right_left, anchor=defn, direction=DOWN, buff=0.35)
        self.play(FadeIn(right_left, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        self.ly.clear()

        # Work through example step by step
        title2 = self.ly.title("Example: Compose (1 2 3) with (1 3)")

        sigma = MathTex(
            r"\sigma = (1\; 2\; 3)",
            color=PRIMARY, font_size=34,
        )
        self.ly.safe_place(sigma, anchor=title2, direction=DOWN, buff=0.5)
        self.play(Write(sigma), run_time=FAST)
        self.wait(0.1)

        tau = MathTex(
            r"\tau = (1\; 3)",
            color=SECONDARY, font_size=34,
        )
        self.ly.safe_place(tau, anchor=sigma, direction=DOWN, buff=0.35)
        self.play(Write(tau), run_time=FAST)
        self.wait(0.2)

        # Step by step tracking
        steps = [
            MathTex(r"\sigma \circ \tau(1): \;\tau(1)=3,\; \sigma(3)=1 \;\Rightarrow\; 1\to 1",
                    color=WHITE, font_size=26),
            MathTex(r"\sigma \circ \tau(2): \;\tau(2)=2,\; \sigma(2)=3 \;\Rightarrow\; 2\to 3",
                    color=WHITE, font_size=26),
            MathTex(r"\sigma \circ \tau(3): \;\tau(3)=1,\; \sigma(1)=2 \;\Rightarrow\; 3\to 2",
                    color=WHITE, font_size=26),
        ]

        steps_vg = VGroup(*steps).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.ly.safe_place(steps_vg, anchor=tau, direction=DOWN, buff=0.4)

        for step in steps:
            self.play(Write(step), run_time=NORMAL)
            self.wait(0.2)
        self.wait(0.2)

        # Result
        result = MathTex(
            r"\sigma \circ \tau = (2\; 3)",
            color=ACCENT, font_size=36,
        )
        self.ly.safe_place(result, anchor=steps_vg, direction=DOWN, buff=0.4)
        boxed = SurroundingRectangle(result, color=ACCENT, buff=0.2, stroke_width=2)
        self.play(Write(result), Create(boxed), run_time=NORMAL)
        self.wait(0.3)

        self.ly.clear()

        # Non-commutativity note
        title3 = self.ly.title("Permutations Are Not Commutative")

        non_comm = MathTex(
            r"\sigma \circ \tau \neq \tau \circ \sigma \quad \text{(in general)}",
            color=RED, font_size=32,
        )
        self.ly.safe_place(non_comm, anchor=title3, direction=DOWN, buff=0.5)
        self.play(Write(non_comm), run_time=NORMAL)
        self.wait(0.2)

        example = MathTex(
            r"\text{e.g. } (1\; 2)(1\; 3) = (1\; 3\; 2) \neq (1\; 2\; 3) = (1\; 3)(1\; 2)",
            color=PRIMARY, font_size=26,
        )
        self.ly.safe_place(example, anchor=non_comm, direction=DOWN, buff=0.4)
        self.play(Write(example), run_time=NORMAL)
        self.wait(0.3)

        warning = Text(
            "S_n is NOT abelian for n >= 3!",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(warning, anchor=example, direction=DOWN, buff=0.4)
        self.play(FadeIn(warning, scale=1.05), run_time=NORMAL)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 6: Transpositions ---

    def scene6_transpositions(self):
        self.add_subcaption(
            "A transposition is a permutation that swaps exactly two elements "
            "and fixes everything else. "
            "For example, one, two swaps one and two, leaving three and four fixed. "
            "The key theorem is that every permutation "
            "can be written as a product of transpositions. "
            "For a single cycle, we can decompose it like this. "
            "Take the cycle one, two, three, four. "
            "This equals the transposition one, four, "
            "times one, three, "
            "times one, two. "
            "Read from right to left: one, two sends one to two, "
            "then one, three sends two to two, then one, four sends two to two. "
            "But tracing one: goes to two, stays at two, then one, four sends two to two. "
            "Actually, let us trace it step by step. "
            "One goes to two via one, two. "
            "Then one, three fixes two. Then one, four fixes two. "
            "So one maps to two. "
            "Similarly, two goes to one via one, two, "
            "then one, three sends one to three, "
            "then one, four sends three to three. "
            "So two maps to three. "
            "The decomposition is not unique, "
            "but we will see that the parity of the number of transpositions is fixed.",
            duration=38,
        )

        title = self.ly.title("Transpositions")

        defn = Text(
            "A transposition swaps exactly two elements:",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(defn, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(0.2)

        trans = MathTex(
            r"(i\; j) \;:\; i \leftrightarrow j, \;\text{rest fixed}",
            color=ACCENT, font_size=32,
        )
        self.ly.safe_place(trans, anchor=defn, direction=DOWN, buff=0.4)
        self.play(Write(trans), run_time=NORMAL)
        self.wait(0.2)

        example_t = MathTex(
            r"(1\; 2) = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 1 & 3 & 4 \end{pmatrix}",
            color=PRIMARY, font_size=28,
        )
        self.ly.safe_place(example_t, anchor=trans, direction=DOWN, buff=0.35)
        self.play(Write(example_t), run_time=FAST)
        self.wait(0.3)

        self.ly.clear()

        # Decomposition
        title2 = self.ly.title("Every Cycle Decomposes into Transpositions")

        theorem = Text(
            "Key Theorem:",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(theorem, anchor=title2, direction=DOWN, buff=0.5)
        self.play(Write(theorem), run_time=FAST)
        self.wait(0.1)

        formula = MathTex(
            r"(a_1\; a_2\; \ldots\; a_k) = (a_1\; a_k)(a_1\; a_{k-1}) \cdots (a_1\; a_2)",
            color=ACCENT, font_size=30,
        )
        self.ly.safe_place(formula, anchor=theorem, direction=DOWN, buff=0.4)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(0.3)

        self.ly.clear()

        # Concrete example
        title3 = self.ly.title("Example: Decompose (1 2 3 4)")

        cycle_input = MathTex(
            r"(1\; 2\; 3\; 4) = (1\; 4)(1\; 3)(1\; 2)",
            color=PRIMARY, font_size=34,
        )
        self.ly.safe_place(cycle_input, anchor=title3, direction=DOWN, buff=0.5)
        boxed = SurroundingRectangle(cycle_input, color=PRIMARY, buff=0.15, stroke_width=2)
        self.play(Write(cycle_input), Create(boxed), run_time=NORMAL)
        self.wait(0.2)

        # Verify step by step
        verify_label = Text(
            "Verify: trace 1 -> 2 -> 3 -> 4 -> 1",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(verify_label, anchor=cycle_input, direction=DOWN, buff=0.4)
        self.play(FadeIn(verify_label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.2)

        trace_steps = [
            MathTex(r"1 \xrightarrow{(1\,2)} 2 \xrightarrow{(1\,3)} 2 \xrightarrow{(1\,4)} 2",
                    color=WHITE, font_size=26),
            MathTex(r"2 \xrightarrow{(1\,2)} 1 \xrightarrow{(1\,3)} 3 \xrightarrow{(1\,4)} 3",
                    color=WHITE, font_size=26),
            MathTex(r"3 \xrightarrow{(1\,2)} 3 \xrightarrow{(1\,3)} 1 \xrightarrow{(1\,4)} 4",
                    color=WHITE, font_size=26),
            MathTex(r"4 \xrightarrow{(1\,2)} 4 \xrightarrow{(1\,3)} 4 \xrightarrow{(1\,4)} 1",
                    color=WHITE, font_size=26),
        ]

        trace_vg = VGroup(*trace_steps).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        self.ly.safe_place(trace_vg, anchor=verify_label, direction=DOWN, buff=0.35)

        for step in trace_steps:
            self.play(Write(step), run_time=FAST)
            self.wait(0.15)
        self.wait(0.2)

        note = Text(
            "Decomposition is NOT unique, but parity is fixed.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, anchor=trace_vg, direction=DOWN, buff=0.3)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 7: Parity ---

    def scene7_parity(self):
        self.add_subcaption(
            "Although a permutation can be decomposed into transpositions "
            "in many different ways, "
            "a remarkable theorem says that the number of transpositions "
            "always has the same parity. "
            "It is always even, or always odd, regardless of the decomposition. "
            "A permutation that decomposes into an even number of transpositions "
            "is called an even permutation. "
            "One that decomposes into an odd number is an odd permutation. "
            "We define the sign of a permutation sigma as minus one to the power of k, "
            "where k is the number of transpositions. "
            "Even permutations have sign plus one, "
            "and odd permutations have sign minus one. "
            "A nice visual way to see parity is the inversion count. "
            "Draw the numbers one through n on the left and the permuted order on the right. "
            "Connect each number to its new position. "
            "Count the crossings. "
            "An even number of crossings means an even permutation. "
            "For S 3, the three even permutations are e, one, two, three, and one, three, two. "
            "The three odd permutations are one, two, one, three, and two, three.",
            duration=38,
        )

        title = self.ly.title("Parity: Even and Odd Permutations")

        theorem = Text(
            "The number of transpositions in any",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(theorem, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(theorem), run_time=NORMAL)
        self.wait(0.1)

        theorem2 = Text(
            "decomposition always has the SAME parity.",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(theorem2, anchor=theorem, direction=DOWN, buff=0.25)
        self.play(Write(theorem2), run_time=NORMAL)
        self.wait(0.2)

        # Sign function
        sign = MathTex(
            r"\text{sgn}(\sigma) = (-1)^k",
            color=ACCENT, font_size=34,
        )
        self.ly.safe_place(sign, anchor=theorem2, direction=DOWN, buff=0.4)
        self.play(Write(sign), run_time=NORMAL)
        self.wait(0.1)

        sign_note = Text(
            "k = number of transpositions in decomposition",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(sign_note, anchor=sign, direction=DOWN, buff=0.3)
        self.play(FadeIn(sign_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        self.ly.clear()

        # Even vs odd labels
        title2 = self.ly.title("Even vs. Odd")

        even_label = MathTex(
            r"\text{sgn}(\sigma) = +1 \implies \text{EVEN}",
            color=SECONDARY, font_size=30,
        )
        self.ly.safe_place(even_label, anchor=title2, direction=DOWN, buff=0.5)
        self.play(Write(even_label), run_time=NORMAL)
        self.wait(0.15)

        odd_label = MathTex(
            r"\text{sgn}(\sigma) = -1 \implies \text{ODD}",
            color=RED, font_size=30,
        )
        self.ly.safe_place(odd_label, anchor=even_label, direction=DOWN, buff=0.4)
        self.play(Write(odd_label), run_time=NORMAL)
        self.wait(0.3)

        # Inversion count visual
        self.ly.clear()

        title3 = self.ly.title("Visual: Inversion Count")

        # Draw numbers on left, permuted on right, with connecting lines
        left_nums = VGroup()
        right_nums = VGroup()
        left_positions = []
        right_positions = []

        for i in range(1, 5):
            pos_l = UP * 1.2 + LEFT * 3 + DOWN * (i - 1) * 0.7
            pos_r = UP * 1.2 + RIGHT * 3 + DOWN * (i - 1) * 0.7
            left_positions.append(pos_l)
            right_positions.append(pos_r)

        perm_order = [2, 4, 1, 3]  # permutation (1 2 4)(3)
        line_colors = [SECONDARY, PRIMARY, ACCENT, RED]

        lines = VGroup()
        for i, target in enumerate(perm_order):
            ln = Line(left_positions[i], right_positions[target - 1],
                      color=line_colors[i], stroke_width=2)
            lines.add(ln)

        for i in range(1, 5):
            ln = Text(str(i), font_size=LABEL_SIZE, color=WHITE, font=MONO)
            ln.move_to(left_positions[i - 1] + LEFT * 0.3)
            left_nums.add(ln)

        for i, target in enumerate(perm_order):
            rn = Text(str(target), font_size=LABEL_SIZE, color=line_colors[i], font=MONO)
            rn.move_to(right_positions[target - 1] + RIGHT * 0.3)
            right_nums.add(rn)

        left_title = Text("Original", font_size=SMALL_SIZE, color=DIM, font=SANS)
        left_title.move_to(left_positions[0] + UP * 0.4 + LEFT * 0.3)
        right_title = Text("Permuted", font_size=SMALL_SIZE, color=DIM, font=SANS)
        right_title.move_to(right_positions[0] + UP * 0.4 + RIGHT * 0.3)

        self.ly.center_in_content(lines)
        self.play(Write(left_title), Write(right_title), run_time=FAST)
        self.play(*[Write(n) for n in left_nums], *[Write(n) for n in right_nums], run_time=FAST)
        self.play(*[Create(l) for l in lines], run_time=NORMAL)
        self.wait(0.3)

        crossing_note = Text(
            "Count the crossing lines: 3 crossings = ODD",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(crossing_note, anchor=lines, direction=DOWN, buff=0.4)
        self.play(FadeIn(crossing_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        self.ly.clear()

        # S_3 parity table
        title4 = self.ly.title("Parity in S_3")

        even_header = Text("Even (sign = +1):", font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        self.ly.safe_place(even_header, anchor=title4, direction=DOWN, buff=0.5)
        self.play(Write(even_header), run_time=FAST)
        self.wait(0.1)

        even_elems = MathTex(
            r"\{e,\; (1\; 2\; 3),\; (1\; 3\; 2)\}",
            color=WHITE, font_size=30,
        )
        self.ly.safe_place(even_elems, anchor=even_header, direction=DOWN, buff=0.3)
        self.play(Write(even_elems), run_time=FAST)
        self.wait(0.2)

        odd_header = Text("Odd (sign = -1):", font_size=HEADING_SIZE, color=RED, font=SANS)
        self.ly.safe_place(odd_header, anchor=even_elems, direction=DOWN, buff=0.35)
        self.play(Write(odd_header), run_time=FAST)
        self.wait(0.1)

        odd_elems = MathTex(
            r"\{(1\; 2),\; (1\; 3),\; (2\; 3)\}",
            color=WHITE, font_size=30,
        )
        self.ly.safe_place(odd_elems, anchor=odd_header, direction=DOWN, buff=0.3)
        self.play(Write(odd_elems), run_time=FAST)
        self.wait(0.2)

        note = Text(
            "Exactly half even, half odd!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, anchor=odd_elems, direction=DOWN, buff=0.35)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 8: Alternating Group and Summary ---

    def scene8_alternating_summary(self):
        self.add_subcaption(
            "The set of all even permutations in S sub n "
            "forms a subgroup called the alternating group, A sub n. "
            "It is closed because the composition of two even permutations "
            "is even. "
            "It contains the identity, and inverses preserve parity. "
            "The order of A sub n is exactly n factorial divided by two. "
            "Half the elements of S sub n are even, and half are odd. "
            "Let us recap what we learned. "
            "The symmetric group S sub n consists of all permutations "
            "of n elements under composition. "
            "Cycle notation is the standard compact way to write permutations. "
            "Every permutation decomposes into transpositions, "
            "and the parity of that decomposition is fixed. "
            "The alternating group A sub n is the subgroup of even permutations. "
            "These ideas are fundamental to abstract algebra "
            "and will be essential when we study cosets and Lagrange's theorem. "
            "Thanks for watching!",
            duration=30,
        )

        title = self.ly.title("The Alternating Group A_n")

        defn = Text(
            "A_n = set of all even permutations in S_n",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(defn, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(0.2)

        subgroup = Text(
            "A_n is a subgroup of S_n",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(subgroup, anchor=defn, direction=DOWN, buff=0.35)
        self.play(FadeIn(subgroup, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.2)

        order = MathTex(
            r"|A_n| = \frac{n!}{2}",
            color=ACCENT, font_size=36,
        )
        self.ly.safe_place(order, anchor=subgroup, direction=DOWN, buff=0.4)
        boxed = SurroundingRectangle(order, color=ACCENT, buff=0.2, stroke_width=2)
        self.play(Write(order), Create(boxed), run_time=NORMAL)
        self.wait(0.3)

        half_note = Text(
            "Exactly half the elements of S_n are even.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(half_note, anchor=order, direction=DOWN, buff=0.35)
        self.play(FadeIn(half_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

        # Summary
        title2 = self.ly.title("Summary")

        takeaways = [
            Text("1. S_n: all permutations of n elements", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Cycle notation: compact standard form", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Every perm decomposes into transpositions", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Parity (even/odd) is well-defined", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("5. A_n = even permutations, |A_n| = n!/2", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]

        self.ly.progressive_reveal(takeaways, start_from=title2, run_time=0.6)
        self.wait(0.3)

        closing = Text(
            "Next time: Cosets and Lagrange's Theorem",
            font_size=HEADING_SIZE, color=WHITE, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(closing, anchor=title2, direction=DOWN, buff=-3.0)
        clamp_position(closing)
        self.play(FadeIn(closing, scale=1.05), run_time=NORMAL)
        self.wait(0.5)

        play_outro(self, "Permutation Groups", "Abstract Algebra I")
