"""Video 116: Group Homomorphisms
TEMPLATE v2 -- Professional quality Manim script

Playlist: Abstract Algebra I (Video 6 of 12)
Class: Video116_GroupHomomorphisms

Quality Rules (mandatory):
1. Max 5 visible elements per scene at any time
2. Use LayoutEngine for ALL positioning — no manual .shift() or .to_edge()
3. Progressive disclosure: add items one at a time
4. Each add_subcaption() duration ≈ words / 2.5 seconds (12 words ≈ 5s)
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
from layout import LayoutEngine, ensure_fits


class Video116_GroupHomomorphisms(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_definition()
        self.scene3_examples()
        self.scene4_properties()
        self.scene5_kernel()
        self.scene6_image()
        self.scene7_kernel_normal()
        self.scene8_summary()

    # --- Scene 1: Hook — Structure-Preserving Maps ---

    def scene1_hook(self):
        self.add_subcaption(
            "In the last video, we built new groups from old ones "
            "using quotient groups. "
            "Now we ask a different question. "
            "How do we COMPARE two groups? "
            "We need a function between groups that respects their structure. "
            "Such a function is called a homomorphism. "
            "If a times b equals c in G, "
            "then phi of a times phi of b equals phi of c in H. "
            "The operation commutes with the function.",
            duration=30,
        )
        play_intro(self, "Group Homomorphisms", "Abstract Algebra I")

        title = self.ly.title("Structure-Preserving Maps Between Groups")

        items = [
            Text("We have functions between SETS...", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("...but what about functions between GROUPS?", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("A homomorphism respects the group operation", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)

        # Show the key property
        self.wait(0.3)
        key_prop = MathTex(
            r"\varphi(ab) = \varphi(a)\,\varphi(b)",
            color=ACCENT, font_size=34,
        )
        boxed_prop = self.ly.formula_box(key_prop, color=ACCENT)
        # FadeOut oldest item to stay within 5-item budget
        self.play(FadeOut(items[0]), run_time=FAST)
        self.ly.safe_place(boxed_prop, anchor=items[-1], direction=DOWN, buff=0.5)
        self.play(Write(key_prop), Create(boxed_prop[1]), run_time=NORMAL)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 2: Formal Definition ---

    def scene2_definition(self):
        self.add_subcaption(
            "Let G and H be groups with operations written as multiplication. "
            "A function phi from G to H is called a group homomorphism "
            "if phi of a b equals phi of a times phi of b "
            "for all elements a and b in G. "
            "The order of operations matters. "
            "We multiply in G first, then apply phi. "
            "Or equivalently, we can apply phi to each element first, "
            "then multiply in H. "
            "Both paths give the same result.",
            duration=30,
        )
        self.ly.section_divider(1, "Definition")

        title = self.ly.title("Group Homomorphism — Formal Definition")

        # Main definition
        def_line1 = MathTex(
            r"\varphi : G \to H",
            color=PRIMARY, font_size=34,
        )
        def_line2 = MathTex(
            r"\text{is a homomorphism if } \varphi(ab) = \varphi(a)\,\varphi(b)",
            r"\;\forall\; a, b \in G",
            color=WHITE, font_size=26,
        )
        self.ly.safe_place(def_line1, anchor=title, direction=DOWN, buff=0.5)
        self.ly.safe_place(def_line2, anchor=def_line1, direction=DOWN, buff=0.4)
        self.play(Write(def_line1), run_time=NORMAL)
        self.play(Write(def_line2), run_time=NORMAL)
        self.wait(0.3)

        # Commutative diagram note
        note = Text(
            "Multiply in G, then map  =  Map each, then multiply in H",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, anchor=def_line2, direction=DOWN, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

        # Terminology sub-scene
        title2 = self.ly.title("Important Terminology")

        terms = [
            Text("Injective homomorphism = monomorphism", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Surjective homomorphism = epimorphism", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Bijective homomorphism = isomorphism", font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD),
        ]
        self.ly.progressive_reveal(terms, start_from=title2, run_time=0.7)
        self.wait(0.3)

        self.ly.clear()

    # --- Scene 3: Key Examples ---

    def scene3_examples(self):
        self.add_subcaption(
            "Let's look at three fundamental examples. "
            "First, the determinant map from G L of n R "
            "to the multiplicative group R star. "
            "The determinant of a product equals "
            "the product of determinants. "
            "Second, the sign map from S n "
            "to the two-element group plus minus one. "
            "Even permutations map to plus one, "
            "odd permutations to minus one. "
            "Third, the logarithm function from "
            "positive reals under multiplication "
            "to all reals under addition. "
            "Log of a b equals log of a plus log of b.",
            duration=35,
        )
        self.ly.section_divider(2, "Examples")

        title = self.ly.title("Three Fundamental Homomorphisms")

        # Example 1: Determinant
        ex1_title = Text(
            "1. Determinant Map",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        ex1_formula = MathTex(
            r"\det : GL(n, \mathbb{R}) \to \mathbb{R}^{\times}",
            color=WHITE, font_size=26,
        )
        ex1_prop = MathTex(
            r"\det(AB) = \det(A) \cdot \det(B)",
            color=SECONDARY, font_size=26,
        )
        self.ly.safe_place(ex1_title, anchor=title, direction=DOWN, buff=0.4)
        self.ly.safe_place(ex1_formula, anchor=ex1_title, direction=DOWN, buff=0.3)
        self.ly.safe_place(ex1_prop, anchor=ex1_formula, direction=DOWN, buff=0.3)
        self.play(FadeIn(ex1_title, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(ex1_formula), Write(ex1_prop), run_time=NORMAL)
        self.wait(0.3)

        # Transition: remove ex1, show ex2
        self.play(
            FadeOut(ex1_title), FadeOut(ex1_formula), FadeOut(ex1_prop),
            run_time=FAST,
        )
        self.wait(0.2)

        # Example 2: Sign map
        ex2_title = Text(
            "2. Sign Map (Parity)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        ex2_formula = MathTex(
            r"\operatorname{sgn} : S_n \to \{+1, -1\}",
            color=WHITE, font_size=26,
        )
        ex2_prop = MathTex(
            r"\operatorname{sgn}(\sigma \tau) = \operatorname{sgn}(\sigma) \cdot \operatorname{sgn}(\tau)",
            color=SECONDARY, font_size=24,
        )
        self.ly.safe_place(ex2_title, anchor=title, direction=DOWN, buff=0.4)
        self.ly.safe_place(ex2_formula, anchor=ex2_title, direction=DOWN, buff=0.3)
        self.ly.safe_place(ex2_prop, anchor=ex2_formula, direction=DOWN, buff=0.3)
        self.play(FadeIn(ex2_title, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(ex2_formula), Write(ex2_prop), run_time=NORMAL)
        self.wait(0.3)

        # Transition: remove ex2, show ex3
        self.play(
            FadeOut(ex2_title), FadeOut(ex2_formula), FadeOut(ex2_prop),
            run_time=FAST,
        )
        self.wait(0.2)

        # Example 3: Logarithm
        ex3_title = Text(
            "3. Logarithm",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS, weight=BOLD,
        )
        ex3_formula = MathTex(
            r"\log : (\mathbb{R}^+, \times) \to (\mathbb{R}, +)",
            color=WHITE, font_size=26,
        )
        ex3_prop = MathTex(
            r"\log(ab) = \log(a) + \log(b)",
            color=SECONDARY, font_size=26,
        )
        self.ly.safe_place(ex3_title, anchor=title, direction=DOWN, buff=0.4)
        self.ly.safe_place(ex3_formula, anchor=ex3_title, direction=DOWN, buff=0.3)
        self.ly.safe_place(ex3_prop, anchor=ex3_formula, direction=DOWN, buff=0.3)
        self.play(FadeIn(ex3_title, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(ex3_formula), Write(ex3_prop), run_time=NORMAL)
        self.wait(0.3)

        self.ly.clear()

    # --- Scene 4: Properties of Homomorphisms ---

    def scene4_properties(self):
        self.add_subcaption(
            "Homomorphisms automatically preserve the key structures of a group. "
            "First, the identity maps to the identity. "
            "Phi of e in G equals e in H. "
            "Proof: phi of e equals phi of e times e, "
            "which equals phi of e times phi of e. "
            "Cancel to get e H. "
            "Second, inverses map to inverses. "
            "Phi of g inverse equals phi of g inverse. "
            "Proof: e H equals phi of g times g inverse, "
            "which equals phi of g times phi of g inverse. "
            "Third, powers map to powers. "
            "Phi of g to the n equals phi of g to the n.",
            duration=35,
        )
        self.ly.section_divider(3, "Properties")

        title = self.ly.title("What Homomorphisms Preserve")

        # Property 1: Identity
        prop1_title = Text(
            "1. Identity maps to identity",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        prop1_formula = MathTex(
            r"\varphi(e_G) = e_H",
            color=ACCENT, font_size=30,
        )
        self.ly.safe_place(prop1_title, anchor=title, direction=DOWN, buff=0.5)
        self.ly.safe_place(prop1_formula, anchor=prop1_title, direction=DOWN, buff=0.3)
        self.play(FadeIn(prop1_title, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(prop1_formula), run_time=NORMAL)
        self.wait(0.3)

        # Proof sketch
        proof1 = MathTex(
            r"\varphi(e) = \varphi(e \cdot e) = \varphi(e)\,\varphi(e) \implies e_H = \varphi(e)",
            color=DIM, font_size=22,
        )
        self.ly.safe_place(proof1, anchor=prop1_formula, direction=DOWN, buff=0.3)
        self.play(Write(proof1), run_time=NORMAL)
        self.wait(0.5)

        self.ly.clear()

        # Property 2: Inverses
        title2 = self.ly.title("Property 2: Inverses Map to Inverses")

        prop2_title = Text(
            "2. Inverses map to inverses",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        prop2_formula = MathTex(
            r"\varphi(g^{-1}) = \varphi(g)^{-1}",
            color=ACCENT, font_size=30,
        )
        self.ly.safe_place(prop2_title, anchor=title2, direction=DOWN, buff=0.5)
        self.ly.safe_place(prop2_formula, anchor=prop2_title, direction=DOWN, buff=0.3)
        self.play(FadeIn(prop2_title, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(prop2_formula), run_time=NORMAL)
        self.wait(0.3)

        # Proof sketch
        proof2 = MathTex(
            r"e_H = \varphi(e) = \varphi(g \cdot g^{-1}) = \varphi(g)\,\varphi(g^{-1})",
            color=DIM, font_size=22,
        )
        self.ly.safe_place(proof2, anchor=prop2_formula, direction=DOWN, buff=0.3)
        self.play(Write(proof2), run_time=NORMAL)
        self.wait(0.5)

        self.ly.clear()

        # Property 3: Powers
        title3 = self.ly.title("Property 3: Powers Map to Powers")

        prop3_formula = MathTex(
            r"\varphi(g^n) = \varphi(g)^n \quad \text{for all } n \in \mathbb{Z}",
            color=ACCENT, font_size=28,
        )
        boxed_prop3 = self.ly.formula_box(prop3_formula, color=ACCENT)

        note3 = Text(
            "Proof: by induction from φ(g·g) = φ(g)φ(g)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(boxed_prop3, anchor=title3, direction=DOWN, buff=0.5)
        self.ly.safe_place(note3, anchor=boxed_prop3, direction=DOWN, buff=0.3)
        self.play(Write(prop3_formula), Create(boxed_prop3[1]), run_time=NORMAL)
        self.play(FadeIn(note3, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 5: Kernel ---

    def scene5_kernel(self):
        self.add_subcaption(
            "The kernel of a homomorphism phi "
            "is the set of all elements in G "
            "that map to the identity in H. "
            "These are the elements that get collapsed "
            "to a single point. "
            "For the determinant, "
            "the kernel is S L of n R, "
            "the matrices with determinant one. "
            "For the sign map, "
            "the kernel is A n, the alternating group. "
            "A fundamental theorem: "
            "the kernel is always a subgroup of the domain. "
            "Even stronger, as we will see, "
            "the kernel is always a NORMAL subgroup.",
            duration=32,
        )
        self.ly.section_divider(4, "The Kernel")

        title = self.ly.title("Definition of the Kernel")

        # Main definition
        def_kernel = MathTex(
            r"\ker(\varphi) = \{g \in G : \varphi(g) = e_H\}",
            color=ACCENT, font_size=32,
        )
        boxed_kernel = self.ly.formula_box(def_kernel, color=ACCENT)

        meaning = Text(
            "All elements of G that map to the identity in H",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(boxed_kernel, anchor=title, direction=DOWN, buff=0.5)
        self.ly.safe_place(meaning, anchor=boxed_kernel, direction=DOWN, buff=0.4)
        self.play(Write(def_kernel), Create(boxed_kernel[1]), run_time=NORMAL)
        self.play(FadeIn(meaning, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        self.ly.clear()

        # Examples of kernels
        title2 = self.ly.title("Kernel Examples")

        ex1 = MathTex(
            r"\ker(\det) = SL(n, \mathbb{R})",
            color=PRIMARY, font_size=26,
        )
        ex1_note = Text(
            "Special linear group (det = 1)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(ex1, anchor=title2, direction=DOWN, buff=0.5)
        self.ly.safe_place(ex1_note, anchor=ex1, direction=DOWN, buff=0.2)
        self.play(Write(ex1), FadeIn(ex1_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        # Remove ex1 before ex2 (content budget)
        self.play(FadeOut(ex1), FadeOut(ex1_note), run_time=FAST)
        self.wait(0.2)

        ex2 = MathTex(
            r"\ker(\operatorname{sgn}) = A_n",
            color=PRIMARY, font_size=26,
        )
        ex2_note = Text(
            "Alternating group (even permutations)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(ex2, anchor=title2, direction=DOWN, buff=0.5)
        self.ly.safe_place(ex2_note, anchor=ex2, direction=DOWN, buff=0.2)
        self.play(Write(ex2), FadeIn(ex2_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(0.3)

        self.ly.clear()

        # Theorem: kernel is a subgroup
        title3 = self.ly.title("Theorem: Kernel is a Subgroup")

        theorem = Text(
            "ker(φ) is a subgroup of G",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        # Proof items
        proof_items = [
            MathTex(r"\varphi(e) = e_H \implies e \in \ker(\varphi)", color=WHITE, font_size=22),
            MathTex(r"a, b \in \ker \implies \varphi(ab) = e \cdot e = e", color=WHITE, font_size=22),
            MathTex(r"a \in \ker \implies \varphi(a^{-1}) = e", color=WHITE, font_size=22),
        ]
        self.ly.safe_place(theorem, anchor=title3, direction=DOWN, buff=0.5)
        self.play(FadeIn(theorem, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.2)

        self.ly.progressive_reveal(proof_items, start_from=theorem, run_time=0.7)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 6: Image ---

    def scene6_image(self):
        self.add_subcaption(
            "While the kernel lives in the domain, "
            "the image lives in the codomain. "
            "The image of phi is the set of all elements "
            "in H that get hit by phi. "
            "For the determinant, "
            "the image is all of R star, "
            "every non-zero real number is a determinant. "
            "For the sign map, "
            "the image is just plus one and minus one. "
            "The image is always a subgroup of H. "
            "A homomorphism is surjective "
            "precisely when the image equals H.",
            duration=30,
        )
        self.ly.section_divider(5, "The Image")

        title = self.ly.title("Definition of the Image")

        # Main definition
        def_image = MathTex(
            r"\operatorname{im}(\varphi) = \{\varphi(g) : g \in G\} \subseteq H",
            color=ACCENT, font_size=30,
        )
        boxed_image = self.ly.formula_box(def_image, color=ACCENT)

        meaning = Text(
            "All elements of H that get 'hit' by the map",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(boxed_image, anchor=title, direction=DOWN, buff=0.5)
        self.ly.safe_place(meaning, anchor=boxed_image, direction=DOWN, buff=0.4)
        self.play(Write(def_image), Create(boxed_image[1]), run_time=NORMAL)
        self.play(FadeIn(meaning, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        self.ly.clear()

        # Two-column: kernel vs image
        title2 = self.ly.title("Kernel vs Image")

        left_items = [
            Text("Kernel", font_size=HEADING_SIZE, color=PRIMARY, font=SANS, weight=BOLD),
            Text("Lives in G (domain)", font_size=LABEL_SIZE, color=DIM, font=SANS),
            MathTex(r"\ker(\varphi) \leq G", color=WHITE, font_size=26),
            Text("Always NORMAL in G", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        right_items = [
            Text("Image", font_size=HEADING_SIZE, color=RED, font=SANS, weight=BOLD),
            Text("Lives in H (codomain)", font_size=LABEL_SIZE, color=DIM, font=SANS),
            MathTex(r"\operatorname{im}(\varphi) \leq H", color=WHITE, font_size=26),
            Text("Subgroup (not necessarily normal)", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]

        cols = self.ly.two_columns(left_items, right_items, start_from=title2)
        # Stagger reveal: left then right
        self.play(FadeIn(cols[0]), run_time=NORMAL)
        self.play(FadeIn(cols[1]), run_time=NORMAL)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 7: Kernel is Normal ---

    def scene7_kernel_normal(self):
        self.add_subcaption(
            "Here is the deep result that connects homomorphisms "
            "to normal subgroups. "
            "The kernel of any homomorphism "
            "is always a normal subgroup. "
            "To prove this, take k in the kernel "
            "and any element g in G. "
            "We need to show that g k g inverse "
            "is also in the kernel. "
            "Apply phi: "
            "phi of g k g inverse equals "
            "phi of g times phi of k times phi of g inverse. "
            "Since k is in the kernel, phi of k is the identity. "
            "So we get phi of g times e times phi of g inverse, "
            "which equals e H. "
            "Therefore g k g inverse is in the kernel. "
            "In fact, every normal subgroup arises as a kernel.",
            duration=38,
        )
        self.ly.section_divider(6, "Why the Kernel is Special")

        title = self.ly.title("Theorem: Kernel is Always Normal")

        # Statement
        theorem = MathTex(
            r"\ker(\varphi) \triangleleft G",
            color=ACCENT, font_size=34,
        )
        boxed_theorem = self.ly.formula_box(theorem, color=ACCENT)

        self.ly.safe_place(boxed_theorem, anchor=title, direction=DOWN, buff=0.5)
        self.play(Write(theorem), Create(boxed_theorem[1]), run_time=NORMAL)
        self.wait(0.3)

        self.ly.clear()

        # Proof
        title2 = self.ly.title("Proof")

        setup = Text(
            "Take k ∈ ker(φ) and any g ∈ G. Show gkg⁻¹ ∈ ker(φ).",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(setup, anchor=title2, direction=DOWN, buff=0.5)
        self.play(FadeIn(setup, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.3)

        # Step 1
        step1 = MathTex(
            r"\varphi(gkg^{-1}) = \varphi(g)\,\varphi(k)\,\varphi(g^{-1})",
            color=PRIMARY, font_size=26,
        )
        self.ly.safe_place(step1, anchor=setup, direction=DOWN, buff=0.4)
        self.play(Write(step1), run_time=NORMAL)
        self.wait(0.3)

        # Remove setup before step 2 (content budget)
        self.play(FadeOut(setup), run_time=FAST)
        self.wait(0.2)

        # Step 2
        step2 = MathTex(
            r"= \varphi(g) \cdot e_H \cdot \varphi(g)^{-1} = e_H",
            color=SECONDARY, font_size=26,
        )
        self.ly.safe_place(step2, anchor=step1, direction=DOWN, buff=0.4)
        self.play(Write(step2), run_time=NORMAL)
        self.wait(0.3)

        # Conclusion
        conclusion = Text(
            "Since φ(gkg⁻¹) = e_H, we have gkg⁻¹ ∈ ker(φ). QED",
            font_size=BODY_SIZE, color=ACCENT, font=SANS, weight=BOLD,
        )
        # Remove step1 for budget
        self.play(FadeOut(step1), run_time=FAST)
        self.ly.safe_place(conclusion, anchor=step2, direction=DOWN, buff=0.4)
        self.play(FadeIn(conclusion, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

        # Key insight
        title3 = self.ly.title("The Deep Connection")

        insight = Text(
            "Every normal subgroup is the kernel of some homomorphism",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS, weight=BOLD,
        )
        insight2 = Text(
            "(Specifically, the quotient map π: G → G/H has ker(π) = H)",
            font_size=LABEL_SIZE, color=DIM, font=SANS,
        )
        boxed_insight = self.ly.formula_box(
            MathTex(r"\pi : G \to G/H, \quad \ker(\pi) = H", color=PRIMARY, font_size=26),
            color=PRIMARY,
        )

        self.ly.safe_place(insight, anchor=title3, direction=DOWN, buff=0.4)
        self.ly.safe_place(boxed_insight, anchor=insight, direction=DOWN, buff=0.3)
        self.ly.safe_place(insight2, anchor=boxed_insight, direction=DOWN, buff=0.2)
        self.play(FadeIn(insight, shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(boxed_insight[0]), Create(boxed_insight[1]), run_time=NORMAL)
        self.play(FadeIn(insight2, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        self.ly.clear()

    # --- Scene 8: Summary + Teaser ---

    def scene8_summary(self):
        self.add_subcaption(
            "Let's recap what we've learned about homomorphisms. "
            "A homomorphism preserves the group operation: "
            "phi of a b equals phi of a times phi of b. "
            "Identity, inverses, and powers are all automatically preserved. "
            "The kernel is the set of elements mapping to the identity, "
            "and it's always a normal subgroup of the domain. "
            "The image is the set of elements that get hit, "
            "and it's always a subgroup of the codomain. "
            "Normal subgroups and homomorphisms "
            "are truly two sides of the same coin. "
            "Next time, the Isomorphism Theorems.",
            duration=30,
        )

        title = self.ly.title("Key Takeaways")

        takeaways = [
            Text("1. φ(ab) = φ(a)φ(b) preserves the operation", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("2. Identity, inverses, powers are preserved", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("3. ker(φ) is always a NORMAL subgroup of G", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("4. im(φ) is always a subgroup of H", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("5. Normal subgroups and kernels are two sides of one coin", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(takeaways, start_from=title, run_time=0.6)
        self.wait(0.3)

        self.ly.clear()

        # Closing
        closing = Text(
            "Next: The Isomorphism Theorems",
            font_size=HEADING_SIZE, color=WHITE, font=SANS, weight=BOLD,
        )
        teaser = Text(
            "Including: G/ker(φ) ≅ im(φ)",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.center_in_content(closing)
        self.ly.safe_place(teaser, anchor=closing, direction=DOWN, buff=0.3)
        self.play(FadeIn(closing, scale=1.05), run_time=NORMAL)
        self.play(FadeIn(teaser, shift=LEFT * 0.15), run_time=FAST)
        self.wait(0.5)

        play_outro(self, "Group Homomorphisms", "Abstract Algebra I")
