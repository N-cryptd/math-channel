"""
Video 93: Proof by Contradiction
Introduction to Proofs -- Video 4 of 9 (Proof-Based Mathematics, L4)

Covers: The logic of proof by contradiction (assume P and not Q, derive False),
when to use contradiction vs direct or contrapositive, two classic examples
(sqrt(2) irrational, infinitude of primes), and the distinction from
contrapositive (linking back to Video 92).

Plan: planning/video-93-proof-by-contradiction.md

Render draft:  manim -ql scripts/undergraduate/video-93-proof-by-contradiction.py Video93_ProofByContradiction
Render final:  manim -qh scripts/undergraduate/video-93-proof-by-contradiction.py Video93_ProofByContradiction
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


class Video93_ProofByContradiction(Scene):
    """Proof by contradiction: assume the opposite, derive absurdity, conclude the truth."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_logic()
        self.scene3_when_to_use()
        self.scene4_sqrt2_irrational()
        self.scene5_infinitude_of_primes()
        self.scene6_vs_contrapositive()
        self.scene7_outro()

    # ------------------------------------------------------------------
    # Scene 1: Hook -- The Impossible Assumption (~25s)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Imagine proving something is true by showing that if it were false, "
            "mathematics itself would break.",
            duration=10,
        )
        play_intro(self, "Proof by Contradiction", "Introduction to Proofs")

        self.add_subcaption(
            "That is proof by contradiction: one of the most powerful tools in all of mathematics.",
            duration=8,
        )

        title = self.ly.title("The Impossible Assumption")

        # A clean equation that "cracks"
        eq = MathTex(
            r"\sqrt{2} = \frac{a}{b}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(eq)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(2)

        # Crack it -- flash red, add contradiction symbol
        self.add_subcaption(
            "What if this equation leads to something that cannot be true?",
            duration=6,
        )
        self.play(
            eq.animate.set_color(RED),
            run_time=0.5,
        )
        contradiction = MathTex(
            r"\bot", font_size=HEADING_SIZE * 2, color=RED,
        )
        contradiction.next_to(eq, DOWN, buff=0.6)
        self.play(
            Flash(eq, color=RED, num_lines=12, line_length=0.4, flash_radius=0.8),
            FadeIn(contradiction, shift=UP * 0.2),
            run_time=0.8,
        )
        self.wait(3)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: The Logic -- How Contradiction Works (~60s)
    # ------------------------------------------------------------------
    def scene2_logic(self):
        self.add_subcaption(
            "In a direct proof, we assume P and walk toward Q.",
            duration=6,
        )
        title = self.ly.title("How Contradiction Works")

        # Direct proof reminder (compact)
        direct_label = Text("Direct Proof", font_size=LABEL_SIZE, color=DIM, font=SANS)
        direct_chain = MathTex(
            r"P \Longrightarrow \cdots \Longrightarrow Q",
            font_size=BODY_SIZE, color=DIM,
        )
        direct_group = VGroup(direct_label, direct_chain).arrange(DOWN, buff=0.15)
        self.ly.safe_place(direct_group, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(direct_label, shift=LEFT * 0.1), run_time=FAST)
        self.play(Write(direct_chain), run_time=FAST)
        self.wait(2)

        self.ly.clear()

        # Contradiction structure
        self.add_subcaption(
            "In proof by contradiction, we assume P is true but Q is false, "
            "and then derive something impossible.",
            duration=10,
        )
        title2 = self.ly.title("How Contradiction Works")

        # Step 1: Assumption
        assume_label = Text("1. Assume", font_size=LABEL_SIZE, color=PRIMARY, font=SANS)
        assume_eq = MathTex(
            r"P \wedge \lnot Q",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        assume_group = VGroup(assume_label, assume_eq).arrange(RIGHT, buff=0.4)
        self.ly.safe_place(assume_group, direction=DOWN, anchor=title2, buff=0.5)

        # Step 2: Reason
        reason_label = Text("2. Reason forward", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)
        reason_eq = MathTex(
            r"\cdots \Longrightarrow \cdots",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        reason_group = VGroup(reason_label, reason_eq).arrange(RIGHT, buff=0.4)
        self.ly.safe_place(reason_group, direction=DOWN, anchor=assume_group, buff=0.4)

        # Step 3: Contradiction
        contra_label = Text("3. Derive", font_size=LABEL_SIZE, color=RED, font=SANS)
        contra_eq = MathTex(
            r"\bot \quad \text{(False!)}",
            font_size=HEADING_SIZE, color=RED,
        )
        contra_group = VGroup(contra_label, contra_eq).arrange(RIGHT, buff=0.4)
        self.ly.safe_place(contra_group, direction=DOWN, anchor=reason_group, buff=0.4)

        # Step 4: Conclusion
        conclude_label = Text("4. Therefore", font_size=LABEL_SIZE, color=ACCENT, font=SANS)
        conclude_eq = MathTex(
            r"Q \text{ must be true.}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        conclude_group = VGroup(conclude_label, conclude_eq).arrange(RIGHT, buff=0.4)
        self.ly.safe_place(conclude_group, direction=DOWN, anchor=contra_group, buff=0.4)

        self.play(
            FadeIn(assume_label, shift=LEFT * 0.1),
            Write(assume_eq),
            run_time=NORMAL,
        )
        self.wait(1.5)
        self.play(
            FadeIn(reason_label, shift=LEFT * 0.1),
            Write(reason_eq),
            run_time=NORMAL,
        )
        self.wait(1.5)
        self.play(
            FadeIn(contra_label, shift=LEFT * 0.1),
            Write(contra_eq),
            run_time=NORMAL,
        )
        self.wait(1.5)
        self.play(
            FadeIn(conclude_label, shift=LEFT * 0.1),
            Write(conclude_eq),
            run_time=NORMAL,
        )
        self.wait(3)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: When to Use Contradiction (~40s)
    # ------------------------------------------------------------------
    def scene3_when_to_use(self):
        self.add_subcaption(
            "How do you know when to use contradiction? There are signals.",
            duration=6,
        )
        title = self.ly.title("When to Use Contradiction")

        # Key signals
        signals = [
            Text("Statements about irrationality", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Claims about infinity", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Non-existence proofs", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Words: cannot, no solution, unique", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(signals, start_from=title)

        self.wait(4)

        self.add_subcaption(
            "The key idea: assume the opposite and you get a concrete object to analyze, "
            "like a rational number or a finite list, that you can show leads to absurdity.",
            duration=10,
        )

        # Key idea box
        idea = Text(
            "Assume the opposite, get a concrete object, show it breaks.",
            font_size=LABEL_SIZE, color=WHITE, font=SANS,
        )
        idea_box = SurroundingRectangle(
            idea, color=ACCENT, buff=0.25,
            stroke_width=1.5, corner_radius=0.1,
        )
        idea_group = VGroup(idea, idea_box)
        self.ly.center_in_content(idea_group)

        self.ly.clear()
        self.play(FadeIn(idea_group, shift=UP * 0.15), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Example 1 -- sqrt(2) is Irrational (~150s)
    # ------------------------------------------------------------------
    def scene4_sqrt2_irrational(self):
        self.add_subcaption(
            "Our first example is the most famous proof by contradiction: "
            "showing that the square root of 2 is irrational.",
            duration=10,
        )
        title = self.ly.title("Example: " + r"$\sqrt{2}$ is Irrational")

        self.add_subcaption(
            "This proof is over two thousand years old, and it is still beautiful.",
            duration=6,
        )
        self.wait(2)

        # Assumption box (persistent visual element)
        assumption_box = RoundedRectangle(
            corner_radius=0.15,
            fill_color=PRIMARY,
            fill_opacity=0.12,
            stroke_color=PRIMARY,
            stroke_width=1.5,
            width=9.0, height=1.0,
        )
        assumption_text = MathTex(
            r"\sqrt{2} = \frac{a}{b}, \quad a, b \in \mathbb{Z}, \quad \gcd(a,b)=1",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        assumption_label = Text(
            "Assume (for contradiction):",
            font_size=SMALL_SIZE, color=PRIMARY, font=SANS,
        )
        assumption_group = VGroup(assumption_label, assumption_box, assumption_text)
        assumption_label.next_to(assumption_box, UP, buff=0.15)
        assumption_text.move_to(assumption_box)
        self.ly.safe_place(assumption_group, direction=DOWN, anchor=title, buff=0.5)

        self.play(
            FadeIn(assumption_label, shift=LEFT * 0.1),
            FadeIn(assumption_box),
            Write(assumption_text),
            run_time=NORMAL,
        )
        self.wait(2)

        # Step 1: Square both sides
        self.add_subcaption(
            "Square both sides: 2 equals a-squared over b-squared, so a-squared equals 2 times b-squared.",
            duration=8,
        )
        step1 = MathTex(
            r"2 = \frac{a^2}{b^2} \Longrightarrow a^2 = 2b^2",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=assumption_group, buff=0.5)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(2)

        # Therefore a^2 is even
        self.add_subcaption(
            "Since a-squared equals 2 times b-squared, a-squared is even.",
            duration=6,
        )
        even_a2 = Text(
            "Therefore a" + u"\u00B2" + " is even.",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(even_a2, direction=DOWN, anchor=step1, buff=0.3)
        self.play(FadeIn(even_a2, shift=LEFT * 0.1), run_time=FAST)
        self.wait(2)

        self.ly.clear()

        # Step 2: Therefore a is even
        self.add_subcaption(
            "If a-squared is even, then a itself must be even. "
            "We proved this in Video 91.",
            duration=8,
        )
        title2 = self.ly.title("Example: " + r"$\sqrt{2}$ is Irrational")

        step2a = Text(
            "If a" + u"\u00B2" + " is even, then a is even.",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        step2b = MathTex(
            r"a = 2k \quad \text{for some integer } k",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        step2_group = VGroup(step2a, step2b).arrange(DOWN, buff=0.3)
        self.ly.safe_place(step2_group, direction=DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(step2a, shift=LEFT * 0.1), run_time=FAST)
        self.play(Write(step2b), run_time=NORMAL)
        self.wait(3)

        # Step 3: Substitute back
        self.add_subcaption(
            "Substitute a equals 2k into a-squared equals 2b-squared.",
            duration=6,
        )
        step3 = MathTex(
            r"(2k)^2 = 2b^2 \Longrightarrow 4k^2 = 2b^2 \Longrightarrow b^2 = 2k^2",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step3, direction=DOWN, anchor=step2_group, buff=0.5)
        self.play(Write(step3), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Step 4: Therefore b is even -- CONTRADICTION
        self.add_subcaption(
            "By the same reasoning, b-squared is even, so b is even.",
            duration=6,
        )
        title3 = self.ly.title("Example: " + r"$\sqrt{2}$ is Irrational")

        step4a = Text(
            "b" + u"\u00B2" + " is even, so b is even.",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        step4b = Text(
            "Both a and b are even!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        step4c = Text(
            "But we assumed gcd(a, b) = 1  (no common factor).",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(step4a, direction=DOWN, anchor=title3, buff=0.5)
        self.ly.safe_place(step4b, direction=DOWN, anchor=step4a, buff=0.4)
        self.ly.safe_place(step4c, direction=DOWN, anchor=step4b, buff=0.3)

        self.play(FadeIn(step4a, shift=LEFT * 0.1), run_time=FAST)
        self.wait(1)
        self.play(FadeIn(step4b, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.play(FadeIn(step4c, shift=LEFT * 0.1), run_time=FAST)
        self.wait(2)

        # Contradiction spark!
        self.add_subcaption(
            "Contradiction! Both a and b cannot be even if they share no common factor. "
            "Therefore, our assumption must be false.",
            duration=8,
        )
        contradiction_symbol = MathTex(
            r"\bot", font_size=HEADING_SIZE * 2.5, color=RED,
        )
        contradiction_symbol.move_to(UP * 0.5)
        flash_group = VGroup(step4a, step4b, step4c)
        self.play(
            Flash(flash_group, color=RED, num_lines=16, line_length=0.5, flash_radius=1.2),
            FadeIn(contradiction_symbol, shift=UP * 0.2),
            flash_group.animate.set_color(RED),
            run_time=0.8,
        )
        self.wait(3)

        self.ly.clear()

        # Conclusion
        self.add_subcaption(
            "Therefore, the square root of 2 cannot be written as a fraction. "
            "It is irrational.",
            duration=8,
        )
        title4 = self.ly.title("Conclusion")
        conclusion = MathTex(
            r"\sqrt{2} \notin \mathbb{Q}. \quad \blacksquare",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(conclusion)
        self.play(Write(conclusion), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Example 2 -- Infinitude of Primes (~130s)
    # ------------------------------------------------------------------
    def scene5_infinitude_of_primes(self):
        self.add_subcaption(
            "Our second example is Euclid's proof that there are infinitely many prime numbers, "
            "from around 300 BCE.",
            duration=10,
        )
        title = self.ly.title("Example: Infinitely Many Primes")

        self.add_subcaption(
            "The argument is stunningly simple and has stood for over two thousand years.",
            duration=6,
        )
        self.wait(2)

        # Assumption box
        assumption_box2 = RoundedRectangle(
            corner_radius=0.15,
            fill_color=PRIMARY,
            fill_opacity=0.12,
            stroke_color=PRIMARY,
            stroke_width=1.5,
            width=9.0, height=1.0,
        )
        assumption_text2 = MathTex(
            r"\text{Only finitely many primes: } p_1, p_2, \ldots, p_n",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        assumption_label2 = Text(
            "Assume (for contradiction):",
            font_size=SMALL_SIZE, color=PRIMARY, font=SANS,
        )
        assumption_group2 = VGroup(assumption_label2, assumption_box2, assumption_text2)
        assumption_label2.next_to(assumption_box2, UP, buff=0.15)
        assumption_text2.move_to(assumption_box2)
        self.ly.safe_place(assumption_group2, direction=DOWN, anchor=title, buff=0.5)

        self.play(
            FadeIn(assumption_label2, shift=LEFT * 0.1),
            FadeIn(assumption_box2),
            Write(assumption_text2),
            run_time=NORMAL,
        )
        self.wait(3)

        # Construct N
        self.add_subcaption(
            "Now construct a new number N by multiplying all the primes together and adding 1.",
            duration=8,
        )
        construct = MathTex(
            r"N = p_1 \cdot p_2 \cdot \ldots \cdot p_n + 1",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(construct, direction=DOWN, anchor=assumption_group2, buff=0.5)
        self.play(Write(construct), run_time=NORMAL)
        self.wait(3)

        # Key insight: N is not divisible by any listed prime
        self.add_subcaption(
            "When you divide N by any prime in our list, the remainder is always 1. "
            "So N is not divisible by any of our primes.",
            duration=10,
        )
        insight = MathTex(
            r"N \div p_i \text{ has remainder } 1 \quad \forall\, i",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=construct, buff=0.4)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()

        # Two cases
        self.add_subcaption(
            "Now, there are two possibilities for N.",
            duration=4,
        )
        title2 = self.ly.title("Example: Infinitely Many Primes")

        # Case 1
        case1_label = Text("Case 1:", font_size=LABEL_SIZE, color=PRIMARY, font=SANS)
        case1_text = Text(
            "N is prime itself.",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        case1_result = Text(
            "But N is not in our list! Contradiction.",
            font_size=LABEL_SIZE, color=RED, font=SANS,
        )
        case1_group = VGroup(case1_label, case1_text, case1_result).arrange(RIGHT, buff=0.3)
        self.ly.safe_place(case1_group, direction=DOWN, anchor=title2, buff=0.5)

        self.play(
            FadeIn(case1_label, shift=LEFT * 0.1),
            FadeIn(case1_text, shift=LEFT * 0.1),
            run_time=FAST,
        )
        self.wait(1)
        self.play(FadeIn(case1_result, shift=LEFT * 0.1), run_time=FAST)
        self.wait(2)

        # Case 2
        self.add_subcaption(
            "Or, N is composite, meaning it has a prime factor.",
            duration=6,
        )
        case2_label = Text("Case 2:", font_size=LABEL_SIZE, color=PRIMARY, font=SANS)
        case2_text = Text(
            "N has a prime factor q.",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        case2_result = Text(
            "But q is not in our list! Contradiction.",
            font_size=LABEL_SIZE, color=RED, font=SANS,
        )
        case2_group = VGroup(case2_label, case2_text, case2_result).arrange(RIGHT, buff=0.3)
        self.ly.safe_place(case2_group, direction=DOWN, anchor=case1_group, buff=0.4)

        self.play(
            FadeIn(case2_label, shift=LEFT * 0.1),
            FadeIn(case2_text, shift=LEFT * 0.1),
            run_time=FAST,
        )
        self.wait(1)
        self.play(FadeIn(case2_result, shift=LEFT * 0.1), run_time=FAST)
        self.wait(3)

        # Contradiction spark
        self.add_subcaption(
            "Either way, we get a contradiction. Our list of all primes cannot be complete.",
            duration=8,
        )
        both_cases = VGroup(case1_group, case2_group)
        contradiction2 = MathTex(
            r"\bot", font_size=HEADING_SIZE * 2, color=RED,
        )
        contradiction2.next_to(both_cases, DOWN, buff=0.4)
        self.play(
            Flash(both_cases, color=RED, num_lines=14, line_length=0.4, flash_radius=1.0),
            FadeIn(contradiction2, shift=UP * 0.2),
            run_time=0.8,
        )
        self.wait(3)

        self.ly.clear()

        # Conclusion
        self.add_subcaption(
            "Therefore, there are infinitely many prime numbers. "
            "No matter how many you find, there is always one more.",
            duration=8,
        )
        title3 = self.ly.title("Conclusion")
        conclusion2 = MathTex(
            r"\text{There are infinitely many primes.} \quad \blacksquare",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(conclusion2)
        self.play(Write(conclusion2), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Contradiction vs Contrapositive (~50s)
    # ------------------------------------------------------------------
    def scene6_vs_contrapositive(self):
        self.add_subcaption(
            "If you have seen Video 92, you might be wondering: "
            "how is this different from proof by contrapositive?",
            duration=8,
        )
        title = self.ly.title("Contradiction vs. Contrapositive")

        # Side by side: Contrapositive
        self.add_subcaption(
            "In contrapositive, you prove an equivalent statement: not Q implies not P, "
            "and you prove it directly.",
            duration=8,
        )

        cp_title = Text("Contrapositive", font_size=BODY_SIZE, color=PRIMARY, font=SANS)
        cp_desc = MathTex(
            r"(\text{Prove } P \to Q) \equiv (\text{Prove } \lnot Q \to \lnot P)",
            font_size=LABEL_SIZE, color=WHITE,
        )
        cp_note = Text(
            "One assumption, one conclusion, direct proof.",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        cp_group = VGroup(cp_title, cp_desc, cp_note).arrange(DOWN, buff=0.25)
        self.ly.safe_place(cp_group, direction=DOWN, anchor=title, buff=0.5)

        self.play(
            FadeIn(cp_title, shift=LEFT * 0.1),
            Write(cp_desc),
            FadeIn(cp_note, shift=LEFT * 0.1),
            run_time=NORMAL,
        )
        self.wait(3)

        self.ly.clear()

        # Contradiction
        self.add_subcaption(
            "In contradiction, you assume P and not Q together, "
            "and derive any contradiction at all.",
            duration=8,
        )
        title2 = self.ly.title("Contradiction vs. Contrapositive")

        cx_title = Text("Contradiction", font_size=BODY_SIZE, color=RED, font=SANS)
        cx_desc = MathTex(
            r"\text{Assume } P \wedge \lnot Q, \text{ derive } \bot",
            font_size=LABEL_SIZE, color=WHITE,
        )
        cx_note = Text(
            "Two assumptions collide, derive any absurdity.",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        cx_group = VGroup(cx_title, cx_desc, cx_note).arrange(DOWN, buff=0.25)
        self.ly.safe_place(cx_group, direction=DOWN, anchor=title2, buff=0.5)

        self.play(
            FadeIn(cx_title, shift=LEFT * 0.1),
            Write(cx_desc),
            FadeIn(cx_note, shift=LEFT * 0.1),
            run_time=NORMAL,
        )
        self.wait(3)

        self.ly.clear()

        # Key distinction
        self.add_subcaption(
            "They are related but distinct. Contradiction is more flexible: "
            "the contradiction can come from anywhere, not just from not-P.",
            duration=10,
        )
        title3 = self.ly.title("Key Distinction")

        key1 = Text(
            "Contrapositive: prove a specific equivalent statement directly.",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        key2 = Text(
            "Contradiction: assume the worst and show it cannot happen.",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        key3 = Text(
            "Every contrapositive proof IS a contradiction proof, but not vice versa.",
            font_size=LABEL_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(key1, direction=DOWN, anchor=title3, buff=0.5)
        self.ly.safe_place(key2, direction=DOWN, anchor=key1, buff=0.4)
        self.ly.safe_place(key3, direction=DOWN, anchor=key2, buff=0.3)

        self.play(
            FadeIn(key1, shift=LEFT * 0.15), run_time=NORMAL,
        )
        self.wait(1)
        self.play(
            FadeIn(key2, shift=LEFT * 0.15), run_time=NORMAL,
        )
        self.wait(1)
        self.play(
            FadeIn(key3, shift=LEFT * 0.1), run_time=NORMAL,
        )
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Summary & Outro (~30s)
    # ------------------------------------------------------------------
    def scene7_outro(self):
        self.add_subcaption(
            "Proof by contradiction: assume the opposite, derive absurdity, conclude the truth.",
            duration=8,
        )
        title = self.ly.title("Key Takeaways")

        items = [
            Text("1. Assume the opposite (P and not Q)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Reason forward with logic", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Find a contradiction", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("4. Conclude Q must be true", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(6)

        play_outro(self, "Proof by Induction", "Introduction to Proofs")
