r"""
Video 225: Insolvability of the Quintic (Abel-Ruffini Theorem) — Advanced Abstract Algebra

The climactic video of the Advanced Abstract Algebra playlist.
Proves Abel-Ruffini using: A5 simplicity -> S5 not solvable -> general quintic
Galois group is S5 -> not solvable by radicals.

Follows v2 template quality rules.
"""

from manim import *
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video225_InsolvabilityQuintic(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_strategy()
        self.scene3_a5_simple()
        self.scene4_s5_not_solvable()
        self.scene5_general_quintic()
        self.scene6_abel_ruffini()
        self.scene7_nuance()
        self.scene8_history()
        self.scene9_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "For two hundred years, the greatest mathematicians in Europe "
            "searched for a general formula to solve the quintic equation. "
            "Today, using Galois theory, we will prove the Abel-Ruffini theorem.",
            duration=12,
        )
        play_intro(self, "Insolvability of the Quintic", "Advanced Abstract Algebra")

        title = self.ly.title("The Impossible Equation")
        items = [
            Text("For 200 years, mathematicians sought a general quintic formula",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Abel (1824) and Ruffini (1799) proved it impossible",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Today: the full proof using Galois theory",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Strategy: show S5 is not solvable, and S5 is the Galois group",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.ly.clear()

    def scene2_strategy(self):
        self.add_subcaption(
            "From Video 224, a polynomial is solvable by radicals if and only if "
            "its Galois group is solvable. So we need two things: "
            "S5 is not solvable, and the general quintic has Galois group S5.",
            duration=11,
        )
        title = self.ly.title("The Proof Strategy")

        thm1 = MathTex(
            r"f 	ext{ solvable by radicals } \iff 	ext{Gal}(	ext{Split}(f)/F) 	ext{ solvable}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        boxed1 = self.ly.formula_box(thm1, PRIMARY)
        self.ly.safe_place(boxed1, DOWN, anchor=title, buff=0.5)
        self.play(Write(thm1), run_time=NORMAL)
        self.wait(3)
        self.play(FadeOut(boxed1), run_time=FAST)

        step1 = Text("Step 1: Prove S5 is not solvable",
                      font_size=HEADING_SIZE, color=RED, font=SANS)
        step2 = Text("Step 2: Prove general quintic has Galois group S5",
                      font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        group = self.ly.stack_down([step1, step2], start_from=title, spacing=0.6)
        self.play(FadeIn(step1, shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(step2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene3_a5_simple(self):
        self.add_subcaption(
            "A group is simple if its only normal subgroups are the trivial group "
            "and itself. The key lemma: the alternating group A5 is simple. "
            "Every element of A5 is either a 3-cycle, a product of two transpositions, "
            "or the identity. All 3-cycles are conjugate in A5, "
            "and the 3-cycles generate A5. So A5 is simple.",
            duration=24,
        )
        self.ly.section_divider(1, "S5 Is Not Solvable")
        title = self.ly.title("The Alternating Group A5 Is Simple")

        defn = MathTex(
            r"G \text{ is } \mathbf{simple} 	ext{ if } N \triangleleft G "
            r"\implies N = \{e\} \text{ or } N = G",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        boxed_def = self.ly.formula_box(defn, PRIMARY)
        self.ly.safe_place(boxed_def, DOWN, anchor=title, buff=0.4)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(4)
        self.play(FadeOut(boxed_def), run_time=FAST)

        elements = [
            MathTex(r"A_5 = \{(1),\ 3\text{-cycles},\ (ab)(cd)\}",
                    font_size=BODY_SIZE, color=WHITE),
            MathTex(r"\text{All } 3\text{-cycles are conjugate in } A_5",
                    font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"\text{3-cycles generate } A_5",
                    font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"\therefore\ A_5 \text{ is simple } \checkmark",
                    font_size=HEADING_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(elements)
        self.wait(5)
        self.ly.clear()

    def scene4_s5_not_solvable(self):
        self.add_subcaption(
            "The commutator subgroup of S5 is A5. Since A5 is simple and non-abelian, "
            "its commutator subgroup is A5 itself. So the derived series is "
            "S5, A5, A5, forever. It never terminates. Compare D4 from Video 224: "
            "its derived series was D4, V4, trivial. D4 is solvable, S5 is not.",
            duration=18,
        )
        title = self.ly.title("S5 Is Not Solvable")

        # S5 derived series
        s5_series = [
            MathTex(r"S_5'", font_size=HEADING_SIZE, color=RED),
            MathTex(r"= A_5", font_size=HEADING_SIZE, color=RED),
            MathTex(r"A_5' = A_5 \quad \text{(simple, non-abelian)}",
                    font_size=BODY_SIZE, color=RED),
            MathTex(r"S_5 > A_5 > A_5 > A_5 > \cdots"),
        ]
        self.ly.progressive_reveal(s5_series, start_from=title)
        self.wait(3)

        # Red X
        x_mark = Text("NOT SOLVABLE", font_size=LABEL_SIZE, color=RED, font=SANS)
        self.ly.safe_place(x_mark, DOWN, anchor=s5_series[-1], buff=0.3)
        self.play(FadeIn(x_mark), run_time=FAST)
        self.wait(3)
        self.play(FadeOut(x_mark), run_time=FAST)
        self.ly.clear()

        # Contrast with D4
        contrast_title = self.ly.title("Contrast: D4 IS Solvable")
        d4_items = [
            MathTex(r"D_4' = V_4", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"V_4' = \{e\}", font_size=BODY_SIZE, color=SECONDARY),
            MathTex(r"D_4 > V_4 > \{e\} \quad \checkmark \text{ SOLVABLE}",
                    font_size=HEADING_SIZE, color=ACCENT),
        ]
        self.ly.progressive_reveal(d4_items, start_from=contrast_title)
        self.wait(5)
        self.ly.clear()

    def scene5_general_quintic(self):
        self.add_subcaption(
            "The general polynomial of degree n has independent transcendental coefficients. "
            "Its Galois group over that field is the full symmetric group Sn. "
            "The proof uses faithful action on the n roots. "
            "For n equals 5, the Galois group is S5.",
            duration=16,
        )
        self.ly.section_divider(2, "The General Quintic Has Galois Group S5")
        title = self.ly.title("The General Polynomial")

        gen_poly = MathTex(
            r"f(x) = x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(gen_poly, DOWN, anchor=title, buff=0.4)
        self.play(Write(gen_poly), run_time=NORMAL)
        self.wait(3)

        items = [
            Text("Coefficients a_0, ..., a_{n-1} are independent transcendentals",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Galois group acts faithfully on the n roots",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=gen_poly)
        self.wait(3)
        self.ly.clear()

        # Key lemma
        lemma_title = self.ly.title("Key Lemma")
        lemma = MathTex(
            r"\text{Gal}(	ext{Split}(f)/\mathbb{Q}(a_0, \ldots, a_{n-1})) \cong S_n",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed_lemma = self.ly.formula_box(lemma, ACCENT)
        self.ly.safe_place(boxed_lemma, DOWN, anchor=lemma_title, buff=0.4)
        self.play(Write(lemma), run_time=NORMAL)
        self.wait(3)

        specialize = Text("For n = 5: Galois group is S5",
                          font_size=HEADING_SIZE, color=RED, font=SANS)
        self.ly.safe_place(specialize, DOWN, anchor=boxed_lemma, buff=0.4)
        self.play(FadeIn(specialize, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene6_abel_ruffini(self):
        self.add_subcaption(
            "The general quintic has Galois group S5. S5 is not solvable. "
            "Therefore, by the solvability-by-radicals theorem, "
            "the general quintic is not solvable by radicals. "
            "This is the Abel-Ruffini theorem. QED.",
            duration=12,
        )
        title = self.ly.title("The Abel-Ruffini Theorem")

        chain = [
            Text("1. General quintic has Galois group S5",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. S5 is not solvable (derived series doesn\'t terminate)",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3. Therefore: general quintic not solvable by radicals",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(chain, start_from=title)
        self.wait(4)
        self.ly.clear()

        # Final theorem box
        thm_title = self.ly.title("ABEL-RUFFINI THEOREM")
        thm = MathTex(
            r"\text{No general radical formula exists for } \deg(f) \geq 5",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        boxed = self.ly.formula_box(thm, ACCENT)
        self.ly.safe_place(boxed, DOWN, anchor=thm_title, buff=0.4)
        self.play(Write(thm), run_time=NORMAL)
        self.wait(2)

        qed = Text("Q.E.D.", font_size=TITLE_SIZE, color=ACCENT, font=SANS)
        self.ly.safe_place(qed, DOWN, anchor=boxed, buff=0.5)
        self.play(Write(qed), run_time=NORMAL)
        self.wait(6)
        self.ly.clear()

    def scene7_nuance(self):
        self.add_subcaption(
            "The Abel-Ruffini theorem says the general quintic has no radical formula. "
            "But specific quintics can still be solvable. "
            "For example, x to the fifth minus 1 has Galois group "
            "cyclic of order 4, which is solvable. "
            "The theorem only rules out a universal formula.",
            duration=16,
        )
        self.ly.section_divider(3, "Nuance")
        title = self.ly.title("Not All Quintics Are Unsolvable")

        poly = MathTex(
            r"x^5 - 1 = (x-1)(x^4 + x^3 + x^2 + x + 1)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(poly, DOWN, anchor=title, buff=0.4)
        self.play(Write(poly), run_time=NORMAL)
        self.wait(3)

        items = [
            Text("Splitting field: Q(zeta_5), a cyclotomic extension",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Galois group: cyclic of order 4 (solvable!)",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("GENERAL quintic: no formula  vs  SPECIFIC quintics: many ARE solvable",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=poly)
        self.wait(5)
        self.ly.clear()

    def scene8_history(self):
        self.add_subcaption(
            "Ruffini published a proof in 1799, but it was incomplete. "
            "Abel gave the first accepted proof in 1824. "
            "But it was Galois, around 1832, who understood why. "
            "The insight that polynomial solvability reduces to group solvability "
            "is one of the most profound in all of mathematics.",
            duration=16,
        )
        title = self.ly.title("History")
        items = [
            Text("Ruffini (1799): first attempt, incomplete proof",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Abel (1824): first accepted proof",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Galois (1832): understood WHY — the deepest insight",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(6)
        self.ly.clear()

    def scene9_summary(self):
        self.add_subcaption(
            "A5 is simple. S5 derived series never terminates, so S5 is not solvable. "
            "The general quintic has Galois group S5. "
            "Therefore the general quintic is not solvable by radicals. "
            "This is the Abel-Ruffini theorem, the climax of Galois theory.",
            duration=14,
        )
        self.ly.section_divider(4, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("A5 is simple: no nontrivial proper normal subgroups",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("S5\' = A5, A5\' = A5, so S5 is not solvable",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The general quintic has Galois group S5",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Abel-Ruffini: general quintic not solvable by radicals",
                 font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Specific quintics (like x^5 - 1) can still be solvable",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4)
        self.ly.clear()

        play_outro(self, "Cyclotomic Fields", "Advanced Abstract Algebra")
