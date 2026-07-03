"""
Video 97: Existence and Uniqueness Proofs
TEMPLATE v2 — Professional quality Manim script

Playlist: Introduction to Proofs (Video 8 of 9)
Class: Video97_ExistenceUniqueness

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


class Video97_ExistenceUniqueness(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_two_types()
        self.scene3_constructive()
        self.scene4_nonconstructive()
        self.scene5_uniqueness_method()
        self.scene6_example_equation()
        self.scene7_example_inverse()
        self.scene8_summary()

    # ─── Scene 1: Hook — The Detective and the Thief ───
    def scene1_hook(self):
        self.add_subcaption(
            "In every proof we have asked: is this statement TRUE? "
            "But some of the most powerful results in mathematics "
            "answer a different question: does a solution exist? "
            "And if so, is it the only one?",
            duration=12,
        )
        play_intro(self, "Existence and Uniqueness Proofs", "Introduction to Proofs")

        title = self.ly.title("Two Fundamental Questions")

        items = [
            Text("Existence: Does a solution exist?", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Uniqueness: Is it the ONLY one?", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1)

        quant = MathTex(
            r"\exists! \; x, \; P(x)",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(quant, direction=DOWN, anchor=items[-1], buff=0.6)
        self.play(Write(quant), run_time=NORMAL)
        self.wait(1)

        meaning = Text(
            '"Exactly one x satisfies P(x)"',
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(meaning, direction=DOWN, anchor=quant, buff=0.4)
        self.play(FadeIn(meaning, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 2: Two Types of Claims ───
    def scene2_two_types(self):
        self.add_subcaption(
            "There are two fundamentally different questions. "
            "Existence asks: is there at least one object with property P? "
            "Uniqueness asks: is there exactly one? "
            "Exists-unique means two things at once: "
            "at least one exists, and any two that exist must be the same.",
            duration=15,
        )

        title = self.ly.title("Two Types of Claims")

        exist_label = Text("Existence", font_size=BODY_SIZE, color=SECONDARY, font=SANS)
        exist_eq = MathTex(
            r"\exists \; x, \; P(x)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        exist_desc = Text('"At least one object satisfies P"', font_size=SMALL_SIZE, color=DIM, font=SANS)

        unique_label = Text("Uniqueness", font_size=BODY_SIZE, color=ACCENT, font=SANS)
        unique_eq = MathTex(
            r"\exists! \; x, \; P(x)",
            font_size=BODY_SIZE, color=ACCENT,
        )
        unique_desc = Text('"Exactly one object satisfies P"', font_size=SMALL_SIZE, color=DIM, font=SANS)

        left_items = VGroup(exist_label, exist_eq, exist_desc).arrange(DOWN, buff=0.2)
        right_items = VGroup(unique_label, unique_eq, unique_desc).arrange(DOWN, buff=0.2)

        left_col, right_col = self.ly.two_columns(
            [left_items], [right_items], start_from=title,
        )

        self.play(
            FadeIn(left_col, shift=LEFT * 0.15),
            FadeIn(right_col, shift=RIGHT * 0.15),
            run_time=NORMAL,
        )
        self.wait(1)

        # Expand exists-unique
        expand = MathTex(
            r"\exists! \; x, \; P(x) \;\equiv\; \exists x, \; P(x) \;\wedge\; \forall y \forall z, \; (P(y) \wedge P(z)) \to y = z",
            font_size=LABEL_SIZE, color=WHITE,
        )
        self.ly.safe_place(expand, direction=DOWN, anchor=left_col, buff=0.4)
        self.play(Write(expand), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 3: Constructive Existence Proofs ───
    def scene3_constructive(self):
        self.add_subcaption(
            "The simplest existence proof: just find the object. "
            "This is called a constructive proof. "
            "We literally exhibit a witness, a specific object that satisfies the property. "
            "Claim: there exists an integer n such that 2n plus 1 equals 7. "
            "Let n equal 3. Check: 2 times 3 plus 1 equals 7. Done. "
            "The witness IS the proof.",
            duration=16,
        )

        self.ly.section_divider(1, "Constructive Existence Proofs")

        title = self.ly.title("Constructive: Find the Witness")

        claim = MathTex(
            r"\exists \; n \in \mathbb{Z}, \; 2n + 1 = 7",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.play(Write(claim), run_time=NORMAL)
        self.wait(0.5)

        step1 = MathTex(
            r"\text{Let } n = 3",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=claim, buff=0.5)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.5)

        step2 = MathTex(
            r"2(3) + 1 = 6 + 1 = 7 \;\checkmark",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.3)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.5)

        witness = Text(
            "n = 3 is the witness that proves existence!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(witness, direction=DOWN, anchor=step2, buff=0.4)
        self.play(FadeIn(witness, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 4: Non-Constructive Existence Proofs ───
    def scene4_nonconstructive(self):
        self.add_subcaption(
            "Sometimes we can prove something exists without ever finding it. "
            "This is a non-constructive existence proof. "
            "Claim: there exist irrational numbers a and b "
            "such that a to the power b is rational. "
            "We know root 2 to the power root 2 "
            "is either rational or irrational. "
            "If it is rational, done. "
            "If it is irrational, raise it to root 2, "
            "and you get root 2 squared equals 2, which is rational. "
            "In either case, such a pair exists, "
            "but we never determined which case!",
            duration=22,
        )

        self.ly.section_divider(2, "Non-Constructive Existence Proofs")

        title = self.ly.title("Prove Existence Without Finding It")

        claim = MathTex(
            r"\exists \; a, b \notin \mathbb{Q}, \; a^b \in \mathbb{Q}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.play(Write(claim), run_time=NORMAL)
        self.wait(0.5)

        # Case 1
        case1_label = Text("Case 1:", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)
        case1_eq = MathTex(
            r"\sqrt{2}^{\sqrt{2}} \in \mathbb{Q} \;\Longrightarrow\; a = \sqrt{2}, \; b = \sqrt{2}",
            font_size=LABEL_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(case1_label, direction=DOWN, anchor=claim, buff=0.5)
        self.play(Write(case1_label), run_time=FAST)
        self.ly.safe_place(case1_eq, direction=DOWN, anchor=case1_label, buff=0.15)
        self.play(Write(case1_eq), run_time=NORMAL)
        self.wait(0.5)

        # Case 2
        case2_label = Text("Case 2:", font_size=LABEL_SIZE, color=ACCENT, font=SANS)
        case2_eq = MathTex(
            r"\sqrt{2}^{\sqrt{2}} \notin \mathbb{Q} \;\Longrightarrow\; (\sqrt{2}^{\sqrt{2}})^{\sqrt{2}} = \sqrt{2}^2 = 2 \in \mathbb{Q}",
            font_size=LABEL_SIZE, color=ACCENT,
        )
        self.ly.safe_place(case2_label, direction=DOWN, anchor=case1_eq, buff=0.3)
        self.play(Write(case2_label), run_time=FAST)
        self.ly.safe_place(case2_eq, direction=DOWN, anchor=case2_label, buff=0.15)
        self.play(Write(case2_eq), run_time=NORMAL)
        self.wait(0.5)

        # Key insight
        insight = Text(
            "We proved existence WITHOUT knowing the actual values!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=case2_eq, buff=0.5)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 5: Uniqueness Proofs — The Method ───
    def scene5_uniqueness_method(self):
        self.add_subcaption(
            "Uniqueness proofs have a beautiful template. "
            "To prove there is at most one object with property P, "
            "assume two such objects exist, call them x and y, "
            "and then show they must be equal. "
            "If any two objects with the property are forced to be the same, "
            "then there can be at most one.",
            duration=13,
        )

        self.ly.section_divider(3, "Uniqueness Proofs — The Method")

        title = self.ly.title("The Uniqueness Template")

        items = [
            MathTex(
                r"\text{Assume } P(x) \text{ and } P(y)",
                font_size=BODY_SIZE, color=PRIMARY,
            ),
            MathTex(
                r"\text{Then } \ldots \Longrightarrow x = y",
                font_size=BODY_SIZE, color=ACCENT,
            ),
            MathTex(
                r"\text{Conclusion: at most one object satisfies } P",
                font_size=BODY_SIZE, color=SECONDARY,
            ),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(1)

        key = Text(
            "If ANY two are equal, there can be at most ONE.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(key, direction=DOWN, anchor=items[-1], buff=0.5)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 6: Example — Unique Solution to an Equation ───
    def scene6_example_equation(self):
        self.add_subcaption(
            "Let us put it all together. "
            "Claim: the equation 3x minus 5 equals 10 "
            "has a unique real solution. "
            "Existence: let x equal 5. "
            "Check: 3 times 5 minus 5 equals 10. A witness exists. "
            "Uniqueness: suppose x and y both satisfy the equation. "
            "Then 3x equals 3y, so x equals y. "
            "Combine both parts: exactly one solution exists.",
            duration=18,
        )

        self.ly.section_divider(4, "Example: Unique Solution")

        title = self.ly.title("3x - 5 = 10 has a unique real solution")

        # Existence part
        exist_label = Text("Existence:", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)
        exist_step = MathTex(
            r"\text{Let } x = 5. \quad 3(5) - 5 = 10 \;\checkmark",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.play(Write(exist_label), run_time=FAST)
        self.ly.safe_place(exist_step, direction=DOWN, anchor=exist_label, buff=0.2)
        self.play(Write(exist_step), run_time=NORMAL)
        self.wait(0.5)

        # Uniqueness part
        uniq_label = Text("Uniqueness:", font_size=LABEL_SIZE, color=ACCENT, font=SANS)
        uniq_line1 = MathTex(
            r"3x - 5 = 10 \text{ and } 3y - 5 = 10",
            font_size=LABEL_SIZE, color=WHITE,
        )
        uniq_line2 = MathTex(
            r"\Longrightarrow 3x = 3y \Longrightarrow x = y \;\blacksquare",
            font_size=LABEL_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(uniq_label, direction=DOWN, anchor=exist_step, buff=0.5)
        self.play(Write(uniq_label), run_time=FAST)
        self.ly.safe_place(uniq_line1, direction=DOWN, anchor=uniq_label, buff=0.2)
        self.play(Write(uniq_line1), run_time=FAST)
        self.ly.safe_place(uniq_line2, direction=DOWN, anchor=uniq_line1, buff=0.15)
        self.play(Write(uniq_line2), run_time=NORMAL)
        self.wait(1)

        qed = MathTex(
            r"\exists! \; x \in \mathbb{R}, \; 3x - 5 = 10",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(qed, direction=DOWN, anchor=uniq_line2, buff=0.5)
        self.play(Write(qed), run_time=NORMAL)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 7: Example — Uniqueness of Multiplicative Inverse ───
    def scene7_example_inverse(self):
        self.add_subcaption(
            "A more abstract example. "
            "Claim: every nonzero real number a "
            "has exactly one multiplicative inverse. "
            "Existence: let x equal 1 over a. "
            "Since a is nonzero, this is defined, "
            "and a times 1 over a equals 1. "
            "Uniqueness: suppose x and y are both inverses of a. "
            "Then a times x equals a times y. "
            "Multiplying by 1 over a gives x equals y. "
            "This is why notation like a to the negative 1 works. "
            "There is only one object to name.",
            duration=22,
        )

        self.ly.section_divider(5, "Example: Multiplicative Inverse")

        title = self.ly.title("Every nonzero a has a unique inverse")

        claim = MathTex(
            r"\forall \; a \in \mathbb{R}, \; a \ne 0, \;\exists! \; x, \; ax = 1",
            font_size=LABEL_SIZE, color=WHITE,
        )
        self.play(Write(claim), run_time=NORMAL)
        self.wait(0.5)

        # Existence
        exist_label = Text("Existence:", font_size=LABEL_SIZE, color=SECONDARY, font=SANS)
        exist_eq = MathTex(
            r"\text{Let } x = \frac{1}{a}. \quad a \cdot \frac{1}{a} = 1 \;\checkmark",
            font_size=LABEL_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(exist_label, direction=DOWN, anchor=claim, buff=0.4)
        self.play(Write(exist_label), run_time=FAST)
        self.ly.safe_place(exist_eq, direction=DOWN, anchor=exist_label, buff=0.2)
        self.play(Write(exist_eq), run_time=NORMAL)
        self.wait(0.5)

        # Uniqueness
        uniq_label = Text("Uniqueness:", font_size=LABEL_SIZE, color=ACCENT, font=SANS)
        uniq_eq = MathTex(
            r"ax = 1 \text{ and } ay = 1 \Longrightarrow ax = ay \Longrightarrow x = y \;\blacksquare",
            font_size=LABEL_SIZE, color=ACCENT,
        )
        self.ly.safe_place(uniq_label, direction=DOWN, anchor=exist_eq, buff=0.4)
        self.play(Write(uniq_label), run_time=FAST)
        self.ly.safe_place(uniq_eq, direction=DOWN, anchor=uniq_label, buff=0.2)
        self.play(Write(uniq_eq), run_time=NORMAL)
        self.wait(0.5)

        # Notation insight
        insight = Text(
            'This is why we write a^{-1} — there is only ONE inverse to name!',
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=uniq_eq, buff=0.5)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.5)

        self.ly.clear()

    # ─── Scene 8: Summary ───
    def scene8_summary(self):
        self.add_subcaption(
            "To wrap up: existence and uniqueness proofs "
            "answer two questions. "
            "First: does a solution exist? "
            "Prove it with a constructive witness "
            "or a non-constructive argument. "
            "Second: is it the only one? "
            "Assume two solutions and show they must coincide. "
            "One warning: proving uniqueness without existence first "
            "is meaningless. Zero solutions also satisfies at most one. "
            "Next up: proof writing style.",
            duration=20,
        )

        title = self.ly.title("The Complete Recipe")

        items = [
            Text("Step 1: EXISTENCE — exhibit a witness (or argue indirectly)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Step 2: UNIQUENESS — assume two solutions, show equal", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            MathTex(
                r"\exists! \; x, \; P(x) \;=\; \text{existence} \;\wedge\; \text{uniqueness}",
                font_size=LABEL_SIZE, color=WHITE,
            ),
            Text("Warning: uniqueness without existence is meaningless!", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        self.wait(2)

        self.ly.clear()

        play_outro(self, "Proof Writing Style", "Introduction to Proofs")
