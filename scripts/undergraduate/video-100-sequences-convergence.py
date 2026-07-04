"""
Video 100: Sequences and Convergence
TEMPLATE v2 -- Professional quality Manim script

Playlist: Real Analysis I (Video 2 of 12)
Class: Video100_SequencesConvergence

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


class Video100_SequencesConvergence(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_intro()
        self.scene3_what_is_a_sequence()
        self.scene4_divider_intuition()
        self.scene5_intuitive_convergence()
        self.scene6_divider_definition()
        self.scene7_formal_definition()
        self.scene8_proof_example()
        self.scene9_rules_and_outro()

    # --- Scene 1: Hook -- The Dance of Dots ---
    def scene1_hook(self):
        self.add_subcaption(
            "You have been using limits since your first calculus course. "
            "A sequence converges to a limit. "
            "But what does that actually mean? "
            "The terms get closer and closer, yes, "
            "but closer in what sense? "
            "And how close is close enough? "
            "In real analysis, we replace that vague intuition "
            "with a definition that is as precise as it is powerful. "
            "Today we study sequences and convergence.",
            duration=24,
        )
        play_intro(self, "Sequences and Convergence", "Real Analysis I")

        title = self.ly.title("The Dance of Dots")

        # Number line centered
        nl = NumberLine(
            x_range=[-0.3, 1.3, 0.5],
            length=10,
            color=PRIMARY,
            stroke_width=2,
            include_tip=True,
        )
        self.ly.center_in_content(nl)
        self.play(Create(nl), run_time=NORMAL)

        # Zero label
        zero_label = MathTex("0", font_size=LABEL_SIZE, color=WHITE)
        zero_label.next_to(nl.n2p(0), DOWN, buff=0.25)
        one_label = MathTex("1", font_size=LABEL_SIZE, color=WHITE)
        one_label.next_to(nl.n2p(1), DOWN, buff=0.25)
        self.play(FadeIn(zero_label), FadeIn(one_label), run_time=FAST)
        self.wait(0.3)

        # Place dots progressively: 1, 1/2, 1/3, 1/4, 1/5, 1/6
        terms = [1.0, 0.5, 1/3, 0.25, 0.2, 1/6]
        dots = []
        for val in terms:
            d = Dot(nl.n2p(val), color=SECONDARY, radius=0.07)
            dots.append(d)
            self.play(FadeIn(d, scale=0.8), run_time=0.5)
            self.wait(0.2)

        self.wait(0.5)

        # Question
        question = Text(
            "How do we make 'getting closer' precise?",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(question, direction=UP, anchor=nl, buff=0.5)
        self.play(FadeIn(question, shift=UP * 0.1), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 2: Intro + Section Divider ---
    def scene2_intro(self):
        self.add_subcaption(
            "We begin with a question that motivates the most "
            "important definition in analysis. "
            "What does it mean for an infinite list of numbers "
            "to converge to a single value?",
            duration=10,
        )
        self.ly.section_divider(1, "What is a Sequence?")
        self.ly.clear()

    # --- Scene 3: What is a Sequence? ---
    def scene3_what_is_a_sequence(self):
        self.add_subcaption(
            "A sequence is simply a function from the natural numbers "
            "to the real numbers. "
            "We write a sub n for the value at position n. "
            "The first few terms are a sub one, a sub two, a sub three, and so on. "
            "Here are three examples. "
            "One over n gives the sequence one, one half, one third, and so on. "
            "Negative one to the n alternates between negative one and one. "
            "And n plus one over n starts at two and decreases toward one. "
            "The key point is that order matters. "
            "A sequence is not a set. The positions one, two, three are fixed, "
            "and each position has exactly one value.",
            duration=34,
        )

        title = self.ly.title("What is a Sequence?")

        # Definition as function
        func_def = MathTex(
            r"a \colon \mathbb{N} \to \mathbb{R}, \quad n \mapsto a_n",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(func_def, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(func_def), run_time=NORMAL)
        self.wait(1)

        # Fade function def, show examples progressively
        self.play(FadeOut(func_def), run_time=0.3)

        examples = [
            MathTex(r"a_n = \frac{1}{n}", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"b_n = (-1)^n", font_size=BODY_SIZE, color=PRIMARY),
            MathTex(r"c_n = \frac{n+1}{n}", font_size=BODY_SIZE, color=ACCENT),
        ]

        values = [
            Text("1, 1/2, 1/3, 1/4, ...", font_size=LABEL_SIZE, color=DIM, font=MONO),
            Text("-1, 1, -1, 1, ...", font_size=LABEL_SIZE, color=DIM, font=MONO),
            Text("2, 3/2, 4/3, 5/4, ...", font_size=LABEL_SIZE, color=DIM, font=MONO),
        ]

        pairs = []
        for ex, val in zip(examples, values):
            pair = VGroup(ex, val).arrange(RIGHT, buff=0.5)
            pairs.append(pair)

        # Reveal pairs progressively
        for i, pair in enumerate(pairs):
            if i == 0:
                self.ly.safe_place(pair, direction=DOWN, anchor=title, buff=0.5)
            else:
                self.ly.safe_place(pair, direction=DOWN, anchor=pairs[i - 1], buff=0.35)
            self.play(FadeIn(pair, shift=LEFT * 0.15), run_time=FAST)
            self.wait(0.5)

        # "Order matters" note
        order_note = Text(
            "Order matters -- a sequence is not a set!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(order_note, direction=DOWN, anchor=pairs[-1], buff=0.4)
        self.play(FadeIn(order_note, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 4: Section Divider -- Intuition ---
    def scene4_divider_intuition(self):
        self.add_subcaption(
            "Before writing the formal definition, "
            "let us build intuition with pictures.",
            duration=5,
        )
        self.ly.section_divider(2, "What Does Convergence Mean?")
        self.ly.clear()

    # --- Scene 5: Intuitive Convergence ---
    def scene5_intuitive_convergence(self):
        self.add_subcaption(
            "Look at the sequence one over n. "
            "The terms are one, one half, one third, one fourth, and so on. "
            "They are clearly approaching zero. "
            "No matter how small a band you draw around zero, "
            "eventually all the terms fall inside it. That is convergence. "
            "Now compare with the sequence negative one to the n. "
            "The terms bounce between negative one and one forever. "
            "They never settle. That is divergence. "
            "The key insight is this. "
            "A sequence converges to a number L "
            "if its terms eventually stay within "
            "any arbitrarily small band around L. "
            "No matter how tight you make the band, "
            "from some point onward, every term is inside.",
            duration=36,
        )

        title = self.ly.title("Convergence vs Divergence")

        # Number line for convergent sequence
        nl_conv = NumberLine(
            x_range=[-0.2, 1.3, 0.5],
            length=9,
            color=PRIMARY,
            stroke_width=2,
            include_tip=True,
        )
        conv_label = Text("a_n = 1/n", font_size=LABEL_SIZE, color=SECONDARY, font=MONO)
        conv_label.next_to(nl_conv, UP, buff=0.2)
        conv_group = VGroup(conv_label, nl_conv)
        self.ly.center_in_content(conv_group)

        self.play(Create(nl_conv), FadeIn(conv_label), run_time=NORMAL)

        # Zero marker
        zl = MathTex("0", font_size=LABEL_SIZE, color=ACCENT)
        zl.next_to(nl_conv.n2p(0), DOWN, buff=0.25)
        self.play(FadeIn(zl), run_time=FAST)

        # Place convergent dots
        conv_terms = [1.0, 0.5, 1/3, 0.25, 0.2, 0.15, 0.12, 0.1]
        conv_dots = []
        for val in conv_terms:
            d = Dot(nl_conv.n2p(val), color=SECONDARY, radius=0.06)
            conv_dots.append(d)
        self.play(FadeIn(*conv_dots, scale=0.8, lag_ratio=0.15), run_time=NORMAL)
        self.wait(0.5)

        # Epsilon band around 0 (highlighted region)
        epsilon_band = Line(
            nl_conv.n2p(-0.15),
            nl_conv.n2p(0.15),
            color=SECONDARY,
            stroke_width=8,
        )
        epsilon_label = MathTex(r"\varepsilon", font_size=LABEL_SIZE, color=SECONDARY)
        epsilon_label.next_to(epsilon_band.get_right(), RIGHT, buff=0.1)
        self.play(Create(epsilon_band), FadeIn(epsilon_label), run_time=FAST)
        self.wait(0.5)

        # "Converges" label
        conv_tag = Text(
            "Terms cluster around 0 -- CONVERGES",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(conv_tag, direction=DOWN, anchor=nl_conv, buff=0.4)
        self.play(FadeIn(conv_tag, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1)

        # Clear and show divergent sequence
        self.ly.clear()

        title2 = self.ly.title("Divergence: Terms Never Settle")

        # Divergent sequence number line
        nl_div = NumberLine(
            x_range=[-1.8, 1.8, 1],
            length=9,
            color=PRIMARY,
            stroke_width=2,
            include_tip=True,
        )
        div_label = Text("b_n = (-1)^n", font_size=LABEL_SIZE, color=RED, font=MONO)
        div_label.next_to(nl_div, UP, buff=0.2)
        div_group = VGroup(div_label, nl_div)
        self.ly.center_in_content(div_group)
        self.play(Create(nl_div), FadeIn(div_label), run_time=NORMAL)

        # Alternating dots
        div_dots_pos = VGroup(*[
            Dot(nl_div.n2p(1), color=RED, radius=0.08)
        ])
        div_dots_neg = VGroup(*[
            Dot(nl_div.n2p(-1), color=RED, radius=0.08)
        ])
        self.play(FadeIn(div_dots_neg, scale=0.8), run_time=FAST)
        self.wait(0.3)
        self.play(FadeIn(div_dots_pos, scale=0.8), run_time=FAST)
        self.wait(0.3)
        # Repeat to show bouncing
        self.play(FadeOut(div_dots_neg), run_time=0.2)
        self.wait(0.3)
        self.play(FadeIn(div_dots_neg, scale=0.8), run_time=0.2)
        self.wait(0.3)
        self.play(FadeOut(div_dots_pos), run_time=0.2)
        self.wait(0.3)
        self.play(FadeIn(div_dots_pos, scale=0.8), run_time=0.2)
        self.wait(0.5)

        # Labels
        neg_label = MathTex("-1", font_size=LABEL_SIZE, color=WHITE)
        neg_label.next_to(nl_div.n2p(-1), DOWN, buff=0.25)
        pos_label = MathTex("1", font_size=LABEL_SIZE, color=WHITE)
        pos_label.next_to(nl_div.n2p(1), DOWN, buff=0.25)
        self.play(FadeIn(neg_label), FadeIn(pos_label), run_time=FAST)

        div_tag = Text(
            "Terms bounce between -1 and 1 -- DIVERGES",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(div_tag, direction=DOWN, anchor=nl_div, buff=0.4)
        self.play(FadeIn(div_tag, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 6: Section Divider -- Formal Definition ---
    def scene6_divider_definition(self):
        self.add_subcaption(
            "Now we translate our visual intuition "
            "into the precise language of real analysis.",
            duration=5,
        )
        self.ly.section_divider(3, "The Epsilon-N Definition")
        self.ly.clear()

    # --- Scene 7: The Formal Definition ---
    def scene7_formal_definition(self):
        self.add_subcaption(
            "The epsilon-N definition is the foundation of convergence. "
            "We say the sequence a sub n converges to L "
            "if for every epsilon greater than zero, "
            "there exists a natural number N "
            "such that for all n greater than N, "
            "the absolute value of a sub n minus L is less than epsilon. "
            "Epsilon is how close we demand the terms to be. "
            "N is how far along the sequence we need to go. "
            "Think of it this way: "
            "you challenge the sequence with a tiny epsilon. "
            "The sequence responds with an N, "
            "a point beyond which all terms are within epsilon of L. "
            "If it can always do this, the sequence converges.",
            duration=34,
        )

        title = self.ly.title("The Formal Definition")

        # Visual: number line with L, epsilon band, N marker
        nl = NumberLine(
            x_range=[-1, 3, 1],
            length=10,
            color=PRIMARY,
            stroke_width=2,
            include_tip=True,
        )
        self.ly.center_in_content(nl)
        self.play(Create(nl), run_time=NORMAL)

        # L point
        l_point = nl.n2p(1.5)
        l_dot = Dot(l_point, color=ACCENT, radius=0.09)
        l_label = MathTex("L", font_size=HEADING_SIZE, color=ACCENT)
        l_label.next_to(l_dot, UP, buff=0.25)
        self.play(FadeIn(l_dot), Write(l_label), run_time=NORMAL)
        self.wait(0.5)

        # Epsilon band
        eps_left = nl.n2p(1.5 - 0.4)
        eps_right = nl.n2p(1.5 + 0.4)
        eps_band = Line(eps_left, eps_right, color=SECONDARY, stroke_width=10)
        eps_label = MathTex(r"\varepsilon", font_size=LABEL_SIZE, color=SECONDARY)
        eps_label.next_to(eps_band, UP, buff=0.15)
        self.play(Create(eps_band), FadeIn(eps_label), run_time=FAST)
        self.wait(0.5)

        # N marker on the number line
        n_pos = nl.n2p(0.3)
        n_line = DashedLine(
            n_pos + UP * 0.4,
            n_pos + DOWN * 0.4,
            color=RED,
            stroke_width=2,
        )
        n_marker = MathTex("N", font_size=LABEL_SIZE, color=RED)
        n_marker.next_to(n_line, DOWN, buff=0.15)
        self.play(Create(n_line), FadeIn(n_marker), run_time=FAST)
        self.wait(0.3)

        # Terms before N (scattered, some outside band)
        pre_terms = [nl.n2p(0.0), nl.n2p(0.1), nl.n2p(0.2)]
        pre_dots = VGroup(*[
            Dot(p, color=DIM, radius=0.05)
            for p in pre_terms
        ])
        self.play(FadeIn(pre_dots, scale=0.8), run_time=FAST)

        # Terms after N (inside band)
        post_vals = [1.3, 1.6, 1.4, 1.7, 1.35, 1.55, 1.45]
        post_dots = VGroup(*[
            Dot(nl.n2p(v), color=SECONDARY, radius=0.06)
            for v in post_vals
        ])
        self.play(FadeIn(post_dots, scale=0.8, lag_ratio=0.1), run_time=NORMAL)
        self.wait(0.5)

        # "All terms after N are inside" label
        tail_label = Text(
            "All n > N: terms inside the band",
            font_size=SMALL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(tail_label, direction=DOWN, anchor=nl, buff=0.4)
        self.play(FadeIn(tail_label, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1)

        # Clear visual, show formal definition
        self.ly.clear()

        title2 = self.ly.title("The Epsilon-N Definition")

        # Build definition step by step
        def_part1 = MathTex(
            r"a_n \to L",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(def_part1, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(def_part1), run_time=NORMAL)
        self.wait(0.5)

        # Full definition
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
            r"n > N \implies |a_n - L| < \varepsilon",
            font_size=HEADING_SIZE, color=WHITE,
        )
        cond_box = self.ly.formula_box(condition, color=ACCENT)
        self.ly.safe_place(cond_box, direction=DOWN, anchor=full_def, buff=0.5)
        self.play(Write(condition), Create(cond_box[1]), run_time=2.0)
        self.wait(1)

        # Part-by-part explanation
        parts = [
            (r"\varepsilon", "How close we demand the terms to be", SECONDARY),
            (r"N", "How far along the sequence we need to go", RED),
            (r"n > N", "All terms beyond this point", PRIMARY),
            (r"|a_n - L| < \varepsilon", "Distance from term to L is less than epsilon", ACCENT),
        ]

        # Fade the definition elements
        self.play(FadeOut(full_def), FadeOut(cond_box), run_time=0.4)

        for sym, desc, col in parts:
            row = VGroup(
                MathTex(sym, font_size=BODY_SIZE, color=col),
                Text(desc, font_size=BODY_SIZE, color=WHITE, font=SANS),
            ).arrange(RIGHT, buff=0.5)
            if not hasattr(self, '_part_rows'):
                self._part_rows = []
                self.ly.safe_place(row, direction=DOWN, anchor=title2, buff=0.5)
            else:
                self.ly.safe_place(row, direction=DOWN, anchor=self._part_rows[-1], buff=0.3)
            self._part_rows.append(row)
            self.play(FadeIn(row, shift=LEFT * 0.15), run_time=FAST)
            self.wait(0.5)
            # Keep budget: fade oldest if > 4 visible
            if len(self._part_rows) > 4:
                old = self._part_rows.pop(0)
                self.play(FadeOut(old), run_time=0.3)

        del self._part_rows
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 8: Proof Example -- 1/n Converges to 0 ---
    def scene8_proof_example(self):
        self.add_subcaption(
            "Let us prove that the sequence one over n "
            "converges to zero using the epsilon-N definition. "
            "We need to show: "
            "for every epsilon greater than zero, "
            "there exists N such that for all n greater than N, "
            "the absolute value of one over n is less than epsilon. "
            "Simplify: one over n is always positive, "
            "so we need one over n less than epsilon. "
            "Rearranging, this means n greater than one over epsilon. "
            "So we choose N to be any integer larger than one over epsilon. "
            "Then for every n greater than N, "
            "we have n greater than one over epsilon, "
            "which gives one over n less than epsilon. "
            "The proof is complete. "
            "One over n converges to zero.",
            duration=34,
        )

        title = self.ly.title("Proof: 1/n Converges to 0")

        # Claim
        claim = MathTex(
            r"\lim_{n \to \infty} \frac{1}{n} = 0",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(claim, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(claim), run_time=NORMAL)
        self.wait(0.5)

        # Proof steps -- reveal progressively, replacing old
        steps = [
            ("Let", r"\varepsilon > 0.", "We need to find N such that:"),
            ("Want:", r"\left| \frac{1}{n} - 0 \right| < \varepsilon", "for all n > N"),
            ("Simplify:", r"\frac{1}{n} < \varepsilon", "which means:"),
            ("Rearrange:", r"n > \frac{1}{\varepsilon}", "So choose:"),
            ("Choose:", r"N = \left\lceil \frac{1}{\varepsilon} \right\rceil + 1", ""),
            ("Then n > N:", r"n > \frac{1}{\varepsilon}", ""),
            ("Therefore:", r"\frac{1}{n} < \varepsilon", ""),
            ("QED:", r"\frac{1}{n} \to 0", ""),
        ]

        step_mobjects = []

        for prefix, formula, suffix in steps:
            self.ly.clear()
            title2 = self.ly.title("Proof: 1/n Converges to 0")

            # Build row
            parts_list = []
            if prefix:
                parts_list.append(Text(prefix, font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD))
            parts_list.append(MathTex(formula, font_size=BODY_SIZE, color=WHITE))
            if suffix:
                parts_list.append(Text(suffix, font_size=LABEL_SIZE, color=DIM, font=SANS))

            row = VGroup(*parts_list).arrange(RIGHT, buff=0.4)
            self.ly.safe_place(row, direction=DOWN, anchor=title2, buff=0.5)
            self.play(
                *[FadeIn(p, shift=LEFT * 0.15) for p in parts_list],
                run_time=NORMAL,
            )
            self.wait(1)

        # Final "QED" in accent color -- keep on screen a moment
        qed = Text(
            "Proof complete: 1/n converges to 0.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(qed, direction=DOWN, anchor=row, buff=0.5)
        self.play(FadeIn(qed, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # --- Scene 9: Convergence Rules + Outro ---
    def scene9_rules_and_outro(self):
        self.add_subcaption(
            "A few basic rules. "
            "Constant sequences trivially converge to their constant value. "
            "If a sequence converges to L, "
            "multiplying by a constant k gives convergence to k times L. "
            "And if two sequences converge, "
            "their sum converges to the sum of their limits. "
            "Three things to remember from today. "
            "A sequence is a function from the natural numbers to the reals. "
            "Convergence means the terms cluster around a single limit value. "
            "And the epsilon-N definition "
            "is the precise formulation of arbitrarily close. "
            "In the next video, we meet Cauchy sequences, "
            "a powerful tool for proving convergence "
            "without knowing the limit in advance.",
            duration=30,
        )

        title = self.ly.title("Basic Convergence Rules")

        # Rule 1: Constant sequences
        rule1 = VGroup(
            MathTex(r"c_n = c", font_size=BODY_SIZE, color=SECONDARY),
            Text("converges to", font_size=LABEL_SIZE, color=DIM, font=SANS),
            MathTex(r"c", font_size=BODY_SIZE, color=SECONDARY),
        ).arrange(RIGHT, buff=0.3)
        self.ly.safe_place(rule1, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(rule1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Rule 2: Scalar multiple
        rule2 = VGroup(
            MathTex(r"a_n \to L", font_size=BODY_SIZE, color=PRIMARY),
            Text("then", font_size=LABEL_SIZE, color=DIM, font=SANS),
            MathTex(r"k \cdot a_n \to kL", font_size=BODY_SIZE, color=PRIMARY),
        ).arrange(RIGHT, buff=0.3)
        self.ly.safe_place(rule2, direction=DOWN, anchor=rule1, buff=0.4)
        self.play(FadeIn(rule2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        # Rule 3: Sum
        rule3 = VGroup(
            MathTex(r"a_n \to L,", font_size=BODY_SIZE, color=ACCENT),
            MathTex(r"b_n \to M", font_size=BODY_SIZE, color=ACCENT),
            Text("then", font_size=LABEL_SIZE, color=DIM, font=SANS),
            MathTex(r"a_n + b_n \to L + M", font_size=BODY_SIZE, color=ACCENT),
        ).arrange(RIGHT, buff=0.3)
        self.ly.safe_place(rule3, direction=DOWN, anchor=rule2, buff=0.4)
        self.play(FadeIn(rule3, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        self.ly.clear()

        # Key takeaways
        title2 = self.ly.title("Key Takeaways")

        takeaways = [
            Text(
                "A sequence is a function from N to R.",
                font_size=BODY_SIZE, color=PRIMARY, font=SANS,
            ),
            Text(
                "Convergence: terms cluster around a limit L.",
                font_size=BODY_SIZE, color=SECONDARY, font=SANS,
            ),
            Text(
                "The epsilon-N definition makes this precise.",
                font_size=BODY_SIZE, color=ACCENT, font=SANS,
            ),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title2)

        self.wait(1)

        play_outro(
            self,
            next_video="Cauchy Sequences",
            next_playlist="Real Analysis I",
        )
