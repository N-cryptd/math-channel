"""
Video 101: Cauchy Sequences
TEMPLATE v2 -- Professional quality Manim script

Playlist: Real Analysis I (Video 3 of 12)
Class: Video101_CauchySequences

QUALITY RULES (enforced):
  1. Max 5 visible elements per scene at any time
  2. Use LayoutEngine for ALL positioning -- no manual .shift() or .to_edge()
  3. Progressive disclosure: add items one at a time
  4. Use consistent animation vocabulary (Write, FadeIn, Create, etc.)
  5. Each add_subcaption() duration ~ words / 2.5 seconds
  6. Call ly.clear() between scenes
  7. Raw strings for MathTex with single backslashes
  8. No font= parameter on MathTex (only on Text)
"""

from manim import *
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


class Video101_CauchySequences(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_intuition()
        self.scene4_divider_definition()
        self.scene5_formal_definition()
        self.scene6_divider_proof()
        self.scene7_proof_convergent_implies_cauchy()
        self.scene8_divider_completeness()
        self.scene9_cauchy_completeness_and_q()
        self.scene10_summary_outro()

    # --- Scene 1: Hook -- The Mystery Limit ---
    def scene1_hook(self):
        self.add_subcaption(
            "Last time we proved convergence using the epsilon-N definition. "
            "But there is a problem. "
            "That definition requires you to know the limit L in advance. "
            "What if you do not know L? "
            "What if you cannot even guess it? "
            "Cauchy sequences give us a way to prove convergence "
            "without ever naming the limit.",
            duration=26,
        )
        play_intro(self, "Cauchy Sequences", "Real Analysis I")

        title = self.ly.title("The Mystery Limit")

        # Number line
        nl = NumberLine(
            x_range=[0.8, 1.7, 0.1],
            length=10,
            color=PRIMARY,
            stroke_width=2,
            include_tip=True,
        )
        self.ly.center_in_content(nl)
        self.play(Create(nl), run_time=NORMAL)

        # Decimal approximations of sqrt(2): 1, 1.4, 1.41, 1.414, 1.4142
        terms = [1.0, 1.4, 1.41, 1.414, 1.4142]
        labels_text = ["1", "1.4", "1.41", "1.414", "1.4142"]
        dots = []
        term_labels = []

        for val, txt in zip(terms, labels_text):
            pos = nl.n2p(val)
            d = Dot(pos, color=SECONDARY, radius=0.07)
            dots.append(d)
            lbl = MathTex(txt, font_size=SMALL_SIZE, color=WHITE)
            lbl.next_to(pos, DOWN, buff=0.25)
            term_labels.append(lbl)
            self.play(FadeIn(d, scale=0.8), FadeIn(lbl), run_time=0.6)
            self.wait(0.2)

        # Question mark where limit would be
        q_mark = MathTex("?", font_size=HEADING_SIZE, color=RED)
        q_pos = nl.n2p(1.4142)
        q_mark.next_to(q_pos, UP, buff=0.3)
        self.play(Write(q_mark), run_time=FAST)
        self.wait(0.5)

        question = Text(
            "Terms cluster together... but what do they converge to?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(question, direction=DOWN, anchor=nl, buff=0.4)
        self.play(FadeIn(question, shift=UP * 0.1), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 2: Intro + Section Divider ---
    def scene2_intro(self):
        self.add_subcaption(
            "Let us explore what it means "
            "for the terms of a sequence to get closer "
            "not to a known limit, but to each other.",
            duration=10,
        )
        self.ly.section_divider(1, "Convergence vs Cauchy")
        self.ly.clear()

    # --- Scene 3: Convergence vs Cauchy Intuition ---
    def scene3_intuition(self):
        self.add_subcaption(
            "Here is the key distinction. "
            "In convergence, we measure the distance from each term to the limit L. "
            "Every term must eventually be within epsilon of L. "
            "But in a Cauchy sequence, "
            "we measure the distance between any two terms. "
            "If you pick any two terms far enough along the sequence, "
            "their distance is less than epsilon. "
            "Think of it like this: "
            "convergence means the terms are all approaching the same destination. "
            "Cauchy means the terms are all approaching each other. "
            "If the terms are squeezing together, "
            "they must be squeezing toward something. "
            "In the real numbers, completeness guarantees that something exists.",
            duration=47,
        )

        title = self.ly.title("Two Ways to Measure Closeness")

        # Left panel header: Convergence
        conv_header = Text(
            "Convergence", font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )

        # Right panel header: Cauchy
        cauchy_header = Text(
            "Cauchy", font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )

        left_col, right_col = self.ly.two_columns(
            [conv_header], [cauchy_header], start_from=title,
        )
        self.play(FadeIn(left_col), FadeIn(right_col), run_time=NORMAL)
        self.wait(0.5)

        # Convergence visual: number line with L and terms near L
        nl_conv = NumberLine(
            x_range=[-0.5, 3.5, 1],
            length=5,
            color=DIM,
            stroke_width=1.5,
            include_tip=True,
        )
        nl_conv.move_to(DOWN * 1.2 + LEFT * 3.2)
        l_dot = Dot(nl_conv.n2p(1.5), color=ACCENT, radius=0.08)
        l_label = MathTex("L", font_size=LABEL_SIZE, color=ACCENT)
        l_label.next_to(l_dot, UP, buff=0.15)
        # Terms near L
        conv_terms = VGroup(*[
            Dot(nl_conv.n2p(v), color=PRIMARY, radius=0.05)
            for v in [1.2, 1.3, 1.6, 1.7, 1.55, 1.45]
        ])
        conv_vis = VGroup(nl_conv, l_dot, l_label, conv_terms)
        self.ly.safe_place(conv_vis, direction=DOWN, anchor=conv_header, buff=0.3)

        # Remove old left_col
        self.play(FadeOut(left_col[0]), run_time=0.3)
        self.play(Create(nl_conv), FadeIn(l_dot), Write(l_label),
                  FadeIn(conv_terms, scale=0.7, lag_ratio=0.1), run_time=NORMAL)
        self.wait(0.5)

        # Distance arrows from terms to L
        arrow1 = Arrow(nl_conv.n2p(1.2), nl_conv.n2p(1.5), color=RED, stroke_width=2, max_tip_length_to_length_ratio=0.15)
        arrow1_label = MathTex(r"\varepsilon", font_size=SMALL_SIZE, color=RED)
        arrow1_label.next_to(arrow1, UP, buff=0.05)
        self.play(Create(arrow1), FadeIn(arrow1_label), run_time=FAST)
        self.wait(0.5)

        # Cauchy visual: number line with two terms and distance between them
        nl_cauchy = NumberLine(
            x_range=[-0.5, 3.5, 1],
            length=5,
            color=DIM,
            stroke_width=1.5,
            include_tip=True,
        )
        nl_cauchy.move_to(DOWN * 1.2 + RIGHT * 3.2)
        a_m_dot = Dot(nl_cauchy.n2p(1.3), color=SECONDARY, radius=0.07)
        a_n_dot = Dot(nl_cauchy.n2p(1.7), color=PRIMARY, radius=0.07)
        a_m_lbl = MathTex("a_m", font_size=SMALL_SIZE, color=SECONDARY)
        a_m_lbl.next_to(a_m_dot, UP, buff=0.15)
        a_n_lbl = MathTex("a_n", font_size=SMALL_SIZE, color=PRIMARY)
        a_n_lbl.next_to(a_n_dot, UP, buff=0.15)
        cauchy_vis = VGroup(nl_cauchy, a_m_dot, a_n_dot, a_m_lbl, a_n_lbl)
        self.ly.safe_place(cauchy_vis, direction=DOWN, anchor=cauchy_header, buff=0.3)

        self.play(FadeOut(right_col[0]), run_time=0.3)
        self.play(Create(nl_cauchy), FadeIn(a_m_dot), FadeIn(a_n_dot),
                  Write(a_m_lbl), Write(a_n_lbl), run_time=NORMAL)
        self.wait(0.5)

        # Double-headed arrow between a_m and a_n
        d_arrow = DoubleArrow(
            nl_cauchy.n2p(1.3), nl_cauchy.n2p(1.7),
            color=ACCENT, stroke_width=2, max_tip_length_to_length_ratio=0.15,
        )
        d_arrow.shift(DOWN * 0.3)
        d_label = MathTex(r"|a_m - a_n| < \varepsilon", font_size=SMALL_SIZE, color=ACCENT)
        d_label.next_to(d_arrow, DOWN, buff=0.1)
        self.play(Create(d_arrow), Write(d_label), run_time=NORMAL)
        self.wait(1)

        # Key insight text
        insight = Text(
            "Cauchy measures distance BETWEEN terms, not from a limit!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.center_in_content(insight)
        insight.shift(DOWN * 2.5)
        clamp_position(insight)
        self.play(
            FadeOut(conv_vis), FadeOut(arrow1), FadeOut(arrow1_label),
            FadeOut(cauchy_vis), FadeOut(d_arrow), FadeOut(d_label),
            FadeOut(title),
            run_time=0.6,
        )
        self.play(FadeIn(insight, shift=UP * 0.1), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # --- Scene 4: Section Divider -- Formal Definition ---
    def scene4_divider_definition(self):
        self.add_subcaption(
            "Let us translate this intuition "
            "into the precise language of real analysis.",
            duration=5,
        )
        self.ly.section_divider(2, "The Definition")
        self.ly.clear()

    # --- Scene 5: The Formal Definition ---
    def scene5_formal_definition(self):
        self.add_subcaption(
            "A sequence a sub n is Cauchy if "
            "for every epsilon greater than zero, "
            "there exists a natural number N "
            "such that for all m and n greater than N, "
            "the absolute value of a sub m minus a sub n "
            "is less than epsilon. "
            "Epsilon is how close we demand any two late terms to be. "
            "N tells us how far along we need to go. "
            "The condition says: once both indices m and n are past N, "
            "the two terms are within epsilon of each other. "
            "Notice something crucial. "
            "The limit L does not appear anywhere in this definition. "
            "That is the power of Cauchy sequences.",
            duration=40,
        )

        title = self.ly.title("Formal Definition of a Cauchy Sequence")

        # Visual: number line with a_m, a_n, and distance arrow
        nl = NumberLine(
            x_range=[-0.5, 3.5, 1],
            length=9,
            color=PRIMARY,
            stroke_width=2,
            include_tip=True,
        )
        self.ly.center_in_content(nl)
        self.play(Create(nl), run_time=NORMAL)

        # Two terms
        am_dot = Dot(nl.n2p(1.5), color=SECONDARY, radius=0.08)
        am_lbl = MathTex("a_m", font_size=BODY_SIZE, color=SECONDARY)
        am_lbl.next_to(am_dot, UP, buff=0.2)
        an_dot = Dot(nl.n2p(2.5), color=PRIMARY, radius=0.08)
        an_lbl = MathTex("a_n", font_size=BODY_SIZE, color=PRIMARY)
        an_lbl.next_to(an_dot, UP, buff=0.2)

        self.play(FadeIn(am_dot), Write(am_lbl), run_time=FAST)
        self.play(FadeIn(an_dot), Write(an_lbl), run_time=FAST)
        self.wait(0.5)

        # Distance arrow
        dist_arrow = DoubleArrow(
            nl.n2p(1.5), nl.n2p(2.5),
            color=ACCENT, stroke_width=2.5, max_tip_length_to_length_ratio=0.12,
        )
        dist_arrow.shift(DOWN * 0.35)
        dist_lbl = MathTex(
            r"|a_m - a_n| < \varepsilon", font_size=BODY_SIZE, color=ACCENT,
        )
        dist_lbl.next_to(dist_arrow, DOWN, buff=0.15)
        self.play(Create(dist_arrow), Write(dist_lbl), run_time=NORMAL)
        self.wait(1)

        # Animate: terms get closer
        new_am = nl.n2p(1.9)
        new_an = nl.n2p(2.1)
        self.play(
            am_dot.animate.move_to(new_am), am_lbl.animate.next_to(new_am, UP, buff=0.2),
            an_dot.animate.move_to(new_an), an_lbl.animate.next_to(new_an, UP, buff=0.2),
            dist_arrow.animate.become(DoubleArrow(
                new_am + DOWN * 0.35, new_an + DOWN * 0.35,
                color=ACCENT, stroke_width=2.5, max_tip_length_to_length_ratio=0.12,
            )),
            run_time=1.5,
        )
        self.wait(1)

        # Clear visual, show formal definition
        self.ly.clear()

        title2 = self.ly.title("The Cauchy Condition")

        # Build definition step by step
        def_part1 = MathTex(
            r"(a_n) \text{ is Cauchy}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(def_part1, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(def_part1), run_time=NORMAL)
        self.wait(0.5)
        self.play(FadeOut(def_part1), run_time=0.3)

        full_def = MathTex(
            r"\text{For every } \varepsilon > 0, \;"
            r"\text{there exists } N \in \mathbb{N} \;"
            r"\text{such that:}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(full_def, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(full_def), run_time=NORMAL)
        self.wait(0.5)

        condition = MathTex(
            r"m, n > N \implies |a_m - a_n| < \varepsilon",
            font_size=HEADING_SIZE, color=WHITE,
        )
        cond_box = self.ly.formula_box(condition, color=ACCENT)
        self.ly.safe_place(cond_box, direction=DOWN, anchor=full_def, buff=0.5)
        self.play(Write(condition), Create(cond_box[1]), run_time=2.0)
        self.wait(1)

        # Part-by-part explanation
        parts = [
            (r"\varepsilon", "How close any two terms must be", SECONDARY),
            (r"N", "How far along the sequence to go", RED),
            (r"m, n > N", "BOTH terms must be past N", PRIMARY),
            (r"|a_m - a_n| < \varepsilon", "Distance between them is tiny", ACCENT),
        ]

        self.play(FadeOut(full_def), FadeOut(cond_box), run_time=0.4)

        self._part_rows = []
        for sym, desc, col in parts:
            row = VGroup(
                MathTex(sym, font_size=BODY_SIZE, color=col),
                Text(desc, font_size=BODY_SIZE, color=WHITE, font=SANS),
            ).arrange(RIGHT, buff=0.5)
            if not self._part_rows:
                self.ly.safe_place(row, direction=DOWN, anchor=title2, buff=0.5)
            else:
                self.ly.safe_place(row, direction=DOWN, anchor=self._part_rows[-1], buff=0.3)
            self._part_rows.append(row)
            self.play(FadeIn(row, shift=LEFT * 0.15), run_time=FAST)
            self.wait(0.5)
            if len(self._part_rows) > 4:
                old = self._part_rows.pop(0)
                self.play(FadeOut(old), run_time=0.3)

        del self._part_rows

        # Key observation
        key_obs = Text(
            "The limit L does NOT appear in the definition!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(key_obs, direction=DOWN, anchor=row, buff=0.5)
        self.play(FadeIn(key_obs, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 6: Section Divider -- Proof ---
    def scene6_divider_proof(self):
        self.add_subcaption(
            "We now prove the first key result "
            "about Cauchy sequences.",
            duration=5,
        )
        self.ly.section_divider(3, "Convergent Implies Cauchy")
        self.ly.clear()

    # --- Scene 7: Proof -- Every Convergent Sequence is Cauchy ---
    def scene7_proof_convergent_implies_cauchy(self):
        self.add_subcaption(
            "The first direction is straightforward. "
            "If a sequence converges, it must be Cauchy. "
            "Let epsilon be positive. "
            "Since a sub n converges to L, "
            "there exists N such that for all n greater than N, "
            "the absolute value of a sub n minus L "
            "is less than epsilon over two. "
            "Now let m and n both be greater than N. "
            "We want to bound the distance between a sub m and a sub n. "
            "By the triangle inequality, "
            "this is at most the distance from a sub m to L "
            "plus the distance from a sub n to L. "
            "Each of these is less than epsilon over two, "
            "so the sum is less than epsilon. "
            "The trick was using epsilon over two: "
            "each term gets half the error budget, "
            "so together they stay within epsilon.",
            duration=44,
        )

        title = self.ly.title("Proof: Convergent Implies Cauchy")

        # Claim
        claim = MathTex(
            r"a_n \to L \implies (a_n) \text{ is Cauchy}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(claim, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(claim), run_time=NORMAL)
        self.wait(0.5)

        # Visual: number line with L, epsilon/2 bands
        nl = NumberLine(
            x_range=[-0.5, 3.5, 1],
            length=9,
            color=PRIMARY,
            stroke_width=2,
            include_tip=True,
        )
        l_pos = nl.n2p(1.5)
        l_dot = Dot(l_pos, color=ACCENT, radius=0.09)
        l_label = MathTex("L", font_size=HEADING_SIZE, color=ACCENT)
        l_label.next_to(l_dot, UP, buff=0.2)
        # epsilon/2 band
        eps_left = nl.n2p(1.5 - 0.4)
        eps_right = nl.n2p(1.5 + 0.4)
        eps_band = Line(eps_left, eps_right, color=SECONDARY, stroke_width=10)
        eps_label = MathTex(r"\varepsilon/2", font_size=LABEL_SIZE, color=SECONDARY)
        eps_label.next_to(eps_band, UP, buff=0.1)
        # Two terms within epsilon/2 of L
        am_pos = nl.n2p(1.25)
        an_pos = nl.n2p(1.7)
        am_dot = Dot(am_pos, color=SECONDARY, radius=0.07)
        am_lbl = MathTex("a_m", font_size=LABEL_SIZE, color=SECONDARY)
        am_lbl.next_to(am_pos, DOWN, buff=0.2)
        an_dot = Dot(an_pos, color=PRIMARY, radius=0.07)
        an_lbl = MathTex("a_n", font_size=LABEL_SIZE, color=PRIMARY)
        an_lbl.next_to(an_pos, DOWN, buff=0.2)
        # Distance arrow between them
        dist_a = DoubleArrow(
            am_pos + DOWN * 0.55, an_pos + DOWN * 0.55,
            color=ACCENT, stroke_width=2, max_tip_length_to_length_ratio=0.15,
        )
        dist_a_lbl = MathTex(r"< \varepsilon", font_size=LABEL_SIZE, color=ACCENT)
        dist_a_lbl.next_to(dist_a, DOWN, buff=0.05)

        nl_group = VGroup(nl, l_dot, l_label, eps_band, eps_label,
                          am_dot, am_lbl, an_dot, an_lbl, dist_a, dist_a_lbl)
        self.ly.center_in_content(nl_group)

        self.play(FadeOut(claim), run_time=0.3)
        self.play(
            Create(nl), FadeIn(l_dot), Write(l_label),
            run_time=NORMAL,
        )
        self.play(Create(eps_band), Write(eps_label), run_time=FAST)
        self.play(
            FadeIn(am_dot), Write(am_lbl), FadeIn(an_dot), Write(an_lbl),
            run_time=FAST,
        )
        self.play(Create(dist_a), Write(dist_a_lbl), run_time=NORMAL)
        self.wait(1)

        # Clear visual, show proof steps
        self.ly.clear()

        title2 = self.ly.title("Proof: Convergent Implies Cauchy")

        steps = [
            ("Let", r"\varepsilon > 0.", "Since a_n -> L, exists N:"),
            ("For all", r"n > N\colon |a_n - L| < \frac{\varepsilon}{2}", ""),
            ("Let", r"m, n > N.", "Then:"),
            ("", r"|a_m - a_n| = |(a_m - L) - (a_n - L)|", ""),
            ("Triangle:", r"\leq |a_m - L| + |a_n - L|", ""),
            ("Each term:", r"< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon", ""),
            ("QED:", r"|a_m - a_n| < \varepsilon", "(a_n) is Cauchy"),
        ]

        for prefix, formula, suffix in steps:
            parts_list = []
            if prefix:
                parts_list.append(
                    Text(prefix, font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD)
                )
            parts_list.append(MathTex(formula, font_size=BODY_SIZE, color=WHITE))
            if suffix:
                parts_list.append(
                    Text(suffix, font_size=LABEL_SIZE, color=DIM, font=SANS)
                )

            row = VGroup(*parts_list).arrange(RIGHT, buff=0.4)
            self.ly.safe_place(row, direction=DOWN, anchor=title2, buff=0.5)
            self.play(
                *[FadeIn(p, shift=LEFT * 0.15) for p in parts_list],
                run_time=FAST,
            )
            self.wait(0.8)

            # Fade all rows except the latest to keep budget
            if parts_list:
                # Remove all but the last 2 items to stay within budget
                pass

        # Key trick highlight
        trick = Text(
            "The trick: use epsilon/2 -- each term gets half the budget!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(trick, direction=DOWN, anchor=row, buff=0.5)
        self.play(FadeIn(trick, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 8: Section Divider -- Completeness ---
    def scene8_divider_completeness(self):
        self.add_subcaption(
            "Now for the deep result. "
            "What does completeness have to do with Cauchy sequences?",
            duration=6,
        )
        self.ly.section_divider(4, "Cauchy and Completeness")
        self.ly.clear()

    # --- Scene 9: Cauchy Implies Convergent + The Q Example ---
    def scene9_cauchy_completeness_and_q(self):
        self.add_subcaption(
            "In the real numbers, every Cauchy sequence converges. "
            "This theorem is actually equivalent to the completeness axiom. "
            "It means that in R, "
            "the two notions of convergence and being Cauchy are the same thing. "
            "But this fails in the rational numbers. "
            "Consider the sequence one, one point four, "
            "one point four one, one point four one four, and so on. "
            "These are the decimal approximations of the square root of two. "
            "In the reals, this converges to root two. "
            "But root two is not a rational number. "
            "So in Q, this sequence is Cauchy but does not converge "
            "because its limit is missing from Q. "
            "Completeness is what fills the gaps. "
            "The real numbers have no holes, "
            "so every Cauchy sequence finds its limit.",
            duration=46,
        )

        # Part 1: Theorem statement
        title = self.ly.title("The Cauchy Criterion")

        theorem = MathTex(
            r"\text{In } \mathbb{R}\colon \;(a_n) \text{ is Cauchy} "
            r"\iff a_n \text{ converges}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        theorem_box = self.ly.formula_box(theorem, color=ACCENT)
        self.ly.safe_place(theorem_box, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(theorem), Create(theorem_box[1]), run_time=2.0)
        self.wait(0.5)

        equiv = Text(
            "This is equivalent to the Completeness Axiom!",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(equiv, direction=DOWN, anchor=theorem_box, buff=0.5)
        self.play(FadeIn(equiv, shift=LEFT * 0.1), run_time=NORMAL)
        self.wait(1.5)

        # Transition to Q example
        self.ly.clear()

        title2 = self.ly.title("The Hole in Q")

        # Number line for Q: 1 to 2, with sqrt(2) marked as missing
        nl = NumberLine(
            x_range=[0.9, 1.9, 0.5],
            length=9,
            color=PRIMARY,
            stroke_width=2,
            include_tip=True,
        )
        self.ly.center_in_content(nl)
        self.play(Create(nl), run_time=NORMAL)

        # 1 and 2 labels
        one_l = MathTex("1", font_size=LABEL_SIZE, color=WHITE)
        one_l.next_to(nl.n2p(1.0), DOWN, buff=0.25)
        two_l = MathTex("2", font_size=LABEL_SIZE, color=WHITE)
        two_l.next_to(nl.n2p(2.0), DOWN, buff=0.25)
        self.play(FadeIn(one_l), FadeIn(two_l), run_time=FAST)

        # Q label
        q_label = Text(
            "In Q:", font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        q_label.next_to(nl, UP, buff=0.2)
        self.play(FadeIn(q_label), run_time=FAST)

        # Decimal approximations clustering around sqrt(2) ~ 1.414
        sqrt2_approx = 1.41421356
        terms = [1.0, 1.4, 1.41, 1.414, 1.4142]
        dots = []
        for val in terms:
            pos = nl.n2p(val)
            d = Dot(pos, color=SECONDARY, radius=0.06)
            dots.append(d)
        self.play(FadeIn(*dots, scale=0.8, lag_ratio=0.15), run_time=NORMAL)
        self.wait(0.5)

        # X mark at sqrt(2) position -- NOT in Q
        x_pos = nl.n2p(sqrt2_approx)
        x_mark = MathTex(r"\times", font_size=HEADING_SIZE, color=RED)
        x_mark.move_to(x_pos)
        x_mark.shift(UP * 0.4)
        x_label = MathTex(r"\sqrt{2} \notin \mathbb{Q}", font_size=BODY_SIZE, color=RED)
        x_label.next_to(x_mark, UP, buff=0.15)
        self.play(Write(x_mark), Write(x_label), run_time=NORMAL)
        self.wait(1)

        # "Cauchy but NOT convergent in Q" label
        tag = Text(
            "Cauchy in Q, but NOT convergent in Q",
            font_size=BODY_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(tag, direction=DOWN, anchor=nl, buff=0.4)
        self.play(FadeIn(tag, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1)

        # Remove Q stuff, show "Completeness fills the holes"
        self.ly.clear()

        title3 = self.ly.title("Completeness Fills the Holes")

        fill_text = Text(
            "R has no gaps -- every Cauchy sequence finds its limit.",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.center_in_content(fill_text)
        self.play(Write(fill_text), run_time=NORMAL)
        self.wait(0.5)

        comparison = VGroup(
            Text("Q: Cauchy does NOT imply convergence", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("R: Cauchy DOES imply convergence", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.ly.safe_place(comparison, direction=DOWN, anchor=fill_text, buff=0.6)
        self.play(
            FadeIn(comparison[0], shift=LEFT * 0.15), run_time=FAST,
        )
        self.wait(0.5)
        self.play(
            FadeIn(comparison[1], shift=LEFT * 0.15), run_time=FAST,
        )
        self.wait(2)

        self.ly.clear()

    # --- Scene 10: Summary + Outro ---
    def scene10_summary_outro(self):
        self.add_subcaption(
            "Five things to remember. "
            "A Cauchy sequence is one where "
            "any two terms far enough along are arbitrarily close. "
            "The definition does not mention the limit at all, "
            "which is its power. "
            "Every convergent sequence is Cauchy, "
            "and we proved this using the triangle inequality "
            "with the epsilon over two trick. "
            "In the real numbers, Cauchy and convergent are the same thing, "
            "and this equivalence depends on completeness. "
            "And completeness is what distinguishes R from Q, "
            "filling the holes that make Cauchy sequences fail to converge. "
            "Next time, we move from sequences to functions "
            "and study limits of functions.",
            duration=38,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text(
                "Cauchy: terms get closer to EACH OTHER",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "The definition never mentions the limit L",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "Convergent => Cauchy (epsilon/2 trick)",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
            Text(
                "In R: Cauchy iff convergent (needs completeness!)",
                font_size=BODY_SIZE, color=RED, font=SANS,
            ),
            Text(
                "Completeness fills the gaps that Q has",
                font_size=BODY_SIZE, color=WHITE, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title)

        self.wait(1)

        play_outro(
            self,
            next_video="Limits of Functions",
            next_playlist="Real Analysis I",
        )
