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


class Video217_GroupActions(Scene):
    """Group Actions: when groups move things around."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_d4_example()
        self.scene4_orbits()
        self.scene5_stabilizers()
        self.scene6_orbit_stabilizer()
        self.scene7_visual_proof()
        self.scene8_conjugation()
        self.scene9_conjugation_s3()
        self.scene10_class_equation()
        self.scene11_coset_action()
        self.scene12_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "We have studied groups as abstract algebraic structures. "
            "Today we give groups something to act upon. When a group "
            "acts on a set, every group element becomes a symmetry or "
            "permutation of that set. This is the concept of a group action.",
            duration=24,
        )
        play_intro(self, "Group Actions", "Advanced Abstract Algebra")
        title = self.ly.title("When Groups Move Things")
        items = [
            Text("Rotations and reflections permute a square", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Every group element becomes a transformation", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Orbits, stabilizers, and the class equation", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(8)
        self.ly.clear()

    def scene2_definition(self):
        self.add_subcaption(
            "A group G acts on a set X if there is a map from G "
            "cross X to X satisfying two axioms. First, the identity "
            "element e of G fixes every point: e dot x equals x. "
            "Second, the action is compatible with the group operation: "
            "g acting on h acting on x equals g h acting on x.",
            duration=26,
        )
        self.ly.section_divider(1, "Definition")
        title = self.ly.title("Group Action: Formal Definition")
        map_def = MathTex(
            r"G \times X \to X, \quad (g, x) \mapsto g \cdot x",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(map_def, DOWN, anchor=title, buff=0.5)
        self.play(Write(map_def), run_time=NORMAL)
        self.wait(3)
        axiom1 = MathTex(
            r"e \cdot x = x \quad \text{(identity)}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(axiom1, DOWN, anchor=map_def, buff=0.4)
        self.play(Write(axiom1), run_time=FAST)
        self.wait(2)
        axiom2 = MathTex(
            r"g \cdot (h \cdot x) = (gh) \cdot x \quad \text{(compat)}",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(axiom2, DOWN, anchor=axiom1, buff=0.4)
        self.play(Write(axiom2), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene3_d4_example(self):
        self.add_subcaption(
            "Our running example: the dihedral group D 4, the symmetry "
            "group of a square, acts on the four vertices labeled 1, 2, "
            "3, 4. The rotation r sends vertex 1 to 2, 2 to 3, 3 to 4, "
            "and 4 back to 1. The reflection s across the vertical axis "
            "swaps 1 with 2 and 3 with 4.",
            duration=26,
        )
        self.ly.section_divider(2, "Running Example")
        title = self.ly.title("D_4 Acts on Square Vertices")
        perm_r = MathTex(
            r"r \mapsto (1\; 2\; 3\; 4), \quad s \mapsto (1\; 2)(3\; 4)",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(perm_r, DOWN, anchor=title, buff=0.5)
        self.play(Write(perm_r), run_time=NORMAL)
        self.wait(3)
        verify = Text(
            "r(s(1)) = r(2) = 3 = (rs)(1)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(verify, DOWN, anchor=perm_r, buff=0.5)
        self.play(FadeIn(verify, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        check = Text(
            "Compatibility axiom verified!",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(check, DOWN, anchor=verify, buff=0.4)
        self.play(FadeIn(check, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene4_orbits(self):
        self.add_subcaption(
            "Given a group action, the orbit of a point x is the set of "
            "all points that x can reach under the action. Formally, "
            "Orb of x equals the set of g dot x for all g in G. "
            "Being in the same orbit is an equivalence relation on X, "
            "so the orbits form a partition of the set.",
            duration=26,
        )
        self.ly.section_divider(3, "Orbits")
        title = self.ly.title("The Orbit of a Point")
        defn = MathTex(
            r"\operatorname{Orb}(x) = \{g \cdot x : g \in G\}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(defn, DOWN, anchor=title, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(3)
        items = [
            Text("Orbits partition X into equivalence classes", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("In D_4: Orb(1) = {1,2,3,4}  (transitive!)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        visible = []
        for item in items:
            anchor = visible[-1] if visible else defn
            self.ly.safe_place(item, DOWN, anchor=anchor, buff=0.4)
            self.play(FadeIn(item, shift=LEFT * 0.15), run_time=FAST)
            visible.append(item)
            self.wait(2)
        self.wait(5)
        self.ly.clear()

    def scene5_stabilizers(self):
        self.add_subcaption(
            "The stabilizer of a point x is the set of all group elements "
            "that fix x. Formally, Stab of x equals the set of g in G "
            "such that g dot x equals x. The stabilizer is always a "
            "subgroup of G. In our example, Stab of vertex 1 in D 4 has "
            "order 2: only the identity and one diagonal reflection.",
            duration=26,
        )
        self.ly.section_divider(4, "Stabilizers")
        title = self.ly.title("The Stabilizer Subgroup")
        defn = MathTex(
            r"\operatorname{Stab}(x) = \{g \in G : g \cdot x = x\} \leq G",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(defn, DOWN, anchor=title, buff=0.5)
        self.play(Write(defn), run_time=NORMAL)
        self.wait(3)
        example = Text(
            "In D_4: Stab(v1) = {e, diagonal reflection}  =>  |Stab| = 2",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(example, DOWN, anchor=defn, buff=0.5)
        self.play(FadeIn(example, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        note = Text(
            "|Orb(1)| = 4,  |Stab(1)| = 2,  |D_4| = 8",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=example, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene6_orbit_stabilizer(self):
        self.add_subcaption(
            "Notice that in our example, the product of the orbit size "
            "and the stabilizer size equals the group order. This is no "
            "coincidence. The orbit-stabilizer theorem states that for any "
            "finite group G acting on X, the size of the orbit of x "
            "times the size of the stabilizer of x equals |G|.",
            duration=26,
        )
        self.ly.section_divider(5, "Orbit-Stabilizer Theorem")
        title = self.ly.title("The Orbit-Stabilizer Theorem")
        formula = MathTex(
            r"|G| = |\operatorname{Orb}(x)| \cdot |\operatorname{Stab}(x)|",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(formula, color=PRIMARY)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed), run_time=NORMAL)
        self.wait(3)
        check = Text(
            "D_4 example: 8 = 4 x 2   (verified!)",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(check, DOWN, anchor=boxed, buff=0.5)
        self.play(FadeIn(check, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene7_visual_proof(self):
        self.add_subcaption(
            "The proof constructs a bijection between the cosets of the "
            "stabilizer and the orbit. Define a map from G to the orbit "
            "by sending g to g dot x. This map is surjective. "
            "The fiber over g dot x is exactly the coset g times Stab of x. "
            "Each fiber has the same size: |Stab of x|. "
            "So |G| equals |Orb of x| times |Stab of x|.",
            duration=28,
        )
        title = self.ly.title("Proof: Cosets <-> Orbit")
        phi = MathTex(
            r"\varphi : G \to \operatorname{Orb}(x), \quad g \mapsto g \cdot x",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(phi, DOWN, anchor=title, buff=0.5)
        self.play(Write(phi), run_time=NORMAL)
        self.wait(3)
        fiber = MathTex(
            r"\varphi^{-1}(g \cdot x) = g \cdot \operatorname{Stab}(x)",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(fiber, DOWN, anchor=phi, buff=0.4)
        self.play(Write(fiber), run_time=NORMAL)
        self.wait(2)
        conclusion = Text(
            "Each fiber has |Stab(x)| elements, so |G| = |Orb(x)| x |Stab(x)|",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(conclusion, DOWN, anchor=fiber, buff=0.4)
        self.play(FadeIn(conclusion, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)
        self.ly.clear()

    def scene8_conjugation(self):
        self.add_subcaption(
            "A group can act on itself by conjugation: g acts on x by "
            "g x g inverse. The two axioms are easy to verify. "
            "The orbits of the conjugation action are called conjugacy "
            "classes, and the stabilizer of an element x is its centralizer, "
            "the set of all elements that commute with x.",
            duration=24,
        )
        self.ly.section_divider(6, "Conjugation Action")
        title = self.ly.title("G Acts on Itself by Conjugation")
        action = MathTex(
            r"g \cdot x = gxg^{-1}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(action, DOWN, anchor=title, buff=0.5)
        self.play(Write(action), run_time=NORMAL)
        self.wait(3)
        items = [
            Text("Orbits = conjugacy classes Cl(x)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Stabilizer = centralizer C_G(x)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        visible = []
        for item in items:
            anchor = visible[-1] if visible else action
            self.ly.safe_place(item, DOWN, anchor=anchor, buff=0.4)
            self.play(FadeIn(item, shift=LEFT * 0.15), run_time=FAST)
            visible.append(item)
            self.wait(2)
        self.wait(5)
        self.ly.clear()

    def scene9_conjugation_s3(self):
        self.add_subcaption(
            "Let us work out the conjugacy classes of S 3, the symmetric "
            "group on 3 elements. The identity e forms its own class. "
            "The three transpositions (1 2), (1 3), (2 3) form one class "
            "because they are all conjugate to each other. "
            "The two 3-cycles (1 2 3) and (1 3 2) form another class.",
            duration=26,
        )
        title = self.ly.title("Conjugacy Classes of S_3")
        classes = MathTex(
            r"\{e\}, \quad \{(12),(13),(23)\}, \quad \{(123),(132)\}",
            font_size=BODY_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(classes, DOWN, anchor=title, buff=0.5)
        self.play(Write(classes), run_time=NORMAL)
        self.wait(3)
        note = Text(
            "Class sizes: 1 + 3 + 2 = 6 = |S_3|",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, DOWN, anchor=classes, buff=0.5)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)
        sizes = Text(
            "Each size divides |S_3| (orbit-stabilizer!)",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(sizes, DOWN, anchor=note, buff=0.4)
        self.play(FadeIn(sizes, shift=LEFT * 0.15), run_time=FAST)
        self.wait(5)
        self.ly.clear()

    def scene10_class_equation(self):
        self.add_subcaption(
            "Applying the orbit-stabilizer theorem to the conjugation action "
            "gives the class equation. The group order equals the size "
            "of the center plus the sum of the sizes of the non-central "
            "conjugacy classes. Each class size equals the index of a "
            "centralizer, so it divides |G|. The class equation is the "
            "starting point for the Sylow theorems.",
            duration=26,
        )
        self.ly.section_divider(7, "Class Equation")
        title = self.ly.title("The Class Equation")
        formula = MathTex(
            r"|G| = |Z(G)| + \sum_{i} [G : C_G(x_i)]",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(formula, color=PRIMARY)
        self.ly.safe_place(boxed, DOWN, anchor=title, buff=0.5)
        self.play(FadeIn(boxed), run_time=NORMAL)
        self.wait(3)
        items = [
            Text("Z(G) = center = elements conjugate only to themselves", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Each [G:C_G(x_i)] divides |G| and is > 1", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Foundation for Sylow theorems (next video!)", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.wait(5)
        self.ly.clear()

    def scene11_coset_action(self):
        self.add_subcaption(
            "Finally, a group G acts on the set of left cosets G over H "
            "by left multiplication: g acts on aH to give gaH. This action "
            "is always transitive: any coset can reach any other. "
            "The kernel of this action is the intersection of all conjugates "
            "of H, which is the largest normal subgroup of G contained in H.",
            duration=26,
        )
        self.ly.section_divider(8, "Coset Action")
        title = self.ly.title("Action on Left Cosets")
        action = MathTex(
            r"g \cdot (aH) = (ga)H",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(action, DOWN, anchor=title, buff=0.5)
        self.play(Write(action), run_time=NORMAL)
        self.wait(3)
        items = [
            Text("This action is always transitive", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Kernel = intersection of all conjugates of H", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        visible = []
        for item in items:
            anchor = visible[-1] if visible else action
            self.ly.safe_place(item, DOWN, anchor=anchor, buff=0.4)
            self.play(FadeIn(item, shift=LEFT * 0.15), run_time=FAST)
            visible.append(item)
            self.wait(2)
        self.wait(5)
        self.ly.clear()

    def scene12_summary(self):
        self.add_subcaption(
            "Let us recap. A group action is a map from G cross X to X "
            "satisfying the identity and compatibility axioms. The orbit "
            "of a point is everywhere it can be sent, and the stabilizer "
            "is everything that fixes it. The orbit-stabilizer theorem "
            "relates their sizes. Conjugation gives the class equation, "
            "and the coset action connects to normal subgroups. "
            "Next time, we tackle the Sylow theorems!",
            duration=30,
        )
        self.ly.section_divider(9, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Group action: G x X -> X with identity + compatibility", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Orbit-Stabilizer: |G| = |Orb(x)| x |Stab(x)|", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Conjugation -> conjugacy classes + class equation", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Coset action: transitive, kernel = core of H", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(5)
        self.ly.clear()

        self.add_subcaption(
            "Next time: the Sylow theorems! Thank you for watching.",
            duration=8,
        )
        play_outro(self, "Sylow Theorems", "Advanced Abstract Algebra")
