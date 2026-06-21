"""Video 80: Predicate Logic
Discrete Mathematics -- Video 2 of 12

Covers: Limitations of propositional logic, predicates, domains of discourse,
universal quantifier (forall), existential quantifier (exists), free vs bound
variables, negating quantified statements (De Morgan's for quantifiers),
nested quantifiers.

Plan: planning/video-80-predicate-logic.md

Render draft:  manim -ql scripts/undergraduate/video-80-predicate-logic.py Video80_PredicateLogic
Render final:  manim -qh scripts/undergraduate/video-80-predicate-logic.py Video80_PredicateLogic
"""

from manim import *
import sys, os
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video80_PredicateLogic(Scene):
    """Predicate Logic -- predicates, domains, quantifiers, negation,
    free/bound variables, nested quantifiers."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_predicates()
        self.scene3_domain()
        self.scene4_universal()
        self.scene5_existential()
        self.scene6_free_bound()
        self.scene7_negation()
        self.scene8_nested()
        self.scene9_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook — The Limitation of Propositional Logic (1:00)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "In propositional logic, every statement is either true or false. "
            "But what about x is greater than 3? This depends on x. "
            "And how do we express for all or there exists? "
            "Propositional logic can't handle variables or quantities. "
            "We need a richer language: predicate logic.",
            duration=14,
        )
        play_intro(self, "Predicate Logic", "Discrete Mathematics")

        title = self.ly.title("The Limitation")

        # Statement that IS a proposition
        prop_ok = Text(
            "2 + 3 = 5  ->  True or False?  Yes!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(prop_ok, direction=DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(prop_ok, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Statement that is NOT a proposition
        prop_bad = Text(
            "x > 3  ->  True or False?  It depends on x!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(prop_bad, direction=DOWN, anchor=prop_ok, buff=0.4)
        self.play(FadeIn(prop_bad, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # "For all" example
        forall_ex = Text(
            '"Every student passed."  How do we write "every"?',
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(forall_ex, direction=DOWN, anchor=prop_bad, buff=0.4)
        self.play(FadeIn(forall_ex, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Teaser
        teaser = Text(
            "We need: variables, domains, and quantifiers.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(teaser, direction=DOWN, anchor=forall_ex, buff=0.5)
        self.play(FadeIn(teaser, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Predicates (1:00)
    # ------------------------------------------------------------------
    def scene2_predicates(self):
        self.add_subcaption(
            "A predicate is a statement containing variables that becomes "
            "true or false once we substitute specific values. "
            "We write predicates as capital letters followed by variables "
            "in parentheses, like P of x. "
            "For example, P of x is x is even. When x equals 4, this is "
            "true. When x equals 7, it is false.",
            duration=15,
        )
        self.ly.section_divider(2, "Predicates")

        title = self.ly.title("What is a Predicate?")

        definition = Text(
            "A predicate becomes true or false when you substitute values.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(definition, direction=DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(definition, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Predicate notation
        pred_notation = MathTex(
            r"P(x): x \text{ is even}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(pred_notation, direction=DOWN, anchor=definition, buff=0.5)
        self.play(Write(pred_notation), run_time=NORMAL)
        self.wait(0.5)

        # Show substitution
        sub_true = Text(
            "P(4) = True   (4 is even)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(sub_true, direction=DOWN, anchor=pred_notation, buff=0.5)
        self.play(FadeIn(sub_true, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        sub_false = Text(
            "P(7) = False   (7 is not even)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(sub_false, direction=DOWN, anchor=sub_true, buff=0.4)
        self.play(FadeIn(sub_false, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: The Domain of Discourse (1:00)
    # ------------------------------------------------------------------
    def scene3_domain(self):
        self.add_subcaption(
            "The domain of discourse tells us what values our variable can "
            "take. The same predicate can be true over one domain and false "
            "over another. "
            "For example, x is greater than zero is true for all natural "
            "numbers, but false over the integers because negative numbers "
            "exist. The domain matters!",
            duration=14,
        )
        self.ly.section_divider(3, "Domain of Discourse")

        title = self.ly.title("The Domain Matters")

        # Domain definition
        dom_def = Text(
            "The domain specifies what values x can take.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(dom_def, direction=DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(dom_def, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Predicate
        pred = MathTex(
            r"P(x): x > 0",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(pred, direction=DOWN, anchor=dom_def, buff=0.5)
        self.play(Write(pred), run_time=NORMAL)
        self.wait(0.5)

        # Two columns: natural numbers vs integers
        nat_title = Text(
            "Natural numbers {0, 1, 2, ...}",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        nat_result = Text(
            "All elements satisfy P(x)  ->  TRUE",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        left_col = VGroup(nat_title, nat_result).arrange(DOWN, buff=0.2)

        int_title = Text(
            "Integers {..., -1, 0, 1, ...}",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        int_result = Text(
            "-1 doesn't satisfy P(x)  ->  FALSE",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        right_col = VGroup(int_title, int_result).arrange(DOWN, buff=0.2)

        self.ly.two_columns(left_col, right_col, start_from=pred)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Universal Quantifier (1:30)
    # ------------------------------------------------------------------
    def scene4_universal(self):
        self.add_subcaption(
            "The universal quantifier, written as the upside-down A, means "
            "for all. It says that a predicate is true for every element in "
            "the domain. For all x, P of x is true only if P holds for "
            "absolutely every value of x. If even one element fails, the "
            "whole statement is false.",
            duration=15,
        )
        self.ly.section_divider(4, "Universal Quantifier")

        title = self.ly.title("For All  (Universal)")

        # Symbol and definition
        forall_sym = MathTex(
            r"\forall x \, P(x)",
            font_size=TITLE_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(forall_sym, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(forall_sym), run_time=SLOW)
        self.wait(0.5)

        meaning = Text(
            '"For every x in the domain, P(x) is true."',
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(meaning, direction=DOWN, anchor=forall_sym, buff=0.5)
        self.play(FadeIn(meaning, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        self.ly.clear()

        # Example 1: TRUE
        title_ex1 = self.ly.title("Example: TRUE")

        ex1_pred = MathTex(
            r"\forall x \, (x \geq 0)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        ex1_dom = Text(
            "Domain: Natural numbers {0, 1, 2, ...}",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(ex1_pred, direction=DOWN, anchor=title_ex1, buff=0.5)
        self.play(Write(ex1_pred), run_time=NORMAL)
        self.ly.safe_place(ex1_dom, direction=DOWN, anchor=ex1_pred, buff=0.4)
        self.play(FadeIn(ex1_dom, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Visual: dots all green
        dots_label = Text(
            "Every element is >= 0  ->  All green checkmarks",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(dots_label, direction=DOWN, anchor=ex1_dom, buff=0.4)
        self.play(FadeIn(dots_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        result1 = Text(
            "TRUE",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(result1, direction=DOWN, anchor=dots_label, buff=0.4)
        self.play(FadeIn(result1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # Example 2: FALSE
        title_ex2 = self.ly.title("Example: FALSE")

        ex2_pred = MathTex(
            r"\forall x \, (x \geq 0)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        ex2_dom = Text(
            "Domain: Integers {..., -2, -1, 0, 1, ...}",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(ex2_pred, direction=DOWN, anchor=title_ex2, buff=0.5)
        self.play(Write(ex2_pred), run_time=NORMAL)
        self.ly.safe_place(ex2_dom, direction=DOWN, anchor=ex2_pred, buff=0.4)
        self.play(FadeIn(ex2_dom, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        counter = Text(
            "Counterexample: x = -1  (fails x >= 0)",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(counter, direction=DOWN, anchor=ex2_dom, buff=0.4)
        self.play(FadeIn(counter, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        result2 = Text(
            "FALSE  (one counterexample is enough)",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(result2, direction=DOWN, anchor=counter, buff=0.4)
        self.play(FadeIn(result2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Existential Quantifier (1:30)
    # ------------------------------------------------------------------
    def scene5_existential(self):
        self.add_subcaption(
            "The existential quantifier, written as a backwards E, means "
            "there exists. It says that at least one element in the domain "
            "makes the predicate true. There exists x such that P of x is "
            "true if we can find even a single value of x that works. "
            "If no element satisfies P, the statement is false.",
            duration=15,
        )
        self.ly.section_divider(5, "Existential Quantifier")

        title = self.ly.title("There Exists  (Existential)")

        # Symbol and definition
        exists_sym = MathTex(
            r"\exists x \, P(x)",
            font_size=TITLE_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(exists_sym, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(exists_sym), run_time=SLOW)
        self.wait(0.5)

        meaning = Text(
            '"There exists some x such that P(x) is true."',
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(meaning, direction=DOWN, anchor=exists_sym, buff=0.5)
        self.play(FadeIn(meaning, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        self.ly.clear()

        # Example 1: TRUE
        title_ex1 = self.ly.title("Example: TRUE")

        ex1_pred = MathTex(
            r"\exists x \, (x > 10)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        ex1_dom = Text(
            "Domain: Natural numbers {0, 1, 2, ...}",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(ex1_pred, direction=DOWN, anchor=title_ex1, buff=0.5)
        self.play(Write(ex1_pred), run_time=NORMAL)
        self.ly.safe_place(ex1_dom, direction=DOWN, anchor=ex1_pred, buff=0.4)
        self.play(FadeIn(ex1_dom, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        witness = Text(
            "Witness: x = 11  (11 > 10, works!)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(witness, direction=DOWN, anchor=ex1_dom, buff=0.4)
        self.play(FadeIn(witness, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        result1 = Text(
            "TRUE  (just need one witness)",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(result1, direction=DOWN, anchor=witness, buff=0.4)
        self.play(FadeIn(result1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # Example 2: FALSE
        title_ex2 = self.ly.title("Example: FALSE")

        ex2_pred = MathTex(
            r"\exists x \, (x < 0)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        ex2_dom = Text(
            "Domain: Natural numbers {0, 1, 2, ...}",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(ex2_pred, direction=DOWN, anchor=title_ex2, buff=0.5)
        self.play(Write(ex2_pred), run_time=NORMAL)
        self.ly.safe_place(ex2_dom, direction=DOWN, anchor=ex2_pred, buff=0.4)
        self.play(FadeIn(ex2_dom, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        no_witness = Text(
            "No natural number is negative. Nothing works.",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(no_witness, direction=DOWN, anchor=ex2_dom, buff=0.4)
        self.play(FadeIn(no_witness, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        result2 = Text(
            "FALSE",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(result2, direction=DOWN, anchor=no_witness, buff=0.4)
        self.play(FadeIn(result2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Free vs Bound Variables (1:00)
    # ------------------------------------------------------------------
    def scene6_free_bound(self):
        self.add_subcaption(
            "Variables in a predicate can be free or bound. A bound variable "
            "is captured by a quantifier, like x in for all x P of x. "
            "A free variable has no quantifier and needs a value to be "
            "assigned. A statement with free variables is not a proposition, "
            "but a fully quantified statement is.",
            duration=14,
        )
        self.ly.section_divider(6, "Free vs Bound Variables")

        title = self.ly.title("Free vs Bound")

        # Bound example
        bound_label = Text(
            "BOUND: captured by a quantifier",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        bound_ex = MathTex(
            r"\forall x \, P(x)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(bound_label, direction=DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(bound_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(bound_ex, direction=DOWN, anchor=bound_label, buff=0.5)
        self.play(Write(bound_ex), run_time=NORMAL)
        self.wait(0.5)

        bound_result = Text(
            "x is bound  ->  This IS a proposition (T or F)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(bound_result, direction=DOWN, anchor=bound_ex, buff=0.4)
        self.play(FadeIn(bound_result, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        self.ly.clear()

        # Free example
        title_free = self.ly.title("Free Variables")

        free_label = Text(
            "FREE: no quantifier, needs a value",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        free_ex = MathTex(
            r"P(x) \land Q(y)",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(free_label, direction=DOWN, anchor=title_free, buff=0.6)
        self.play(FadeIn(free_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.ly.safe_place(free_ex, direction=DOWN, anchor=free_label, buff=0.5)
        self.play(Write(free_ex), run_time=NORMAL)
        self.wait(0.5)

        free_result = Text(
            "x and y are free  ->  NOT a proposition yet!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(free_result, direction=DOWN, anchor=free_ex, buff=0.4)
        self.play(FadeIn(free_result, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Mixed example
        mixed = MathTex(
            r"\forall x \, \big(P(x) \land Q(y)\big)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        mixed_label = Text(
            "x is bound, y is free  ->  Still not a proposition!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(mixed, direction=DOWN, anchor=free_result, buff=0.5)
        self.play(Write(mixed), run_time=NORMAL)
        self.ly.safe_place(mixed_label, direction=DOWN, anchor=mixed, buff=0.4)
        self.play(FadeIn(mixed_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Negating Quantified Statements (1:30)
    # ------------------------------------------------------------------
    def scene7_negation(self):
        self.add_subcaption(
            "Negating quantified statements follows a beautiful pattern. "
            "The negation of for all is there exists. "
            "Not for all x P of x means there exists some x where P of x "
            "is false. Similarly, the negation of there exists is for all. "
            "These are De Morgan's laws for quantifiers! "
            "In plain English: not everyone passed means someone failed.",
            duration=16,
        )
        self.ly.section_divider(7, "Negating Quantifiers")

        title = self.ly.title("De Morgan's Laws for Quantifiers")

        # Law 1
        law1 = MathTex(
            r"\neg \forall x \, P(x)",
            font_size=HEADING_SIZE, color=RED,
        )
        equiv1 = MathTex(
            r"\equiv \; \exists x \, \neg P(x)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(law1, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(law1), run_time=NORMAL)
        self.ly.safe_place(equiv1, direction=DOWN, anchor=law1, buff=0.3)
        self.play(Write(equiv1), run_time=NORMAL)
        self.wait(0.5)

        words1 = Text(
            '"Not for all" = "There exists some that does not"',
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(words1, direction=DOWN, anchor=equiv1, buff=0.4)
        self.play(FadeIn(words1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # Law 2
        title2 = self.ly.title("The Other Direction")

        law2 = MathTex(
            r"\neg \exists x \, P(x)",
            font_size=HEADING_SIZE, color=RED,
        )
        equiv2 = MathTex(
            r"\equiv \; \forall x \, \neg P(x)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(law2, direction=DOWN, anchor=title2, buff=0.6)
        self.play(Write(law2), run_time=NORMAL)
        self.ly.safe_place(equiv2, direction=DOWN, anchor=law2, buff=0.3)
        self.play(Write(equiv2), run_time=NORMAL)
        self.wait(0.5)

        words2 = Text(
            '"There does not exist" = "For all, not"',
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(words2, direction=DOWN, anchor=equiv2, buff=0.4)
        self.play(FadeIn(words2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # Real-world example
        title_rw = self.ly.title("Real-World Example")

        rw_neg = Text(
            '"Not everyone passed the exam."',
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(rw_neg, direction=DOWN, anchor=title_rw, buff=0.6)
        self.play(FadeIn(rw_neg, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        arrow = Text(
            "  means  ",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(arrow, direction=DOWN, anchor=rw_neg, buff=0.3)
        self.play(FadeIn(arrow, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        rw_pos = Text(
            '"Someone failed the exam."',
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(rw_pos, direction=DOWN, anchor=arrow, buff=0.3)
        self.play(FadeIn(rw_pos, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Nested Quantifiers (1:30)
    # ------------------------------------------------------------------
    def scene8_nested(self):
        self.add_subcaption(
            "When predicates have multiple variables, we use nested "
            "quantifiers. For every x there exists y such that y is greater "
            "than x means every number has a bigger one. "
            "The order of quantifiers matters! "
            "For every student there exists a class is different from "
            "there exists a class for every student.",
            duration=16,
        )
        self.ly.section_divider(8, "Nested Quantifiers")

        title = self.ly.title("Quantifiers Inside Quantifiers")

        # First nested example
        nested = MathTex(
            r"\forall x \, \exists y \, (y > x)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(nested, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(nested), run_time=SLOW)
        self.wait(0.5)

        meaning = Text(
            '"For every x, there exists some y greater than x."',
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(meaning, direction=DOWN, anchor=nested, buff=0.5)
        self.play(FadeIn(meaning, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        witness = Text(
            "Witness: y = x + 1  (always works!)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(witness, direction=DOWN, anchor=meaning, buff=0.4)
        self.play(FadeIn(witness, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        result = Text(
            "TRUE over natural numbers",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(result, direction=DOWN, anchor=witness, buff=0.4)
        self.play(FadeIn(result, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # Order matters
        title_order = self.ly.title("Order Matters!")

        order_left = MathTex(
            r"\forall x \, \exists y \, P(x, y)",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        order_right = MathTex(
            r"\exists y \, \forall x \, P(x, y)",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        left_label = Text(
            "For every x, there is a y",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        right_label = Text(
            "There is a y for every x",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        left_col = VGroup(order_left, left_label).arrange(DOWN, buff=0.2)
        right_col = VGroup(order_right, right_label).arrange(DOWN, buff=0.2)

        self.ly.two_columns(left_col, right_col, start_from=title_order)
        self.wait(0.5)

        not_eq = Text(
            "These are NOT the same in general!",
            font_size=HEADING_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(not_eq, direction=DOWN, anchor=left_col, buff=0.5)
        self.play(FadeIn(not_eq, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Summary + Outro (0:30)
    # ------------------------------------------------------------------
    def scene9_summary(self):
        self.add_subcaption(
            "Let's recap predicate logic. "
            "Predicates have variables and become true or false when we "
            "substitute values. "
            "The domain of discourse tells us what values are allowed. "
            "For all means every element satisfies the predicate. "
            "There exists means at least one does. "
            "Negating flips for all to there exists and vice versa. "
            "Nested quantifiers let us express statements about "
            "relationships between variables. "
            "This is the language mathematicians use every day. "
            "Next up: Sets and Operations.",
            duration=22,
        )
        title = self.ly.title("Summary")

        items = [
            Text("Predicates + domains + quantifiers", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text(r"For all: every element must satisfy", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text(r"There exists: at least one works", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text(r"Negation flips quantifiers", font_size=BODY_SIZE, color=RED, font=SANS),
            Text(r"Nested quantifiers: order matters!", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        play_outro(self, "Sets and Operations", "Discrete Mathematics")
        self.ly.clear()
