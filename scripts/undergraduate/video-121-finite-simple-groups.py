"""
Video 121: Finite Simple Groups
TEMPLATE v2 -- Professional quality Manim script

Playlist: Abstract Algebra I (Video 11 of 12)
Class: Video121_FiniteSimpleGroups

Topics: definition of simple groups, why they matter (building blocks of
         finite groups), the classification of finite simple groups,
         simplicity of A_n for n >= 5 (proof sketch using conjugacy
         classes), A_5 as the smallest non-abelian simple group.

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


class Video121_FiniteSimpleGroups(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_why_simple_groups()
        self.scene4_classification_overview()
        self.scene5_an_simple_for_n_ge_5()
        self.scene6_proving_a5_simple()
        self.scene7_conjugacy_classes()
        self.scene8_summary()

    # --- Scene 1: Hook --- "The Atoms of Group Theory"
    # Narration ~35s.

    def scene1_hook(self):
        self.add_subcaption(
            "Every integer greater than one factors uniquely into primes. "
            "What if groups had a similar decomposition? "
            "Simple groups are to group theory what prime numbers are to arithmetic. "
            "A simple group has no nontrivial proper normal subgroups, "
            "meaning it cannot be broken down any further. "
            "Understanding simple groups is the key to understanding all finite groups. "
            "Today we will define simple groups, explore why they matter, "
            "and prove that the alternating group A_n is simple for all n >= 5. "
            "This is Abstract Algebra, Video 11.",
            duration=35,
        )
        play_intro(self, "Finite Simple Groups", "Abstract Algebra I")

        title = self.ly.title("The Atoms of Group Theory")
        self.wait(2)

        items = [
            Text("Primes \u2192 building blocks of integers", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Simple groups \u2192 building blocks of groups", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Cannot be decomposed any further", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(6)

        # Key question
        q = MathTex(
            r"1 = p_1 \cdots p_k \quad \longleftrightarrow \quad G = G_0 \rhd G_1 \rhd \cdots \rhd G_k = \{e\}",
            color=WHITE, font_size=30,
        )
        boxed = self.ly.formula_box(q, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=items[-1], direction=DOWN, buff=0.4)
        self.play(Write(q), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 2: Definition of Simple Groups ---
    # Narration ~40s.

    def scene2_definition(self):
        self.add_subcaption(
            "A group G is called simple if its only normal subgroups "
            "are the trivial group and G itself. "
            "Formally, if N is a normal subgroup of G, "
            "then N equals the identity or N equals G. "
            "Equivalently, a group is simple if it has no nontrivial "
            "proper normal subgroups. "
            "The word simple does not mean easy or small. "
            "It means indivisible. "
            "Cyclic groups of prime order are simple, "
            "because by Lagrange's theorem, the only subgroups have "
            "order 1 or p. "
            "But there are also non-abelian simple groups, "
            "and those are far more interesting.",
            duration=40,
        )
        self.ly.section_divider("1", "Definition of Simple Groups")

        title = self.ly.title("Simple Groups")
        self.wait(1)

        # Definition box
        defn = MathTex(
            r"G \text{ is simple } \iff N \triangleleft G \implies N = \{e\} \text{ or } N = G",
            color=WHITE, font_size=32,
        )
        boxed = self.ly.formula_box(defn, color=ACCENT)
        self.ly.center_in_content(boxed)
        self.play(Write(defn), Create(boxed[1]), run_time=NORMAL)
        self.wait(6)

        self.ly.clear()

        # Examples and non-examples
        title2 = self.ly.title("Examples")
        self.wait(1)

        items = [
            Text(r"\mathbb{Z}_p for prime p \u2014 abelian, simple", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text(r"\mathbb{Z}_6 \u2014 NOT simple (3 \triangleleft \mathbb{Z}_6)", font_size=BODY_SIZE, color=RED, font=SANS),
            Text(r"S_3 \u2014 NOT simple (A_3 \triangleleft S_3)", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        visible = self.ly.progressive_reveal(items, start_from=title2, run_time=0.8)
        self.wait(5)

        # FadeOut examples before adding new content (content budget)
        self.play(*[FadeOut(v) for v in visible if v is not None], run_time=FAST)

        # Highlight: abelian vs non-abelian
        note = Text(
            "All abelian simple groups are cyclic of prime order",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, anchor=title2, direction=DOWN, buff=0.5)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        # Tease
        tease = Text(
            "The real mystery: non-abelian simple groups",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(tease, anchor=note, direction=DOWN, buff=0.35)
        self.play(FadeIn(tease, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # --- Scene 3: Why Simple Groups Matter ---
    # Narration ~35s.

    def scene3_why_simple_groups(self):
        self.add_subcaption(
            "Why do we care about simple groups? "
            "The answer comes from composition series. "
            "A composition series is a chain of subgroups "
            "where each subgroup is normal in the previous one, "
            "and the quotients are all simple groups. "
            "The Jordan-Holder theorem says that the simple groups "
            "appearing as quotients are uniquely determined by G, "
            "up to isomorphism and ordering. "
            "This is the group-theoretic analogue of unique "
            "prime factorization of integers. "
            "If we can classify all simple groups, "
            "then in principle we can classify all finite groups.",
            duration=35,
        )
        self.ly.section_divider("2", "Why Simple Groups Matter")

        title = self.ly.title("Composition Series")
        self.wait(1)

        # Composition series definition
        series = MathTex(
            r"G = G_0 \rhd G_1 \rhd G_2 \rhd \cdots \rhd G_k = \{e\}",
            color=WHITE, font_size=32,
        )
        self.ly.safe_place(series)
        self.play(Write(series), run_time=NORMAL)
        self.wait(3)

        # Quotient condition
        quot = MathTex(
            r"G_i / G_{i+1} \text{ is simple for each } i",
            color=ACCENT, font_size=30,
        )
        self.ly.safe_place(quot, anchor=series, direction=DOWN, buff=0.4)
        self.play(Write(quot), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        title2 = self.ly.title("Jordan-Holder Theorem")
        self.wait(1)

        items = [
            Text("Composition factors are unique (up to isomorphism)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Analogous to unique prime factorization", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Classify simple groups \u21d2 classify ALL finite groups", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2, run_time=0.8)
        self.wait(6)

        self.ly.clear()

    # --- Scene 4: Classification Overview ---
    # Narration ~35s.

    def scene4_classification_overview(self):
        self.add_subcaption(
            "One of the greatest achievements of 20th century mathematics "
            "is the classification of finite simple groups. "
            "The theorem, proved by hundreds of mathematicians "
            "over several decades, states that every finite simple group "
            "belongs to one of four families. "
            "First, the cyclic groups of prime order. "
            "Second, the alternating groups A_n for n >= 5. "
            "Third, the groups of Lie type, which are related to "
            "algebraic groups over finite fields. "
            "And fourth, the 26 sporadic groups, "
            "which do not fit into any of the other families. "
            "The largest sporadic group is called the Monster, "
            "and has approximately 8 times 10 to the 53rd elements.",
            duration=35,
        )
        self.ly.section_divider("3", "The Classification")

        title = self.ly.title("Classification of Finite Simple Groups")
        self.wait(1)

        # The four families
        left_items = [
            Text("1. Cyclic: Z_p (p prime)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("2. Alternating: A_n (n \u2265 5)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        right_items = [
            Text("3. Lie type (16 infinite families)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("4. Sporadic (26 groups)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        left_col, right_col = self.ly.two_columns(left_items, right_items, start_from=title)
        self.play(
            FadeIn(left_col[0], shift=LEFT * 0.15), run_time=NORMAL,
        )
        self.play(
            FadeIn(left_col[1], shift=LEFT * 0.15), run_time=FAST,
        )
        self.play(
            FadeIn(right_col[0], shift=RIGHT * 0.15), run_time=FAST,
        )
        self.play(
            FadeIn(right_col[1], shift=RIGHT * 0.15), run_time=FAST,
        )
        self.wait(6)

        # Monster fact — FadeOut columns first (content budget)
        self.play(
            *[FadeOut(left_col[i]) for i in range(len(left_col))],
            *[FadeOut(right_col[i]) for i in range(len(right_col))],
            run_time=FAST,
        )
        monster = MathTex(
            r"|\text{Monster}| \approx 8 \times 10^{53}",
            color=RED, font_size=34,
        )
        monster_label = Text(
            "The Monster Group", font_size=LABEL_SIZE, color=RED, font=SANS,
        )
        monster_group = VGroup(monster, monster_label).arrange(DOWN, buff=0.2)
        self.ly.safe_place(monster_group, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(monster), FadeIn(monster_label), run_time=NORMAL)
        self.wait(5)

        # Proof scale — FadeOut monster first (content budget)
        self.play(FadeOut(monster_group), run_time=FAST)
        scale = Text(
            "Proof: ~10,000 pages across 500+ papers (1960\u20132004)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(scale, anchor=title, direction=DOWN, buff=0.6)
        self.play(FadeIn(scale, shift=LEFT * 0.1), run_time=FAST)
        self.wait(4)

        self.ly.clear()

    # --- Scene 5: A_n is Simple for n >= 5 (Statement + Intuition) ---
    # Narration ~40s.

    def scene5_an_simple_for_n_ge_5(self):
        self.add_subcaption(
            "Now we come to one of the most important theorems "
            "in finite group theory. "
            "The alternating group A_n is simple for every n >= 5. "
            "The cases n = 1, 2, 3, 4 are all not simple. "
            "The proof strategy is elegant. "
            "We will show that every nontrivial normal subgroup N of A_n "
            "must contain a 3-cycle. "
            "Then, since N is normal and A_n acts transitively on 3-cycles, "
            "N must contain ALL 3-cycles. "
            "But the 3-cycles generate A_n. "
            "So N equals A_n, proving simplicity. "
            "For A_5 specifically, we can prove this directly "
            "using conjugacy class sizes.",
            duration=40,
        )
        self.ly.section_divider("4", "Simplicity of A_n")

        title = self.ly.title("Theorem: A_n is Simple for n \u2265 5")
        self.wait(1)

        # Statement
        theorem = MathTex(
            r"A_n \text{ is simple for all } n \geq 5",
            color=WHITE, font_size=34,
        )
        boxed = self.ly.formula_box(theorem, color=ACCENT)
        self.ly.center_in_content(boxed)
        self.play(Write(theorem), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

        # Small cases
        title2 = self.ly.title("Small Cases (Not Simple)")
        self.wait(1)

        items = [
            Text("A_1 = A_2 = A_3 are trivial or abelian", font_size=BODY_SIZE, color=DIM, font=SANS),
            Text("A_4 is NOT simple (V_4 \u25c1 A_4)", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("A_5 IS simple \u2014 the smallest non-abelian case!", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title2, run_time=0.8)
        self.wait(6)

        # Klein four note
        k4 = MathTex(
            r"V_4 = \{e, (12)(34), (13)(24), (14)(23)\} \lhd A_4",
            color=DIM, font_size=28,
        )
        self.ly.safe_place(k4, anchor=items[-1], direction=DOWN, buff=0.35)
        self.play(Write(k4), run_time=NORMAL)
        self.wait(4)

        self.ly.clear()

    # --- Scene 6: Proof Strategy for A_n, n >= 5 ---
    # Narration ~40s.

    def scene6_proving_a5_simple(self):
        self.add_subcaption(
            "Here is the proof strategy for A_n, n >= 5. "
            "Step 1: Let N be a nontrivial normal subgroup of A_n. "
            "Pick any non-identity element sigma in N. "
            "Step 2: Show that N contains a 3-cycle. "
            "This is the hardest part. "
            "The key insight is that if sigma is not a 3-cycle, "
            "we can conjugate sigma by elements of A_n "
            "to produce two elements of N whose commutator is a 3-cycle. "
            "Step 3: Since N is normal and A_n is transitive on 3-cycles, "
            "conjugation sends our 3-cycle to any other 3-cycle. "
            "So N contains every 3-cycle. "
            "Step 4: The 3-cycles generate A_n, so N = A_n.",
            duration=40,
        )
        self.ly.section_divider("5", "Proof Strategy")

        title = self.ly.title("Four-Step Proof")
        self.wait(1)

        items = [
            Text("1. Let N \u25c1 A_n be nontrivial; pick \u03c3 \u2260 e in N", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Show N contains a 3-cycle", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Normality \u21d2 N contains ALL 3-cycles", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. 3-cycles generate A_n \u21d2 N = A_n", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(6)

        # Key insight box
        self.ly.clear()

        title2 = self.ly.title("The Key Insight (Step 2)")
        self.wait(1)

        insight = MathTex(
            r"\text{If } \sigma \text{ is not a 3-cycle, conjugate to get } [\sigma, \tau] = (abc)",
            color=WHITE, font_size=28,
        )
        boxed = self.ly.formula_box(insight, color=SECONDARY)
        self.ly.center_in_content(boxed)
        self.play(Write(insight), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        detail = Text(
            "Commutator of two elements of N is in N (N is normal)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(detail, anchor=boxed, direction=DOWN, buff=0.4)
        self.play(FadeIn(detail, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 7: A_5 Simplicity via Conjugacy Classes ---
    # Narration ~45s.

    def scene7_conjugacy_classes(self):
        self.add_subcaption(
            "For A_5, we can prove simplicity directly "
            "using conjugacy classes. "
            "The order of A_5 is 60. "
            "In S_5, the conjugacy classes of even permutations are: "
            "the identity of class size 1, "
            "products of two disjoint transpositions with class size 15, "
            "3-cycles with class size 20, "
            "5-cycles with class size 24, "
            "and the other 5-cycles with class size 24. "
            "But in A_5, the two 5-cycle classes merge "
            "into a single class of size 24. "
            "Now let N be a nontrivial normal subgroup of A_5. "
            "By Lagrange's theorem, the order of N divides 60. "
            "Since N is normal, it is a union of conjugacy classes "
            "including the identity. "
            "So the order of N must equal 1 plus a sum of "
            "selected class sizes. "
            "The only possibilities are 1, 60, or sums that don't work. "
            "Therefore N must be A_5, proving simplicity.",
            duration=45,
        )
        self.ly.section_divider("6", "A_5: Conjugacy Class Proof")

        title = self.ly.title("Conjugacy Classes of A_5")
        self.wait(1)

        # |A_5| = 60
        order = MathTex(
            r"|A_5| = \frac{5!}{2} = 60",
            color=WHITE, font_size=34,
        )
        boxed = self.ly.formula_box(order, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.35)
        self.play(Write(order), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        # Class sizes table
        self.ly.clear()

        title2 = self.ly.title("Class Sizes in A_5")
        self.wait(1)

        left_items = [
            Text("identity: size 1", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("(12)(34): size 15", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("(123): size 20", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        right_items = [
            Text("(12345): size 12", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("(13524): size 12", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        left_col, right_col = self.ly.two_columns(left_items, right_items, start_from=title2)
        self.play(FadeIn(left_col[0], shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(left_col[1], shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(left_col[2], shift=LEFT * 0.15), run_time=FAST)
        self.play(FadeIn(right_col[0], shift=RIGHT * 0.15), run_time=FAST)
        self.play(FadeIn(right_col[1], shift=RIGHT * 0.15), run_time=FAST)
        self.wait(4)

        # Total line — FadeOut columns first (content budget: title2 + 5 items was 6)
        self.play(
            *[FadeOut(left_col[i]) for i in range(len(left_col))],
            *[FadeOut(right_col[i]) for i in range(len(right_col))],
            run_time=FAST,
        )
        total = Text("Total: 1 + 15 + 20 + 12 + 12 = 60", font_size=BODY_SIZE, color=WHITE, font=SANS)
        self.ly.safe_place(total, anchor=title2, direction=DOWN, buff=0.6)
        self.play(FadeIn(total, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # The argument
        title3 = self.ly.title("The Lagrange Argument")
        self.wait(1)

        items = [
            Text("N \u25c1 A_5 \u21d2 N is a union of conjugacy classes", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            MathTex(r"|N| = 1 + 15 + 20 + 12 + 12 = 60", color=WHITE, font_size=30),
            MathTex(r"|N| = 1 \implies N = \{e\} \text{ (trivial)}", color=DIM, font_size=30),
        ]
        self.ly.progressive_reveal(items, start_from=title3, run_time=0.8)
        self.wait(5)

        conclusion = Text(
            "Only possibilities: |N| = 1 or 60 \u21d2 A_5 is simple!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(conclusion, anchor=items[-1], direction=DOWN, buff=0.35)
        self.play(FadeIn(conclusion, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # --- Scene 8: Summary ---
    # Narration ~30s.

    def scene8_summary(self):
        self.add_subcaption(
            "Let us summarize what we learned today. "
            "A simple group has no nontrivial proper normal subgroups, "
            "making it the atomic unit of group theory. "
            "The Jordan-Holder theorem tells us that every finite group "
            "can be decomposed into simple composition factors. "
            "The classification theorem says there are exactly four families: "
            "cyclic groups of prime order, alternating groups A_n for n >= 5, "
            "groups of Lie type, and the 26 sporadic groups. "
            "We proved that A_5 is simple by analyzing its conjugacy classes, "
            "and sketched the general proof for A_n when n >= 5. "
            "In the next video, we begin our study of rings. "
            "Thanks for watching.",
            duration=30,
        )

        title = self.ly.title("Summary")
        self.wait(1)

        items = [
            Text("Simple group = no nontrivial proper normal subgroups", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Jordan-Holder: composition factors are unique", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Classification: cyclic, alternating, Lie type, sporadic", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("A_n is simple for n \u2265 5 (proved via 3-cycles)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(6)

        # Tease next video
        self.ly.clear()

        tease_title = self.ly.title("Coming Up Next")
        self.wait(1)

        tease = Text(
            "Video 12: Introduction to Rings",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.center_in_content(tease)
        self.play(FadeIn(tease, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)

        self.ly.clear()
        play_outro(self)
