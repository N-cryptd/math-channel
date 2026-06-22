"""Video 82: Relations and Functions
Discrete Mathematics -- Video 4 of 12

Covers: Relations as subsets of Cartesian products, directed graphs,
reflexive/symmetric/transitive properties, functions as special relations,
injective/surjective/bijective functions, composition.

Plan: planning/video-82-relations-functions.md

Render draft:  manim -ql scripts/undergraduate/video-82-relations-functions.py Video82_RelationsFunctions
Render final:  manim -qh scripts/undergraduate/video-82-relations-functions.py Video82_RelationsFunctions
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


class Video82_RelationsFunctions(Scene):
    """Relations and Functions -- relations as subsets, digraphs,
    reflexive/symmetric/transitive, functions, injective/surjective/bijective,
    composition."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_what_is_relation()
        self.scene3_digraphs()
        self.scene4_reflexive()
        self.scene5_symmetric()
        self.scene6_transitive()
        self.scene7_functions()
        self.scene8_function_types()
        self.scene9_composition()
        self.scene10_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook -- From Sets to Relationships (1:00)
    # ------------------------------------------------------------------
    def scene1_hook(self):
        self.add_subcaption(
            "Last video, we learned about sets: collections of objects. "
            "But in mathematics, we often care about how objects relate "
            "to each other. What does it mean for one number to be less "
            "than another? For two people to be friends? For one integer "
            "to divide another evenly? These are connections between "
            "pairs of objects. A relation is how we capture these "
            "connections mathematically.",
            duration=15,
        )
        play_intro(self, "Relations and Functions", "Discrete Mathematics")

        title = self.ly.title("From Sets to Connections")

        # Motivating example 1
        ex1 = Text(
            '"is less than"  --  a connection between pairs of numbers',
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(ex1, direction=DOWN, anchor=title, buff=0.6)
        self.play(FadeIn(ex1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Motivating example 2
        ex2 = Text(
            '"is a friend of"  --  a connection between pairs of people',
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(ex2, direction=DOWN, anchor=ex1, buff=0.4)
        self.play(FadeIn(ex2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Motivating example 3
        ex3 = Text(
            '"divides evenly"  --  a connection between pairs of integers',
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(ex3, direction=DOWN, anchor=ex2, buff=0.4)
        self.play(FadeIn(ex3, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Teaser
        teaser = Text(
            "These aren't properties of single objects -- they are CONNECTIONS.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(teaser, direction=DOWN, anchor=ex3, buff=0.5)
        self.play(FadeIn(teaser, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: What is a Relation? (1:00)
    # ------------------------------------------------------------------
    def scene2_what_is_relation(self):
        self.add_subcaption(
            "A relation R from set A to set B is simply a subset of the "
            "Cartesian product A times B. Remember from the last video, "
            "A times B contains every ordered pair where the first element "
            "comes from A and the second from B. A relation is any "
            "collection of these pairs. We can visualize a relation using "
            "an arrow diagram: elements of A on the left, B on the right, "
            "with arrows connecting each pair in the relation.",
            duration=15,
        )
        self.ly.section_divider(2, "What is a Relation?")

        title = self.ly.title("Relations as Subsets")

        # Definition
        definition = MathTex(
            r"R \subseteq A \times B",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(definition, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(definition), run_time=NORMAL)
        self.wait(0.5)

        # Concrete example
        example = Text(
            "Example: A = {1, 2, 3},  B = {a, b}",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(example, direction=DOWN, anchor=definition, buff=0.5)
        self.play(FadeIn(example, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # A specific relation
        rel = MathTex(
            r"R = \{(1,a),\;(2,b),\;(3,a)\}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(rel, direction=DOWN, anchor=example, buff=0.4)
        self.play(Write(rel), run_time=NORMAL)
        self.wait(0.5)

        # Arrow diagram explanation
        arrow_note = Text(
            "Visualize with arrows: A -- arrow --> B for each pair",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(arrow_note, direction=DOWN, anchor=rel, buff=0.4)
        self.play(FadeIn(arrow_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Directed Graphs (1:00)
    # ------------------------------------------------------------------
    def scene3_digraphs(self):
        self.add_subcaption(
            "When A and B are the same set, we say R is a relation on A. "
            "We can draw this as a directed graph, or digraph. "
            "Each element becomes a vertex, a dot on screen. "
            "Each ordered pair becomes a directed arrow from the first "
            "element to the second. If an element is related to itself, "
            "we draw a loop arrow starting and ending at the same vertex.",
            duration=14,
        )
        self.ly.section_divider(3, "Directed Graphs")

        title = self.ly.title("Visualizing Relations as Digraphs")

        # Define a relation on a set
        rel_def = MathTex(
            r"R = \{(1,2),\;(2,3),\;(1,1)\} \text{ on } \{1,2,3\}",
            font_size=BODY_SIZE, color=ACCENT,
        )
        self.ly.safe_place(rel_def, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(rel_def), run_time=NORMAL)
        self.wait(0.5)

        # Build the digraph
        vertices = VGroup(*[
            Dot(radius=0.12, color=PRIMARY).move_to(LEFT * 3 + UP * 1),
            Dot(radius=0.12, color=PRIMARY).move_to(LEFT * 3 + DOWN * 1),
            Dot(radius=0.12, color=PRIMARY).move_to(RIGHT * 3),
        ])
        labels = VGroup(
            MathTex("1", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[0], UP, buff=0.15),
            MathTex("2", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[1], DOWN, buff=0.15),
            MathTex("3", font_size=LABEL_SIZE, color=WHITE).next_to(vertices[2], UP, buff=0.15),
        )
        graph_group = VGroup(vertices, labels)
        self.ly.safe_place(graph_group, direction=DOWN, anchor=rel_def, buff=0.5)
        # Center the graph manually within content area
        graph_group.move_to(self.ly.content_top * DOWN * 0.4 + ORIGIN)
        graph_group.move_to(ORIGIN + DOWN * 0.3)

        self.play(Create(vertices), run_time=NORMAL)
        self.play(FadeIn(labels), run_time=NORMAL)
        self.wait(0.3)

        # Arrow 1->2
        arrow_12 = Arrow(
            vertices[0].get_center() + RIGHT * 0.15,
            vertices[1].get_center() + RIGHT * 0.15,
            buff=0.12, stroke_width=3, color=SECONDARY,
        )
        self.play(Create(arrow_12), run_time=FAST)
        self.wait(0.3)

        # Arrow 2->3
        arrow_23 = Arrow(
            vertices[1].get_center() + UP * 0.15,
            vertices[2].get_center() + DOWN * 0.15,
            buff=0.12, stroke_width=3, color=SECONDARY,
        )
        self.play(Create(arrow_23), run_time=FAST)
        self.wait(0.3)

        # Loop at 1
        loop_1 = ArcBetweenPoints(
            vertices[0].get_center() + UP * 0.2 + LEFT * 0.15,
            vertices[0].get_center() + UP * 0.2 + RIGHT * 0.15,
            angle=TAU / 2, color=ACCENT, stroke_width=2.5,
        ).add_tip(tip_length=0.15, tip_width=0.08)
        self.play(Create(loop_1), run_time=FAST)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Reflexive Relations (1:00)
    # ------------------------------------------------------------------
    def scene4_reflexive(self):
        self.add_subcaption(
            "A relation R on a set A is reflexive if every element is "
            "related to itself. Formally: for every a in A, the pair "
            "a comma a is in R. In a digraph, this means every vertex "
            "has a loop. The less than or equal to relation on real "
            "numbers is reflexive, because every number is less than or "
            "equal to itself. But the strict less than relation is not "
            "reflexive, since no number is strictly less than itself.",
            duration=16,
        )
        self.ly.section_divider(4, "Reflexive")

        title = self.ly.title("Every Element Relates to Itself")

        # Definition
        definition = MathTex(
            r"\forall a \in A: (a, a) \in R",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(definition, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(definition), run_time=NORMAL)
        self.wait(0.5)

        # Visual note
        visual = Text(
            "In a digraph: every vertex has a loop",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(visual, direction=DOWN, anchor=definition, buff=0.5)
        self.play(FadeIn(visual, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Yes example
        yes = MathTex(
            r"\leq \text{ is reflexive: } x \leq x \text{ for all } x",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(yes, direction=DOWN, anchor=visual, buff=0.4)
        self.play(Write(yes), run_time=NORMAL)
        self.wait(0.5)

        # No example
        no = MathTex(
            r"< \text{ is NOT reflexive: } x \not< x",
            font_size=BODY_SIZE, color=RED,
        )
        self.ly.safe_place(no, direction=DOWN, anchor=yes, buff=0.4)
        self.play(Write(no), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Symmetric Relations (1:00)
    # ------------------------------------------------------------------
    def scene5_symmetric(self):
        self.add_subcaption(
            "A relation R is symmetric if whenever a is related to b, "
            "then b is also related to a. In a digraph, every arrow "
            "has a matching return arrow. The relation is a sibling of "
            "is symmetric. The relation is less than is not symmetric. "
            "If a is less than b, then b is not less than a.",
            duration=13,
        )
        self.ly.section_divider(5, "Symmetric")

        title = self.ly.title("Arrows Go Both Ways")

        # Definition
        definition = MathTex(
            r"(a,b) \in R \implies (b,a) \in R",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(definition, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(definition), run_time=NORMAL)
        self.wait(0.5)

        # Visual note
        visual = Text(
            "In a digraph: every arrow has a return arrow",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(visual, direction=DOWN, anchor=definition, buff=0.5)
        self.play(FadeIn(visual, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Yes example
        yes = Text(
            '"is a sibling of" -- symmetric (if A is sibling of B, B is sibling of A)',
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(yes, direction=DOWN, anchor=visual, buff=0.4)
        self.play(FadeIn(yes, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # No example
        no = Text(
            '"is less than" -- NOT symmetric (if a < b, then NOT b < a)',
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(no, direction=DOWN, anchor=yes, buff=0.4)
        self.play(FadeIn(no, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Transitive Relations (1:00)
    # ------------------------------------------------------------------
    def scene6_transitive(self):
        self.add_subcaption(
            "A relation R is transitive if whenever a is related to b and "
            "b is related to c, then a is related to c. In a digraph, "
            "following a chain of arrows always lands at a valid target. "
            "The relation less than or equal to is transitive. If a is "
            "less than or equal to b and b is less than or equal to c, "
            "then a is less than or equal to c. But the relation is a "
            "friend of is not transitive in general.",
            duration=16,
        )
        self.ly.section_divider(6, "Transitive")

        title = self.ly.title("Chains Complete")

        # Definition
        definition = MathTex(
            r"(a,b) \in R \text{ and } (b,c) \in R \implies (a,c) \in R",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(definition, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(definition), run_time=NORMAL)
        self.wait(0.5)

        # Visual note
        visual = Text(
            "In a digraph: chain a -> b -> c implies a -> c exists",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(visual, direction=DOWN, anchor=definition, buff=0.5)
        self.play(FadeIn(visual, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Yes example
        yes = MathTex(
            r"a \leq b \text{ and } b \leq c \implies a \leq c",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(yes, direction=DOWN, anchor=visual, buff=0.4)
        self.play(Write(yes), run_time=NORMAL)
        self.wait(0.5)

        # No example
        no = Text(
            '"is a friend of" -- a knows b, b knows c, but a may not know c',
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(no, direction=DOWN, anchor=yes, buff=0.4)
        self.play(FadeIn(no, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: From Relations to Functions (1:00)
    # ------------------------------------------------------------------
    def scene7_functions(self):
        self.add_subcaption(
            "A function is a special kind of relation with extra constraints. "
            "A function f from A to B is a relation where every element of "
            "A appears exactly once as the first component. Two rules: "
            "every element of A must be assigned something, and each element "
            "of A is assigned exactly one element of B. If an element maps "
            "to two targets, or has no target, it is not a function.",
            duration=16,
        )
        self.ly.section_divider(7, "Functions")

        title = self.ly.title("Special Relations: Functions")

        # Definition
        definition = MathTex(
            r"f: A \to B \quad \text{where } \forall a \in A,\; \exists! \; b \in B: (a,b) \in f",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(definition, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(definition), run_time=NORMAL)
        self.wait(0.5)

        # Two rules
        rule1 = Text(
            "Rule 1: Every a in A must have a mapping",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(rule1, direction=DOWN, anchor=definition, buff=0.5)
        self.play(FadeIn(rule1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        rule2 = Text(
            "Rule 2: Each a maps to exactly one b",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(rule2, direction=DOWN, anchor=rule1, buff=0.4)
        self.play(FadeIn(rule2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Notation
        notation = Text(
            'Notation: f(a) = b  instead of  (a, b) in f',
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(notation, direction=DOWN, anchor=rule2, buff=0.4)
        self.play(FadeIn(notation, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

        # Non-function examples
        title2 = self.ly.title("Not Every Relation is a Function")

        # Two arrows from same element
        bad1 = Text(
            "Two arrows from one element?  NOT a function.",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(bad1, direction=DOWN, anchor=title2, buff=0.6)
        self.play(FadeIn(bad1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # No arrow from an element
        bad2 = Text(
            "An element with no arrow?  NOT a function.",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(bad2, direction=DOWN, anchor=bad1, buff=0.4)
        self.play(FadeIn(bad2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Types of Functions (1:00)
    # ------------------------------------------------------------------
    def scene8_function_types(self):
        self.add_subcaption(
            "Not all functions are the same. An injective function maps "
            "different inputs to different outputs. If f of a equals f of b, "
            "then a must equal b. No two arrows point to the same target. "
            "A surjective function hits every element of the codomain. "
            "Every element of B has an incoming arrow. A bijective function "
            "is both injective and surjective, creating a perfect pairing.",
            duration=16,
        )
        self.ly.section_divider(8, "Types of Functions")

        title = self.ly.title("Injective, Surjective, Bijective")

        # Injective definition
        inj_title = Text(
            "Injective (one-to-one):",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        inj_def = MathTex(
            r"f(a) = f(b) \implies a = b",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        inj_desc = Text(
            "Different inputs give different outputs",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        inj_group = VGroup(inj_title, inj_def, inj_desc).arrange(DOWN, buff=0.15)

        # Surjective definition
        sur_title = Text(
            "Surjective (onto):",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        sur_def = MathTex(
            r"\forall b \in B,\; \exists a \in A: f(a) = b",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        sur_desc = Text(
            "Every codomain element is hit",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        sur_group = VGroup(sur_title, sur_def, sur_desc).arrange(DOWN, buff=0.15)

        self.ly.two_columns(inj_group, sur_group, start_from=title)
        self.wait(0.5)

        # Bijective below
        bij_title = Text(
            "Bijective = injective AND surjective (perfect pairing)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(bij_title, direction=DOWN, anchor=inj_group, buff=0.5)
        self.play(FadeIn(bij_title, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.5)

        # Concrete example
        example = MathTex(
            r"f(x) = 2x \text{ on } \mathbb{Z} \to \mathbb{Z}: \text{ injective but NOT surjective}",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(example, direction=DOWN, anchor=bij_title, buff=0.4)
        self.play(Write(example), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Composition (0:30)
    # ------------------------------------------------------------------
    def scene9_composition(self):
        self.add_subcaption(
            "Functions can be composed. If f maps A to B and g maps B to "
            "C, then the composition g circle f maps A to C, defined by "
            "g of f of x equals g of f of x. For example, if f of x "
            "equals x plus 1, and g of x equals 2x, then g composed "
            "with f of 3 equals g of 4 equals 8. "
            "An important fact: composition of injective functions is "
            "injective, and composition of surjective functions is surjective.",
            duration=18,
        )
        self.ly.section_divider(9, "Composition")

        title = self.ly.title("Chaining Functions Together")

        # Definition
        comp_def = MathTex(
            r"(g \circ f)(x) = g(f(x))",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(comp_def, direction=DOWN, anchor=title, buff=0.6)
        self.play(Write(comp_def), run_time=NORMAL)
        self.wait(0.5)

        # Visual: A -> B -> C
        chain = MathTex(
            r"A \xrightarrow{f} B \xrightarrow{g} C",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(chain, direction=DOWN, anchor=comp_def, buff=0.5)
        self.play(Write(chain), run_time=NORMAL)
        self.wait(0.5)

        # Example
        example = MathTex(
            r"f(x) = x+1, \quad g(x) = 2x \implies (g \circ f)(3) = g(4) = 8",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(example, direction=DOWN, anchor=chain, buff=0.4)
        self.play(Write(example), run_time=NORMAL)
        self.wait(0.5)

        # Property
        prop = Text(
            "Injective composed with injective = injective (same for surjective!)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(prop, direction=DOWN, anchor=example, buff=0.4)
        self.play(FadeIn(prop, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Summary + Outro (0:30)
    # ------------------------------------------------------------------
    def scene10_summary(self):
        self.add_subcaption(
            "Let's recap relations and functions. "
            "A relation is a subset of a Cartesian product. "
            "We visualize relations as directed graphs. "
            "Key properties: reflexive means every element relates to itself, "
            "symmetric means arrows go both ways, transitive means chains "
            "complete. "
            "Functions are special relations where every input maps to "
            "exactly one output. "
            "Functions can be injective, surjective, or bijective. "
            "Functions compose by chaining together. "
            "Next up: Equivalence Relations, where we'll explore relations "
            "that satisfy all three properties at once.",
            duration=22,
        )
        title = self.ly.title("Summary")

        items = [
            Text("Relations = subsets of A x B, visualized as digraphs", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Reflexive: (a,a) for all a", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Symmetric: (a,b) implies (b,a)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Transitive: chains complete (a,b)+(b,c) implies (a,c)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Functions: every input maps to exactly one output", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(1)

        play_outro(self, "Equivalence Relations", "Discrete Mathematics")
        self.ly.clear()
