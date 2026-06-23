"""Video 83: Equivalence Relations
Discrete Mathematics -- Video 5 of 12

Covers: Equivalence relations (reflexive + symmetric + transitive),
equivalence classes [a], partitions, modular arithmetic as canonical example,
theorem: equivalence relations <-> partitions.

Plan: planning/video-83-equivalence-relations.md

Render draft:  manim -ql scripts/undergraduate/video-83-equivalence-relations.py Video83_EquivalenceRelations
Render final:  manim -qh scripts/undergraduate/video-83-equivalence-relations.py Video83_EquivalenceRelations
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


class Video83_EquivalenceRelations(Scene):
    """Equivalence Relations -- reflexive + symmetric + transitive combined,
    equivalence classes, partitions, modular arithmetic."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_examples()
        self.scene4_equivalence_classes()
        self.scene5_modular_arithmetic()
        self.scene6_partitions()
        self.scene7_deep_connection()
        self.scene8_proof_sketch()
        self.scene9_practice()
        self.scene10_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook -- The Power of "Same As" (1:30)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Last video, we learned that relations can be reflexive, "
            "symmetric, or transitive. But what happens when a relation "
            "has ALL THREE properties at once? Think about real life. "
            "\"Same birthday\", \"same blood type\", \"same nationality\". "
            "These are all relations that group things into categories. "
            "A relation with all three properties is called an "
            "equivalence relation, and it naturally splits the world "
            "into groups of equivalent items.",
            duration=30,
        )
        play_intro(self, "Equivalence Relations", "Discrete Mathematics")

        title = self.ly.title("The Power of \"Same As\"")

        # Bridge from last video
        bridge = Text(
            "Last video: reflexive, symmetric, transitive -- separately.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(bridge, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.2)

        # Real-world example 1
        ex1 = Text(
            "\"same birthday\"  --  groups people by birth date",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(ex1, direction=DOWN, anchor=bridge, buff=0.4)
        self.play(FadeIn(ex1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.5)

        # Real-world example 2
        ex2 = Text(
            "\"same blood type\"  --  groups people by medical type",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(ex2, direction=DOWN, anchor=ex1, buff=0.4)
        self.play(FadeIn(ex2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.5)

        # Real-world example 3
        ex3 = Text(
            "\"same nationality\"  --  groups people by country",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(ex3, direction=DOWN, anchor=ex2, buff=0.4)
        self.play(FadeIn(ex3, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.5)

        # Key insight
        insight = Text(
            "These relations share a deep structure: they split the "
            "world into groups of equivalent items.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=ex3, buff=0.5)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(8)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Definition -- Equivalence Relation (1:00)
    # ------------------------------------------------------------------
    def scene2_definition(self):
        self.add_subcaption(
            "A relation R on a set A is an equivalence relation if it "
            "is reflexive, symmetric, AND transitive, all at the same "
            "time. Reflexive means every element relates to itself. "
            "Symmetric means if a is related to b, then b is related to a. "
            "Transitive means chains complete. When all three hold, the "
            "relation earns the title equivalence relation. This is the "
            "\"triple crown\" of relation properties.",
            duration=28,
        )
        self.ly.section_divider(2, "Definition")

        title = self.ly.title("The Equivalence Relation")

        # Definition
        definition = MathTex(
            r"R \text{ is an equivalence relation on } A \text{ if } R \text{ is }",
            r"\text{reflexive, symmetric, AND transitive}",
            font_size=BODY_SIZE,
        )
        definition[0].set_color(WHITE)
        definition[1].set_color(ACCENT)
        self.ly.safe_place(definition, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(definition), run_time=NORMAL)
        self.wait(1.2)

        # Triple crown visual -- three properties listed
        reflexive = Text(
            "Reflexive:  (a, a) in R for all a",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(reflexive, direction=DOWN, anchor=definition, buff=0.5)
        self.play(FadeIn(reflexive, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.8)

        symmetric = Text(
            "Symmetric:  (a, b) implies (b, a)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(symmetric, direction=DOWN, anchor=reflexive, buff=0.3)
        self.play(FadeIn(symmetric, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.8)

        transitive = Text(
            "Transitive:  (a, b) + (b, c) implies (a, c)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(transitive, direction=DOWN, anchor=symmetric, buff=0.3)
        self.play(FadeIn(transitive, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Examples -- Which Relations Are Equivalence Relations? (1:30)
    # ------------------------------------------------------------------
    def scene3_examples(self):
        self.add_subcaption(
            "Let's check which relations are equivalence relations. "
            "Example one: the equals relation on real numbers. Is it "
            "reflexive? Yes, a equals a. Symmetric? Yes, if a equals b "
            "then b equals a. Transitive? Yes, if a equals b and b equals "
            "c, then a equals c. All three pass! Equals is an equivalence "
            "relation. It's the simplest one.",
            duration=27,
        )
        self.ly.section_divider(3, "Examples")

        title = self.ly.title("Which Relations Qualify?")

        # Example 1: = on reals
        ex1_label = Text(
            "Example 1:  = (equals) on real numbers",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(ex1_label, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(ex1_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        # Check properties
        checks1 = MathTex(
            r"\checkmark \text{ reflexive: } a = a",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(checks1, direction=DOWN, anchor=ex1_label, buff=0.3)
        self.play(Write(checks1), run_time=FAST)
        self.wait(0.8)

        checks2 = MathTex(
            r"\checkmark \text{ symmetric: } a = b \implies b = a",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(checks2, direction=DOWN, anchor=checks1, buff=0.3)
        self.play(Write(checks2), run_time=FAST)
        self.wait(0.8)

        checks3 = MathTex(
            r"\checkmark \text{ transitive: } a = b, b = c \implies a = c",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(checks3, direction=DOWN, anchor=checks2, buff=0.3)
        self.play(Write(checks3), run_time=FAST)
        self.wait(1.2)

        # Verdict
        verdict1 = Text(
            "YES -- equals is an equivalence relation!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(verdict1, direction=DOWN, anchor=checks3, buff=0.4)
        self.play(FadeIn(verdict1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(3.8)

        self.ly.clear()

        # Example 2: <= on reals (not an equivalence relation)
        self.add_subcaption(
            "Example two: less than or equal to on real numbers. "
            "Reflexive? Yes, a is less than or equal to itself. "
            "Transitive? Yes, chains of inequalities work. "
            "But symmetric? No! One is less than or equal to two, "
            "but two is NOT less than or equal to one. "
            "It fails the symmetric test, so it is not an "
            "equivalence relation.",
            duration=26,
        )
        title2 = self.ly.title("Counterexample: Not Equivalence")

        ex2_label = Text(
            "Example 2:  <= (less than or equal) on real numbers",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(ex2_label, direction=DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(ex2_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        ref_check = MathTex(
            r"\checkmark \text{ reflexive: } a \leq a",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ref_check, direction=DOWN, anchor=ex2_label, buff=0.3)
        self.play(Write(ref_check), run_time=FAST)
        self.wait(0.8)

        sym_fail = MathTex(
            r"\times \text{ NOT symmetric: } 1 \leq 2 \text{ but } 2 \not\leq 1",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(sym_fail, direction=DOWN, anchor=ref_check, buff=0.3)
        self.play(Write(sym_fail), run_time=FAST)
        self.wait(1.2)

        verdict2 = Text(
            "NO -- fails symmetry. Not an equivalence relation.",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(verdict2, direction=DOWN, anchor=sym_fail, buff=0.4)
        self.play(FadeIn(verdict2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(3.8)

        self.ly.clear()

        # Example 3: same parity
        self.add_subcaption(
            "Example three: has the same parity as on integers. "
            "Reflexive? Yes, every integer has the same parity as itself. "
            "Symmetric? Yes, if n and m have the same parity, so do m "
            "and n. Transitive? Yes, if n matches m and m matches k, "
            "then n matches k. All three pass! Same parity is an "
            "equivalence relation.",
            duration=26,
        )
        title3 = self.ly.title("Another Example: Parity")

        ex3_label = Text(
            "Example 3:  \"same parity\" on integers",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(ex3_label, direction=DOWN, anchor=title3, buff=0.5)
        self.play(FadeIn(ex3_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        parity_props = MathTex(
            r"\checkmark \text{ reflexive} \quad "
            r"\checkmark \text{ symmetric} \quad "
            r"\checkmark \text{ transitive}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(parity_props, direction=DOWN, anchor=ex3_label, buff=0.4)
        self.play(Write(parity_props), run_time=NORMAL)
        self.wait(1.2)

        parity_explain = Text(
            "Same parity groups integers into evens and odds",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(parity_explain, direction=DOWN, anchor=parity_props, buff=0.4)
        self.play(FadeIn(parity_explain, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3.8)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Equivalence Classes (1:30)
    # ------------------------------------------------------------------
    def scene4_equivalence_classes(self):
        self.add_subcaption(
            "When we have an equivalence relation, every element belongs "
            "to a group called its equivalence class. The equivalence "
            "class of a, written in square brackets, a, is the set of "
            "all elements that are related to a. Let's see this with "
            "the same parity relation on the set 1 through 5. "
            "The equivalence class of 1 is 1, 3, and 5. "
            "The equivalence class of 2 is 2 and 4. "
            "A key fact: two equivalence classes are equal if and only "
            "if their representatives are related.",
            duration=35,
        )
        self.ly.section_divider(4, "Equivalence Classes")

        title = self.ly.title("Grouping Related Elements")

        # Definition
        definition = MathTex(
            r"[a] = \{b \in A : b \sim a\}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(definition, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(definition), run_time=NORMAL)
        self.wait(1.2)

        desc = Text(
            "The equivalence class of a: all elements related to a",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(desc, direction=DOWN, anchor=definition, buff=0.4)
        self.play(FadeIn(desc, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.2)

        # Concrete example
        example_set = Text(
            "Example: \"same parity\" on {1, 2, 3, 4, 5}",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(example_set, direction=DOWN, anchor=desc, buff=0.4)
        self.play(FadeIn(example_set, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        # Class of 1 (odd numbers)
        class1 = MathTex(
            r"[1] = \{1, 3, 5\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(class1, direction=DOWN, anchor=example_set, buff=0.4)
        self.play(Write(class1), run_time=FAST)
        self.wait(0.8)

        # Class of 2 (even numbers)
        class2 = MathTex(
            r"[2] = \{2, 4\}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(class2, direction=DOWN, anchor=class1, buff=0.3)
        self.play(Write(class2), run_time=FAST)
        self.wait(1.2)

        # Key insight
        insight = MathTex(
            r"[a] = [b] \iff a \sim b",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=class2, buff=0.4)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Equivalence Classes -- Modular Arithmetic (1:30)
    # ------------------------------------------------------------------
    def scene5_modular_arithmetic(self):
        self.add_subcaption(
            "The canonical example of equivalence relations is modular "
            "arithmetic. We say a is congruent to b modulo n if n "
            "divides a minus b. This is an equivalence relation on the "
            "integers. Let's check: reflexive, since n divides zero. "
            "Symmetric, since if n divides a minus b, then n divides "
            "b minus a. Transitive, by a standard divisibility argument. "
            "For mod 3, the equivalence classes are: class zero is all "
            "multiples of three, class one is numbers that leave "
            "remainder one, and class two is numbers that leave "
            "remainder two.",
            duration=36,
        )
        self.ly.section_divider(5, "Modular Arithmetic")

        title = self.ly.title("The Canonical Example: Mod n")

        # Definition of congruence
        congruence_def = MathTex(
            r"a \equiv b \pmod{n} \iff n \mid (a - b)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(congruence_def, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(congruence_def), run_time=NORMAL)
        self.wait(1.2)

        # Quick property check
        prop_check = Text(
            "Check: reflexive (n|0), symmetric (n|(a-b) -> n|(b-a)), transitive",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(prop_check, direction=DOWN, anchor=congruence_def, buff=0.4)
        self.play(FadeIn(prop_check, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.2)

        # Mod 3 example
        mod3_title = Text(
            "Mod 3 equivalence classes on Z:",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(mod3_title, direction=DOWN, anchor=prop_check, buff=0.5)
        self.play(FadeIn(mod3_title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        # Three classes
        class0 = MathTex(
            r"[0] = \{\ldots, -6, -3, 0, 3, 6, 9, \ldots\}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(class0, direction=DOWN, anchor=mod3_title, buff=0.3)
        self.play(Write(class0), run_time=FAST)
        self.wait(0.8)

        class1 = MathTex(
            r"[1] = \{\ldots, -5, -2, 1, 4, 7, 10, \ldots\}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(class1, direction=DOWN, anchor=class0, buff=0.3)
        self.play(Write(class1), run_time=FAST)
        self.wait(0.8)

        class2 = MathTex(
            r"[2] = \{\ldots, -4, -1, 2, 5, 8, 11, \ldots\}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(class2, direction=DOWN, anchor=class1, buff=0.3)
        self.play(Write(class2), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Partitions (1:00)
    # ------------------------------------------------------------------
    def scene6_partitions(self):
        self.add_subcaption(
            "A partition of a set A is a collection of non-empty, "
            "pairwise disjoint subsets whose union is A. Three "
            "requirements: every block must be non-empty, blocks must "
            "not overlap, and every element of A must belong to some "
            "block. Think of it as splitting a set into non-overlapping "
            "groups that together cover everything.",
            duration=26,
        )
        self.ly.section_divider(6, "Partitions")

        title = self.ly.title("Splitting a Set Into Blocks")

        # Definition
        definition = Text(
            "A partition of A: non-empty, disjoint subsets",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(definition, direction=DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(definition, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        # Three requirements
        req1 = Text(
            "1. Every block is non-empty",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(req1, direction=DOWN, anchor=definition, buff=0.4)
        self.play(FadeIn(req1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.8)

        req2 = Text(
            "2. Blocks are pairwise disjoint (no overlap)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(req2, direction=DOWN, anchor=req1, buff=0.3)
        self.play(FadeIn(req2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.8)

        req3 = Text(
            "3. Union of all blocks equals A (nothing left out)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(req3, direction=DOWN, anchor=req2, buff=0.3)
        self.play(FadeIn(req3, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.2)

        # Formal notation
        formal = MathTex(
            r"A = B_1 \sqcup B_2 \sqcup \cdots \sqcup B_k",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(formal, direction=DOWN, anchor=req3, buff=0.5)
        self.play(Write(formal), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: The Deep Connection -- Equivalence Relations = Partitions (1:30)
    # ------------------------------------------------------------------
    def scene7_deep_connection(self):
        self.add_subcaption(
            "Here is the deep connection that makes equivalence "
            "relations so powerful. Theorem one: every equivalence "
            "relation on A defines a partition of A. The equivalence "
            "classes themselves form the blocks. Theorem two: every "
            "partition of A defines an equivalence relation. Just "
            "declare two elements related if they are in the same "
            "block. These two facts together mean equivalence "
            "relations and partitions are two sides of the same coin. "
            "Every equivalence relation gives a partition, and every "
            "partition gives an equivalence relation.",
            duration=36,
        )
        self.ly.section_divider(7, "The Deep Connection")

        title = self.ly.title("Two Sides of the Same Coin")

        # Theorem 1
        thm1_title = Text(
            "Theorem 1:",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        thm1_body = Text(
            "Every equivalence relation defines a partition",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        thm1_group = VGroup(thm1_title, thm1_body).arrange(RIGHT, buff=0.3)
        self.ly.safe_place(thm1_group, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(thm1_group, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.2)

        # Theorem 2
        thm2_title = Text(
            "Theorem 2:",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        thm2_body = Text(
            "Every partition defines an equivalence relation",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        thm2_group = VGroup(thm2_title, thm2_body).arrange(RIGHT, buff=0.3)
        self.ly.safe_place(thm2_group, direction=DOWN, anchor=thm1_group, buff=0.5)
        self.play(FadeIn(thm2_group, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.2)

        # Bridge visual
        bridge = MathTex(
            r"\text{equivalence relation} \longleftrightarrow \text{partition}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(bridge, direction=DOWN, anchor=thm2_group, buff=0.6)
        self.play(Write(bridge), run_time=SLOW)
        self.wait(1.2)

        # Elaboration
        elab = Text(
            "a ~ b  iff  a and b belong to the same block",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(elab, direction=DOWN, anchor=bridge, buff=0.4)
        self.play(FadeIn(elab, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Proof Sketch -- Classes Form a Partition (1:00)
    # ------------------------------------------------------------------
    def scene8_proof_sketch(self):
        self.add_subcaption(
            "Let's sketch the proof that equivalence classes form a "
            "partition. We need three things. First, classes are "
            "non-empty. Since the relation is reflexive, a tilde a, so "
            "a is in its own class. Second, classes are either "
            "disjoint or identical. If some element c is in both "
            "bracket a and bracket b, then c tilde a and c tilde b. "
            "By symmetry, a tilde c. By transitivity, a tilde b. "
            "This forces bracket a to equal bracket b. Third, the "
            "union covers A. Every element a is in bracket a, so "
            "nothing is left out. All three requirements are satisfied.",
            duration=40,
        )
        self.ly.section_divider(8, "Proof Sketch")

        title = self.ly.title("Why Classes Form a Partition")

        # Part 1
        part1 = Text(
            "1. Non-empty:  a ~ a (reflexive), so a in [a]",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(part1, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(part1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.2)

        # Part 2
        part2 = Text(
            "2. Disjoint or identical:",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(part2, direction=DOWN, anchor=part1, buff=0.4)
        self.play(FadeIn(part2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        part2_detail = MathTex(
            r"[a] \cap [b] \neq \emptyset \implies [a] = [b]",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(part2_detail, direction=DOWN, anchor=part2, buff=0.3)
        self.play(Write(part2_detail), run_time=NORMAL)
        self.wait(0.8)

        part2_proof = Text(
            "If c in both, then c~a, c~b. By sym: a~c. By trans: a~b.",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(part2_proof, direction=DOWN, anchor=part2_detail, buff=0.2)
        self.play(FadeIn(part2_proof, shift=LEFT * 0.15), run_time=FAST)
        self.wait(1.2)

        # Part 3
        part3 = Text(
            "3. Union covers A:  every a in A is in [a]",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(part3, direction=DOWN, anchor=part2_proof, buff=0.4)
        self.play(FadeIn(part3, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2.5)

        # QED
        qed = MathTex(
            r"\square \text{  All three partition requirements hold.}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(qed, direction=DOWN, anchor=part3, buff=0.4)
        self.play(Write(qed), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Practice -- Another Partition Example (0:30)
    # ------------------------------------------------------------------
    def scene9_practice(self):
        self.add_subcaption(
            "Let's try another example. Consider a class of students, "
            "where the relation is having the same major. Is this an "
            "equivalence relation? Reflexive: yes, every student has "
            "the same major as themselves. Symmetric: yes, if you have "
            "the same major as me, then I have the same major as you. "
            "Transitive: yes, chains of same-major pairs work. The "
            "equivalence classes are the groups of students in each "
            "major, like all CS students, all math students, and so on. "
            "This naturally partitions the class.",
            duration=32,
        )
        self.ly.section_divider(9, "Practice")

        title = self.ly.title("Real-World Partition")

        # Setup
        setup = Text(
            "A = {students in a class},  ~ = \"same major\"",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(setup, direction=DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(setup, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.8)

        # Quick check
        quick = MathTex(
            r"\checkmark \text{ reflexive} \quad "
            r"\checkmark \text{ symmetric} \quad "
            r"\checkmark \text{ transitive}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(quick, direction=DOWN, anchor=setup, buff=0.4)
        self.play(Write(quick), run_time=NORMAL)
        self.wait(1.2)

        # Result
        result = Text(
            "Equivalence classes: {CS students}, {Math students}, ...",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=quick, buff=0.4)
        self.play(FadeIn(result, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.2)

        takeaway = Text(
            "\"Same major\" partitions the class by department!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(takeaway, direction=DOWN, anchor=result, buff=0.4)
        self.play(FadeIn(takeaway, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Summary + Outro (0:30)
    # ------------------------------------------------------------------
    def scene10_summary(self):
        self.add_subcaption(
            "Let's recap equivalence relations. An equivalence "
            "relation is reflexive, symmetric, and transitive all at "
            "once. The equivalence class of an element a is the set of "
            "all elements related to a. Every equivalence relation "
            "partitions its set into equivalence classes, and every "
            "partition defines an equivalence relation. Modular "
            "arithmetic is the canonical example. Next up: Counting "
            "Principles, where we'll learn to count the sizes of these "
            "partitions and much more.",
            duration=32,
        )
        title = self.ly.title("Summary")

        items = [
            Text("Equivalence relation = reflexive + symmetric + transitive", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("[a] = all elements related to a", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Equivalence classes partition the set", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Every partition defines an equivalence relation", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Canonical example: congruence mod n", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2.5)

        play_outro(self, "Counting Principles", "Discrete Mathematics")
        self.ly.clear()
