"""
Video 98: Proof Writing Style
TEMPLATE v2 — Professional quality Manim script

Playlist: Introduction to Proofs (Video 9 of 9 — FINAL)
Class: Video98_ProofWritingStyle

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


class Video98_ProofWritingStyle(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_skeleton()
        self.scene3_before_after()
        self.scene4_language()
        self.scene5_pitfalls()
        self.scene6_recap()
        self.scene7_outro()

    # ─── Scene 1: Hook — Two Proofs, Same Idea ───
    def scene1_hook(self):
        self.add_subcaption(
            "You have learned seven proof techniques. "
            "Direct proof, contrapositive, contradiction, induction, "
            "strong induction, cases, and existence and uniqueness. "
            "But knowing a technique is not the same as writing a good proof. "
            "Today we focus on style: the structure, language, and conventions "
            "that turn a correct argument into a proof "
            "that mathematicians actually want to read.",
            duration=18,
        )
        play_intro(self, "Proof Writing Style", "Introduction to Proofs")

        title = self.ly.title("Same Logic, Different Presentation")

        # Bad proof (compact, run-together)
        bad_label = Text("Sloppy:", font_size=LABEL_SIZE, color=RED, font=SANS)
        bad_proof = Text(
            'a,b odd so a=2k+1,b=2m+1 '
            'so a+b=2(k+m+1) even',
            font_size=SMALL_SIZE, color=DIM, font=MONO,
        )
        bad_group = VGroup(bad_label, bad_proof).arrange(DOWN, buff=0.15)

        # Good proof (structured)
        good_label = Text("Clear:", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)
        good_proof = Text(
            "Let a=2k+1, b=2m+1. Then\n"
            "a+b = 2(k+m+1), which is\n"
            "even. QED",
            font_size=SMALL_SIZE, color=WHITE, font=MONO,
        )
        good_group = VGroup(good_label, good_proof).arrange(DOWN, buff=0.15)

        left_col, right_col = self.ly.two_columns(
            [bad_group], [good_group], start_from=title,
        )

        self.play(
            FadeIn(left_col, shift=LEFT * 0.15),
            FadeIn(right_col, shift=RIGHT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1)

        message = Text(
            "The logic is identical. The presentation makes all the difference.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(message, direction=DOWN, anchor=right_col, buff=0.5)
        self.play(FadeIn(message, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 2: The Proof Skeleton ───
    def scene2_skeleton(self):
        self.add_subcaption(
            "Every well-written proof follows a skeleton. "
            "First, state the claim clearly. "
            "Then write the word Proof followed by a colon or period. "
            "Introduce your variables with Let or Suppose. "
            "This is the body where definitions and reasoning live. "
            "Finally Therefore or Hence leads to the conclusion "
            "and QED marks the end.",
            duration=16,
        )

        title = self.ly.title("The Proof Skeleton")

        items = [
            Text("Claim:  State what you will prove", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Proof:  Opening declaration", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Let / Suppose:  Introduce variables", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Body:  Definitions + reasoning", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Therefore / Hence:  The conclusion", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("QED:  End mark", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1)

        self.ly.clear()

    # ─── Scene 3: Before and After — The Transformation ───
    def scene3_before_after(self):
        self.add_subcaption(
            "Here is the same argument written two ways. "
            "The first is correct but unreadable. "
            "The second is the same logic presented clearly. "
            "Notice the improvements: variables are introduced with Let, "
            "each step is on its own line, the algebra is shown explicitly, "
            "and QED marks the end. "
            "The logic did not change. Only the presentation did.",
            duration=18,
        )

        self.ly.section_divider(1, "Before and After")

        title = self.ly.title("Claim: If a, b are odd, then a + b is even")

        # Show the bad proof
        bad_header = Text("BAD PROOF", font_size=LABEL_SIZE, color=RED, font=MONO)
        bad_proof = Text(
            "a,b odd, a=2k+1, b=2m+1\n"
            "a+b=2k+1+2m+1=2(k+m+1)\n"
            "so it's even",
            font_size=LABEL_SIZE, color=DIM, font=MONO,
        )
        bad_group = VGroup(bad_header, bad_proof).arrange(DOWN, buff=0.15)
        self.ly.safe_place(bad_group, direction=DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(bad_group, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1)

        # Fade out bad, show good
        self.play(FadeOut(bad_group), run_time=0.5)

        good_header = Text("GOOD PROOF", font_size=LABEL_SIZE, color=SECONDARY, font=MONO)
        good_line1 = MathTex(
            r"\text{Let } a = 2k + 1 \text{ and } b = 2m + 1",
            font_size=LABEL_SIZE, color=PRIMARY,
        )
        good_line2 = MathTex(
            r"a + b = 2k + 1 + 2m + 1 = 2(k + m + 1)",
            font_size=LABEL_SIZE, color=WHITE,
        )
        good_line3 = MathTex(
            r"\text{Since } k + m + 1 \in \mathbb{Z}, \; a + b \text{ is even}",
            font_size=LABEL_SIZE, color=WHITE,
        )
        good_qed = Text("QED", font_size=LABEL_SIZE, color=ACCENT, font=MONO)

        good_steps = VGroup(good_line1, good_line2, good_line3, good_qed).arrange(DOWN, buff=0.25)
        good_full = VGroup(good_header, good_steps).arrange(DOWN, buff=0.15)
        self.ly.safe_place(good_full, direction=DOWN, anchor=title, buff=0.4)
        self.play(FadeIn(good_full, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Highlight improvements
        improvements = [
            Text("Variables introduced with Let", font_size=SMALL_SIZE, color=SECONDARY, font=SANS),
            Text("Each step on its own line", font_size=SMALL_SIZE, color=PRIMARY, font=SANS),
            Text("Algebra shown explicitly", font_size=SMALL_SIZE, color=WHITE, font=SANS),
            Text("Clear QED at the end", font_size=SMALL_SIZE, color=ACCENT, font=SANS),
        ]

        # Show improvements one by one as highlights (using a side note)
        imp_title = Text("Improvements:", font_size=LABEL_SIZE, color=ACCENT, font=SANS)
        self.ly.safe_place(imp_title, direction=LEFT, buff=0.3)

        for imp in improvements:
            self.ly.safe_place(imp, direction=DOWN, anchor=imp_title, buff=0.2)
            self.play(FadeIn(imp, shift=LEFT * 0.1), run_time=0.4)
            self.wait(0.3)
            imp_title = imp  # chain placement

        self.wait(1)

        self.ly.clear()

    # ─── Scene 4: Language — Words vs. Symbols ───
    def scene4_language(self):
        self.add_subcaption(
            "A common question: should you write Therefore or draw an arrow? "
            "Should you write for all x in Z or use the universal quantifier? "
            "The answer is balance. "
            "Use symbols for things that are standard: quantifiers, set notation, "
            "algebraic expressions. "
            "Use words for logical flow: therefore, since, suppose, let. "
            "A proof is a piece of writing meant to be read by a human being.",
            duration=18,
        )

        self.ly.section_divider(2, "Words vs. Symbols")

        title = self.ly.title("Finding the Right Balance")

        # Formal column
        formal_label = Text("Use SYMBOLS for:", font_size=LABEL_SIZE, color=PRIMARY, font=SANS)
        formal_items = VGroup(
            MathTex(r"\forall, \; \exists", font_size=BODY_SIZE, color=PRIMARY),
            Text("Set notation  (x in Z)", font_size=LABEL_SIZE, color=WHITE, font=MONO),
            Text("Algebraic expressions", font_size=LABEL_SIZE, color=WHITE, font=SANS),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        formal_group = VGroup(formal_label, formal_items).arrange(DOWN, buff=0.15)

        # Conversational column
        conv_label = Text("Use WORDS for:", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)
        conv_items = VGroup(
            Text("Logical flow", font_size=LABEL_SIZE, color=WHITE, font=SANS),
            Text("therefore, since, suppose", font_size=LABEL_SIZE, color=WHITE, font=MONO),
            Text("Explanations and context", font_size=LABEL_SIZE, color=WHITE, font=SANS),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        conv_group = VGroup(conv_label, conv_items).arrange(DOWN, buff=0.15)

        left_col, right_col = self.ly.two_columns(
            [formal_group], [conv_group], start_from=title,
        )
        self.play(
            FadeIn(left_col, shift=LEFT * 0.15),
            FadeIn(right_col, shift=RIGHT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1)

        # Key rule
        rule = Text(
            "Write for humans, not for computers.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(rule, direction=DOWN, anchor=left_col, buff=0.5)
        self.play(FadeIn(rule, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 5: Common Pitfalls ───
    def scene5_pitfalls(self):
        self.add_subcaption(
            "There are traps that even experienced mathematicians fall into. "
            "Circular reasoning: assuming the very thing you need to prove. "
            "Always check that your starting point does not secretly contain the conclusion. "
            "Undefined variables: never use a symbol without first saying what it represents. "
            "Missing QED: every proof needs a clear ending. "
            "And a classic error: confusing the converse with the contrapositive. "
            "Remember the contrapositive is logically equivalent, but the converse is not.",
            duration=20,
        )

        self.ly.section_divider(3, "Common Pitfalls")

        title = self.ly.title("Mistakes to Avoid")

        items = [
            Text("Circular reasoning: don't assume what you prove", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Undefined variables: always say what n, x, k mean", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Missing QED: every proof needs a clear end", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Converse != Contrapositive: know the difference", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(0.5)

        # Correct pairing reminder
        remind = MathTex(
            r"P \to Q \;\;\equiv\;\; \neg Q \to \neg P \;\;\neq\;\; Q \to P",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(remind, direction=DOWN, anchor=items[-1], buff=0.5)
        self.play(Write(remind), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 6: Playlist Recap — Your Proof Toolkit ───
    def scene6_recap(self):
        self.add_subcaption(
            "This brings us to the end of the Introduction to Proofs playlist. "
            "You now have a complete toolkit. "
            "Direct proof for straightforward claims. "
            "Contrapositive when the conclusion is easier to negate. "
            "Contradiction for existence results. "
            "Induction for natural numbers. "
            "Strong induction when you need the full history. "
            "Cases for exhaustive arguments. "
            "And existence and uniqueness for showing exactly one solution exists. "
            "Combine any technique with the writing style we learned today "
            "and you can write proofs that are not just correct, "
            "but clear, elegant, and professional.",
            duration=24,
        )

        title = self.ly.title("Your Complete Proof Toolkit")

        techniques = [
            Text("Direct Proof", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Contrapositive", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Contradiction", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Induction", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Strong Induction", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Proof by Cases", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Existence & Uniqueness", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(techniques, start_from=title)

        self.wait(0.5)

        # Style overlay
        overlay = Text(
            "Apply PROOF WRITING STYLE to all of these!",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        box = SurroundingRectangle(overlay, color=ACCENT, buff=0.2,
                                    stroke_width=2, corner_radius=0.1)
        overlay_group = VGroup(overlay, box)
        self.ly.center_in_content(overlay_group)
        self.play(
            FadeIn(overlay_group, shift=UP * 0.15),
            run_time=NORMAL,
        )
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 7: Outro — Where to Go From Here ───
    def scene7_outro(self):
        self.add_subcaption(
            "Three things to remember. "
            "First, follow the skeleton: Claim, Proof, Let, therefore, QED. "
            "Second, write for humans: use symbols where they help, "
            "words where they clarify. "
            "Third, practice: every proof you write makes the next one easier. "
            "Thank you for joining me through this entire "
            "Introduction to Proofs playlist. "
            "In the next playlist, Real Analysis, "
            "we will put these skills to work on the foundations of calculus.",
            duration=20,
        )

        title = self.ly.title("Three Things to Remember")

        items = [
            Text("1. Follow the skeleton: Claim, Proof, Let, therefore, QED", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Write for humans: symbols where they help, words where they clarify", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Practice: every proof you write makes the next one easier", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(2)

        self.ly.clear()

        play_outro(self, "The Real Numbers (Completeness)", "Real Analysis I")
