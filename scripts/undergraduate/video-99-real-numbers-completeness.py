"""
Video 99: The Real Numbers (Completeness)
TEMPLATE v2 — Professional quality Manim script

Playlist: Real Analysis I (Video 1 of 12)
Class: Video99_RealNumbers

QUALITY RULES (enforced):
  1. Max 5 visible elements per scene at any time
  2. Use LayoutEngine for ALL positioning — no manual .shift() or .to_edge()
  3. Progressive disclosure: add items one at a time
  4. Use consistent animation vocabulary (Write, FadeIn, Create, etc.)
  5. Each add_subcaption() duration ~ words / 2.5 seconds
  6. Call ly.clear() between scenes
  7. Raw strings for MathTex with single backslashes
  8. No font= parameter on MathTex (only on Text)
"""

from manim import *
import sys, os, math
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video99_RealNumbers(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_problem_with_q()
        self.scene4_divider_bounds()
        self.scene5_upper_bounds_suprema()
        self.scene6_divider_completeness()
        self.scene7_completeness_axiom()
        self.scene8_why_it_matters()
        self.scene9_outro()

    # ─── Scene 1: Hook — The Hidden Foundation ───
    def scene1_hook(self):
        self.add_subcaption(
            "You have spent your mathematical life using real numbers. "
            "They seem seamless, a continuous number line stretching to infinity. "
            "But this seamlessness is not automatic. "
            "The rational numbers, which you might think of as complete, "
            "actually have gaps. And filling those gaps is what makes calculus possible. "
            "Today we begin Real Analysis with the foundation: the Completeness Axiom.",
            duration=24.3,
        )
        play_intro(self, "The Real Numbers", "Real Analysis I")

        title = self.ly.title("The Hidden Foundation")

        # Number line setup
        number_line = NumberLine(
            x_range=[-1, 4, 1],
            length=10,
            color=PRIMARY,
            stroke_width=2,
            include_tip=True,
        )
        self.ly.center_in_content(number_line)
        self.play(Create(number_line), run_time=NORMAL)

        # Labels for 1 and 2
        label1 = MathTex("1", font_size=LABEL_SIZE, color=WHITE)
        label1.next_to(number_line.n2p(1), DOWN, buff=0.2)
        label2 = MathTex("2", font_size=LABEL_SIZE, color=WHITE)
        label2.next_to(number_line.n2p(2), DOWN, buff=0.2)
        self.play(FadeIn(label1), FadeIn(label2), run_time=FAST)
        self.wait(0.5)

        # Question
        question = Text(
            "Is there a number between 1 and 2 whose square is 2?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(question, direction=UP, anchor=number_line, buff=0.5)
        self.play(FadeIn(question, shift=UP * 0.1), run_time=NORMAL)
        self.wait(1)

        # sqrt(2) reveal
        sqrt_label = MathTex(r"\sqrt{2}", font_size=HEADING_SIZE, color=SECONDARY)
        sqrt_point = number_line.n2p(np.sqrt(2))
        sqrt_label.move_to(sqrt_point + UP * 0.6)
        dot = Dot(sqrt_point, color=SECONDARY, radius=0.08)
        self.play(FadeIn(dot), Write(sqrt_label), run_time=NORMAL)
        self.wait(0.5)

        # The gap in Q
        gap_label = Text(
            "sqrt(2) exists in R ... but NOT in Q",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(gap_label, direction=DOWN, anchor=number_line, buff=0.5)
        self.play(FadeIn(gap_label, shift=UP * 0.1), run_time=NORMAL)
        # pacing: extends previous caption slot
        self.wait(11.5)

        self.ly.clear()

    # ─── Scene 2: Intro + Section Divider ───
    def scene2_intro(self):
        self.add_subcaption(
            "We begin with a question that motivated the construction of the real numbers. "
            "Can we guarantee that every bounded collection of numbers "
            "has a well-defined limit point? "
            "The answer for the rational numbers is no. "
            "For the real numbers, yes. And that yes is called completeness.",
            duration=16.7,
        )

        self.ly.section_divider(1, "Why the Rationals Are Not Enough", hold=15.4)
        self.ly.clear()

    # ─── Scene 3: The Problem with Q ───
    def scene3_problem_with_q(self):
        self.add_subcaption(
            "The rational numbers seem complete. "
            "You can add, subtract, multiply, divide, and take many roots. "
            "But there is a fatal flaw. "
            "Consider the set of all rational numbers whose square is less than two. "
            "This set is bounded above, but it has no least upper bound that is rational. "
            "The least upper bound would be the square root of two, "
            "and the square root of two is irrational. "
            "The rationals have a hole right there. "
            "The real numbers exist to fill every such hole.",
            duration=30.5,
        )

        title = self.ly.title("The Rationals Have Holes")

        # Q number line with visible dots
        q_line = NumberLine(
            x_range=[-1, 3, 1],
            length=10,
            color=DIM,
            stroke_width=2,
            include_tip=True,
        )
        q_label = Text("Q (Rational Numbers)", font_size=LABEL_SIZE, color=DIM, font=MONO)
        q_label.next_to(q_line, UP, buff=0.2)
        q_group = VGroup(q_label, q_line)
        self.ly.center_in_content(q_group)
        self.play(Create(q_line), FadeIn(q_label), run_time=NORMAL)

        # Place rational dots near sqrt(2)
        rationals = [1.0, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 2.0]
        q_dots = VGroup(*[
            Dot(q_line.n2p(r), color=PRIMARY, radius=0.06)
            for r in rationals
        ])
        self.play(FadeIn(q_dots, scale=0.8), run_time=FAST)
        self.wait(0.5)

        # Show the gap
        gap_brace = Brace(
            VGroup(
                Dot(q_line.n2p(1.4), color=RED, radius=0.04),
                Dot(q_line.n2p(1.5), color=RED, radius=0.04),
            ),
            DOWN,
            color=RED,
        )
        gap_text = Text(
            "No rational number here!",
            font_size=SMALL_SIZE, color=RED, font=SANS,
        )
        gap_text.next_to(gap_brace, DOWN, buff=0.15)
        self.play(Create(gap_brace), FadeIn(gap_text), run_time=NORMAL)
        self.wait(0.5)

        # Fade gap elements, show the set definition
        self.play(FadeOut(gap_brace), FadeOut(gap_text), run_time=0.3)

        set_def = MathTex(
            r"S = \{ x \in \mathbb{Q} : x^2 < 2 \}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(set_def, direction=DOWN, anchor=q_line, buff=0.5)
        self.play(Write(set_def), run_time=NORMAL)
        self.wait(0.5)

        # Bounded above, but no supremum
        upper_label = Text(
            "Bounded above by 2, 1.5, 1.42 ...",
            font_size=LABEL_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(upper_label, direction=DOWN, anchor=set_def, buff=0.4)
        self.play(FadeIn(upper_label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        no_sup = Text(
            "But NO least upper bound exists in Q!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(no_sup, direction=DOWN, anchor=upper_label, buff=0.4)
        self.play(FadeIn(no_sup, shift=LEFT * 0.15), run_time=FAST)
        # pacing: extends previous caption slot
        self.wait(24.2)

        self.ly.clear()

    # ─── Scene 4: Section Divider — Bounded Sets ───
    def scene4_divider_bounds(self):
        self.add_subcaption(
            "To state the completeness axiom precisely, "
            "we need the language of upper bounds and least upper bounds. "
            "These definitions are the building blocks of real analysis.",
            duration=10.4,
        )
        self.ly.section_divider(2, "Bounded Sets and Bounds", hold=8.6)
        self.ly.clear()

    # ─── Scene 5: Upper Bounds and Suprema ───
    def scene5_upper_bounds_suprema(self):
        self.add_subcaption(
            "An upper bound of a set S is a number M "
            "such that every element of S is less than or equal to M. "
            "Think of it as a ceiling that nothing in the set can exceed. "
            "The supremum, also called the least upper bound, "
            "is the lowest such ceiling. "
            "Among all upper bounds, it is the smallest one. "
            "The supremum has two properties. "
            "First, it IS an upper bound. "
            "Second, any number strictly less than it fails to be an upper bound. "
            "The infimum is defined symmetrically as the greatest lower bound.",
            duration=32.5,
        )

        title = self.ly.title("Upper Bounds and Suprema")

        # Definition of upper bound
        def_ub = MathTex(
            r"M \text{ is an upper bound of } S "
            r"\iff x \leq M \;\; \forall\, x \in S",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(def_ub, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(def_ub), run_time=NORMAL)
        self.wait(1)

        # Number line with set dots and upper bound
        nl = NumberLine(
            x_range=[0, 4, 1],
            length=9,
            color=PRIMARY,
            stroke_width=2,
            include_tip=True,
        )
        self.ly.safe_place(nl, direction=DOWN, anchor=def_ub, buff=0.5)

        # Set dots
        set_vals = [0.5, 1.2, 1.8, 2.5, 3.1]
        set_dots = VGroup(*[
            Dot(nl.n2p(v), color=SECONDARY, radius=0.07)
            for v in set_vals
        ])
        s_label = Text("S", font_size=LABEL_SIZE, color=SECONDARY, font=MONO)
        s_label.next_to(set_dots, UP, buff=0.15)

        self.play(Create(nl), run_time=FAST)
        self.play(FadeIn(set_dots, scale=0.8), FadeIn(s_label), run_time=FAST)
        self.wait(0.5)

        # Upper bound M
        m_dot = Dot(nl.n2p(3.5), color=RED, radius=0.07)
        m_label = Text("M (upper bound)", font_size=SMALL_SIZE, color=RED, font=MONO)
        m_label.next_to(m_dot, UP, buff=0.2)
        self.play(FadeIn(m_dot), FadeIn(m_label), run_time=FAST)
        self.wait(0.5)

        # Fade def_ub to make room, show supremum definition
        self.play(FadeOut(def_ub), run_time=0.3)

        # Supremum definition
        sup_def = MathTex(
            r"\alpha = \sup(S) \iff "
            r"\begin{cases} "
            r"x \leq \alpha \;\;\forall\, x \in S & \text{(upper bound)} \\ "
            r"\text{if } \epsilon > 0, \;\exists\, x \in S : x > \alpha - \epsilon & \text{(least)} "
            r"\end{cases}",
            font_size=LABEL_SIZE, color=WHITE,
        )
        self.ly.safe_place(sup_def, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(sup_def), run_time=2.0)
        self.wait(1)

        # Highlight the sup on the number line
        sup_point = nl.n2p(3.1)
        sup_dot = Dot(sup_point, color=ACCENT, radius=0.09)
        sup_label = MathTex(r"\sup(S)", font_size=LABEL_SIZE, color=ACCENT)
        sup_label.next_to(sup_dot, DOWN, buff=0.25)
        self.play(
            FadeIn(sup_dot),
            Write(sup_label),
            FadeOut(m_dot), FadeOut(m_label),
            run_time=NORMAL,
        )
        self.wait(1)

        # Brief infimum mention
        inf_note = Text(
            "Infimum (greatest lower bound) is defined symmetrically.",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(inf_note, direction=DOWN, anchor=nl, buff=0.5)
        self.play(FadeIn(inf_note, shift=LEFT * 0.1), run_time=FAST)
        # pacing: extends previous caption slot
        self.wait(22.8)

        self.ly.clear()

    # ─── Scene 6: Section Divider — Completeness Axiom ───
    def scene6_divider_completeness(self):
        self.add_subcaption(
            "Now we are ready for the axiom that distinguishes "
            "the real numbers from every other number system.",
            duration=6.0,
        )
        self.ly.section_divider(3, "The Completeness Axiom", hold=3.8)
        self.ly.clear()

    # ─── Scene 7: The Completeness Axiom ───
    def scene7_completeness_axiom(self):
        self.add_subcaption(
            "Here is the Completeness Axiom, the foundation of real analysis. "
            "Every nonempty set of real numbers that has an upper bound, "
            "has a least upper bound that is itself a real number. "
            "This sounds simple, but it is profound. "
            "The rational numbers fail this property. "
            "The set of rationals whose square is less than two "
            "is nonempty, bounded above, but has no least upper bound in the rationals. "
            "The real numbers, by contrast, guarantee "
            "that every bounded-above set finds its ceiling. "
            "This single axiom is what makes limits work, "
            "what makes the Intermediate Value Theorem true, "
            "and what makes calculus rigorous.",
            duration=40.2,
        )

        title = self.ly.title("The Completeness Axiom")

        # Axiom in a formula box
        axiom = MathTex(
            r"\text{If } S \subseteq \mathbb{R}, \; S \neq \emptyset, "
            r"\text{ and } S \text{ is bounded above,} \\[4pt] "
            r"\text{then } \sup(S) \text{ exists and } \sup(S) \in \mathbb{R}.",
            font_size=BODY_SIZE, color=WHITE,
        )
        axiom_box = self.ly.formula_box(axiom, color=ACCENT)
        self.ly.center_in_content(axiom_box)
        self.play(Write(axiom), Create(axiom_box[1]), run_time=2.0)
        self.wait(1.5)

        # R number line (complete)
        r_line = NumberLine(
            x_range=[-1, 3, 1],
            length=9,
            color=PRIMARY,
            stroke_width=2,
            include_tip=True,
        )
        r_label = Text("R (Complete)", font_size=LABEL_SIZE, color=PRIMARY, font=MONO)
        r_label.next_to(r_line, UP, buff=0.2)
        r_group = VGroup(r_label, r_line)
        self.ly.safe_place(r_group, direction=DOWN, anchor=axiom_box, buff=0.6)

        # Q number line (incomplete, with gap)
        q_line2 = NumberLine(
            x_range=[-1, 3, 1],
            length=9,
            color=DIM,
            stroke_width=2,
            include_tip=True,
        )
        q_label2 = Text("Q (Incomplete)", font_size=LABEL_SIZE, color=DIM, font=MONO)
        q_label2.next_to(q_line2, UP, buff=0.2)

        left_col, right_col = self.ly.two_columns(
            [VGroup(q_label2, q_line2)],
            [VGroup(r_label, r_line)],
        )

        # Add gap marker on Q line
        gap_x = q_line2.n2p(np.sqrt(2))
        gap_marker = VGroup(
            Line(gap_x + UP * 0.2, gap_x + DOWN * 0.2, color=RED, stroke_width=3),
            Text("gap", font_size=SMALL_SIZE, color=RED, font=MONO).next_to(
                gap_x, DOWN, buff=0.15,
            ),
        )
        gap_marker.move_to(gap_x)
        gap_marker.shift(DOWN * 0.05)

        self.play(
            FadeIn(left_col, shift=LEFT * 0.15),
            FadeIn(right_col, shift=RIGHT * 0.15),
            run_time=NORMAL,
        )
        self.play(FadeIn(gap_marker), run_time=FAST)
        self.wait(1.5)

        # Key insight text
        insight = Text(
            "Completeness is what distinguishes R from Q.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=left_col, buff=0.5)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=FAST)
        # pacing: extends previous caption slot
        self.wait(34.9)

        self.ly.clear()

    # ─── Scene 8: Why Completeness Matters ───
    def scene8_why_it_matters(self):
        self.add_subcaption(
            "Why should you care about completeness? Three reasons. "
            "First, limits. When a sequence converges in R, "
            "its limit is guaranteed to exist in R. "
            "Without completeness, a sequence could converge to a hole. "
            "Second, the Intermediate Value Theorem, "
            "which you used in Calculus One to show "
            "that continuous functions hit every intermediate value, "
            "relies on completeness. "
            "Third, the entire theory of Riemann integration, "
            "area under a curve, requires that certain sets have least upper bounds. "
            "Every theorem you learned in Calculus One and Two "
            "ultimately traces back to this axiom.",
            duration=37.8,
        )

        title = self.ly.title("Why Completeness Matters")

        # Three application cards
        cards = []
        card_data = [
            ("Limits Exist", "Convergent sequences in R have\ntheir limit IN R", PRIMARY),
            ("Intermediate Value Theorem", "Continuous functions take\nevery value between endpoints", SECONDARY),
            ("Riemann Integration", "Area under a curve requires\nleast upper bounds of areas", ACCENT),
        ]

        for card_title, card_desc, card_color in card_data:
            bg_rect = RoundedRectangle(
                corner_radius=0.15,
                fill_color="#12102A",
                fill_opacity=0.9,
                stroke_color=card_color,
                stroke_width=1.5,
                width=4.0,
                height=1.8,
            )
            ct = Text(card_title, font_size=BODY_SIZE, color=card_color, font=SANS, weight=BOLD)
            ct.next_to(bg_rect.get_top(), DOWN, buff=0.2)
            cd = Text(card_desc, font_size=SMALL_SIZE, color=WHITE, font=SANS)
            cd.next_to(ct, DOWN, buff=0.1)
            card = VGroup(bg_rect, ct, cd)
            cards.append(card)

        # Reveal cards one by one
        for i, card in enumerate(cards):
            self.ly.safe_place(card, direction=DOWN, anchor=title if i == 0 else cards[i - 1], buff=0.35)
            self.play(FadeIn(card, shift=LEFT * 0.15), run_time=NORMAL)
            self.wait(0.5)

        # Calculus connection
        calc_link = Text(
            "Every theorem in Calculus traces back to this axiom.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(calc_link, direction=DOWN, anchor=cards[-1], buff=0.4)
        self.play(FadeIn(calc_link, shift=LEFT * 0.15), run_time=FAST)
        # pacing: extends previous caption slot
        self.wait(34.0)

        self.ly.clear()

    # ─── Scene 9: Outro ───
    def scene9_outro(self):
        self.add_subcaption(
            "Three things to remember. "
            "First, the rational numbers have holes. "
            "The real numbers fill every gap. "
            "Second, the Completeness Axiom guarantees "
            "that every bounded-above set of real numbers "
            "has a least upper bound in the reals. "
            "Third, this axiom is the hidden foundation of calculus. "
            "Without it, limits, continuity, and integration all break down. "
            "In the next video, we put completeness to work "
            "with sequences and convergence.",
            duration=29.7,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text("Q has holes. R has none.", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Completeness: every bounded-above set", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("in R has a supremum in R.", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("This axiom is the foundation of calculus.", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title)

        # pacing: extends previous caption slot
        self.wait(18.6)

        play_outro(
            self,
            next_video="Sequences and Convergence",
            next_playlist="Real Analysis I",
        )
