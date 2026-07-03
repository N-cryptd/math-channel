"""
Video 96: Proof by Cases
TEMPLATE v2 — Professional quality Manim script

Playlist: Introduction to Proofs (Video 7 of 9)
Class: Video96_ProofByCases

QUALITY RULES (enforced):
  1. Max 5 visible elements per scene at any time
  2. Use LayoutEngine for ALL positioning — no manual .shift() or .to_edge()
  3. Progressive disclosure: add items one at a time
  4. Use consistent animation vocabulary (Write, FadeIn, Create, etc.)
  5. Each add_subcaption() duration ≈ words / 2.5 seconds
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
from layout import LayoutEngine, ensure_fits


class Video96_ProofByCases(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_logical_structure()
        self.scene3_triggers()
        self.scene4_example_even_odd()
        self.scene5_example_absolute()
        self.scene6_example_mod3()
        self.scene7_summary()

    # ─── Scene 1: Hook — The Mystery Envelope ───
    def scene1_hook(self):
        self.add_subcaption(
            "Imagine someone hands you a sealed envelope with a number inside. "
            "They say prove that n squared minus n is always even. "
            "You cannot see the number, but you can still prove it, "
            "because there are only two possibilities: even or odd. "
            "That is proof by cases.",
            duration=16,
        )
        play_intro(self, "Proof by Cases", "Introduction to Proofs")

        # Mystery envelope visual
        envelope = VGroup(
            Rectangle(width=1.8, height=1.2, fill_color=DIM, fill_opacity=0.3,
                      stroke_color=PRIMARY, stroke_width=2),
            Text("?", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
        )
        envelope[1].move_to(envelope[0])

        # Two branching arrows
        case_even = Text("n is even", font_size=LABEL_SIZE, color=PRIMARY, font=SANS)
        case_odd = Text("n is odd", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)

        arrow_e = Arrow(envelope.get_right(), case_even.get_left() + RIGHT * 0.5,
                        buff=0.3, color=PRIMARY, stroke_width=2)
        arrow_o = Arrow(envelope.get_right(), case_odd.get_left() + RIGHT * 0.5,
                        buff=0.3, color=SECONDARY, stroke_width=2)

        # Conclusion badge
        conclusion = MathTex(
            r"n^2 - n \text{ is even}",
            font_size=BODY_SIZE, color=ACCENT,
        )

        # Layout: envelope center-left, cases branching right, conclusion bottom
        envelope.move_to(LEFT * 2 + UP * 0.5)
        case_even.move_to(RIGHT * 2.5 + UP * 1.0)
        case_odd.move_to(RIGHT * 2.5 + UP * -0.5)
        arrow_e.put_start_and_end_on(
            envelope.get_right(), case_even.get_left()
        )
        arrow_o.put_start_and_end_on(
            envelope.get_right(), case_odd.get_left()
        )
        conclusion.move_to(UP * -1.5)

        self.play(
            FadeIn(envelope, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(
            Create(arrow_e), FadeIn(case_even, shift=UP * 0.1),
            Create(arrow_o), FadeIn(case_odd, shift=DOWN * 0.1),
            run_time=NORMAL,
        )
        self.wait(0.5)
        self.play(Write(conclusion), run_time=FAST)
        self.wait(2)

        self.ly.clear()

    # ─── Scene 2: The Logical Structure ───
    def scene2_logical_structure(self):
        self.add_subcaption(
            "Proof by cases works when your hypothesis is a disjunction, "
            "an OR statement. If P1 or P2 or Pn, then R. "
            "You prove R under each case separately. "
            "For this to work, three things: your cases must cover every possibility, "
            "they must not overlap, and each case must independently lead to R.",
            duration=17,
        )

        title = self.ly.title("The Logical Structure")

        # Main formula
        formula = MathTex(
            r"(P_1 \lor P_2 \lor \cdots \lor P_n) \Longrightarrow R",
            font_size=LABEL_SIZE, color=WHITE,
        )
        self.ly.safe_place(formula, direction=DOWN, anchor=title, buff=0.4)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(0.5)

        # Decision tree visualization
        # Top node
        node_hyp = Circle(radius=0.35, fill_color=DIM, fill_opacity=0.5,
                           stroke_color=WHITE, stroke_width=1.5)
        hyp_text = Text("Hyp", font_size=SMALL_SIZE, color=WHITE, font=SANS)
        hyp_text.move_to(node_hyp)
        node_hyp.move_to(UP * 0.2)

        # Bottom node
        node_conc = Circle(radius=0.35, fill_color=ACCENT, fill_opacity=0.4,
                           stroke_color=ACCENT, stroke_width=1.5)
        conc_text = Text("R", font_size=SMALL_SIZE, color=WHITE, font=SANS)
        conc_text.move_to(node_conc)
        node_conc.move_to(DOWN * 2.0)

        # Case nodes
        node_p1 = Circle(radius=0.3, fill_color=PRIMARY, fill_opacity=0.4,
                          stroke_color=PRIMARY, stroke_width=1.5)
        p1_text = Text("P1", font_size=SMALL_SIZE, color=WHITE, font=SANS)
        p1_text.move_to(node_p1)
        node_p1.move_to(LEFT * 2.5 + DOWN * 0.9)

        node_p2 = Circle(radius=0.3, fill_color=SECONDARY, fill_opacity=0.4,
                          stroke_color=SECONDARY, stroke_width=1.5)
        p2_text = Text("P2", font_size=SMALL_SIZE, color=WHITE, font=SANS)
        p2_text.move_to(node_p2)
        node_p2.move_to(LEFT * 0.5 + DOWN * 0.9)

        node_pn = Circle(radius=0.3, fill_color=RED, fill_opacity=0.4,
                          stroke_color=RED, stroke_width=1.5)
        pn_text = Text("Pn", font_size=SMALL_SIZE, color=WHITE, font=SANS)
        pn_text.move_to(node_pn)
        node_pn.move_to(RIGHT * 1.5 + DOWN * 0.9)

        # Arrows
        arrow_h1 = Arrow(node_hyp.get_bottom(), node_p1.get_top(), buff=0.05,
                         color=PRIMARY, stroke_width=1.5)
        arrow_h2 = Arrow(node_hyp.get_bottom(), node_p2.get_top(), buff=0.05,
                         color=SECONDARY, stroke_width=1.5)
        arrow_hn = Arrow(node_hyp.get_bottom(), node_pn.get_top(), buff=0.05,
                         color=RED, stroke_width=1.5)
        arrow_1c = Arrow(node_p1.get_bottom(), node_conc.get_left(), buff=0.05,
                         color=PRIMARY, stroke_width=1.5)
        arrow_2c = Arrow(node_p2.get_bottom(), node_conc.get_top(), buff=0.05,
                         color=SECONDARY, stroke_width=1.5)
        arrow_nc = Arrow(node_pn.get_bottom(), node_conc.get_right(), buff=0.05,
                         color=RED, stroke_width=1.5)

        tree = VGroup(
            node_hyp, hyp_text, node_p1, p1_text, node_p2, p2_text,
            node_pn, pn_text, node_conc, conc_text,
            arrow_h1, arrow_h2, arrow_hn, arrow_1c, arrow_2c, arrow_nc,
        )
        self.ly.center_in_content(tree)

        self.play(Create(tree), run_time=NORMAL)
        self.wait(1)

        # Three requirements
        req1 = Text("1. Cases cover ALL possibilities", font_size=BODY_SIZE,
                    color=PRIMARY, font=SANS)
        req2 = Text("2. Cases are mutually EXCLUSIVE", font_size=BODY_SIZE,
                    color=SECONDARY, font=SANS)
        req3 = Text("3. Each case proves R independently", font_size=BODY_SIZE,
                    color=ACCENT, font=SANS)
        reqs = VGroup(req1, req2, req3).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        # Remove tree, show requirements
        self.play(FadeOut(tree), run_time=FAST)
        self.ly.safe_place(reqs, direction=DOWN, anchor=formula, buff=0.5)
        self.play(
            FadeIn(req1, shift=LEFT * 0.1),
            run_time=FAST,
        )
        self.play(FadeIn(req2, shift=LEFT * 0.1), run_time=FAST)
        self.play(FadeIn(req3, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 3: Common Case-Split Triggers ───
    def scene3_triggers(self):
        self.add_subcaption(
            "When do we reach for proof by cases? "
            "Whenever the universe naturally splits into categories. "
            "Parity, even or odd. "
            "Sign, positive, negative, or zero. "
            "Thresholds, less than, equal to, or greater than. "
            "Remainder classes. "
            "This is the same logic behind if-else statements in programming.",
            duration=16,
        )

        title = self.ly.title("Common Case-Split Triggers")

        triggers = [
            Text("Parity:  even / odd", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Sign:  positive / negative / zero", font_size=BODY_SIZE,
                 color=SECONDARY, font=SANS),
            Text("Thresholds:  x < a,  x = a,  x > a", font_size=BODY_SIZE,
                 color=ACCENT, font=SANS),
            Text("Remainder classes:  n mod 3 in {0, 1, 2}", font_size=BODY_SIZE,
                 color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(triggers, start_from=title)
        self.wait(1)

        # Programming connection
        code_label = Text("In code:  if / elif / else", font_size=BODY_SIZE,
                          color=DIM, font=MONO)
        self.ly.safe_place(code_label, direction=DOWN, anchor=triggers[-1], buff=0.5)
        self.play(FadeIn(code_label, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 4: Example 1 — n^2 - n is Always Even ───
    def scene4_example_even_odd(self):
        self.add_subcaption(
            "Let us prove that for all integers n, "
            "n squared minus n is always even. "
            "We split into two cases. "
            "Case 1: n is even. Write n equals 2k. "
            "Then n squared minus n equals 4k squared minus 2k, "
            "which factors as 2 times 2k squared minus k. That is even. "
            "Case 2: n is odd. Write n equals 2k plus 1. "
            "Then n squared minus n equals 4k squared plus 2k, "
            "which is 2 times 2k squared plus k. Also even. "
            "In both cases the result is even. Q.E.D.",
            duration=24,
        )

        self.ly.section_divider(1, "Example 1: n^2 - n is Even")

        title = self.ly.title("Prove: n^2 - n is even for all integers n")

        # Claim
        claim = MathTex(
            r"\forall\, n \in \mathbb{Z},\; n^2 - n \text{ is even}",
            font_size=LABEL_SIZE, color=WHITE,
        )
        self.ly.safe_place(claim, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(claim), run_time=FAST)
        self.wait(0.5)

        # Case 1: n is even
        case1_label = Text("Case 1: n is even (n = 2k)", font_size=LABEL_SIZE,
                           color=PRIMARY, font=SANS)
        self.ly.safe_place(case1_label, direction=DOWN, anchor=claim, buff=0.4)
        self.play(FadeIn(case1_label, shift=LEFT * 0.1), run_time=FAST)

        case1_work = MathTex(
            r"n^2 - n = (2k)^2 - 2k = 4k^2 - 2k = 2(2k^2 - k)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(case1_work, direction=DOWN, anchor=case1_label, buff=0.2)
        self.play(Write(case1_work), run_time=NORMAL)
        self.wait(0.5)

        case1_done = Text("Even! (factor of 2)", font_size=BODY_SIZE,
                          color=SECONDARY, font=SANS)
        self.ly.safe_place(case1_done, direction=DOWN, anchor=case1_work, buff=0.2)
        self.play(FadeIn(case1_done, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1)

        # Transition: remove Case 1 work, show Case 2
        self.play(
            FadeOut(case1_work), FadeOut(case1_done),
            run_time=FAST,
        )

        # Case 2: n is odd
        case2_label = Text("Case 2: n is odd (n = 2k + 1)", font_size=LABEL_SIZE,
                           color=SECONDARY, font=SANS)
        self.ly.safe_place(case2_label, direction=DOWN, anchor=case1_label, buff=0.3)
        self.play(FadeIn(case2_label, shift=LEFT * 0.1), run_time=FAST)

        case2_work = MathTex(
            r"n^2 - n = (2k{+}1)^2 - (2k{+}1) = 4k^2 + 2k = 2(2k^2 + k)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(case2_work, direction=DOWN, anchor=case2_label, buff=0.2)
        self.play(Write(case2_work), run_time=NORMAL)
        self.wait(0.5)

        case2_done = Text("Even! (factor of 2)", font_size=BODY_SIZE,
                          color=SECONDARY, font=SANS)
        self.ly.safe_place(case2_done, direction=DOWN, anchor=case2_work, buff=0.2)
        self.play(FadeIn(case2_done, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1)

        # QED
        qed = MathTex(r"\blacksquare", font_size=HEADING_SIZE, color=ACCENT)
        self.ly.safe_place(qed, direction=DOWN, anchor=case2_done, buff=0.3)
        self.play(Write(qed), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 5: Example 2 — Absolute Value Inequality ───
    def scene5_example_absolute(self):
        self.add_subcaption(
            "Example 2. Prove that for all real x, "
            "the absolute value of 2x minus 1 is at least 2x minus 1. "
            "The absolute value always forces a case split at zero. "
            "Case 1: 2x minus 1 is non-negative. "
            "Then the absolute value equals 2x minus 1, "
            "so the inequality is trivially true. "
            "Case 2: 2x minus 1 is negative. "
            "Then the absolute value is 1 minus 2x, which is positive, "
            "and that is always greater than a negative number. Q.E.D.",
            duration=24,
        )

        self.ly.section_divider(2, "Example 2: Absolute Value Inequality")

        title = self.ly.title("Prove: |2x - 1| >= 2x - 1  for all real x")

        # Claim
        claim = MathTex(
            r"\forall\, x \in \mathbb{R},\; |2x - 1| \ge 2x - 1",
            font_size=LABEL_SIZE, color=WHITE,
        )
        self.ly.safe_place(claim, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(claim), run_time=FAST)
        self.wait(0.5)

        # Number line with split point
        line = NumberLine(
            x_range=[-3, 3, 1], length=6,
            color=DIM, stroke_width=1.5,
            include_numbers=True,
        )
        split_dot = Dot(line.n2p(0), color=ACCENT, radius=0.06)
        split_label = Text("x = 1/2", font_size=SMALL_SIZE, color=ACCENT, font=SANS)
        split_label.next_to(split_dot, UP, buff=0.15)

        # Color the zones
        zone_right = line.copy().set_color(PRIMARY)
        zone_right.get_pieces_by_x_values(0, 3).set_color(PRIMARY)
        zone_right.get_pieces_by_x_values(-3, 0).set_opacity(0.2)
        zone_right.set_opacity(0.3)

        self.ly.safe_place(line, direction=DOWN, anchor=claim, buff=0.4)
        self.play(Create(line), run_time=NORMAL)
        self.play(
            FadeIn(split_dot), Write(split_label),
            run_time=FAST,
        )

        right_label = Text(">= 0", font_size=SMALL_SIZE, color=PRIMARY, font=SANS)
        right_label.next_to(line.n2p(2), UP, buff=0.15)
        self.play(Write(right_label), run_time=FAST)
        self.wait(0.5)

        self.play(FadeOut(line), FadeOut(split_dot), FadeOut(split_label),
                  FadeOut(right_label), run_time=FAST)

        # Case 1
        case1_label = Text("Case 1: 2x - 1 >= 0  (x >= 1/2)", font_size=LABEL_SIZE,
                           color=PRIMARY, font=SANS)
        self.ly.safe_place(case1_label, direction=DOWN, anchor=claim, buff=0.4)
        self.play(FadeIn(case1_label, shift=LEFT * 0.1), run_time=FAST)

        case1_work = MathTex(
            r"|2x - 1| = 2x - 1 \ge 2x - 1 \quad \checkmark",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(case1_work, direction=DOWN, anchor=case1_label, buff=0.2)
        self.play(Write(case1_work), run_time=NORMAL)
        self.wait(1)

        self.play(FadeOut(case1_work), run_time=FAST)

        # Case 2
        case2_label = Text("Case 2: 2x - 1 < 0  (x < 1/2)", font_size=LABEL_SIZE,
                           color=SECONDARY, font=SANS)
        self.ly.safe_place(case2_label, direction=DOWN, anchor=case1_label, buff=0.3)
        self.play(FadeIn(case2_label, shift=LEFT * 0.1), run_time=FAST)

        case2_work = MathTex(
            r"|2x-1| = -(2x-1) = 1-2x > 0 > 2x-1 \quad \checkmark",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(case2_work, direction=DOWN, anchor=case2_label, buff=0.2)
        self.play(Write(case2_work), run_time=NORMAL)
        self.wait(0.5)

        qed = MathTex(r"\blacksquare", font_size=HEADING_SIZE, color=ACCENT)
        self.ly.safe_place(qed, direction=DOWN, anchor=case2_work, buff=0.3)
        self.play(Write(qed), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 6: Example 3 — n^2 mod 3 ───
    def scene6_example_mod3(self):
        self.add_subcaption(
            "Example 3. Prove that for all integers n, "
            "n squared leaves remainder 0 or 1 when divided by 3. "
            "Every integer falls into one of three residue classes modulo 3. "
            "Case 1: n equals 3k. Then n squared equals 9k squared, "
            "remainder 0. "
            "Case 2: n equals 3k plus 1. Then n squared equals "
            "9k squared plus 6k plus 1, remainder 1. "
            "Case 3: n equals 3k plus 2. Then n squared equals "
            "9k squared plus 12k plus 4, remainder 4 equals 1. "
            "So n squared is either 0 or 1 modulo 3, never 2. Q.E.D.",
            duration=26,
        )

        self.ly.section_divider(3, "Example 3: n^2 mod 3")

        title = self.ly.title("Prove: n^2 = 0 or 1 (mod 3) for all integers n")

        # Claim
        claim = MathTex(
            r"\forall\, n \in \mathbb{Z},\; n^2 \equiv 0 \text{ or } 1 \pmod{3}",
            font_size=LABEL_SIZE, color=WHITE,
        )
        self.ly.safe_place(claim, direction=DOWN, anchor=title, buff=0.3)
        self.play(Write(claim), run_time=FAST)
        self.wait(0.5)

        # Case 1
        case1_label = Text("Case 1: n = 3k", font_size=LABEL_SIZE,
                           color=PRIMARY, font=SANS)
        self.ly.safe_place(case1_label, direction=DOWN, anchor=claim, buff=0.4)
        self.play(FadeIn(case1_label, shift=LEFT * 0.1), run_time=FAST)

        case1_work = MathTex(
            r"n^2 = (3k)^2 = 9k^2 \equiv 0 \pmod{3} \quad \checkmark",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(case1_work, direction=DOWN, anchor=case1_label, buff=0.2)
        self.play(Write(case1_work), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(case1_work), run_time=FAST)

        # Case 2
        case2_label = Text("Case 2: n = 3k + 1", font_size=LABEL_SIZE,
                           color=SECONDARY, font=SANS)
        self.ly.safe_place(case2_label, direction=DOWN, anchor=case1_label, buff=0.3)
        self.play(FadeIn(case2_label, shift=LEFT * 0.1), run_time=FAST)

        case2_work = MathTex(
            r"n^2 = 9k^2 + 6k + 1 \equiv 1 \pmod{3} \quad \checkmark",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(case2_work, direction=DOWN, anchor=case2_label, buff=0.2)
        self.play(Write(case2_work), run_time=NORMAL)
        self.wait(0.5)

        self.play(FadeOut(case2_work), run_time=FAST)

        # Case 3
        case3_label = Text("Case 3: n = 3k + 2", font_size=LABEL_SIZE,
                           color=ACCENT, font=SANS)
        self.ly.safe_place(case3_label, direction=DOWN, anchor=case2_label, buff=0.3)
        self.play(FadeIn(case3_label, shift=LEFT * 0.1), run_time=FAST)

        case3_work = MathTex(
            r"n^2 = 9k^2 + 12k + 4 \equiv 4 \equiv 1 \pmod{3} \quad \checkmark",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(case3_work, direction=DOWN, anchor=case3_label, buff=0.2)
        self.play(Write(case3_work), run_time=NORMAL)
        self.wait(0.5)

        # Key insight
        insight = Text(
            "n^2 is NEVER congruent to 2 (mod 3)!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=case3_work, buff=0.3)
        self.play(FadeIn(insight, shift=LEFT * 0.1), run_time=FAST)
        self.wait(0.5)

        qed = MathTex(r"\blacksquare", font_size=HEADING_SIZE, color=ACCENT)
        self.ly.safe_place(qed, direction=DOWN, anchor=insight, buff=0.3)
        self.play(Write(qed), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 7: Summary ───
    def scene7_summary(self):
        self.add_subcaption(
            "To summarize, proof by cases splits your hypothesis "
            "into exhaustive, mutually exclusive cases. "
            "Each case independently proves the conclusion. "
            "This is the same logic as if-elif-else in programming. "
            "The keys: make sure your cases cover everything, "
            "do not overlap, and each one independently gets you to the conclusion. "
            "Next up, existence and uniqueness proofs.",
            duration=18,
        )

        title = self.ly.title("Proof by Cases — Summary")

        items = [
            Text("Split hypothesis into exhaustive, exclusive cases",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Each case independently proves the conclusion",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Same as if / elif / else in code",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Cases must be EXHAUSTIVE (cover all) and EXCLUSIVE (no overlap)",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        key = Text(
            "When in doubt, split it up!",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=items[-1], buff=0.5)
        self.play(FadeIn(key, shift=LEFT * 0.1), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

        play_outro(self, "Existence and Uniqueness Proofs", "Introduction to Proofs")
