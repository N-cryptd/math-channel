"""Video 119: Group Actions
TEMPLATE v2 -- Professional quality Manim script

Playlist: Abstract Algebra I (Video 9 of 12)
Class: Video119_GroupActions

Topics: group action definition, orbits, stabilizers, orbit-stabilizer theorem,
         examples (rotation of polygon, permutation action), Cayley's theorem.

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


class Video119_GroupActions(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_polygon_example()
        self.scene4_orbits()
        self.scene5_stabilizers()
        self.scene6_orbit_stabilizer()
        self.scene7_cayley()
        self.scene8_summary()

    # --- Scene 1: Hook ---
    # Narration ~33s.

    def scene1_hook(self):
        self.add_subcaption(
            "Groups do not just exist in the abstract. They act on things. "
            "When a dihedral group rotates a pentagon, "
            "each group element performs a specific transformation. "
            "A rotation sends vertex 1 to vertex 2. A reflection flips the shape. "
            "This is a group action: a group moving the elements of a set. "
            "Today we will define group actions, explore orbits and stabilizers, "
            "and prove one of the most useful counting tools in group theory: "
            "the orbit-stabilizer theorem. "
            "This is Abstract Algebra, Video 9.",
            duration=33,
        )
        play_intro(self, "Group Actions", "Abstract Algebra I")

        title = self.ly.title("Groups Don't Just Exist -- They Act")
        self.wait(2)

        items = [
            Text("Rotation sends vertex 1 to vertex 2", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Reflection flips the shape", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Group action = a group moving elements of a set", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(5)

        # Teaser formula
        teaser = MathTex(
            r"|G| = |\mathrm{Orb}(x)| \times |\mathrm{Stab}(x)|",
            color=WHITE, font_size=36,
        )
        boxed = self.ly.formula_box(teaser, color=ACCENT)
        self.play(FadeOut(items[0]), run_time=FAST)
        self.ly.safe_place(boxed, anchor=items[-1], direction=DOWN, buff=0.5)
        self.play(Write(teaser), Create(boxed[1]), run_time=NORMAL)
        self.wait(6)

        self.ly.clear()

    # --- Scene 2: Definition of Group Action ---
    # Narration ~55s.

    def scene2_definition(self):
        self.add_subcaption(
            "A group action is a formal way to describe a group moving the elements of a set. "
            "We say a group G acts on a set X "
            "if there is a map from G cross X to X "
            "satisfying two conditions. "
            "First, the identity fixes everything: e dot x equals x. "
            "Second, compatibility: g times h acting on x "
            "equals g acting on h acting on x. "
            "Think of it as a switchboard: "
            "each group element is a button that permutes the elements of X, "
            "and pressing the a button then the b button "
            "gives the same result as pressing the ab button. "
            "There is an equivalent viewpoint using homomorphisms. "
            "A group action of G on X is exactly a homomorphism "
            "phi from G to Sym of X, the group of permutations of X. "
            "This connects group actions to what we learned about homomorphisms in Video 6. "
            "Notation: we write g dot x for the element that g sends x to.",
            duration=55,
        )

        title = self.ly.title("Definition of a Group Action")
        self.wait(2)

        # Set up
        sets = MathTex(
            r"G \text{ acts on } X",
            color=WHITE, font_size=32,
        )
        self.ly.safe_place(sets, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(sets), run_time=NORMAL)
        self.wait(3)

        # Conditions
        cond1 = MathTex(
            r"e \cdot x = x",
            color=PRIMARY, font_size=30,
        )
        cond1_label = Text("identity fixes everything", font_size=SMALL_SIZE, color=PRIMARY, font=SANS)
        g1 = VGroup(cond1, cond1_label).arrange(DOWN, buff=0.15)

        cond2 = MathTex(
            r"(gh) \cdot x = g \cdot (h \cdot x)",
            color=SECONDARY, font_size=30,
        )
        cond2_label = Text("compatibility with group operation", font_size=SMALL_SIZE, color=SECONDARY, font=SANS)
        g2 = VGroup(cond2, cond2_label).arrange(DOWN, buff=0.15)

        self.ly.safe_place(g1, anchor=sets, direction=DOWN, buff=0.4)
        self.ly.safe_place(g2, anchor=g1, direction=DOWN, buff=0.3)
        self.play(Write(cond1), run_time=NORMAL)
        self.ly.safe_place(cond1_label, anchor=cond1, direction=DOWN, buff=0.15)
        self.play(FadeIn(cond1_label, shift=LEFT * 0.1), run_time=FAST)
        self.wait(4)
        self.play(Write(cond2), run_time=NORMAL)
        self.ly.safe_place(cond2_label, anchor=cond2, direction=DOWN, buff=0.15)
        self.play(FadeIn(cond2_label, shift=LEFT * 0.1), run_time=FAST)
        self.wait(6)

        # Switchboard metaphor
        switch_text = Text(
            "\"Switchboard\": each g permutes the elements of X",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.play(FadeOut(sets), FadeOut(g1), FadeOut(g2), run_time=FAST)
        self.ly.safe_place(switch_text, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(switch_text), run_time=NORMAL)
        self.wait(8)

        # Homomorphism viewpoint
        homo = MathTex(
            r"\phi : G \to \mathrm{Sym}(X)",
            color=WHITE, font_size=32,
        )
        homo_label = Text("action = homomorphism (Video 6)", font_size=SMALL_SIZE, color=DIM, font=SANS)
        hg = VGroup(homo, homo_label).arrange(DOWN, buff=0.15)
        self.play(FadeOut(switch_text), run_time=FAST)
        self.ly.safe_place(hg, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(homo), run_time=NORMAL)
        self.ly.safe_place(homo_label, anchor=homo, direction=DOWN, buff=0.15)
        self.play(FadeIn(homo_label, shift=LEFT * 0.1), run_time=FAST)
        self.wait(8)

        # Notation
        notn = MathTex(
            r"g \cdot x \; \text{ or } \; \phi(g)(x)",
            color=WHITE, font_size=30,
        )
        self.play(FadeOut(hg), run_time=FAST)
        self.ly.safe_place(notn, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(notn), run_time=NORMAL)
        self.wait(6)

        self.ly.clear()

    # --- Scene 3: Dihedral Group Acting on Polygon ---
    # Narration ~55s.

    def scene3_polygon_example(self):
        self.add_subcaption(
            "Let us see a concrete example. "
            "The dihedral group D_5 has order 10 and consists of 5 rotations and 5 reflections of a regular pentagon. "
            "D_5 acts on the set of vertices 1 through 5. "
            "The rotation r sends vertex 1 to 2, vertex 2 to 3, and so on. "
            "The reflection s sends vertex 1 to 5, vertex 2 to 4, and fixes no vertex. "
            "Each group element is a permutation of the 5 vertices. "
            "The identity rotation fixes all vertices, and the composition of two rotations is another rotation. "
            "This is exactly what the two axioms require. "
            "The key insight is that a single group can act on many different sets. "
            "D_5 acts on vertices, on edges, on diagonals, on the whole pentagon itself. "
            "Each action reveals different structure about the group.",
            duration=55,
        )

        self.ly.section_divider(1, "Example: D_5 on a Pentagon")
        self.wait(2)

        title = self.ly.title("Dihedral Group D_5 Acting on Vertices")
        self.wait(2)

        # Draw pentagon
        pentagon = RegularPolygon(n=5, radius=1.8, color=PRIMARY, stroke_width=2.5)
        self.ly.center_in_content(pentagon)
        self.play(Create(pentagon), run_time=NORMAL)

        # Label vertices
        vertex_labels = VGroup()
        for i in range(5):
            angle = PI / 2 - i * 2 * PI / 5
            pos = np.array([1.8 * np.cos(angle), 1.8 * np.sin(angle), 0])
            label = Text(str(i + 1), font_size=BODY_SIZE, color=WHITE, font=SANS)
            label.move_to(pos + np.array([0.4 * np.cos(angle), 0.4 * np.sin(angle), 0]))
            vertex_labels.add(label)
        self.play(*[FadeIn(l) for l in vertex_labels], run_time=FAST)
        self.wait(3)

        # Show rotation arrow
        rot_label = Text(
            "rotation r: 1 -> 2 -> 3 -> 4 -> 5 -> 1",
            font_size=LABEL_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(rot_label, anchor=pentagon, direction=DOWN, buff=0.6)
        self.play(Write(rot_label), run_time=NORMAL)
        self.wait(5)

        # Rotation animation
        pent_copy = pentagon.copy()
        rotated = Rotate(pent_copy, angle=-2 * PI / 5, about_point=ORIGIN)
        rot_label_new = Text(
            "Each rotation cycles the vertices",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(rot_label_new, anchor=rot_label, direction=DOWN, buff=0.3)
        self.play(rotated, run_time=NORMAL)
        self.play(FadeOut(pent_copy), run_time=FAST)
        self.play(Write(rot_label_new), run_time=FAST)
        self.wait(6)

        # Reflection
        refl_label = Text(
            "Reflection s: 1 <-> 5, 2 <-> 4, fixes 3",
            font_size=LABEL_SIZE, color=RED, font=SANS,
        )
        self.play(FadeOut(rot_label), FadeOut(rot_label_new), run_time=FAST)
        self.ly.safe_place(refl_label, anchor=pentagon, direction=DOWN, buff=0.6)
        self.play(Write(refl_label), run_time=NORMAL)
        self.wait(5)

        # Key insight
        key = Text(
            "One group, many possible actions",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(key, anchor=refl_label, direction=DOWN, buff=0.3)
        self.play(FadeIn(key, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 4: Orbits ---
    # Narration ~50s.

    def scene4_orbits(self):
        self.add_subcaption(
            "Given a group action, the orbit of an element x "
            "is the set of all elements that x can be sent to by the group. "
            "Formally, the orbit of x equals the set of g dot x for all g in G. "
            "For D_5 acting on vertices, "
            "the orbit of vertex 1 is all 5 vertices, "
            "because rotations can send 1 to any other vertex. "
            "We say the action is transitive when there is only one orbit. "
            "An important fact: orbits partition the set X into disjoint pieces. "
            "Every element belongs to exactly one orbit. "
            "As an example, consider S_3 acting on the set 1 through 6, "
            "where S_3 only permutes 1, 2, 3 and leaves 4, 5, 6 fixed. "
            "Then 1, 2, 3 form one orbit, and 4, 5, 6 form another.",
            duration=50,
        )

        title = self.ly.title("Orbits")
        self.wait(2)

        # Definition
        defn = MathTex(
            r"\mathrm{Orb}(x) = \{g \cdot x : g \in G\}",
            color=WHITE, font_size=32,
        )
        boxed = self.ly.formula_box(defn, color=PRIMARY)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(defn), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        # D_5 example
        ex = Text(
            "D_5 on vertices: Orb(1) = {1,2,3,4,5}",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        trans = Text(
            "Transitive: one orbit covers everything",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(ex, anchor=boxed, direction=DOWN, buff=0.4)
        self.play(Write(ex), run_time=NORMAL)
        self.wait(3)
        self.ly.safe_place(trans, anchor=ex, direction=DOWN, buff=0.3)
        self.play(FadeIn(trans, shift=LEFT * 0.15), run_time=FAST)
        self.wait(6)

        # Partition property
        part = Text(
            "Orbits partition X into disjoint pieces",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.play(FadeOut(boxed), FadeOut(ex), FadeOut(trans), run_time=FAST)
        self.ly.safe_place(part, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(part), run_time=NORMAL)
        self.wait(4)

        # S_3 example
        s3ex = Text(
            "S_3 on {1,2,3,4,5}: Orb({1,2,3}) = {1,2,3}, Orb({4,5,6}) = {4,5,6}",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(s3ex, anchor=part, direction=DOWN, buff=0.3)
        self.play(FadeIn(s3ex, shift=LEFT * 0.15), run_time=FAST)
        self.wait(8)

        # Equivalence class note
        equiv = Text(
            "Orbits are equivalence classes: x ~ y iff y = g.x",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(equiv, anchor=s3ex, direction=DOWN, buff=0.3)
        self.play(FadeIn(equiv, shift=LEFT * 0.1), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 5: Stabilizers ---
    # Narration ~45s.

    def scene5_stabilizers(self):
        self.add_subcaption(
            "The stabilizer of an element x is the set of group elements "
            "that leave x fixed. Formally, "
            "Stab of x equals the set of g in G such that g dot x equals x. "
            "The stabilizer is always a subgroup of G. "
            "Proof: the identity fixes x, so e is in Stab of x. "
            "If g and h fix x, then gh also fixes x by compatibility. "
            "And if g fixes x, then g inverse also fixes x. "
            "For D_5 acting on vertices, "
            "the stabilizer of any vertex has order 2: just the identity and the reflection through that vertex. "
            "For D_5 acting on the whole pentagon, "
            "the stabilizer is trivial, just the identity, "
            "because no non-trivial symmetry leaves the pentagon exactly where it is.",
            duration=45,
        )

        title = self.ly.title("Stabilizers")
        self.wait(2)

        # Definition
        defn = MathTex(
            r"\mathrm{Stab}(x) = \{g \in G : g \cdot x = x\}",
            color=WHITE, font_size=32,
        )
        boxed = self.ly.formula_box(defn, color=SECONDARY)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(defn), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        # Subgroup
        sub = Text(
            "Stab(x) is always a subgroup of G",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(sub, anchor=boxed, direction=DOWN, buff=0.4)
        self.play(Write(sub), run_time=NORMAL)
        self.wait(4)

        # Proof sketch items
        proof = [
            Text("e fixes x (identity axiom)", font_size=SMALL_SIZE, color=DIM, font=SANS),
            Text("g,h fix x => gh fixes x (compatibility)", font_size=SMALL_SIZE, color=DIM, font=SANS),
            Text("g fixes x => g^-1 fixes x", font_size=SMALL_SIZE, color=DIM, font=SANS),
        ]
        self.ly.stack_down(proof, start_from=sub, spacing=0.25)
        for p in proof:
            self.play(FadeIn(p, shift=LEFT * 0.1), run_time=FAST)
            self.wait(1)
        self.wait(3)

        # Example
        ex = Text(
            "D_5 on vertices: Stab(v1) has order 2",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        ex2 = Text(
            "{e, reflection through v1}",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.play(
            FadeOut(boxed), FadeOut(sub), FadeOut(proof[0]), FadeOut(proof[1]), FadeOut(proof[2]),
            run_time=FAST,
        )
        self.ly.safe_place(ex, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(ex), run_time=NORMAL)
        self.wait(2)
        self.ly.safe_place(ex2, anchor=ex, direction=DOWN, buff=0.3)
        self.play(FadeIn(ex2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        # Interpretation
        interp = Text(
            "Stabilizer measures: how much of G doesn't move x",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(interp, anchor=ex2, direction=DOWN, buff=0.3)
        self.play(FadeIn(interp, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 6: Orbit-Stabilizer Theorem ---
    # Narration ~60s.

    def scene6_orbit_stabilizer(self):
        self.add_subcaption(
            "We now come to one of the most useful theorems in group theory. "
            "The orbit-stabilizer theorem states that "
            "for any finite group G acting on a set X, "
            "the order of G equals the size of the orbit times the size of the stabilizer. "
            "That is, |G| = |Orb of x| times |Stab of x| "
            "for any element x in X. "
            "The proof is a counting argument. "
            "Consider all elements g of G. "
            "How many of them send x to a particular target y in the orbit? "
            "If g_0 sends x to y, then every g sending x to y "
            "has the form g = h g_0 where h fixes x, so h is in Stab of x. "
            "This means each element of the orbit is hit exactly |Stab of x| times. "
            "So |G| = |Orb of x| times |Stab of x|. "
            "Let us verify with D_5 on vertices. "
            "The orbit of vertex 1 has size 5, "
            "the stabilizer has order 2, "
            "and 5 times 2 equals 10, which is |D_5|. It checks out.",
            duration=60,
        )

        self.ly.section_divider(2, "The Orbit-Stabilizer Theorem")
        self.wait(2)

        title = self.ly.title("Orbit-Stabilizer Theorem")
        self.wait(2)

        # Theorem
        theorem = MathTex(
            r"|G| = |\mathrm{Orb}(x)| \times |\mathrm{Stab}(x)|",
            color=WHITE, font_size=36,
        )
        boxed = self.ly.formula_box(theorem, color=ACCENT)
        self.ly.safe_place(boxed, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(theorem), Create(boxed[1]), run_time=NORMAL)
        self.wait(5)

        # Proof idea
        idea_title = Text(
            "Proof idea: counting argument",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(idea_title, anchor=boxed, direction=DOWN, buff=0.5)
        self.play(Write(idea_title), run_time=NORMAL)
        self.wait(3)

        idea_steps = [
            Text("Each y in Orb(x) is hit by |Stab(x)| elements of G", font_size=SMALL_SIZE, color=WHITE, font=SANS),
            Text("If g0.x = y, then g.x = y iff g = h*g0 for h in Stab(x)", font_size=SMALL_SIZE, color=WHITE, font=SANS),
            Text("Total: |G| = |Orb(x)| * |Stab(x)|", font_size=SMALL_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.stack_down(idea_steps, start_from=idea_title, spacing=0.25)
        for s in idea_steps:
            self.play(FadeIn(s, shift=LEFT * 0.1), run_time=FAST)
            self.wait(2)
        self.wait(5)

        # Verification
        ver = Text(
            "Verify: D_5 on vertices",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.play(
            FadeOut(boxed), FadeOut(idea_title),
            FadeOut(idea_steps[0]), FadeOut(idea_steps[1]), FadeOut(idea_steps[2]),
            run_time=FAST,
        )
        self.ly.safe_place(ver, anchor=title, direction=DOWN, buff=0.6)
        self.play(Write(ver), run_time=NORMAL)
        self.wait(3)

        check = MathTex(
            r"|\mathrm{Orb}(v_1)| = 5, \quad |\mathrm{Stab}(v_1)| = 2, \quad 5 \times 2 = 10 = |D_5|",
            color=WHITE, font_size=28,
        )
        self.ly.safe_place(check, anchor=ver, direction=DOWN, buff=0.3)
        self.play(Write(check), run_time=NORMAL)
        self.wait(5)

        checkmark = Text(
            "The theorem checks out!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(checkmark, anchor=check, direction=DOWN, buff=0.3)
        self.play(FadeIn(checkmark, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 7: Permutation Action and Cayley's Theorem ---
    # Narration ~55s.

    def scene7_cayley(self):
        self.add_subcaption(
            "Every group has a natural action on itself by left multiplication. "
            "Define g dot x equals g times x, using the group operation. "
            "This is an action because e times x equals x, "
            "and gh times x equals g times h times x by associativity. "
            "The orbit of any element is the whole group, so the action is transitive. "
            "The stabilizer of any x is just the identity element, "
            "because g times x equals x only when g equals e. "
            "So orbit-stabilizer gives |G| = |G| times 1, which is trivial. "
            "But this action leads to a deep result: Cayley's theorem. "
            "Each group element g defines a permutation of G via left multiplication. "
            "This gives a homomorphism from G to Sym of G, "
            "which is injective because only the identity fixes every element. "
            "Therefore every group G is isomorphic to a subgroup of a symmetric group. "
            "Cayley's theorem answers a fundamental question: "
            "all groups are symmetry groups of some set.",
            duration=55,
        )

        title = self.ly.title("Permutation Action and Cayley's Theorem")
        self.wait(2)

        # Left multiplication action
        action = MathTex(
            r"g \cdot x = gx \qquad (\text{left multiplication})",
            color=WHITE, font_size=30,
        )
        self.ly.safe_place(action, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(action), run_time=NORMAL)
        self.wait(4)

        # Orbit/stab facts
        orbit_fact = Text(
            "Orbit of any x = all of G (transitive action)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        stab_fact = Text(
            "Stabilizer of any x = {e} (trivial)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(orbit_fact, anchor=action, direction=DOWN, buff=0.3)
        self.play(Write(orbit_fact), run_time=FAST)
        self.wait(3)
        self.ly.safe_place(stab_fact, anchor=orbit_fact, direction=DOWN, buff=0.3)
        self.play(Write(stab_fact), run_time=FAST)
        self.wait(5)

        # Cayley's theorem
        cayley_label = Text(
            "Cayley's Theorem",
            font_size=HEADING_SIZE, color=ACCENT, font=SANS,
        )
        cayley = MathTex(
            r"G \cong \text{subgroup of } S_{|G|}",
            color=WHITE, font_size=32,
        )
        self.play(
            FadeOut(action), FadeOut(orbit_fact), FadeOut(stab_fact),
            run_time=FAST,
        )
        self.ly.safe_place(cayley_label, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(cayley_label), run_time=NORMAL)
        self.wait(2)

        cayley_boxed = self.ly.formula_box(cayley, color=ACCENT)
        self.ly.safe_place(cayley_boxed, anchor=cayley_label, direction=DOWN, buff=0.4)
        self.play(Write(cayley), Create(cayley_boxed[1]), run_time=NORMAL)
        self.wait(6)

        # Payoff
        payoff = Text(
            "Every group is a symmetry group of some set!",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(payoff, anchor=cayley_boxed, direction=DOWN, buff=0.4)
        self.play(FadeIn(payoff, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)

        # Connection
        connect = Text(
            "Homomorphism phi: G -> Sym(G) is injective",
            font_size=SMALL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(connect, anchor=payoff, direction=DOWN, buff=0.3)
        self.play(FadeIn(connect, shift=LEFT * 0.1), run_time=FAST)
        self.wait(5)

        self.ly.clear()

    # --- Scene 8: Summary ---
    # Narration ~30s.

    def scene8_summary(self):
        self.add_subcaption(
            "Let us recap what we learned today. "
            "A group action is a group moving the elements of a set, "
            "formally a map from G cross X to X satisfying identity and compatibility. "
            "Every action determines orbits, which partition the set, "
            "and stabilizers, which are always subgroups. "
            "The orbit-stabilizer theorem tells us that "
            "|G| = |Orb of x| times |Stab of x|, "
            "a powerful counting tool. "
            "Finally, Cayley's theorem shows every group is a subgroup of a symmetric group. "
            "Next time, we will use group actions to prove the Sylow theorems, "
            "which count subgroups of prime power order. "
            "This is Abstract Algebra, Video 9.",
            duration=30,
        )

        title = self.ly.title("Summary")
        self.wait(2)

        items = [
            Text("Group action: G acts on X with identity + compatibility", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Orbits partition X into disjoint pieces", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Stabilizers are always subgroups", font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title, run_time=0.8)
        self.wait(5)

        # Key formula
        key = MathTex(
            r"|G| = |\mathrm{Orb}(x)| \times |\mathrm{Stab}(x)|",
            color=ACCENT, font_size=36,
        )
        boxed = self.ly.formula_box(key, color=ACCENT)
        self.ly.safe_place(boxed, anchor=items[-1], direction=DOWN, buff=0.4)
        self.play(Write(key), Create(boxed[1]), run_time=NORMAL)
        self.wait(4)

        # Cayley recap
        cayley_recap = Text(
            "Cayley: every group is a subgroup of S_n",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(cayley_recap, anchor=boxed, direction=DOWN, buff=0.4)
        self.play(FadeIn(cayley_recap, shift=LEFT * 0.15), run_time=FAST)
        self.wait(4)

        self.ly.clear()

        # Tease next
        self.add_subcaption(
            "Next time: the Sylow theorems.",
            duration=3,
        )
        tease = self.ly.title("Next: Sylow Theorems")
        self.wait(3)
        self.ly.clear()

        play_outro(self)
