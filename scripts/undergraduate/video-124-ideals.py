"""
Video 124: Ideals in Ring Theory
TEMPLATE v2 -- Professional quality Manim script

Playlist: Abstract Algebra I (Video 11 of 12 -- cont.)
Class: Video124_Ideals

Topics: definition of ideal, absorption property, examples in Z and Z[x],
         principal ideals, ideal operations, prime ideals, maximal ideals,
         key theorems (R/P integral domain, R/M field),
         connection to quotient rings.

Based on competitive analysis: first animated explanation of ideals on YouTube.
Color coding: GREEN=arbitrary ideals, YELLOW=principal, BLUE=prime, RED=maximal.

Quality Rules (mandatory):
1. Max 5 visible elements per scene at any time
2. Use LayoutEngine for ALL positioning -- no manual .shift() or .to_edge()
3. Progressive disclosure: add items one at a time
4. Each add_subcaption() duration = words / 2.5 seconds (12 words = 5s)
5. Call ly.clear() between scenes
6. Use consistent animation vocabulary from channel_branding.py
7. MathTex: raw strings with single backslashes
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


class Video124_Ideals(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_motivation()
        self.scene3_definition()
        self.scene4_examples()
        self.scene5_principal_ideals()
        self.scene6_prime_maximal()
        self.scene7_key_theorems()
        self.scene8_summary()

    # --- Scene 1: Hook --- "Why Not Just Subrings?"
    # Narration ~30s.

    def scene1_hook(self):
        self.add_subcaption(
            "Every ring has subrings, but subrings don't let us "
            "build quotient rings. In group theory, we needed "
            "normal subgroups to form quotient groups. "
            "For rings, we need ideals. "
            "Ideals are the ring-theoretic analog of normal subgroups, "
            "and they unlock the deep structure of every ring. "
            "This is Abstract Algebra, Video 124.",
            duration=22.6,
        )
        play_intro(self, "Ideals in Ring Theory", "Abstract Algebra I")

        title = self.ly.title("Why Not Just Subrings?")
        self.wait(1)

        items = [
            Text("Every ring has subrings", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Subrings \u2192 quotient rings?  NO", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("We need a stronger condition: IDEALS", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(8)

        # Bridge formula
        bridge = MathTex(
            r"\text{Normal subgroups} : \text{Groups} \;\approx\; \text{Ideals} : \text{Rings}",
            color=WHITE, font_size=28,
        )
        boxed = self.ly.formula_box(bridge, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=items[-1], direction=DOWN, buff=0.35)
        self.play(Write(bridge), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: Motivation --- From Normal Subgroups to Ideals
    # Narration ~45s.

    def scene2_motivation(self):
        self.add_subcaption(
            "Recall that for groups, we needed normal subgroups "
            "to form quotient groups. The condition g N g inverse equals N "
            "guaranteed well-defined multiplication of cosets. "
            "For rings, addition of cosets is always well-defined "
            "because any additive subgroup gives abelian cosets. "
            "But multiplication is the constraint. "
            "For R over I to be a ring, "
            "we need the product of any coset r plus I "
            "with any coset s plus I to land in coset r s plus I. "
            "This forces a strong condition on I: "
            "for every r in R and a in I, "
            "both r a and a r must lie in I. "
            "This is called the absorption law.",
            duration=41.1,
        )

        self.ly.section_divider("1", "From Groups to Rings")

        title = self.ly.title("The Normal Subgroup Analogy")
        self.wait(1)

        # Two-column comparison
        left_items = [
            Text("Groups", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
            Text("N \u25c1 G  (normal subgroup)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("gNg\u207b\u00b9 = N", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("\u2192 G/N is a group", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        right_items = [
            Text("Rings", font_size=HEADING_SIZE, color=PRIMARY, font=SANS),
            Text("I \u25c1 R  (ideal)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("rI \u2286 I, Ir \u2286 I", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("\u2192 R/I is a ring", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        left_group, right_group = self.ly.two_columns(left_items, right_items, start_from=title)

        self.play(
            *[FadeIn(item, shift=LEFT * 0.15) for item in left_items],
            *[FadeIn(item, shift=RIGHT * 0.15) for item in right_items],
            run_time=1.5,
        )
        self.wait(10)

        self.ly.clear()

        # Absorption law highlight
        title2 = self.ly.title("The Absorption Law")
        self.wait(1)

        absorption = MathTex(
            r"\forall\, r \in R,\; a \in I: \quad r a \in I \;\text{ and }\; a r \in I",
            color=WHITE, font_size=32,
        )
        boxed = self.ly.formula_box(absorption, color=SECONDARY)
        self.ly.center_in_content(boxed)
        self.play(Write(absorption), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        items = [
            Text("This is the ring-theoretic analog of normality", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Without it, coset multiplication breaks", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed, run_time=0.8)
        self.wait(17.4)  # pacing: extends previous caption slot (+9.4s)

        self.ly.clear()

    # --- Scene 3: Definition of an Ideal
    # Narration ~40s.

    def scene3_definition(self):
        self.add_subcaption(
            "Formally, a subset I of a ring R is an ideal "
            "if it satisfies two conditions. "
            "First, I is an additive subgroup of R. "
            "Second, I absorbs multiplication from both sides: "
            "for every r in R and every a in I, "
            "both r a and a r belong to I. "
            "We write I triangle-left R. "
            "If R is commutative, left and right absorption coincide, "
            "so every ideal is automatically two-sided. "
            "Every ideal is a subring, but the converse is false: "
            "not every subring is an ideal.",
            duration=33.9,
        )

        self.ly.section_divider("2", "Definition")

        title = self.ly.title("Definition of an Ideal")
        self.wait(1)

        # Formal definition
        defn_line1 = MathTex(
            r"I \trianglelefteq R \;\text{ if } I \subseteq R \text{ and:}",
            color=WHITE, font_size=30,
        )
        self.ly.center_in_content(defn_line1)
        self.play(Write(defn_line1), run_time=NORMAL)
        self.wait(3)

        # Clear and show conditions
        self.ly.clear()

        title2 = self.ly.title("Two Conditions")
        self.wait(1)

        cond1 = MathTex(
            r"\text{(1) } (I, +) \leq (R, +) \quad\text{(additive subgroup)}",
            color=SECONDARY, font_size=30,
        )
        cond2 = MathTex(
            r"\text{(2) } \forall\, r \in R,\; a \in I:\; r a \in I \;\text{ and }\; a r \in I",
            color=ACCENT, font_size=30,
        )
        self.ly.safe_place(cond1, anchor=title2, direction=DOWN, buff=0.4)
        self.play(Write(cond1), run_time=NORMAL)
        self.wait(3)

        self.ly.safe_place(cond2, anchor=cond1, direction=DOWN, buff=0.35)
        self.play(Write(cond2), run_time=NORMAL)
        self.wait(5)

        # Note about commutativity
        note = Text(
            "Commutative rings \u2192 left = right (automatic)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(note, anchor=cond2, direction=DOWN, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(13.8)  # pacing: extends previous caption slot (+9.8s)

        self.ly.clear()

    # --- Scene 4: Examples
    # Narration ~50s.

    def scene4_examples(self):
        self.add_subcaption(
            "Let's see concrete examples. "
            "In the integers, the multiples of n form an ideal. "
            "We write n Z equals the set of all integer multiples of n. "
            "This is closed under addition, and any integer times "
            "a multiple of n is again a multiple of n. "
            "In the polynomial ring Z bracket x, "
            "the set of all polynomials divisible by x "
            "forms the ideal (x). "
            "These are polynomials with zero constant term. "
            "Every ideal must also contain zero, "
            "and R itself is always an ideal. "
            "These are the trivial ideals. "
            "A key counterexample: Z is a subring of Q, "
            "but not an ideal. One half times one equals one half, "
            "which is not an integer. "
            "The absorption law fails.",
            duration=46.3,
        )

        title = self.ly.title("Example: nZ in Z")
        self.wait(1)

        # Example 1: nZ
        nz = MathTex(
            r"n\mathbb{Z} = \{\ldots, -2n, -n, 0, n, 2n, \ldots\}",
            color=WHITE, font_size=34,
        )
        boxed = self.ly.formula_box(nz, color=SECONDARY)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.4)
        self.play(Write(nz), Create(boxed[1]), run_time=NORMAL)
        self.wait(3)

        checks = [
            Text("(I,+) subgroup \u2713", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Z \u00b7 (nZ) \u2286 nZ \u2713 (absorption)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        visible = self.ly.progressive_reveal(checks, start_from=boxed, run_time=0.8)
        self.wait(6)

        self.ly.clear()

        # Example 2: (x) in Z[x]
        title2 = self.ly.title("Example: (x) in Z[x]")
        self.wait(1)

        px = MathTex(
            r"(x) = \{x \cdot f(x) \mid f(x) \in \mathbb{Z}[x]\}",
            color=WHITE, font_size=30,
        )
        boxed2 = self.ly.formula_box(px, color=PRIMARY)
        self.ly.safe_place(boxed2, anchor=title2, direction=DOWN, buff=0.4)
        self.play(Write(px), Create(boxed2[1]), run_time=NORMAL)
        self.wait(3)

        desc = Text(
            "Polynomials with zero constant term",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(desc, anchor=boxed2, direction=DOWN, buff=0.35)
        self.play(FadeIn(desc, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Counterexample
        title3 = self.ly.title("Counterexample: Z in Q")
        self.wait(1)

        bad = MathTex(
            r"\mathbb{Z} \subset \mathbb{Q}: \quad \tfrac{1}{2} \cdot 1 = \tfrac{1}{2} \notin \mathbb{Z}",
            color=RED, font_size=30,
        )
        boxed3 = self.ly.formula_box(bad, color=RED)
        self.ly.safe_place(boxed3, anchor=title3, direction=DOWN, buff=0.4)
        self.play(Write(bad), Create(boxed3[1]), run_time=NORMAL)
        self.wait(4)

        verdict = Text(
            "Z is a subring of Q, but NOT an ideal",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(verdict, anchor=boxed3, direction=DOWN, buff=0.35)
        self.play(FadeIn(verdict, shift=LEFT * 0.15), run_time=FAST)
        self.wait(15.2)  # pacing: extends previous caption slot (+11.2s)

        self.ly.clear()

    # --- Scene 5: Principal Ideals and Ideal Operations
    # Narration ~50s.

    def scene5_principal_ideals(self):
        self.add_subcaption(
            "A principal ideal is generated by a single element. "
            "The ideal generated by a in R is the set of all "
            "r a plus n a, where r ranges over R and n over Z. "
            "In a commutative ring with unity, this simplifies to "
            "the set of all r a for r in R. "
            "A remarkable fact: in the integers Z, "
            "every ideal is principal. "
            "The containment (a) subset (b) holds "
            "if and only if b divides a. "
            "We can also combine ideals: "
            "the sum I plus J is the smallest ideal containing both, "
            "and the intersection I intersect J is also an ideal.",
            duration=39.0,
        )

        self.ly.section_divider("3", "Principal Ideals")

        title = self.ly.title("Principal Ideals")
        self.wait(1)

        gen = MathTex(
            r"\langle a \rangle = \{ra + na \mid r \in R,\; n \in \mathbb{Z}\}",
            color=WHITE, font_size=30,
        )
        boxed = self.ly.formula_box(gen, color=ACCENT)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.4)
        self.play(Write(gen), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        facts = [
            Text("In Z: every ideal is principal (Z is a PID)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text(r"$\langle a \rangle \subseteq \langle b \rangle$  iff  $b \mid a$", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("(6) = 6Z, (4) = 4Z, (12) = 12Z", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(facts, start_from=boxed, run_time=0.8)
        self.wait(8)

        self.ly.clear()

        # Ideal operations
        title2 = self.ly.title("Ideal Operations")
        self.wait(1)

        sum_ideal = MathTex(
            r"I + J = \{i + j \mid i \in I,\; j \in J\}",
            color=PRIMARY, font_size=30,
        )
        prod_ideal = MathTex(
            r"I \cap J \;\text{ is also an ideal}",
            color=SECONDARY, font_size=30,
        )
        smallest = Text(
            "I + J is the smallest ideal containing both I and J",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(sum_ideal, anchor=title2, direction=DOWN, buff=0.4)
        self.play(Write(sum_ideal), run_time=NORMAL)
        self.wait(3)

        self.ly.safe_place(prod_ideal, anchor=sum_ideal, direction=DOWN, buff=0.35)
        self.play(Write(prod_ideal), run_time=NORMAL)
        self.wait(3)

        self.ly.safe_place(smallest, anchor=prod_ideal, direction=DOWN, buff=0.35)
        self.play(FadeIn(smallest, shift=LEFT * 0.15), run_time=FAST)
        self.wait(8.3)  # pacing: extends previous caption slot (+4.3s)

        self.ly.clear()

    # --- Scene 6: Prime and Maximal Ideals
    # Narration ~45s.

    def scene6_prime_maximal(self):
        self.add_subcaption(
            "Two special types of ideals reveal the deepest structure of a ring. "
            "A prime ideal P satisfies: "
            "if the product a b is in P, then a is in P or b is in P. "
            "This mirrors the definition of a prime number. "
            "A maximal ideal M is one where "
            "no proper ideal sits strictly between M and R. "
            "Every maximal ideal is prime, but not conversely, "
            "unless R is a principal ideal domain. "
            "In Z, the ideal (p) is both prime and maximal "
            "when p is a prime number. "
            "In Z bracket x, the ideal (x) is prime "
            "but not maximal, since (x) is contained in (2, x).",
            duration=43.1,
        )

        self.ly.section_divider("4", "Prime and Maximal Ideals")

        # Prime ideal definition
        title = self.ly.title("Prime Ideal")
        self.wait(1)

        prime_def = MathTex(
            r"P \trianglelefteq R \text{ is prime if } ab \in P \Rightarrow a \in P \;\text{or}\; b \in P",
            color=WHITE, font_size=28,
        )
        boxed = self.ly.formula_box(prime_def, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.4)
        self.play(Write(prime_def), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        prime_note = Text(
            "Mirrors: prime p | ab \u2192 p|a or p|b",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(prime_note, anchor=boxed, direction=DOWN, buff=0.35)
        self.play(FadeIn(prime_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Maximal ideal definition
        title2 = self.ly.title("Maximal Ideal")
        self.wait(1)

        max_def = MathTex(
            r"M \trianglelefteq R \text{ is maximal if } M \subsetneq J \subseteq R \Rightarrow J = R",
            color=WHITE, font_size=28,
        )
        boxed2 = self.ly.formula_box(max_def, color=RED)
        self.ly.safe_place(boxed2, anchor=title2, direction=DOWN, buff=0.4)
        self.play(Write(max_def), Create(boxed2[1]), run_time=NORMAL)
        self.wait(4)

        max_note = Text(
            "No proper ideal sits strictly between M and R",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(max_note, anchor=boxed2, direction=DOWN, buff=0.35)
        self.play(FadeIn(max_note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Containment relationship
        title3 = self.ly.title("Maximal \u2282 Prime")
        self.wait(1)

        items = [
            Text("Every maximal ideal is prime", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("The converse is FALSE in general", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("Exception: in a PID, maximal = prime", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title3, run_time=0.8)
        self.wait(12.9)  # pacing: extends previous caption slot (+6.9s)

        self.ly.clear()

    # --- Scene 7: Key Theorems
    # Narration ~45s.

    def scene7_key_theorems(self):
        self.add_subcaption(
            "Ideals are worth studying because they classify quotient rings. "
            "Two beautiful theorems make this precise. "
            "First: an ideal P is prime "
            "if and only if the quotient ring R over P "
            "is an integral domain. "
            "The absence of zero divisors in the quotient "
            "mirrors the primality condition on the ideal. "
            "Second: an ideal M is maximal "
            "if and only if R over M is a field. "
            "Every nonzero element being invertible in the quotient "
            "means there is no room between M and R. "
            "Example: Z over (5) is Z subscript 5, which is a field. "
            "So (5) is maximal and prime. "
            "But Z over (6) is Z subscript 6, which has zero divisors. "
            "Since 2 times 3 equals 0 in Z subscript 6, "
            "the ideal (6) is neither prime nor maximal.",
            duration=54.4,
        )

        self.ly.section_divider("5", "Key Theorems")

        title = self.ly.title("The Payoff: Quotient Rings")
        self.wait(1)

        # Theorem 1: Prime
        thm1_label = Text(
            "Theorem 1:", font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        thm1 = MathTex(
            r"P \text{ is prime } \Leftrightarrow R/P \text{ is an integral domain}",
            color=WHITE, font_size=28,
        )
        thm1_group = VGroup(thm1_label, thm1).arrange(RIGHT, buff=0.3)
        self.ly.safe_place(thm1_group, anchor=title, direction=DOWN, buff=0.4)
        self.play(FadeIn(thm1_label, shift=LEFT * 0.15), Write(thm1), run_time=NORMAL)
        self.wait(5)

        # Theorem 2: Maximal
        thm2_label = Text(
            "Theorem 2:", font_size=BODY_SIZE, color=RED, font=SANS,
        )
        thm2 = MathTex(
            r"M \text{ is maximal } \Leftrightarrow R/M \text{ is a field}",
            color=WHITE, font_size=28,
        )
        thm2_group = VGroup(thm2_label, thm2).arrange(RIGHT, buff=0.3)
        self.ly.safe_place(thm2_group, anchor=thm1_group, direction=DOWN, buff=0.4)
        self.play(FadeIn(thm2_label, shift=LEFT * 0.15), Write(thm2), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

        # Containment chain: field ⊂ integral domain ⊂ ring
        title2 = self.ly.title("The Hierarchy")
        self.wait(1)

        chain = MathTex(
            r"\text{field} \;\subset\; \text{integral domain} \;\subset\; \text{ring}",
            color=WHITE, font_size=30,
        )
        boxed = self.ly.formula_box(chain, color=PRIMARY)
        self.ly.center_in_content(boxed)
        self.play(Write(chain), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        items = [
            Text("R/M is a field \u2192 M is maximal \u2192 M is prime", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("R/P is an integral domain \u2192 P is prime", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed, run_time=0.8)
        self.wait(6)

        self.ly.clear()

        # Worked example
        title3 = self.ly.title("Example: Ideals of Z")
        self.wait(1)

        ex_good = MathTex(
            r"\mathbb{Z}/(5) \cong \mathbb{Z}_5 \;\text{ is a field} \Rightarrow (5) \text{ is maximal}",
            color=SECONDARY, font_size=26,
        )
        boxed_good = self.ly.formula_box(ex_good, color=SECONDARY)
        self.ly.safe_place(boxed_good, anchor=title3, direction=DOWN, buff=0.4)
        self.play(Write(ex_good), Create(boxed_good[1]), run_time=NORMAL)
        self.wait(4)

        ex_bad = MathTex(
            r"\mathbb{Z}/(6) \cong \mathbb{Z}_6: \quad 2 \cdot 3 = 0 \Rightarrow (6) \text{ is not prime}",
            color=RED, font_size=26,
        )
        boxed_bad = self.ly.formula_box(ex_bad, color=RED)
        self.ly.safe_place(boxed_bad, anchor=boxed_good, direction=DOWN, buff=0.4)
        self.play(Write(ex_bad), Create(boxed_bad[1]), run_time=NORMAL)
        self.wait(15.9)  # pacing: extends previous caption slot (+10.9s)

        self.ly.clear()

    # --- Scene 8: Summary and Preview
    # Narration ~30s.

    def scene8_summary(self):
        self.add_subcaption(
            "Let's recap what we've learned. "
            "Ideals are to rings what normal subgroups are to groups. "
            "The absorption law is the key condition "
            "that makes quotient rings well-defined. "
            "Principal ideals are generated by a single element, "
            "and in Z every ideal is principal. "
            "Prime ideals capture the no-zero-divisor property, "
            "while maximal ideals capture the every-element-invertible property. "
            "Next time, we'll construct quotient rings R over I "
            "and explore their structure in detail.",
            duration=29.9,
        )

        title = self.ly.title("Summary")
        self.wait(1)

        items = [
            Text("Ideals \u2261 ring-theoretic normal subgroups", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Absorption law: r a, a r \u2208 I for all r\u2208R, a\u2208I", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Z is a PID: every ideal is principal", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Prime \u2192 R/P integral domain; Maximal \u2192 R/M field", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(17.2)  # pacing: extends previous caption slot (+7.2s)

        self.ly.clear()
        play_outro(self, next_video="Quotient Rings", next_playlist="Abstract Algebra I")
