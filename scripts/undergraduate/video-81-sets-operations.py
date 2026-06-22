"""Video 81: Sets and Operations
Discrete Mathematics -- Video 3 of 12

Covers: Set notation, roster method, set builder notation, special sets (empty,
universal, subset), union and intersection, difference and complement, power set,
Cartesian product, De Morgan's laws for sets.

Plan: planning/video-81-sets-operations.md

Render draft:  manim -ql scripts/undergraduate/video-81-sets-operations.py Video81_SetsOperations
Render final:  manim -qh scripts/undergraduate/video-81-sets-operations.py Video81_SetsOperations
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
from layout import LayoutEngine, ensure_fits, clamp_position


class Video81_SetsOperations(Scene):
    """Sets and Operations -- notation, builder notation, special sets,
    operations, power set, Cartesian product, De Morgan's laws."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_roster()
        self.scene3_builder()
        self.scene4_special()
        self.scene5_union_intersection()
        self.scene6_difference_complement()
        self.scene7_power_set()
        self.scene8_cartesian()
        self.scene9_demorgan()
        self.scene10_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook — What is a Set? (1:00)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "In the last video we studied predicate logic. "
            "A predicate like P of x picks out the elements that satisfy it. "
            "Those elements form a set. "
            "A set is simply a well-defined collection of distinct objects. "
            "You've already been using sets your whole mathematical life. "
            "The natural numbers are a set. The even numbers are a set. "
            "Sets are the absolute foundation of all of mathematics. "
            "Everything we study, from numbers to functions to spaces, "
            "is built from sets. "
            "Let's learn how to work with them.",
            duration=24,
        )
        play_intro(self, "Sets and Operations", "Discrete Mathematics")

        title = self.ly.title("What is a Set?")

        # Bridge from Video 80
        bridge = Text(
            "A predicate P(x) picks out elements that satisfy it.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(bridge, direction=DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Definition
        definition = Text(
            "A set is a well-defined collection of distinct objects.",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(definition, direction=DOWN, anchor=bridge, buff=0.5)
        self.play(FadeIn(definition, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Examples
        ex1 = MathTex(
            r"A = \{1, 2, 3\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ex1, direction=DOWN, anchor=definition, buff=0.5)
        self.play(Write(ex1), run_time=NORMAL)
        self.wait(1)

        ex2 = MathTex(
            r"B = \{\text{red}, \text{blue}, \text{green}\}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex2, direction=DOWN, anchor=ex1, buff=0.4)
        self.play(Write(ex2), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Set Notation and Roster Method (1:15)
    # ------------------------------------------------------------------
    def scene2_roster(self):
        self.add_subcaption(
            "We write sets using curly braces. These curly braces are the "
            "universal symbol for sets across all of mathematics. "
            "To say that x belongs to A, we write x element-of A. "
            "The element-of symbol is a stylized epsilon. "
            "If x does not belong to A, we put a slash through it: "
            "x not-element-of A. "
            "The simplest way to describe a set is the roster method: "
            "just list every element inside the braces. "
            "For example, A equals curly-brace 1, 2, 3, 4, 5. "
            "Two important properties: the order of elements does not matter, "
            "so 1, 2, 3 is the same set as 3, 1, 2. "
            "And duplicates are ignored, so curly-brace 1, 1, 2 "
            "is just the set curly-brace 1, 2.",
            duration=30,
        )
        self.ly.section_divider(2, "Set Notation")

        title = self.ly.title("The Roster Method")

        # Notation intro
        braces = Text(
            "Curly braces { } denote a set",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(braces, direction=DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(braces, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        # Element of
        elem = MathTex(
            r"x \in A",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(elem, direction=DOWN, anchor=braces, buff=0.5)
        self.play(Write(elem), run_time=NORMAL)
        self.wait(1)

        elem_meaning = Text(
            '"x is an element of A"  or  "x belongs to A"',
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(elem_meaning, direction=DOWN, anchor=elem, buff=0.4)
        self.play(FadeIn(elem_meaning, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Roster example
        title2 = self.ly.title("Roster Method: List the Elements")

        roster = MathTex(
            r"A = \{1, 2, 3, 4, 5\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(roster, direction=DOWN, anchor=title2, buff=0.6)
        self.play(Write(roster), run_time=NORMAL)
        self.wait(1.5)

        # Properties
        prop1 = Text(
            "Order doesn't matter:  {1,2,3} = {3,1,2}",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(prop1, direction=DOWN, anchor=roster, buff=0.5)
        self.play(FadeIn(prop1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        prop2 = Text(
            "No duplicates:  {1, 1, 2} = {1, 2}",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(prop2, direction=DOWN, anchor=prop1, buff=0.4)
        self.play(FadeIn(prop2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Set Builder Notation (1:30)
    # ------------------------------------------------------------------
    def scene3_builder(self):
        self.add_subcaption(
            "For infinite sets we can't list every element. "
            "Imagine trying to write down every even number! "
            "Instead, we use set builder notation to describe a set by a rule. "
            "The general form is: open curly brace, "
            "x in U such that P of x, close curly brace. "
            "This reads as: the set of all x in the universal set U "
            "where the predicate P of x is true. "
            "The vertical bar means 'such that' or 'where'. "
            "For example, the set of even integers: "
            "all integers x such that x is divisible by 2. "
            "The set of primes: all natural numbers x "
            "where x has exactly two divisors. "
            "Notice how this directly uses predicates from the last video. "
            "The predicate P of x defines which elements make it into the set.",
            duration=36,
        )
        self.ly.section_divider(3, "Set Builder Notation")

        title = self.ly.title("Describing Sets by a Rule")

        # Motivation
        motivation = Text(
            "For infinite sets, we can't list every element!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(motivation, direction=DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(motivation, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # General form
        form = MathTex(
            r"\{ x \in U \mid P(x) \}",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.safe_place(form, direction=DOWN, anchor=motivation, buff=0.5)
        self.play(Write(form), run_time=SLOW)
        self.wait(1)

        form_words = Text(
            '"The set of all x in U such that P(x) is true"',
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(form_words, direction=DOWN, anchor=form, buff=0.5)
        self.play(FadeIn(form_words, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Examples
        title2 = self.ly.title("Examples")

        # Even numbers
        ex1 = MathTex(
            r"E = \{ x \in \mathbb{Z} \mid x \text{ is even} \}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ex1, direction=DOWN, anchor=title2, buff=0.6)
        self.play(Write(ex1), run_time=NORMAL)
        self.wait(1.5)

        # Primes
        ex2 = MathTex(
            r"P = \{ x \in \mathbb{N} \mid x \text{ is prime} \}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex2, direction=DOWN, anchor=ex1, buff=0.5)
        self.play(Write(ex2), run_time=NORMAL)
        self.wait(1.5)

        # Bridge to predicate logic
        bridge = Text(
            "The predicate P(x) from the last video defines the set!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(bridge, direction=DOWN, anchor=ex2, buff=0.5)
        self.play(FadeIn(bridge, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Special Sets (1:00)
    # ------------------------------------------------------------------
    def scene4_special(self):
        self.add_subcaption(
            "Some sets deserve special names and symbols. "
            "The empty set, written with the null symbol or empty braces, "
            "contains absolutely nothing. It may seem trivial, "
            "but the empty set is a subset of every set. "
            "The universal set U contains every element under consideration. "
            "When we take a complement, we remove elements from U. "
            "When every element of set A is also in set B, "
            "we say A is a subset of B. "
            "If A is contained in B but they are not equal, "
            "we call it a proper subset. "
            "We can visualize this with Venn diagrams: "
            "the subset A appears as a smaller circle "
            "completely inside the larger circle B.",
            duration=28,
        )
        self.ly.section_divider(4, "Special Sets")

        title = self.ly.title("Empty Set, Universal Set, Subsets")

        # Empty set
        empty = MathTex(
            r"\emptyset = \{\}",
            font_size=HEADING_SIZE, color=RED,
        )
        empty_label = Text(
            "Empty set: contains nothing",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(empty, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(empty), run_time=NORMAL)
        self.ly.safe_place(empty_label, direction=DOWN, anchor=empty, buff=0.3)
        self.play(FadeIn(empty_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Universal set
        univ = MathTex(
            r"U",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        univ_label = Text(
            "Universal set: all elements under consideration",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(univ, direction=DOWN, anchor=empty_label, buff=0.5)
        self.play(Write(univ), run_time=NORMAL)
        self.ly.safe_place(univ_label, direction=DOWN, anchor=univ, buff=0.3)
        self.play(FadeIn(univ_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # Subset (sub-scene to stay within 5-item budget)
        title2 = self.ly.title("Subsets")

        subset = MathTex(
            r"A \subseteq B",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        subset_label = Text(
            "A is a subset of B: every element of A is in B",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(subset, direction=DOWN, anchor=title2, buff=0.6)
        self.play(Write(subset), run_time=NORMAL)
        self.ly.safe_place(subset_label, direction=DOWN, anchor=subset, buff=0.3)
        self.play(FadeIn(subset_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Proper subset
        proper = MathTex(
            r"A \subset B",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        proper_label = Text(
            "Proper subset: A is contained in B, but A is not equal to B",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(proper, direction=DOWN, anchor=subset_label, buff=0.4)
        self.play(Write(proper), run_time=NORMAL)
        self.ly.safe_place(proper_label, direction=DOWN, anchor=proper, buff=0.3)
        self.play(FadeIn(proper_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Union and Intersection (1:30)
    # ------------------------------------------------------------------
    def scene5_union_intersection(self):
        self.add_subcaption(
            "Now we combine sets using operations. "
            "The two most fundamental operations are union and intersection. "
            "The union of A and B, written A union B, "
            "contains every element that is in A or in B or in both. "
            "Think of it as combining everything from both sets. "
            "The intersection of A and B, written A intersect B, "
            "contains only elements that are in BOTH sets simultaneously. "
            "On a Venn diagram, the union shades both circles entirely. "
            "The intersection shades only the overlapping region. "
            "If two sets share no elements at all, "
            "their intersection is the empty set. "
            "We call such sets disjoint.",
            duration=34,
        )
        self.ly.section_divider(5, "Union and Intersection")

        title = self.ly.title("Two Fundamental Operations")

        # Venn diagram setup — circles positioned within a group, group placed with layout
        circle_a = Circle(radius=1.2, color=PRIMARY, stroke_width=3)
        circle_a.move_to(LEFT * 0.6 + DOWN * 0.3)
        label_a = Text("A", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        label_a.next_to(circle_a, UP, buff=0.2)

        circle_b = Circle(radius=1.2, color=SECONDARY, stroke_width=3)
        circle_b.move_to(RIGHT * 0.6 + DOWN * 0.3)
        label_b = Text("B", font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        label_b.next_to(circle_b, UP, buff=0.2)

        venn_group = VGroup(circle_a, circle_b, label_a, label_b)
        venn_group.scale(0.9)
        venn_group.move_to(RIGHT * 2.5 + DOWN * 0.2)
        clamp_position(venn_group)

        # Union formula — placed with safe_place instead of raw move_to
        union_formula = MathTex(
            r"A \cup B = \{ x \mid x \in A \text{ or } x \in B \}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(union_formula, direction=DOWN, anchor=title, buff=0.6)
        self.play(Create(circle_a), Create(circle_b), run_time=NORMAL)
        self.play(FadeIn(label_a), FadeIn(label_b), run_time=FAST)
        self.wait(0.5)
        self.play(Write(union_formula), run_time=NORMAL)
        self.wait(0.5)

        union_label = Text(
            "Union: everything in A OR B or both",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(union_label, direction=DOWN, anchor=union_formula, buff=0.3)
        self.play(FadeIn(union_label, shift=LEFT * 0.15), run_time=NORMAL)

        # Shade union
        union_fill_a = circle_a.copy().set_fill(PRIMARY, opacity=0.25).set_stroke(width=0)
        union_fill_b = circle_b.copy().set_fill(SECONDARY, opacity=0.25).set_stroke(width=0)
        self.play(FadeIn(union_fill_a), FadeIn(union_fill_b), run_time=NORMAL)
        self.wait(2)
        self.play(FadeOut(union_fill_a), FadeOut(union_fill_b), run_time=FAST)

        self.ly.clear()

        # Intersection on fresh scene
        title2 = self.ly.title("Intersection")

        circle_a2 = Circle(radius=1.2, color=PRIMARY, stroke_width=3)
        circle_a2.move_to(LEFT * 0.6 + DOWN * 0.3)
        label_a2 = Text("A", font_size=HEADING_SIZE, color=PRIMARY, font=SANS)
        label_a2.next_to(circle_a2, UP, buff=0.2)

        circle_b2 = Circle(radius=1.2, color=SECONDARY, stroke_width=3)
        circle_b2.move_to(RIGHT * 0.6 + DOWN * 0.3)
        label_b2 = Text("B", font_size=HEADING_SIZE, color=SECONDARY, font=SANS)
        label_b2.next_to(circle_b2, UP, buff=0.2)

        venn2 = VGroup(circle_a2, circle_b2, label_a2, label_b2)
        venn2.scale(0.9)
        venn2.move_to(RIGHT * 2.5 + DOWN * 0.2)
        clamp_position(venn2)

        inter_formula = MathTex(
            r"A \cap B = \{ x \mid x \in A \text{ and } x \in B \}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(inter_formula, direction=DOWN, anchor=title2, buff=0.6)
        self.play(Create(circle_a2), Create(circle_b2), run_time=NORMAL)
        self.play(FadeIn(label_a2), FadeIn(label_b2), run_time=FAST)
        self.play(Write(inter_formula), run_time=NORMAL)
        self.wait(0.5)

        inter_label = Text(
            "Intersection: only elements in BOTH",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(inter_label, direction=DOWN, anchor=inter_formula, buff=0.3)
        self.play(FadeIn(inter_label, shift=LEFT * 0.15), run_time=NORMAL)

        # Shade intersection
        inter_dot = Circle(radius=0.55, color=ACCENT, fill_opacity=0.35, stroke_width=0)
        inter_dot.move_to((circle_a2.get_center() + circle_b2.get_center()) / 2)
        clamp_position(inter_dot)
        self.play(FadeIn(inter_dot), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Example
        title3 = self.ly.title("Example")

        ex_a = MathTex(
            r"A = \{1, 2, 3, 4\}, \quad B = \{3, 4, 5, 6\}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex_a, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(ex_a), run_time=NORMAL)
        self.wait(1)

        ex_union = MathTex(
            r"A \cup B = \{1, 2, 3, 4, 5, 6\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ex_union, direction=DOWN, anchor=ex_a, buff=0.5)
        self.play(Write(ex_union), run_time=NORMAL)
        self.wait(1)

        ex_inter = MathTex(
            r"A \cap B = \{3, 4\}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex_inter, direction=DOWN, anchor=ex_union, buff=0.4)
        self.play(Write(ex_inter), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Difference and Complement (1:15)
    # ------------------------------------------------------------------
    def scene6_difference_complement(self):
        self.add_subcaption(
            "Two more operations let us remove elements from sets. "
            "The set difference A minus B contains elements that are in A "
            "but NOT in B. It's like taking A and stripping away anything "
            "that also appears in B. "
            "The complement of A goes further: it removes everything in A "
            "from the universal set U. The complement contains all elements "
            "that are NOT in A. "
            "These operations connect beautifully to logic from the last video. "
            "Set difference A minus B is like A AND NOT B. "
            "Complement is like negation. "
            "Union is like OR. Intersection is like AND. "
            "The parallels between logic and sets are deep and powerful.",
            duration=32,
        )
        self.ly.section_divider(6, "Difference and Complement")

        title = self.ly.title("Removing Elements")

        # Difference
        diff_formula = MathTex(
            r"A \setminus B = \{ x \mid x \in A \text{ and } x \notin B \}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        diff_label = Text(
            "Set difference: in A but NOT in B",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(diff_formula, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(diff_formula), run_time=NORMAL)
        self.wait(1)
        self.ly.safe_place(diff_label, direction=DOWN, anchor=diff_formula, buff=0.3)
        self.play(FadeIn(diff_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1.5)

        # Example for difference
        diff_ex = MathTex(
            r"\{1,2,3,4\} \setminus \{3,4,5\} = \{1, 2\}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(diff_ex, direction=DOWN, anchor=diff_label, buff=0.5)
        self.play(Write(diff_ex), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Complement
        title2 = self.ly.title("Complement")

        comp_formula = MathTex(
            r"A^{c} = U \setminus A = \{ x \mid x \in U \text{ and } x \notin A \}",
            font_size=HEADING_SIZE, color=RED,
        )
        comp_label = Text(
            "Complement: everything NOT in A",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(comp_formula, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(comp_formula), run_time=NORMAL)
        self.wait(1)
        self.ly.safe_place(comp_label, direction=DOWN, anchor=comp_formula, buff=0.3)
        self.play(FadeIn(comp_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Example
        ex = MathTex(
            r"U = \{1,2,3,4,5\}, \quad A = \{1,2\}, \quad A^{c} = \{3,4,5\}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex, direction=DOWN, anchor=comp_label, buff=0.5)
        self.play(Write(ex), run_time=NORMAL)
        self.wait(1)

        # Logic connection
        logic = Text(
            "Complement ~ NOT  |  Union ~ OR  |  Intersection ~ AND",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(logic, direction=DOWN, anchor=ex, buff=0.5)
        self.play(FadeIn(logic, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Power Set (1:15)
    # ------------------------------------------------------------------
    def scene7_power_set(self):
        self.add_subcaption(
            "Given a set A, its power set is the collection of ALL subsets of A. "
            "Let's work through an example. "
            "For A equals curly-brace 1, 2, the subsets are: "
            "the empty set, curly-brace 1, curly-brace 2, "
            "and curly-brace 1, 2 itself. "
            "That gives us 4 subsets in total. "
            "Notice that 4 equals 2 squared. "
            "For A equals curly-brace 1, 2, 3, "
            "there are 8 subsets, which is 2 cubed. "
            "The pattern is clear: a set with n elements "
            "has exactly 2 to the n subsets. "
            "This means the power set grows exponentially! "
            "Each new element you add to the set doubles "
            "the number of subsets. "
            "This is a beautiful combinatorial insight.",
            duration=34,
        )
        self.ly.section_divider(7, "Power Set")

        title = self.ly.title("The Set of All Subsets")

        definition = Text(
            "The power set P(A) contains ALL subsets of A.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(definition, direction=DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(definition, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        # Example 1
        ex1_set = MathTex(
            r"A = \{1, 2\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(ex1_set, direction=DOWN, anchor=definition, buff=0.5)
        self.play(Write(ex1_set), run_time=NORMAL)
        self.wait(1)

        ex1_power = MathTex(
            r"\mathcal{P}(A) = \big\{ \emptyset, \{1\}, \{2\}, \{1, 2\} \big\}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex1_power, direction=DOWN, anchor=ex1_set, buff=0.5)
        self.play(Write(ex1_power), run_time=NORMAL)
        self.wait(1)

        count1 = MathTex(
            r"|\mathcal{P}(A)| = 4 = 2^{2}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(count1, direction=DOWN, anchor=ex1_power, buff=0.4)
        self.play(Write(count1), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Example 2 and formula
        title2 = self.ly.title("The Pattern")

        ex2_set = MathTex(
            r"A = \{1, 2, 3\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        ex2_count = MathTex(
            r"|\mathcal{P}(A)| = 8 = 2^{3}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(ex2_set, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(ex2_set), run_time=NORMAL)
        self.wait(1)
        self.ly.safe_place(ex2_count, direction=DOWN, anchor=ex2_set, buff=0.5)
        self.play(Write(ex2_count), run_time=NORMAL)
        self.wait(1)

        # The formula
        formula_box = self.ly.formula_box(
            MathTex(
                r"|\mathcal{P}(A)| = 2^{|A|}",
                font_size=TITLE_SIZE, color=ACCENT,
            ),
            color=ACCENT,
        )
        self.ly.safe_place(formula_box, direction=DOWN, anchor=ex2_count, buff=0.6)
        self.play(Write(formula_box), run_time=SLOW)
        self.wait(1)

        insight = Text(
            "Each new element DOUBLES the power set!",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=formula_box, buff=0.5)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Cartesian Product (1:15)
    # ------------------------------------------------------------------
    def scene8_cartesian(self):
        self.add_subcaption(
            "An ordered pair combines two elements in a specific sequence. "
            "The pair 1 comma 2 is different from 2 comma 1. "
            "Order matters! This is crucial. "
            "The Cartesian product A times B is the set of ALL ordered pairs "
            "where the first element comes from A and the second from B. "
            "For example, if A is curly-brace 1, 2 and B is curly-brace x, y, "
            "then A times B contains four ordered pairs: "
            "1,x, 1,y, 2,x, and 2,y. "
            "The size of the Cartesian product is "
            "the product of the sizes: |A| times |B|. "
            "You've already seen this idea. "
            "The x-y coordinate plane is the Cartesian product "
            "of the real numbers with itself: R times R. "
            "Every point on the plane is an ordered pair in this set.",
            duration=38,
        )
        self.ly.section_divider(8, "Cartesian Product")

        title = self.ly.title("Ordered Pairs and Products")

        # Ordered pair
        pair_def = MathTex(
            r"(a, b) \neq (b, a) \quad \text{order matters!}",
            font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(pair_def, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(pair_def), run_time=NORMAL)
        self.wait(1)

        # Definition
        cart_def = MathTex(
            r"A \times B = \{ (a, b) \mid a \in A, \; b \in B \}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(cart_def, direction=DOWN, anchor=pair_def, buff=0.5)
        self.play(Write(cart_def), run_time=NORMAL)
        self.wait(1)
        self.ly.clear()

        # Example (sub-scene to stay within 5-item budget)
        title2 = self.ly.title("Cartesian Product Example")

        ex_sets = MathTex(
            r"A = \{1, 2\}, \quad B = \{x, y\}",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(ex_sets, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(ex_sets), run_time=NORMAL)
        self.wait(1)

        ex_product = MathTex(
            r"A \times B = \{(1,x), (1,y), (2,x), (2,y)\}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(ex_product, direction=DOWN, anchor=ex_sets, buff=0.5)
        self.play(Write(ex_product), run_time=NORMAL)
        self.wait(0.5)

        # Size formula
        size = MathTex(
            r"|A \times B| = |A| \times |B| = 2 \times 2 = 4",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(size, direction=DOWN, anchor=ex_product, buff=0.4)
        self.play(Write(size), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Connection to geometry
        title2 = self.ly.title("The x-y Plane")

        connection = Text(
            "The coordinate plane is R times R:",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(connection, direction=DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(connection, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(1)

        plane_eq = MathTex(
            r"\mathbb{R} \times \mathbb{R} = \mathbb{R}^{2}",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.safe_place(plane_eq, direction=DOWN, anchor=connection, buff=0.5)
        self.play(Write(plane_eq), run_time=SLOW)
        self.wait(1)

        plane_words = Text(
            "Every point (x, y) is an ordered pair in R x R",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(plane_words, direction=DOWN, anchor=plane_eq, buff=0.5)
        self.play(FadeIn(plane_words, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: De Morgan's Laws for Sets (1:15)
    # ------------------------------------------------------------------
    def scene9_demorgan(self):
        self.add_subcaption(
            "One of the most elegant results in set theory is that "
            "De Morgan's laws from logic carry over to sets. "
            "The complement of A union B "
            "equals the intersection of A complement and B complement. "
            "In words: everything NOT in the union "
            "is exactly the stuff that's outside A AND outside B. "
            "Similarly, the complement of A intersect B "
            "equals the union of A complement and B complement. "
            "You can verify these with Venn diagrams. "
            "Shade the region outside both circles, "
            "then shade outside A and outside B separately. "
            "You get the same region! "
            "These laws mirror exactly what we saw in propositional logic. "
            "Union behaves like OR, intersection like AND, "
            "and complement like NOT. "
            "This deep connection between logic and sets "
            "is one of the foundations of modern mathematics.",
            duration=38,
        )
        self.ly.section_divider(9, "De Morgan's Laws for Sets")

        title = self.ly.title("De Morgan's Laws for Sets")

        # Law 1
        law1 = MathTex(
            r"(A \cup B)^{c} = A^{c} \cap B^{c}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        words1 = Text(
            "Complement of union = Intersection of complements",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(law1, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(law1), run_time=NORMAL)
        self.wait(1)
        self.ly.safe_place(words1, direction=DOWN, anchor=law1, buff=0.3)
        self.play(FadeIn(words1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Law 2
        title2 = self.ly.title("The Other Direction")

        law2 = MathTex(
            r"(A \cap B)^{c} = A^{c} \cup B^{c}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        words2 = Text(
            "Complement of intersection = Union of complements",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(law2, direction=DOWN, anchor=title2, buff=0.5)
        self.play(Write(law2), run_time=NORMAL)
        self.wait(1)
        self.ly.safe_place(words2, direction=DOWN, anchor=law2, buff=0.3)
        self.play(FadeIn(words2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        self.ly.clear()

        # Logic connection
        title3 = self.ly.title("Same Pattern as Logic!")

        logic1 = MathTex(
            r"\neg(A \lor B) \equiv \neg A \land \neg B",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        sets1 = MathTex(
            r"(A \cup B)^{c} = A^{c} \cap B^{c}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(logic1, direction=DOWN, anchor=title3, buff=0.5)
        self.play(Write(logic1), run_time=NORMAL)
        self.wait(1)
        self.ly.safe_place(sets1, direction=DOWN, anchor=logic1, buff=0.5)
        self.play(Write(sets1), run_time=NORMAL)
        self.wait(1)

        insight = Text(
            "Union ~ OR  |  Intersection ~ AND  |  Complement ~ NOT",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(insight, direction=DOWN, anchor=sets1, buff=0.5)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Summary + Outro (0:30)
    # ------------------------------------------------------------------
    def scene10_summary(self):
        self.add_subcaption(
            "Let's recap everything we've learned about sets. "
            "A set is a collection of objects written in curly braces. "
            "We can list elements with the roster method, "
            "or describe them with set builder notation using predicates. "
            "Special sets include the empty set, the universal set, "
            "and the concept of subsets. "
            "The four set operations are union, intersection, "
            "difference, and complement. "
            "The power set collects all subsets "
            "and always has 2 to the n elements. "
            "The Cartesian product creates ordered pairs. "
            "And De Morgan's laws connect set operations to logic. "
            "Sets truly are the foundation of all mathematics. "
            "Next up: Relations and Functions, "
            "which are built entirely on sets.",
            duration=28,
        )
        title = self.ly.title("Summary")

        items = [
            Text("Sets: collections in curly braces", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Notation: roster method + set builder", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Operations: union, intersection, difference, complement", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Power set: 2^n subsets  |  Cartesian product: ordered pairs", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("De Morgan's laws: sets mirror logic", font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(2)

        play_outro(self, "Relations and Functions", "Discrete Mathematics")
        self.ly.clear()
