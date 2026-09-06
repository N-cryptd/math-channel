"""Video 111: Groups -- Definition and Examples
TEMPLATE v2 -- Professional quality Manim script

Playlist: Abstract Algebra I (Video 1 of 12)
Class: Video111_GroupsDefinitionExamples
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


class Video111_GroupsDefinitionExamples(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_pattern()
        self.scene3_axioms()
        self.scene4_integers()
        self.scene5_modular()
        self.scene6_nonexamples()
        self.scene7_abelian()
        self.scene8_big_picture()
        self.scene9_summary()

    # --- Scene 1: Hook ---

    def scene1_hook(self):
        self.add_subcaption(
            "Look at this equilateral triangle. "
            "If you rotate it 120 degrees, it looks exactly the same. "
            "These symmetries form a structure called a group. "
            "Today we define what a group is, "
            "and see how this same structure appears everywhere in mathematics. "
            "This is the first video in our Abstract Algebra series.",
            duration=24.2,  # pacing: 1.25x natural TTS slot
        )
        play_intro(self, "Groups: Definition and Examples", "Abstract Algebra I")

        title = self.ly.title("What Makes Something a Group?")

        # Create triangle and labels as a VGroup for positioning
        tri_size = 1.5
        tri = RegularPolygon(n=3, radius=tri_size, color=WHITE, stroke_width=2.5)
        # Position triangle left of center
        self.ly.safe_place(tri, anchor=ORIGIN, direction=LEFT, buff=2.0)
        self.play(Create(tri), run_time=NORMAL)

        # Labels for vertices
        va = tri.get_vertices()[0]
        vb = tri.get_vertices()[1]
        vc = tri.get_vertices()[2]
        label_a = MathTex(r"A", color=PRIMARY, font_size=28).next_to(va, RIGHT, buff=0.15)
        label_b = MathTex(r"B", color=SECONDARY, font_size=28).next_to(vb, UP + RIGHT, buff=0.15)
        label_c = MathTex(r"C", color=ACCENT, font_size=28).next_to(vc, UP + LEFT, buff=0.15)
        self.play(
            Write(label_a),
            Write(label_b),
            Write(label_c),
            run_time=FAST,
        )
        self.wait(0.3)

        # Rotation text
        rot_label = Text(
            "120° rotation",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(rot_label, anchor=tri, direction=RIGHT, buff=1.5)
        self.play(FadeIn(rot_label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        # Reflection text
        ref_label = Text(
            "Reflection across axis",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(ref_label, anchor=rot_label, direction=DOWN, buff=0.5)
        self.play(FadeIn(ref_label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        # Composition text
        comp_label = Text(
            "Compose two symmetries = another symmetry",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(comp_label, anchor=ref_label, direction=DOWN, buff=0.5)
        self.play(FadeIn(comp_label, shift=LEFT * 0.15), run_time=FAST)
        self.wait(12.6)  # pacing: extends previous caption slot

        # Fade out everything except title? We'll clear at end of scene.
        self.ly.clear()

    # --- Scene 2: Pattern ---

    def scene2_pattern(self):
        self.add_subcaption(
            "Before we define a group formally, "
            "let us look at three examples that all share the same pattern. "
            "The integers under addition. "
            "Clock arithmetic. "
            "And the symmetries of a triangle. "
            "Each has a set, an operation, "
            "and three special properties.",
            duration=19.0,  # pacing: 1.25x natural TTS slot
        )

        title = self.ly.title("The Common Pattern")

        examples = [
            Text("Integers under addition: (ℤ, +)", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Clock arithmetic: (ℤ₆, +)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Symmetries of a triangle", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]

        self.ly.progressive_reveal(examples, start_from=title, run_time=0.6)
        self.wait(0.3)

        feat_title = Text(
            "Every example has:",
            font_size=HEADING_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(feat_title, anchor=examples[-1], direction=DOWN, buff=0.6)
        self.play(Write(feat_title), run_time=FAST)
        self.wait(0.2)

        features = [
            Text("1. A SET of elements", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("2. An OPERATION to combine them", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3. An IDENTITY element", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("4. Every element has an INVERSE", font_size=BODY_SIZE, color=RED, font=SANS),
        ]

        prev = feat_title
        for f in features:
            self.ly.safe_place(f, anchor=prev, direction=DOWN, buff=0.35)
            self.play(FadeIn(f, shift=LEFT * 0.15), run_time=FAST)
            self.wait(0.2)
            prev = f

        self.wait(10.6)  # pacing: extends previous caption slot
        self.ly.clear()

    # --- Scene 3: Axioms ---

    def scene3_axioms(self):
        self.add_subcaption(
            "Now let us state the definition precisely. "
            "A group is a set G with a binary operation star, "
            "satisfying four axioms. "
            "Closure: combining any two elements stays in the set. "
            "Associativity: the grouping does not matter. "
            "Identity: there is a do-nothing element. "
            "Inverse: every element can be undone. "
            "Note that commutativity is NOT required.",
            duration=29.7,  # pacing: 1.25x natural TTS slot
        )

        title = self.ly.title("Definition: Group")

        defn = Text(
            "A group is a set G with an operation",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(defn, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)

        defn2 = Text(
            "satisfying four axioms:",
            font_size=HEADING_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(defn2, anchor=defn, direction=DOWN, buff=0.3)
        self.play(Write(defn2), run_time=NORMAL)
        self.wait(0.3)

        axiom_data = [
            (r"1.\;\text{Closure: } a * b \in G \;\forall\, a,b \in G", PRIMARY),
            (r"2.\;\text{Associativity: } (a*b)*c = a*(b*c)", SECONDARY),
            (r"3.\;\text{Identity: } \exists\, e \in G : e*a = a*e = a", ACCENT),
            (r"4.\;\text{Inverse: } \forall\, a \in G,\;\exists\, a^{-1} : a*a^{-1} = e", RED),
        ]

        prev = defn2
        for tex_str, color in axiom_data:
            card = MathTex(tex_str, color=color, font_size=32)
            self.ly.safe_place(card, anchor=prev, direction=DOWN, buff=0.45)
            self.play(Write(card), run_time=NORMAL)
            self.wait(0.2)
            prev = card

        self.wait(0.3)

        note = Text(
            "Commutativity is NOT on this list!",
            font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(note, anchor=prev, direction=DOWN, buff=0.5)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(19.7)  # pacing: extends previous caption slot

        self.ly.clear()

    # --- Scene 4: Integers Example ---

    def scene4_integers(self):
        self.add_subcaption(
            "Our first verified example: "
            "the integers under addition. "
            "The sum of two integers is an integer: closure holds. "
            "Addition is associative. "
            "Zero is the identity element. "
            "And every integer n has negative n as its inverse. "
            "All four axioms satisfied. The integers form a group.",
            duration=24.8,  # pacing: 1.25x natural TTS slot
        )

        title = self.ly.title(r"Example: $(\mathbb{Z}, +)$")

        items = [
            MathTex(r"\text{Closure: } a + b \in \mathbb{Z}\; \checkmark", color=PRIMARY, font_size=30),
            MathTex(r"\text{Associative: } (a+b)+c = a+(b+c)\; \checkmark", color=SECONDARY, font_size=30),
            MathTex(r"\text{Identity: } e = 0\; \checkmark", color=ACCENT, font_size=30),
            MathTex(r"\text{Inverse: } a^{-1} = -a\; \checkmark", color=RED, font_size=30),
        ]

        prev = title
        for item in items:
            self.ly.safe_place(item, anchor=prev, direction=DOWN, buff=0.4)
            self.play(Write(item), run_time=NORMAL)
            self.wait(0.3)
            prev = item

        result = Text(
            r"$(\mathbb{Z}, +)$ is a group!",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(result, anchor=items[-1], direction=DOWN, buff=0.5)
        self.play(FadeIn(result, scale=1.1), run_time=NORMAL)
        self.wait(0.3)

        note = Text(
            "The star symbol * is just a placeholder for any operation.",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, anchor=result, direction=DOWN, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(15.9)  # pacing: extends previous caption slot

        self.ly.clear()

    # --- Scene 5: Modular Example ---

    def scene5_modular(self):
        self.add_subcaption(
            "Our second example: "
            "the integers modulo 6 under addition. "
            "Think of a clock with hours 0 through 5. "
            "3 plus 4 equals 7, which wraps around to 1. "
            "The sum always stays in the set: closure. "
            "Zero is the identity. "
            "The inverse of n is 6 minus n. "
            "This is a finite group with exactly 6 elements.",
            duration=28.5,  # pacing: 1.25x natural TTS slot
        )

        title = self.ly.title(r"Example: $(\mathbb{Z}_6, +)$")

        elements = MathTex(
            r"\mathbb{Z}_6 = \{0,\; 1,\; 2,\; 3,\; 4,\; 5\}",
            color=WHITE, font_size=30,
        )
        self.ly.safe_place(elements, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(elements), run_time=NORMAL)
        self.wait(0.3)

        # Clock circle and numbers as a VGroup for positioning
        circle_radius = 1.2
        clock = Circle(radius=circle_radius, color=PRIMARY, stroke_width=2)
        # We'll position the clock later relative to elements
        clock_nums = VGroup()
        for i in range(6):
            angle = PI / 2 - i * TAU / 6
            pos = np.array([
                np.cos(angle),
                np.sin(angle),
                0
            ]) * (circle_radius * 0.75)
            num = Text(str(i), font_size=LABEL_SIZE, color=WHITE, font=MONO)
            num.move_to(pos)
            clock_nums.add(num)
        clock_with_nums = VGroup(clock, clock_nums)

        # Place the clock to the right of the elements
        self.ly.safe_place(clock_with_nums, anchor=elements, direction=RIGHT, buff=1.0)
        self.play(Create(clock_with_nums), run_time=FAST)
        self.wait(0.3)

        calc = MathTex(r"3 + 4 \equiv 1 \pmod{6}", color=ACCENT, font_size=28)
        self.ly.safe_place(calc, anchor=clock, direction=DOWN, buff=0.5)
        self.play(Write(calc), run_time=NORMAL)
        self.wait(0.3)

        chk1 = MathTex(
            r"\text{Closure: } a+b \pmod{6} \in \mathbb{Z}_6\; \checkmark",
            color=PRIMARY, font_size=28,
        )
        self.ly.safe_place(chk1, anchor=elements, direction=DOWN, buff=0.4)
        self.play(Write(chk1), run_time=NORMAL)
        self.wait(0.2)

        chk2 = MathTex(
            r"\text{Identity: } e=0,\; \text{Inverse: } n^{-1}=6-n\; \checkmark",
            color=SECONDARY, font_size=28,
        )
        self.ly.safe_place(chk2, anchor=chk1, direction=DOWN, buff=0.35)
        self.play(Write(chk2), run_time=NORMAL)
        self.wait(21.2)  # pacing: extends previous caption slot

        self.ly.clear()

    # --- Scene 6: Non-examples ---

    def scene6_nonexamples(self):
        self.add_subcaption(
            "Now let us see what is NOT a group. "
            "The integers under multiplication: "
            "closure holds, associativity holds, and 1 is the identity. "
            "But the inverse of 2 is one half, not an integer. "
            "One failed axiom is enough. "
            "The integers under subtraction fail associativity: "
            "5 minus 3 minus 2 is 0, "
            "but 5 minus open paren 3 minus 2 close paren is 4.",
            duration=33.8,  # pacing: 1.25x natural TTS slot
        )

        title = self.ly.title("What Is NOT a Group?")

        ne1_title = MathTex(
            r"\text{Non-example: } (\mathbb{Z},\, \times)",
            color=ACCENT, font_size=30,
        )
        self.ly.safe_place(ne1_title, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(ne1_title), run_time=NORMAL)
        self.wait(0.3)

        ne1a = MathTex(
            r"\text{Closure: yes} \quad \text{Assoc: yes} \quad \text{Identity: } 1",
            color=PRIMARY, font_size=26,
        )
        self.ly.safe_place(ne1a, anchor=ne1_title, direction=DOWN, buff=0.35)
        self.play(Write(ne1a), run_time=NORMAL)
        self.wait(0.2)

        ne1b = MathTex(
            r"\text{Inverse: } 2^{-1} = \tfrac{1}{2} \notin \mathbb{Z} \;\textbf{FAILS!}",
            color=RED, font_size=26,
        )
        self.ly.safe_place(ne1b, anchor=ne1a, direction=DOWN, buff=0.35)
        self.play(Write(ne1b), run_time=NORMAL)
        self.wait(0.2)

        note1 = Text(
            "One failed axiom disqualifies it.",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(note1, anchor=ne1b, direction=DOWN, buff=0.35)
        self.play(FadeIn(note1, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

        title2 = self.ly.title("What Is NOT a Group? (cont.)")

        ne2_title = MathTex(
            r"\text{Non-example: } (\mathbb{Z},\, -)",
            color=ACCENT, font_size=30,
        )
        self.ly.safe_place(ne2_title, anchor=title2, direction=DOWN, buff=0.5)
        self.play(Write(ne2_title), run_time=NORMAL)
        self.wait(0.3)

        ne2a = MathTex(r"(5 - 3) - 2 = 0", color=PRIMARY, font_size=30)
        self.ly.safe_place(ne2a, anchor=ne2_title, direction=DOWN, buff=0.4)
        self.play(Write(ne2a), run_time=NORMAL)
        self.wait(0.2)

        ne2b = MathTex(r"5 - (3 - 2) = 4", color=SECONDARY, font_size=30)
        self.ly.safe_place(ne2b, anchor=ne2a, direction=DOWN, buff=0.4)
        self.play(Write(ne2b), run_time=NORMAL)
        self.wait(0.2)

        fail = MathTex(
            r"0 \neq 4 \implies \text{Associativity FAILS}",
            color=RED, font_size=28,
        )
        self.ly.safe_place(fail, anchor=ne2b, direction=DOWN, buff=0.4)
        self.play(Write(fail), run_time=NORMAL)
        self.wait(20.5)  # pacing: extends previous caption slot

        self.ly.clear()

    # --- Scene 7: Abelian ---

    def scene7_abelian(self):
        self.add_subcaption(
            "Here is the surprising part. "
            "The group axioms never required a star b to equal b star a. "
            "When the operation commutes for all elements, "
            "we call the group abelian, named after Niels Henrik Abel. "
            "The integers under addition are abelian. "
            "But the symmetries of a triangle are not. "
            "Rotating then reflecting gives a different result than reflecting then rotating. "
            "Matrix multiplication and Rubik's cube moves are also non-abelian.",
            duration=34.7,  # pacing: 1.25x natural TTS slot
        )

        title = self.ly.title("Abelian Groups")

        defn = MathTex(
            r"G \text{ is } \mathbf{abelian} \iff a * b = b * a \;\forall\, a,b \in G",
            color=ACCENT, font_size=30,
        )
        self.ly.safe_place(defn, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(0.3)

        ab_ex = MathTex(
            r"(\mathbb{Z}, +)\text{ is abelian: } a+b = b+a\; \checkmark",
            color=SECONDARY, font_size=28,
        )
        self.ly.safe_place(ab_ex, anchor=defn, direction=DOWN, buff=0.5)
        self.play(Write(ab_ex), run_time=NORMAL)
        self.wait(0.3)

        nab_title = Text(
            "Symmetries of a triangle: NOT abelian",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(nab_title, anchor=ab_ex, direction=DOWN, buff=0.5)
        self.play(FadeIn(nab_title, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        comp1 = MathTex(
            r"\text{rotate then reflect} \neq \text{reflect then rotate}",
            color=WHITE, font_size=24,
        )
        self.ly.safe_place(comp1, anchor=nab_title, direction=DOWN, buff=0.35)
        self.play(Write(comp1), run_time=NORMAL)
        self.wait(0.3)

        others = Text(
            "Also non-abelian: matrix multiplication, Rubik's cube, permutations",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(others, anchor=comp1, direction=DOWN, buff=0.35)
        self.play(FadeIn(others, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        hist = Text(
            "Named after Niels Henrik Abel (1802 - 1829)",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(hist, anchor=others, direction=DOWN, buff=0.3)
        self.play(FadeIn(hist, shift=LEFT * 0.15), run_time=FAST)
        self.wait(27.0)  # pacing: extends previous caption slot

        self.ly.clear()

    # --- Scene 8: Big Picture ---

    def scene8_big_picture(self):
        self.add_subcaption(
            "Why do groups matter? "
            "Because they unify seemingly different structures under one framework. "
            "Integers, symmetries, matrices, permutations, "
            "and polynomials all share the same algebraic DNA. "
            "When you prove a theorem about groups, "
            "it applies to all of these at once. "
            "That is the power of abstraction. "
            "Next time we will look at subgroups.",
            duration=27.6,  # pacing: 1.25x natural TTS slot
        )

        title = self.ly.title("Why Groups Matter")

        unified = Text(
            "Groups unify: integers, symmetries, matrices, permutations",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(unified, anchor=title, direction=DOWN, buff=0.6)
        self.play(FadeIn(unified, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        power = Text(
            "Prove one theorem about groups = apply to ALL of these",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(power, anchor=unified, direction=DOWN, buff=0.5)
        self.play(FadeIn(power, scale=1.05), run_time=NORMAL)
        self.wait(0.3)

        abstract = Text(
            "This is the power of abstraction.",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(abstract, anchor=power, direction=DOWN, buff=0.5)
        self.play(FadeIn(abstract, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        preview_title = Text(
            "Coming Up in Abstract Algebra I:",
            font_size=HEADING_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(preview_title, anchor=abstract, direction=DOWN, buff=0.6)
        self.play(Write(preview_title), run_time=FAST)
        self.wait(0.2)

        roadmap = Text(
            "Subgroups -> Cyclic Groups -> Permutations -> "
            "Cosets -> Homomorphisms -> Quotients -> Rings & Fields",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(roadmap, anchor=preview_title, direction=DOWN, buff=0.3)
        self.play(FadeIn(roadmap, shift=LEFT * 0.15), run_time=FAST)
        self.wait(21.5)  # pacing: extends previous caption slot

        self.ly.clear()

    # --- Scene 9: Summary ---

    def scene9_summary(self):
        self.add_subcaption(
            "Let us recap what we learned today. "
            "A group is a set with an operation satisfying closure, "
            "associativity, identity, and inverse. "
            "Examples include the integers under addition, "
            "integers modulo n, and the symmetries of a triangle. "
            "Non-examples fail at least one axiom. "
            "And abelian groups are commutative, "
            "while non-abelian groups are common and important. "
            "This is the foundation of abstract algebra. "
            "Thanks for watching!",
            duration=35.6,  # pacing: 1.25x natural TTS slot
        )

        title = self.ly.title("Summary")

        takeaways = [
            Text("1. A group = set + operation + 4 axioms", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Examples: (Z, +), (Z_n, +), symmetries", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("3. Non-examples fail at least one axiom", font_size=BODY_SIZE, color=RED, font=SANS),
            Text("4. Abelian = commutative; non-abelian is common", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]

        self.ly.progressive_reveal(takeaways, start_from=title, run_time=0.6)
        self.wait(0.3)

        closing = Text(
            "You now know what a group is!",
            font_size=HEADING_SIZE, color=WHITE, font=SANS, weight=BOLD,
        )
        self.ly.safe_place(closing, anchor=takeaways[-1], direction=DOWN, buff=0.5)
        self.play(FadeIn(closing, scale=1.05), run_time=NORMAL)
        self.wait(24.8)  # pacing: extends previous caption slot

        play_outro(self, "Groups: Definition and Examples", "Abstract Algebra I")